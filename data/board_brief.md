# Transmission Layer — board brief · 2026-09-30 10:28Z

data as of **2026-09-30** · 97 series · 11 red / 30 amber · 8 events surfaced (23 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.681, 5d in regime; vol-pct 0.611, breadth-off 0.75, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.5, corr60 -0.41, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.8, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 -0.04, corr60 0.09, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.08, corr60 0.12, last shift 2026-08-17. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.78, corr60 -0.76, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.11, corr60 -0.1, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.29, corr60 -0.15, last shift 2026-08-10. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.43, corr60 0.21, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 4.5035700777074084e-05)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.501** (n=1117) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.831** (n=2323) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.34] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.56, z20 3.34, zc 0.44, resid-z 0.60 [quiet], 1d 1.28%, |z20|=3.34; 1y-pct=100
- tips_10y_real [RATES]: last 2.90, z20 2.41, zc -0.31, resid-z -0.18 [quiet], 1d 2.47%, 1d move +7.0bps ≥ 5bps; |z20|=2.41; 1y-pct=100
- ust_10y [RATES]: last 5.24, z20 2.36, zc -0.18, resid-z -0.02 [quiet], 1d 1.35%, |z20|=2.36; 1y-pct=100
- dyn_bond [EQUITIES]: last 87.07, z20 -2.24, zc -0.59, resid-z 0.13 [quiet], 1d -0.23%, |z20|=2.24; 1y-pct=0
- ust_2y [RATES]: last 4.92, z20 1.81, zc -0.92, resid-z -0.78 [quiet], 1d 2.29%, |z20|=1.81; 1y-pct=100
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.546 vs dyn_bond
- Source: Global Market: Eurozone bond yields ease from highs as rate-hike bets cool — ET Markets, 2026-09-30. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-eurozone-bond-yields-ease-from-highs-as-rate-hike-bets-cool/articleshow/134590223.cms
- Source: Sebi and RBI working closely to streamline FPIs, bond market: Tuhin Kanta Pandey — Mint Markets, 2026-09-30. https://www.livemint.com/market/sebi-rbi-fpi-onboarding-five-days-bond-market-liquidity-11790756166465.html
- Source: Sensex, Nifty impact Explained: Why 30-year US Treasury bond yields surged to 2002 levels and why it matters to India? — Mint Markets, 2026-09-30. https://www.livemint.com/market/stock-market-news/sensex-nifty-impact-explained-why-30-year-us-treasury-bond-yields-surged-to-2002-levels-and-why-it-matters-to-india-11790751047666.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 7.89] cross-asset · 3 series ↓
- comex_silver [COMMODITIES]: last 61.22, z20 -1.99, zc 0.46, resid-z -0.27 [quiet], 1d 0.90%, |z20|=1.99; co-occur[gold_silver] same-direction (channel VALID)
- comex_gold [COMMODITIES]: last 4218.90, z20 -1.78, zc 0.97, resid-z -0.30 [quiet], 1d 0.94%, |z20|=1.78; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 68.92, z20 1.57, zc n/a, resid-z n/a [quiet], 1d 0.04%, GSR<75 (extreme low); |z20|=1.57
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.594 vs comex_silver, historically leads by 1d
- Watch next: btc_usd (co-move) — not yet - watch; rho 0.534 vs comex_silver
- Source: Today’s Gold Rate in India September 30: Gold prices up in Coimbatore, Nagpur, Visakhapatnam, Surat and other cities — BusinessLine Mkts, 2026-09-30. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-coimbatore-nagpur-visakhapatnam-surat-jaipur-lucknow-chandigarh-gold-rates-other-cities-september-30-2026/article71527482.ece
- Source: Today’s Gold Rate in India September 30: Gold prices up in Delhi, Mumbai, Kolkata, Chennai, Bengaluru — BusinessLine Mkts, 2026-09-30. https://www.thehindubusinessline.com/markets/gold/gold-price-today-in-delhi-mumbai-kolkata-chennai-bengaluru-hyderabad-pune-gold-rates-metro-cities-september-30-2026/article71527481.ece
- Source: Gold on track for monthly decline as investors brace for US inflation data — BusinessLine Mkts, 2026-09-30. https://www.thehindubusinessline.com/markets/gold/gold-set-to-register-monthly-decline-as-investors-brace-for-us-inflation-data/article71526677.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.87] hy_oas ↑
- hy_oas [RATES]: last 3.02, z20 4.87, zc 2.51, resid-z 4.08 [unexplained], 1d 3.07%, |z20|=4.87
- **Mechanism**: hy_oas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: GOLDMAN WARNS JUNK BOND SUPPLY IS OVERWHELMING INVESTORS Goldman Sachs says a flood of U.S. high-yield debt issuance is straining investor demand, pushing junk-bond spreads to their widest since April. September issuance has reached $38.5 billion, while CCC spreads have surged to their highest since — DeItaone, 2026-09-28. https://t.me/walter_bloomberg/36264
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-25 (d=0.0), 2025-07-31 (d=0.01)

