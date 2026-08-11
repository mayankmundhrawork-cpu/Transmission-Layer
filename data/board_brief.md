# Transmission Layer — board brief · 2026-08-11 05:21Z

data as of **2026-08-11** · 98 series · 6 red / 33 amber · 8 events surfaced (18 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.365, 1d in regime; vol-pct 0.443, breadth-off 0.286, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.4, corr60 -0.4, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.81, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.31, corr60 0.35, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.15, corr60 -0.08, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.79, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.09, corr60 -0.03, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.41, corr60 -0.25, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.07, corr60 0.16, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.492** (n=1132) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.82** (n=2389) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.36] cross-asset · 11 series ↑
- comex_gold [COMMODITIES]: last 4464.70, z20 3.42, zc 1.32, resid-z 1.08 [quiet], 1d 2.36%, |z20|=3.42; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 65.65, z20 2.84, zc 0.30, resid-z 1.16 [quiet], 1d 0.84%, |z20|=2.84; co-occur[gold_silver] same-direction (channel VALID)
- stoxx_50 [INDICES]: last 6539.07, z20 2.17, zc 0.28, resid-z 0.93 [quiet], 1d 0.23%, |z20|=2.17; 1y-pct=100
- cac_40 [INDICES]: last 8724.88, z20 1.99, zc 0.15, resid-z 1.16 [quiet], 1d 0.11%, |z20|=1.99; 1y-pct=100
- dyn_vt [EQUITIES]: last 160.99, z20 1.94, zc -0.20, resid-z 0.29 [quiet], 1d -0.19%, 1y-pct=99
- dax [INDICES]: last 26354.84, z20 1.91, zc 0.17, resid-z 0.67 [quiet], 1d 0.13%, |z20|=1.91; 1y-pct=100
- sp500 [INDICES]: last 7753.15, z20 1.88, zc -0.06, resid-z 0.23 [quiet], 1d -0.06%, |z20|=1.88; 1y-pct=99
- dow_jones [INDICES]: last 53967.51, z20 1.63, zc -0.14, resid-z 0.74 [quiet], 1d -0.13%, |z20|=1.63; 1y-pct=98
- comex_copper [COMMODITIES]: last 6.65, z20 1.52, zc 0.35, resid-z 0.40 [quiet], 1d 0.78%, |z20|=1.52; 1y-pct=98; co-occur[metal_copper] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 68.00, z20 -1.48, zc n/a, resid-z n/a [quiet], 1d 1.50%, GSR<75 (extreme low)
- russell_2000 [INDICES]: last 3016.94, z20 1.46, zc -0.46, resid-z -0.51 [quiet], 1d -0.58%, 1y-pct=98
- **Mechanism**: The recent surge in gold and silver prices, driven by safe-haven demand and uncertainty over US inflation data, has led to a co-movement in monetary metals. This, in turn, has triggered a global risk-on sentiment, causing equity indices such as Stoxx 50, CAC 40, and DAX to rise. The VALID gold_silver_comove channel and metal_copper_channel have facilitated this transmission.
- **Gap**: No gap: The big raw move in gold and silver is largely priced, with resid_z values of 1.08 and 1.16, respectively, indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian metal index, Nifty Metal, has reacted to the surge in global metal prices, while the Nifty Midcap 100 has also moved in tandem with the DAX. The Nifty 50, however, is yet to react fully to the global risk-on sentiment.
- Watch next: nifty_metal (up) — reacted; rho=0.478 via comex_silver, z20=1.78
- Watch next: nifty_midcap_100 (up) — reacted; rho=0.503 via dax, z20=1.64
- Watch next: nifty_50 (up) — not yet - watch; rho=0.501 via cac_40, z20=0.73
- **India receivers**: nifty_midcap_100 (rho 0.503, z 1.64); nifty_50 (rho 0.501, z 0.73); nifty_metal (rho 0.478, z 1.78)
- Source: Q1 Results Today Live:  Siemens, Zydus Lifesciences, MRF, RVNL, PI Industries, Manappuram Finance, NBCC, Kalpataru, Swan Defence, Bata, Gujarat Energy, KPI Green to announce Q1 results, Vi, Bosch, Hindustan Copper, Info Edge shares gain after Q1, Zee, Bharat Forge in red — BusinessLine Mkts, 2026-08-11. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-siemens-zydus-lifescience-mrf-rvnl-pi-industries-manappuram-finance-nbcc-kalpataru-swan-defence-bata-gujarat-energy-kpi-green-vi-bosch-zee-results-11-august-2026/article71327946.ece
- Source: US Stock Market: JP Morgan raises S&P 500 year-end target to 8,000 on AI, earnings optimism — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stock-market-jp-morgan-raises-sp-500-year-end-target-to-8000-on-ai-earnings-optimism/articleshow/133142288.cms
- Source: Gold prices rise Rs 6,600/10g in 3 days; silver jumps Rs 16,200/kg ahead of US inflation data. Big rally brewing? — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/commodities/news/gold-prices-rise-rs-6600/10g-in-3-days-silver-jumps-rs-16200/kg-ahead-of-us-inflation-data-big-rally-brewing/articleshow/133141863.cms
- Historical analogues: 2024-11-26 (d=0.91), 2025-10-31 (d=0.93), 2024-10-09 (d=0.99)

