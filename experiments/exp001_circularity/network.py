"""Synthetic UK-calibrated firm-level trade-credit networks for Experiment 001.

Construction (all randomness from one numpy Generator, so a seed fixes the economy):
 1. Sectors are the CPA products of the ONS 2023 domestic input-output table (103 after
    dropping imputed owner-occupier rent, see EXCLUDED_PRODUCTS). Domestic
    technical coefficients a[s, t] = Z[s, t] / X[t] give the GBP of product s bought per GBP of
    product t produced (imports are excluded: they are paid to firms outside the network).
 2. n_firms firms are allocated to sectors in proportion to sector output (or its square root),
    at least one per sector, by the largest-remainder method.
 3. Firm sizes within a sector are Pareto(alpha) draws rescaled to the sector's output.
 4. Each firm's supplier count is lognormal with a given median, rising with firm size.
 5. A buyer draws its supplier slots across input sectors in proportion to its input
    coefficients; within a sector it picks distinct suppliers with probability proportional to
    size**beta and splits that sector's spend between them by the same weights. Spend on input
    sectors it draws no supplier from is bought outside the modelled network.
 6. The outstanding obligation on each buyer->supplier link is annual spend x payment days / 365,
    with payment days rising linearly in the buyer's size quantile (large firms pay slower).

structure="configuration" keeps every firm, size, supplier count and total spend but rewires
suppliers ignoring sectors: a null model that removes input-output structure.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass, replace
from pathlib import Path

import numpy as np

from .clearing import Network

DATA = Path(__file__).resolve().parents[2] / "data/processed"


@dataclass(frozen=True)
class EconomyParams:
    n_firms: int = 2000
    supplier_median: float = 10.0
    supplier_sigma: float = 0.8
    supplier_size_elasticity: float = 0.35
    pareto_alpha: float = 1.1
    attachment_beta: float = 1.0
    firms_by: str = "output"  # "output" | "sqrt_output"
    payment_days_small: float = 40.0
    payment_days_large: float = 65.0
    structure: str = "io"  # "io" | "configuration"

    def with_(self, **kw) -> "EconomyParams":
        return replace(self, **kw)


@dataclass(frozen=True)
class Economy:
    params: EconomyParams
    sector: np.ndarray  # sector index per firm
    size: np.ndarray  # annual output per firm (GBP m, scaled replica)
    size_quantile: np.ndarray  # in [0, 1]
    net: Network
    spend_coverage: float  # share of domestic intermediate spend placed on modelled links


# Imputed rental of owner-occupied dwellings is a national-accounts imputation, not trade between
# firms; it also carries the table's only negative cell (a FISIM adjustment from CPA_K64).
EXCLUDED_PRODUCTS = ("CPA_L68A",)


def load_io() -> tuple[np.ndarray, np.ndarray, list[str]]:
    """Domestic flows Z[s, t] (GBP m of product s used to make product t) and outputs X[t],
    with EXCLUDED_PRODUCTS removed and any remaining negative cells set to zero."""
    with (DATA / "ons_iot2023_domestic_Z.csv").open() as fh:
        rows = list(csv.reader(fh))
    codes = rows[0][1:]
    z = np.array([[float(v) for v in r[1:]] for r in rows[1:]])
    with (DATA / "ons_iot2023_products.csv").open() as fh:
        prod = list(csv.DictReader(fh))
    x = np.array([float(p["total_output_basic_prices_gbp_m"]) for p in prod])
    if [p["code"] for p in prod] != codes:
        raise ValueError("product files disagree")
    keep = np.array([c not in EXCLUDED_PRODUCTS for c in codes])
    z = np.clip(z[np.ix_(keep, keep)], 0, None)
    return z, x[keep], [c for c, k in zip(codes, keep) if k]


def sector_network(days: float = 45.0, include_intra_sector: bool = False) -> Network:
    """The aggregated sector-level obligation network (buyer sector owes supplier sector)."""
    z, _, _ = load_io()
    s, t = np.nonzero(z)
    keep = s != t
    if include_intra_sector:
        raise ValueError("intra-sector flows are self-loops at sector level; they cannot be represented")
    return Network(z.shape[0], t[keep], s[keep], z[s[keep], t[keep]] * days / 365.0)


def _allocate(weights: np.ndarray, total: int) -> np.ndarray:
    if total < len(weights):
        raise ValueError("need at least one firm per sector")
    counts = np.ones(len(weights), dtype=int)
    share = weights / weights.sum() * (total - len(weights))
    counts += np.floor(share).astype(int)
    remainder = total - counts.sum()
    counts[np.argsort(-(share - np.floor(share)))[:remainder]] += 1
    return counts


def generate(params: EconomyParams, seed: int) -> Economy:
    rng = np.random.default_rng(seed)
    z, x, _ = load_io()
    n_sec = len(x)
    a = z / x[None, :]

    w = x if params.firms_by == "output" else np.sqrt(x)
    counts = _allocate(w, params.n_firms)
    sector = np.repeat(np.arange(n_sec), counts)
    size = np.empty(params.n_firms)
    members: list[np.ndarray] = []
    start = 0
    for t, k in enumerate(counts):
        draw = rng.pareto(params.pareto_alpha, k) + 1.0
        size[start : start + k] = draw / draw.sum() * x[t]
        members.append(np.arange(start, start + k))
        start += k
    quant = (np.argsort(np.argsort(size)) + 0.5) / params.n_firms

    k_sup = params.supplier_median * (size / np.median(size)) ** params.supplier_size_elasticity
    k_sup *= np.exp(params.supplier_sigma * rng.standard_normal(params.n_firms))
    k_sup = np.clip(np.rint(k_sup), 1, params.n_firms - 1).astype(int)

    attach = size**params.attachment_beta
    src, dst, spend = [], [], []
    placed = 0.0
    total = 0.0
    for j in range(params.n_firms):
        t = sector[j]
        coef = a[:, t]
        total += coef.sum() * size[j]
        if coef.sum() <= 0:
            continue
        picks = np.bincount(rng.choice(n_sec, size=k_sup[j], p=coef / coef.sum()), minlength=n_sec)
        for s in np.flatnonzero(picks):
            cand = members[s][members[s] != j]
            if len(cand) == 0:
                continue
            m = min(picks[s], len(cand))
            pw = attach[cand] / attach[cand].sum()
            chosen = rng.choice(cand, size=m, replace=False, p=pw)
            share = attach[chosen] / attach[chosen].sum()
            amount = coef[s] * size[j]
            placed += amount
            src.extend([j] * m)
            dst.extend(chosen.tolist())
            spend.extend((amount * share).tolist())
    src_a = np.array(src)
    dst_a = np.array(dst)
    spend_a = np.array(spend)

    if params.structure == "configuration":
        src_a, dst_a, spend_a = _rewire(rng, params.n_firms, src_a, spend_a, attach)
    elif params.structure != "io":
        raise ValueError(f"unknown structure {params.structure!r}")

    days = params.payment_days_small + (params.payment_days_large - params.payment_days_small) * quant
    amt = spend_a * days[src_a] / 365.0
    net = Network(params.n_firms, src_a, dst_a, amt)
    return Economy(params, sector, size, quant, net, placed / total if total else 0.0)


def _rewire(rng, n, src, spend, attach):
    """Keep each buyer's supplier count and total spend; draw suppliers ignoring sectors."""
    new_src, new_dst, new_spend = [], [], []
    for j in np.unique(src):
        mask = src == j
        k = int(mask.sum())
        budget = float(spend[mask].sum())
        cand = np.delete(np.arange(n), j)
        pw = attach[cand] / attach[cand].sum()
        chosen = rng.choice(cand, size=min(k, len(cand)), replace=False, p=pw)
        share = attach[chosen] / attach[chosen].sum()
        new_src.extend([j] * len(chosen))
        new_dst.extend(chosen.tolist())
        new_spend.extend((budget * share).tolist())
    return np.array(new_src), np.array(new_dst), np.array(new_spend)


