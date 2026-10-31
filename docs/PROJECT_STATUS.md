# Project Status

> **Historical research note (17 October 2026).** Preserved for intellectual provenance. The current programme is independent computational research; earlier product, pilot and commercial proposals below are historical options, not a business being launched. Legal, market and novelty statements are dated research assessments, not current advice or independently established priority claims. Personal goals have been omitted from this public edition; equations and scientific results are retained.


*Snapshot as of 2026-10-17 12:15 BST (Stage E complete for Experiment 001; next gate is real data).*

## Project Objective
Economic Genome / ValueGenomics set out to find the single most promising economic institution
that can be invented, tested and built from the accumulated research. Candidates included money,
credit, clearing, ownership, allocation, governance and rights to future resources. The governing
instruction is the founder's mandate (`sources/pasted/2026-10-17_01_project-discovery-mandate.md`):
work in evidence-gated stages, prefer one mathematical result and one reproducible simulation, and
never present an unrun experiment as done.
## Current Stage
- **Stage A (reconstruction): complete.**
- **Stage B (project selection): complete.** Flagship = **Zero-Net**: consent-based,
  custody-free multilateral trade-credit set-off for UK SMEs.
- **Stage C (formal specification): complete.** Preregistered at commit `fc2561e`.
- **Stage D (minimal experiment): complete.** Experiment 001 was run at `fc2561e` with 30 seeds;
  all integrity checks passed.
- **Stage E (continue / redesign / kill): complete for Experiment 001.**
  - Preregistered verdict: **CONTINUE**.
  - The result is interpreted as a model ceiling about 2× real-world benchmarks.
  - The recommendation is to proceed to a real-data gate (one anchor cluster). No product build.
- **Next stage (not started):** Experiment 002, a real-data clearing study. Its spec must be
  written and preregistered before any data arrives.

