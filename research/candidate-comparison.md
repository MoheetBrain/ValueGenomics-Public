# Candidate Comparison — twelve flagship candidates

> **Historical research note (17 October 2026).** Preserved for intellectual provenance. The current programme is independent computational research; earlier product, pilot and commercial proposals below are historical options, not a business being launched. Legal, market and novelty statements are dated research assessments, not current advice or independently established priority claims. Personal goals have been omitted from this public edition; equations and scientific results are retained.


Stage B artefact · 2026-10-17 · inputs: `original-ideas.md`, `prior-art.md`, `design-space.md`

Twelve substantially different candidates are assessed: the ten suggested directions plus two that came out of the source material. Each is stated as an institution in the extended ontology M = (R, O, A, G, S, E, I, P, T). No probabilities of success are given; the mandate forbids fabricated ones. §3 gives the Pareto analysis, computed by `scripts/pareto_candidates.py`.

---

## 1. The candidates

### C1 — Compute-denominated money (compute reserve unit / redeemable compute coin)
- **Unsolved problem claimed:** agents need a unit tied to the resource they consume. Hedge AI-capital depreciation.
- **Existing best solution:** stablecoins and fiat for payment; prepaid credits and reservations for capacity; rental-index futures (pending) for price risk.
- **Proposed innovation:** a transferable claim on q units of standardised compute, used as money.
- **Why it might be new:** it is not new. Setara NCU™, ICP cycles, AWS ECU and Aethir/io.net-style tokens all exist.
- **First proposition (kill result) — compute deflation.** Let a claim entitle its holder to q units of standard compute at any future date, and let compute prices fall at rate g relative to the general price level. Price-performance gains have historically been tens of percent a year. The claim's real purchasing power falls at rate g, while sterling's falls at inflation π. A risk-neutral holder prefers sterling whenever g > π. In Kiyotaki–Wright terms, g is a carrying cost, and high-carrying-cost goods lose the medium-of-exchange role to low-cost ones. Rebasing the unit to hold its value makes it a fiat-indexed unit, which brings back the incumbent money. So a compute claim can be a *product* (a prepaid service or capacity right) but not a store of value. ∎ (elementary; INFERENCE from KW89)
- **Cheapest decisive experiment:** none needed beyond the proposition and a check of the rental-price index trend (falling H100 rental rates are on record).
- **Data / compute:** public GPU rental indices. £0.
- **Obstacles:** UK financial promotions (PS23/6), DSA rules, cold start.
- **Users:** none identified who prefer it to stablecoins (Coinbase reports agent payments are overwhelmingly USDC; unverified).
- **Commercialisation:** spread on token trading. Regulatory exposure.
- **Why it may never work:** the proposition above.
- **Earliest falsifier:** already falsified as a store of value.

### C2 — Open workload-indexed compute exchange rates (compute basis-risk measurement)
- **Problem:** single-chip rental indices (Silicon Data H100) hedge workload costs only as well as hardware is fungible across workloads. Basis risk is unmeasured publicly.
- **Existing best solution:** proprietary indices (Silicon Data, Ornn, CF Benchmarks, Setara NCU™). Heterogeneity-aware exchange rates exist inside single clusters (Gavel, Gandiva_fair).
- **Innovation:** an open, reproducible exchange rate between accelerators per workload class, derived from MLPerf throughput. It would be tested out of sample against market rental-price ratios, and would give the "monetary dimensionality" of compute (H-11).
- **Why it might be new:** being open, plus the out-of-sample test. The maths is not new.
- **First proposition:** a scalar compute unit is exact iff the throughput matrix P has rank 1. Any scalar unit has worst-case log-pricing error E ≥ ¼·max over 2×2 minors of |log cross-ratio| (archive result, verified correct).
- **Cheapest decisive experiment:** build P from MLPerf Inference v6.0/6.1 `summary_results.json`. Compute ε_k for k = 1, 2, 3 factors. Test whether k = 1 throughput ratios predict the H100/B200 rental-price ratio (Silicon Data / CME forward curves) within a preset error band.
- **Data / compute:** public MLPerf JSON; published index prints. Laptop. £0.
- **Obstacles:** vendor-optimised submissions; few accelerators per benchmark; prices are quoted per GPU-hour, not per throughput; index data licensing.
- **Users:** compute buyers, GPU-backed lenders, index providers, exchanges.
- **Commercialisation:** data product or licensing to index providers. Consulting on GPU collateral basis risk.
- **Why it may never work:** if rank-1 holds approximately (one factor explains nearly all variance), the "vector compute money" idea dies and only a commoditised index remains. If it fails, incumbents can add factors faster than a solo founder can sell.
- **Earliest falsifier:** a single factor explains ≥ 95 % of log-throughput variance, and MLPerf ratios track rental ratios within the noise.

