# Transmission Layer — board brief · 2026-08-25 04:52Z

data as of **2026-08-25** · 98 series · 8 red / 30 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.43, 1d in regime; vol-pct 0.235, breadth-off 0.625, Markov P(high-vol) 0.014)
- [INVERTED] **safe_haven_gold** — corr20 -0.29, corr60 -0.4, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.78, corr60 0.86, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.19, corr60 0.35, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.2, corr60 -0.11, last shift 2026-07-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.65, corr60 -0.83, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.15, corr60 -0.13, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.21, corr60 -0.1, last shift 2026-06-30. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.33, corr60 0.2, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 90** scanned series survive multiplicity control (effective p ≤ 0.0008684598407633359)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.496** (n=1114) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.815** (n=2455) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.71] commodities · 2 series ↑
- corn [COMMODITIES]: last 517.75, z20 3.88, zc 4.19, resid-z 1.08 [moved], 1d 5.34%, |z20|=3.88; 1y-pct=100
- wheat [COMMODITIES]: last 701.50, z20 2.54, zc 1.83, resid-z 0.12 [moved], 1d 2.90%, |z20|=2.54; 1y-pct=99
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Govt lifts wheat export ban with immediate effect — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/economy/agri-business/govt-lifts-wheat-export-ban-with-immediate-effect/article71384020.ece
- Source: Corn rockets to 3-year high as traders eye lower U.S. production — Mint Markets, 2026-08-24. https://www.livemint.com/market/corn-rockets-to-3-year-high-as-traders-eye-lower-u-s-production-11787533218087.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [RED 6.62] cross-asset · 4 series ↑
- btc_usd [CRYPTO]: last 80280.01, z20 2.96, zc 0.40, resid-z 0.81 [quiet], 1d 1.61%, |z20|=2.96
- dyn_mrna [EQUITIES]: last 138.89, z20 2.77, zc -0.33, resid-z 0.89 [quiet], 1d -4.30%, |z20|=2.77; 1y-pct=99
- eth_usd [CRYPTO]: last 2493.17, z20 2.40, zc 0.06, resid-z 0.17 [quiet], 1d 0.27%, |z20|=2.40
- dyn_coin [EQUITIES]: last 179.49, z20 2.22, zc -0.69, resid-z 2.03 [unexplained], 1d -3.76%, |z20|=2.22
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.79).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.41 via btc_usd, z 1.01, reacted)
- **India receivers**: nifty_metal (rho 0.41, z 1.01)
- Source: Global Market: Unitree’s 45% share slump raises bubble concerns after blockbuster Shanghai debut — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-unitrees-45-share-slump-raises-bubble-concerns-after-blockbuster-shanghai-debut/articleshow/133491891.cms
- Source: Global Market: Kospi drops 2% as chip stocks tumble ahead of Nvidia earnings — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-kospi-drops-2-as-chip-stocks-tumble-ahead-of-nvidia-earnings/articleshow/133490877.cms
- Source: Bitcoin tops $80,000 for the first time since mid-May — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-tops-80000-for-the-first-time-since-mid-may/articleshow/133489161.cms
- Historical analogues: 2025-08-13 (d=0.79), 2024-11-21 (d=1.34), 2026-05-05 (d=1.35)

