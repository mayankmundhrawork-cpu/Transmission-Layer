# Transmission Layer — board brief · 2026-08-11 07:34Z

data as of **2026-08-11** · 98 series · 5 red / 34 amber · 8 events surfaced (17 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.291, 2d in regime; vol-pct 0.4, breadth-off 0.182, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.37, corr60 -0.39, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.81, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.3, corr60 0.34, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.16, corr60 -0.07, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.79, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.08, corr60 -0.03, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.41, corr60 -0.25, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.0, corr60 0.16, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.492** (n=1132) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.82** (n=2389) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.97] cross-asset · 11 series ↑
- comex_gold [COMMODITIES]: last 4417.70, z20 2.97, zc 0.72, resid-z 1.08 [quiet], 1d 1.28%, |z20|=2.97; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 64.57, z20 2.38, zc -0.30, resid-z -1.48 [quiet], 1d -0.83%, |z20|=2.38; co-occur[gold_silver] same-direction (channel VALID)
- dyn_vt [EQUITIES]: last 160.99, z20 1.94, zc -0.20, resid-z 0.29 [quiet], 1d -0.19%, 1y-pct=99
- stoxx_50 [INDICES]: last 6546.82, z20 1.94, zc 0.21, resid-z 0.86 [quiet], 1d 0.17%, |z20|=1.94; 1y-pct=100
- sp500 [INDICES]: last 7753.15, z20 1.88, zc -0.06, resid-z 0.23 [quiet], 1d -0.06%, |z20|=1.88; 1y-pct=99
- cac_40 [INDICES]: last 8730.25, z20 1.76, zc 0.07, resid-z 1.18 [quiet], 1d 0.05%, |z20|=1.76; 1y-pct=100
- dow_jones [INDICES]: last 53967.51, z20 1.63, zc -0.14, resid-z 0.74 [quiet], 1d -0.13%, |z20|=1.63; 1y-pct=98
- dax [INDICES]: last 26329.40, z20 1.63, zc 0.03, resid-z 0.54 [quiet], 1d 0.02%, |z20|=1.63; 1y-pct=100
- comex_copper [COMMODITIES]: last 6.64, z20 1.47, zc 0.29, resid-z 0.40 [quiet], 1d 0.66%, 1y-pct=98
- russell_2000 [INDICES]: last 3016.94, z20 1.46, zc -0.46, resid-z -0.51 [quiet], 1d -0.58%, 1y-pct=98
- gold_silver_ratio [DERIVED]: last 68.42, z20 -1.09, zc n/a, resid-z n/a [quiet], 1d 2.13%, GSR<75 (extreme low)
- **Mechanism**: The recent surge in gold prices, as seen in COMEX gold and COMEX silver, is driven by a combination of factors including a firm spot demand and a rise in gold futures. This move is also reflected in the Indian market, with gold prices increasing across all cities. The VALID gold_silver_comove channel and the metal_copper_channel suggest a co-move of monetary metals and a potential lead of global copper to Indian metal equities.
- **Gap**: No gap: the big raw move in gold prices is largely priced, with a small resid_z of 1.08, indicating that the move is mostly explained by factor exposures
- **India take**: The Indian instruments such as NIFTY METAL and NIFTY MIDCAP 100 have already reacted to the move in COMEX silver and CAC 40, respectively. The rise in gold prices in India is also reflected in the increase in gold futures, with prices rising to ₹1.54 lakh per 10 grams.
- Watch next: nifty_metal (up) — reacted; already reacted to the move in COMEX silver
- Watch next: nifty_midcap_100 (up) — reacted; already reacted to the move in CAC 40
- **India receivers**: nifty_50 (rho 0.494, z 0.64); nifty_metal (rho 0.479, z 1.44); nifty_midcap_100 (rho 0.479, z 1.52)
- Source: Today’s Gold Rate in India August 11: Gold prices up in Delhi, Mumbai, Kolkata, Bengaluru, Ahmedabad — BusinessLine Mkts, 2026-08-11. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-mumbai-chennai-ahmedabad-delhi-hyderabad-bengaluru-kolkata-gold-rates-august-11-2026/article71331334.ece
- Source: Gold futures rise to ₹1.54 lakh/10 gm on spot demand — BusinessLine Mkts, 2026-08-11. https://www.thehindubusinessline.com/markets/commodities/gold-futures-rise-to-154-lakh10-gm-on-spot-demand/article71331152.ece
- Source: Forget gold and stocks: Nvidia CEO Jensen Huang aims to make chips an investable asset, lines up $500 bn in financing — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/us-stocks/news/forget-gold-and-stocks-nvidia-ceo-jensen-huang-aims-to-make-chips-an-investable-asset-lines-up-500-bn-in-financing/articleshow/133142905.cms
- Historical analogues: 2024-11-26 (d=0.91), 2025-10-31 (d=0.93), 2024-10-09 (d=0.99)

