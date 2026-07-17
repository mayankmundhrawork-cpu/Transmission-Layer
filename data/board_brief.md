# Transmission Layer — board brief · 2026-07-17 21:13Z

data as of **2026-07-17** · 98 series · 15 red / 29 amber · 8 events surfaced (28 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.57, 9d in regime; vol-pct 0.703, breadth-off 0.438, Markov P(high-vol) 0.056)
- [INVERTED] **safe_haven_gold** — corr20 0.01, corr60 -0.42, contra nifty_50 corr20=0.25, last shift 2026-06-01. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.82, last shift 2026-01-29. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.43, corr60 0.38, last shift 2026-05-15. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.18, corr60 -0.06, last shift 2026-05-28. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.8, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.06, corr60 -0.06, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.17, corr60 -0.27, last shift 2026-05-15. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.21, corr60 0.23, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **4 of 89** scanned series survive multiplicity control (effective p ≤ 0.001935206426436853)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.494** (n=1166) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=3045) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.632** (n=19) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.39] commodities · 2 series ↑
- brent [COMMODITIES]: last 88.09, z20 2.56, zc 2.21, resid-z 1.13 [moved], 1d 4.58%, 1-session move +4.58% ≥ 1.5%; |z20|=2.56; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 81.77, z20 2.39, zc 1.69, resid-z 0.74 [moved], 1d 3.57%, 1-session move +3.57% ≥ 1.5%; |z20|=2.39
- **Mechanism**: The recent surge in Brent and WTI prices can be attributed to the proposed stricter vehicle emission rules in India, which may lead to reduced oil consumption, and the increase in US oil drilling activity. However, the small resid_z values for both Brent and WTI suggest that this move is largely priced in, with the market already accounting for these factors. The valid gold_silver_comove and metal_copper_channel may also play a role in transmitting this move to other markets.
- **Gap**: No gap: the small resid_z values for Brent and WTI indicate that the current price move is largely explained by factor exposures and is not an anomaly
- **India take**: The proposed stricter vehicle emission rules in India may lead to reduced oil consumption, and the Nifty Midcap 100 may react to this development. However, the Indian market has not yet reacted to this news, and the Nifty Midcap 100 is still quiet.
- Watch next: nifty_midcap_100 (down) — not yet - watch; correlated with WTI, may react to oil price movement
- **India receivers**: nifty_midcap_100 (rho -0.564, z 0.11)
- Source: India Proposes Stricter Vehicle Emission Rules To Cut Oil Consumption — OilPrice, 2026-07-17. https://oilprice.com/Latest-Energy-News/World-News/India-Proposes-Stricter-Vehicle-Emission-Rules-To-Cut-Oil-Consumption.html
- Source: US Oil Drilling Picks Up As Brent Gains 4% — OilPrice, 2026-07-17. https://oilprice.com/Energy/Energy-General/US-Oil-Drilling-Picks-Up-As-Brent-Gains-4.html
- Source: Jeff Currie: Illusion of Oil Abundance Is Gone — OilPrice, 2026-07-17. https://oilprice.com/Latest-Energy-News/World-News/Jeff-Currie-Illusion-of-Oil-Abundance-Is-Gone.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 7.14] indices · 3 series ↓
- taiwan_weighted [INDICES]: last 42918.00, z20 -3.82, zc -4.41, resid-z -3.10 [unexplained], 1d -5.93%, |z20|=3.82
- nikkei_225 [INDICES]: last 64113.21, z20 -3.28, zc -2.03, resid-z -1.47 [moved], 1d -4.07%, |z20|=3.28
- kospi [INDICES]: last 6835.21, z20 -1.70, zc -1.45, resid-z -1.41 [quiet], 1d -6.17%, |z20|=1.70
- **Mechanism**: The decline in Asian indices, particularly the Nikkei 225 and Kospi, is driven by a sell-off in chip-related stocks and escalating US-Iran tensions, which has dampened risk appetite. This has led to a decline in Indian transmission candidates such as nifty_metal, which has reacted to the Kospi's move. The metal_copper_channel, which is a valid channel, may also contribute to the transmission of the decline to Indian metal equities.
- **Gap**: No gap: the decline in Asian indices is largely priced in, with resid_z values indicating that the moves are mostly explained by factor exposures
- **India take**: The Indian instrument nifty_metal has reacted to the decline in Kospi, while other transmission candidates such as dyn_hdbfs_bo and dyn_ceatltd_ns remain quiet. The metal_copper_channel may lead to further declines in Indian metal equities.
- Watch next: nifty_metal (down) — already moved; reacted to Kospi's decline
- **India receivers**: nifty_metal (rho 0.525, z -1.1); dyn_hdbfs_bo (rho 0.498, z -0.83); dyn_ceatltd_ns (rho 0.446, z -0.72); nifty_midcap_100 (rho 0.437, z 0.11)
- Source: US stock market to Nikkei: Here’s global equity heatmap you should know before opening of the Indian stock market today — Mint Markets, 2026-07-17. https://www.livemint.com/market/stock-market-news/us-stock-market-to-nikkei-here-s-global-equity-heatmap-you-should-know-before-opening-of-the-indian-stock-market-today-11784257058033.html
- Source: Global Markets: Japan's Nikkei drops nearly 3% as chip stocks slide despite robust TSMC results — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/us-stocks/news/global-markets-japans-nikkei-drops-nearly-3-as-chip-stocks-slide-despite-robust-tsmc-results/articleshow/132433045.cms
- Source: Asian stocks today: Kospi, Nikkei extend losses, plunge up to 6% amid sell-off in chip stocks — Mint Markets, 2026-07-16. https://www.livemint.com/market/stock-market-news/asian-stocks-today-kospi-nikkei-extend-losses-plunge-up-to-6-amid-sell-off-in-chip-stocks-11784165210140.html

