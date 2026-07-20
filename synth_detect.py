"""SYNTH_V2 · S2b — deterministic anomaly detectors over bus + prices + channels.

Three detectors, no LLM anywhere, every threshold adaptive (a percentile of
the object's OWN history — grep this file: no series id appears as a literal).

transmission_gap (flagship)
    For every driver market-event (adaptive |zc| bar, incl. backfilled
    triggers that WOULD have fired — ruling 8) and every discovered channel
    driver -> target that is currently active/turning_on:

      expected  = beta_pair(d) * driver_ret(d)        beta PIT (shift 1)
      actual    = target cum return over the lead-lag window from d
      residual  = actual - expected                    SIGNED (ruling 6)
      shortfall = -residual * sign(expected)           in target-sigma units

    A candidate exists when shortfall clears the high percentile of that
    pair's OWN shortfall history (same formula applied to every historical
    session). Directionality per ruling 6: the gap is the target being SHORT
    of the IMPLIED direction. If the target moved hard AGAINST the implied
    direction (its own zc beyond its own adaptive bar, counter-signed), that
    is that series' own market event, NOT a lag gap — excluded here.

news_move_divergence
    move_no_news : market event with zero entity-joined text events within
                   NEWS_WINDOW_H — trust discounted by the bus join-miss rate
                   (the instrumentation that makes this claim honest).
    news_no_move : entity whose 48h news intensity (sum salience*weight) is
                   in the top decile of entities-with-news while its own
                   |zc| sits below its own historical median.

channel_shift
    turning_on / breaking / sign-flip channels straight from S2a, scored by
    the size of the percentile migration, with the change-point date.

Scores are DECOMPOSED: every candidate carries its named components and the
rank score is a documented product of them — no opaque composite.

Output: data/synth/candidates.json (ranked). Golden-snapshot mode:
    python synth_detect.py [data_dir]     e.g. data/synth/golden_2026-07-20
"""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pandas as pd

DATA_DIR = Path(__file__).parent / "data"
SYNTH_DIR = DATA_DIR / "synth"
CANDIDATES_JSON = SYNTH_DIR / "candidates.json"

GAP_LOOKBACK_SESSIONS = 5   # driver events this recent can still have open gaps
GAP_QUANTILE = 0.90         # bar = q of the pair's OWN shortfall history
GAP_MIN_HISTORY = 180       # shortfall obs to trust the adaptive bar
GAP_FLOOR_HISTORY = 60      # below this the pair emits nothing (ruling 5 spirit)
GAP_FIXED_BAR = 2.0         # sigma bar used between floor and full history
COUNTER_QUANTILE = 0.50     # a gap is a LAGGARD: any against-move beyond the
COUNTER_FIXED_BAR = 0.67    # target's own MEDIAN window move breaks the lag
#                             story (|N(0,1)| median as the low-history bar)
CHANNEL_STATES_OK = ("active", "turning_on")

NEWS_WINDOW_H = 48          # entity-join window around a market event
NEWS_INTENSITY_PCTILE = 0.90
NO_MOVE_PCTILE = 0.50       # |zc| below own median counts as "did not move"


# ── shared helpers ─────────────────────────────────────────────────────
def _cid(kind: str, key: str) -> str:
    return hashlib.sha1(f"{kind}|{key}".encode()).hexdigest()[:12]


def _fwd_cum(ret: pd.Series, h: int) -> pd.Series:
    """Forward h-session cumulative return starting AT t (t .. t+h-1)."""
    cum = (1.0 + ret).cumprod()
    return cum.shift(-(h - 1)) / cum.shift(1) - 1.0


def _own_bar(abs_hist: pd.Series, q: float, min_hist: int,
             floor_hist: int, fixed_bar: float) -> tuple[float | None, bool]:
    """(bar, low_history) from a series' own |history| — ruling 5 pattern."""
    n = int(abs_hist.notna().sum())
    if n < floor_hist:
        return None, True
    if n < min_hist:
        return fixed_bar, True
    return float(abs_hist.quantile(q)), False


