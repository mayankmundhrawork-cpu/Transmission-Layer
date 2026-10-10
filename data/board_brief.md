# Transmission Layer — board brief · 2026-10-10 01:04Z

data as of **2026-10-10** · 97 series · 4 red / 38 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.704, 5d in regime; vol-pct 0.675, breadth-off 0.733, Markov P(high-vol) 0.015)
- [INVERTED] **safe_haven_gold** — corr20 -0.42, corr60 -0.41, contra nifty_50 corr20=0.28, last shift 2026-06-05. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.82, corr60 0.84, last shift 2026-02-05. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.24, corr60 0.22, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.07, corr60 0.13, last shift 2026-08-20. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.75, corr60 -0.77, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [INVERTED] **dxy_inr_channel** — corr20 -0.27, corr60 -0.11, last shift 2026-08-13. Channel: broad dollar strength -> EM FX weakness incl INR
- [VALID] **real_rates_gold_inverse** — corr20 -0.29, corr60 -0.29, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.66, corr60 0.17, last shift 2026-07-28. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 2.044269036804991e-05)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.495** (n=1143) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.826** (n=2110) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.31] usd_inr ↑
- usd_inr [FX]: last 96.78, z20 2.31, zc 0.05, resid-z -0.10 [quiet], 1d 0.02%, 20d range extreme; |z20|=2.31; 1y-pct=99
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.411 via usd_inr, z -0.57, quiet); dyn_karurvysya_ns (rho -0.361 via usd_inr, z 2.87, reacted)
- **India receivers**: dyn_idbi_ns (rho -0.411, z -0.57); dyn_karurvysya_ns (rho -0.361, z 2.87)
- Source: Rupee recovers to 96.73 vs US dollar after RBI intervention, but dollar demand persists — ET Markets, 2026-10-09. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-recovers-to-96-73-vs-us-dollar-after-rbi-intervention-but-dollar-demand-persists/articleshow/134838115.cms
- Source: Rupee rises 16 paise to close at 96.72 against US dollar — BusinessLine Mkts, 2026-10-09. https://www.thehindubusinessline.com/markets/forex/rupee-rises-16-paise-to-close-at-9672-against-us-dollar/article71563647.ece
- Source: Rupee posts weekly fall despite rate hike amid adverse flows, weak sentiment — ET Markets, 2026-10-09. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-posts-weekly-fall-despite-rate-hike-amid-adverse-flows-weak-sentiment/articleshow/134831035.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 5.41] commodities · 2 series ↓
- corn [COMMODITIES]: last 480.50, z20 -2.58, zc -2.70, resid-z -2.46 [unexplained], 1d -3.95%, |z20|=2.58
- wheat [COMMODITIES]: last 670.75, z20 -1.95, zc -0.98, resid-z -0.96 [quiet], 1d -1.83%, |z20|=1.95
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: soybeans (co-move) — not yet - watch; rho 0.642 vs corn
- Source: CME feeder cattle hit 3-month peak after corn price plunge — Mint Markets, 2026-10-09. https://www.livemint.com/market/cme-feeder-cattle-hit-3-month-peak-after-corn-price-plunge-11791582473869.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-04-01 (d=0.35), 2025-08-28 (d=0.36)

### [RED 5.06] usd_cny ↓
- usd_cny [FX]: last 6.68, z20 -5.06, zc -2.98, resid-z -4.27 [unexplained], 1d -0.32%, |z20|=5.06; 1y-pct=0
- **Mechanism**: usd_cny ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-09-25 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indianb_ns (rho -0.388 via usd_cny, z 0.25, quiet); nifty_50 (rho -0.372 via usd_cny, z -1.3, reacted); dyn_muthootfin_ns (rho -0.367 via usd_cny, z -1.77, reacted); nifty_midcap_100 (rho -0.354 via usd_cny, z -1.38, reacted)
- **India receivers**: dyn_indianb_ns (rho -0.388, z 0.25); nifty_50 (rho -0.372, z -1.3); dyn_muthootfin_ns (rho -0.367, z -1.77); nifty_midcap_100 (rho -0.354, z -1.38)
- Historical analogues: 2026-09-25 (d=0.0), 2025-08-22 (d=0.01), 2026-05-05 (d=0.01)