### [RED 6.42] cross-asset · 2 series ↑
- dyn_techm_ns [EQUITIES]: last 1571.00, z20 3.59, zc 2.15, resid-z 1.06 [moved], 1d 4.02%, |z20|=3.59
- nifty_it [INDICES]: last 29178.55, z20 1.96, zc 0.89, resid-z 0.28 [quiet], 1d 1.59%, |z20|=1.96
- **Mechanism**: The recent rally in IT stocks, led by a 2.3% gain in the Nifty IT index, has lifted sentiment across the broader Indian stock market. This move is priced, with a relatively small resid_z of 1.25 for dyn_techm_ns, indicating that the factor exposures have largely explained the move. The valid metal_copper_channel and vix_equity_inverse channels suggest that the global economic trends and volatility are influencing the Indian market.
- **Gap**: No gap: the recent move in IT stocks is largely explained by factor exposures, with a small resid_z of 1.25, indicating that the market has already priced in the positive news.
- **India take**: The Indian instrument that expresses this move is the Nifty IT index, which has already reacted with a 2.3% gain. Other Indian transmission candidates, such as dyn_tataelxsi_ns and nifty_50, have also reacted with rho values of 0.706 and 0.352, respectively.
- Watch next: dyn_techm_ns (up) — already moved; IT stocks rally on strong Q1 results
- **India receivers**: dyn_tataelxsi_ns (rho 0.706, z -1.51); nifty_50 (rho 0.352, z 1.61)
- Source: Infosys, TCS, HCL Technologies to Tech Mahindra: Why are IT stocks rising today? — Mint Markets, 2026-07-17. https://www.livemint.com/market/stock-market-news/infosys-tcs-hcl-technologies-to-tech-mahindra-why-are-it-stocks-rising-today-11784271768196.html
- Source: Tech Mahindra shares jump on Q1 results; analysts split on valuation — BusinessLine Mkts, 2026-07-17. https://www.thehindubusinessline.com/markets/stock-markets/tech-mahindra-surges-on-strong-q1-results-analysts-split-on-valuation/article71232908.ece
- Source: Q1 Results Today Live: Reliance shares up ahead of results, JSW Steel, Havells, Oberoi Realty, Tata Tech to announce Q1 results, Jio Financial, Tech Mahindra, BHEL soar after Q1, Wipro, WeWork, CEAT, Polycab shares decline — BusinessLine Mkts, 2026-07-17. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-reliance-industries-jsw-steel-tata-tech-turtlemint-havells-poonawalla-navkar-wipro-jio-financial-tech-mahindra-bhel-itc-results-17-july-2026/article71229272.ece
- Historical analogues: 2025-12-30 (d=0.52), 2025-08-13 (d=0.76), 2026-01-06 (d=0.77)

