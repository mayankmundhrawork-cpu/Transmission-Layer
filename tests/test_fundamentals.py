"""SYNTH_V2 · fundamentals adapter tests (exposure Step 1).

Source is INJECTED (fixture frames), so this runs with no network — the same
discipline as the Call A/B client. Guards: the three conventions, fail-closed on
every partial-data path, vintage no-overwrite, no-lookahead, per-field staleness.

Run: pytest -q tests/test_fundamentals.py
"""
import pandas as pd
import pytest


def _income(quarters):
    """quarters: list of (period_end, revenue, cogs), newest first."""
    cols = [pd.Timestamp(p) for p, _, _ in quarters]
    data = {c: [q[1], q[2]] for c, q in zip(cols, quarters)}
    return pd.DataFrame(data, index=["Total Revenue", "Cost Of Revenue"])


def _balance(period_end, inventory):
    return pd.DataFrame({pd.Timestamp(period_end): [inventory]},
                        index=["Inventory"])


class FixtureSource:
    def __init__(self, by_ticker):
        self._b = by_ticker

    def statements(self, ticker):
        return self._b.get(ticker, {"income_q": None, "income_a": None,
                                     "balance_q": None})


def test_rm_to_sales_three_conventions():
    from fetch_fundamentals import compute_rm_to_sales
    # 4 quarters: latest cor/rev = 60/100 = 0.6; ttm = 240/400 = 0.6
    q = _income([("2026-06-30", 100, 60), ("2026-03-31", 100, 55),
                 ("2025-12-31", 100, 50), ("2025-09-30", 100, 75)])
    a = _income([("2026-03-31", 400, 250)])   # annual 0.625
    stmts = {"income_q": q, "income_a": a, "balance_q": None}
    assert compute_rm_to_sales(stmts, "latest_q")[0]["value"] == 0.6
    assert compute_rm_to_sales(stmts, "ttm4q")[0]["value"] == 0.6
    assert compute_rm_to_sales(stmts, "annual")[0]["value"] == 0.625
    # provenance names the actual fields (aggregate, not materials)
    assert "Cost Of Revenue" in compute_rm_to_sales(stmts, "ttm4q")[0]["source"]


def test_rm_to_sales_fail_closed_paths():
    from fetch_fundamentals import compute_rm_to_sales
    # missing cost line
    df = pd.DataFrame({pd.Timestamp("2026-06-30"): [100]},
                      index=["Total Revenue"])
    assert compute_rm_to_sales({"income_q": df}, "latest_q") == \
        (None, "missing_cost_or_revenue_line")
    # zero revenue
    z = _income([("2026-06-30", 0, 60)])
    assert compute_rm_to_sales({"income_q": z}, "latest_q")[1] == \
        "zero_or_missing_revenue"
    # out of range (a percentage slip: cor > rev)
    hi = _income([("2026-06-30", 100, 803)])
    assert "out_of_range" in compute_rm_to_sales({"income_q": hi}, "latest_q")[1]
    # not enough quarters for ttm
    one = _income([("2026-06-30", 100, 60)])
    assert compute_rm_to_sales({"income_q": one}, "ttm4q")[1] == \
        "insufficient_quarters_for_ttm4q"


def test_inventory_days_and_inherits_bs_period():
    from fetch_fundamentals import compute_inventory_days
    q = _income([("2026-06-30", 100, 50), ("2026-03-31", 100, 50),
                 ("2025-12-31", 100, 50), ("2025-09-30", 100, 50)])  # ttm cogs 200
    b = _balance("2026-03-31", 50)   # inv 50 ; days = 50/(200/365) = 91.25
    rec, reason = compute_inventory_days({"income_q": q, "balance_q": b})
    assert reason is None and abs(rec["value"] - 91.2) < 0.3
    assert rec["period_end"] == "2026-03-31"          # BS cadence, not income
    # no inventory -> fail closed
    assert compute_inventory_days({"income_q": q, "balance_q": None})[1] == \
        "no_inventory"


def test_ticker_unresolved_is_fail_closed_not_empty():
    from fetch_fundamentals import fetch_metric
    src = FixtureSource({})            # every ticker returns empty frames
    rec, reason = fetch_metric("CEAT.NS", "rm_to_sales", src, "2026-07-26")
    assert rec is None and reason == "ticker_unresolved"


def test_vintage_never_overwritten_and_no_lookahead(tmp_path, monkeypatch):
    import fetch_fundamentals as ff
    monkeypatch.setattr(ff, "VINTAGES_JSON", tmp_path / "v.json")
    monkeypatch.setattr(ff, "FUND_DIR", tmp_path)
    q1 = _income([("2026-06-30", 100, 60)])
    src1 = FixtureSource({"X": {"income_q": q1, "income_a": None, "balance_q": None}})
    r, _ = ff.fetch_metric("X", "rm_to_sales", src1, "2026-07-14",
                           convention="latest_q")
    assert r["value"] == 0.6
    # a RESTATEMENT of the same period, fetched later, is stored ALONGSIDE
    q2 = _income([("2026-06-30", 100, 65)])
    src2 = FixtureSource({"X": {"income_q": q2, "income_a": None, "balance_q": None}})
    ff.fetch_metric("X", "rm_to_sales", src2, "2026-08-14", convention="latest_q")
    # a screen registered 2026-07-20 sees the ORIGINAL 0.6, not the 0.65 restate
    asof = ff.fundamentals_asof("X", "rm_to_sales", "2026-07-20", "latest_q")
    assert asof["value"] == 0.6 and asof["fetched_at"] == "2026-07-14"
    # after the restatement, it is visible
    assert ff.fundamentals_asof("X", "rm_to_sales", "2026-08-20",
                                "latest_q")["value"] == 0.65


def test_per_field_staleness_asymmetry():
    from fetch_fundamentals import METRIC_STALE_DAYS, metric_stale
    assert METRIC_STALE_DAYS["inventory_days"] > METRIC_STALE_DAYS["rm_to_sales"]
    # inventory 150 days old is within its ~2Q tolerance; rm_to_sales is not
    inv = metric_stale({"metric": "inventory_days", "period_end": "2026-02-01"},
                       "2026-07-01")
    rm = metric_stale({"metric": "rm_to_sales", "period_end": "2026-02-01"},
                      "2026-07-01")
    assert inv["stale"] is False and rm["stale"] is True
