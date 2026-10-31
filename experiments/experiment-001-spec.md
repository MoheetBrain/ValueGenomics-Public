# Experiment 001 — How much UK trade credit can be extinguished without money?

**Status: PREREGISTERED.** This specification, the code in `experiments/exp001_circularity/`
and the decision thresholds below are committed **before** the full run. Git history is the
timestamp. Before preregistration only three things were run: (a) unit tests on hand-built toy
graphs and small random graphs, (b) a timing-only smoke run that printed run times and edge
counts but no clearing results, and (c) a solver-scaling check on one 8,000-firm network,
which printed solver status and objective agreement between two solvers. No reference-scenario
clearing fraction had been viewed when the thresholds were fixed.

Stage C/D artefact · flagship: **Zero-Net** (`research/flagship-decision.md`) · date 2026-10-17

---

## 1. The unknown being resolved

Multilateral set-off is a proven institution abroad. Its value depends entirely on one
quantity: **how much of an economy's trade credit lies on cycles**, and how much of that
survives partial participation. Published real-world rates range from ≈2.4 % (Slovenia 2025,
of reported obligations) through ≈7 % (Republika Srpska, per round) to 21–25 % (a vendor
corpus; the closed Sardex circuit). No UK estimate exists, and no validated model predicts the
rate from network structure (`research/prior-art.md` §B).

**Primary question.** In a firm-level trade-credit network calibrated to the UK economy, what
share of participants' trade-credit book does optimal consent-based set-off extinguish, at
realistic participation and with realistic recruitment strategies?

## 2. Model

### 2.1 Obligation network
Firms i = 1…n. An obligation edge e = (i → j, f_e) means firm i (debtor) owes firm j (creditor)
f_e > 0. Write b = B f for net positions (receivables − payables), where B is the node–edge
incidence matrix.

### 2.2 Clearing (the intervention)
Among participants P, optimal multilateral trade-credit set-off (MTCS) solves the bounded
maximum-circulation linear programme on edges with both endpoints in P:

  maximise Σ_e c_e  subject to  B_P c = 0,  0 ≤ c_e ≤ f_e.

Implementation: `clearing.max_circulation`, HiGHS via SciPy, with obligation amounts scaled by
the median. Interior point is the fallback solver. Every solution is checked for circulation
validity and residual acyclicity (`checks_ok`).

### 2.3 Baselines
1. **No clearing** (gross settlement): 0 extinguished.
2. **Bilateral netting** (2-cycles only).
3. **Greedy 3-cycle heuristic**: bilateral netting, then greedy offsetting of directed
   triangles. This stands in for simple "find loops and offset them" tools.
4. **Netting upper bound**: the reduction a central counterparty with novation could achieve,
   gross − Σ net debit positions. Not attainable by set-off; reported as a ceiling.

### 2.4 Synthetic UK-calibrated economies (`network.py`)
- **Sectors:** the 104 CPA products of the ONS 2023 domestic product-by-product IO table
  (`data/raw/ons_iot2023product.xlsx`, OGL v3). **CPA_L68A (imputed owner-occupier rent)** is
  dropped because it is not trade between firms. The one negative cell (a FISIM adjustment) is
  in that row; any remaining negatives are clipped to 0. This leaves 103 sectors and domestic
  technical coefficients a[s,t] = Z[s,t]/X[t]. Imports are excluded: they are paid outside the
  network.
- **Firms per sector:** proportional to output (sensitivity: √output), at least one each.
- **Size within sector:** Pareto(α) draws scaled to sector output.
- **Supplier count:** lognormal (median k̃, dispersion σ) × (size/median size)^η, clipped to [1, n−1].
- **Supplier choice:** a buyer allocates supplier slots across input sectors in proportion to
  its coefficients. Within a sector it chooses distinct suppliers with probability ∝ size^β and
  splits spend by the same weights. Spend on sectors with no drawn supplier is bought outside
  the network; its share is recorded as `spend_coverage`.
