"""SYNTH_V2 · S4 — base-rate reconstruction (matching rule + outcome).

The setup IS the live detector predicate re-run on strictly-prior data. For
each historical driver-event date t this module rebuilds the channel state
POINT-IN-TIME (synth_channels.build_channels on prices.loc[:t] — never today's
channels.json, section A of S4_METHODOLOGY.md) and calls the unchanged
synth_detect.detect_transmission_gaps on prices.loc[:t]. Whatever it returns is
the reconstructed trigger population — the same object the live board emits,
graded on data it could actually have seen at t.

The OUTCOME ("did the gap close?") is the only forward-looking quantity and is
never a trigger input: from t+1..t+K (K = clamp(lead_lag,5,15)) the target's
cumulative return is projected onto the implied direction; CLOSED = it catches
>= CLOSE_FRAC of the outstanding gap (both 0.5 and 1.0 stored), first-touch,
with time-to-touch. A material against-move separates FADED_AGAINST from
FADED_FLAT.

THIS FILE COMPUTES NO HEADLINE HIT RATE YET. `python synth_baserates.py` runs
the reconstruction AUDIT: trigger population + resolved outcomes on a few
pairs, so the outcome definition can be checked on the rows before any rate is
aggregated (owner gate).
"""
from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd

DATA_DIR = Path(__file__).parent / "data"

K_MIN, K_MAX = 5, 15          # resolution horizon clamp (sessions)
CLOSE_FRACS = (0.5, 1.0)      # headline 0.5, purist 1.0 — store both
AGAINST_FRAC = 0.5            # against-move this large => FADED_AGAINST
CENSOR_MIN_FRAC = 0.6         # need this fraction of K valid forward obs to
#                               call a FADE; else the window is right-censored
#                               (matrix edge or data gaps) — never a fade.
#                               A close that already happened still counts.


def driver_event_dates(prices: pd.DataFrame, driver: str) -> list:
    """Every session t where the live market adapter would have fired on the
    driver, judged PIT (its own |zc| history strictly before t)."""
    from conditional import zc_frame
    from synth_events import _move_event
    if driver not in prices.columns:
        return []
    zc = zc_frame(prices, [driver])
    if driver not in zc.columns:
        return []
    s = zc[driver].dropna()
    r = prices[driver].pct_change(fill_method=None)
    out = []
    for pos in range(len(s)):
        e = _move_event(driver, s, r, pos)
        if e is not None:
            out.append((s.index[pos], e))
    return out


def resolve_outcome(prices: pd.DataFrame, trig: dict) -> dict:
    """Grade a trigger forward. Outstanding gap = expected - realised-at-t;
    caught(k) = target cum return t+1..t+k projected onto the implied dir."""
    tgt = trig["target"]
    t = pd.Timestamp(trig["asof"])
    lead = int(trig.get("lead_lag") or 1)
    K = int(min(max(lead, K_MIN), K_MAX))
    idx = prices.index
    if t not in idx or tgt not in prices.columns:
        return {"outcome": "NO_DATA", "K": K}
    pos = idx.get_loc(t)
    avail = len(idx) - 1 - pos                       # sessions after t on matrix
    fwd = prices[tgt].pct_change(fill_method=None).iloc[pos + 1:pos + 1 + K]
    expected = trig["expected_pct"] / 100.0
    realized0 = trig["actual_pct"] / 100.0
    gap = expected - realized0                      # outstanding implied move
    gap_mag = abs(gap)
    idir = trig["implied_dir"]
    cum, c05, c10, against, path = 1.0, None, None, False, []
    for k, r in enumerate(fwd.to_numpy(), 1):
        if np.isnan(r):
            path.append(None)
            continue
        cum *= (1.0 + r)
        caught = float((cum - 1.0) * idir)
        path.append(round(caught * 100, 3))
        if gap_mag > 0:
            if c05 is None and caught >= CLOSE_FRACS[0] * gap_mag:
                c05 = k
            if c10 is None and caught >= CLOSE_FRACS[1] * gap_mag:
                c10 = k
            if caught <= -AGAINST_FRAC * gap_mag:
                against = True
    n = sum(1 for p in path if p is not None)
    # right-censoring (point B applied to history): a window that ran off the
    # matrix (avail<K) or is too sparse (n<0.6K) cannot be called a fade — we
    # don't know if it would have closed. A close that already fired counts.
    censored = min(avail, K) < K or n < CENSOR_MIN_FRAC * K
    outcome = ("CLOSED" if c05 else
               "CENSORED" if censored else
               "FADED_AGAINST" if against else
               "FADED_FLAT")
    return {"K": K, "window_n": n, "avail_sessions": int(avail),
            "gap_pct": round(gap * 100, 3),
            "closed_05": bool(c05), "closed_10": bool(c10),
            "ttt_05": c05, "ttt_10": c10, "outcome": outcome,
            "caught_path_pct": path}


def _filter_relations(relations: dict, drivers: set) -> dict:
    """Only pairs whose leader (driver) is in `drivers` — keeps the PIT
    channel rebuild cheap for a targeted reconstruction."""
    pairs = [p for p in relations.get("pairs", [])
             if p.get("leader") in drivers or p.get("follower") in drivers]
    return {**relations, "pairs": pairs}


