# Transmission Layer — board brief · 2026-10-08 00:11Z

data as of **2026-10-08** · 97 series · 10 red / 36 amber · 8 events surfaced (33 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.639, 3d in regime; vol-pct 0.654, breadth-off 0.625, Markov P(high-vol) 0.014)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.42, contra nifty_50 corr20=0.1, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.81, corr60 0.85, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.07, corr60 0.15, last shift 2026-07-10. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.04, corr60 0.11, last shift 2026-08-25. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.77, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [INVERTED] **dxy_inr_channel** — corr20 -0.28, corr60 -0.1, last shift 2026-08-11. Channel: broad dollar strength -> EM FX weakness incl INR
- [VALID] **real_rates_gold_inverse** — corr20 -0.33, corr60 -0.27, last shift 2026-08-11. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.52, corr60 0.19, last shift 2026-07-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** dax → usd_mxn: leads 1d (ccf -0.252, β -0.1392, p 0.00209); driver zc -1.5 → expected 0.197%. Type hit-rate 0.828 (n=2136).
- **SETUP** stoxx_50 → usd_mxn: leads 1d (ccf -0.251, β -0.1459, p 0.0031); driver zc -1.7 → expected 0.23%. Type hit-rate 0.828 (n=2136).
- Track record · residual_reversion: hit-rate **0.496** (n=1134) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.828** (n=2136) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.19] usd_inr ↑
- usd_inr [FX]: last 96.66, z20 2.19, zc 0.57, resid-z 0.06 [quiet], 1d 0.30%, 20d range extreme; |z20|=2.19; 1y-pct=99
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.406 via usd_inr, z 1.21, reacted); dyn_karurvysya_ns (rho -0.383 via usd_inr, z 0.42, quiet)
- **India receivers**: dyn_idbi_ns (rho -0.406, z 1.21); dyn_karurvysya_ns (rho -0.383, z 0.42)
- Source: Rupee slides to a five-month low of 96.7/$, yields rise — BusinessLine Mkts, 2026-10-07. https://www.thehindubusinessline.com/markets/rupee-slides-to-a-five-month-low-of-967-yields-rise/article71556132.ece
- Source: RBI says it will ensure 'undervalued' Rupee finds its correct level — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/forex/forex-news/rbi-says-it-will-ensure-undervalued-rupee-finds-its-correct-level/articleshow/134770024.cms
- Source: Rupee tumbles 43 paise to close at 96.78 against US dollar following RBI policy decision — BusinessLine Mkts, 2026-10-07. https://www.thehindubusinessline.com/markets/forex/rupee-tumbles-43-paise-to-close-at-9678-against-us-dollar-following-rbi-policy-decision/article71555232.ece
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2025-09-16 (d=0.01)

### [RED 5.87] dyn_ohi ↓
- dyn_ohi [EQUITIES]: last 43.75, z20 -3.87, zc -1.71, resid-z -1.07 [moved], 1d -2.28%, |z20|=3.87
- **Mechanism**: dyn_ohi ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Foreign investors pull out $26.3 billion from emerging markets in September as hawkish Fed pushes US Treasury yields higher — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/foreign-investors-pull-out-26-3-billion-from-emerging-markets-in-september-as-hawkish-fed-pushes-us-treasury-yields-higher/articleshow/134772977.cms
- Source: CAPITAL ECONOMICS: CENTRAL BANKS MAY HIKE LESS THAN MARKETS EXPECT Capital Economics says central banks are unlikely to raise rates as far as investors currently price over the next year. While elevated bond yields have tightened financial conditions, much of that tightening reflects expectations fo — DeItaone, 2026-10-07. https://t.me/walter_bloomberg/36799
- Source: Top stocks in focus today: Investors must watch Tata Power, Senco Gold, Dixon Tech shares on Thu, 8 Oct | Triggers — Mint Markets, 2026-10-07. https://www.livemint.com/market/stock-market-news/top-stocks-in-focus-tomorrow-investors-must-watch-tata-power-senco-gold-dixon-tech-shares-on-thu-8-oct-triggers-11791383936715.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2025-04-02 (d=0.09)