### [AMBER 6.26] brent ↓
- brent [COMMODITIES]: last 97.23, z20 -1.26, zc -1.94, resid-z -1.14 [moved], 1d -5.22%, 1-session move -5.22% ≥ 1.5%
- **Mechanism**: brent ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.532 vs brent, historically leads by 5d
- Watch next: dax (inverse) — not yet - watch; rho -0.503 vs brent, historically leads by 5d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.611 vs brent
- Source: Foreign Investors Pull $3.2 Billion From Indian Markets as Oil Rally Returns — OilPrice, 2026-09-30. https://oilprice.com/Latest-Energy-News/World-News/Foreign-Investors-Pull-32-Billion-From-Indian-Markets-as-Oil-Rally-Returns.html
- Source: One group of funds is holding up the stock market. Barclays says oil prices have to fall to drive a year-end rally. — MarketWatch Top, 2026-09-30. https://www.marketwatch.com/story/one-group-of-funds-is-holding-up-the-stock-market-barclays-says-oil-prices-have-to-fall-to-drive-a-year-end-rally-c6d551f9?mod=mw_rss_topstories
- Source: India Boosts Middle East Oil Imports, Cuts Russian Flows — OilPrice, 2026-09-30. https://oilprice.com/Latest-Energy-News/World-News/India-Boosts-Middle-East-Oil-Imports-Cuts-Russian-Flows.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.0), 2025-08-14 (d=0.02)

### [AMBER 6.03] cross-asset · 4 series ↓
- nifty_midcap_100 [INDICES]: last 59321.50, z20 -2.37, zc 0.00, resid-z 0.61 [quiet], 1d 0.00%, |z20|=2.37
- dyn_policybzr_ns [EQUITIES]: last 1063.90, z20 -2.31, zc -0.14, resid-z -0.11 [quiet], 1d -1.58%, |z20|=2.31; 1y-pct=0
- nifty_50 [INDICES]: last 22620.45, z20 -2.23, zc -0.64, resid-z -0.65 [quiet], 1d -0.42%, |z20|=2.23; 1y-pct=1
- india_vix [INDICES]: last 13.46, z20 1.67, zc 0.06, resid-z n/a [quiet], 1d 0.39%, |z20|=1.67
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.49).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.611 via nifty_midcap_100, z -1.45, reacted); dyn_jiofin_bo (rho 0.57 via nifty_50, z -2.59, reacted); nifty_fmcg (rho 0.557 via nifty_50, z -2.49, reacted); dyn_indusindbk_bo (rho 0.476 via nifty_midcap_100, z -1.9, reacted); dyn_techm_ns (rho 0.47 via nifty_50, z -1.13, reacted)
- **India receivers**: midcap_largecap_ratio (rho 0.611, z -1.45); dyn_jiofin_bo (rho 0.57, z -2.59); nifty_fmcg (rho 0.557, z -2.49); dyn_indusindbk_bo (rho 0.476, z -1.9)
- Source: Sensex today | Stock Market Closing Bell: Sensex settled at 72,480.29; Nifty 50 fell to 22,620.45 — BusinessLine Mkts, 2026-09-30. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-30-september-2026/article71523523.ece
- Source: Sensex, Nifty remains volatile: Where should investors put their money? Experts decode portfolio allocation — Mint Markets, 2026-09-30. https://www.livemint.com/market/stock-market-news/sensex-nifty-remains-volatile-where-should-investors-put-their-money-experts-decode-portfolio-allocation-11790757435686.html
- Source: Sensex, Nifty impact Explained: Why 30-year US Treasury bond yields surged to 2002 levels and why it matters to India? — Mint Markets, 2026-09-30. https://www.livemint.com/market/stock-market-news/sensex-nifty-impact-explained-why-30-year-us-treasury-bond-yields-surged-to-2002-levels-and-why-it-matters-to-india-11790751047666.html
- Historical analogues: 2025-07-21 (d=0.49), 2025-07-14 (d=0.72), 2025-12-30 (d=0.96)