### [AMBER 4.94] cross-asset · 3 series ↑
- sp500 [INDICES]: last 7811.09, z20 1.62, zc 0.83, resid-z -1.45 [quiet], 1d 0.59%, |z20|=1.62; 1y-pct=99
- nasdaq_100 [INDICES]: last 30881.86, z20 0.91, zc 0.47, resid-z -0.78 [quiet], 1d 0.51%, 1y-pct=98
- dyn_nvda [EQUITIES]: last 229.32, z20 0.39, zc -0.24, resid-z -1.26 [quiet], 1d -0.50%, 1y-pct=96
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.952 vs sp500
- Watch next: vix (inverse) — not yet - watch; rho -0.724 vs sp500, historically leads by 4d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.887 vs sp500
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.86 vs sp500
- Watch next: brent (inverse) — not yet - watch; rho -0.629 vs sp500, historically leads by 2d
- Source: As AT&T, Verizon and T-Mobile shares fall, Wall Street assesses the growing SpaceX threat — MarketWatch Top, 2026-10-09. https://www.marketwatch.com/story/as-at-t-verizon-and-t-mobile-shares-fall-wall-street-assesses-the-growing-spacex-threat-e869ef9e?mod=mw_rss_topstories
- Source: NVDA - UBS REAFFIRMS NVIDIA BUY RATING WITH $300 PRICE TARGET UBS reiterated its Buy rating on Nvidia, maintaining a $300 price target following strong Taiwanese export data. Taiwan's computing equipment exports surged 25.9% month-over-month to $29.8 billion in September, significantly exceeding nor — DeItaone, 2026-10-09. https://t.me/walter_bloomberg/36877
- Source: S&P 500 BULL MARKET GAINS 117% AS AI RALLY RAISES CONCENTRATION RISKS The S&P 500 has surged 117% since October 2022, adding nearly $40 trillion in market value, largely driven by AI-related stocks. However, the equal-weight S&P 500 has underperformed by a record 52 percentage points, highlighting t — DeItaone, 2026-10-09. https://t.me/walter_bloomberg/36876
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-04 (d=0.18), 2025-08-28 (d=0.22)

### [AMBER 4.62] cross-asset · 4 series ↑
- ust_30y [RATES]: last 5.60, z20 0.95, zc -1.60, resid-z -2.34 [unexplained], 1d -1.23%, 1y-pct=97
- dyn_bond [EQUITIES]: last 86.93, z20 -0.86, zc 0.03, resid-z 0.58 [quiet], 1d 0.01%, 1y-pct=2
- tips_10y_real [RATES]: last 2.87, z20 0.73, zc -0.90, resid-z -1.52 [unexplained], 1d -1.71%, 1y-pct=96
- ust_10y [RATES]: last 5.22, z20 0.72, zc -1.11, resid-z -1.95 [unexplained], 1d -1.14%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.646 vs ust_30y, historically leads by 3d
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.559 vs ust_30y, historically leads by 1d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.585 vs dyn_bond
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.535 vs ust_30y
- Source: RBI OMO sale fears spur bond sell-off; 10-year G-Sec hits three year high — BusinessLine Mkts, 2026-10-09. https://www.thehindubusinessline.com/markets/rbi-omo-sale-fears-spur-bond-sell-off-10-year-g-sec-hits-three-year-high/article71564483.ece
- Source: US 10-year Treasury yield could hit 6% as oil prices, debt worries mount: Pimco CIO — ET Markets, 2026-10-09. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-10-year-treasury-yield-could-hit-6-as-oil-prices-debt-worries-mount-pimco-cio/articleshow/134825801.cms
- Source: US bank earnings in focus as Treasury yields surge, raising concerns over lending and dealmaking — ET Markets, 2026-10-09. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-bank-earnings-in-focus-as-treasury-yields-surge-raising-concerns-over-lending-and-dealmaking/articleshow/134806882.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

