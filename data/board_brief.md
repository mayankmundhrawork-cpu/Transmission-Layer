# Transmission Layer — board brief · 2026-09-02 08:46Z

data as of **2026-09-02** · 98 series · 11 red / 38 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.465, 2d in regime; vol-pct 0.347, breadth-off 0.583, Markov P(high-vol) 0.021)
- [INVERTED] **safe_haven_gold** — corr20 -0.43, corr60 -0.4, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.84, corr60 0.87, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.1, corr60 0.31, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.16, corr60 0.05, last shift 2026-06-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.38, corr60 -0.84, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.23, corr60 -0.12, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.34, corr60 -0.15, last shift 2026-06-29. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.07, corr60 0.21, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 90** scanned series survive multiplicity control (effective p ≤ 0.0002726380408915041)
- **SETUP** ust_2y → usd_jpy: leads 1d (ccf 0.49, β 0.2162, p 0.0); driver zc 2.79 → expected 0.721%. Type hit-rate 0.828 (n=1971).
- Track record · residual_reversion: hit-rate **0.5** (n=1115) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.828** (n=1971) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.54] cross-asset · 11 series ↓
- russell_2000 [INDICES]: last 2920.04, z20 -3.66, zc -1.02, resid-z -0.59 [quiet], 1d -1.23%, |z20|=3.66
- dax [INDICES]: last 25865.59, z20 -2.52, zc -0.46, resid-z -0.71 [quiet], 1d -0.40%, |z20|=2.52
- stoxx_50 [INDICES]: last 6356.44, z20 -2.49, zc -0.23, resid-z -0.32 [quiet], 1d -0.20%, |z20|=2.49
- dow_jones [INDICES]: last 52773.59, z20 -2.42, zc -1.11, resid-z 0.18 [quiet], 1d -0.78%, |z20|=2.42
- vix [INDICES]: last 16.49, z20 2.32, zc 0.11, resid-z n/a [quiet], 1d 0.92%, |z20|=2.32
- dyn_vt [EQUITIES]: last 159.32, z20 -2.24, zc -1.11, resid-z 0.35 [quiet], 1d -0.77%, |z20|=2.24
- sp500 [INDICES]: last 7632.60, z20 -2.05, zc -0.99, resid-z -0.32 [quiet], 1d -0.70%, |z20|=2.05
- wti [COMMODITIES]: last 90.18, z20 2.00, zc -0.02, resid-z 1.42 [quiet], 1d -0.04%, |z20|=2.00
- cac_40 [INDICES]: last 8266.99, z20 -1.95, zc -0.47, resid-z 0.48 [quiet], 1d -0.42%, |z20|=1.95
- nasdaq_100 [INDICES]: last 29080.06, z20 -1.62, zc -1.18, resid-z -0.39 [quiet], 1d -1.28%, |z20|=1.62
- brent [COMMODITIES]: last 94.70, z20 1.50, zc 0.02, resid-z 1.25 [quiet], 1d 0.05%, |z20|=1.50
- **Mechanism**: cross-asset · 11 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-11-26 (z-distance 0.54).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_adanient_bo (rho 0.459 via dax, z -1.65, reacted); dyn_indusindbk_bo (rho 0.427 via cac_40, z -2.26, reacted)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.501 vs dax, historically leads by 5d
- Watch next: shanghai_comp (co-move) — not yet - watch; rho 0.449 vs nasdaq_100, historically leads by 1d
- Watch next: dyn_nvda (inverse) — not yet - watch; rho -0.546 vs vix
- Watch next: india_vix (inverse) — not yet - watch; rho -0.516 vs cac_40
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.512 vs wti
- **India receivers**: dyn_adanient_bo (rho 0.459, z -1.65); dyn_indusindbk_bo (rho 0.427, z -2.26)
- Source: Sensex today | Stock Market Live: Sensex down 500 pts, Nifty trades near 23,850 as crude oil surges; Auto stocks weigh markets down — BusinessLine Mkts, 2026-09-02. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-2nd-september-2026/article71416736.ece
- Source: Crude oil price rise as US conducts fresh strikes on Iranian targets — BusinessLine Mkts, 2026-09-02. https://www.thehindubusinessline.com/markets/commodities/crude-oil-futures-rise-as-us-conducts-fresh-strikes-on-iranian-targets/article71418065.ece
- Source: Markets sink mid-session; auto stocks bleed as crude surges — BusinessLine Mkts, 2026-09-02. https://www.thehindubusinessline.com/markets/markets-sink-mid-session-auto-stocks-bleed-as-crude-surges/article71418626.ece
- Historical analogues: 2024-11-26 (d=0.54), 2024-10-21 (d=0.71), 2024-11-14 (d=0.75)

