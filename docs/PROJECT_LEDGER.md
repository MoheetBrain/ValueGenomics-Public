# Project Ledger

> **Historical research note (17 October 2026).** Preserved for intellectual provenance. The current programme is independent computational research; earlier product, pilot and commercial proposals below are historical options, not a business being launched. Legal, market and novelty statements are dated research assessments, not current advice or independently established priority claims. Personal goals have been omitted from this public edition; equations and scientific results are retained.


Append-only chronological record. One entry per commit. Old entries are never rewritten except
to correct a demonstrable factual error, and any such correction is documented in the entry
that makes it.

---

## 2026-10-17 11:50 BST — Stages A–C complete; Experiment 001 preregistered

- **Branch:** `main` (parent `238d82b` "Initial commit")
- **Project stage:** Stage C complete; Stage D code written and tested; full experiment not yet run.
- **Objective of the change:**
  - Turn an empty repository into an auditable research base.
  - Reconstruct and audit all sources.
  - Select one flagship project by evidence.
  - Formally specify it, and preregister its first experiment before any result is viewed.
- **Files and systems changed:**
  - **New:**
    - `sources/pasted/` (4 founder-supplied documents);
    - `research/audit/` (4 audit reports);
    - `research/{source-manifest, original-ideas, prior-art, design-space, candidate-comparison,
      adversarial-review, flagship-decision, governance-and-rights}.md`;
    - `experiments/experiment-001-spec.md`;
    - `experiments/exp001_circularity/` (package: network, clearing, defaults, run, tests);
    - `scripts/extract_ons_iot.py`, `scripts/pareto_candidates.py`;
    - `data/raw/ons_iot2023product.xlsx`, `data/processed/*.csv`;
    - `requirements.txt`, `.gitignore`;
    - `docs/PROJECT_STATUS.md`, `docs/PROJECT_LEDGER.md`.
  - **Modified:** `README.md`.
  - **Local only:** `.venv/` (git-ignored).
- **What was completed:**
  - Corpus located: the repo had only a README; sources were in the session and a private reference library.
  - Four parallel audits completed.
  - Private material was excluded during the original research audit.
  - Twelve candidates compared.
  - Flagship **Zero-Net** selected: consent-based, custody-free multilateral trade-credit
    set-off for UK SMEs, with a clearability science.
  - Four propositions proved.
  - Experiment 001 fully specified with thresholds and decision rule.
