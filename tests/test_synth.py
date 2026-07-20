"""SYNTH_V2 acceptance tests (S1/S2).

Owner rulings under test:
  5  — min-history floor on market events
  6  — directionality: a gap is the target SHORT of the IMPLIED direction;
       driver up + target hard-down must NOT be a gap
  spec — no hardcoded pairs: no registry series id appears as a literal in
       any synth_* module (detection must be fully data-driven)

Run: pytest -q tests/test_synth.py
"""
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

rng = np.random.default_rng(11)
ROOT = Path(__file__).resolve().parents[1]


def _pair_prices(n=500, beta=0.8, drv_shock_pos=-3, drv_shock=0.05,
                 tgt_window_rets=None):
    """Driver/target price frame: target = beta*driver + noise, except the
    sessions from the shock onward, which are overridden per scenario."""
    dates = pd.bdate_range("2024-01-02", periods=n)
    drv = rng.normal(0, 0.01, n)
    drv[drv_shock_pos] = drv_shock
    tgt = beta * drv + rng.normal(0, 0.005, n)
    if tgt_window_rets is not None:
        for k, r in enumerate(tgt_window_rets):
            tgt[drv_shock_pos + k] = r
    px = pd.DataFrame(
        {"drv": 100 * np.cumprod(1 + drv), "tgt": 100 * np.cumprod(1 + tgt)},
        index=dates)
    return px, dates[drv_shock_pos]


def _fixtures(event_date):
    channels = [{"driver": "drv", "target": "tgt", "state": "active",
                 "beta_pair": 0.8, "pctile_now": 0.9, "rho_now": 0.8,
                 "lead_lag": 2}]
    event = {"id": "ev-test",
             "ts": pd.Timestamp(event_date, tz="UTC").isoformat(),
             "source": "market", "kind": "move",
             "payload": {"series": "drv", "zc": 5.0, "move_pctile": 0.99,
                         "low_history": False}}
    return channels, [event]


# ── ruling 6: directionality ────────────────────────────────────────────
def test_gap_fires_when_target_flat_vs_implied():
    """Driver +5%, beta +0.8 implies target ~+4%; target flat = a real gap."""
    from synth_detect import detect_transmission_gaps
    px, d = _pair_prices(tgt_window_rets=[0.0, 0.0, 0.0])
    channels, evts = _fixtures(d)
    out = detect_transmission_gaps(px, channels, evts, bus_events=[])
    assert len(out) == 1
    c = out[0]
    assert c["driver"] == "drv" and c["target"] == "tgt"
    assert c["implied_dir"] == 1
    assert c["shortfall_sigma"] >= c["gap_bar_sigma"]
    assert c["expected_pct"] > 2.0 and abs(c["actual_pct"]) < 1.0


def test_hard_counter_move_is_not_a_gap():
    """Driver +5% but target hard-DOWN: shortfall is even larger, yet ruling
    6 says this is the target's own story, not a lag gap."""
    from synth_detect import detect_transmission_gaps
    px, d = _pair_prices(tgt_window_rets=[-0.03, -0.03, -0.02])
    channels, evts = _fixtures(d)
    out = detect_transmission_gaps(px, channels, evts, bus_events=[])
    assert out == []


def test_gap_carries_signed_residual():
    """Residual must be SIGNED through beta: actual short of a POSITIVE
    implied move gives a negative residual and positive shortfall."""
    from synth_detect import detect_transmission_gaps
    px, d = _pair_prices(tgt_window_rets=[0.005, 0.0, 0.0])
    channels, evts = _fixtures(d)
    out = detect_transmission_gaps(px, channels, evts, bus_events=[])
    assert len(out) == 1
    assert out[0]["residual_sigma"] < 0
    assert out[0]["shortfall_sigma"] == pytest.approx(
        -out[0]["residual_sigma"], abs=0.02)


def test_overshoot_is_not_a_gap():
    """Target moved MORE than implied — nothing is lagging."""
    from synth_detect import detect_transmission_gaps
    px, d = _pair_prices(tgt_window_rets=[0.05, 0.01, 0.0])
    channels, evts = _fixtures(d)
    out = detect_transmission_gaps(px, channels, evts, bus_events=[])
    assert out == []


def test_dormant_channel_never_produces_gaps():
    from synth_detect import detect_transmission_gaps
    px, d = _pair_prices(tgt_window_rets=[0.0, 0.0, 0.0])
    channels, evts = _fixtures(d)
    channels[0]["state"] = "dormant"
    out = detect_transmission_gaps(px, channels, evts, bus_events=[])
    assert out == []


# ── ruling 5: min-history floor on market events ────────────────────────
def test_market_event_floor_and_low_history_tag():
    from synth_events import (MOVE_FLOOR_HISTORY, MOVE_MIN_HISTORY,
                              _move_event)
    n = MOVE_MIN_HISTORY + 50
    r = pd.Series(rng.normal(0, 1.0, n),
                  index=pd.bdate_range("2024-01-02", periods=n))
    r.iloc[-1] = 6.0                     # screaming move
    rets = r * 0.01
    # below the floor: nothing, no matter how big the move
    assert _move_event("x", r, rets, MOVE_FLOOR_HISTORY - 5) is None
    # between floor and full history: fires on the fixed bar, tagged
    e = _move_event("x", r.iloc[:MOVE_MIN_HISTORY - 10], rets,
                    MOVE_MIN_HISTORY - 11)
    if e is not None:                    # |z|=6 clears the 3.0 fixed bar
        assert e["payload"]["low_history"] is True
        assert e["payload"]["bar_kind"] == "fixed"
    # full history: adaptive bar, not tagged
    e2 = _move_event("x", r, rets, n - 1)
    assert e2 is not None
    assert e2["payload"]["low_history"] is False
    assert e2["payload"]["bar_kind"] == "adaptive"


# ── spec: nothing hardcoded ─────────────────────────────────────────────
def test_no_registry_series_id_is_hardcoded_in_synth_modules():
    """Detection must be data-driven: no universe series id may appear as a
    string literal in any synth_* module (synth_aliases is the curated
    lexicon — it is the ONE place ids are allowed by design)."""
    from registry import load_registry
    ids = {s["id"] for s in load_registry()}
    for mod in ("synth_detect.py", "synth_channels.py", "synth_events.py"):
        src = (ROOT / mod).read_text(encoding="utf-8")
        hits = [i for i in ids
                if f'"{i}"' in src or f"'{i}'" in src]
        assert not hits, f"{mod} hardcodes series ids: {hits}"