### [AMBER 5.49] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.64, z20 1.56, zc -0.44, resid-z -0.33 [quiet], 1d -0.35%, |z20|=1.56; 1y-pct=99
- dyn_bond [EQUITIES]: last 86.57, z20 -1.43, zc -0.25, resid-z 0.02 [quiet], 1d -0.09%, 1y-pct=1
- ust_10y [RATES]: last 5.27, z20 1.26, zc -0.72, resid-z -0.60 [quiet], 1d -0.75%, 1y-pct=98
- tips_10y_real [RATES]: last 2.91, z20 1.18, zc -0.69, resid-z -0.53 [quiet], 1d -1.36%, 1y-pct=98
- ust_2y [RATES]: last 4.79, z20 0.41, zc -0.77, resid-z -0.49 [quiet], 1d -1.03%, 1y-pct=96
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.535 vs ust_10y, historically leads by 4d
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.53 vs ust_30y
- Source: US stocks: US market ends lower, off record highs, as Treasury yields climb — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-us-market-ends-lower-off-record-highs-as-treasury-yields-climb/articleshow/134774342.cms
- Source: Wall Street ends lower, off record highs, as Treasury yields climb — Mint Markets, 2026-10-07. https://www.livemint.com/market/wall-street-ends-lower-off-record-highs-as-treasury-yields-climb-11791403312250.html
- Source: Gold prices drop over 2%, slide to 2-month low as Treasury yields, US dollar climb — Mint Markets, 2026-10-07. https://www.livemint.com/market/stock-market-news/gold-prices-drop-over-2-slide-to-2-month-low-as-treasury-yields-us-dollar-climb-11791396712994.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.36] dyn_tgt ↓
- dyn_tgt [EQUITIES]: last 150.92, z20 -3.36, zc -1.03, resid-z 0.04 [quiet], 1d -2.21%, |z20|=3.36
- **Mechanism**: dyn_tgt ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eth_usd (co-move) — not yet - watch; rho 0.531 vs dyn_tgt, historically leads by 5d
- Source: 26% returns in 2026! UBS retains 'Buy' rating on this metal stock | Target, upside and rationale — Mint Markets, 2026-10-07. https://www.livemint.com/market/stock-market-news/26-returns-in-2026-ubs-retains-buy-rating-on-this-metal-stock-target-upside-and-rationale-11791381587885.html
- Source: Best 3 stocks to buy: Balrampur Chini, Bluestone, Kotak Bank by Vaishali Parekh | Target, stop-loss, Nifty prediction — Mint Markets, 2026-10-07. https://www.livemint.com/market/stock-market-news/best-3-stocks-to-buy-balrampur-chini-bluestone-kotak-bank-by-vaishali-parekh-target-stop-loss-nifty-prediction-11791379340026.html
- Source: SPCX - SUSQUEHANNA: RAISES TARGET PRICE TO $173 FROM $144 — DeItaone, 2026-10-07. https://t.me/walter_bloomberg/36726
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.01), 2025-09-30 (d=0.01)

### [AMBER 4.92] indices · 2 series ↑
- nikkei_225 [INDICES]: last 70163.27, z20 2.09, zc -0.44, resid-z -0.51 [quiet], 1d -0.74%, |z20|=2.09; 1y-pct=97
- taiwan_weighted [INDICES]: last 49710.92, z20 1.97, zc -0.23, resid-z -0.45 [quiet], 1d -0.22%, |z20|=1.97; 1y-pct=99
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.7).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho 0.553 via taiwan_weighted, z -1.16, reacted); nifty_it (rho -0.359 via taiwan_weighted, z -1.45, reacted)
- Watch next: kospi (co-move) — not yet - watch; rho 0.847 vs nikkei_225
- **India receivers**: dyn_bajfinance_ns (rho 0.553, z -1.16); nifty_it (rho -0.359, z -1.45)
- Source: Stock market outlook today, 6 Oct: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Nikkei, Taiwan cues — Mint Markets, 2026-10-06. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-6-oct-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-nikkei-taiwan-cues-11791247193944.html
- Historical analogues: 2025-12-30 (d=0.7), 2025-07-11 (d=0.77), 2026-06-09 (d=1.0)

