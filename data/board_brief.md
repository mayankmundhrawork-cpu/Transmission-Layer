# Transmission Layer — board brief · 2026-10-07 18:55Z

data as of **2026-10-07** · 97 series · 9 red / 36 amber · 8 events surfaced (30 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.639, 3d in regime; vol-pct 0.654, breadth-off 0.625, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.39, corr60 -0.42, contra nifty_50 corr20=0.1, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.81, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.06, corr60 0.15, last shift 2026-07-09. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.04, corr60 0.11, last shift 2026-08-24. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.77, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.17, corr60 -0.07, last shift 2026-08-17. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.3, corr60 -0.24, last shift 2026-08-17. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.52, corr60 0.19, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** stoxx_50 → asx_200: leads 1d (ccf 0.258, β 0.1965, p 0.00873); driver zc -1.7 → expected -0.31%. Type hit-rate 0.823 (n=2182).
- **SETUP** dax → asx_200: leads 1d (ccf 0.255, β 0.1858, p 0.00565); driver zc -1.5 → expected -0.263%. Type hit-rate 0.823 (n=2182).
- **SETUP** dax → usd_mxn: leads 1d (ccf -0.252, β -0.1399, p 0.00208); driver zc -1.5 → expected 0.198%. Type hit-rate 0.823 (n=2182).
- **SETUP** stoxx_50 → usd_mxn: leads 1d (ccf -0.252, β -0.1468, p 0.00308); driver zc -1.7 → expected 0.231%. Type hit-rate 0.823 (n=2182).
- Track record · residual_reversion: hit-rate **0.496** (n=1133) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.823** (n=2182) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.35] usd_inr ↑
- usd_inr [FX]: last 96.76, z20 2.35, zc 0.83, resid-z 0.92 [quiet], 1d 0.44%, 20d range extreme; |z20|=2.35; 1y-pct=99
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.407 via usd_inr, z 1.21, reacted); dyn_karurvysya_ns (rho -0.355 via usd_inr, z 0.42, quiet)
- **India receivers**: dyn_idbi_ns (rho -0.407, z 1.21); dyn_karurvysya_ns (rho -0.355, z 0.42)
- Source: Rupee slides to a five-month low of 96.7/$, yields rise — BusinessLine Mkts, 2026-10-07. https://www.thehindubusinessline.com/markets/rupee-slides-to-a-five-month-low-of-967-yields-rise/article71556132.ece
- Source: RBI says it will ensure 'undervalued' Rupee finds its correct level — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/forex/forex-news/rbi-says-it-will-ensure-undervalued-rupee-finds-its-correct-level/articleshow/134770024.cms
- Source: Rupee tumbles 43 paise to close at 96.78 against US dollar following RBI policy decision — BusinessLine Mkts, 2026-10-07. https://www.thehindubusinessline.com/markets/forex/rupee-tumbles-43-paise-to-close-at-9678-against-us-dollar-following-rbi-policy-decision/article71555232.ece
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2025-09-16 (d=0.01)

