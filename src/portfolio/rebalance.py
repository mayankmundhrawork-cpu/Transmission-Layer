"""Rebalance: diff current holdings against a target and price the orders (§13).

Produces an order list with an estimated cost per order and in aggregate. The
cost estimate uses the same `CostModel` the backtest uses, so a live rebalance
and a simulated one are priced by identical code — a cost model that differs
between backtest and execution is how a strategy that looked viable stops being
viable on contact.

Circuit-locked names are flagged rather than silently priced at the locked
price (§9): a stock at its upper circuit is not purchasable at that price, and
an order list that pretends otherwise is a fiction.
"""
from __future__ import annotations

import datetime as dt
from dataclasses import dataclass, field
from typing import Any, Sequence

import numpy as np
import pandas as pd

from src.costs.model import CostModel, TradeCost


@dataclass(frozen=True)
class Order:
    isin: str
    symbol: str | None
    side: str                # buy | sell
    quantity: int
    price: float
    notional: float
    estimated_cost: float
    cost_bps: float
    days_to_liquidate: float
    circuit_locked: bool
    participation_pct: float
    note: str = ""

    def as_dict(self) -> dict[str, Any]:
        return dict(vars(self))


@dataclass
class RebalancePlan:
    as_of_date: str
    orders: list[Order]
    current_value: float
    target_value: float
    unresolved: list[str] = field(default_factory=list)

    @property
    def total_cost(self) -> float:
        return float(sum(o.estimated_cost for o in self.orders))

    @property
    def total_notional(self) -> float:
        return float(sum(abs(o.notional) for o in self.orders))

    @property
    def turnover(self) -> float:
        return (self.total_notional / self.target_value / 2.0
                if self.target_value > 0 else 0.0)

    @property
    def blocked_orders(self) -> list[Order]:
        return [o for o in self.orders if o.circuit_locked]

    def summary(self) -> dict[str, Any]:
        return {
            "as_of_date": self.as_of_date,
            "n_orders": len(self.orders),
            "n_buys": sum(1 for o in self.orders if o.side == "buy"),
            "n_sells": sum(1 for o in self.orders if o.side == "sell"),
            "total_notional": self.total_notional,
            "total_cost": self.total_cost,
            "cost_bps": (1e4 * self.total_cost / self.total_notional
                         if self.total_notional > 0 else 0.0),
            "one_way_turnover": self.turnover,
            "blocked_by_circuit": len(self.blocked_orders),
        }

    def to_frame(self) -> pd.DataFrame:
        if not self.orders:
            return pd.DataFrame(columns=[f.name for f in Order.__dataclass_fields__.values()])
        return pd.DataFrame([o.as_dict() for o in self.orders])

    def confirmation_text(self) -> str:
        """The text a human must read before a live rebalance (§14)."""
        s = self.summary()
        lines = [
            f"REBALANCE {self.as_of_date}",
            f"  {s['n_orders']} orders ({s['n_buys']} buys, {s['n_sells']} sells)",
            f"  total notional  ₹{s['total_notional']:,.2f}",
            f"  estimated cost  ₹{s['total_cost']:,.2f} ({s['cost_bps']:.1f} bps)",
            f"  one-way turnover {s['one_way_turnover']:.1%}",
        ]
        if self.blocked_orders:
            lines.append(
                f"  WARNING: {len(self.blocked_orders)} names are circuit-locked "
                "and are not transactable at the quoted price"
            )
        if self.unresolved:
            lines.append(f"  WARNING: {len(self.unresolved)} names have no price")
        return "\n".join(lines)


def build_plan(
    *,
    target_weights: pd.Series,
    current_quantities: pd.Series,
    prices: pd.Series,
    portfolio_value: float,
    as_of_date: str | dt.date,
    median_turnover: pd.Series | None = None,
    spread_bps: pd.Series | None = None,
    impact_bps: pd.Series | None = None,
    circuit_locked: pd.Series | None = None,
    symbols: pd.Series | None = None,
    cost_model: CostModel | None = None,
    max_participation_pct: float = 5.0,
    lot_size: int = 1,
) -> RebalancePlan:
    """Diff current holdings against target weights and price the resulting orders."""
    date = as_of_date if isinstance(as_of_date, str) else as_of_date.isoformat()
    model = cost_model or CostModel()

    universe = target_weights.index.union(current_quantities.index)
    prices = prices.reindex(universe)
    unresolved = [i for i in universe if not np.isfinite(prices.get(i, np.nan))
                  or prices.get(i, 0) <= 0]
    tradeable = [i for i in universe if i not in unresolved]

    target_qty = pd.Series(0.0, index=tradeable)
    for isin in tradeable:
        weight = float(target_weights.get(isin, 0.0))
        target_qty[isin] = np.floor(
            weight * portfolio_value / prices[isin] / lot_size) * lot_size

    current = current_quantities.reindex(tradeable).fillna(0.0)
    delta = target_qty - current

    orders: list[Order] = []
    for isin in tradeable:
        quantity = int(delta[isin])
        if quantity == 0:
            continue
        side = "buy" if quantity > 0 else "sell"
        price = float(prices[isin])
        notional = abs(quantity) * price

        adv = float(median_turnover.get(isin, 0.0)) if median_turnover is not None else 0.0
        capacity = adv * max_participation_pct / 100.0
        participation = (notional / adv * 100.0) if adv > 0 else float("inf")
        dtl = (notional / capacity) if capacity > 0 else float("inf")

        locked = bool(circuit_locked.get(isin, False)) if circuit_locked is not None else False

        cost: TradeCost = model.leg(
            side, price=price, quantity=abs(quantity), date=date,
            spread_bps=float(spread_bps.get(isin)) if spread_bps is not None
            and np.isfinite(spread_bps.get(isin, np.nan)) else None,
            impact_bps=float(impact_bps.get(isin)) if impact_bps is not None
            and np.isfinite(impact_bps.get(isin, np.nan)) else None,
        )

        notes = []
        if locked:
            notes.append("circuit-locked: not transactable at this price")
        if participation > max_participation_pct:
            notes.append(
                f"exceeds participation cap ({participation:.1f}% of ADV vs "
                f"{max_participation_pct:.1f}% limit)")

        orders.append(Order(
            isin=isin,
            symbol=str(symbols.get(isin)) if symbols is not None else None,
            side=side, quantity=abs(quantity), price=price, notional=notional,
            estimated_cost=cost.total, cost_bps=cost.bps,
            days_to_liquidate=dtl, circuit_locked=locked,
            participation_pct=participation, note="; ".join(notes),
        ))

    # Sells first: a rebalance that buys before it sells needs cash it may not
    # have, and in a T+1 settlement regime that is a real constraint, not an
    # ordering preference.
    orders.sort(key=lambda o: (o.side != "sell", -o.notional))

    return RebalancePlan(
        as_of_date=date, orders=orders,
        current_value=float((current * prices.reindex(current.index)).sum()),
        target_value=float(portfolio_value), unresolved=unresolved,
    )
