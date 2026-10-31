# Flagship Decision

> **Historical research note (17 October 2026).** Preserved for intellectual provenance. The current programme is independent computational research; earlier product, pilot and commercial proposals below are historical options, not a business being launched. Legal, market and novelty statements are dated research assessments, not current advice or independently established priority claims. Personal goals have been omitted from this public edition; equations and scientific results are retained.


Stage B artefact · 2026-10-17 · decision status: **selected. Experiment 001 preregistered verdict CONTINUE**
(as a model ceiling about 2× real-world benchmarks; next gate is real data; see `results/experiment-001-summary.md`
and `research/final-decision-memo.md`)

## The flagship: **Zero-Net** (working name)

> **A UK institution that lets groups of businesses cancel the debts they owe each other in
> loops, by consented legal set-off, without moving money, holding anyone's funds or lending
> anything. It is built on a pre-registered science of how much of an economy's debt can be
> cleared this way.**

### In plain English
Every month, member businesses connect their unpaid invoices from their accounting software.
The software looks for loops: A owes B, B owes C, C owes A. It proposes cancelling the smallest
amount around each loop. Every firm in a loop sees only its own part (the invoices it already
has with its own trading partners) and confirms it. Once all confirm, the debts in that loop
are discharged by legal set-off, exactly as if everyone had paid each other at the same moment.
No money moves, nobody lends, and Zero-Net never touches the funds. What remains is paid
normally in pounds. Zero-Net can also tell members in what order to pay so that the least cash
is needed (Proposition 1).

The working name comes from the cancellation idea in the source material ("Zero-Net Economic
Clearing", source 03) and its zero net position. "ZeroNet" is also the name of an unrelated
2015 peer-to-peer web project, so a final name needs a trademark check.

---

## The ten questions

**1. What exactly are we discovering or inventing?**
- *Discovering:* how much UK business-to-business debt is circular, and so needs no money to
  discharge. Also what network properties predict that share, and what participation threshold
  makes clearing worthwhile. No validated predictor exists anywhere (`prior-art.md` §B).
- *Inventing:* the UK institutional design that makes custody-free clearing lawful and
  trustworthy. That means eligibility rules, per-cycle consent, solvency and petition
  screening, immediate finality, governance and a legal template robust to *British Eagle*,
  s.127 and s.239.

The mechanism itself (multilateral set-off) is **not** our invention: Slovenia (1991–),
Republika Srpska (2015–), Sardex, Cycles. This is stated plainly.

**2. Why doesn't an existing solution already solve it?**
- No UK service exists. The foreign systems are statutory and state-run, or are closed
  mutual-credit circuits.
- Cycles has gone crypto-first, starting with OTC netting for trading firms.
- UK tools address other parts of the problem:
  - Invoice finance and supply-chain finance cost money and need a creditworthy anchor.
  - Payment-term law (the Commercial Payments Bill) shortens terms but cannot cancel loops.
  - Accounting platforms each see only one side of every invoice.
  - No individual firm can see a cycle.

**3. What mathematical model must we establish?**
- The obligation graph G = (N, E, f), cleared by bounded maximum circulation (an LP), plus four
  propositions:
  - P1: custody-free clearing plus sequencing reaches the netting liquidity bound.
  - P2: cold start decays like p^|C| under random participation.
  - P3: no wealth is created; late payers lose float.
  - P4: the *British Eagle* transfer formula.
- The empirical objects are the clearability curve φ(p, strategy | topology) and a predictor
  φ ≈ F(reciprocity, strongly connected share, degree), validated out of sample.
- The next mathematical problem, for Stage 3: **constrained clearing design**. Maximise cleared
  value subject to circulation, consent and individual rationality (no member's float loss
  exceeds its gains), plus exclusion of distressed firms. That is still an LP, and it is the
  first honest target for Economic Genome mechanism search (`candidate-comparison.md` §4).

**4. What resource, contract, institution or right does it operate on?**
- *Resource:* existing trade receivables. In English law these are choses in action: the
  creditor's right to be paid.
- *Contract:* a per-round **multilateral set-off agreement**. Each member of a confirmed cycle
  agrees that its debt to the next member is discharged in exchange for the discharge of the
  debt owed to it by the previous member. Each party's consideration is the release it receives.
- *Institution:* a membership rulebook (eligibility, confirmation, screening, finality, fees,
  data use, governance).
- *No new right is created:* no money, token, credit line, security or investment.

**5. Who has authority over it?**
- Each member over its own receivables and payables. Nothing is set off without its
  confirmation of that specific cycle.
- The operator only over running the published algorithm and the rulebook.
- Members collectively over rule changes affecting consent, eligibility or fees (member
  council with veto; see `governance-and-rights.md` §6).
- English courts over disputes. A discharged debt is enforceable as discharged.

**6. Why would participants voluntarily adopt it?**
- *Small firms owed money late:* part of their receivables is turned into discharge of their
  own payables, at zero cost, with no credit check and no cash.
- *Distressed firms:* in Republika Srpska, clearing lowered payment-default probability by
  about 6 pp, more for cash-poor firms.
- *Large buyers:* the Commercial Payments Bill makes statutory interest mandatory and caps
  terms, so float becomes a liability.
  - If set-off counts as payment for statutory interest and payment-practice reporting (legal
    question N-8), clearing improves their reported performance and avoids interest.
  - Where it does not, Proposition 3 says some large late payers lose float. Adoption by them
    is a known risk, not an assumption.
- *Effort:* adoption is easier if it plugs into existing accounting software (Xero, Sage,
  QuickBooks marketplaces).

**7. How would it work in a real transaction?** See the worked example below.

**8. What happens if an agent defaults, cheats or refuses to participate?**
- **Refuses:** the firm declines the cycle. It is recomputed without that firm's debts (the
  two-round opt-out, as in Republika Srpska), and nothing it did not confirm is discharged.
