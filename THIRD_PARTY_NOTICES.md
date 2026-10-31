# Third-party notices

## Office for National Statistics

**Source:** Office for National Statistics (ONS), *UK input-output analytical tables: product by product*, **2023 edition**, released **11 December 2025**. Original retrieval: **17 October 2026**.

- [Official dataset page](https://www.ons.gov.uk/economy/nationalaccounts/supplyandusetables/datasets/ukinputoutputanalyticaltablesdetailed)
- [2023 workbook download](https://www.ons.gov.uk/file?uri=/economy/nationalaccounts/supplyandusetables/datasets/ukinputoutputanalyticaltablesdetailed/2023/iot2023product.xlsx)
- [ONS content terms](https://www.ons.gov.uk/help/terms-conditions)
- [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)

**Contains public sector information licensed under the Open Government Licence v3.0. Source: Office for National Statistics.** Crown copyright applies to the source information. No ONS endorsement is implied.

Files: `data/raw/ons_iot2023product.xlsx`, `data/processed/ons_iot2023_domestic_Z.csv`, `data/processed/ons_iot2023_products.csv`. The workbook and existing extracts are unchanged. The extraction script selects the 104-product domestic flow matrix and output column; the simulation loader removes imputed owner-occupied rent and clips remaining negative values as documented in the original code. Those are existing modelling transformations, not corrections made during publication.

The official ONS terms and OGL were checked on **31 October 2026**. They permit copying, distribution and adaptation with attribution, subject to excluded rights. OGL does not cover third-party rights, personal data or separate trademarks. The workbook's public ONS team contact is part of the published source, not a private personal contact introduced by this project.

## Publications and references

Books, articles, papers, legal authorities and websites cited in research notes retain their own rights. Research annotations and brief attributed excerpts do not grant reuse rights over the underlying publications. No complete third-party book or article is bundled. Source verification dates in the historical notes remain 17 October 2026 and were not silently refreshed.

## Software dependencies

NumPy, SciPy, openpyxl and their dependencies are installed from the versions in `requirements.txt`; their source/distributions are not bundled here. Their own licences and notices apply. GitHub Actions use official GitHub-owned actions pinned to full commit IDs, not vendored code.

## Other research branches

The private archive also preserves monetary-substrate and private-equity-access investigations. Those branch-only files are outside this public core snapshot. Their registry covers mixed rights, including ambiguous ontology licences and third-party market-data sources; a separate source-by-source publication review is required before those datasets can be added. This release does not relicense them or claim they are publicly downloadable. The complete original branches remain preserved privately.