- **Obligation stock:** annual spend × payment days / 365. Payment days rise linearly from
  `payment_days_small` to `payment_days_large` with the buyer's size quantile.
- **Configuration null** (`structure="configuration"`): same firms, sizes, supplier counts and
  spend per buyer, but suppliers drawn ignoring sectors. This removes input-output structure.

**Reference parameters, fixed before the run:**

| Parameter | Value | Justification |
|---|---|---|
| n_firms | 2,000 | Regional-cluster scale. Sensitivity 500 and 8,000. |
| supplier_median k̃ | 10 | Belgian B2B data: median suppliers 9 (2014) and 12 domestic (2002–21) (Bernard et al. 2022; NBB WP 444) |
| supplier_sigma σ | 0.8 | Heavy-tailed degrees together with the size effect. Sensitivity 0.4, 1.2. |
| supplier_size_elasticity η | 0.35 | Assumption (larger firms have more suppliers). Sensitivity 0, 0.7. |
| pareto_alpha α | 1.1 | Zipf-like firm sizes (Axtell 2001). Sensitivity 1.5, 2.0. |
| attachment_beta β | 1.0 | Assumption (choose larger suppliers more often). Sensitivity 0, 0.5. |
| payment days | 40 → 65 by size quantile | Assumption: large firms pay slower. Sensitivity uniform 45; 30 → 90. |
| firms_by | output | Assumption. Sensitivity √output. |

### 2.5 Participation (independent variable)
- `random`: a uniformly random p-share of firms.
- `sme_random`: a random p-share drawn only from firms outside the top 1 % by size.
- `anchor`: breadth-first recruitment from the largest firm through its trading links,
  neighbours largest first. This is the "onboard an anchor buyer and its supply chain"
  go-to-market.
- `all`: every firm.

p ∈ {0.05, 0.10, 0.20, 0.30, 0.50}, plus `all`.

## 3. Mathematical results (proved here; checked numerically in `test_exp001.py`)

**Proposition 1 (custody-free clearing reaches the netting liquidity bound).** Let c* be an
optimal bounded circulation and r = f − c*.
(i) The support of r is acyclic.
(ii) b is unchanged: B r = B f.
(iii) Settling r in topological order requires total cash injection exactly Σ_i (−b_i)^+.
(iv) No settlement method whatever, including a central counterparty with novation, can
inject less.

*Proof.* (i) If r had a cycle C with r_e > 0 on all its edges, c* + ε·1_C with ε = min_C r_e
would be feasible with a larger objective. That contradicts optimality. (ii) B c* = 0.
(iii) In topological order every predecessor of v has already paid, so v holds in_v before
paying out_v and must inject max(0, out_v − in_v) = (−b_v)^+. (iv) Cash is conserved, and
each net debtor's outflows exceed its inflows by −b_v, which must come from outside. ∎

*Meaning.* Firms that never hand money to the operator, and never novate debts to it, can
still achieve the cash efficiency of full multilateral netting. Two things are needed:
consented set-off of cycles, and paying the residual in the right order.

**Proposition 2 (cold start).** Decompose c* into simple cycles C_k with weights w_k (flow
decomposition). For any participant set P, c*(G[P]) ≥ Σ_{k: C_k ⊆ P} w_k |C_k|. Under
independent participation with probability p:

  E[cleared(P)] ≥ Σ_k w_k |C_k| p^{|C_k|}.

*Proof.* The cycles that lie wholly inside P sum to a feasible bounded circulation on G[P]. ∎

*Meaning.* Value from random recruitment decays like p^L in cycle length L. Republika Srpska's
median cycle length is about 10, so recruitment must be clustered, not random. (H3 tests the
size of this effect.)

