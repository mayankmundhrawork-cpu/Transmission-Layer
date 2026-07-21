"""Layer 0 — the stable macro backbone.

These series are static BY DESIGN: broad, liquid, cross-asset coverage that
grounds the board regardless of what the news cycle is doing. The dynamic
(news-assembled) layer sits on top of this — see universe.py / registry.py.

Spec shape is engine-compatible (same keys the v1 registry used):
  id · market (class bucket) · source (yfinance|fred|derived) · symbol/formula
  · freq · framework (extra flag triggers layered on the generic z-score).

Proven framework thresholds from the original board are preserved verbatim.
"""

CLASSES = ["INDICES", "EQUITIES", "FX", "RATES", "COMMODITIES", "CRYPTO", "DERIVED"]

BACKBONE = [
    # ── Equity indices · US ────────────────────────────────────────────
    {"id": "sp500",         "market": "INDICES", "source": "yfinance", "symbol": "^GSPC",     "freq": "eod", "framework": {}},
    {"id": "nasdaq_100",    "market": "INDICES", "source": "yfinance", "symbol": "^NDX",      "freq": "eod", "framework": {}},
    {"id": "dow_jones",     "market": "INDICES", "source": "yfinance", "symbol": "^DJI",      "freq": "eod", "framework": {}},
    {"id": "russell_2000",  "market": "INDICES", "source": "yfinance", "symbol": "^RUT",      "freq": "eod", "framework": {}},
    # no_despike: VIX legitimately spikes-and-reverts — the despike filter's
    # bad-tick signature IS this series' signal, so it is exempted.
    {"id": "vix",           "market": "INDICES", "source": "yfinance", "symbol": "^VIX",      "freq": "eod", "framework": {"single_session_pct": 15.0}, "no_despike": True},
    {"id": "india_vix",     "market": "INDICES", "source": "yfinance", "symbol": "^INDIAVIX", "freq": "eod", "framework": {"single_session_pct": 15.0}, "no_despike": True},
    # ── Equity indices · Europe ────────────────────────────────────────
    {"id": "ftse_100",      "market": "INDICES", "source": "yfinance", "symbol": "^FTSE",     "freq": "eod", "framework": {}},
    {"id": "dax",           "market": "INDICES", "source": "yfinance", "symbol": "^GDAXI",    "freq": "eod", "framework": {}},
    {"id": "cac_40",        "market": "INDICES", "source": "yfinance", "symbol": "^FCHI",     "freq": "eod", "framework": {}},
    {"id": "stoxx_50",      "market": "INDICES", "source": "yfinance", "symbol": "^STOXX50E", "freq": "eod", "framework": {}},
    # ── Equity indices · Asia-Pacific & EM ─────────────────────────────
    {"id": "nikkei_225",    "market": "INDICES", "source": "yfinance", "symbol": "^N225",     "freq": "eod", "framework": {}},
    {"id": "hang_seng",     "market": "INDICES", "source": "yfinance", "symbol": "^HSI",      "freq": "eod", "framework": {}},
    {"id": "shanghai_comp", "market": "INDICES", "source": "yfinance", "symbol": "000001.SS", "freq": "eod", "framework": {}},
    {"id": "kospi",         "market": "INDICES", "source": "yfinance", "symbol": "^KS11",     "freq": "eod", "framework": {}},
    {"id": "taiwan_weighted","market": "INDICES","source": "yfinance", "symbol": "^TWII",     "freq": "eod", "framework": {}},
    {"id": "asx_200",       "market": "INDICES", "source": "yfinance", "symbol": "^AXJO",     "freq": "eod", "framework": {}},
    {"id": "bovespa",       "market": "INDICES", "source": "yfinance", "symbol": "^BVSP",     "freq": "eod", "framework": {}},
    # ── Equity indices · India (proven set) ────────────────────────────
    {"id": "nifty_50",         "market": "INDICES", "source": "yfinance", "symbol": "^NSEI",              "freq": "eod", "framework": {}},
    {"id": "nifty_midcap_100", "market": "INDICES", "source": "yfinance", "symbol": "NIFTY_MIDCAP_100.NS","freq": "eod", "framework": {}},
    {"id": "nifty_fmcg",       "market": "INDICES", "source": "yfinance", "symbol": "^CNXFMCG",           "freq": "eod", "framework": {}},
    {"id": "nifty_metal",      "market": "INDICES", "source": "yfinance", "symbol": "^CNXMETAL",          "freq": "eod", "framework": {}},
    {"id": "nifty_it",         "market": "INDICES", "source": "yfinance", "symbol": "^CNXIT",             "freq": "eod", "framework": {}},
    # ── Equity single names · India (legacy price history; classed so the
    #    class prior can never fail OPEN on them — an unclassified series must
    #    not be admissible as a macro driver). Detector uses them as targets. ─
    {"id": "britannia", "market": "EQUITIES", "source": "yfinance", "symbol": "BRITANNIA.NS", "freq": "eod", "framework": {}},
    {"id": "bpcl",      "market": "EQUITIES", "source": "yfinance", "symbol": "BPCL.NS",      "freq": "eod", "framework": {}},
    {"id": "dabur",     "market": "EQUITIES", "source": "yfinance", "symbol": "DABUR.NS",     "freq": "eod", "framework": {}},

    # ── FX ─────────────────────────────────────────────────────────────
    {"id": "dxy",     "market": "FX", "source": "yfinance", "symbol": "DX-Y.NYB", "freq": "eod", "framework": {"range_extreme_days": 20}},
    {"id": "eur_usd", "market": "FX", "source": "yfinance", "symbol": "EURUSD=X", "freq": "eod", "framework": {}},
    {"id": "usd_jpy", "market": "FX", "source": "yfinance", "symbol": "JPY=X",    "freq": "eod", "framework": {}},
    {"id": "gbp_usd", "market": "FX", "source": "yfinance", "symbol": "GBPUSD=X", "freq": "eod", "framework": {}},
    {"id": "aud_usd", "market": "FX", "source": "yfinance", "symbol": "AUDUSD=X", "freq": "eod", "framework": {}},
    # CNH=X returns no data on Yahoo — using onshore CNY=X instead [VERIFY]
    {"id": "usd_cny", "market": "FX", "source": "yfinance", "symbol": "CNY=X",    "freq": "eod", "framework": {}},
    {"id": "usd_inr", "market": "FX", "source": "yfinance", "symbol": "INR=X",    "freq": "eod", "framework": {"range_extreme_days": 20}},
    {"id": "eur_inr", "market": "FX", "source": "yfinance", "symbol": "EURINR=X", "freq": "eod", "framework": {}},
    {"id": "usd_mxn", "market": "FX", "source": "yfinance", "symbol": "MXN=X",    "freq": "eod", "framework": {}},
    {"id": "usd_brl", "market": "FX", "source": "yfinance", "symbol": "BRL=X",    "freq": "eod", "framework": {}},

    # ── Rates & credit (FRED) ──────────────────────────────────────────
    {"id": "ust_2y",        "market": "RATES", "source": "fred", "symbol": "DGS2",            "freq": "daily",   "framework": {}},
    {"id": "ust_10y",       "market": "RATES", "source": "fred", "symbol": "DGS10",           "freq": "daily",   "framework": {}},
    {"id": "ust_30y",       "market": "RATES", "source": "fred", "symbol": "DGS30",           "freq": "daily",   "framework": {}},
    {"id": "tips_10y_real", "market": "RATES", "source": "fred", "symbol": "DFII10",          "freq": "daily",   "framework": {"single_day_bps": 5}},
    {"id": "sofr",          "market": "RATES", "source": "fred", "symbol": "SOFR",            "freq": "daily",   "framework": {}},
    {"id": "hy_oas",        "market": "RATES", "source": "fred", "symbol": "BAMLH0A0HYM2",    "freq": "daily",   "framework": {"single_day_bps": 25}},
    {"id": "ig_oas",        "market": "RATES", "source": "fred", "symbol": "BAMLC0A0CM",      "freq": "daily",   "framework": {}},
    {"id": "goi_10y",       "market": "RATES", "source": "fred", "symbol": "INDIRLTLT01STM",  "freq": "monthly", "framework": {}},
    {"id": "bund_10y",      "market": "RATES", "source": "fred", "symbol": "IRLTLT01DEM156N", "freq": "monthly", "framework": {}},
    # India macro print (monthly, lagged — sparse guard suppresses flags) [VERIFY]
    {"id": "india_cpi_yoy", "market": "RATES", "source": "fred", "symbol": "CPALTT01INM659N", "freq": "monthly", "framework": {}},

    # ── Commodities ────────────────────────────────────────────────────
    {"id": "wti",          "market": "COMMODITIES", "source": "yfinance", "symbol": "CL=F", "freq": "eod", "framework": {"single_session_pct": 1.5}},
    {"id": "brent",        "market": "COMMODITIES", "source": "yfinance", "symbol": "BZ=F", "freq": "eod", "framework": {"single_session_pct": 1.5}},
    {"id": "natgas",       "market": "COMMODITIES", "source": "yfinance", "symbol": "NG=F", "freq": "eod", "framework": {"single_session_pct": 5.0}},
    {"id": "comex_gold",   "market": "COMMODITIES", "source": "yfinance", "symbol": "GC=F", "freq": "eod", "framework": {}},
    {"id": "comex_silver", "market": "COMMODITIES", "source": "yfinance", "symbol": "SI=F", "freq": "eod", "framework": {}},
    {"id": "comex_copper", "market": "COMMODITIES", "source": "yfinance", "symbol": "HG=F", "freq": "eod", "framework": {}},
    {"id": "wheat",        "market": "COMMODITIES", "source": "yfinance", "symbol": "ZW=F", "freq": "eod", "framework": {}},
    {"id": "corn",         "market": "COMMODITIES", "source": "yfinance", "symbol": "ZC=F", "freq": "eod", "framework": {}},
    {"id": "soybeans",     "market": "COMMODITIES", "source": "yfinance", "symbol": "ZS=F", "freq": "eod", "framework": {}},

    # ── Crypto (risk-appetite gauges) ──────────────────────────────────
    {"id": "btc_usd", "market": "CRYPTO", "source": "yfinance", "symbol": "BTC-USD", "freq": "eod", "framework": {}},
    {"id": "eth_usd", "market": "CRYPTO", "source": "yfinance", "symbol": "ETH-USD", "freq": "eod", "framework": {}},

    # ── Derived (proven ratios + curve) ────────────────────────────────
    {"id": "midcap_largecap_ratio", "market": "DERIVED", "source": "derived", "formula": ("ratio", "nifty_midcap_100", "nifty_50"), "freq": "eod",     "framework": {"pct_extreme_52w": True, "break_below_100dma": True}},
    {"id": "brent_wti_spread",      "market": "DERIVED", "source": "derived", "formula": ("sub",   "brent", "wti"),                 "freq": "eod",     "framework": {}},
    {"id": "gold_silver_ratio",     "market": "DERIVED", "source": "derived", "formula": ("ratio", "comex_gold", "comex_silver"),   "freq": "eod",     "framework": {"gsr_bands": True}},
    {"id": "goi_ust_spread",        "market": "DERIVED", "source": "derived", "formula": ("sub",   "goi_10y", "ust_10y"),           "freq": "monthly", "framework": {"monthly_bps_move": 20}},
    {"id": "ust_2s10s",             "market": "DERIVED", "source": "derived", "formula": ("sub",   "ust_10y", "ust_2y"),            "freq": "daily",   "framework": {}},
]

