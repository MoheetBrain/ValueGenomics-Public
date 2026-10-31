"""Run Experiment 001 — the circularity of UK-calibrated trade-credit networks.

    .venv/bin/python -m experiments.exp001_circularity.run            # full preregistered run
    .venv/bin/python -m experiments.exp001_circularity.run --smoke    # 2 seeds, timing only

Outputs (results/exp001/): runs.csv (one row per economy x participation setting),
defaults.csv (exploratory default shocks), summary.json (aggregates with 95% CIs, the
preregistered decision, environment and timing). See experiments/experiment-001-spec.md.
"""
from __future__ import annotations

import argparse
import csv
import json
import platform
import subprocess
import time
from dataclasses import asdict
from pathlib import Path

import numpy as np
import scipy
import scipy.sparse as sp
from scipy.sparse.csgraph import connected_components

from .clearing import (
    Network,
    bilateral_netting,
    is_circulation,
    max_circulation,
    netting_bound,
    residual_is_acyclic,
    short_cycle_greedy,
)
from .defaults import loss_split, shock_scenario
from .network import Economy, EconomyParams, generate, sector_network, select_participants

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "results/exp001"
BASE_SEED = 20261017
N_SEEDS = 30
REFERENCE = EconomyParams()
P_GRID = (0.05, 0.10, 0.20, 0.30, 0.50)
STRATEGIES = ("random", "sme_random", "anchor")
SENSITIVITY: dict[str, tuple] = {
    "supplier_median": (3.0, 5.0, 20.0, 40.0),
    "n_firms": (500, 8000),
    "attachment_beta": (0.0, 0.5),
    "pareto_alpha": (1.5, 2.0),
    "supplier_size_elasticity": (0.0, 0.7),
    "supplier_sigma": (0.4, 1.2),
    "firms_by": ("sqrt_output",),
    "structure": ("configuration",),
    "payment_days": ((45.0, 45.0), (30.0, 90.0)),
}
SENS_SETTINGS = (("all", 1.0), ("anchor", 0.2), ("random", 0.2))
THRESH_MATERIAL = 0.10
THRESH_KILL = 0.03
RECIPROCITY_BAND = (0.01, 0.15)  # validation gate V1: real firm networks show ~2-9% (Bacilieri et al. 2026)
H4_R2 = 0.7


def topology(net: Network) -> dict:
    """Cheap whole-network statistics used to predict clearability (hypothesis H4)."""
    pairs = set(zip(net.src.tolist(), net.dst.tolist()))
    recip = float(np.mean([(d, s) in pairs for s, d in pairs]))
    adj = sp.csr_matrix((np.ones(net.m), (net.src, net.dst)), shape=(net.n, net.n))
    _, labels = connected_components(adj, directed=True, connection="strong")
    sizes = np.bincount(labels)
    big = int(np.argmax(sizes))
    in_scc = (labels[net.src] == big) & (labels[net.dst] == big)
    return {"reciprocity": recip, "scc_node_share": float(sizes[big] / net.n),
            "scc_weight_share": float(net.amt[in_scc].sum() / net.amt.sum()), "mean_out_degree": float(net.m / net.n)}


def logit(x: np.ndarray) -> np.ndarray:
    x = np.clip(x, 1e-6, 1 - 1e-6)
    return np.log(x / (1 - x))


def lovo_r2(rows: list[dict]) -> dict:
    """Leave-one-variant-out prediction of phi (full participation) from topology statistics."""
    y = np.array([r["phi_book_mtcs"] for r in rows])
    x = np.column_stack([np.ones(len(rows)), logit(np.array([r["reciprocity"] for r in rows])),
                         logit(np.array([r["scc_weight_share"] for r in rows])),
                         np.log(np.array([r["mean_out_degree"] for r in rows]))])
    groups = np.array([r["variant"] for r in rows])
    pred = np.empty(len(rows))
    for g in np.unique(groups):
        test = groups == g
        beta, *_ = np.linalg.lstsq(x[~test], logit(y[~test]), rcond=None)
        pred[test] = 1 / (1 + np.exp(-(x[test] @ beta)))
    beta_all, *_ = np.linalg.lstsq(x, logit(y), rcond=None)
    sse = float(((y - pred) ** 2).sum())
    sst = float(((y - y.mean()) ** 2).sum())
    return {"r2_out_of_sample": 1 - sse / sst if sst > 0 else float("nan"), "n_runs": int(len(rows)),
            "n_variants": int(len(np.unique(groups))),
            "coefficients_full_fit": dict(zip(["const", "logit_reciprocity", "logit_scc_weight_share", "log_mean_out_degree"],
                                              beta_all.tolist()))}