### [RED 8.24] cross-asset · 5 series ↑
- dyn_bond [EQUITIES]: last 89.76, z20 -4.31, zc -2.35, resid-z 0.00 [priced], 1d -0.73%, |z20|=4.31; 1y-pct=0
- ust_2y [RATES]: last 4.34, z20 3.15, zc 2.79, resid-z 2.28 [unexplained], 1d 0.00%, |z20|=3.15; 1y-pct=99
- ust_10y [RATES]: last 4.75, z20 2.04, zc 1.32, resid-z 0.99 [quiet], 1d 0.42%, |z20|=2.04; 1y-pct=99
- tips_10y_real [RATES]: last 2.44, z20 1.28, zc 2.13, resid-z 1.76 [unexplained], 1d 0.83%, 1y-pct=98
- ust_30y [RATES]: last 5.25, z20 0.74, zc 0.71, resid-z 0.58 [quiet], 1d 0.57%, 1y-pct=97
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eur_usd (co-move) — not yet - watch; rho 0.515 vs ust_10y, historically leads by 1d
- Source: Why are global bond yields surging to multi-decade highs? — ET Markets, 2026-09-02. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/why-are-global-bond-yields-surging-to-multi-decade-highs/articleshow/133703126.cms
- Source: Explained: How multi-decade high global bond yields spell caution for Indian stock market investors — ET Markets, 2026-09-02. https://economictimes.indiatimes.com/markets/bonds/explained-how-multi-decade-high-global-bond-yields-spell-caution-for-indian-stock-market-investors/articleshow/133702453.cms
- Source: US Stock Market: Higher long-term Treasury yields face structural headwinds — ET Markets, 2026-09-02. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stock-market-higher-long-term-treasury-yields-face-structural-headwinds/articleshow/133702242.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 6.03] dyn_heromotoco_ns ↓
- dyn_heromotoco_ns [EQUITIES]: last 5230.00, z20 -4.03, zc -3.83, resid-z -3.64 [unexplained], 1d -5.85%, |z20|=4.03
- **Mechanism**: dyn_heromotoco_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_voltas_ns (rho 0.36 via dyn_heromotoco_ns, z -2.59, reacted)
- **India receivers**: dyn_voltas_ns (rho 0.36, z -2.59)
- Source: Hero MotoCorp, Eicher Motors fall despite strong August sales — BusinessLine Mkts, 2026-09-02. https://www.thehindubusinessline.com/markets/hero-motocorp-eicher-motors-fall-despite-strong-august-sales/article71418612.ece
- Source: Why Hero MotoCorp shares fell 5% despite record dispatches — BusinessLine Mkts, 2026-09-02. https://www.thehindubusinessline.com/markets/stock-markets/hero-motocorp-shares-slide-5-as-retail-data-disappoints-despite-record-dispatch-numbers/article71418322.ece
- Source: Hero MotoCorp shares fall over 4% as August exports, motorcycle dispatches decline — ET Markets, 2026-09-02. https://economictimes.indiatimes.com/markets/stocks/news/hero-motocorp-shares-fall-over-4-as-august-exports-motorcycle-dispatches-decline/articleshow/133700041.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-22 (d=0.03), 2025-07-09 (d=0.04)

