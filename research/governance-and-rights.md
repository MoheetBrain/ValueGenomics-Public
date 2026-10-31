# Governance and Rights

> **Historical research note (17 October 2026).** Preserved for intellectual provenance. The current programme is independent computational research; earlier product, pilot and commercial proposals below are historical options, not a business being launched. Legal, market and novelty statements are dated research assessments, not current advice or independently established priority claims. Personal goals have been omitted from this public edition; equations and scientific results are retained.


Stage C artefact · 2026-10-17

**Not legal advice.** This maps the issues to put to qualified English counsel and, where
relevant, to the FCA (perimeter query), HMRC and the ICO. Authorities are cited from
`research/audit/prior-art-verification.md` §(i): [V] = checked on 2026-10-17, [K] = standard
citation not re-checked, [U] = unverified.

Part A covers the flagship (Zero-Net). Part B records the rights analysis for the rejected
candidates, so the reasoning is preserved.

---

## Part A — Zero-Net

### A1. What rights exist, and what Zero-Net does to them

| Object | Legal character | Effect of Zero-Net |
|---|---|---|
| A trade receivable (an invoice owed to a firm) | Chose in action: the creditor's personal right to be paid. Assignable by statute (LPA 1925 s.136) or in equity [K] | **Discharged** by set-off for the cleared amount, only with the creditor's and debtor's confirmation of that cycle |
| A trade payable | The debtor's obligation | Discharged by the same act |
| Set-off | Five kinds in English law: legal (statutory, between mutual debts in litigation), equitable (closely connected claims), **contractual**, insolvency (mandatory, IR 2016 r.14.25 [V]) and banker's [K] | **Multilateral set-off is purely contractual.** Without an agreement, triangular debts lack mutuality and cannot be set off |
| A new asset, money, credit line or security | none | **None created.** This is the design constraint that keeps Zero-Net outside most of the regulatory perimeter (A3) |

**The instrument.** For each confirmed cycle (i₁ → i₂ → … → i_k → i₁, amount c), the members
execute an *n-party set-off agreement*. Each member agrees that £c of its debt to its successor
is discharged in consideration of the discharge of £c owed to it by its predecessor. Each
party's release is its consideration. Agreements are executed electronically (electronic
signatures are admissible; Electronic Communications Act 2000 [K]). Each one is executed
atomically, cycle by cycle, and nothing remains outstanding once it is executed.

### A2. Insolvency: the hardest constraint

1. ***British Eagle v Air France* [1975] 1 WLR 758 (HL)** [V summary]. A clearing-house
   arrangement could not displace pari passu distribution on a member's liquidation.
   **Design response:** Zero-Net never holds standing multilateral netting obligations. Each
   cycle is executed and finished immediately. No "net position" with the operator or the
   network survives the round. There is nothing executory for a liquidator to set aside.
2. **The CCP alternative is rejected.** IATA's later scheme, upheld in Australia in *IATA v
   Ansett* [2008] HCA 3 [V], made the clearing house each member's sole counterparty. That
   would turn Zero-Net into a credit intermediary bearing counterparty risk, and possibly a
   regulated one. It contradicts "holds no funds, extends no credit".
3. **s.127 Insolvency Act 1986** [K]: dispositions after a winding-up petition is presented
   are void unless the court validates them. **Design response:** before each execution,
   screen every member of every cycle against The Gazette (petitions), Companies House status
   (administration, liquidation) and CIGA 2020 moratoria. Exclude any hit and recompute the
   cycles.
4. **s.239 preferences** [K]: within 6 months (2 years if connected) of insolvency, a
   transaction that puts a creditor in a better position is voidable if the company was
   "influenced by a desire" to prefer (*Re MC Bacon* [1990] [K]). **Design response:**
   arm's-length, automated, rules-based allocation, with no member choosing who gets cleared.
   Connected-party edges excluded. An audit trail shows that the algorithm, not a member,
   selected the cycle.
5. **Residual exposure: Proposition 4.** A firm that fails *after* a valid round has
   transferred value from its unscreened creditors to its cleared creditors. That is lawful if
   the round was valid. Its size is measured exploratorily in Experiment 001 (E4) and is a
   disclosure item in the rulebook.