### [RED 4.66] dyn_techm_ns ↓
- dyn_techm_ns [EQUITIES]: last 1491.10, z20 -2.66, zc -0.58, resid-z -0.15 [quiet], 1d -0.89%, |z20|=2.66
- **Mechanism**: dyn_techm_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.837 via dyn_techm_ns, z -1.45, reacted); dyn_tataelxsi_ns (rho 0.46 via dyn_techm_ns, z -1.4, reacted); dyn_justdial_bo (rho 0.446 via dyn_techm_ns, z -1.05, reacted); dyn_tatatech_ns (rho 0.39 via dyn_techm_ns, z -1.01, reacted)
- **India receivers**: nifty_it (rho 0.837, z -1.45); dyn_tataelxsi_ns (rho 0.46, z -1.4); dyn_justdial_bo (rho 0.446, z -1.05); dyn_tatatech_ns (rho 0.39, z -1.01)
- Source: Market Trading Guide: Kotak Mahindra Bank among 5 stock recommendations for Thursday — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/stocks/news/market-trading-guide-kotak-mahindra-bank-among-5-stock-recommendations-for-thursday/slideshow/134769639.cms
- Source: Kotak Mahindra Bank shares rise 2% as HSBC upgrades stock to buy — BusinessLine Mkts, 2026-10-07. https://www.thehindubusinessline.com/markets/kotak-mahindra-bank-shares-rise-2-as-hsbc-upgrades-stock-to-buy/article71554661.ece
- Source: PNB, Kotak Mahindra Bank, other bank stocks rise up to 2% after RBI’s rate hike, Nifty Bank above 55,500 — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/stocks/news/pnb-kotak-mahindra-bank-other-bank-stocks-rise-up-to-2-after-rbis-rate-hike-nifty-bank-above-55500/articleshow/134757463.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-11 (d=0.03), 2025-02-10 (d=0.09)

### [RED 4.64] dyn_adanient_bo ↓
- dyn_adanient_bo [EQUITIES]: last 2744.00, z20 -2.64, zc -1.67, resid-z -1.86 [unexplained], 1d -3.72%, |z20|=2.64
- **Mechanism**: dyn_adanient_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.448 via dyn_adanient_bo, z -2.49, reacted)
- **India receivers**: nifty_metal (rho 0.448, z -2.49)
- Source: Adani Enterprises: AEL gets highest-ever rating in its credit history; shares up over 22% YTD — Mint Markets, 2026-10-07. https://www.livemint.com/market/stock-market-news/adani-enterprises-ael-gets-highest-ever-rating-in-its-credit-history-shares-up-over-21-ytd-11791392672814.html
- Source: Adani Enterprises gets rating upgrade from CARE Ratings to AA; Stable; shares up 21% in 2026 — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/stocks/news/adani-enterprises-gets-rating-upgrade-from-care-ratings-to-aa-stable-shares-up-21-in-2026/articleshow/134768104.cms
- Source: Market wrap: Kotak Bank, Bharti Airtel, Titan Company, Adani Ent top gainers and losers on Nifty and Sensex on Wednesday — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-kotak-bank-bharti-airtel-titan-company-adani-ent-top-gainers-and-losers-on-nifty-and-sensex-on-wednesday/articleshow/134765160.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [RED 4.61] dyn_sepn ↓
- dyn_sepn [EQUITIES]: last 35.96, z20 -2.61, zc 0.20, resid-z -1.53 [unexplained], 1d 0.81%, |z20|=2.61
- **Mechanism**: dyn_sepn ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho -0.353 via dyn_sepn, z -0.87, quiet)
- **India receivers**: nifty_fmcg (rho -0.353, z -0.87)
- Source: India's forex reserves fall for fourth week, down $50 bn from Sept peak at $734 bn — BusinessLine Mkts, 2026-10-07. https://www.thehindubusinessline.com/markets/forex/indias-forex-reserves-fall-for-fourth-week-down-50-bn-from-sep-peak-to-734-bn/article71554797.ece
- Source: IEX logs 10.4% growth in electricity trade volume to 12.2 billion units in Sept — BusinessLine Mkts, 2026-10-06. https://www.thehindubusinessline.com/economy/iex-logs-104-growth-in-electricity-trade-volume-to-122-billion-units-in-sept/article71550216.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-13 (d=0.0), 2025-05-01 (d=0.01)

