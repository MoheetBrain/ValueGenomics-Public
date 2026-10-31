# Final Decision Memo — Economic Genome

> **Historical research note (17 October 2026).** Preserved for intellectual provenance. The current programme is independent computational research; earlier product, pilot and commercial proposals below are historical options, not a business being launched. Legal, market and novelty statements are dated research assessments, not current advice or independently established priority claims. Personal goals have been omitted from this public edition; equations and scientific results are retained.


**To:** Moheet · **From:** Claude Code (research director role) · **Date:** 2026-10-17
**Basis:** Stages A–E in this repository. Preregistration commit `fc2561e`. Results in
`results/experiment-001-summary.md`.

---

### THE PROJECT — what exactly should I build?
**Zero-Net** (working name): a UK clearing institution for business debts. Members connect
their unpaid invoices. The system finds loops of debt (A owes B owes C owes A). Each firm
confirms its own part, and the loop is cancelled by legal set-off.
- No money moves, no funds are held, no credit is extended, no token exists.
- Whatever remains is paid normally in pounds, in an order that needs the least cash.

The first build is **not** an app. It is a real-data clearing study with one anchor-led
cluster of 30–200 UK firms, plus a counsel-reviewed legal template.

### THE DISCOVERY — what is the potentially new economic principle?
**Circularity principle** (stated as a hypothesis; the mathematics is standard, the measurement
is new). Money is needed to settle business-to-business obligations only for the *acyclic* part
of the obligation network. The cyclic part is a coordination failure that an information
institution can remove without money or credit. This is Kocherlakota's "money is memory" made
operational.
- **Proposition 1:** custody-free set-off plus correctly sequenced payment needs exactly the
  cash a central counterparty would need. Clearing-house efficiency without a clearing house.

What is genuinely new is empirical:
- the first UK-calibrated measurement of how much trade credit is circular;
- proof that **who you recruit matters more than how many**: anchor clusters clear 6–27× more
  than random recruits of the same size;
- the finding that cheap network statistics do *not* yet predict clearability (out-of-sample
  R² 0.37). The prediction problem remains open.

### THE MATHEMATICS — what should I formulate?
1. **Clearing:** maximise Σc subject to Bc = 0 and 0 ≤ c ≤ f (bounded maximum circulation;
   an LP).
2. **Four propositions, proved:**
   - P1: netting-liquidity equivalence;
   - P2: cold start decays like p^|cycle|;
   - P3: no wealth is created, and late payers lose float, so participation can fail to be
     voluntary for them;
   - P4: the *British Eagle* transfer from a failing firm's outside creditors.
3. **Next optimisation problem: constrained clearing design.** Maximise cleared value subject
   to: circulation; per-cycle consent; each member's gains covering any float it loses;
   exclusion of firms at risk of insolvency; and, as a redesign option, priced liquidity for
   near-cycles. This is the first domain where an Economic Genome mechanism search can be
   evaluated honestly: real data, hard constraints, an exact baseline.

### THE INSTITUTION — how are rights, money, ownership, governance and enforcement connected?
- **Rights / ownership:** the resource is existing trade receivables, which members own. The
  only right created is a per-round contractual set-off, executed cycle by cycle.
- **Money:** sterling stays the unit and settles residuals. Zero-Net changes only how debts
  are discharged, not what money is.
- **Governance:** an operator company with binding member protections:
  - an open, deterministic algorithm;
  - a member council with veto over consent, eligibility, data and fees;
  - a full audit log;
  - a fee cap.
  This is the only model compatible with founder ownership. A cooperative has more
  legitimacy; the trade-off is stated.
- **Enforcement:**
  - A completed set-off is a legal discharge.
  - Residual debts are enforced as usual, with statutory interest.
  - Insolvency is handled by screening out petitioned or insolvent firms before each round
    (s.127) and by never carrying obligations forward (*British Eagle*).
  - Fraud is countered by two-sided confirmation, invoice evidence and exclusion of connected
    parties.

Full analysis: `research/governance-and-rights.md`.

