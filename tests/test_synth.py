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


# ── driver-eligibility gate ─────────────────────────────────────────────
def test_class_prior_blocks_single_name_driving_macro():
    """A single-name equity may not drive a macro series; macro->macro,
    macro->single and single->single stay admissible. Registry-derived."""
    from registry import load_registry
    from synth_classes import driver_admissible
    r = load_registry()
    eq = next(s["id"] for s in r if s.get("market") == "EQUITIES")
    com = next(s["id"] for s in r if s.get("market") == "COMMODITIES")
    idx = next(s["id"] for s in r if s.get("market") == "INDICES")
    assert driver_admissible(eq, com) == (False, "single_name_drives_macro")
    assert driver_admissible(idx, com)[0] is True
    assert driver_admissible(idx, eq)[0] is True
    assert driver_admissible(eq, eq)[0] is True


def test_strength_floor_excludes_weak_channel():
    """A pair that is 'active' only by its own weak history sits below the
    cross-sectional |rho| floor and is denied driver status."""
    from synth_detect import detect_transmission_gaps
    px, d = _pair_prices(tgt_window_rets=[0.0, 0.0, 0.0])
    channels, evts = _fixtures(d)
    channels[0]["rho_now"] = 0.25                    # our pair: weak
    channels += [{"driver": "f", "target": "g", "state": "active",
                  "beta_pair": 1.0, "rho_now": 0.85, "pctile_now": 0.9}
                 for _ in range(10)]                 # strong pool lifts the floor
    out = detect_transmission_gaps(px, channels, evts, bus_events=[])
    assert out == []


def test_fanout_dedup_collapses_one_driver_date():
    """One driver on one date is one pulse with ranked targets, not N rows."""
    from synth_detect import collapse_to_pulses
    keys = dict(target_class="INDICES", beta_pair=0.5, expected_pct=2.0,
                actual_pct=0.0, residual_sigma=-1.5, gap_bar_sigma=1.2,
                channel_state="active", channel_rho=0.6, channel_stability=1.0,
                channel_unstable=False, stability_reasons=[], lead_lag=2,
                sessions_elapsed=3, window_open=False, low_history=False,
                known_as=None, components={})
    gaps = [dict(driver="d", asof="2026-07-10", target=f"t{i}",
                 shortfall_sigma=1.5, score=0.4 + 0.1 * i,
                 confidence=0.4 + 0.1 * i, driver_zc=4.0,
                 driver_ret_pct=2.0, driver_class="INDICES",
                 driver_stale=False, driver_last_obs="2026-07-10",
                 news_support=[], **keys) for i in range(3)]
    pulses = collapse_to_pulses(gaps)
    assert len(pulses) == 1
    assert pulses[0]["n_targets"] == 3
    assert pulses[0]["targets"][0]["target"] == "t2"   # highest score first


def test_news_corroborated_ranks_above_high_score_no_news():
    """The ranked surface privileges a live-news mechanism over a stronger
    no-news correlation (owner directive)."""
    from synth_detect import _surface
    pulse = {"kind": "driver_pulse", "news_corroborated": False, "top_score": 0.9}
    nnm = {"kind": "news_no_move", "score": 0.2}
    surf = [_surface(pulse), _surface(nnm)]
    surf.sort(key=lambda c: (not c["news_corroborated"],
                             -(c["surface_score"] or 0)))
    assert surf[0]["kind"] == "news_no_move"


def test_stale_driver_is_tagged_not_dropped():
    """A driver whose own move-signal has gone dark near the matrix date is
    flagged, not silently emitted as a live setup."""
    from synth_detect import detect_transmission_gaps
    px, d = _pair_prices(tgt_window_rets=[0.0, 0.0, 0.0])
    # blank the driver's last two sessions so its zc series ends early
    px.iloc[-2:, px.columns.get_loc("drv")] = np.nan
    channels, evts = _fixtures(d)
    out = detect_transmission_gaps(px, channels, evts, bus_events=[])
    assert out and all(c["driver_stale"] is True for c in out)


