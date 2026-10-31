# Source manifest — public edition

Compiled from the original 17 October 2026 research snapshot. This publication retains scholarly references, original research annotations, data provenance and explicit uncertainty. Private conversation originals, personal goals, local library paths and source-acquisition details are not published. Topic-level summaries occupy the original pasted-document and conversation-audit paths so the intellectual provenance remains discoverable.

## Founding sources and evidence boundaries

| Public provenance note | Origin and role |
|---|---|
| [Founding mandate](../sources/pasted/2026-10-17_01_project-discovery-mandate.md) | Founder instructions: source audit, mathematical formulation, experiments, falsification |
| [Frontier report](../sources/pasted/2026-10-17_02_frontier-research-mandate-and-programme-01.md) | Earlier AI output; introduced clearing and mutual credit; factual corrections retained in prior-art.md |
| [Zero-inspired hypotheses](../sources/pasted/2026-10-17_03_zero-x-economic-genome.md) | Earlier AI analogies and mechanism proposals; not empirical evidence |
| [Genome reconstruction](../sources/pasted/2026-10-16_04_economic-genome-reconstruction.md) | Earlier AI reconstruction and high-dimensional property space; claimed origin/archive not verified |
| [Conversation audit 1](audit/archives-part1.md) / [audit 2](audit/archives-part2.md) | Topic-level public summaries; full private audits remain in the private archive |
| [Scholarly audit](audit/books-and-papers.md) | Research annotations and bibliographic references; source books/papers not bundled |
| [Primary-source verification](audit/prior-art-verification.md) | Existing dated fact checks and literature verification, not a current update |

The source audit found that the clearing strand entered through earlier AI-generated reports, rather than through the founder's archived monetary questions. Its validity depends on external evidence and the formal experiment, not that conversational origin. The original claimed August origin and promised earlier research repository were not verified. Missing source attachments remain missing; no results are inferred from them.

## Scholarly references and original audit findings

Relevance 3 = directly load-bearing for the decision. Full table: `books-and-papers.md` §1.

| Source | Identity verified | Relevance | Load-bearing content |
|---|---|---|---|
| Ljungqvist & Sargent, *Recursive Macroeconomic Theory* 4e (2018) | yes | 3 | Complete markets make money redundant via multilateral netting (§8.5 p.255; §8.12 p.287); Townsend turnpike (ch.28); private IOUs netted in a clearinghouse (§18.10 pp.808–810); Kiyotaki–Wright (§29.8) |
| Desan, *Making Money* (2014) | yes | 3 | Money as a legally constructed institution; Exchequer and Bank of Amsterdam as clearing houses (pp.175, 390) |
| Milgrom, *Putting Auction Theory to Work* (2004) | yes | 3 | Myerson–Satterthwaite (Thm 3.6); VCG uniqueness and budget-balance failure (Thms 2.2–2.3) |
| Börgers, *Theory of Mechanism Design* (2015) | yes | 3 | Revelation principle, Gibbard–Satterthwaite, Jehiel–Moldovanu |
| Pistor, *The Code of Capital* (2019) | yes | 3 | Legal attributes of capital (priority, durability, universality, convertibility) |
| *Handbook of Space Resources* (2023), chs 33–34 | yes | 3 (law) | OST Art. II; CSLCA §51303; Luxembourg 2017; Artemis §§10–11; Hague priority-rights registry |
| Solan, *Stochastic Game Theory* (2022) | yes | 2 | Equilibrium existence; multiplayer uniform equilibrium open |
| Roughgarden, Lecture 17 (2016) | yes (chapter only) | 2 | No-regret → coarse correlated equilibrium |
| Trammell & Korinek, *Annu. Rev. Econ.* (2026) | metadata only | 2 | Labour share under transformative AI |
| MacKenzie, Padgett & Powell, Spence, Vohra, Pass, *A City on Mars* | yes | 2 | Performativity, historical clearing via bills, signalling, IC, space politics |
| Seife, *Zero* (2000) | yes | 0 (economics) | Chapter claims of the pasted Zero report verified (§3.1). No economic results. |
| Muniesa, *The Provoked Economy* | partial | 2 | **Image-only, even pages only**; sample OCR |
| Others (Greene, Cowen–Tabarrok, Perez, Bostrom, Huawei/EY, space business books) | yes | 0–1 | Background only |


## Data acquired for Experiment 001


| File | Bytes | SHA-256 (16) | Source and licence | Use |
|---|---:|---|---|---|
| `data/raw/ons_iot2023product.xlsx` | 845,524 | `14d8f4bd2993f8f0` | ONS, *UK input-output analytical tables, product by product, 2023* (released Dec 2025); downloaded 2026-10-17 from ons.gov.uk; Open Government Licence v3.0 | Calibrates Experiment 001 |
| `data/processed/ons_iot2023_domestic_Z.csv` | 105,927 | `5447f014030791da` | Extracted by `scripts/extract_ons_iot.py` | Domestic intermediate flows, 104×104, £m |
| `data/processed/ons_iot2023_products.csv` | 6,852 | `0f2fb4a77d1d78ac` | Same | Product codes, names, output |


The ONS workbook and extracted CSVs are preserved byte-for-byte. Source: [ONS product-by-product input-output analytical tables, 2023 edition](https://www.ons.gov.uk/economy/nationalaccounts/supplyandusetables/datasets/ukinputoutputanalyticaltablesdetailed), released 11 December 2025; retrieved in the original research on 17 October 2026. Contains public sector information licensed under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). Source: Office for National Statistics. See [third-party notices](../THIRD_PARTY_NOTICES.md).

## Data still missing

No real UK firm-level invoice graph is included. The original research identified restricted-access sources and a registration-gated Sarafu dataset, but did not acquire those data. Synthetic networks remain a model ceiling. A consented real-data research evaluation is the next scientific milestone.

The two additional private research branches (monetary substrates and private-equity access) are preserved in the complete private backup. Their raw-source and derived-data licensing requires a separate release review; none of those branch-only datasets is silently included under this snapshot's CC BY grant. This public release covers the audited core Economic Genome framework and Zero-Net Experiment 001.