- **Defaults after clearing:** cleared obligations stay discharged (final). Residual debts are
  ordinary debts, enforced as usual, with statutory interest where applicable.
- **Becomes insolvent:** firms with a winding-up petition, in administration, under moratorium
  or in liquidation are excluded before execution (Gazette and Companies House checks). Nothing
  multilateral is carried forward, so a liquidator has no unexecuted netting arrangement to
  attack (*British Eagle*). Arm's-length automated clearing makes a s.239 "desire to prefer"
  unlikely. Clearing between connected parties is excluded or capped.
- **Cheats (fabricated invoices):**
  - Every obligation must be confirmed by both parties and backed by invoice evidence.
  - Connected-party edges are excluded.
  - The fabricated-edge laundering attack (`adversarial-review.md`) is blocked mainly by
    solvency screening, because its victims are the creditors of an insolvent colluder.

**9. How does the mechanism affect inequality, welfare and productivity?**
- *Welfare:* no wealth is created (P3). Gains come from financing-cost differences, avoided
  defaults (P4 and the Republika Srpska evidence) and lower collection costs.
- *Distribution:* expected to be progressive, because the firms that gain most are the small
  firms waiting on late payers. Large late payers lose float, and outside creditors of a firm
  that fails soon after a round can lose (P4). Experiment 001 measures the first; E4 explores
  the second.
- *Productivity:* fewer liquidity-driven failures of viable firms, and less time chasing
  payments (86 hours a year per firm, per DBT research).
- *Political power:* the operator gains information power over the trade graph. This is
  mitigated by data minimisation, member governance and, later, privacy-preserving computation.

**10. What concrete evidence would convince us to abandon it?**
Any one of:
- (a) Experiment 001 returns **KILL**: UK-calibrated full-participation clearability is below
  3 %.
- (b) A real consenting cluster of at least 30 firms clears **below 3 % of submitted value**.
- (c) Counsel or an FCA perimeter answer concludes the service is a regulated payment service
  needing authorisation that a solo founder cannot obtain.
- (d) Fewer than 30 firms in a target cluster agree to share invoice data within 3 months of
  structured outreach.

---

## Worked example — a south-London construction supply chain

