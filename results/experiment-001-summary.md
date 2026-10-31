# Experiment 001 — Results and Stage E verdict

**Run:** 2026-10-17, 11:48–12:10 BST, at preregistration commit `fc2561e`. 30 seeds per cell,
2,100 economy × participation evaluations plus 60 default-shock scenarios. Runtime 22.6 min.
Python 3.14.7, NumPy 2.5.4, SciPy 1.18.1.
**Integrity:** every optimal solution passed the circulation and residual-acyclicity checks
(`all_checks_ok = true`).
**Raw outputs:** `results/exp001/runs.csv`, `defaults.csv`, `summary.json`. Tables below are
rendered by `scripts/summarise_exp001.py`.
**Post-hoc analyses** are labelled as such and do not change the preregistered verdict.

---

## 1. Preregistered verdict: **CONTINUE**

| Criterion (spec §4) | Threshold | Result | Met? |
|---|---|---|---|
| H1a: anchor cluster, p = 0.2, φ_book lower 95 % CI | ≥ 10 % | **30.91 % [28.27, 33.56]** | yes |
| H1b: full participation, φ_book lower 95 % CI | ≥ 10 % | **51.75 % [50.85, 52.64]** | yes |
| H1c: share of 18 sensitivity variants with full-participation mean ≥ 10 % | ≥ 70 % | **100 %** (minimum 23.94 %, at β = 0) | yes |
| Kill rule: full-participation upper 95 % CI < 3 % | — | 52.64 % | not triggered |
| V1: mean reciprocity of reference networks in [1 %, 15 %] | — | **6.40 %** (range 5.44–7.74) | passed |
| H2: sector-level φ ≥ 2× firm-level | ≥ 2.0 | **1.14×** (58.77 % vs 51.75 %) | **not supported** |
| H3: anchor ≥ 2× random at p = 0.2 | ≥ 2.0 | **5.86×** | supported |
| H4: topology predictor, out-of-sample R² | ≥ 0.7 | **0.370** (570 runs, 19 variants) | **not supported** |

**What CONTINUE means here (and what it does not).** Under UK-calibrated topology, the
*mechanical ceiling* on debt that can be cancelled without money is large, and robust across
every plausible parameter. Every variant clears ≥ 24 % at full participation. A recruited anchor
cluster of 20 % clears ≥ 10 % in 17 of 18 variants. The experiment does **not** show that real
UK firms would achieve these numbers. The model's ceiling is about twice the best real-world
complete-network figures (§4), so these results are upper bounds. CONTINUE authorises the
next evidence gate (real data), not a product build.

## 2. Main results

### 2.1 Participation curves (reference economy; φ_book, % of participants' trade-credit book; mean [95 % CI], n = 30)

| strategy | p=0.05 | p=0.1 | p=0.2 | p=0.3 | p=0.5 |
|---|---|---|---|---|---|
| random | 0.69 [0.30, 1.09] | 1.87 [1.34, 2.41] | 5.27 [4.51, 6.04] | 10.42 [9.22, 11.62] | 20.56 [19.18, 21.94] |
| small firms only (random) | 0.35 [0.20, 0.50] | 1.16 [0.82, 1.49] | 3.64 [3.10, 4.18] | 7.28 [6.60, 7.96] | 14.91 [14.12, 15.71] |
| **anchor cluster** | **18.57 [16.37, 20.76]** | **22.54 [20.18, 24.91]** | **30.91 [28.27, 33.56]** | 38.62 [36.46, 40.77] | 47.60 [46.65, 48.55] |
| all (p = 1) | 51.75 [50.85, 52.64] | | | | |

- **Cold start is real, and recruitment strategy dominates it.** Random recruitment at 5 %
  clears 0.7 % of members' books. Anchor-cluster recruitment of the same number of firms clears
  18.6 %, about 27× more. This is Proposition 2 in action: random sets rarely contain whole cycles.
- **Small firms alone cannot close cycles.** Small-firm-only recruitment is the *worst*
  strategy at every p. Cycles run through large firms, so the hubs are needed, even though
  Proposition 3 says late-paying hubs may lose float. The central adoption problem is therefore
  **getting an anchor to join**, not getting many small firms to join.

