# Transmission Layer — board brief · 2026-08-03 19:55Z

data as of **2026-08-03** · 98 series · 19 red / 32 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.33, 2d in regime; vol-pct 0.367, breadth-off 0.294, Markov P(high-vol) 0.07)
- [INVERTED] **safe_haven_gold** — corr20 -0.43, corr60 -0.44, contra nifty_50 corr20=0.21, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.82, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.35, corr60 0.32, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.15, corr60 -0.05, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.84, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.07, corr60 -0.05, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.13, corr60 -0.24, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.29, corr60 0.2, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **5 of 90** scanned series survive multiplicity control (effective p ≤ 0.00244553738718456)
- **SETUP** dyn_coin → asx_200: leads 1d (ccf 0.322, β 0.05, p 0.0); driver zc -2.26 → expected -0.529%. Type hit-rate 0.816 (n=3048).
- **SETUP** dyn_coin → aud_usd: leads 1d (ccf 0.264, β 0.0328, p 0.00023); driver zc -2.26 → expected -0.348%. Type hit-rate 0.816 (n=3048).
- Track record · residual_reversion: hit-rate **0.493** (n=1136) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.816** (n=3048) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.34] cross-asset · 2 series ↑
- usd_jpy [FX]: last 156.91, z20 -6.51, zc -6.07, resid-z -5.83 [unexplained], 1d -2.04%, |z20|=6.51
- dyn_amzn [EQUITIES]: last 285.11, z20 4.16, zc 6.66, resid-z 1.43 [moved], 1d 4.98%, |z20|=4.16; 1y-pct=100
- **Mechanism**: The joint intervention by Japan and the US to support the yen has led to a significant move in usd_jpy, which has not been fully explained by factor exposures, as indicated by a high resid_z score. This move has also been accompanied by a surge in Amazon's stock price, driven by strong earnings and cloud growth. The transmission of these moves to the Indian market is likely to be through the correlated instruments, particularly dyn_muthootfin_ns and dyn_thangamayl_ns, which have already reacted.
- **Gap**: No gap: the big raw move in usd_jpy has a small resid_z, indicating that it is largely priced in, and the move in dyn_amzn is also largely explained by its factor exposures.
- **India take**: The Indian instruments, such as dyn_muthootfin_ns and dyn_thangamayl_ns, have already reacted to the moves in usd_jpy and dyn_amzn, while dyn_cartrade_ns is still to be watched. The transmission of the global moves to the Indian market is likely to be through these correlated instruments.
- Watch next: dyn_muthootfin_ns (down) — already moved; correlated with usd_jpy
- Watch next: dyn_thangamayl_ns (down) — already moved; correlated with dyn_amzn
- Watch next: dyn_cartrade_ns (down) — not yet - watch; correlated with dyn_amzn
- **India receivers**: dyn_muthootfin_ns (rho -0.512, z -3.09); dyn_thangamayl_ns (rho -0.369, z -3.5); dyn_cartrade_ns (rho -0.364, z 0.13)
- Source: Yen holds gains after Japan, US confirm joint intervention, signal more action — ET Markets, 2026-08-03. https://economictimes.indiatimes.com/markets/forex/forex-news/yen-holds-gains-after-japan-us-confirm-joint-intervention-signal-more-action/articleshow/132839035.cms
- Source: Amazon joins $3 trillion club as AI, cloud growth fuel stock rally — ET Markets, 2026-08-03. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/amazon-joins-3-trillion-club-as-ai-cloud-growth-fuel-stock-rally/articleshow/132835634.cms
- Source: Why the U.S. decided to help Japan by boosting the flailing yen — MarketWatch Top, 2026-08-03. https://www.marketwatch.com/story/joint-u-s-japanese-intervention-boosts-the-yen-but-will-it-be-enough-069451f5?mod=mw_rss_topstories
- Historical analogues: 2024-10-16 (d=0.15), 2024-11-21 (d=0.23), 2026-03-31 (d=0.24)