def select_participants(econ: Economy, strategy: str, p: float, rng: np.random.Generator) -> np.ndarray:
    """Firms that join the clearing network.

    random       : a uniformly random p-share of all firms.
    sme_random   : a random p-share of all firms drawn only from firms outside the top 1% by size.
    anchor       : breadth-first from the largest firm over trading links (either direction),
                   neighbours visited largest first, until the p-share is reached — the "onboard an
                   anchor buyer and its supply chain" go-to-market.
    all          : every firm (p ignored).
    """
    n = econ.params.n_firms
    k = int(round(p * n))
    if strategy == "all":
        return np.arange(n)
    if strategy == "random":
        return np.sort(rng.choice(n, size=k, replace=False))
    if strategy == "sme_random":
        smes = np.flatnonzero(econ.size_quantile < 0.99)
        return np.sort(rng.choice(smes, size=min(k, len(smes)), replace=False))
    if strategy == "anchor":
        nbrs: dict[int, set[int]] = {}
        for s, d in zip(econ.net.src, econ.net.dst):
            nbrs.setdefault(int(s), set()).add(int(d))
            nbrs.setdefault(int(d), set()).add(int(s))
        order = np.argsort(-econ.size)
        chosen: list[int] = []
        seen = np.zeros(n, dtype=bool)
        for root in order:  # restart from the next-largest firm if a component is exhausted
            if len(chosen) >= k:
                break
            if seen[root]:
                continue
            frontier = [int(root)]
            seen[root] = True
            while frontier and len(chosen) < k:
                chosen.extend(frontier[: k - len(chosen)])
                nxt = {w for v in frontier for w in nbrs.get(v, ()) if not seen[w]}
                frontier = sorted(nxt, key=lambda v: -econ.size[v])
                seen[frontier] = True
        return np.sort(np.array(chosen[:k]))
    raise ValueError(f"unknown strategy {strategy!r}")
