"""SYNTH_V2 · fundamentals adapter (exposure Step 1) — vintage, no-lookahead.

Computes exposure metrics (`rm_to_sales`, `inventory_days`) over a fundamentals
feed instead of hand-curated YAML. Mirrors `fetch_wpi.py`'s vintage discipline
exactly: financials restate, so a screen registered against Q1 numbers must
grade against those numbers AS THEY STOOD at registration —
`fundamentals_asof(ticker, metric, registration_date)` has no lookahead.

Design rulings baked in (EXPOSURE_REDESIGN_AUDIT.md §7):
  * `rm_to_sales` production default is TRAILING-4Q (seasonality smoothing),
    chosen on principle — all three conventions (latest_q / ttm4q / annual) are
    computed and stored so reproduction can be REPORTED, never tuned to.
  * `inventory_days` uses the latest balance sheet (only 2-3 Q available) with a
    longer staleness tolerance; it inherits the balance-sheet period_end.
  * FAIL-CLOSED: a missing cost/revenue line, zero/negative denominator, a
    negative ratio or a range-guard breach yields NO value + an explicit reason.
    Never a default, never a silent carry-forward. Never a fabricated number.
  * PROVENANCE names the ACTUAL fields used (`CostOfRevenue/TotalRevenue`) so a
    packet reader sees the metric is an aggregate-COGS proxy, not materials-only.
  * The Yahoo `Cost Of Revenue` line is aggregate COGS; for paints it reads ~7pts
    above the published materials-based ratio (§7). quality is always `derived`.

The feed source is INJECTED (`YFinanceSource` in prod, a fixture source in CI),
so this module is testable with no network — the same discipline as the LLM
client in Call A/B.
"""
from __future__ import annotations

import json
from datetime import date, datetime
from pathlib import Path

FUND_DIR = Path(__file__).parent / "data" / "fundamentals"
VINTAGES_JSON = FUND_DIR / "vintages.json"

REV_ROW, COR_ROW, INV_ROW = "Total Revenue", "Cost Of Revenue", "Inventory"
CONVENTIONS = ("latest_q", "ttm4q", "annual")
DEFAULT_CONVENTION = "ttm4q"                 # trailing-4Q, on principle
RM_RANGE = (0.0, 1.0)                         # rm_to_sales unit guard
METRIC_STALE_DAYS = {"rm_to_sales": 100,     # P&L, ~1 quarter
                     "inventory_days": 210}   # balance sheet, ~2 quarters


# ── source protocol ──────────────────────────────────────────────────────
class YFinanceSource:
    """Prod source. `.statements(ticker)` -> the three frames, or empties on a
    ticker miss (which the caller turns into a fail-closed reason, never a
    silent empty)."""
    def statements(self, ticker: str) -> dict:
        import yfinance as yf
        t = yf.Ticker(ticker)

        def _safe(attr):
            try:
                df = getattr(t, attr)
                return df if (df is not None and not df.empty) else None
            except Exception:
                return None
        return {"income_q": _safe("quarterly_income_stmt"),
                "income_a": _safe("income_stmt"),
                "balance_q": _safe("quarterly_balance_sheet")}


# ── metric computation (pure; fail-closed) ──────────────────────────────
def _sum_over(df, cols, row) -> float | None:
    if df is None or row not in df.index:
        return None
    tot = 0.0
    seen = False
    for c in cols:
        v = df.loc[row, c]
        if v == v and v is not None:               # not NaN
            tot += float(v)
            seen = True
    return tot if seen else None


def _period_str(col) -> str:
    try:
        return col.date().isoformat()
    except Exception:
        return str(col)[:10]


def compute_rm_to_sales(stmts: dict, convention: str = DEFAULT_CONVENTION):
    """(record, None) or (None, reason). record carries value + provenance."""
    if convention == "annual":
        df = stmts.get("income_a")
        cols = list(df.columns[:1]) if df is not None and not df.empty else []
    else:
        df = stmts.get("income_q")
        if df is None or df.empty:
            return None, "no_quarterly_income"
        n = 4 if convention == "ttm4q" else 1
        if len(df.columns) < n:
            return None, f"insufficient_quarters_for_{convention}"
        cols = list(df.columns[:n])
    if df is None or not cols:
        return None, "no_income_statement"
    if COR_ROW not in df.index or REV_ROW not in df.index:
        return None, "missing_cost_or_revenue_line"
    rev = _sum_over(df, cols, REV_ROW)
    cor = _sum_over(df, cols, COR_ROW)
    if not rev or rev <= 0:
        return None, "zero_or_missing_revenue"
    if cor is None:
        return None, "missing_cost"
    v = cor / rev
    lo, hi = RM_RANGE
    if not (lo < v < hi):
        return None, f"out_of_range_{v:.3f}"
    return {"metric": "rm_to_sales", "value": round(v, 4),
            "period_end": _period_str(cols[0]), "convention": convention,
            "quality": "derived",
            "source": f"yfinance {COR_ROW}/{REV_ROW} [{convention}]",
            "fields": [COR_ROW, REV_ROW]}, None