### [RED 5.74] shanghai_comp ↓
- shanghai_comp [INDICES]: last 3764.63, z20 -3.74, zc -2.61, resid-z -3.15 [unexplained], 1d -3.03%, |z20|=3.74
- **Mechanism**: The Shanghai Composite's decline is driven by concerns over liquidity crunch due to CXMT's $8.6 billion IPO and a pipeline of large listings, which has triggered heavy selling in AI and semiconductor stocks. This move is unexplained by factor exposures, with a resid_z of -1.76. The valid vix_equity_inverse channel suggests that the vol spike will lead to equity drawdown, potentially transmitting to Indian markets.
- **Gap**: No gap: the big raw move in Shanghai Composite is largely priced, with a z20 of -3.74 and a resid_z of -1.76, indicating that the move is mostly explained by the liquidity concerns and tech sell-off
- **India take**: The Indian instruments that express this move are the midcap_largecap_ratio and dyn_hdbfs_bo, both of which have already reacted with a z20 of -1.34 and -1.06, respectively. The metal_copper_channel may also transmit the move to Indian metal equities.
- Watch next: nifty_50 (down) — not yet - watch; Indian equities often follow Chinese market trends
- **India receivers**: midcap_largecap_ratio (rho 0.39, z -1.34); dyn_hdbfs_bo (rho 0.359, z -0.83)
- Source: Global Market: China stocks face steep weekly losses as CXMT IPO sparks liquidity crunch fears — ET Markets, 2026-07-17. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-face-steep-weekly-losses-as-cxmt-ipo-sparks-liquidity-crunch-fears/articleshow/132453628.cms
- Source: Global Market:  China stocks slide as tech sell-off hits mainland markets; Alibaba lifts Hong Kong shares — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-slide-as-tech-sell-off-hits-mainland-markets-alibaba-lifts-hong-kong-shares/articleshow/132431074.cms
- Historical analogues: 2026-06-18 (d=0.0), 2025-12-19 (d=0.02), 2025-09-25 (d=0.03)

### [RED 5.56] dyn_icicigi_bo ↓
- dyn_icicigi_bo [EQUITIES]: last 1612.30, z20 -3.56, zc -0.41, resid-z -0.56 [quiet], 1d -0.67%, |z20|=3.56; 1y-pct=0
- **Mechanism**: The decline in dyn_icicigi_bo is largely priced, with a small resid_z of -0.6, indicating that the move is mostly explained by factor exposures. The Valid metal_copper_channel and vix_equity_inverse channels suggest that global market sentiment and risk appetite are influencing the move. However, the Weak inr_oil_channel and dxy_inr_channel imply that the Indian rupee and oil prices may not be significant drivers of this move.
- **Gap**: No gap: the small resid_z and low r2 of 0.086 suggest that the move is largely explained by factor exposures and there is no significant event-to-price gap.
- **India take**: The Indian instrument that expresses this move is dyn_nuvoco_ns, which has already reacted with a z20 of 1.58. Other related instruments like dyn_indianb_ns and dyn_adanient_bo are quiet, with z20 values of 0.27 and 0.74, respectively.
- Watch next: nifty_midcap_100 (down) — not yet - watch; rho=0.428 via dyn_icicigi_bo
- **India receivers**: nifty_midcap_100 (rho 0.428, z 0.11); dyn_indianb_ns (rho 0.365, z 0.3); dyn_adanient_bo (rho 0.352, z 0.8)
- Source: HDFC Bank, Axis Bank, ICICI, Kotak shares rise up to 3% ahead of Q1 earnings; Nifty Bank gains 500 pts. What to expect? — ET Markets, 2026-07-17. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-bank-axis-bank-icici-kotak-shares-rise-up-to-3-ahead-of-q1-earnings-nifty-bank-gains-500-pts-what-to-expect/articleshow/132455002.cms
- Source: Sensex jumps 950 points, Nifty 50 ends above 24,300, driven by Reliance, HDFC Bank, ICICI Bank shares — Mint Markets, 2026-07-17. https://www.livemint.com/market/stock-market-news/sensex-jumps-800-points-reliance-hdfc-bank-icici-bank-power-indian-stock-market-ahead-of-q1-results-2026-11784268199353.html
- Source: Market wrap: ICICI Lombard, IndiGo among top gainers & losers on Nifty and Sensex today — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-icici-lombard-indigo-among-top-gainers-losers-on-nifty-and-sensex-today/articleshow/132439120.cms
- Historical analogues: 2026-06-24 (d=0.0), 2025-05-30 (d=0.03), 2026-01-07 (d=0.04)

