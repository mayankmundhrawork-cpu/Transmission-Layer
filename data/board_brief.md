# Transmission Layer — board brief · 2026-09-29 01:06Z

data as of **2026-09-29** · 97 series · 12 red / 30 amber · 7 events surfaced (23 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.667, 4d in regime; vol-pct None, breadth-off 0.667, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.54, corr60 -0.41, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.83, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 -0.02, corr60 0.24, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.03, corr60 0.11, last shift 2026-08-17. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.78, corr60 -0.78, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.05, corr60 -0.1, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.29, corr60 -0.15, last shift 2026-08-10. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.42, corr60 0.21, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 4.5035700777074084e-05)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.5** (n=1119) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.83** (n=2378) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.6] hy_oas ↑
- hy_oas [RATES]: last 2.93, z20 5.60, zc 2.51, resid-z 4.08 [unexplained], 1d 4.64%, |z20|=5.60
- **Mechanism**: hy_oas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: GOLDMAN WARNS JUNK BOND SUPPLY IS OVERWHELMING INVESTORS Goldman Sachs says a flood of U.S. high-yield debt issuance is straining investor demand, pushing junk-bond spreads to their widest since April. September issuance has reached $38.5 billion, while CCC spreads have surged to their highest since — DeItaone, 2026-09-28. https://t.me/walter_bloomberg/36264
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-25 (d=0.0), 2025-07-31 (d=0.01)

### [RED 6.94] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4149.60, z20 -3.01, zc -0.03, resid-z -0.30 [quiet], 1d -0.03%, |z20|=3.01; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 61.01, z20 -2.56, zc -0.03, resid-z 0.50 [quiet], 1d -0.07%, |z20|=2.56; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 68.01, z20 0.63, zc n/a, resid-z n/a [quiet], 1d 0.04%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.6 vs comex_silver, historically leads by 1d
- Watch next: btc_usd (co-move) — not yet - watch; rho 0.59 vs comex_gold
- Watch next: eth_usd (co-move) — not yet - watch; rho 0.588 vs comex_gold
- Source: Gold, silver tumble; festive buyers wait — ET Markets, 2026-09-29. https://economictimes.indiatimes.com/markets/commodities/news/gold-silver-tumble-festive-buyers-wait/articleshow/134553241.cms
- Source: Gold, silver slide as buyers wait for prices to stabilise — ET Markets, 2026-09-29. https://economictimes.indiatimes.com/markets/commodities/news/gold-silver-tumble-festive-buyers-wait/articleshow/134553241.cms
- Source: Gold tumbles 4% to seven-week low as oil, dollar and yields climb — ET Markets, 2026-09-28. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/gold-tumbles-4-to-seven-week-low-as-oil-dollar-and-yields-climb/articleshow/134549139.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.78] cross-asset · 4 series ↓
- dyn_policybzr_ns [EQUITIES]: last 1151.30, z20 -3.12, zc -0.11, resid-z -1.03 [quiet], 1d -1.26%, |z20|=3.12; 1y-pct=0
- india_vix [INDICES]: last 13.74, z20 2.62, zc -0.55, resid-z n/a [quiet], 1d 13.03%, |z20|=2.62
- nifty_midcap_100 [INDICES]: last 59913.20, z20 -2.51, zc -0.14, resid-z -1.03 [quiet], 1d -1.62%, |z20|=2.51
- nifty_50 [INDICES]: last 22780.25, z20 -2.29, zc 0.48, resid-z 0.36 [quiet], 1d -1.56%, |z20|=2.29; 1y-pct=2
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.49).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.586 via nifty_midcap_100, z -1.36, reacted); dyn_jiofin_bo (rho 0.582 via nifty_50, z -2.84, reacted); nifty_fmcg (rho 0.558 via nifty_50, z -1.07, reacted); nifty_metal (rho 0.51 via nifty_midcap_100, z -1.26, reacted); dyn_techm_ns (rho 0.495 via nifty_50, z -0.69, quiet)
- **India receivers**: midcap_largecap_ratio (rho 0.586, z -1.36); dyn_jiofin_bo (rho 0.582, z -2.84); nifty_fmcg (rho 0.558, z -1.07); nifty_metal (rho 0.51, z -1.26)
- Source: Sensex today | Stock Market Live Updates: Stock to buy today: Parag Milk Foods (₹275) – BUY — BusinessLine Mkts, 2026-09-29. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-29-september-2026/article71520150.ece
- Source: Nifty 50 breaks below 23K! Monthly expiry may keep volatility elevated | Support, resistance, outlook for Sep 29 — Mint Markets, 2026-09-28. https://www.livemint.com/market/stock-market-news/nifty-50-breaks-below-23k-monthly-expiry-may-keep-volatility-elevated-support-resistance-outlook-for-sep-29-11790611758900.html
- Source: Nifty slides to six-month low as US-Iran deal hopes fade, oil tops $100 a barrel — Mint Markets, 2026-09-28. https://www.livemint.com/market/stock-market-news/crude-oil-impact-india-stock-market-nifty-today-11790598428016.html
- Historical analogues: 2025-07-21 (d=0.49), 2025-07-14 (d=0.72), 2025-12-30 (d=0.96)