### [RED 4.9] dyn_icicigi_bo ↓
- dyn_icicigi_bo [EQUITIES]: last 1534.05, z20 -2.90, zc -1.41, resid-z -0.84 [quiet], 1d -2.10%, |z20|=2.90; 1y-pct=0
- **Mechanism**: dyn_icicigi_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Expert view: Favour value over growth; IT not an outright contra bet, says Chockalingam Narayanan of ICICI Pru AMC — Mint Markets, 2026-09-01. https://www.livemint.com/market/stock-market-news/expert-view-favour-value-over-growth-it-not-an-outright-contra-bet-says-chockalingam-narayanan-of-icici-pru-amc-11788256314458.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.0), 2025-05-30 (d=0.03)

### [RED 4.65] dyn_lth ↓
- dyn_lth [EQUITIES]: last 41.83, z20 -2.65, zc -0.19, resid-z -0.94 [quiet], 1d -0.45%, |z20|=2.65
- **Mechanism**: dyn_lth ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Every time FIIs panicked, here's what happened next - Nikhil Kamath explains why smart foreign money isn't always right — Mint Markets, 2026-09-02. https://www.livemint.com/market/stock-market-news/every-time-fiis-panicked-heres-what-happened-zerodha-nikhil-kamath-explains-why-smart-foreign-money-isnt-always-right-11788328352008.html
- Source: US Oil Tops $90 for First Time Since July Amid Fresh Strikes — Mint Markets, 2026-09-01. https://www.livemint.com/market/us-oil-tops-90-for-first-time-since-july-amid-fresh-strikes-11788290702226.html
- Source: Global Market: Japan bond yields hit 3% for first time in 30 years amid inflation, fiscal risks — ET Markets, 2026-09-01. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-japan-bond-yields-hit-3-for-first-time-in-30-years-amid-inflation-fiscal-risks/articleshow/133671709.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.01), 2025-04-17 (d=0.02)

### [AMBER 4.31] nifty_50 ↓
- nifty_50 [INDICES]: last 23883.40, z20 -2.31, zc -1.36, resid-z 0.26 [quiet], 1d -0.72%, |z20|=2.31
- **Mechanism**: nifty_50 ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-01-14 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.719 via nifty_50, z -1.41, reacted); nifty_midcap_100 (rho 0.646 via nifty_50, z -3.63, reacted); nifty_fmcg (rho 0.613 via nifty_50, z -1.82, reacted); nifty_it (rho 0.524 via nifty_50, z 0.02, quiet); dyn_techm_ns (rho 0.488 via nifty_50, z 0.07, quiet)
- Watch next: india_vix (inverse) — not yet - watch; rho -0.74 vs nifty_50
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.524 vs nifty_50, historically leads by 3d
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.641 vs nifty_50
- **India receivers**: dyn_jiofin_bo (rho 0.719, z -1.41); nifty_midcap_100 (rho 0.646, z -3.63); nifty_fmcg (rho 0.613, z -1.82); nifty_it (rho 0.524, z 0.02)
- Source: Sensex today | Stock Market Live: Sensex down 500 pts, Nifty trades near 23,850 as crude oil surges; Auto stocks weigh markets down — BusinessLine Mkts, 2026-09-02. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-2nd-september-2026/article71416736.ece
- Source: Bigger market crash ahead? Analysts weigh how Sensex, Nifty may react if US 10-year bond yield touches 5% — ET Markets, 2026-09-02. https://economictimes.indiatimes.com/markets/stocks/news/bigger-market-crash-ahead-analysts-weigh-how-sensex-nifty-may-react-if-us-10-year-bond-yield-touches-5/articleshow/133702065.cms
- Source: Sensex falls 700 pts, Nifty below 24,000 as crude oil surges: What’s driving the fall? — BusinessLine Mkts, 2026-09-02. https://www.thehindubusinessline.com/markets/nifty-breaches-24000-as-oil-spike-and-bond-yield-surge-rattle-markets/article71418055.ece
- Historical analogues: 2026-01-14 (d=0.0), 2024-11-12 (d=0.04), 2025-07-18 (d=0.05)

