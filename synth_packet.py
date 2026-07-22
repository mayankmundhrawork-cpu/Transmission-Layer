"""SYNTH_V2 · S5 — deterministic investigation-assembler (NO LLM).

The bar (acceptance test #4, and the one that matters most now that S5 is an
assembler not a narrator): a competent human — or a mid-tier model — reaches
the same INVESTIGATE / DISMISS call from the packet ALONE, LLM off. If the
packet only becomes decision-ready once Groq runs, intelligence has leaked back
into the model. So everything needed to judge "is this worth my time" is here:
the divergence with its SIGNED shortfall, the reference-class verdict and its
evidence, the news join (or its explicit absence), the channel stability, the
counter-move expectation. Call A later adds only a label the packet implies.

Disposition is capped by the S4 reference-class verdict and the cap is
ARITHMETIC (clamp_disposition), never a request to a model: even a hallucinated
promotion is overridden and logged. S6 may only ever LOWER a disposition.

Run: python synth_packet.py            # assemble + render the golden bovespa LEAD
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

DATA_DIR = Path(__file__).parent / "data"
SYNTH_DIR = DATA_DIR / "synth"

# disposition ordinal — DISMISS < LEAD < OBSERVATION. Only OBSERVATION is
# actionable; a LEAD is "worth a look, not a trade".
DISPOSITION = {"DISMISS": 0, "LEAD": 1, "OBSERVATION": 2}
_INV = {v: k for k, v in DISPOSITION.items()}

# S4 reference-class verdict -> the MAX disposition it permits (the cap table).
VERDICT_CAP = {
    "PROVISIONAL_EDGE": "OBSERVATION",
    "NO_DEMONSTRATED_EDGE": "LEAD",
    "NO_RELIABLE_EDGE": "LEAD",
    "INSUFFICIENT": "LEAD",
}


def clamp_disposition(proposed: str, cap: str) -> tuple[str, bool]:
    """Arithmetic monotonicity: the final disposition can never exceed the cap.
    Returns (final, was_overridden). S6/Call B propose; the CODE clamps — the
    cap is real because it is arithmetic, not a polite instruction. An override
    is logged (a model repeatedly trying to promote NO_RELIABLE_EDGE leads is a
    prompt smell)."""
    pi, ci = DISPOSITION.get(proposed, 0), DISPOSITION.get(cap, 0)
    if pi > ci:
        return cap, True
    return proposed, False


# ── corroboration (deterministic, PIT) ──────────────────────────────────
def _co_movers(prices: pd.DataFrame, driver: str, t: pd.Timestamp,
               neighbours: list, implied_up: bool) -> dict:
    """How broad was the driver's move? Of its correlation neighbours, how many
    moved the SAME direction on day t. A move confirmed across assets has a
    macro cause; a lone move is idiosyncratic — weaker grounds to expect
    transmission."""
    r = prices.pct_change(fill_method=None)
    if t not in r.index:
        return {"checked": 0, "confirmed": 0, "detail": []}
    row = r.loc[t]
    drv_sign = np.sign(row.get(driver, 0.0))
    checked, confirmed, detail = 0, 0, []
    for nb in neighbours[:8]:
        nid = nb["id"] if isinstance(nb, dict) else nb
        if nid not in row or pd.isna(row[nid]):
            continue
        checked += 1
        agree = np.sign(row[nid]) == drv_sign and drv_sign != 0
        confirmed += int(agree)
        detail.append({"id": nid, "ret_pct": round(float(row[nid]) * 100, 2),
                       "confirms": bool(agree)})
    return {"checked": checked, "confirmed": confirmed, "detail": detail}


# ── the question + falsifier (templated from the packet, deterministic) ──
def _the_question(rc: dict, driver: str, targets: list, news: bool,
                  cooling: list, stale: bool) -> str:
    ev = rc.get("evidence", {})
    r05 = ev.get("rate_05", {})
    parts = []
    v = rc["verdict"]
    if v in ("NO_RELIABLE_EDGE", "NO_DEMONSTRATED_EDGE", "INSUFFICIENT"):
        if r05:
            ms = ev.get("miss_split_episodes", {})
            parts.append(
                f"{rc['level'].replace('class_pair ','')} historically does NOT "
                f"reliably transmit (half-close {r05.get('point')} "
                f"{r05.get('wilson95')}, misses "
                f"{ms.get('faded_against','?')}:{ms.get('faded_flat','?')} "
                f"against).")
        else:
            parts.append(f"{rc['level']} is too rare to rate "
                         f"({ev.get('clusters')} episodes).")
    parts.append(f"Does THIS {driver} move implicate {', '.join(targets)} "
                 f"through a mechanism the reference class omits (shared "
                 f"catalyst, exposure, positioning)?")
    against = []
    if not news:
        against.append("no catalyst/news is attached to the driver")
    if cooling:
        against.append(f"the channel to {', '.join(cooling)} is cooling")
    if stale:
        against.append("the driver feed is stale")
    if against:
        parts.append("Working against it: " + "; ".join(against) + ".")
    parts.append("If no such mechanism exists, this is a lead at best — not a "
                 "trade.")
    return " ".join(parts)


def _falsifier(rc: dict, lead_lag: int) -> str:
    ev = rc.get("evidence", {})
    ms = ev.get("miss_split_episodes", {})
    base = (f"Killed if any target moves AGAINST the implied direction beyond "
            f"its own median window move (counter-move), or the {lead_lag}-"
            f"session window closes with the gap unclosed.")
    if ms:
        base += (f" The reference class's misses are "
                 f"{ms.get('faded_against')}:{ms.get('faded_flat')} "
                 f"against-dominated — the base-rate expectation is that it "
                 f"does NOT close.")
    return base


# ── assembler ────────────────────────────────────────────────────────────
def assemble_transmission_packet(pulse: dict, prices: pd.DataFrame,
                                 neighbours: dict, pop: dict | None = None,
                                 prices_stale: bool = False) -> dict:
    """Deterministic InvestigationPacket for a transmission driver_pulse."""
    from synth_baserates import base_rate_record

    driver = pulse["driver"]
    legs = pulse["targets"]
    targets = [l["target"] for l in legs]
    date = pulse["asof"]
    # reference class (class-pair verdict) — legs here share a target class;
    # take the first leg's, note if mixed.
    rc = base_rate_record(driver, targets[0], pop=pop)
    classes = {l.get("target_class") for l in legs}
    rc["mixed_target_classes"] = len(classes) > 1

    cap = VERDICT_CAP.get(rc["verdict"], "LEAD")
    disposition = cap                                  # no LLM: sits at the cap
    cooling = [l["target"] for l in legs if l.get("channel_unstable")]
    news = bool(pulse.get("news_support"))

    corr = _co_movers(prices, driver, pd.Timestamp(date),
                      neighbours.get(driver, []),
                      implied_up=legs[0]["expected_pct"] > 0)

    return {
        "instance": f"{driver} -> {{{', '.join(targets)}}}",
        "asof": date,
        "disposition": disposition,
        "disposition_cap": cap,
        "cap_reason": f"reference-class verdict {rc['verdict']}",
        "divergence": [{
            "target": l["target"], "target_class": l.get("target_class"),
            "beta_pair": l["beta_pair"], "expected_pct": l["expected_pct"],
            "actual_pct": l["actual_pct"], "residual_sigma": l["residual_sigma"],
            "shortfall_sigma": l["shortfall_sigma"],
            "channel_state": l["channel_state"],
            "channel_stability": l.get("channel_stability"),
            "channel_unstable": l.get("channel_unstable"),
            "stability_reasons": l.get("stability_reasons"),
            "window_open": l.get("window_open"),
        } for l in legs],
        "driver_zc": pulse["driver_zc"],
        "driver_class": pulse["driver_class"],
        "driver_stale": pulse.get("driver_stale"),
        "reference_class": rc,
        "corroboration": {
            "news_join": pulse.get("news_support") or None,
            "join_trust": None,
            "cross_asset": corr,
        },
        "the_question": _the_question(
            rc, driver, targets, news, cooling, pulse.get("driver_stale")),
        "falsifier": _falsifier(rc, int(legs[0].get("lead_lag") or 1)),
        "prices_stale": prices_stale,
    }


def render_packet(pkt: dict) -> str:
    L = []
    L.append(f"INVESTIGATION PACKET  [{pkt['disposition']}]  (cap: "
             f"{pkt['disposition_cap']} <- {pkt['cap_reason']})")
    L.append(f"  instance : {pkt['instance']}  @ {pkt['asof']}")
    L.append(f"  driver   : {pkt['driver_class']} move {pkt['driver_zc']:+.1f}z"
             + ("  [FEED STALE]" if pkt.get("driver_stale") else ""))
    L.append("  DIVERGENCE (signed, per target):")
    for d in pkt["divergence"]:
        flag = ""
        if d["channel_unstable"]:
            flag = f"  UNSTABLE-CH [{','.join(d['stability_reasons'] or [])}]"
        openf = " window-open" if d["window_open"] else ""
        L.append(f"    {d['target']:<16} beta {d['beta_pair']:+.2f}  "
                 f"expected {d['expected_pct']:+.2f}%  actual {d['actual_pct']:+.2f}%"
                 f"  shortfall {d['shortfall_sigma']:.2f}s  "
                 f"ch={d['channel_state']}(stab {d['channel_stability']}){flag}{openf}")
    rc = pkt["reference_class"]
    ev = rc.get("evidence", {})
    r05, r10 = ev.get("rate_05", {}), ev.get("rate_10", {})
    L.append(f"  REFERENCE CLASS : {rc['verdict']}  (adequacy "
             f"{rc.get('adequacy')})")
    if r05:
        ms = ev.get("miss_split_episodes", {})
        L.append(f"    evidence: half-close {r05.get('point')} "
                 f"{r05.get('wilson95')} | full-close {r10.get('point')} "
                 f"{r10.get('wilson95')} | N={ev.get('clusters')} episodes "
                 f"(raw:cluster {ev.get('ratio')}:1)")
        L.append(f"    misses: {ms.get('faded_against')} against / "
                 f"{ms.get('faded_flat')} flat")
    L.append(f"    basis: {rc.get('basis','')}")
    c = pkt["corroboration"]
    nj = c["news_join"]
    L.append(f"  CORROBORATION:")
    L.append(f"    news join : {'NONE (no catalyst attached)' if not nj else nj}")
    ca = c["cross_asset"]
    L.append(f"    cross-asset: {ca['confirmed']}/{ca['checked']} neighbours "
             f"moved WITH the driver on the day "
             f"({'broad' if ca['checked'] and ca['confirmed']*2>=ca['checked'] else 'idiosyncratic'})")
    L.append(f"  THE QUESTION:\n    {pkt['the_question']}")
    L.append(f"  FALSIFIER:\n    {pkt['falsifier']}")
    if pkt.get("prices_stale"):
        L.append("  [prices_stale: true]")
    return "\n".join(L)


if __name__ == "__main__":
    from relations import load_relations
    prices = pd.read_csv(SYNTH_DIR / "golden_2026-07-20" / "prices.csv",
                         index_col=0, parse_dates=True).sort_index()
    cands = json.loads((SYNTH_DIR / "golden_2026-07-20" / "candidates.json")
                       .read_text(encoding="utf-8"))
    neigh = load_relations().get("neighbours", {})
    pulses = [c for c in cands["candidates"] if c["kind"] == "driver_pulse"]
    bov = next((p for p in pulses if p["driver"] == "bovespa"), None)
    if bov is None:
        print("no bovespa pulse in golden candidates")
    else:
        pkt = assemble_transmission_packet(bov, prices, neigh)
        print(render_packet(pkt))