### THE EXPERIMENT — what can we test immediately?
Experiment 001 has been run. Its preregistered verdict is **CONTINUE**:
- full participation clears 51.7 % of trade-credit books;
- an anchor cluster of 20 % of firms clears 30.9 %;
- both hold in every sensitivity variant.

**But that is a model ceiling about 2× the best real-world figures (21–25 %).** Under a
calibration that matches real levels by reducing hub concentration, small anchor clusters clear
only 1–6 %. Belgian network data favour the other explanation (frictions, with topology
correct), which would put a 20 % anchor cluster near 13–15 %.

**The immediate test is therefore real data.** One anchor firm and its counterparties export
their open invoices, under an NDA and a data-protection impact assessment. Measure:
- (a) the realised clearable share of submitted value;
- (b) hub concentration;
- (c) the share of invoices simultaneously outstanding.

Preregister before receiving the data:
- abandon if < 3 % of submitted value clears;
- continue to a live pilot if ≥ 10 %;
- otherwise test liquidity-assisted clearing (Experiment 002).

### THE COST — what is the minimum capital required for decisive evidence?
- **Experiment 001:** £0 (laptop, public ONS data).
- **Real-data study:** about **£0–£3k**. The founder's time for anchor outreach, plus an
  optional fixed-fee legal opinion on the set-off template and perimeter (budget from about
  £1.5k; a quote is needed). There is also a free UK Data Service registration for the public
  Sarafu transaction dataset, as a secondary real-network test.
- No borrowing, no leverage, no token, no paid infrastructure. Nothing here needs more than
  this until the real-data gate is passed.

### THE OPPORTUNITY — what could make the result important?
- **Scientific:**
  - the first UK estimate of circular trade credit;
  - the first evidence that recruitment structure dominates participation rate;
  - an open legal design for consent-based clearing under English insolvency law;
  - a validated domain for constrained mechanism search.
  All of these are publishable even if commercialisation fails.
- **Commercial:**
  - about £26bn of late payments is outstanding to UK small firms;
  - the Commercial Payments Bill (third reading listed 20 Oct 2026) makes late payment costly
    for large buyers;
  - no UK clearing service exists;
  - abroad, the Republika Srpska clearinghouse cut default probability by about 6 pp.
  - Revenue would be a small fee on value cleared. The ceiling is modest unless adoption is
    national.
- [Personal objective and deadline omitted from this public edition.]

### THE FAILURE — what would prove this project was a bad choice?
Any one of:
- (a) a real anchor cluster of ≥ 30 firms clears **< 3 %** of submitted invoice value;
- (b) **no anchor firm** agrees to share invoice data within 3 months of structured outreach;
- (c) counsel or the FCA concludes the service is a **regulated payment service** that a solo
  founder cannot run, or that the per-cycle design does not survive *British Eagle*;
- (d) Cycles (or an accounting platform) launches UK SME clearing first, with anchor
  partnerships we cannot match.

**Fallback if Zero-Net dies:** C2. An open MLPerf-derived compute exchange rate, tested out of
sample against GPU rental-index ratios. Cheap and falsifiable, but a measurement rather than an
institution.

### THE NEXT ACTION — what exact task should be executed first?
**Identify one anchor firm and request a single invoice-ledger export from it and its direct
counterparties.**
- The best candidates are a south-London main contractor with an active subcontractor base, or
  a council's top-200 suppliers via its procurement team.
- Before any data arrives, write and commit `experiments/experiment-002-spec.md`:
  - the real-data protocol (fields: invoice ID, debtor and creditor Companies House numbers,
    amount, due date, status);
  - the DPIA outline;
  - the preregistered thresholds (< 3 % kill, ≥ 10 % continue).

In parallel, and at no cost: register with the UK Data Service and download the public Sarafu
dataset. Run the existing clearing code on it as the first *real* transaction network, as a
check on the synthetic results.

---
*No probabilities of success are stated anywhere in this memo, by design. Every number above is
either a measured model output with its confidence interval, a cited external figure, or
labelled post-hoc arithmetic.*