### [AMBER 6.29] commodities · 2 series ↑
- wti [COMMODITIES]: last 83.95, z20 0.45, zc 0.64, resid-z 1.51 [unexplained], 1d 2.22%, 1-session move +2.22% ≥ 1.5%
- brent [COMMODITIES]: last 89.60, z20 0.37, zc 0.59, resid-z 1.52 [unexplained], 1d 2.14%, 1-session move +2.14% ≥ 1.5%
- **Mechanism**: The recent surge in crude oil prices, led by a 2.22% increase in WTI and a 2.14% increase in Brent, is driven by supply concerns following drone attacks on Libya's Zawiya oil hub. This move is unexplained by factor exposures, with resid_z values of 1.51 and 1.52 for WTI and Brent, respectively. The RISK_ON regime and VALID gold_silver_comove and metal_copper_channel suggest that the market is pricing in inflationary pressures and potential rotations in the monetary metals complex.
- **Gap**: No gap: the big raw move in crude oil prices is largely priced, with small resid_z values indicating that the move is mostly explained by supply concerns and inflation fears
- **India take**: Indian equities, such as the Nifty Midcap 100, have already reacted to the surge in crude oil prices, while Indian metal equities may follow suit due to the VALID metal_copper_channel. The INR may also weaken due to higher import bills, although the WEAK inr_oil_channel suggests that this relationship is not currently driving price action.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to WTI move
- **India receivers**: nifty_midcap_100 (rho -0.435, z 1.52); dyn_bharatcoal_ns (rho -0.377, z -1.0)
- Source: Sensex today | Stock Market Live: Noon trade - Sensex falls over 450 points as elevated crude oil prices weigh on equities — BusinessLine Mkts, 2026-08-11. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-11-august-2026/article71328121.ece
- Source: India bonds skid as crude soars, Treasuries fall — BusinessLine Mkts, 2026-08-11. https://www.thehindubusinessline.com/markets/india-bonds-skid-as-crude-soars-treasuries-fall/article71331293.ece
- Source: Libya Weighs Force Majeure After Drone Attacks on Zawiya Oil Hub — OilPrice, 2026-08-11. https://oilprice.com/Latest-Energy-News/World-News/Libya-Weighs-Force-Majeure-After-Drone-Attacks-on-Zawiya-Oil-Hub.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

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

### [RED 4.62] dyn_cupid_ns ↑
- dyn_cupid_ns [EQUITIES]: last 276.76, z20 2.62, zc 1.15, resid-z 1.54 [unexplained], 1d 4.65%, |z20|=2.62; 1y-pct=100
- **Mechanism**: The recent surge in Cupid's Q1 FY27 profit, which tripled to Rs 44 crore, and the company's raised revenue and profit guidance for FY27, may have triggered a positive response in the stock. However, the stock's quiet move, with a low resid_z of 0.02, suggests that the move is largely priced in. The VALID metal_copper_channel and the company's strong financial performance may be contributing to the stock's upward momentum.
- **Gap**: No gap: the stock's move is largely priced in, with a low resid_z of 0.02 and a strong financial performance
- **India take**: The Indian instrument that expresses this move is the Nifty Midcap 100, which has already reacted with a rho of 0.357 via dyn_cupid_ns. The stock's strong financial performance and the VALID metal_copper_channel may continue to support the Nifty Midcap 100's upward momentum.
- Watch next: nifty_midcap_100 (up) — already moved; rho=0.357 via dyn_cupid_ns
- Source: Cupid shares fall 2% even as Q1 profit jumps 3x. What’s ahead for multibagger stock that rose 680% in a year? — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/news/cupid-shares-fall-2-even-as-q1-profit-jumps-3x-whats-ahead-for-multibagger-stock-that-rose-680-in-a-year/articleshow/133085241.cms
- Source: Q1 Results Highlights: BEML loss narrows to ₹27 cr, Eveready profit up 22%, Aditya Birla Fashion loss widens to ₹249 cr, Cupid profit nearly triples, Ceigall up 35% — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/stock-markets/q1-results-today-live-updates-delhivery-anant-raj-apollo-micro-systems-akums-drugs-pharma-aditya-birla-fashion-ceigall-pnc-infratech-oswal-pumps-results-08-august-2026/article71320548.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-06 (d=0.01), 2025-07-24 (d=0.02)

