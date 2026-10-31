"""Unit tests for Experiment 001. Run: .venv/bin/python -m unittest experiments.exp001_circularity.test_exp001 -v"""
from __future__ import annotations

import unittest

import numpy as np

from .clearing import (
    Network,
    bilateral_netting,
    is_circulation,
    max_circulation,
    net_positions,
    netting_bound,
    residual_is_acyclic,
    sequenced_liquidity,
    short_cycle_greedy,
)
from .defaults import loss_split
from .network import EconomyParams, generate, sector_network, select_participants


def net(edges, n=None):
    s, d, a = zip(*edges)
    return Network(n or max(max(s), max(d)) + 1, np.array(s), np.array(d), np.array(a, dtype=float))


def random_network(rng, n=40, m=200):
    pairs = set()
    while len(pairs) < m:
        s, d = rng.integers(0, n, 2)
        if s != d:
            pairs.add((int(s), int(d)))
    s, d = map(np.array, zip(*sorted(pairs)))
    return Network(n, s, d, rng.lognormal(0, 1, m))


def cycle_decomposition(nw: Network, c: np.ndarray, eps: float = 1e-9):
    """Decompose a circulation into weighted simple cycles (lists of edge indices)."""
    c = c.copy()
    out: dict[int, list[int]] = {}
    for e, s in enumerate(nw.src):
        out.setdefault(int(s), []).append(e)
    cycles = []
    while c.max(initial=0) > eps:
        e0 = int(np.argmax(c))
        path, pos = [e0], {int(nw.src[e0]): 0}
        v = int(nw.dst[e0])
        while v not in pos:
            pos[v] = len(path)
            e = max(out[v], key=lambda k: c[k])
            path.append(e)
            v = int(nw.dst[e])
        cyc = path[pos[v]:]
        w = min(c[e] for e in cyc)
        for e in cyc:
            c[e] -= w
        cycles.append((cyc, w))
    return cycles


class ClearingToyCases(unittest.TestCase):
    def test_equal_triangle_fully_cleared(self):
        nw = net([(0, 1, 10), (1, 2, 10), (2, 0, 10)])
        self.assertAlmostEqual(max_circulation(nw).sum(), 30)
        self.assertAlmostEqual(short_cycle_greedy(nw).sum(), 30)
        self.assertAlmostEqual(bilateral_netting(nw).sum(), 0)
        self.assertAlmostEqual(netting_bound(nw), 30)

    def test_unequal_triangle_clears_minimum(self):
        nw = net([(0, 1, 10), (1, 2, 6), (2, 0, 8)])
        c = max_circulation(nw)
        np.testing.assert_allclose(c, [6, 6, 6], atol=1e-9)
        self.assertTrue(is_circulation(nw, c))
        self.assertTrue(residual_is_acyclic(nw, c))
        np.testing.assert_allclose(net_positions(nw, nw.amt - c), net_positions(nw), atol=1e-9)

    def test_bilateral_pair(self):
        nw = net([(0, 1, 5), (1, 0, 3)])
        self.assertAlmostEqual(bilateral_netting(nw).sum(), 6)
        self.assertAlmostEqual(max_circulation(nw).sum(), 6)

    def test_chain_has_nothing_to_clear_but_netting_bound_is_positive(self):
        nw = net([(0, 1, 10), (1, 2, 10)])
        self.assertAlmostEqual(max_circulation(nw).sum(), 0)
        self.assertAlmostEqual(netting_bound(nw), 10)  # needs novation of 0->1->2 into 0->2
        self.assertAlmostEqual(sequenced_liquidity(nw, nw.amt), 10)

    def test_sequenced_liquidity_rejects_cycles(self):
        with self.assertRaises(ValueError):
            sequenced_liquidity(net([(0, 1, 1), (1, 0, 1)]), np.array([1.0, 1.0]))