## Current Branch
`main` (founder's choice). Remote `https://github.com/MoheetBrain/ValueGenomics`. Commits so far:
`238d82b` (initial README), `fc2561e` (Stages A–C plus preregistration). This snapshot is
part of the Stage D/E results commit.

## Current System Architecture
A research repository with one experiment package plus reporting scripts:
- `experiments/exp001_circularity/`:
  - `network.py`: UK-calibrated synthetic firm networks from the ONS 2023 IO table.
  - `clearing.py`: bilateral netting, greedy 3-cycle, optimal max-circulation LP, netting bound,
    checks, sequenced liquidity.
  - `defaults.py`: Eisenberg–Noe default shocks.
  - `run.py`: preregistered runner with automatic verdict.
  - `test_exp001.py`: 15 unit tests.
- `scripts/`:
  - `extract_ons_iot.py`: data extraction.
  - `pareto_candidates.py`: candidate frontier.
  - `summarise_exp001.py`: renders result tables.
  - `posthoc_exp001_beta0.py`: post-hoc benchmark-calibrated curve; labelled post hoc.

## Capabilities Implemented
- Reproducible, seeded UK-calibrated synthetic trade-credit networks, with a configuration null
  model.
- Exact optimal multilateral set-off up to ~130k edges in about a second per instance, with
  validity checks.
- Baselines: bilateral, greedy 3-cycle, netting bound.
- Participation strategies: random, small-firm-only, anchor-cluster.
- Default-shock loss attribution: participants, non-participants, outside creditors.
- Topology statistics, a validation gate, and a leave-one-variant-out predictor.
- An automatic preregistered verdict, with Markdown result tables rendered from `summary.json`.

## Work Completed to Date
1. Corpus located and preserved (`sources/pasted/`). Archives and books audited by four parallel
   sub-agents (`research/audit/`). Personal financial details redacted before commit.
2. Stage A–C documents in `research/`:
   - `source-manifest.md`, `original-ideas.md`, `prior-art.md`, `design-space.md`;
   - `candidate-comparison.md`, `adversarial-review.md`, `flagship-decision.md`;
   - `governance-and-rights.md`.
   Plus `experiments/experiment-001-spec.md`.
3. Experiment 001 executed. Results in `results/exp001/` and `results/experiment-001-summary.md`.
4. Post-hoc calibration analysis (labelled): `results/exp001/posthoc_beta0.json`.
5. Final memo: `research/final-decision-memo.md`.

## Important Files and Artifacts
- **Decision:** `research/final-decision-memo.md` (the nine questions).
- **Evidence:** `results/experiment-001-summary.md`, `results/exp001/summary.json`.
- **Preregistration:** `experiments/experiment-001-spec.md` at `fc2561e`.
- **Prior-art base:** `research/audit/prior-art-verification.md`.
- **Legal design:** `research/governance-and-rights.md`.

## Data Sources and Provenance
- ONS UK input-output analytical tables, product by product, 2023 (Dec 2025 release),
  downloaded 2026-10-17, OGL v3: `data/raw/ons_iot2023product.xlsx` (sha256 `14d8f4bd…`) and
  extracted CSVs. CPA_L68A (imputed rent) is excluded; one negative cell is clipped.
- Founder-supplied pasted documents (three of four are AI-generated): `sources/pasted/`.
- Archives and books in a private reference library are not committed (personal data or copyright). They are
  recorded by path and SHA-256 in the audits.
- External facts were verified on 2026-10-17 (links in the prior-art audit). Benchmarks used:
  - Slovenia AJPES 2025 (≈2.4 % of reported, ≈14 % of considered);
  - Republika Srpska (≈7 % per round; −6 pp default probability);
  - Sardex (≈25 %);
  - vendor corpus (21 % cycle-only);
  - Belgian B2B degree statistics.

## Decisions and Rationale
- **No new currency or token.** Compute money fails a carrying-cost argument, and currency
  candidates face the acceptance equilibrium and the UK perimeter.
- **Flagship = Zero-Net (C6):** on every Pareto frontier; a full institution; causal real-world
  welfare evidence; a £0 decisive test. Its novelty is modest (prior art abroad).
- **Fallback = C2** (open MLPerf compute exchange rates).
- **Stage E:** the preregistered rule gave CONTINUE, so the project proceeds to the real-data
  gate. The post-hoc calibration shows pilot-scale value could be immaterial (1–6 %) under one
  explanation of the model–reality gap, or about 13–15 % under the other. Belgian topology
  favours the second. That makes real data the decisive next step.
- **Go-to-market redesign from the results:**
  - Recruitment must be anchor-led (anchor clusters clear 5.9× random at p = 0.2; small-firm-only
    recruitment is worst).
  - Optimal clearing must be used (greedy heuristics lose ≈46 %).
  - Liquidity-assisted clearing is the redesign path if real yields fall at 3–10 %.
- **Governance for any pilot:** an operator company with binding member protections.

## Verification and Test Results
- `.venv/bin/python -m unittest experiments.exp001_circularity.test_exp001` → **15 tests OK**
  (2026-10-17 12:14 BST).
- `.venv/bin/python -m experiments.exp001_circularity.run` at `fc2561e` → completed in **1,354 s**,
  `all_checks_ok = true`, verdict **CONTINUE**:
  - H1: anchor p = 0.2 φ_book **30.91 % [28.27, 33.56]**; full participation **51.75 %
    [50.85, 52.64]**; 100 % of 18 sensitivity variants ≥ 10 % at full participation (minimum
    23.94 %).
  - V1: reciprocity 6.40 %, passed.
  - H2: sector/firm ratio 1.14, **not supported**.
  - H3: anchor/random 5.86, supported.
  - H4: out-of-sample R² 0.370, **not supported**.
  - E4 (exploratory): clearing cut defaults 108.4 → 99.5 at full participation. The *British
    Eagle* transfer was ≈0.7p per £ cleared.
- `.venv/bin/python scripts/posthoc_exp001_beta0.py` (POST HOC) → under β = 0, full
  participation 23.05 %; anchor p = 0.05/0.1/0.2/0.3/0.5 = 1.00/2.34/6.30/9.46/14.01 %.
- `python3 scripts/pareto_candidates.py` → frontiers as recorded in
  `research/candidate-comparison.md`.

## Known Failures and Limitations
- **The model's ceiling is about 2× the best real-world complete-network clearing rates.**
  Results are upper bounds. Synthetic networks cannot measure real UK clearability.
- Non-strategic participation; a static snapshot; a closed domestic economy; 500–8,000-firm
  economies; stylised default shocks.
- **H2 rejected** (aggregation bias small). **H4 rejected:** the clearability predictor remains
  an open problem.
- The mechanism is prior art (Slovenia, Republika Srpska, Sardex, Cycles). The novelty claim is
  limited to UK design, data and recruitment findings.
- Several claims in the pasted reports were wrong, outdated or fabricated (`research/prior-art.md`
  §F). The claimed APMN origin and the "research repository" archive were not found.
- The legal analysis is an issues map, not counsel advice.

## Risks and Technical Debt
- **Strategic:**
  - real clearability may be low;
  - anchors may refuse because they lose float (Proposition 3);
  - Cycles ($8.7m raised) or accounting platforms could enter the UK;
  - UK e-invoicing could let platforms or HMRC do clearing themselves [unverified].
- **Legal:** *British Eagle*, s.127, s.239, the FCA substance test, competition-law information
  exchange, UK GDPR for sole traders.
- **Technical debt:**
  - Python loops in the greedy heuristic and topology statistics are slow at 100k+ edges.
  - Solver selection was tuned empirically: HiGHS default with an interior-point fallback.
  - A lightweight publication CI workflow now runs the existing unit tests; this line described the original research snapshot.
  - The H4 feature set is too narrow.

## Current Blockers
- **Real invoice data:** an anchor firm and its counterparties must agree to share ledgers. This
  is founder outreach; an agent cannot do it.
- **UK Data Service registration** for the public Sarafu dataset (an account the founder must
  create).
- A **legal opinion** on the set-off template and perimeter is needed before any live pilot. The
  real-data study does not need it.

## Exact Next Actions
1. Write and commit `experiments/experiment-002-spec.md` *before* any data arrives:
   - real-data protocol (invoice ID, Companies House numbers, amount, due date, status);
   - DPIA outline and NDA template;
   - preregistered thresholds: < 3 % kill, ≥ 10 % continue to a live pilot, otherwise
     liquidity-assisted redesign.
2. Approach one anchor firm, either a south-London main contractor or a council procurement
   team for its top-200 suppliers, for a one-off open-invoice export.
3. Register with the UK Data Service, download Sarafu 2020–21, and run the existing clearing
   code on it as the first real-network check.
4. Extend the H4 feature set (hub concentration, size–degree elasticity, cycle-space measures)
   and re-test on synthetic plus Sarafu data.
5. Obtain a fixed-fee counsel quote for the set-off template and perimeter opinion.
