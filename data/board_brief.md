# Transmission Layer — board brief · 2026-11-26 03:41Z

data as of **2026-11-26** · 97 series · 6 red / 44 amber · 8 events surfaced (31 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 1.0, 9d in regime; vol-pct None, breadth-off 1.0, Markov P(high-vol) 0.211)
- [WEAK] **safe_haven_gold** — corr20 -0.13, corr60 -0.24, contra nifty_50 corr20=0.2, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.93, corr60 0.88, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.35, corr60 0.21, last shift 2026-09-23. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.15, corr60 0.06, last shift 2026-09-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.9, last shift 2026-09-24. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.06, corr60 -0.0, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.18, corr60 -0.01, last shift 2026-08-12. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.25, corr60 0.33, last shift 2026-10-08. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **4 of 88** scanned series survive multiplicity control (effective p ≤ 0.000779424725164013)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.509** (n=1138) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=2213) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.35] cross-asset · 4 series ↓
- gold_silver_ratio [DERIVED]: last 86.08, z20 1.69, zc n/a, resid-z n/a [quiet], 1d 0.02%, GSR>85 (extreme high); |z20|=1.69; 1y-pct=99
- comex_silver [COMMODITIES]: last 41.87, z20 -1.58, zc 0.00, resid-z 1.13 [quiet], 1d 0.01%, |z20|=1.58; 1y-pct=1; co-occur[gold_silver] same-direction (channel VALID)
- comex_copper [COMMODITIES]: last 5.48, z20 -1.53, zc 0.00, resid-z 1.73 [unexplained], 1d 0.01%, |z20|=1.53; co-occur[metal_copper] suppressed: channel WEAK
- comex_gold [COMMODITIES]: last 3603.60, z20 -1.47, zc 0.01, resid-z -2.50 [unexplained], 1d 0.03%, 1y-pct=1; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.601 via comex_gold, z -0.55, quiet); dyn_karurvysya_ns (rho 0.502 via comex_gold, z 0.65, quiet)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.585 vs comex_silver, historically leads by 4d
- Watch next: dyn_karurvysya_ns (co-move) — not yet - watch; rho 0.502 vs comex_gold, historically leads by 4d
- **India receivers**: dyn_muthootfin_ns (rho 0.601, z -0.55); dyn_karurvysya_ns (rho 0.502, z 0.65)
- Source: Gold prices fall below $3,500, silver rises 0.7% as Fed rate hike bets weigh on bullion: Gold Silver Rates Live Updates — ET Markets, 2026-11-26. https://economictimes.indiatimes.com/markets/stocks/live-blog/url-live-updates-gold-rate-today-26th-november-24k-22k-20k-18-carat-mcx-gold-silver-price-in-delhi-hyderabad-chennai-bengaluru-citywise/liveblog/136176736.cms
- Source: Gold extends losses as hot US inflation cements Fed hike bets — ET Markets, 2026-11-26. https://economictimes.indiatimes.com/markets/commodities/news/gold-extends-losses-as-hot-us-inflation-cements-fed-hike-bets/articleshow/136176262.cms
- Source: Copper slumps to lowest in 11 months as investors flee — ET Markets, 2026-11-25. https://economictimes.indiatimes.com/markets/commodities/copper-slumps-to-lowest-in-11-months-as-investors-flee/articleshow/136172100.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.34)

