"""Explicit, itemised transaction cost model (§9).

No single blended number. Every component is computed and reported separately,
because a blended "0.5% round trip" hides which half of the trade the cost sits
on, and hides that the impact term — the one that actually binds in the
smallcap tier — scales with position size while the statutory terms do not.

The rate table is **data** (`rates.yaml`), effective-dated, not code. Rates
change; a stale table silently biases every backtest, and correcting one should
never mean editing a function.

Cost stack for cash-delivery equity:

    STT                buy + sell legs
    stamp duty         buy leg only (uniform regime from 2020-07)
    exchange txn       both legs
    SEBI turnover fee  both legs
    GST                on brokerage + exchange + SEBI + DP, never on STT/stamp
    DP charges         flat ₹ per scrip per sell day
    brokerage          zero on delivery at a discount broker, still modelled
    spread             half-spread per leg
    impact             Amihud λ × value (see costs/impact.py)

§18.6 is enforced structurally: `TradeCost.total` cannot be zero for a non-zero
trade, because the statutory components alone are strictly positive.
"""
from __future__ import annotations

import datetime as dt
import warnings
from dataclasses import asdict, dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any, Literal, Sequence

Side = Literal["buy", "sell"]

RATES_PATH = Path(__file__).with_name("rates.yaml")


class UnverifiedRates(UserWarning):
    """The rate table has not been checked against primary sources (§9)."""


@dataclass(frozen=True)
class RateTable:
    effective_from: str
    verified: bool
    verified_on: str | None
    note: str
    stt_delivery_buy: float
    stt_delivery_sell: float
    stamp_duty_buy: float
    exchange_txn: float
    sebi_turnover_fee: float
    gst_rate: float
    dp_charge_per_sell: float
    brokerage_pct: float
    brokerage_max_per_order: float
    gst_applies_to: tuple[str, ...] = ("brokerage", "exchange_txn", "sebi_fee", "dp_charges")


@dataclass(frozen=True)
class TradeCost:
    """Itemised cost of one leg. Every field is rupees."""

    side: Side
    turnover: float
    stt: float = 0.0
    stamp_duty: float = 0.0
    exchange_txn: float = 0.0
    sebi_fee: float = 0.0
    dp_charges: float = 0.0
    brokerage: float = 0.0
    gst: float = 0.0
    spread: float = 0.0
    impact: float = 0.0
    #: Slippage from carrying a trade forward off a circuit-locked session (§9).
    circuit_slippage: float = 0.0
    rate_table_effective_from: str = ""
    rates_verified: bool = False

    @property
    def statutory(self) -> float:
        return self.stt + self.stamp_duty + self.exchange_txn + self.sebi_fee + self.gst

    @property
    def explicit(self) -> float:
        """Everything billed on a contract note."""
        return self.statutory + self.dp_charges + self.brokerage

    @property
    def implicit(self) -> float:
        """Everything the market takes: spread, impact, forced delay."""
        return self.spread + self.impact + self.circuit_slippage

    @property
    def total(self) -> float:
        return self.explicit + self.implicit

    @property
    def bps(self) -> float:
        return 0.0 if self.turnover <= 0 else 1e4 * self.total / self.turnover

    def items(self) -> dict[str, float]:
        return {
            "stt": self.stt, "stamp_duty": self.stamp_duty,
            "exchange_txn": self.exchange_txn, "sebi_fee": self.sebi_fee,
            "gst": self.gst, "dp_charges": self.dp_charges,
            "brokerage": self.brokerage, "spread": self.spread,
            "impact": self.impact, "circuit_slippage": self.circuit_slippage,
        }

    def report(self) -> str:
        """Full itemisation, for the CP5 worked example and study reports."""
        lines = [
            f"{self.side.upper():4s}  turnover ₹{self.turnover:,.2f}",
            f"      rate table effective {self.rate_table_effective_from}"
            + ("" if self.rates_verified else "   [RATES UNVERIFIED]"),
            "      " + "-" * 52,
        ]
        for name, value in self.items().items():
            if value:
                lines.append(f"      {name:<20s} ₹{value:>14,.4f}")
        lines += [
            "      " + "-" * 52,
            f"      {'explicit':<20s} ₹{self.explicit:>14,.4f}",
            f"      {'implicit':<20s} ₹{self.implicit:>14,.4f}",
            f"      {'TOTAL':<20s} ₹{self.total:>14,.4f}  ({self.bps:.2f} bps)",
        ]
        return "\n".join(lines)


@dataclass(frozen=True)
class RoundTrip:
    buy: TradeCost
    sell: TradeCost

    @property
    def total(self) -> float:
        return self.buy.total + self.sell.total

    @property
    def bps(self) -> float:
        """Round-trip cost in bps of the *entry* notional — the number that
        matters for whether a signal survives, since that is the capital
        committed."""
        return 0.0 if self.buy.turnover <= 0 else 1e4 * self.total / self.buy.turnover

    def report(self) -> str:
        return (
            f"{self.buy.report()}\n\n{self.sell.report()}\n\n"
            + "=" * 60
            + f"\nROUND TRIP  ₹{self.total:,.4f}  = {self.bps:.2f} bps of entry notional\n"
            + "=" * 60
        )


@lru_cache(maxsize=4)
def load_rate_tables(path: str | None = None) -> tuple[RateTable, ...]:
    """Load effective-dated rate tables from YAML, oldest first."""
    import yaml

    raw = yaml.safe_load(Path(path or RATES_PATH).read_text(encoding="utf-8"))
    gst_applies = tuple(raw.get("gst_applies_to", ()))
    tables = [
        RateTable(
            effective_from=str(entry["effective_from"]),
            verified=bool(entry.get("verified", False)),
            verified_on=entry.get("verified_on"),
            note=str(entry.get("note", "")).strip(),
            gst_applies_to=gst_applies,
            **entry["rates"],
        )
        for entry in raw["tables"]
    ]
    return tuple(sorted(tables, key=lambda t: t.effective_from))


