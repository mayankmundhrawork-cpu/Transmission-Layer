"""Continuous-tier fetch — registry-driven, incremental, rate-limit-safe.

v4 changes (see V3_BUILD_NOTES.md):
- symbol list comes from registry (backbone + news-admitted universe), not a
  hardcoded config list;
- known symbols get a cheap 15-day tail refresh merged onto committed history;
  only NEW symbols get a full 2-year backfill, budgeted per run — so request
  volume stays low even as the universe grows;
- yfinance calls are batched with sleeps, retries and per-symbol fallback; one
  bad ticker never sinks the run.

The despike filter is UNCHANGED from the proven v1 implementation.

Output: data/prices.csv (rows = date, cols = series id)
        data/fetch_log.json (per-series status + corrections + run meta)

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

from registry import load_registry
from settings import MAX_BACKFILL_PER_RUN, get_fred_key

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)
PRICES_CSV = DATA_DIR / "prices.csv"
FETCH_LOG = DATA_DIR / "fetch_log.json"

# ~2 years of history — enough for 20-day z, 60-day z, and 252-day percentile.
HISTORY_DAYS = 730
TAIL_PERIOD = "15d"      # incremental refresh window for known symbols
MIN_KNOWN_ROWS = 50      # fewer than this → treat as new (re-backfill)
BATCH_SIZE = 10
BATCH_SLEEP = 1.0        # seconds between yfinance batch calls
RETRY_SLEEP = 10.0

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


# ── yfinance ───────────────────────────────────────────────────────────
def _clean_close(obj) -> pd.Series:
    s = obj.dropna()
    if s.empty:
        return pd.Series(dtype="float64")
    s.index = pd.to_datetime(s.index).tz_localize(None).normalize()
    s = s[~s.index.duplicated(keep="last")]
    return s.astype("float64")


def fetch_yf_single(symbol: str, *, full: bool) -> pd.Series:
    import yfinance as yf
    kwargs = dict(progress=False, auto_adjust=False, threads=False)
    if full:
        end = datetime.utcnow()
        start = end - timedelta(days=HISTORY_DAYS)
        df = yf.download(symbol, start=start.strftime("%Y-%m-%d"),
                         end=end.strftime("%Y-%m-%d"), **kwargs)
    else:
        df = yf.download(symbol, period=TAIL_PERIOD, **kwargs)
    if df is None or df.empty:
        return pd.Series(dtype="float64")
    if isinstance(df.columns, pd.MultiIndex):
        if "Close" in df.columns.get_level_values(0):
            close = df["Close"]
            if isinstance(close, pd.DataFrame):
                close = close.iloc[:, 0]
        else:
            close = df.iloc[:, 0]
    else:
        close = df["Close"] if "Close" in df.columns else df.iloc[:, 0]
    return _clean_close(close)


def fetch_yf_batch_tails(symbols: list[str]) -> dict[str, pd.Series]:
    """Tail-refresh a batch in one request; per-symbol fallback on failure."""
    import yfinance as yf
    out: dict[str, pd.Series] = {}
    if not symbols:
        return out
    try:
        df = yf.download(symbols, period=TAIL_PERIOD, progress=False,
                         auto_adjust=False, threads=False, group_by="column")
    except Exception as e:
        print(f"  WARN batch failed ({symbols[0]}..): {str(e)[:100]} — "
              f"falling back per-symbol", file=sys.stderr)
        df = None
    if df is not None and not df.empty:
        try:
            close = df["Close"] if isinstance(df.columns, pd.MultiIndex) else df[["Close"]]
            for sym in symbols:
                if isinstance(close, pd.DataFrame) and sym in close.columns:
                    out[sym] = _clean_close(close[sym])
                elif len(symbols) == 1:
                    out[sym] = _clean_close(close.squeeze())
        except Exception:
            pass
    missing = [s for s in symbols if s not in out or out[s].empty]
    for sym in missing:
        try:
            out[sym] = fetch_yf_single(sym, full=False)
        except Exception as e:
            print(f"  WARN tail failed {sym}: {str(e)[:100]}", file=sys.stderr)
            out[sym] = pd.Series(dtype="float64")
        time.sleep(0.3)
    return out


# ── FRED ───────────────────────────────────────────────────────────────
def fetch_fred(series_id: str) -> pd.Series:
    end = date.today()
    start = end - timedelta(days=HISTORY_DAYS)
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": series_id,
        "api_key": get_fred_key(),
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
        try:
            vals.append(float(o["value"]))
        except (TypeError, ValueError):
            vals.append(float("nan"))
    s = pd.Series(vals, index=idx).dropna()
    s.index = s.index.normalize()
    return s.astype("float64")


# ── derived ────────────────────────────────────────────────────────────
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


# ── main ───────────────────────────────────────────────────────────────
def main() -> int:
    registry = load_registry()
    log: dict[str, dict] = {}

    existing = pd.DataFrame()
    if PRICES_CSV.exists():
        try:
            existing = pd.read_csv(PRICES_CSV, index_col=0, parse_dates=True).sort_index()
        except Exception as e:
            print(f"  WARN could not read existing prices.csv: {e}", file=sys.stderr)

    def known(sid: str) -> bool:
        return sid in existing.columns and existing[sid].dropna().shape[0] >= MIN_KNOWN_ROWS

    yf_specs = [s for s in registry if s["source"] == "yfinance"]
    fred_specs = [s for s in registry if s["source"] == "fred"]
    derived_specs = [s for s in registry if s["source"] == "derived"]

    tails = [s for s in yf_specs if known(s["id"])]
    backfills = [s for s in yf_specs if not known(s["id"])]
    deferred_backfills = backfills[MAX_BACKFILL_PER_RUN:]
    backfills = backfills[:MAX_BACKFILL_PER_RUN]
    if deferred_backfills:
        print(f"backfill budget: deferring {len(deferred_backfills)} symbols "
              f"to the next run: {[s['id'] for s in deferred_backfills]}")

    frames: dict[str, pd.Series] = {}

    # 1 · tail refresh known yfinance symbols, in batches
    print(f"tail-refresh {len(tails)} known symbols "
          f"({(len(tails) + BATCH_SIZE - 1) // BATCH_SIZE} batches) ...")
    sym_to_id = {s["symbol"]: s["id"] for s in yf_specs}
    for i in range(0, len(tails), BATCH_SIZE):
        chunk = [s["symbol"] for s in tails[i:i + BATCH_SIZE]]
        got = fetch_yf_batch_tails(chunk)
        empty = [sym for sym, ser in got.items() if ser.empty]
        if len(empty) == len(chunk):  # whole batch empty → likely throttled
            print(f"  batch {i//BATCH_SIZE}: all empty, retrying in {RETRY_SLEEP}s",
                  file=sys.stderr)
            time.sleep(RETRY_SLEEP)
            got = fetch_yf_batch_tails(chunk)
        for sym, ser in got.items():
            frames[sym_to_id[sym]] = ser
        time.sleep(BATCH_SLEEP)

    # 2 · full backfill for new symbols (budgeted)
    for spec in backfills:
        sid, sym = spec["id"], spec["symbol"]
        print(f"backfill {sid} ({sym}) ...", flush=True)
        try:
            frames[sid] = fetch_yf_single(sym, full=True)
        except Exception as e:
            log[sid] = {"status": "ERROR", "error": str(e)[:200], "rows": 0}
            print(f"  ERROR {sid}: {e}", file=sys.stderr)
        time.sleep(0.6)

    # 3 · FRED (few series, cheap, full window each run as before)
    for spec in fred_specs:
        sid = spec["id"]
        print(f"fred {sid} ({spec['symbol']}) ...", flush=True)
        try:
            frames[sid] = fetch_fred(spec["symbol"])
        except Exception as e:
            log[sid] = {"status": "ERROR", "error": str(e)[:200], "rows": 0}
            print(f"  ERROR {sid}: {e}", file=sys.stderr)

    # 4 · merge onto existing history (fresh values win on overlap), despike
    no_despike = {s["id"] for s in registry if s.get("no_despike")}
    wide = existing.copy()
    for sid, fresh in frames.items():
        if fresh is None or fresh.empty:
            if sid not in wide.columns:
                log.setdefault(sid, {"status": "EMPTY", "rows": 0})
            else:
                base = wide[sid].dropna()
                log.setdefault(sid, {
                    "status": "STALE", "rows": int(len(base)),
                    "last_date": base.index.max().strftime("%Y-%m-%d") if len(base) else None,
                })
            continue
        base = wide[sid] if sid in wide.columns else pd.Series(dtype="float64")
        merged = fresh.combine_first(base).sort_index()
        if sid in no_despike:
            merged, corrections = merged.dropna(), []
        else:
            merged, corrections = despike(merged.dropna())
        if corrections:
            print(f"  despiked {sid}: {len(corrections)} correction(s)")
        wide[sid] = merged
        log[sid] = {
            "status": "OK",
            "rows": int(merged.dropna().shape[0]),
            "last_date": merged.dropna().index.max().strftime("%Y-%m-%d"),
            "last_value": float(merged.dropna().iloc[-1]),
            "corrections": corrections,
        }

    if wide.empty:
        print("no data at all — aborting without writing", file=sys.stderr)
        return 1

    # 5 · derived series over the merged frame
    for spec in derived_specs:
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
            "corrections": [],
        }

    # 6 · column order: registry first, legacy history after (kept, not fetched)
    reg_ids = [s["id"] for s in registry if s["id"] in wide.columns]
    legacy = [c for c in wide.columns if c not in reg_ids]
    wide = wide[reg_ids + legacy].sort_index()
    wide.index.name = "date"
    # trim rows older than the stats window needs
    cutoff = pd.Timestamp(datetime.utcnow().date() - timedelta(days=HISTORY_DAYS))
    wide = wide[wide.index >= cutoff]

    wide.to_csv(PRICES_CSV)
    meta = {
        "fetched_at": datetime.utcnow().isoformat() + "Z",
        "registry_series": len(registry),
        "tails": len(tails), "backfills": len(backfills),
        "deferred_backfills": [s["id"] for s in deferred_backfills],
        "legacy_columns": legacy,
        "series": log,
    }
    with FETCH_LOG.open("w") as f:
        json.dump(meta, f, indent=2)

    ok = sum(1 for v in log.values() if v["status"] == "OK")
    print(f"\nwrote {PRICES_CSV} — {ok}/{len(log)} series OK, "
          f"{len(wide)} rows x {len(wide.columns)} cols")
    for sid, m in sorted(log.items(), key=lambda kv: kv[1]["status"]):
        if m["status"] == "OK":
            print(f"  OK    {sid:26} rows={m['rows']:4} last={m['last_date']} "
                  f"val={m['last_value']:.4f}")
        else:
            print(f"  {m['status']:5} {sid:26} {m.get('error','')[:80]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