### [AMBER 5.14] cross-asset · 4 series ↑
- dyn_bond [EQUITIES]: last 90.40, z20 -1.48, zc -1.38, resid-z -0.39 [quiet], 1d -0.42%, 1y-pct=0
- ust_30y [RATES]: last 5.19, z20 0.77, zc -0.71, resid-z -0.57 [quiet], 1d -0.57%, 1y-pct=98
- tips_10y_real [RATES]: last 2.40, z20 0.25, zc -0.77, resid-z -0.36 [quiet], 1d -1.23%, 1y-pct=95
- ust_10y [RATES]: last 4.65, z20 0.23, zc -0.86, resid-z -0.43 [quiet], 1d -0.85%, 1y-pct=96
- **Mechanism**: The recent move in bond yields and equities can be attributed to the pricing of the State Bank of India's dollar bond issue, which has led to a repricing of risk in the market. The move is largely priced, with resid_z values indicating that the unexplained component of the move is relatively small. The VALID gold_silver_comove and metal_copper_channel suggest that the move may have implications for Indian metal equities.
- **Gap**: No gap: The move is largely priced, with small resid_z values indicating that the unexplained component of the move is relatively small.
- **India take**: The Indian instrument that expresses this move is the 10-year Government of India bond yield, which may react to the repricing of risk in the global market. However, the INR may not weaken significantly due to the WEAK inr_oil_channel and dxy_inr_channel.
- Watch next: dyn_bond (down) — already moved; Pricing of SBI's dollar bond issue
- Watch next: ust_30y (up) — already moved; Repricing of risk in the market
- Source: State Bank of India taps dollar bond market with five-year issue: Report — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/bonds/state-bank-of-india-taps-dollar-bond-market-with-five-year-issue-report/articleshow/133141420.cms
- Source: State Bank of India taps dollar bond market with five-year issue — BusinessLine Mkts, 2026-08-11. https://www.thehindubusinessline.com/markets/state-bank-of-india-taps-dollar-bond-market-with-five-year-issue/article71330917.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

### [AMBER 4.34] dyn_tatatech_ns ↑
- dyn_tatatech_ns [EQUITIES]: last 864.90, z20 2.34, zc -0.50, resid-z 0.15 [quiet], 1d -1.62%, |z20|=2.34; 1y-pct=99
- **Mechanism**: The recent surge in dyn_tatatech_ns is largely priced, with a small resid_z of 0.15, indicating that the move is mostly explained by factor exposures. The metal_copper_channel, which is currently valid, may provide a mechanism for this move to propagate, given the global copper leads Indian metal equities. However, the lack of a strong channel connecting dyn_tatatech_ns to other assets limits the potential for further propagation.
- **Gap**: No gap: the move in dyn_tatatech_ns is largely priced, with a small resid_z and no clear dislocation from historical analogues
- **India take**: Indian instruments such as dyn_tataelxsi_ns and nifty_it have already reacted to the move in dyn_tatatech_ns, given their correlations of 0.467 and 0.461, respectively. Further reaction is unlikely, given the priced nature of the move.
- Watch next: dyn_tataelxsi_ns (up) — already moved; rho=0.467 with dyn_tatatech_ns
- **India receivers**: dyn_tataelxsi_ns (rho 0.467, z 1.44); nifty_it (rho 0.461, z 1.33)
- Source: Tata Consumer Share Price Live Updates: Tata Consumer's Current Market Position — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tata-consumer-share-price-live-updates-11-aug-2026/liveblog/133140823.cms
- Source: Titan shares: Is the Tata Group stock an attractive buy after Q1FY27 results? — Mint Markets, 2026-08-10. https://www.livemint.com/market/stock-market-news/titan-shares-is-the-tata-group-stock-an-attractive-buy-after-q1fy27-results-11786352452848.html
- Source: Tata Technologies among 5 stocks flashing bullish signals. Upside on cards? — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/news/tata-technologies-among-5-stocks-flashing-bullish-signals-upside-on-cards/slideshow/133080114.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

