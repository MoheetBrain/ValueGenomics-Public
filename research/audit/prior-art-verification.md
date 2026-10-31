# Prior-Art Map and Fact Verification — Economic Genome (ValueGenomics)

**Date of research:** 2026-10-17
**Scope:** Prior art for candidate economic-institution projects, a fact-check of claims made in earlier AI-written reports, and the data sources available. The aim is to stop the programme from claiming novelty for things that already exist.
**Method:** Live web search and document retrieval on 2026-10-17, plus local text extraction of two primary PDFs (AJPES monthly set-off reports for 2025; Croatian National Bank Working Paper W-66). Calculations derived from those PDFs are marked as such.

**Verification legend used throughout**

- **[V]** — checked in this session against the linked source.
- **[K]** — a standard citation given from domain knowledge. Its bibliographic details (pages and DOI) were *not* re-checked in this session, so confirm them before publication.
- **[U]** — UNVERIFIED: no source was found, or sources conflict.

Nothing in Part 1(i) is legal advice. It is a map of the issues to put to qualified English counsel.

---

## 0. Decision-relevant summary

1. **Multilateral trade-credit set-off is not new. It runs at national scale and has been studied causally.**
   - **Slovenia** has run it since 1991, now through AJPES.
   - **Republika Srpska** (Bosnia and Herzegovina) has run a statutory clearinghouse since 2015. A causal study finds that clearing lowers firm default rates.
   - **Cycles**, a 2026 spin-out of Informal Systems, is a venture-funded attempt to run an open, privacy-preserving version.
   - Any claim that the cycle-finding algorithm, the institution itself, or "consent-based" clearing is novel would be false.
2. **Real systems clear a much smaller share of debt than the "25%" figure in circulation.**
   - **Slovenia, 2025** (summed from AJPES monthly reports; my calculation): €57.9m was set off. That is **≈2.4% of the €2.41bn reported** and **≈14.2% of the €408m "considered"** (*upoštevane*).
   - **Republika Srpska, 2015–2019:** about **0.6% of GDP is cleared per round**, against late debt of about **9% of GDP** per round. Clearing therefore removes roughly 7% of reported late debt per round, about 1.6% of GDP per year.
   - **Where 25% comes from:** it is a *Sardex* figure for a closed mutual-credit circuit (Fleischman, Dini & Littera 2020). It does not describe Slovenia's national system.
   - **The highest figure:** a 2026 preprint from a vendor reports 21% for cycle-only netting on a €19.7bn invoice corpus, and 54% for "path-enabled" compensation. The path-enabled figure is not pure set-off: it generates new settlement instructions.
3. **Network topology explains why yields are low.** Firm-level production networks have low reciprocity: about 5% in Ecuador, 4–9% in Hungary and about 2% in FactSet (Bacilieri et al., JEDC 2026). In Republika Srpska the clearable core was one strongly connected component of about 1,000 firms, with a median cycle length of about 10. Clearing depends on long cycles and a high participation rate.
4. **UK law: no route was found that gives multilateral set-off among SMEs statutory protection in insolvency.**
   - Insolvency set-off (IR 2016 r.14.25) is mandatory and requires mutuality.
   - *British Eagle* [1975] 1 WLR 758 (HL) means a multilateral netting agreement that has not yet been executed cannot bind a liquidator.
   - Settlement Finality Regulations protection is limited to designated systems whose participants are financial institutions. Companies Act 1989 Part VII protection is limited to recognised exchanges and clearing houses.
   - Netting that has already completed between solvent, consenting firms is in principle a valid contractual discharge. It remains exposed to s.127 (dispositions after a winding-up petition) and s.239 (preferences).
   - A service that only calculates offsets, never holds funds and never executes payment transactions does not obviously fall within the PSRs 2017 Schedule 1 Part 1 list. No FCA PERG 15 guidance specifically on netting services was found [U]. Counsel or an FCA perimeter query is needed.
5. **No agent payment protocol does multilateral netting.** As of October 2026 this covers AP2, ACP, x402, MPP, Visa TAP/Intelligent Commerce and Mastercard Agent Pay. x402's "batch-settlement" scheme (May 2026) aggregates payments over a *bilateral* payment channel; its abstract spec allows "credit-backed commitments". Cycles targets crypto OTC netting (Cycles Prime) and stablecoin payments for SMEs (Cycles Pay).
6. **Compute markets are being financialised quickly.** CME's Silicon Data H100/B200 rental-index futures were set for 5 October 2026, but CME has since postponed them to an effective date "to be announced", still pending CFTC review. ICE/Ornn and Architect/Ornn contracts are announced and pending. Setara Financial markets a trademarked "Normalized Compute Unit (NCU™)", but its live series is pre-production and built on list prices.
7. **Fact-check results (Part 2).**
   - Several earlier claims are **outdated or wrong**:
     - BoE stablecoin backing: the final split is 30/70 (not 40/60), and holding limits were dropped.
     - NPPF station density: 35–45 dph, not 40.
     - "MTCS reduces 25%": this is a misattribution of the Sardex figure.
     - Sardex velocity "5×": sources give about 8×, as measured by the company.
     - Private credit "$1.96tn": only a market-research estimate; other definitions give $1.7–2.3tn or more.
   - The remaining claims are broadly **confirmed**: the 25 October 2027 crypto go-live, PS23/6, the €1m LNE threshold, the 10-year enforcement rule, NIST FIPS 203/204/205, the 1,200–1,450 logical-qubit estimate, the BIS December 2025 auction-LSM paper, and BoE (2014).

---

## Part 1 — Prior-art map

### (a) Monetary search theory