def reconstruct(prices: pd.DataFrame, drivers: list, relations: dict,
                full_floor: bool = True) -> list:
    """Reconstructed trigger population for `drivers` with forward outcomes.
    full_floor=True rebuilds ALL channels PIT so the cross-sectional strength
    floor is exact; False restricts to the drivers' pairs (faster, floor
    approximate — only safe for strong audit pairs)."""
    from synth_channels import build_channels
    from synth_detect import detect_transmission_gaps

    rel = relations if full_floor else _filter_relations(relations, set(drivers))
    by_date: dict[pd.Timestamp, list] = defaultdict(list)
    for drv in drivers:
        for t, e in driver_event_dates(prices, drv):
            by_date[t].append(e)

    keep = ("id", "kind", "asof", "driver", "target", "driver_class",
            "target_class", "beta_pair", "expected_pct", "actual_pct",
            "residual_sigma", "shortfall_sigma", "gap_bar_sigma", "implied_dir",
            "channel_state", "channel_rho", "channel_stability", "lead_lag")
    triggers = []
    for t in sorted(by_date):
        pt = prices.loc[:t]
        ch = build_channels(pt, relations=rel, changepoints=False,
                            persist=False)["channels"]
        gaps = detect_transmission_gaps(pt, ch, by_date[t], [])
        for g in gaps:
            if g["driver"] not in drivers:
                continue
            row = {k: g[k] for k in keep}
            row.update(resolve_outcome(prices, g))
            row["beta_pit"] = g["beta_pair"]     # PIT beta used (section A)
            triggers.append(row)
    return triggers


# ── audit (owner gate: check CLOSED-calling before any rate) ─────────────
def _counter_move_exclusion_demo(prices, relations):
    """Show the ruling-6 counter-move logic refusing to score dyn_gs->dyn_mu on
    the Goldman event date: detect emits NO trigger, and the target's forward
    path runs AWAY from the implied direction — a false laggard correctly
    never counted."""
    from synth_channels import build_channels
    from synth_detect import detect_transmission_gaps
    drv, tgt = "dyn_gs", "dyn_mu"
    evs = driver_event_dates(prices, drv)
    if not evs:
        return
    t, e = evs[-1]
    pt = prices.loc[:t]
    ch = build_channels(pt, relations=_filter_relations(relations, {drv}),
                        changepoints=False, persist=False)["channels"]
    gaps = detect_transmission_gaps(pt, ch, [e], [])
    emitted = any(g["target"] == tgt for g in gaps)
    # what the trigger WOULD have claimed, and where the target actually went
    from synth_channels import pair_beta_series
    r = prices.pct_change(fill_method=None)
    beta = pair_beta_series(r, drv, tgt).reindex(prices.index)
    pos = prices.index.get_loc(t)
    exp = float(beta.iloc[pos] * r[drv].iloc[pos]) * 100
    day0 = float(r[tgt].iloc[pos]) * 100
    fwd5 = float((1 + r[tgt].iloc[pos + 1:pos + 6].dropna()).prod() - 1) * 100
    print(f"\nCOUNTER-MOVE EXCLUSION (ruling 6) — {drv} -> {tgt} @ {t:%Y-%m-%d}")
    print(f"  implied (beta*drv_ret) = {exp:+.2f}%  | target day0 = {day0:+.2f}%"
          f"  | target next-5d = {fwd5:+.2f}%")
    print(f"  detector emitted a trigger for this pair: {emitted}  "
          f"(expected: False)")
    print(f"  -> target moved HARD against the implied +{exp:.0f}%; it is the "
          f"target's own story, not a laggard. Never scored as a close.")


def audit():
    prices = pd.read_csv(DATA_DIR / "prices.csv", index_col=0,
                         parse_dates=True).sort_index()
    from relations import load_relations
    rel = load_relations()

    drivers = ["sp500", "stoxx_50", "dax", "nikkei_225", "bovespa", "cac_40",
               "brent", "wti", "dxy", "ust_10y", "india_vix", "hy_oas"]
    print(f"reconstruction audit over {prices.index.min():%Y-%m-%d}.."
          f"{prices.index.max():%Y-%m-%d}  drivers={drivers}")
    trg = reconstruct(prices, drivers, rel, full_floor=False)
    graded = [t for t in trg if t["outcome"] in
              ("CLOSED", "FADED_FLAT", "FADED_AGAINST")]
    censored = [t for t in trg if t["outcome"] == "CENSORED"]
    n_closed = sum(t["closed_05"] for t in graded)
    print(f"triggers reconstructed: {len(trg)} | gradeable: {len(graded)} "
          f"| right-censored (excluded): {len(censored)} | CLOSED@0.5: "
          f"{n_closed} | (NO rate computed — audit only)")

    def show(t):
        print(f"  {t['driver']:>10} -> {t['target']:<16} {t['asof']} "
              f"K={t['K']:>2} exp={t['expected_pct']:+6.2f}% "
              f"day0={t['actual_pct']:+6.2f}% gap={t['gap_pct']:+6.2f}% "
              f"short={t['shortfall_sigma']:.2f}s n={t['window_n']} "
              f"{t['outcome']:13} ttt05={t['ttt_05']} ttt10={t['ttt_10']} "
              f"path%={t['caught_path_pct']}")

    closes = sorted((t for t in graded if t["closed_05"]),
                    key=lambda t: (t["ttt_05"] or 99))
    print("\nGENUINE CLOSES (first-touch early = clean transmission):")
    for t in closes[:3]:
        show(t)
    near = [t for t in closes if t["ttt_05"] and t["ttt_05"] >= t["K"] - 1]
    print("\nFIRST-TOUCH LATE IN THE WINDOW (drift warning — ttt near K):")
    for t in (near[:2] or [None]):
        show(t) if t else print("  (none — this macro set has short "
                                "lead-lags so K floored at 5)")
    fades = [t for t in graded if not t["closed_05"]]
    print("\nFADES (full window available, target did NOT close):")
    for t in fades[:3]:
        show(t)
    print("\nRIGHT-CENSORED (near matrix edge / too sparse — NOT graded as "
          "fades; incl. the golden-day bovespa legs):")
    for t in censored[:4]:
        show(t)

    _counter_move_exclusion_demo(prices, rel)


if __name__ == "__main__":
    audit()