### [RED 8.36] cross-asset · 9 series ↑
- cac_40 [INDICES]: last 8626.25, z20 3.72, zc 0.32, resid-z 0.18 [quiet], 1d 1.37%, |z20|=3.72; 1y-pct=100
- stoxx_50 [INDICES]: last 6431.81, z20 3.17, zc 0.20, resid-z -0.13 [quiet], 1d 1.16%, |z20|=3.17; 1y-pct=100
- dax [INDICES]: last 26038.36, z20 2.90, zc 0.08, resid-z -0.25 [quiet], 1d 1.60%, |z20|=2.90; 1y-pct=100
- comex_copper [COMMODITIES]: last 6.54, z20 2.32, zc -0.06, resid-z -0.83 [quiet], 1d 1.65%, |z20|=2.32; 1y-pct=98; co-occur[metal_copper] same-direction (channel VALID)
- dow_jones [INDICES]: last 53192.62, z20 2.25, zc 0.47, resid-z 0.22 [quiet], 1d 1.35%, |z20|=2.25; 1y-pct=100
- sp500 [INDICES]: last 7602.12, z20 1.88, zc 0.67, resid-z 0.56 [quiet], 1d 1.50%, |z20|=1.88; 1y-pct=99
- dyn_vt [EQUITIES]: last 157.63, z20 1.47, zc 0.23, resid-z 0.81 [quiet], 1d 1.14%, 1y-pct=96
- ftse_100 [INDICES]: last 10850.38, z20 1.38, zc -0.46, resid-z -0.48 [quiet], 1d -0.16%, 1y-pct=98
- russell_2000 [INDICES]: last 2982.50, z20 0.96, zc -0.39, resid-z -1.82 [unexplained], 1d 1.75%, 1y-pct=95
- **Mechanism**: The recent easing of geopolitical tensions in the Middle East has led to a sharp decline in crude oil prices, boosting investor sentiment and causing a rally in major US stock indices. This move is propagated through the VALID vix_equity_inverse channel, where a decrease in volatility leads to an increase in equity prices. The VALID metal_copper_channel also supports this move, as global copper prices have been rising, leading to an increase in Indian metal equities.
- **Gap**: No gap: the recent move in US stock indices is largely priced in, with most indices showing a high z20 score and a low resid_z, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian market has already reacted to the global cues, with the Nifty 50, Nifty Midcap 100, and Nifty IT indices all showing a high correlation with their respective global counterparts. The metal_copper_channel also suggests that Indian metal equities may continue to rise in tandem with global copper prices.
- Watch next: nifty_50 (up) — already moved; high correlation with cac_40
- Watch next: nifty_midcap_100 (up) — already moved; high correlation with dax
- Watch next: nifty_it (up) — already moved; high correlation with ftse_100
- **India receivers**: nifty_50 (rho 0.545, z 3.43); nifty_midcap_100 (rho 0.51, z 2.51); nifty_it (rho 0.366, z 2.46)
- Source: Wall Street climbs as crude oil prices plunge, Amazon jumps 3.8% — Mint Markets, 2026-08-03. https://www.livemint.com/market/stock-market-news/wall-street-climbs-as-crude-oil-prices-plunge-amazon-jumps-38-11785765123026.html
- Source: Wall Street climbs as crude oil prices plunge, Amazon jumps 5.3% — Mint Markets, 2026-08-03. https://www.livemint.com/market/stock-market-news/wall-street-climbs-as-crude-oil-prices-plunge-amazon-jumps-38-11785765123026.html
- Source: US stock market today: Wall Street futures gain as easing Iran tensions trigger sharp fall in oil prices — Mint Markets, 2026-08-03. https://www.livemint.com/market/stock-market-news/us-stock-market-today-wall-street-futures-gain-as-easing-iran-tensions-trigger-sharp-fall-in-oil-prices-11785756062931.html
- Historical analogues: 2024-10-11 (d=0.86), 2024-10-04 (d=0.88), 2024-11-21 (d=1.01)

