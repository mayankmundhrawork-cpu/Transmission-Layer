"""Morning digest assembler — Step 6 of the spec.

Pure concatenation, no intelligence (that happens when you paste it into chat).
Reads the proven data layer (engine.build_snapshot over data/prices.csv) for
metric state + fired flags, the release calendar for proximity, and live RSS for
headlines. Writes data/digest_latest.txt in the exact Step 6 format.

Every RSS feed is wrapped in try/except: a dead feed logs a warning and is
skipped, never crashing assembly. Run: python digest.py
"""
from __future__ import annotations

import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from engine import build_snapshot
from release_calendar import build_calendar
from rss_sources import MANUAL_BOOKMARKS, RSS_FEEDS

DATA_DIR = Path(__file__).parent / "data"
DIGEST_TXT = DATA_DIR / "digest_latest.txt"

# Digest market buckets, in display order.
DIGEST_MARKETS = ["USA", "INDIA", "EU", "CHINA", "COMMODITIES"]

WINDOW_HOURS = 24
MIN_PER_FEED = 2      # fallback: always keep at least this many most-recent items
MAX_PER_FEED = 6      # cap so one chatty feed does not flood a section
MAX_PER_MARKET = 12

# The fixed chat prompt paired with the digest (spec Step 6, verbatim).
CHAT_PROMPT = (
    "Here is my morning market digest. Do not summarise it. Identify only where "
    "a news item in [4] would mechanically move a metric in [1] in a direction "
    "that metric has NOT yet reflected — i.e. an event-to-price gap. For each, "
    "name the transmission chain and the instrument in my four-market universe "
    "that expresses it. Weight leading-indicator sources (physical, credit, "
    "positioning) over commentary. If there is no genuine gap, say so — a quiet "
    "day is a valid output."
)


def _entry_dt(entry) -> datetime | None:
    for key in ("published_parsed", "updated_parsed"):
        t = getattr(entry, key, None) or (entry.get(key) if hasattr(entry, "get") else None)
        if t:
            try:
                return datetime.fromtimestamp(time.mktime(t), tz=timezone.utc)
            except (OverflowError, ValueError):
                return None
    return None


def _pull_feed(url: str) -> list[dict]:
    """Return list of {title, dt} for a feed, newest first. Raises on hard failure."""
    import feedparser
    parsed = feedparser.parse(url)
    # feedparser sets .bozo on malformed feeds but often still yields entries;
    # only treat as failure when there are genuinely no entries.
    import html as _h
    items = []
    for e in parsed.entries:
        title = _h.unescape((getattr(e, "title", None) or "")).strip()
        if not title:
            continue
        items.append({"title": title, "dt": _entry_dt(e)})
    items.sort(key=lambda x: (x["dt"] is not None, x["dt"] or datetime.min.replace(tzinfo=timezone.utc)),
               reverse=True)
    return items


def gather_headlines() -> tuple[dict[str, list[str]], dict]:
    """Return ({market: [headline, ...]}, report) pulling every RSS feed."""
    now = datetime.now(timezone.utc)
    cutoff = now.timestamp() - WINDOW_HOURS * 3600
    out: dict[str, list[str]] = {m: [] for m in DIGEST_MARKETS}
    report = {"ok": [], "failed": [], "empty": []}

    for market in DIGEST_MARKETS:
        seen: set[str] = set()
        for feed in RSS_FEEDS.get(market, []):
            name, url = feed["name"], feed["url"]
            try:
                items = _pull_feed(url)
            except Exception as e:  # never crash assembly on a bad feed
                report["failed"].append({"market": market, "name": name, "error": str(e)[:160]})
                print(f"  WARN feed failed [{market}] {name}: {e}", file=sys.stderr)
                continue

            if not items:
                report["empty"].append({"market": market, "name": name})
                print(f"  WARN feed empty  [{market}] {name}", file=sys.stderr)
                continue

            # 24h window, with a most-recent-N fallback for clock-skew robustness.
            recent = [it for it in items
                      if it["dt"] is not None and it["dt"].timestamp() >= cutoff]
            if len(recent) < MIN_PER_FEED:
                recent = items[:MIN_PER_FEED]
            recent = recent[:MAX_PER_FEED]

            added = 0
            for it in recent:
                key = it["title"].lower()
                if key in seen:
                    continue
                seen.add(key)
                out[market].append(f"{it['title']}  — {name}")
                added += 1
            report["ok"].append({"market": market, "name": name, "headlines": added})

        out[market] = out[market][:MAX_PER_MARKET]

    return out, report


def _fmt_num(v, dp=2, suffix=""):
    if v is None:
        return "n/a"
    try:
        return f"{v:.{dp}f}{suffix}"
    except (TypeError, ValueError):
        return "n/a"