### [AMBER 4.93] cross-asset · 3 series ↑
- nifty_50 [INDICES]: last 24343.65, z20 1.61, zc 1.41, resid-z 1.84 [unexplained], 1d 1.13%, |z20|=1.61
- dyn_indusindbk_bo [EQUITIES]: last 1027.20, z20 1.45, zc 0.72, resid-z -0.34 [quiet], 1d 1.32%, 1y-pct=100
- nifty_midcap_100 [INDICES]: last 62369.75, z20 0.11, zc -0.62, resid-z -2.55 [unexplained], 1d -0.58%, 1y-pct=96
- **Mechanism**: The move in Nifty 50 and other Indian equities is driven by robust Q1 earnings and IT buying, with financials rallying ahead of key earnings. The move is priced, given the relatively small resid_z values, indicating that the market has already factored in the positive earnings and sectoral trends. The valid gold_silver_comove and metal_copper_channel suggest that monetary metals and global copper are co-moving, which could influence Indian metal equities.
- **Gap**: No gap: The move in Nifty 50 is largely priced, with a resid_z of 1.84, indicating that the market has already factored in the positive earnings and sectoral trends.
- **India take**: The Indian instruments that express this move are dyn_jiofin_bo and nifty_metal, which have already reacted. Other transmission candidates like dyn_indianb_ns and dyn_adanient_bo are quiet, but may react in the coming days.
- Watch next: nifty_50 (up) — already moved; Robust Q1 earnings and IT buying
- Watch next: dyn_indusindbk_bo (up) — quiet; Financial stocks rallying ahead of key earnings
- **India receivers**: dyn_jiofin_bo (rho 0.902, z 1.28); dyn_indianb_ns (rho 0.623, z 0.3); dyn_ceatltd_ns (rho 0.605, z -0.72); nifty_metal (rho 0.597, z -1.1)
- Source: Market wrap: Top gainers and losers on Nifty and Sensex today — ET Markets, 2026-07-17. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-top-gainers-and-losers-on-nifty-and-sensex-today/articleshow/132460186.cms
- Source: Sensex today | Stock Market Highlights: Sensex jumps 965 pts, Nifty ends above 24,334; financials rally ahead of key earnings — BusinessLine Mkts, 2026-07-17. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-17th-july-2026/article71229818.ece
- Source: Sensex today | Stock Market Live: Sensex surges 965 points, Nifty tops 24,334; banking, financial stocks shine ahead of key earnings — BusinessLine Mkts, 2026-07-17. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-17th-july-2026/article71229818.ece
- Historical analogues: 2025-07-18 (d=0.85), 2025-07-11 (d=1.33), 2025-05-30 (d=1.51)

### [RED 4.9] dyn_nflx ↓
- dyn_nflx [EQUITIES]: last 68.86, z20 -2.90, zc -4.07, resid-z 0.65 [moved], 1d -7.38%, |z20|=2.90; 1y-pct=0
- **Mechanism**: The sharp decline in Netflix shares is largely priced, given the weak sales forecast and the company's decision to cut back on reporting viewership statistics, which has raised investor anxiety regarding its future trajectory. The move is also reflected in the broader technology sector, with the Nasdaq Composite down 1.7%. The vix_equity_inverse channel is valid, indicating a potential vol spike and equity drawdown. However, the resid_z of -0.01 suggests that the move is largely explained by factor exposures, indicating that the decline is priced.
- **Gap**: No gap: the decline in Netflix shares is largely explained by factor exposures, with a resid_z of -0.01, indicating that the move is priced
- **India take**: The Indian instrument that expresses this move is dyn_indianb_ns, which has a rho of -0.353 with dyn_nflx, but it has not reacted yet, with a z20 of 0.3, indicating a quiet status.
- Watch next: dyn_nflx (down) — already moved; weak sales forecast and cut back on reporting viewership statistics
- **India receivers**: dyn_indianb_ns (rho -0.353, z 0.3)
- Source: Netflix shares tumble 13% after weak sales forecast, hit 22-month low — Mint Markets, 2026-07-17. https://www.livemint.com/market/netflix-shares-tumble-13-after-weak-sales-forecast-hit-22-month-low-11784295044711.html
- Source: Netflix shares tumble over 10% as slowing growth, less viewership data spook investors — ET Markets, 2026-07-17. https://economictimes.indiatimes.com/markets/us-stocks/news/netflix-shares-tumble-over-10-as-slowing-growth-less-viewership-data-spook-investors/articleshow/132465122.cms
- Source: Wall Street falls on deepening selloff in chip stocks, Netflix slumps10.6%, Nvidia tumbles 4% — Mint Markets, 2026-07-17. https://www.livemint.com/market/stock-market-news/wall-street-falls-on-deepening-selloff-in-chip-stocks-netflix-slumps-11784295818738.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-10 (d=0.03), 2025-04-01 (d=0.05)