6. **CIGA 2020 s.233B (ipso facto)** [U]: can membership be terminated when a member enters
   an insolvency procedure? Membership is not obviously a "contract for the supply of goods or
   services". This is a question for counsel.

### A3. Regulatory perimeter (FCA)

| Regime | Trigger | Zero-Net design | Residual risk |
|---|---|---|---|
| **PSRs 2017, Sch.1 Pt.1** [V] | Execution of payment transactions, money remittance, payment initiation (PIS), account information (AIS) | Never receives funds, never executes transfers, never initiates payments. Residual payments are made by members through their own banks. Payment *sequencing* is advisory only | The FCA looks at substance (PERG 15.3 [V]). Initiating residual payments needs an authorised PISP partner; reading bank data needs an AISP. **Perimeter query recommended before a Level 2 pilot** |
| **EMR 2011** [K] | Stored monetary value issued on receipt of funds | No stored value, no units | None unless a mutual-credit unit is added (it is not) |
| **Consumer Credit Act / FSMA credit activities** | Extending credit | No credit extended | Members are businesses; check sole traders and partnerships |
| **FSMA 2023 DSA / crypto regime (from 25 Oct 2027)** [V] | Digital settlement assets, cryptoassets | No token, no chain | None |
| **Settlement Finality Regs 1999; CA 1989 Pt VII** [V] | Designated systems / recognised clearing houses | Not available to SME clearing | No statutory netting protection, hence the per-cycle execution design (A2) |
| **Money Laundering Regs 2017** | Listed regulated activities | Probably outside scope [U] | Business onboarding and controls are adopted voluntarily, because fabricated-invoice laundering is the main abuse risk |

### A4. Tax
- **VAT:** set-off does not change VAT on the underlying supplies. Each supply is taxed at its
  own tax point and value [V].
- **Cash accounting scheme** (VAT Notice 731): the scheme treats payment in kind as payment on
  receipt of consideration. Treating the set-off date as the payment date is an **inference**
  [U]. Confirm with HMRC manuals or a non-statutory clearance.
- Direct tax: no new income. Discharge equals receipt and payment.

### A5. Data protection, confidentiality and competition law
- **UK GDPR:** invoice data from sole traders and partnerships is personal data.
  - Lawful basis: contract (Art. 6(1)(b)).
  - A DPIA is needed before the pilot, with data minimisation (amount, due date, counterparty
    ID only) and retention limited to the audit period.
- **Commercial confidentiality:** a member sees only its own proposed cycle edges, which are
  invoices it already holds. It never sees the wider graph.
- **Competition Act 1998, Chapter I:** competitors exchanging commercially sensitive
  information (prices, volumes, customers) can infringe (CMA horizontal guidance, 2023 [K]).
  - **Design response:** the operator acts as a "clean team". No member-level data leaves it.
  - Network statistics are published only in aggregate, with minimum cell sizes.

### A6. Governance — options and recommendation