### [RED 6.75] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.49, z20 2.82, zc 0.44, resid-z 0.60 [quiet], 1d 0.37%, |z20|=2.82; 1y-pct=100
- dyn_bond [EQUITIES]: last 87.27, z20 -2.28, zc 0.33, resid-z 0.13 [quiet], 1d -0.48%, |z20|=2.28; 1y-pct=0
- tips_10y_real [RATES]: last 2.83, z20 2.13, zc -0.31, resid-z -0.18 [quiet], 1d -0.70%, |z20|=2.13; 1y-pct=99
- ust_10y [RATES]: last 5.17, z20 2.05, zc -0.18, resid-z -0.02 [quiet], 1d -0.19%, |z20|=2.05; 1y-pct=99
- ust_2y [RATES]: last 4.81, z20 1.31, zc -0.92, resid-z -0.78 [quiet], 1d -1.23%, 1y-pct=99
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.666 vs ust_30y, historically leads by 3d
- Watch next: wti (co-move) — not yet - watch; rho 0.517 vs ust_30y, historically leads by 3d
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.504 vs ust_10y, historically leads by 4d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.6 vs dyn_bond
- Watch next: sp500 (co-move) — not yet - watch; rho 0.548 vs dyn_bond
- Source: Global Market Today: Asian shares mixed as surging oil, Treasury yields weigh — ET Markets, 2026-09-29. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-today-asian-shares-mixed-as-surging-oil-treasury-yields-weigh/articleshow/134553458.cms
- Source: Ten-year bond yield hits 7.19%, highest in two years — ET Markets, 2026-09-29. https://economictimes.indiatimes.com/markets/bonds/ten-year-bond-yield-hits-7-19-highest-in-two-years/articleshow/134553130.cms
- Source: Bond yields move relentlessly higher, as Wall Street wonders how much more tech stocks can take — MarketWatch Top, 2026-09-28. https://www.marketwatch.com/story/bond-yields-move-relentlessly-higher-as-wall-street-wonders-how-much-more-tech-stocks-can-take-dd050c39?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 4.89] fx · 4 series ↓
- usd_mxn [FX]: last 17.98, z20 3.23, zc 1.74, resid-z 2.44 [unexplained], 1d 1.28%, |z20|=3.23
- aud_usd [FX]: last 0.70, z20 -1.92, zc 0.14, resid-z -0.69 [quiet], 1d 0.09%, |z20|=1.92
- eur_usd [FX]: last 1.14, z20 -1.82, zc -0.18, resid-z -0.19 [quiet], 1d -0.06%, |z20|=1.82; 1y-pct=1
- gbp_usd [FX]: last 1.32, z20 -1.71, zc 0.38, resid-z -0.67 [quiet], 1d 0.14%, |z20|=1.71
- **Mechanism**: fx · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_icicigi_bo (rho -0.488 via gbp_usd, z 0.91, quiet); dyn_muthootfin_ns (rho 0.464 via aud_usd, z -1.43, reacted); dyn_policybzr_ns (rho -0.455 via usd_mxn, z -3.12, reacted); dyn_inoxindia_ns (rho 0.419 via aud_usd, z -1.1, reacted); nifty_50 (rho 0.378 via eur_usd, z -2.29, reacted)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.552 vs aud_usd, historically leads by 3d
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.408 vs eur_usd, historically leads by 1d
- **India receivers**: dyn_icicigi_bo (rho -0.488, z 0.91); dyn_muthootfin_ns (rho 0.464, z -1.43); dyn_policybzr_ns (rho -0.455, z -3.12); dyn_inoxindia_ns (rho 0.419, z -1.1)
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [AMBER 4.3] dyn_chkp ↓
- dyn_chkp [EQUITIES]: last 129.19, z20 -2.30, zc -1.60, resid-z -1.27 [moved], 1d -1.56%, |z20|=2.30
- **Mechanism**: dyn_chkp ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tatatech_ns (rho 0.351 via dyn_chkp, z -1.56, reacted)
- **India receivers**: dyn_tatatech_ns (rho 0.351, z -1.56)
- Source: 4 Adani group companies settle public shareholding violations case with Sebi. Check details — ET Markets, 2026-09-28. https://economictimes.indiatimes.com/markets/stocks/news/4-adani-group-companies-settle-public-shareholding-violations-case-with-sebi-check-details/articleshow/134547647.cms
- Source: Top 2 stocks to buy or sell tomorrow: Laurus Labs, Indus Towers by Chandan Taparia - Check stop-loss, targets — Mint Markets, 2026-09-28. https://www.livemint.com/market/stock-market-news/top-2-stocks-to-buy-or-sell-tomorrow-laurus-labs-indus-towers-by-chandan-taparia-check-stop-loss-targets-11790594465913.html
- Source: BSE stock falls 2.3% as SEBI mulls self-listing rules revamp, days after NSE IPO listing - Check details — Mint Markets, 2026-09-28. https://www.livemint.com/market/bse-stock-falls-2-3-as-sebi-mulls-self-listing-rules-revamp-days-after-nse-ipo-listing-check-details-11790585815691.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2025-05-20 (d=0.04)