### [RED 7.03] cross-asset · 3 series ↑
- dyn_jiofin_bo [EQUITIES]: last 262.00, z20 3.71, zc 1.84, resid-z 2.39 [unexplained], 1d 2.16%, |z20|=3.71
- nifty_50 [INDICES]: last 24774.30, z20 3.43, zc 0.36, resid-z 0.42 [quiet], 1d 1.60%, |z20|=3.43
- nifty_midcap_100 [INDICES]: last 63668.10, z20 2.51, zc 0.40, resid-z -0.10 [quiet], 1d 1.26%, |z20|=2.51; 1y-pct=100
- **Mechanism**: The Nifty 50's unusual surge of nearly 200 points in the final minutes of trade, due to the new closing auction session, has created a discrepancy in the Indian stock market. This move is not fully explained by factor exposures, as evidenced by the resid_z of 0.42 for Nifty 50. The metal_copper_channel and vix_equity_inverse channels are valid and may be contributing to the propagation of this move.
- **Gap**: No gap: The move in Nifty 50 is largely priced, given its z20 level of 3.43 and the small resid_z of 0.42, indicating that the market has already accounted for this move.
- **India take**: The Indian instruments that express this move are dyn_muthootfin_ns, dyn_bharatcoal_ns, and nifty_metal, which have already reacted. However, dyn_indianb_ns and dyn_indusindbk_bo have not yet reacted and may be worth watching.
- Watch next: dyn_jiofin_bo (up) — already moved; High z20 level and unexplained move
- Watch next: nifty_50 (up) — already moved; Unusual surge in the final minutes of trade
- **India receivers**: dyn_muthootfin_ns (rho 0.692, z -3.09); dyn_bharatcoal_ns (rho 0.633, z -1.52); dyn_indianb_ns (rho 0.622, z 0.79); dyn_indusindbk_bo (rho 0.614, z 0.04)
- Source: New closing auction sparks rare Nifty-Sensex split amid low participation — Mint Markets, 2026-08-03. https://www.livemint.com/market/new-closing-auction-sparks-rare-nifty-sensex-split-amid-low-participation-11785769915392.html
- Source: Closing price discovery faces first test as CAS spikes Nifty by nearly 200 points — BusinessLine Mkts, 2026-08-03. https://www.thehindubusinessline.com/markets/closing-price-discovery-faces-first-test-as-cas-spikes-nifty-by-nearly-200-points/article71302249.ece
- Source: Why did Nifty 50 jump 200 points in the final minutes of trade? Here's what happened — Mint Markets, 2026-08-03. https://www.livemint.com/market/stock-market-news/why-did-the-nifty-50-jump-200-points-in-the-final-minutes-of-trade-heres-what-happened-11785765452716.html
- Historical analogues: 2025-07-17 (d=0.69), 2024-11-07 (d=0.98), 2025-08-13 (d=1.26)

### [RED 6.31] dyn_msft ↑
- dyn_msft [EQUITIES]: last 488.46, z20 4.31, zc 0.72, resid-z 6.76 [unexplained], 1d 5.11%, |z20|=4.31
- **Mechanism**: The recent surge in Microsoft's stock, erasing its year-to-date losses, is driven by its addition to Goldman Sachs' U.S. Conviction List and a broader rally in US hyperscalers. This move is unexplained by factor exposures, with a high resid_z of 6.76. The valid vix_equity_inverse channel suggests that the low volatility environment is contributing to the equity rally.
- **Gap**: No gap: the big raw move in Microsoft's stock is accompanied by a small z20 of 4.31, indicating that the move is largely priced in.
- **India take**: The Indian instrument dyn_thangamayl_ns has already reacted to the move in Microsoft's stock, with a negative rho of -0.383. Further reaction in Indian metal equities may be expected via the valid metal_copper_channel.
- Watch next: dyn_msft (up) — already moved; recent surge in stock price
- **India receivers**: dyn_thangamayl_ns (rho -0.383, z -3.5)
- Source: Microsoft’s stock is on a run not seen in 26 years — erasing its year-to-date losses — MarketWatch Top, 2026-08-03. https://www.marketwatch.com/story/microsofts-stock-is-on-a-run-not-seen-in-26-years-erasing-its-year-to-date-losses-d9827b6c?mod=mw_rss_topstories
- Source: SHARES OF US HYPERSCALERS CLIMB • META RISES 6.1% • MICROSOFT JUMPS 4.7% • AMAZON GAINS 4.6% — DeItaone, 2026-08-03. https://t.me/walter_bloomberg/34236
- Source: GOLDMAN REFRESHES U.S. CONVICTION LIST Goldman Sachs added Applied Materials ( $AMAT), Delta ( $DAL), Microsoft ( $MSFT), O'Reilly Automotive ( $ORLY), Viking Holdings ( $VIK) and UPS to its U.S. Conviction List. The firm removed Broadcom ( $AVGO), Dick's Sporting Goods ( — DeItaone, 2026-08-03. https://t.me/walter_bloomberg/34209
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.02), 2025-10-20 (d=0.06)

