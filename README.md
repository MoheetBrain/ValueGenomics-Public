# ValueGenomics

**Computational Discovery of Economic Systems**

> **What if we could decode the DNA of money—and use artificial intelligence to invent entirely new economic systems?**

ValueGenomics, also called **Economic Genome**, is an independent computational research project investigating the architecture of money, currencies, ownership, exchange and economic institutions. It asks whether their underlying rules can be represented mathematically, compared systematically and explored through computation.

[Framework](research/design-space.md) · [Experiment](experiments/experiment-001-spec.md) · [Results](results/experiment-001-summary.md) · [Code](experiments/exp001_circularity/) · [Source audit](research/source-manifest.md)

## The genome of money

Can economic institutions be represented as formal design spaces, simulated and systematically evaluated? The initial investigation decomposed currencies and assets into characteristics such as scarcity, stability, acceptance, liquidity, ownership, transferability, trust, enforceability, governance, settlement, information, participation and time. Earlier AI-assisted work expanded this into a high-dimensional property space, including a 99-property framing.

The important refinement was conceptual: **liquidity, acceptance and stability are often equilibrium outcomes, not variables a designer can simply choose.** The project therefore moved from describing monetary properties to specifying institutional rules. The [hypothesis ledger](research/original-ideas.md) and [prior-art review](research/prior-art.md) preserve that progression, including rejected ideas and corrected claims.

## The mathematical framework

The project's working institutional representation is:

$$M = (R, O, A, G, S, E, I, P, T)$$

| Variable | Institutional dimension | Variable | Institutional dimension | Variable | Institutional dimension |
|---|---|---|---|---|---|
| **R** | Resources and claims | **G** | Governance | **I** | Information and records |
| **O** | Ownership | **S** | Settlement | **P** | Participation, entry and exit |
| **A** | Allocation | **E** | Enforcement | **T** | Time and dynamics |

**Genotype:** rules that can be designed. **Phenotype:** allocation, settlement, trust, stability and distributional outcomes emerging when those rules interact with participants and their environment. This is a proposed research framework informed by established economics, not a demonstrated new scientific law. [Read the formulation and constraints →](research/design-space.md)

## AI-assisted economic discovery

Computational search, optimisation, simulation and mechanism design could explore alternative rule combinations under explicit feasibility, incentive and institutional constraints. A credible search needs held-out environments, strong baselines and falsification tests; optimising an unvalidated simulator can reward its artefacts.

```text
Economic design space → Institutional variables → Mathematical model
                     → Simulation → Evidence → Evaluation → New hypotheses
```

The repository contains AI-assisted source analysis, mathematical arguments, a twelve-candidate comparison, optimisation code and a seeded experiment. **It does not demonstrate an autonomous discovery engine or an AI-discovered superior currency.** Automated institutional search remains a research direction. [Candidate analysis](research/candidate-comparison.md) · [Adversarial review](research/adversarial-review.md)

## Experiment 001: Zero-Net

Zero-Net is one application of the framework: **can circular business debts be cancelled through consent-based multilateral set-off, without equivalent money transfers?** It studies settlement and information rules while retaining the existing unit of account. The mechanism has established prior art; the experiment does not claim to have invented clearing.

For an obligation graph with edge amounts $f$ and incidence matrix $B$, the implemented optimisation is:

$$\max_c \sum_e c_e \quad \text{subject to} \quad Bc=0, \quad 0\leq c\leq f.$$

Flow conservation preserves each firm's net position. The code compares optimal bounded circulation with bilateral netting, a greedy three-cycle heuristic and a netting bound, and includes exploratory default-shock analysis.

The [preregistered specification](experiments/experiment-001-spec.md) uses **ONS-calibrated synthetic firm networks**, 30 seeds per cell, participation strategies and 18 sensitivity variants. Its full saved run contains 2,100 economy/participation evaluations and 60 default-shock scenarios. Preregistration refers to the original private research history; [publication provenance](docs/PUBLICATION.md) explains the clean snapshot.

## Results and limitations

**Synthetic model results — 17 October 2026.** Clearability below is the share of participants' trade-credit book, defined in the specification; it is not measured cash savings.

