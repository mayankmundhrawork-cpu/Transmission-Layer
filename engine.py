"""Step 5 abnormality engine.

Reads data/prices.csv and computes, for every series, the latest snapshot:
  last, 1d%, 5d%, 20d-z, 60d-z, 1y-percentile, flag ("none"|"amber"|"red"),
  reasons (list of triggered rules), framework triggers.

Then applies co-occurrence escalation across linked groups and produces a
composite ranking for the anomaly panel.

Entry point: build_snapshot() -> dict with 'series' (list of row dicts) and
'flags' (list of composite anomaly rows already sorted by score desc).
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from registry import LINKED_GROUPS, load_registry

DATA_DIR = Path(__file__).parent / "data"
PRICES_CSV = DATA_DIR / "prices.csv"

Z_WIN_SHORT = 20
Z_WIN_LONG = 60
PCT_WIN = 252

AMBER_Z = 1.5
RED_Z = 2.5

# Below this many valid observations, still surface the numbers but do not fire
# any flags (z / percentile / framework / co-occurrence). Statistics are too
# thin to trust — see goi_ust_spread with ~11 monthly points.
MIN_OBS_FOR_FLAGS = 30


def _z(series: pd.Series, window: int) -> float:
    s = series.dropna().tail(window + 1)
    if len(s) < window:
        return float("nan")
    tail = s.iloc[-window - 1 : -1] if len(s) > window else s.iloc[:-1]
    m, sd = tail.mean(), tail.std(ddof=0)
    if sd == 0 or np.isnan(sd):
        return float("nan")
    return float((s.iloc[-1] - m) / sd)


def _percentile(series: pd.Series, window: int = PCT_WIN) -> float:
    s = series.dropna().tail(window)
    if len(s) < 20:
        return float("nan")
    x = s.iloc[-1]
    return float((s < x).sum() / len(s) * 100.0)


def _pct_change(series: pd.Series, n: int) -> float:
    s = series.dropna()
    if len(s) < n + 1:
        return float("nan")
    prev = s.iloc[-1 - n]
    if abs(prev) < 1e-9:  # zero-crossing spreads: % change is meaningless
        return float("nan")
    return float((s.iloc[-1] / prev - 1) * 100.0)


def _framework_reasons(spec: dict, series: pd.Series, snap: dict[str, float]) -> list[str]:
    reasons: list[str] = []
    fw = spec.get("framework", {})
    s = series.dropna()
    if s.empty:
        return reasons

    if "range_extreme_days" in fw:
        n = fw["range_extreme_days"]
        tail = s.tail(n)
        last = s.iloc[-1]
        if last >= tail.max() or last <= tail.min():
            reasons.append(f"{n}d range extreme")

    if "single_session_pct" in fw:
        thr = fw["single_session_pct"]
        pct = snap.get("d1_pct")
        if pct is not None and not np.isnan(pct) and abs(pct) >= thr:
            reasons.append(f"1-session move {pct:+.2f}% ≥ {thr}%")

    if "single_day_bps" in fw:
        thr = fw["single_day_bps"]
        if len(s) >= 2:
            diff_bps = (s.iloc[-1] - s.iloc[-2]) * 100.0  # FRED yields are in %
            if abs(diff_bps) >= thr:
                reasons.append(f"1d move {diff_bps:+.1f}bps ≥ {thr}bps")

    if fw.get("pct_extreme_52w"):
        p = snap.get("pct_1y")
        if p is not None and not np.isnan(p) and (p >= 95 or p <= 5):
            reasons.append(f"52-wk extreme (pct={p:.0f})")

    if fw.get("break_below_100dma"):
        if len(s) >= 101:
            dma = s.tail(101).iloc[:-1].mean()
            if s.iloc[-1] < dma and s.iloc[-2] >= dma:
                reasons.append("break below 100-DMA")

    if fw.get("gsr_bands"):
        # band levels are the framework rule; the NARRATIVE (monetary stress
        # vs industrial rotation) now lives in the assumption ledger and is
        # only quotable when measured VALID (see assumptions.yaml:gsr_stress_gauge)
        last = s.iloc[-1]
        if last > 85:
            reasons.append(f"GSR>{85} (extreme high)")
        elif last < 75:
            reasons.append(f"GSR<{75} (extreme low)")

    if "monthly_bps_move" in fw:
        thr = fw["monthly_bps_move"]
        if len(s) >= 22:
            diff_bps = (s.iloc[-1] - s.iloc[-22]) * 100.0
            if abs(diff_bps) >= thr:
                reasons.append(f"~1mo spread move {diff_bps:+.1f}bps ≥ {thr}bps")

    return reasons


def _flag_level(z: float, pct: float, framework_hit: bool,
                amber_z: float = AMBER_Z) -> str:
    """Unchanged v1 semantics; `amber_z` allows a stricter per-series amber bar
    (news-admitted names use settings.DYNAMIC_AMBER_Z via their spec)."""
    z_abs = abs(z) if not np.isnan(z) else 0.0
    pct_ext = (not np.isnan(pct)) and (pct <= 5 or pct >= 95)
    if z_abs >= RED_Z or (framework_hit and z_abs >= amber_z):
        return "red"
    if z_abs >= amber_z or pct_ext or framework_hit:
        return "amber"
    return "none"


def build_snapshot() -> dict[str, Any]:
    if not PRICES_CSV.exists():
        return {"series": [], "flags": [], "error": f"missing {PRICES_CSV} — run fetch.py"}

    df = pd.read_csv(PRICES_CSV, index_col=0, parse_dates=True).sort_index()

    rows: list[dict[str, Any]] = []
    by_id: dict[str, dict[str, Any]] = {}
    series_specs = load_registry()

    for spec in series_specs:
        sid = spec["id"]
        if sid not in df.columns:
            row = {
                "id": sid, "market": spec["market"], "last": None,
                "d1_pct": None, "d5_pct": None, "z20": None, "z60": None,
                "pct_1y": None, "flag": "missing", "reasons": ["no data"],
                "last_date": None,
            }
            rows.append(row); by_id[sid] = row
            continue

        s = df[sid].dropna()
        if s.empty:
            row = {
                "id": sid, "market": spec["market"], "last": None,
                "d1_pct": None, "d5_pct": None, "z20": None, "z60": None,
                "pct_1y": None, "flag": "missing", "reasons": ["empty"],
                "last_date": None,
            }
            rows.append(row); by_id[sid] = row
            continue

        d1 = _pct_change(s, 1)
        d5 = _pct_change(s, 5)
        z20 = _z(s, Z_WIN_SHORT)
        z60 = _z(s, Z_WIN_LONG)
        pct1y = _percentile(s, PCT_WIN)

        sparse = len(s) < MIN_OBS_FOR_FLAGS
        amber_bar = spec.get("amber_z") or AMBER_Z
        if sparse:
            level = "none"
            all_reasons = [f"sparse ({len(s)} obs < {MIN_OBS_FOR_FLAGS}) — flagging suppressed"]
            framework_hit = False
        else:
            snap = {"d1_pct": d1, "d5_pct": d5, "z20": z20, "z60": z60, "pct_1y": pct1y}
            reasons = _framework_reasons(spec, s, snap)

            z_reasons: list[str] = []
            if not np.isnan(z20) and abs(z20) >= amber_bar:
                z_reasons.append(f"|z20|={abs(z20):.2f}")
            if not np.isnan(pct1y) and (pct1y <= 5 or pct1y >= 95):
                z_reasons.append(f"1y-pct={pct1y:.0f}")

            level = _flag_level(z20, pct1y, framework_hit=bool(reasons),
                                amber_z=amber_bar)
            all_reasons = reasons + z_reasons
            framework_hit = bool(reasons)

        row = {
            "id": sid,
            "market": spec["market"],
            "name": spec.get("name") or sid,
            "symbol": spec.get("symbol"),
            "dynamic": bool(spec.get("dynamic")),
            "last": float(s.iloc[-1]),
            "d1_pct": None if np.isnan(d1) else d1,
            "d5_pct": None if np.isnan(d5) else d5,
            "z20": None if np.isnan(z20) else z20,
            "z60": None if np.isnan(z60) else z60,
            "pct_1y": None if np.isnan(pct1y) else pct1y,
            "flag": level,
            "reasons": all_reasons,
            "framework_hit": framework_hit,
            "sparse": sparse,
            "obs": int(len(s)),
            "last_date": s.index[-1].strftime("%Y-%m-%d"),
        }
        rows.append(row)
        by_id[sid] = row

    # Conditional/residual annotation (P2/P3 state, computed by the CI
    # analytics pass; display + gating metadata, flag levels unchanged here).
    try:
        from conditional import load_conditional
        from factors import load_factor_state
        _cond = load_conditional().get("series", {})
        _fact = load_factor_state().get("series", {})
        for r in rows:
            c = _cond.get(r["id"]) or {}
            f = _fact.get(r["id"]) or {}
            r["zc"] = c.get("zc")
            r["resid_z"] = f.get("resid_z")
            r["r2_60d"] = f.get("r2_60d")
            r["top_factors"] = f.get("top_contributors")
            zc, rz = c.get("zc"), f.get("resid_z")
            if rz is not None and abs(rz) >= 1.5:
                r["move_label"] = "unexplained"
            elif zc is not None and abs(zc) >= 1.5 and (f.get("r2_60d") or 0) >= 0.25 \
                    and rz is not None and abs(rz) < 1.0:
                r["move_label"] = "priced"
            elif zc is not None and abs(zc) >= 1.5:
                r["move_label"] = "moved"
            else:
                r["move_label"] = "quiet"
    except Exception:
        pass

    # Co-occurrence: two+ in a linked group flagged same direction → composite
    # red — GATED on the assumption ledger: a group whose measured channel is
    # WEAK/INVERTED must not escalate (the "gold safe-haven" class of bug).
    try:
        from assumptions import group_status, load_assumptions_state
        _ledger = load_assumptions_state()
    except Exception:
        _ledger, group_status = {}, None

    composites: list[dict[str, Any]] = []
    for group_name, members in LINKED_GROUPS.items():
        flagged = [by_id[m] for m in members
                   if m in by_id and by_id[m]["flag"] in ("amber", "red")
                   and by_id[m]["z20"] is not None]
        if len(flagged) >= 2:
            signs = {np.sign(r["z20"]) for r in flagged}
            same_dir = len(signs) == 1
            if same_dir:
                status = group_status(group_name, _ledger) if group_status else None
                if status in ("WEAK", "INVERTED", "INSUFFICIENT_DATA"):
                    for r in flagged:
                        r["reasons"].append(
                            f"co-occur[{group_name}] suppressed: channel {status}")
                    continue  # measured channel not live — no escalation
                for r in flagged:
                    r["flag"] = "red"
                    r["reasons"].append(f"co-occur[{group_name}] same-direction"
                                        + (" (channel VALID)" if status else ""))
                composites.append({
                    "group": group_name, "kind": "same-direction",
                    "members": [r["id"] for r in flagged],
                    "max_abs_z": max(abs(r["z20"]) for r in flagged),
                    "count": len(flagged),
                    "framework_hit": any(r.get("framework_hit") for r in flagged),
                })

    # Composite ranking: max|z| in group + 2*n + 3*framework
    def score_row(r: dict[str, Any]) -> float:
        z = abs(r["z20"]) if r.get("z20") is not None else 0.0
        return z + (3.0 if r.get("framework_hit") else 0.0)

    def score_group(g: dict[str, Any]) -> float:
        return g["max_abs_z"] + 2.0 * g["count"] + (3.0 if g["framework_hit"] else 0.0)

    flag_entries: list[dict[str, Any]] = []
    for r in rows:
        if r["flag"] in ("amber", "red"):
            flag_entries.append({
                "type": "series", "id": r["id"], "market": r["market"],
                "flag": r["flag"], "score": score_row(r), "reasons": r["reasons"],
                "z20": r.get("z20"), "last": r.get("last"),
            })
    for g in composites:
        flag_entries.append({
            "type": "co-occurrence", "id": g["group"], "market": "CROSS",
            "flag": "red", "score": score_group(g),
            "reasons": [f"{g['kind']}: {', '.join(g['members'])}"],
            "z20": g["max_abs_z"], "last": None,
        })
    flag_entries.sort(key=lambda x: x["score"], reverse=True)

    last_data_date = df.index.max().strftime("%Y-%m-%d") if len(df) else None
    return {"series": rows, "flags": flag_entries, "last_data_date": last_data_date}


if __name__ == "__main__":
    import json
    snap = build_snapshot()
    print(json.dumps(snap, indent=2, default=str))
