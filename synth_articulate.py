"""SYNTH_V2 · S5 Call B — Articulate (the question + falsifier for the reader).

Call B runs only when Call A returned INVESTIGATE. It phrases the divergence's
question and its kill condition — it does NOT narrate a thesis. It is the
higher-risk call, because articulation is where a model wants to add color: a
plausible mechanism, a tidy causal story, a number that sounds right. So Call B
inherits Call A's grounding check VERBATIM, plus two more, all in code:

  * GROUNDING — every field Call B emits must resolve to a packet path; an
    ungrounded articulation voids to NO articulation and the reader gets the
    deterministic packet's own question + falsifier (which already exist and are
    already good). The packet is never worse off for Call B failing — Call B is
    strictly additive polish.
  * NO VERDICT LANGUAGE — "setup", "should", a probability/percent, "likely to"
    void the output (arithmetic, not a prompt request).
  * FALSIFIER-OR-DROP, mechanically defined — the articulated falsifier must be
    non-trivial, name a concrete observable condition, and be grounded; else it
    is dropped in favour of the packet's deterministic falsifier. A card ALWAYS
    ends with a checkable falsifier because the scaffold always supplied one.

Every failure mode FALLS BACK to the deterministic packet — the card is never
dropped for Call B's benefit, because the packet carried a good question and
falsifier before the LLM existed.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from synth_classify import _grounding_ok, citable_fields

PROMPTS = Path(__file__).parent / "prompts"
PROMPT_B_VERSION = "articulate_b_v1"

# verdict / probability language that must never appear in an articulation
_FORBIDDEN = re.compile(
    r"\b(setup|should|probab\w*|likely\s+to|odds)\b|\d+\s*%", re.I)
# A checkable falsifier names a concrete observable a human can verify — not a
# vacuous "proves wrong". The vocabulary differs by anatomy: transmission
# resolves on a window/counter-move, news on a level/staleness test, an
# unexplained move on finding the catalyst under inspection (tighter than a
# window). All three are concrete; "the thesis proves wrong" is not.
_CHECK_TOKENS = re.compile(
    r"\b(session|sessions|day|days|week|weeks|window|against|beyond|exceed\w*|"
    r"above|below|elevated|stale|already|resolv\w*|counter-?move|close[sd]?|"
    r"priced|level|catalyst|found|verif\w*|inspect\w*|explain\w*|print|"
    r"data\s+error)\b", re.I)
_FALSIFIER_MIN_LEN = 40


def build_prompt(packet: dict) -> str:
    tmpl = (PROMPTS / f"{PROMPT_B_VERSION}.md").read_text(encoding="utf-8")
    return (tmpl.replace("{packet_json}",
                         json.dumps(packet, indent=2, ensure_ascii=False))
                .replace("{citable_fields}",
                         "\n".join(sorted(citable_fields(packet)))))


def _falsifier_checkable(text: str) -> bool:
    """Mechanical bar (owner): non-trivial, names a concrete observable
    condition. Rejects 'killed if it proves wrong'; accepts a level/counter-
    move/staleness/window condition."""
    if not text or len(text.strip()) < _FALSIFIER_MIN_LEN:
        return False
    return bool(_CHECK_TOKENS.search(text))


def _scaffold(packet: dict, reason: str | None) -> dict:
    """The deterministic fallback — always available, always checkable."""
    return {"articulated": False, "source": "scaffold",
            "headline": f"{packet.get('disposition')}: {packet.get('instance')}",
            "question": packet.get("the_question"),
            "falsifier": packet.get("falsifier"),
            "cited_fields": [], "reason": reason, "voided": None}


def articulate(packet: dict, call_a_classification: str, client) -> dict:
    """Articulate a packet that Call A marked INVESTIGATE. Any failure returns
    the deterministic scaffold card — the reader never loses the packet's own
    question and falsifier."""
    if call_a_classification != "INVESTIGATE":
        return _scaffold(packet, "call_a_not_investigate")
    try:
        raw = client.complete(build_prompt(packet))
        obj = json.loads(raw)
    except Exception:
        return _scaffold(packet, "unparseable")

    headline = str(obj.get("headline", ""))
    question = str(obj.get("question", ""))
    falsifier = str(obj.get("falsifier", ""))
    if not headline or not question or not falsifier:
        return _scaffold(packet, "missing_field")

    # no verdict / probability language anywhere in the emitted text
    blob = f"{headline}\n{question}\n{falsifier}"
    if _FORBIDDEN.search(blob):
        return _scaffold(packet, "forbidden_language")

    # grounding — every cited field must resolve; else void to scaffold
    grounded, bad = _grounding_ok(packet, obj.get("cited_fields"))
    if not grounded:
        r = _scaffold(packet, "ungrounded_citation")
        r["voided"] = bad
        return r
    if not obj.get("cited_fields"):
        return _scaffold(packet, "no_citation")

    # falsifier-or-drop (mechanical): non-trivial + concrete observable, or fall
    # back to the deterministic falsifier (which is checkable by construction)
    if not _falsifier_checkable(falsifier):
        r = _scaffold(packet, "falsifier_not_checkable")
        # keep the LLM's headline/question if THEY were clean, but the falsifier
        # is the scaffold's — a card must end on a checkable falsifier
        r.update(articulated=True, source="hybrid",
                 headline=headline, question=question,
                 cited_fields=obj.get("cited_fields", []))
        return r

    return {"articulated": True, "source": "llm",
            "headline": headline, "question": question, "falsifier": falsifier,
            "cited_fields": obj.get("cited_fields", []),
            "reason": None, "voided": None}


def render_card(art: dict) -> str:
    L = [f"CARD  (articulation: {art['source']}"
         + (f", fell back: {art['reason']}" if art.get("reason") else "") + ")",
         f"  {art['headline']}",
         f"  QUESTION : {art['question']}",
         f"  FALSIFIER: {art['falsifier']}"]
    return "\n".join(L)


if __name__ == "__main__":
    import pandas as pd

    from synth_classify import FixtureClient, classify
    from synth_packet import assemble_news_packet
    gdir = Path(__file__).parent / "data" / "synth" / "golden_2026-07-20"
    cands = json.loads((gdir / "candidates.json").read_text(encoding="utf-8"))["candidates"]
    wti = next(c for c in cands if c["kind"] == "news_no_move"
               and c["series"] == "wti")
    pkt = assemble_news_packet(wti, cands)

    a_fixture = {pkt["instance"]: {
        "classification": "INVESTIGATE", "confidence": 0.8,
        "cited_fields": ["corroboration.news_cluster"],
        "rationale": "dense catalyst, complex quiet"}}
    a = classify(pkt, FixtureClient(a_fixture))

    b_fixture = {pkt["instance"]: {
        "headline": "wti is not pricing a dense Gulf/Iran escalation cluster "
                    "while the whole energy-vol complex sits quiet",
        "question": "Is the market genuinely not pricing this escalation, or is "
                    "the flow already discounted / low-signal?",
        "falsifier": "Killed if wti's LEVEL is already elevated (not just today's "
                     "return quiet), if the headlines are stale/low-signal on "
                     "inspection, or if the divergence is already resolving as "
                     "price begins to move over the next sessions.",
        "cited_fields": ["corroboration.news_cluster",
                         "corroboration.complex_co_quiet",
                         "divergence.quietness_pctile"]}}
    b = articulate(pkt, a["classification"], FixtureClient(b_fixture))
    print("Call A:", a["classification"])
    print(render_card(b))
    print("\n-- adversarial: model invents a mechanism (ungrounded) --")
    bad = {pkt["instance"]: {
        "headline": "wti dropped because OPEC secretly agreed to raise output",
        "question": "will the secret OPEC deal hold?",
        "falsifier": "killed if the OPEC deal is announced",
        "cited_fields": ["opec.secret_deal"]}}
    b2 = articulate(pkt, "INVESTIGATE", FixtureClient(bad))
    print(render_card(b2), "\n  voided:", b2.get("voided"))
