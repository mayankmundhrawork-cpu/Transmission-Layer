"""Name → Yahoo symbol resolution with a persistent cache.

Resolution order:
  1. seed gazetteer (instant, curated, high precision)
  2. data/resolution_cache.json (positive AND negative results remembered —
     junk is rejected once, then never queried again)
  3. LLM ticker hint, validated like any other candidate symbol
  4. yfinance Search (network; budgeted per run by the caller)

Validation gate (the junk killer): a search result is accepted only if its
quoteType is in the whitelist AND its name is genuinely similar to the
candidate (or the exchange-preferred top hit with a strong API score).
Network failures are NOT negative-cached; genuine no-matches are.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path

from extract import normalize

DATA_DIR = Path(__file__).parent / "data"
CACHE_JSON = DATA_DIR / "resolution_cache.json"

QUOTE_TYPES = {"EQUITY", "ETF", "FUTURE"}
PREFERRED_EXCH = {"NMS", "NYQ", "NGM", "NCM", "ASE", "NSI", "BSE"}  # US primary + India
REJECT_EXCH = {"PNK"}  # OTC pink sheets
MIN_SIMILARITY = 0.55

# Seed gazetteer: common names the news uses ↔ the symbol that expresses them.
# Companies mostly resolve fine via Search; this seeds the ambiguous/shorthand
# cases and the commodity/theme words that deserve a specific instrument.
GAZETTEER = {
    # commodities not in the backbone
    "cocoa": ("CC=F", "commodity"), "coffee": ("KC=F", "commodity"),
    "sugar": ("SB=F", "commodity"), "cotton": ("CT=F", "commodity"),
    "platinum": ("PL=F", "commodity"), "palladium": ("PA=F", "commodity"),
    "aluminum": ("ALI=F", "commodity"), "aluminium": ("ALI=F", "commodity"),
    "gasoline": ("RB=F", "commodity"), "heating oil": ("HO=F", "commodity"),
    "orange juice": ("OJ=F", "commodity"), "cattle": ("LE=F", "commodity"),
    "hogs": ("HE=F", "commodity"), "rice": ("ZR=F", "commodity"),
    # theme ETFs (liquid, listed)
    "uranium": ("URA", "etf"), "lithium": ("LIT", "etf"),
    "rare earths": ("REMX", "etf"), "rare earth": ("REMX", "etf"),
    "semiconductors": ("SOXX", "etf"), "chipmakers": ("SOXX", "etf"),
    "defense stocks": ("ITA", "etf"), "gold miners": ("GDX", "etf"),
    "regional banks": ("KRE", "etf"), "homebuilders": ("XHB", "etf"),
    "steel": ("SLX", "etf"), "solar": ("TAN", "etf"),
    "cybersecurity": ("HACK", "etf"), "biotech": ("XBI", "etf"),
    # frequent shorthands the similarity check would under-score
    "google": ("GOOGL", "equity"), "alphabet": ("GOOGL", "equity"),
    "meta": ("META", "equity"), "facebook": ("META", "equity"),
    "xbox": ("MSFT", "equity"), "instagram": ("META", "equity"),
    "youtube": ("GOOGL", "equity"), "waymo": ("GOOGL", "equity"),
    "openai": (None, None),      # private — hard negative
    "anthropic": (None, None),   # private — hard negative
    "spacex": (None, None), "bytedance": (None, None), "tiktok": (None, None),
}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_cache() -> dict:
    if not CACHE_JSON.exists():
        return {}
    try:
        return json.loads(CACHE_JSON.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_cache(cache: dict) -> None:
    DATA_DIR.mkdir(exist_ok=True)
    CACHE_JSON.write_text(json.dumps(cache, indent=1, sort_keys=True), encoding="utf-8")


def _similar(a: str, b: str) -> float:
    a, b = normalize(a), normalize(b)
    if not a or not b:
        return 0.0
    ratio = SequenceMatcher(None, a, b).ratio()
    # token containment bonus: every candidate token appears in the result name
    at, bt = set(a.split()), set(b.split())
    if at and at <= bt:
        ratio = max(ratio, 0.9)
    return ratio


def _validate_quotes(name: str, quotes: list[dict]) -> dict | None:
    """Pick the best acceptable quote for a candidate name, else None."""
    scored = []
    for q in quotes:
        sym = q.get("symbol") or ""
        qt = q.get("quoteType") or ""
        exch = q.get("exchange") or ""
        disp = q.get("shortname") or q.get("longname") or ""
        if not sym or qt not in QUOTE_TYPES or exch in REJECT_EXCH:
            continue
        sim = _similar(name, disp)
        api = float(q.get("score") or 0)
        pref = 1 if exch in PREFERRED_EXCH else 0
        if sim < MIN_SIMILARITY and not (api >= 100000 and pref):
            continue  # not similar enough and not an overwhelming primary hit
        scored.append((pref, sim, api, {"symbol": sym, "shortname": disp,
                                        "quoteType": qt, "exchange": exch}))
    if not scored:
        return None
    scored.sort(key=lambda t: (t[0], t[1], t[2]), reverse=True)
    return scored[0][3]


def _search(query: str) -> list[dict] | None:
    """yfinance Search; None = network/API failure (do not negative-cache)."""
    import yfinance as yf
    try:
        s = yf.Search(query, max_results=6, news_count=0)
        return list(s.quotes or [])
    except Exception as e:
        print(f"  WARN search failed '{query}': {str(e)[:120]}", file=sys.stderr)
        return None


def resolve(norm: str, display: str, ticker_hint: str | None = None,
            cls_hint: str | None = None, cache: dict | None = None,
            allow_network: bool = True) -> dict:
    """Resolve one candidate. Returns
    {ok, symbol?, shortname?, quoteType?, cls?, via, cached: bool}."""
    cache = cache if cache is not None else load_cache()

    # 1 · gazetteer
    if norm in GAZETTEER:
        sym, cls = GAZETTEER[norm]
        if sym is None:
            return {"ok": False, "via": "gazetteer-negative", "cached": True}
        return {"ok": True, "symbol": sym, "shortname": display,
                "quoteType": "GAZETTEER", "cls": cls or "equity",
                "via": "gazetteer", "cached": True}

    # 2 · cache (positive or negative)
    hit = cache.get(norm)
    if hit is not None:
        return {**hit, "cached": True}

    if not allow_network:
        return {"ok": False, "via": "budget-exhausted", "cached": False,
                "deferred": True}

    # 3 · LLM hint — validate the hinted symbol by searching IT and comparing
    quotes = None
    if ticker_hint:
        quotes = _search(ticker_hint)
        if quotes:
            for q in quotes:
                if (q.get("symbol") or "").upper() == ticker_hint.upper():
                    best = _validate_quotes(norm, [q]) or (
                        # hint symbol exists; accept if the name is plausibly it
                        {"symbol": q["symbol"], "shortname": q.get("shortname") or "",
                         "quoteType": q.get("quoteType") or "",
                         "exchange": q.get("exchange") or ""}
                        if _similar(norm, q.get("shortname") or "") >= 0.4
                        and (q.get("quoteType") or "") in QUOTE_TYPES else None)
                    if best:
                        res = {"ok": True, **best, "cls": cls_hint or "equity",
                               "via": "llm-hint", "resolved_at": _now()}
                        cache[norm] = res
                        return {**res, "cached": False}

    # 4 · name search
    quotes = _search(display)
    if quotes is None:
        return {"ok": False, "via": "network-error", "cached": False}
    best = _validate_quotes(norm, quotes)
    if best is None:
        res = {"ok": False, "via": "no-acceptable-match", "resolved_at": _now()}
        cache[norm] = res  # genuine no-match → negative-cache it
        return {**res, "cached": False}
    cls = cls_hint or ("commodity" if best["quoteType"] == "FUTURE"
                       else "etf" if best["quoteType"] == "ETF" else "equity")
    res = {"ok": True, **best, "cls": cls, "via": "search", "resolved_at": _now()}
    cache[norm] = res
    return {**res, "cached": False}


if __name__ == "__main__":
    # smoke test against live Search
    cache: dict = {}
    for name in ["HDFC Bank", "Micron", "TeraWulf", "Ather Energy",
                 "cocoa", "Anthropic", "Important Moment"]:
        r = resolve(normalize(name), name, cache=cache)
        print(f"  {name:18} -> {r.get('ok')} {r.get('symbol','-'):12} "
              f"{r.get('shortname','')[:30]:30} via={r['via']}")
