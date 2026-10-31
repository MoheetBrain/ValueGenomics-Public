# Books and Papers Audit: Economic Genome (ValueGenomics)

Audit date: 2026-10-17. Public edition of the existing bibliography and research audit; private library paths and acquisition details omitted.

**Method.** I got sizes from `stat` and hashes from `shasum -a 256`. Text came from `pdftotext` (poppler 26.07), with `pdfinfo` for page counts. Each EPUB was copied into its own empty directory under `/private/tmp/claude-books/` and its XHTML stripped to text by a standard-library script run with `python3 -I`. The two image-only PDFs were rendered with `pdftoppm` and OCR'd locally with `tesseract`. Nothing inside any file was executed. I checked each identity against the document's own title page, copyright page or JSTOR cover, not the filename.

**Page conventions.** "p." means the printed page number, worked out from the running heads. "PDF p." means the page index in the file. Where a book has no printed numbers, I cite the chapter or section and the PDF page.

**Publication scope.** Bibliographic references, research annotations and brief attributed quotations are retained. No book, paper or private source copy is bundled; underlying publications retain their own rights.

---

## 1. Summary table

| # | Source (short) | Type | Accessible | Verified identity | Rel. 0–3 |
|---|---|---|---|---|---|
| 1 | Seife, *Zero* | EPUB | Yes, XHTML text, chapters 0–9 | Charles Seife, *Zero: The Biography of a Dangerous Idea*, Viking/Penguin 2000 | 0 |
| 2 | Desan, *Making Money* | PDF, 498 pp. | Yes, text layer | Christine Desan, *Making Money: Coin, Currency, and the Coming of Capitalism*, OUP 2014 | **3** |
| 3 | Diamantaras JEL 2016 | PDF, 4 pp. | Yes | **Book review** (not an article) of Börgers 2015, *JEL* 54(2):589–591 | 1 |
| 4 | Muniesa, *Provoked Economy* | PDF, 84 pp. | **Image-only, and only even-numbered pages present**; OCR on samples | Fabian Muniesa, *The Provoked Economy*, Routledge 2014 | 2 |
| 5 | Milgrom, *Putting Auction Theory to Work* | PDF, 393 pp. | Yes | Paul Milgrom, CUP 2004 (Churchill Lectures) | **3** |
| 6 | Solan, *Stochastic Game Theory* | PDF, 279 pp. | Yes | Eilon Solan, *A Course in Stochastic Game Theory*, LMS Student Texts 103, CUP 2022 | 2 |
| 7 | Roughgarden, "No-Regret Dynamics" | PDF, 17 pp. | Yes | Lecture 17 only of *Twenty Lectures on AGT*, CUP 2016, pp. 230–246 | 2 |
| 8 | "Theory, Recursive Macroeconomic" | PDF, 1477 pp. | Yes (calibre conversion) | Ljungqvist & Sargent, *Recursive Macroeconomic Theory*, **4th ed.**, MIT Press 2018 | **3** |
| 9 | Greene, *Econometric Analysis* | PDF, 1168 pp. | Yes; online appendices A–F absent | William H. Greene, 8th ed., Pearson 2018 | 1 |
| 10 | Cowen & Tabarrok | PDF, 929 pp. | Yes | *Modern Principles of Economics*, 2nd ed., Worth 2011/12 | 1 |
| 11 | intelligent-economy | PDF, 68 pp. | Yes | Huawei, *Intelligent Economy: Enabling Sustainable Growth* (2022), modelled by EY with its EYGEM CGE model | 0 |
| 12 | annurev-economics-051624-061002 | PDF, 23 pp. | Yes | Trammell & Korinek, "Economic Growth Under Transformative AI," *Annu. Rev. Econ.* 18:589–611 (2026) | 2 |
| 13 | Anderson, *The Space Economy* | PDF, 255 pp. | Yes | Chad Anderson, Wiley 2023 | 1 |
| 14 | *Handbook of Space Resources* | PDF, 1201 pp. | Yes | Badescu, Zacny & Bar-Cohen (eds.), Springer 2023 | **3** (law chapters) |
| 15 | Perez | PDF, 218 pp. | Yes | Carlota Perez, *Technological Revolutions and **Financial** Capital: The Dynamics of Bubbles and Golden Ages*, Elgar 2002 | 1 |
| 16 | Bostrom, *Deep Utopia* | PDF, 541 pp. | Yes; calibre conversion with no print pages | Nick Bostrom, Ideapress 2024 | 1 |
| 17 | Spence 1973 | PDF, 21 pp. | **Image-only**; whole file OCR'd | "Job Market Signaling," *QJE* 87(3), **Aug** 1973, 355–374 | 2 |
| 18 | Börgers et al. (extra) | PDF, 263 pp. | Yes | *An Introduction to the Theory of Mechanism Design*, OUP 2015 | **3** |
| 19 | Vohra ch. 4 (extra) | PDF, 41 pp. | Yes | "Incentive Compatibility," ch. 4 of *Mechanism Design: A Linear Programming Approach*, CUP 2011, pp. 38–78 | 2 |
| 20 | Pass (extra) | PDF, 244 pp. | Yes | Rafael Pass, *A Course in Networks and Markets* (lecture notes, Jan 2018) | 2 |
| 21 | Pistor (extra) | PDF, 316 pp. | Yes | Katharina Pistor, *The Code of Capital*, Princeton 2019 | **3** |
| 22 | MacKenzie (extra) | PDF, 391 pp. | Yes | *An Engine, Not a Camera*, MIT 2006 | 2 |
| 23 | Padgett & Powell (extra) | EPUB | Yes | *The Emergence of Organizations and Markets*, Princeton 2012 | 2 |
| 24 | Weinersmith, *A City on Mars* (extra) | PDF, 633 pp. | Yes; ebook render with no print pages | Penguin 2023 | 2 |
| 25 | Papazian (extra) | PDF, 280 pp. | Yes | *Financing the Race to Space*, Palgrave 2024 | 1 |
| 26 | Ojala & Baber (eds.) (extra) | PDF, 330 pp. | Yes (open access) | *Space Business: Emerging Theory and Practice*, Palgrave 2024 | 0 |
| 27 | AI-economics working papers (extras, 8 files) | PDF | Yes | See §2.27 | 1 |
| 28 | Reviews and duplicates (extras) | PDF | Yes | See §2.28 | 0–1 |

---

## 2. Source-by-source