| Reference setting | Mean clearability | Reported 95% interval |
|---|---:|---:|
| Full participation | **51.75%** | 50.85–52.64% |
| Anchor-led cluster: 20% of firms | **30.91%** | 28.27–33.56% |
| Random participation: 20% of firms | **5.27%** | 4.51–6.04% |

Anchor-led recruitment achieved **5.86×** the simulated clearability of random recruitment at the same 20% participation. The preregistered **CONTINUE** verdict means proceed to further research. The material-clearability threshold was a lower interval bound of 10%, with a full-participation upper bound below 3% as the kill criterion; the specification includes robustness and generator-validation gates.

Two hypotheses failed: sector aggregation did not overstate clearability by the hypothesised 2× (**1.14×** observed), and the topology predictor fell short of its out-of-sample $R^2\geq0.7$ threshold (**0.370** observed).

These are optimistic **model ceilings**, not real-world commercial validation. Networks assume non-strategic participation, a static closed domestic economy and universal consent within the selected group. The saved analysis identifies a substantial model–reality gap; its post-hoc calibration is labelled separately. Real UK invoice-network data are still required. **Zero-Net is not a business being launched.** Earlier commercial proposals are retained only as clearly labelled historical research context. [Full results and negative findings →](results/experiment-001-summary.md)

## Source code and reproducibility

The original run used **Python 3.14.7**, NumPy **2.5.4** and SciPy **1.18.1**; the pinned requirements also include openpyxl **3.1.5** for ONS extraction.

```bash
git clone https://github.com/MoheetBrain/ValueGenomics-Public.git
cd ValueGenomics-Public
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest experiments.exp001_circularity.test_exp001 -v
python scripts/verify_release.py
python scripts/summarise_exp001.py

# Optional smoke run: existing two-seed check; writes no result files.
python -m experiments.exp001_circularity.run --smoke
```

To rerun the full experiment, use a disposable worktree: the original runner rewrites `results/exp001/`. The saved outputs remain the reference; a full rerun is not part of lightweight CI.

```bash
git worktree add --detach ../ValueGenomics-reproduction HEAD
cd ../ValueGenomics-reproduction
../ValueGenomics-Public/.venv/bin/python scripts/extract_ons_iot.py
../ValueGenomics-Public/.venv/bin/python -m experiments.exp001_circularity.run
```

| Directory | Research content |
|---|---|
| [research/](research/) | Institutional ontology, hypotheses, prior art, candidate comparison and critical evaluation |
| [experiments/](experiments/) | Experiment specification, network generator, circulation algorithms, default model and tests |
| [data/](data/) | ONS 2023 workbook and extracted product-level matrices; retained under OGL v3.0 |
| [results/](results/) | Saved synthetic runs, uncertainty summaries, negative findings and labelled post-hoc analysis |
| [scripts/](scripts/) | Extraction, reporting, candidate analysis and publication verification |
| [docs/](docs/) | Historical research status, provenance and publication scope |

## Future research

The programme remains active. The next scientific milestone is a **preregistered real-data evaluation** of clearing on a consented, appropriately de-identified invoice network. Further questions include strategic participation, better out-of-sample predictors, distributional effects, enforceable claims and constrained computational search over institutional rules. These are open questions, not completed findings. [Research roadmap](docs/RESEARCH_ROADMAP.md)

## Citation, copyright and licensing

Created and maintained by **[MoheetBrain](https://github.com/MoheetBrain)**, with AI assistance documented in the original research headers and [authorship note](AUTHORS.md). This is independent research; peer review and novelty priority are not claimed.

- **Original software:** [MIT](LICENSE).
- **Original research, documentation and research compilations:** [CC BY 4.0](DATA_LICENSE.md), within the rights held by the contributors.
- **ONS inputs and extracts:** [Open Government Licence v3.0](THIRD_PARTY_NOTICES.md); original source rights and attribution remain intact.

Cite [CITATION.cff](CITATION.cff), credit the project, retain source-level attribution and indicate changes as required by the applicable licence. These licences permit commercial reuse; they do not confer ownership of abstract ideas or economic mechanisms. [Notice](NOTICE.md) · [Contributing through forks and pull requests](CONTRIBUTING.md)
