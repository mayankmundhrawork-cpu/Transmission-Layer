"""SYNTH_V2 · S5 Call A — Classify {INVESTIGATE | DISMISS | INSUFFICIENT_CONTEXT}.

The LLM finally enters the pipeline — last, narrow, and unable to override
anything the scaffold decided. Call A adds a single triage word to a packet that
already forces the call. It is a PURE FUNCTION of the deterministic packet with
the model client INJECTED (real Groq in prod, a fixture client in CI), so it is
testable with no network at all — anything that only works when Groq answers is
the model-dependence we spent the whole build removing.

Three things are enforced in CODE, never trusted to the prompt:
  * GROUNDING — every field the model cites must resolve to a real packet path;
    a citation that doesn't is a hallucination and the output is VOID.
  * ESCAPE HATCH — malformed JSON, low confidence, an unparseable class, or a
    voided output all resolve to INSUFFICIENT_CONTEXT. NEVER to INVESTIGATE:
    the failure mode at the top of an attention funnel is silence, not a false
    summons.
  * NO PROMOTION — Call A can DISMISS (drop a lead) or keep it; it never raises
    the scaffold-set disposition/tier.

`implied_classification(packet)` is the deterministic call the packet forces —
the CI ground truth the hand-authored fixtures must match, and the proof the
packet is self-sufficient (the call is computable WITHOUT a model).
"""
from __future__ import annotations

import json
from pathlib import Path

PROMPTS = Path(__file__).parent / "prompts"
PROMPT_A_VERSION = "classify_a_v1"
ALLOWED = {"INVESTIGATE", "DISMISS", "INSUFFICIENT_CONTEXT"}
CONF_MIN = 0.5


# ── citable field paths + grounding ──────────────────────────────────────
def _leaf_paths(obj, prefix="") -> set:
    """All dotted paths into the packet (leaves AND dict/list container keys),
    so a model may cite either a specific value or a section it read."""
    paths = set()
    if isinstance(obj, dict):
        for k, v in obj.items():
            p = f"{prefix}.{k}" if prefix else k
            paths.add(p)
            paths |= _leaf_paths(v, p)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            paths |= _leaf_paths(v, f"{prefix}[{i}]")
    return paths


def citable_fields(packet: dict) -> set:
    return _leaf_paths(packet)


def _grounding_ok(packet: dict, cited: list) -> tuple[bool, list]:
    paths = citable_fields(packet)
    # accept a cited path if it (or a parent prefix of it) is a real packet path
    bad = []
    for c in cited or []:
        c = str(c)
        if c in paths or any(p == c or p.startswith(c + ".") or p.startswith(c + "[")
                             for p in paths):
            continue
        bad.append(c)
    return (len(bad) == 0, bad)


# ── deterministic ground truth (the packet forces the call) ─────────────
def implied_classification(packet: dict) -> str:
    """What a correct reader concludes from the packet ALONE. This is the CI
    ground truth; if it is computable, the packet is self-sufficient and the
    model is convenience, not cognition."""
    corr = packet.get("corroboration", {})
    if "news_cluster" in corr:                    # tier-1 news observation
        # dense real catalyst + wider complex quiet => worth a look
        nc = corr["news_cluster"]
        if (nc.get("n_headlines", 0) >= 10 and not nc.get("watch_only_join")):
            return "INVESTIGATE"
        return "INSUFFICIENT_CONTEXT"
    if "explanation_search" in packet:            # tier-2 unexplained move
        jt = packet["explanation_search"].get("join_trust")
        return "INVESTIGATE" if (jt is not None and jt >= 0.8) \
            else "INSUFFICIENT_CONTEXT"
    if isinstance(packet.get("divergence"), list):  # tier-3 transmission lead
        rc = packet["reference_class"]["verdict"]
        news = corr.get("news_join")
        if rc in ("NO_RELIABLE_EDGE", "NO_DEMONSTRATED_EDGE", "INSUFFICIENT",
                  "UNRATED") and not news:
            return "DISMISS"
        return "INVESTIGATE"
    return "INSUFFICIENT_CONTEXT"


# ── the classifier (pure; client injected) ──────────────────────────────
def build_prompt(packet: dict) -> str:
    tmpl = (PROMPTS / f"{PROMPT_A_VERSION}.md").read_text(encoding="utf-8")
    return (tmpl.replace("{packet_json}",
                         json.dumps(packet, indent=2, ensure_ascii=False))
                .replace("{citable_fields}",
                         "\n".join(sorted(citable_fields(packet)))))


def _escape(reason: str, confidence=0.0) -> dict:
    return {"classification": "INSUFFICIENT_CONTEXT", "confidence": confidence,
            "cited_fields": [], "rationale": f"escape: {reason}",
            "grounded": True, "escape_reason": reason, "llm_raw": None}


