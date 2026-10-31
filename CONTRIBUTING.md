# Contributing

ValueGenomics is active independent research. The next scientific milestone is a preregistered real-data study; proposed improvements must preserve the distinction between hypotheses, model results and empirical validation.

Use the fork-and-pull workflow: fork → feature branch → implementation/documentation → tests → pull request → maintainer review → merge. Anyone can propose a change. Only authorised maintainers can merge; proposing a pull request does not grant write access. MoheetBrain remains the sole administrator.

```bash
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest experiments.exp001_circularity.test_exp001 -v
python scripts/verify_release.py
```

CI runs the existing unit tests and read-only publication verification, not the full simulations. Run expensive experiments separately, record the code/environment/seeds and compare against the saved reference outputs. When deliberately changing a baseline file, update its public digest and reason in `docs/PUBLICATION_MANIFEST.json` as part of the reviewed change; retain the original digest so the historical snapshot remains distinguishable. Preregister new hypotheses and thresholds before viewing results; label post-hoc analyses. Never replace negative results to improve a narrative.

Keep private invoice data, contact details, credentials, local paths and private conversations out of commits, PR text, logs and artifacts. Do not commit full copyrighted publications or third-party datasets without verified redistribution rights. Use a deliberately public Git identity, such as your GitHub noreply address.

Code contributions are offered under MIT and research/documentation contributions under CC BY 4.0, within rights you hold. Retain third-party notices and document provenance. Do not change licence terms, ownership controls or research conclusions without explicit maintainer review.

`main` requires a pull request; force pushes and deletion are blocked. Zero mandatory approvals allows the sole maintainer to merge their own reviewed changes without needing another account. CODEOWNERS identifies the maintainer but does not give visitors permission to push. The maintainer can continue creating branches, opening PRs and merging changes; the repository is not archived.