### [AMBER 5.87] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.66, z20 1.94, zc 0.44, resid-z 0.65 [quiet], 1d 0.53%, |z20|=1.94; 1y-pct=100
- ust_10y [RATES]: last 5.31, z20 1.66, zc 0.72, resid-z 1.07 [quiet], 1d 0.57%, |z20|=1.66; 1y-pct=100
- tips_10y_real [RATES]: last 2.95, z20 1.57, zc 0.69, resid-z 1.03 [quiet], 1d 1.03%, |z20|=1.57; 1y-pct=100
- dyn_bond [EQUITIES]: last 86.64, z20 -1.35, zc -0.02, resid-z -0.41 [quiet], 1d -0.01%, 1y-pct=1
- ust_2y [RATES]: last 4.84, z20 0.82, zc 0.78, resid-z 1.10 [quiet], 1d 0.21%, 1y-pct=98
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.534 vs ust_30y
- Source: Gold prices drop over 2%, slide to 2-month low as Treasury yields, US dollar climb — Mint Markets, 2026-10-07. https://www.livemint.com/market/stock-market-news/gold-prices-drop-over-2-slide-to-2-month-low-as-treasury-yields-us-dollar-climb-11791396712994.html
- Source: Foreign investors pull out $26.3 billion from emerging markets in September as hawkish Fed pushes US Treasury yields higher — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/foreign-investors-pull-out-26-3-billion-from-emerging-markets-in-september-as-hawkish-fed-pushes-us-treasury-yields-higher/articleshow/134772977.cms
- Source: US bond selloff resumes as 10- and 30-year yields hit fresh 24-year highs — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/us-stocks/news/us-bonds-selloff-resumes-as-10-year-30-yields-hit-new-24-year-high/articleshow/134771853.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.47] dyn_ohi ↓
- dyn_ohi [EQUITIES]: last 44.03, z20 -3.47, zc -1.24, resid-z 1.04 [quiet], 1d -1.65%, |z20|=3.47
- **Mechanism**: dyn_ohi ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Foreign investors pull out $26.3 billion from emerging markets in September as hawkish Fed pushes US Treasury yields higher — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/foreign-investors-pull-out-26-3-billion-from-emerging-markets-in-september-as-hawkish-fed-pushes-us-treasury-yields-higher/articleshow/134772977.cms
- Source: Top stocks in focus today: Investors must watch Tata Power, Senco Gold, Dixon Tech shares on Thu, 8 Oct | Triggers — Mint Markets, 2026-10-07. https://www.livemint.com/market/stock-market-news/top-stocks-in-focus-tomorrow-investors-must-watch-tata-power-senco-gold-dixon-tech-shares-on-thu-8-oct-triggers-11791383936715.html
- Source: NSE cautions investors over pricey overseas ETFs as demand surges — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/stocks/news/nse-cautions-investors-over-pricey-overseas-etfs-as-demand-surges/articleshow/134767663.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2025-04-02 (d=0.09)

### [AMBER 5.12] cross-asset · 3 series ↑
- sp500 [INDICES]: last 7802.77, z20 1.80, zc -0.28, resid-z 0.67 [quiet], 1d -0.21%, |z20|=1.80; 1y-pct=99
- dyn_nvda [EQUITIES]: last 236.76, z20 1.55, zc -0.53, resid-z -0.19 [quiet], 1d -1.04%, 1y-pct=99
- nasdaq_100 [INDICES]: last 31134.18, z20 1.48, zc -0.28, resid-z -0.27 [quiet], 1d -0.29%, 1y-pct=99
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_justdial_bo (rho -0.406 via dyn_nvda, z -1.05, reacted)
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.953 vs sp500
- Watch next: vix (inverse) — not yet - watch; rho -0.742 vs sp500, historically leads by 4d
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.556 vs nasdaq_100
- **India receivers**: dyn_justdial_bo (rho -0.406, z -1.05)
- Source: SpaceX may chase ‘stunning’ AI returns by taking on a lot of debt to buy Nvidia chips — MarketWatch Top, 2026-10-07. https://www.marketwatch.com/story/spacex-reportedly-is-looking-to-raise-as-much-money-as-the-company-generates-in-revenue-to-buy-nvidia-chips-01ca6d82?mod=mw_rss_topstories
- Source: Washington and Wall Street chose to delay paying their bills — and to put them on your tab — MarketWatch Top, 2026-10-07. https://www.marketwatch.com/story/washington-and-wall-street-chose-to-delay-paying-their-bills-and-to-put-them-on-your-tab-2eba83aa?mod=mw_rss_topstories
- Source: US stocks: S&P 500, Nasdaq retreat from records as oil and Treasury yields rebound — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-sp-500-nasdaq-retreat-from-records-as-oil-and-treasury-yields-rebound/articleshow/134767913.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-04 (d=0.18), 2025-08-28 (d=0.22)