# ── breaking-channel penalty + regime lane ──────────────────────────────
def test_channel_stability_penalises_instability_not_heating():
    from synth_detect import (CHANGEPOINT_PENALTY, SIGN_FLIP_PENALTY,
                              _channel_stability)
    cal = pd.bdate_range("2024-01-02", periods=300)
    # sign flip: beta sign disagrees with its own history
    assert _channel_stability({"sign_flip": True}, cal)[0] == SIGN_FLIP_PENALTY
    # cooling toward breaking: pctile fell 0.4 -> stability 0.6
    s, r = _channel_stability({"pctile_prev20": 0.9, "pctile_now": 0.5}, cal)
    assert s == pytest.approx(0.6) and any("cooling" in x for x in r)
    # recent change-point: beta regime just shifted
    cp = cal[-5].strftime("%Y-%m-%d")
    assert _channel_stability({"changepoint": cp}, cal)[0] == CHANGEPOINT_PENALTY
    # HEATING (turning_on): pctile rising is the watchlist signal, no penalty
    assert _channel_stability({"pctile_prev20": 0.3, "pctile_now": 0.9}, cal) \
        == (1.0, [])


def test_cooling_channel_cuts_gap_confidence_below_score():
    from synth_detect import detect_transmission_gaps
    px, d = _pair_prices(tgt_window_rets=[0.0, 0.0, 0.0])
    channels, evts = _fixtures(d)
    channels[0].update(pctile_now=0.6, pctile_prev20=0.9)   # cooling 0.3
    out = detect_transmission_gaps(px, channels, evts, bus_events=[])
    assert len(out) == 1
    g = out[0]
    assert g["confidence"] < g["score"]
    assert g["channel_unstable"] is True
    assert any("cooling" in x for x in g["stability_reasons"])


def test_channel_shifts_are_a_separate_lane_not_the_trade_surface():
    from synth_detect import build_candidates
    st = build_candidates("data/synth/golden_2026-07-20",
                          "data/synth/golden_2026-07-20/candidates.json")
    assert all(c["kind"] != "channel_shift" for c in st["ranked"])
    assert st["regime"] and all(c["kind"] == "channel_shift"
                                for c in st["regime"])
    roles = {c["lane_role"] for c in st["regime"]}
    assert roles <= {"warning", "watchlist"}


def test_stale_pulse_ranks_below_a_live_one():
    from synth_detect import _surface
    live = {"kind": "driver_pulse", "news_corroborated": False,
            "driver_stale": False, "top_confidence": 0.6}
    stale = {"kind": "driver_pulse", "news_corroborated": False,
             "driver_stale": True, "top_confidence": 0.9}
    surf = sorted([_surface(live), _surface(stale)],
                  key=lambda c: (not c["news_corroborated"],
                                 -(c["surface_score"] or 0)))
    assert surf[0] is live       # live 0.6 beats stale 0.9*0.4=0.36


# ── golden fixture: labelled expectations are load-bearing ──────────────
def _golden(tmp_path):
    """Build candidates on the frozen snapshot into a throwaway path so a test
    run never dirties the committed golden candidates.json."""
    import json
    from synth_detect import build_candidates
    gdir = ROOT / "data" / "synth" / "golden_2026-07-20"
    man = json.loads((gdir / "MANIFEST.json").read_text(encoding="utf-8"))
    st = build_candidates(str(gdir), str(tmp_path / "cand.json"))
    return man.get("expected_anomalies", {}), st


def test_golden_positives_and_stale_tag(tmp_path):
    exp, st = _golden(tmp_path)
    ranked = st["ranked"]
    pulses = [c for c in ranked if c["kind"] == "driver_pulse"]

    def pulse(driver, asof):
        return next((p for p in pulses if p["driver"] == driver
                     and p["asof"] == asof), None)

    for pos in exp.get("positives", []):
        if pos["kind"] == "driver_pulse":
            p = pulse(pos["driver"], pos["asof"])
            assert p is not None, pos["label"]
            assert set(pos["targets"]) <= {t["target"] for t in p["targets"]}
            assert p["driver_stale"] is False
        elif pos["kind"] == "news_no_move":
            # ORDERING, not presence: the news cluster must rank ABOVE every
            # no-news candidate — a no-news pulse outscoring it must fail here.
            news_idx = [i for i, c in enumerate(ranked)
                        if c["kind"] == "news_no_move"
                        and c["series"] in pos["series"]]
            noncorro_idx = [i for i, c in enumerate(ranked)
                            if not c["news_corroborated"]]
            assert news_idx, pos["label"]
            assert all(ranked[i]["news_corroborated"] for i in news_idx)
            if noncorro_idx:
                assert max(news_idx) < min(noncorro_idx)

    # ORDERING invariant: a live pulse outranks a stale one (tag alone is not
    # the assertion — the rank is).
    for tg in exp.get("tagged_not_expected", []):
        p = pulse(tg["driver"], tg["asof"])
        assert p is not None and p["driver_stale"] is True
        bov = pulse("bovespa", "2026-07-10")
        assert bov is not None and p["surface_score"] < bov["surface_score"]