### [AMBER 4.32] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.61, z20 1.32, zc n/a, resid-z n/a [quiet], 1d 0.39%, 52-wk extreme (pct=98); 1y-pct=98
- **Mechanism**: The midcap_largecap_ratio has risen, indicating a potential shift in market sentiment towards midcaps. This move is priced, with a resid_z of None, suggesting that the move is largely explained by factor exposures. The valid gold_silver_comove and metal_copper_channel may influence the transmission of this move to Indian markets.
- **Gap**: No gap: the move is priced with a resid_z of None, indicating that the current price reflects the known factors
- **India take**: The Nifty Midcap 100 and Dyn PC Jeweller have already reacted to the midcap_largecap_ratio move, while Dyn Bharat Coal remains quiet. The Indian market may see further adjustments in midcap stocks.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to midcap_largecap_ratio move
- **India receivers**: nifty_midcap_100 (rho 0.535, z 1.64); dyn_bharatcoal_ns (rho 0.468, z -0.89); dyn_pcjeweller_ns (rho 0.423, z 1.66)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [AMBER 4.3] dyn_cupid_ns ↑
- dyn_cupid_ns [EQUITIES]: last 270.87, z20 2.30, zc 0.60, resid-z 0.20 [quiet], 1d 2.43%, |z20|=2.30; 1y-pct=100
- **Mechanism**: The recent surge in Cupid's Q1 FY27 profit, which tripled to Rs 44 crore, and the company's raised revenue and profit guidance for FY27, may have triggered a positive response in the stock. However, the stock's quiet move, with a low resid_z of 0.02, suggests that the move is largely priced in. The VALID metal_copper_channel and the company's strong financial performance may be contributing to the stock's upward momentum.
- **Gap**: No gap: the stock's move is largely priced in, with a low resid_z of 0.02 and a strong financial performance
- **India take**: The Indian instrument that expresses this move is the Nifty Midcap 100, which has already reacted with a rho of 0.357 via dyn_cupid_ns. The stock's strong financial performance and the VALID metal_copper_channel may continue to support the Nifty Midcap 100's upward momentum.
- Watch next: nifty_midcap_100 (up) — already moved; rho=0.357 via dyn_cupid_ns
- Source: Cupid shares fall 2% even as Q1 profit jumps 3x. What’s ahead for multibagger stock that rose 680% in a year? — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/news/cupid-shares-fall-2-even-as-q1-profit-jumps-3x-whats-ahead-for-multibagger-stock-that-rose-680-in-a-year/articleshow/133085241.cms
- Source: Q1 Results Highlights: BEML loss narrows to ₹27 cr, Eveready profit up 22%, Aditya Birla Fashion loss widens to ₹249 cr, Cupid profit nearly triples, Ceigall up 35% — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/stock-markets/q1-results-today-live-updates-delhivery-anant-raj-apollo-micro-systems-akums-drugs-pharma-aditya-birla-fashion-ceigall-pnc-infratech-oswal-pumps-results-08-august-2026/article71320548.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-06 (d=0.01), 2025-07-24 (d=0.02)

### [AMBER 4.22] dyn_bac ↑
- dyn_bac [EQUITIES]: last 63.88, z20 2.22, zc 0.79, resid-z -0.22 [quiet], 1d 1.12%, |z20|=2.22; 1y-pct=100
- **Mechanism**: The recent move in dyn_bac is largely priced, with a small resid_z of -0.33, suggesting that the market has already accounted for the factor exposures. The historical analogues suggest a potential positive outcome for dyn_bac and sp500 in the next 20 days, with median returns of 9.68% and 3.69%, respectively. The VALID metal_copper_channel and gold_silver_comove channels may also contribute to the propagation of this move.
- **Gap**: No gap: the move in dyn_bac is largely priced, with a small resid_z and a high z20 level
- **India take**: The Indian instrument dyn_cupid_ns has already reacted, with a rho of 0.378 via dyn_bac and a z20 of 2.28. Further reaction in Indian metal equities may be expected via the metal_copper_channel.
- Watch next: dyn_ms (up) — not yet - watch; historically leads dyn_bac by 2d
- **India receivers**: dyn_cupid_ns (rho 0.378, z 2.3)
- Source: America's $4 Billion Wind Retreat Is a Bet on Permanently Cheap Gas — OilPrice, 2026-08-10. https://oilprice.com/Alternative-Energy/Wind-Power/Americas-4-Billion-Wind-Retreat-Is-a-Bet-on-Permanently-Cheap-Gas.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