### [AMBER 3.3] dyn_nvda ↑
- dyn_nvda [EQUITIES]: last 228.88, z20 1.30, zc 0.09, resid-z -0.57 [quiet], 1d 1.69%, 1y-pct=99
- **Mechanism**: dyn_nvda ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.629 vs dyn_nvda, historically leads by 4d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.624 vs dyn_nvda, historically leads by 4d
- Watch next: vix (inverse) — not yet - watch; rho -0.593 vs dyn_nvda, historically leads by 4d
- Watch next: dyn_dell (co-move) — not yet - watch; rho 0.521 vs dyn_nvda, historically leads by 1d
- Source: Nvidia makes a statement with historic $150 billion buyback announcement — MarketWatch Top, 2026-09-28. https://www.marketwatch.com/story/nvidia-makes-a-statement-with-historic-150-billion-buyback-announcement-bfab5a22?mod=mw_rss_topstories
- Source: Nvidia is right: Its stock is a bargain by this measure — MarketWatch Top, 2026-09-28. https://www.marketwatch.com/story/nvidia-is-right-its-stock-is-a-bargain-95cee6ca?mod=mw_rss_topstories
- Source: Nvidia announces $150 billion buyback boost as AI boom drives massive cash flow — Mint Markets, 2026-09-28. https://www.livemint.com/market/stock-market-news/nvidia-announces-150-billion-buyback-boost-as-ai-boom-drives-massive-cash-flow-11790598664870.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-24 (d=0.03), 2026-05-04 (d=0.03)

## Watchlist (below surfacing floor)
dyn_4417_t ↑ (3.16), shanghai_comp ↓ (3.13), dyn_tech ↑ (3.1), dyn_hdb ↓ (3.04), dyn_havells_ns ↓ (3.0), usd_brl ↑ (2.92), dyn_jiofin_bo ↓ (2.84), commodities · 2 series ↓ (2.74), dyn_indianb_ns ↓ (2.7), dyn_indusindbk_bo ↓ (2.41), dyn_atherenerg_ns ↓ (2.2), dyn_ms ↓ (2.08)

