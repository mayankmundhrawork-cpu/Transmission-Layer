"""SYNTH_V2 · S6 — the gate (deliberately THIN).

S4 already turned the critic into a confidence CAP and the packet already
enforces grounding, falsifier-or-drop and no-verdict-language. So S6 is not a
second AMIFT critic duplicating that work — it is exactly one thing: the
arithmetic monotonicity clamp, with an override log.

A candidate's disposition is set by the scaffold at the reference-class cap.
Call A may only LOWER it (DISMISS drops a lead). S6 applies `clamp_disposition`
so that ANY proposed disposition above the cap — a future code path, a
hallucinated promotion, a bug — is overridden to the cap and LOGGED. The log is
the smell detector: a component repeatedly trying to promote capped leads is
something to see, not silently absorb.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from synth_packet import clamp_disposition

SYNTH_DIR = Path(__file__).parent / "data" / "synth"
OVERRIDE_LOG = SYNTH_DIR / "gate_overrides.json"

# Call A classification -> the disposition it PROPOSES for the card. INVESTIGATE
# and INSUFFICIENT_CONTEXT keep the card at its scaffold cap; DISMISS lowers it.
_PROPOSED = {"INVESTIGATE": "keep", "INSUFFICIENT_CONTEXT": "keep",
             "DISMISS": "DISMISS"}


def gate(cap: str, call_a_classification: str, proposed_override: str | None = None,
         instance: str = "", log: bool = True) -> dict:
    """Final disposition after the clamp. `cap` is the scaffold/S4 cap;
    `proposed_override` lets a caller (or a test) inject a raw proposed
    disposition to prove the clamp bites. Returns the final disposition, whether
    it was clamped, and the surfacing decision."""
    if proposed_override is not None:
        proposed = proposed_override
    else:
        p = _PROPOSED.get(call_a_classification, "keep")
        proposed = cap if p == "keep" else p
    final, clamped = clamp_disposition(proposed, cap)
    if clamped and log:
        _log_override(instance, proposed, cap, call_a_classification)
    return {"final_disposition": final, "clamped": clamped,
            "call_a": call_a_classification,
            # DISMISS is not surfaced on the board; it is dropped to a dismissed
            # list. INSUFFICIENT_CONTEXT surfaces (a hedged lead), never dropped.
            "surfaced": call_a_classification != "DISMISS"}


def _log_override(instance, proposed, cap, call_a):
    SYNTH_DIR.mkdir(parents=True, exist_ok=True)
    entries = []
    if OVERRIDE_LOG.exists():
        try:
            entries = json.loads(OVERRIDE_LOG.read_text(encoding="utf-8"))["overrides"]
        except Exception:
            pass
    entries.append({"ts": datetime.now(timezone.utc).isoformat(),
                    "instance": instance, "proposed": proposed, "cap": cap,
                    "call_a": call_a})
    OVERRIDE_LOG.write_text(json.dumps({"overrides": entries[-500:]}),
                            encoding="utf-8")


if __name__ == "__main__":
    # a hallucinated promotion is clamped and logged
    print("normal INVESTIGATE @ LEAD cap:", gate("LEAD", "INVESTIGATE", log=False))
    print("DISMISS @ LEAD cap:", gate("LEAD", "DISMISS", log=False))
    print("hallucinated promotion:",
          gate("LEAD", "INVESTIGATE", proposed_override="OBSERVATION",
               instance="test", log=False))
