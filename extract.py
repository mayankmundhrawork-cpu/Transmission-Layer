"""Entity extraction from headlines — tier 1 (heuristic) + tier 2 (optional LLM).

Tier 1 is always on and free: capitalized-span mining over titles with
aggressive stop-lists. It is deliberately tuned for PRECISION-VIA-PIPELINE
rather than precision-per-headline: noisy candidates are cheap because nothing
is fetched or even resolved until a candidate has repeated across feeds
(universe.py admission gate) and passed symbol validation (resolve.py).

Tier 2 (LLM) runs ONLY when ANTHROPIC_API_KEY is present: a single capped
Haiku call per run over the new headlines, returning structured entities with
ticker hints. It raises recall on messy names; the system functions without it.
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict

from settings import get_anthropic_key

# ── stop-lists (normalized, lowercase) ─────────────────────────────────
# Institutions / policy / geography / macro vocabulary — things headlines
# capitalize that are NOT tradeable entities (or are already backbone-covered).
STOP_PHRASES = {
    # institutions & policy
    "fed", "federal reserve", "ecb", "european central bank", "rbi",
    "reserve bank", "reserve bank of india", "boj", "bank of japan",
    "bank of england", "pboc", "imf", "world bank", "sec", "sebi", "treasury",
    "white house", "congress", "senate", "supreme court", "pentagon",
    "opec", "opec+", "eu", "un", "nato", "fomc", "doj", "eia", "bls", "bea",
    "cftc", "nsdl", "amfi", "nse", "bse", "lme", "comex", "nymex", "mcx",
    # geography & demonyms
    "us", "usa", "u.s.", "america", "american", "china", "chinese", "india",
    "indian", "europe", "european", "japan", "japanese", "russia", "russian",
    "ukraine", "israel", "iran", "iraq", "saudi arabia", "saudi", "uae",
    "qatar", "venezuela", "colombia", "canada", "mexico", "brazil", "uk",
    "britain", "british", "germany", "german", "france", "french", "italy",
    "spain", "greece", "turkey", "korea", "south korea", "north korea",
    "taiwan", "hong kong", "singapore", "australia", "africa", "asia",
    "asian", "latin america", "middle east", "gulf", "washington", "beijing",
    "moscow", "delhi", "new delhi", "mumbai", "london", "new york", "tokyo",
    "strait of hormuz", "hormuz", "red sea", "british columbia",
    # markets vocabulary & indices (backbone-covered or generic)
    "wall street", "dalal street", "main street", "nifty", "sensex", "nasdaq",
    "dow", "dow jones", "s&p", "ftse", "dax", "nikkei", "hang seng", "kospi",
    "stoxx", "vix", "gift nifty",
    # publications & desks (incl. our own feed names)
    "reuters", "bloomberg", "cnbc", "marketwatch", "moneywatch", "mint",
    "livemint", "economic times", "et markets", "business standard",
    "businessline", "oilprice", "scmp", "caixin", "barron's", "wsj",
    "financial times", "morningstar", "motley fool", "seeking alpha",
    "zacks", "benzinga", "investor's business daily",
    # macro & finance generics
    "gdp", "cpi", "wpi", "ppi", "pce", "pmi", "ipo", "ipos", "etf", "etfs",
    "sip", "fpi", "fii", "dii", "cad", "repo", "reverse repo", "rate cut",
    "rate hike", "q1", "q2", "q3", "q4", "h1", "h2", "fy26", "fy27",
    "earnings", "results", "stocks", "shares", "markets", "market", "economy",
    "inflation", "recession", "tariff", "tariffs", "budget", "gst", "tax",
    "bonds", "yields", "futures", "options", "crypto", "ai", "ev", "evs",
    "covid", "top", "best", "buy", "sell", "hold", "street", "stock",
    # commodities already covered by backbone aliases
    "oil", "crude", "brent", "wti", "gold", "silver", "copper", "wheat",
    "corn", "soybean", "soybeans", "natural gas", "lng", "gas", "bitcoin",
    "btc", "ethereum", "dollar", "euro", "yen", "yuan", "rupee", "pound",
    "sterling", "greenback",
    # people (politicians / officials / figureheads — never tradeable)
    "trump", "donald trump", "biden", "harris", "vance", "modi",
    "narendra modi", "putin", "xi", "xi jinping", "powell", "jerome powell",
    "lagarde", "christine lagarde", "yellen", "bessent", "sitharaman",
    "nirmala sitharaman", "musk", "elon musk", "buffett", "warren buffett",
    "communist party", "republicans", "democrats", "bjp",
    # headline boilerplate
    "report", "reports", "broker", "brokers", "op-ed", "editorial",
    "explainer", "interview", "profile", "moment", "things", "reasons",
}

# Single tokens never allowed to BE or START a candidate span.
STOP_TOKENS = {
    "the", "a", "an", "in", "on", "at", "of", "for", "to", "and", "as", "is",
    "are", "was", "will", "would", "could", "should", "may", "might", "can",
    "here", "there", "why", "how", "what", "when", "where", "who", "which",
    "this", "that", "these", "those", "its", "his", "her", "your", "my", "our",
    "their", "after", "before", "amid", "despite", "over", "under", "from",
    "with", "without", "into", "vs", "versus", "via", "per", "about", "more",
    "most", "less", "least", "new", "old", "big", "small", "high", "low",
    "monday", "tuesday", "wednesday", "thursday", "friday", "saturday",
    "sunday", "january", "february", "march", "april", "may", "june", "july",
    "august", "september", "october", "november", "december", "today",
    "tomorrow", "yesterday", "week", "month", "year", "live", "watch",
    "update", "updates", "explained", "analysis", "opinion", "exclusive",
    "breaking", "podcast", "video", "chart", "charts", "record", "key",
}

_CORP_SUFFIX = re.compile(
    r"\b(incorporated|inc|corporation|corp|company|co|limited|ltd|plc|llc|"
    r"lp|sa|ag|nv|se|ab|asa|spa|oyj|group|holdings|holding|industries|"
    r"enterprises|technologies|technology|labs)\b\.?", re.I)
_TOKEN = re.compile(r"[A-Za-z][A-Za-z&'\.\-]*")
_DOLLAR_TICKER = re.compile(r"\$([A-Za-z]{1,5})\b")


def normalize(name: str) -> str:
    import html
    n = html.unescape(name).lower().strip()
    n = _CORP_SUFFIX.sub("", n)
    n = re.sub(r"[^a-z0-9& ]+", " ", n)
    n = re.sub(r"\s+", " ", n).strip()
    # drop trailing quarter/report tokens picked up from earnings headlines
    toks = n.split()
    while toks and toks[-1] in {"q", "q1", "q2", "q3", "q4", "h1", "h2", "fy"}:
        toks.pop()
    return " ".join(toks)


def _is_capitalized(tok: str) -> bool:
    return tok[0].isupper() or (len(tok) > 1 and tok.isupper())


def _spans_from_title(title: str) -> list[str]:
    """Runs of 1–4 capitalized tokens (allowing '&' and lowercase connectors)."""
    toks = _TOKEN.findall(title)
    spans, cur = [], []
    for tok in toks:
        low = tok.lower().strip(".")
        if _is_capitalized(tok) and low not in STOP_TOKENS:
            cur.append(tok)
        elif cur and low in {"&", "and", "of", "de"} and len(cur) < 4:
            cur.append(tok)  # connector inside a span; kept only if span continues
        else:
            if cur:
                spans.append(cur)
            cur = []
    if cur:
        spans.append(cur)

    out = []
    for span in spans:
        # trim trailing connectors, cap at 4 tokens
        while span and span[-1].lower() in {"&", "and", "of", "de"}:
            span.pop()
        span = span[:4]
        if not span:
            continue
        # single ALL-CAPS short token is more likely an acronym/junk than a
        # company unless $-prefixed (handled separately) — require len ≥ 2 words
        # OR a mixed-case word of length ≥ 4.
        if len(span) == 1 and (span[0].isupper() and len(span[0]) <= 3):
            continue
        if len(span) == 1 and len(span[0]) < 4:
            continue
        out.append(" ".join(span))
    return out


def heuristic_candidates(items: list[dict]) -> dict[str, dict]:
    """{name_norm: {display, mentions: [{feed, ts, title}], tickers: set}}"""
    cands: dict[str, dict] = {}
    for it in items:
        title = it["title"]
        seen_in_title: set[str] = set()

        for m in _DOLLAR_TICKER.finditer(title):
            tick = m.group(1).upper()
            key = f"${tick}"
            if key in seen_in_title:
                continue
            seen_in_title.add(key)
            c = cands.setdefault(key, {"display": tick, "mentions": [], "ticker_hint": tick})
            c["mentions"].append({"feed": it["feed"], "ts": it["ts"], "title": title})

        import html as _html
        for span in _spans_from_title(_html.unescape(title)):
            norm = normalize(span)
            if not norm or norm in STOP_PHRASES or len(norm) < 3:
                continue
            toks = norm.split()
            if all(t in STOP_TOKENS or len(t) < 3 for t in toks):
                continue
            # every token individually a stop-phrase ("us ipo") → junk
            if all(t in STOP_PHRASES or t in STOP_TOKENS for t in toks):
                continue
            if norm in seen_in_title:
                continue
            seen_in_title.add(norm)
            c = cands.setdefault(norm, {"display": span, "mentions": []})
            c["mentions"].append({"feed": it["feed"], "ts": it["ts"], "title": title})
    return cands


# ── tier 2: optional LLM pass ──────────────────────────────────────────
LLM_MODEL = "claude-haiku-4-5-20251001"
LLM_MAX_HEADLINES = 150
LLM_MAX_TOKENS = 1500

_LLM_PROMPT = """From the numbered financial headlines below, extract entities a trader could
express with a single Yahoo Finance symbol: public companies, specific
commodities, or liquid thematic ETFs. EXCLUDE countries, governments, central
banks, regulators, politicians, macro statistics, and broad indices.

