# Transmission Layer — board brief · 2026-07-17 10:28Z

data as of **2026-07-17** · 98 series · 11 red / 35 amber · 8 events surfaced (33 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.552, 9d in regime; vol-pct 0.649, breadth-off 0.455, Markov P(high-vol) 0.023)
- [WEAK] **safe_haven_gold** — corr20 -0.03, corr60 -0.44, contra nifty_50 corr20=0.23, last shift 2026-06-01. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.82, last shift 2026-01-29. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.43, corr60 0.38, last shift 2026-05-15. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.14, corr60 -0.05, last shift 2026-05-28. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.9, corr60 -0.79, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.06, corr60 -0.06, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.22, corr60 -0.28, last shift 2026-05-15. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.24, corr60 0.24, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.00024255046857080131)
- **SETUP** dyn_ms → asx_200: leads 1d (ccf 0.509, β 0.2112, p 0.0); driver zc -2.4 → expected -0.941%. Type hit-rate 0.819 (n=2909).
- Track record · residual_reversion: hit-rate **0.491** (n=1157) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.819** (n=2909) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.632** (n=19) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.92] commodities · 2 series ↑
- brent [COMMODITIES]: last 85.95, z20 2.09, zc 0.98, resid-z -0.48 [quiet], 1d 2.04%, 1-session move +2.04% ≥ 1.5%; |z20|=2.09; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 80.04, z20 1.93, zc 0.65, resid-z -0.41 [quiet], 1d 1.38%, |z20|=1.93
- **Mechanism**: The recent surge in Brent and WTI crude oil prices, with z20 levels of 2.0853717900812465 and 1.9349155069522184 respectively, is driven by supply-side factors such as the major oil discovery in Libya and production revival gains pace. This move is priced, with resid_z values of -0.48 and -0.41 indicating that the unexplained component is relatively small.
- **Gap**: No gap: the move in Brent and WTI is largely explained by supply-side factors and is priced, with small resid_z values.
- **India take**: The Indian instrument that expresses this move is the nifty_midcap_100, which has a correlation of -0.561 with WTI and is expected to move down. However, it has not reacted yet and is currently quiet with a z20 level of 0.11.
- Watch next: nifty_midcap_100 (down) — not yet - watch; correlated instrument with rho=-0.561 via wti
- **India receivers**: nifty_midcap_100 (rho -0.561, z 0.11)
- Source: Rupee logs sharpest weekly drop in nine as oil price jump stings — BusinessLine Mkts, 2026-07-17. https://www.thehindubusinessline.com/markets/forex/rupee-logs-sharpest-weekly-drop-in-nine-as-oil-price-jump-stings/article71233543.ece
- Source: Libya Declares Major Oil Discovery Commercial as Production Revival Gains Pace — OilPrice, 2026-07-17. https://oilprice.com/Latest-Energy-News/World-News/Libya-Declares-Major-Oil-Discovery-Commercial-as-Production-Revival-Gains-Pace.html
- Source: Vedanta, demerged Vedanta Aluminium, Vedanta Oil & Gas get rating upgrades from CRISIL — ET Markets, 2026-07-17. https://economictimes.indiatimes.com/markets/stocks/news/vedanta-demerged-vedanta-aluminium-vedanta-oil-gas-get-rating-upgrades-from-crisil/articleshow/132456232.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 7.8] cross-asset · 2 series ↑
- gold_silver_ratio [DERIVED]: last 71.81, z20 1.97, zc n/a, resid-z n/a [quiet], 1d 0.72%, GSR<75 (extreme low); |z20|=1.97
- comex_silver [COMMODITIES]: last 55.69, z20 -1.70, zc -0.13, resid-z -0.52 [quiet], 1d -0.38%, |z20|=1.70
- **Mechanism**: The gold-silver ratio has reached an extreme low, indicating a potential rotation between the two metals. This rotation is likely driven by monetary policy expectations, with the recent oil price rally stoking inflation concerns and rate hike bets. The valid gold_silver_comove channel suggests that the ratio extremes are rotations, which may lead to a reversal in the price movement of gold and silver.
- **Gap**: No gap: The current price movement in gold and silver is largely priced in, with the resid_z values indicating that the moves are largely explained by factor exposures. The gold-silver ratio extreme is a rotation signal rather than an anomaly.
- **India take**: The Indian instruments that express this move are the MCX gold and silver futures. While they have reacted to the global cues, the price movement is largely in line with the global trends, with MCX gold August futures up 0.26% and MCX silver September futures down 0.23%.
- Watch next: comex_copper (up) — not yet - watch; Global copper leads Indian metal equities through the metal_copper_channel
- Watch next: dax (up) — not yet - watch; Historical analogues suggest a potential upside in equity markets
- Source: Gold prices dip Rs 3,000/10 gram this week, silver plunges Rs 7,300/kg as oil rally raises rate hike bets. What’s next? — ET Markets, 2026-07-17. https://economictimes.indiatimes.com/markets/commodities/news/gold-prices-dip-rs-3000/10-gram-this-week-silver-plunges-rs-7300/kg-as-oil-rally-raises-rate-hike-bets-whats-next/articleshow/132452126.cms
- Source: Gold and silver prices volatile amid weak global cues, growing concerns over inflation, US Fed rate hike bets — Mint Markets, 2026-07-17. https://www.livemint.com/market/commodities/gold-and-silver-prices-volatile-amid-weak-global-cues-growing-concerns-over-inflation-us-fed-rate-hike-bets-11784258025527.html
- Source: Gold, silver prices today: Comex gold and silver extend losses as Middle East tensions fuel rate hike fears — Mint Markets, 2026-07-16. https://www.livemint.com/market/commodities/gold-silver-prices-today-comex-gold-and-silver-extend-losses-as-middle-east-tensions-lift-rate-hike-fears-11784218381820.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-29 (d=0.06), 2025-08-12 (d=0.14)

