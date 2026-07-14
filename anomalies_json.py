"""P8 — machine-readable anomaly records (full contract).

One record per candidate with every measured gate input, FDR control across
the scan (P7), lead-lag evidence (P5), mean-reversion horizon (P6), the
signal-type track record (P9), and built-in falsifiers.

Run: python anomalies_json.py
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
OUT_JSON = DATA_DIR / "anomalies.json"

FDR_Q = 0.10


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
    from fdr import benjamini_hochberg, z_to_p
    from leadlag import load_setups
    from regime import load_regime
    from scorecard import load_scorecard
    from spreads import load_spreads

    snap = build_snapshot()
    reg = load_regime()
    ledger = load_assumptions_state().get("assumptions", {})
    setups_state = load_setups()
    spreads = load_spreads().get("series", {})
    card = load_scorecard().get("types", {})
    broken = [n for n, a in ledger.items()
              if a["status"] in ("WEAK", "INVERTED")]

    # ── P7: BH-FDR across the WHOLE scan (every series with a test stat,
    # not just the flagged ones — that's what controls the discovery rate)
    scan = []
    for r in snap.get("series", []):
        stat = r.get("resid_z") if r.get("resid_z") is not None else r.get("zc")
        if stat is not None:
            scan.append((r["id"], float(stat)))
    bh = benjamini_hochberg([z_to_p(s) for _, s in scan], q=FDR_Q)
    bh_pass = {sid: rej for (sid, _), rej in zip(scan, bh["reject"])}

    def _track(sig_type):
        t = card.get(sig_type) or {}
        return {"type": sig_type, "hit_rate": t.get("hit_rate"),
                "n": t.get("n"), "definition": t.get("definition")}

    records = []
    for r in snap.get("series", []):
        if r.get("flag") not in ("amber", "red") and \
                r.get("move_label") != "unexplained":
            continue
        sid = r["id"]
        sp = spreads.get(sid) or {}
        ll = [s for s in setups_state.get("setups", [])
              if s["driver"] == sid or s["target"] == sid] or None
        sig_type = ("spread_reversion" if sp else
                    "residual_reversion" if r.get("move_label") == "unexplained"
                    else None)
        records.append({
            "id": sid, "market": r["market"], "flag": r["flag"],
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
            "bh_significant": bh_pass.get(sid),
            "leadlag_evidence": ll,
            "mean_reversion": ({"half_life_days": sp.get("half_life_days"),
                                "adf_p": sp.get("adf_p"),
                                "hurst": sp.get("hurst")} if sp else None),
            "track_record": _track(sig_type) if sig_type else None,
            "falsifiers": _falsifiers(r),
        })

    out = {"generated": datetime.now(timezone.utc).isoformat(),
           "regime": reg.get("label"),
           "fdr": {"q": FDR_Q, "n_scanned": bh["n"],
                   "n_significant": bh["n_rejected"],
                   "effective_p_threshold": bh["threshold"]},
           "setups": setups_state.get("setups", []),
           "setups_track_record": _track("transmission_follow"),
           "n": len(records),
           "records": records}
    OUT_JSON.write_text(json.dumps(out), encoding="utf-8")
    return out


if __name__ == "__main__":
    o = build_anomalies()
    f = o["fdr"]
    print(f"anomalies.json: {o['n']} records | scan {f['n_scanned']} -> "
          f"{f['n_significant']} BH-significant (q={f['q']}, "
          f"p<={f['effective_p_threshold']}) | {len(o['setups'])} setups")
    for rec in o["records"][:6]:
        tr = rec.get("track_record") or {}
        print(f"  {rec['id']:22} {rec['flag'] or '-':6} zc={rec['conditional_z']} "
              f"rz={rec['residual_z']} bh={rec['bh_significant']} "
              f"label={rec['move_label']}"
              + (f" | {tr['type']} hit {tr['hit_rate']}" if tr else ""))