def compute_inventory_days(stmts: dict):
    """Inventory (latest BS) / (annualised COGS / 365). Inherits the balance
    sheet's period_end and its longer staleness tolerance."""
    bq = stmts.get("balance_q")
    if bq is None or bq.empty or INV_ROW not in bq.index:
        return None, "no_inventory"
    inv = bq.loc[INV_ROW, bq.columns[0]]
    if not (inv == inv) or float(inv) <= 0:
        return None, "bad_inventory"
    iq = stmts.get("income_q")
    if iq is None or iq.empty or COR_ROW not in iq.index:
        return None, "no_cogs"
    if len(iq.columns) >= 4:
        cogs = _sum_over(iq, iq.columns[:4], COR_ROW)          # true ttm
        basis = "ttm_cogs"
    else:
        q = _sum_over(iq, iq.columns[:1], COR_ROW)
        cogs = q * 4 if q else None                            # annualised
        basis = "annualised_q_cogs"
    if not cogs or cogs <= 0:
        return None, "bad_cogs"
    days = float(inv) / (cogs / 365.0)
    return {"metric": "inventory_days", "value": round(days, 1),
            "period_end": _period_str(bq.columns[0]),         # BS cadence
            "convention": basis, "quality": "derived",
            "source": f"yfinance {INV_ROW} / ({COR_ROW}/365) [{basis}]",
            "fields": [INV_ROW, COR_ROW]}, None


# ── vintage store (never overwritten; no-lookahead) ─────────────────────
def load_vintages() -> dict:
    if VINTAGES_JSON.exists():
        try:
            return json.loads(VINTAGES_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"records": []}


def store_vintage(ticker: str, record: dict, fetched_at: str) -> bool:
    """Append one as-fetched record. Refuses a duplicate (ticker, metric,
    convention, period_end, fetched_at) — a restatement is a NEW fetched_at,
    stored alongside, never an overwrite."""
    FUND_DIR.mkdir(parents=True, exist_ok=True)
    v = load_vintages()
    key = (ticker, record["metric"], record["convention"],
           record["period_end"], fetched_at)
    for r in v["records"]:
        if (r["ticker"], r["metric"], r["convention"], r["period_end"],
                r["fetched_at"]) == key:
            return False
    v["records"].append({"ticker": ticker, "fetched_at": fetched_at, **record})
    VINTAGES_JSON.write_text(json.dumps(v, indent=2), encoding="utf-8")
    return True


def _d(x):
    try:
        return datetime.fromisoformat(str(x)[:10]).date()
    except Exception:
        return None


def fundamentals_asof(ticker: str, metric: str, registration_date: str,
                      convention: str = DEFAULT_CONVENTION,
                      vintages: dict | None = None) -> dict | None:
    """The value as it stood AT registration: among records fetched on/before
    registration_date, the latest period_end (ties broken by latest fetched_at).
    A restatement fetched later is invisible — no lookahead."""
    v = vintages or load_vintages()
    reg = _d(registration_date)
    if reg is None:
        return None
    elig = [r for r in v.get("records", [])
            if r["ticker"] == ticker and r["metric"] == metric
            and r["convention"] == convention
            and _d(r["fetched_at"]) is not None and _d(r["fetched_at"]) <= reg]
    if not elig:
        return None
    return max(elig, key=lambda r: (_d(r["period_end"]) or date.min,
                                    _d(r["fetched_at"]) or date.min))


def metric_stale(record: dict, asof: str) -> dict:
    """Per-field staleness: rm_to_sales ~1Q, inventory_days ~2Q (asymmetry is a
    ruling, grounded in the 2-3 balance-sheet quarters the audit measured)."""
    tol = METRIC_STALE_DAYS.get(record.get("metric"), 120)
    pe, a = _d(record.get("period_end")), _d(asof)
    if pe is None or a is None:
        return {"stale": True, "age_days": None}
    age = (a - pe).days
    return {"stale": age > tol, "age_days": age, "tolerance_days": tol}


# ── fetch = compute + store vintage + return record | fail-closed ───────
def fetch_metric(ticker: str, metric: str, source, fetched_at: str,
                 convention: str = DEFAULT_CONVENTION, persist: bool = True):
    """(record, None) or (None, reason). A ticker that resolves to empty
    statements is a fail-closed 'ticker_unresolved' — surfaced as a lookup
    failure, NEVER an empty frame that reads as delisted."""
    stmts = source.statements(ticker)
    if all(stmts.get(k) is None for k in ("income_q", "income_a", "balance_q")):
        return None, "ticker_unresolved"
    if metric == "rm_to_sales":
        rec, reason = compute_rm_to_sales(stmts, convention)
    elif metric == "inventory_days":
        rec, reason = compute_inventory_days(stmts)
    else:
        return None, f"unknown_metric_{metric}"
    if rec is None:
        return None, reason
    if persist:
        store_vintage(ticker, rec, fetched_at)
    return {"ticker": ticker, "fetched_at": fetched_at, **rec}, None


if __name__ == "__main__":
    import sys
    tk = sys.argv[1] if len(sys.argv) > 1 else "VOLTAS.NS"
    src = YFinanceSource()
    at = date.today().isoformat()
    for m in ("rm_to_sales", "inventory_days"):
        for conv in (CONVENTIONS if m == "rm_to_sales" else (DEFAULT_CONVENTION,)):
            rec, why = fetch_metric(tk, m, src, at, convention=conv, persist=False)
            print(f"{tk} {m:14} {conv:9} -> "
                  + (f"{rec['value']}  ({rec['source']}, as_of {rec['period_end']})"
                     if rec else f"FAIL-CLOSED: {why}"))