### [RED 7.14] indices · 3 series ↓
- taiwan_weighted [INDICES]: last 42918.00, z20 -3.82, zc -4.41, resid-z -0.01 [moved], 1d -5.93%, |z20|=3.82
- nikkei_225 [INDICES]: last 64113.21, z20 -3.28, zc -2.03, resid-z -1.29 [moved], 1d -4.07%, |z20|=3.28
- kospi [INDICES]: last 6835.21, z20 -1.70, zc -1.45, resid-z -1.41 [quiet], 1d -6.17%, |z20|=1.70
- **Mechanism**: The decline in Asian indices, particularly the Nikkei 225 and Kospi, is driven by a sell-off in chip-related stocks and escalating US-Iran tensions, which has dampened risk appetite. This has led to a decline in Indian transmission candidates such as nifty_metal, which has reacted to the Kospi's move. The metal_copper_channel, which is a valid channel, may also contribute to the transmission of the decline to Indian metal equities.
- **Gap**: No gap: the decline in Asian indices is largely priced in, with resid_z values indicating that the moves are mostly explained by factor exposures
- **India take**: The Indian instrument nifty_metal has reacted to the decline in Kospi, while other transmission candidates such as dyn_hdbfs_bo and dyn_ceatltd_ns remain quiet. The metal_copper_channel may lead to further declines in Indian metal equities.
- Watch next: nifty_metal (down) — already moved; reacted to Kospi's decline
- **India receivers**: nifty_metal (rho 0.525, z -1.1); dyn_hdbfs_bo (rho 0.502, z -1.06); dyn_ceatltd_ns (rho 0.446, z -0.72); nifty_midcap_100 (rho 0.437, z 0.11)
- Source: US stock market to Nikkei: Here’s global equity heatmap you should know before opening of the Indian stock market today — Mint Markets, 2026-07-17. https://www.livemint.com/market/stock-market-news/us-stock-market-to-nikkei-here-s-global-equity-heatmap-you-should-know-before-opening-of-the-indian-stock-market-today-11784257058033.html
- Source: Global Markets: Japan's Nikkei drops nearly 3% as chip stocks slide despite robust TSMC results — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/us-stocks/news/global-markets-japans-nikkei-drops-nearly-3-as-chip-stocks-slide-despite-robust-tsmc-results/articleshow/132433045.cms
- Source: Asian stocks today: Kospi, Nikkei extend losses, plunge up to 6% amid sell-off in chip stocks — Mint Markets, 2026-07-16. https://www.livemint.com/market/stock-market-news/asian-stocks-today-kospi-nikkei-extend-losses-plunge-up-to-6-amid-sell-off-in-chip-stocks-11784165210140.html