### [RED 7.08] usd_inr ↓
- usd_inr [FX]: last 92.47, z20 -2.08, zc -0.88, resid-z -0.00 [quiet], 1d -0.36%, 20d range extreme; |z20|=2.08
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indianb_ns (rho -0.448 via usd_inr, z 0.73, quiet); nifty_it (rho -0.442 via usd_inr, z 0.29, quiet); dyn_havells_ns (rho -0.434 via usd_inr, z 1.21, reacted); dyn_techm_ns (rho -0.379 via usd_inr, z 0.8, quiet); dyn_tataelxsi_ns (rho -0.374 via usd_inr, z 0.43, quiet)
- **India receivers**: dyn_indianb_ns (rho -0.448, z 0.73); nifty_it (rho -0.442, z 0.29); dyn_havells_ns (rho -0.434, z 1.21); dyn_techm_ns (rho -0.379, z 0.8)
- Source: Rupee has room to rally before RBI steps in, strategists say — ET Markets, 2026-11-26. https://economictimes.indiatimes.com/markets/forex/rupee-has-room-to-rally-before-rbi-steps-in-strategists-say/articleshow/136176673.cms
- Source: Rupee hits eight-month high as foreign inflows lift markets; Nifty nears record peak — BusinessLine Mkts, 2026-11-25. https://www.thehindubusinessline.com/markets/rupee-hits-eight-month-high-as-foreign-inflows-lift-markets-nifty-nears-record-peak/article71743427.ece
- Source: Rupee soars 69 paise to settle at its eight-month high of 92.16 against US dollar — BusinessLine Mkts, 2026-11-25. https://www.thehindubusinessline.com/markets/forex/rupee-soars-69-paise-to-settle-at-its-eight-month-high-of-9216-against-us-dollar/article71742189.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [AMBER 6.6] cross-asset · 6 series ↓
- stoxx_50 [INDICES]: last 5904.97, z20 -2.45, zc -1.23, resid-z -2.24 [unexplained], 1d -1.65%, |z20|=2.45
- dax [INDICES]: last 24736.99, z20 -2.32, zc -0.80, resid-z -1.80 [unexplained], 1d -1.12%, |z20|=2.32
- dyn_ms [EQUITIES]: last 167.53, z20 -2.15, zc -0.29, resid-z -1.14 [quiet], 1d -0.75%, |z20|=2.15
- dyn_gs [EQUITIES]: last 800.45, z20 -2.12, zc -0.25, resid-z -1.23 [quiet], 1d -0.69%, |z20|=2.12; 1y-pct=5
- ftse_100 [INDICES]: last 10433.66, z20 -1.68, zc -0.43, resid-z -0.63 [quiet], 1d -0.32%, |z20|=1.68
- vix [INDICES]: last 28.32, z20 1.18, zc 0.69, resid-z n/a [quiet], 1d 7.44%, 1y-pct=98
- **Mechanism**: cross-asset · 6 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-04-01 (z-distance 0.82).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.512 via dax, z -0.55, quiet); dyn_kaynes_ns (rho 0.429 via ftse_100, z -2.31, reacted); nifty_metal (rho 0.369 via ftse_100, z -1.92, reacted); dyn_tataelxsi_ns (rho 0.369 via ftse_100, z 0.43, quiet)
- Watch next: cac_40 (co-move) — not yet - watch; rho 0.898 vs stoxx_50
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.76 vs dyn_gs
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.513 vs stoxx_50, historically leads by 5d
- Watch next: wti (inverse) — not yet - watch; rho -0.512 vs stoxx_50, historically leads by 4d
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.512 vs dax
- **India receivers**: dyn_muthootfin_ns (rho 0.512, z -0.55); dyn_kaynes_ns (rho 0.429, z -2.31); nifty_metal (rho 0.369, z -1.92); dyn_tataelxsi_ns (rho 0.369, z 0.43)
- Source: CRWV - COREWEAVE BANKS PREPARE $4.5 BILLION LOAN SALE AS DEFAULT FEARS SURGE Morgan Stanley and MUFG are preparing to sell $4.5 billion in CoreWeave-linked debt as soon as next week, Bloomberg reports. The loan, backed by GPUs supporting a Meta data center project, is expected to carry investment-gr — DeItaone, 2026-11-25. https://t.me/walter_bloomberg/39209
- Source: SPY $QQQ - GOLDMAN WARNS IT'S TOO EARLY TO BUY THE AI SELLOFF Goldman Sachs strategist Christian Mueller-Glissmann warns that markets remain fragile as investors question AI investment returns and elevated borrowing costs. Goldman's risk appetite indicator has not reached levels typically associated — DeItaone, 2026-11-25. https://t.me/walter_bloomberg/39170
- Source: CBOE VOLATILITY INDEX UP 4.54 POINTS AT 30.88 — DeItaone, 2026-11-25. https://t.me/walter_bloomberg/39169
- Historical analogues: 2026-04-01 (d=0.82), 2025-10-31 (d=1.49), 2025-10-24 (d=1.62)