### [AMBER 4.47] dyn_adanient_bo ↓
- dyn_adanient_bo [EQUITIES]: last 2633.10, z20 -2.47, zc 0.43, resid-z -0.20 [quiet], 1d 1.47%, |z20|=2.47
- **Mechanism**: dyn_adanient_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.556 via dyn_adanient_bo, z -2.34, reacted); nifty_50 (rho 0.383 via dyn_adanient_bo, z -1.3, reacted); nifty_midcap_100 (rho 0.373 via dyn_adanient_bo, z -1.38, reacted)
- **India receivers**: nifty_metal (rho 0.556, z -2.34); nifty_50 (rho 0.383, z -1.3); nifty_midcap_100 (rho 0.373, z -1.38)
- Source: Broker’s call: Adani Power (Accumulate) — BusinessLine Mkts, 2026-10-09. https://www.thehindubusinessline.com/markets/brokers-call-adani-power-accumulate/article71564351.ece
- Source: Adani Power shares: GQG Partners-managed entities cut stake to 5.72% from 5.74% — ET Markets, 2026-10-09. https://economictimes.indiatimes.com/markets/stocks/news/adani-power-shares-gqg-partners-managed-entities-cut-stake-to-5-72-from-5-74/articleshow/134834452.cms
- Source: Adani Power shares rise despite US-based FPI GQG Partners trimming stake in Gautam Adani-led company — Mint Markets, 2026-10-09. https://www.livemint.com/market/stock-market-news/adani-power-shares-rise-despite-us-based-fpi-gqg-partners-trimming-stake-in-gautam-adani-led-company-11791542076904.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [AMBER 4.13] indices · 2 series ↓
- nifty_50 [INDICES]: last 22520.45, z20 -1.30, zc 1.54, resid-z 2.21 [unexplained], 1d 1.30%, 1y-pct=2
- nifty_fmcg [INDICES]: last 44864.80, z20 -0.48, zc 2.25, resid-z 1.61 [unexplained], 1d 2.20%, 1y-pct=3
- **Mechanism**: indices · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-18 (z-distance 0.29).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.782 via nifty_50, z -1.38, reacted); dyn_jiofin_bo (rho 0.61 via nifty_50, z -1.25, reacted); nifty_metal (rho 0.583 via nifty_50, z -2.34, reacted); dyn_policybzr_ns (rho 0.521 via nifty_50, z -1.02, reacted); dyn_justdial_bo (rho 0.52 via nifty_50, z -1.42, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.782, z -1.38); dyn_jiofin_bo (rho 0.61, z -1.25); nifty_metal (rho 0.583, z -2.34); dyn_policybzr_ns (rho 0.521, z -1.02)
- Source: TCS rally pulls Dalal Street out of its 8-week rut — BusinessLine Mkts, 2026-10-09. https://www.thehindubusinessline.com/markets/tcs-lifts-dalal-street-out-of-its-eight-week-rut/article71563965.ece
- Source: Relief rally in Indian stock market; biggest weekly losing streak in 25 years snapped: What's next for Sensex, Nifty? — Mint Markets, 2026-10-09. https://www.livemint.com/market/stock-market-news/relief-rally-in-indian-stock-market-biggest-weekly-losing-streak-in-25-years-snapped-whats-next-for-sensex-nifty-11791550093630.html
- Source: Navratri 2025 to Navratri 2026: Nifty's performance - Top gainers, losers, outlook — Mint Markets, 2026-10-09. https://www.livemint.com/market/stock-market-news/navratri-2025-to-navratri-2026-niftys-performance-top-gainers-losers-outlook-11791549174535.html
- Historical analogues: 2025-07-18 (d=0.29), 2025-08-01 (d=0.88), 2025-07-11 (d=1.11)