Four real types of firm, with invoices outstanding on the clearing date (amounts in £k):

| Debtor → Creditor | Amount | Why it exists | Status |
|---|---:|---|---|
| Electrical subcontractor **E** → wholesaler **W** | 25 | cable and switchgear | due now |
| Wholesaler **W** → logistics firm **L** | 18 | deliveries | due in 10 days |
| Logistics firm **L** → main contractor **M** (plant-hire division) | 20 | telehandler hire | due in 20 days |
| Main contractor **M** → electrical subcontractor **E** | 40 | stage payment | 30 days overdue |

**Behaviour without Zero-Net.** M pays E late, as large contractors often do. E must pay W now:
it draws its overdraft at about 14 %, or pays W late. Paying late pushes the problem along to W,
then to L. Everyone is solvent on paper. The chain is jammed because of timing, not wealth.

**The clearing round.** The loop E→W→L→M→E has a minimum of 18. Each firm confirms only its
own two invoices. After the round:

| Edge | Before | Cleared | After |
|---|---:|---:|---:|
| E → W | 25 | 18 | 7 |
| W → L | 18 | 18 | 0 |
| L → M | 20 | 18 | 2 |
| M → E | 40 | 18 | 22 |
| **Gross outstanding** | **103** | **72** | **31** |

Net positions are unchanged (E +15, W +7, L −2, M −20), as P3 requires. £72k of debt has been
discharged with **£0 moved**. The remaining £31k needs only **£22k** of cash if paid in the
right order (P1):

1. L pays M 2.
2. M adds 20 and pays E 22.
3. E pays W 7 from what it received.

**Who gained what.**
- E escapes about £18k of overdraft for about 30 days, worth roughly £200, and is no longer
  exposed to M's lateness on that £18k.
- W is fully paid and owes L nothing.
- M loses £18k of float. But that £18k is already overdue. Under the Commercial Payments
  Bill, mandatory statutory interest (8 % over base) on it would cost M more than the float is
  worth at M's own cost of funds, so clearing is in M's interest too. This holds if the Bill
  passes as drafted and interest is enforced.

The direct interest saving per firm is small. That is the honest scale of the value. The large
value arises when one firm in the loop is near failure and the cleared £18k decides whether it
survives. That is the effect Republika Srpska's data detected.

**What if W had a winding-up petition?** W is excluded from the round. The loop is broken and
nothing is cleared. That protects W's other creditors (P4, s.127).

---

## Conceptual invention vs software implementation

| Layer | What it is | Defensible? |
|---|---|---|
| **Conceptual invention** | The institutional rules: eligibility, two-sided confirmation, per-cycle consent, solvency and petition screening, immediate finality, no carried-forward obligations, governance; a UK legal template; the scientific model of clearability and recruitment | **Yes**: legal template, trust, member network and the predictor that tells you *which clusters to recruit* |
| **Software implementation** | An LP solver (max-circulation), accounting-software connectors, a confirmation UI, set-off notices, an audit log | **No**: the algorithm is public (TCT, MTCS, OR-Tools). It could be open-sourced without losing anything that matters |

## Why this project and not another (summary of Stage B)
- It is the only candidate that is an economic institution in the full sense: rights,
  settlement, governance, enforcement.
- It respects every hard constraint.
- It has causal real-world evidence of welfare gains.
- Its main risk can be tested for £0 immediately.
- It is honest about modest novelty and a revenue ceiling.

Alternatives were rejected on evidence: compute money (carrying-cost proposition), future
resource claims (untestable), the AI governance engine (circular until a validated domain
exists), and agent liability (incumbents). The fallback if Experiment 001 kills C6 is **C2**,
open compute exchange rates.

## Commercial realism (no probabilities)
- Revenue at plausible fees is a few basis points to a few tenths of a percent of value set off.
- [Personal objective and deadline omitted from this public edition.]
- The cheapest credible path to value is to own the UK legal template and the first real UK
  clearability data, since both are scarce.
- The research outputs are publishable even if the business is not viable: first UK estimate,
  a predictor, and a legal design.
