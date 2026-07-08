"""Hypotheses & trading journal (v6). No broker/demat API by design.

Two record types, one state file (data/journal.json):

  hypothesis — an idea jotted on the board, optionally evaluated by the free
               LLM (structured critique: mechanism check, what would confirm/
               refute, which tracked instruments express it). The evaluation
               is on-demand (user-clicked), one free call per click.

  trade      — a manual journal entry (instrument, side, level, rationale),
               linked to the board context that motivated it (event/thesis/
               hypothesis id). This is the groundwork for the future broker
               integration: the schema records intent + rationale now, fills
               can attach later.

Export renders a markdown journal ready for the article workflow.
"""
from __future__ import annotations

import json
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
JOURNAL_JSON = DATA_DIR / "journal.json"

EVAL_PROMPT = """You are a sceptical macro editor reviewing a practitioner's hypothesis for an
article about INDIAN markets. Do not flatter. Assess mechanism plausibility,
name what data would CONFIRM and what would REFUTE it, and which instruments
from the supplied tracked list express it. If untestable or vague, say so.

Return STRICT JSON:
{"verdict": "<plausible|weak|untestable>",
 "mechanism_check": "<2-3 sentences>",
 "confirming": "<the data/print that would confirm>",
 "refuting": "<the data/print that would refute>",
 "instruments": ["<ids from the tracked list only>"],
 "sharpened": "<a tighter one-sentence restatement of the hypothesis>"}"""


def load_journal() -> dict:
    if JOURNAL_JSON.exists():
        try:
            return json.loads(JOURNAL_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"hypotheses": [], "trades": []}


def save_journal(j: dict) -> None:
    DATA_DIR.mkdir(exist_ok=True)
    JOURNAL_JSON.write_text(json.dumps(j, indent=1), encoding="utf-8")


def add_hypothesis(text: str, context: str = "") -> dict:
    j = load_journal()
    h = {"id": uuid.uuid4().hex[:8],
         "ts": datetime.now(timezone.utc).isoformat(),
         "text": text.strip(), "context": context, "evaluation": None}
    j["hypotheses"].insert(0, h)
    save_journal(j)
    return h


def evaluate_hypothesis(hid: str, tracked_ids: list[str],
                        board_context: str = "") -> dict | None:
    """One free-LLM call, user-initiated. Returns the evaluation or None."""
    from settings import get_llm_backend
    from thesis import _llm_call
    backend = get_llm_backend()
    j = load_journal()
    h = next((x for x in j["hypotheses"] if x["id"] == hid), None)
    if h is None:
        return None
    if backend is None:
        h["evaluation"] = {"verdict": "unassessed",
                           "mechanism_check": "LLM off — add a free GROQ_API_KEY."}
        save_journal(j)
        return h["evaluation"]
    prompt = (f"HYPOTHESIS: {h['text']}\n\n"
              f"BOARD CONTEXT (current state, optional):\n{board_context[:1500]}\n\n"
              f"TRACKED INSTRUMENTS: {', '.join(sorted(tracked_ids))}\n\n"
              "Evaluate per the JSON contract.")
    res = _llm_call(backend, prompt, system=EVAL_PROMPT)
    if res is None:
        return None
    h["evaluation"] = res
    h["evaluated_at"] = datetime.now(timezone.utc).isoformat()
    save_journal(j)
    return res


def add_trade(instrument: str, side: str, level: str, rationale: str,
              link: str = "") -> dict:
    j = load_journal()
    t = {"id": uuid.uuid4().hex[:8],
         "ts": datetime.now(timezone.utc).isoformat(),
         "instrument": instrument, "side": side, "level": level,
         "rationale": rationale.strip(), "link": link, "status": "open"}
    j["trades"].insert(0, t)
    save_journal(j)
    return t


def close_trade(tid: str, note: str = "") -> None:
    j = load_journal()
    for t in j["trades"]:
        if t["id"] == tid:
            t["status"] = "closed"
            t["closed_at"] = datetime.now(timezone.utc).isoformat()
            if note:
                t["close_note"] = note
    save_journal(j)


def export_markdown() -> str:
    j = load_journal()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%MZ")
    L = [f"# Journal — {now}", ""]
    if j["hypotheses"]:
        L.append("## Hypotheses")
        for h in j["hypotheses"]:
            L.append(f"### {h['ts'][:10]} · {h['text']}")
            if h.get("context"):
                L.append(f"- context: {h['context']}")
            ev = h.get("evaluation")
            if ev:
                L.append(f"- verdict: **{ev.get('verdict','')}** — "
                         f"{ev.get('mechanism_check','')}")
                if ev.get("confirming"):
                    L.append(f"- confirms: {ev['confirming']}")
                if ev.get("refuting"):
                    L.append(f"- refutes: {ev['refuting']}")
                if ev.get("instruments"):
                    L.append(f"- expressed via: {', '.join(ev['instruments'])}")
                if ev.get("sharpened"):
                    L.append(f"- sharpened: _{ev['sharpened']}_")
            L.append("")
    if j["trades"]:
        L.append("## Trade journal")
        for t in j["trades"]:
            L.append(f"- **{t['ts'][:16]}Z · {t['side'].upper()} "
                     f"{t['instrument']}** @ {t['level'] or 'mkt'} "
                     f"[{t['status']}] — {t['rationale']}"
                     + (f" (ctx: {t['link']})" if t.get("link") else ""))
            if t.get("close_note"):
                L.append(f"  - closed: {t['close_note']}")
    return "\n".join(L)


if __name__ == "__main__":
    h = add_hypothesis("If Brent holds above 72 on Hormuz risk, OMC margins "
                       "compress and BPCL underperforms nifty_50 within 5 sessions.",
                       context="oil event 2026-07-08")
    add_trade("usd_inr", "watch", "95.40", "INR weakness lags oil spike; "
              "watch for break of 20d range", link=h["id"])
    print(export_markdown())