Return ONLY a JSON array, each element:
{"name": "<canonical entity name>", "ticker": "<Yahoo symbol or null>",
 "cls": "equity|commodity|etf|crypto", "headlines": [<headline numbers>]}

Headlines:
"""


def llm_candidates(items: list[dict]) -> dict[str, dict]:
    """One capped Haiku call. Returns same shape as heuristic_candidates.
    Silently returns {} when no key is configured or anything fails."""
    key = get_anthropic_key()
    if not key or not items:
        return {}
    try:
        import anthropic
    except ImportError:
        print("  WARN llm tier: anthropic package not installed", file=sys.stderr)
        return {}
    subset = items[:LLM_MAX_HEADLINES]
    numbered = "\n".join(f"{i+1}. {it['title']}" for i, it in enumerate(subset))
    try:
        client = anthropic.Anthropic(api_key=key)
        msg = client.messages.create(
            model=LLM_MODEL, max_tokens=LLM_MAX_TOKENS,
            messages=[{"role": "user", "content": _LLM_PROMPT + numbered}],
        )
        text = "".join(b.text for b in msg.content if getattr(b, "type", "") == "text")
        start, end = text.find("["), text.rfind("]")
        entities = json.loads(text[start:end + 1]) if start != -1 and end != -1 else []
    except Exception as e:  # LLM failure must never sink the run
        print(f"  WARN llm tier failed: {str(e)[:160]}", file=sys.stderr)
        return {}

    cands: dict[str, dict] = {}
    for ent in entities:
        try:
            name = str(ent["name"]).strip()
            norm = normalize(name)
            if not norm or norm in STOP_PHRASES:
                continue
            refs = [subset[i - 1] for i in ent.get("headlines", [])
                    if isinstance(i, int) and 1 <= i <= len(subset)]
            c = cands.setdefault(norm, {"display": name, "mentions": [], "via_llm": True})
            tick = ent.get("ticker")
            if tick and isinstance(tick, str) and 1 <= len(tick) <= 12:
                c["ticker_hint"] = tick.upper()
            if ent.get("cls") in {"equity", "commodity", "etf", "crypto"}:
                c["cls_hint"] = ent["cls"]
            for it in refs:
                c["mentions"].append({"feed": it["feed"], "ts": it["ts"], "title": it["title"]})
        except Exception:
            continue
    return cands


def extract(items: list[dict]) -> dict[str, dict]:
    """Merged candidates from both tiers over the given headline items."""
    cands = heuristic_candidates(items)
    for norm, c in llm_candidates(items).items():
        if norm in cands:
            base = cands[norm]
            base.setdefault("ticker_hint", c.get("ticker_hint"))
            base.setdefault("cls_hint", c.get("cls_hint"))
            base["via_llm"] = True
            seen = {m["title"] for m in base["mentions"]}
            base["mentions"] += [m for m in c["mentions"] if m["title"] not in seen]
        else:
            cands[norm] = c
    return cands


if __name__ == "__main__":
    from headlines import recent_items
    cands = extract(recent_items())
    ranked = sorted(cands.items(), key=lambda kv: -len(kv[1]["mentions"]))
    print(f"{len(cands)} candidates from stored headlines; top 25 by mentions:")
    for norm, c in ranked[:25]:
        feeds = {m['feed'] for m in c['mentions']}
        print(f"  {len(c['mentions']):>2}x {len(feeds)}f  {c['display'][:44]:44} "
              f"hint={c.get('ticker_hint','-')}")