- **Decisions made and why:**
  - No currency or token. Compute money fails a carrying-cost argument, and currency candidates
    face acceptance and perimeter barriers.
  - C6 chosen: it is on every Pareto frontier, is a full institution, has causal real-world
    welfare evidence and a £0 decisive test.
  - C2 is the fallback.
  - Thresholds fixed at 10 % / 3 % before results, justified by external benchmarks.
  - Raw archives and books are not committed (personal data, copyright).
  - Work stays on `main` (founder's choice).
- **Tests and verification actually executed:**
  - `.venv/bin/python -m unittest experiments.exp001_circularity.test_exp001 -v` → 15 tests OK.
  - `.venv/bin/python -m experiments.exp001_circularity.run --smoke` → finished in 104 s,
    printing timings only.
  - `python3 scripts/pareto_candidates.py` → frontiers as recorded in
    `research/candidate-comparison.md` §3.
  - Solver check on one 8,000-firm network: HiGHS default and interior point agree to about 12
    significant figures.
- **Results:** no experimental results yet (by design).
- **Failures or unresolved uncertainty:**
  - First solver configuration (max-scaling) falsely reported "infeasible" at 8,000 firms.
    Fixed with median scaling.
  - Dual simplex stalled (112 s) on one instance. Switched to the HiGHS default with an
    interior-point fallback.
  - The claimed APMN origin and the "research repository" archive are not found.
  - Legal conclusions are unverified by counsel.
  - Synthetic data cannot measure real UK clearability.
- **Effect on the overall project:**
  - The programme moves from a broad "invent better money" ambition to one falsifiable
    institution with a concrete kill test.
  - The "Economic Genome" engine is repositioned as later-stage constrained mechanism search,
    once one validated domain exists.
- **Next intended step:**
  - Run Experiment 001 at this commit.
  - Interpret it against the preregistered rule.
  - Write the results summary and final decision memo, then commit.

---

## 2026-10-17 12:15 BST — Experiment 001 executed; Stage E verdict CONTINUE (as model ceiling); final memo

- **Branch:** `main` (parent `fc2561e`, the preregistration commit)
- **Project stage:** Stage D and Stage E complete for Experiment 001. Next gate: Experiment 002
  (real data), not started.
- **Objective of the change:**
  - Record the preregistered Experiment 001 results and their interpretation against the
    preregistered rule.
  - Add a clearly labelled post-hoc calibration analysis.
  - Write the final decision memo.
- **Files and systems changed:**
  - **New:**
    - `results/exp001/{runs.csv, defaults.csv, summary.json, posthoc_beta0.json}`;
    - `results/experiment-001-summary.md`;
    - `research/final-decision-memo.md`;
    - `scripts/summarise_exp001.py`, `scripts/posthoc_exp001_beta0.py`.
  - **Modified:**
    - `docs/PROJECT_STATUS.md` (full rewrite);
    - `research/flagship-decision.md` (status line);
    - `research/original-ideas.md` (outcomes for N-3, N-4/N-5, N-6, N-7);
    - `README.md`.
- **What was completed:**
  - Full run at `fc2561e`: 30 seeds, 2,100 evaluations plus 60 default scenarios, 1,354 s,
    all integrity checks passed.
  - Results interpreted.
  - Post-hoc β = 0 calibration run (30 fresh seeds).
  - Post-hoc customer-degree comparison with Belgian statistics.
  - Final memo answering all nine questions.
- **Decisions made and why:**
  - The verdict is the preregistered rule's output (CONTINUE). It is not overridden.
  - Because the model's full-participation ceiling (51.7 %) is about 2× the best real-world
    complete-network figures (21–25 %), CONTINUE is read as authorising the real-data gate only.
  - The go-to-market is redesigned to be anchor-led, because H3 showed 5.9× over random and
    small-firm-only recruitment was worst.
  - Liquidity-assisted clearing is added as the Experiment 002 redesign path.
- **Tests and verification actually executed:**
  - `.venv/bin/python -m experiments.exp001_circularity.run` → verdict CONTINUE;
    `all_checks_ok = true`.
  - `.venv/bin/python -m unittest experiments.exp001_circularity.test_exp001` → 15 OK.
  - `python3 scripts/summarise_exp001.py` → tables reproduced in
    `results/experiment-001-summary.md`.
  - `.venv/bin/python scripts/posthoc_exp001_beta0.py` → β = 0 curve (post hoc).
- **Results:**
  - **H1 supported:** anchor p = 0.2 30.91 % [28.27, 33.56]; full participation 51.75 %
    [50.85, 52.64]; 100 % of sensitivity variants ≥ 10 %.
  - **V1 passed:** reciprocity 6.40 %.
  - **H2 rejected:** 1.14×.
  - **H3 supported:** 5.86×.
  - **H4 rejected:** R² 0.370.
  - Greedy 3-cycle clearing captures only 28.0 % against 51.7 % optimal.
  - E4: defaults 108.4 → 99.5; transfer to participants ≈0.7p per £ cleared.
  - Post hoc, β = 0: full participation 23.05 %; anchor p = 0.2 6.30 %.
- **Failures or unresolved uncertainty:**
  - The model overstates real-world clearability by about 2×. The cause is unidentified:
    frictions vs topology. Belgian degree skew favours frictions, but this is not conclusive.
  - H4 predictor failed. Real UK data are absent.
  - Legal conclusions are not counsel-verified.
- **Effect on the overall project:**
  - The flagship survives its first kill test.
  - The decisive unknown is narrowed to two measurable real-data quantities: hub concentration
    and the friction factor.
  - It also needs an anchor that will join.
  - No product or infrastructure is justified yet.
- **Next intended step:**
  - Preregister `experiments/experiment-002-spec.md` (real-data protocol, DPIA, thresholds
    < 3 % kill / ≥ 10 % continue).
  - Founder outreach to one anchor cluster.
  - Founder registration with the UK Data Service for the Sarafu dataset.