### [RED 6.42] cross-asset · 2 series ↑
- dyn_techm_ns [EQUITIES]: last 1571.00, z20 3.59, zc 2.15, resid-z 1.25 [moved], 1d 4.02%, |z20|=3.59
- nifty_it [INDICES]: last 29178.55, z20 1.96, zc 0.89, resid-z 0.33 [quiet], 1d 1.59%, |z20|=1.96
- **Mechanism**: The recent rally in IT stocks, led by a 2.3% gain in the Nifty IT index, has lifted sentiment across the broader Indian stock market. This move is priced, with a relatively small resid_z of 1.25 for dyn_techm_ns, indicating that the factor exposures have largely explained the move. The valid metal_copper_channel and vix_equity_inverse channels suggest that the global economic trends and volatility are influencing the Indian market.
- **Gap**: No gap: the recent move in IT stocks is largely explained by factor exposures, with a small resid_z of 1.25, indicating that the market has already priced in the positive news.
- **India take**: The Indian instrument that expresses this move is the Nifty IT index, which has already reacted with a 2.3% gain. Other Indian transmission candidates, such as dyn_tataelxsi_ns and nifty_50, have also reacted with rho values of 0.706 and 0.352, respectively.
- Watch next: dyn_techm_ns (up) — already moved; IT stocks rally on strong Q1 results
- **India receivers**: dyn_tataelxsi_ns (rho 0.706, z -1.51); nifty_50 (rho 0.352, z 1.61)
- Source: Infosys, TCS, HCL Technologies to Tech Mahindra: Why are IT stocks rising today? — Mint Markets, 2026-07-17. https://www.livemint.com/market/stock-market-news/infosys-tcs-hcl-technologies-to-tech-mahindra-why-are-it-stocks-rising-today-11784271768196.html
- Source: Tech Mahindra shares jump on Q1 results; analysts split on valuation — BusinessLine Mkts, 2026-07-17. https://www.thehindubusinessline.com/markets/stock-markets/tech-mahindra-surges-on-strong-q1-results-analysts-split-on-valuation/article71232908.ece
- Source: Q1 Results Today Live: Reliance shares up ahead of results, JSW Steel, Havells, Oberoi Realty, Tata Tech to announce Q1 results, Jio Financial, Tech Mahindra, BHEL soar after Q1, Wipro, WeWork, CEAT, Polycab shares decline — BusinessLine Mkts, 2026-07-17. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-reliance-industries-jsw-steel-tata-tech-turtlemint-havells-poonawalla-navkar-wipro-jio-financial-tech-mahindra-bhel-itc-results-17-july-2026/article71229272.ece
- Historical analogues: 2025-12-30 (d=0.52), 2025-08-13 (d=0.76), 2026-01-06 (d=0.77)

### [RED 6.0] dyn_pypl ↑
- dyn_pypl [EQUITIES]: last 56.74, z20 4.00, zc 0.85, resid-z 7.78 [unexplained], 1d 2.21%, |z20|=4.00
- **Mechanism**: The surge in PayPal shares following a $53 billion buyout offer from Stripe and Advent International has triggered a rally in the US markets, with the S&P 500 and Dow Jones Industrial Average rising. This move is likely to propagate through the vix_equity_inverse channel, which is currently valid, leading to a potential decline in volatility and further gains in equity markets. However, the move in dyn_pypl is priced, with a resid_z of -0.56, indicating that the unexplained component is relatively small.
- **Gap**: No gap: the move in dyn_pypl is priced, with a resid_z of -0.56, indicating that the unexplained component is relatively small
- **India take**: The Indian instrument nifty_it has reacted to the move in dyn_pypl, with a rho of 0.148, and is likely to continue its upward trend. Additionally, dyn_patanjali_ns has also reacted, with a rho of -0.629, indicating a potential decline in its value.
- Watch next: nifty_it (up) — reacted; rho=0.148 via dyn_pypl
- **India receivers**: dyn_patanjali_ns (rho -0.622, z -3.59); nifty_it (rho 0.161, z 1.96)
- Source: PayPal’s battered stock is getting a record boost from a report of buyout interest — MarketWatch Top, 2026-07-15. https://www.marketwatch.com/story/a-53-billion-lifeline-stripe-and-advent-reportedly-team-up-to-bid-for-battered-paypal-3bc6fcc2?mod=mw_rss_topstories
- Source: PayPal shares jump over 15% after Stripe, Advent make $53 billion buyout offer — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/us-stocks/news/paypal-shares-jump-over-15-after-stripe-advent-make-53-billion-buyout-offer/articleshow/132418333.cms
- Source: Wall Street surges on soft producer inflation, robust earnings; PayPal climbs 13.58%, BlackRock soars 7.6% — Mint Markets, 2026-07-15. https://www.livemint.com/market/stock-market-news/wall-street-surges-on-softer-than-expected-producer-inflation-paypal-climbs-1358-11784122704074.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.0), 2025-04-16 (d=0.05)