### C3 — AI-designed allocation and governance engine ("Economic Genome search" as the product)
- **Problem:** institutions are designed by hand.
- **Existing best solution:** AI Economist, Democratic AI, RegretNet, LLM-evolved mechanisms (Liu–Guo–Conitzer 2025).
- **Innovation claimed:** search over the full institution genotype.
- **Why it might be new:** not, at the method level. Only evaluation on real data with hard constraints is open.
- **First proposition:** none distinctive. Arrow and Gibbard–Satterthwaite bound the objective.
- **Cheapest decisive experiment:** evolve a rule in one domain and test it on held-out real data against the best human baseline.
- **Data / compute:** needs a real-data domain first. Without one, evaluation is circular.
- **Obstacles:** circularity (Lucas critique), compute cost (the source report proposed £10k of GPU), no buyer.
- **Users / commercialisation:** academic; none commercial near-term.
- **Why it may never work:** search without a validated environment optimises simulator artefacts.
- **Earliest falsifier:** the evolved rule fails to beat a simple baseline on held-out data.
- **Note:** this is the *right later stage* for the Economic Genome engine, once one domain has validated data (see §4).

### C4 — Enforceable claims on machine output (robot/agent revenue rights + rights-audit standard)
- **Problem:** tokenised "ownership" of robots and agents often confers no enforceable claim (the DEUS case: discretionary 40 % distributions, circular NAV, top-10 voters cast 61 %).
- **Existing best solution:** equipment ABS, royalty finance, peaq Machine RWA and credit ratings, Securitize, the UK Digital Securities Sandbox.
- **Innovation:** a minimum-covenant rights standard: mandatory distribution, redemption, anti-capture quorum, verified telemetry for servicing.
- **Why it might be new:** as a public audit standard for tokenised productive assets. The instruments themselves are not new.
- **First proposition:** a claim's value is bounded by its enforceable cash-flow right ("reference ≠ ownership"). Discretionary distributions are worth at most the governance-controlled payout.
- **Cheapest decisive experiment:** rights-audit 20 live tokenised machine/agent offerings and see whether the rating predicts price-to-NAV discounts.
- **Data:** public documents and on-chain data. Low cost.
- **Obstacles:** securities law (specified investments); a solo founder cannot issue.
- **Users:** investors, regulators, sandbox participants.
- **Commercialisation:** ratings or audits. Small market.
- **Why it may never work:** the market is microscopic (archive: "only 48 historical runs" of agent NFTs). Incumbent rating agencies would own any standard that mattered.
- **Earliest falsifier:** audit ratings do not explain price discounts.

### C5 — Contingent future-resource entitlements (lunar He-3, asteroid metals, priority rights)
- **Problem:** financing long-dated extraction ventures.
- **Existing best solution:** offtake contracts (Interlune–Bluefors up to ≈1.3 kg/yr; DOE 3 litres), equity, NASA regolith purchases.
- **Innovation claimed:** tradable claims on future extraterrestrial resources.
- **Why it might be new:** no source analyses tradable future-resource claims (books audit §3.4).
- **First proposition:** the four-way distinction. A hypothetical entitlement, a contractual claim on a venture, a right to extracted resources, and territorial ownership have different enforceability. OST Art. II bars the last, and national laws (US/LU/JP/UAE) grant the third only *after* extraction.
- **Cheapest decisive experiment:** none cheap. There is no price history and no deliverable asset.
- **Obstacles:** enforceability, decade-scale horizons, securities law.
- **Users:** space ventures, speculative investors.
- **Commercialisation:** structuring fees, far off.
- **Why it may never work:** the asset does not exist yet.
- **Earliest falsifier:** n/a. Cannot be tested by July 2027.

