"""Cross-instrument correlation & lead-lag substrate (v5 feature 3).

Reads data/prices.csv (read-only over the core), computes:
  - pairwise return correlation at CORR_WINDOW (60d) and CORR_CONTEXT (252d)
  - lead-lag: corr(ret_a shifted +k, ret_b) for k=1..MAX_LAG — "a leads b by k"
Persists data/relations.json. Full recompute is ~seconds at this universe
size; honest recomputation beats a fake incremental scheme.

Consumers:
  neighbours(sid)            ranked correlation neighbours for the UI view
  laggards_for(member_ids)   correlated instruments that HAVEN'T moved yet —
                             the "X moved; Y is next" substrate for theses.

Run: python relations.py
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from settings import (CORR_CONTEXT, CORR_WINDOW, LAGGARD_MAX_Z,
                      LAGGARD_MIN_CORR, MAX_LAG, MIN_CORR)

DATA_DIR = Path(__file__).parent / "data"
PRICES_CSV = DATA_DIR / "prices.csv"
RELATIONS_JSON = DATA_DIR / "relations.json"

MIN_OBS = 120        # pair needs this many overlapping return obs
NEIGHBOURS_TOP = 12  # ranked neighbours persisted per series


def _std_matrix(rets: pd.DataFrame, min_obs: int) -> tuple[np.ndarray, list[str]]:
    """Z-standardised return matrix with NaN->0 after standardisation.
    Zeros contribute nothing to covariance; slight shrinkage on ragged
    columns is an accepted approximation (documented in build notes)."""
    cols = [c for c in rets.columns if rets[c].notna().sum() >= min_obs]
    X = rets[cols].to_numpy(dtype=float)
    mu = np.nanmean(X, axis=0)
    sd = np.nanstd(X, axis=0)
    sd[sd == 0] = np.nan
    Z = (X - mu) / sd
    Z[np.isnan(Z)] = 0.0
    return Z, cols


def _corr(Z: np.ndarray, min_obs: int) -> np.ndarray:
    n = (Z != 0).astype(float).T @ (Z != 0).astype(float)
    n[n < min_obs] = np.nan
    return (Z.T @ Z) / n


def _lagged_corr(Z: np.ndarray, lag: int, min_obs: int) -> np.ndarray:
    """corr(a_t-lag, b_t): row i leads column j by `lag` sessions."""
    A, B = Z[:-lag], Z[lag:]
    n = (A != 0).astype(float).T @ (B != 0).astype(float)
    n[n < min_obs] = np.nan
    return (A.T @ B) / n


def build_relations() -> dict:
    prices = pd.read_csv(PRICES_CSV, index_col=0, parse_dates=True).sort_index()
    rets = prices.pct_change(fill_method=None)

    min60 = int(CORR_WINDOW * 0.6)          # ≥36 obs inside the 60d window
    Z60, cols = _std_matrix(rets.tail(CORR_WINDOW + 1), min60)
    Z252, cols252 = _std_matrix(rets.tail(CORR_CONTEXT + 1), MIN_OBS)
    if cols != cols252:  # use the common, order-stable set
        common = [c for c in cols if c in set(cols252)]
        Z60, cols = _std_matrix(rets.tail(CORR_WINDOW + 1)[common], min60)
        Z252, _ = _std_matrix(rets.tail(CORR_CONTEXT + 1)[common], MIN_OBS)

    C60, C252 = _corr(Z60, min60), _corr(Z252, MIN_OBS)

    # lead-lag over the long window (needs history to be meaningful)
    best_lag = np.zeros_like(C252)
    best_lag_rho = np.zeros_like(C252)
    for k in range(1, MAX_LAG + 1):
        Ck = _lagged_corr(Z252, k, MIN_OBS)
        mask = np.abs(np.nan_to_num(Ck)) > np.abs(np.nan_to_num(best_lag_rho))
        best_lag_rho = np.where(mask, Ck, best_lag_rho)
        best_lag = np.where(mask, k, best_lag)

    idx = {c: i for i, c in enumerate(cols)}
    pairs = []
    for i, a in enumerate(cols):
        for j in range(i + 1, len(cols)):
            b = cols[j]
            r60 = C60[i, j] if not np.isnan(C60[i, j]) else None
            r252 = C252[i, j] if not np.isnan(C252[i, j]) else None
            # lead-lag is directional: check both orientations
            lr_ab, lg_ab = best_lag_rho[i, j], int(best_lag[i, j])   # a leads b
            lr_ba, lg_ba = best_lag_rho[j, i], int(best_lag[j, i])   # b leads a
            keep = any(x is not None and abs(x) >= MIN_CORR for x in (r60, r252)) \
                or max(abs(np.nan_to_num(lr_ab)), abs(np.nan_to_num(lr_ba))) >= MIN_CORR
            if not keep:
                continue
            if abs(np.nan_to_num(lr_ab)) >= abs(np.nan_to_num(lr_ba)):
                leader, follower, lrho, lagk = a, b, lr_ab, lg_ab
            else:
                leader, follower, lrho, lagk = b, a, lr_ba, lg_ba
            pairs.append({
                "a": a, "b": b,
                "rho60": None if r60 is None else round(float(r60), 3),
                "rho252": None if r252 is None else round(float(r252), 3),
                "leader": leader, "follower": follower,
                "lead_lag": lagk,
                "lead_rho": None if np.isnan(lrho) else round(float(lrho), 3),
            })

    neigh: dict[str, list[dict]] = {c: [] for c in cols}
    for p in pairs:
        r = p["rho60"] if p["rho60"] is not None else p["rho252"]
        if r is None:
            continue
        neigh[p["a"]].append({"id": p["b"], "rho60": p["rho60"], "rho252": p["rho252"],
                              "leader": p["leader"], "lead_lag": p["lead_lag"],
                              "lead_rho": p["lead_rho"]})
        neigh[p["b"]].append({"id": p["a"], "rho60": p["rho60"], "rho252": p["rho252"],
                              "leader": p["leader"], "lead_lag": p["lead_lag"],
                              "lead_rho": p["lead_rho"]})
    for c in neigh:
        neigh[c].sort(key=lambda x: -abs(x["rho60"] if x["rho60"] is not None
                                         else (x["rho252"] or 0)))
        neigh[c] = neigh[c][:NEIGHBOURS_TOP]

    state = {
        "updated": datetime.now(timezone.utc).isoformat(),
        "data_date": prices.index.max().strftime("%Y-%m-%d"),
        "window": CORR_WINDOW, "context": CORR_CONTEXT, "max_lag": MAX_LAG,
        "series": cols, "pairs": pairs, "neighbours": neigh,
    }
    RELATIONS_JSON.write_text(json.dumps(state), encoding="utf-8")
    return state


def load_relations() -> dict:
    if not RELATIONS_JSON.exists():
        return {}
    try:
        return json.loads(RELATIONS_JSON.read_text(encoding="utf-8"))
    except Exception:
        return {}


def neighbours(sid: str, relations: dict | None = None) -> list[dict]:
    rel = relations if relations is not None else load_relations()
    return rel.get("neighbours", {}).get(sid, [])


def laggards_for(member_ids: list[str], snapshot_by_id: dict,
                 relations: dict | None = None, top: int = 5) -> list[dict]:
    """Correlated (or lead-following) instruments that have NOT moved yet.
    Pure math — no LLM. Returns [{id, via, rho, lead_lag, z20}] ranked."""
    rel = relations if relations is not None else load_relations()
    members = set(member_ids)
    out: dict[str, dict] = {}
    for m in member_ids:
        for nb in neighbours(m, rel):
            nid = nb["id"]
            if nid in members or nid in out:
                continue
            row = snapshot_by_id.get(nid)
            if not row or row.get("z20") is None:
                continue
            rho = nb["rho60"] if nb["rho60"] is not None else nb["rho252"]
            qualifies = (rho is not None and abs(rho) >= LAGGARD_MIN_CORR) or \
                        (nb.get("leader") == m and
                         abs(nb.get("lead_rho") or 0) >= MIN_CORR)
            if not qualifies:
                continue
            if abs(row["z20"]) >= LAGGARD_MAX_Z:
                continue  # it already moved — not a laggard
            out[nid] = {
                "id": nid, "via": m,
                "rho": rho,
                "leads": nb.get("leader") == m,
                "lead_lag": nb.get("lead_lag"),
                "lead_rho": nb.get("lead_rho"),
                "z20": round(row["z20"], 2),
            }
    ranked = sorted(out.values(),
                    key=lambda x: -(abs(x["rho"] or 0) +
                                    (0.2 if x["leads"] else 0)))
    return ranked[:top]


if __name__ == "__main__":
    st = build_relations()
    print(f"relations: {len(st['series'])} series, {len(st['pairs'])} pairs "
          f"(|rho|>={MIN_CORR}), data through {st['data_date']}")
    for sid in ("sp500", "brent", "usd_inr", "hy_oas"):
        ns = neighbours(sid, st)[:4]
        print(f"  {sid}: " + ", ".join(
            f"{n['id']}({n['rho60']})" for n in ns) if ns else f"  {sid}: -")
    # laggard smoke test against the live snapshot
    from engine import build_snapshot
    from events import build_events
    from headlines import recent_items
    snap = build_snapshot()
    prices = pd.read_csv(PRICES_CSV, index_col=0, parse_dates=True)
    ev = build_events(snap, prices, recent_items())
    by_id = {r["id"]: r for r in snap["series"]}
    for e in ev["events"][:3]:
        lg = laggards_for([m["id"] for m in e["members"]], by_id, st)
        print(f"  event '{e['label']}' laggards: " +
              (", ".join(f"{l['id']}(rho {l['rho']}, z {l['z20']})" for l in lg) or "none"))
