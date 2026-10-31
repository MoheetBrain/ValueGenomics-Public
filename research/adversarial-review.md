# Adversarial Review — steelman and destroy the three finalists

> **Historical research note (17 October 2026).** Preserved for intellectual provenance. The current programme is independent computational research; earlier product, pilot and commercial proposals below are historical options, not a business being launched. Legal, market and novelty statements are dated research assessments, not current advice or independently established priority claims. Personal goals have been omitted from this public edition; equations and scientific results are retained.


Stage B artefact · 2026-10-17 · finalists from `candidate-comparison.md` §3: **C6** Zero-Net trade-credit clearing, **C2** open compute exchange rates, **C8** agent mandate and liability layer.

Each finalist gets: the case for, the case against, adversarial strategies, distributional effects, concentration of control, behaviour under shocks, the "incumbent money plus better contracts" baseline, and the smallest decisive test.

---

## Finalist C6 — Zero-Net: consent-based, custody-free multilateral trade-credit set-off (UK)

### Case for success
1. **The welfare benefit has been measured causally, which no other candidate can claim.** Republika Srpska's statutory clearinghouse lowered firms' payment-default probability by about 6 percentage points from a mean of about 11 %. The effect was larger for distressed and cash-poor firms, and concentrated in long, complex cycles: a coordination failure that firms cannot fix alone (Božić & Zrnc 2022). Slovenia has run the mechanism for 35 years.
2. **The UK has a gap and an open policy window.** There is no UK clearing service. Late payment ties up about £26bn and is linked to about 14,000 closures a year. The Commercial Payments Bill (third reading listed 20 Oct 2026) adds mandatory statutory interest, a 60-day cap and fining powers. That makes late payment costly for large buyers, and set-off is a way to discharge debts without cash.
3. **It respects every hard constraint in `design-space.md` §5.** It creates no money or net wealth (accounting identity). It needs no price discovery (sidesteps Myerson–Satterthwaite). It holds no funds (designed outside PSRs/EMR, subject to counsel). It aggregates no preferences: each cycle is executed only with every member's consent.
4. **Solo-buildable at near-zero capital.** The optimal algorithm is a linear programme. The binding work is recruitment, legal design and trust.
5. **Scientific contribution with a clear gap.** Nobody has published a pre-registered model predicting how much of a network can be cleared. The first UK estimate and an open legal template are public goods.
6. **Option value.** The same machinery covers agent-to-agent clearing (C7) and AI-finance circularity (C12). It is also the first validated domain where Economic Genome mechanism search could be honest (C3, later).

### Case against
1. **The clearable fraction may be too small to matter.** Slovenia 2025 cleared about 2.4 % of reported obligations (14 % of those "considered"). Republika Srpska cleared about 7 % of late debt per round. Only closed circuits (Sardex 25 %) and one vendor corpus (21 %) reach double digits. If UK-like open networks sit near 2–5 %, the value per firm is small.
2. **Cold start.** Every member of a cycle must participate. With typical cycle lengths around 10, random recruitment at rate p clears roughly in proportion to p^10 (Proposition 2). Network businesses die at exactly this stage: LETS, Open Credit Network, the Bristol Pound.
3. **The firms needed to close cycles may be the ones that lose.** Large buyers that pay late earn float. Set-off accelerates their payables (Proposition 3). They are also the hubs that close many cycles.
4. **Competition.** Cycles ($8.7m raised) partners with a UK franchise (Mutual Credit Services). Accounting platforms see half of every invoice. If UK e-invoicing becomes mandatory, the invoice graph becomes machine-readable to HMRC and platforms, who could run clearing themselves. (A 2029 UK e-invoicing mandate was reported in 2025, but this audit did not verify it [U].)
5. **Legal fragility.** *British Eagle* makes pre-agreed multilateral netting void against a liquidator. Completed set-offs are exposed to s.127 (after a winding-up petition) and s.239 (preferences). The FCA judges perimeter questions on substance (PERG 15.3). Sharing invoice data between competitors raises competition-law questions. Invoice data is personal data for sole traders (UK GDPR).
6. **Revenue ceiling.** At a fee of 0.1–0.5 % of value set off, revenue scales with cleared volume. If cleared volume is a few percent of participants' trade credit, a large customer base is needed before revenue is meaningful.