### C6 — **Zero-Net: consent-based, custody-free multilateral trade-credit set-off for UK SMEs**, built on a pre-registered science of clearability
- **Problem:** about £26bn of late payments is outstanding to UK small firms at any time. Late payment is linked to about 14,000 closures a year and costs about £11bn a year (DBT/London Economics, July 2025). Invoices are paid one by one, so a chain of firms each waiting for the next is stuck even when the debts form a loop.
- **Existing best solution:** abroad, statutory national clearing exists (Slovenia since 1991; Republika Srpska since 2015, with causal evidence of −6 pp default probability) and closed mutual-credit circuits (Sardex). Cycles is crypto-first. **There is no UK service.** In the UK the alternatives are invoice finance, which costs money, and statutory late-payment interest, which is rarely claimed.
- **Innovation:** (i) a UK institution executing per-cycle, consent-confirmed set-off among solvent participants. It holds no funds, creates no money and extends no credit, so it is designed outside the PSRs/EMR perimeter (subject to counsel). (ii) A legal template robust to *British Eagle*, s.127 and s.239. (iii) The science: what fraction of a network can be cleared, how it depends on topology and participation, and how to recruit so that cycles exist.
- **Why it might be new:** the mechanism is **not** new. New elements would be the first UK implementation and legal template, and the first pre-registered cross-dataset predictor of clearability (an open gap per the prior-art audit).
- **First propositions:** P1–P4 in `experiment-001-spec.md` §3: the netting-liquidity equivalence, the p^|C| cold-start bound, the no-free-money identity with its individual-rationality problem for late payers, and the British Eagle externality formula.
- **Cheapest decisive experiment:** Experiment 001, a UK-input-output-calibrated synthetic firm network. It measures the clearable fraction under realistic participation and validates against Slovenia, Republika Srpska and Sardex figures. Then a real-data test on one consenting UK cluster.
- **Data / compute:** ONS 2023 IO tables (public); a laptop; £0. Real data later: ledger exports from about 30–200 consenting firms.
- **Obstacles:** cold start (network effects); data access; legal (*British Eagle*, preferences, perimeter); competition law on information sharing (see `governance-and-rights.md`).
- **Users:** SME clusters (trade associations, construction supply chains, local-authority supplier bases), accountants and bookkeepers, large buyers facing the Commercial Payments Bill.
- **Commercialisation:** a percentage fee on value set off (AJPES charges one), or a subscription. Channels: accounting-software marketplaces (Xero, Sage, QuickBooks), trade bodies, councils.
- **Why it may never work:** clearable fractions in open economies are low (Slovenia ≈2.4 % of reported). Participation is the binding constraint. Large late payers lose float (P3).
- **Earliest falsifier:** Experiment 001 shows full-participation clearability below 3 % in UK-calibrated networks; or a real cluster clears below 3 % of submitted value.

### C7 — Agent-to-agent mutual credit and clearing network
- **Problem:** pre-funding machine-to-machine payments ties up capital.
- **Existing best solution:** x402 batch-settlement (bilateral escrow channels), MPP sessions, issuer credit (Mastercard + Aave).
- **Innovation:** multilateral netting and limited credit among verified agents.
- **Why it might be new:** no agent protocol nets multilaterally (verified).
- **First proposition:** shared with C6. The extra agent-specific piece is that reputation-only enforcement fails under cheap pseudonyms (Friedman–Resnick 2001), so credit needs stake or legal identity.
- **Cheapest decisive experiment:** simulate or trace agent obligation graphs and measure cyclicity. The prior expectation is hub-and-spoke (agents pay tool and API providers), which means low cyclicity.
- **Data:** no public agent transaction traces (x402 on-chain data is a possible proxy).
- **Obstacles:** no market at scale (x402 ≈ $0.30 per transaction average by April, per archive).
- **Users:** none at scale yet.
- **Commercialisation:** protocol fees, unlikely before 2028.
- **Why it may never work:** agent economies may not generate cycles.
- **Earliest falsifier:** on-chain x402 graphs show cyclic share below 5 %.
- **Relation to C6:** C6 dominates on evidence. It shares the mathematics and adds a real market. C7 is C6's option value.