### [AMBER 4.92] indices · 2 series ↑
- nikkei_225 [INDICES]: last 70163.27, z20 2.09, zc -0.44, resid-z -0.45 [quiet], 1d -0.74%, |z20|=2.09; 1y-pct=97
- taiwan_weighted [INDICES]: last 49710.92, z20 1.97, zc -0.23, resid-z -0.35 [quiet], 1d -0.22%, |z20|=1.97; 1y-pct=99
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.7).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho 0.546 via taiwan_weighted, z -1.16, reacted); nifty_it (rho -0.367 via taiwan_weighted, z -1.45, reacted)
- Watch next: kospi (co-move) — not yet - watch; rho 0.844 vs nikkei_225
- **India receivers**: dyn_bajfinance_ns (rho 0.546, z -1.16); nifty_it (rho -0.367, z -1.45)
- Source: Stock market outlook today, 6 Oct: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Nikkei, Taiwan cues — Mint Markets, 2026-10-06. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-6-oct-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-nikkei-taiwan-cues-11791247193944.html
- Historical analogues: 2025-12-30 (d=0.7), 2025-07-11 (d=0.77), 2026-06-09 (d=1.0)

### [RED 4.66] dyn_techm_ns ↓
- dyn_techm_ns [EQUITIES]: last 1491.10, z20 -2.66, zc -0.58, resid-z -0.31 [quiet], 1d -0.89%, |z20|=2.66
- **Mechanism**: dyn_techm_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.838 via dyn_techm_ns, z -1.45, reacted); dyn_tataelxsi_ns (rho 0.467 via dyn_techm_ns, z -1.4, reacted); dyn_justdial_bo (rho 0.453 via dyn_techm_ns, z -1.05, reacted); dyn_tatatech_ns (rho 0.397 via dyn_techm_ns, z -1.01, reacted)
- **India receivers**: nifty_it (rho 0.838, z -1.45); dyn_tataelxsi_ns (rho 0.467, z -1.4); dyn_justdial_bo (rho 0.453, z -1.05); dyn_tatatech_ns (rho 0.397, z -1.01)
- Source: Market Trading Guide: Kotak Mahindra Bank among 5 stock recommendations for Thursday — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/stocks/news/market-trading-guide-kotak-mahindra-bank-among-5-stock-recommendations-for-thursday/slideshow/134769639.cms
- Source: Kotak Mahindra Bank shares rise 2% as HSBC upgrades stock to buy — BusinessLine Mkts, 2026-10-07. https://www.thehindubusinessline.com/markets/kotak-mahindra-bank-shares-rise-2-as-hsbc-upgrades-stock-to-buy/article71554661.ece
- Source: PNB, Kotak Mahindra Bank, other bank stocks rise up to 2% after RBI’s rate hike, Nifty Bank above 55,500 — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/stocks/news/pnb-kotak-mahindra-bank-other-bank-stocks-rise-up-to-2-after-rbis-rate-hike-nifty-bank-above-55500/articleshow/134757463.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-11 (d=0.03), 2025-02-10 (d=0.09)

### [RED 4.64] dyn_adanient_bo ↓
- dyn_adanient_bo [EQUITIES]: last 2744.00, z20 -2.64, zc -1.67, resid-z -1.95 [unexplained], 1d -3.72%, |z20|=2.64
- **Mechanism**: dyn_adanient_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.452 via dyn_adanient_bo, z -2.49, reacted)
- **India receivers**: nifty_metal (rho 0.452, z -2.49)
- Source: Adani Enterprises: AEL gets highest-ever rating in its credit history; shares up over 22% YTD — Mint Markets, 2026-10-07. https://www.livemint.com/market/stock-market-news/adani-enterprises-ael-gets-highest-ever-rating-in-its-credit-history-shares-up-over-21-ytd-11791392672814.html
- Source: Adani Enterprises gets rating upgrade from CARE Ratings to AA; Stable; shares up 21% in 2026 — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/stocks/news/adani-enterprises-gets-rating-upgrade-from-care-ratings-to-aa-stable-shares-up-21-in-2026/articleshow/134768104.cms
- Source: Market wrap: Kotak Bank, Bharti Airtel, Titan Company, Adani Ent top gainers and losers on Nifty and Sensex on Wednesday — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-kotak-bank-bharti-airtel-titan-company-adani-ent-top-gainers-and-losers-on-nifty-and-sensex-on-wednesday/articleshow/134765160.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [RED 4.54] dxy ↑
- dxy [FX]: last 102.23, z20 1.54, zc 1.14, resid-z -0.40 [quiet], 1d 0.40%, 20d range extreme; |z20|=1.54; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-21 (d=0.02), 2025-10-10 (d=0.03)

