"""RSS feed registry for the news digest — Step 6, section [4].

Feeds are grouped by the digest's market buckets. Every feed is a candidate:
digest.py wraps each pull in try/except, so a feed that dies or changes URL is
skipped with a warning, never crashes assembly. Feeds proven dead or without a
stable public RSS are recorded in MANUAL_BOOKMARKS instead — those become
click-through bookmarks on your side, not digest items.

Stability notes:
- Reuters retired most public RSS; excluded here in favour of feeds that still
  serve XML publicly (BLS, Fed, ECB, CNBC, MarketWatch, ET, BS, Mint, OilPrice,
  EIA, Mining.com).
- Chinese official sources (NBS, PBoC) do not offer reliable English RSS; China
  leans on MANUAL_BOOKMARKS with one best-effort feed (SCMP economy) attempted.
"""

RSS_FEEDS = {
    "USA": [
        {"name": "BLS latest",        "url": "https://www.bls.gov/feed/bls_latest.rss"},
        {"name": "Federal Reserve",   "url": "https://www.federalreserve.gov/feeds/press_all.xml"},
        {"name": "CNBC Economy",      "url": "https://www.cnbc.com/id/20910258/device/rss/rss.html"},
        {"name": "MarketWatch Top",   "url": "https://feeds.marketwatch.com/marketwatch/topstories/"},
    ],
    "INDIA": [
        {"name": "ET Markets",        "url": "https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms"},
        {"name": "Business Standard", "url": "https://www.business-standard.com/rss/markets-106.rss"},
        {"name": "Mint Markets",      "url": "https://www.livemint.com/rss/markets"},
        {"name": "BusinessLine Mkts", "url": "https://www.thehindubusinessline.com/markets/feeder/default.rss"},
    ],
    "EU": [
        {"name": "ECB press",         "url": "https://www.ecb.europa.eu/rss/press.xml"},
        {"name": "ECB blog",          "url": "https://www.ecb.europa.eu/rss/blog.xml"},
    ],
    "CHINA": [
        {"name": "SCMP Economy",      "url": "https://www.scmp.com/rss/318198/feed"},
    ],
    "COMMODITIES": [
        {"name": "OilPrice",          "url": "https://oilprice.com/rss/main"},
        {"name": "EIA Today in Energy","url": "https://www.eia.gov/rss/todayinenergy.xml"},
        {"name": "Mining.com",        "url": "https://www.mining.com/feed/"},
    ],
}

# Sources with no reliable public RSS — click-through bookmarks, not digest feeds.
MANUAL_BOOKMARKS = {
    "CHINA": [
        {"name": "NBS China",  "url": "https://www.stats.gov.cn/english/"},
        {"name": "PBoC",       "url": "http://www.pbc.gov.cn/en/3688006/index.html"},
        {"name": "Caixin Global", "url": "https://www.caixinglobal.com/"},
    ],
    "INDIA": [
        {"name": "RBI press",  "url": "https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx"},
    ],
}