### [AMBER 4.3] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.61, z20 1.30, zc n/a, resid-z n/a [quiet], 1d 0.38%, 52-wk extreme (pct=98); 1y-pct=98
- **Mechanism**: The midcap_largecap_ratio has risen, indicating a potential shift in market sentiment towards midcaps. This move is priced, with a resid_z of None, suggesting that the move is largely explained by factor exposures. The valid gold_silver_comove and metal_copper_channel may influence the transmission of this move to Indian markets.
- **Gap**: No gap: the move is priced with a resid_z of None, indicating that the current price reflects the known factors
- **India take**: The Nifty Midcap 100 and Dyn PC Jeweller have already reacted to the midcap_largecap_ratio move, while Dyn Bharat Coal remains quiet. The Indian market may see further adjustments in midcap stocks.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to midcap_largecap_ratio move
- **India receivers**: nifty_midcap_100 (rho 0.533, z 1.52); dyn_bharatcoal_ns (rho 0.466, z -1.0); dyn_pcjeweller_ns (rho 0.419, z 1.09)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [AMBER 4.28] dyn_tatatech_ns ↑
- dyn_tatatech_ns [EQUITIES]: last 862.30, z20 2.28, zc -0.59, resid-z -0.74 [quiet], 1d -1.92%, |z20|=2.28; 1y-pct=99
- **Mechanism**: The recent surge in dyn_tatatech_ns is largely priced, with a small resid_z of 0.15, indicating that the move is mostly explained by factor exposures. The metal_copper_channel, which is currently valid, may provide a mechanism for this move to propagate, given the global copper leads Indian metal equities. However, the lack of a strong channel connecting dyn_tatatech_ns to other assets limits the potential for further propagation.
- **Gap**: No gap: the move in dyn_tatatech_ns is largely priced, with a small resid_z and no clear dislocation from historical analogues
- **India take**: Indian instruments such as dyn_tataelxsi_ns and nifty_it have already reacted to the move in dyn_tatatech_ns, given their correlations of 0.467 and 0.461, respectively. Further reaction is unlikely, given the priced nature of the move.
- Watch next: dyn_tataelxsi_ns (up) — already moved; rho=0.467 with dyn_tatatech_ns
- **India receivers**: dyn_tataelxsi_ns (rho 0.466, z 1.44); nifty_it (rho 0.457, z 1.39)
- Source: Tata Consumer Share Price Live Updates: Tata Consumer's Current Market Position — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tata-consumer-share-price-live-updates-11-aug-2026/liveblog/133140823.cms
- Source: Titan shares: Is the Tata Group stock an attractive buy after Q1FY27 results? — Mint Markets, 2026-08-10. https://www.livemint.com/market/stock-market-news/titan-shares-is-the-tata-group-stock-an-attractive-buy-after-q1fy27-results-11786352452848.html
- Source: Tata Technologies among 5 stocks flashing bullish signals. Upside on cards? — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/news/tata-technologies-among-5-stocks-flashing-bullish-signals-upside-on-cards/slideshow/133080114.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

### [AMBER 4.22] dyn_bac ↑
- dyn_bac [EQUITIES]: last 63.88, z20 2.22, zc 0.79, resid-z -0.22 [quiet], 1d 1.12%, |z20|=2.22; 1y-pct=100
- **Mechanism**: The recent move in dyn_bac is largely priced, with a small resid_z of -0.33, suggesting that the market has already accounted for the factor exposures. The historical analogues suggest a potential positive outcome for dyn_bac and sp500 in the next 20 days, with median returns of 9.68% and 3.69%, respectively. The VALID metal_copper_channel and gold_silver_comove channels may also contribute to the propagation of this move.
- **Gap**: No gap: the move in dyn_bac is largely priced, with a small resid_z and a high z20 level
- **India take**: The Indian instrument dyn_cupid_ns has already reacted, with a rho of 0.378 via dyn_bac and a z20 of 2.28. Further reaction in Indian metal equities may be expected via the metal_copper_channel.
- Watch next: dyn_ms (up) — not yet - watch; historically leads dyn_bac by 2d
- **India receivers**: dyn_cupid_ns (rho 0.374, z 2.62)
- Source: America's $4 Billion Wind Retreat Is a Bet on Permanently Cheap Gas — OilPrice, 2026-08-10. https://oilprice.com/Alternative-Energy/Wind-Power/Americas-4-Billion-Wind-Retreat-Is-a-Bet-on-Permanently-Cheap-Gas.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