### [AMBER 4.07] natgas ↑
- natgas [COMMODITIES]: last 2.95, z20 2.07, zc 0.51, resid-z -0.15 [quiet], 1d 1.55%, |z20|=2.07
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.024 vs natgas, historically leads by 4d
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.022 vs natgas, historically leads by 4d
- Source: Pakistan Rejects Costly LNG Cargo as Blackout Risk Deepens — OilPrice, 2026-09-02. https://oilprice.com/Latest-Energy-News/World-News/Pakistan-Rejects-Costly-LNG-Cargo-as-Blackout-Risk-Deepens.html
- Source: Asia Spot LNG Prices Hit 5-Month High as Hormuz Blockage Drags On — OilPrice, 2026-09-01. https://oilprice.com/Latest-Energy-News/World-News/Asia-Spot-LNG-Prices-Hit-5-Month-High-as-Hormuz-Blockage-Drags-On.html
- Source: U.S. LNG exports rose 23% in the first half of 2026 because of higher capacity — EIA Today in Energy, 2026-09-01. https://www.eia.gov/todayinenergy/detail.php?id=
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [AMBER 4.01] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1677.40, z20 2.01, zc -0.86, resid-z -1.23 [quiet], 1d -2.79%, |z20|=2.01; 1y-pct=99
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Ather Energy surges 130% in 2026, outpacing Tesla, BYD — BusinessLine Mkts, 2026-09-01. https://www.thehindubusinessline.com/markets/stock-markets/ather-energy-surges-130-in-2026-outpacing-tesla-byd/article71414201.ece
- Source: Ather Energy’s 130% stock surge leaves Tesla and BYD behind in 2026 — ET Markets, 2026-09-01. https://economictimes.indiatimes.com/markets/stocks/news/ather-energys-130-stock-surge-leaves-tesla-and-byd-behind-in-2026/articleshow/133672575.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

## Watchlist (below surfacing floor)
wheat ↑ (3.91), nikkei_225 ↓ (3.86), nifty_midcap_100 ↓ (3.63), dyn_havells_ns ↓ (3.57), dyn_tataelxsi_ns ↓ (3.51), gold_silver_ratio ↑ (3.28), midcap_largecap_ratio ↑ (3.2), dyn_hdb ↓ (2.98), sofr ↑ (2.83), dyn_voltas_ns ↓ (2.59), dyn_indusindbk_bo ↓ (2.26), corn ↑ (2.14)