def evaluate(econ: Economy, members: np.ndarray) -> dict:
    net = econ.net
    sub, _ = net.subnetwork(members)
    inside = np.zeros(net.n, dtype=bool)
    inside[members] = True
    recv = np.zeros(net.n)
    np.add.at(recv, net.dst, net.amt)
    pay = np.zeros(net.n)
    np.add.at(pay, net.src, net.amt)
    book = 0.5 * (recv[inside].sum() + pay[inside].sum())
    g_int = float(sub.amt.sum())

    c_bi = bilateral_netting(sub)
    c_gr = short_cycle_greedy(sub)
    c_mx = max_circulation(sub)
    ok = is_circulation(sub, c_mx) and is_circulation(sub, c_gr) and residual_is_acyclic(sub, c_mx)

    cleared_recv = np.zeros(net.n)
    np.add.at(cleared_recv, sub.dst, c_mx)
    large = econ.size_quantile >= 0.99
    has_recv = inside & (recv > 0)
    share = np.divide(cleared_recv, recv, out=np.zeros(net.n), where=recv > 0)
    sme_mask, large_mask = has_recv & ~large, has_recv & large
    return {
        "participants": int(inside.sum()),
        "internal_edges": int(sub.m),
        "book": float(book),
        "internal_gross": g_int,
        "phi_book_bilateral": float(c_bi.sum() / book) if book else 0.0,
        "phi_book_greedy3": float(c_gr.sum() / book) if book else 0.0,
        "phi_book_mtcs": float(c_mx.sum() / book) if book else 0.0,
        "phi_int_mtcs": float(c_mx.sum() / g_int) if g_int else 0.0,
        "phi_int_netting_bound": float(netting_bound(sub) / g_int) if g_int else 0.0,
        "phi_economy_mtcs": float(c_mx.sum() / net.amt.sum()),
        "median_recv_share_sme": float(np.median(share[sme_mask])) if sme_mask.any() else float("nan"),
        "median_recv_share_large": float(np.median(share[large_mask])) if large_mask.any() else float("nan"),
        "sme_share_of_cleared": float(cleared_recv[sme_mask].sum() / c_mx.sum()) if c_mx.sum() else float("nan"),
        "sme_share_of_participant_recv": float(recv[sme_mask].sum() / recv[has_recv].sum()) if has_recv.any() else float("nan"),
        "checks_ok": bool(ok),
    }


def default_shock(econ: Economy, members: np.ndarray, rng: np.random.Generator) -> dict:
    net = econ.net
    outside, assets, shocked = shock_scenario(net, econ.size, rng)
    inside = np.zeros(net.n, dtype=bool)
    inside[members] = True
    before = loss_split(net, net.amt, outside, assets, inside)

    def clear_among(group: np.ndarray) -> np.ndarray:
        sub, idx = net.subnetwork(group)
        c = np.zeros(net.m)
        c[idx] = max_circulation(sub)
        return c

    c_all = clear_among(members)
    after = loss_split(net, net.amt - c_all, outside, assets, inside)
    # Distress-aware variant: an imperfect risk signal flags 2x as many participants as are
    # actually shocked; flagged firms are left out of the clearing round.
    signal = np.isin(np.arange(net.n), shocked).astype(float) + rng.normal(0, 0.75, net.n)
    cand = members[np.argsort(-signal[members])]
    flagged = cand[: min(len(cand), 2 * len(shocked))]
    c_ex = clear_among(np.setdiff1d(members, flagged))
    excl = loss_split(net, net.amt - c_ex, outside, assets, inside)

    def transfer(x) -> float:
        return (x.other_firms + x.outside_creditors) - (before.other_firms + before.outside_creditors)

    return {
        "cleared": float(c_all.sum()),
        "cleared_excluding_flagged": float(c_ex.sum()),
        "defaults_before": before.defaults,
        "defaults_after": after.defaults,
        "loss_total_before": before.total,
        "loss_total_after": after.total,
        "loss_participants_before": before.participant_firms,
        "loss_participants_after": after.participant_firms,
        "transfer_to_participants": transfer(after),
        "transfer_to_participants_excluding_flagged": transfer(excl),
        "transfer_per_cleared": transfer(after) / c_all.sum() if c_all.sum() else float("nan"),
        "transfer_per_cleared_excluding_flagged": transfer(excl) / c_ex.sum() if c_ex.sum() else float("nan"),
        "flagged_recall": float(np.isin(shocked[np.isin(shocked, members)], flagged).mean()) if np.isin(shocked, members).any() else float("nan"),
    }


