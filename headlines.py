"""Rolling headline store — the raw material the universe assembles from.

Pulls every RSS feed in rss_sources.RSS_FEEDS (same graceful-degradation rule
as the digest: a dead feed logs a warning and is skipped, never crashes the
run) and maintains data/headlines.json, a deduplicated rolling window of the
last HEADLINE_WINDOW_DAYS of headlines.

Run:  python headlines.py   (also invoked by update_universe.py)
"""
from __future__ import annotations

import hashlib
import json
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

from rss_sources import RSS_FEEDS
from settings import HEADLINE_WINDOW_DAYS

DATA_DIR = Path(__file__).parent / "data"
HEADLINES_JSON = DATA_DIR / "headlines.json"
MAX_ITEMS = 2500  # hard cap on the store


def _entry_dt(entry) -> datetime | None:
    for key in ("published_parsed", "updated_parsed"):
        t = getattr(entry, key, None)
        if t:
            try:
                return datetime.fromtimestamp(time.mktime(t), tz=timezone.utc)
            except (OverflowError, ValueError):
                return None
    return None


def _hid(title: str) -> str:
    return hashlib.sha1(title.strip().lower().encode("utf-8")).hexdigest()[:12]


def load_store() -> dict:
    if not HEADLINES_JSON.exists():
        return {"updated": None, "items": []}
    try:
        return json.loads(HEADLINES_JSON.read_text(encoding="utf-8"))
    except Exception:
        return {"updated": None, "items": []}


def recent_items(hours: float | None = None) -> list[dict]:
    """Items from the store, optionally restricted to the last N hours."""
    items = load_store().get("items", [])
    if hours is None:
        return items
    cutoff = (datetime.now(timezone.utc) - timedelta(hours=hours)).isoformat()
    return [it for it in items if it["ts"] >= cutoff]


def pull_and_update() -> dict:
    """Pull all feeds, merge into the rolling store, return a run report."""
    import feedparser

    now = datetime.now(timezone.utc)
    store = load_store()
    by_id = {it["id"]: it for it in store["items"]}
    known = set(by_id)
    report = {"ok": [], "failed": [], "empty": [], "new_items": 0}

    for market, feeds in RSS_FEEDS.items():
        for feed in feeds:
            name, url = feed["name"], feed["url"]
            try:
                parsed = feedparser.parse(url)
                entries = parsed.entries
            except Exception as e:  # never crash the run on one feed
                report["failed"].append({"feed": name, "error": str(e)[:160]})
                print(f"  WARN feed failed [{market}] {name}: {e}", file=sys.stderr)
                continue
            if not entries:
                report["empty"].append({"feed": name})
                continue
            added = 0
            for e in entries:
                title = (getattr(e, "title", None) or "").strip()
                if not title:
                    continue
                hid = _hid(title)
                link = (getattr(e, "link", None) or "").strip()
                if hid in known:
                    # backfill links onto items stored before the link field
                    if link and not by_id[hid].get("link"):
                        by_id[hid]["link"] = link
                    continue
                dt = _entry_dt(e) or now
                # clamp future-stamped items to now
                if dt > now:
                    dt = now
                store["items"].append({
                    "id": hid,
                    "ts": dt.isoformat(),
                    "market": market,
                    "feed": name,
                    "title": title,
                    "link": link,
                })
                known.add(hid)
                added += 1
            report["ok"].append({"feed": name, "new": added})
            report["new_items"] += added

    # roll the window
    cutoff = (now - timedelta(days=HEADLINE_WINDOW_DAYS)).isoformat()
    store["items"] = [it for it in store["items"] if it["ts"] >= cutoff]
    store["items"].sort(key=lambda it: it["ts"], reverse=True)
    store["items"] = store["items"][:MAX_ITEMS]
    store["updated"] = now.isoformat()

    DATA_DIR.mkdir(exist_ok=True)
    HEADLINES_JSON.write_text(json.dumps(store, indent=1), encoding="utf-8")
    report["total_items"] = len(store["items"])
    return report


def main() -> int:
    rep = pull_and_update()
    print(f"headlines: +{rep['new_items']} new, {rep['total_items']} in "
          f"{HEADLINE_WINDOW_DAYS}d window · feeds ok {len(rep['ok'])} / "
          f"failed {len(rep['failed'])} / empty {len(rep['empty'])}")
    for f in rep["failed"]:
        print(f"  FAIL {f['feed']}: {f['error']}")
    for f in rep["empty"]:
        print(f"  EMPTY {f['feed']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