def _news_support(bus_events: list[dict], sid: str, ts_iso: str,
                  window_h: int = NEWS_WINDOW_H) -> list[dict]:
    """Text events joined to `sid` within +/- window_h of ts. Each ref keeps
    the join layer so watch-entry joins stay auditable (ruling 11)."""
    try:
        t0 = datetime.fromisoformat(ts_iso)
    except Exception:
        return []
    lo, hi = t0 - timedelta(hours=window_h), t0 + timedelta(hours=window_h)
    out = []
    for e in bus_events:
        if e["source"] not in ("squawk", "rss") or sid not in e["entities"]:
            continue
        try:
            te = datetime.fromisoformat(e["ts"])
        except Exception:
            continue
        if lo <= te <= hi:
            layers = e["payload"].get("layers") or []
            out.append({"event_id": e["id"], "title": e["payload"]["title"][:120],
                        "salience": e["salience"],
                        "via_watch": any("watch" in l for l in layers)})
    out.sort(key=lambda r: -r["salience"])
    return out[:5]


# ── detector 1: transmission_gap ───────────────────────────────────────
def detect_transmission_gaps(prices: pd.DataFrame, channels: list[dict],
                             market_evts: list[dict],
                             bus_events: list[dict]) -> list[dict]:
    from conditional import ewma_sigma, zc_frame
    from synth_channels import pair_beta_series

    rets = prices.pct_change(fill_method=None)
    sigma = ewma_sigma(rets)
    zc = zc_frame(prices)

    by_driver: dict[str, list[dict]] = {}
    for c in channels:
        if c["state"] in CHANNEL_STATES_OK and c.get("beta_pair") is not None:
            by_driver.setdefault(c["driver"], []).append(c)

    # newest event per (series, date); only drivers that have channels
    ev_by_series: dict[str, list[dict]] = {}
    for e in market_evts:
        sid = e["payload"]["series"]
        if sid in by_driver:
            ev_by_series.setdefault(sid, []).append(e)

    out = []
    for drv, evts in ev_by_series.items():
        for ch in by_driver[drv]:
            tgt = ch["target"]
            if drv not in rets.columns or tgt not in rets.columns:
                continue
            df = rets[[drv, tgt]].dropna()
            if df.empty:
                continue
            betas = pair_beta_series(rets, drv, tgt).reindex(df.index)
            sig_t = sigma[tgt].reindex(df.index)
            h = int(ch.get("lead_lag") or 1) + 1        # event day + k follows
            fwd = _fwd_cum(df[tgt], h)
            # pair's own shortfall history: same formula at every session
            exp_hist = betas * df[drv]
            resid_hist = fwd - exp_hist
            denom = sig_t * np.sqrt(h)
            short_hist = (-resid_hist * np.sign(exp_hist)) / denom

            for e in evts:
                d = pd.Timestamp(e["ts"]).tz_localize(None).normalize()
                if d not in df.index:
                    continue
                pos = df.index.get_loc(d)
                beta_d = betas.iloc[pos]
                sig_d = sig_t.iloc[pos]
                drv_ret = float(df[drv].iloc[pos])
                if not np.isfinite(beta_d) or not np.isfinite(sig_d) or sig_d <= 0:
                    continue
                expected = float(beta_d) * drv_ret
                if expected == 0.0:
                    continue
                implied_dir = float(np.sign(expected))

                h_avail = min(h, len(df) - pos)
                seg = df[tgt].iloc[pos:pos + h_avail]
                actual = float((1.0 + seg).prod() - 1.0)
                resid = actual - expected
                short_now = (-resid * implied_dir) / (float(sig_d) * np.sqrt(h_avail))

                hist = short_hist.iloc[:pos].dropna()
                bar, low_hist = _own_bar(hist, GAP_QUANTILE, GAP_MIN_HISTORY,
                                         GAP_FLOOR_HISTORY, GAP_FIXED_BAR)
                if bar is None or short_now < bar:
                    continue

                # ruling 6: a counter-move = the target's own story, not a
                # lag gap. Two adaptive exclusions, both from the target's own
                # history: (a) any single day's zc counter-signed beyond its
                # own market-event bar; (b) the cumulative window move against
                # the implied direction beyond the target's own MEDIAN window
                # move — a laggard is flat-to-noise, not "moved the other way"
                # (catches the grind-down no single day flags).
                tz = zc[tgt].reindex(df.index).iloc[pos:pos + h_avail]
                tz_hist = zc[tgt].reindex(df.index).iloc[:pos].abs().dropna()
                t_bar, _ = _own_bar(tz_hist, 0.98, 180, 60, 3.0)
                if t_bar is not None and \
                        float((tz * implied_dir).min() if len(tz) else 0) <= -t_bar:
                    continue
                actual_z = actual / (float(sig_d) * np.sqrt(h_avail))
                win_hist = (fwd / denom).iloc[:pos].abs().dropna()
                c_bar, _ = _own_bar(win_hist, COUNTER_QUANTILE,
                                    GAP_MIN_HISTORY, GAP_FLOOR_HISTORY,
                                    COUNTER_FIXED_BAR)
                if c_bar is not None and actual_z * implied_dir <= -c_bar:
                    continue

                gap_pct = float((hist < short_now).mean()) if len(hist) else None
                news = _news_support(bus_events, drv, e["ts"])
                comp = {
                    "driver_move_pctile": e["payload"].get("move_pctile"),
                    "channel_pctile": ch["pctile_now"],
                    "gap_pctile": gap_pct,
                }
                score = None
                if all(v is not None for v in comp.values()):
                    score = round(comp["driver_move_pctile"] *
                                  comp["channel_pctile"] * comp["gap_pctile"], 4)
                out.append({
                    "id": _cid("gap", f"{drv}|{tgt}|{d:%Y-%m-%d}"),
                    "kind": "transmission_gap",
                    "asof": f"{d:%Y-%m-%d}",
                    "driver": drv, "target": tgt,
                    "driver_zc": e["payload"]["zc"],
                    "driver_ret_pct": round(drv_ret * 100, 3),
                    "beta_pair": round(float(beta_d), 4),
                    "expected_pct": round(expected * 100, 3),
                    "actual_pct": round(actual * 100, 3),
                    "residual_sigma": round(float(-short_now * implied_dir), 2),
                    "shortfall_sigma": round(float(short_now), 2),
                    "gap_bar_sigma": round(bar, 2),
                    "implied_dir": int(implied_dir),
                    "channel_state": ch["state"],
                    "channel_rho": ch["rho_now"],
                    "known_as": ch.get("known_as"),
                    "lead_lag": ch.get("lead_lag"),
                    "sessions_elapsed": int(h_avail),
                    "window_open": bool(h_avail < h),
                    "low_history": bool(low_hist or
                                        e["payload"].get("low_history")),
                    "components": comp, "score": score,
                    "news_support": news,
                    "watch_join": any(n["via_watch"] for n in news),
                    "refs": {"market_event": e["id"]},
                })
    out.sort(key=lambda c: -(c["score"] or 0))
    return out


