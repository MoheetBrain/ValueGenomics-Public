"""POST-HOC analysis for Experiment 001 (not preregistered; does not change the verdict).

Motivation (written after seeing the preregistered results): the reference economy clears ~52 % at
full participation, about twice the best real-world complete-network figures (21-25 %). The only
single-parameter sensitivity variant landing near the real figures is attachment_beta = 0
(suppliers chosen without regard to size), which cleared 23.9 % at full participation but only
6.5 % for an anchor cluster at p = 0.2. This script maps the participation curve in that
"benchmark-calibrated" world, to size a real pilot cluster.

    .venv/bin/python scripts/posthoc_exp001_beta0.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from experiments.exp001_circularity.network import generate, select_participants  # noqa: E402
from experiments.exp001_circularity.run import REFERENCE, evaluate, ci  # noqa: E402

BASE = 20261017 + 900_000  # seed stream disjoint from the preregistered blocks
P_GRID = (0.05, 0.1, 0.2, 0.3, 0.5)


def main() -> None:
    params = REFERENCE.with_(attachment_beta=0.0)
    out: dict[str, dict] = {}
    rows: dict[str, list[float]] = {}
    for r in range(30):
        econ = generate(params, BASE + r)
        prng = np.random.default_rng(BASE + r + 500_000)
        settings = [("all", 1.0)] + [(s, p) for s in ("anchor", "random") for p in P_GRID]
        for s, p in settings:
            res = evaluate(econ, select_participants(econ, s, p, prng))
            rows.setdefault(f"{s}@{p}", []).append(res["phi_book_mtcs"])
    for k, v in rows.items():
        out[k] = ci(v)
    path = ROOT / "results/exp001/posthoc_beta0.json"
    path.write_text(json.dumps({"label": "POST HOC - not preregistered", "params": "reference with attachment_beta=0",
                                "base_seed": BASE, "phi_book_mtcs": out}, indent=2))
    for k, c in out.items():
        print(f"{k:12s} {100 * c['mean']:6.2f} [{100 * c['ci95_low']:.2f}, {100 * c['ci95_high']:.2f}]")


if __name__ == "__main__":
    main()