### [RED 4.67] dyn_muthootfin_ns ↑
- dyn_muthootfin_ns [EQUITIES]: last 3191.50, z20 2.67, zc -0.16, resid-z 3.53 [unexplained], 1d -0.55%, |z20|=2.67
- **Mechanism**: dyn_muthootfin_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.646 via dyn_muthootfin_ns, z 1.01, reacted); nifty_midcap_100 (rho 0.571 via dyn_muthootfin_ns, z 0.44, quiet); nifty_50 (rho 0.5 via dyn_muthootfin_ns, z -1.24, reacted); dyn_karurvysya_ns (rho 0.468 via dyn_muthootfin_ns, z 2.3, reacted); dyn_idbi_ns (rho 0.399 via dyn_muthootfin_ns, z 2.68, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.571 vs dyn_muthootfin_ns, historically leads by 3d
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.512 vs dyn_muthootfin_ns
- **India receivers**: nifty_metal (rho 0.646, z 1.01); nifty_midcap_100 (rho 0.571, z 0.44); nifty_50 (rho 0.5, z -1.24); dyn_karurvysya_ns (rho 0.468, z 2.3)
- Source: Muthoot Finance among 6 stocks flashing bullish signals, hinting at a possible uptrend — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/stocks/news/muthoot-finance-among-6-stocks-flashing-bullish-signals-hinting-at-a-possible-uptrend/slideshow/133489659.cms
- Source: Muthoot Finance, Manappuram Finance shares rally up to 11% in 4 days as gold crosses Rs 1.63 lakh — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/stocks/news/muthoot-finance-manappuram-finance-shares-rally-up-to-11-in-4-days-as-gold-crosses-rs-1-63-lakh/articleshow/133455929.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-22 (d=0.01), 2025-12-04 (d=0.01)

### [AMBER 4.63] rates · 2 series ↑
- ust_10y [RATES]: last 4.74, z20 1.79, zc 1.07, resid-z 1.37 [quiet], 1d 1.07%, |z20|=1.79; 1y-pct=99
- ust_30y [RATES]: last 5.27, z20 1.13, zc 0.90, resid-z 1.12 [quiet], 1d 0.76%, 1y-pct=98
- **Mechanism**: rates · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.768 vs ust_10y, historically leads by 1d
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.952 vs ust_10y
- Watch next: tips_10y_real (co-move) — not yet - watch; rho 0.853 vs ust_10y
- Watch next: wti (co-move) — not yet - watch; rho 0.559 vs ust_10y, historically leads by 3d
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.514 vs ust_10y
- Source: GERMAN FIN. MIN. KLINGBEIL: SURGE IN BOND YIELDS A RESULT OF TRUMP'S WAR — DeItaone, 2026-08-24. https://t.me/walter_bloomberg/34951
- Source: US stock market today: Wall Street futures slip as tech rout, Iran tensions and bond yields weigh — Mint Markets, 2026-08-24. https://www.livemint.com/market/stock-market-news/us-stock-market-today-wall-street-futures-slip-as-tech-rout-iran-tensions-and-bond-yields-weigh-11787385929496.html
- Source: This market shift resembles the post–World War II era — and bond yields could have room to go higher, says Morgan Stanley — MarketWatch Top, 2026-08-24. https://www.marketwatch.com/story/the-post-world-war-ii-market-shift-is-here-and-bond-yields-could-have-higher-to-go-says-morgan-stanley-9381532c?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.11), 2025-05-16 (d=0.19)

### [RED 4.52] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.64, z20 1.52, zc n/a, resid-z n/a [quiet], 1d 0.17%, 52-wk extreme (pct=100); |z20|=1.52; 1y-pct=100
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.48 via midcap_largecap_ratio, z 0.44, quiet); dyn_fincables_ns (rho 0.353 via midcap_largecap_ratio, z 0.88, quiet)
- **India receivers**: nifty_midcap_100 (rho 0.48, z 0.44); dyn_fincables_ns (rho 0.353, z 0.88)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [AMBER 4.27] dyn_techm_ns ↓
- dyn_techm_ns [EQUITIES]: last 1570.10, z20 -2.27, zc -0.58, resid-z -0.01 [quiet], 1d -0.88%, |z20|=2.27
- **Mechanism**: dyn_techm_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.854 via dyn_techm_ns, z -1.4, reacted); dyn_tataelxsi_ns (rho 0.397 via dyn_techm_ns, z -1.27, reacted); dyn_tatatech_ns (rho 0.363 via dyn_techm_ns, z -0.45, quiet)
- Watch next: shanghai_comp (inverse) — not yet - watch; rho -0.503 vs dyn_techm_ns, historically leads by 5d
- **India receivers**: nifty_it (rho 0.854, z -1.4); dyn_tataelxsi_ns (rho 0.397, z -1.27); dyn_tatatech_ns (rho 0.363, z -0.45)
- Source: Tech Mahindra Share Price Live Updates: Tech Mahindra's Performance Overview — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tech-mahindra-stock-price-livestock-price-today-live-updates-24-aug-2026/liveblog/133450069.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-11 (d=0.03), 2025-02-10 (d=0.09)