### [AMBER 4.88] rates · 3 series ↑
- tips_10y_real [RATES]: last 2.35, z20 1.56, zc 0.74, resid-z 0.05 [quiet], 1d 1.29%, |z20|=1.56; 1y-pct=99
- ust_30y [RATES]: last 5.09, z20 1.47, zc 0.28, resid-z -0.18 [quiet], 1d 0.20%, 1y-pct=97
- ust_10y [RATES]: last 4.57, z20 1.18, zc 0.45, resid-z -0.21 [quiet], 1d 0.44%, 1y-pct=97
- **Mechanism**: The recent surge in Japanese bond yields, driven by rising oil prices and fiscal concerns, has led to a global market reaction, with US Treasury yields (ust_10y, ust_30y) increasing. This move is largely priced, as evidenced by the low resid_z values (0.05, -0.18, -0.21) for the affected series, indicating that the factor exposures can explain most of the move.
- **Gap**: No gap: the move in US Treasury yields is largely explained by factor exposures, with low resid_z values indicating that the move is priced
- **India take**: The Indian 10-year government bond yield may react to this global trend, potentially leading to an increase in yields. However, the inr_oil_channel is weak, which may limit the transmission of global oil price shocks to Indian markets.
- Watch next: ust_2y (up) — not yet - watch; historically leads by 1d
- Source: Global Market: Japanese bond yields climb as oil surge and fiscal concerns weigh on market — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japanese-bond-yields-climb-as-oil-surge-and-fiscal-concerns-weigh-on-market/articleshow/132431940.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.25), 2026-03-30 (d=0.31)

## Watchlist (below surfacing floor)
gold_silver_ratio ↑ (4.83), commodities · 3 series ↑ (4.54), nasdaq_100 ↓ (4.53), dyn_qessf ↓ (4.34), dyn_aapl ↑ (3.98), dyn_bac ↑ (3.75), dyn_patanjali_ns ↓ (3.59), dyn_ohi ↑ (3.55), usd_inr ↑ (3.53), dyn_atherenerg_ns ↑ (3.52), dyn_tataelxsi_ns ↓ (3.51), dyn_bhel_ns ↑ (3.34)

