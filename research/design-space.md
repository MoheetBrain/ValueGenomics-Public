# Design Space — redefining the Economic Genome

Stage A/B artefact · 2026-10-17 · author: Claude Code (research director role) for Moheet

Evidence tags used throughout: **[EST]** established result in credible literature (citation in
`research/prior-art.md`); **[INF]** inference from combining established results; **[HYP]** new
hypothesis needing independent verification; **[USER]** / **[ASSIST]** origin of an idea (see
`research/original-ideas.md`).

---

## 1. Why the original "genome" was the wrong unit of analysis

The programme began **[USER]** by asking whether every monetary instrument could be written as a
high-dimensional property vector (scarcity, stability, acceptance, liquidity, trust, governance,
enforceability …), and whether AI could search that vector space for better money. An earlier
assistant expanded this to 99 properties in eight families **[ASSIST]**
(`sources/pasted/2026-10-16_04_economic-genome-reconstruction.md` §4).

That framing has three defects. The first two are fatal for a discovery engine:

1. **The properties are outputs, not inputs.** Liquidity, acceptance and stability are not
   chosen by a designer. They are equilibrium outcomes of rules interacting with other people's
   beliefs. An object becomes a medium of exchange because others expect it to be accepted
   (Kiyotaki–Wright 1989 **[EST]**). Searching over outcome vectors invites designs that are not
   implementable: the search can "choose" high acceptance, which nobody can do. A genome should
   encode what a designer *can* set (the genotype). The observed properties (the phenotype) come
   from the genotype together with the environment.
2. **The sample is tiny and selected on the outcome.** About 100 historical currencies, labelled
   success or failure after the fact, cannot identify the causal effect of 99 features.
   Any classifier trained on that data measures retrospective correlation. The source mandate
   itself notes the risk (`sources/pasted/2026-10-17_02_…` §5, Experiment A).
