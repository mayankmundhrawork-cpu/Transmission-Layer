"""Transmission-chain theses per event (v5 feature 1). ZERO-BUDGET.

For each surfaced event, produce a written first-pass thesis:
  mechanism -> which tracked instruments should respond (and whether they
  have, from relations.laggards_for) -> the event-to-price gap (or an honest
  "no gap").

LLM routing (settings.get_llm_backend): FREE OpenAI-compatible endpoints
only — Groq free tier or OpenRouter :free models, via plain requests. No key
configured -> the rule-based skeleton renders instead (laggards + analogues
are pure math and always present). No paid plan exists anywhere in this path.

Caching: thesis keyed on (members + quantized z + news ids); an unchanged
event across runs never re-calls the API. State: data/theses.json.

Run: python thesis.py
"""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

from research import event_key
from settings import THESIS_MAX_PER_RUN, THESIS_MAX_TOKENS, get_llm_backend

DATA_DIR = Path(__file__).parent / "data"
THESES_JSON = DATA_DIR / "theses.json"

SYSTEM_PROMPT = """You are the first-pass macro analyst for a professional's own research
terminal. Your written output will be edited by the owner and published under
THEIR name, so write like a sceptical practitioner drafting for himself:
mechanism-first, specific, numerate, no hedging boilerplate, no
"it remains to be seen", no disclaimers. British or Indian market vocabulary
is fine. If the evidence does not support a gap, say "No gap: ..." plainly —
a quiet conclusion is a valid output. Never invent numbers not given to you.

The owner writes for INDIAN market practitioners: always close the loop to
the Indian expression of the move, using the INDIA TRANSMISSION CANDIDATES
supplied (never invent Indian instruments not listed).

Return STRICT JSON only:
{"mechanism": "<2-4 sentences: why this move propagates, through what channel>",
 "responders": [{"id": "<series id>", "expect": "<up|down>",
                 "status": "<already moved|not yet - watch>", "why": "<1 line>"}],
 "gap": "<the specific event-to-price gap, or 'No gap: <reason>'>",
 "india_take": "<1-2 sentences: the Indian instrument(s) that express this,
                and whether they have reacted yet>",
 "confidence": "<low|medium|high>",
 "one_liner": "<a single quotable sentence for the article>"}"""


def _quantize(z) -> str:
    return "na" if z is None else f"{round(z * 2) / 2:+.1f}"


THESIS_SCHEMA_V = "v2"  # bump to invalidate cached theses on schema change


def thesis_key(event: dict) -> str:
    parts = [THESIS_SCHEMA_V]
    parts += [m["id"] + _quantize(m.get("z20")) for m in event["members"]]
    parts += sorted(n["title"][:40] for n in event.get("news", []))
    return hashlib.sha1("|".join(sorted(parts)).encode()).hexdigest()[:12]


def _skeleton(event: dict, laggards: list[dict], analogues: dict,
              india: list[dict] | None = None) -> dict:
    """Rule-based thesis when no LLM key is configured — pure math, honest."""
    responders = [{
        "id": l["id"],
        "expect": "co-move" if (l["rho"] or 0) > 0 else "inverse",
        "status": "not yet - watch",
        "why": f"rho {l['rho']} vs {l['via']}" +
               (f", historically leads by {l['lead_lag']}d" if l.get("leads") else ""),
    } for l in laggards]
    ana_line = ""
    if analogues.get("analogues"):
        best = analogues["analogues"][0]
        ana_line = (f"Nearest historical analogue: {best['date']} "
                    f"(z-distance {best['distance']}).")
    try:
        from india import format_receivers
        india_take = format_receivers(india or []) or "No exposed Indian receivers above the correlation floor."
    except Exception:
        india_take = ""
    return {
        "mechanism": f"{event['label']}: correlated cluster flagged by the "
                     f"engine. Mechanism narrative unassessed (LLM off). {ana_line}",
        "responders": responders,
        "gap": "Unassessed (LLM off) — laggard list above is the live math.",
        "india_take": india_take,
        "confidence": "low",
        "one_liner": "",
    }


def _llm_call(backend: dict, user_prompt: str,
              system: str | None = None) -> dict | None:
    try:
        r = requests.post(backend["url"], timeout=45, headers={
            "Authorization": f"Bearer {backend['key']}",
            "Content-Type": "application/json",
        }, json={
            "model": backend["model"],
            "max_tokens": THESIS_MAX_TOKENS,
            "temperature": 0.4,
            "messages": [{"role": "system", "content": system or SYSTEM_PROMPT},
                         {"role": "user", "content": user_prompt}],
        })
        r.raise_for_status()
        text = r.json()["choices"][0]["message"]["content"]
        start, end = text.find("{"), text.rfind("}")
        return json.loads(text[start:end + 1])
    except Exception as e:
        print(f"  WARN llm thesis failed ({backend['name']}): {str(e)[:140]}",
              file=sys.stderr)
        return None