# Cross-market co-occurrence groups (proven Step 5 pairs, engine-consumed).
LINKED_GROUPS = {
    "metal_copper": ["nifty_metal", "comex_copper"],
    "inr_oil":      ["usd_inr", "brent"],
    "gold_silver":  ["comex_gold", "comex_silver"],
    "goi_ust":      ["goi_10y", "ust_10y"],
}

# Headline-matching aliases for backbone series (events layer: ties a flagged
# backbone series to the news that plausibly motivated the move). Lowercase
# substrings, deliberately conservative to avoid false ties.
NEWS_ALIASES = {
    "sp500":        ["s&p 500", "s&p500", "wall street"],
    "nasdaq_100":   ["nasdaq"],
    "dow_jones":    ["dow jones"],
    "vix":          ["vix", "volatility index"],
    "nikkei_225":   ["nikkei"],
    "hang_seng":    ["hang seng"],
    "shanghai_comp":["shanghai composite", "china stocks"],
    "nifty_50":     ["nifty", "sensex", "dalal street"],
    "dax":          ["dax"],
    "ftse_100":     ["ftse"],
    "dxy":          ["dollar index", "greenback"],
    "eur_usd":      ["euro "],
    "usd_jpy":      ["yen"],
    "gbp_usd":      ["sterling", "pound"],
    "usd_cnh":      ["yuan", "renminbi"],
    "usd_inr":      ["rupee"],
    "ust_10y":      ["treasury yield", "10-year", "bond yields"],
    "hy_oas":       ["high yield", "junk bond", "credit spread"],
    "wti":          ["oil", "crude", "wti", "opec"],
    "brent":        ["oil", "crude", "brent", "opec"],
    "natgas":       ["natural gas", "lng"],
    "comex_gold":   ["gold"],
    "comex_silver": ["silver"],
    "comex_copper": ["copper"],
    "wheat":        ["wheat"],
    "corn":         ["corn"],
    "soybeans":     ["soybean"],
    "btc_usd":      ["bitcoin", "btc"],
    "eth_usd":      ["ethereum"],
}