def variant_params(key: str, value) -> EconomyParams:
    if key == "payment_days":
        return REFERENCE.with_(payment_days_small=value[0], payment_days_large=value[1])
    return REFERENCE.with_(**{key: value})


def ci(values: list[float]) -> dict:
    a = np.array([v for v in values if v == v], dtype=float)
    if len(a) == 0:
        return {"n": 0}
    sd = float(a.std(ddof=1)) if len(a) > 1 else 0.0
    half = 1.96 * sd / np.sqrt(len(a)) if len(a) > 1 else 0.0
    return {"n": int(len(a)), "mean": float(a.mean()), "sd": sd, "ci95_low": float(a.mean() - half),
            "ci95_high": float(a.mean() + half), "min": float(a.min()), "max": float(a.max())}


def git_head() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true", help="2 seeds, timing only, writes nothing")
    args = ap.parse_args()
    n_seeds = 2 if args.smoke else N_SEEDS
    t0 = time.time()
    rows: list[dict] = []
    drows: list[dict] = []

    def record(block: str, variant: str, params: EconomyParams, seed: int, econ: Economy, strategy: str, p: float, prng):
        members = select_participants(econ, strategy, p, prng)
        t = time.time()
        r = evaluate(econ, members)
        topo = topology(econ.net) if strategy == "all" else dict.fromkeys(
            ("reciprocity", "scc_node_share", "scc_weight_share", "mean_out_degree"), float("nan"))
        rows.append({"block": block, "variant": variant, "seed": seed, "strategy": strategy, "p": p,
                     "edges": econ.net.m, "spend_coverage": econ.spend_coverage, "seconds": time.time() - t, **r, **topo})

    # Block E1: reference economy, participation grid.
    for r in range(n_seeds):
        seed = BASE_SEED + r
        econ = generate(REFERENCE, seed)
        prng = np.random.default_rng(seed + 500_000)
        record("E1", "reference", REFERENCE, seed, econ, "all", 1.0, prng)
        for strategy in STRATEGIES:
            for p in P_GRID:
                record("E1", "reference", REFERENCE, seed, econ, strategy, p, prng)
        # Block E4 (exploratory): default shocks at two participation settings.
        for strategy, p in (("anchor", 0.2), ("all", 1.0)):
            drng = np.random.default_rng(seed + 900_000)
            members = select_participants(econ, strategy, p, drng)
            drows.append({"seed": seed, "strategy": strategy, "p": p, **default_shock(econ, members, drng)})
        if args.smoke:
            print(f"E1 seed {r}: {econ.net.m} edges, elapsed {time.time() - t0:.1f}s")

    # Block E2: one-factor-at-a-time sensitivity.
    for k, (key, values) in enumerate(SENSITIVITY.items()):
        for v_i, value in enumerate(values):
            params = variant_params(key, value)
            variant = f"{key}={value}"
            for r in range(n_seeds):
                seed = BASE_SEED + 10_000 * (k + 1) + 100 * v_i + r
                econ = generate(params, seed)
                prng = np.random.default_rng(seed + 500_000)
                for strategy, p in SENS_SETTINGS:
                    record("E2", variant, params, seed, econ, strategy, p, prng)
            if args.smoke:
                print(f"E2 {variant}: elapsed {time.time() - t0:.1f}s")

    # Block E3: aggregation — the same clearing on the sector-level network.
    sn = sector_network()
    c_sn = max_circulation(sn)
    sector_phi = float(c_sn.sum() / sn.amt.sum())

    if args.smoke:
        print(f"smoke run finished in {time.time() - t0:.1f}s; nothing written")
        return

    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "runs.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    with (OUT / "defaults.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(drows[0]))
        w.writeheader()
        w.writerows(drows)

    def sel(block, variant, strategy, p):
        return [x for x in rows if x["block"] == block and x["variant"] == variant and x["strategy"] == strategy and abs(x["p"] - p) < 1e-12]

    metrics = ("phi_book_mtcs", "phi_book_greedy3", "phi_book_bilateral", "phi_int_mtcs", "phi_int_netting_bound",
               "phi_economy_mtcs", "median_recv_share_sme", "median_recv_share_large", "sme_share_of_cleared",
               "sme_share_of_participant_recv", "reciprocity", "scc_node_share", "scc_weight_share",
               "mean_out_degree", "spend_coverage")
    e1 = {}
    for strategy, p in [("all", 1.0)] + [(s, q) for s in STRATEGIES for q in P_GRID]:
        e1[f"{strategy}@{p}"] = {m: ci([x[m] for x in sel("E1", "reference", strategy, p)]) for m in metrics}
    e2 = {}
    for key, values in SENSITIVITY.items():
        for value in values:
            variant = f"{key}={value}"
            e2[variant] = {f"{s}@{p}": ci([x["phi_book_mtcs"] for x in sel("E2", variant, s, p)]) for s, p in SENS_SETTINGS}
    e4 = {}
    for strategy, p in (("anchor", 0.2), ("all", 1.0)):
        rs = [x for x in drows if x["strategy"] == strategy]
        e4[f"{strategy}@{p}"] = {m: ci([x[m] for x in rs]) for m in drows[0] if m not in ("seed", "strategy", "p")}

    # Preregistered decision (experiments/experiment-001-spec.md, section 9).
    ref_anchor = e1["anchor@0.2"]["phi_book_mtcs"]
    ref_all = e1["all@1.0"]["phi_book_mtcs"]
    sens_all = [v["all@1.0"]["mean"] for v in e2.values()]
    sens_anchor = [v["anchor@0.2"]["mean"] for v in e2.values()]
    robust_share_all = float(np.mean([s >= THRESH_MATERIAL for s in sens_all]))
    robust_share_anchor = float(np.mean([s >= THRESH_MATERIAL for s in sens_anchor]))
    recip = e1["all@1.0"]["reciprocity"]["mean"]
    v1_ok = RECIPROCITY_BAND[0] <= recip <= RECIPROCITY_BAND[1]
    if ref_all["ci95_high"] < THRESH_KILL:
        verdict = "KILL"
    elif ref_anchor["ci95_low"] >= THRESH_MATERIAL and ref_all["ci95_low"] >= THRESH_MATERIAL and robust_share_all >= 0.7:
        verdict = "CONTINUE" if v1_ok else "REDESIGN (CONTINUE criteria met but generator failed validation gate V1)"
    else:
        verdict = "REDESIGN"
    h4 = lovo_r2([x for x in rows if x["strategy"] == "all"])
    h2_ratio = sector_phi / ref_all["mean"] if ref_all["mean"] else float("inf")
    h3_ratio = ref_anchor["mean"] / e1["random@0.2"]["phi_book_mtcs"]["mean"] if e1["random@0.2"]["phi_book_mtcs"]["mean"] else float("inf")

    summary = {
        "experiment": "001 circularity of UK-calibrated trade-credit networks",
        "git_head_at_run": git_head(),
        "environment": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__,
                        "platform": platform.platform()},
        "runtime_seconds": time.time() - t0,
        "n_seeds": n_seeds,
        "base_seed": BASE_SEED,
        "reference_params": asdict(REFERENCE),
        "all_checks_ok": all(x["checks_ok"] for x in rows),
        "E1_reference": e1,
        "E2_sensitivity_phi_book_mtcs": e2,
        "E3_sector_level_phi": sector_phi,
        "E4_default_shock_exploratory": e4,
        "decision": {
            "verdict": verdict,
            "H1_ref_anchor_p0.2_phi_book_mtcs": ref_anchor,
            "H1_ref_all_phi_book_mtcs": ref_all,
            "robust_share_all_ge_10pct": robust_share_all,
            "robust_share_anchor_ge_10pct": robust_share_anchor,
            "H2_sector_over_firm_ratio": h2_ratio,
            "H2_supported": bool(h2_ratio >= 2.0),
            "H3_anchor_over_random_ratio_p0.2": h3_ratio,
            "H3_supported": bool(h3_ratio >= 2.0),
            "V1_reference_reciprocity": recip,
            "V1_passed": bool(v1_ok),
            "H4_topology_predictor": h4,
            "H4_supported": bool(h4["r2_out_of_sample"] >= H4_R2),
        },
    }
    (OUT / "summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary["decision"], indent=2))
    print(f"runtime {summary['runtime_seconds']:.0f}s; all checks ok: {summary['all_checks_ok']}")


if __name__ == "__main__":
    main()