### Adversarial strategies and defences

| Attack | Mechanism | Who is harmed | Defence (design requirement) |
|---|---|---|---|
| **Fabricated-edge laundering** | An insolvent firm B and an accomplice A fabricate "B owes A" to close a cycle with real debts C owes B and A owes C. Clearing uses B's real receivable from C to extinguish the fake debt. | B's other creditors (estate assets diverted). Net positions of honest members are unchanged, so they don't notice. | Both parties confirm every obligation. Invoice evidence (VAT records, e-invoice IDs). Edges between connected parties excluded or capped. Solvency and petition screening (Gazette). Clawback terms. |
| **Cycle manufacturing for float** | A large firm invents trades to pull its receivables forward | Counterparties' float | Only genuine, confirmed, due or near-due invoices are eligible. Per-cycle consent lets anyone opt out. |
| **Free-riding / strategic withholding** | Firms submit only receivables they are worried about, keeping good ones for themselves | Clearing yield | Every submitted debt can be cleared (no cherry-picking after allocation). Republika Srpska's two-round withdrawal limits this. |
| **Sybil participation** | Shell firms join to observe the graph | Privacy | Know-your-business onboarding (Companies House number, VAT number); data minimisation; privacy-preserving computation (Cycles uses TEE+ZK). |
| **Operator manipulation** | The operator biases which cycles clear (e.g., towards fee-paying members) | Members | Open, deterministic algorithm with a published objective (maximum circulation); audit log; member verification. |

### Distributional effects (to be measured, not assumed)
- **Who gains:** firms with high financing costs and late receivables, mostly small. In Republika Srpska, distressed firms gained most.
- **Who may lose:** firms that earn float by paying late (Proposition 3). Outside creditors of firms that go insolvent soon after a round (Proposition 4).
- **Experiment 001 measures:** the share of cleared value going to small firms vs their share of receivables; median receivable share cleared for small vs large firms; and the size of the outside-creditor transfer under a default shock (exploratory).

### Concentration of control
The operator sees a commercially sensitive graph: who supplies whom and on what terms. That is power over information. Mitigations, in increasing strength: data minimisation and retention limits; member-owned (cooperative) governance; federated or privacy-preserving computation where the operator never sees the full graph. The governance options are compared in `governance-and-rights.md`.

### Behaviour under shocks
- In a credit crunch, demand for clearing rises (Slovenia peaked in 2012). So do defaults, and with them the outside-creditor externality.
- In a bank or payment outage, set-off still works because it moves no money.
- If the graph churns (55 % of Hungarian supply links disappear within a year), monthly rounds must work on a moving graph. Clearing value comes from current, not historical, obligations.