def classify(packet: dict, client) -> dict:
    """Classify a packet. `client.complete(prompt) -> str`. Every failure mode
    resolves to INSUFFICIENT_CONTEXT in CODE."""
    prompt = build_prompt(packet)
    try:
        raw = client.complete(prompt)
    except Exception as e:
        return _escape(f"client_error:{type(e).__name__}")
    try:
        obj = json.loads(raw)
    except Exception:
        return _escape("unparseable_json")
    cls = obj.get("classification")
    if cls not in ALLOWED:
        return _escape("invalid_classification")
    conf = obj.get("confidence")
    if not isinstance(conf, (int, float)) or conf < CONF_MIN:
        return _escape("low_confidence", confidence=conf if isinstance(conf, (int, float)) else 0.0)
    grounded, bad = _grounding_ok(packet, obj.get("cited_fields"))
    if not grounded:
        # hallucinated citation -> VOID -> silence, and log the ungrounded refs
        return {**_escape("ungrounded_citation"), "ungrounded": bad,
                "llm_raw": obj}
    # an INVESTIGATE must be grounded in at least one packet field
    if cls == "INVESTIGATE" and not obj.get("cited_fields"):
        return _escape("investigate_without_citation")
    return {"classification": cls, "confidence": round(float(conf), 3),
            "cited_fields": obj.get("cited_fields", []),
            "rationale": str(obj.get("rationale", ""))[:200],
            "grounded": True, "escape_reason": None, "llm_raw": obj}


# ── clients: fixture (CI) and Groq (prod) ───────────────────────────────
class FixtureClient:
    """Returns HAND-AUTHORED expected classifications keyed by packet instance.
    These are NOT real model outputs — they are what a correct model SHOULD
    produce, authored from the packet, so CI can gate with no network. If a
    fixture ever disagrees with implied_classification, that is a real bug."""
    def __init__(self, by_instance: dict):
        self.by_instance = by_instance

    def complete(self, prompt: str) -> str:
        for inst, resp in self.by_instance.items():
            if inst in prompt:
                return json.dumps(resp)
        return json.dumps({"classification": "INSUFFICIENT_CONTEXT",
                           "confidence": 0.9, "cited_fields": [],
                           "rationale": "no fixture for this instance"})


def groq_client(model: str = "llama-3.3-70b-versatile", temperature: float = 0.2):
    """Production client (temp <=0.2, strict JSON). Lazy — only touches the
    network/keys when actually called, so importing this module never requires
    Groq. Not used in CI."""
    import os

    from groq import Groq  # optional dependency; only in prod
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY not set")
    cli = Groq(api_key=api_key)

    class _C:
        def complete(self, prompt: str) -> str:
            r = cli.chat.completions.create(
                model=model, temperature=temperature,
                response_format={"type": "json_object"},
                messages=[{"role": "user", "content": prompt}])
            return r.choices[0].message.content
    return _C()


# ── convergence audit (owner runs out of band; NOT a CI gate) ───────────
def run_convergence(packets: list, client_mid, client_frontier) -> list:
    """Run Call A through two models and report DIVERGENCES. The finding on a
    divergence is NEVER 'use a bigger model' — it is 'the packet is missing the
    field that made the difference'. The message points at the ASSEMBLER."""
    out = []
    for pkt in packets:
        a = classify(pkt, client_mid)["classification"]
        b = classify(pkt, client_frontier)["classification"]
        if a != b:
            msg = (f"packet under-specified: models diverged on "
                   f"{pkt.get('instance')} (mid={a}, frontier={b}) — inspect "
                   f"which packet field the frontier model used that the "
                   f"mid-tier lacked, and add it to the assembler.")
            out.append({"instance": pkt.get("instance"), "mid": a,
                        "frontier": b, "action": msg})
    return out


if __name__ == "__main__":
    # worked example: the bovespa LEAD packet in -> classification + grounding out
    import pandas as pd

    from relations import load_relations
    from synth_packet import assemble_transmission_packet
    gdir = Path(__file__).parent / "data" / "synth" / "golden_2026-07-20"
    prices = pd.read_csv(gdir / "prices.csv", index_col=0,
                         parse_dates=True).sort_index()
    cands = json.loads((gdir / "candidates.json").read_text(encoding="utf-8"))
    bov = next(c for c in cands["candidates"]
               if c["kind"] == "driver_pulse" and c["driver"] == "bovespa")
    pkt = assemble_transmission_packet(bov, prices,
                                       load_relations().get("neighbours", {}))
    fixture = {pkt["instance"]: {
        "classification": "DISMISS", "confidence": 0.8,
        "cited_fields": ["reference_class.verdict", "corroboration.news_join",
                         "divergence"],
        "rationale": "NO_RELIABLE_EDGE class, no catalyst, cooling channel — a "
                     "coin-flip divergence with nothing instance-specific."}}
    result = classify(pkt, FixtureClient(fixture))
    print("packet implied :", implied_classification(pkt))
    print("Call A (fixture):", json.dumps(result, indent=2))