### [RED 5.74] shanghai_comp ↓
- shanghai_comp [INDICES]: last 3764.63, z20 -3.74, zc -2.61, resid-z -1.76 [unexplained], 1d -3.03%, |z20|=3.74
- **Mechanism**: The Shanghai Composite's decline is driven by concerns over liquidity crunch due to CXMT's $8.6 billion IPO and a pipeline of large listings, which has triggered heavy selling in AI and semiconductor stocks. This move is unexplained by factor exposures, with a resid_z of -1.76. The valid vix_equity_inverse channel suggests that the vol spike will lead to equity drawdown, potentially transmitting to Indian markets.
- **Gap**: No gap: the big raw move in Shanghai Composite is largely priced, with a z20 of -3.74 and a resid_z of -1.76, indicating that the move is mostly explained by the liquidity concerns and tech sell-off
- **India take**: The Indian instruments that express this move are the midcap_largecap_ratio and dyn_hdbfs_bo, both of which have already reacted with a z20 of -1.34 and -1.06, respectively. The metal_copper_channel may also transmit the move to Indian metal equities.
- Watch next: nifty_50 (down) — not yet - watch; Indian equities often follow Chinese market trends
- **India receivers**: midcap_largecap_ratio (rho 0.39, z -1.34); dyn_hdbfs_bo (rho 0.367, z -1.06)
- Source: Global Market: China stocks face steep weekly losses as CXMT IPO sparks liquidity crunch fears — ET Markets, 2026-07-17. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-face-steep-weekly-losses-as-cxmt-ipo-sparks-liquidity-crunch-fears/articleshow/132453628.cms
- Source: Global Market:  China stocks slide as tech sell-off hits mainland markets; Alibaba lifts Hong Kong shares — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-slide-as-tech-sell-off-hits-mainland-markets-alibaba-lifts-hong-kong-shares/articleshow/132431074.cms
- Historical analogues: 2026-06-18 (d=0.0), 2025-12-19 (d=0.02), 2025-09-25 (d=0.03)

### [RED 5.56] dyn_icicigi_bo ↓
- dyn_icicigi_bo [EQUITIES]: last 1612.30, z20 -3.56, zc -0.41, resid-z -0.60 [quiet], 1d -0.67%, |z20|=3.56; 1y-pct=0
- **Mechanism**: The decline in dyn_icicigi_bo is largely priced, with a small resid_z of -0.6, indicating that the move is mostly explained by factor exposures. The Valid metal_copper_channel and vix_equity_inverse channels suggest that global market sentiment and risk appetite are influencing the move. However, the Weak inr_oil_channel and dxy_inr_channel imply that the Indian rupee and oil prices may not be significant drivers of this move.
- **Gap**: No gap: the small resid_z and low r2 of 0.086 suggest that the move is largely explained by factor exposures and there is no significant event-to-price gap.
- **India take**: The Indian instrument that expresses this move is dyn_nuvoco_ns, which has already reacted with a z20 of 1.58. Other related instruments like dyn_indianb_ns and dyn_adanient_bo are quiet, with z20 values of 0.27 and 0.74, respectively.
- Watch next: nifty_midcap_100 (down) — not yet - watch; rho=0.428 via dyn_icicigi_bo
- **India receivers**: nifty_midcap_100 (rho 0.428, z 0.11); dyn_nuvoco_ns (rho 0.399, z 1.58); dyn_indianb_ns (rho 0.365, z 0.27); dyn_adanient_bo (rho 0.353, z 0.74)
- Source: HDFC Bank, Axis Bank, ICICI, Kotak shares rise up to 3% ahead of Q1 earnings; Nifty Bank gains 500 pts. What to expect? — ET Markets, 2026-07-17. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-bank-axis-bank-icici-kotak-shares-rise-up-to-3-ahead-of-q1-earnings-nifty-bank-gains-500-pts-what-to-expect/articleshow/132455002.cms
- Source: Sensex jumps 950 points, Nifty 50 ends above 24,300, driven by Reliance, HDFC Bank, ICICI Bank shares — Mint Markets, 2026-07-17. https://www.livemint.com/market/stock-market-news/sensex-jumps-800-points-reliance-hdfc-bank-icici-bank-power-indian-stock-market-ahead-of-q1-results-2026-11784268199353.html
- Source: Market wrap: ICICI Lombard, IndiGo among top gainers & losers on Nifty and Sensex today — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-icici-lombard-indigo-among-top-gainers-losers-on-nifty-and-sensex-today/articleshow/132439120.cms
- Historical analogues: 2026-06-24 (d=0.0), 2025-05-30 (d=0.03), 2026-01-07 (d=0.04)

