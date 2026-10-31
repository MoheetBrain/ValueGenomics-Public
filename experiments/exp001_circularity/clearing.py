"""Obligation-clearing algorithms for Experiment 001.

An obligation network is a list of directed edges (debtor -> creditor, amount > 0) over n firms.
All algorithms return the amount cleared on each edge, c_e in [0, f_e]. A clearing is valid
only if it is a circulation: every firm's cleared payables equal its cleared receivables, so no
firm's net position changes and no money moves.

Algorithms
----------
bilateral_netting : offsets only pairs that owe each other (2-cycles).
short_cycle_greedy: bilateral netting, then greedy offset of directed triangles (3-cycles);
                    a stand-in for the simple "find cycles and offset them" tools.
max_circulation   : optimal multilateral trade-credit set-off (MTCS) — the maximum circulation
                    bounded by the obligations, solved exactly as a linear programme.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import scipy.sparse as sp
from scipy.optimize import linprog


@dataclass(frozen=True)
class Network:
    n: int
    src: np.ndarray  # debtor index per edge
    dst: np.ndarray  # creditor index per edge
    amt: np.ndarray  # outstanding obligation per edge (> 0)

    def __post_init__(self) -> None:
        if not (len(self.src) == len(self.dst) == len(self.amt)):
            raise ValueError("edge arrays differ in length")
        if np.any(self.src == self.dst):
            raise ValueError("self-loops are not obligations between distinct firms")
        if np.any(self.amt <= 0):
            raise ValueError("obligation amounts must be positive")

    @property
    def m(self) -> int:
        return len(self.amt)

    def subnetwork(self, members: np.ndarray) -> tuple["Network", np.ndarray]:
        """Edges whose debtor and creditor are both members; returns (network, edge index)."""
        inside = np.zeros(self.n, dtype=bool)
        inside[members] = True
        keep = np.flatnonzero(inside[self.src] & inside[self.dst])
        return Network(self.n, self.src[keep], self.dst[keep], self.amt[keep]), keep


def net_positions(net: Network, amt: np.ndarray | None = None) -> np.ndarray:
    """b_i = receivables - payables (positive: net creditor)."""
    a = net.amt if amt is None else amt
    b = np.zeros(net.n)
    np.add.at(b, net.dst, a)
    np.subtract.at(b, net.src, a)
    return b


def is_circulation(net: Network, c: np.ndarray, rtol: float = 1e-7) -> bool:
    scale = max(float(net.amt.sum()), 1.0)
    return bool(np.all(c >= -rtol * scale)) and bool(np.all(c <= net.amt + rtol * scale)) and float(
        np.abs(net_positions(net, c)).max(initial=0.0)
    ) <= rtol * scale


def netting_bound(net: Network) -> float:
    """Largest possible reduction in gross obligations if all of them could be novated to a
    central counterparty: gross minus the sum of net debit positions. Not achievable by set-off
    on existing edges in general; reported as an upper bound."""
    b = net_positions(net)
    return float(net.amt.sum() - np.clip(-b, 0, None).sum())


def bilateral_netting(net: Network) -> np.ndarray:
    c = np.zeros(net.m)
    index = {(int(s), int(d)): e for e, (s, d) in enumerate(zip(net.src, net.dst))}
    for (s, d), e in index.items():
        r = index.get((d, s))
        if r is not None and e < r:
            x = min(net.amt[e], net.amt[r])
            c[e] += x
            c[r] += x
    return c


def short_cycle_greedy(net: Network) -> np.ndarray:
    """Bilateral netting followed by greedy offsetting of directed triangles in edge order."""
    c = bilateral_netting(net)
    res = net.amt - c
    out_edges: dict[int, dict[int, int]] = {}
    for e, (s, d) in enumerate(zip(net.src, net.dst)):
        out_edges.setdefault(int(s), {})[int(d)] = e
    for e1, (i, j) in enumerate(zip(net.src, net.dst)):
        if res[e1] <= 0:
            continue
        for k, e2 in out_edges.get(int(j), {}).items():
            if res[e1] <= 0:
                break
            e3 = out_edges.get(k, {}).get(int(i))
            if e3 is None or res[e2] <= 0 or res[e3] <= 0:
                continue
            x = min(res[e1], res[e2], res[e3])
            for e in (e1, e2, e3):
                res[e] -= x
                c[e] += x
    return c


def max_circulation(net: Network) -> np.ndarray:
    """Optimal MTCS: maximise sum(c) s.t. flow conservation at every firm and 0 <= c <= f."""
    if net.m == 0:
        return np.zeros(0)
    used = np.unique(np.concatenate([net.src, net.dst]))
    row = np.full(net.n, -1)
    row[used] = np.arange(len(used))
    e = np.arange(net.m)
    a_eq = sp.csr_matrix(
        (
            np.concatenate([np.ones(net.m), -np.ones(net.m)]),
            (np.concatenate([row[net.src], row[net.dst]]), np.concatenate([e, e])),
        ),
        shape=(len(used), net.m),
    )
    # Scale by the median, not the max: obligation sizes span ~8 orders of magnitude and
    # max-scaling pushes small bounds below HiGHS feasibility tolerances (spurious "infeasible").
    scale = float(np.median(net.amt))
    ub = net.amt / scale
    # HiGHS' default strategy is fastest here; dual simplex alone stalls on some 100k-edge
    # instances. Interior point is the fallback (it agrees to ~1e-12 relative on tests).
    for method in ("highs", "highs-ipm"):
        sol = linprog(
            -np.ones(net.m),
            A_eq=a_eq,
            b_eq=np.zeros(len(used)),
            bounds=np.column_stack([np.zeros(net.m), ub]),
            method=method,
            options={"time_limit": 600.0},
        )
        if sol.status == 0:
            break
    else:
        raise RuntimeError(f"max-circulation LP failed: {sol.message}")
    c = np.clip(sol.x, 0, ub) * scale
    return c


def residual_is_acyclic(net: Network, c: np.ndarray, rel_eps: float = 1e-9) -> bool:
    """After an optimal MTCS no directed cycle of strictly positive residual obligations remains."""
    res = net.amt - c
    keep = res > rel_eps * float(net.amt.max(initial=1.0))
    indeg = np.zeros(net.n, dtype=int)
    adj: dict[int, list[int]] = {}
    for s, d in zip(net.src[keep], net.dst[keep]):
        adj.setdefault(int(s), []).append(int(d))
        indeg[d] += 1
    stack = [v for v in range(net.n) if indeg[v] == 0]
    seen = 0
    while stack:
        v = stack.pop()
        seen += 1
        for w in adj.get(v, []):
            indeg[w] -= 1
            if indeg[w] == 0:
                stack.append(w)
    return seen == net.n


def sequenced_liquidity(net: Network, amt: np.ndarray) -> float:
    """Cash that must be injected to settle an acyclic obligation network when each firm pays
    only after receiving everything owed to it (topological order). Raises if a cycle remains."""
    keep = amt > 0
    src, dst, a = net.src[keep], net.dst[keep], amt[keep]
    indeg = np.zeros(net.n, dtype=int)
    np.add.at(indeg, dst, 1)
    out: dict[int, list[tuple[int, float]]] = {}
    for s, d, x in zip(src, dst, a):
        out.setdefault(int(s), []).append((int(d), float(x)))
    cash = np.zeros(net.n)
    injected = 0.0
    stack = [v for v in range(net.n) if indeg[v] == 0]
    seen = 0
    while stack:
        v = stack.pop()
        seen += 1
        due = sum(x for _, x in out.get(v, []))
        if due > cash[v]:
            injected += due - cash[v]
            cash[v] = due
        for w, x in out.get(v, []):
            cash[v] -= x
            cash[w] += x
            indeg[w] -= 1
            if indeg[w] == 0:
                stack.append(w)
    if seen != net.n:
        raise ValueError("obligation network still contains a cycle")
    return injected
