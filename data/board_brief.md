# Transmission Layer — board brief · 2026-08-11 22:11Z

data as of **2026-08-11** · 98 series · 9 red / 32 amber · 8 events surfaced (18 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.268, 1d in regime; vol-pct 0.348, breadth-off 0.188, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.37, corr60 -0.39, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.81, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.3, corr60 0.34, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.16, corr60 -0.07, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.75, corr60 -0.79, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.08, corr60 -0.03, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.4, corr60 -0.22, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.01, corr60 0.16, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** bovespa → aud_usd: leads 1d (ccf 0.396, β 0.2381, p 0.0); driver zc -2.34 → expected -0.616%. Type hit-rate 0.815 (n=2507).
- **SETUP** bovespa → usd_mxn: leads 1d (ccf -0.365, β -0.2213, p 0.0); driver zc -2.34 → expected 0.572%. Type hit-rate 0.815 (n=2507).
- **SETUP** ust_10y → eur_usd: leads 1d (ccf -0.282, β -0.1155, p 0.0); driver zc 1.52 → expected -0.174%. Type hit-rate 0.815 (n=2507).
- **SETUP** ust_10y → gbp_usd: leads 1d (ccf -0.275, β -0.1119, p 0.0); driver zc 1.52 → expected -0.168%. Type hit-rate 0.815 (n=2507).
- Track record · residual_reversion: hit-rate **0.491** (n=1134) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.815** (n=2507) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.14] cross-asset · 11 series ↑
- comex_gold [COMMODITIES]: last 4430.50, z20 3.09, zc 0.88, resid-z 0.81 [quiet], 1d 1.58%, |z20|=3.09; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 64.93, z20 2.53, zc -0.10, resid-z -1.45 [quiet], 1d -0.28%, |z20|=2.53; co-occur[gold_silver] same-direction (channel VALID)
- stoxx_50 [INDICES]: last 6553.86, z20 2.01, zc 0.35, resid-z 0.63 [quiet], 1d 0.28%, |z20|=2.01; 1y-pct=100
- dax [INDICES]: last 26392.05, z20 1.74, zc 0.34, resid-z 0.60 [quiet], 1d 0.26%, |z20|=1.74; 1y-pct=100
- cac_40 [INDICES]: last 8717.47, z20 1.67, zc -0.13, resid-z 0.13 [quiet], 1d -0.10%, |z20|=1.67; 1y-pct=99
- dyn_vt [EQUITIES]: last 160.80, z20 1.62, zc -0.11, resid-z 0.13 [quiet], 1d -0.10%, 1y-pct=99
- russell_2000 [INDICES]: last 3026.71, z20 1.58, zc 0.25, resid-z 1.13 [quiet], 1d 0.31%, |z20|=1.58; 1y-pct=99
- sp500 [INDICES]: last 7727.41, z20 1.45, zc -0.38, resid-z 0.97 [quiet], 1d -0.33%, 1y-pct=98
- comex_copper [COMMODITIES]: last 6.63, z20 1.38, zc 0.21, resid-z 0.59 [quiet], 1d 0.47%, 1y-pct=98
- gold_silver_ratio [DERIVED]: last 68.24, z20 -1.26, zc n/a, resid-z n/a [quiet], 1d 1.86%, GSR<75 (extreme low)
- dow_jones [INDICES]: last 53785.19, z20 1.24, zc -0.41, resid-z -0.17 [quiet], 1d -0.35%, 1y-pct=98
- **Mechanism**: The current move in gold and other commodities is driven by market participants awaiting key US inflation figures, which could shape expectations for the Federal Reserve's policy. The VALID gold_silver_comove channel and metal_copper_channel suggest that monetary metals and copper are co-moving, with the gold-silver ratio extremes indicating rotations. The RISK_ON regime and the vix_equity_inverse channel also support this move.
- **Gap**: No gap: the big raw move in gold is largely priced, with a resid_z of 0.81, indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian instruments nifty_metal and nifty_midcap_100 have reacted, with the former driven by the comex_silver price and the latter by the dax index. The nifty_50 is still quiet, with a z20 of 0.72.
- Watch next: comex_gold (up) — already moved; market awaits US inflation data
- Watch next: comex_silver (up) — already moved; co-movement with gold
- **India receivers**: nifty_50 (rho 0.498, z 0.72); nifty_midcap_100 (rho 0.495, z 1.71); nifty_metal (rho 0.475, z 1.33)
- Source: Gold edges lower as markets await key US inflation data — Mint Markets, 2026-08-11. https://www.livemint.com/market/gold-edges-lower-as-markets-await-key-us-inflation-data-11786474118005.html
- Source: Gold Nears Two-Month High Ahead of Wednesday's CPI Report — OilPrice, 2026-08-11. https://oilprice.com/Metals/Gold/Gold-Nears-Two-Month-High-Ahead-of-Wednesdays-CPI-Report.html
- Source: Gold edges higher near two-month peak ahead of US inflation data — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/gold-edges-higher-near-two-month-peak-ahead-of-us-inflation-data/articleshow/133159810.cms
- Historical analogues: 2024-11-26 (d=0.91), 2025-10-31 (d=0.93), 2024-10-09 (d=0.99)

