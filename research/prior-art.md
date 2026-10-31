# Prior-Art Map

Stage A artefact · 2026-10-17

This is the decision-oriented summary. The full evidence, with links, verification status
([V] checked on 2026-10-17, [K] standard citation not re-checked, [U] unverified), Slovenian
monthly data and fact checks, is in `research/audit/prior-art-verification.md`. Book-level
locations are in `research/audit/books-and-papers.md` §5.

**Rule applied:** a mechanism is not novel because it has a new name. Each row says what the
work already does, what it leaves open, and what that means for the candidates in
`candidate-comparison.md`.

---

## A. The foundations the mandate named

| Work | What it already accomplishes | Limitation that remains | Consequence for us |
|---|---|---|---|
| **Kiyotaki & Wright** (JPE 1989; AER 1993); Trejos–Wright 1995; Lagos–Wright 2005 [K] | Money arises as an equilibrium medium of exchange under double-coincidence frictions. Which object becomes money depends on storage costs and beliefs, and multiple equilibria are normal. | No record of who owes whom; no obligation networks; no clearing. | "Compute becomes money" is a KW question with a known answer. High carrying cost (compute deflation) makes a poor medium. The adoption-threshold "theorem" (H-10) is not new. |
| **Kocherlakota**, "Money Is Memory" (JET 1998); Kocherlakota & Wallace 1998 [K] | Any allocation achievable with money is achievable with a complete public record. Better record-keeping shifts the optimum from money towards credit. | Abstract. No insolvency law, network structure, partial participation or strategic withholding of records. | The theoretical warrant for clearing: an obligation ledger is "memory". **Open:** how much liquidity does a *partial*, consent-based record recover? |
| **Ljungqvist & Sargent**, *RMT* 4e (2018) | Complete markets make money redundant through multilateral netting (§8.5, §8.12). Currency has value only when private credit is restricted (ch. 28). | Textbook environments. | Same warrant from macro theory: money demand is driven by frictions that netting partially removes. |
| **Arrow** (1951/63); **Gibbard–Satterthwaite** (1973/75) [K] | No non-dictatorial aggregation rule satisfies the standard axioms; every non-dictatorial rule over 3+ options can be manipulated. | Binds less with money transfers, restricted domains or randomisation. | Any AI-governance candidate must name the axiom it gives up. Clearing needs no preference aggregation: each cycle is unanimously consented or not executed. |
| **Myerson & Satterthwaite** (JET 1983) [K]; Milgrom Thm 3.6 | No bilateral-trade mechanism is efficient, IC, IR and budget-balanced at once. | Applies where valuations are private and trade terms are being set. | Compute-rights markets and allocation designs hit it. **Clearing largely sidesteps it**: the debts and prices already exist, and net positions are preserved. |
| **Fair division**: Budish 2011 A-CEEI; Course Match 2017; DRF (NSDI 2011); Karma (OSDI 2023); Gavel (OSDI 2020); Gandiva_fair (EuroSys 2020); Shockwave (NSDI 2023) [K/V] | Pseudo-markets with equal budgets, multi-resource fairness, and credit-based allocation of compute over time. Heterogeneity-aware GPU "exchange rates" and GPU trading exist *inside one cluster*. | Inside one operator. No cross-provider, legally transferable entitlement. | Compute-entitlement candidates (C2) are novel only as an **open, cross-provider, out-of-sample** exchange-rate test. |
| **Distributed clearing and financial networks**: Eisenberg–Noe (Mgmt Sci 2001); Bech–Soramäki gridlock resolution (2001); Martin–McAndrews LSMs (JME 2008); compression (D'Errico–Roukny 2021; Schuldenzucker–Seuken 2020; Veraart 2022); BIS WP 1318 auction LSMs (Dec 2025) [K/V] | Default clearing vectors; RTGS gridlock resolution; liquidity-saving queues; compression keeping net positions fixed, with proof it is *not always* welfare-improving; auction-priced liquidity provision (79 % success on RTGS data). | Banks and derivatives dealers with central-bank money and statutory netting protection. | The **mathematics of clearing is mature**. Our contribution can only be empirical (non-bank trade credit), legal (UK SME template) or predictive (topology → clearability). |
| **Salesforce AI Economist** (Zheng et al., Sci. Adv. 2022) [V] | Two-level RL co-adapts agents and a tax planner; better equality–productivity trade-off in simulation. | Welfare depends on the simulator; agents are synthetic. | "AI designs policy" is done. Re-running it would be circular evaluation. |
| **DeepMind Democratic AI** (Koster et al., Nat. Hum. Behav. 2022) [V] | RL designs a redistribution rule that wins a human majority vote in a public-goods game. | A lab game, with majority vote as the objective. | Shows legitimacy can be an objective. Not a deployable institution. |
| **LLM / automated mechanism design**: RegretNet (Dütting et al.); Liu, Guo & Conitzer (arXiv 2502.12203, 2025); AlphaEvolve; PNAS 2025 perspective [V] | Neural and LLM-evolved mechanisms recover Myerson's auction and enforce IC/IR by a fixing step. The PNAS perspective calls the field "largely proof-of-concept". | Small settings, synthetic evaluation. | **Narrow open slot:** evolved clearing or allocation rules with hard constraints, evaluated on *real* data against strong baselines. That is a later-stage use of Economic Genome search, not the first project. |
| **Agent-payment protocols** (Oct 2026): Google AP2, OpenAI/Stripe ACP, Coinbase x402 (Linux Foundation since Jul 2026), Stripe/Tempo MPP (Mar 2026), Visa TAP, Mastercard Agent Pay for Machines (Jun 2026) [V] | Mandates proving authorisation; checkout tokens; pay-per-request; metered sessions; bilateral batch settlement (x402 `batch-settlement`, May 2026); Mastercard pairs issuer credit with Aave as a "credit layer". | **None performs multilateral netting.** AP2 leaves liability out of scope (per archive; [U]). | Agent clearing (C7) has no rival protocol, but probably no cycles either: agent spending looks hub-and-spoke. User idea H-20 (liability layer) faces Visa, Mastercard and insurance start-ups. |
| **Stochastic wealth inequality**: Bouchaud–Mézard 2000; yard-sale / affine wealth model (Boghosian et al. 2017; Li et al. 2019); Berman–Peters–Adamou [K/V] | Without redistribution, multiplicative exchange concentrates wealth (Gini → 1, "oligarchy" phase transition). Redistribution gives Pareto-tailed steady states. US estimates suggest negative effective reallocation. | Stylised dynamics. | Any equality-constitution candidate (C10) restates known phase transitions unless it brings data. Any simulation must model redistribution explicitly, or condensation is an artefact. |
| **Space law**: Outer Space Treaty 1967 Art. II; Moon Agreement 1979 (17 parties); US CSLCA 2015 §51303; Luxembourg 2017; UAE 2023 decree-law; Japan 2021; Artemis Accords (76 signatories at 25 Sep 2026) [V/K] | Territory cannot be appropriated. Ownership of *extracted* resources is recognised by five national laws and asserted by Artemis §10. The Hague group proposes a priority-rights registry. | No enforceable instrument over *future* extraterrestrial resources. No price history. | Future-resource entitlements (C5) cannot be cheaply tested. A hypothetical entitlement, a contractual claim on a venture, a right to extracted resources and territorial ownership are four different things. Only the third has legal footing, and only once resources are extracted. |

## B. Multilateral trade-credit set-off (the institution behind candidate C6)

| System / work | What it does | Measured result | Limitation |
|---|---|---|---|
| **Slovenia — AJPES multilateral set-off** (since 1991; mandatory reporting since 2011) [V] | Monthly national cycle-clearing of reported obligations; percentage fee on the amount set off | 2012: €683m (1.89 % GDP, ~14k firms). 2019: €209m (~2.7k firms). **2025 (summed from monthly reports): €57.9m set off = ≈2.4 % of €2.41bn reported, ≈14.2 % of the €408m "considered"**; ~1,000 debtors/month | Declining participation; open economy (exports ≈80 % GDP) leaks cycles |
| **Republika Srpska clearinghouse** (since 2015; Banja Luka Stock Exchange) — Božić & Zrnc 2022, CNB WP W-66 [V] | Statutory reporting of late debts; **two-round opt-out** (participants can withdraw debts after a preliminary allocation) | ≈0.6 % GDP cleared per round vs ≈9 % GDP late debt (≈7 % per round). One SCC of ≈1,000 nodes; median cycle length ≈10. **Causal: −6 pp payment-default probability** (mean 11 %), stronger for distressed firms; value concentrated in long, complex cycles | Statutory compulsion for reporting; data not public |
| **Sardex** (Sardinia) — Fleischman, Dini & Littera 2020, JRFM 13(12):295 [V] | Closed B2B mutual-credit circuit with obligation clearing | Clearing alone ≈25 % of net internal debt; ≈50 % with mutual credit as liquidity source (3,199 firms, >138k transactions) | Closed circuit whose rules push intra-network trade; authors have commercial interests |
| **Cycles Protocol** (Informal Systems spin-out, Lausanne) — arXiv 2507.22309; 2605.02436 [V] | Bilaterally approved obligations; cycle finding in a TEE with ZK proofs; atomic multilateral set-off; no novation | **No published empirical percentages.** $8.7m raised (incl. $6.4m, May 2026). Go-to-market moved crypto-first (FalconX, Lynq) plus stablecoin SME payments | Not a UK SME trade-credit service today |
| **Mutual Credit Services** (UK social franchise) [V] | Says it is building "Clearing Clubs" with Informal Systems | No volumes found [U] | Small; status unclear |
| **Open Credit Network** (UK) [V] | National mutual-credit network (≈2020) | A co-founder wrote in 2026 that it "failed" | Mutual credit, not set-off |
| **Byppay "path-enabled compensation"** — arXiv 2606.26126 (Jun 2026) [V] | Vendor preprint on 133k invoices worth €19.7bn (2021 corpus, provenance unstated) | **Cycle-only 21 %**; "path-enabled" 54 % | The 54 % redirects payments: legally an assignment or payment direction, not set-off |
| Romania Ministry of Economy app (Gavrila & Popa 2020) [V] | Government clearing tool | — | Algorithm reportedly misses cycles |
| Firm-network topology: Bacilieri et al. JEDC 2026 [V]; Bernard et al. JPE 2022 (Belgium) [V]; Hungarian VAT network [V] | Reciprocity ≈2–9 %. Belgian median suppliers 9–12, customers 4–5. Hungarian links have a 13-month half-life | — | The graph churns quickly; bilateral netting alone is small |

**What is genuinely open** (the prior-art audit's conclusion, which this programme adopts):

1. A **pre-registered, cross-dataset model that predicts the clearable fraction** from cheap
   topology statistics. Fleischman & Dini (2021) explicitly leave "significant" undefined.
2. The **first UK estimate** of clearability, on real UK invoice data from a consenting cluster.
3. An **open UK legal template** robust to *British Eagle*, s.127 and s.239 (see
   `governance-and-rights.md`).
4. A **trade-credit version of auction-priced liquidity** (BIS WP 1318 applied to near-cycles).

Not open: the algorithm, the institution, "consent-based" clearing (Republika Srpska's opt-out),
privacy-preserving clearing (Cycles), and the UK "clearing club" concept (MCS).

## C. Compute markets (candidates C1, C2)

| Item | Status Oct 2026 | Consequence |
|---|---|---|
| CME/Silicon Data H100 & B200 rental-index futures [V] | Announced for 5 Oct 2026; **postponed** ("effective date TBA"), pending CFTC. Non-tradable forward curves distributed from 15 Oct | Compute is being financialised as a **cash-settled price index**, not as money or a delivery right |
| ICE/Ornn, Architect/Ornn GPU futures; CF Benchmarks GPU series [V] | Announced or pending; perpetuals reportedly live on Architect | Crowded index-provider field |
| Setara Financial NCU™ [V] | "Pre-production" series from list prices | The "normalised compute unit" idea is taken |
| MLPerf Inference v6.x, Training v6.0 [V] | Public `summary_results.json` | Enables a cheap open test: do throughput-implied exchange rates predict rental-price ratios? |

## D. Ownership of machine output (candidate C4)

peaq Machine RWA, credit ratings and the Doosan pilot (Sep 2026) [V]; Securitize (NYSE: SECZ) [V];
ERC-8004 and ERC-8257 [V]; equipment ABS and royalty finance [K]; XMAQUINA/DEUS governance facts [V].
**Conclusion:** the rights layer (verified telemetry → servicing → enforceable, mandatorily
distributed claims) is the only open part, and it sits inside securities regulation.

## E. Agent mandate and liability (candidate C8)

AP2 mandates; Visa TAP; Mastercard Agent Pay; x402 `auth-capture`; insurance start-ups named in
the archives (Skyfire, Catena, Klaimee and others, [U]); card chargeback rules [K].
**Conclusion:** the user's idea (H-20) points at a real gap, liability allocation for agent
errors. Payment networks and well-funded start-ups are converging on it.

## F. Fact check of the pasted AI reports (summary)

| Claim (source) | Verdict | Correction |
|---|---|---|
| BoE systemic stablecoins: 40 % BoE deposits / 60 % gilts; holding limits (02) | **Outdated** | Final (22 Jun 2026): ≥30 % unremunerated deposits / ≤70 % short gilts; holding limits dropped for a £40bn issuance guardrail; **no interest to holders** |
| FCA crypto regime live Oct 2027 (02) | True | 25 Oct 2027 |
| PS23/6 cooling-off and referral ban (02) | True | — |
| PSRs LNE €1m notification (02) | True | reg 38 |
| LURA 10-year enforcement rule (02) | True (England) | in force 25 Apr 2024 |
| NPPF Aug 2026, 40 dph near hubs (02) | Partly | Final: 35–45 dph near qualifying stations |
| Private credit "$1.96tn in 2026" (02) | Unverified / misleading | Quote $1.7–2.3tn with its definition |
| Shor on secp256k1 needs ≈1,200–1,450 logical qubits; FIPS 203/204/205 (02) | True | — |
| "MTCS reduces ≈25 % of debt"; Sardex velocity 5× (02) | **False / inaccurate** | 25 % is Sardex only; Slovenia ≈2.4 % of reported. Velocity ≈8× (self-reported) |
| Credit Commons 2016 (Slater & Jenkin); OCN founders (02) | True / partly | OCN "failed" (2026) |
| BIS Dec 2025 auction-LSM paper; BIS unified ledger (03) | True | WP 1318 |
| CME GPU futures "pending regulatory review" (04) | True and postponed | 5 Oct date withdrawn 25 Sep 2026 |
| "Preliminary differentiable models identified a hybrid UBS+auction optimum" (02) | **Fabricated** | No models were run |