### [AMBER 4.22] dyn_heromotoco_ns ↑
- dyn_heromotoco_ns [EQUITIES]: last 5906.00, z20 2.22, zc 0.41, resid-z 1.50 [unexplained], 1d 0.78%, |z20|=2.22
- **Mechanism**: dyn_heromotoco_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_havells_ns (rho 0.452 via dyn_heromotoco_ns, z 1.03, reacted); nifty_midcap_100 (rho 0.386 via dyn_heromotoco_ns, z 1.64, reacted); nifty_50 (rho 0.355 via dyn_heromotoco_ns, z 0.73, quiet)
- **India receivers**: dyn_havells_ns (rho 0.452, z 1.03); nifty_midcap_100 (rho 0.386, z 1.64); nifty_50 (rho 0.355, z 0.73)
- Source: Hero MotoCorp gains speed as premium bikes, EVs fuel Q1 — Mint Markets, 2026-08-10. https://www.livemint.com/market/mark-to-market/hero-motocorp-q1fy27-earnings-stock-margin-ev-growth-11786338356204.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-22 (d=0.03), 2025-07-09 (d=0.04)

### [AMBER 4.04] dyn_ohi ↓
- dyn_ohi [EQUITIES]: last 47.39, z20 -2.04, zc -1.62, resid-z -0.48 [moved], 1d -2.21%, |z20|=2.04
- **Mechanism**: dyn_ohi ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Paytm shares recover 410% from 2024 low, but will long-awaiting IPO investors finally see redemption? — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/stocks/news/paytm-shares-recover-410-from-2024-low-but-will-long-awaiting-ipo-investors-finally-see-redemption/articleshow/133142649.cms
- Source: Dhoot, Milky Mist or Molbio? What should investors pick in Rs 7,000 crore IPO rush this week — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/ipos/fpos/dhoot-milky-mist-or-molbio-what-should-investors-pick-in-rs-7000-crore-ipo-rush-this-week/articleshow/133142167.cms
- Source: Retail investors make Rs 18,000 crore bold contra bet on 6 falling bluechip stocks. Will it pay off? — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/stocks/news/retail-investors-make-rs-18000-crore-bold-contra-bet-on-6-falling-bluechip-stocks-will-it-pay-off/articleshow/133142033.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2024-10-15 (d=0.09)

## Watchlist (below surfacing floor)
dyn_coin ↓ (3.27), dyn_tech ↑ (3.09), dyn_pltr ↑ (2.76), dyn_hdb ↓ (2.74), dyn_idbi_ns ↓ (2.61), usd_mxn ↓ (2.32), dyn_atherenerg_ns ↑ (2.27), dyn_icicigi_bo ↓ (2.25), usd_cny ↓ (1.99), bovespa ↓ (1.93), asx_200 ↑ (1.79), nifty_metal ↑ (1.78)

