"""Exploratory default-shock analysis for Experiment 001 (Eisenberg–Noe 2001 clearing).

Question: when a firm becomes insolvent shortly after a clearing round, who bears the loss?
Set-off before insolvency pays the defaulter's cleared creditors in full out of receivables
that would otherwise have been shared pro rata among all its creditors — the outcome the House
of Lords refused to let a contractual clearing scheme impose after liquidation in British Eagle
v Air France [1975]. This module measures that transfer.

Model: each firm owes trade creditors (the network) and outside creditors (banks, HMRC, staff),
outside liabilities = outside_ratio x trade payables. External assets give every firm a solvency
buffer before the shock. A shock wipes out the external assets of a set of firms. Payments
follow the Eisenberg–Noe greatest clearing vector with pro-rata priority and no default costs.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .clearing import Network


@dataclass(frozen=True)
class LossSplit:
    participant_firms: float  # losses on trade receivables held by clearing participants
    other_firms: float  # losses on trade receivables held by non-participants
    outside_creditors: float
    defaults: int

    @property
    def total(self) -> float:
        return self.participant_firms + self.other_firms + self.outside_creditors


def eisenberg_noe(net: Network, amt: np.ndarray, outside: np.ndarray, assets: np.ndarray,
                  tol: float = 1e-10, max_iter: int = 10_000) -> np.ndarray:
    """Greatest clearing payment vector p (total paid by each firm)."""
    liab = outside.copy()
    np.add.at(liab, net.src, amt)
    share = np.divide(amt, liab[net.src], out=np.zeros_like(amt), where=liab[net.src] > 0)
    p = liab.copy()
    for _ in range(max_iter):
        inflow = np.zeros(net.n)
        np.add.at(inflow, net.dst, share * p[net.src])
        p_new = np.minimum(liab, assets + inflow)
        if np.max(np.abs(p_new - p), initial=0.0) <= tol * max(1.0, float(liab.max(initial=0.0))):
            return p_new
        p = p_new
    raise RuntimeError("Eisenberg–Noe iteration did not converge")


def loss_split(net: Network, amt: np.ndarray, outside: np.ndarray, assets: np.ndarray,
               participant: np.ndarray) -> LossSplit:
    p = eisenberg_noe(net, amt, outside, assets)
    liab = outside.copy()
    np.add.at(liab, net.src, amt)
    ratio = np.divide(p, liab, out=np.ones_like(p), where=liab > 0)
    edge_loss = amt * (1.0 - ratio[net.src])
    held_by_participant = participant[net.dst]
    return LossSplit(
        participant_firms=float(edge_loss[held_by_participant].sum()),
        other_firms=float(edge_loss[~held_by_participant].sum()),
        outside_creditors=float((outside * (1.0 - ratio)).sum()),
        defaults=int(np.sum(ratio < 1.0 - 1e-9)),
    )


def shock_scenario(net: Network, size: np.ndarray, rng: np.random.Generator,
                   shock_share: float = 0.05, outside_ratio: float = 1.0,
                   buffer_max: float = 0.3) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Outside liabilities, post-shock external assets, and the shocked set.

    Pre-shock, every firm can meet all liabilities from external assets plus receivables, with a
    buffer drawn U(0, buffer_max) of liabilities. The shock removes all external assets of
    shock_share of firms, sampled with weights 1/sqrt(size) (small firms are more fragile)."""
    payables = np.zeros(net.n)
    np.add.at(payables, net.src, net.amt)
    receivables = np.zeros(net.n)
    np.add.at(receivables, net.dst, net.amt)
    outside = outside_ratio * payables
    liab = payables + outside
    assets = np.clip(liab - receivables, 0, None) + rng.uniform(0, buffer_max, net.n) * liab
    w = 1.0 / np.sqrt(size)
    shocked = rng.choice(net.n, size=max(1, int(round(shock_share * net.n))), replace=False, p=w / w.sum())
    assets = assets.copy()
    assets[shocked] = 0.0
    return outside, assets, shocked