### [AMBER 6.16] commodities · 2 series ↑
- wti [COMMODITIES]: last 83.40, z20 0.33, zc 0.45, resid-z 0.24 [quiet], 1d 1.55%, 1-session move +1.55% ≥ 1.5%
- brent [COMMODITIES]: last 89.23, z20 0.30, zc 0.47, resid-z 0.28 [quiet], 1d 1.72%, 1-session move +1.72% ≥ 1.5%
- **Mechanism**: The recent surprise build in US crude oil inventories has led to a moderate increase in oil prices, with WTI and Brent crude rising by 1.55% and 1.60% respectively. This move is largely priced in, given the relatively low resid_z values of 0.24 and 0.25 for WTI and Brent respectively. The RISK_ON regime and VALID gold_silver_comove and metal_copper_channel suggest that the market is positioned for further risk-on moves, but the weak inr_oil_channel and dxy_inr_channel may limit the transmission of oil price moves to Indian markets.
- **Gap**: No gap: the move in oil prices is largely priced in, with low resid_z values and a moderate price increase
- **India take**: Indian markets, such as the nifty_midcap_100, have already reacted to the oil price move, while dyn_bharatcoal_ns and midcap_largecap_ratio have also moved in response to the oil price increase. However, the weak inr_oil_channel may limit further transmission of oil price moves to Indian markets.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to oil price move via wti, rho=-0.433
- **India receivers**: nifty_midcap_100 (rho -0.433, z 1.71); dyn_bharatcoal_ns (rho -0.378, z -1.02); midcap_largecap_ratio (rho -0.351, z 1.46)
- Source: US Crude Oil Inventories See Surprise Build: API — OilPrice, 2026-08-11. https://oilprice.com/Latest-Energy-News/World-News/US-Crude-Oil-Inventories-See-Surprise-Build-API.html
- Source: Why the US-Iran war continues to disrupt oil markets — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/commodities/news/why-the-us-iran-war-continues-to-disrupt-oil-markets/articleshow/133163454.cms
- Source: U.S. SAYS HORMUZ OIL FLOWS ARE RECOVERING Energy Secretary Chris Wright says nearly 9 million barrels of oil a day are now moving through the Strait of Hormuz. Including pipelines, regional oil flows have reached roughly 15 million barrels daily, suggesting supply pressures — DeItaone, 2026-08-11. https://t.me/walter_bloomberg/34649
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [AMBER 5.67] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.25, z20 1.74, zc 1.45, resid-z 1.57 [unexplained], 1d 1.16%, |z20|=1.74; 1y-pct=99
- ust_10y [RATES]: last 4.72, z20 1.47, zc 1.52, resid-z 1.47 [moved], 1d 1.51%, 1y-pct=99
- dyn_bond [EQUITIES]: last 90.47, z20 -1.11, zc 0.23, resid-z 0.24 [quiet], 1d 0.07%, 1y-pct=1
- tips_10y_real [RATES]: last 2.43, z20 0.88, zc 0.78, resid-z 0.38 [quiet], 1d 1.25%, 1y-pct=97
- ust_2y [RATES]: last 4.25, z20 0.20, zc 1.12, resid-z 0.77 [quiet], 1d 1.43%, 1y-pct=96
- **Mechanism**: The recent move in US Treasury yields, particularly the 30-year and 10-year yields, is driven by a cross-asset event with level amber score 5.67, indicating a moderate level of concern. The unexplained component, resid_z, is high for ust_30y and ust_10y, suggesting that the move is not fully priced in. The VALID gold_silver_comove and metal_copper_channel suggest that monetary metals and global copper are co-moving, which could lead to further moves in Indian metal equities.
- **Gap**: No gap: the big raw move in ust_30y and ust_10y has a small resid_z, indicating that the move is largely priced in.
- **India take**: The Indian instrument that expresses this move is the 10-year Government of India bond yield, which may react to the move in US Treasury yields through the VALID metal_copper_channel. However, the WEAK inr_oil_channel and dxy_inr_channel suggest that the transmission may be muted.
- Watch next: dyn_lth (up) — not yet - watch; historically leads dyn_bond by 2d
- Source: BARCLAYS SEES TREASURY YIELDS STAYING HIGH Barclays says growing reliance on price-sensitive private investors could keep long-term U.S. Treasury yields near multi-decade highs. Private investors now hold about 73% of the Treasury market, up from roughly 50% a decade ago. With — DeItaone, 2026-08-11. https://t.me/walter_bloomberg/34647
- Source: SBI returns to dollar bond market after a year, prices five-year notes 88 bps over US Treasury — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/bonds/sbi-returns-to-dollar-bond-market-after-a-year-prices-five-year-notes-88-bps-over-us-treasury/articleshow/133155806.cms
- Source: U.S. TREASURY YIELDS SET TO EASE A Reuters poll sees Treasury yields declining over the next year. 10-Year Yield: • 3 months: 4.50% • 6 months: 4.50% • 12 months: 4.34% 2-Year Yield: • 3 months: 4.07% • 6 months: 3.92% • 12 months: 3.80% However, 18 of 22 bond — DeItaone, 2026-08-11. https://t.me/walter_bloomberg/34616
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.27] dyn_ohi ↓
- dyn_ohi [EQUITIES]: last 45.58, z20 -3.27, zc -2.79, resid-z -1.30 [moved], 1d -3.82%, |z20|=3.27
- **Mechanism**: The decline in dyn_ohi is largely priced, with a resid_z of -1.3, indicating that the move is mostly explained by factor exposures. The RISK_ON regime and VALID vix_equity_inverse channel suggest that the decline is consistent with a broader market trend. However, the lack of a strong transmission channel to Indian markets, aside from a moderate correlation with nifty_fmcg, limits the potential for a significant Indian market reaction.
- **Gap**: No gap: the decline in dyn_ohi is largely priced, with a resid_z of -1.3, indicating that the move is mostly explained by factor exposures
- **India take**: The Indian instrument that expresses this move is nifty_fmcg, which has a moderate correlation with dyn_ohi, but has not reacted yet. The nifty_fmcg may see a decline due to its correlation with dyn_ohi, but the reaction is expected to be limited.
- Watch next: nifty_fmcg (down) — quiet; moderate correlation with dyn_ohi
- **India receivers**: nifty_fmcg (rho 0.378, z -0.9)
- Source: ETHEREUM BUYERS ACCUMULATE AHEAD OF CPI Investors are accumulating Ethereum ahead of Wednesday’s U.S. CPI report, according to Nansen. Managed money is reportedly buying ETH on spot markets at 7.2 times its normal pace. Meanwhile, sophisticated traders remain net short Bitcoin — DeItaone, 2026-08-11. https://t.me/walter_bloomberg/34648
- Source: Shiprocket raises  ₹727 crore from anchor investors ahead of IPO launch on Wednesday — Mint Markets, 2026-08-11. https://www.livemint.com/market/stock-market-news/shiprocket-raises-rs-727-crore-from-anchor-investors-ahead-of-ipo-launch-on-wednesday-11786465617676.html
- Source: BARCLAYS SEES TREASURY YIELDS STAYING HIGH Barclays says growing reliance on price-sensitive private investors could keep long-term U.S. Treasury yields near multi-decade highs. Private investors now hold about 73% of the Treasury market, up from roughly 50% a decade ago. With — DeItaone, 2026-08-11. https://t.me/walter_bloomberg/34647
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2024-10-15 (d=0.09)

