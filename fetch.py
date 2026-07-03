"""Continuous-tier fetch — pulls every Step 3 series and writes a wide CSV.

Output: data/prices.csv (rows = date, cols = series id)
        data/fetch_log.json (per-series status: OK / EMPTY / ERROR + row count + last date)

Run: python fetch.py
"""
from __future__ import annotations

import json
import sys
import time
from datetime import date, datetime, timedelta
from pathlib import Path

import pandas as pd
import requests

from config import FRED_API_KEY, SERIES

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)
PRICES_CSV = DATA_DIR / "prices.csv"
FETCH_LOG = DATA_DIR / "fetch_log.json"

# ~2 years of history — enough for 20-day z, 60-day z, and 252-day percentile.
HISTORY_DAYS = 730

# Spike-filter threshold. A point is an isolated bad tick only if it deviates
# >SPIKE_PCT from BOTH neighbours in the same direction (up-then-down or
# down-then-up). A sustained move survives because the next close does not revert.
SPIKE_PCT = 0.15


def despike(s: pd.Series) -> tuple[pd.Series, list[dict]]:
    """Replace isolated spike-and-revert points with the neighbour mean.

    Returns (cleaned_series, corrections). Only interior points are checked
    (first/last have no full neighbour pair). A large but sustained move never
    matches — one neighbour will be close to the moved value.
    """
    if len(s) < 3:
        return s, []
    v = s.values.astype(float)
    corrections: list[dict] = []
    cleaned = v.copy()
    # Iterate on original values so a spike does not mask an adjacent spike.
    for i in range(1, len(v) - 1):
        prev_v, cur, next_v = v[i - 1], v[i], v[i + 1]
        if prev_v == 0 or next_v == 0:
            continue
        dev_prev = (cur - prev_v) / abs(prev_v)
        dev_next = (cur - next_v) / abs(next_v)
        if abs(dev_prev) > SPIKE_PCT and abs(dev_next) > SPIKE_PCT and (dev_prev * dev_next) > 0:
            replacement = (prev_v + next_v) / 2.0
            cleaned[i] = replacement
            corrections.append({
                "date": s.index[i].strftime("%Y-%m-%d"),
                "original": float(cur),
                "replacement": float(replacement),
                "prev": float(prev_v),
                "next": float(next_v),
                "dev_prev_pct": round(dev_prev * 100.0, 2),
                "dev_next_pct": round(dev_next * 100.0, 2),
            })
    return pd.Series(cleaned, index=s.index, dtype="float64"), corrections


def fetch_yfinance(symbol: str) -> pd.Series:
    import yfinance as yf
    end = datetime.utcnow()
    start = end - timedelta(days=HISTORY_DAYS)
    df = yf.download(
        symbol,
        start=start.strftime("%Y-%m-%d"),
        end=end.strftime("%Y-%m-%d"),
        progress=False,
        auto_adjust=False,
        threads=False,
    )
    if df is None or df.empty:
        return pd.Series(dtype="float64")
    # yfinance sometimes returns a MultiIndex on columns even for a single symbol.
    if isinstance(df.columns, pd.MultiIndex):
        # take the outer level "Close"
        if "Close" in df.columns.get_level_values(0):
            close = df["Close"]
            if isinstance(close, pd.DataFrame):
                close = close.iloc[:, 0]
        else:
            close = df.iloc[:, 0]
    else:
        close = df["Close"] if "Close" in df.columns else df.iloc[:, 0]
    close = close.dropna()
    close.index = pd.to_datetime(close.index).tz_localize(None).normalize()
    return close.astype("float64")


def fetch_fred(series_id: str) -> pd.Series:
    end = date.today()
    start = end - timedelta(days=HISTORY_DAYS)
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": series_id,
        "api_key": FRED_API_KEY,
        "file_type": "json",
        "observation_start": start.isoformat(),
        "observation_end": end.isoformat(),
    }
    r = requests.get(url, params=params, timeout=30)
    r.raise_for_status()
    obs = r.json().get("observations", [])
    if not obs:
        return pd.Series(dtype="float64")
    idx = pd.to_datetime([o["date"] for o in obs])
    vals = []
    for o in obs:
        v = o["value"]
        try:
            vals.append(float(v))
        except (TypeError, ValueError):
            vals.append(float("nan"))
    s = pd.Series(vals, index=idx).dropna()
    s.index = s.index.normalize()
    return s.astype("float64")


