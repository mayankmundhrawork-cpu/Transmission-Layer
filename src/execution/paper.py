"""Paper execution adapter (§14) — the default.

Writes to a ledger with full cost attribution. Every fill records the itemised
cost that produced it, so a paper track record can be reconciled against a
backtest line by line rather than compared as two aggregate numbers.

Two modelling choices worth stating:

* **Circuit-locked orders are deferred, not filled.** §9 requires that a stock
  at its circuit is not transactable at that price. The order is recorded with
  status `deferred` rather than dropped, so the intent is preserved and the
  slippage from carrying it forward is measurable.
* **Fills happen at the quoted price plus the modelled cost**, never at mid.
  §18.6 forbids mid fills, and the adapter has no code path that produces one.
"""
from __future__ import annotations

import datetime as dt
import json
import sqlite3
from pathlib import Path
from typing import Any

from src.costs.model import CostModel
from src.execution.adapter import ExecutionAdapter, ExecutionResult, Fill
from src.portfolio.rebalance import RebalancePlan

LEDGER_SCHEMA = """
CREATE TABLE IF NOT EXISTS paper_fill (
    fill_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_date   TEXT NOT NULL,
    isin        TEXT NOT NULL,
    symbol      TEXT,
    side        TEXT NOT NULL,
    quantity    INTEGER NOT NULL,
    price       REAL NOT NULL,
    notional    REAL NOT NULL,
    cost_total  REAL NOT NULL,
    cost_items  TEXT NOT NULL,
    status      TEXT NOT NULL,
    note        TEXT,
    executed_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS ix_fill_date ON paper_fill(plan_date);

CREATE TABLE IF NOT EXISTS paper_position (
    isin     TEXT PRIMARY KEY,
    quantity INTEGER NOT NULL
);
"""


class PaperAdapter(ExecutionAdapter):
    """Simulated execution with a persistent ledger."""

    name = "paper"
    is_live = False

    def __init__(self, ledger_path: Path | str, cost_model: CostModel | None = None) -> None:
        self.ledger_path = Path(ledger_path)
        self.ledger_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.ledger_path, isolation_level=None)
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(LEDGER_SCHEMA)
        self.cost_model = cost_model or CostModel()

    def close(self) -> None:
        self.conn.close()

    def __enter__(self) -> "PaperAdapter":
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    # -- execution ---------------------------------------------------------

    def execute(self, plan: RebalancePlan, **kwargs: Any) -> ExecutionResult:
        result = ExecutionResult(adapter=self.name, plan_date=plan.as_of_date)
        executed_at = dt.datetime.now(tz=dt.timezone.utc).isoformat()

        for order in plan.orders:
            if order.circuit_locked:
                # Deferred, not dropped: the intent is preserved so the carry
                # slippage is measurable (§9).
                fill = Fill(
                    isin=order.isin, symbol=order.symbol, side=order.side,
                    quantity=0, price=order.price, notional=0.0,
                    cost_total=0.0, cost_items={}, executed_at=executed_at,
                    status="deferred",
                    note="circuit-locked on the rebalance date; carried forward",
                )
                self._write(plan.as_of_date, fill)
                result.rejected.append((order, fill.note))
                continue

            cost = self.cost_model.leg(
                order.side, price=order.price, quantity=order.quantity,
                date=plan.as_of_date,
            )
            fill = Fill(
                isin=order.isin, symbol=order.symbol, side=order.side,
                quantity=order.quantity, price=order.price,
                notional=order.notional, cost_total=cost.total,
                cost_items=cost.items(), executed_at=executed_at,
                status="filled", note=order.note,
            )
            self._write(plan.as_of_date, fill)
            self._apply_position(order.isin, order.quantity if order.side == "buy"
                                 else -order.quantity)
            result.fills.append(fill)

        return result

    def _write(self, plan_date: str, fill: Fill) -> None:
        self.conn.execute(
            "INSERT INTO paper_fill (plan_date, isin, symbol, side, quantity,"
            " price, notional, cost_total, cost_items, status, note, executed_at)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
            (plan_date, fill.isin, fill.symbol, fill.side, fill.quantity,
             fill.price, fill.notional, fill.cost_total,
             json.dumps(fill.cost_items), fill.status, fill.note, fill.executed_at),
        )

    def _apply_position(self, isin: str, delta: int) -> None:
        self.conn.execute(
            "INSERT INTO paper_position (isin, quantity) VALUES (?,?)"
            " ON CONFLICT(isin) DO UPDATE SET quantity = quantity + excluded.quantity",
            (isin, delta),
        )
        self.conn.execute("DELETE FROM paper_position WHERE quantity = 0")

    # -- state -------------------------------------------------------------

    def positions(self) -> dict[str, int]:
        return {r["isin"]: r["quantity"]
                for r in self.conn.execute("SELECT isin, quantity FROM paper_position")}

    def fills(self, plan_date: str | None = None) -> list[dict[str, Any]]:
        sql = "SELECT * FROM paper_fill"
        args: list[Any] = []
        if plan_date:
            sql += " WHERE plan_date = ?"
            args.append(plan_date)
        sql += " ORDER BY fill_id"
        return [dict(r) for r in self.conn.execute(sql, args)]

    def cost_attribution(self) -> dict[str, float]:
        """Total cost by component across the whole ledger."""
        totals: dict[str, float] = {}
        for row in self.conn.execute("SELECT cost_items FROM paper_fill"):
            for name, value in json.loads(row["cost_items"]).items():
                totals[name] = totals.get(name, 0.0) + float(value)
        return totals
