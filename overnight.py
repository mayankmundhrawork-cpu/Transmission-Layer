"""Overnight research pass — the zero-work-default orchestrator (v5).

Runs in the scheduled job AFTER fetch+digest so that when the board is opened
in the morning, everything expensive is already computed:

  1. relations refresh (correlation + lead-lag)      -> data/relations.json
  2. events -> laggards + historical analogues       -> data/pattern_cache.json
  3. research bundles (+ budgeted article fetches)   -> data/research_bundles.json
  4. theses (free-LLM or skeleton, cached)           -> data/theses.json

Every step is fail-soft: one broken stage prints a warning and the rest
still complete. Run: python overnight.py
"""
from __future__ import annotations

import sys
import traceback

import pandas as pd

from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"


def main() -> int:
    # 1 · relations
    try:
        from relations import build_relations
        rel = build_relations()
        print(f"relations: {len(rel['pairs'])} pairs over {len(rel['series'])} series")
    except Exception:
        print("WARN relations failed:\n" + traceback.format_exc()[-500:], file=sys.stderr)
        rel = {}

    # shared inputs
    try:
        from engine import build_snapshot
        from events import build_events
        from headlines import recent_items
        snap = build_snapshot()
        prices = pd.read_csv(DATA_DIR / "prices.csv", index_col=0, parse_dates=True)
        hl = recent_items()
        ev = build_events(snap, prices, hl)
        by_id = {r["id"]: r for r in snap["series"]}
        print(f"events: {len(ev['events'])} surfaced")
    except Exception:
        print("FATAL snapshot/events failed:\n" + traceback.format_exc()[-500:],
              file=sys.stderr)
        return 1

    # 1b · squawk persist + inject (DeItaone mirror)
    try:
        from squawk import pull_and_store
        srep = pull_and_store()
        print(f"squawk: live={srep['live']} new={srep['new']} "
              f"injected={srep['injected']}")
    except Exception:
        print("WARN squawk failed:\n" + traceback.format_exc()[-400:], file=sys.stderr)

    # 2 · laggards + analogues + India receivers per event
    lag_by, ana_by, ind_by = {}, {}, {}
    try:
        from india import india_receivers
        from patterns import analogues_for_event
        from relations import laggards_for, load_relations
        from research import event_key
        relx = rel or load_relations()
        for e in ev["events"]:
            mids = [m["id"] for m in e["members"]]
            k = event_key(mids)
            try:
                lag_by[k] = laggards_for(mids, by_id, relx)
                ana_by[k] = analogues_for_event(mids, prices)
                ind_by[k] = india_receivers(mids, by_id, relx)
            except Exception:
                lag_by.setdefault(k, [])
                ana_by.setdefault(k, {})
                ind_by.setdefault(k, [])
        print(f"analogues+laggards+india: {len(ana_by)} events prepared")
    except Exception:
        print("WARN analogue stage failed:\n" + traceback.format_exc()[-500:],
              file=sys.stderr)

    # 3 · research bundles (article fetches inside are budget-capped)
    bundles = {"bundles": {}}
    try:
        from research import build_bundles
        bundles = build_bundles(ev["events"], hl, ana_by)
        print(f"bundles: {len(bundles['bundles'])} events, "
              f"fetched {bundles.get('fetched', 0)} articles "
              f"({bundles.get('cache_hits', 0)} cache hits)")
    except Exception:
        print("WARN bundles failed:\n" + traceback.format_exc()[-500:], file=sys.stderr)

    # 4 · theses
    try:
        from thesis import build_theses
        state = build_theses(ev["events"], lag_by, ana_by, bundles, ind_by)
        lr = state["ledger"]["last_run"]
        print(f"theses: backend={lr['backend']} llm_calls={lr['llm_calls']} "
              f"generated={lr['generated']} skeletons={lr['skeletons']} "
              f"kept={lr['cache_kept']} cost=${lr['cost_usd']}")
    except Exception:
        print("WARN theses failed:\n" + traceback.format_exc()[-500:], file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