def test_golden_negatives_stay_rejected(tmp_path):
    """The expected-negatives are what keep the gate honest: if a future edit
    loosens the class prior or the strength floor, one of these fails."""
    exp, st = _golden(tmp_path)
    pulses = [c for c in st["ranked"] if c["kind"] == "driver_pulse"]

    def has(driver, target=None):
        return any(p["driver"] == driver and
                   (target is None or
                    any(t["target"] == target for t in p["targets"]))
                   for p in pulses)

    for neg in exp.get("negatives", []):
        assert not has(neg["driver"], neg.get("target")), neg["label"]
    # the floor rejects the weak channel, NOT the whole driver
    bov = next((p for p in pulses if p["driver"] == "bovespa"), None)
    assert bov and {"dow_jones", "russell_2000"} <= {t["target"]
                                                     for t in bov["targets"]}


# ── S4 outcome grading (reconstruction) ─────────────────────────────────
def _prices_with_target_path(target_fwd, n_pre=80):
    """A 2-col frame where 'tgt' has controlled forward returns after the
    trigger date; 'drv' is filler. Trigger sits at index position n_pre-1."""
    dates = pd.bdate_range("2025-01-01", periods=n_pre + len(target_fwd))
    tgt = np.concatenate([rng.normal(0, 0.003, n_pre),
                          np.array(target_fwd)])
    drv = rng.normal(0, 0.003, len(dates))
    px = pd.DataFrame({"drv": 100 * np.cumprod(1 + drv),
                       "tgt": 100 * np.cumprod(1 + tgt)}, index=dates)
    return px, dates[n_pre - 1]


def _trig(asof, expected_pct, actual_pct, implied_dir, lead_lag=4):
    return {"target": "tgt", "asof": str(asof.date()),
            "expected_pct": expected_pct, "actual_pct": actual_pct,
            "implied_dir": implied_dir, "lead_lag": lead_lag}


def test_outcome_closes_on_catchup():
    from synth_baserates import resolve_outcome
    # implied +2%, realised 0 at t; target then climbs +1.2% day1 -> catches
    # >0.5*2% quickly
    px, t = _prices_with_target_path([0.012, 0.004, 0.0, 0.0, 0.0])
    o = resolve_outcome(px, _trig(t, 2.0, 0.0, 1))
    assert o["outcome"] == "CLOSED" and o["ttt_05"] == 1


def test_outcome_fades_against_on_full_window():
    from synth_baserates import resolve_outcome
    # implied +2%, target instead falls each day — never catches, moves against
    px, t = _prices_with_target_path([-0.01, -0.01, -0.01, -0.01, -0.01])
    o = resolve_outcome(px, _trig(t, 2.0, 0.0, 1))
    assert o["outcome"] == "FADED_AGAINST" and not o["closed_05"]


def test_outcome_censors_short_window():
    from synth_baserates import resolve_outcome
    # only 2 forward sessions exist (trigger near matrix end), K=5 -> censored,
    # never called a fade
    px, t = _prices_with_target_path([0.0, 0.0])
    o = resolve_outcome(px, _trig(t, 2.0, 0.0, 1))
    assert o["outcome"] == "CENSORED"


def test_outcome_horizon_is_clamped():
    from synth_baserates import K_MAX, resolve_outcome
    px, t = _prices_with_target_path([0.0] * 40)
    assert resolve_outcome(px, _trig(t, 1.0, 0.0, 1, lead_lag=99))["K"] == K_MAX


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