| Work | Citation |
|---|---|
| Kiyotaki & Wright (1989), "On Money as a Medium of Exchange" | *Journal of Political Economy* 97(4): 927–954. DOI [10.1086/261634](https://doi.org/10.1086/261634) [K] |
| Kiyotaki & Wright (1993), "A Search-Theoretic Approach to Monetary Economics" | *American Economic Review* 83(1): 63–77 [K] |
| Trejos & Wright (1995), "Search, Bargaining, Money, and Prices" | *JPE* 103(1): 118–141. DOI [10.1086/261978](https://doi.org/10.1086/261978) [K] |
| Lagos & Wright (2005), "A Unified Framework for Monetary Theory and Policy Analysis" | *JPE* 113(3): 463–484. DOI [10.1086/429804](https://doi.org/10.1086/429804) [K] |

**What they accomplish**
- KW89 derives money as an equilibrium medium of exchange in a random-matching economy with a double-coincidence-of-wants friction. Which good becomes money depends on storage costs and beliefs, so equilibria can be multiple.
- KW93 simplifies this to fiat money with indivisible goods.
- Trejos–Wright makes prices endogenous through bilateral bargaining.
- Lagos–Wright adds a periodic centralised market with quasi-linear preferences. This collapses the money-holdings distribution and makes monetary policy analysis tractable. It is the workhorse of New Monetarist economics.

**Limitation for us.** These models explain *why* a medium of exchange is needed. They assume no record of who owes whom. They do not model networks of credit obligations, or clearing of obligations without a medium of exchange.

**Open space.** Linking obligation-graph topology (cycles and reciprocity) to how much money a given trade pattern actually needs. That is, measuring the "money demand avoided" by clearing on real graphs. Search theory gives the language, but no empirical clearing benchmarks.

### (b) "Money is memory"

| Work | Citation |
|---|---|
| Kocherlakota (1998), "Money Is Memory" | *Journal of Economic Theory* 81(2): 232–251. DOI [10.1006/jeth.1997.2357](https://doi.org/10.1006/jeth.1997.2357) [K] |
| Kocherlakota & Wallace (1998), "Incomplete Record-Keeping and Optimal Payment Arrangements" | *JET* 81(2): 272–289 [K]. DOI not given because it was not confirmed. |

**What they accomplish**
- Kocherlakota shows that any allocation achievable with money is also achievable with a complete public record of past actions ("memory"). Money is therefore a technologically inferior substitute for a perfect record.
- Kocherlakota–Wallace show that when records update with a lag, the best arrangement mixes money and credit. Better record-keeping shifts the optimum towards credit.

**Limitation.** Abstract environments with no insolvency law, no network structure and no strategic withholding of records.

**Open space.** This is the cleanest theoretical justification for obligation clearing and agent credit: a shared ledger of obligations is "memory". The open empirical question is how much liquidity a *partial* record recovers — one that covers only consenting participants, with consent given per cycle. Slovenia's and Republika Srpska's participation figures are natural calibration points.

### (c) Social choice impossibility

| Work | Citation |
|---|---|
| Arrow (1950), "A Difficulty in the Concept of Social Welfare" | *JPE* 58(4): 328–346. DOI [10.1086/256963](https://doi.org/10.1086/256963) [K] |
| Arrow (1951; 2nd edn 1963), *Social Choice and Individual Values* | Wiley / Cowles Foundation [K] |
| Gibbard (1973) | *Econometrica* 41(4): 587–601. DOI [10.2307/1914083](https://doi.org/10.2307/1914083) [K] |
| Satterthwaite (1975) | *JET* 10(2): 187–217. DOI [10.1016/0022-0531(75)90050-2](https://doi.org/10.1016/0022-0531(75)90050-2) [K] |

**What they accomplish**
- Arrow: no rule that aggregates ordinal preferences over three or more options can satisfy unrestricted domain, weak Pareto, independence of irrelevant alternatives and non-dictatorship at the same time.
- Gibbard–Satterthwaite: every onto, non-dictatorial deterministic voting rule over three or more outcomes can be manipulated.

**Limitation.** These rule out "perfect" AI-designed governance in general. They bind less in restricted domains, with money transfers or quasi-linear utility, or with randomised rules.

**Open space.** None at the level of the theorems. Any "AI governance" project has to say which axiom it relaxes. Claims to escape these results without doing so are a red flag.

### (d) Bilateral trade impossibility

| Work | Citation |
|---|---|
| Myerson & Satterthwaite (1983), "Efficient Mechanisms for Bilateral Trading" | *JET* 29(2): 265–281. DOI [10.1016/0022-0531(83)90048-0](https://doi.org/10.1016/0022-0531(83)90048-0) [K] |

**What it accomplishes.** With privately informed buyer and seller whose value ranges overlap, no mechanism is at once Bayesian incentive-compatible, interim individually rational, budget-balanced and ex-post efficient.

**Limitation for us.** Any compute or entitlement market with private valuations and no subsidy will trade inefficiently.

**Open space.** Obligation clearing largely sidesteps the theorem. It reallocates existing, already-agreed debts and does not require price discovery, so participation is individually rational by construction if net positions are preserved. That is a genuine design advantage, but not a novelty.

### (e) Fair division and resource allocation

| Work | Citation | What it does | Key limitation |
|---|---|---|---|
| Budish (2011), A-CEEI | *JPE* 119(6): 1061–1103. DOI [10.1086/664613](https://doi.org/10.1086/664613) [K] | Approximate competitive equilibrium from equal incomes for combinatorial assignment. Approximately efficient, envy-free up to one good, and strategy-proof in the large. | Needs a price-finding computation. Assumes equal budgets and stationary preferences. |
| Budish, Cachon, Kessler & Othman (2017), Course Match | *Operations Research* 65(2): 314–336. DOI [10.1287/opre.2016.1544](https://doi.org/10.1287/opre.2016.1544) [K] | Large-scale A-CEEI deployment at Wharton for course allocation, with a preference-reporting language. | Domain-specific; relies on a well-designed preference-reporting interface. |
| Ghodsi, Zaharia, Hindman, Konwinski, Shenker & Stoica (2011), Dominant Resource Fairness | NSDI 2011 [K] | Multi-resource max-min fairness on each user's dominant share. Strategy-proof, envy-free, Pareto-efficient and satisfies sharing incentives under Leontief demands. | Static demands; Leontief assumption. |
| Vuppalapati, Fikioris, Agarwal, Cidon, Khandelwal & Tardos (2023), Karma | [OSDI 2023](https://www.usenix.org/conference/osdi23/presentation/vuppalapati) [V] | Generalises max-min fairness to *dynamic* demands with credits: users donate idle resources, earn credits and spend them later. Proves Pareto efficiency, online strategy-proofness and optimal fairness. | Single resource type. Credits are internal, not transferable across systems. |
| Narayanan, Santhanam, Kazhamiaka, Phanishayee & Zaharia (2020), Gavel | [OSDI 2020](https://www.usenix.org/conference/osdi20/presentation/narayanan-deepak) [V] | Heterogeneity-aware cluster scheduling. Converts policies to "effective throughput" across GPU types per job. | Requires throughput profiling per job/accelerator pair. |
| Chaudhary, Ramjee, Sivathanu, Kwatra & Viswanatha (2020), Gandiva_fair | EuroSys 2020, DOI [10.1145/3342195.3387555](https://dl.acm.org/doi/10.1145/3342195.3387555) [V] | Fair-share GPU scheduler balancing efficiency and fairness. Includes automated *trading* of heterogeneous GPUs between users according to relative speedups. | Within one cluster operator; no external market or settlement. |
| Zheng, Pan, Khan, Venkataraman & Akella (2023), Shockwave | [NSDI 2023](https://www.usenix.org/conference/nsdi23/presentation/zheng) [V] | Extends market (Fisher/CEEI-style) allocation to dynamic ML jobs using stochastic dynamic programming. Reports 1.3× makespan and 2× fairness improvement. | Single cluster; no cross-provider entitlements. |

**Open space.** "Compute credits", "heterogeneity-aware exchange rates" and "GPU trading" all exist *inside* one cluster.
- Still open: a *public, reproducible* exchange rate between accelerator types per workload class, derived from MLPerf, and tested against market rental-index ratios (see (n)).
- Also open: entitlements that move across providers. These overlap with commercial efforts such as Setara's NCU (see (n)).

### (f) Clearing and financial networks

- **Eisenberg & Noe (2001)**, "Systemic Risk in Financial Systems", *Management Science* 47(2): 236–249, DOI [10.1287/mnsc.47.2.236.9835](https://doi.org/10.1287/mnsc.47.2.236.9835) [K].
  - Proves that a unique clearing payment vector exists, under mild conditions, for a network of nominal liabilities with proportional repayment. Gives an algorithm.
  - Limitation: focuses on *default* clearing (who can pay what), not on voluntary netting among solvent firms.
- **Bech & Soramäki (2001)**, "Gridlock Resolution in Interbank Payment Systems", [Bank of Finland Discussion Paper 9/2001](https://publications.bof.fi/bitstreams/041214ea-a9f3-4ea3-ab0b-5bb4d02eff2f/download) [V].
  - Gives an algorithm for multilateral resolution of queued interbank payments, used by Danmarks Nationalbank.
  - A 2005 follow-up chapter in Bank of Finland Studies E:31 is [U]; its title was not verified.
- **Martin & McAndrews (2008)**, "Liquidity-Saving Mechanisms", *Journal of Monetary Economics* 55(3): 554–567 [V via citing sources].
  - Shows that LSMs (queues with offsetting) reduce strategic payment delay, with conditions under which welfare rises.
- **Portfolio compression**
  - **D'Errico & Roukny (2021)**, "Compressing Over-the-Counter Markets", *Operations Research* 69(6): 1660–1679, DOI [10.1287/opre.2021.2107](https://doi.org/10.1287/opre.2021.2107) [V]. Shows that compression can remove large shares of notional in dense OTC networks while keeping net positions unchanged.
  - **Schuldenzucker & Seuken**, "Portfolio Compression in Financial Networks: Incentives and Systemic Risk", ACM EC 2020, DOI [10.1145/3391403.3399538](https://dl.acm.org/doi/abs/10.1145/3391403.3399538) [V]. Shows that compression is *not* always socially beneficial (loss-sharing vs contagion trade-off) and gives sufficient conditions.
  - **Veraart (2022)**, "When Does Portfolio Compression Reduce Systemic Risk?", *Mathematical Finance* 32(3): 727–778, DOI [10.1111/mafi.12346](https://onlinelibrary.wiley.com/doi/full/10.1111/mafi.12346) [V].
- **BIS Working Paper No. 1318 (16 Dec 2025)**, Ates, Bech, Garratt & Nanut Petrič, ["Auction-based liquidity saving mechanisms"](https://www.bis.org/publ/work1318.htm) [V].
  - Reverses the LSM logic: participants bid to *supply* liquidity for a proposed set of payments, compensated by side payments from liquidity receivers.
  - Simulations on Peru's BCRP-RTGS, South Africa's SAMOS and SADC-RTGS, and Switzerland's SIC give an average auction success rate of 79% (range 62–100%).

**Limitation.** All of this concerns banks or derivatives dealers with central-bank money and legal netting protection.

**Open space.** The *ideas* are mature: gridlock resolution, LSMs, compression, and liquidity auctions with side payments. Applying the side-payment auction to *trade credit* (SMEs paying a liquidity provider to close a near-cycle) has, as far as we found, no published empirical test. Cycles' published work frames something similar for trade credit, but without empirical results (see (g)).

### (g) Multilateral trade-credit set-off — the most important item

#### g.1 Slovenia: national multilateral set-off (TCT/"Tetris", operated by AJPES)

**History [V].**
- **Origins:** Fleischman, Dini et al. state that the Tetris Core Technologies (TCT) set-off software, developed by Be Solutions, "has been running uninterrupted in Slovenia since 1991". It was first used in the 1991–1995 transition and liquidity crisis, through the payments agency SDK.
- **Operation today:** AJPES runs it **once a month** on a preset date. Firms submit obligations electronically. The algorithm finds a maximum-weight set of cycles. Firms receive set-off notices, and AJPES charges a percentage fee on the amount set off.
- **Legal basis:** Slovenia's 2011 Act on Prevention of Late Payments made reporting of due obligations to *compulsory* multilateral set-off mandatory for debtors ([Mondaq summary, 2011](https://mondaq.co.uk/eu-law/127460/act-on-prevention-of-late-payments-in-force-since-16-march-2011)). Current AJPES reports split reported value into *obvezni* (mandatory) and *prostovoljni* (voluntary) streams.
- Sources:
  - [Fleischman, Dini & Littera 2020, JRFM 13(12):295](https://www.mdpi.com/1911-8074/13/12/295)
  - [Fleischman & Dini 2021, JRFM 14(9):452](https://www.mdpi.com/1911-8074/14/9/452)

**Published scale (as cited by Fleischman et al. 2020 from AJPES 2002–2019) [V]**

| Year | Amount cleared | % of GDP | Participating companies |
|---|---|---|---|
| 2012 (crisis peak) | €683m | 1.89% | ~14,000 (8.3% of registered firms) |
| 2019 | €209m | 0.5% | ~2,700 (1.2%) |

**Internal inconsistency to flag [V].** The same authors elsewhere claim TCT reduces mutual indebtedness by "between 1% and 7.5% of GDP" ([JRFM 2021](https://www.mdpi.com/1911-8074/14/9/452)). This conflicts with their own AJPES-sourced peak of 1.89% in 2012. Treat "1–7.5% of GDP" as unsupported.

**2025 data, computed by me from AJPES monthly reports** ([AJPES, *Poročilo o večstranskem pobotu* 2025, PDF](https://www.ajpes.si/Doc/Bonitete/Pobot/Pobot-obvezni-Porocila_2025.pdf); text extracted locally) [V for the inputs; the derived ratios are my arithmetic]

| Month (as labelled) | Reported (*prijavljene*) € | Considered (*upoštevane*) € | Set off (*pobotan znesek*) € | Debtors reporting | % of debtors with any set-off |
|---|---|---|---|---|---|
| Jan | 206,405,225 | 36,965,240 | 4,052,362 | 1,028 | 57.5% |
| Feb | 206,814,195 | 35,968,287 | 4,022,266 | 1,035 | 55.4% |
| Mar | 190,038,896 | 32,815,697 | 4,864,840 | 1,054 | 58.9% |
| Apr | 208,017,424 | 36,660,345 | 6,366,611 | 1,043 | 60.5% |
| May | 208,860,765 | 34,135,772 | 4,994,529 | 1,036 | 56.8% |
| Jun | 209,013,027 | 37,457,107 | 5,085,884 | 1,009 | 58.9% |
| Jul | 196,237,082 | 32,096,807 | 4,853,606 | 967 | 56.0% |
| Aug | 212,609,197 | 34,026,581 | 5,965,279 | 978 | 58.5% |
| Sep | 195,446,130 | 33,346,296 | 4,625,645 | 990 | 60.8% |
| Oct | 189,299,323 | 31,315,805 | 5,177,294 | 969 | 59.0% |
| Nov | 199,091,256 | 32,193,024 | 4,088,277 | 983 | 56.3% |
| Dec | 188,534,684 | 30,953,908 | 3,757,248 | 936 | 58.1% |
| **2025 total** | **2,410,367,203** | **407,934,869** | **57,853,841** | — | — |

Derived ratios:
- set off ÷ reported ≈ **2.4%** (monthly range 1.9–3.1%)
- set off ÷ considered ≈ **14.2%** (range 11.0–17.5%)
- considered ÷ reported ≈ **16.9%**
- Mandatory reporting is about 62–70% of reported value in each month.

Caveats:
- (i) "Reported" amounts are monthly *stocks*. Unpaid obligations are probably re-reported month after month, so the annual sum double-counts. The *ratios* are the robust figures.
- (ii) The precise meaning of *upoštevane* (my translation: "considered" or "taken into account") was not confirmed from AJPES methodology [U]. It most likely means obligations eligible for the calculation, for example where the counterparty also participates.
- (iii) The €57.9m set off in 2025 is far below 2019's €209m. Participation has fallen to about 1,000 debtors a month.

**Implication.** Even with mandatory reporting and 35 years of operation, the national system clears a low single-digit percentage of reported overdue obligations. The binding constraint is participation and cycle density, not the algorithm.

#### g.2 Republika Srpska (Bosnia and Herzegovina): statutory trade-credit clearinghouse

[Božić & Zrnc (2022), "The Trade Credit Clearinghouse: Liquidity and Coordination", Croatian National Bank Working Paper W-66](https://api.hnb.hr/documents/20182/4279599/w-066.pdf/f3e50d7c-b476-7e82-fbe6-f68b2c93e9ee) [V, full text read]:

- **Legal basis:** the Multilateral Compensation Law of 2014, run by the Banja Luka Stock Exchange.
  - Clearing ran every six months, quarterly from 2017 and every two months from 2019.
  - Firms and government units *must* report late debts and may report debts that are not yet late.
- **Consent mechanism:** after a preliminary allocation, participants may withdraw individual debts. Cycles are then recomputed on the remaining debts and the second round is final. The paper calls participation voluntary on this basis. This is the closest existing analogue to a "consent-based clearing service".
- **Algorithm:** Simić & Milanović (1992), solved as a min-cost-flow problem with Google OR-Tools.
- **Scale (Oct 2015–Dec 2019):**
  - Late debt averages **9% of GDP** per clearing round (16% at the start, 8% at the end).
  - Firms and government clear about **0.6% of GDP per round, about 1.6% of GDP per year** (1.8% in 2015, 1.2% in 2019).
  - The total reduction in gross debt is about **8% of GDP** over the period.
  - About 12,000–15,700 participants per round, of which roughly 1,000–1,350 are cleared.
- **Topology:** typically one large strongly connected component of about 1,000 nodes, plus many nodes that cannot be cleared. The median cycle length is about 10, from an approximation using Johnson's algorithm.
- **Causal effects (instrumented with "outer-network" variation):**
  - Clearing lowers payment-default probability by about 6 percentage points, against a sample mean of about 11%. The effect is stronger for distressed and cash-poor firms.
  - It raises sales, and raises investment only for cash-rich firms.
  - Extrapolated, the aggregate default rate falls by 0.4 pp from about 7%.
  - The clearinghouse adds more value for firms in large or complex cycles, which supports a *coordination-failure* explanation. For simple three-firm triangles the effect is insignificant.

#### g.3 Sardex data: Fleischman, Dini & Littera (2020)

**Citation [V].** Fleischman, T., Dini, P. & Littera, G. (2020), "Liquidity-Saving through Obligation-Clearing and Mutual Credit: An Effective Monetary Innovation for SMEs in Times of Crisis", *Journal of Risk and Financial Management* 13(12): 295, published 27 Nov 2020.
- [MDPI](https://www.mdpi.com/1911-8074/13/12/295) · [LSE eprint 107529](https://eprints.lse.ac.uk/107529/)
- Littera is a Sardex co-founder, and Fleischman is linked to Be Solutions/TCT. Both have a commercial interest.

**Reported results [V].**
- On real Sardex invoice data, obligation-clearing alone reduces **net internal debt of the obligation network by ≈25%**. Combined with mutual credit as a liquidity source, the reduction is **≈50%**.
- The data cover over 138,000 transactions from 3,199 firms worth more than €31m, per the [RAMICS conference note](https://ramics.org/2021/02/27/conference-liquidity-saving-through-obligation-clearing-and-mutual-credit/).
- The authors treated Sardex credits as euros and *simulated* the mutual-credit layer.

**Limitations.**
- Sardex is a closed regional circuit whose rules push members to keep balances near zero and trade inside the network. That raises cycle density compared with an open economy.
- 25% is a result for one network, not a general clearable fraction.
- The companion paper ([Fleischman & Dini 2021](https://www.mdpi.com/1911-8074/14/9/452)) proves that clearing always reduces debt when the network has cycles, but explicitly does not address what "significant" means.

#### g.4 Cycles (Informal Systems spin-out)

**Papers [V]**
- Buchman, Dini, Ahmed, Miller & Fleischman (2025), ["Cycles Protocol: A Peer-to-Peer Electronic Clearing System"](https://arxiv.org/abs/2507.22309), arXiv 2507.22309, 30 July 2025. Open, decentralised clearing, settlement and issuance based on graph optimisation, with privacy-preserving multilateral settlement. The abstract claims "liquidity resides within cycles", with no empirical percentages.
- Fleischman & Buchman (2026), ["Deepening the Secondary Market: Integrating Trade Credit into Market Clearing with the Cycles Protocol"](https://arxiv.org/abs/2605.02436), arXiv 2605.02436, 4 May 2026.
  - Proposes a compression layer between clearing members and CCPs, and bringing trade credit into formal settlement.
  - Stresses that Cycles does *not* redistribute counterparty risk (set-off, not novation).
  - The abstract reports no empirical clearing percentages.

**What it does [V].** Bilateral obligations are mutually approved by counterparties. At clearing time, closed loops and nettable positions are found inside a TEE with ZK proofs, and obligations are discharged by atomic multilateral set-off. Version 1 clears existing debts only and creates no new debt. Sources: [cycles.money/prime](https://cycles.money/prime) and [arXiv 2507.22309](https://arxiv.org/abs/2507.22309).

**Company and funding [V].**
- Cycles Protocol SA, Lausanne, Switzerland; CEO Ethan Buchman (Cosmos co-founder); Principal Scientist Tomaž Fleischman.
- **$6.4m raised on 21 May 2026**, led by Blockchange Ventures with Coinbase Ventures, Compound VC and Primitive Ventures. This brings total funding to **$8.7m**, after a $2.3m pre-seed in 2025.
- Sources: [press release](https://yellow.com/press-releases/cycles-raises-6-4m-to-build-the-open-clearing-network-for-on-chain-finance) and [about page](https://cycles.money/about).

**Products and status [V].**
- **Cycles Prime:** private OTC obligation netting for crypto trading firms, launching with **Lynq and FalconX** as anchor or pilot partners.
- **Cycles Pay:** stablecoin payments and invoicing for SMEs, including receivables-based financing.
- In practice the go-to-market has moved crypto-first. No SME trade-credit pilot with published results was found [U].

**Related UK partner [V].** Mutual Credit Services, a UK social franchise founded in 2020, states that it is "working closely with Informal Systems (the developers of an improved version of TETRIS called MTCS)" to offer multilateral set-off through a "Clearing Clubs" platform ([MCS](https://www.mutualcredit.services/multilateral-obligation-set-off)). No live volumes were found [U].

#### g.5 Other services and schemes

| Scheme | Status and key facts | Source |
|---|---|---|
| **Credit Commons** | Protocol for federating mutual-credit ledgers; white paper by Matthew Slater & Tim Jenkin (**2016**). The Credit Commons Society governs it. A reference implementation was built around 2020. | [White paper PDF (dated 2016)](http://creditcommons.org/assets/credit-commons.pdf) [V] |
| **Open Credit Network (UK)** | National UK mutual-credit network co-founded by Dil Green and Oli Sylvester-Bradley (Open.coop), with Dave Darby (Lowimpact). Described as "new" in April 2020. One co-founder wrote in March 2026 that "the OCN failed". | [Lowimpact 2020](https://www.lowimpact.org/posts/alternative-money-system-tim-jenkin-matthew-slater-dil-green); [Resilience 2026](https://www.resilience.org/stories/2026-03-12/new-tools-for-growing-the-commons-and-how-i-discovered-them/) [V]; exact founding date [U] |
| **Sardex (Sardinia, Italy)** | B2B mutual-credit circuit. €51.2m transaction volume in 2015; more than 212m units by 2017 (cumulative or annual unclear). SardexPay later announced a cumulative €1bn transacted; date [U]. | [Littera et al. (Unibo)](https://cris.unibo.it/retrieve/e1dcb333-5cdd-7715-e053-1705fe0a6cc9/littera_sartori_dini_antoniadis_From%20an%20Idea%20to%20a%20Scalable%20Working%20Model.pdf); [Monneta](https://monneta.org/en/sardex); [SardexPay](https://www.sardexpay.net/news/il-primo-miliardo-di-sardex) [V] |
| **WIR (Switzerland)** | B2B complementary currency, WIR Bank since 2004 according to Fleischman et al. Founded 1934 [K]. It is mutual credit, not trade-credit set-off. | [Fleischman et al. 2020](https://www.mdpi.com/1911-8074/13/12/295), footnote 2 [V] |
| **Romania (Ministry of Economy)** | Gavrila & Popa (2020/21): an algorithm for clearing obligations between companies in a Romanian Ministry of Economy application. Fleischman & Dini note it "does not identify all cycles". | [arXiv 2012.05564](https://arxiv.org/abs/2012.05564v1) [V] |
| **Byppay ("path-enabled compensation")** | Vendor method that clears along open chains, producing a "settlement-instruction layer" (in effect, redirected payment instructions). Preprint (3 Jun 2026) on the "2021 IMI invoice corpus": 133,191 invoices worth €19.67bn. Cycle-only netting gives **20.99%** debt relief; Byppay gives **53.87%**. The corpus's country and provenance are not stated [U]. | [arXiv 2606.26126](https://arxiv.org/abs/2606.26126); [Research Square DOI 10.21203/rs.3.rs-9838159/v1](https://europepmc.org/article/PPR/PPR1241774) [V] |
| **Croatia, Bulgaria, other Italian schemes** | Not verified in this session. Croatian FINA multilateral set-off and Bulgarian schemes are mentioned anecdotally elsewhere. | [U] |
| **UK statutory or public obligation clearing** | None found. | [U — absence of evidence] |

**Note on Byppay.** "Path-enabled" reduction (A→B→C becomes A pays C directly) is legally an assignment or novation of payment rights, or a payment direction. It is not a set-off of mutual debts. It needs counterparty consent and has different insolvency and regulatory consequences. Comparing 54% with 21% is therefore comparing different legal acts.

#### g.6 Academic estimates of clearable fraction and topology

| Setting | Clearable or cleared share | Source |
|---|---|---|
| Sardex (closed circuit) | ≈25% of net internal debt; ≈50% with mutual credit | Fleischman et al. 2020 [V] |
| Slovenia, 2025 actual | ≈2.4% of reported, ≈14% of "considered" | AJPES; my calculation [V] |
| Republika Srpska, 2015–19 | ~0.6% of GDP per round vs ~9% of GDP late debt (≈7%) | Božić & Zrnc 2022 [V] |
| IMI corpus (2021) | 21% cycle-only | de la Rosa Esteva & Madugula 2026 [V] |
| Slovakia (public sector included) | Including taxes and government increases clearing (qualitative) | Gazda et al. 2015, as summarised by Fleischman & Dini 2021 [V for the summary; primary not read] |

**Topology drivers.**
1. **Reciprocity is low** in real production networks: about 4.6% in Ecuador (2015), 4–9% in Hungary depending on the threshold, and about 2% in FactSet ([Bacilieri, Borsos, Astudillo-Estévez, Hoefer & Lafond 2026, JEDC 187:105313](https://ora.ox.ac.uk/objects/uuid:21f006d7-4273-4f28-b81a-d18cd6af97e8)) [V]. Bilateral netting alone is therefore small, and clearing depends on long cycles.
2. **The strongly connected core is a minority of firms.** In Republika Srpska it was about 1,000 of 12,000–16,000 participants [V].
3. **Participation is the main lever.** Fleischman et al. argue that clearing would be "much larger" with 50% participation [V; this is the authors' conjecture].
4. **Exports and imports leak out of national cycles.** Slovenian exports are about 80% of GDP (Fleischman et al.).
5. **Long-standing very-late debts rarely clear**, because insolvent firms lack offsetting receivables (Republika Srpska) [V].

**Genuinely open.** No published, pre-registered model *predicts* the clearable fraction from cheap observable statistics and is validated across several real datasets. Candidate predictors include reciprocity, the share of firms in the largest strongly connected component, the weight of the cycle space, and the participation rate. Fleischman & Dini 2021 explicitly leave "significant" undefined.

### (h) Firm-network stylised facts and UK late payment

**Belgium (NBB B2B VAT network).**
- Bernard, Dhyne, Magerman, Manova & Moxnes (2022), "The Origins of Firm Heterogeneity: A Production Network Approach", *JPE* 130(7): 1765–1804 ([journal page](https://www.journals.uchicago.edu/doi/abs/10.1086/719759)).
- Degree statistics from the working-paper version, 2014 data ([NBER w25441](https://www.nber.org/system/files/working_papers/w25441/w25441.pdf)) [V]:
  - Customers per seller: mean **29.3** (sd 394), median **4**.
  - Suppliers per buyer: mean **20.6** (sd 49.5), median **9**.
  - The top 1% of firms have more than 400 buyers and more than 177 suppliers.
  - The JPE version may differ slightly [U].
- Later NBB data, 2002–2021 ([NBB WP 444](https://www.nbb.be/doc/ts/publications/wp/wp444en.pdf)) [V]:
  - Buyers: mean 36, median 5.
  - Domestic suppliers: mean 26, median 12.
  - Transactions grew from 7.8m (2002) to 13.9m (2021).

**Japan (TSR).**
- Carvalho, Nirei, Saito & Tahbaz-Salehi (2021), "Supply Chain Disruptions: Evidence from the Great East Japan Earthquake", *QJE* 136(2): 1255–1321 [V via citation].
- The data cover about **1 million firms**. Each firm self-reports up to 24 suppliers and 24 customers, and links are completed with partners' reports ([working-paper version](https://bepp.wharton.upenn.edu/wp-content/uploads/2017/02/AE-S17-Tahbaz-Salehi.pdf)) [V].
- The TSR data are binary, with no yen values.
- Mean and median degree from the QJE paper: [U, not extracted].

**Reciprocity and cycles.** See Bacilieri et al. 2026 above [V]. Hungary's VAT network (Reisch et al.) covers 711,248 firms and 38.6m links over 2014–2022; 55% of supply links disappear within a year, with a half-life of 13 months ([IDEAS](https://ideas.repec.org/p/arx/papers/2503.20594.html)) [V].
- *Relevance:* obligation graphs churn quickly, so monthly clearing has to work on a moving graph.

**UK late payment, 2024–2026 [V].**
- **Research for DBT and the Small Business Commissioner** (London Economics, published 15 July 2025): about **£26bn** of late payments is outstanding at any time, about £17,000 per affected business. Late payment costs about **£11bn a year** and is linked to about **14,000 business closures a year**. Firms spend 86 hours a year chasing late payments, about 133m hours in total ([SBC research page](https://www.smallbusinesscommissioner.gov.uk/?p=64916); [consultation response](https://www.gov.uk/government/consultations/late-payments-tackling-poor-payment-practices/outcome/late-payment-consultation-time-to-pay-up-government-response-web-version)).
  - The £26bn figure echoes a 2017 government estimate of £26.3bn.
- **"Time to Pay Up"** was launched on 31 July 2025. The consultation ran to 23 October 2025, and the government response was published on 24 March 2026. A **45-day cap was consulted on but is not being taken forward now**.
- **Commercial Payments Bill [HL]** ("Small Business Protections Bill"):
  - Introduced on 19 May 2026 ([GOV.UK](https://www.gov.uk/government/news/largest-crackdown-on-late-payments-in-over-25-years-as-landmark-bill-enters-parliament)).
  - Measures: a **60-day cap** on payment terms for large firms paying smaller suppliers; *mandatory* statutory interest (8% over base, with no contracting out); a fixed 30-day maximum for public bodies; a construction retentions ban; and **SBC powers to investigate, adjudicate and fine** (fines "worth tens of millions").
  - Status: Lords report stage completed on 15 Sept 2026, with third reading listed for 20 Oct 2026. It is **not law**, and the government says the 60-day cap will start no earlier than 2027 ([Adfin, 12 Oct 2026](https://adfin.com/information/the-uk-late-payment-reforms-what-has-been-decided-and-what-has-not); [Parliament bill page](https://bills.parliament.uk/bills/4128/stages)).
  - The government also says "late payments close 38 businesses every single day".
- **Average UK payment days:** not collected in this pass [U].

### (i) UK law for a consent-based clearing service that holds no funds

1. ***British Eagle International Air Lines Ltd v Compagnie Nationale Air France* [1975] 1 WLR 758 (HL)** [V for the summary; full judgment not read].
   - **Facts and holding:** British Eagle went into liquidation. Under the IATA clearing house it was a net debtor to the clearing house but a creditor of Air France. A 3–2 majority held that the clearing arrangement could not displace the statutory pari passu distribution: the liquidator could recover Air France's debt directly. Contracting out of the insolvency distribution scheme is contrary to public policy.
   - **Australian sequel:** IATA redrafted its rules so that airlines are not debtors and creditors of each other, only of IATA. The High Court of Australia upheld the revised scheme in *IATA v Ansett Australia Holdings Ltd* [2008] HCA 3 ([HCA](https://www.hcourt.gov.au/cases-and-judgments/judgments/judgments-1998-current/international-air-transport-association-v-ansett-australia-holdings-limited)) [V]. The majority size (reported as 6:1) is [U].
   - **English sequel:** *Belmont Park v BNY Corporate Trustee Services* [2011] UKSC 38 confirmed the anti-deprivation rule and pari passu principle as distinct, and upheld commercially justified flip clauses [K].
   - **Implication:** a multilateral netting agreement that has not been executed does not bind a liquidator. Structuring through a central counterparty would avoid *British Eagle*, but would make the operator a credit intermediary bearing counterparty risk. That is precisely what a "holds no funds" model wants to avoid.
2. **Insolvency set-off: [IR 2016 r.14.25](https://www.legislation.gov.uk/uksi/2016/1024/rule/14.25)** [V].
   - Automatic and mandatory in liquidation, and limited to "mutual dealings between the company and a creditor". Mutuality means the same parties in the same capacity, so multi-party (triangular) set-off is excluded.
   - Debts incurred with notice of a pending winding-up petition or a creditors' decision are excluded, as are debts acquired by assignment after those trigger points.
   - Administration has a parallel rule (r.14.24) [K].
   - *Re BCCI (No 8)* [1998] AC 214 is the leading authority on mutuality [K].
3. **Preferences, s.239 Insolvency Act 1986** [K].
   - A set-off that discharges debts *before* insolvency is generally a completed discharge. It can be challenged if, within 6 months (2 years for connected persons) before onset, an insolvent company "was influenced by a desire" to put a creditor in a better position.
   - **Mechanism risk:** in a cycle A→B→C→A, clearing effectively pays A's creditor B using A's asset, its claim on C.
   - The subjective "desire" test (*Re MC Bacon* [1990] BCLC 324 [K]) makes successful challenges uncommon for arm's-length automated clearing, but the risk is real for connected-party cycles.
   - **More acute: s.127 IA 1986** makes dispositions of company property after a winding-up petition is presented void unless the court validates them. A monthly clearing run should screen out any participant with a pending petition, for example by checking The Gazette [K].
   - **Also check:** CIGA 2020 s.233B (ipso facto ban). It applies to contracts for the supply of goods or services, so whether a clearing membership agreement can be terminated on insolvency is uncertain [U].
4. **Settlement Finality Regulations 1999 (SI 1999/2979) and Companies Act 1989 Part VII** [V/K].
   - **SFRs:** protect transfer orders, netting and collateral in *designated* systems, designated by the Bank of England (originally the FSA for some systems), against insolvency rules including the *British Eagle* effect ([legislation.gov.uk](https://www.legislation.gov.uk/uksi/1999/2979)).
   - **Who can participate:** credit institutions, investment firms, public authorities, CCPs, settlement agents, clearing houses and system operators. A 2017 amendment extended this to non-bank payment institutions ([A&O Shearman note](https://finreg.aoshearman.com/uk-legislation-published-on-payment-services-and-)). Trade-credit SMEs cannot be participants, and invoices are not "transfer orders" under these rules.
   - **CA 1989 Part VII:** protects "market contracts" and default rules of recognised investment exchanges, recognised clearing houses and CCPs [K].
   - **Bottom line:** neither regime is available to an unrecognised SME clearing service.
5. **Payment Services Regulations 2017** ([Schedule 1](https://www.legislation.gov.uk/uksi/2017/752/schedule/1)) [V].
   - **Part 1 list:** cash placement and withdrawal, *execution of payment transactions*, issuing and acquiring, money remittance, payment initiation services (PIS) and account information services (AIS).
   - **Relevant Part 2 exclusions:** (h) transactions within a payment or securities settlement system between PSPs, settlement agents, CCPs, clearing houses and similar; (j) technical service providers that support payment services "without … entering at any time into possession of the funds"; (k) limited network.
   - **Analysis:** a service that only *computes* multilateral offsets and issues set-off notices — no funds received, no transfers executed, no payment instructions initiated — does not obviously fall within Part 1. Discharge by set-off is not a "transfer of funds" [analysis, not authority].
   - **Where the risk lies:** at the edges. Collecting residual balances (money remittance or account operation), initiating residual payments from users' bank accounts (PIS), or reading bank data (AIS) would each bring the service into scope.
   - **PERG 15:** no specific PERG 15 Q&A on netting or set-off services was found ([PERG 15.2](https://www.handbook.fca.org.uk/handbook/PERG/15/2.html), [15.3](https://www.handbook.fca.org.uk/handbook/PERG/15/3.html) reviewed) [U]. PERG 15.3 does note that acquiring can exist "where there is no actual transfer of funds … because another form of settlement is agreed". The FCA therefore looks at substance, which is a caution.
6. **Electronic Money Regulations 2011** [K]. E-money requires stored monetary value that represents a claim on the issuer, is issued on receipt of funds and is accepted by third parties.
   - Pure set-off creates no stored value and no claim on the operator, so it is not e-money.
   - Adding a mutual-credit unit (the Sardex-style "liquidity source") changes the analysis: closed-loop or limited-network questions arise.
   - **LNE notification:** under PSRs 2017 reg 38, notification is required once LNE transactions exceed €1m in any 12-month period ([reg 38](https://www.legislation.gov.uk/uksi/2017/752/regulation/38)) [V].
7. **VAT** [partially V].
   - Set-off does not change the VAT due on the underlying supplies. Each supply is taxed at its own time of supply and value.
   - Under the Cash Accounting Scheme, VAT is accounted for when payment is received or made. [VAT Notice 731](https://www.gov.uk/guidance/vat-cash-accounting-scheme-notice-731) para 5.9 treats payment in kind (barter or part exchange) as "payment" on the date the consideration is received.
   - Notice 731 does not mention set-off explicitly. Treating the set-off date as the payment date is an inference [U — confirm with HMRC manuals].
8. **UK precedent for contractual multilateral set-off upheld before insolvency:** none found in this session [U].
   - Contractual set-off and netting among solvent parties is ordinary freedom of contract [K]. Intra-group netting agreements are common practice.
   - What is untested is enforceability against an insolvency officeholder, and *British Eagle* answers that negatively.
   - Practical design implication, borrowed from Republika Srpska: **per-cycle confirmation (two-round opt-out)**, execution only among currently solvent, non-petitioned participants, immediate finality of each executed cycle, and no unexecuted netting obligations carried forward.

### (j) AI-designed economic mechanisms

| Work | Citation | Accomplishment | Limitation |
|---|---|---|---|
| Zheng, Trott, Srinivasa, Parkes & Socher, "The AI Economist" | arXiv 2004.13332 (2020) [K]; *Science Advances* 8(18): eabk2607 (2022), DOI [10.1126/sciadv.abk2607](https://www.science.org/doi/10.1126/sciadv.abk2607) [V] | Two-level deep RL in which agents and a tax planner co-adapt. Recovers the optimal tax in one-step economies and improves the equality–productivity trade-off in a gather-and-build simulation. | Simulated agents only; welfare depends on the simulator. |
| Koster et al., "Human-centred mechanism design with Democratic AI" | *Nature Human Behaviour* 6: 1398–1407 (2022), DOI [10.1038/s41562-022-01383-x](https://www.nature.com/articles/s41562-022-01383-x) [V] | RL designs a redistribution rule for a public-goods game that wins a majority vote of human players. It redresses wealth imbalance and sanctions free riders. | Lab game; majority-vote objective. |
| Dütting, Feng, Narasimhan, Parkes & Ravindranath, RegretNet | ICML 2019 (PMLR 97: 1706–1715) [V via citation]; extended version "Optimal Auctions through Deep Learning: Advances in Differentiable Economics" ([arXiv 1706.03459v6](https://arxiv.org/abs/1706.03459v6)) [V]; JACM 2024 publication details [U] | Neural networks learn near-optimal, approximately incentive-compatible multi-item auctions. Recovers known analytical solutions. | Only approximate incentive compatibility (regret); hard to interpret. |
| Liu, Guo & Conitzer, "An Interpretable Automated Mechanism Design Framework with Large Language Models" | [arXiv 2502.12203](https://arxiv.org/abs/2502.12203) (16 Feb 2025) [V] | LLM-generated mechanisms as code, evolved with a fixing step that enforces strategy-proofness and individual rationality. Rediscovers Myerson's auction and interprets RegretNet. | Small settings. |
| Dütting, Mirrokni, Paes Leme, Xu & Zuo, "Mechanism Design for Large Language Models" | [arXiv 2310.10826](https://arxiv.org/abs/2310.10826) [V] | Token-level auctions among LLM agents. | Concerns ad content, not allocation. |
| AlphaEvolve (Google DeepMind) | [arXiv 2506.13131](https://arxiv.org/html/2506.13131v1) [V] | LLM plus evolutionary code search on machine-gradeable problems. Includes a data-centre scheduling heuristic. | Not mechanism design as such; needs an automatic evaluator. |
| "Deep mechanism design" perspective (DeepMind authors) | [PNAS 2025, DOI 10.1073/pnas.2319949121](https://www.pnas.org/doi/10.1073/pnas.2319949121) [V] | States that AI-designed mechanisms remain "largely at a proof-of-concept stage". | — |

**Open space.** "An AI designs a mechanism" is no longer novel. A narrow open slot remains: LLM- or evolution-designed *clearing and allocation rules with hard constraints* (net-position preservation, per-cycle consent, individual rationality) that are evaluated on *real* obligation or compute data rather than synthetic agents.

### (k) Agent payment and settlement protocols (status October 2026)

| Protocol | What it does | Status | Netting or credit? |
|---|---|---|---|
| **Google AP2** (Agent Payments Protocol) | Cryptographically signed "mandates" prove that a user authorised an agent's purchase. Payment-method agnostic. Announced Sept 2025 with 60+ partners. x402 is described as its stablecoin settlement extension. | Partners listed; maturity described in vendor sources only [U] ([BIIA summary](https://www.biia.com/visa-mastercard-and-stripe-back-open-standard-letting-ai-agents-pay-autonomously/)) | No netting. Security analyses flag "whisper attacks" ([arXiv 2609.11757](https://arxiv.org/pdf/2609.11757)). |
| **OpenAI/Stripe ACP** (Agentic Commerce Protocol) | Powers ChatGPT Instant Checkout. Merchants accept orders through ACP; payment uses Stripe Shared Payment Tokens or a Delegated Payments Spec. | Live in the US since launch ([OpenAI](https://openai.com/index/buy-it-in-chatgpt/)) [V] | No netting. SPTs are single-use and bound to merchant and amount. |
| **Coinbase x402** | HTTP 402-based pay-per-request; v2 uses standard headers and CAIP chain IDs. Schemes: `exact`, `upto`, `batch-settlement` (launched 11 May 2026) and `auth-capture`. | Contributed to the Linux Foundation's **x402 Foundation**: intent announced 2 Apr 2026, operational launch on **14 Jul 2026** with 40 members including AWS, Google, Visa, Mastercard, Stripe, Amex and Circle ([LF](https://www.linuxfoundation.org/press/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications)) [V] | `batch-settlement` puts a one-time escrow deposit behind off-chain cumulative vouchers, redeemed in batches. This is **bilateral channel aggregation**, and the abstract spec permits "capital-backed or credit-backed commitments" ([docs](https://docs.x402.org/schemes/batch-settlement)) [V]. **No multilateral netting.** |
| **Stripe/Tempo MPP** (Machine Payments Protocol) | Open standard co-authored by Tempo and Stripe. An agent requests a resource, the service returns a payment request, and the agent authorises it. Supports stablecoins, cards and BNPL through SPTs. | Launched **18 Mar 2026** with Tempo mainnet ([Stripe](https://stripe.com/blog/machine-payments-protocol)) [V]. Visa extended it to cards (reported). | Sessions with pre-authorised limits and aggregated settlement. No multilateral netting. |
| **Visa Intelligent Commerce / Trusted Agent Protocol** | TAP (14 Oct 2025) lets merchants verify agent identity through signed HTTP messages. Designed to complement ACP and to align with x402. | Announced; early-stage for banks and merchants ([Visa](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-unveils-trusted-agent-protocol-for-ai-commerce.html)) [V] | No netting or credit innovation. |
| **Mastercard Agent Pay** | Agentic tokens with issuer controls. Announced Apr 2025. | All European issuers enabled at network level (June 2026). "Agent Pay for Machines" launched **10 Jun 2026** with "guaranteed multi-rail settlement" across cards, accounts and stablecoins; Aave is quoted as the "credit layer". Trust and intelligence services added 30 Sep 2026 ([MC Machines](https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-launches-agent-pay-for-machines.html), [MC Europe](https://www.mastercard.com/news/europe/en/perspectives/en/2026/europe-is-building-the-foundations-for-trusted-agentic-commerce/)) [V] | Credit through issuers and an Aave partnership. **No multilateral netting described.** |

**Open space.** None of these protocols offers multilateral netting of agent-to-agent obligations. The open question is empirical: **do agent economies generate cycles at all?** Agent spending looks hub-and-spoke (agents pay API and tool providers), which predicts low cyclicity and little netting gain. That is a falsifiable, cheap simulation question, and may give a negative result.

### (l) Stochastic wealth inequality

- **Bouchaud & Mézard (2000)**, "Wealth condensation in a simple model of economy", *Physica A* 282(3–4): 536–545 [K, title verified via citation].
  - Multiplicative random returns plus exchange give Pareto tails.
  - When exchange is weak relative to return noise, a phase transition produces "condensation", where a finite number of agents hold a finite share of wealth.
- **Yard-sale and affine wealth model**
  - Boghosian, Devitt-Lee, Johnson, Li, Marcq & Wang (2017), "Oligarchy as a phase transition: the effect of wealth-attained advantage in a Fokker–Planck description of asset exchange", *Physica A* 476: 15–37 [V].
  - Li, Boghosian & Li (2019), "The Affine Wealth Model…", *Physica A* 516: 423–442 [V].
  - Without redistribution, the yard-sale model drives the Gini coefficient to 1 (complete oligarchy).
  - Redistribution gives Pareto-like steady states, and wealth-attained advantage above a critical bias gives an oligarchy phase transition.
  - The affine model allows negative wealth and fits US wealth data.
- **Berman, Peters & Adamou**, "Wealth inequality and the ergodic hypothesis: evidence from the United States" (arXiv 1605.05238; final venue [U]) [K].
  - Fits a reallocating geometric Brownian motion to US data.
  - Estimates a *negative* effective reallocation rate in recent decades, implying no stationary wealth distribution.
- **Relevance.** Any simulation of credit or clearing networks with multiplicative dynamics needs an explicit redistribution or reallocation parameter. Otherwise condensation is the default outcome, not a finding.

### (m) Space-resource law

| Instrument | What it says on resources vs territory | Status |
|---|---|---|
| **Outer Space Treaty 1967, Art. II** | Outer space, including the Moon and celestial bodies, "is not subject to national appropriation by claim of sovereignty, by means of use or occupation, or by any other means". Silent on extracted resources. | [K] |
| **Moon Agreement 1979** | Declares the Moon and its resources the "common heritage of mankind" and envisages an international regime for exploitation. | **17 parties.** Signatories that have not ratified: France, Guatemala, India and Romania. Saudi Arabia withdrew with effect from 5 Jan 2024 ([UN Treaty Collection, status at 16 Oct 2026](https://treaties.un.org/pages/ViewDetails.aspx?src=TREATY&mtdsg_no=XXIV-2&chapter=24&clang=_en)) [V] |
| **US Commercial Space Launch Competitiveness Act 2015, Title IV** (51 U.S.C. §51303) | A US citizen engaged in commercial recovery of an asteroid or space resource "shall be entitled to any asteroid resource or space resource obtained", including to possess, own, transport, use and sell it. §403 disclaims US sovereignty or ownership of any celestial body. | [K] |
| **Luxembourg, Law of 20 July 2017** | Art. 1: "space resources are capable of being appropriated" in accordance with international law. No sovereignty over territory. | [V] ([Ministry of the Economy](https://meco.gouvernement.lu/fr/actualites.gouvernement2024+fr+actualites+toutes_actualites+communiques+2016+11-novembre+11-presentation-spaceresources.html)) |
| **UAE** | Federal Law No. 12 of 2019 covers space resource activities. It was **repealed by Federal Decree-Law No. 46 of 2023** (Art. 8 covers space resources). The Space Resources Regulations (Cabinet Resolution) allow operators to "exercise ownership rights … over any Space Resources" they extract under authorisation. | [V] ([2023 law](https://uaelegislation.gov.ae/en/legislations/2129/download); [regulations](https://uaelegislation.gov.ae/en/legislations/1634/archived)) |
| **Japan, Act No. 83 of 2021** | Art. 5: a permitted operator acquires ownership of the space resources it extracts under an approved plan. In force 23 Dec 2021. | [V] ([LoC](https://www.loc.gov/item/global-legal-monitor/2021-09-15/japan-space-resources-act-enacted/); [JLT](https://www.japaneselawtranslation.go.jp/en/laws/view/4816)) |
| **Artemis Accords (2020)** | Non-binding. Extraction of space resources "does not inherently constitute national appropriation" under OST Art. II (Section 10) [K]. Provides for "safety zones". | **76 signatories**; San Marino was the 76th, on 25 Sep 2026 ([State Dept](https://www.state.gov/bureau-of-oceans-and-international-environmental-and-scientific-affairs/artemis-accords); [NASA](https://www.nasa.gov/news-release/nasa-celebrates-as-artemis-accords-surpasses-75-signatories/)) [V] |

**Open space.** Ownership of *extracted* resources is settled in five national laws and the Artemis framework. Ownership of territory is prohibited. Tradeable *future* resource claims have no enforceable underlying asset and no way to test them cheaply. Treat this as low-priority speculation.

### (n) Compute markets

- **CME compute futures** [V].
  - Silicon Data H100 Rental Index Futures (GPU1) and B200 Rental Index Futures (GPU2) on NYMEX: 730 GPU-hours per contract, cash-settled, monthly contracts listed 36 months out, settled against Silicon Data daily indices (Bloomberg SDH100RT and SDRB200RT).
  - Announced 11 Aug 2026 for a trade date of **5 Oct 2026**, "pending all relevant CFTC regulatory review periods" ([SER-9785](https://www.cmegroup.com/content/dam/cmegroup/notices/ser/2026/08/ser-9785.pdf)).
  - **Update, 25 Sep 2026 (SER-9785R): "The Exchange will further advise regarding the specific effective date"** ([SER-9785R](https://www.cmegroup.com/content/dam/cmegroup/notices/ser/2026/09/ser-9785r.pdf)). As of 17 Oct 2026 the contracts are **not trading**.
  - On 15 Oct 2026 CME started distributing *non-tradable* Silicon Data forward curves. These have been live since 20 Apr 2026, project 36 months out, and put mid-October H100 rental at about $2.53–2.81/GPU-hr and B200 at about $5.45–6.01 ([Crypto Briefing](https://cryptobriefing.com/cme-group-gpu-rental-forward-curve-pricing/)).
- **ICE/Ornn** [V]. Cash-settled GPU futures on Ornn's Compute Price Index (OCPI; H100, H200, B200, RTX 5090) were announced on 19 May 2026, subject to regulatory approval; no launch was found ([ICE](https://ir.theice.com/press/news-details/2026/ICE-and-Ornn-to-Launch-GPU-Compute-Futures-Contracts/default.aspx)). Ornn reports a first compute swap using cleared prices in Dec 2025.
- **Architect/Ornn** [V]. Exchange-traded GPU and DRAM futures on AX (Bermuda) were announced 21 Jan 2026, pending approval; perpetuals are reportedly live ([PR Newswire](https://www.prnewswire.com/news-releases/architect-financial-technologies-partners-with-compute-index-provider-ornn-to-launch-exchange-traded-futures-on-gpu-and-ram-prices-302666613.html)).
- **Other indices** [V]. CF Benchmarks GPU Rental Series ([methodology PDF](https://docs.cfbenchmarks.com/CF%20GPU%20Rental%20Series%20Methodology%20Guide.pdf)). Setara Financial (Chicago) offers a "Normalized Compute Unit (NCU™)" with a "pre-production" Class C series built from public list prices ([methodology](https://www.setarafinancial.com/methodology)).
- **MLPerf as a hardware×workload throughput source** [V].
  - Inference v6.0 (1 Apr 2026) and v6.1 (16 Sep 2026, a record 30 submitters, adding agentic and end-to-end RAG tests).
  - Training v6.0 (16 Jun 2026, adding DeepSeek-V3 671B and GPT-OSS 20B).
  - Each repository includes `summary_results.json` (see Part 3).
  - **Limitations:** vendor-optimised submissions, uneven coverage of accelerators, no price data, and frequent benchmark churn.
- **Open space.** A public, reproducible, workload-specific exchange rate between accelerators, derived from MLPerf throughput and tested *out of sample* against the ratio of market rental indices (Silicon Data, Ornn and CF). This is cheap, falsifiable and adjacent to Setara's proprietary NCU. Novelty depends on being open and on the out-of-sample test.

---

## Part 2 — Fact check of earlier AI-written claims

| # | Claim | Verdict | Correction and source |
|---|---|---|---|
| 1 | BoE systemic sterling stablecoins: 40% unremunerated BoE deposits + 60% short-term gilts; issuers prohibited from paying interest; £40bn temporary issuance guardrail; holding limits | **PARTLY TRUE (outdated)** | 40/60 and holding limits (£20k for individuals, £10m for businesses) were the **Nov 2025 proposals**. The **22 June 2026 policy statement**: ≥**30%** unremunerated BoE deposits and up to **70%** gilts of ≤6 months (up to 95% gilts at launch for issuers systemic at launch); holding limits **dropped** in favour of a temporary **£40bn issuance guardrail** per stablecoin; **interest to coinholders prohibited**; Code of Practice to be finalised by end-2026, operations from 2027. [BoE](https://www.bankofengland.co.uk/news/2026/june/boe-launches-policy-statement-and-draft-rules-on-regulating-systemic-stablecoins); [Eversheds](https://www.eversheds-sutherland.com/en/united-kingdom/insights/uk-bo-e-finalises-systemic-stablecoin-regime) |
| 2 | FCA cryptoasset regime goes live October 2027 | **TRUE** | Most provisions of the FSMA 2000 (Cryptoassets) Regulations apply from **25 Oct 2027**. FCA final rules 30 Jun 2026 and gateway open 30 Sep 2026 are reported by law firms. [Linklaters](https://financialregulation.linklaters.com/post/102lxrd/uk-makes-milestone-law-to-regulate-cryptoassets); [Gherson](https://www.gherson.com/blog/uk-cryptoasset-regulation-2026-legal-update/) |
| 3 | PS23/6 (Oct 2023): 24-hour cooling-off and referral-bonus ban | **TRUE** | In force 8 Oct 2023. 24-hour cooling-off for first-time investors, running from the request to view a direct offer; a ban on incentives to invest, including refer-a-friend bonuses; plus appropriateness tests and risk warnings. [FCA PS23/6](https://www.fca.org.uk/publication/policy/ps23-6.pdf) |
| 4 | PSRs 2017 limited network exclusion and €1m notification threshold | **TRUE** | Reg 38: notify the FCA if LNE transactions exceed **1 million euros** in any 12 months. [legislation.gov.uk](https://www.legislation.gov.uk/uksi/2017/752/regulation/38) |
| 5a | LURA 2023 replaced the 4-year enforcement rule with a 10-year rule | **TRUE (England only)** | s.115 amends TCPA 1990 s.171B, in force **25 Apr 2024**; all breaches are now on 10 years. Wales keeps 4 years. [SI 2024/452](https://www.legislation.gov.uk/uksi/2024/452/made) |
| 5b | An "August 2026 NPPF" sets 40 dwellings/ha near transport hubs, with a grey-belt presumption | **PARTLY TRUE** | The NPPF was published **17 Aug 2026** ([GOV.UK](https://www.gov.uk/government/publications/national-planning-policy-framework--2)). The **draft** proposed 40–50 dph; the **final** sets a minimum of **35 dph near qualifying stations, rising to 45 dph** for higher-frequency stations (secondary sources: [Planning Geek](https://www.planninggeek.co.uk/2026/revised-nppf-2026/), [Urbanist Architecture](https://urbanistarchitecture.co.uk/nppf-2026/)). Grey belt policy remains, broadly unchanged. The exact paragraph text was not checked on GOV.UK [U]. |
| 6 | Private credit "$1.96 trillion in 2026" | **UNVERIFIED / misleading** | $1.96tn appears in secondary tables attributed to Mordor Intelligence/Moody's ([example](https://economy.com.pk/global-economy-2026-imf-growth-private-credit-boom)). Other estimates: European Parliament briefing **~$2.3tn global AUM (2025)** ([EP](https://www.europarl.europa.eu/RegData/etudes/BRIE/2026/784039/ECTI_BRI(2026)784039_EN.pdf)); about $1.7tn (Preqin, early 2026, secondary). $1.96tn coincides with Preqin's Dec 2022 *all-private-capital dry powder* ([JPMorgan](https://www.jpmorgan.com/insights/banking/capital-markets/private-markets-outlook)), so conflation is likely. Quote a range with its definition. |
| 7a | Shor on secp256k1 needs ~1,200–1,450 logical qubits | **TRUE (as of Mar 2026)** | Either ≤1,200 logical qubits and ≤90m Toffoli gates, or ≤1,450 and ≤70m ([IACR ePrint 2026/625](https://eprint.iacr.org/2026/625); [arXiv 2603.28846](https://arxiv.org/abs/2603.28846)). Earlier estimate: 2,330 logical qubits (Roetteler et al. 2017, [arXiv 1706.06752](https://arxiv.org/abs/1706.06752)). A Sept 2026 trapped-ion compilation estimates about 1,450 logical qubits and about 20,000 physical qubits over 26 days ([ePrint 2026/1916](https://eprint.iacr.org/2026/1916.pdf)). |
| 7b | NIST FIPS 203/204/205 finalised Aug 2024 | **TRUE** | Published 13 Aug 2024 [K]. |
| 8a | Sardex ~€51m+ annual volume | **TRUE for 2015 only** | €51.2m in 2015 ([Littera et al.](https://cris.unibo.it/retrieve/e1dcb333-5cdd-7715-e053-1705fe0a6cc9/littera_sartori_dini_antoniadis_From%20an%20Idea%20to%20a%20Scalable%20Working%20Model.pdf)). There is no current annual figure; SardexPay reports a cumulative €1bn. |
| 8b | Sardex velocity 5× the euro | **INACCURATE** | Company-measured velocity was 12.28 vs 1.5 for the euro in 2015 (≈8×) and 11.56 vs 1.5 in 2016 ≈7.7× ([FREIT WP](https://mail.freit.org/WorkingPapers/Papers/ForeignInvestment/FREIT948.pdf); [Monneta](https://monneta.org/en/sardex)). Self-reported, with a non-standard definition. |
| 8c | "MTCS reduces ~25% of debt" | **FALSE (misattribution)** | 25% is the **Sardex** obligation-clearing result (Fleischman et al. 2020). Slovenia's national system in 2025: ≈2.4% of reported and ≈14% of "considered" obligations (AJPES; my calculation, Part 1(g)). |
| 9a | Liberty Dollar founder convicted | **TRUE** | Bernard von NotHaus, convicted 18 Mar 2011 of making, possessing and selling his own coins ([FBI](https://www.fbi.gov/charlotte/press-releases/2011/defendant-convicted-of-minting-his-own-currency)). |
| 9b | e-gold indicted for unlicensed money transmission | **TRUE** | Apr 2007 indictment for money laundering and operating an unlicensed money transmitting business ([DOJ 2007](https://www.justice.gov/archive/opa/pr/2007/April/07_crm_301.html)). |
| 9c | Liberty Reserve founder: 20 years | **TRUE** | Arthur Budovsky, sentenced 6 May 2016 ([DOJ](https://www.justice.gov/archives/opa/pr/liberty-reserve-founder-sentenced-20-years-laundering-hundreds-millions-dollars)). |
| 9d | Bristol Pound closed 2021 | **TRUE (nuance)** | Digital scheme ended Aug 2020; paper notes withdrawn by end of Sept 2021 ([BBC](https://www.bbc.com/news/uk-england-bristol-57694453)). Bristol Pay CIC closed in 2023 ([legacy site](https://www.bristolpoundlegacy.info/)). |
| 9e | Ripplepay → Ripple/XRP | **TRUE** | Ryan Fugger, RipplePay 2004; handed to Jed McCaleb 2011; OpenCoin with Chris Larsen 2012; became Ripple/XRP ([BitMEX Research](https://www.bitmex.com/blog/the-ripple-story)). |
| 10a | Credit Commons founders and date | **TRUE if stated as Slater & Jenkin, 2016** | White paper "The Credit Commons: A Money for the Solidarity Economy", Matthew Slater & Tim Jenkin, **2016**; the term was coined by Thomas Greco ([PDF](http://creditcommons.org/assets/credit-commons.pdf)). Any "2018" date is wrong. |
| 10b | Open Credit Network founder and date | **PARTLY VERIFIED** | Co-founded by Dil Green and Oli Sylvester-Bradley (Open.coop), with Dave Darby; described as "new" in Apr 2020; a co-founder says it "failed" ([Resilience 2026](https://www.resilience.org/stories/2026-03-12/new-tools-for-growing-the-commons-and-how-i-discovered-them/)). Exact founding date [U]. |
| 11a | BIS published Dec 2025 work on auction-based liquidity arrangements | **TRUE** | BIS WP 1318, "Auction-based liquidity saving mechanisms", 16 Dec 2025 ([BIS](https://www.bis.org/publ/work1318.htm)). |
| 11b | BIS unified ledger | **TRUE** | BIS Annual Economic Report 2023, ch. III ([BIS](https://www.bis.org/publ/arpdf/ar2023e3.htm)), developed further in AER 2025, ch. III ([BIS](https://www.bis.org/publ/arpdf/ar2025e3.htm)). |
| 12 | BoE "Money creation in the modern economy" (2014): loans create deposits | **TRUE** | McLeay, Radia & Thomas, *BoE Quarterly Bulletin* 2014 Q1: commercial banks create deposits when they lend [K]. |
| 13a | Setara "Normalized Compute Unit" methodology | **PARTLY TRUE** | Setara Financial Corp (Chicago) markets the NCU™ ([Setara](https://www.setarafinancial.com/insights)). Its published methodology describes a **pre-production** series from public list prices (Class C evidence) ([methodology](https://www.setarafinancial.com/methodology)); no full NCU formula is public. |
| 13b | CME H100/B200 rental-index futures "pending regulatory review" | **TRUE (and postponed)** | Pending CFTC review. The Oct 5 2026 date was withdrawn on 25 Sep 2026; the effective date is TBA ([SER-9785R](https://www.cmegroup.com/content/dam/cmegroup/notices/ser/2026/09/ser-9785r.pdf)). |

---

## Part 3 — Data sources

### (a) ONS UK input–output analytical tables (IOATs) [V]

- **Latest edition: 2023** (released December 2025), consistent with Blue Book 2025. Format: **.xlsx**.
- **Product by product, 2023:** <https://www.ons.gov.uk/file?uri=/economy/nationalaccounts/supplyandusetables/datasets/ukinputoutputanalyticaltablesdetailed/2023/iot2023product.xlsx> (825.7 KB)
  - 2022 revised: <https://www.ons.gov.uk/file?uri=/economy/nationalaccounts/supplyandusetables/datasets/ukinputoutputanalyticaltablesdetailed/2022revised/iot2022revisedproduct.xlsx>
  - 2022: <https://www.ons.gov.uk/file?uri=/economy/nationalaccounts/supplyandusetables/datasets/ukinputoutputanalyticaltablesdetailed/2022/iot2022product.xlsx>
  - Landing page: <https://www.ons.gov.uk/economy/nationalaccounts/supplyandusetables/datasets/ukinputoutputanalyticaltablesdetailed>
- **Industry by industry, current (2023):** <https://www.ons.gov.uk/file?uri=/economy/nationalaccounts/supplyandusetables/datasets/ukinputoutputanalyticaltablesindustrybyindustry/current/iot2023industry.xlsx> (642.9 KB)
  - Landing page: <https://www.ons.gov.uk/economy/nationalaccounts/supplyandusetables/datasets/ukinputoutputanalyticaltablesindustrybyindustry>
- **Caveat:** sector-level tables cannot measure firm-level cycles. They can only seed *synthetic* firm networks, for example by disaggregating IO flows in the way CBS reconstructed the Dutch network ([CBS slides](https://www.cbs.nl/-/media/_pdf/2023/27/slides-cbs---odissei-microdata-meeting-on-supply-chain-networks.pdf)).

### (b) Firm-level or B2B transaction networks usable for clearing experiments

| Dataset | Access | Format | Suitability |
|---|---|---|---|
| **Sarafu Community Inclusion Currency 2020–2021** (Kenya): ~55,000 users, every transaction 25 Jan 2020–15 Jun 2021, ~300m Sarafu | **Public with free UKDS registration** (End User Licence): <https://reshare.ukdataservice.ac.uk/855142/> (DOI 10.5255/UKDA-SN-855142); file `Sarafu2021_UKdb_submission_complete_d.zip`; descriptor [Sci Data 2022](https://www.nature.com/articles/s41597-022-01539-4) [V] | ZIP containing CSV (`sarafu_txns_20200125-20210615.csv`) | The best openly obtainable *real* transaction network. It records payments, not invoices, so obligations would have to be constructed. Includes business-type labels. |
| **Sarafu Network Community Asset Vouchers 2022–2023** (Kenya, Cameroon, South Africa): ~20,000 users | UKDS registration: <https://reshare.ukdataservice.ac.uk/856593/> [V] | ZIP + ReadMe PDF | As above. Multi-voucher setting, close to a "multi-currency mutual credit" test bed. |
| **AJPES monthly multilateral set-off reports** (Slovenia) | Public PDF: <https://www.ajpes.si/Doc/Bonitete/Pobot/Pobot-obvezni-Porocila_2025.pdf> [V] | PDF (aggregate only) | Calibration targets (reported, considered and set-off amounts; participation). No graph data. |
| **Republika Srpska clearinghouse** | The paper states the algorithm library is public and that the authors held the full data. Public availability of debt-network data from the Banja Luka Stock Exchange was **not confirmed** [U]. | — | Ideal if obtainable: a real national obligation graph with outcomes. |
| **NBB B2B (Belgium), Ecuador SRI and Hungarian VAT networks** | Restricted administrative microdata (researcher agreements) [V] | — | Best for topology; not downloadable. |
| **TSR (Japan), FactSet Revere, Bloomberg SPLC** | Proprietary [V] | — | Binary links (TSR) or large-firm bias (FactSet). |
| **Sardex invoice data** | Not public (used by Fleischman et al. under affiliation) [U] | — | — |

### (c) MLPerf results [V]

| Repository | URL | Machine-readable file |
|---|---|---|
| Inference v6.1 (Sep 2026) | <https://mlcommons.org/2026/09/mlperf-inference-v6-1-results> (repository presumably `mlcommons/inference_results_v6.1` [U]) | — |
| Inference v6.0 | <https://github.com/mlcommons/inference_results_v6.0> | **`summary_results.json`**; per-submission folders under `closed/` and `open/`; visualiser linked in repository description |
| Inference v5.1 | <https://github.com/mlcommons/inference_results_v5.1> | `summary_results.json` |
| Training v5.1 | <https://github.com/mlcommons/training_results_v5.1> | Per-vendor folders with result logs |
| Training v6.0 (Jun 2026) | Results sheet linked from <https://mlcommons.org/benchmarks/training/>; GitHub repository presumably `mlcommons/training_results_v6.0` [U] | Results sheet (format not checked) |
| Aggregated history (third party) | <https://github.com/ctuning/ck_mlperf_results> | Collective Mind JSON |

---

## Unoccupied research space — honest assessment

Ranked by how genuinely new, falsifiable and cheap a contribution would be. Nothing here repeats an existing claim of novelty.

### Multilateral clearing among SMEs

- **Not novel:** cycle-finding algorithms (Simić–Milanović 1992; TCT; MTCS); national clearing institutions (Slovenia since 1991; Republika Srpska since 2015); consent by opt-out round (Republika Srpska); privacy-preserving or decentralised clearing (Cycles); a UK "clearing club" concept (Mutual Credit Services); causal evidence on default (Božić & Zrnc).
- **Genuinely open and cheap:**
  1. **A pre-registered, cross-dataset model that predicts the clearable fraction from cheap topology statistics.** Candidate predictors: reciprocity, size of the largest strongly connected component, weight of the cycle space, participation rate and churn.
     - *Datasets:* Sarafu (public), AJPES aggregates, Republika Srpska published figures, and synthetic networks calibrated to Bacilieri-style statistics.
     - *Falsifiable:* predicted vs realised fraction.
     - *Cost:* low.
     - Nobody has published this; Fleischman & Dini leave "significant" undefined.
  2. **The first UK estimate on real UK invoice data.** For example, a consenting cluster of SMEs exporting ledgers from Xero, Sage or QuickBooks. Pre-register the hypothesis that realised clearing is below 10% of submitted value unless the cluster includes a dense trade-association core.
     - *Main risk:* data access, not technology.
  3. **An open legal template for UK consent-based clearing** that is robust to *British Eagle*, s.127 and s.239: per-cycle confirmation, petition screening, immediate finality and no carried-forward netting obligations.
     - *Falsifiable:* via counsel opinion and an FCA perimeter answer.
     - Useful as a public good. Novelty is moderate, because practice exists abroad but no UK template has been published.
  4. **Trade-credit version of the BIS auction LSM.** Price the liquidity a third party injects to close near-cycles, with side payments from beneficiaries.
     - BIS WP 1318 tests this only on RTGS data. Cycles' trade-credit paper reports no empirics.
     - *Cost:* simulation-cheap.
- **Expect** low headline clearing rates in open economies (single-digit to low-teens percent of submitted value). Frame the value as default-risk and coordination effects, as in Republika Srpska, not "25%".

### Multilateral clearing among AI agents

- **Not novel:** agent payment rails (AP2, ACP, x402, MPP, Visa TAP, Mastercard Agent Pay) and bilateral batching (x402 batch-settlement, MPP sessions).
- **Open:** whether agent economies have cycles at all. A cheap simulation or trace study of agent-to-agent obligations (tools, data, compute, sub-agents) can test it. *Hypothesis to falsify:* "agent payment graphs are hub-and-spoke, with clearable fraction below 5%." A negative result is likely and still publishable. Multilateral agent netting only matters if agents *sell to each other* in loops.

### Compute entitlements

- **Not novel:** credits for compute (Karma); heterogeneity-aware exchange rates and trading inside a cluster (Gavel, Gandiva_fair); market allocation (Shockwave); compute rental indices and futures (Silicon Data/CME, Ornn/ICE/Architect, CF Benchmarks); a "normalised compute unit" brand (Setara NCU™).
- **Open and cheap:** an **open, reproducible, workload-specific exchange rate** between accelerators derived from MLPerf throughput (Inference v6.x, Training v6.0), tested **out of sample** against market rental-index ratios (H100 vs B200, etc.).
  - *Falsifiable:* if MLPerf-implied ratios fail to predict market price ratios within a pre-set error band, the "throughput-normalised entitlement" idea fails.
  - *Overlap risk:* Setara; stay public and empirical.

### Agent credit

- **Not novel:** Kocherlakota's memory argument; Karma's credit ledger; Mastercard + Aave "credit layer"; the x402 spec's "credit-backed commitments"; Cycles Pay's receivables financing.
- **Open but weaker:** simulation tests of record-keeping-based credit limits for agents (Kocherlakota–Wallace with partial records). Cheap but mostly theoretical. Novelty is modest unless tied to real agent transaction traces, which are not publicly available.

### AI-designed allocation and governance

- **Not novel:** AI Economist, Democratic AI, RegretNet, LLM-evolved mechanisms (Liu–Guo–Conitzer 2025) and AlphaEvolve-style search. Arrow and Gibbard–Satterthwaite still bind.
- **Narrow open slot:** LLM- or evolution-designed **clearing or allocation rules with hard constraints** (net-position preservation, individual rationality, per-cycle consent), benchmarked on **real** obligation data (Sarafu) or **real** compute throughput data (MLPerf) against known baselines. *Falsifiable:* does the evolved rule beat the max-weight-cycle baseline on held-out months without violating constraints?

### Future-resource claims

- **Settled or not novel:** ownership of extracted resources in national law (US 2015, Luxembourg 2017, UAE 2019/2023, Japan 2021); the Artemis Accords (76 signatories). Territorial appropriation is prohibited by OST Art. II.
- **Assessment:** instruments over *future* extraterrestrial resources lack an enforceable underlying asset, a price history and a cheap test. **Not recommended** as the programme's single falsifiable project.

### Bottom line for project selection

The two most defensible "one project" candidates are:
- **(1)** a cross-dataset, pre-registered **clearable-fraction predictor**, combined with a UK legal template;
- **(2)** an **MLPerf-derived compute exchange-rate** test against market rental indices.

Both are cheap, falsifiable and adjacent to well-documented prior art. Their novelty claims must be limited to the *empirical test and its openness*, not the mechanism.
