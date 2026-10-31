"""Read-only checks for the public research snapshot and its saved results.

No experiment is rerun and no result file is rewritten. Uses the original
experiment's aggregation and predictor functions to check the published CSVs.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from experiments.exp001_circularity.run import ci, lovo_r2


def close(actual, expected, label):
    if isinstance(expected, bool):
        assert actual == expected, label
    elif isinstance(expected, (float, int)):
        assert math.isclose(float(actual), float(expected), rel_tol=1e-10, abs_tol=1e-12), label
    else:
        assert actual == expected, label


def main():
    manifest = json.loads((ROOT / 'docs/PUBLICATION_MANIFEST.json').read_text())
    for entry in manifest['entries']:
        p = ROOT / entry['path']
        assert p.is_file(), entry['path']
        assert hashlib.sha256(p.read_bytes()).hexdigest() == entry['public_sha256'], entry['path']
        if entry['status'] == 'unchanged':
            assert entry['public_sha256'] == entry['original_sha256'], entry['path']
    print(f"Publication manifest: {len(manifest['entries'])} original-file dispositions verified")

    with (ROOT / 'results/exp001/runs.csv').open(newline='') as f:
        runs = list(csv.DictReader(f))
    with (ROOT / 'results/exp001/defaults.csv').open(newline='') as f:
        defaults = list(csv.DictReader(f))
    summary = json.loads((ROOT / 'results/exp001/summary.json').read_text())
    assert len(runs) == 2100 and len(defaults) == 60
    assert all(r['checks_ok'] == 'True' for r in runs)
    assert summary['all_checks_ok'] is True and summary['n_seeds'] == 30
    checked = 0

    def check_cell(records, metrics, label):
        nonlocal checked
        assert len(records) == 30, label
        for metric, saved in metrics.items():
            computed = ci([float(r[metric]) for r in records])
            assert set(computed) == set(saved), (label, metric)
            for key, value in saved.items():
                close(computed[key], value, (label, metric, key))
            checked += 1

    for setting, metrics in summary['E1_reference'].items():
        strategy, p = setting.split('@')
        group = [r for r in runs if r['block'] == 'E1' and r['strategy'] == strategy and float(r['p']) == float(p)]
        check_cell(group, metrics, setting)
    for variant, settings in summary['E2_sensitivity_phi_book_mtcs'].items():
        for setting, saved in settings.items():
            strategy, p = setting.split('@')
            group = [r for r in runs if r['block'] == 'E2' and r['variant'] == variant and r['strategy'] == strategy and float(r['p']) == float(p)]
            check_cell(group, {'phi_book_mtcs': saved}, (variant, setting))
    for setting, metrics in summary['E4_default_shock_exploratory'].items():
        strategy, p = setting.split('@')
        group = [r for r in defaults if r['strategy'] == strategy and float(r['p']) == float(p)]
        check_cell(group, metrics, setting)

    decision = summary['decision']
    full = summary['E1_reference']['all@1.0']['phi_book_mtcs']
    anchor = summary['E1_reference']['anchor@0.2']['phi_book_mtcs']
    random = summary['E1_reference']['random@0.2']['phi_book_mtcs']
    close(anchor['mean'] / random['mean'], decision['H3_anchor_over_random_ratio_p0.2'], 'H3')
    close(summary['E3_sector_level_phi'] / full['mean'], decision['H2_sector_over_firm_ratio'], 'H2')
    all_runs = [{k: float(v) if k in ('phi_book_mtcs', 'reciprocity', 'scc_weight_share', 'mean_out_degree') else v for k, v in r.items()}
                for r in runs if r['strategy'] == 'all']
    predictor = lovo_r2(all_runs)
    close(predictor['r2_out_of_sample'], decision['H4_topology_predictor']['r2_out_of_sample'], 'H4')
    assert decision['verdict'] == 'CONTINUE'
    assert decision['H2_supported'] is False and decision['H3_supported'] is True and decision['H4_supported'] is False
    assert full['ci95_low'] >= 0.1 and anchor['ci95_low'] >= 0.1
    assert decision['robust_share_all_ge_10pct'] >= 0.7 and decision['V1_passed']
    print(f'Saved results: 2,100 evaluations, 60 default scenarios and {checked} metric aggregates reconcile')
    print('Headline means: full 51.75%; anchor p=0.2 30.91%; random p=0.2 5.27%')
    print('Negative results retained: H2 unsupported; H4 unsupported. No files modified.')


if __name__ == '__main__':
    main()