### [AMBER 3.88] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 6580.00, z20 1.88, zc -0.07, resid-z 2.45 [unexplained], 1d -0.45%, 1y-pct=99
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: South India set to play a key role in India’s next phase of steel growth: Experts — BusinessLine Mkts, 2026-10-09. https://www.thehindubusinessline.com/markets/commodities/south-india-set-to-play-a-key-role-in-indias-next-phase-of-steel-growth-experts/article71563711.ece
- Source: Experts say it's time to look at mid-caps, suggest looking at mid-cap funds through the SIP route — Mint Markets, 2026-10-09. https://www.livemint.com/market/stock-market-news/experts-say-its-time-to-look-at-mid-caps-suggest-looking-at-mid-cap-funds-through-the-sip-route-11791544855519.html
- Source: BEL shares down 16% in 6 months - Is a trend reversal in this multibagger defence stock on the cards? Experts decode — Mint Markets, 2026-10-09. https://www.livemint.com/market/stock-market-news/bel-shares-down-16-in-6-months-is-a-trend-reversal-in-this-multibagger-defence-stock-on-the-cards-experts-decode-11791540651920.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

## Watchlist (below surfacing floor)
shanghai_comp ↓ (3.87), gold_silver_ratio ↑ (3.81), dyn_muthootfin_ns ↓ (3.77), eur_usd ↓ (3.59), natgas ↑ (3.52), dyn_rs ↑ (3.5), comex_copper ↑ (3.32), dyn_jiofin_bo ↓ (3.25), dyn_policybzr_ns ↓ (3.02), dyn_hdb ↓ (2.98), dyn_karurvysya_ns ↑ (2.87), indices · 2 series ↓ (2.46)