### [AMBER 6.11] commodities · 2 series ↓
- brent [COMMODITIES]: last 83.76, z20 -0.27, zc 0.28, resid-z 0.70 [quiet], 1d -7.06%, 1-session move -7.06% ≥ 1.5%
- wti [COMMODITIES]: last 80.25, z20 -0.00, zc 0.36, resid-z 0.65 [quiet], 1d -5.22%, 1-session move -5.22% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.498 via wti, z 2.51, reacted); midcap_largecap_ratio (rho -0.415 via wti, z -1.14, reacted); dyn_hdbfs_bo (rho -0.381 via brent, z -1.26, reacted)
- **India receivers**: nifty_midcap_100 (rho -0.498, z 2.51); midcap_largecap_ratio (rho -0.415, z -1.14); dyn_hdbfs_bo (rho -0.381, z -1.26)
- Source: Ukraine’s Drone Campaign Drives Russian Oil Refining to 24-Year Low — OilPrice, 2026-08-03. https://oilprice.com/Latest-Energy-News/World-News/Ukraines-Drone-Campaign-Drives-Russian-Oil-Refining-to-24-Year-Low.html
- Source: Big Oil Companies Report Record Profits Amid High Oil Prices — OilPrice, 2026-08-03. https://oilprice.com/Energy/Energy-General/Big-Oil-Companies-Report-Record-Profits-Amid-High-Oil-Prices.html
- Source: Trump Orders Oil Companies to Cut Gas Prices, Targets Chevron CEO — OilPrice, 2026-08-03. https://oilprice.com/Latest-Energy-News/World-News/Trump-Orders-Oil-Companies-to-Cut-Gas-Prices-Targets-Chevron-CEO.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [AMBER 6.01] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.21, z20 2.08, zc 0.29, resid-z 1.09 [quiet], 1d 0.19%, |z20|=2.08; 1y-pct=100
- dyn_bond [EQUITIES]: last 90.35, z20 -1.95, zc -1.14, resid-z 0.13 [quiet], 1d -0.16%, 1y-pct=0
- ust_10y [RATES]: last 4.68, z20 1.39, zc 0.22, resid-z 1.94 [unexplained], 1d 0.21%, 1y-pct=99
- tips_10y_real [RATES]: last 2.41, z20 1.11, zc 0.00, resid-z 1.88 [unexplained], 1d 0.00%, 1y-pct=98
- ust_2y [RATES]: last 4.23, z20 0.15, zc 0.18, resid-z 2.50 [unexplained], 1d 0.24%, 1y-pct=96
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.578 vs ust_30y, historically leads by 1d
- Watch next: wti (inverse) — not yet - watch; rho -0.527 vs dyn_bond, historically leads by 3d
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.551 vs dyn_bond
- Watch next: brent (co-move) — not yet - watch; rho 0.506 vs ust_30y
- Source: US 10-year yield falls from 18-month high on Iran peace talk hopes — ET Markets, 2026-08-03. https://economictimes.indiatimes.com/markets/bonds/us-10-year-yield-falls-from-18-month-high-on-iran-peace-talk-hopes/articleshow/132831577.cms
- Source: Warsh tightened more by pausing than by lifting rates, this bond-market veteran argues. Here’s the math. — MarketWatch Top, 2026-08-03. https://www.marketwatch.com/story/warsh-tightened-more-by-pausing-than-by-lifting-rates-this-bond-market-veteran-argues-heres-the-math-31cb15a1?mod=mw_rss_topstories
- Source: BNP SEES FED HIKES PUSHING YIELDS HIGHER BNP Paribas expects U.S. Treasury yields to keep rising as markets price in future Fed rate hikes. The bank forecasts three Fed hikes starting in December, arguing investors will continue to question the Fed's credibility after last — DeItaone, 2026-08-03. https://t.me/walter_bloomberg/34210
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.5] dyn_thangamayl_ns ↓
- dyn_thangamayl_ns [EQUITIES]: last 4965.50, z20 -3.50, zc -1.06, resid-z -2.34 [unexplained], 1d -4.99%, |z20|=3.50
- **Mechanism**: dyn_thangamayl_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho -0.371 via dyn_thangamayl_ns, z 3.71, reacted)
- **India receivers**: dyn_jiofin_bo (rho -0.371, z 3.71)
- Source: Thangamayil Jewellery shares crash 32% in a week. What should investors do? — ET Markets, 2026-08-03. https://economictimes.indiatimes.com/markets/stocks/news/thangamayil-jewellery-shares-crash-32-in-a-week-what-should-investors-do/articleshow/132821479.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-29 (d=0.01), 2026-06-11 (d=0.01)