## Watchlist (below surfacing floor)
indices · 4 series ↓ (4.37), indices · 2 series ↓ (4.29), dyn_tgt ↓ (4.08), eur_usd ↓ (3.9), natgas ↑ (3.89), gold_silver_ratio ↑ (3.85), hang_seng ↓ (3.71), comex_gold ↓ (3.67), dyn_jiofin_bo ↓ (3.3), dyn_policybzr_ns ↓ (3.17), dyn_hdb ↓ (3.16), dyn_4417_t ↑ (3.05)

## India macro
- nifty_50: 22603.0508 (1d -0.76%, z20 -1.46, flag amber)
- nifty_midcap_100: 59376.8516 (1d -0.64%, z20 -1.33, flag none)
- usd_inr: 96.7650 (1d 0.44%, z20 2.35, flag red)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6269 (1d 0.12%, z20 -0.80, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI MPC decision T-0d · AMFI SIP / MF flows T-1d · RBI Weekly Statistical Supplement T-2d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 92.4 — "U.S. 30-YEAR YIELD HITS NEW 24-YEAR HIGH The 30-year Treasury yield climbed to 5.706%, its"
- COALINDIA.NS (COAL INDIA LTD) score 82.8 — "Saurabh Mukherjea’s Marcellus ties up with VanEck to widen global investment offerings for"
- INOXINDIA.NS (INOX INDIA LIMITED) score 82.7 — "Saurabh Mukherjea’s Marcellus ties up with VanEck to widen global investment offerings for"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 80.4 — "Saurabh Mukherjea’s Marcellus ties up with VanEck to widen global investment offerings for"
- BAC (Bank of America Corporation) score 78.9 — "U.S. 30-YEAR YIELD HITS NEW 24-YEAR HIGH The 30-year Treasury yield climbed to 5.706%, its"
- HDB (HDFC Bank Limited) score 74.6 — "U.S. 30-YEAR YIELD HITS NEW 24-YEAR HIGH The 30-year Treasury yield climbed to 5.706%, its"
- IDBI.NS (IDBI BANK LIMITED) score 71.9 — "U.S. 30-YEAR YIELD HITS NEW 24-YEAR HIGH The 30-year Treasury yield climbed to 5.706%, its"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 71.9 — "U.S. 30-YEAR YIELD HITS NEW 24-YEAR HIGH The 30-year Treasury yield climbed to 5.706%, its"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 71.9 — "U.S. 30-YEAR YIELD HITS NEW 24-YEAR HIGH The 30-year Treasury yield climbed to 5.706%, its"
- COIN (Coinbase Global, Inc.) score 54.5 — "U.S. 30-YEAR YIELD HITS NEW 24-YEAR HIGH The 30-year Treasury yield climbed to 5.706%, its"
- OHI (Omega Healthcare Investors, In) score 49.0 — "Saurabh Mukherjea’s Marcellus ties up with VanEck to widen global investment offerings for"
- BOND (PIMCO Active Bond Exchange-Tra) score 46.5 — "FRENCH 10-YEAR GOVERNMENT BOND YIELD NOW UP 15 BPS AT 4.8974%"
- TECHM.NS (TECH MAHINDRA LIMITED) score 44.8 — "Top stocks in focus today: Investors must watch Tata Power, Senco Gold, Dixon Tech shares "
- TGT (Target Corporation) score 38.4 — "SPCX - SUSQUEHANNA: RAISES TARGET PRICE TO $173 FROM $144"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 36.3 — "Top stocks in focus today: Investors must watch Tata Power, Senco Gold, Dixon Tech shares "
- TECH (Bio-Techne Corp) score 36.3 — "Top stocks in focus today: Investors must watch Tata Power, Senco Gold, Dixon Tech shares "
- CHKP (Check Point Software Technolog) score 33.8 — "Top 2 stocks to buy for short-term: Bank of Maharashtra, Usha Martin by Nagaraj Shetti - C"
- LTH (Life Time Group Holdings, Inc.) score 29.7 — "TCS Q2 results 2026: Expectations, date and time, dividend announcement schedule, quarterl"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 25.2 — "Mixed outlook for energy expenditures this winter"
- SEPN (Septerna, Inc.) score 23.4 — "Minutes of the Federal Open Market Committee, September 15-16, 2026"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 19.4 — "IDFC First Bank share: 30% rally in 6 months! Experts see more upside after Q2FY27 busines"
- 301077.SZ (CHINASTARS) score 19.3 — "CHINA COULD USE TRADE PROBE TOOLS AGAINST EU: CCTV"
- BZ=F (Brent Crude Oil Last Day Finan) score 14.7 — "Stock split, spin-off: Last chance to buy these stocks today - Check record date, share pe"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 12.6 — "Landmark Group raises Rs 330 crore SBI finance for Gurugram project"
- JUSTDIAL.BO (JUST DIAL LTD.) score 12.2 — "ITALY'S ECONOMY MINISTER: ITALY ASKS EU TO CONSIDER INFLATION AS A SIGNIFICANT FACTOR THAT"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.7 — "Top stocks in focus today: Investors must watch Tata Power, Senco Gold, Dixon Tech shares "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 11.7 — "Top stocks in focus today: Investors must watch Tata Power, Senco Gold, Dixon Tech shares "
- JIOFIN.BO (Jio Financial Services Limited) score 11.1 — "JM Financial, ICICI Securities top IPO deals in H1FY27"
- JEF (Jefferies Financial Group Inc.) score 10.7 — "Margin boost: Jefferies picks 3 bank stocks to gain the most from RBI rate hikes"
- VT (Vanguard Total World Stock Ind) score 9.6 — "KREMLIN: MOST OF WHAT THE MEDIA ARE REPORTING ABOUT SIBERIAN PLAGUE LAB INCIDENT IS FALSE "
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 9.4 — "Landmark Group raises Rs 330 crore SBI finance for Gurugram project"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.3 — "Sensex today | Stock Market Highlights: Sensex closes 429 pts, Nifty slips 0.76% as RBI ra"
- META (Meta) score 8.5 — "26% returns in 2026! UBS retains 'Buy' rating on this metal stock | Target, upside and rat"
- NVDA (NVIDIA Corporation) score 7.9 — "SpaceX may chase ‘stunning’ AI returns by taking on a lot of debt to buy Nvidia chips"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 6.0 — "Trent’s Rs 1.80 lakh crore rout from peak: Has Q2 just flipped the script for Tata group’s"
- RS (Reliance, Inc.) score 5.2 — "Jefferies increases weight in Reliance, 2 others; trims weight in 3 stocks in latest model"
- POLICYBZR.NS (PB FINTECH LIMITED) score 5.2 — "Pine Labs, CAMS, Moneyview, other fintech stocks rally up to 11% after RBI MPC move. Here’"
- GS (Goldman Sachs Group, Inc. (The) score 5.1 — "TSLA - GOLDMAN: TESLA’S AI STORY MATTERS MORE THAN Q3 EARNINGS Goldman Sachs reiterated it"
- VOLTAS.NS (VOLTAS LTD) score 0.1 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 0.1 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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