## India macro
- nifty_50: 23883.4004 (1d -0.72%, z20 -2.31, flag amber)
- nifty_midcap_100: 62791.2500 (1d -0.86%, z20 -3.63, flag red)
- usd_inr: 94.9600 (1d -0.16%, z20 -0.82, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6291 (1d -0.14%, z20 0.20, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 83.2 — "Stock recommendations for 2 September from MarketSmith India"
- COALINDIA.NS (COAL INDIA LTD) score 81.7 — "Stock recommendations for 2 September from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 79.4 — "Stock recommendations for 2 September from MarketSmith India"
- INDIANB.NS (INDIAN BANK) score 72.8 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 2"
- BAC (Bank of America Corporation) score 62.9 — "How to trade HDFC Bank shares after new 52-week low? 2 technical analysts explain"
- COIN (Coinbase Global, Inc.) score 57.6 — "Global Market: South Korean stocks slide more than 3% as Iran conflict deepens global mark"
- BOND (PIMCO Active Bond Exchange-Tra) score 55.9 — "Fresh selloff on cards for India bonds as oil, Treasury yields see persistent spike"
- HDB (HDFC Bank Limited) score 54.7 — "How to trade HDFC Bank shares after new 52-week low? 2 technical analysts explain"
- IDBI.NS (IDBI BANK LIMITED) score 52.8 — "How to trade HDFC Bank shares after new 52-week low? 2 technical analysts explain"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 52.8 — "How to trade HDFC Bank shares after new 52-week low? 2 technical analysts explain"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 52.8 — "How to trade HDFC Bank shares after new 52-week low? 2 technical analysts explain"
- TECHM.NS (TECH MAHINDRA LIMITED) score 37.3 — "HCL Tech Share Price Live Updates: HCL Tech's Performance Overview"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 36.8 — "HCL Tech Share Price Live Updates: HCL Tech's Performance Overview"
- TECH (Bio-Techne Corp) score 36.8 — "HCL Tech Share Price Live Updates: HCL Tech's Performance Overview"
- CHKP (Check Point Software Technolog) score 34.3 — "ESDS Software Solution IPO allotment in focus today; GMP hints 59% listing pop, 6 steps to"
- 301077.SZ (CHINASTARS) score 32.2 — "China’s corruption investigation procedures"
- OHI (Omega Healthcare Investors, In) score 31.4 — "Best FII bets: 3 AI-linked stocks and up to 250% rally in Q1. Have investors missed the bu"
- LTH (Life Time Group Holdings, Inc.) score 30.7 — "Global Market: China, Hong Kong stocks fall as global bond selloff, oil surge weigh on sen"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 26.2 — "U.S. Energy Secretary Says Venezuela Could More Than Double Oil Production"
- PCJEWELLER.NS (PC JEWELLER LTD) score 16.9 — "Deepa Jewellers IPO GMP today: Grey market hints 25% listing gain; check subscription, rev"
- NVDA (NVIDIA Corporation) score 16.2 — "SB Energy heads for IPO after Nvidia backs $105 billion OpenAI data-centre project"
- JIOFIN.BO (Jio Financial Services Limited) score 14.0 — "Wipro Share Price Live Updates: Wipro's Financial Snapshot"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 13.9 — "Purple Style Labs IPO Day 3: GMP, subscription status, key details. Should you subscribe?"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 11.9 — "Why Coal India share price is surging today - Here's what fuelling the PSU stock rally"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 10.8 — "Bajaj Finance Share Price Live Updates: Bajaj Finance's Price and Performance Overview"
- META (Meta) score 9.1 — "META - META DISABLES CAMERAS ON SOME TAMPERED SMART GLASSES - SEMAFOR"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.0 — "How Adani Group stocks are performing today after share prices plunged yesterday | Top gai"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 8.9 — "Why auto stocks are down today? Eicher, Tata Motors, Hyundai, Bajaj Auto and others - Chec"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 8.8 — "Why auto stocks are down today? Eicher, Tata Motors, Hyundai, Bajaj Auto and others - Chec"
- MS (Morgan Stanley) score 8.2 — "JPMORGAN: RISING YIELDS WON’T KILL STOCK RALLY JPMorgan remains bullish on global equities"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.0 — "TRUMP: THE UNITED STATES IS, AS WE SPEAK, STRIKING IRANIAN TARGETS NEAR THE STRAIT OF TRUM"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 7.9 — "Wipro Share Price Live Updates: Wipro's Financial Snapshot"
- VT (Vanguard Total World Stock Ind) score 7.4 — "What’s behind the selloff in world bond markets?"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.5 — "Expert view: Favour value over growth; IT not an outright contra bet, says Chockalingam Na"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.7 — "Lenskart shares to rally 40%? Nomura initiates coverage with Buy, says its growth journey "
- HEROMOTOCO.NS (HERO MOTOCORP LIMITED) score 2.0 — "Hero MotoCorp shares fall over 4% as August exports, motorcycle dispatches decline"
- SWIGGY.NS (SWIGGY LIMITED) score 2.0 — "Swiggy share price down today: Why food delivery stock is delivering 'red' today | Negativ"
- DKS (Dick's Sporting Goods Inc) score 1.1 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- MRNA (Moderna, Inc.) score 0.8 — "Can Wolfe’s upgrade push Moderna stock higher?"
- VOLTAS.NS (VOLTAS LTD) score 0.1 — "Voltas reported strong growth in June quarter, but failed to impress"

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