3. **Money is only one of the institutions that move resources.** The same economic job can be
   done by money, by credit, by record-keeping with enforcement (Kocherlakota 1998, "money is
   memory" **[EST]**), by clearing (cancelling offsetting obligations), or by non-market
   allocation. A genome restricted to "currencies" cannot find the cheapest institution for the job.

**Redefinition:** the unit of analysis is an **institution**: a set of rules about claims on
resources. Instruments such as coins, tokens and deposits are artefacts that some institutions produce.

## 2. The extended ontology  M = (R, O, A, G, S, E, I, P, T)

The mandate's six dimensions are kept. Three are added, because every serious failure in the
source material traces back to one of them.

| Dim | Name | Question it answers | Why it is needed |
|---|---|---|---|
| **R** | Resources & claims | What exists, and what claims on it can be created? | Separates the thing (a GPU, a kWh, an invoice) from the right to it (a reservation, a future, a receivable). |
| **O** | Ownership | Who holds each claim? Can it be transferred, split or pledged? | Transferability and pledgeability decide whether a claim can circulate or back credit. |
| **A** | Allocation | Who gets what: price, queue, lottery, entitlement, plan, or a mix? | Myerson–Satterthwaite **[EST]** limits efficient voluntary allocation under private information. |
| **G** | Governance | Who changes the rules, by what procedure, and how fast? | Arrow / Gibbard–Satterthwaite **[EST]** limit aggregation. Rule change is also the main attack surface. |
| **S** | Settlement | How are obligations discharged: money transfer, set-off, delivery, or forgiveness? | Discharging without moving money (set-off, netting) is a separate design dimension from issuing money. |
| **E** | Enforcement | What happens on breach, default or dispute, and who has authority? | Without enforcement, records cannot replace money (Kocherlakota) and credit collapses (LETS free-riding). |
| **I** | Information & records **(new)** | What is recorded, who can see it, and how it is verified. | "Money is memory" **[EST]**: the ledger is the real primitive. Privacy, auditability and verification costs live here. |
| **P** | Participation, entry & exit **(new)** | Who may join or leave, at what cost, and with what identity? | Adoption thresholds, Sybil attacks, adverse selection and cold start all sit here. Most historical failures are P-failures. |
| **T** | Time & dynamics **(new)** | Maturities, payment terms, update rules, and the response to shocks. | Obligations have dates. Late payment, maturity mismatch, rebasing and death spirals are T-phenomena. |

Distribution is not a separate genotype dimension. It is a **phenotype**: the joint result of
O, A, S and E. It must be measured on six separate axes, as the mandate requires: wealth,
income, access, opportunity, ownership and political power. An institution can improve one and
worsen another.

### The environment  e = (Tech, Phys, Law, Demand, Network)

- **Tech:** verification costs, communication and computation.
- **Phys:** finite energy, land, compute, manufacturing capacity and time.
- **Law:** which claims are enforceable, where, and against whom (insolvency law decides what
  survives a default).
- **Demand:** heterogeneous preferences. No single welfare function is imposed.
- **Network:** who already trades with whom. The existing trade graph is the most
  under-used input in the source material.

### The phenotype (what we measure, never what we choose)

Efficiency (welfare, deadweight loss, liquidity needed), stability (behaviour under shocks),
distribution (the six axes), adoption (voluntary participation, as individual rationality),
manipulation resistance (incentive compatibility, coalition-proofness, Sybil cost),
legitimacy (who consented to the rules), and operating cost.

## 3. The seven questions, as a checklist every candidate must pass

1. **What exists?** (R) 2. **Who owns it?** (O) 3. **Who can use it?** (A, P) 4. **Who decides?** (G)
5. **How are obligations discharged?** (S, T) 6. **What happens when participants disagree?**
(E, G) 7. **What prevents manipulation?** (I, P, E)

A candidate that cannot answer all seven in one sentence each is not yet an institution. It is a
narrative. Several of the 20 "inventions" in `sources/pasted/2026-10-17_02_…` §13 fail this test.
Examples: Orbital Logistics Credits (no enforceable R today), the BoE Yield Splitter (O and G
conflict with the stated reserve regime), and Agentic Mutual Credit (E is "reputation slashing",
which fails against free pseudonyms).

## 4. Known institutions placed in the ontology

| Institution | R (claim) | O | A | G | S | E | I | P | T |
|---|---|---|---|---|---|---|---|---|---|
| Sterling cash / reserves | Liability of BoE | Bearer / account | Market prices | Parliament, BoE MPC | Transfer | Legal tender, tax liability | Central (reserves); none (cash) | Universal | Perpetual |
| Bank deposit | Claim on a bank | Account holder | Market | Bank + PRA | Interbank RTGS / netting | Contract + deposit insurance | Bank ledger | KYC | On demand |
| Fiat-backed stablecoin | Claim on issuer reserves | Token holder | Market | Issuer + regulator | Token transfer | Contract, redemption right | Public chain | Wallet (+ KYC at ramps) | On demand redemption |
| Bitcoin | No claim (bearer asset) | Key holder | Market | Rough consensus of nodes/miners | Chain transfer | Cryptography only | Public ledger | Permissionless | Fixed issuance |
| LETS mutual credit | Claim on "the community" | Members | Bilateral trade | Members | Ledger transfer | Social only | Shared ledger | Open → adverse selection | No maturity |
| Sardex / WIR (B2B mutual credit) | Claim on network | Member firms | Trade within circuit | Operator (WIR: licensed bank) | Ledger transfer | Contract + credit limits + brokers | Operator ledger | Vetted firms | Credit lines |
| **Multilateral trade-credit set-off (MTCS)** | **Existing invoices (receivables)** | **Original creditors** | **None (no new allocation)** | **Participants consent per round** | **Set-off: discharge without payment** | **Contract law; insolvency law limits** | **Invoice graph seen by the clearer** | **Consenting firms** | **Invoice due dates** |
| CCP netting | Novated trades | CCP members | Market | CCP rules + regulator | Net settlement | Default fund, statutory protection | CCP | Members only | Settlement cycle |
| Compute credits / reservations | Provider liability for compute | Customer (often non-transferable) | Posted price | Provider | Delivery | Contract | Provider | Account | Expiry |
| GPU rental-index future (proposed) | Cash claim on index | Holder | Exchange | Exchange + CFTC | Cash | Clearing house | Exchange | Members | Expiry |
| Citizen wealth fund / dividend | Claim on fund income | Citizens (non-transferable) | Equal shares | State | Transfer | Statute | Public | Residency | Annual |
| Lunar / asteroid resource claim | Extracted resources only (US/LU law); no territory (OST Art. II) | Extractor | First possession | National licensing | Delivery | National law only | Registry | Licensed operators | Undefined |

The bolded MTCS row is the only one that creates **no new money, no new asset and no new
allocation rule**. It changes only S (how existing obligations are discharged) and I (someone
sees the graph). Section 6 explains why this matters.

## 5. Constraints that bound the feasible set F(e)

These are hard walls. A design outside them is not "ambitious". It is impossible or illegal.

1. **Accounting identity [EST].** Every financial asset is someone's liability. Issuing a claim
   creates no net wealth. "Money from nothing" designs violate this, including several "yield"
   and "reserve unit" ideas in the source material.
2. **Myerson–Satterthwaite [EST].** With private values, no voluntary, budget-balanced,
   incentive-compatible mechanism achieves efficient bilateral trade in general. A design that
   claims all four needs a subsidy, or it is wrong.
3. **Arrow / Gibbard–Satterthwaite [EST].** No non-dictatorial rule for three or more options is
   strategy-proof on unrestricted preferences. Governance designs must choose which property to give up.
4. **Kiyotaki–Wright / search [EST].** Acceptance is an equilibrium with multiple steady states.
   A new unit of account faces a coordination problem that decent technology cannot remove.
5. **Kocherlakota [EST].** Record-keeping can replace money only if defectors can be punished.
   Under free pseudonyms (cheap identities), punishment fails (Friedman & Resnick 2001 **[EST]**).
6. **Pari passu in insolvency [EST, UK law].** A contractual multilateral netting scheme cannot
   override pro-rata distribution once a participant is in liquidation (British Eagle v Air
   France [1975]). Set-offs completed before insolvency are discharges, but they are exposed to
   preference challenge (Insolvency Act 1986 s.239).
7. **Physical finitude.** Claims on compute, energy or land cannot exceed deliverable capacity.
   Compute claims also depreciate fast, because price-performance improves rapidly.
8. **Regulatory perimeter (UK).** Holding client funds triggers EMR 2011 and PSRs 2017.
   Promoting cryptoassets triggers the financial promotion regime. Issuing payment stablecoins
   triggers FSMA 2023 DSA rules. Details are verified in `research/prior-art.md` and
   `research/governance-and-rights.md`.

## 6. Where the open space is: the S and I dimensions, not the unit of account

**[INF]** Combining constraints 4–6 with the historical record (independent currencies dismantled
or stalled; B2B mutual credit and clearing surviving; Sardex and WIR succeeding only with
operators and credit discipline) gives a structural conclusion:

> The cheapest place to innovate is **how existing obligations are discharged (S)** and
> **who can see and verify the obligation graph (I)**, keeping the incumbent unit of account.
> Changing the unit of account is the most expensive move. It fights the acceptance equilibrium,
> the tax system and the regulatory perimeter all at once.

This is why the programme's centre of gravity has shifted from "a better currency" to "a better
discharge mechanism". The flagship decision (`research/flagship-decision.md`) tests this
inference against the candidates. It is not assumed true.

## 7. How a computational search should use this ontology (later stages only)

A mechanism-search engine is only worthwhile once one hand-built mechanism has been shown to
beat a strong baseline on real-ish data. When that happens, the ontology defines the search space:

- **Genotype** = a choice in each of R, O, A, G, S, E, I, P, T.
- **Environment** = e, sampled from held-out calibrations: different IO tables, network
  topologies and shock processes.
- **Fitness** = a vector, never a scalar (Pareto front): efficiency, stability, the six
  distribution axes, voluntary participation, manipulation resistance and operating cost.
- **Anti-circularity rule.** The model that proposes a mechanism must never set the evaluation
  environment or the baselines. Every reported improvement is measured on environments the
  search never saw. This answers the Lucas-critique and Goodhart concerns raised in the source
  mandate (§9).