def _compose_prompt(event: dict, laggards: list[dict], analogues: dict,
                    bundle: dict, india: list[dict] | None = None) -> str:
    L = [f"EVENT: {event['label']} (level {event['level']}, score {event['score']})"]
    L.append("MEMBERS (z20 = 20-day z-score, d1 = 1-day %):")
    for m in event["members"]:
        L.append(f"  {m['id']} [{m['market']}] z20={m.get('z20')} "
                 f"d1={m.get('d1_pct')} last={m.get('last')} "
                 f"reasons={'; '.join(m.get('reasons', []))}")
    if laggards:
        L.append("CORRELATED INSTRUMENTS THAT HAVE NOT MOVED (live math):")
        for l in laggards:
            L.append(f"  {l['id']}: rho={l['rho']} vs {l['via']}, own z20={l['z20']}"
                     + (f", historically leads by {l['lead_lag']}d" if l.get("leads") else ""))
    if analogues.get("analogues"):
        L.append("HISTORICAL ANALOGUES (nearest z-vector dates) AND WHAT FOLLOWED:")
        for a in analogues["analogues"][:3]:
            L.append(f"  {a['date']} (distance {a['distance']})")
        for rid, r in list(analogues.get("aftermath", {}).items())[:4]:
            s = r.get("stats", {}).get("+20d")
            if s:
                L.append(f"  aftermath {rid}: +20d median {s['median_pct']}% "
                         f"(n={s['n']}, hit-rate-up {s['hit_rate_up']})")
    if india:
        L.append("INDIA TRANSMISSION CANDIDATES (live math — use these for india_take):")
        for r in india:
            L.append(f"  {r['id']}: rho={r['rho']} via {r['via']}"
                     + (f", leads {r['lead_lag']}d" if r.get("leads") else "")
                     + f", z20={r['z20']} ({'reacted' if r['reacted'] else 'quiet'})")
    arts = [a for a in bundle.get("articles", []) if a.get("excerpt")]
    if arts:
        L.append("MOTIVATING NEWS (excerpts):")
        for a in arts[:3]:
            L.append(f"  [{a['feed']}] {a['title']}")
            L.append(f"    {a['excerpt'][:400]}")
    elif event.get("news"):
        L.append("MOTIVATING HEADLINES (no article text available):")
        for n in event["news"][:3]:
            L.append(f"  [{n['feed']}] {n['title']}")
    L.append("\nWrite the JSON thesis. Identify the event-to-price gap if one "
             "genuinely exists; otherwise say 'No gap' and why.")
    return "\n".join(L)


def load_theses() -> dict:
    if THESES_JSON.exists():
        try:
            return json.loads(THESES_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"theses": {}, "ledger": {"llm_calls_total": 0}}


def build_theses(events: list[dict], laggards_by_key: dict,
                 analogues_by_key: dict, bundles: dict,
                 india_by_key: dict | None = None) -> dict:
    india_by_key = india_by_key or {}
    state = load_theses()
    backend = get_llm_backend()
    calls = 0
    kept, generated, skeletons = 0, 0, 0

    live_keys = set()
    for e in events:
        ekey = event_key([m["id"] for m in e["members"]])
        tkey = thesis_key(e)
        live_keys.add(ekey)
        cur = state["theses"].get(ekey)
        if cur and cur.get("tkey") == tkey and cur.get("model") != "skeleton":
            kept += 1
            continue  # unchanged event, real thesis cached — never re-spend
        laggards = laggards_by_key.get(ekey, [])
        analogues = analogues_by_key.get(ekey, {})
        bundle = bundles.get("bundles", {}).get(ekey, {})
        india = india_by_key.get(ekey, [])
        thesis, model = None, "skeleton"
        if backend and calls < THESIS_MAX_PER_RUN:
            # (a cached skeleton also lands here when a key appears — upgrade)
            calls += 1
            thesis = _llm_call(backend, _compose_prompt(e, laggards, analogues,
                                                        bundle, india))
            if thesis:
                model = backend["model"]
                generated += 1
        if thesis is None:
            thesis = _skeleton(e, laggards, analogues, india)
            skeletons += 1
        state["theses"][ekey] = {
            "tkey": tkey, "label": e["label"], "level": e["level"],
            "score": e["score"], "model": model,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "laggards": laggards,
            "thesis": thesis,
        }

    # prune theses for events no longer live (keep a small trail)
    stale = [k for k in state["theses"] if k not in live_keys]
    for k in sorted(stale, key=lambda k: state["theses"][k].get("generated_at", ""))[:-20]:
        del state["theses"][k]

    state["ledger"]["llm_calls_total"] = state["ledger"].get("llm_calls_total", 0) + calls
    state["ledger"]["last_run"] = {
        "at": datetime.now(timezone.utc).isoformat(),
        "backend": backend["name"] if backend else "none",
        "llm_calls": calls, "generated": generated,
        "skeletons": skeletons, "cache_kept": kept,
        "cost_usd": 0.0,  # free endpoints only, by constraint
    }
    THESES_JSON.write_text(json.dumps(state), encoding="utf-8")
    return state


if __name__ == "__main__":
    import pandas as pd
    from engine import build_snapshot
    from events import build_events
    from headlines import recent_items
    from patterns import analogues_for_event
    from relations import laggards_for, load_relations
    from research import load_bundles

    snap = build_snapshot()
    prices = pd.read_csv(DATA_DIR / "prices.csv", index_col=0, parse_dates=True)
    ev = build_events(snap, prices, recent_items())
    by_id = {r["id"]: r for r in snap["series"]}
    rel = load_relations()
    lag_by, ana_by = {}, {}
    for e in ev["events"]:
        mids = [m["id"] for m in e["members"]]
        k = event_key(mids)
        lag_by[k] = laggards_for(mids, by_id, rel)
        ana_by[k] = analogues_for_event(mids, prices)
    state = build_theses(ev["events"], lag_by, ana_by, load_bundles())
    lr = state["ledger"]["last_run"]
    print(f"theses: backend={lr['backend']} llm={lr['llm_calls']} "
          f"generated={lr['generated']} skeleton={lr['skeletons']} kept={lr['cache_kept']}")
    for k, t in list(state["theses"].items())[:3]:
        print(f"\n[{t['level']}] {t['label']} ({t['model']})")
        th = t["thesis"]
        print(f"  mechanism: {th['mechanism'][:180]}")
        print(f"  gap: {th['gap'][:180]}")
        for r in th.get("responders", [])[:4]:
            print(f"  responder: {r['id']} {r.get('expect')} — {r.get('status')}")