# ── detector 2: news_move_divergence ───────────────────────────────────
def detect_news_move_divergence(prices: pd.DataFrame, bus: dict,
                                now: datetime) -> list[dict]:
    from conditional import zc_frame
    zc = zc_frame(prices)
    events = bus.get("events", [])
    miss_rate = float(bus.get("join_miss_rate") or 0.0)
    out = []

    # (a) big move, no news
    for e in events:
        if e["source"] != "market":
            continue
        sid = e["payload"]["series"]
        news = _news_support(events, sid, e["ts"])
        if news:
            continue
        trust = round(1.0 - miss_rate, 3)   # honest: how complete is the join
        pct = e["payload"].get("move_pctile")
        comp = {"move_pctile": pct, "join_trust": trust}
        out.append({
            "id": _cid("mnn", f"{sid}|{e['ts'][:10]}"),
            "kind": "move_no_news", "asof": e["ts"][:10],
            "series": sid, "zc": e["payload"]["zc"],
            "ret_1d_pct": e["payload"].get("ret_1d_pct"),
            "low_history": bool(e["payload"].get("low_history")),
            "components": comp,
            "score": None if pct is None else round(pct * trust, 4),
            "refs": {"market_event": e["id"]},
        })

    # (b) big news, no move — 48h entity intensity vs own-zc quietness
    cutoff = (now - timedelta(hours=NEWS_WINDOW_H)).isoformat()
    intensity: dict[str, float] = {}
    heads: dict[str, list[dict]] = {}
    for e in events:
        if e["source"] not in ("squawk", "rss") or e["ts"] < cutoff:
            continue
        wts = e["payload"].get("entity_weights") or {}
        layers = e["payload"].get("layers") or []
        for sid in e["entities"]:
            w = wts.get(sid, 1.0)
            intensity[sid] = intensity.get(sid, 0.0) + e["salience"] * w
            heads.setdefault(sid, []).append(
                {"event_id": e["id"], "title": e["payload"]["title"][:120],
                 "salience": e["salience"],
                 "via_watch": any("watch" in l for l in layers)})
    if intensity:
        vals = pd.Series(intensity)
        bar = float(vals.quantile(NEWS_INTENSITY_PCTILE))
        for sid, inten in vals[vals >= bar].items():
            if sid not in zc.columns:
                continue
            s = zc[sid].dropna()
            if len(s) < GAP_FLOOR_HISTORY:
                continue
            z_now = float(s.iloc[-1])
            own_med = float(s.abs().iloc[:-1].median())
            if abs(z_now) >= own_med:
                continue                    # it moved (by its own standard)
            quiet = float((s.abs().iloc[:-1] > abs(z_now)).mean())
            ipct = float((vals < inten).mean())
            supp = sorted(heads[sid], key=lambda r: -r["salience"])[:5]
            comp = {"intensity_pctile": round(ipct, 3),
                    "quietness_pctile": round(quiet, 3)}
            out.append({
                "id": _cid("nnm", f"{sid}|{now:%Y-%m-%d}"),
                "kind": "news_no_move", "asof": f"{now:%Y-%m-%d}",
                "series": sid, "zc": round(z_now, 2),
                "own_median_abs_zc": round(own_med, 2),
                "news_intensity": round(float(inten), 3),
                "n_headlines": len(heads[sid]),
                "components": comp,
                "score": round(ipct * quiet, 4),
                "news_support": supp,
                "watch_join": any(n["via_watch"] for n in supp),
                "refs": {},
            })
    out.sort(key=lambda c: -(c["score"] or 0))
    return out


