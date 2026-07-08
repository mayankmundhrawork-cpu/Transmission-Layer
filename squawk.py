"""Squawk feed — DeItaone / Walter Bloomberg headlines (v6).

X has no free API lane, but DeItaone mirrors to a public Telegram channel
whose web preview (t.me/s/walter_bloomberg) serves the last ~20 messages
without auth. Zero-budget, no keys.

Two consumption modes:
  - the app pulls live with a 120s cache (the accepted ~2-min lag) so the
    panel is near-realtime while someone is watching;
  - the scheduled job persists into data/squawk.json (rolling 48h) and
    injects items into the headline store (feed='DeItaone') so extraction,
    the universe, and event news-matching all see squawk headlines.

Run: python squawk.py
"""
from __future__ import annotations

import hashlib
import html as _html
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

DATA_DIR = Path(__file__).parent / "data"
SQUAWK_JSON = DATA_DIR / "squawk.json"

CHANNEL_URLS = [
    "https://t.me/s/walter_bloomberg",   # primary mirror of @DeItaone
]
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
WINDOW_HOURS = 48
MAX_ITEMS = 400

_MSG_RE = re.compile(
    r'data-post="([^"]+)".*?class="tgme_widget_message_text[^"]*" dir="auto">'
    r'(.*?)</div>.*?<time datetime="([^"]+)"', re.S)
_TAG_RE = re.compile(r"<[^>]+>")


def _clean(fragment: str) -> str:
    text = _html.unescape(_TAG_RE.sub(" ", fragment))
    text = re.sub(r"\s+", " ", text).strip()
    # strip channel-suffix noise and lead sirens — the board has no emoji
    text = re.sub(r"@walter_bloomberg(\s*\|\s*Source)?", "", text, flags=re.I)
    text = re.sub(r"^[\W_]+", "", text)  # leading emoji/symbols
    return text.strip(" |·-")


def fetch_live(timeout: int = 12) -> list[dict]:
    """Last ~20 squawk messages, newest last. [] on any failure — a dead
    mirror must never break the board."""
    for url in CHANNEL_URLS:
        try:
            r = requests.get(url, headers=UA, timeout=timeout)
            if not r.ok:
                continue
            out = []
            for post, frag, ts in _MSG_RE.findall(r.text):
                text = _clean(frag)
                if not text:
                    continue
                out.append({
                    "id": hashlib.sha1(post.encode()).hexdigest()[:12],
                    "post": post,
                    "ts": ts,  # ISO with offset from telegram
                    "text": text[:500],
                })
            if out:
                return out
        except Exception as e:
            print(f"  WARN squawk fetch failed {url}: {str(e)[:100]}", file=sys.stderr)
    return []


def load_squawk() -> list[dict]:
    if SQUAWK_JSON.exists():
        try:
            return json.loads(SQUAWK_JSON.read_text(encoding="utf-8")).get("items", [])
        except Exception:
            pass
    return []


def pull_and_store() -> dict:
    """Persist live squawk into the rolling store + inject into the headline
    store so the universe/extraction/news-matching pipeline sees it."""
    live = fetch_live()
    items = load_squawk()
    known = {it["id"] for it in items}
    new = [it for it in live if it["id"] not in known]
    items.extend(new)

    cutoff = (datetime.now(timezone.utc) - timedelta(hours=WINDOW_HOURS))
    def _keep(it):
        try:
            return datetime.fromisoformat(it["ts"]) >= cutoff
        except Exception:
            return True
    items = sorted([it for it in items if _keep(it)],
                   key=lambda x: x["ts"])[-MAX_ITEMS:]
    DATA_DIR.mkdir(exist_ok=True)
    SQUAWK_JSON.write_text(json.dumps({
        "updated": datetime.now(timezone.utc).isoformat(), "items": items,
    }), encoding="utf-8")

    # inject new items into the headline store (same schema as RSS items)
    injected = 0
    if new:
        try:
            from headlines import HEADLINES_JSON, _hid, load_store
            store = load_store()
            ids = {i["id"] for i in store["items"]}
            for it in new:
                hid = _hid(it["text"])
                if hid in ids:
                    continue
                try:
                    ts = datetime.fromisoformat(it["ts"]).astimezone(timezone.utc)
                except Exception:
                    ts = datetime.now(timezone.utc)
                store["items"].append({
                    "id": hid, "ts": ts.isoformat(), "market": "USA",
                    "feed": "DeItaone", "title": it["text"][:300],
                    "link": f'https://t.me/{it["post"]}',
                })
                ids.add(hid)
                injected += 1
            store["items"].sort(key=lambda x: x["ts"], reverse=True)
            HEADLINES_JSON.write_text(json.dumps(store, indent=1), encoding="utf-8")
        except Exception as e:
            print(f"  WARN squawk->headlines inject failed: {str(e)[:120]}",
                  file=sys.stderr)
    return {"live": len(live), "new": len(new), "stored": len(items),
            "injected": injected}


if __name__ == "__main__":
    rep = pull_and_store()
    print(f"squawk: live={rep['live']} new={rep['new']} stored={rep['stored']} "
          f"injected->headlines={rep['injected']}")
    for it in load_squawk()[-5:]:
        print(f"  {it['ts'][:16]}  {it['text'][:90]}")