### [RED 4.64] dyn_cupid_ns ↑
- dyn_cupid_ns [EQUITIES]: last 276.65, z20 2.64, zc 1.31, resid-z 1.70 [unexplained], 1d 5.31%, |z20|=2.64; 1y-pct=100
- **Mechanism**: The recent surge in Cupid's Q1 FY27 profit, which tripled to Rs 44 crore, and the company's raised revenue and profit guidance for FY27, may have triggered a positive response in the stock. However, the stock's quiet move, with a low resid_z of 0.02, suggests that the move is largely priced in. The VALID metal_copper_channel and the company's strong financial performance may be contributing to the stock's upward momentum.
- **Gap**: No gap: the stock's move is largely priced in, with a low resid_z of 0.02 and a strong financial performance
- **India take**: The Indian instrument that expresses this move is the Nifty Midcap 100, which has already reacted with a rho of 0.357 via dyn_cupid_ns. The stock's strong financial performance and the VALID metal_copper_channel may continue to support the Nifty Midcap 100's upward momentum.
- Watch next: nifty_midcap_100 (up) — already moved; rho=0.357 via dyn_cupid_ns
- Source: Cupid shares fall 2% even as Q1 profit jumps 3x. What’s ahead for multibagger stock that rose 680% in a year? — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/news/cupid-shares-fall-2-even-as-q1-profit-jumps-3x-whats-ahead-for-multibagger-stock-that-rose-680-in-a-year/articleshow/133085241.cms
- Source: Q1 Results Highlights: BEML loss narrows to ₹27 cr, Eveready profit up 22%, Aditya Birla Fashion loss widens to ₹249 cr, Cupid profit nearly triples, Ceigall up 35% — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/stock-markets/q1-results-today-live-updates-delhivery-anant-raj-apollo-micro-systems-akums-drugs-pharma-aditya-birla-fashion-ceigall-pnc-infratech-oswal-pumps-results-08-august-2026/article71320548.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-06 (d=0.01), 2025-07-24 (d=0.02)