**Proposition 3 (no free money; who gains).** For any circulation c, every firm's cleared
receivables equal its cleared payables. Net positions and cash balances are therefore
unchanged, and **no wealth is created**. Suppose each invoice e would otherwise be paid τ_e
after the clearing date, and firm i finances at rate r_i. The time-value gain to firm i is
r_i(Σ_{e→i} c_e τ_e − Σ_{i→e} c_e τ_e). The total gain is Σ_e c_e τ_e (r_creditor − r_debtor),
which is zero under uniform financing costs. A firm whose payables would have been settled
later than its receivables (a late payer) loses float, so individual rationality can fail for
large late payers. Welfare gains therefore come only from heterogeneous financing costs,
avoided default and coordination losses, and lower transaction and collection costs. ∎

**Proposition 4 (British Eagle externality).** Let firm D be insolvent with assets a and
liabilities l (a < l). A cycle through D with cleared amount c removes c from both. A creditor
of D whose claim x was not cleared then recovers x(a−c)/(l−c) instead of xa/l. That is a loss
of x·c(l−a)/(l(l−c)) > 0, transferred to D's cleared creditor, who is paid in full. ∎

*Meaning.* This is the effect the House of Lords refused to let a contractual clearing scheme
impose in *British Eagle* [1975]. The design must screen out insolvent and petitioned firms
and must not carry unexecuted netting obligations forward (`research/governance-and-rights.md`).

## 4. Hypotheses and decision rule (preregistered)

Primary metric: **φ_book** = value set off ÷ participants' trade-credit book, where the book is
the average of participants' total receivables and total payables, **including obligations
with non-participants**. At full participation φ_book equals the economy-wide cleared share.

**H1 (primary).** In the reference economy, optimal MTCS gives φ_book ≥ 10 % (lower 95 % CI
bound) both for `anchor` at p = 0.2 and for `all`, and the `all` mean is ≥ 10 % in at least
70 % of the 18 sensitivity variants.

**Decision rule** (implemented verbatim in `run.py`):
- **KILL** if the reference `all` upper 95 % CI bound is < 3 %. Cycle-only clearing is then
  immaterial even at full participation. Abandon C6 and fall back to C2.
- **CONTINUE** if every H1 condition holds **and** the validation gate V1 passes.
- **REDESIGN** otherwise. In practice: the effect is between 3 % and 10 %, or it is sensitive
  to an uncertain parameter, or V1 fails. The next step is then to measure the deciding
  parameter on real data.

*Why 10 % and 3 %.* Closed circuits and dense corpora reach 21–25 %, and open national systems
2–14 %. Proposition 3 implies the value per £ cleared is roughly financing cost × lateness
gap, plus avoided default loss, i.e. low single-digit percent of the cleared amount. Below
about 3 % of a firm's book, that value cannot cover onboarding effort. At 10 % or more it is a
material share of working capital relief.

**V1 (validation gate).** Mean unweighted reciprocity of the reference networks must lie in
[1 %, 15 %]. Real production networks show 2–9 % (Bacilieri et al. 2026). If V1 fails, the
generator is unrealistic and the verdict cannot be better than REDESIGN.

**H2 (aggregation bias).** Clearability computed on the 103-sector IO network (intra-sector
flows excluded) is ≥ 2× the firm-level reference `all` value.

**H3 (recruitment strategy).** At p = 0.2, `anchor` recruitment gives ≥ 2× the φ_book of
`random`.

**H4 (predictor).** In leave-one-variant-out cross-validation over all full-participation runs
(reference + 18 variants), a logit-linear model of φ on logit(reciprocity),
logit(SCC weight share) and log(mean degree) achieves out-of-sample R² ≥ 0.7.

**Exploratory (no thresholds; reported descriptively):**
- algorithm comparison (bilateral, greedy-3, MTCS, netting bound) and participation curves;
- distribution: the share of cleared value going to small firms (outside the top 1 %) vs their
  share of participants' receivables, and median share of receivables cleared, small vs large;