class Propositions(unittest.TestCase):
    def test_p1_mtcs_plus_sequencing_reaches_netting_liquidity(self):
        """Proposition 1: after optimal MTCS the residual is acyclic and settles with exactly the
        sum of net debit positions — the same cash a central counterparty would need."""
        rng = np.random.default_rng(1)
        for _ in range(20):
            nw = random_network(rng)
            c = max_circulation(nw)
            self.assertTrue(is_circulation(nw, c))
            self.assertTrue(residual_is_acyclic(nw, c))
            debit = np.clip(-net_positions(nw), 0, None).sum()
            self.assertAlmostEqual(sequenced_liquidity(nw, np.where(nw.amt - c > 1e-9 * nw.amt.max(), nw.amt - c, 0)), debit,
                                   delta=1e-6 * nw.amt.sum())

    def test_algorithm_ordering(self):
        rng = np.random.default_rng(2)
        for _ in range(20):
            nw = random_network(rng)
            b, g, m = bilateral_netting(nw).sum(), short_cycle_greedy(nw).sum(), max_circulation(nw).sum()
            self.assertLessEqual(b, g + 1e-9)
            self.assertLessEqual(g, m + 1e-6 * nw.amt.sum())
            self.assertLessEqual(m, netting_bound(nw) + 1e-6 * nw.amt.sum())
            self.assertTrue(is_circulation(nw, short_cycle_greedy(nw)))

    def test_p2_participation_lower_bound(self):
        """Proposition 2: clearing among participants P is at least the weight of cycles of a full
        optimal circulation that lie entirely inside P (so E[cleared] >= sum_C w_C |C| p^|C|)."""
        rng = np.random.default_rng(3)
        for _ in range(10):
            nw = random_network(rng, n=30, m=150)
            c = max_circulation(nw)
            cycles = cycle_decomposition(nw, c)
            self.assertAlmostEqual(sum(w * len(cy) for cy, w in cycles), c.sum(), delta=1e-6 * c.sum() + 1e-9)
            members = np.flatnonzero(rng.random(nw.n) < 0.6)
            inside = np.zeros(nw.n, bool)
            inside[members] = True
            surviving = sum(w * len(cy) for cy, w in cycles if all(inside[nw.src[e]] for e in cy))
            sub, _ = nw.subnetwork(members)
            self.assertGreaterEqual(max_circulation(sub).sum() + 1e-6 * nw.amt.sum(), surviving)

    def test_p4_set_off_before_insolvency_transfers_from_outside_creditors(self):
        """Proposition 4 on the British Eagle configuration: D owes B 10 and an outside creditor 10;
        A owes D 10; B owes A 10. D has no other assets. Clearing the cycle D->B->A->D before D's
        insolvency moves 5 of loss from B (paid in full by set-off) to D's outside creditor."""
        nw = net([(3, 1, 10), (0, 3, 10), (1, 0, 10)], n=4)  # D=3, B=1, A=0
        outside = np.array([0.0, 0.0, 0.0, 10.0])
        assets = np.array([100.0, 100.0, 100.0, 0.0])
        participant = np.ones(4, bool)
        before = loss_split(nw, nw.amt, outside, assets, participant)
        after = loss_split(nw, nw.amt - max_circulation(nw), outside, assets, participant)
        self.assertAlmostEqual(before.participant_firms, 5)
        self.assertAlmostEqual(before.outside_creditors, 5)
        self.assertAlmostEqual(after.participant_firms, 0)
        self.assertAlmostEqual(after.outside_creditors, 10)
        self.assertAlmostEqual(before.total, after.total)


class Generator(unittest.TestCase):
    def test_deterministic_and_valid(self):
        p = EconomyParams(n_firms=300, supplier_median=6)
        a, b = generate(p, 7), generate(p, 7)
        np.testing.assert_array_equal(a.net.src, b.net.src)
        np.testing.assert_allclose(a.net.amt, b.net.amt)
        self.assertTrue(0 < a.spend_coverage <= 1)
        self.assertEqual(len(np.unique(a.sector)), 103)
        pairs = set(zip(a.net.src.tolist(), a.net.dst.tolist()))
        self.assertEqual(len(pairs), a.net.m)

    def test_configuration_null_preserves_degrees_and_spend(self):
        p = EconomyParams(n_firms=300, supplier_median=6)
        io, cf = generate(p, 9), generate(p.with_(structure="configuration"), 9)
        np.testing.assert_array_equal(np.bincount(io.net.src, minlength=300), np.bincount(cf.net.src, minlength=300))
        self.assertAlmostEqual(io.net.amt.sum(), cf.net.amt.sum(), delta=1e-6 * io.net.amt.sum())

    def test_participation_strategies(self):
        econ = generate(EconomyParams(n_firms=300, supplier_median=6), 11)
        rng = np.random.default_rng(0)
        for strat in ("random", "sme_random", "anchor"):
            sel = select_participants(econ, strat, 0.2, rng)
            self.assertEqual(len(sel), 60)
            self.assertEqual(len(np.unique(sel)), 60)
        self.assertIn(int(np.argmax(econ.size)), select_participants(econ, "anchor", 0.2, rng).tolist())
        self.assertEqual(len(select_participants(econ, "all", 0.2, rng)), 300)

    def test_sector_network(self):
        sn = sector_network()
        self.assertEqual(sn.n, 103)
        self.assertTrue(np.all(sn.src != sn.dst))


class TopologyAndPredictor(unittest.TestCase):
    def test_topology_toy(self):
        from .run import topology
        t = topology(net([(0, 1, 1), (1, 2, 1), (2, 0, 1), (1, 0, 1)], n=4))
        self.assertAlmostEqual(t["reciprocity"], 0.5)  # 0->1 and 1->0 reciprocate; 2 of 4 edges
        self.assertAlmostEqual(t["scc_node_share"], 0.75)
        self.assertAlmostEqual(t["scc_weight_share"], 1.0)
        self.assertAlmostEqual(t["mean_out_degree"], 1.0)

    def test_lovo_recovers_exact_relationship(self):
        from .run import logit, lovo_r2
        rng = np.random.default_rng(5)
        rows = []
        for g in range(6):
            for _ in range(10):
                r, s, d = rng.uniform(0.02, 0.2), rng.uniform(0.2, 0.9), rng.uniform(3, 30)
                y = 1 / (1 + np.exp(-(-1.0 + 0.5 * logit(np.array(r)) + 0.8 * logit(np.array(s)) + 0.3 * np.log(d))))
                rows.append({"variant": f"v{g}", "phi_book_mtcs": float(y), "reciprocity": r,
                             "scc_weight_share": s, "mean_out_degree": d})
        out = lovo_r2(rows)
        self.assertGreater(out["r2_out_of_sample"], 0.999)
        self.assertAlmostEqual(out["coefficients_full_fit"]["logit_scc_weight_share"], 0.8, places=6)


if __name__ == "__main__":
    unittest.main()