### [RED 5.45] fx · 2 series ↑
- eur_usd [FX]: last 1.15, z20 2.62, zc 1.31, resid-z 1.62 [unexplained], 1d -0.07%, |z20|=2.62
- usd_mxn [FX]: last 17.32, z20 -2.15, zc -1.30, resid-z -1.35 [quiet], 1d -0.15%, |z20|=2.15
- **Mechanism**: fx · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.52 via usd_mxn, z -3.09, reacted)
- Watch next: gbp_usd (co-move) — not yet - watch; rho 0.848 vs eur_usd, historically leads by 4d
- **India receivers**: dyn_muthootfin_ns (rho -0.52, z -3.09)
- Source: Global Market: Euro zone bond yields decline as falling oil prices boost market sentiment — ET Markets, 2026-08-03. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-bond-yields-decline-as-falling-oil-prices-boost-market-sentiment/articleshow/132826355.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-05 (d=0.17), 2025-09-05 (d=0.21)

## Watchlist (below surfacing floor)
dyn_muthootfin_ns ↓ (5.09), dyn_chkp ↓ (4.61), dyn_coin ↓ (4.38), dyn_aapl ↓ (4.14), gold_silver_ratio ↑ (3.81), dyn_tech ↑ (3.34), nifty_metal ↑ (3.27), dyn_lth ↑ (3.19), dyn_atherenerg_ns ↑ (3.07), dyn_havells_ns ↑ (2.88), corn ↑ (2.66), ust_2s10s ↑ (2.6)