### [AMBER 5.12] rates · 2 series ↑
- hy_oas [RATES]: last 3.72, z20 2.29, zc 0.71, resid-z 0.43 [quiet], 1d 2.48%, |z20|=2.29; 1y-pct=99
- ig_oas [RATES]: last 0.98, z20 2.17, zc 0.45, resid-z 0.00 [quiet], 1d 1.03%, |z20|=2.17; 1y-pct=99
- **Mechanism**: rates · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.485 via ig_oas, z -2.06, reacted)
- Watch next: ust_2y (inverse) — not yet - watch; rho -0.527 vs hy_oas
- **India receivers**: midcap_largecap_ratio (rho -0.485, z -2.06)
- Source: U.S. $44 BILLION 7-YEAR TREASURY AUCTION TAILS AS DEMAND DISAPPOINTS The U.S. Treasury sold $44 billion in 7-year notes at a high yield of 4.708%, above the 4.698% when-issued yield before the auction. That represents a 1-basis-point tail, signaling weaker-than-expected demand. 🔸 Bid-to-cover ratio: — DeItaone, 2026-11-25. https://t.me/walter_bloomberg/39202
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-01 (d=0.48), 2026-07-01 (d=0.59)

### [RED 4.68] dyn_chkp ↑
- dyn_chkp [EQUITIES]: last 163.83, z20 2.68, zc 1.04, resid-z 0.00 [quiet], 1d 2.82%, |z20|=2.68
- **Mechanism**: dyn_chkp ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Devyani Intl, DOMS Industries shares: Top 2 stocks to buy in near term; check target price, stop loss by Nagaraj Shetti — Mint Markets, 2026-11-26. https://www.livemint.com/market/stock-market-news/devyani-intl-doms-industries-shares-top-2-stocks-to-buy-in-near-term-check-target-price-stop-loss-by-nagaraj-shetti-11795622752268.html
- Source: LG Electronics shares to be in focus as promoter to sell 2% stake to meet public float norms; check details — Mint Markets, 2026-11-25. https://www.livemint.com/market/lg-electronics-shares-to-be-in-focus-as-promoter-to-sell-2-stake-to-meet-public-float-norms-check-details-11795612944008.html
- Source: NSE shares hit record high after ICICI Securities initiates coverage with Buy; check target price and key triggers — Mint Markets, 2026-11-25. https://www.livemint.com/market/stock-market-news/nse-shares-hit-record-high-after-icici-securities-initiates-coverage-with-buy-check-target-price-and-key-triggers-11795600817257.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2025-05-20 (d=0.04)

### [AMBER 4.45] natgas ↑
- natgas [COMMODITIES]: last 3.68, z20 2.45, zc 0.00, resid-z 3.61 [unexplained], 1d 0.00%, |z20|=2.45
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Global LNG Supply Crunch Set to Spill Into 2027 — OilPrice, 2026-11-25. https://oilprice.com/Latest-Energy-News/World-News/Global-LNG-Supply-Crunch-Set-to-Spill-Into-2027.html
- Source: Goldman Sachs Sees U.S. Natural Gas Demand Surging on Data Center Boom — OilPrice, 2026-11-25. https://oilprice.com/Latest-Energy-News/World-News/Goldman-Sachs-Sees-US-Natural-Gas-Demand-Surging-on-Data-Center-Boom.html
- Source: Iran Faces a Deepening Natural Gas Crisis Ahead of Winter — OilPrice, 2026-11-24. https://oilprice.com/Energy/Energy-General/Iran-Faces-a-Deepening-Natural-Gas-Crisis-Ahead-of-Winter.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [AMBER 4.33] cross-asset · 2 series ↓
- dyn_coin [EQUITIES]: last 103.71, z20 -1.50, zc 0.28, resid-z -1.54 [unexplained], 1d 1.33%, 1y-pct=1
- btc_usd [CRYPTO]: last 60597.92, z20 -1.10, zc 0.46, resid-z 0.12 [quiet], 1d 1.10%, 1y-pct=4
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-03-31 (z-distance 0.14).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (inverse) — not yet - watch; rho -0.557 vs btc_usd, historically leads by 3d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.528 vs dyn_coin, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.525 vs btc_usd
- Source: Will Nifty cross 26,000 today? FPI inflows, global cues in focus — BusinessLine Mkts, 2026-11-26. https://www.thehindubusinessline.com/markets/will-nifty-cross-26000-today-fpi-inflows-global-cues-in-focus/article71745061.ece
- Source: Global Market Today: Asian equities advance after late rebound in US stocks — ET Markets, 2026-11-26. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-today-asian-equities-advance-after-late-rebound-in-us-stocks/articleshow/136175415.cms
- Source: Bitcoin Miners Hammered Again as Price Rout Squeezes Margins — Mint Markets, 2026-11-25. https://www.livemint.com/market/bitcoin-miners-hammered-again-as-price-rout-squeezes-margins-11795637714378.html
- Historical analogues: 2025-03-31 (d=0.14), 2026-04-01 (d=0.15), 2025-10-30 (d=0.19)