### [RED 4.7] dyn_chkp ↓
- dyn_chkp [EQUITIES]: last 126.93, z20 -2.70, zc -0.78, resid-z -1.27 [quiet], 1d -1.81%, |z20|=2.70
- **Mechanism**: dyn_chkp ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tatatech_ns (rho 0.363 via dyn_chkp, z -1.22, reacted)
- **India receivers**: dyn_tatatech_ns (rho 0.363, z -1.22)
- Source: Up 50% in 1 year, Vedanta raises  ₹2,000 crore via NCDs: Check full details - what it means for shareholders, company — Mint Markets, 2026-09-30. https://www.livemint.com/market/stock-market-news/up-50-in-1-year-vedanta-raises-rs-2-000-crore-via-ncds-check-full-details-what-it-means-for-shareholders-company-11790748528736.html
- Source: Solar Industries shares up over 6%! What's driving defence stock that has surged 60% in YTD | Check target, stop loss — Mint Markets, 2026-09-30. https://www.livemint.com/market/stock-market-news/solar-industries-shares-up-over-6-whats-driving-defence-stock-that-has-surged-60-in-ytd-check-target-price-11790745066638.html
- Source: Inox Clean Energy files DRHP for Rs 10,000 crore IPO. Check details — ET Markets, 2026-09-30. https://economictimes.indiatimes.com/markets/ipos/fpos/inox-clean-energy-files-drhp-for-rs-10000-crore-ipo-check-details/articleshow/134582612.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2025-05-20 (d=0.04)

### [RED 4.69] dyn_havells_ns ↓
- dyn_havells_ns [EQUITIES]: last 1016.00, z20 -2.69, zc -1.67, resid-z -1.42 [moved], 1d -2.62%, |z20|=2.69; 1y-pct=0
- **Mechanism**: dyn_havells_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.351 via dyn_havells_ns, z -2.37, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.351, z -2.37)
- Source: Havells India among 8 midcap stocks that hit 52-week lows and slipped up to 15% in a month — ET Markets, 2026-09-28. https://economictimes.indiatimes.com/markets/stocks/news/havells-india-among-8-midcap-stocks-that-hit-52-week-lows-and-slipped-up-to-15-in-a-month/slideshow/134543453.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-22 (d=0.01), 2025-06-30 (d=0.02)

### [AMBER 4.66] indices · 2 series ↑
- nikkei_225 [INDICES]: last 66864.15, z20 1.83, zc 1.72, resid-z -0.06 [moved], 1d 2.11%, |z20|=1.83
- taiwan_weighted [INDICES]: last 48163.78, z20 1.70, zc 1.02, resid-z -0.46 [quiet], 1d 1.12%, |z20|=1.70; 1y-pct=100
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.7).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho -0.448 via taiwan_weighted, z -1.48, reacted); dyn_techm_ns (rho -0.399 via taiwan_weighted, z -1.13, reacted); dyn_icicigi_bo (rho 0.352 via nikkei_225, z 2.16, reacted)
- Watch next: kospi (co-move) — not yet - watch; rho 0.837 vs nikkei_225
- **India receivers**: nifty_it (rho -0.448, z -1.48); dyn_techm_ns (rho -0.399, z -1.13); dyn_icicigi_bo (rho 0.352, z 2.16)
- Source: Global Market: Japan’s Nikkei rises as AI stocks track US chip gains — ET Markets, 2026-09-30. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-rises-as-ai-stocks-track-us-chip-gains/articleshow/134581624.cms
- Source: Global Market: Nikkei falls as oil surge, global bond selloff rattle markets — ET Markets, 2026-09-29. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-nikkei-falls-as-oil-surge-global-bond-selloff-rattle-markets/articleshow/134555654.cms
- Historical analogues: 2025-12-30 (d=0.7), 2025-07-11 (d=0.77), 2026-06-09 (d=1.0)

## Watchlist (below surfacing floor)
dyn_jiofin_bo ↓ (4.59), dyn_icicigi_bo ↑ (4.16), eur_usd ↓ (3.7), shanghai_comp ↓ (3.69), fx · 2 series ↑ (3.67), dyn_meta ↑ (3.2), dyn_4417_t ↑ (3.0), dyn_voltas_ns ↓ (2.94), dyn_nvda ↑ (2.89), nifty_fmcg ↓ (2.49), dyn_hdb ↓ (2.43), ig_oas ↑ (2.21)

