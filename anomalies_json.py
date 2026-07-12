"""P8 — machine-readable anomaly records (basic contract now, gates evolve).

Emits data/anomalies.json alongside the human digest: one record per
currently-flagged series with every measured gate input attached, plus
built-in falsifiers. P5 (lead-lag emit gate) and P7 (BH significance) will
extend these records rather than reshape them.

Run: python anomalies_json.py
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
OUT_JSON = DATA_DIR / "anomalies.json"


def _falsifiers(r: dict) -> list[str]:
    out = []
    ml = r.get("move_label")
    if ml == "unexplained":
        out.append("becomes PRICED if factor betas catch up (resid_z -> |<1| "
                   "as R2 holds) or the move retraces within its half-life")
        out.append("becomes NOISE if resid_z mean-reverts within 5 sessions "
                   "with no follow-through in correlated receivers")
    elif ml == "priced":
        out.append("re-opens as anomaly if resid_z breaks |1.5| while the "
                   "explaining factors stay flat")
    if r.get("zc") is not None:
        out.append(f"conditional move invalidates if next-session zc "
                   f"reverses sign at comparable magnitude (now {r['zc']})")
    return out


def build_anomalies() -> dict:
    from assumptions import load_assumptions_state
    from engine import build_snapshot
    from regime import load_regime

    snap = build_snapshot()
    reg = load_regime()
    ledger = load_assumptions_state().get("assumptions", {})
    broken = [n for n, a in ledger.items()
              if a["status"] in ("WEAK", "INVERTED")]

    records = []
    for r in snap.get("series", []):
        if r.get("flag") not in ("amber", "red") and \
                r.get("move_label") not in ("unexplained",):
            continue
        records.append({
            "id": r["id"], "market": r["market"], "flag": r["flag"],
            "asof": r.get("last_date"),
            "raw": {"last": r.get("last"), "d1_pct": r.get("d1_pct"),
                    "z20": r.get("z20"), "pct_1y": r.get("pct_1y")},
            "conditional_z": r.get("zc"),
            "residual_z": r.get("resid_z"),
            "r2_60d": r.get("r2_60d"),
            "explained_by": r.get("top_factors"),
            "move_label": r.get("move_label"),
            "reasons": r.get("reasons", []),
            "regime": reg.get("label"),
            "assumptions_degraded": broken,
            "falsifiers": _falsifiers(r),
            # P5/P7 extensions land here:
            "leadlag_evidence": None,      # TODO P5
            "bh_significant": None,        # TODO P7
            "mean_reversion_half_life": None,  # spreads only, joined in P6+
        })
    out = {"generated": datetime.now(timezone.utc).isoformat(),
           "regime": reg.get("label"), "n": len(records),
           "records": records}
    OUT_JSON.write_text(json.dumps(out), encoding="utf-8")
    return out


if __name__ == "__main__":
    o = build_anomalies()
    print(f"anomalies.json: {o['n']} records (regime {o['regime']})")
    for rec in o["records"][:6]:
        print(f"  {rec['id']:22} {rec['flag'] or '-':6} zc={rec['conditional_z']} "
              f"rz={rec['residual_z']} label={rec['move_label']}")