### 2.2 Algorithms (reference economy)

| setting | bilateral | greedy 3-cycle | **optimal MTCS** | MTCS as % of internal obligations | netting bound (% of internal) |
|---|---|---|---|---|---|
| all | 16.19 [15.42, 16.96] | 27.99 [27.29, 28.68] | **51.75 [50.85, 52.64]** | 51.75 | 67.60 [66.81, 68.39] |
| anchor p=0.2 | 13.04 [11.46, 14.62] | 19.90 [18.19, 21.60] | **30.91 [28.27, 33.56]** | 50.29 [47.25, 53.34] | 66.60 [64.07, 69.14] |
| random p=0.2 | 3.03 [2.35, 3.72] | 3.68 [2.95, 4.41] | **5.27 [4.51, 6.04]** | 27.18 [24.28, 30.09] | 53.47 [51.57, 55.38] |

- The naive "find loops and offset them" approach (greedy 3-cycles, as proposed in source 02)
  **misses ≈ 46 % of the clearable value** at full participation. Optimal max-circulation
  matters, and the LP is cheap.
- The gap between MTCS and the netting bound is what only novation to a central counterparty
  could add. Per Proposition 1, *sequenced settlement of the residual already achieves the
  netting bound's cash requirement* without novation.

### 2.3 Sensitivity (φ_book, optimal MTCS, %; mean [95 % CI])

| variant | all (p=1) | anchor p=0.2 | random p=0.2 |
|---|---|---|---|
| supplier_median=3 | 32.00 [30.80, 33.20] | 20.83 [19.01, 22.65] | 1.77 [1.08, 2.47] |
| supplier_median=5 | 42.35 [41.20, 43.51] | 26.25 [23.05, 29.45] | 4.52 [2.91, 6.13] |
| supplier_median=20 | 58.30 [57.49, 59.10] | 33.88 [31.83, 35.94] | 8.37 [7.50, 9.25] |
| supplier_median=40 | 61.77 [61.14, 62.40] | 37.17 [35.23, 39.11] | 10.15 [9.49, 10.81] |
| n_firms=500 | 53.59 [52.42, 54.77] | 24.01 [21.86, 26.16] | 6.19 [5.26, 7.11] |
| n_firms=8000 | 47.93 [47.06, 48.80] | 34.94 [31.68, 38.20] | 5.42 [4.42, 6.43] |
| **attachment_beta=0** | **23.94 [22.89, 24.99]** | **6.51 [6.12, 6.90]** | 1.81 [1.67, 1.94] |
| attachment_beta=0.5 | 44.58 [43.83, 45.33] | 22.61 [21.20, 24.01] | 3.79 [3.45, 4.14] |
| pareto_alpha=1.5 | 52.08 [51.33, 52.83] | 23.29 [21.07, 25.52] | 4.17 [3.66, 4.67] |
| pareto_alpha=2.0 | 53.42 [52.79, 54.05] | 20.61 [18.89, 22.34] | 3.88 [3.44, 4.33] |
| supplier_size_elasticity=0 | 39.56 [38.39, 40.74] | 16.03 [13.12, 18.93] | 2.32 [1.89, 2.74] |
| supplier_size_elasticity=0.7 | 59.81 [59.09, 60.52] | 38.67 [36.89, 40.46] | 8.24 [7.27, 9.21] |
| supplier_sigma=0.4 | 53.30 [52.40, 54.20] | 31.07 [28.29, 33.86] | 5.78 [4.82, 6.74] |
| supplier_sigma=1.2 | 50.82 [49.70, 51.95] | 31.64 [29.13, 34.15] | 5.74 [4.94, 6.54] |
| firms_by=√output | 53.58 [52.68, 54.49] | 38.57 [36.55, 40.58] | 5.22 [4.22, 6.23] |
| structure=configuration (no IO structure) | 45.01 [44.04, 45.99] | 33.32 [31.27, 35.37] | 4.90 [3.93, 5.87] |
| payment days uniform 45 | 51.14 [50.11, 52.18] | 29.29 [26.21, 32.37] | 5.85 [5.11, 6.60] |
| payment days 30→90 | 52.30 [51.22, 53.39] | 30.66 [28.31, 33.00] | 5.50 [4.51, 6.49] |