def apply_derived(wide: pd.DataFrame, spec: dict) -> pd.Series:
    op, *args = spec["formula"]
    parts = [wide[a] for a in args if a in wide.columns]
    if len(parts) != len(args):
        missing = [a for a in args if a not in wide.columns]
        print(f"  derived {spec['id']}: missing inputs {missing}", file=sys.stderr)
        return pd.Series(dtype="float64")
    if op == "ratio":
        return parts[0] / parts[1]
    if op == "sub":
        return parts[0] - parts[1]
    raise ValueError(f"unknown derived op {op}")


def main() -> int:
    log: dict[str, dict] = {}
    frames: dict[str, pd.Series] = {}

    # Pass 1: primary sources
    for spec in SERIES:
        sid, src = spec["id"], spec["source"]
        if src == "derived":
            continue
        print(f"fetching {sid} ({src}: {spec['symbol']}) ...", flush=True)
        try:
            if src == "yfinance":
                s = fetch_yfinance(spec["symbol"])
                # be polite to Yahoo
                time.sleep(0.4)
            elif src == "fred":
                s = fetch_fred(spec["symbol"])
            else:
                raise ValueError(f"unknown source {src}")
        except Exception as e:
            log[sid] = {"status": "ERROR", "error": str(e)[:200], "rows": 0}
            print(f"  ERROR {sid}: {e}", file=sys.stderr)
            continue

        if s.empty:
            log[sid] = {"status": "EMPTY", "rows": 0}
            print(f"  EMPTY {sid}", file=sys.stderr)
            continue

        s, corrections = despike(s)
        if corrections:
            print(f"  despiked {sid}: {len(corrections)} correction(s)")
            for c in corrections:
                print(f"    {c['date']} {c['original']:.4f} → {c['replacement']:.4f} "
                      f"(prev={c['prev']:.4f}, next={c['next']:.4f})")

        frames[sid] = s
        log[sid] = {
            "status": "OK",
            "rows": int(len(s)),
            "last_date": s.index.max().strftime("%Y-%m-%d"),
            "last_value": float(s.iloc[-1]),
            "corrections": corrections,
        }

    if not frames:
        print("no primary series fetched — aborting", file=sys.stderr)
        return 1

    wide = pd.concat(frames, axis=1).sort_index()
    wide.index.name = "date"

    # Pass 2: derived
    for spec in SERIES:
        if spec["source"] != "derived":
            continue
        sid = spec["id"]
        s = apply_derived(wide, spec).dropna()
        if s.empty:
            log[sid] = {"status": "EMPTY", "rows": 0}
            continue
        wide[sid] = s
        log[sid] = {
            "status": "OK",
            "rows": int(len(s)),
            "last_date": s.index.max().strftime("%Y-%m-%d"),
            "last_value": float(s.iloc[-1]),
        }

    # Preserve the registry ordering in the CSV.
    ordered = [spec["id"] for spec in SERIES if spec["id"] in wide.columns]
    wide = wide[ordered]

    wide.to_csv(PRICES_CSV)
    with FETCH_LOG.open("w") as f:
        json.dump({"fetched_at": datetime.utcnow().isoformat() + "Z", "series": log}, f, indent=2)

    ok = sum(1 for v in log.values() if v["status"] == "OK")
    print(f"\nwrote {PRICES_CSV} — {ok}/{len(log)} series OK, {len(wide)} rows")
    for sid, meta in log.items():
        tag = meta["status"]
        if tag == "OK":
            print(f"  {tag:5} {sid:28} rows={meta['rows']:4} last={meta['last_date']} val={meta['last_value']:.4f}")
        else:
            print(f"  {tag:5} {sid:28} {meta.get('error','')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