## India macro
- nifty_50: 22620.4492 (1d -0.42%, z20 -2.23, flag amber)
- nifty_midcap_100: 59321.5000 (1d 0.00%, z20 -2.37, flag amber)
- usd_inr: 95.8300 (1d -0.16%, z20 0.68, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6225 (1d 0.42%, z20 -1.45, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 90.9 — "Negative opening likely for Indian stock markets"
- COALINDIA.NS (COAL INDIA LTD) score 90.0 — "Negative opening likely for Indian stock markets"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 88.8 — "Negative opening likely for Indian stock markets"
- INDIANB.NS (INDIAN BANK) score 54.5 — "Negative opening likely for Indian stock markets"
- COIN (Coinbase Global, Inc.) score 50.8 — "Global Market: South Korea stocks erase gains as Kospi eyes steepest quarterly fall since "
- TECHM.NS (TECH MAHINDRA LIMITED) score 48.7 — "IT sector Q2 FY27 preview: TCS, Infosys to HCL Tech, Tech M— Kotak sees muted quarter for "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 47.0 — "IT sector Q2 FY27 preview: TCS, Infosys to HCL Tech, Tech M— Kotak sees muted quarter for "
- TECH (Bio-Techne Corp) score 47.0 — "IT sector Q2 FY27 preview: TCS, Infosys to HCL Tech, Tech M— Kotak sees muted quarter for "
- OHI (Omega Healthcare Investors, In) score 42.6 — "Gold on track for monthly decline as investors brace for US inflation data"
- BOND (PIMCO Active Bond Exchange-Tra) score 41.6 — "India bonds to edge up on steady US yields, oil prices"
- CHKP (Check Point Software Technolog) score 39.5 — "Nityas Gems & Jewellery IPO opens today. Check GMP, price band and key details"
- SEPN (Septerna, Inc.) score 35.5 — "Foreign outflows from Indian stocks hit 6-month high in September on higher oil, yields"
- HDB (HDFC Bank Limited) score 34.6 — "PSU banks face a bigger risk from bond yields than potential loan waivers"
- BAC (Bank of America Corporation) score 33.2 — "PSU banks face a bigger risk from bond yields than potential loan waivers"
- LTH (Life Time Group Holdings, Inc.) score 32.3 — "Firstsource Solutions share price jumps 9% with volume surging 2 times - Experts highlight"
- IDBI.NS (IDBI BANK LIMITED) score 31.1 — "PSU banks face a bigger risk from bond yields than potential loan waivers"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 31.1 — "PSU banks face a bigger risk from bond yields than potential loan waivers"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 31.1 — "PSU banks face a bigger risk from bond yields than potential loan waivers"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 29.7 — "Inox Clean Energy files DRHP for Rs 10,000 crore IPO. Check details"
- 301077.SZ (CHINASTARS) score 25.2 — "Slow is beautiful: China launches war against AI drama, goes beyond algorithms"
- TGT (Target Corporation) score 17.7 — "Morgan Stanley raises Lenskart target price to Rs 718; bull case implies 41% upside. Here’"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 16.2 — "Power Mech Projects shares rise 4% after company secures Rs 549 crore order from Adani Gro"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 16.1 — "20 stocks to watch today: Tata Steel, Time Technoplast, Shiva Cement/JSW Cement, KPI Energ"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 16.1 — "20 stocks to watch today: Tata Steel, Time Technoplast, Shiva Cement/JSW Cement, KPI Energ"
- BZ=F (Brent Crude Oil Last Day Finan) score 15.6 — "Dividend, bonus, rights issue: Last chance to buy today before record date - IGL, KM Sugar"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 13.6 — "Firstsource Solutions share price jumps 9% with volume surging 2 times - Experts highlight"
- GS (Goldman Sachs Group, Inc. (The) score 10.5 — "JP Morgan, Goldman Diverge on Hormuz Oil Flow Estimates"
- POLICYBZR.NS (PB FINTECH LIMITED) score 9.8 — "PB Fintech shares suffer Rs 37,000 crore shock in 4 days but Jefferies, Bernstein see up t"
- JIOFIN.BO (Jio Financial Services Limited) score 9.7 — "TRUMP: PEOPLE IN AREAS WHERE DATA CENTERS BUILT WILL GREATLY BENEFIT FINANCIALLY"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.8 — "Nifty Outlook: Down in just 3 of last 10 Octobers — Can bulls return after September sell-"
- NVDA (NVIDIA Corporation) score 7.9 — "NVIDIA'S HUANG: WE'RE GOING TO ADVANCE THIS RESPONSIBLY AND SAFELY"
- META (Meta) score 7.9 — "Nifty Metal slips 5% in September post 29% 1 yr rally, October comeback ahead? Hindustan Z"
- JEF (Jefferies Financial Group Inc.) score 7.6 — "Molbio Diagnostics shares rally 9% as Jefferies initiates 'high conviction top pick' call "
- VT (Vanguard Total World Stock Ind) score 7.3 — "The real prize in AMD’s $8 billion World Labs acquisition isn’t what you’d think"
- MS (Morgan Stanley) score 5.8 — "Morgan Stanley raises Lenskart target price to Rs 718; bull case implies 41% upside. Here’"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 5.6 — "Hollywood’s big debt deal hits a wall of higher yields as Paramount finances Warner Bros. "
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.6 — "Govt vs private banks dividend comparison: SBI, HDFC, ICICI, PNB, BoB, Axis, Canara - Whic"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 3.8 — "ETMarkets Smart Talk| F&O STT, UPI charges and trading costs: Sandeep Neema on the hidden "
- VOLTAS.NS (VOLTAS LTD) score 0.5 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 0.3 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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