## India macro
- nifty_50: 24774.3008 (1d 1.60%, z20 3.43, flag red)
- nifty_midcap_100: 63668.1016 (1d 1.26%, z20 2.51, flag red)
- usd_inr: 95.3300 (1d -0.37%, z20 -1.43, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5699 (1d -0.33%, z20 -1.14, flag none)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI MPC decision T-4d · RBI Weekly Statistical Supplement T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 65.0 — "HSBC, SBI and ICICI Bank get half of India's FCNR flows under incentive window"
- COALINDIA.NS (COAL INDIA LTD) score 62.8 — "HSBC, SBI and ICICI Bank get half of India's FCNR flows under incentive window"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 61.6 — "HSBC, SBI and ICICI Bank get half of India's FCNR flows under incentive window"
- INDIANB.NS (INDIAN BANK) score 53.6 — "BNP SEES FED HIKES PUSHING YIELDS HIGHER BNP Paribas expects U.S. Treasury yields to keep "
- COIN (Coinbase Global, Inc.) score 46.1 — "THIS WEEK'S U.S. ECONOMIC CALENDAR (ET) 🟢 Monday • 9:45 AM – S&P Global Manufacturing PMI "
- TECHM.NS (TECH MAHINDRA LIMITED) score 40.2 — "Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks climb higher as Big Tech ralli"
- BAC (Bank of America Corporation) score 39.6 — "Should wealthier Americans forgo their Social Security benefits as a charitable gesture?"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 38.2 — "Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks climb higher as Big Tech ralli"
- HDB (HDFC Bank Limited) score 37.5 — "BNP SEES FED HIKES PUSHING YIELDS HIGHER BNP Paribas expects U.S. Treasury yields to keep "
- OHI (Omega Healthcare Investors, In) score 37.0 — "BNP SEES FED HIKES PUSHING YIELDS HIGHER BNP Paribas expects U.S. Treasury yields to keep "
- IDBI.NS (IDBI BANK LIMITED) score 36.6 — "BNP SEES FED HIKES PUSHING YIELDS HIGHER BNP Paribas expects U.S. Treasury yields to keep "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 36.5 — "BNP SEES FED HIKES PUSHING YIELDS HIGHER BNP Paribas expects U.S. Treasury yields to keep "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 34.1 — "BNP SEES FED HIKES PUSHING YIELDS HIGHER BNP Paribas expects U.S. Treasury yields to keep "
- TECH (Bio-Techne Corp) score 31.0 — "Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks climb higher as Big Tech ralli"
- CHKP (Check Point Software Technolog) score 27.6 — "LIC OFS opens on August 4 as govt looks to sell up to 6.5% stake. Check details"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 26.9 — "MV Electrosystems leads mainboard IPO rush with 188.85 times subscription, Juniper Green E"
- LTH (Life Time Group Holdings, Inc.) score 25.7 — "TRUMP'S MONDAY SCHEDULE • 8:00 AM ET – Executive Time • 12:00 PM ET – Policy Meeting • 1:3"
- BOND (PIMCO Active Bond Exchange-Tra) score 22.6 — "Oil, dollar inflows blunt impact on Indian bonds from index inclusion snub"
- 301077.SZ (CHINASTARS) score 16.9 — "Why Have China and Russia Just Stepped Out Of The Shadows In The U.S.-Iran War?"
- MS (Morgan Stanley) score 13.0 — "U.S. TIGHTENS ROBOT IMPORT RULES The FCC will restrict imports of certain foreign-made adv"
- AMZN (Amazon.com, Inc.) score 12.2 — "Wall Street climbs as crude oil prices plunge, Amazon jumps 5.3%"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.3 — "Stocks to watch, Aug 3: Tata Motors Passenger vehicles, TMCV, Maruti Suzuki, Mahindra & Ma"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.1 — "Why Have China and Russia Just Stepped Out Of The Shadows In The U.S.-Iran War?"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.7 — "Adani Total Gas raises CNG prices by ₹4 per kg amid rising LNG costs"
- MSFT (Microsoft Corporation) score 9.4 — "SHARES OF US HYPERSCALERS CLIMB • META RISES 6.1% • MICROSOFT JUMPS 4.7% • AMAZON GAINS 4."
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 9.0 — "‘NCDEX entry into MF distribution will be a Vande Bharat movement for the industry’"
- AAPL (Apple Inc.) score 8.6 — "Apple suffers worst rout since 2025 on disappointing outlook"
- JIOFIN.BO (Jio Financial Services Limited) score 8.5 — "Sensex, Nifty gap up on Iran diplomacy, crude slide; financials lead, pharma drags"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 7.6 — "Sensex, Nifty gap up on Iran diplomacy, crude slide; financials lead, pharma drags"
- VT (Vanguard Total World Stock Ind) score 5.9 — "Healthcare stock Park Medi World inches close to record high after the Q1 results 2026"
- GS (Goldman Sachs Group, Inc. (The) score 5.9 — "GOLDMAN REFRESHES U.S. CONVICTION LIST Goldman Sachs added Applied Materials ( $AMAT), Del"
- META (Meta) score 5.8 — "SHARES OF US HYPERSCALERS CLIMB • META RISES 6.1% • MICROSOFT JUMPS 4.7% • AMAZON GAINS 4."
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 5.7 — "Muthoot Microfin case: Sebi exempts six family trusts from open offer obligation"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.5 — "HSBC, SBI and ICICI Bank get half of India's FCNR flows under incentive window"
- PCJEWELLER.NS (PC JEWELLER LTD) score 5.5 — "Thangamayil Jewellery shares crash 32% in a week. What should investors do?"
- INFY (Infosys Limited) score 4.7 — "Kospi’s mammoth 17% surge spells caution for Indian IT stocks. Why TCS, Infosys, others ar"
- NVDA (NVIDIA Corporation) score 3.8 — "Did China build a top-tier AI model by itself? A new report suggests Nvidia chips played a"
- THANGAMAYL.NS (THANGAMAYIL JEWELLERY LTD) score 3.0 — "Thangamayil Jewellery shares crash 32% in a week. What should investors do?"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 1.0 — "LT Foods shares jump 4% on strong Q1 results; stock outperforms market"
- CUPID.NS (CUPID LIMITED) score 0.7 — "Cupid increases investment by $5 million in GII’s Healthcare-focused platform"

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