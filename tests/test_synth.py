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


# ── S5 investigation-assembler (deterministic, LLM-off) ─────────────────
def test_cap_is_arithmetic_monotonic_not_a_request():
    """S6/Call B may only LOWER a disposition; a proposed promotion above the
    reference-class cap is overridden in CODE and flagged (owner: the cap is
    real because it is arithmetic, not a polite instruction to the model)."""
    from synth_packet import VERDICT_CAP, clamp_disposition
    # NO_RELIABLE_EDGE caps at LEAD — a hallucinated OBSERVATION is clamped
    assert VERDICT_CAP["NO_RELIABLE_EDGE"] == "LEAD"
    final, overridden = clamp_disposition("OBSERVATION", "LEAD")
    assert final == "LEAD" and overridden is True
    # lowering is always allowed and not flagged as an override
    assert clamp_disposition("DISMISS", "LEAD") == ("DISMISS", False)
    assert clamp_disposition("LEAD", "LEAD") == ("LEAD", False)


def test_golden_bovespa_lead_packet_is_self_sufficient():
    """The hard case: a NO_RELIABLE_EDGE transmission divergence, no news,
    cooling channel. The deterministic packet must carry everything a cold
    reader needs — verdict headline, evidence, news-absence, the question,
    the falsifier — with the LLM OFF."""
    import json
    import pandas as pd
    from relations import load_relations
    from synth_packet import assemble_transmission_packet, render_packet
    gdir = ROOT / "data" / "synth" / "golden_2026-07-20"
    prices = pd.read_csv(gdir / "prices.csv", index_col=0,
                         parse_dates=True).sort_index()
    cands = json.loads((gdir / "candidates.json").read_text(encoding="utf-8"))
    bov = next(c for c in cands["candidates"]
               if c["kind"] == "driver_pulse" and c["driver"] == "bovespa")
    pkt = assemble_transmission_packet(
        bov, prices, load_relations().get("neighbours", {}))
    # capped to LEAD by the reference-class verdict, never OBSERVATION
    assert pkt["disposition"] == "LEAD"
    assert pkt["reference_class"]["verdict"] == "NO_RELIABLE_EDGE"
    # evidence present, and it is under reference_class, never the headline
    ev = pkt["reference_class"]["evidence"]
    assert ev["rate_05"]["wilson95"][0] < 0.5           # coin-flip floor
    assert ev["miss_split_episodes"]["faded_against"] > \
        ev["miss_split_episodes"]["faded_flat"]         # against-skew shown
    # the honest context a cold reader needs
    assert pkt["corroboration"]["news_join"] is None    # no catalyst
    assert any(d["channel_unstable"] for d in pkt["divergence"])  # cooling ch
    assert pkt["the_question"] and pkt["falsifier"]
    rendered = render_packet(pkt)
    assert "NO_RELIABLE_EDGE" in rendered and "FALSIFIER" in rendered


def test_golden_board_tiers_news_above_capped_transmission_leads(tmp_path):
    """Integration: on the golden board a news OBSERVATION always outranks every
    transmission LEAD, the leads are capped by their NO_RELIABLE_EDGE reference
    class (never OBSERVATION), and no scoring quirk re-promotes a capped lead."""
    from synth_detect import build_candidates
    st = build_candidates("data/synth/golden_2026-07-20",
                          str(tmp_path / "c.json"))
    ranked = st["ranked"]
    tiers = [c["tier"] for c in ranked]
    assert tiers == sorted(tiers)                       # tier is primary order
    last_obs = max((i for i, c in enumerate(ranked)
                    if c["disposition"] == "OBSERVATION"), default=-1)
    first_lead = min((i for i, c in enumerate(ranked)
                      if c["disposition"] == "LEAD"), default=len(ranked))
    assert last_obs < first_lead                        # every OBS above LEADs
    # four-tier ordering: news(1) OBS > unexplained-move(2) LEAD > transmission(3)
    tier_of = {"news_no_move": 1, "move_no_news": 2, "driver_pulse": 3}
    for c in ranked:
        assert c["tier"] == tier_of[c["kind"]]
        if c["kind"] == "driver_pulse":
            assert c["reference_verdict"] == "NO_RELIABLE_EDGE"
            assert c["disposition"] == "LEAD"           # capped, not promoted
        if c["kind"] == "news_no_move":
            assert c["disposition"] == "OBSERVATION"
        if c["kind"] == "move_no_news":
            assert c["disposition"] == "LEAD" and c["tier"] == 2
    # an unexplained move outranks every transmission lead, categorically
    mnn_idx = [i for i, c in enumerate(ranked) if c["kind"] == "move_no_news"]
    pulse_idx = [i for i, c in enumerate(ranked) if c["kind"] == "driver_pulse"]
    if mnn_idx and pulse_idx:
        assert max(mnn_idx) < min(pulse_idx)
    # regime lane stays separate from the trade surface
    assert all(c["kind"] != "channel_shift" for c in ranked)
    assert st["regime"]