### [AMBER 4.04] dyn_ohi ↓
- dyn_ohi [EQUITIES]: last 47.39, z20 -2.04, zc -1.62, resid-z -0.48 [moved], 1d -2.21%, |z20|=2.04
- **Mechanism**: The recent decline in dyn_ohi is largely priced, with a small resid_z of -0.48, indicating that the move is mostly explained by factor exposures. The valid vix_equity_inverse channel suggests that the vol spike is leading to an equity drawdown. The metal_copper_channel also indicates that global copper leads Indian metal equities, which could be a contributing factor to the decline in dyn_ohi.
- **Gap**: No gap: the decline in dyn_ohi is largely priced, with a small resid_z and a low r2 value, indicating that the move is mostly explained by factor exposures
- **India take**: The Indian instrument that expresses this move is Vedanta, which could see potential outflows due to the Nifty September rejig. However, it has not reacted yet.
- Watch next: VEDANTA (down) — not yet - watch; potential outflows due to Nifty September rejig
- Source: 4 Vedanta Group stocks to see inflows worth $160 million in Nifty September rejig. What investors must know — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/stocks/news/4-vedanta-group-stocks-to-see-inflows-worth-160-million-in-nifty-september-rejig-what-investors-must-know/articleshow/133143084.cms
- Source: Paytm shares recover 410% from 2024 low, but will long-awaiting IPO investors finally see redemption? — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/stocks/news/paytm-shares-recover-410-from-2024-low-but-will-long-awaiting-ipo-investors-finally-see-redemption/articleshow/133142649.cms
- Source: Dhoot, Milky Mist or Molbio? What should investors pick in Rs 7,000 crore IPO rush this week — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/ipos/fpos/dhoot-milky-mist-or-molbio-what-should-investors-pick-in-rs-7000-crore-ipo-rush-this-week/articleshow/133142167.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2024-10-15 (d=0.09)

## Watchlist (below surfacing floor)
dyn_coin ↓ (3.27), fx · 2 series ↑ (3.09), dyn_tech ↑ (3.09), dyn_pltr ↑ (2.76), dyn_hdb ↓ (2.74), dyn_idbi_ns ↓ (2.65), dyn_atherenerg_ns ↑ (2.31), dyn_icicigi_bo ↓ (2.22), bovespa ↓ (1.93), usd_cny ↓ (1.83), corn ↑ (1.71), asx_200 ↑ (1.67)

