"""SYNTH_V2 · S7 — ranked output + copy-packet (the shareable artifact).

Ties the whole pipeline together into the object a practitioner actually uses:
for each candidate on the dispositioned board — assemble the packet (S5),
classify (Call A), gate (S6 clamp), articulate (Call B, INVESTIGATE only), and
render a COPY-PACKET: a clean markdown block ready to paste into notes or a
Substack draft. DISMISS candidates drop to a dismissed list; the surfaced board
keeps INVESTIGATE and (hedged) INSUFFICIENT_CONTEXT cards, tier order preserved.

LLM-OFF by default: with `client=None` the board uses `implied_classification`
and each packet's own deterministic question + falsifier — fully usable, the
baseline condition. A real client only sharpens phrasing and prunes noise; it
never manufactures a card the scaffold couldn't.

Run: python synth_output.py [data_dir]     # LLM-off board on the golden snapshot
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).parent / "data"
SYNTH_DIR = DATA_DIR / "synth"
BOARD_JSON = SYNTH_DIR / "board.json"


def _assemble(cand: dict, prices, neighbours, all_cands):
    from synth_packet import (assemble_move_packet, assemble_news_packet,
                              assemble_transmission_packet)
    k = cand["kind"]
    if k == "driver_pulse":
        return assemble_transmission_packet(cand, prices, neighbours)
    if k == "news_no_move":
        return assemble_news_packet(cand, all_cands)
    if k == "move_no_news":
        return assemble_move_packet(cand)
    return None


def _copy_packet(cand, packet, call_a, card) -> str:
    """The paste-ready markdown block. Always cites the reference-class verdict
    (or NOT_APPLICABLE + why) and always ends on a checkable falsifier — the
    reader can never mistake a lead for a thesis."""
    disp = card["final_disposition"]
    L = [f"### [{disp}] {packet['instance']}  ({packet['asof']})",
         f"*{card['headline']}*", ""]
    k = cand["kind"]
    if k == "driver_pulse":
        legs = ", ".join(f"{d['target']} (short {d['shortfall_sigma']:.1f}s"
                         f"{', cooling' if d['channel_unstable'] else ''})"
                         for d in packet["divergence"])
        L.append(f"- **Divergence**: {packet['driver_class']} driver "
                 f"{packet['driver_zc']:+.1f}z -> {legs}")
        rc = packet["reference_class"]
        ev = rc.get("evidence", {})
        r5 = ev.get("rate_05", {})
        L.append(f"- **Reference class**: {rc['verdict']} — half-close "
                 f"{r5.get('point')} {r5.get('wilson95')}, misses "
                 f"{ev.get('miss_split_episodes', {}).get('faded_against','?')} "
                 f"against")
        L.append(f"- **Catalyst**: "
                 + ("none joined" if not packet["corroboration"]["news_join"]
                    else "news attached"))
    elif k == "news_no_move":
        d = packet["divergence"]
        L.append(f"- **Divergence**: {d['n_headlines']} headlines (intensity "
                 f"p{d['intensity_pctile']}), price zc {d['zc']:+.2f} vs median "
                 f"{d['own_median_abs_zc']}")
        L.append(f"- **Reference class**: {packet['reference_class']['verdict']} "
                 f"(catalyst-vs-price; unrated)")
        cq = packet["corroboration"]["complex_co_quiet"]
        L.append(f"- **Corroboration**: complex co-quiet — "
                 + (", ".join(cq) if cq else "single series"))
    elif k == "move_no_news":
        d = packet["divergence"]
        L.append(f"- **Divergence**: {d['series']} {d['ret_1d_pct']}% "
                 f"({d['zc']:+.1f}z), no catalyst joined")
        L.append(f"- **Explanation search**: join-trust "
                 f"{packet['explanation_search']['join_trust']} — "
                 + ("confident no-news" if (packet['explanation_search']['join_trust'] or 0) >= 0.8
                    else "LOW-RECALL maybe (check join-miss log)"))
    L += ["", f"- **Triage**: {call_a}",
          f"- **Question**: {card['question']}",
          f"- **Falsifier**: {card['falsifier']}",
          f"- _articulation: {card['source']}"
          + (f" (fell back: {card['reason']})" if card.get("reason") else "")
          + "_"]
    return "\n".join(L)


def build_board(data_dir=None, client=None, out_path=None,
                candidates_state=None, prices_df=None, persist=True) -> dict:
    """`candidates_state` + `prices_df` let the in-app tick build a board from
    an in-memory live pipeline with no file I/O (persist=False)."""
    from relations import load_relations
    from synth_articulate import articulate
    from synth_classify import classify, implied_classification
    from synth_gate import gate

    base = Path(data_dir) if data_dir else SYNTH_DIR
    if candidates_state is None:
        cfile = (base / "candidates.json") if (base / "candidates.json").exists() \
            else SYNTH_DIR / "candidates.json"
        candidates_state = json.loads(cfile.read_text(encoding="utf-8"))
    all_cands = candidates_state["candidates"]
    ranked = candidates_state.get("ranked", [])
    if prices_df is not None:
        prices = prices_df
    else:
        pfile = (base / "prices.csv") if (base / "prices.csv").exists() \
            else DATA_DIR / "prices.csv"
        prices = pd.read_csv(pfile, index_col=0, parse_dates=True).sort_index()
    neighbours = load_relations().get("neighbours", {})

    surfaced, dismissed = [], []
    for cand in ranked:
        packet = _assemble(cand, prices, neighbours, all_cands)
        if packet is None:
            continue
        call_a = (classify(packet, client)["classification"] if client
                  else implied_classification(packet))
        g = gate(packet["disposition"], call_a, instance=packet["instance"],
                 log=client is not None)
        art = articulate(packet, call_a, client) if client else \
            _scaffold_card(packet, call_a)
        card = {**g, **art}
        entry = {"kind": cand["kind"], "tier": cand.get("tier"),
                 "instance": packet["instance"],
                 "final_disposition": g["final_disposition"],
                 "call_a": call_a, "clamped": g["clamped"],
                 "copy_packet": _copy_packet(cand, packet, call_a, card)}
        (surfaced if g["surfaced"] else dismissed).append(entry)

    state = {"data_date": prices.index.max().strftime("%Y-%m-%d"),
             "llm": bool(client),
             "surfaced": surfaced, "dismissed": dismissed}
    if persist:
        outp = Path(out_path) if out_path else BOARD_JSON
        outp.parent.mkdir(parents=True, exist_ok=True)
        outp.write_text(json.dumps(state), encoding="utf-8")
    return state


def _scaffold_card(packet, call_a):
    """LLM-off card: the packet's own question + falsifier verbatim."""
    return {"articulated": False, "source": "scaffold",
            "headline": f"{packet.get('disposition')}: {packet.get('instance')}",
            "question": packet.get("the_question"),
            "falsifier": packet.get("falsifier"),
            "reason": "llm_off", "cited_fields": []}


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "data/synth/golden_2026-07-20"
    st = build_board(src)
    print(f"BOARD (LLM-off) data {st['data_date']} — "
          f"{len(st['surfaced'])} surfaced, {len(st['dismissed'])} dismissed\n")
    for e in st["surfaced"]:
        print(e["copy_packet"])
        print()
    if st["dismissed"]:
        print("--- DISMISSED (Call A) ---")
        for e in st["dismissed"]:
            print(f"  [{e['final_disposition']}] {e['instance']} "
                  f"(ref via reference class -> {e['call_a']})")