## India macro
- nifty_50: 24343.6504 (1d 1.13%, z20 1.61, flag amber)
- nifty_midcap_100: 62369.7500 (1d -0.58%, z20 0.11, flag amber)
- usd_inr: 96.2700 (1d -0.24%, z20 1.53, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5621 (1d -1.68%, z20 -1.34, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 80.9 — "India Proposes Stricter Vehicle Emission Rules To Cut Oil Consumption"
- INDIANB.NS (INDIAN BANK) score 67.9 — "Federal Bank among 4 stocks that hit 52-week highs and rallied up to 25% in a month"
- HDB (HDFC Bank Limited) score 60.5 — "PB Fintech share price rises 3% after HDFC Mutual Fund stake raise to 5.02%"
- COIN (Coinbase Global, Inc.) score 52.9 — "Japan's LNG Giant Weighs U.S. IPO to Accelerate Global Expansion"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 51.8 — "Federal Bank among 4 stocks that hit 52-week highs and rallied up to 25% in a month"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 44.5 — "PB Fintech share price rises 3% after HDFC Mutual Fund stake raise to 5.02%"
- BAC (Bank of America Corporation) score 41.0 — "IRAN WARNS U.S. FORCES Iran’s Revolutionary Guard said it is closely monitoring U.S. milit"
- IDBI.NS (IDBI BANK LIMITED) score 28.7 — "Federal Bank among 4 stocks that hit 52-week highs and rallied up to 25% in a month"
- CHKP (Check Point Software Technolog) score 27.7 — "MakeMyTrip India files confidential IPO DRHP with Sebi. Check details"
- BOND (PIMCO Active Bond Exchange-Tra) score 23.0 — "India bonds sink on oil spike, index-entry uncertainty"
- VT (Vanguard Total World Stock Ind) score 22.3 — "APPLE CLOSES IN ON NVIDIA $AAPL is on the verge of reclaiming the title of the world’s mos"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 18.8 — "Look on the bright side: Energy companies are booming"
- JIOFIN.BO (Jio Financial Services Limited) score 15.5 — "A bad health diagnosis will upend your financial plan, but you can set it right again"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 15.4 — "A bad health diagnosis will upend your financial plan, but you can set it right again"
- TECHM.NS (TECH MAHINDRA LIMITED) score 11.5 — "PB Fintech share price rises 3% after HDFC Mutual Fund stake raise to 5.02%"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.1 — "Tata Technologies Q1 Results: Profit rises 6% to Rs 180 crore"
- SKHYV (SK hynix Inc. American Deposit) score 10.4 — "SKHY – SK HYNIX DOWN 0.7% IN PREMARKET SK Hynix shares are slipping 0.7% in premarket afte"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.4 — "HORMUZ TRAFFIC HITS 3-WEEK LOW Confirmed crossings via the Strait of Hormuz dropped to a 3"
- WIT (Wipro Limited) score 9.4 — "Stocks to watch: Reliance Industries, Wipro, CEAT among shares in focus today; check list "
- NFLX (Netflix, Inc.) score 8.3 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Highlights: S&P 500 and Nasdaq slip "
- BHEL.NS (BHEL) score 8.1 — "BHEL hits 52-week high before retreating; analysts split as Q1 profit ends eight-year wait"
- META (Meta) score 7.3 — "META IN TALKS TO LEASE COMPUTING POWER TO ANTHROPIC IN POTENTIAL $10 BILLION DEAL - NYT"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.7 — "Sensex jumps 950 points, Nifty 50 ends above 24,300, driven by Reliance, HDFC Bank, ICICI "
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.6 — "India's gold jewellery demand revives as prices stabilise; festive orders pick up: WGC"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.0 — "Adani Ent Share Price Live Updates: Adani Enterprises  Current Price Update"
- AAPL (Apple Inc.) score 4.9 — "APPLE CLOSES IN ON NVIDIA $AAPL is on the verge of reclaiming the title of the world’s mos"
- NVDA (NVIDIA Corporation) score 4.9 — "APPLE CLOSES IN ON NVIDIA $AAPL is on the verge of reclaiming the title of the world’s mos"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 4.7 — "KUWAIT DEFENCE MINISTRY SAYS IRANIAN 'AGGRESSION' ON THURSDAY TARGETED NUMBER OF VITAL FAC"
- MS (Morgan Stanley) score 4.2 — "Dimon-led JPMorgan poised to become world's first $1 trillion bank"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 3.9 — "KUWAIT SAYS ELECTRICAL AND DESALINATION POWER PLANT DAMAGED IN IRANIAN ATTACK - ELECTRICIT"
- KALYANKJIL.NS (KALYAN JEWELLERS IND LTD) score 3.7 — "Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. T"
- GS (Goldman Sachs Group, Inc. (The) score 3.6 — "Crude oil prices rise for 4th session amid escalating US-Iran war; Brent likely to hit $11"
- CEATLTD.NS (CEAT LIMITED) score 3.4 — "CEAT share price slumps over 9% on Q1 results. Should you buy, sell or hold?"
- SWIGGY.NS (SWIGGY LIMITED) score 3.4 — "Stocks to buy for short term: Swiggy among 3 shares Amol Athawale of Kotak Securities reco"
- OHI (Omega Healthcare Investors, In) score 2.9 — "APPLE CLOSES IN ON NVIDIA $AAPL is on the verge of reclaiming the title of the world’s mos"
- MU (Micron Technology, Inc.) score 2.5 — "Micron has turned into ‘the most important stock in the market.’ So is it time to worry?"
- PYPL (PayPal Holdings, Inc.) score 2.4 — "US stocks today: US stocks rise with earnings in focus; PayPal jumps on takeover bid repor"
- BIOCON.BO (BIOCON LTD.) score 2.3 — "Mylan exits Biocon, sells entire 5.64% stake for ₹3,679 crore via block deals"
- CUPID.NS (CUPID LIMITED) score 1.6 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 1.1 — "Patanjali Foods share price crashes 20%, extending losses for third straight session; what"

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