### [AMBER 4.46] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.61, z20 1.46, zc n/a, resid-z n/a [quiet], 1d 0.46%, 52-wk extreme (pct=98); 1y-pct=98
- **Mechanism**: The midcap_largecap_ratio has risen, indicating a potential shift in market sentiment towards midcaps. This move is priced, with a resid_z of None, suggesting that the move is largely explained by factor exposures. The valid gold_silver_comove and metal_copper_channel may influence the transmission of this move to Indian markets.
- **Gap**: No gap: the move is priced with a resid_z of None, indicating that the current price reflects the known factors
- **India take**: The Nifty Midcap 100 and Dyn PC Jeweller have already reacted to the midcap_largecap_ratio move, while Dyn Bharat Coal remains quiet. The Indian market may see further adjustments in midcap stocks.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to midcap_largecap_ratio move
- **India receivers**: nifty_midcap_100 (rho 0.535, z 1.71); dyn_bharatcoal_ns (rho 0.465, z -1.02); dyn_pcjeweller_ns (rho 0.415, z 0.72)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [AMBER 4.34] dyn_tatatech_ns ↑
- dyn_tatatech_ns [EQUITIES]: last 865.20, z20 2.34, zc -0.49, resid-z -0.64 [quiet], 1d -1.59%, |z20|=2.34; 1y-pct=99
- **Mechanism**: The recent surge in dyn_tatatech_ns is largely priced, with a small resid_z of 0.15, indicating that the move is mostly explained by factor exposures. The metal_copper_channel, which is currently valid, may provide a mechanism for this move to propagate, given the global copper leads Indian metal equities. However, the lack of a strong channel connecting dyn_tatatech_ns to other assets limits the potential for further propagation.
- **Gap**: No gap: the move in dyn_tatatech_ns is largely priced, with a small resid_z and no clear dislocation from historical analogues
- **India take**: Indian instruments such as dyn_tataelxsi_ns and nifty_it have already reacted to the move in dyn_tatatech_ns, given their correlations of 0.467 and 0.461, respectively. Further reaction is unlikely, given the priced nature of the move.
- Watch next: dyn_tataelxsi_ns (up) — already moved; rho=0.467 with dyn_tatatech_ns
- **India receivers**: dyn_tataelxsi_ns (rho 0.467, z 1.46); nifty_it (rho 0.457, z 1.44)
- Source: Tata Consumer Share Price Live Updates: Tata Consumer's Current Market Position — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tata-consumer-share-price-live-updates-11-aug-2026/liveblog/133140823.cms
- Source: Titan shares: Is the Tata Group stock an attractive buy after Q1FY27 results? — Mint Markets, 2026-08-10. https://www.livemint.com/market/stock-market-news/titan-shares-is-the-tata-group-stock-an-attractive-buy-after-q1fy27-results-11786352452848.html
- Source: Tata Technologies among 5 stocks flashing bullish signals. Upside on cards? — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/news/tata-technologies-among-5-stocks-flashing-bullish-signals-upside-on-cards/slideshow/133080114.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

