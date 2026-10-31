# Public edition and preservation record

**Public edition:** 31 October 2026. **Underlying research snapshot:** 17 October 2026.

ValueGenomics is independent computational research into money and economic institutions. The opening question is whether monetary architecture can be formally decomposed and explored computationally. Zero-Net is one experiment; earlier product/commercial recommendations are historical context and are not a venture being launched. The current scientific roadmap is in [RESEARCH_ROADMAP.md](RESEARCH_ROADMAP.md).

## Why this is a clean snapshot

The original private repository's reachable history contains a personal author email. Its source manifests and conversation audits also include local filesystem paths and private personal context. Removing text from the latest commit would not remove the historical objects. Under the owner's publication instructions, the complete original repository and all branches were backed up privately, and this independent public snapshot was prepared without importing its Git object database or original commit metadata.

The public repository is **MoheetBrain/ValueGenomics-Public**. The original **MoheetBrain/ValueGenomics** remains private, unarchived and unchanged in scientific content. No original branch was deleted, rebased or force-pushed. A private preservation tag and a verified full-history Git bundle retain the source state. Public commits use the maintainer's intentionally public GitHub noreply identity.

## Audited source scope

The original audit covered **8 commits**, **130 distinct reachable file blobs**, all three original branches, tags, author/committer metadata, deleted historical file versions, hidden/configuration files and the workbook's ZIP/XML contents. Common credential/private-key/authentication-URL patterns, contact details, local paths and sensitive personal context were checked. No credential match was found. The workbook contains a public ONS team contact, verified against its official dataset page; it is retained as part of the published source.

There were **no original GitHub Actions runs or artifacts**. No full source books, articles, brokerage records or raw private conversation archives were present in tracked files; references to private sources nevertheless required editing before publication. Pattern scanning has limits and is not an assertion that undisclosed secrets cannot exist.

## File-by-file preservation

[PUBLICATION_MANIFEST.json](PUBLICATION_MANIFEST.json) accounts for all **42 original main-branch files**. **26 remain byte-identical** and **16 have public editorial editions**. Every existing Python file, experiment specification, input dataset and saved result is unchanged. Original versions of all editorially modified files remain in the private repository and backup.

| Public treatment | Files | Reason |
|---|---|---|
| Replaced by explicitly labelled public provenance summaries | Four files in `sources/pasted/`; `research/audit/archives-part1.md`; `research/audit/archives-part2.md` | Exclude private conversations, personal context, filenames and pasted instructions while retaining topic/origin/evidence boundaries |
| Public provenance/bibliography editions | `research/source-manifest.md`; `research/audit/books-and-papers.md` | Remove private library paths and acquisition details; retain scholarly references, corrections, data hashes and source limitations |
| Historical status/ledger editions | `docs/PROJECT_STATUS.md`; `docs/PROJECT_LEDGER.md` | Remove personal objectives and local paths; distinguish historical direction from the current independent research programme |
| Historical analytical editions | `research/flagship-decision.md`; `research/final-decision-memo.md`; `research/candidate-comparison.md`; `research/adversarial-review.md`; `research/governance-and-rights.md` | Omit personal financial targets where present; label earlier commercial/pilot discussion as superseded without changing equations, experimental choices or findings |
| New landing page | `README.md` | Present the Economic Genome motivation, nine-dimensional institutional framework, AI-assisted research direction and one subordinate experiment |

Original proofs, methods, simulation parameters, hypotheses, statistical results, negative findings and dated source-level analysis were not rewritten to improve the story. In particular H2 and H4 remain unsupported. The public edition adds no new economic research and makes no claim of peer review, established novelty or real-world commercial validation.

## Additional private branches

The backup also retains `research/monetary-substrates` and `research/private-equity-access`, including their code, observations, negative results and documentation. Those branch-only files are **not included in this first public core snapshot**. Their source registry includes mixed licensing and third-party market-data rights that require a separate publication review; they are not covered by this release's blanket project attribution. No records were discarded or quietly relicensed. The core release includes the complete requested institutional framework and Zero-Net Experiment 001.

## Experiment provenance and reproducibility

Original main source commit: `558b1414c25f557065b308913f696d50b405514c`. The saved result metadata records the original preregistration commit `fc2561e`; the full commit ID remains in the unchanged JSON. This is preregistration in the private project's sequence, not an external public registration or independently time-stamped registry. The clean public history does not expose the private commit objects. Exact specification/result hashes in the manifest allow inspection of what was preserved.

The publication checks used **Python 3.14.7**, NumPy **2.5.4**, SciPy **1.18.1** and openpyxl **3.1.5**, matching the pinned dependencies and original run environment. Checks include:

- All **15 existing unit tests**.
- Existing two-seed smoke run across the reference and sensitivity blocks, completed in **104.7 seconds**, with no result files written.
- Read-only reconciliation of **2,100 saved evaluations**, **60 default-shock scenarios** and **320 metric aggregates**, including means, dispersion, reported intervals, recruitment ratio and the out-of-sample predictor result.
- Byte preservation of the original code, specification, input data and saved outputs, plus exact hashes for each public edition.
- Regeneration of the ONS extracts only in a disposable copy and comparison against the saved extracts.
- README/local documentation link checks and citation syntax checks.

The original full-scale simulation was not rerun for publication. Its results remain those recorded on 17 October 2026. Reproduction commands run the unchanged original code in a disposable worktree; runtime/environment metadata will naturally differ. CI runs the unit suite and read-only result checks, not full-scale simulations. Historical assertions such as “first UK estimate” in retained notes are dated author assessments, not a verified priority claim adopted by this publication.

## Data rights and attribution

Official [ONS content terms](https://www.ons.gov.uk/help/terms-conditions), the [2023 dataset page](https://www.ons.gov.uk/economy/nationalaccounts/supplyandusetables/datasets/ukinputoutputanalyticaltablesdetailed) and [OGL v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) were checked for this release. The ONS workbook and extracts can be distributed with the required attribution and applicable exceptions. They retain OGL v3.0, not a claim of exclusive project ownership. Original software uses MIT; original research/documentation and synthetic compilations use CC BY 4.0 within contributors' rights. Third-party quotations/publications are excluded from that grant. See [third-party notices](../THIRD_PARTY_NOTICES.md) and [data licence](../DATA_LICENSE.md).

## Maintainer-controlled participation

MoheetBrain retains sole administrator control. Visitors can read, clone, fork and propose pull requests but receive no write permission. `main` is protected against direct changes, force pushes and deletion, with pull requests required and zero mandatory approvals so the sole maintainer can merge their own work. CODEOWNERS identifies `@MoheetBrain`; it does not grant access. Settings are verified again after public visibility is enabled.

The wiki is disabled. The test workflow uses only full-SHA-pinned official GitHub actions, a read-only contents token and no persisted checkout credentials. It does not use privileged `pull_request_target`, secrets, deployment or third-party services. Repository Actions permissions are restricted to read-only defaults, with action-created approving reviews disabled. No collaborator or outside administrator is added. The original private repository remains available for continued private research; safe changes can be proposed to this public repository through feature branches and pull requests.