- **E4 default shock:** outside liabilities = trade payables; pre-shock solvency buffers
  U(0, 30 %); 5 % of firms lose their external assets, sampled ∝ 1/√size; Eisenberg–Noe
  clearing. Reports the transfer to participants from non-participants and outside creditors
  per £ cleared, without exclusion and with an imperfect distress screen that excludes
  2× as many flagged participants as are shocked;
- descriptive comparison with the external benchmarks (Slovenia, Republika Srpska, Sardex,
  the 2026 vendor corpus). Institutional settings differ, so this is not a gate.

## 5. Variables
- **Independent:** participation share p; recruitment strategy; network parameters (sensitivity
  block); network structure (IO vs configuration null); aggregation level (firm vs sector).
- **Dependent:** φ_book, φ_internal and φ_economy for each algorithm; the netting bound;
  topology statistics; distribution metrics; default-shock losses and transfers.
- **Held fixed:** consent to all cycles among participants (non-strategic participation);
  single snapshot of obligations; no churn; no residual-settlement frictions.

## 6. Agent incentives, constraints and resource limits
Experiment 001 deliberately treats participation as exogenous and consent as universal within
P. It measures the **mechanical ceiling** of value. Strategic withholding, opt-outs by late
payers (Proposition 3) and fabricated invoices are deferred to Experiment 002. If the ceiling
fails, strategy cannot rescue it. Resources: one laptop, about 30 CPU-minutes, £0.

## 7. Statistical evaluation
30 independent seeds per cell. Each seed draws a new economy, and participation draws use an
independent stream. Seeds are BASE_SEED = 20261017 plus fixed offsets. We report the mean,
standard deviation and t-approximate 95 % CI (mean ± 1.96·SD/√30). There is one primary
decision (H1 plus the rule). H2–H4 are secondary, with fixed thresholds and no correction,
reported as such. Nothing is re-run with different seeds or parameters to change a verdict. Any
post-hoc analysis is labelled **post hoc** in the results.

## 8. Avoiding circular evaluation
- The generator is calibrated to external data (ONS IO table, Belgian degree statistics,
  Zipf firm sizes). It was not tuned to the clearing outcome, and no outcome was viewed before
  preregistration.
- The intervention is an exact optimum (an LP), not a learned or tuned rule. Nothing is fitted
  to the test.
- Held-out environments: a configuration null model, 18 sensitivity variants, and
  leave-one-variant-out prediction for H4.
- External anchors: Slovenia, Republika Srpska, Sardex and the vendor corpus are compared
  descriptively.

## 9. Failure scenarios and how they are handled
| Failure | Detection | Consequence |
|---|---|---|
| LP numerical failure | `checks_ok` false in any run | Results invalid; fix the solver and re-run all seeds (reported) |
| Generator unrealistic (too reciprocal or dense) | V1 | Verdict capped at REDESIGN |
| Results driven by closed-economy artefact | n_firms sensitivity; configuration null | Reported. If φ falls steeply with n, conclusions are labelled upper bounds |
| Real-world clearing is lower than the model (open economy, churn, disputes) | Benchmarks | Model results treated as ceilings; real-data test required before any pilot claim |

## 10. Reproduction
```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/extract_ons_iot.py          # optional: regenerate processed CSVs
.venv/bin/python -m unittest experiments.exp001_circularity.test_exp001 -v
.venv/bin/python -m experiments.exp001_circularity.run
```
Outputs: `results/exp001/runs.csv`, `defaults.csv`, `summary.json` (including git HEAD at run
time and package versions). Interpretation goes in `results/experiment-001-summary.md`, written
only after the run.

## 11. What this experiment cannot tell us
- Real UK clearability. Synthetic networks give a calibrated *ceiling and sensitivity map*,
  not a measurement.
- Strategic behaviour, consent refusals and legal enforceability.
- Willingness to adopt. That requires the real-cluster test (Stage 2).