def assemble() -> tuple[str, dict]:
    snap = build_snapshot()
    cal = build_calendar()
    headlines, report = gather_headlines()

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    L: list[str] = []
    L.append(f"=== TRANSMISSION LAYER MORNING DIGEST — {today} ===")
    L.append("")

    # [0] REGIME & ASSUMPTION HEALTH — measured at generation time; every
    # transmission claim below is conditional on this block.
    try:
        from assumptions import load_assumptions_state
        from regime import load_regime
        reg = load_regime()
        L.append("[0] REGIME & ASSUMPTIONS (measured now, not assumed)")
        comp = reg.get("components", {})
        L.append(f"  Regime: {reg.get('label')} (score {reg.get('score')}, "
                 f"{reg.get('days_in_regime')}d) — vol-pct {comp.get('vol_pct')}, "
                 f"breadth-off {comp.get('breadth_off')}, "
                 f"P(high-vol) {reg.get('markov', {}).get('p_highvol')}")
        for name, a in load_assumptions_state().get("assumptions", {}).items():
            extra = ""
            if a.get("contra_corr20") is not None:
                extra = f", contra {a['contra_series']} corr20={a['contra_corr20']}"
            cp = f", shifted {a['last_changepoint']}" if a.get("last_changepoint") else ""
            L.append(f"  [{a['status']}] {name}: corr20={a['corr20']} "
                     f"corr60={a['corr60']}{extra}{cp}")
        L.append("")
    except Exception:
        pass

    # [1] METRIC STATE
    L.append("[1] METRIC STATE (as of last close)")
    L.append("  ID | last | 1d% | 5d% | 20d-z | zc | resid-z | 1yr-pct | flag | move")
    for r in snap.get("series", []):
        L.append(
            f"  {r['id']} | {_fmt_num(r['last'], 4)} | "
            f"{_fmt_num(r['d1_pct'], 2, '%')} | {_fmt_num(r['d5_pct'], 2, '%')} | "
            f"{_fmt_num(r['z20'], 2)} | {_fmt_num(r.get('zc'), 2)} | "
            f"{_fmt_num(r.get('resid_z'), 2)} | {_fmt_num(r['pct_1y'], 0)} | "
            f"{r['flag']} | {r.get('move_label', 'n/a')}"
        )
    L.append("")

    # [2] FLAGS FIRED
    L.append("[2] FLAGS FIRED")
    flags = snap.get("flags", [])
    if not flags:
        L.append("  No flags — calm session.")
    else:
        for f in flags:
            reason = "; ".join(f.get("reasons", []))
            L.append(f"  [{f['flag'].upper()}] {f['id']} ({f['type']}, {f['market']}) "
                     f"score={f['score']:.2f} — {reason}")
    L.append("")

    # [3] RELEASE PROXIMITY
    L.append("[3] RELEASE PROXIMITY")
    for r in cal["upcoming"][:5]:
        L.append(f"  T-{r['days_until']}d  {r['name']} — {r['threshold']}")
    if cal["recent"]:
        L.append("  Released in last 24h:")
        for r in cal["recent"]:
            L.append(f"    {r['name']} ({r['released_date']}) — {r['url']}")
    L.append("")

    # [4] NEWS by market
    L.append("[4] NEWS — headlines by market (from RSS, last 24h)")
    label = {"USA": "USA", "INDIA": "India", "EU": "EU", "CHINA": "China",
             "COMMODITIES": "Commodities"}
    for m in DIGEST_MARKETS:
        hs = headlines.get(m, [])
        if hs:
            L.append(f"  {label[m]}:")
            for h in hs:
                L.append(f"    - {h}")
        else:
            L.append(f"  {label[m]}: (no headlines in last 24h)")
        # surface manual bookmarks where a market has no live feed
        for bm in MANUAL_BOOKMARKS.get(m, []):
            L.append(f"    [manual] {bm['name']}: {bm['url']}")
    L.append("")
    L.append("=== END DIGEST ===")

    return "\n".join(L), report


def main() -> int:
    DATA_DIR.mkdir(exist_ok=True)
    text, report = assemble()
    DIGEST_TXT.write_text(text, encoding="utf-8")

    per_market_counts: dict[str, int] = {}
    for ok in report["ok"]:
        per_market_counts[ok["market"]] = per_market_counts.get(ok["market"], 0) + ok["headlines"]
    populated = sum(1 for c in per_market_counts.values() if c > 0)

    print(f"\nwrote {DIGEST_TXT} ({len(text)} chars)")
    print(f"feeds OK: {len(report['ok'])}, failed: {len(report['failed'])}, "
          f"empty: {len(report['empty'])}")
    print(f"market groups with headlines: {populated}/{len(DIGEST_MARKETS)}")
    for ok in report["ok"]:
        print(f"  OK   [{ok['market']}] {ok['name']}: {ok['headlines']} headlines")
    for f in report["failed"]:
        print(f"  FAIL [{f['market']}] {f['name']}: {f['error']}")
    for e in report["empty"]:
        print(f"  EMPTY[{e['market']}] {e['name']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
