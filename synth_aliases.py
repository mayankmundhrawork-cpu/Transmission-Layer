"""SYNTH_V2 · S1 — curated entity/topic alias map (THE recall bottleneck).

Deterministic, auditable lexicon joining news/squawk text to tracked series
and topic tags. Three matching layers are applied at ingest (synth_events):

  L1  universe layer (AUTOMATIC, not here): every tracked symbol + company
      norm from the registry/universe — code-generated, so single names
      never need manual entries.
  L2  backbone NEWS_ALIASES (existing, backbone.py) — index/FX/commodity
      shorthands.
  L3  THIS FILE — topics, chokepoints, institutions, macro phrases that map
      to *baskets* of series. This is the layer that decides whether
      "Hormuz" reaches brent/wti/usd_inr or silently misses.

Every entry: phrases (word-boundary matched, lowercase), series (registry
ids), topics (free tags used for grouping/dispersion later).

Join-miss instrumentation (ruling 2): items matching NOTHING across L1-L3
are logged to data/synth/join_misses.json — the MiniLM upgrade triggers on
evidence of misses, not vibes. Add phrases here when the miss log shows
real news failing the join.
"""

TOPIC_ALIASES = [
    # ── energy & chokepoints ───────────────────────────────────────────
    {"phrases": ["hormuz", "strait of hormuz", "red sea", "houthis", "tanker",
                 "tankers", "suez"],
     "series": ["brent", "wti", "usd_inr", "natgas"],
     "topics": ["energy_chokepoint", "geopolitics"]},
    {"phrases": ["opec", "opec+", "output cut", "production quota", "saudi",
                 "aramco"],
     "series": ["brent", "wti"], "topics": ["oil_supply"]},
    {"phrases": ["refinery", "refineries", "diesel", "gasoline", "jet fuel",
                 "crack spread", "gasoil"],
     "series": ["brent", "wti"], "topics": ["refining"]},
    {"phrases": ["lng", "natural gas", "gas pipeline", "gazprom"],
     "series": ["natgas"], "topics": ["gas"]},
    {"phrases": ["sanction", "sanctions", "price cap", "urals"],
     "series": ["brent", "wti", "comex_gold"],
     "topics": ["sanctions", "geopolitics"]},
    {"phrases": ["iran", "iranian", "tehran", "gulf escalation",
                 "attacks on ships", "israel", "israel strikes",
                 "strait closure", "strait of hormuz"],
     "series": ["brent", "wti", "comex_gold", "vix"],
     "topics": ["geopolitics", "energy_chokepoint"]},

    # ── india macro & policy ───────────────────────────────────────────
    {"phrases": ["rbi", "reserve bank of india", "mpc", "repo rate",
                 "monetary policy committee"],
     "series": ["goi_10y", "usd_inr", "nifty_50"],
     "topics": ["india_policy", "rates"]},
    {"phrases": ["india cpi", "india inflation", "wpi", "food inflation"],
     "series": ["india_cpi_yoy", "goi_10y", "usd_inr"],
     "topics": ["india_macro", "inflation"]},
    # nifty_50 enters at weight 0.5 (owner ruling): rural demand routes to
    # index-heavy autos/staples/financials, but monsoon is not usually a
    # broad-index driver — down-weighted so a false join costs less.
    {"phrases": ["monsoon", "rainfall", "kharif", "sowing", "el nino",
                 "la nina", "imd"],
     "series": ["nifty_fmcg", "india_cpi_yoy", "wheat", "corn", "soybeans",
                "nifty_50"],
     "weights": {"nifty_50": 0.5},
     "topics": ["monsoon", "agri", "india_macro"]},
    {"phrases": ["fii", "fpi", "dii", "foreign outflow", "foreign inflow"],
     "series": ["nifty_50", "nifty_midcap_100", "usd_inr"],
     "topics": ["india_flows"]},
    {"phrases": ["gst", "union budget", "fiscal deficit", "sitharaman",
                 "capex push"],
     "series": ["nifty_50", "goi_10y"], "topics": ["india_fiscal"]},
    {"phrases": ["sensex", "nifty", "dalal street", "gift nifty"],
     "series": ["nifty_50", "nifty_midcap_100"], "topics": ["india_equity"]},
    {"phrases": ["rupee", "inr"],
     "series": ["usd_inr", "eur_inr"], "topics": ["india_fx"]},

    # ── us macro & fed ─────────────────────────────────────────────────
    {"phrases": ["fomc", "federal reserve", "fed ", "powell", "rate cut",
                 "rate hike", "dot plot", "qt ", "quantitative"],
     "series": ["ust_2y", "ust_10y", "sofr", "dxy", "comex_gold", "sp500"],
     "topics": ["fed", "rates"]},
    {"phrases": ["us cpi", "pce", "payrolls", "nonfarm", "jobless claims",
                 "ism ", "us inflation"],
     "series": ["ust_2y", "ust_10y", "dxy", "sp500"],
     "topics": ["us_macro", "inflation"]},
    # Indian legs added (owner ruling): tariff escalation transmits to
    # Indian IT (US-demand proxy) and metals (global price + dumping flows)
    {"phrases": ["tariff", "tariffs", "trade war", "trade deal", "import duty"],
     "series": ["sp500", "usd_cny", "usd_inr", "comex_copper", "hang_seng",
                "nifty_it", "nifty_metal"],
     "topics": ["trade_policy", "geopolitics"]},
    {"phrases": ["treasury yield", "bond selloff", "duration", "term premium",
                 "10-year"],
     "series": ["ust_10y", "ust_30y", "ust_2s10s"], "topics": ["rates"]},
    {"phrases": ["credit spread", "high yield", "junk bond", "default"],
     "series": ["hy_oas", "ig_oas"], "topics": ["credit"]},

    # ── china ──────────────────────────────────────────────────────────
    {"phrases": ["pboc", "china stimulus", "yuan", "renminbi", "china gdp",
                 "china pmi", "tsf", "beijing stimulus", "evergrande",
                 "china property"],
     "series": ["usd_cny", "shanghai_comp", "hang_seng", "comex_copper"],
     "topics": ["china_macro"]},

    # ── metals & agri ──────────────────────────────────────────────────
    {"phrases": ["gold"], "series": ["comex_gold", "gold_silver_ratio"],
     "topics": ["precious"]},
    {"phrases": ["silver"], "series": ["comex_silver", "gold_silver_ratio"],
     "topics": ["precious"]},
    {"phrases": ["copper", "lme"], "series": ["comex_copper", "nifty_metal"],
     "topics": ["base_metals"]},
    {"phrases": ["steel", "iron ore", "aluminium", "aluminum"],
     "series": ["nifty_metal"], "topics": ["base_metals"]},
    {"phrases": ["wheat", "grain", "grains"], "series": ["wheat"],
     "topics": ["agri"]},
    {"phrases": ["corn"], "series": ["corn"], "topics": ["agri"]},
    {"phrases": ["soybean", "soybeans", "soy ", "veg oil", "edible oil",
                 "palm oil"],
     "series": ["soybeans", "nifty_fmcg"], "topics": ["agri"]},

    # ── vol / risk / crypto ────────────────────────────────────────────
    {"phrases": ["vix", "volatility spike", "risk-off", "risk off",
                 "flight to safety", "safe haven"],
     "series": ["vix", "india_vix", "comex_gold"], "topics": ["vol", "risk"]},
    {"phrases": ["bitcoin", "btc", "crypto", "ethereum", "eth "],
     "series": ["btc_usd", "eth_usd"], "topics": ["crypto"]},
    {"phrases": ["dollar index", "greenback", "king dollar"],
     "series": ["dxy"], "topics": ["fx"]},

    # ── tech / semis (drives both US and Indian IT baskets) ────────────
    # watch=True (owner ruling): semis->nifty_it is the loosest causal link
    # in the map — most likely to generate spurious transmission gaps. The
    # S2 audit surfaces every candidate whose news-join came through a
    # watch-flagged entry so its hit rate is visible early; cut if noise.
    {"phrases": ["nvidia", "semiconductor", "semiconductors", "chipmaker",
                 "chips act", "tsmc", "ai capex", "data center",
                 "datacenter", "h100", "h200"],
     "series": ["nasdaq_100", "taiwan_weighted", "nifty_it"],
     "watch": True,
     "topics": ["semis", "ai"]},
    {"phrases": ["it services", "infosys", "tcs", "wipro", "hcl tech"],
     "series": ["nifty_it"], "topics": ["india_it"]},

    # ── banks ──────────────────────────────────────────────────────────
    {"phrases": ["bank credit", "npa", "banking system", "deposit growth",
                 "credit growth"],
     "series": ["nifty_50", "hy_oas"], "topics": ["banks"]},
]

# institutions/people whose mention alone shouldn't create a market entity
# (they tag TOPICS only when no series phrase co-fires) — prevents "Powell
# spoke" from becoming a nifty event via over-eager joins.
TOPIC_ONLY = {
    "white house": ["us_politics"], "election": ["politics"],
    "trump": ["us_politics"], "biden": ["us_politics"],
    "modi": ["india_politics"], "putin": ["geopolitics"],
    "ukraine": ["geopolitics"], "israel": ["geopolitics"],
    "iran": ["geopolitics", "energy_chokepoint"],
    "iranian": ["geopolitics", "energy_chokepoint"],
    "tehran": ["geopolitics", "energy_chokepoint"],
    "bahrain": ["geopolitics", "energy_chokepoint"],
    "missile": ["geopolitics"], "drone attack": ["geopolitics"],
    "air defence": ["geopolitics"], "air defense": ["geopolitics"],
    "war": ["geopolitics"], "ceasefire": ["geopolitics"],
    "china": ["china"], "chinese": ["china"],
    "ipo": ["ipo"], "earnings": ["earnings"],
    "artificial intelligence": ["ai"],
    "stock market": ["equities"], "stocks": ["equities"],
}