| Model | Who decides rules | Legitimacy | Speed | Investability (relevant to the user's goal) | Precedent |
|---|---|---|---|---|---|
| **(a) Operator company** | Board of the company | Low–medium | High | High (equity can be raised; founder ownership) | Sardex |
| **(b) Member cooperative / mutual** | Members, one-member-one-vote | High | Low | Low (limited return on capital) | WIR (originally); Credit Commons Society |
| **(c) Federated open protocol** | Protocol governance; many operators | Medium–high | Medium | Medium (value in services, not protocol) | Cycles; Credit Commons |
| **(d) Public utility** | Statute / regulator | High | Low | None | Slovenia (AJPES), Republika Srpska (Banja Luka Stock Exchange) |

**Recommendation for the pilot: (a) with binding member protections.** The trade-off is stated
openly.
- An operator company can move quickly and raise capital. Of the four models, it is the only
  one compatible with the user's ownership ambition.
- Its legitimacy deficit is reduced by the protections below.
- If adoption grows, migration to (c) remains possible, and (d) is the natural endgame if
  government wants national coverage (Slovenia).

Binding member protections:
1. **Published, deterministic objective.** Maximum cleared value subject to the rules. The
   algorithm is open source, and members can verify their own cycles.
2. **Member council with veto** over any rule change affecting consent, eligibility,
   screening, data use or fees.
3. **No discretion over individual cycles.** The operator cannot include, exclude or
   prioritise particular members outside the published rules.
4. **Full audit log** per round, available to members for their own cycles and to an
   independent reviewer for all.
5. **Fee cap** and fee-schedule changes only with council consent.

### A7. Disputes, enforcement and failure modes
- **Disputed invoices are ineligible.** Only invoices confirmed by both parties enter a round.
- **Post-round disputes** (for example, goods later found defective) are resolved bilaterally,
  like any paid invoice: a credit note or refund between the two parties. The discharge itself
  is not reversed, because reversing it would unwind other members' cycles.
- **Enforcement:** a completed set-off is a discharge, which a member can plead as payment.
  Residual debts are enforceable in the ordinary way, including statutory interest under the
  Late Payment of Commercial Debts (Interest) Act 1998, as amended by the Commercial Payments
  Bill if enacted.
- **Dispute forum:** an arbitration clause for rulebook disputes; otherwise English courts.
- **Open legal questions for counsel:**
  - (i) Does a set-off discharge count as "payment" for statutory interest and payment-practice
    reporting? (Hypothesis N-8.)
  - (ii) The ipso facto point (A2.6).
  - (iii) Perimeter confirmation for advisory sequencing (A3).
  - (iv) Robustness of the per-cycle execution design against *British Eagle* (A2.1).

### A8. What prevents manipulation (summary)
| Threat | Control |
|---|---|
| Fabricated invoices / laundering via insolvent colluder | Two-sided confirmation; invoice evidence (VAT/e-invoice IDs); connected-party exclusion; solvency and petition screening; clawback term |
| Strategic withholding / cherry-picking | Once submitted, debts are cleared by the published rule. Withdrawal is allowed only in the opt-out round |
| Sybil observers | Business onboarding (Companies House, VAT); members see only their own edges |
| Operator bias | Deterministic open algorithm; audit log; council veto |

---

## Part B — rights analysis for rejected candidates (kept for the record)

### B1. Future extraterrestrial resources (C5)
These four things must never be conflated:

| Claim type | Enforceable today? | Basis |
|---|---|---|
| A *hypothetical entitlement* to future lunar or Martian resources | **No.** There is no asset and no obligor | — |
| A *contractual claim on a future venture* (equity, revenue share, offtake) | **Yes, against the venture,** under the contract's governing law | Ordinary contract and securities law. Example: Interlune–Bluefors He-3 offtake |
| A *right to extracted resources* | **Yes, once extracted,** in five national regimes | US CSLCA 2015 §51303; Luxembourg 2017; UAE decree-law 2023; Japan 2021; Artemis §10 (non-binding) |
| *Ownership of extraterrestrial territory* | **No.** Prohibited | Outer Space Treaty Art. II. Moon Agreement (17 parties) |

Any "future resource token" sold today could only be the second type, a claim on a company. It
would be regulated as a security or specified investment.

### B2. Compute claims (C1, C2)
- A compute claim is a **service contract** against a specific provider: a reservation or
  prepaid credit.
- A rental-index future is a **cash-settled derivative**, not a delivery right (CME products
  pending CFTC review).
- A transferable token representing compute would raise UK financial-promotion (PS23/6) and
  possibly collective-investment questions. A compute "currency" adds nothing legally to a
  service contract except regulatory exposure.

### B3. Machine-output rights (C4)
"A token about an asset is not a claim on it." An enforceable claim on robot or agent revenue
needs:
- (i) a legal owner of the machine (an SPV);
- (ii) a contractual cash-flow right with mandatory distribution;
- (iii) servicing and verification of revenue;
- (iv) securities-law compliance.

XMAQUINA/DEUS fails (ii): its distributions are discretionary.

### B4. Equality and entitlements (C10)
Guaranteed entitlements (dividends from citizen funds, universal basic services) need a
sovereign or statutory issuer and a funding source. They are legitimate design objects, but a
private founder cannot create them. Arrow and Gibbard–Satterthwaite constrain the governance of
any such fund. The yard-sale / reallocation literature shows the inequality dynamics without
redistribution.
