"""Daily prices, returns, and point-in-time corporate-action adjustment (§5).

Bhavcopy prices are raw and unadjusted. The usual convenience — back-adjusting
the whole history whenever a split happens — is quietly a look-ahead
construction: it rewrites what a price "was" on a past date using an event that
had not happened yet, and any factor reading a price level (not just a return)
then sees a number nobody could have observed.

So this module never rewrites history. It applies an adjustment **only on the
ex-date**, inside the return calculation:

    r_t = (close_t * shares_ratio_t + dividend_t) / close_{t-1} - 1

where `shares_ratio_t` and `dividend_t` come from actions whose ex-date *is* t.
The price series stays raw, the return series is correct, and a price level
read on any date is the number that was actually printed.

Circuit detection is a heuristic and is labelled as one. NSE does not publish
per-scrip price bands in the bhavcopy, so a lock is inferred from a zero
intraday range at a band-sized move. It has false negatives (a stock that
opens at its band and stays there with one tick of range) and the estimate is
reported alongside the trade, never silently swallowed.
"""
from __future__ import annotations

import datetime as dt
import sqlite3
from dataclasses import dataclass
from typing import Iterable, Sequence

import numpy as np
import pandas as pd

#: Standard NSE price bands. A move landing on one of these with no intraday
#: range is the circuit-lock signature.
CIRCUIT_BANDS = (0.02, 0.05, 0.10, 0.20)
#: How close to a band a move must land to count as a lock.
BAND_TOLERANCE = 0.004


def price_panel(
    conn: sqlite3.Connection,
    isins: Sequence[str] | None = None,
    start: str | dt.date | None = None,
    end: str | dt.date | None = None,
    columns: Sequence[str] = ("close",),
) -> pd.DataFrame:
    """Wide panel of raw daily prices: index=date, columns=isin.

    With more than one column requested, returns a column MultiIndex of
    (field, isin).
    """
    sql = "SELECT isin, date, " + ", ".join(columns) + " FROM price_daily WHERE 1=1"
    args: list[object] = []
    if isins is not None:
        if not len(isins):
            return pd.DataFrame()
        sql += f" AND isin IN ({','.join('?' * len(isins))})"
        args.extend(isins)
    if start is not None:
        sql += " AND date >= ?"
        args.append(_iso(start))
    if end is not None:
        sql += " AND date <= ?"
        args.append(_iso(end))

    frame = pd.read_sql_query(sql, conn, params=args, parse_dates=["date"])
    if frame.empty:
        return pd.DataFrame()
    if len(columns) == 1:
        return frame.pivot(index="date", columns="isin", values=columns[0]).sort_index()
    panel = frame.pivot(index="date", columns="isin", values=list(columns)).sort_index()
    return panel


def corporate_action_factors(
    conn: sqlite3.Connection,
    isins: Sequence[str] | None = None,
    start: str | dt.date | None = None,
    end: str | dt.date | None = None,
) -> pd.DataFrame:
    """Per (isin, ex_date) share ratio and cash dividend.

    `share_ratio` is shares held *after* per share held *before* — 5.0 for a
    1:5 split, 2.0 for a 1:1 bonus. Actions whose ratio could not be parsed
    contribute nothing rather than a guess (see `classify_action`): a wrong
    ratio multiplies a return by an integer and looks like alpha.
    """
    sql = ("SELECT isin, ex_date, action_type, ratio_to, amount FROM corporate_action"
           " WHERE action_type IN ('split','bonus','dividend')")
    args: list[object] = []
    if isins is not None:
        if not len(isins):
            return pd.DataFrame(columns=["isin", "ex_date", "share_ratio", "dividend"])
        sql += f" AND isin IN ({','.join('?' * len(isins))})"
        args.extend(isins)
    if start is not None:
        sql += " AND ex_date >= ?"
        args.append(_iso(start))
    if end is not None:
        sql += " AND ex_date <= ?"
        args.append(_iso(end))

    raw = pd.read_sql_query(sql, conn, params=args)
    if raw.empty:
        return pd.DataFrame(columns=["isin", "ex_date", "share_ratio", "dividend"])

    raw["share_ratio"] = np.where(
        raw["action_type"].isin(["split", "bonus"]) & raw["ratio_to"].notna(),
        raw["ratio_to"], 1.0,
    )
    raw["dividend"] = np.where(
        raw["action_type"] == "dividend", raw["amount"].fillna(0.0), 0.0
    )
    return (
        raw.groupby(["isin", "ex_date"], as_index=False)
        .agg(share_ratio=("share_ratio", "prod"), dividend=("dividend", "sum"))
    )


