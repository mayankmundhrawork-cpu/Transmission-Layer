"""SYNTH_V2 · S2a — channel discovery over every relation pair.

A "channel" is a *discovered* transmission link, not a curated prior. For
each ordered pair (driver -> target) in data/relations.json we compute the
rolling-60d return correlation over the full price history and ask where
TODAY's reading sits inside that pair's OWN historical distribution:

  active       |rho| is in the upper tail of its own history and materially
               non-zero — the channel is carrying signal right now
  turning_on   same, but it was NOT in the upper tail 20 sessions ago
  breaking     it WAS in the upper tail 20 sessions ago and has since
               collapsed into the lower tail
  dormant      everything else

Because every threshold is a percentile of the pair's own history, a pair
that normally runs at |rho| 0.8 is not "active" at 0.45, and a pair that
normally runs at 0.1 is not dismissed at 0.3. Nothing about which pairs
matter is hardcoded — assumptions.yaml is consulted ONLY to attach a human
name to a channel that the data already found (owner ruling 3).

Also persisted per channel: the PIT pair beta (target on driver, rolling
60d, shifted one session so it never sees the return it explains) — this is
the coefficient S2b's transmission_gap detector uses to form an expected
target move, and the reason the board can finally say "short of implied"
instead of "priced".

Direction: driver/target come from relations' leader/follower (lead-lag
sign), so the pair is ORDERED. Beta and correlation stay contemporaneous;
lead_lag rides along as metadata for the base-rate horizon in S4.

State: data/synth/channels.json.  Run: python synth_channels.py
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

DATA_DIR = Path(__file__).parent / "data"
SYNTH_DIR = DATA_DIR / "synth"
CHANNELS_JSON = SYNTH_DIR / "channels.json"

CORR_WIN = 60          # rolling correlation / beta window (sessions)
LOOKBACK = 20          # "was it on 20 sessions ago" comparison point
MIN_HISTORY = 120      # rolling-corr observations before a pair is scored
HIGH_PCTILE = 0.70     # upper tail of the pair's own |rho| distribution
MID_PCTILE = 0.50
LOW_PCTILE = 0.30
MIN_ABS_RHO = 0.20     # a percentile-high but near-zero corr is still noise


def pair_beta_series(rets: pd.DataFrame, driver: str, target: str,
                     window: int = CORR_WIN) -> pd.Series:
    """PIT rolling beta of target on driver: cov/var over `window`, shifted
    one session so the estimate at date t uses only returns before t."""
    df = rets[[driver, target]].dropna()
    if len(df) < window + 2:
        return pd.Series(dtype=float)
    d, t = df[driver], df[target]
    cov = d.rolling(window).cov(t)
    var = d.rolling(window).var()
    beta = (cov / var.replace(0.0, np.nan)).shift(1)
    return beta.dropna()


def _state(pct_now: float, pct_prev: float, rho_now: float) -> str:
    strong = abs(rho_now) >= MIN_ABS_RHO
    if strong and pct_now >= HIGH_PCTILE:
        return "turning_on" if pct_prev < MID_PCTILE else "active"
    if pct_prev >= HIGH_PCTILE and pct_now <= LOW_PCTILE:
        return "breaking"
    return "dormant"


def _name_overlay() -> dict[tuple[str, str], dict]:
    """assumptions.yaml as a DISPLAY overlay only (ruling 3): {(a,b): rec}
    keyed both orientations so a discovered channel can be given its name."""
    try:
        import yaml
        conf = yaml.safe_load(
            (Path(__file__).parent / "assumptions.yaml").read_text())
    except Exception:
        return {}
    out: dict[tuple[str, str], dict] = {}
    for a in conf.get("assumptions", []):
        rec = {"name": a["name"], "channel": a.get("channel"),
               "expected_sign": int(a.get("expected_sign", 0))}
        out[(a["driver"], a["target"])] = rec
        out[(a["target"], a["driver"])] = rec
    return out


def build_channels(prices: pd.DataFrame | None = None,
                   relations: dict | None = None) -> dict:
    from relations import load_relations

    SYNTH_DIR.mkdir(parents=True, exist_ok=True)
    if prices is None:
        prices = pd.read_csv(DATA_DIR / "prices.csv", index_col=0,
                             parse_dates=True).sort_index()
    rel = relations if relations is not None else load_relations()
    rets = prices.pct_change(fill_method=None)
    overlay = _name_overlay()

    channels = []
    for p in rel.get("pairs", []):
        drv, tgt = p.get("leader"), p.get("follower")
        if not drv or not tgt or drv not in rets.columns or tgt not in rets.columns:
            continue
        df = rets[[drv, tgt]].dropna()
        if len(df) < MIN_HISTORY + CORR_WIN:
            continue
        roll = df[drv].rolling(CORR_WIN).corr(df[tgt]).dropna()
        if len(roll) < MIN_HISTORY:
            continue
        rho_now = float(roll.iloc[-1])
        rho_prev = float(roll.iloc[-1 - LOOKBACK]) if len(roll) > LOOKBACK else rho_now
        hist = roll.iloc[:-1].abs()
        pct_now = float((hist < abs(rho_now)).mean())
        pct_prev = float((hist < abs(rho_prev)).mean())
        state = _state(pct_now, pct_prev, rho_now)

        med = float(roll.median())
        sign_flip = bool(abs(rho_now) >= MIN_ABS_RHO and abs(med) >= MIN_ABS_RHO
                         and np.sign(rho_now) != np.sign(med))

        betas = pair_beta_series(rets, drv, tgt)
        beta_now = float(betas.iloc[-1]) if len(betas) else None

        rec = {
            "driver": drv, "target": tgt,
            "state": state,
            "rho_now": round(rho_now, 3),
            "rho_prev20": round(rho_prev, 3),
            "rho_median": round(med, 3),
            "pctile_now": round(pct_now, 3),
            "pctile_prev20": round(pct_prev, 3),
            "sign_flip": sign_flip,
            "beta_pair": None if beta_now is None else round(beta_now, 4),
            "lead_lag": p.get("lead_lag"),
            "lead_rho": p.get("lead_rho"),
            "n_obs": int(len(roll)),
            "changepoint": None,
        }
        # change-point dating is the expensive step — only for live channels
        if state != "dormant":
            from assumptions import _changepoint_date
            rec["changepoint"] = _changepoint_date(roll)
        nm = overlay.get((drv, tgt))
        if nm:
            rec["known_as"] = nm["name"]
            rec["known_channel"] = nm["channel"]
        channels.append(rec)

    channels.sort(key=lambda c: -c["pctile_now"])
    counts: dict[str, int] = {}
    for c in channels:
        counts[c["state"]] = counts.get(c["state"], 0) + 1
    state = {
        "updated": datetime.now(timezone.utc).isoformat(),
        "data_date": prices.index.max().strftime("%Y-%m-%d"),
        "params": {"corr_window": CORR_WIN, "lookback": LOOKBACK,
                   "high_pctile": HIGH_PCTILE, "low_pctile": LOW_PCTILE,
                   "min_abs_rho": MIN_ABS_RHO},
        "counts": counts,
        "channels": channels,
    }
    CHANNELS_JSON.write_text(json.dumps(state), encoding="utf-8")
    return state


def load_channels() -> dict:
    if CHANNELS_JSON.exists():
        try:
            return json.loads(CHANNELS_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"channels": [], "counts": {}}


def channel_index(state: dict | None = None) -> dict[tuple[str, str], dict]:
    st = state or load_channels()
    return {(c["driver"], c["target"]): c for c in st.get("channels", [])}


if __name__ == "__main__":
    st = build_channels()
    c = st["counts"]
    print(f"channels: {len(st['channels'])} ordered pairs through "
          f"{st['data_date']} | " +
          " · ".join(f"{k} {v}" for k, v in sorted(c.items())))
    live = [x for x in st["channels"] if x["state"] != "dormant"]
    for x in live[:15]:
        nm = f"  [{x['known_as']}]" if x.get("known_as") else ""
        flip = " SIGN-FLIP" if x["sign_flip"] else ""
        print(f"  {x['state']:11} {x['driver']:>14} -> {x['target']:<14} "
              f"rho={x['rho_now']:+.2f} (pct {x['pctile_now']:.2f}, was "
              f"{x['pctile_prev20']:.2f}) beta={x['beta_pair']} "
              f"lag={x['lead_lag']} cp={x['changepoint']}{flip}{nm}")