class CostModel:
    """Prices a trade against the rate table in force on its date."""

    def __init__(
        self,
        rates_path: str | None = None,
        *,
        warn_unverified: bool = True,
        default_spread_bps: float = 25.0,
    ) -> None:
        self.tables = load_rate_tables(rates_path)
        if not self.tables:
            raise ValueError("no rate tables loaded")
        self.warn_unverified = warn_unverified
        # Fallback half-spread when no estimate is available. 25bps full spread
        # is a reasonable smallcap default and is deliberately not free — a
        # missing estimate must not become a zero cost.
        self.default_spread_bps = default_spread_bps
        self._warned = False

    def table_for(self, date: str | dt.date) -> RateTable:
        iso = date if isinstance(date, str) else date.isoformat()
        chosen = self.tables[0]
        for table in self.tables:
            if table.effective_from <= iso:
                chosen = table
            else:
                break
        if self.warn_unverified and not chosen.verified and not self._warned:
            self._warned = True
            warnings.warn(
                f"Cost rate table effective {chosen.effective_from} is marked "
                "verified: false. Every backtest run against it inherits "
                "whatever error is in it. Verify the rates against the "
                "source_url entries in src/costs/rates.yaml and set "
                "verified: true before treating a net-of-cost result as real.",
                UnverifiedRates, stacklevel=2,
            )
        return chosen

    def leg(
        self,
        side: Side,
        *,
        price: float,
        quantity: float,
        date: str | dt.date,
        spread_bps: float | None = None,
        impact_bps: float | None = None,
        circuit_slippage: float = 0.0,
        dp_scrips: int = 1,
    ) -> TradeCost:
        """Cost of one leg. `quantity` is shares; `price` is the fill price."""
        if quantity < 0:
            raise ValueError("quantity must be non-negative; use `side` for direction")
        table = self.table_for(date)
        turnover = float(price) * float(quantity)
        if turnover <= 0:
            return TradeCost(side=side, turnover=0.0,
                             rate_table_effective_from=table.effective_from,
                             rates_verified=table.verified)

        stt = turnover * (table.stt_delivery_buy if side == "buy"
                          else table.stt_delivery_sell)
        stamp = turnover * table.stamp_duty_buy if side == "buy" else 0.0
        exchange = turnover * table.exchange_txn
        sebi = turnover * table.sebi_turnover_fee
        # DP charges are levied per scrip on the sell (debit) side only.
        dp = table.dp_charge_per_sell * dp_scrips if side == "sell" else 0.0
        brokerage = turnover * table.brokerage_pct
        if table.brokerage_max_per_order:
            brokerage = min(brokerage, table.brokerage_max_per_order)

        gstable = 0.0
        components = {"brokerage": brokerage, "exchange_txn": exchange,
                      "sebi_fee": sebi, "dp_charges": dp}
        for name in table.gst_applies_to:
            gstable += components.get(name, 0.0)
        gst = gstable * table.gst_rate

        half_spread_bps = (
            spread_bps if spread_bps is not None else self.default_spread_bps
        ) / 2.0
        spread = turnover * half_spread_bps / 1e4
        impact = turnover * (impact_bps or 0.0) / 1e4

        return TradeCost(
            side=side, turnover=turnover, stt=stt, stamp_duty=stamp,
            exchange_txn=exchange, sebi_fee=sebi, dp_charges=dp,
            brokerage=brokerage, gst=gst, spread=spread, impact=impact,
            circuit_slippage=circuit_slippage,
            rate_table_effective_from=table.effective_from,
            rates_verified=table.verified,
        )

    def round_trip(
        self,
        *,
        buy_price: float,
        sell_price: float,
        quantity: float,
        buy_date: str | dt.date,
        sell_date: str | dt.date,
        spread_bps: float | None = None,
        impact_bps: float | None = None,
    ) -> RoundTrip:
        return RoundTrip(
            buy=self.leg("buy", price=buy_price, quantity=quantity, date=buy_date,
                         spread_bps=spread_bps, impact_bps=impact_bps),
            sell=self.leg("sell", price=sell_price, quantity=quantity, date=sell_date,
                          spread_bps=spread_bps, impact_bps=impact_bps),
        )

    def net_return(
        self, gross_return: float, *, entry_notional: float,
        buy_date: str | dt.date, sell_date: str | dt.date,
        spread_bps: float | None = None, impact_bps: float | None = None,
    ) -> float:
        """Gross return converted to net. §9: net is the headline, always."""
        quantity = 1.0
        buy_price = entry_notional
        sell_price = entry_notional * (1.0 + gross_return)
        trip = self.round_trip(
            buy_price=buy_price, sell_price=sell_price, quantity=quantity,
            buy_date=buy_date, sell_date=sell_date,
            spread_bps=spread_bps, impact_bps=impact_bps,
        )
        return gross_return - trip.total / entry_notional


def rate_table_status(rates_path: str | None = None) -> dict[str, Any]:
    """Verification status of every rate table — surfaced in study reports."""
    tables = load_rate_tables(rates_path)
    return {
        "tables": [
            {"effective_from": t.effective_from, "verified": t.verified,
             "verified_on": t.verified_on, "note": t.note}
            for t in tables
        ],
        "all_verified": all(t.verified for t in tables),
        "unverified_count": sum(1 for t in tables if not t.verified),
    }