# ── detector 3: channel_shift ──────────────────────────────────────────
def detect_channel_shifts(channels: list[dict]) -> list[dict]:
    out = []
    for c in channels:
        shift = c["state"] in ("turning_on", "breaking")
        if not shift and not c.get("sign_flip"):
            continue
        move = abs(c["pctile_now"] - c["pctile_prev20"])
        out.append({
            "id": _cid("chs", f"{c['driver']}|{c['target']}|{c['state']}"),
            "kind": "channel_shift",
            "driver": c["driver"], "target": c["target"],
            "state": c["state"], "sign_flip": c.get("sign_flip", False),
            "rho_now": c["rho_now"], "rho_prev20": c["rho_prev20"],
            "beta_pair": c.get("beta_pair"),
            "known_as": c.get("known_as"),
            "changepoint": c.get("changepoint"),
            "components": {"pctile_migration": round(move, 3)},
            "score": round(move, 4),
            "refs": {},
        })
    out.sort(key=lambda c: -(c["score"] or 0))
    return out


# ── build ──────────────────────────────────────────────────────────────
def build_candidates(data_dir: Path | str | None = None,
                     out_path: Path | str | None = None) -> dict:
    """Run all detectors. `data_dir` overrides where prices/channels/events
    are read from (golden-snapshot mode); output still goes to out_path
    (default data/synth/candidates.json) unless overridden."""
    from synth_events import market_events_backfill

    base = Path(data_dir) if data_dir else DATA_DIR
    prices = pd.read_csv(
        base / "prices.csv" if (base / "prices.csv").exists()
        else DATA_DIR / "prices.csv", index_col=0, parse_dates=True).sort_index()

    def _load(name: str, fallback: Path) -> dict:
        p = base / name
        if not p.exists():
            p = fallback
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return {}

    channels_state = _load("channels.json", SYNTH_DIR / "channels.json")
    bus = _load("events.json", SYNTH_DIR / "events.json")
    channels = channels_state.get("channels", [])
    bus_events = bus.get("events", [])
    now = datetime.now(timezone.utc)

    # reconstructed driver triggers — what WOULD have fired (ruling 8)
    market_evts = market_events_backfill(prices, sessions=GAP_LOOKBACK_SESSIONS)

    gaps = detect_transmission_gaps(prices, channels, market_evts, bus_events)
    divs = detect_news_move_divergence(prices, bus, now)
    shifts = detect_channel_shifts(channels)

    state = {
        "updated": now.isoformat(),
        "data_date": prices.index.max().strftime("%Y-%m-%d"),
        "source_dir": str(base),
        "params": {"gap_quantile": GAP_QUANTILE,
                   "gap_lookback_sessions": GAP_LOOKBACK_SESSIONS,
                   "news_window_h": NEWS_WINDOW_H,
                   "news_intensity_pctile": NEWS_INTENSITY_PCTILE},
        "counts": {"transmission_gap": len(gaps),
                   "move_no_news": sum(1 for c in divs
                                       if c["kind"] == "move_no_news"),
                   "news_no_move": sum(1 for c in divs
                                       if c["kind"] == "news_no_move"),
                   "channel_shift": len(shifts)},
        "candidates": gaps + divs + shifts,
    }
    outp = Path(out_path) if out_path else CANDIDATES_JSON
    outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text(json.dumps(state), encoding="utf-8")
    return state


