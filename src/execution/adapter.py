"""Execution adapter interface (§14).

Two implementations: :class:`~src.execution.paper.PaperAdapter` (the default)
and :class:`~src.execution.dhan_live.DhanLiveAdapter` (gated three ways).

The interface is deliberately narrow. An adapter places orders and reports
fills; it does not decide what to trade, does not size positions, and cannot
initiate a rebalance. Everything upstream of `execute` is research code, and
keeping the boundary this sharp is what stops "just one more convenience
method" from turning the execution layer into a place where trading decisions
get made.
"""
from __future__ import annotations

import datetime as dt
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Sequence

from src.portfolio.rebalance import Order, RebalancePlan


@dataclass(frozen=True)
class Fill:
    """One executed order, with its cost fully attributed."""

    isin: str
    symbol: str | None
    side: str
    quantity: int
    price: float
    notional: float
    cost_total: float
    cost_items: dict[str, float]
    executed_at: str
    order_id: str = ""
    status: str = "filled"          # filled | partial | rejected | deferred
    note: str = ""

    def as_dict(self) -> dict[str, Any]:
        return dict(vars(self))


@dataclass
class ExecutionResult:
    adapter: str
    plan_date: str
    fills: list[Fill] = field(default_factory=list)
    rejected: list[tuple[Order, str]] = field(default_factory=list)

    @property
    def total_cost(self) -> float:
        return float(sum(f.cost_total for f in self.fills))

    @property
    def total_notional(self) -> float:
        return float(sum(abs(f.notional) for f in self.fills))

    def summary(self) -> dict[str, Any]:
        return {
            "adapter": self.adapter,
            "plan_date": self.plan_date,
            "filled": len(self.fills),
            "rejected": len(self.rejected),
            "total_notional": self.total_notional,
            "total_cost": self.total_cost,
            "cost_bps": (1e4 * self.total_cost / self.total_notional
                         if self.total_notional > 0 else 0.0),
        }


class ExecutionAdapter(ABC):
    """Places orders. Does not decide what to place."""

    name: str = ""
    #: True only for adapters that move real money.
    is_live: bool = False

    @abstractmethod
    def execute(self, plan: RebalancePlan, **kwargs: Any) -> ExecutionResult:
        """Execute a rebalance plan and return the fills."""

    @abstractmethod
    def positions(self) -> dict[str, int]:
        """Current holdings, ISIN -> quantity."""

    def preflight(self, plan: RebalancePlan) -> list[str]:
        """Checks run before execution. Non-empty means do not proceed."""
        problems = []
        if plan.unresolved:
            problems.append(f"{len(plan.unresolved)} names have no usable price")
        return problems