## India macro
- nifty_50: 22520.4492 (1d 1.30%, z20 -1.30, flag amber)
- nifty_midcap_100: 58780.8984 (1d 1.56%, z20 -1.38, flag none)
- usd_inr: 96.7800 (1d 0.02%, z20 2.31, flag red)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6101 (1d 0.25%, z20 -1.46, flag none)
- Next India prints: India CPI T-2d · NSDL FPI flows T-2d · IMD weekly rainfall T-2d · India WPI T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 84.2 — "De Beers to open 100 Forevermark stores in India by 2030"
- COALINDIA.NS (COAL INDIA LTD) score 83.4 — "De Beers to open 100 Forevermark stores in India by 2030"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 81.9 — "De Beers to open 100 Forevermark stores in India by 2030"
- INDIANB.NS (INDIAN BANK) score 80.7 — "Gold, silver boom puts US bank trading revenues on track for record $5 billion"
- BAC (Bank of America Corporation) score 72.9 — "Trump on Truth Social: 'Diesel Prices for Americans and, Indeed, the World, Will Be COMING"
- HDB (HDFC Bank Limited) score 64.7 — "Gold, silver boom puts US bank trading revenues on track for record $5 billion"
- IDBI.NS (IDBI BANK LIMITED) score 62.4 — "Gold, silver boom puts US bank trading revenues on track for record $5 billion"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 62.4 — "Gold, silver boom puts US bank trading revenues on track for record $5 billion"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 62.4 — "Gold, silver boom puts US bank trading revenues on track for record $5 billion"
- COIN (Coinbase Global, Inc.) score 59.6 — "TRUMP ANNOUNCES DEAL WITH PUTIN FOR RUSSIAN DIESEL SUPPLIES President Trump says he held a"
- OHI (Omega Healthcare Investors, In) score 45.0 — "Share price down 29% in 2026, retail investors’ favourite wind energy stock under pressure"
- TECHM.NS (TECH MAHINDRA LIMITED) score 42.9 — "Anthem Biosciences block deal: Portsmouth Technologies sells 30 lakh shares worth Rs 250 c"
- BOND (PIMCO Active Bond Exchange-Tra) score 41.3 — "Reissued bonds account for nearly 66% of state borrowings in H1 FY27: Report"
- TGT (Target Corporation) score 38.0 — "NVDA - UBS REAFFIRMS NVIDIA BUY RATING WITH $300 PRICE TARGET UBS reiterated its Buy ratin"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 37.8 — "Anthem Biosciences block deal: Portsmouth Technologies sells 30 lakh shares worth Rs 250 c"
- TECH (Bio-Techne Corp) score 37.8 — "Anthem Biosciences block deal: Portsmouth Technologies sells 30 lakh shares worth Rs 250 c"
- CHKP (Check Point Software Technolog) score 35.0 — "‘I feel like a loser’: I check my ETFs every day. They’re up one minute, down the next. Sh"
- LTH (Life Time Group Holdings, Inc.) score 31.1 — "U.S. CONSUMER SENTIMENT FALLS AS INFLATION EXPECTATIONS RISE University of Michigan consum"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 27.2 — "PUTIN'S ENVOY DMITRIEV ON X: RUSSIA-US COOPERATION ON DIESEL AND ENERGY WILL BENEFIT THE W"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 26.7 — "Experts say it's time to look at mid-caps, suggest looking at mid-cap funds through the SI"
- SEPN (Septerna, Inc.) score 25.9 — "NVDA - UBS REAFFIRMS NVIDIA BUY RATING WITH $300 PRICE TARGET UBS reiterated its Buy ratin"
- 301077.SZ (CHINASTARS) score 18.8 — "EU AND CHINA REACH RARE EARTHS DEAL AS TRADE PRESSURE MOUNTS EU Trade Commissioner Maroš Š"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 16.4 — "Adani Power shares: GQG Partners-managed entities cut stake to 5.72% from 5.74%"
- JIOFIN.BO (Jio Financial Services Limited) score 15.7 — "Anand Rathi Wealth Q2 results 2026: Dividend declared; check amount, record date, net prof"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 12.9 — "ET Alpha Wealth Summit 2.0 | SIFs, passive funds and GIFT City: How India's wealth portfol"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 12.9 — "ET Alpha Wealth Summit 2.0 | SIFs, passive funds and GIFT City: How India's wealth portfol"
- JUSTDIAL.BO (JUST DIAL LTD.) score 12.4 — "Madhusudan Kela-backed MV Electrosystems shares more than double from IPO price in just 2 "
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 11.6 — "Micro, trading MSMEs need targeted support: Equitas Small Finance Bank MD"
- BZ=F (Brent Crude Oil Last Day Finan) score 11.1 — "₹5 dividend vs  ₹34 last year: Why Vedanta's dividend payout story has fundamentally chang"
- JEF (Jefferies Financial Group Inc.) score 10.9 — "Kalyan Jewellers shares shine: 55% up in 3 months, Jefferies India sees further 46% upside"
- VT (Vanguard Total World Stock Ind) score 9.1 — "Trump on Truth Social: 'Diesel Prices for Americans and, Indeed, the World, Will Be COMING"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 9.0 — "Micro, trading MSMEs need targeted support: Equitas Small Finance Bank MD"
- NVDA (NVIDIA Corporation) score 8.7 — "NVDA - UBS REAFFIRMS NVIDIA BUY RATING WITH $300 PRICE TARGET UBS reiterated its Buy ratin"
- META (Meta) score 8.1 — "Monetary tightening likely to keep industrial metal prices on leash"
- RS (Reliance, Inc.) score 7.2 — "Reliance Jio IPO price band alert: Mukesh Ambani's telecom giant likely to set band at  ₹1"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 5.3 — "Share price down 29% in 2026, retail investors’ favourite wind energy stock under pressure"
- GS (Goldman Sachs Group, Inc. (The) score 4.6 — "TCS shares jump 4% after Q2 results. What are Goldman Sachs, Nomura, others saying?"
- POLICYBZR.NS (PB FINTECH LIMITED) score 4.0 — "Nomura becomes latest brokerage to cut PB Fintech share price target by 31%, lists 2 scena"
- DELL (Dell Technologies Inc.) score 0.7 — "Piero Cipollone: Interview with Corriere della Sera"
- VOLTAS.NS (VOLTAS LTD) score 0.1 — "Voltas’s market share is growing. Will margins follow?"

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