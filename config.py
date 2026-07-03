"""Series registry — Step 3 of the spec.

Each series has:
  id           internal name
  market       INDIA | USA | EU | COMMODITIES
  source       yfinance | fred | derived
  symbol       ticker (yfinance) or series id (fred) or formula (derived)
  freq         eod | daily | monthly
  framework    dict describing extra flag triggers beyond generic z-score

Derived series reference other series' ids in `formula`.
"""

import os

FRED_API_KEY = os.environ.get("FRED_API_KEY")
if not FRED_API_KEY:
    raise RuntimeError(
        "FRED_API_KEY is not set. Export it in your shell before running, e.g.:\n"
        "  PowerShell:  $env:FRED_API_KEY = '<your-key>'\n"
        "  bash/zsh:    export FRED_API_KEY='<your-key>'\n"
        "In CI it is injected from the FRED_API_KEY repository secret."
    )

SERIES = [
    # INDIA — equities & ratios
    {"id": "nifty_50",          "market": "INDIA",       "source": "yfinance", "symbol": "^NSEI",              "freq": "eod",     "framework": {}},
    {"id": "nifty_midcap_100",  "market": "INDIA",       "source": "yfinance", "symbol": "NIFTY_MIDCAP_100.NS","freq": "eod",     "framework": {}},
    {"id": "nifty_fmcg",        "market": "INDIA",       "source": "yfinance", "symbol": "^CNXFMCG",           "freq": "eod",     "framework": {}},
    {"id": "nifty_metal",       "market": "INDIA",       "source": "yfinance", "symbol": "^CNXMETAL",          "freq": "eod",     "framework": {}},
    {"id": "nifty_it",          "market": "INDIA",       "source": "yfinance", "symbol": "^CNXIT",             "freq": "eod",     "framework": {}},
    {"id": "dabur",             "market": "INDIA",       "source": "yfinance", "symbol": "DABUR.NS",           "freq": "eod",     "framework": {}},
    {"id": "britannia",         "market": "INDIA",       "source": "yfinance", "symbol": "BRITANNIA.NS",       "freq": "eod",     "framework": {}},
    {"id": "bpcl",              "market": "INDIA",       "source": "yfinance", "symbol": "BPCL.NS",            "freq": "eod",     "framework": {}},

    # INDIA — currency & rates
    {"id": "usd_inr",           "market": "INDIA",       "source": "yfinance", "symbol": "INR=X",              "freq": "eod",     "framework": {"range_extreme_days": 20}},
    {"id": "eur_inr",           "market": "INDIA",       "source": "yfinance", "symbol": "EURINR=X",           "freq": "eod",     "framework": {}},
    {"id": "goi_10y",           "market": "INDIA",       "source": "fred",     "symbol": "INDIRLTLT01STM",     "freq": "monthly", "framework": {}},

    # USA — monetary anchor
    {"id": "ust_2y",            "market": "USA",         "source": "fred",     "symbol": "DGS2",               "freq": "daily",   "framework": {}},
    {"id": "ust_10y",           "market": "USA",         "source": "fred",     "symbol": "DGS10",              "freq": "daily",   "framework": {}},
    {"id": "tips_10y_real",     "market": "USA",         "source": "fred",     "symbol": "DFII10",             "freq": "daily",   "framework": {"single_day_bps": 5}},
    {"id": "sofr",              "market": "USA",         "source": "fred",     "symbol": "SOFR",               "freq": "daily",   "framework": {}},

    # USA — dollar & commodities
    {"id": "dxy",               "market": "USA",         "source": "yfinance", "symbol": "DX-Y.NYB",           "freq": "eod",     "framework": {"range_extreme_days": 20}},
    {"id": "wti",               "market": "COMMODITIES", "source": "yfinance", "symbol": "CL=F",               "freq": "eod",     "framework": {"single_session_pct": 1.5}},
    {"id": "brent",             "market": "COMMODITIES", "source": "yfinance", "symbol": "BZ=F",               "freq": "eod",     "framework": {"single_session_pct": 1.5}},
    {"id": "comex_copper",      "market": "COMMODITIES", "source": "yfinance", "symbol": "HG=F",               "freq": "eod",     "framework": {}},
    {"id": "comex_gold",        "market": "COMMODITIES", "source": "yfinance", "symbol": "GC=F",               "freq": "eod",     "framework": {}},
    {"id": "comex_silver",      "market": "COMMODITIES", "source": "yfinance", "symbol": "SI=F",               "freq": "eod",     "framework": {}},

    # EU
    {"id": "eur_usd",           "market": "EU",          "source": "yfinance", "symbol": "EURUSD=X",           "freq": "eod",     "framework": {}},
    {"id": "bund_10y",          "market": "EU",          "source": "fred",     "symbol": "IRLTLT01DEM156N",    "freq": "monthly", "framework": {}},

    # Derived
    {"id": "midcap_largecap_ratio", "market": "INDIA",       "source": "derived", "formula": ("ratio", "nifty_midcap_100", "nifty_50"),        "freq": "eod", "framework": {"pct_extreme_52w": True, "break_below_100dma": True}},
    {"id": "brent_wti_spread",      "market": "COMMODITIES", "source": "derived", "formula": ("sub",   "brent", "wti"),                        "freq": "eod", "framework": {}},
    {"id": "gold_silver_ratio",     "market": "COMMODITIES", "source": "derived", "formula": ("ratio", "comex_gold", "comex_silver"),          "freq": "eod", "framework": {"gsr_bands": True}},
    {"id": "goi_ust_spread",        "market": "INDIA",       "source": "derived", "formula": ("sub",   "goi_10y", "ust_10y"),                  "freq": "monthly", "framework": {"monthly_bps_move": 20}},
]

# Cross-market co-occurrence groups (Step 5)
LINKED_GROUPS = {
    "metal_copper":   ["nifty_metal", "comex_copper"],
    "inr_oil":        ["usd_inr", "brent"],
    "gold_silver":    ["comex_gold", "comex_silver"],
    "goi_ust":        ["goi_10y", "ust_10y"],
}

MARKETS = ["INDIA", "USA", "EU", "COMMODITIES"]
