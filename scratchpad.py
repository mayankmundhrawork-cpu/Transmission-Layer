"""Article scratchpad with evidence pinning (v5 feature 4).

Pins carry their evidence: numbers, timestamps, citations, thesis text,
precedent stats. State persists to data/scratchpad.json (same pattern as the
universe state). On Streamlit Cloud the filesystem is EPHEMERAL across
redeploys — the durable artifact is the exported markdown brief; export
before you close. (True cloud persistence via a GitHub-API commit is a
documented later toggle, needs a PAT secret.)

Export produces a structured brief: thesis, evidence with citations,
historical precedent, open questions — ready to paste into an editor.
"""
from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
PAD_JSON = DATA_DIR / "scratchpad.json"


def load_pad() -> dict:
    if PAD_JSON.exists():
        try:
            return json.loads(PAD_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"pins": []}


def save_pad(pad: dict) -> None:
    DATA_DIR.mkdir(exist_ok=True)
    PAD_JSON.write_text(json.dumps(pad, indent=1), encoding="utf-8")


def add_pin(kind: str, topic: str, payload: dict, note: str = "") -> dict:
    """kind: event|series|headline|precedent|source. payload carries evidence."""
    pad = load_pad()
    # dedupe: identical kind+payload fingerprint replaces (refreshes) the pin
    fp = json.dumps([kind, payload.get("id") or payload.get("title")
                     or payload.get("date")], sort_keys=True)
    pad["pins"] = [p for p in pad["pins"] if p.get("fp") != fp]
    pin = {
        "pin_id": uuid.uuid4().hex[:8], "fp": fp,
        "kind": kind, "topic": topic or "general",
        "pinned_at": datetime.now(timezone.utc).isoformat(),
        "note": note, "payload": payload,
    }
    pad["pins"].append(pin)
    save_pad(pad)
    return pin


def set_note(pin_id: str, note: str) -> None:
    pad = load_pad()
    for p in pad["pins"]:
        if p["pin_id"] == pin_id:
            p["note"] = note
    save_pad(pad)


def remove_pin(pin_id: str) -> None:
    pad = load_pad()
    pad["pins"] = [p for p in pad["pins"] if p["pin_id"] != pin_id]
    save_pad(pad)


def clear_pad() -> None:
    save_pad({"pins": []})


# ── export ─────────────────────────────────────────────────────────────
def _fmt_event(p: dict) -> list[str]:
    pl = p["payload"]
    L = [f"### {pl.get('label', 'event')} (score {pl.get('score')}, {pl.get('level')})"]
    th = pl.get("thesis") or {}
    if th.get("mechanism"):
        L.append(f"**Mechanism.** {th['mechanism']}")
    if th.get("one_liner"):
        L.append(f"> {th['one_liner']}")
    if th.get("gap"):
        L.append(f"**Gap.** {th['gap']}")
    for m in pl.get("members", []):
        L.append(f"- {m['id']}: last {m.get('last')}, z20 {m.get('z20')}, "
                 f"1d {m.get('d1_pct')}%  _(as of {pl.get('as_of', '?')})_")
    for r in (th.get("responders") or [])[:5]:
        L.append(f"- watch: **{r['id']}** ({r.get('expect')}) — {r.get('why', '')}")
    return L


def _fmt_precedent(p: dict) -> list[str]:
    pl = p["payload"]
    L = [f"### Precedent · {pl.get('date')} (z-distance {pl.get('distance')})"]
    for rid, s in (pl.get("aftermath") or {}).items():
        L.append(f"- {rid}: +20d median {s.get('median_pct')}% "
                 f"(n={s.get('n')}, hit-rate {s.get('hit_rate_up')})")
    if pl.get("query"):
        L.append(f"- query: `{pl['query']}`")
    return L


def export_markdown() -> str:
    pad = load_pad()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%MZ")
    L = [f"# Research brief — {now}", ""]
    by_topic: dict[str, list[dict]] = {}
    for p in pad["pins"]:
        by_topic.setdefault(p["topic"], []).append(p)
    citations: list[str] = []
    open_qs: list[str] = []
    for topic, pins in by_topic.items():
        L.append(f"## {topic}")
        for p in pins:
            pl = p["payload"]
            if p["kind"] == "event":
                L += _fmt_event(p)
            elif p["kind"] == "precedent":
                L += _fmt_precedent(p)
            elif p["kind"] == "headline":
                L.append(f"- {pl.get('title')} — {pl.get('feed')}, "
                         f"{(pl.get('ts') or '')[:10]}")
                if pl.get("excerpt"):
                    L.append(f"  > {pl['excerpt'][:280]}")
            elif p["kind"] == "series":
                L.append(f"- **{pl.get('id')}**: last {pl.get('last')}, "
                         f"z20 {pl.get('z20')}, 1y-pct {pl.get('pct_1y')} "
                         f"_(as of {pl.get('as_of')})_")
            elif p["kind"] == "source":
                L.append(f"- source: {pl.get('name')} — {pl.get('url')}")
            if p.get("note"):
                L.append(f"  - _note:_ {p['note']}")
                if p["note"].rstrip().endswith("?"):
                    open_qs.append(p["note"])
            if pl.get("citation"):
                citations.append(pl["citation"])
            for c in pl.get("citations", []):
                citations.append(c)
        L.append("")
    if citations:
        L.append("## Citations")
        L += [f"{i+1}. {c}" for i, c in enumerate(dict.fromkeys(citations))]
        L.append("")
    L.append("## Open questions")
    L += [f"- {q}" for q in open_qs] or ["- "]
    return "\n".join(L)


if __name__ == "__main__":
    clear_pad()
    add_pin("event", "test", {"label": "indices · 4 series", "score": 6.75,
                              "level": "red", "as_of": "2026-07-06",
                              "members": [{"id": "dax", "last": 25779.3,
                                           "z20": 3.09, "d1_pct": 0.78}],
                              "thesis": {"mechanism": "test mechanism",
                                         "gap": "test gap"},
                              "citations": ["FTSE story — ET, 2026-07-06. http://x"]},
            note="does the ECB angle hold?")
    print(export_markdown())
    clear_pad()
