"""The self-assembling universe — Layer 1 state machine.

Reads the headline store, extracts candidate entities, scores mentions with an
exponential decay, admits qualified candidates through the resolver, ages and
evicts quiet members, and persists everything to data/universe.json.

Stability guarantees (anti-churn):
- mentions accumulate across runs (EWMA, half-life settings.DECAY_HALF_LIFE_DAYS)
- admission needs ≥ADMIT_SCORE score AND ≥ADMIT_MIN_FEEDS distinct feeds
- eviction needs BOTH a decayed score AND EVICT_QUIET_DAYS without a mention
- a currently-flagged member is never evicted (the board is watching it)
- every headline is counted at most once (processed-id ledger)
- resolutions are cached forever, so readmission after eviction is free
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from extract import extract, normalize
from headlines import load_store
from resolve import load_cache, resolve, save_cache
from settings import (ADMIT_MIN_FEEDS, ADMIT_SCORE, DECAY_HALF_LIFE_DAYS,
                      DYNAMIC_AMBER_Z, EVICT_QUIET_DAYS, EVICT_SCORE,
                      MAX_LOOKUPS_PER_RUN, UNIVERSE_CAP)

DATA_DIR = Path(__file__).parent / "data"
UNIVERSE_JSON = DATA_DIR / "universe.json"

MAX_CANDIDATES = 300
MAX_EVIDENCE = 5
CLS_BUCKET = {"equity": "EQUITIES", "etf": "EQUITIES",
              "commodity": "COMMODITIES", "crypto": "CRYPTO"}


def _now() -> datetime:
    return datetime.now(timezone.utc)


def load_state() -> dict:
    if UNIVERSE_JSON.exists():
        try:
            return json.loads(UNIVERSE_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"updated": None, "processed_ids": [], "members": {}, "candidates": {}}


def save_state(state: dict) -> None:
    DATA_DIR.mkdir(exist_ok=True)
    UNIVERSE_JSON.write_text(json.dumps(state, indent=1, sort_keys=True),
                             encoding="utf-8")


def _decay_factor(state: dict, now: datetime) -> float:
    if not state.get("updated"):
        return 1.0
    try:
        prev = datetime.fromisoformat(state["updated"])
        days = max((now - prev).total_seconds() / 86400.0, 0.0)
        return 0.5 ** (days / DECAY_HALF_LIFE_DAYS)
    except Exception:
        return 1.0


def _member_terms(m: dict) -> list[str]:
    """Lowercase substrings that count as a mention of this member."""
    terms = set()
    norm = m.get("norm") or normalize(m.get("name", ""))
    for tok in norm.split():
        if len(tok) >= 4:
            terms.add(tok)
    if len(norm) >= 4:
        terms.add(norm)
    return sorted(terms)


def _push_evidence(target: list, item: dict) -> None:
    if any(e["title"] == item["title"] for e in target):
        return
    target.insert(0, {"ts": item["ts"], "feed": item["feed"], "title": item["title"]})
    del target[MAX_EVIDENCE:]


def _flagged_dynamic_symbols() -> set[str]:
    """Symbols of currently-flagged dynamic series (never evict these).
    Uses the committed prices.csv via the engine; failure → empty set."""
    try:
        from engine import build_snapshot
        from registry import registry_index
        idx = registry_index()
        snap = build_snapshot()
        out = set()
        for r in snap.get("series", []):
            if r.get("flag") in ("amber", "red"):
                spec = idx.get(r["id"])
                if spec and spec.get("dynamic"):
                    out.add(spec["symbol"])
        return out
    except Exception as e:
        print(f"  WARN flag-protection check failed: {str(e)[:120]}", file=sys.stderr)
        return set()


def update_universe() -> dict:
    """One scheduled-run update. Returns a human-readable report dict."""
    now = _now()
    state = load_state()
    store = load_store()
    items = store.get("items", [])

    processed = set(state.get("processed_ids", []))
    new_items = [it for it in items if it["id"] not in processed]

    # 1 · decay every score by elapsed time
    decay = _decay_factor(state, now)
    for m in state["members"].values():
        m["score"] = round(m.get("score", 0.0) * decay, 4)
    for c in state["candidates"].values():
        c["score"] = round(c.get("score", 0.0) * decay, 4)

    # 2 · count member mentions in the NEW headlines
    member_mentions = 0
    for m in state["members"].values():
        terms = _member_terms(m)
        for it in new_items:
            tl = it["title"].lower()
            if any(t in tl for t in terms):
                m["score"] = m.get("score", 0.0) + 1.0
                m["last_mention"] = it["ts"]
                _push_evidence(m.setdefault("evidence", []), it)
                member_mentions += 1

    # 3 · extract candidates from the NEW headlines
    member_norms = {m.get("norm") for m in state["members"].values()}
    extracted = extract(new_items) if new_items else {}
    for norm, c in extracted.items():
        if norm in member_norms:
            continue
        cand = state["candidates"].setdefault(norm, {
            "display": c["display"], "score": 0.0, "feeds": [],
            "first_seen": now.isoformat(), "evidence": [],
        })
        cand["score"] = cand.get("score", 0.0) + len(c["mentions"])
        cand["last_seen"] = now.isoformat()
        if c.get("ticker_hint"):
            cand["ticker_hint"] = c["ticker_hint"]
        if c.get("cls_hint"):
            cand["cls_hint"] = c["cls_hint"]
        feeds = set(cand.get("feeds", []))
        for mnt in c["mentions"]:
            feeds.add(mnt["feed"])
            _push_evidence(cand["evidence"], mnt)
        cand["feeds"] = sorted(feeds)

    # 4 · admission — resolve qualified candidates within the lookup budget
    admitted, rejected, deferred = [], [], []
    cache = load_cache()
    budget = MAX_LOOKUPS_PER_RUN
    member_symbols = set(state["members"].keys())
    qualified = sorted(
        [(norm, c) for norm, c in state["candidates"].items()
         if c["score"] >= ADMIT_SCORE and len(c.get("feeds", [])) >= ADMIT_MIN_FEEDS],
        key=lambda kv: -kv[1]["score"])
    for norm, c in qualified:
        res = resolve(norm, c["display"], ticker_hint=c.get("ticker_hint"),
                      cls_hint=c.get("cls_hint"), cache=cache,
                      allow_network=budget > 0)
        if not res.get("cached"):
            budget -= 1
        if res.get("deferred"):
            deferred.append(c["display"])
            continue
        if res.get("via") == "network-error":
            deferred.append(c["display"])  # transient — retry next run
            continue
        del state["candidates"][norm]
        if not res.get("ok"):
            rejected.append(c["display"])
            continue
        sym = res["symbol"]
        if sym in member_symbols:
            ex = state["members"][sym]  # same instrument, another alias
            ex["score"] = ex.get("score", 0.0) + c["score"]
            for e in c.get("evidence", []):
                _push_evidence(ex.setdefault("evidence", []), e)
            continue
        bucket = CLS_BUCKET.get(res.get("cls", "equity"), "EQUITIES")
        state["members"][sym] = {
            "name": res.get("shortname") or c["display"],
            "norm": norm,
            "cls": bucket,
            "status": "active",
            "score": round(c["score"], 4),
            "added": now.isoformat(),
            "last_mention": (c.get("evidence") or [{}])[0].get("ts", now.isoformat()),
            "evidence": c.get("evidence", []),
            "amber_z": DYNAMIC_AMBER_Z,
            "via": res.get("via"),
        }
        member_symbols.add(sym)
        admitted.append(f"{c['display']} -> {sym}")
    save_cache(cache)

    # 5 · eviction — decayed AND quiet AND not currently flagged
    protected = _flagged_dynamic_symbols()
    evicted = []
    for sym in list(state["members"].keys()):
        m = state["members"][sym]
        if sym in protected:
            continue
        try:
            quiet_days = (now - datetime.fromisoformat(m["last_mention"])).days
        except Exception:
            quiet_days = 0
        if m.get("score", 0.0) < EVICT_SCORE and quiet_days > EVICT_QUIET_DAYS:
            evicted.append(f"{m['name']} ({sym})")
            del state["members"][sym]

    # 6 · cap — drop lowest-score non-flagged overflow
    active = [(s, m) for s, m in state["members"].items()]
    if len(active) > UNIVERSE_CAP:
        active.sort(key=lambda kv: kv[1].get("score", 0.0))
        for sym, m in active:
            if len(state["members"]) <= UNIVERSE_CAP:
                break
            if sym in protected:
                continue
            evicted.append(f"{m['name']} ({sym}) [cap]")
            del state["members"][sym]

    # 7 · prune candidates + roll the processed ledger
    state["candidates"] = dict(sorted(
        ((n, c) for n, c in state["candidates"].items() if c["score"] >= 0.15),
        key=lambda kv: -kv[1]["score"])[:MAX_CANDIDATES])
    store_ids = {it["id"] for it in items}
    processed |= {it["id"] for it in new_items}
    state["processed_ids"] = sorted(processed & store_ids)
    state["updated"] = now.isoformat()
    save_state(state)

    return {
        "new_headlines": len(new_items),
        "member_mentions": member_mentions,
        "members": len(state["members"]),
        "candidates": len(state["candidates"]),
        "admitted": admitted,
        "rejected": rejected,
        "deferred": deferred,
        "evicted": evicted,
        "lookup_budget_left": budget,
    }


if __name__ == "__main__":
    rep = update_universe()
    print(json.dumps(rep, indent=2))