## Watchlist (below surfacing floor)
indices · 2 series ↑ (4.6), indices · 4 series ↓ (4.37), indices · 2 series ↓ (4.29), natgas ↑ (4.03), gold_silver_ratio ↑ (3.85), eur_usd ↓ (3.76), hang_seng ↓ (3.71), dyn_nvda ↑ (3.63), comex_gold ↓ (3.53), dyn_jiofin_bo ↓ (3.3), dyn_hdb ↓ (3.18), dyn_policybzr_ns ↓ (3.17)

## India macro
- nifty_50: 22603.0508 (1d -0.76%, z20 -1.46, flag amber)
- nifty_midcap_100: 59376.8516 (1d -0.64%, z20 -1.33, flag none)
- usd_inr: 96.6580 (1d 0.30%, z20 2.19, flag red)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6269 (1d 0.12%, z20 -0.80, flag none)
- Next India prints: AMFI SIP / MF flows T-0d · NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 88.8 — "CAPITAL ECONOMICS: CENTRAL BANKS MAY HIKE LESS THAN MARKETS EXPECT Capital Economics says "
- COALINDIA.NS (COAL INDIA LTD) score 78.7 — "Saurabh Mukherjea’s Marcellus ties up with VanEck to widen global investment offerings for"
- INOXINDIA.NS (INOX INDIA LIMITED) score 78.6 — "Saurabh Mukherjea’s Marcellus ties up with VanEck to widen global investment offerings for"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 76.4 — "Saurabh Mukherjea’s Marcellus ties up with VanEck to widen global investment offerings for"
- BAC (Bank of America Corporation) score 76.0 — "CAPITAL ECONOMICS: CENTRAL BANKS MAY HIKE LESS THAN MARKETS EXPECT Capital Economics says "
- HDB (HDFC Bank Limited) score 71.9 — "CAPITAL ECONOMICS: CENTRAL BANKS MAY HIKE LESS THAN MARKETS EXPECT Capital Economics says "
- IDBI.NS (IDBI BANK LIMITED) score 69.4 — "CAPITAL ECONOMICS: CENTRAL BANKS MAY HIKE LESS THAN MARKETS EXPECT Capital Economics says "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 69.4 — "CAPITAL ECONOMICS: CENTRAL BANKS MAY HIKE LESS THAN MARKETS EXPECT Capital Economics says "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 69.4 — "CAPITAL ECONOMICS: CENTRAL BANKS MAY HIKE LESS THAN MARKETS EXPECT Capital Economics says "
- COIN (Coinbase Global, Inc.) score 54.8 — "TREASURY'S BESSENT: BONDS ARE A GLOBAL PHENOMENON"
- OHI (Omega Healthcare Investors, In) score 47.6 — "CAPITAL ECONOMICS: CENTRAL BANKS MAY HIKE LESS THAN MARKETS EXPECT Capital Economics says "
- BOND (PIMCO Active Bond Exchange-Tra) score 47.2 — "TREASURY'S BESSENT: BONDS ARE A GLOBAL PHENOMENON"
- TECHM.NS (TECH MAHINDRA LIMITED) score 42.6 — "Top stocks in focus today: Investors must watch Tata Power, Senco Gold, Dixon Tech shares "
- TGT (Target Corporation) score 36.5 — "SPCX - SUSQUEHANNA: RAISES TARGET PRICE TO $173 FROM $144"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 34.5 — "Top stocks in focus today: Investors must watch Tata Power, Senco Gold, Dixon Tech shares "
- TECH (Bio-Techne Corp) score 34.5 — "Top stocks in focus today: Investors must watch Tata Power, Senco Gold, Dixon Tech shares "
- CHKP (Check Point Software Technolog) score 32.1 — "Top 2 stocks to buy for short-term: Bank of Maharashtra, Usha Martin by Nagaraj Shetti - C"
- LTH (Life Time Group Holdings, Inc.) score 28.3 — "TCS Q2 results 2026: Expectations, date and time, dividend announcement schedule, quarterl"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 27.0 — "BESSENT: ENERGY MARKET WILL BE WELL SUPPLIED AFTER IRAN CONFLICT ENDS"
- SEPN (Septerna, Inc.) score 24.3 — "FED MINUTES: MOST OFFICIALS SEE ANOTHER RATE HIKE BY YEAR-END All Fed participants backed "
- 301077.SZ (CHINASTARS) score 19.4 — "China’s Weak Holiday Spending Casts Shadow as Markets Reopen"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 18.4 — "IDFC First Bank share: 30% rally in 6 months! Experts see more upside after Q2FY27 busines"
- BZ=F (Brent Crude Oil Last Day Finan) score 13.9 — "Stock split, spin-off: Last chance to buy these stocks today - Check record date, share pe"
- JUSTDIAL.BO (JUST DIAL LTD.) score 12.6 — "U.S. 10-YEAR TREASURY AUCTION DRAWS STRONG DEMAND The Treasury sold $39 billion of 9-year "
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 12.0 — "Landmark Group raises Rs 330 crore SBI finance for Gurugram project"
- JIOFIN.BO (Jio Financial Services Limited) score 11.5 — "CAPITAL ECONOMICS: CENTRAL BANKS MAY HIKE LESS THAN MARKETS EXPECT Capital Economics says "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.1 — "Top stocks in focus today: Investors must watch Tata Power, Senco Gold, Dixon Tech shares "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 11.1 — "Top stocks in focus today: Investors must watch Tata Power, Senco Gold, Dixon Tech shares "
- JEF (Jefferies Financial Group Inc.) score 10.2 — "Margin boost: Jefferies picks 3 bank stocks to gain the most from RBI rate hikes"
- VT (Vanguard Total World Stock Ind) score 10.2 — "TRUMP: WE SHOULD HAVE THE LOWEST INTEREST RATE IN THE WORLD"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 8.9 — "Landmark Group raises Rs 330 crore SBI finance for Gurugram project"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.8 — "Sensex today | Stock Market Highlights: Sensex closes 429 pts, Nifty slips 0.76% as RBI ra"
- NVDA (NVIDIA Corporation) score 8.5 — "Microsoft and Nvidia are teaming up on a supercharged AI laptop"
- META (Meta) score 8.1 — "26% returns in 2026! UBS retains 'Buy' rating on this metal stock | Target, upside and rat"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 5.7 — "Trent’s Rs 1.80 lakh crore rout from peak: Has Q2 just flipped the script for Tata group’s"
- RS (Reliance, Inc.) score 5.0 — "Jefferies increases weight in Reliance, 2 others; trims weight in 3 stocks in latest model"
- POLICYBZR.NS (PB FINTECH LIMITED) score 5.0 — "Pine Labs, CAMS, Moneyview, other fintech stocks rally up to 11% after RBI MPC move. Here’"
- GS (Goldman Sachs Group, Inc. (The) score 4.8 — "TSLA - GOLDMAN: TESLA’S AI STORY MATTERS MORE THAN Q3 EARNINGS Goldman Sachs reiterated it"
- VOLTAS.NS (VOLTAS LTD) score 0.1 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 0.0 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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