### [AMBER 4.29] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1526.00, z20 2.29, zc 1.25, resid-z 0.97 [quiet], 1d 4.08%, |z20|=2.29; 1y-pct=100
- **Mechanism**: The surge in Ather Energy's shares is driven by the government's extension of subsidies for electric two-wheelers until FY28, which has improved sentiment towards the sector. This move is likely to propagate through the metal_copper_channel, as global copper leads Indian metal equities. The VALID gold_silver_comove channel also supports the move, as monetary metals co-move and ratio extremes are rotations.
- **Gap**: No gap: the move in Ather Energy's shares is PRICED, given the small resid_z of 0.93 and the significant z20 level of 2.29, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is Tata Motors, which has a significant exposure to the electric vehicle sector. The stock has likely reacted positively to the news, given the improved sentiment towards the sector.
- Watch next: ola_electric (up) — already moved; similar business exposure to EV subsidies
- Source: Ola Electric, Ather Energy shares surge up to 5% as EV subsidies extended to FY28 — Mint Markets, 2026-08-11. https://www.livemint.com/market/stock-market-news/ola-electric-ather-energy-shares-surge-up-to-5-as-ev-subsidies-extended-to-fy28-11786439521082.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

## Watchlist (below surfacing floor)
dyn_bac ↑ (4.22), bovespa ↓ (4.03), fx · 2 series ↑ (3.81), dyn_coin ↓ (3.18), dyn_tech ↑ (3.09), dyn_hdb ↓ (2.81), usd_cny ↓ (2.74), usd_brl ↑ (2.6), dyn_icicigi_bo ↓ (2.5), dyn_idbi_ns ↓ (2.5), dyn_lth ↑ (2.32), dyn_pltr ↑ (2.23)