Reading the table:
- The decisive parameters are **supplier concentration on large firms (β)**, the size
  elasticity of supplier counts (η) and the supplier count (k̃). Payment-day assumptions,
  degree dispersion and the firm allocation rule barely matter.
- **Input-output structure adds only ≈ 7 pp** (configuration null 45.0 % vs 51.75 %). Most of
  the circularity comes from size and degree structure, not sectoral composition.
- **Scale:** clearability at full participation falls slowly with economy size (53.6 % →
  51.7 % → 47.9 % for 500 → 2,000 → 8,000 firms). Extrapolation to millions of firms is
  untested, which is another reason to read results as upper bounds.

### 2.4 Network statistics of the reference economy (validation)
- Reciprocity 6.40 % (real production networks: 2–9 %) ✓.
- Mean out-degree 15.1; spend coverage 62.5 %.
- **The largest strongly connected component holds 92.6 % of firms and 98.7 % of obligation
  value.** Republika Srpska's *reported late-debt* network had a strongly connected component of
  about 1,000 of 12,000–16,000 participants. The real clearing graph is a sparse subgraph
  (only reported, overdue debts), not the full trade network. This is the main candidate
  explanation for the model–reality gap (§4).

### 2.5 Distribution (exploratory)
- Full participation: small firms (outside the top 1 %) get **74.9 %** of cleared value
  against **76.5 %** of participants' receivables. The median share of receivables cleared is
  64.1 % for small firms and 59.9 % for large ones.
- Anchor cluster p = 0.2: 60.7 % vs 63.4 %. Median share 26.9 % (small) vs 30.7 % (large).
- **Interpretation:** in volume terms, clearing is roughly **distribution-neutral**. It is
  neither strongly progressive nor regressive. Any progressive effect must come from the
  *value* per £ cleared: higher financing costs and fragility of small firms (Proposition 3; the
  Republika Srpska evidence). It does not come from who gets cleared.

### 2.6 Default shock (exploratory E4; 5 % of firms lose external assets; Eisenberg–Noe)

| | defaults (mean) | total loss | losses of participants | transfer to participants from others, per £ cleared | same with distress screen | cleared value kept with screen |
|---|---|---|---|---|---|---|
| no clearing | 108.4 | 5,711 | — | — | — | — |
| anchor p=0.2 | 107.8 | 5,686 | 1,633 → 1,398 | **0.72p [0.18, 1.27]** | 0.07p | 21.9 % |
| all | **99.5** | **5,630** | 2,855 → 2,122 | **0.66p [0.50, 0.83]** | 0.33p | 81.0 % |

- **Clearing reduced defaults** by 8 % at full participation and total losses by 1.4 %. The
  direction matches Republika Srpska's causal finding, though the magnitude is not comparable.
- **The *British Eagle* externality (Proposition 4) is real but small:** about 0.7p per £
  cleared moves from non-participants and outside creditors to participants.
- An imperfect distress screen cuts the transfer by 50–90 %, at a large cost in cleared value
  for small clusters. Screening design is a real trade-off.

## 3. Hypotheses scorecard

| ID | Hypothesis | Outcome |
|---|---|---|
| H1 | Material clearability (≥ 10 %) at anchor p = 0.2 and full participation, robust | **Supported** (as a model ceiling) |
| V1 | Generator reciprocity realistic | **Passed** |
| H2 / N-6 | Sector-level data overstate clearability ≥ 2× | **Rejected**: only 1.14×. Sector IO data are a usable rough guide to the ceiling |
| H3 / N-3 | Anchor recruitment ≥ 2× random | **Supported**: 5.9× at p = 0.2 and about 27× at p = 0.05 |
| H4 / N-7 | Cheap topology statistics predict clearability out of sample (R² ≥ 0.7) | **Rejected**: R² = 0.37. The predictor gap identified by the prior-art audit **remains open**. Reciprocity, strongly connected share and degree are not enough; candidate features are hub concentration (β-like) and supplier-count elasticity |
| P1–P4 | Propositions | Proved; P1, P2 and P4 verified numerically in tests; P4 magnitude measured in E4 |