### Incumbent money plus better contracts: the honest baseline
Is "sterling plus statutory interest plus 60-day caps plus supply-chain finance plus Faster Payments" better than clearing?
- **Supply-chain finance** solves the large-buyer → small-supplier leg, at a cost (the buyer's credit spread), and only where an anchor buyer exists.
- **Statutory interest and caps** shorten terms by law. They help where enforcement is credible.
- **Clearing** addresses the residual those tools miss: *cycles among firms with no anchor* and *coordination failure*.

The baseline wins if the cyclic share is small. **That is exactly what Experiment 001 measures.** If the clearable share is below 3 %, incumbent money plus better contracts dominates and C6 should be abandoned.

### Smallest decisive test
Experiment 001 (synthetic, UK-calibrated, £0, laptop): full-participation clearability, its sensitivity, the participation curve and targeting, and a validation gate. **Then** a real-data test: 30–200 consenting firms in one cluster export ledgers; measure realised clearable value of submitted debts against a preregistered threshold.

---

## Finalist C2 — Open workload-indexed compute exchange rates

### Case for success
1. Cheap, public, falsifiable, and timely. CME's futures are pending, ICE and Ornn are announced, GPU-backed lending is large, and the GPU depreciation debate is live.
2. Directly continues the user's own September thread on intelligence and compute fungibility (H-05, H-11). The correct small result (the 4-cycle bound) gives a theory hook.
3. Laptop-scale and legally trivial. It deals in data, not financial products.

### Case against
1. **Market prices are not throughput.** Rental prices reflect availability, memory, interconnect, software ecosystem, region, contract term and scarcity rents. Throughput ratios may predict them poorly for reasons unrelated to "monetary dimensionality".
2. **Data quality.** MLPerf submissions are vendor-optimised and sparse: few accelerators per benchmark, and benchmarks change each round.
3. **Value capture.** Index providers (Silicon Data with CME, Ornn with ICE, CF Benchmarks, Setara NCU™) can add workload factors faster than a solo founder can sell an index. Exchanges capture the value.
4. **Science may be anticlimactic.** If one factor explains nearly all log-throughput variance, "vector compute money" dies quietly.
5. **No institution.** It is a measurement, not a new way of organising rights, ownership or settlement. It answers the original "properties of money" question narrowly, but not the mandate's broader question.

### Adversarial strategies, distribution, control, shocks
Vendors game benchmarks, and index providers can front-run any published method. Distributional effects are minimal. Under shocks such as an obsolescence event (a new architecture), exchange rates jump, which is basis risk itself: interesting to measure, hard to sell.

### Smallest decisive test
From MLPerf v6.x, compute the k-factor variance-explained curve of log throughput. Test whether the 1-factor implied H100/B200 ratio falls within ±15 % of the published rental-index ratio. If 1 factor explains ≥95 % and the ratio test passes, the "vector" story is dead. If 1 factor explains <80 %, there is a measurable basis-risk product.

---

## Finalist C8 — Agent mandate and liability layer (user's idea)

### Case for success
1. Highest demand of any candidate. Agentic payments are being deployed by every network and the liability question is real.
2. It is the user's own strongest institutional idea (STABLECOINS L5377).
3. It fits the "incumbent money plus better contracts" thesis: no new currency, a better contract.

### Case against
1. **Incumbents allocate liability by network rule.** Visa TAP, Mastercard Agent Pay ("guaranteed multi-rail settlement" for machines, Jun 2026) and AP2 move faster than a standard set by a newcomer. Insurance-based versions need FCA authorisation and risk capital.
2. **Low science.** Least-cost-avoider liability allocation is textbook law and economics.
3. **Solo disadvantage.** Distribution means integrations with issuers, networks and agent frameworks.

### Smallest decisive test
Survey published network rules (Visa, Mastercard, AP2, ACP, x402 `auth-capture`) for agent-error liability. If every major rail allocates it, the gap is closed. If not, red-team simulated agents against three mandate-evidence schemes and measure unauthorised-spend rates.

---

## Verdict

| | C6 Zero-Net | C2 compute exchange rates | C8 liability layer |
|---|---|---|---|
| Real-world evidence of welfare benefit | **Yes (causal, RS)** | No | Indirect |
| Decisive uncertainty testable for £0 now | **Yes (Exp. 001)** | Yes | Partly |
| Legal operability without authorisation | Likely (counsel needed) | Yes | No (insurance) |
| Defensible position for a solo founder | Moderate: first UK template and data | Weak | Weak |
| Is it an economic *institution*? | **Yes**: rights, settlement, governance, enforcement | No (measurement) | Partly (contract standard) |
| Main way it dies | Low clearable share / cold start | Approximately rank-1, or incumbents | Network rules close the gap |

**C6 is selected** (`flagship-decision.md`). It is the only finalist that is an economic institution in the full sense, has causal evidence of welfare gains, and whose main risk (a clearable share too small, or recruitment too hard) can be tested immediately at no cost. Its weaknesses are stated plainly: modest novelty, a revenue ceiling, cold start and legal fragility. **C2 is the fallback** if Experiment 001 returns KILL.