### 2.1 Seife, *Zero*
- **Private source path omitted.**
- **File:** EPUB, 1,923,138 B. sha256 `38279b5f8b46a5c5420f69f543480c98ed07efbe7b1ce8475a5612385267a666`.
- **Access:** full text, about 56,800 words across chapters 0–9, plus appendices A–E.
- **Identity:** confirmed from the title page. Mismatches: the copyright page's CIP data gives the hardcover subtitle "the biography of a number", and the embedded ISBN differs from the filename's ISBN.
- **Topic:** popular history of zero and infinity.
- **Relevance:** Ch. 3 covers Italian merchants adopting Hindu–Arabic numerals, and Florence banning them in 1299 because entries were easy to alter. That is an anecdote about tamper-resistance in record-keeping, nothing more.
- **Established results:** none economic.
- **Limitation:** not an economics source. See §3.1 for the chapter checks.

### 2.2 Desan, *Making Money* (2014)
- **Private source path omitted.**
- **File:** PDF, 72,614,396 B. sha256 `e1d9c4e8bf0e375dba945492f1e4306108e5c8f9577c85dd87ca34427380a340`. 498 pp. with a text layer; printed page = PDF − 20.
- **Identity:** confirmed (OUP 2014, ISBN 978-0-19-870957-2).
- **Topic:** legal and constitutional history of English money, from medieval coin to Bank of England currency.
- **Relevant parts:**
  - Introduction, pp. 1–22: money as a governance project.
  - Ch. 1 "Creation stories," pp. 23–69: a critique of the Mengerian commodity-convergence story (p. 28) and a review of tax-backed and asset-pricing theories (p. 46).
  - Ch. 4, pp. 151–190: "English invention of public credit," including Exchequer tallies.
  - Ch. 5, pp. 191–230: coin and credit strata, clearing and bills of exchange.
  - Ch. 8, pp. 295–329: bank currency and the Bank of England.
  - Ch. 10, pp. 360–403: Locke and the 1696 recoinage; the 18th-century architecture of money.
- **Established results (historical-legal, not formal):**
  - Money's functions (unit of account, payment, exchange) are produced by a public institutional design. Desan's thesis is that "money is a mode of mobilizing resources" (p. 1).
  - Bills of exchange and promissory notes could not discharge public obligations, and they moved by endorsement, unlike coin (p. 95).
  - By the 14th century the Exchequer worked as a clearing-house for tallies of assignment rather than a cash office (p. 175).
  - Banks of issue combined with fractional reserves and centralized clearing produced cash that circulated hand to hand. Earlier transfer banks and bills only moved credit between known parties (p. 18).
  - Bankers' reciprocal note-clearing extended the public unit of account and did not create a private one (p. 300, n. 22).
  - An Exchequer–Bank clearing system for notes and bills existed (p. 315). The Bank of Amsterdam extended credit by clearing merchants' mutual debts (p. 390).
- **Limitation:** qualitative and England-centred. It offers no model, so the programme gets institutional mechanisms and precedents from it, not testable parameters.

### 2.3 Diamantaras, *JEL* 2016
- **Private source path omitted.**
- **File:** PDF, 801,854 B. sha256 `ecbe30e59feb5487dde54bf04e082f756709c59342126e3ec3956aa3ccc6700a`. 4 pp. (JSTOR cover plus pp. 589–591).
- **Identity:** a three-page **book review** by Dimitrios Diamantaras of Börgers (2015). It is not a research article, and page 4 runs into the next review (Basu).
- **Relevance:** a map of mechanism-design results. It flags a gap: the revelation principle guarantees only that truth-telling is *an* equilibrium, so implementation theory (uniqueness) is outside the book. It lists Crémer–McLean, Gibbard–Satterthwaite, Jehiel–Moldovanu, robust design and dynamic design.
- **Limitation:** secondary. Cite Börgers (§2.18) instead.

### 2.4 Muniesa, *The Provoked Economy* (2014)
- **Private source path omitted.**
- **File:** PDF, 1,757,479 B. sha256 `7d3816274266f5ab6368a6692a1113ac3e8435c4382314758238a967e97423f3`.
- **Access:** an 84-page HP scanjet scan with **no text layer**. OCR of sample pages shows the file holds only **even-numbered** book pages; the odd pages, including contents p. vii, are missing.
- **Identity:** confirmed from the title and copyright pages (Routledge 2014).
- **Topic:** performativity ("provocation") of economic knowledge.
- **Relevant parts:**
  - Ch. 1, p. 7: theoretical rudiments.
  - Ch. 2, p. 28: economic reality.
  - Ch. 3, c. pp. 44–60: back-office description of derivatives. Confirmations go either directly to counterparties or through centralized clearing and settlement (p. 50).
  - Ch. 4, p. 61ff: the Paris Bourse electronic call auction as an attempt to make the Walrasian auctioneer explicit (p. 64).
- **Established results:** conceptual only. Models and tests partly bring about the realities they describe.
- **Limitation:** about half the text is missing and none is searchable. Use MacKenzie (§2.22) for the operational performativity typology.

### 2.5 Milgrom, *Putting Auction Theory to Work* (2004)
- **Private source path omitted.**
- **File:** PDF, 1,649,395 B. sha256 `0ecece399d0cc715f7e17d307c372c75314dff8cc21b58df6c9adf759cddf06d`. 393 pp.; printed page = PDF − 25.
- **Identity:** confirmed (CUP 2004).
- **Relevant parts:**
  - Ch. 1.4.1, p. 19: resale and the Coase theorem. Milgrom argues resale does not guarantee efficient allocation.
  - Ch. 2, pp. 45–61: VCG.
  - Ch. 3, pp. 64–94: envelope theorem and payoff equivalence.
  - Ch. 4, pp. 98–154: equilibrium and revenue.
  - Ch. 6, pp. 188–247: entry, set-asides and non-performance.
  - Ch. 7, pp. 255–293: uniform-price and clock auctions.
  - Ch. 8, pp. 296–333: package auctions and the core.