### [AMBER 3.97] comex_gold ↑
- comex_gold [COMMODITIES]: last 4680.60, z20 1.97, zc 0.54, resid-z 1.19 [quiet], 1d 0.86%, |z20|=1.97
- **Mechanism**: comex_gold ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.441 via comex_gold, z 1.01, reacted)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.633 vs comex_gold, historically leads by 1d
- Watch next: dax (co-move) — not yet - watch; rho 0.536 vs comex_gold, historically leads by 4d
- **India receivers**: nifty_metal (rho 0.441, z 1.01)
- Source: Gold prices fall after 4 days; silver dips Rs 4,300/kg ahead of inflation data, Warsh speech at Jackson Hole — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/commodities/news/gold-prices-fall-after-4-days-silver-dips-rs-4300/kg-ahead-of-inflation-data-warsh-speech-at-jackson-hole/articleshow/133491244.cms
- Source: Gold and silver prices drop on the MCX ahead of US inflation, Jackson Hole Symposium this week — Mint Markets, 2026-08-25. https://www.livemint.com/market/commodities/gold-and-silver-prices-mixed-on-the-mcx-ahead-of-us-inflation-jackson-hole-symposium-this-week-11787628975454.html
- Source: Gold touches highest level since mid-May as buying momentum builds — BusinessLine Mkts, 2026-08-25. https://www.thehindubusinessline.com/markets/gold/gold-touches-highest-level-since-mid-may-as-buying-momentum-builds/article71387137.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-15 (d=0.0), 2024-11-18 (d=0.1)

### [AMBER 3.9] dyn_lenskart_ns ↑
- dyn_lenskart_ns [EQUITIES]: last 660.75, z20 1.90, zc 0.55, resid-z -0.67 [quiet], 1d 0.88%, 1y-pct=99
- **Mechanism**: dyn_lenskart_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: SoftBank pares nearly 2.6% stake in Lenskart for Rs 2,888 crore — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/stocks/news/softbank-pares-nearly-2-6-stake-in-lenskart-for-rs-2888-crore/articleshow/133472713.cms
- Source: Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 20% in a month — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/stocks/news/lenskart-solutions-among-4-stocks-to-hit-52-week-highs-amp-surge-up-to-20-in-a-month/slideshow/133468092.cms
- Source: 20 stocks to watch: Lenskart, Natco Pharma, Power Grid, GHCL, Sigachi — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/markets/20-stocks-to-watch-on-monday-lenskart-natco-pharma-power-grid-ghcl-sigachi-and-others/article71383021.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

## Watchlist (below surfacing floor)
gold_silver_ratio ↑ (3.67), dyn_lth ↑ (3.43), dyn_tech ↑ (3.4), dyn_icicigi_bo ↓ (3.18), cross-asset · 2 series ↑ (3.15), dyn_pcjeweller_ns ↑ (3.02), dyn_idbi_ns ↑ (2.68), fx · 2 series ↑ (2.66), ftse_100 ↑ (2.5), dyn_karurvysya_ns ↑ (2.3), dyn_cartrade_ns ↑ (2.22), dyn_jef ↓ (2.05)