### C8 — Agent mandate and liability layer (the user's idea H-20)
- **Problem:** when an authorised agent buys the wrong thing, who bears the loss? AP2 leaves liability out of scope (per archive).
- **Existing best solution:** card chargeback rules, Visa/Mastercard agentic-token rules, AP2 mandates, agent insurance start-ups.
- **Innovation:** a cross-rail standard for evidence of authorisation type (human-authorised vs agent-chosen), with refund and insurance backing priced on that evidence.
- **Why it might be new:** the liability-pricing piece is plausibly open; the mandate piece is not.
- **First proposition:** with per-transaction loss probability p and loss ℓ, an insurer breaks even at premium ≥ p·ℓ plus loading. Mandate evidence is valuable insofar as it lowers p or shifts liability to the party best able to prevent the loss (the least-cost avoider, an established principle of law and economics).
- **Cheapest decisive experiment:** red-team simulated agents against mandate schemes and measure unauthorised-spend rates by scheme.
- **Data:** synthetic. Real loss data belongs to the networks.
- **Obstacles:** incumbents set liability by network rule. Insurance needs FCA authorisation.
- **Users:** merchants, agent developers, issuers.
- **Commercialisation:** standards body or an insurance MGA. Capital heavy.
- **Why it may never work:** Visa and Mastercard allocate liability by rule before any start-up can.
- **Earliest falsifier:** network rules (already announced) allocate agent-error liability, leaving no gap.

### C9 — Economic Failure Atlas (singularity detector)
- **Problem:** financial arrangements fail at discontinuous boundaries (leverage → ∞ as equity → 0).
- **Existing best solution:** stress testing, Eisenberg–Noe, systemic-risk literature.
- **Innovation:** real-time boundary detection for autonomous agents.
- **Why it might be new:** weakly. It is applied systemic-risk work.
- **First proposition:** L = A/(A−D) diverges as A→D (trivial).
- **Cheapest decisive experiment:** compare boundary-aware vs standard stress tests on synthetic portfolios.
- **Obstacles / users:** no buyer. Synthetic only.
- **Why it may never work:** incumbent risk systems already do this.
- **Earliest falsifier:** no lead-time advantage over standard stress tests.