- **Established results:**
  - Thm 2.1, p. 51: truthful reporting is always optimal under VCG.
  - Thm 2.2, p. 54: necessary and sufficient condition for a budget-balanced VCG mechanism. The condition generally fails.
  - Thm 2.3, p. 56 (Green–Laffont/Holmström): with smoothly connected type spaces, VCG is the *only* efficient dominant-strategy mechanism.
  - §2.5, pp. 56–61: VCG's monotonicity, shill-bidding and merger problems.
  - Thm 3.3, p. 74 (Myerson's lemma); Thms 3.4–3.5, pp. 75–76 (revenue equivalence).
  - Thm 3.6, p. 78 (Myerson–Satterthwaite).
  - §3.3.6, p. 80, Thm 3.7 (Jehiel–Moldovanu impossibility).
  - §4.4, p. 148 (Myerson optimal auction; Bulow–Klemperer).
  - §8.1, pp. 302–312: when Vickrey outcomes lie in the core; the role of substitutes.
  - §8.3, p. 319ff: Ausubel–Milgrom proxy auctions.
  - The revelation principle is stated at p. 141.
- **Limitation:** single-shot, mostly quasi-linear settings. It has no computational-complexity analysis and nothing on money or credit.

### 2.6 Solan, *A Course in Stochastic Game Theory* (2022)
- **Private source path omitted.**
- **File:** PDF, 2,186,180 B. sha256 `82d3bceaaa58584301fa8d4a9ffac10c9c47f771e40f56de19320030f9b90217`. 279 pp.; printed page = PDF − 11.
- **Identity:** confirmed (CUP 2022, ISBN 978-1-316-51633-1).
- **Established results:**
  - Thm 5.9, p. 68 (Shapley 1953): every two-player zero-sum discounted game has a value.
  - Thm 8.11, p. 117 (Fink 1964; Takahashi 1964): every finite stochastic game has a stationary discounted equilibrium.
  - Thm 9.13, p. 139 (Mertens–Neyman 1981): a uniform value exists in two-player zero-sum games.
  - §9.5, p. 155 (Solan–Vieille 2002): extensive-form correlated equilibrium exists.
  - Thm 10.4, p. 179: uniform equilibrium exists in two-player absorbing games.
- **Stated open problems:**
  - Existence of a uniform equilibrium payoff in general stochastic games (p. 189).
  - Absorbing games with four or more players (p. 179).
  - Quitting games with four or more players (p. 211).
  - p. 121 reports an example (Levy 2013) with no stationary discounted equilibrium on general state spaces.
  - The uniform-value algorithm cited (Oliu-Barton 2020) is exponential in states and actions (p. 161).
- **Limitation:** mathematics only. Economic applications are just mentioned, and there is no mechanism design.

### 2.7 Roughgarden, Lecture 17 "No-Regret Dynamics"
- **Private source path omitted.**
- **File:** PDF, 343,390 B. sha256 `8083fc2bcd6b769ca61afe5b8ae880383f5534793ed11e90ae8cc8784cdf0ca9`. 17 pp. (book pp. 230–246; DOI 10.1017/CBO9781316779309.018).
- **Established results:**
  - Thm 17.6, p. 234: no-regret algorithms exist. Multiplicative weights has expected regret O(√(ln n / T)), and an Ω(√(ln n / T)) lower bound applies.
  - Cor 17.7, p. 234: (4 ln n)/ε² rounds suffice for regret ε.
  - Prop 17.9, p. 240: the time-averaged joint play of no-regret dynamics is an approximate **coarse correlated equilibrium**.
  - Cor 17.10, pp. 241–242: price-of-anarchy bounds for smooth games carry over to no-regret dynamics.
- **Limitation:** only one lecture. Swap regret leading to correlated equilibrium (Lecture 18) and the PPAD hardness of Nash equilibrium are referenced but **not in the file**. Convergence is of the empirical average, not of day-to-day play.

### 2.8 Ljungqvist & Sargent, *Recursive Macroeconomic Theory*, 4th ed. (2018)
- **Private source path omitted.**
- **File:** PDF, 14,332,372 B. sha256 `0f41cbceae17ca1e088a09263214ae1e9c6b69b62501e789abd56d3794d1e989`. 1477 pp.; printed page = PDF − 39.
- **Identity:** confirmed from the title and LoC pages (MIT 2018, ISBN 9780262038669). The filename is a garbled inversion of the title, and the PDF metadata reads "RMT4.dvi".
- **Relevant parts:** ch. 8 (complete markets), ch. 9 (OLG and fiat money), ch. 18 (Bewley/Huggett and inside money), ch. 22 (limited commitment), ch. 27 (fiscal-monetary inflation), **ch. 28 "Credit and Currency"** (pp. 1171–1206), **§29.8 Kiyotaki–Wright** (pp. 1248–c.1256). See §3.2.
- **Established results:**
  - Complete-markets models give money no role because they embed efficient multilateral clearing (p. 287).
  - Townsend turnpike model: unbacked currency is valued only if private loan markets are restricted (§28.1, p. 1171).
  - Proposition 2, p. 808: with pure private IOUs, the equilibrium rate stays below the complete-markets rate.
  - Bewley fiat-money equilibrium (§18.10.4, p. 810).
  - Kiyotaki–Wright monetary equilibria and their welfare (§29.8.1–29.8.2).
  - Friedman rule (§27.5, §28.6).
  - Commodity money is Pareto-dominated by fiat (p. 1199).
- **Limitation:** Kocherlakota's "money is memory" (1998) and Kocherlakota–Wallace's incomplete record-keeping (1998) are **cited but not derived** (pp. 365, 810). Get the originals if the programme relies on them.

### 2.9 Greene, *Econometric Analysis*, 8th ed.
- **Private source path omitted.**
- **File:** PDF, 21,446,185 B. sha256 `7879d902200dd8fa050d83145c0fac5d24f934247c3ce823778d6aa1c36558b3`. 1168 pp.
- **Identity:** Pearson; front matter dated 2017, copyright 2018.
- **Relevance:** methods for falsification tests.
  - Ch. 5, p. 113: hypothesis tests.
  - Ch. 6, p. 153: difference-in-differences and structural change.
  - Ch. 8, p. 242: instrumental variables.
  - Ch. 11, p. 373: panel data.
  - Ch. 19, p. 918: selection and treatment effects.
- **Limitation:** generic toolkit. Appendices A–F are online-only and not in the file.

### 2.10 Cowen & Tabarrok, *Modern Principles*, 2nd ed.
- **Private source path omitted.**
- **File:** PDF, 17,660,309 B. sha256 `afe38ff2f17dd2636ae9154aa4b7165f9f59e5b5810c8ad6be9c215e9ccf84a2`. 929 pp.; printed page = PDF − 54.
- **Relevant parts:**
  - Ch. 27, pp. 543–576: intermediaries; banks in the payments system at p. 554.
  - Ch. 29, p. 603: quantity theory and neutrality, pp. 609–611.
  - Ch. 32, p. 673: the Fed as government's and bankers' bank that manages the payment system (p. 674); means of payment and liquidity (pp. 675–676); M1/M2 and fractional reserves (p. 677); lender of last resort (c. pp. 681–690).
- **Limitation:** introductory. The phrase "medium of exchange" and the barter story do not appear at all, and there is nothing on record-keeping or multilateral clearing.

### 2.11 Huawei/EY, *Intelligent Economy* (2022)
- **Private source path omitted.**
- **File:** PDF, 12,514,456 B. sha256 `c99c3c778c14713c4a3f2b54204577982ca60f862264820e6dd7b8b7fee0d661`. 68 pp.
- **Identity:** metadata author "Huawei". The back matter (PDF p. 67) discloses that Ernst & Young (China) Advisory was engaged and used its EYGEM CGE model.
- **Content:** a corporate forecast of US$18.8 trillion added value by 2030 (productivity 9.1, social 5.2, environmental 4.5), on p. 2. Blockchain is described as an immutable ledger.
- **Limitation:** advocacy, no labour-share or distribution analysis, unvalidated inputs. See §3.5.

### 2.12 Trammell & Korinek (2026), *Annual Review of Economics*
- **Private source path omitted.**
- **File:** PDF, 284,564 B. sha256 `2ad632ff4c14208a4b52788035771493d7b8512bfe0d1fc89b0fa6318274abeb`. 23 pp. (journal pp. 589–611, CC BY-NC-ND).
- **Established/synthesised results:**
  - If capital becomes a gross substitute for labour in production, growth accelerates and the labour share tends to zero, breaking the Kaldor facts (§2, p. 591ff).
  - Automating R&D alone has ambiguous effects.
  - Wages may rise or fall depending on returns to scale, fixed factors and the direction of technical change (Table 1, p. 605).
  - §6.2 (p. 606) points to distributional policy (Korinek & Lockwood 2026).
- **Limitation:** a review of models; it designs no institutions. It was published after my training cutoff, so I verified its identity only from the document's own metadata.

### 2.13 Anderson, *The Space Economy* (2023)
- **Private source path omitted.**
- **File:** PDF, 7,979,494 B. sha256 `7bc44ce64357a7a5f8aba5649d300c2b19ed5f6ad508345990f8abf1b5954c72`. 255 pp.; printed page = PDF − 26.
- **Identity:** a venture-capital practitioner book.
- **Relevant parts:** OST Art. VI authorisation, Luxembourg as a regulatory haven, and the Artemis Accords (pp. 130–131, in an interview with P. Marquez); the 2015 "Space Resource Exploration and Utilization Act" (p. 111); the maritime-law analogy (pp. 191–192); "asteroid mining is not for today" (pp. 8, 135).
- **Limitation:** no analysis of resource ownership, Moon Agreement or Article II, and nothing on tradable claims. See §3.4.

### 2.14 *Handbook of Space Resources* (2023)
- **Private source path omitted.**
- **File:** PDF, 34,266,017 B. sha256 `673ab1ec9f50c7269d1f971df602cdb0265a79fd0ce49eba5953570770dbb5cd`. 1201 pp. (ISBN 978-3-030-97912-6). The printed-to-PDF offset varies (+11 to −8), so I quote printed pages.
- **Relevant parts (Part VII):**
  - Ch. 30 LORS-101 (Espejel et al.), p. 999.
  - Ch. 31 Economics of space resources (Link, Martin, Mousel), p. 1023.
  - Ch. 32 Embodied-energy value theory, p. 1053.
  - **Ch. 33 "Policy, Legal Processes and Precedents for Space Mining"** (Anderson et al., Hogan Lovells / Colorado School of Mines), pp. 1109–1162.
  - **Ch. 34 "Legal Considerations for Space Resources"** (Murnane), pp. 1163–1200.
  - Ch. 7 §7.3 on debris ownership, p. 328.
- **Established results:** see §3.4. The most precise treatment of the legal regimes in the corpus.
- **Limitation:** written c. 2020–21, before the later Artemis signatories and national laws. No market design for claims.

### 2.15 Perez (2002)
- **Private source path omitted.**
- **File:** PDF, 1,222,480 B. sha256 `7a9435c8446804d92e7188db33265379c2c3c6413f0c26806110500ad9b3c0bc`. 218 pp.
- **Identity:** the title page reads "Financial Capital," not the filename's "finance capital". The PDF carries ISBN 1 84064 922 4, which differs from the filename's ISBN.
- **Relevant parts:** installation versus deployment periods (ch. 4, p. 36); four phases (ch. 5, p. 47); financial versus production capital (ch. 7, p. 71); Frenzy (ch. 10, p. 99); Turning Point (ch. 11, p. 114); typology of financial innovations (ch. 13, p. 138; Table 13.1, p. 139).
- **Limitation:** a historical stage theory, not falsifiable as a mechanism.

### 2.16 Bostrom, *Deep Utopia* (2024)
- **Private source path omitted.**
- **File:** PDF, 4,972,565 B. sha256 `3a8c8cd28d8aca35717c155cc51430f4c7cf40787b38307ccd16ddb51944c716`. 541 pp. (calibre render).
- **Relevant parts:** "Monday" lecture: "A simple three-factor model" (labour, capital, land) under perfect robot substitution, plus "Paradoxes of a Malthusian world" (PDF pp. 31–39); positional goods (PDF c. pp. 83–91). The model explicitly assumes fully reliable property rights and no redistribution (PDF p. 34).
- **Limitation:** a philosophical thought experiment.

### 2.17 Spence (1973)
- **Private source path omitted.**
- **File:** PDF, 1,799,863 B. sha256 `1192a337a73a51113a94181da940a270fe333545028cd1715b5b01c3e890bd99`. 21 pp. of JSTOR scan with no text layer; all pages OCR'd locally.
- **Identity:** the JSTOR cover says Aug. 1973; the filename's "apr" is wrong.
- **Established results:**
  - A signal separates types only if its cost is negatively correlated with productivity (p. 358).
  - Equilibrium is defined by self-confirming employer beliefs (p. 360).
  - There is an infinite number of signaling equilibria (p. 363).
  - Private and social returns to the signal diverge (p. 364).
  - Some signaling equilibria are Pareto-inferior (p. 365).
- **Limitation:** single-market model. OCR may contain character errors.

### 2.18 Börgers et al., *An Introduction to the Theory of Mechanism Design* (2015), extra
- **Private source path omitted.**
- **File:** PDF, 1,281,516 B. sha256 `c81c302daede385b733e0df34f664218d1085e286b4747707d1f36c99f03bd0b`. 263 pp.; printed page = PDF − 18.
- **Established results:**
  - Revelation principle (Prop 3.1, p. 33).
  - Myerson optimal auction (Prop 3.4, p. 40).
  - Public-goods first-best impossibility (Prop 3.7, §3.3.4, pp. 49–50).
  - **Myerson–Satterthwaite** (Prop 3.12, p. 65).
  - Crémer–McLean full extraction with correlated types (§6.4, pp. 119–127).
  - Prop 7.10 (§7.5, p. 137) gives the necessary and sufficient condition for a budget-balanced VCG mechanism. For bilateral trade it implies that no efficient, DSIC, ex-post budget-balanced mechanism exists, even without an IR constraint (p. 139).
  - **Gibbard–Satterthwaite** (§8.2, pp. 142–149).
  - Jehiel–Moldovanu (§9.3, p. 158).
  - Robust mechanism design (ch. 10, p. 164).
  - Dynamic mechanism design (ch. 11, p. 204).
- **Limitation:** Arrow's theorem is only mentioned in the endnotes, and implementation theory is excluded.

### 2.19 Vohra, "Incentive Compatibility" (2011), extra
- **Private source path omitted.**
- **File:** PDF, 407,169 B. sha256 `1d70a218a1face6a56a5b1dae8a63a7264a53c004b7bed0079dfe691cf33f623`. Book pp. 38–78.
- **Established results:**
  - Rochet: an allocation rule is DSIC-implementable iff its type graph has no negative cycles (cycle monotonicity), Thm 4.2.1, p. 40.
  - Taxation principle, p. 42.
  - Saks–Yu: the 2-cycle condition suffices on convex domains (Thm 4.2.7, p. 46).
  - **Roberts:** with three or more outcomes and unrestricted valuations, the only DSIC rules are affine maximisers (Thm 4.2.14, p. 54).
- **Limitation:** chapter only.

### 2.20 Pass, *A Course in Networks and Markets* (2018), extra
- **Private source path omitted.**
- **File:** PDF, 7,692,838 B. sha256 `c2905f8e5fe0f78634538a3fc3ff79482f05022b6fc8bbb00325ce08babe1ab2`. 244 pp.; printed page = PDF − 13.
- **Relevant results:** market-clearing prices in matching markets (ch. 8, p. 69ff); VCG and auctions (ch. 10, p. 95); voting impossibilities including Gibbard–Satterthwaite (Thm 12.2, p. 120); the median-voter strategy-proof exception (Thm 12.10, p. 126); common knowledge (chs. 17–18).
- **Limitation:** lecture notes, not peer-reviewed.

### 2.21 Pistor, *The Code of Capital* (2019), extra
- **Private source path omitted.**
- **File:** PDF, 3,845,090 B. sha256 `a1cbad6526f66848505909e4d598931694e97ee62f2b30392ca130ddb2762d0e`. 316 pp.; printed page = PDF − 17.
- **Established results (legal analysis):** assets become capital through legal coding that confers priority, durability, universality and convertibility (pp. 2–3, 13–15). Convertibility into state money is the decisive attribute for financial assets (p. 15).
- **Relevant parts:** ch. 4 "Minting Debt" (pp. 77–107); ch. 8 "A New Code?" on digital code (p. 183).
- **Limitation:** qualitative.

### 2.22 MacKenzie, *An Engine, Not a Camera* (2006), extra
- **Private source path omitted.**
- **File:** PDF, 3,020,523 B. sha256 `67473de82ff858727b812e00a6893f892a7c4cd5ee00e891a9b30f6541b8dfc5`. 391 pp.
- **Established results:** a typology of performativity: generic, effective, Barnesian, and counterperformativity (Fig. 1.1, pp. 16–18). Case material: Black–Scholes–Merton (chs. 5–6, pp. 119–178), the 1987 crash (ch. 7, p. 179) and LTCM (ch. 8, p. 211).
- **Limitation:** sociology of finance, with no formal tests.

### 2.23 Padgett & Powell, *The Emergence of Organizations and Markets* (2012), extra
- **Private source path omitted.**
- **File:** EPUB, 6,563,351 B. sha256 `1bd40339511780bdb90a81b6b281f8798d606b2a28efce892010ea1ea9766857`. No print pages.
- **Relevance:** ch. 5 (Dugento Tuscan merchant-banks): bills of exchange between cooperating banks are first explicitly attested in 1291. Ch. 6 (Florentine partnership systems): current accounts and double-entry bookkeeping spread through partnership networks.
- **Limitation:** historical network sociology.

### 2.24 Weinersmith & Weinersmith, *A City on Mars* (2023), extra
- **Private source path omitted.**
- **File:** PDF, 79,096,316 B. sha256 `674439bc98642220cf29928864bf85be49d9917d3c90cf728b1e8f6433fad43f`. 633 pp.
- **Relevant parts:** Part IV, chs. 11–13 (OST and the Moon Agreement); Part V, chs. 14–16 ("Commonsing the Cosmos," "Dividing the Sky," space-states). See §3.4.
- **Limitation:** popular and polemical.

### 2.25 Papazian, *Financing the Race to Space* (2024), extra
- **Private source path omitted.**
- **File:** PDF, 5,966,457 B. sha256 `25c1b662c9ecb04e770acdd149e46e470d32c0e7c03347b060b986a7a4ba742c`. 280 pp.
- **Content:** a heterodox proposal. It critiques debt-based money (ch. 7, p. 103), proposes a "space value of money" (ch. 12, p. 167), and proposes Public Capitalisation Notes and "value easing" (ch. 14, pp. 191–201).
- **Limitation:** these are proposals, not established results, and the book has almost no resource law.

### 2.26 Ojala & Baber (eds.), *Space Business* (2024), extra
- **Private source path omitted.**
- **File:** PDF, 6,572,537 B. sha256 `da327fe20805ab135613e5996573aaf36599153b2737db706cabf06a7e5d589e`. 330 pp.
- **Relevance:** management studies of NewSpace and ground-station regulation (p. 195). It mentions the OST once and has no resource-rights analysis.

### 2.27 AI-economics working papers (extras)

| File (in the private reference library) | Identity | Bytes / sha256 |
|---|---|---|
| `econ_scenarios_transformative_ai.pdf` | Korinek, Jones, Sacher, Cotter, McCrory, "Economic Scenarios for Transformative AI," Anthropic Institute WP 2026-02 (Sep 2026): 2026–30 scenarios for GDP, labour share and unemployment | 656,236 / `9fe6667ec24b8a1dce3cde7c8ae5d5e6631bb95f68dae82dbd827cbfa2410327` |
| `w34256.pdf` | Brynjolfsson, Korinek, Agrawal, NBER w34256: TAI research agenda with nine "Grand Challenges" | 436,769 / `6aba39435ace5667574b08fb77586d97d52865c9d970ff66e8537f037d40c90c` |
| `w35155.pdf` | Davidson, Halperin, Houlden, Korinek, NBER w35155: condition for explosive growth from automated research | 1,758,645 / `1c9786749b9b6939887ade3415573c9c4c940690756c9ecda757d9ca430a3438` |
| `FINANCING THE AI BUILDOUT.pdf` | Van Nieuwerburgh, NBER w35865 (Oct 2026; forthcoming in BPEA) | 468,306 / `f18a7506cb739174f1fd814a72ea6d4d2a09609d9f159068d1b6fd85825891ed` |
| `2609.15802v1.pdf` | Cunningham et al., "The Economics of Recursive Self-Improvement," arXiv econ.GN (Sep 2026) | 694,940 / `bbcb1659ca4635bf985b02a679b058cf3b09e169b83f2af4172cd7481d4335d3` |
| `working-paper-1179-…-inflation.pdf` | Aldasoro, Doerr, Gambacorta, Rees, BIS WP 1179 (Apr 2024), effect of AI on output and inflation | 1,267,947 / `690c5b86bba0c76d41374e9dcb574b5af9d22c9e25414c6ca1500c325b182a87` |
| `EconIndex6-I.pdf` | Anthropic Economic Index report "Cadences" (Jun 2026), usage data | 3,259,219 / `5215ed71fc9f95c67a0fabdf57f35e15462943405c9a7b7278cc8c32d8455828` |
| `Power and progress _ ….pdf` | Acemoglu & Johnson, *Power and Progress* (2023). **Mismatch:** the file is a **Spanish translation** ("Contenido," "Cubrir") despite the English filename | 8,086,082 / `db0a61178df27d009ba67eea601e0ba3cc57d17fb81c8d30481f8d94f5f90d97` |
| `a359b3dfd13d4116a2ecd5e89a0ef4dc.pdf` | Huawei, *Intelligent World 2030* (2021), companion to item 11 | 55,842,473 / `f4d874f1ac846e162ddb85da2517d696d6e64907ed9205382f6739d8f4c2a8ce` |

All of these are context for demand and distribution under AI. None designs payment, clearing or property institutions.

### 2.28 Reviews and duplicates (extras)
- `Book_Review_An_Introduction_.pdf` (469,105 B; `e839255bbcd4f28efa4adcc61ae00b60a1b4e7db7e28fdb422ea6c88c1348ced`): the **same Diamantaras JEL review** without the JSTOR cover.
- `Kahn-AmericanAnthropologist-1988.pdf` (558,799 B; `dfd1fe4eb1117b8549e023869543090f0ea81a1457bfc869bbaeef1b16c53b5e`): review of Munn, *The Fame of Gawa* (kula, value transformation).
- `robertson-2008-book-review-…-property-in-question….pdf` (37,771 B; `588c0ad746a9f2bb477ff68cc231d0a8d865ef7045dd14cbfb5a33a5660f3b9c`): review of Verdery & Humphrey, *Property in Question*.
- `1-s2.0-S1755458619300799-main.pdf` (475,592 B; `d95faa85082f3742d0b3f8007dde8dbdf983abc12ef195410d541e1086368019`): one-page review of Massumi, *99 Theses on the Revaluation of Value*.
- `w33351.pdf` and `ARTIFICIAL INTELLIGENCE ASSET PRICING MODELS.pdf` are **byte-identical** (sha256 `437b319921db234af713be8bdc83cb3c2afb9e724035b66fc54045516b2abd56`): Kelly et al., NBER w33351.
- `Ayache, Elie - The Blank Swan…epub` (871,696 B; `e9cbdbca7f79027041296d41fd241b292bffa01c1bb953ca3ec580d34bb0da17`): Wiley 2010, a philosophy of derivatives pricing. Relevance 0–1.

---

## 3. Special tasks

### 3.1 Seife, *Zero*: chapter structure and claim check
**Structure: CONFIRMED.** Chapters 0–9 are: 0 Null and Void; 1 Nothing Doing; 2 Nothing Comes of Nothing; 3 Nothing Ventured; 4 The Infinite God of Nothing; 5 Infinite Zeros and Infidel Mathematicians; 6 Infinity's Twin; 7 Absolute Zeros; 8 Zero Hour at Ground Zero; 9 Zero's Final Victory. Appendices A–E follow.

| Claim from the earlier report | Verdict | Where it actually is |
|---|---|---|
| Ch. 0 opens with the USS Yorktown divide-by-zero failure | CONFIRMED | Ch. 0, first paragraph (21 Sep 1997) |
| Babylonian placeholder zero and Indian zero-as-number in Ch. 1/Ch. 3 | CONFIRMED (split) | Babylonian placeholder in Ch. 1 (recapped in Ch. 3); Indian zero as a number in **Ch. 3 only**; Ch. 1's "Indians" are the Siriono of Bolivia |
| Brahmagupta's negative numbers in Ch. 3 | CONFIRMED | Ch. 3, including his 0÷0 and 1÷0 attempts |
| Zeno/Achilles in Ch. 2 | CONFIRMED | Ch. 2; resolved via limits again in Ch. 5 |
| Pythagorean irrationals in Ch. 2 | CONFIRMED | Ch. 2 (diagonal of the square, golden ratio) |
| Calculus and infinitesimals in Ch. 5 | CONFIRMED | Ch. 5 (Newton, Leibniz) |
| "Infinity's Twin" is the Ch. 6 title | CONFIRMED | Ch. 6, subtitle "The Infinite Nature of Zero" |
| Absolute zero, thermodynamics, zero-point energy, Casimir in Ch. 7 | CONFIRMED | Ch. 7 (Kelvin, laser cooling, Casimir and Polder 1948, Lamoreaux 1995); zero-point energy returns in Ch. 8 |
| Singularities in Ch. 8 | PARTLY CONFIRMED | Ch. 8 has the Big Bang and point-particle singularities. Black-hole and naked singularities are mainly in **Ch. 7**, and poles and essential singularities in **Ch. 6** |
| Merchants adopting Hindu–Arabic numerals in Ch. 3 | CONFIRMED | Ch. 3 (Fibonacci's *Liber Abaci*; Italian merchants; the 1299 Florence ban) |

### 3.2 Money topics in the macro and money books

| Topic | RMT (Ljungqvist & Sargent) | Desan | Cowen & Tabarrok |
|---|---|---|---|
| Money as medium of exchange | Overcoming double coincidence of wants (p. 200); Samuelson OLG fiat money (§9.4, p. 342); Kiyotaki–Wright (§29.8, pp. 1248ff) | Critique of functional definitions (p. 1) and of Menger (p. 28) | Not stated as such; "means of payment" and liquidity (pp. 675–676) |
| Credit versus money | Huggett private IOUs and Proposition 2 (pp. 808–809); Townsend turnpike: currency valued only when loan markets are restricted (ch. 28, p. 1171); legal restrictions (§28.8, §9.8 p. 364) | Credit transfers versus cash; public credit and tallies (ch. 4); Bank currency (ch. 8) | Intermediation and banks (ch. 27); fractional reserves (p. 677) |
| Record-keeping and memory | Gift-giving equilibrium, with money substituting for memory (§9.9, pp. 364–365, citing Kocherlakota 1998); memory in contracts (ch. 22, "amnesia overwhelms memory," pp. 959–965) | Tally records and Exchequer accounting (pp. 171–190) | None |
| Clearing, netting, bills of exchange | Clearinghouse device in OLG time-0 trading (pp. 332, 340, 345); notes "cleared or netted out in a centralized clearinghouse" (p. 809) | Exchequer as clearing-house (p. 175); merchants settling balances by bills (p. 228); money-changers as clearinghouses (p. 229); inland bills discounted by banks (pp. 394–397) | Check clearing as a bank service only (p. 677) |
| Multilateral settlement | Time-0 Arrow–Debreu trades use clearing of net claims (§8.5, p. 255); complete markets need no money because of multilateral netting (p. 287); free-banking reading (p. 810, citing Kocherlakota–Wallace) | Bank of Amsterdam clearing mutual debts (p. 390); Exchequer–Bank clearing (p. 315) | None |

### 3.3 Results that bound an AI-designed mechanism
**Impossibility and uniqueness.**
- **Myerson–Satterthwaite:** no efficient, IC, IR and budget-balanced bilateral trade (Milgrom Thm 3.6, p. 78; Börgers Prop 3.12, p. 65).
- **Green–Laffont–Holmström:** VCG is the only efficient DSIC rule (Milgrom Thm 2.3, p. 56).
- VCG budget balance generally fails (Milgrom Thm 2.2, p. 54; Börgers §7.5).
- **Jehiel–Moldovanu:** efficient implementation fails with interdependent multidimensional values (Milgrom §3.3.6, p. 80; Börgers §9.3).
- **Gibbard–Satterthwaite** (Börgers §8.2; Pass Thm 12.2).
- **Roberts:** DSIC rules reduce to affine maximisers (Vohra Thm 4.2.14).
- **Arrow's theorem is not stated in any corpus file**; it appears only as a reference in Börgers' notes.

**Incentive constraints.**
- Revelation principle (Börgers Prop 3.1; Milgrom p. 141), with Diamantaras' caveat about multiple equilibria.
- Payoff and revenue equivalence (Milgrom Thms 3.3–3.5).
- Rochet cycle monotonicity (Vohra Thm 4.2.1).
- VCG's collusion, shill and monotonicity failures (Milgrom pp. 56–61, ch. 8).
- Crémer–McLean (Börgers §6.4) shows that correlated beliefs make extraction results fragile.

**Equilibrium existence and computation.**
- Finite stochastic games have stationary discounted equilibria (Solan Thm 8.11).
- A uniform value exists in zero-sum games (Thm 9.13).
- General multiplayer uniform-equilibrium existence is **open** (p. 189), and known algorithms are exponential (p. 161).
- Designs should therefore target discounted or correlated solution concepts: extensive-form correlated equilibrium always exists (§9.5).
- No-regret learners reach coarse correlated equilibria quickly (Roughgarden Prop 17.9, Cor 17.7), but only in time-average. The PPAD and Nash-hardness material is **not in the file**.

### 3.4 Space books: extracted resources versus territory; future-resource claims

**OST.** *Handbook* ch. 33, pp. 1118–1120:
- Art. I gives free access, "for the benefit … of all countries."
- Art. II bars national appropriation "by claim of sovereignty, by means of use or occupation, or by any other means."
- Art. VI requires states to authorise and continually supervise non-governmental actors.
- The treaty is silent on extraction. The authors read the silence as deliberate ambiguity.
- The high-seas analogy (fish and minerals) supports private title to *extracted* resources.
- The US State Department position is that non-appropriation applies to resources only "in place."
- Taking a whole asteroid could amount to territorial control, and the authors leave that open.

**Moon Agreement.** Ch. 33, p. 1122: Art. 4 and Art. 11 make resources "common heritage." Fewer than 20 parties. US Executive Order 13914 (2020) rejects it as customary law. *A City on Mars* ch. 13 adds political history.

**US CSLCA 2015.** Title IV, 51 U.S.C. §51303. Ch. 33, pp. 1123–1124:
- US citizens may "possess, own, transport, use, and sell" space resources they obtain.
- The authors read this as close to rule-of-capture or pedis possessio.
- A sense-of-Congress clause disclaims sovereignty.
- An IISL 2015 statement finds ownership of extracted resources compatible with the OST.

**Luxembourg 2017.** Law of 20 July 2017. Ch. 33, pp. 1129–1130: an explicit private right of ownership in extracted materials, with authorisation conditions: Luxembourg seat, governance, disclosure of 10% or larger owners, insurance, audits, and a €5,000–500,000 fee. The state lost about €12M on Planetary Resources.

**Artemis Accords (2020).** Ch. 33, pp. 1125–1126:
- §10: extraction does not violate the OST.
- §11: temporary "safety zones."
- *A City on Mars* (PDF pp. 285–289) argues safety zones can act as de facto area claims.
- Murnane counts 23 signatories (ch. 34, p. 1196).

**Other jurisdictions.**
- Ch. 33 (p. 1132): the UAE's 2019 law and Australia's 2018 Act **do not** address property in extracted resources.
- Murnane (ch. 34) reports a Japanese law similar to the US one.
- **Conflict:** *A City on Mars* (PDF p. 270) groups the UAE with the US, Japan and Luxembourg as having extraction-rights laws. Check the primary statutes.

**Tradable future-resource claims.** **None of the space books analyse futures, forwards or tradable claims.** The nearest analogues:
- (a) The Hague Working Group "Building Blocks" (2019) propose an **international registry of priority rights** to explore and produce in a defined area for a defined time, plus confirmation of resource rights (ch. 33, pp. 1132–1136).
- (b) NASA's 2020 solicitation to **buy lunar regolith** from contractors, described as policy precedent (ch. 34, p. 1195).
- (c) **LORS-101** (ch. 30, p. 999ff) adapts JORC, NI 43-101, CRIRSCO and PRMS resource/reserve reporting for investors, a precondition for financeable claims.
- *The Space Economy* covers only OST Art. VI, Artemis and Luxembourg as a haven, and *Space Business* nothing material.

### 3.5 intelligent-economy and annurev
- **intelligent-economy:** Huawei's 2022 corporate report, built on EY's CGE model. Topic: AI, 5G and IoT "intelligent economy" value (US$18.8 trillion by 2030). It contains **no labour-share, wage-distribution or ownership analysis**, apart from generic calls for equitable diffusion (ch. 5, p. 52). Relevance 0. Do not use it as evidence.
- **annurev:** Trammell & Korinek (2026), a peer-reviewed review of growth under transformative AI. It is directly about the **labour share** (it tends to zero if capital substitutes for labour), **wages** (ambiguous), and **distribution** (§6.2, concentration of capital and policy). Relevance 2: it motivates the programme's distribution and ownership problem but proposes no institution.

---

## 4. Records that could not be accessed and why

- **Muniesa (item 4):** a scanned image with no text layer. The file contains only even-numbered pages (odd pages, including contents p. vii, are missing). I OCR'd samples only. The fix is a complete copy, or full OCR of what is present, which still leaves about 50% missing.
- **Spence (item 17):** no text layer. Fully OCR'd locally, so expect occasional OCR character errors.
- **Greene (item 9):** online appendices A–F are not in the PDF.
- **Roughgarden (item 7):** only Lecture 17. Lectures 13–14 (equilibrium concepts and smoothness), 18 (swap regret) and 19–20 (complexity) are referenced but absent.
- **Vohra (item 19):** only chapter 4.
- **Page fidelity:** *Deep Utopia* and *A City on Mars* have no printed page numbers in the files, so I cite sections and PDF pages. RMT, *Deep Utopia* and the Handbook show conversion artefacts; the Handbook's page offset varies.
- **Identity mismatches:**
  - The RMT filename is garbled.
  - Spence is dated "apr" in the filename; the article is August 1973.
  - The Perez title differs ("Financial" versus "finance"), and so does the ISBN.
  - *Power and Progress* is in Spanish.
  - Seife's embedded ISBN differs from the filename.
- **Not externally verified:** items published after June 2026 (annurev 2026, Anthropic Institute WP 2026-02, NBER w35865, arXiv 2609.15802, Economic Index "Cadences"). I checked identity only against the documents' own metadata.
- **No file failed to open.**

**Peripheral files reviewed and excluded (relevance 0; finance or out of scope):**
- Fama–French five-factor model (JFE 2015); Ball et al. on accruals (JFE 2016); Bessembinder (ssrn-2900447); Asness et al. "Quality minus junk"; Gormsen–Huber–Jensen (ssrn-7093959); ML asset-pricing papers (ssrn-7458140, ssrn-7494298, arXiv 2409.09684, 2512.16251, 2605.28853, 2608.13056, `1417039.pdf`, three PLOS ONE papers, AlphaPortfolio, agentic AI for asset management, conformal portfolio selection).
- Investing manuals: Mauboussin and Rappaport; Valentine; *The Investment Checklist*.
- Fernholz, *Stochastic Portfolio Theory*; Embrechts et al. and Coles on extremes.
- An ASX quarterly report (`64751_rns…`); FinEx Metals presentation; Seedhouse, *SpaceX Starship* (engineering history).
- AI-safety and mathematics or complexity preprints.

---

## 5. Top established results the programme can rely on

- **Complete markets make money redundant through multilateral netting.** Money needs frictions such as limited commitment, spatial separation or missing records. *RMT* §8.5 p. 255 and §8.12 p. 287.
- **Unbacked currency has value only when private credit is restricted** (Townsend turnpike). *RMT* ch. 28, p. 1171.
- **Private IOU (inside-money) equilibrium is suboptimal**, and it can be read as notes netted in a central clearinghouse. *RMT* §18.10, pp. 808–810.
- **Kiyotaki–Wright search model:** monetary equilibria exist that overcome double coincidence of wants, with welfare analysis. *RMT* §29.8, pp. 1248ff.
- **"Money is memory" (Kocherlakota 1998) and incomplete record-keeping (Kocherlakota–Wallace 1998)** are *cited only* (*RMT* pp. 365, 810). Obtain the primary papers before relying on them.
- **Money is a legally constructed public institution.** Clearing of tallies, notes and bills was state-embedded. Desan pp. 1, 18, 175, 300 n. 22, 315, 390.
- **Capital's legal attributes** are priority, durability, universality and convertibility. Pistor pp. 2–3, 13–15.
- **Myerson–Satterthwaite impossibility.** Milgrom Thm 3.6 p. 78; Börgers Prop 3.12 p. 65.
- **VCG is the unique efficient DSIC mechanism and is generally not budget-balanced.** Milgrom Thms 2.2–2.3, pp. 54–56; Börgers §7.5.
- **Gibbard–Satterthwaite.** Börgers §8.2 pp. 142–149; Pass Thm 12.2 p. 120.
- **Roberts:** DSIC rules reduce to affine maximisers. Vohra Thm 4.2.14 p. 54.
- **Revelation principle** (truth-telling is *an* equilibrium only). Börgers Prop 3.1 p. 33; Milgrom p. 141.
- **Revenue and payoff equivalence; Myerson optimal auction.** Milgrom Thms 3.3–3.5 pp. 74–76; Börgers Prop 3.4 p. 40.
- **Jehiel–Moldovanu impossibility.** Milgrom §3.3.6 p. 80; Börgers §9.3 p. 158.
- **Stationary discounted equilibrium exists in finite stochastic games** (Fink–Takahashi), and a **uniform value exists in zero-sum games** (Mertens–Neyman). Solan Thm 8.11 p. 117; Thm 9.13 p. 139.
- **Multiplayer uniform-equilibrium existence is open.** Solan pp. 179, 189, 211.
- **No-regret dynamics converge in time-average to coarse correlated equilibria.** MW regret is O(√(ln n/T)). Roughgarden Thm 17.6, Prop 17.9, pp. 234–240.
- **Signaling equilibria require cost–type correlation, are multiple, and can be Pareto-inferior.** Spence pp. 358, 363, 365.
- **Performativity typology** (generic, effective, Barnesian, counter). MacKenzie pp. 16–18.
- **Space law:** non-appropriation (OST Art. II); the extracted-resource ownership position (US CSLCA §51303; Luxembourg 2017); Artemis §§10–11; the Moon Agreement's minimal uptake; Hague priority-rights registry proposal. *Handbook of Space Resources* ch. 33 pp. 1118–1136; ch. 34 pp. 1195–1196.
- **Under transformative AI the labour share may collapse and wage effects are ambiguous.** Trammell & Korinek 2026, pp. 591ff, Table 1.