### [RED 5.06] dyn_qessf ↓
- dyn_qessf [EQUITIES]: last 0.23, z20 -3.06, zc -1.21, resid-z -0.78 [quiet], 1d -7.88%, |z20|=3.06
- **Mechanism**: The decline in dyn_qessf is accompanied by a low resid_z of -0.78, indicating that the move is largely priced and explained by factor exposures. The valid metal_copper_channel and gold_silver_comove channels suggest that monetary metals and copper are co-moving, which may be influencing the move in dyn_qessf. However, the weak inr_oil_channel and dxy_inr_channel imply that the Indian rupee and oil prices are not significantly impacting the move.
- **Gap**: No gap: The low resid_z and priced move suggest that the current price of dyn_qessf is largely explained by factor exposures, leaving no significant event-to-price gap.
- **India take**: The Indian instrument that expresses this move is likely to be the metal equities, such as Hindalco or Tata Steel, which may react to the co-movement of copper and monetary metals. However, the reaction has not yet occurred.
- Watch next: nifty_50 (down) — not yet - watch; Risk-off sentiment may lead to a decline in Indian equities
- Source: KUWAIT DEFENCE MINISTRY SAYS IRANIAN 'AGGRESSION' ON THURSDAY TARGETED NUMBER OF VITAL FACILITIES, RESULTING IN MATERIAL DAMAGE — DeItaone, 2026-07-16. https://t.me/walter_bloomberg/33733
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-15 (d=0.32), 2024-11-14 (d=0.52)

