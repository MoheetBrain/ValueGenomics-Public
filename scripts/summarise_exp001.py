"""Render Experiment 001 results (results/exp001/summary.json) as Markdown tables.

    python3 scripts/summarise_exp001.py > /tmp/exp001_tables.md

Reporting only: it reads the outputs written by experiments/exp001_circularity/run.py and makes
no decisions of its own (the verdict is computed by run.py under the preregistered rule).
"""
from __future__ import annotations

import json
from pathlib import Path

S = json.loads((Path(__file__).resolve().parents[1] / "results/exp001/summary.json").read_text())


def pct(c: dict, key: str = "mean") -> str:
    return f"{100 * c[key]:.2f}" if c.get("n") else "n/a"


def cell(c: dict) -> str:
    return f"{pct(c)} [{pct(c, 'ci95_low')}, {pct(c, 'ci95_high')}]" if c.get("n") else "n/a"


def main() -> None:
    e1 = S["E1_reference"]
    print("### E1 — reference economy, optimal set-off (φ_book, % of participants' book; mean [95 % CI], n=30)\n")
    print("| strategy | " + " | ".join(f"p={p}" for p in (0.05, 0.1, 0.2, 0.3, 0.5)) + " |")
    print("|---|" + "---|" * 5)
    for s in ("random", "sme_random", "anchor"):
        print(f"| {s} | " + " | ".join(cell(e1[f"{s}@{p}"]["phi_book_mtcs"]) for p in (0.05, 0.1, 0.2, 0.3, 0.5)) + " |")
    a = e1["all@1.0"]
    print(f"| **all (p=1)** | {cell(a['phi_book_mtcs'])} | | | | |\n")

    print("### E1 — algorithms at full participation and anchor p=0.2 (% of book; internal % for bound)\n")
    print("| setting | bilateral | greedy 3-cycle | optimal MTCS | MTCS, % of internal obligations | netting bound, % of internal |")
    print("|---|---|---|---|---|---|")
    for key in ("all@1.0", "anchor@0.2", "random@0.2"):
        c = e1[key]
        print(f"| {key} | {cell(c['phi_book_bilateral'])} | {cell(c['phi_book_greedy3'])} | {cell(c['phi_book_mtcs'])} | "
              f"{cell(c['phi_int_mtcs'])} | {cell(c['phi_int_netting_bound'])} |")
    print()

    print("### Reference network statistics (full participation)\n")
    for k in ("reciprocity", "scc_node_share", "scc_weight_share", "mean_out_degree", "spend_coverage"):
        c = a[k]
        scale = 100 if k != "mean_out_degree" else 1
        unit = "%" if scale == 100 else ""
        print(f"- {k}: {c['mean'] * scale:.2f}{unit} (min {c['min'] * scale:.2f}, max {c['max'] * scale:.2f})")
    print()

    print("### Distribution (exploratory)\n")
    for key in ("all@1.0", "anchor@0.2"):
        c = e1[key]
        print(f"- {key}: small firms' share of cleared value {pct(c['sme_share_of_cleared'])} % vs their share of "
              f"participants' receivables {pct(c['sme_share_of_participant_recv'])} %; median share of receivables cleared — "
              f"small {pct(c['median_recv_share_sme'])} %, large {pct(c['median_recv_share_large'])} %")
    print()

    print("### E2 — sensitivity (φ_book optimal MTCS, %; mean [95 % CI])\n")
    print("| variant | all (p=1) | anchor p=0.2 | random p=0.2 |")
    print("|---|---|---|---|")
    for v, d in S["E2_sensitivity_phi_book_mtcs"].items():
        print(f"| {v} | {cell(d['all@1.0'])} | {cell(d['anchor@0.2'])} | {cell(d['random@0.2'])} |")
    print()

    print(f"### E3 — sector-level network: φ = {100 * S['E3_sector_level_phi']:.2f} %\n")

    print("### E4 — default shock (exploratory; means over 30 seeds)\n")
    for key, d in S["E4_default_shock_exploratory"].items():
        print(f"- **{key}**: defaults before {d['defaults_before']['mean']:.1f} / after {d['defaults_after']['mean']:.1f}; "
              f"total loss before {d['loss_total_before']['mean']:.3f} / after {d['loss_total_after']['mean']:.3f}; "
              f"participant losses before {d['loss_participants_before']['mean']:.3f} / after {d['loss_participants_after']['mean']:.3f}; "
              f"transfer to participants per £ cleared {d['transfer_per_cleared']['mean']:.4f} "
              f"[{d['transfer_per_cleared']['ci95_low']:.4f}, {d['transfer_per_cleared']['ci95_high']:.4f}]; "
              f"with distress screen {d['transfer_per_cleared_excluding_flagged']['mean']:.4f}; "
              f"cleared kept with screen {100 * d['cleared_excluding_flagged']['mean'] / d['cleared']['mean']:.1f} %; "
              f"screen recall {100 * d['flagged_recall']['mean']:.1f} %")
    print()

    dec = S["decision"]
    print("### Decision\n")
    print(f"- verdict: **{dec['verdict']}**")
    print(f"- H1 anchor p=0.2: {cell(dec['H1_ref_anchor_p0.2_phi_book_mtcs'])}; all: {cell(dec['H1_ref_all_phi_book_mtcs'])}")
    print(f"- share of sensitivity variants with all-participation mean ≥ 10 %: {100 * dec['robust_share_all_ge_10pct']:.0f} % "
          f"(anchor p=0.2: {100 * dec['robust_share_anchor_ge_10pct']:.0f} %)")
    print(f"- V1 reciprocity {100 * dec['V1_reference_reciprocity']:.2f} % → passed: {dec['V1_passed']}")
    print(f"- H2 sector/firm ratio {dec['H2_sector_over_firm_ratio']:.2f} → supported: {dec['H2_supported']}")
    print(f"- H3 anchor/random ratio {dec['H3_anchor_over_random_ratio_p0.2']:.2f} → supported: {dec['H3_supported']}")
    h4 = dec["H4_topology_predictor"]
    print(f"- H4 LOVO R² {h4['r2_out_of_sample']:.3f} over {h4['n_runs']} runs / {h4['n_variants']} variants → supported: "
          f"{dec['H4_supported']}; full-fit coefficients {json.dumps({k: round(v, 3) for k, v in h4['coefficients_full_fit'].items()})}")
    print(f"- all checks ok: {S['all_checks_ok']}; runtime {S['runtime_seconds'] / 60:.1f} min; git HEAD at run {S['git_head_at_run'][:7]}; "
          f"python {S['environment']['python']}, numpy {S['environment']['numpy']}, scipy {S['environment']['scipy']}")


if __name__ == "__main__":
    main()