## India macro
- nifty_50: 24474.2500 (1d -0.45%, z20 0.73, flag none)
- nifty_midcap_100: 63810.0508 (1d -0.06%, z20 1.64, flag amber)
- usd_inr: 95.3875 (1d 0.19%, z20 -0.99, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6072 (1d 0.39%, z20 1.32, flag amber)
- Next India prints: NSDL FPI flows T-0d · India CPI T-1d · India WPI T-3d · RBI Weekly Statistical Supplement T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 79.7 — "Stock recommendations for 11 August from MarketSmith India"
- COALINDIA.NS (COAL INDIA LTD) score 79.1 — "Stock recommendations for 11 August from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 78.8 — "Stock recommendations for 11 August from MarketSmith India"
- INDIANB.NS (INDIAN BANK) score 62.2 — "From Gift Nifty to Oil prices, Asian banking stocks rally: 8 key things that changed for I"
- BAC (Bank of America Corporation) score 50.9 — "From Gift Nifty to Oil prices, Asian banking stocks rally: 8 key things that changed for I"
- TECHM.NS (TECH MAHINDRA LIMITED) score 45.3 — "Tech Mahindra Share Price Live Updates: Tech Mahindra Sees Positive Movement Today"
- HDB (HDFC Bank Limited) score 45.2 — "From Gift Nifty to Oil prices, Asian banking stocks rally: 8 key things that changed for I"
- COIN (Coinbase Global, Inc.) score 44.5 — "Nikkei, Kospi to US stocks: Global equity heatmap you must know before the opening bell of"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 44.2 — "Tech Mahindra Share Price Live Updates: Tech Mahindra Sees Positive Movement Today"
- TECH (Bio-Techne Corp) score 42.9 — "Tech Mahindra Share Price Live Updates: Tech Mahindra Sees Positive Movement Today"
- IDBI.NS (IDBI BANK LIMITED) score 42.9 — "From Gift Nifty to Oil prices, Asian banking stocks rally: 8 key things that changed for I"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 42.9 — "From Gift Nifty to Oil prices, Asian banking stocks rally: 8 key things that changed for I"
- OHI (Omega Healthcare Investors, In) score 42.6 — "Adani Group stocks jump up to 3% after US judge drops criminal case against Gautam Adani. "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 42.4 — "From Gift Nifty to Oil prices, Asian banking stocks rally: 8 key things that changed for I"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 34.2 — "Colombia Revives Oil And Gas After Four-Year Renewable Energy Push"
- CHKP (Check Point Software Technolog) score 33.0 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 1"
- LTH (Life Time Group Holdings, Inc.) score 28.9 — "TRUMP EXTENDS JONES ACT SHIPPING WAIVER President Trump extended the Jones Act shipping wa"
- 301077.SZ (CHINASTARS) score 21.8 — "CHINA SAYS LAUNCH OF LONG MARCH 7 ROCKET FAILED - XINHUA"
- BOND (PIMCO Active Bond Exchange-Tra) score 20.9 — "State Bank of India taps dollar bond market with five-year issue"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 13.6 — "Bharat Forge among 4 F&O stocks with sharp rise in futures open interest"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 12.3 — "Nvidia teams with Wall Street firms to help finance $500 billion for AI infrastructure"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 12.0 — "Tata Consumer Share Price Live Updates: Tata Consumer's Current Market Position"
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.9 — "Good news for stock-market bulls: Corporate earnings growth is no longer being driven just"
- PCJEWELLER.NS (PC JEWELLER LTD) score 11.0 — "Shankesh Jewellers IPO price band fixed at  ₹88- ₹93 per share; issue date, key details he"
- JIOFIN.BO (Jio Financial Services Limited) score 9.7 — "NVDA - NVIDIA TEAMS WITH WALL STREET ON $500BN AI FINANCING PUSH Nvidia is partnering with"
- MS (Morgan Stanley) score 9.5 — "US Stock Market: JP Morgan raises S&P 500 year-end target to 8,000 on AI, earnings optimis"
- AAPL (Apple Inc.) score 8.6 — "AAPL - APPLE REPORTEDLY SCRAPS ALL-GLASS IPHONE Apple has canceled its planned 20th-annive"
- META (Meta) score 8.4 — "Q1 Results Today Highlights: Bharat Forge shares tank after Q1 loss, Kwality Pharma, Ramco"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 8.0 — "Bharat Forge among 4 F&O stocks with sharp rise in futures open interest"
- VT (Vanguard Total World Stock Ind) score 7.7 — "GLENCORE'S EXPOSURE TO IRON ORE TRADER RADIANT WORLD MORE THAN $500 MILLION, SOURCES SAY"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 7.6 — "NVDA - NVIDIA TEAMS WITH WALL STREET ON $500BN AI FINANCING PUSH Nvidia is partnering with"
- NVDA (NVIDIA Corporation) score 6.9 — "Nvidia teams with Wall Street firms to help finance $500 billion for AI infrastructure"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.8 — "Adani Group stocks jump up to 3% after US judge drops criminal case against Gautam Adani. "
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.9 — "ICICI Bank Share Price Live Updates: ICICI Bank's Price Movement Indicates Positive Trend"
- GOOGL (Alphabet) score 3.8 — "US Stock Market: Berkshire steps up buybacks, boosts Alphabet stake as cash falls"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 3.4 — "Tata Consumer Share Price Live Updates: Tata Consumer's Current Market Position"
- PLTR (Palantir Technologies Inc.) score 3.4 — "Palantir’s stock stages best week since 2024 — showing it’s no longer an AI loser"
- AMZN (Amazon.com, Inc.) score 2.4 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- CUPID.NS (CUPID LIMITED) score 2.2 — "Q1 Results Highlights: BEML loss narrows to ₹27 cr, Eveready profit up 22%, Aditya Birla F"
- HEROMOTOCO.NS (HERO MOTOCORP LIMITED) score 1.6 — "Hero MotoCorp gains speed as premium bikes, EVs fuel Q1"

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