"""Board brief — the dashboard's full state as one LLM-ready markdown file.

Assembles everything a writing session needs into data/board_brief.md:
status, events with theses + India transmission + citations, watchlist,
India macro, squawk tape, universe with evidence, open hypotheses and
journal intents, and the article-writing prompt.

Written by every scheduled run (after the overnight pass), so a fresh
Claude conversation can be fed the live board with zero copy-paste.
Optionally mirrors to a GitHub Gist when GIST_TOKEN + GIST_ID are set,
giving a stable public raw URL for auto-fetch.

Run: python brief.py
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).parent / "data"
BRIEF_MD = DATA_DIR / "board_brief.md"

WRITING_PROMPT = """---
## How to use this brief (instruction to the assistant)
You are helping draft a macro article for an audience of Indian market
practitioners. Work ONLY from the data above — never invent numbers.
Priorities: (1) the event-to-price gap — what the news implies that price
has not yet reflected; (2) the transmission chain into Indian instruments,
using the INDIA lines and laggards; (3) historical precedent where given.
A sceptical 'no gap here' is a valid conclusion. Cite specifics (levels,
z-scores, dates) from the brief. The owner's hypotheses and journal intents
show what they are already thinking — engage with them directly."""


def _fmt(v, dp=2):
    try:
        return f"{v:.{dp}f}"
    except (TypeError, ValueError):
        return "n/a"


def build_brief() -> str:
    from engine import build_snapshot
    from events import build_events
    from headlines import recent_items
    from india import india_receivers
    from registry import load_universe
    from relations import laggards_for, load_relations
    from research import event_key, load_bundles
    from thesis import load_theses

    snap = build_snapshot()
    prices = pd.read_csv(DATA_DIR / "prices.csv", index_col=0, parse_dates=True)
    hl = recent_items()
    ev = build_events(snap, prices, hl)
    by_id = {r["id"]: r for r in snap["series"]}
    rel = load_relations()
    theses = load_theses().get("theses", {})
    bundles = load_bundles().get("bundles", {})
    uni = load_universe()

    now = datetime.now(timezone.utc)
    red = sum(1 for r in snap["series"] if r["flag"] == "red")
    amber = sum(1 for r in snap["series"] if r["flag"] == "amber")

    L: list[str] = []
    L.append(f"# Transmission Layer — board brief · {now:%Y-%m-%d %H:%M}Z")
    L.append(f"\ndata as of **{snap.get('last_data_date')}** · "
             f"{len(snap['series'])} series · {red} red / {amber} amber · "
             f"{len(ev['events'])} events surfaced "
             f"({ev['counts'].get('suppressed', 0)} suppressed)")

    # ── events ──────────────────────────────────────────────────────────
    L.append("\n## Events (ranked)")
    if not ev["events"]:
        L.append("None — calm session. That is a valid state.")
    for e in ev["events"]:
        k = event_key([m["id"] for m in e["members"]])
        L.append(f"\n### [{e['level'].upper()} {e['score']}] {e['label']}")
        for m in e["members"]:
            L.append(f"- {m['id']} [{m['market']}]: last {_fmt(m.get('last'))}, "
                     f"z20 {_fmt(m.get('z20'))}, 1d {_fmt(m.get('d1_pct'))}%, "
                     f"{'; '.join(m.get('reasons', []))}")
        t = theses.get(k, {}).get("thesis", {})
        if t.get("mechanism"):
            L.append(f"- **Mechanism**: {t['mechanism']}")
        if t.get("gap"):
            L.append(f"- **Gap**: {t['gap']}")
        if t.get("india_take"):
            L.append(f"- **India take**: {t['india_take']}")
        for r in (t.get("responders") or [])[:5]:
            L.append(f"- Watch next: {r.get('id')} ({r.get('expect')}) — "
                     f"{r.get('status')}; {r.get('why', '')}")
        try:
            ind = india_receivers([m["id"] for m in e["members"]], by_id, rel)
            if ind:
                L.append("- **India receivers**: " + "; ".join(
                    f"{x['id']} (rho {x.get('rho')}, z {x.get('z20')})"
                    for x in ind[:4]))
        except Exception:
            pass
        b = bundles.get(k, {})
        for a in (b.get("articles") or [])[:3]:
            if a.get("citation"):
                L.append(f"- Source: {a['citation']}")
        ana = (b.get("analogues") or {}).get("analogues") or []
        if ana:
            L.append("- Historical analogues: " + ", ".join(
                f"{x['date']} (d={x['distance']})" for x in ana[:3]))

    wl = ev.get("watchlist", [])
    if wl:
        L.append("\n## Watchlist (below surfacing floor)")
        L.append(", ".join(f"{w['label']} ({w['score']})" for w in wl[:12]))

    # ── india macro ─────────────────────────────────────────────────────
    L.append("\n## India macro")
    for sid in ("nifty_50", "nifty_midcap_100", "usd_inr", "goi_10y",
                "india_cpi_yoy", "goi_ust_spread", "midcap_largecap_ratio"):
        r = by_id.get(sid)
        if r and r.get("last") is not None:
            L.append(f"- {sid}: {_fmt(r['last'], 4)} (1d {_fmt(r.get('d1_pct'))}%, "
                     f"z20 {_fmt(r.get('z20'))}, flag {r['flag']})")
    try:
        from release_calendar import build_calendar
        cal = build_calendar()
        nxt = [r for r in cal["upcoming"] if r["market"] == "INDIA"][:4]
        L.append("- Next India prints: " + " · ".join(
            f"{r['name']} T-{r['days_until']}d" for r in nxt))
    except Exception:
        pass

    # ── squawk tape ─────────────────────────────────────────────────────
    try:
        from squawk import load_squawk
        items = load_squawk().get("items", [])[:12]
        if items:
            L.append("\n## Squawk (latest wire headlines)")
            for it in items:
                L.append(f"- [{(it.get('ts') or '')[:16]}Z] {it['text'][:180]}")
    except Exception:
        pass

    # ── universe ────────────────────────────────────────────────────────
    members = uni.get("members", {})
    if members:
        L.append("\n## News-tracked universe (why each is watched)")
        for sym, m in sorted(members.items(), key=lambda kv: -kv[1].get("score", 0)):
            ev0 = (m.get("evidence") or [{}])[0]
            L.append(f"- {sym} ({m.get('name', '')[:30]}) score {m.get('score', 0):.1f} — "
                     f"\"{ev0.get('title', '')[:90]}\"")

    # ── owner's thinking ────────────────────────────────────────────────
    try:
        from journal import load_journal
        j = load_journal()
        hyps = [h for h in j.get("hypotheses", []) if not h.get("archived")]
        trades = [t for t in j.get("trades", []) if t.get("status") != "closed"]
        if hyps:
            L.append("\n## Open hypotheses")
            for h in hyps[:8]:
                L.append(f"- {h.get('text', '')[:200]}")
                verdict = (h.get("evaluation") or {}).get("verdict")
                if verdict:
                    L.append(f"  - LLM evaluation verdict: {verdict}")
        if trades:
            L.append("\n## Journal — open trade intents")
            for t in trades[:8]:
                L.append(f"- {t.get('instrument')} {t.get('side')} @ "
                         f"{t.get('level', '?')} — {t.get('rationale', '')[:140]}")
    except Exception:
        pass

    L.append("\n" + WRITING_PROMPT)
    return "\n".join(L)


def publish_gist(text: str) -> bool:
    """Optional mirror to a Gist (stable public raw URL for auto-fetch).
    Needs GIST_TOKEN (gist-scoped PAT) + GIST_ID. Silently skipped if unset."""
    token = (os.environ.get("GIST_TOKEN") or "").strip()
    gid = (os.environ.get("GIST_ID") or "").strip()
    if not token or not gid:
        return False
    import requests
    try:
        r = requests.patch(
            f"https://api.github.com/gists/{gid}",
            headers={"Authorization": f"Bearer {token}",
                     "Accept": "application/vnd.github+json"},
            json={"files": {"board_brief.md": {"content": text}}}, timeout=20)
        r.raise_for_status()
        return True
    except Exception as e:
        print(f"  WARN gist publish failed: {str(e)[:120]}", file=sys.stderr)
        return False


def main() -> int:
    text = build_brief()
    BRIEF_MD.write_text(text, encoding="utf-8")
    gist = publish_gist(text)
    print(f"brief: {len(text)} chars -> {BRIEF_MD.name}"
          f"{' + gist mirror' if gist else ' (gist mirror off)'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
