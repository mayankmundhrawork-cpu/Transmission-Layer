"""India transmission lens (v6).

The board's editorial core: global signal -> Indian expression. This module
answers, for any event, "which INDIAN instruments receive this move, at what
correlation/lead, and have they reacted yet?" — pure math over the relations
substrate, surfaced on every event card and fed into the thesis prompt.
"""
from __future__ import annotations

from registry import registry_index
from relations import load_relations, neighbours

# Backbone ids that ARE the Indian complex.
INDIA_STATIC = {
    "nifty_50", "nifty_midcap_100", "nifty_fmcg", "nifty_metal", "nifty_it",
    "usd_inr", "eur_inr", "goi_10y", "goi_ust_spread",
    "midcap_largecap_ratio", "india_cpi_yoy",
}
MIN_RHO = 0.35
REACTED_Z = 1.0


def india_ids() -> set[str]:
    """Static Indian complex + any news-admitted member listed on NSE/BSE."""
    out = set(INDIA_STATIC)
    for sid, spec in registry_index().items():
        sym = (spec.get("symbol") or "").upper()
        if spec.get("dynamic") and (sym.endswith(".NS") or sym.endswith(".BO")):
            out.add(sid)
    return out


def india_receivers(member_ids: list[str], snapshot_by_id: dict,
                    relations: dict | None = None, top: int = 5) -> list[dict]:
    """Indian instruments most exposed to the event's members, ranked by
    |rho| (+ lead bonus). Each carries whether it has already reacted."""
    rel = relations if relations is not None else load_relations()
    indian = india_ids()
    members = set(member_ids)
    out: dict[str, dict] = {}
    for m in member_ids:
        for nb in neighbours(m, rel):
            nid = nb["id"]
            if nid not in indian or nid in members:
                continue
            rho = nb["rho60"] if nb["rho60"] is not None else nb["rho252"]
            lead = (nb.get("leader") == m and
                    abs(nb.get("lead_rho") or 0) >= MIN_RHO)
            if (rho is None or abs(rho) < MIN_RHO) and not lead:
                continue
            row = snapshot_by_id.get(nid) or {}
            z = row.get("z20")
            score = abs(rho or 0) + (0.2 if lead else 0)
            if nid in out and out[nid]["_score"] >= score:
                continue
            out[nid] = {
                "id": nid, "via": m, "rho": rho,
                "leads": lead, "lead_lag": nb.get("lead_lag"),
                "z20": None if z is None else round(z, 2),
                "reacted": (z is not None and abs(z) >= REACTED_Z),
                "_score": score,
            }
    ranked = sorted(out.values(), key=lambda x: -x["_score"])[:top]
    for r in ranked:
        r.pop("_score", None)
    return ranked


def format_receivers(recv: list[dict]) -> str:
    """One-line plain-text rendering for thesis prompts / digest."""
    if not recv:
        return ""
    parts = []
    for r in recv:
        state = "reacted" if r["reacted"] else "quiet"
        lead = f", leads {r['lead_lag']}d" if r["leads"] else ""
        parts.append(f"{r['id']} (rho {r['rho']} via {r['via']}{lead}, "
                     f"z {r['z20']}, {state})")
    return "; ".join(parts)


if __name__ == "__main__":
    import pandas as pd
    from pathlib import Path
    from engine import build_snapshot
    from events import build_events
    from headlines import recent_items
    snap = build_snapshot()
    prices = pd.read_csv(Path("data/prices.csv"), index_col=0, parse_dates=True)
    ev = build_events(snap, prices, recent_items())
    by_id = {r["id"]: r for r in snap["series"]}
    rel = load_relations()
    for e in ev["events"]:
        recv = india_receivers([m["id"] for m in e["members"]], by_id, rel)
        print(f"[{e['level']}] {e['label']}")
        print("   -> INDIA:", format_receivers(recv) or "no exposed receivers")