def test_move_packet_discloses_join_trust_not_silent_no_cause():
    """A move_no_news LEAD must disclose HOW HARD it looked: 'no news' at low
    join-trust is a low-recall maybe, not a confident dislocation. The packet
    must never let 'no news joined' quietly imply 'no cause'."""
    from synth_packet import assemble_move_packet, render_move_packet
    cand = {"kind": "move_no_news", "asof": "2026-07-14",
            "series": "wti", "zc": 9.5, "ret_1d_pct": 16.6,
            "components": {"move_pctile": 1.0, "join_trust": 0.735}}
    pkt = assemble_move_packet(cand)
    assert pkt["disposition"] == "LEAD"
    assert pkt["reference_class"]["verdict"] == "NOT_APPLICABLE"
    assert pkt["explanation_search"]["join_trust"] == 0.735
    assert "low-recall" in pkt["explanation_search"]["reading"].lower()
    # a high-trust move reads as a confident no
    hi = assemble_move_packet({**cand, "components": {"join_trust": 0.95}})
    assert "confident" in hi["explanation_search"]["reading"].lower()
    assert "join-trust" in render_move_packet(pkt).lower()


def test_golden_wti_news_packet_is_loud_about_no_reference_class():
    """The tier-1 anatomy: no base-rate verdict to lean on. Self-sufficiency
    must come from newsflow density + complex co-quiet, and the absence of a
    rateable reference class must be STATED (an omitted section reads as
    'nothing to say'; an explicit NOT_APPLICABLE reads as the honest gap)."""
    import json
    from synth_packet import assemble_news_packet, render_news_packet
    cands = json.loads((ROOT / "data" / "synth" / "golden_2026-07-20"
                        / "candidates.json").read_text(encoding="utf-8"))["candidates"]
    wti = next(c for c in cands if c["kind"] == "news_no_move"
               and c["series"] == "wti")
    pkt = assemble_news_packet(wti, cands)
    assert pkt["disposition"] == "OBSERVATION"
    # the no-reference-class section is PRESENT and explicit, not omitted
    assert pkt["reference_class"]["verdict"] == "NOT_APPLICABLE"
    assert "not" in pkt["reference_class"]["basis"].lower() and \
        "base-rate" in pkt["reference_class"]["basis"].lower()
    # self-sufficiency fields: newsflow density + complex co-quiet
    assert pkt["corroboration"]["news_cluster"]["n_headlines"] >= 10
    assert set(pkt["corroboration"]["complex_co_quiet"]) & {"brent", "vix"}
    assert pkt["the_question"] and pkt["falsifier"]
    rendered = render_news_packet(pkt)
    assert "NOT_APPLICABLE" in rendered and "co-quiet" in rendered


# ── taxonomy completeness (no fail-open registry hole) ──────────────────
def test_every_price_and_relations_series_is_classified():
    """A series in prices/relations with no registry class fails the class
    prior OPEN — the exact bug the coverage reconstruction surfaced
    (britannia/bpcl/dabur). Guard it so a future orphan can't reintroduce it."""
    import json
    import pandas as pd
    from registry import load_registry
    from synth_classes import market_of
    reg = {s["id"] for s in load_registry()}
    cols = pd.read_csv(ROOT / "data" / "prices.csv", index_col=0, nrows=1).columns
    unclassified = [c for c in cols if market_of(c) is None]
    assert unclassified == [], f"unclassified price series: {unclassified}"
    rel = json.loads((ROOT / "data" / "relations.json").read_text())
    rel_series = set(rel.get("series", []))
    assert [s for s in rel_series if market_of(s) is None] == []


def test_class_prior_fails_closed_on_unclassified_driver():
    from synth_classes import driver_admissible
    # a series not in the registry must NOT be admissible as a macro driver
    assert driver_admissible("ghost_unregistered", "sp500") == \
        (False, "unclassified_drives_macro")
    # and a now-registered single name is blocked with the single-name reason
    assert driver_admissible("britannia", "sp500")[0] is False


def test_edge_gate_is_orthogonal_to_adequacy():
    """A sample-adequate family whose Wilson lower bound is below a coin flip
    with against-dominated misses is NO_RELIABLE_EDGE — adequacy != edge."""
    from synth_baserates import EDGE_LB_MIN, edge_finding
    lo_below = {"wilson95": [EDGE_LB_MIN - 0.15, 0.8]}
    lo_above = {"wilson95": [EDGE_LB_MIN + 0.05, 0.9]}
    against = {"faded_against": 6, "faded_flat": 1}
    flat = {"faded_against": 1, "faded_flat": 6}
    assert edge_finding(lo_below, against)["finding"] == "NO_RELIABLE_EDGE"
    assert edge_finding(lo_below, flat)["finding"] == "NO_DEMONSTRATED_EDGE"
    assert edge_finding(lo_above, against)["finding"] == "PROVISIONAL_EDGE"


def test_wilson_interval_uses_cluster_n():
    from synth_baserates import _wilson
    p, lo, hi = _wilson(6, 8)
    assert p == 0.75 and 0.0 <= lo < p < hi <= 1.0
    # smaller n -> wider interval (cluster N must widen it, not raw N)
    _, lo8, hi8 = _wilson(6, 8)
    _, lo40, hi40 = _wilson(30, 40)      # same p, larger n
    assert (hi8 - lo8) > (hi40 - lo40)


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