def load_candidates() -> dict:
    if CANDIDATES_JSON.exists():
        try:
            return json.loads(CANDIDATES_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"candidates": [], "counts": {}}


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else None
    st = build_candidates(src)
    c = st["counts"]
    print(f"candidates from {st['source_dir']} (data {st['data_date']}): "
          + " · ".join(f"{k} {v}" for k, v in c.items()))
    for cd in st["candidates"]:
        if cd["kind"] == "transmission_gap":
            nm = f" [{cd['known_as']}]" if cd.get("known_as") else ""
            print(f"  GAP  {cd['driver']:>14} -> {cd['target']:<14} "
                  f"drv_zc={cd['driver_zc']:+.1f} beta={cd['beta_pair']:+.3f} "
                  f"exp={cd['expected_pct']:+.2f}% act={cd['actual_pct']:+.2f}% "
                  f"short={cd['shortfall_sigma']:.2f}s(bar {cd['gap_bar_sigma']:.2f}) "
                  f"ch={cd['channel_state']} score={cd['score']}{nm}")
        elif cd["kind"] == "move_no_news":
            print(f"  MNN  {cd['series']:>14} zc={cd['zc']:+.1f} "
                  f"ret={cd['ret_1d_pct']}% score={cd['score']}")
        elif cd["kind"] == "news_no_move":
            print(f"  NNM  {cd['series']:>14} zc={cd['zc']:+.1f} "
                  f"intensity={cd['news_intensity']} n={cd['n_headlines']} "
                  f"score={cd['score']}")
        else:
            print(f"  CHS  {cd['driver']:>14} -> {cd['target']:<14} "
                  f"{cd['state']}{' SIGN-FLIP' if cd['sign_flip'] else ''} "
                  f"rho {cd['rho_prev20']} -> {cd['rho_now']} score={cd['score']}")
