"""Pareto analysis of the 12 flagship candidates (research/candidate-comparison.md §3).

Ratings are ordinal judgements (1 = low, 2 = medium, 3 = high; for capital, 3 = needs little capital;
for time-to-revenue, 3 = fast). They are recorded here so the frontier computation is reproducible
and the judgements are open to challenge. No weights are used: step 1 is full-vector Pareto
dominance; step 2 aggregates each objective by median and by mean (both weight-free) and
recomputes the two-objective frontier.

    python3 scripts/pareto_candidates.py
"""
from __future__ import annotations

from statistics import mean, median

SCIENCE = ("novelty", "falsifiability", "tractability", "explanatory", "empirical_validation", "significance")
ECONOMY = ("demand", "legal_operability", "solo_advantage", "time_to_revenue", "distribution", "capital_light", "upside")

R = {
    "C1 compute-denominated money":            (1, 3, 3, 1, 2, 1,  1, 1, 1, 1, 1, 2, 2),
    "C2 open compute exchange rates":          (2, 3, 3, 2, 3, 2,  2, 3, 1, 2, 2, 3, 2),
    "C3 AI allocation/governance engine":      (1, 2, 1, 2, 1, 2,  1, 2, 1, 1, 1, 1, 2),
    "C4 machine-output rights":                (1, 2, 2, 1, 2, 2,  2, 1, 1, 1, 1, 1, 3),
    "C5 future-resource entitlements":         (2, 1, 1, 1, 1, 2,  1, 1, 1, 1, 1, 1, 3),
    "C6 Zero-Net trade-credit clearing (UK)":  (2, 3, 3, 3, 3, 2,  2, 2, 2, 2, 1, 3, 2),
    "C7 agent mutual credit/clearing":         (2, 3, 3, 2, 1, 2,  1, 2, 2, 1, 1, 3, 2),
    "C8 agent mandate + liability layer":      (1, 2, 2, 1, 2, 1,  3, 2, 1, 2, 2, 2, 3),
    "C9 economic failure atlas":               (1, 2, 2, 2, 2, 1,  1, 3, 1, 1, 1, 3, 1),
    "C10 equality constitution":               (1, 2, 3, 2, 2, 3,  1, 1, 1, 1, 1, 3, 1),
    "C11 credit-intelligence race model":      (1, 2, 3, 2, 2, 2,  1, 3, 1, 1, 1, 3, 1),
    "C12 circular AI-finance compression map": (2, 3, 3, 2, 2, 2,  1, 3, 2, 2, 2, 3, 1),
}


def dominates(a, b) -> bool:
    return all(x >= y for x, y in zip(a, b)) and any(x > y for x, y in zip(a, b))


def frontier(vectors: dict[str, tuple]) -> list[str]:
    return [k for k, v in vectors.items() if not any(dominates(w, v) for j, w in vectors.items() if j != k)]


def main() -> None:
    n_s = len(SCIENCE)
    print("Step 1 - full 13-criterion Pareto frontier:")
    for k in frontier(R):
        print("  ", k)
    for name, agg in (("median", median), ("mean", mean)):
        two = {k: (agg(v[:n_s]), agg(v[n_s:])) for k, v in R.items()}
        print(f"\nStep 2 - two-objective frontier, {name} aggregation (science, economy):")
        for k in frontier(two):
            print(f"   {k}: ({two[k][0]:.2f}, {two[k][1]:.2f})")
        print("   all:", {k.split()[0]: tuple(round(x, 2) for x in v) for k, v in two.items()})


if __name__ == "__main__":
    main()