## Watchlist (below surfacing floor)
cross-asset · 3 series ↑ (4.93), cross-asset · 2 series ↓ (4.9), dyn_bac ↑ (4.2), dyn_blk ↑ (4.02), natgas ↓ (3.73), commodities · 2 series ↑ (3.61), dyn_patanjali_ns ↓ (3.59), usd_inr ↑ (3.53), dyn_atherenerg_ns ↑ (3.52), dyn_tataelxsi_ns ↓ (3.51), dyn_bhel_ns ↑ (3.28), dyn_inoxindia_ns ↑ (3.06)

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
- INOXINDIA.NS (INOX INDIA LIMITED) score 81.2 — "Maharatna PSU stock Indian Oil Corporation sets board meeting date to declare Q1 results 2"
- INDIANB.NS (INDIAN BANK) score 69.0 — "Sensex jumps 950 points, Nifty 50 ends above 24,300, driven by Reliance, HDFC Bank, ICICI "
- HDB (HDFC Bank Limited) score 58.6 — "Sensex jumps 950 points, Nifty 50 ends above 24,300, driven by Reliance, HDFC Bank, ICICI "
- COIN (Coinbase Global, Inc.) score 56.6 — "Why is market rising today? Sensex surges 900 points: 4 reasons why D-Street is defying th"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 51.1 — "Sensex jumps 950 points, Nifty 50 ends above 24,300, driven by Reliance, HDFC Bank, ICICI "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 46.1 — "Tech Mahindra shares jump on Q1 results; analysts split on valuation"
- BAC (Bank of America Corporation) score 38.0 — "Sensex jumps 950 points, Nifty 50 ends above 24,300, driven by Reliance, HDFC Bank, ICICI "
- CHKP (Check Point Software Technolog) score 28.5 — "Tata Power to declare Q1 results 2026 on this date. Check details"
- IDBI.NS (IDBI BANK LIMITED) score 25.5 — "Sensex jumps 950 points, Nifty 50 ends above 24,300, driven by Reliance, HDFC Bank, ICICI "
- BOND (PIMCO Active Bond Exchange-Tra) score 24.4 — "Foreign inflows in Asian bonds surge to seven-month high in June"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 19.7 — "Rescuers in southwest China race extreme weather to reach residents trapped by landslide"
- VT (Vanguard Total World Stock Ind) score 19.2 — "Alpine Texworld IPO: Focus shifts to allotment date. Latest GMP, step-by-step guide to che"
- JIOFIN.BO (Jio Financial Services Limited) score 13.9 — "Jio Financial Services share price jumps 6% after Q1 profit soars 155%; should you buy the"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 13.9 — "Jio Financial Services share price jumps 6% after Q1 profit soars 155%; should you buy the"
- WIT (Wipro Limited) score 10.5 — "Stocks to watch: Reliance Industries, Wipro, CEAT among shares in focus today; check list "
- SKHYV (SK hynix Inc. American Deposit) score 10.4 — "NEW 2X SK HYNIX ETF DEBUTS Leverage Shares launched $SKHX on Tuesday, a 2x leveraged ETF t"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.4 — "IEA Warns World Has Just Weeks to Avoid Hormuz Economic Shock"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.2 — "Tata Power to declare Q1 results 2026 on this date. Check details"
- TECHM.NS (TECH MAHINDRA LIMITED) score 9.6 — "Tech Mahindra shares jump on Q1 results; analysts split on valuation"
- BHEL.NS (BHEL) score 9.0 — "BHEL hits 52-week high before retreating; analysts split as Q1 profit ends eight-year wait"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.5 — "Sensex jumps 950 points, Nifty 50 ends above 24,300, driven by Reliance, HDFC Bank, ICICI "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.6 — "Adani Ent Share Price Live Updates: Adani Enterprises  Current Price Update"
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.3 — "250% return in five years! Multibagger penny stock PC Jeweller to raise  ₹1,000 crore thro"
- META (Meta) score 5.9 — "Is SpaceX’s stock a bust because it fell below $135? Look what happened after Meta’s IPO."
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 5.2 — "KUWAIT DEFENCE MINISTRY SAYS IRANIAN 'AGGRESSION' ON THURSDAY TARGETED NUMBER OF VITAL FAC"
- MS (Morgan Stanley) score 4.7 — "Dimon-led JPMorgan poised to become world's first $1 trillion bank"
- KALYANKJIL.NS (KALYAN JEWELLERS IND LTD) score 4.1 — "Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. T"
- GS (Goldman Sachs Group, Inc. (The) score 4.0 — "Crude oil prices rise for 4th session amid escalating US-Iran war; Brent likely to hit $11"
- CEATLTD.NS (CEAT LIMITED) score 3.8 — "CEAT share price slumps over 9% on Q1 results. Should you buy, sell or hold?"
- SWIGGY.NS (SWIGGY LIMITED) score 3.7 — "Stocks to buy for short term: Swiggy among 3 shares Amol Athawale of Kotak Securities reco"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 3.3 — "AI trade moves from chips to electricity: Why 7 power stocks are gaining Wall Street atten"
- NFLX (Netflix, Inc.) score 2.8 — "What triggered Netflix's sharp post-earnings selloff?"
- MU (Micron Technology, Inc.) score 2.7 — "Micron has turned into ‘the most important stock in the market.’ So is it time to worry?"
- PYPL (PayPal Holdings, Inc.) score 2.7 — "US stocks today: US stocks rise with earnings in focus; PayPal jumps on takeover bid repor"
- BLK (BlackRock, Inc.) score 2.6 — "BlackRock assets hit record $15 trillion on boost from buoyant markets, ETF inflows"
- BIOCON.BO (BIOCON LTD.) score 2.5 — "Mylan exits Biocon, sells entire 5.64% stake for ₹3,679 crore via block deals"
- 453950.KS (TIGER TSMC Foundry Value Chain) score 2.4 — "TSMC posts 77% profit jump for Q2, surging past market expectations"
- NUVOCO.NS (NUVOCO VISTAS CORP LTD) score 1.9 — "Broker’s Call: Nuvoco Vistas (Accumulate)"
- CUPID.NS (CUPID LIMITED) score 1.7 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 1.3 — "Patanjali Foods share price crashes 20%, extending losses for third straight session; what"

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