### [AMBER 4.18] fx · 2 series ↓
- gbp_usd [FX]: last 1.31, z20 -1.35, zc -0.29, resid-z 1.75 [unexplained], 1d -0.11%, 1y-pct=1
- eur_usd [FX]: last 1.10, z20 -1.24, zc -0.02, resid-z 1.72 [unexplained], 1d -0.01%, 1y-pct=0
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: usd_cny (co-move) — not yet - watch; rho 0.005 vs eur_usd, historically leads by 1d
- Source: Card payments edge past cash in shops; euro area consumers want both — ECB press, 2026-11-25. https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr261125~26d1ade228.en.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

## Watchlist (below surfacing floor)
equities · 2 series ↓ (4.14), dyn_301077_sz ↓ (3.93), dyn_tgt ↑ (3.8), usd_mxn ↑ (3.23), dyn_bajfinance_ns ↑ (3.21), dyn_eternal_ns ↑ (3.08), dyn_lth ↑ (3.06), dyn_2545_tw ↓ (3.05), cross-asset · 2 series ↓ (2.75), dyn_4417_t ↑ (2.48), shanghai_comp ↓ (2.43), corn ↑ (2.31)

## India macro
- nifty_50: 25819.2500 (1d 1.85%, z20 1.30, flag none)
- nifty_midcap_100: 61582.6992 (1d 0.29%, z20 0.85, flag none)
- usd_inr: 92.4750 (1d -0.36%, z20 -2.08, flag red)
- goi_10y: 7.3800 (1d 4.53%, z20 3.03, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.1400 (1d -5.73%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.3851 (1d -1.53%, z20 -2.06, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 71.9 — "Stock recommendations for 26 November from MarketSmith India"
- NVDA (NVIDIA Corporation) score 70.4 — "NVDA - U.S. INTELLIGENCE FINDS NO EVIDENCE CHINA ORCHESTRATED JENSEN HUANG AFFAIR — WSJ U."
- INOXINDIA.NS (INOX INDIA LIMITED) score 67.7 — "Stock recommendations for 26 November from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 67.5 — "Stock recommendations for 26 November from MarketSmith India"
- INDIANB.NS (INDIAN BANK) score 58.1 — "COREWEAVE’S BANKS TO SELL $4.5 BILLION META-TIED LOAN NEXT WEEK"
- BAC (Bank of America Corporation) score 45.3 — "SPY $QQQ - TRUMP BLAMES STOCK MARKET SELLOFF ON MIDTERM ELECTIONS President Trump blames W"
- HDB (HDFC Bank Limited) score 40.4 — "COREWEAVE’S BANKS TO SELL $4.5 BILLION META-TIED LOAN NEXT WEEK"
- TGT (Target Corporation) score 37.0 — "Devyani Intl, DOMS Industries shares: Top 2 stocks to buy in near term; check target price"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 36.8 — "COREWEAVE’S BANKS TO SELL $4.5 BILLION META-TIED LOAN NEXT WEEK"
- IDBI.NS (IDBI BANK LIMITED) score 36.8 — "COREWEAVE’S BANKS TO SELL $4.5 BILLION META-TIED LOAN NEXT WEEK"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 36.8 — "COREWEAVE’S BANKS TO SELL $4.5 BILLION META-TIED LOAN NEXT WEEK"
- OHI (Omega Healthcare Investors, In) score 35.4 — "Volatility-weary US investors side swiped as tariff mayhem adds to tech pain"
- TECHM.NS (TECH MAHINDRA LIMITED) score 33.3 — "Volatility-weary US investors side swiped as tariff mayhem adds to tech pain"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 32.1 — "Volatility-weary US investors side swiped as tariff mayhem adds to tech pain"
- TECH (Bio-Techne Corp) score 32.1 — "Volatility-weary US investors side swiped as tariff mayhem adds to tech pain"
- 2545.TW (HUANG HSIANG CONSTRUCTION) score 31.2 — "NVDA - U.S. INTELLIGENCE FINDS NO EVIDENCE CHINA ORCHESTRATED JENSEN HUANG AFFAIR — WSJ U."
- BLLN (BillionToOne, Inc.) score 29.8 — "U.S. $44 BILLION 7-YEAR TREASURY AUCTION TAILS AS DEMAND DISAPPOINTS The U.S. Treasury sol"
- 301077.SZ (CHINASTARS) score 23.4 — "NVDA - U.S. INTELLIGENCE FINDS NO EVIDENCE CHINA ORCHESTRATED JENSEN HUANG AFFAIR — WSJ U."
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.4 — "UK Energy Bills Set to Soar 26% as Iran War Drives Up Gas Prices"
- COIN (Coinbase Global, Inc.) score 20.4 — "NVDA - S&P PLACES NVIDIA'S AA CREDIT RATING ON WATCH FOR POSSIBLE DOWNGRADE S&P Global Rat"
- CHKP (Check Point Software Technolog) score 19.0 — "Devyani Intl, DOMS Industries shares: Top 2 stocks to buy in near term; check target price"
- LTH (Life Time Group Holdings, Inc.) score 18.9 — "Nasdaq 100 plunges nearly 5%, briefly enters bear-market zone as AI fears and fresh tariff"
- BOND (PIMCO Active Bond Exchange-Tra) score 14.4 — "CRWV - COREWEAVE BONDS PLUNGE AS 2031 YIELD SURGES TO 17.91% CoreWeave's debt is coming un"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.6 — "Stocks to watch, November 26: LG Electronics, Tata Steel, SG Mart, APL Apollo Tubes, Fino "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.6 — "Stocks to watch, November 26: LG Electronics, Tata Steel, SG Mart, APL Apollo Tubes, Fino "
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 13.1 — "Top Nifty Bank gainer today: HDFC Bank shares jump 4% as index soars 2%— Should you buy or"
- BZ=F (Brent Crude Oil Last Day Finan) score 11.7 — "ANT - ANTHROPIC SHARES TURN POSITIVE, LAST UP 2% AT $83.50"
- META (Meta) score 9.4 — "COREWEAVE’S BANKS TO SELL $4.5 BILLION META-TIED LOAN NEXT WEEK"
- JIOFIN.BO (Jio Financial Services Limited) score 8.9 — "Jio Financial Services vs Reliance vs Jio Platforms shares: Which Mukesh Ambani's stock to"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.5 — "ANT - ANTHROPIC RISKS LOSING $1 TRILLION MARKET VALUATION JUST DAYS AFTER IPO Anthropic is"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 7.9 — "Bajaj Auto Share Price Highlights: Bajaj Auto Stock Price History"
- CRWV (CoreWeave, Inc.) score 7.4 — "CRWV - COREWEAVE BONDS PLUNGE AS 2031 YIELD SURGES TO 17.91% CoreWeave's debt is coming un"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 5.9 — "Climate Finance Dispute Derails COP31 Negotiations"
- GS (Goldman Sachs Group, Inc. (The) score 5.5 — "SPY $QQQ - GOLDMAN WARNS IT'S TOO EARLY TO BUY THE AI SELLOFF Goldman Sachs strategist Chr"
- MS (Morgan Stanley) score 5.1 — "CRWV - COREWEAVE BANKS PREPARE $4.5 BILLION LOAN SALE AS DEFAULT FEARS SURGE Morgan Stanle"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 4.7 — "Top stocks to watch today: Tata Steel, Lenskart, Adani Enterprises, PhysicsWallah, Hindalc"
- TATASTEEL.BO (TATA STEEL LTD.) score 3.6 — "Stocks to watch, November 26: LG Electronics, Tata Steel, SG Mart, APL Apollo Tubes, Fino "
- ETERNAL.NS (ETERNAL LIMITED) score 1.7 — "BSE, Eternal, Titan, SBI among 18 Nifty 50 stocks that rallied 10–43% in 2026; what's driv"
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 1.2 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 0.7 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "

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