## India macro
- nifty_50: 22780.2500 (1d -1.56%, z20 -2.29, flag amber)
- nifty_midcap_100: 59913.1992 (1d -1.62%, z20 -2.51, flag red)
- usd_inr: 95.9730 (1d 0.19%, z20 1.01, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6301 (1d -0.07%, z20 -1.36, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 65.8 — "Goldman Sachs identifies 42 Indian stocks riding AI build-out"
- INOXINDIA.NS (INOX INDIA LIMITED) score 64.3 — "Goldman Sachs identifies 42 Indian stocks riding AI build-out"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 64.1 — "Goldman Sachs identifies 42 Indian stocks riding AI build-out"
- INDIANB.NS (INDIAN BANK) score 42.1 — "Goldman Sachs identifies 42 Indian stocks riding AI build-out"
- COIN (Coinbase Global, Inc.) score 41.7 — "Global Market Today: Asian shares mixed as surging oil, Treasury yields weigh"
- OHI (Omega Healthcare Investors, In) score 34.5 — "GOLDMAN WARNS JUNK BOND SUPPLY IS OVERWHELMING INVESTORS Goldman Sachs says a flood of U.S"
- TECHM.NS (TECH MAHINDRA LIMITED) score 33.0 — "GM - TRUMP ADMINISTRATION FORECASTS GENERAL MOTORS TECHNOLOGY COSTS THROUGH 2031 WILL DECL"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 33.0 — "GM - TRUMP ADMINISTRATION FORECASTS GENERAL MOTORS TECHNOLOGY COSTS THROUGH 2031 WILL DECL"
- TECH (Bio-Techne Corp) score 33.0 — "GM - TRUMP ADMINISTRATION FORECASTS GENERAL MOTORS TECHNOLOGY COSTS THROUGH 2031 WILL DECL"
- CHKP (Check Point Software Technolog) score 32.4 — "Top 2 stocks to buy or sell tomorrow: Laurus Labs, Indus Towers by Chandan Taparia - Check"
- HDB (HDFC Bank Limited) score 30.6 — "Govt vs private banks dividend comparison: SBI, HDFC, ICICI, PNB, BoB, Axis, Canara - Whic"
- BOND (PIMCO Active Bond Exchange-Tra) score 29.2 — "GOLDMAN WARNS JUNK BOND SUPPLY IS OVERWHELMING INVESTORS Goldman Sachs says a flood of U.S"
- BAC (Bank of America Corporation) score 28.8 — "Govt vs private banks dividend comparison: SBI, HDFC, ICICI, PNB, BoB, Axis, Canara - Whic"
- 301077.SZ (CHINASTARS) score 27.3 — "TRUMP REJECTS AI INTEGRATION WITH CHINA President Trump said the U.S. should not integrate"
- IDBI.NS (IDBI BANK LIMITED) score 25.9 — "Govt vs private banks dividend comparison: SBI, HDFC, ICICI, PNB, BoB, Axis, Canara - Whic"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 25.9 — "Govt vs private banks dividend comparison: SBI, HDFC, ICICI, PNB, BoB, Axis, Canara - Whic"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 25.9 — "Govt vs private banks dividend comparison: SBI, HDFC, ICICI, PNB, BoB, Axis, Canara - Whic"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 24.6 — "Stocks in news: Tata Group, ITC, IRFC, NCC, Zydus Lifesciences and JSW Energy"
- SEPN (Septerna, Inc.) score 24.1 — "GOLDMAN WARNS JUNK BOND SUPPLY IS OVERWHELMING INVESTORS Goldman Sachs says a flood of U.S"
- LTH (Life Time Group Holdings, Inc.) score 23.8 — "RBI completes 1 trillion rupee net debt sale for first time in a decade"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 15.3 — "Sebi clears Gautam, Vinod Adani of MPS norm violation"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 14.0 — "Stocks in news: Tata Group, ITC, IRFC, NCC, Zydus Lifesciences and JSW Energy"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 14.0 — "Stocks in news: Tata Group, ITC, IRFC, NCC, Zydus Lifesciences and JSW Energy"
- BZ=F (Brent Crude Oil Last Day Finan) score 11.5 — "STOCKS OF CRUDE OIL IN US STRATEGIC PETROLEUM RESERVE FELL TO 283.8 MLN BARRELS LAST WEEK,"
- JIOFIN.BO (Jio Financial Services Limited) score 10.0 — "Spending $800 to see my family this Thanksgiving is a financial burden. How can I push for"
- META (Meta) score 9.7 — "META - META PRICE TARGET RAISED TO $830 Monness Crespi Hardt raised its Meta price target "
- POLICYBZR.NS (PB FINTECH LIMITED) score 9.1 — "PB Fintech: the risk was known. Investors chased the stock anyway"
- GS (Goldman Sachs Group, Inc. (The) score 7.9 — "Goldman Sachs identifies 42 Indian stocks riding AI build-out"
- VT (Vanguard Total World Stock Ind) score 6.5 — "The World Is Entering a New Era of Energy Security"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.4 — "Govt vs private banks dividend comparison: SBI, HDFC, ICICI, PNB, BoB, Axis, Canara - Whic"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 6.3 — "IPO frenzy attracts FPIs, even as stock selling hits  ₹25,682 crore in September: Will tre"
- JUSTDIAL.BO (JUST DIAL LTD.) score 6.1 — "The Next Global Energy Crisis Won’t Come From Just One Direction"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 5.3 — "JAPANESE, US FINANCE CHIEFS DISCUSS YEN DEPRECIATION: KYODO"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 5.3 — "ETMarkets Smart Talk| F&O STT, UPI charges and trading costs: Sandeep Neema on the hidden "
- NVDA (NVIDIA Corporation) score 4.8 — "NVDA - NVIDIA EXPANDS BUYBACK PROGRAM TO $235 BILLION Nvidia’s board authorized a $150 bil"
- MS (Morgan Stanley) score 4.2 — "‘We were wrong.’ Why Morgan Stanley changed its tune on the U.S. dollar — and what it expe"
- TGT (Target Corporation) score 2.8 — "EU'S KALLAS: EUROPE NEEDS TO REARM MORE QUICKLY AND MORE EFFECTIVELY TO MEET OUR 2030 TARG"
- MU (Micron Technology, Inc.) score 2.3 — "Micron has a chance to set the record straight with its earnings report"
- VOLTAS.NS (VOLTAS LTD) score 0.7 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 0.4 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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