## India macro
- nifty_50: 24131.2500 (1d -0.36%, z20 -1.24, flag none)
- nifty_midcap_100: 63695.6992 (1d -0.19%, z20 0.44, flag amber)
- usd_inr: 95.7200 (1d 0.02%, z20 1.07, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6396 (1d 0.17%, z20 1.52, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 80.7 — "Stock recommendations for 25 August from MarketSmith India"
- INOXINDIA.NS (INOX INDIA LIMITED) score 80.1 — "Stock recommendations for 25 August from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 78.9 — "Stock recommendations for 25 August from MarketSmith India"
- INDIANB.NS (INDIAN BANK) score 76.5 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 2"
- BAC (Bank of America Corporation) score 65.1 — "Axis Bank Share Price Live Updates: Axis Bank Surpasses 20-Day Simple Moving Average"
- BOND (PIMCO Active Bond Exchange-Tra) score 62.1 — "India bonds may edge up as oil remains steady despite US sanctions on Iran"
- HDB (HDFC Bank Limited) score 60.5 — "Axis Bank Share Price Live Updates: Axis Bank Surpasses 20-Day Simple Moving Average"
- IDBI.NS (IDBI BANK LIMITED) score 56.8 — "Axis Bank Share Price Live Updates: Axis Bank Surpasses 20-Day Simple Moving Average"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 56.8 — "Axis Bank Share Price Live Updates: Axis Bank Surpasses 20-Day Simple Moving Average"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 56.7 — "Axis Bank Share Price Live Updates: Axis Bank Surpasses 20-Day Simple Moving Average"
- TECHM.NS (TECH MAHINDRA LIMITED) score 48.0 — "Shares dip with pressure from technology, yields and oil fall"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 46.7 — "Shares dip with pressure from technology, yields and oil fall"
- TECH (Bio-Techne Corp) score 46.6 — "Shares dip with pressure from technology, yields and oil fall"
- COIN (Coinbase Global, Inc.) score 44.9 — "Global Market: Kospi drops 2% as chip stocks tumble ahead of Nvidia earnings"
- OHI (Omega Healthcare Investors, In) score 33.0 — "Shankesh Jewellers IPO to debut today: What GMP signals for investors"
- LTH (Life Time Group Holdings, Inc.) score 31.2 — "Bitcoin tops $80,000 for the first time since mid-May"
- CHKP (Check Point Software Technolog) score 27.9 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 2"
- JIOFIN.BO (Jio Financial Services Limited) score 21.4 — "ETMarkets Smart Talk | India enters earnings-led phase; Anil Rego favours financials, auto"
- 301077.SZ (CHINASTARS) score 20.6 — "How China’s anti-corruption fight became Xi Jinping’s most important policy"
- PCJEWELLER.NS (PC JEWELLER LTD) score 18.5 — "Shankesh Jewellers IPO to debut today: What GMP signals for investors"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 15.4 — "ONTARIO PREMIER FORD: NEED TO RESTRICT ENERGY, POTASH, ELECTRICITY SHIPMENTS TO U.S."
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 14.6 — "ETMarkets Smart Talk | India enters earnings-led phase; Anil Rego favours financials, auto"
- NVDA (NVIDIA Corporation) score 12.5 — "Global Market: Kospi drops 2% as chip stocks tumble ahead of Nvidia earnings"
- MS (Morgan Stanley) score 11.9 — "JPMorgan says bond market can handle issuance stampede"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 11.3 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Sees Strong Trading Activity"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 10.7 — "Shein IPO: Fast fashion retailer eyes $27 billion price tag in long-awaited Hong Kong list"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.6 — "Stocks to buy in 2026 for long term: Welspun Corp, Tata Consumer among 5 stocks which coul"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 10.2 — "Stocks to buy in 2026 for long term: Welspun Corp, Tata Consumer among 5 stocks which coul"
- VT (Vanguard Total World Stock Ind) score 8.8 — "BESSENT: TRUMP IS MAKING PHONE CALLS TO WORLD LEADERS TO CUT ECONOMIC TIES WITH IRAN"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.8 — "ICICI raises $1 billion, Union Bank $600 million through dollar bonds"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 7.4 — "Coal India Share Price Live Updates: Coal India Ltd's Price Breakout Signals Strength"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.4 — "Adani Ent Share Price Live Updates: Adani Enterprises  Market Performance Snapshot"
- META (Meta) score 6.0 — "Stock market today: Sensex falls 170 points, Nifty 50 ends below 24,219; metal stocks shin"
- JUSTDIAL.BO (JUST DIAL LTD.) score 5.2 — "20 MILLION TO SHIP OIL THROUGH HORMUZ Shipping a supertanker through the Strait of Hormuz "
- JEF (Jefferies Financial Group Inc.) score 4.9 — "Why Jefferies’ Chris Wood sees gold as the second-best hedge amid Iran war and fiscal risk"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.6 — "SoftBank pares nearly 2.6% stake in Lenskart for Rs 2,888 crore"
- MRNA (Moderna, Inc.) score 4.1 — "Moderna’s personalized mRNA shot could reshape the fight against skin cancer — but it may "
- VOLTAS.NS (VOLTAS LTD) score 0.9 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.2 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.1 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

---
## Appendix — how every statistic in this brief is computed

**z20 (primary z-score).** For a series with daily observations x:
`z20 = (x_today − mean(x_prev20)) / std(x_prev20)`
where `x_prev20` is the 20 most recent observations STRICTLY BEFORE today
(the window excludes today, so today's move is measured against yesterday's
baseline) and std is the population standard deviation (ddof=0). Computed on
LEVELS, not returns. `z60` is identical with a 60-observation window.
A series needs the full prior window; otherwise z is n/a.

**1-year percentile (pct_1y).** Over the trailing window of up to 252
observations INCLUDING today (n = actual observations available, min 20):
`pct_1y = 100 × (count of window values strictly below today) / n`.
0 = lowest of the year, 100 = highest. (The Patterns query engine uses a
rank-based variant that treats ties by average rank — equivalent in
practice.)

**1d% / 5d%.** Simple percent change vs the observation 1 (resp. 5) trading
observations ago: `100 × (x_today/x_prev − 1)`. Reported as n/a when the
prior value is ~0 (zero-crossing spreads like 2s10s).

**Flag thresholds.**
- amber: |z20| ≥ 1.5 (backbone) or ≥ 2.0 (news-admitted names), OR pct_1y ≤5
  or ≥95, OR a named framework trigger (e.g. WTI/Brent 1-session ≥1.5%,
  TIPS 1-day ≥5bp, VIX 1-session ≥15%, gold/silver ratio >85 or <75).
- red: |z20| ≥ 2.5, OR framework trigger with |z20| above the amber bar.
- Series with <30 observations never flag (sparse guard).
- Data hygiene: an isolated print deviating >15% from BOTH neighbours in the
  same direction (spike-and-revert) is replaced by the neighbour mean before
  any statistic is computed (VIX exempt — that pattern is its signal).

**Events.** Flagged series are clustered when their 60-day daily-return
correlation satisfies |ρ| ≥ 0.65 AND today's moves are consistent with ρ's
sign. Event score = (strongest member's engine score, i.e. |z20| + 3 if a
framework trigger fired) + 1.2·ln(n_members) + 2 if corroborating news is
attached. Events surface only above a floor of 3.2, max 8 cards; the rest
are suppressed to the watchlist.

**Correlations / lead-lag (rho in "India receivers" and "watch next").**
Pearson correlation of daily percent-change returns over trailing 60d
(rho60) and 252d (rho252) windows; pairs kept at |ρ| ≥ 0.35. "Leads by k
days" means corr(return_A at t−k, return_B at t) over the 252d window is
the strongest lagged relationship, k ∈ 1..5. A "receiver/laggard" is a
correlated instrument whose own |z20| < 1.0 (it has not yet moved).

**Historical analogues.** Nearest past dates by Euclidean distance between
today's member z20 vector and every historical date's vector (last 10
sessions excluded, episodes ≥5 sessions apart). Aftermath stats are the
median/hit-rate of forward percent changes +5 and +20 observations after
each analogue date.

**zc (vol-conditional return z).** `zc = r_today / sigma_EWMA(t|t-1)` where
sigma is the RiskMetrics EWMA (lambda 0.94) of squared returns strictly
before today; GARCH(1,1) refines the latest sigma when the fit converges.
This is the "unusual" gate: it sees a 2-sigma move in a quiet regime that
the 20-day levels-z drowns. Daily series only.

**resid_z (unexplained z).** Rolling 60d OLS of the instrument's returns on
its configured factor block (betas from the window ending t-1 applied to
today's factor returns). `resid = actual − predicted`; resid_z = resid vs
the std of the prior 60 residuals. Large raw move + small resid_z = PRICED
(factors explain it); large resid_z = genuinely unexplained. Move labels:
priced / unexplained / moved / quiet per these thresholds (1.5/1.0, r2>=.25).

**Assumption statuses.** Each standing prior (safe-haven gold, oil->INR,
etc.) is scored live: VALID = 20d AND 60d return corr clear (|corr|>=0.25)
in the expected sign; INVERTED = clearly wrong sign on 20d or the contra
check fires (e.g. gold trading WITH nifty); WEAK = neither clear;
INSUFFICIENT_DATA = too few paired observations. Change-point dates mark
the last shift of the 60d rolling correlation (PELT/rbf). Co-occurrence
escalation and thesis mechanisms are gated on these statuses.

**Regime.** Rules-based risk-on/off score = mean(vol 1y-percentile,
share of equity indices below 50DMA, sign-scaled 20d equity-rates corr);
RISK_OFF >= 0.6, RISK_ON <= 0.35. Markov 2-state switching-variance
P(high-vol) reported as corroborating evidence, never as a gate.

**Data.** Daily closes: yfinance (indices/FX/commodities/equities/crypto)
and FRED (rates/credit/India macro), ~2 years of history, refreshed every
2h on weekdays with an intraday provisional last price that the official
close later overwrites. All statistics use this daily series — intraday
prints enter as today's provisional observation.

---
## How to use this brief (instruction to the assistant)
You are helping draft a macro article for an audience of Indian market
practitioners. Work ONLY from the data above — never invent numbers.
Priorities: (1) the event-to-price gap — what the news implies that price
has not yet reflected; (2) the transmission chain into Indian instruments,
using the INDIA lines and laggards; (3) historical precedent where given.
A sceptical 'no gap here' is a valid conclusion. Cite specifics (levels,
z-scores, dates) from the brief. The owner's hypotheses and journal intents
show what they are already thinking — engage with them directly.