## 4. External calibration (POST HOC — not preregistered)

| Benchmark | Clearing share | Comparable model quantity | Model |
|---|---|---|---|
| Sardex (closed circuit, Fleischman et al. 2020) | ≈ 25 % of net internal debt | full participation | 51.75 % |
| Vendor corpus, 133k invoices (arXiv 2606.26126) | 21 % cycle-only | full participation | 51.75 % |
| Slovenia AJPES 2025 | 14.2 % of "considered"; 2.4 % of reported | internal share at random low p; φ_book at p ≈ 0.05 | 27 % (p = 0.2 internal); 0.7 % (p = 0.05) |
| Republika Srpska | ≈ 7 % of late debt per round | — | — |

**The model's full-participation ceiling is about 2× the best real complete-network figures.**
Two explanations give different answers for pilot-scale value:

1. **Frictions explanation.** Topology is right, but real-world frictions scale clearing down
   by about half: only some invoices are submitted, timing mismatches, foreign suppliers, cash
   payments, disputes. Applying the real/model ratio (21–25 / 51.75 ≈ 0.41–0.48) to the anchor
   results gives about **13–15 % at p = 0.2** and about **8–9 % at p = 0.05**. Material, but
   only just at small cluster sizes.
2. **Topology explanation.** Real networks have less hub concentration. The one variant that
   matches the benchmarks is β = 0 (23.9 %). A post-hoc run (`scripts/posthoc_exp001_beta0.py`,
   `results/exp001/posthoc_beta0.json`, 30 fresh seeds) gives anchor clusters only **1.0 % at
   p = 0.05, 2.3 % at 0.1, 6.3 % at 0.2, 9.5 % at 0.3 and 14.0 % at 0.5**. A pilot of 5–10 % of
   a local economy would be immaterial.

**Evidence between the two (post hoc).** Customer-degree skew in Belgian data (median 4–5,
mean 29–36, top 1 % > 400 buyers) is *more* concentrated than the reference model (median 7.8,
mean 14.9) and far more than β = 0 (median 14.0, mean 14.9). That **favours the frictions
explanation**. It cannot settle the matter: synthetic degree statistics at n = 2,000 are not
directly comparable with a 100k-firm national network.

## 5. Stage E recommendation

**CONTINUE, as the preregistered rule requires, to the real-data gate. Redesign the go-to-market
around what the experiment revealed. Build no product beyond what that gate needs.**

1. **The decisive unknown is now precise.** Two empirical quantities in a real cluster decide
   whether a pilot-sized clearing club is material:
   - (a) how concentrated trade is on hub firms (β/η-like statistics);
   - (b) what fraction of members' invoices are actually submitted and simultaneously
     outstanding (the friction factor).
   Synthetic data cannot resolve either.
2. **Recruitment must be anchor-led.** Random or SME-only recruitment cannot close cycles at
   feasible sizes. The first conversation is with one anchor (a main contractor, a council's
   supplier base, a wholesaler) and its trading partners. That anchor may lose float, so the
   value proposition must run through the Commercial Payments Bill (statutory interest, caps,
   reporting): legal question N-8.
3. **Use optimal clearing, not loop-finding heuristics.** Heuristics lose about half the value.
4. **Add liquidity-assisted clearing as Experiment 002 candidate.** If real clearability lands
   at 3–10 %, the open prior-art slot (BIS-style auction pricing of liquidity for near-cycles;
   Sardex 25 % → 50 % with a liquidity source) is the redesign path. Custody would be through a
   regulated partner.
5. **Kill criteria remain armed:** fewer than 3 % of submitted value cleared in a real
   ≥ 30-firm anchor cluster; or no anchor recruitable within 3 months; or an adverse FCA or
   counsel perimeter view.

## 6. Limitations of this experiment
- Synthetic networks. Non-strategic participation (universal consent within clusters). A
  single static snapshot with no churn. A closed domestic economy (imports excluded).
- Modelled economies have 500–8,000 firms.
- Default shocks are stylised: no default costs, external assets assumed.
- H4 used one feature set. Its failure says these three features are insufficient, not that
  clearability is unpredictable.
- The post-hoc analyses (§4) were designed after seeing results. They inform the next step
  only.