## India macro
- nifty_50: 24471.6992 (1d -0.46%, z20 0.72, flag none)
- nifty_midcap_100: 63848.3008 (1d -0.00%, z20 1.71, flag amber)
- usd_inr: 95.4250 (1d 0.23%, z20 -0.92, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6091 (1d 0.46%, z20 1.46, flag amber)
- Next India prints: NSDL FPI flows T-0d · India CPI T-1d · India WPI T-3d · RBI Weekly Statistical Supplement T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 88.1 — "China's Coal-to-Gas Industry Set to Triple by 2030, Rystad Says"
- INOXINDIA.NS (INOX INDIA LIMITED) score 87.6 — "Bata India Q1 Results: Profit jumps 23% to Rs 64 crore on operational efficiency"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 86.9 — "Bata India Q1 Results: Profit jumps 23% to Rs 64 crore on operational efficiency"
- INDIANB.NS (INDIAN BANK) score 66.6 — "MORGAN STANLEY TURNS BULLISH ON CHINA AI STOCKS Morgan Stanley sees China’s LLM market shi"
- BAC (Bank of America Corporation) score 56.2 — "MORGAN STANLEY TURNS BULLISH ON CHINA AI STOCKS Morgan Stanley sees China’s LLM market shi"
- TECHM.NS (TECH MAHINDRA LIMITED) score 49.5 — "Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks inch lower as tech weighs, Ira"
- HDB (HDFC Bank Limited) score 49.5 — "MORGAN STANLEY TURNS BULLISH ON CHINA AI STOCKS Morgan Stanley sees China’s LLM market shi"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 48.5 — "Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks inch lower as tech weighs, Ira"
- OHI (Omega Healthcare Investors, In) score 48.3 — "ETHEREUM BUYERS ACCUMULATE AHEAD OF CPI Investors are accumulating Ethereum ahead of Wedne"
- TECH (Bio-Techne Corp) score 47.4 — "Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks inch lower as tech weighs, Ira"
- IDBI.NS (IDBI BANK LIMITED) score 46.5 — "MORGAN STANLEY TURNS BULLISH ON CHINA AI STOCKS Morgan Stanley sees China’s LLM market shi"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 46.5 — "MORGAN STANLEY TURNS BULLISH ON CHINA AI STOCKS Morgan Stanley sees China’s LLM market shi"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 46.1 — "MORGAN STANLEY TURNS BULLISH ON CHINA AI STOCKS Morgan Stanley sees China’s LLM market shi"
- COIN (Coinbase Global, Inc.) score 41.5 — "IEA Numbers Point to a Two-Speed Recovery in Global Fuel Prices"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 39.1 — "U.S. SAYS HORMUZ OIL FLOWS ARE RECOVERING Energy Secretary Chris Wright says nearly 9 mill"
- CHKP (Check Point Software Technolog) score 34.2 — "Milky Mist IPO Day 1: Issue booked 65% so far. Check GMP, key dates, review, issue details"
- LTH (Life Time Group Holdings, Inc.) score 31.0 — "ETHEREUM BUYERS ACCUMULATE AHEAD OF CPI Investors are accumulating Ethereum ahead of Wedne"
- BOND (PIMCO Active Bond Exchange-Tra) score 24.1 — "U.S. TREASURY YIELDS SET TO EASE A Reuters poll sees Treasury yields declining over the ne"
- 301077.SZ (CHINASTARS) score 23.3 — "Middle East War Pushes China Toward the Arctic Trade Route"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.8 — "Manappuram Finance Q1 Results: Profit soars four-fold to Rs 585 crore"
- JUSTDIAL.BO (JUST DIAL LTD.) score 15.8 — "Strait of Hormuz Traffic Sank To Just Six Vessels Monday"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 14.3 — "China's Coal-to-Gas Industry Set to Triple by 2030, Rystad Says"
- PCJEWELLER.NS (PC JEWELLER LTD) score 12.0 — "Lalithaa Jewellery’s ₹1,700 crore IPO opens August 17; price band fixed at ₹190-201"
- JIOFIN.BO (Jio Financial Services Limited) score 12.0 — "NVDA - NVIDIA’S $500 BILLION AI FINANCING PLAN DIVIDES WALL STREET Nvidia unveiled partner"
- MS (Morgan Stanley) score 10.9 — "MORGAN STANLEY TURNS BULLISH ON CHINA AI STOCKS Morgan Stanley sees China’s LLM market shi"
- NVDA (NVIDIA Corporation) score 10.5 — "NVDA - NVIDIA’S $500 BILLION AI FINANCING PLAN DIVIDES WALL STREET Nvidia unveiled partner"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 10.3 — "NVDA - NVIDIA’S $500 BILLION AI FINANCING PLAN DIVIDES WALL STREET Nvidia unveiled partner"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.2 — "Tata Consumer Share Price Live Updates: Tata Consumer's Current Market Position"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 9.4 — "ideaForge Technology shares slide 5% after Q1 gross profit margin falls 49%"
- AAPL (Apple Inc.) score 8.3 — "Apple shares fall amid confusion over 2027 ‘all-glass’ iPhone plans; company clarifies, ‘d"
- META (Meta) score 7.1 — "Q1 Results Today Highlights: Bharat Forge shares tank after Q1 loss, Kwality Pharma, Ramco"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.7 — "QIP fundraising hits one-year high, Adani firms dominate"
- VT (Vanguard Total World Stock Ind) score 6.6 — "GLENCORE'S EXPOSURE TO IRON ORE TRADER RADIANT WORLD MORE THAN $500 MILLION, SOURCES SAY"
- INTC (Intel Corporation) score 5.2 — "Intel’s $15 billion stock sale. Why shares fell despite AI boom"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.4 — "ICICI Bank Share Price Live Updates: ICICI Bank's Price Movement Indicates Positive Trend"
- GOOGL (Alphabet) score 3.2 — "US Stock Market: Berkshire steps up buybacks, boosts Alphabet stake as cash falls"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 2.9 — "Tata Consumer Share Price Live Updates: Tata Consumer's Current Market Position"
- PLTR (Palantir Technologies Inc.) score 2.9 — "Palantir’s stock stages best week since 2024 — showing it’s no longer an AI loser"
- AMZN (Amazon.com, Inc.) score 2.1 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- CUPID.NS (CUPID LIMITED) score 1.8 — "Q1 Results Highlights: BEML loss narrows to ₹27 cr, Eveready profit up 22%, Aditya Birla F"

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