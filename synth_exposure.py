"""SYNTH_V2 · exposure store (§2) — curated, quality-tagged, FAIL-CLOSED.

There is no free exposure feed for Indian names (EXPOSURE_SCOPING.md §1). The
store is small, human-editable YAML curated on results days. Its whole job is to
make the FX-capture lesson structural: every field carries `value`, `as_of`
(filing date), `source` (filing + note), and `quality` in {disclosed, derived,
proxy} — and the store literally cannot hold a value without provenance.

FAIL-CLOSED, like `driver_admissible` and the taxonomy-completeness test:
  * a field with a `value` but null `source` or null/invalid `quality` is an
    ERROR — the basket does not build;
  * a field still at its sentinel (value null) is UNCURATED — the basket is not
    ready until the owner fills it;
  * a field whose `as_of` is older than one reporting cycle is STALE — it still
    builds but discounts the candidate (staleness is first-class, like
    driver_stale).
The owner supplies value/source/quality; this module never invents a number.

Run: python synth_exposure.py [basket]   # validate + report readiness
"""
from __future__ import annotations

import sys
from datetime import date, datetime
from pathlib import Path

EXPOSURE_DIR = Path(__file__).parent / "data" / "exposure"
QUALITY = ("disclosed", "derived", "proxy")
REQUIRED_FIELD_KEYS = ("value", "as_of", "source", "quality")


def load_basket(name: str) -> dict:
    import yaml
    p = EXPOSURE_DIR / f"{name}.yaml"
    return yaml.safe_load(p.read_text(encoding="utf-8"))


def _field_state(f: dict) -> tuple[str, str | None]:
    """(state, error) for one field. state in {curated, uncurated, error}."""
    if not isinstance(f, dict) or any(k not in f for k in REQUIRED_FIELD_KEYS):
        return "error", "field missing one of value/as_of/source/quality"
    if f["value"] is None:
        return "uncurated", None                       # sentinel — not filled yet
    # a value MUST carry provenance (fail-closed)
    if not f.get("source"):
        return "error", "value present but source is null"
    if f.get("quality") not in QUALITY:
        return "error", f"value present but quality not in {QUALITY}"
    if not f.get("as_of"):
        return "error", "value present but as_of is null"
    return "curated", None


def _as_of_date(v) -> date | None:
    if isinstance(v, date):
        return v
    try:
        return datetime.fromisoformat(str(v)).date()
    except Exception:
        return None


def validate_basket(basket: dict, today: date | None = None) -> dict:
    """Readiness report. ready=True only if EVERY required field on EVERY name is
    curated with valid provenance and none errored."""
    today = today or date.today()
    cycle = int(basket.get("reporting_cycle_days", 100))
    required = basket.get("required_fields", [])
    errors, uncurated, stale, curated = [], [], [], 0
    names = basket.get("names", {})
    for nm, rec in names.items():
        fields = (rec or {}).get("fields", {})
        for fk in required:
            if fk not in fields:
                errors.append(f"{nm}.{fk}: field absent (required)")
                continue
            state, err = _field_state(fields[fk])
            if state == "error":
                errors.append(f"{nm}.{fk}: {err}")
            elif state == "uncurated":
                uncurated.append(f"{nm}.{fk}")
            else:
                curated += 1
                d = _as_of_date(fields[fk].get("as_of"))
                if d is not None and (today - d).days > cycle:
                    stale.append({"field": f"{nm}.{fk}",
                                  "as_of": str(d),
                                  "age_days": (today - d).days})
    ready = not errors and not uncurated and bool(names) and bool(required)
    return {"basket": basket.get("basket"), "ready": ready,
            "n_names": len(names), "n_required": len(required),
            "curated": curated, "errors": errors,
            "uncurated": uncurated, "stale": stale}


def basket_quality_summary(basket: dict) -> dict:
    """Per-basket data-quality header for the packet: how many fields are
    disclosed vs derived vs proxy, and the oldest as_of (loudness requirement)."""
    counts = {q: 0 for q in QUALITY}
    oldest = None
    for rec in basket.get("names", {}).values():
        for f in (rec or {}).get("fields", {}).values():
            state, _ = _field_state(f) if isinstance(f, dict) else ("error", "")
            if state == "curated":
                counts[f["quality"]] += 1
                d = _as_of_date(f.get("as_of"))
                if d and (oldest is None or d < oldest):
                    oldest = d
    total = sum(counts.values())
    return {"counts": counts, "total": total,
            "mostly_proxy": total > 0 and counts["proxy"] * 2 >= total,
            "oldest_as_of": None if oldest is None else str(oldest)}


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "margin_trap"
    b = load_basket(name)
    rep = validate_basket(b)
    q = basket_quality_summary(b)
    print(f"basket '{rep['basket']}': ready={rep['ready']} | "
          f"{rep['n_names']} names x {rep['n_required']} required | "
          f"curated {rep['curated']}")
    print(f"  quality: {q['counts']} (mostly_proxy={q['mostly_proxy']}, "
          f"oldest_as_of={q['oldest_as_of']})")
    if rep["errors"]:
        print("  ERRORS (fail-closed):")
        for e in rep["errors"][:10]:
            print(f"    - {e}")
    if rep["uncurated"]:
        print(f"  UNCURATED ({len(rep['uncurated'])}) — owner must fill: "
              + ", ".join(rep["uncurated"][:8])
              + (" ..." if len(rep["uncurated"]) > 8 else ""))
    if rep["stale"]:
        print(f"  STALE ({len(rep['stale'])}): "
              + ", ".join(s["field"] for s in rep["stale"][:8]))
