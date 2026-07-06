"""Deep-link research bundles per event (v5 feature 2).

For every surfaced event, assembles:
  - motivating headlines with LINKS + clean-text excerpts (fetched once,
    cached forever in data/articles/; paywalls keep whatever pre-paywall
    text the extractor recovers — zero-budget heuristics, no services)
  - primary-source links for the underlying data (FRED page per series,
    exchange/Yahoo quote page, official release pages)
  - pre-formatted citations ready to paste into a draft
Written overnight to data/research_bundles.json; the app only reads.

Run: python research.py   (builds bundles for the current live events)
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import time
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

import requests

from registry import registry_index
from settings import (ARTICLE_FETCH_MAX_PER_RUN, ARTICLE_MAX_CHARS,
                      ARTICLE_TIMEOUT)

DATA_DIR = Path(__file__).parent / "data"
ARTICLES_DIR = DATA_DIR / "articles"
BUNDLES_JSON = DATA_DIR / "research_bundles.json"

UA = {"User-Agent": "TransmissionLayer/1.0 (personal research board; "
                    "polite cache; contact: repo owner)"}
FETCH_SPACING = 1.0
PAYWALL_MARKERS = [
    "subscribe to read", "subscribe to continue", "sign in to read",
    "to continue reading", "premium subscribers", "is a premium article",
    "start your free trial", "already a subscriber",
]

# Primary-source landing pages per series class / id.
PRIMARY_STATIC = {
    "wti":   ("EIA Weekly Petroleum Status", "https://www.eia.gov/petroleum/supply/weekly/"),
    "brent": ("EIA Weekly Petroleum Status", "https://www.eia.gov/petroleum/supply/weekly/"),
    "natgas": ("EIA Natural Gas Weekly", "https://www.eia.gov/naturalgas/weekly/"),
    "usd_inr": ("RBI Weekly Statistical Supplement", "https://www.rbi.org.in/Scripts/WSSView.aspx"),
    "nifty_50": ("NSE India reports", "https://www.nseindia.com/market-data/live-equity-market"),
    "vix": ("CBOE VIX dashboard", "https://www.cboe.com/tradable_products/vix/"),
    "wheat": ("CFTC Commitments of Traders", "https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm"),
    "corn": ("CFTC Commitments of Traders", "https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm"),
    "soybeans": ("CFTC Commitments of Traders", "https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm"),
    "comex_gold": ("CFTC Commitments of Traders", "https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm"),
}


# ── article text extraction (stdlib heuristic) ─────────────────────────
class _TextExtract(HTMLParser):
    SKIP = {"script", "style", "nav", "header", "footer", "aside", "form",
            "button", "figure", "noscript", "svg", "iframe"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.paras: list[str] = []
        self._buf: list[str] = []
        self._skip_depth = 0
        self._in_p = False
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self._skip_depth += 1
        elif tag == "p" and self._skip_depth == 0:
            self._in_p, self._buf = True, []
        elif tag == "title":
            self._in_title = True
        elif tag == "meta" and not self.title:
            d = dict(attrs)
            if d.get("property") in ("og:title",) and d.get("content"):
                self.title = d["content"].strip()

    def handle_endtag(self, tag):
        if tag in self.SKIP and self._skip_depth:
            self._skip_depth -= 1
        elif tag == "p" and self._in_p:
            text = re.sub(r"\s+", " ", "".join(self._buf)).strip()
            if len(text) >= 40:  # drop boilerplate crumbs
                self.paras.append(text)
            self._in_p = False
        elif tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_p and self._skip_depth == 0:
            self._buf.append(data)
        elif self._in_title and not self.title:
            self.title += data


def _extract(html: str) -> tuple[str, str]:
    p = _TextExtract()
    try:
        p.feed(html)
    except Exception:
        pass
    text = "\n\n".join(p.paras)[:ARTICLE_MAX_CHARS]
    return (p.title or "").strip()[:200], text


def _akey(url: str) -> str:
    return hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]


def fetch_article(url: str) -> dict:
    """Fetch-once article cache. Returns {status, title, text, fetched_at}.
    status: ok | partial(paywall, pre-paywall text kept) | error | skipped."""
    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
    f = ARTICLES_DIR / f"{_akey(url)}.json"
    if f.exists():
        try:
            return json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            pass
    rec = {"url": url, "fetched_at": datetime.now(timezone.utc).isoformat(),
           "status": "error", "title": "", "text": ""}
    try:
        r = requests.get(url, headers=UA, timeout=ARTICLE_TIMEOUT,
                         allow_redirects=True)
        if r.status_code in (401, 402, 403):
            rec["status"] = "skipped"
        elif r.ok and "html" in (r.headers.get("content-type") or "html"):
            title, text = _extract(r.text)
            rec["title"], rec["text"] = title, text
            low = r.text[:20000].lower()
            paywalled = any(m in low for m in PAYWALL_MARKERS)
            if paywalled:
                # zero-budget rule: keep whatever renders before the wall
                rec["status"] = "partial" if len(text) >= 200 else "skipped"
            else:
                rec["status"] = "ok" if len(text) >= 300 else "partial"
    except Exception as e:
        rec["error"] = str(e)[:120]
    f.write_text(json.dumps(rec), encoding="utf-8")
    return rec


# ── primary sources ────────────────────────────────────────────────────
def primary_sources(member_ids: list[str]) -> list[dict]:
    idx = registry_index()
    out, seen = [], set()
    for sid in member_ids:
        spec = idx.get(sid)
        if not spec:
            continue
        links: list[tuple[str, str]] = []
        if spec.get("source") == "fred":
            links.append((f"FRED · {spec['symbol']}",
                          f"https://fred.stlouisfed.org/series/{spec['symbol']}"))
        elif spec.get("source") == "yfinance":
            links.append((f"Yahoo · {spec['symbol']}",
                          f"https://finance.yahoo.com/quote/{spec['symbol'].replace('^', '%5E')}"))
        if sid in PRIMARY_STATIC:
            links.append(PRIMARY_STATIC[sid])
        for name, url in links:
            if url in seen:
                continue
            seen.add(url)
            out.append({"series": sid, "name": name, "url": url})
    return out


# ── bundle assembly ────────────────────────────────────────────────────
def event_key(members: list[str]) -> str:
    return hashlib.sha1("|".join(sorted(members)).encode()).hexdigest()[:12]


def _citation(title: str, feed: str, ts: str, url: str) -> str:
    d = (ts or "")[:10]
    return f"{title} — {feed}, {d}. {url}" if url else f"{title} — {feed}, {d}."


def build_bundles(events: list[dict], headlines: list[dict],
                  analogues_by_key: dict | None = None) -> dict:
    """Assemble bundles for the surfaced events; budget-capped article pulls."""
    by_id_link = {h["id"]: h.get("link", "") for h in headlines}
    budget = ARTICLE_FETCH_MAX_PER_RUN
    bundles = {}
    fetched, cached = 0, 0
    for e in events:
        members = [m["id"] for m in e["members"]]
        key = event_key(members)
        arts = []
        for n in e.get("news", []):
            url = ""
            for h in headlines:
                if h["title"] == n["title"]:
                    url = h.get("link", "") or by_id_link.get(h["id"], "")
                    break
            rec = None
            if url:
                had = (ARTICLES_DIR / f"{_akey(url)}.json").exists()
                if had or budget > 0:
                    rec = fetch_article(url)
                    if had:
                        cached += 1
                    else:
                        budget -= 1
                        fetched += 1
                        time.sleep(FETCH_SPACING)
            arts.append({
                "title": n["title"], "feed": n["feed"], "ts": n["ts"],
                "url": url,
                "status": (rec or {}).get("status", "no-link"),
                "excerpt": ((rec or {}).get("text") or "")[:700],
                "citation": _citation(n["title"], n["feed"], n["ts"], url),
            })
        bundles[key] = {
            "label": e["label"], "level": e["level"], "score": e["score"],
            "members": members,
            "articles": arts,
            "primary_sources": primary_sources(members),
            "analogues": (analogues_by_key or {}).get(key, {}),
            "built_at": datetime.now(timezone.utc).isoformat(),
        }
    out = {"updated": datetime.now(timezone.utc).isoformat(),
           "fetched": fetched, "cache_hits": cached, "bundles": bundles}
    BUNDLES_JSON.write_text(json.dumps(out), encoding="utf-8")
    return out


def load_bundles() -> dict:
    if BUNDLES_JSON.exists():
        try:
            return json.loads(BUNDLES_JSON.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"bundles": {}}


if __name__ == "__main__":
    import pandas as pd
    from engine import build_snapshot
    from events import build_events
    from headlines import recent_items
    snap = build_snapshot()
    prices = pd.read_csv(DATA_DIR / "prices.csv", index_col=0, parse_dates=True)
    hl = recent_items()
    ev = build_events(snap, prices, hl)
    out = build_bundles(ev["events"], hl)
    print(f"bundles: {len(out['bundles'])} events, fetched {out['fetched']} "
          f"articles, {out['cache_hits']} cache hits")
    for k, b in out["bundles"].items():
        print(f"\n[{b['level']}] {b['label']}")
        for a in b["articles"]:
            print(f"  {a['status']:8} {a['title'][:56]}")
            if a["excerpt"]:
                print(f"           excerpt: {a['excerpt'][:90]}...")
        for p in b["primary_sources"][:3]:
            print(f"  primary: {p['name']} -> {p['url']}")