### C10 — Constitutional equality mechanism (citizen equity stake in automated capital)
- **Problem:** AI may collapse the labour share (Trammell–Korinek 2026), concentrating income in capital owners.
- **Existing best solution:** sovereign wealth funds (Norway, Alaska dividend), Windfall Clause proposals, taxes.
- **Innovation:** an equity-stake rule (a share η of new automated capital to a citizens' fund) sized to keep the wealth distribution stationary.
- **Why it might be new:** the sizing rule may be new as a calibration. The phase-transition mathematics is known (yard-sale, Bouchaud–Mézard).
- **First proposition:** in a reallocating geometric Brownian motion, a stationary distribution exists iff the reallocation rate is above zero. The equity-stake rate maps to a reallocation rate.
- **Cheapest decisive experiment:** calibrate to ONS wealth data. Simulate inequality paths under η.
- **Obstacles:** political legitimacy, not mathematics. No customer. A solo founder cannot implement it.
- **Why it may never work:** it is a policy proposal, not a buildable institution.
- **Earliest falsifier:** n/a commercially.

### C11 — Credit–intelligence race model (user idea H-13)
- **Problem:** can debt-financed AI capex become self-financing before funding runs out?
- **Existing best solution:** Caballero 2026 (speculative growth leaves a capital legacy), Van Nieuwerburgh 2026, Kiyotaki–Moore.
- **Innovation:** explicit maturities, GPU obsolescence and correlated collateral recovery.
- **Why it might be new:** narrowly, as a calibrated vintage-collateral model.
- **First proposition:** the capital-maintenance threshold q ≥ c + δ/s + (r+μ)D/K (archive, correct).
- **Cheapest decisive experiment:** calibrate on public hyperscaler and neocloud filings.
- **Obstacles:** prior art; motivated-reasoning risk (audit D2).
- **Users / commercialisation:** research and commentary only.
- **Earliest falsifier:** the model adds nothing beyond Caballero's mechanism.

### C12 — Circular AI-finance compression map (new connection: clearing mathematics × AI capex circularity)
- **Problem:** 55.2 % of incoming investment in AI firms comes from other AI firms (BIS Bulletin 137). Gross headline commitments overstate net external funding.
- **Existing best solution:** BIS aggregate statistics; journalistic deal maps.
- **Innovation:** apply maximum-circulation compression (the C6 mathematics) to the network of announced AI compute, chip and cloud commitments to estimate the circular share and the net external funding need.
- **Why it might be new:** the application appears unpublished. It is timely.
- **First proposition:** the same as C6 P1. Net positions are invariant, and the cyclic share measures self-referential financing.
- **Cheapest decisive experiment:** hand-build the commitment graph from public announcements. Compute the circulation share. Compare with the BIS figure.
- **Obstacles:** commitments are conditional and opaque (amounts, timing, optionality).
- **Users:** researchers, journalists, macroprudential analysts.
- **Commercialisation:** low (reputational, consulting).
- **Why it may never work:** announced figures are not enforceable obligations, so "clearing" them is metaphorical.
- **Earliest falsifier:** the circular share is insensitive to the data and adds nothing to the BIS figure.

---

## 2. Two separate objectives

Ratings are ordinal (1 low, 2 medium, 3 high). For capital, 3 means little capital is needed. For time to revenue, 3 means fast. The full matrix, with the rationale encoded, is in `scripts/pareto_candidates.py`.

| | Nov | Fals | Tract | Expl | EmpVal | Sig | Demand | Legal | Solo adv. | TTR | Distrib. | Capital | Upside |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 compute money | 1 | 3 | 3 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 |
| C2 compute exchange rates | 2 | 3 | 3 | 2 | 3 | 2 | 2 | 3 | 1 | 2 | 2 | 3 | 2 |
| C3 AI governance engine | 1 | 2 | 1 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 2 |
| C4 machine-output rights | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 3 |
| C5 future-resource claims | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 3 |
| **C6 Zero-Net clearing** | 2 | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | **1** | 3 | 2 |
| C7 agent clearing | 2 | 3 | 3 | 2 | 1 | 2 | 1 | 2 | 2 | 1 | 1 | 3 | 2 |
| C8 agent liability layer | 1 | 2 | 2 | 1 | 2 | 1 | 3 | 2 | 1 | 2 | 2 | 2 | 3 |
| C9 failure atlas | 1 | 2 | 2 | 2 | 2 | 1 | 1 | 3 | 1 | 1 | 1 | 3 | 1 |
| C10 equality constitution | 1 | 2 | 3 | 2 | 2 | 3 | 1 | 1 | 1 | 1 | 1 | 3 | 1 |
| C11 credit–intelligence race | 1 | 2 | 3 | 2 | 2 | 2 | 1 | 3 | 1 | 1 | 1 | 3 | 1 |
| C12 AI-finance compression | 2 | 3 | 3 | 2 | 2 | 2 | 1 | 3 | 2 | 2 | 2 | 3 | 1 |

C6's weakest cell is **distribution**: the cold-start problem. Experiment 001 is designed to measure exactly that weakness.

## 3. Pareto analysis (no weights)

Output of `python3 scripts/pareto_candidates.py`:

1. **Full 13-criterion dominance.** The frontier is {C2, C4, C5, C6, C8, C10, C12}. C1, C3, C7, C9 and C11 are each dominated. C7 is dominated by C6: it has the same mathematics and C6 is better on empirical validation, demand and time to revenue.
2. **Two-objective dominance, aggregating each objective by its median** (weight-free): C6 = (3.0, 2.0) is the **unique** non-dominated candidate.
3. **Same with mean aggregation:** the frontier is {C6 (2.67, 2.00), C2 (2.50, 2.14)}. C2 edges C6 on economics because its distribution is easier and it is fully legally operable. C6 edges C2 on science because its explanatory power is larger.

**Robust conclusion:** C6 is on every frontier. C2 is the only alternative that survives an aggregation choice. C8 survives full-vector dominance only through its demand and upside cells. It is kept as the third finalist because it is the user's own strongest idea, and because it stands for the important "incumbent money + better contracts" alternative. Finalists: **C6, C2, C8** (`adversarial-review.md`).

## 4. What the comparison says about the original "Economic Genome" ambition

- **Kill results.** Compute money (C1) fails a one-line carrying-cost argument. Future-resource claims (C5) cannot be tested before 2027. The AI governance engine (C3) is circular until a domain has validated data.
- **The engine has a place, later.** It belongs at the stage where a validated environment exists, and the clearing domain is one: real obligation graphs, hard constraints (net-position preservation, consent, solvency screening) and an exact optimum (max-circulation) as the baseline to beat. If C6 survives its data test, constrained mechanism search over *clearing rules* becomes the first honest use of the Economic Genome engine. Examples of such rules: who to include, how to price liquidity for near-cycles, how to share fees.
- **The shift in centre of gravity is supported by the evidence:** from "a better currency" to "a better way to discharge obligations in the existing currency" (`design-space.md` §6).