def daily_returns(
    conn: sqlite3.Connection,
    isins: Sequence[str] | None = None,
    start: str | dt.date | None = None,
    end: str | dt.date | None = None,
    *,
    include_dividends: bool = True,
) -> pd.DataFrame:
    """Total-return series per ISIN, adjusted on ex-dates only.

    The adjustment is applied *at* the event, never backwards over history —
    see the module docstring for why that distinction is not cosmetic.
    """
    closes = price_panel(conn, isins, start, end, ("close",))
    if closes.empty:
        return pd.DataFrame()

    actions = corporate_action_factors(conn, isins, start, end)
    ratio = pd.DataFrame(1.0, index=closes.index, columns=closes.columns)
    cash = pd.DataFrame(0.0, index=closes.index, columns=closes.columns)
    for row in actions.itertuples(index=False):
        stamp = pd.Timestamp(row.ex_date)
        if stamp in ratio.index and row.isin in ratio.columns:
            ratio.loc[stamp, row.isin] *= float(row.share_ratio or 1.0)
            if include_dividends:
                cash.loc[stamp, row.isin] += float(row.dividend or 0.0)

    numerator = closes * ratio + cash
    returns = numerator / closes.shift(1) - 1.0
    # A gap in a name's trading (suspension, then resumption) is not a return;
    # forward-filling across it would manufacture a spike on the resume date.
    returns = returns.where(closes.notna() & closes.shift(1).notna())
    return returns


def cumulative_return(returns: pd.Series | pd.DataFrame) -> pd.Series | pd.DataFrame:
    return (1.0 + returns.fillna(0.0)).cumprod() - 1.0


def trailing_return(
    returns: pd.DataFrame, as_of: str | dt.date, lookback: int, skip: int = 0
) -> pd.Series:
    """Compound return over `lookback` sessions ending `skip` sessions before
    `as_of`. `skip=1, lookback=252` is 12-1 momentum (§8)."""
    window = returns.loc[: pd.Timestamp(_iso(as_of))]
    if skip:
        window = window.iloc[:-skip] if len(window) > skip else window.iloc[:0]
    window = window.tail(lookback)
    if window.empty:
        return pd.Series(dtype="float64")
    # Require most of the window present: a name with 8 observations out of 252
    # produces a "12-month return" that is nothing of the sort.
    enough = window.notna().sum() >= max(int(lookback * 0.6), 1)
    compounded = (1.0 + window.fillna(0.0)).prod() - 1.0
    return compounded.where(enough)


def realised_volatility(returns: pd.DataFrame, as_of: str | dt.date,
                        lookback: int = 252, annualise: bool = True) -> pd.Series:
    window = returns.loc[: pd.Timestamp(_iso(as_of))].tail(lookback)
    if window.empty:
        return pd.Series(dtype="float64")
    vol = window.std()
    vol = vol.where(window.notna().sum() >= max(int(lookback * 0.5), 20))
    return vol * np.sqrt(252.0) if annualise else vol


def circuit_locked(
    conn: sqlite3.Connection, isin: str, date: str | dt.date,
    bands: Iterable[float] = CIRCUIT_BANDS,
) -> bool:
    """Heuristic: was this scrip locked at a circuit on this date?

    A locked scrip has no intraday range and a move sitting on a band. §9
    requires that such a stock is not treated as transactable at that price.

    Known limitation: NSE does not publish per-scrip bands in the bhavcopy, so
    this infers them. It under-detects (a lock with one tick of range) rather
    than over-detects, which is the safer direction — a missed lock costs a
    modelled slippage, a false lock silently drops a real trade.
    """
    row = conn.execute(
        "SELECT high, low, close, prev_close FROM price_daily WHERE isin=? AND date=?",
        (isin, _iso(date)),
    ).fetchone()
    if row is None or not row["prev_close"]:
        return False
    if row["high"] is None or row["low"] is None:
        return False
    if row["high"] != row["low"]:
        return False
    move = abs(row["close"] / row["prev_close"] - 1.0)
    return any(abs(move - band) <= BAND_TOLERANCE for band in bands)


def next_transactable_session(
    conn: sqlite3.Connection, isin: str, date: str | dt.date, *, max_forward: int = 10
) -> str | None:
    """First session at or after `date` on which this scrip was not locked.

    §9: a trade intended on a circuit-locked date is carried forward and the
    slippage recorded. None means it never became transactable inside the
    window, which is a real outcome — the position simply cannot be entered.
    """
    rows = conn.execute(
        "SELECT date FROM price_daily WHERE isin=? AND date>=? ORDER BY date LIMIT ?",
        (isin, _iso(date), max_forward),
    ).fetchall()
    for row in rows:
        if not circuit_locked(conn, isin, row["date"]):
            return row["date"]
    return None


def benchmark_returns(conn: sqlite3.Connection, index_name: str,
                      start: str | dt.date | None = None,
                      end: str | dt.date | None = None) -> pd.Series:
    """Total-return series for the benchmark (§11: the control, not raw return)."""
    sql = ("SELECT date, COALESCE(total_return_close, close) AS level"
           " FROM benchmark_daily WHERE index_name=?")
    args: list[object] = [index_name]
    if start is not None:
        sql += " AND date>=?"
        args.append(_iso(start))
    if end is not None:
        sql += " AND date<=?"
        args.append(_iso(end))
    sql += " ORDER BY date"
    frame = pd.read_sql_query(sql, conn, params=args, parse_dates=["date"])
    if frame.empty:
        return pd.Series(dtype="float64", name=index_name)
    series = frame.set_index("date")["level"]
    return series.pct_change().rename(index_name)


def _iso(value: str | dt.date | pd.Timestamp) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, pd.Timestamp):
        return value.date().isoformat()
    return value.isoformat()