## India macro
- nifty_50: 24449.9004 (1d -0.54%, z20 0.64, flag none)
- nifty_midcap_100: 63740.8008 (1d -0.17%, z20 1.52, flag amber)
- usd_inr: 95.4325 (1d 0.23%, z20 -0.91, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6070 (1d 0.38%, z20 1.30, flag amber)
- Next India prints: NSDL FPI flows T-0d · India CPI T-1d · India WPI T-3d · RBI Weekly Statistical Supplement T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 83.0 — "Coal India Share Price Live Updates: Coal India Ltd News"
- COALINDIA.NS (COAL INDIA LTD) score 82.4 — "Coal India Share Price Live Updates: Coal India Ltd News"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 82.2 — "Coal India Share Price Live Updates: Coal India Ltd News"
- INDIANB.NS (INDIAN BANK) score 60.9 — "From Gift Nifty to Oil prices, Asian banking stocks rally: 8 key things that changed for I"
- BAC (Bank of America Corporation) score 49.8 — "From Gift Nifty to Oil prices, Asian banking stocks rally: 8 key things that changed for I"
- TECHM.NS (TECH MAHINDRA LIMITED) score 45.4 — "Technocraft Ventures IPO Day 3: Issue subscribed 7.35x so far. Check GMP, key dates, revie"
- COIN (Coinbase Global, Inc.) score 44.6 — "Global Market: Mainland Chinese stocks mixed, Hong Kong shares slip as Iran conflict weigh"
- HDB (HDFC Bank Limited) score 44.3 — "From Gift Nifty to Oil prices, Asian banking stocks rally: 8 key things that changed for I"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 44.2 — "Technocraft Ventures IPO Day 3: Issue subscribed 7.35x so far. Check GMP, key dates, revie"
- TECH (Bio-Techne Corp) score 43.0 — "Technocraft Ventures IPO Day 3: Issue subscribed 7.35x so far. Check GMP, key dates, revie"
- OHI (Omega Healthcare Investors, In) score 42.7 — "4 Vedanta Group stocks to see inflows worth $160 million in Nifty September rejig. What in"
- IDBI.NS (IDBI BANK LIMITED) score 42.0 — "From Gift Nifty to Oil prices, Asian banking stocks rally: 8 key things that changed for I"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 42.0 — "From Gift Nifty to Oil prices, Asian banking stocks rally: 8 key things that changed for I"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 41.5 — "From Gift Nifty to Oil prices, Asian banking stocks rally: 8 key things that changed for I"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 35.4 — "Nifty Rejig: BSE to enter Nifty 50, Wipro moves to Nifty Next 50; Hitachi Energy, Polycab "
- CHKP (Check Point Software Technolog) score 35.3 — "Milky Mist IPO Day 1: Issue booked 18% so far. Check GMP, key dates, review, issue details"
- LTH (Life Time Group Holdings, Inc.) score 30.2 — "Molbio Diagnostics IPO Day 2: Issue subscribed 1.75 times so far. Check GMP, size, & other"
- BOND (PIMCO Active Bond Exchange-Tra) score 21.5 — "India bonds skid as crude soars, Treasuries fall"
- 301077.SZ (CHINASTARS) score 21.4 — "CHINA SAYS LAUNCH OF LONG MARCH 7 ROCKET FAILED - XINHUA"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 14.3 — "Coal India Share Price Live Updates: Coal India Ltd News"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 14.1 — "Bajaj Finance Share Price Live Updates: Bajaj Finance News"
- PCJEWELLER.NS (PC JEWELLER LTD) score 12.8 — "PC Jeweller share price jumps 6% as Q1FY27 profit surges 37% YoY, revenue up 21%"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.7 — "Tata Consumer Share Price Live Updates: Tata Consumer's Current Market Position"
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.6 — "Good news for stock-market bulls: Corporate earnings growth is no longer being driven just"
- JIOFIN.BO (Jio Financial Services Limited) score 10.5 — "Jio Financial Services Share Price Live Updates: Jio Financial Services News"
- MS (Morgan Stanley) score 9.3 — "US Stock Market: JP Morgan raises S&P 500 year-end target to 8,000 on AI, earnings optimis"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 8.8 — "Forget gold and stocks: Nvidia CEO Jensen Huang aims to make chips an investable asset, li"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.5 — "Jio Financial Services Share Price Live Updates: Jio Financial Services News"
- AAPL (Apple Inc.) score 8.4 — "AAPL - APPLE REPORTEDLY SCRAPS ALL-GLASS IPHONE Apple has canceled its planned 20th-annive"
- META (Meta) score 8.2 — "Q1 Results Today Highlights: Bharat Forge shares tank after Q1 loss, Kwality Pharma, Ramco"
- NVDA (NVIDIA Corporation) score 7.7 — "Forget gold and stocks: Nvidia CEO Jensen Huang aims to make chips an investable asset, li"
- VT (Vanguard Total World Stock Ind) score 7.6 — "GLENCORE'S EXPOSURE TO IRON ORE TRADER RADIANT WORLD MORE THAN $500 MILLION, SOURCES SAY"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.7 — "Adani Group stocks jump up to 3% after US judge drops criminal case against Gautam Adani. "
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.9 — "ICICI Bank Share Price Live Updates: ICICI Bank's Price Movement Indicates Positive Trend"
- GOOGL (Alphabet) score 3.7 — "US Stock Market: Berkshire steps up buybacks, boosts Alphabet stake as cash falls"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 3.3 — "Tata Consumer Share Price Live Updates: Tata Consumer's Current Market Position"
- PLTR (Palantir Technologies Inc.) score 3.3 — "Palantir’s stock stages best week since 2024 — showing it’s no longer an AI loser"
- HEROMOTOCO.NS (HERO MOTOCORP LIMITED) score 2.6 — "Hero MotoCorp Share Price Live Updates: Hero MotoCorp's Daily Performance"
- AMZN (Amazon.com, Inc.) score 2.4 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- CUPID.NS (CUPID LIMITED) score 2.1 — "Q1 Results Highlights: BEML loss narrows to ₹27 cr, Eveready profit up 22%, Aditya Birla F"

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