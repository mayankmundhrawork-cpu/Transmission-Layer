# Transmission Layer — board brief · 2026-08-05 22:33Z

data as of **2026-08-05** · 98 series · 19 red / 27 amber · 8 events surfaced (20 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.3, 1d in regime; vol-pct 0.365, breadth-off 0.235, Markov P(high-vol) 0.058)
- [INVERTED] **safe_haven_gold** — corr20 -0.4, corr60 -0.42, contra nifty_50 corr20=0.09, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.87, corr60 0.81, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.42, corr60 0.34, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.21, corr60 -0.05, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.78, corr60 -0.8, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.03, corr60 -0.02, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [VALID] **real_rates_gold_inverse** — corr20 -0.32, corr60 -0.26, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.13, corr60 0.18, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 90** scanned series survive multiplicity control (effective p ≤ 0.00020725924734810164)
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.482, β 0.2616, p 0.0); driver zc -1.54 → expected -0.39%. Type hit-rate 0.821 (n=2924).
- Track record · residual_reversion: hit-rate **0.494** (n=1156) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.821** (n=2924) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 11.08] cross-asset · 13 series ↑
- comex_gold [COMMODITIES]: last 4307.70, z20 6.00, zc 3.59, resid-z 1.40 [moved], 1d 5.18%, |z20|=6.00; co-occur[gold_silver] same-direction (channel VALID)
- dow_jones [INDICES]: last 54349.94, z20 3.66, zc 0.43, resid-z 0.97 [quiet], 1d 0.49%, |z20|=3.66; 1y-pct=100
- comex_silver [COMMODITIES]: last 62.33, z20 3.35, zc 1.39, resid-z -2.73 [unexplained], 1d 3.79%, |z20|=3.35; co-occur[gold_silver] same-direction (channel VALID)
- comex_copper [COMMODITIES]: last 6.75, z20 3.30, zc 0.88, resid-z 1.48 [quiet], 1d 1.99%, |z20|=3.30; 1y-pct=100; co-occur[metal_copper] same-direction (channel VALID)
- stoxx_50 [INDICES]: last 6477.07, z20 2.75, zc -0.15, resid-z -0.25 [quiet], 1d -0.15%, |z20|=2.75; 1y-pct=99
- cac_40 [INDICES]: last 8665.36, z20 2.64, zc -0.02, resid-z -0.14 [quiet], 1d -0.01%, |z20|=2.64; 1y-pct=99
- sp500 [INDICES]: last 7722.12, z20 2.58, zc -0.17, resid-z 3.71 [unexplained], 1d -0.19%, |z20|=2.58; 1y-pct=99
- dyn_vt [EQUITIES]: last 160.14, z20 2.53, zc -0.17, resid-z -0.90 [quiet], 1d -0.19%, |z20|=2.53; 1y-pct=99
- dax [INDICES]: last 26144.19, z20 2.39, zc -0.26, resid-z -0.22 [quiet], 1d -0.22%, |z20|=2.39; 1y-pct=99
- dyn_nvda [EQUITIES]: last 219.20, z20 2.37, zc 1.32, resid-z -1.09 [quiet], 1d 3.43%, |z20|=2.37; 1y-pct=95
- russell_2000 [INDICES]: last 3018.42, z20 2.11, zc -0.46, resid-z -0.60 [quiet], 1d -0.61%, |z20|=2.11; 1y-pct=99
- ftse_100 [INDICES]: last 10894.68, z20 1.40, zc 0.26, resid-z -0.18 [quiet], 1d 0.14%, 1y-pct=98
- gold_silver_ratio [DERIVED]: last 69.11, z20 -0.75, zc n/a, resid-z n/a [quiet], 1d 1.34%, GSR<75 (extreme low)
- **Mechanism**: The recent surge in gold prices is driven by a combination of factors, including a technical breakout and reduced expectations for Federal Reserve rate hikes due to prospects of a deal to reopen the Strait of Hormuz. This has led to a rise in gold and silver prices, with comex_gold and comex_silver showing significant moves. The VALID gold_silver_comove channel suggests that monetary metals are co-moving, and the gold/silver ratio extremes are indicative of rotations.
- **Gap**: No gap: The big raw move in comex_gold is PRICED, with a resid_z of 1.4, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instrument nifty_metal has reacted to the move in comex_silver, with a z20 of 4.14. Other Indian instruments such as nifty_50 and nifty_midcap_100 have also reacted, with z20 values of 1.92 and 1.74, respectively.
- Watch next: comex_gold (up) — already moved; Technical breakout and reduced expectations for Federal Reserve rate hikes
- Watch next: comex_silver (up) — already moved; Co-movement with gold due to VALID gold_silver_comove channel
- Watch next: nifty_metal (up) — already moved; Transmission from comex_silver via metal_copper_channel
- **India receivers**: nifty_fmcg (rho -0.528, z 0.59); nifty_50 (rho 0.524, z 1.92); nifty_midcap_100 (rho 0.519, z 1.74); nifty_metal (rho 0.477, z 4.14)
- Source: Gold Jumps Most Since February on Hormuz, Technical Breakout — Mint Markets, 2026-08-05. https://www.livemint.com/market/gold-jumps-most-since-february-on-hormuz-technical-breakout-11785964080778.html
- Source: Aggressive options trading helped drive the S&P 500’s latest rally. What that means for investors. — MarketWatch Top, 2026-08-05. https://www.marketwatch.com/story/aggressive-options-trading-helped-drive-the-s-p-500s-latest-rally-what-that-means-for-investors-623fe41c?mod=mw_rss_topstories
- Source: Philippines Could Become the World's First Geologic Hydrogen Hub — OilPrice, 2026-08-05. https://oilprice.com/Energy/Energy-General/Philippines-Could-Become-the-Worlds-First-Geologic-Hydrogen-Hub.html
- Historical analogues: 2024-11-26 (d=1.04), 2025-10-31 (d=1.11), 2024-10-15 (d=1.12)

### [RED 6.86] usd_inr ↓
- usd_inr [FX]: last 95.11, z20 -1.86, zc -0.55, resid-z -0.72 [quiet], 1d -0.24%, 20d range extreme; |z20|=1.86
- **Mechanism**: The recent decline in usd_inr is largely priced, given the small resid_z of -0.66, which suggests that the move is mostly explained by factor exposures. The drop in oil prices and a weakening dollar have contributed to the rupee's strength. However, the RBI's decision to maintain rates has restricted further growth. The valid channels, such as gold_silver_comove and metal_copper_channel, do not directly influence the usd_inr move, but the risk-on regime and the inverse safe_haven_gold channel indicate a broader market sentiment that supports the rupee's strength.
- **Gap**: No gap: the usd_inr move is largely priced, with a small resid_z and a big raw move, indicating that the market has already accounted for the factors driving the decline.
- **India take**: The Indian instrument dyn_havells_ns has already reacted to the usd_inr move, given its rho of 0.415. Other transmission candidates, such as dyn_bharatcoal_ns and eur_inr, remain quiet for now.
- Watch next: dyn_havells_ns (up) — already moved; rho=0.415 via usd_inr
- **India receivers**: dyn_havells_ns (rho 0.415, z 2.06); dyn_bharatcoal_ns (rho 0.408, z -0.99); eur_inr (rho 0.378, z 0.65)
- Source: Rupee hits one-month closing high as oil slide outweighs RBI pause — ET Markets, 2026-08-05. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-hits-one-month-closing-high-as-oil-slide-outweighs-rbi-pause/articleshow/132916592.cms
- Source: Rupee sails past 95 to one-month high, premiums drop before RBI decision — ET Markets, 2026-08-05. https://economictimes.indiatimes.com/markets/forex/rupee-sails-past-95-to-one-month-high-premiums-drop-before-rbi-decision/articleshow/132890285.cms
- Source: Rupee jumps 39 paise to 94.89 against US dollar ahead of RBI monetary policy decision — BusinessLine Mkts, 2026-08-05. https://www.thehindubusinessline.com/markets/forex/rupee-jumps-39-paise-to-9489-against-us-dollar-ahead-of-rbi-monetary-policy-decision/article71308047.ece
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2024-10-24 (d=0.01)

### [RED 5.77] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1467.00, z20 3.77, zc 0.35, resid-z 0.30 [quiet], 1d 1.14%, |z20|=3.77; 1y-pct=100
- **Mechanism**: The recent surge in Ather Energy's stock price can be attributed to the company's narrowing quarterly loss, which has ignited investor interest. The stock's move is largely priced, given the small resid_z value of 0.09, indicating that the move is largely explained by factor exposures. The VALID metal_copper_channel may also be contributing to the stock's upward momentum, as global copper leads Indian metal equities.
- **Gap**: No gap: the stock's move is largely priced, with a small resid_z value and a significant portion of the move explained by factor exposures
- **India take**: The Indian instrument that expresses this move is the Nifty Metal index, which may react positively to the surge in Ather Energy's stock price. However, the reaction is not yet evident, and the index is still watching for further developments.
- Watch next: nifty_50 (up) — not yet - watch; Risk-on regime and potential co-movement with metal equities
- Source: Ather Energy shares jump 14% after Q1 loss narrows — BusinessLine Mkts, 2026-08-04. https://www.thehindubusinessline.com/markets/ather-energy-shares-jump-18-to-fresh-52-week-high-after-q1-loss-narrows/article71303894.ece
- Source: Ather Energy's tapering losses put stock in fast lane, but is the rally justified? — Mint Markets, 2026-08-04. https://www.livemint.com/market/mark-to-market/ather-energy-electric-vehicles-ev-q1fy27-ebitda-operating-losses-ev-sales-hero-motocorp-11785824423599.html
- Source: Multibagger stock Ather Energy share price soars 18% to record high post Q1 FY27 results: Should you buy? — Mint Markets, 2026-08-04. https://www.livemint.com/market/stock-market-news/multibagger-stock-ather-energy-share-price-soars-18-to-record-high-post-q1-fy27-results-should-you-buy-11785824415092.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [AMBER 5.43] cross-asset · 3 series ↑
- dyn_jiofin_bo [EQUITIES]: last 261.50, z20 2.11, zc -0.53, resid-z -0.94 [quiet], 1d -1.15%, |z20|=2.11
- nifty_50 [INDICES]: last 24624.65, z20 1.92, zc 0.05, resid-z -0.11 [quiet], 1d 0.04%, |z20|=1.92
- nifty_midcap_100 [INDICES]: last 63597.60, z20 1.74, zc 0.23, resid-z 0.10 [quiet], 1d 0.18%, |z20|=1.74; 1y-pct=99
- **Mechanism**: The recent move in smallcap stocks, particularly the Nifty Midcap 100, may propagate through the metal_copper_channel, given its VALID status and the strong correlation between global copper and Indian metal equities. The Nifty Midcap 100's 1.74 z20 level and the Nifty Smallcap 100's record high suggest a potential rotation into smaller stocks. However, the resid_z values for the Nifty 50 and Nifty Midcap 100 are relatively low, indicating that the move may be largely priced in.
- **Gap**: No gap: the recent move in smallcap stocks is largely priced in, given the low resid_z values for the Nifty 50 and Nifty Midcap 100
- **India take**: The Indian instruments that express this move are the Nifty Midcap 100 and the Nifty Smallcap 100, which have already reacted to the move. Other related instruments, such as dyn_muthootfin_ns and nifty_metal, have also reacted.
- Watch next: dyn_muthootfin_ns (up) — already moved; reacted to Nifty Midcap 100 move
- Watch next: dyn_indianb_ns (up) — already moved; reacted to Nifty Midcap 100 move
- Watch next: nifty_metal (up) — already moved; reacted to Nifty Midcap 100 move
- **India receivers**: dyn_muthootfin_ns (rho 0.695, z -2.07); dyn_bharatcoal_ns (rho 0.641, z -0.99); dyn_indianb_ns (rho 0.62, z 1.07); dyn_indusindbk_bo (rho 0.619, z 0.04)
- Source: US JULY ISM SERVICES PMI RISES TO 54.1 FROM 54; EST. 54.5 — DeItaone, 2026-08-05. https://t.me/walter_bloomberg/34400
- Source: US S&P JULY SERVICES PMI AT 54.6 VS 51.2 PRIOR *US S&P JULY COMPOSITE PMI AT 54.5 VS 51.9 PRIOR — DeItaone, 2026-08-05. https://t.me/walter_bloomberg/34399
- Source: Smallcaps hit all-time high even as Nifty, Sensex remain directionless — BusinessLine Mkts, 2026-08-05. https://www.thehindubusinessline.com/markets/smallcaps-hit-all-time-high-as-nifty-treads-water/article71309640.ece
- Historical analogues: 2025-07-17 (d=0.69), 2024-11-07 (d=0.98), 2025-08-13 (d=1.26)

### [RED 5.4] cross-asset · 2 series ↑
- usd_jpy [FX]: last 157.69, z20 -2.56, zc 0.19, resid-z 0.21 [quiet], 1d 0.10%, |z20|=2.56
- dyn_amzn [EQUITIES]: last 272.60, z20 1.69, zc -0.74, resid-z -1.63 [unexplained], 1d -1.74%, 1y-pct=97
- **Mechanism**: The recent move in usd_jpy and dyn_amzn is driven by a cross-asset event, with the Japanese yen firming after a landmark intervention and the dollar hovering near six-week lows against major peers. The move in usd_jpy has a low resid_z, indicating that it is largely priced in, while the move in dyn_amzn has a higher resid_z, suggesting some unexplained component. The valid vix_equity_inverse channel suggests that the vol spike may lead to an equity drawdown.
- **Gap**: No gap: the move in usd_jpy has a low resid_z, indicating that it is largely priced in, and the move in dyn_amzn, although having a higher resid_z, is still within the realm of explained moves given the cross-asset event
- **India take**: The Indian instrument dyn_muthootfin_ns has already reacted, with a rho of -0.507 via usd_jpy, while dyn_cartrade_ns remains quiet, with a rho of -0.358 via dyn_amzn. The metal_copper_channel may also transmit to Indian metal equities.
- Watch next: taiwan_weighted (down) — not yet - watch; historically leads usd_jpy by 1d
- **India receivers**: dyn_muthootfin_ns (rho -0.507, z -2.07); dyn_cartrade_ns (rho -0.358, z 0.63)
- Source: Yen firms after landmark intervention, dollar near lows on optimism over Iran talks — Mint Markets, 2026-08-05. https://www.livemint.com/market/yen-firms-after-landmark-intervention-dollar-near-lows-on-optimism-over-iran-talks-11785963413851.html
- Source: BOFA ANTICIPATE STRONGER JAPANESE YEN FOLLOWING INTERVENTION, CHANGE YEAR END DOLLAR/YEN FORECAST TO 149 FROM 152 - CURRENTLY TRADES AT 157.7 — DeItaone, 2026-08-05. https://t.me/walter_bloomberg/34369
- Source: US TREASURY SECRETARY BESSENT: UPTICK IN JAPAN'S INFLATION WAS RESULT OF WEAK YEN, ENERGY PRICES — DeItaone, 2026-08-04. https://t.me/walter_bloomberg/34358
- Historical analogues: 2024-10-16 (d=0.15), 2024-11-21 (d=0.23), 2026-03-31 (d=0.24)

### [RED 5.26] dyn_pltr ↑
- dyn_pltr [EQUITIES]: last 158.43, z20 3.26, zc -0.51, resid-z 8.43 [unexplained], 1d -2.60%, |z20|=3.26
- **Mechanism**: The recent surge in Palantir's stock price, driven by strong Q2 results and AI-fueled rally, has led to a short squeeze, resulting in $3 billion in losses for short sellers. This move is priced, with a relatively small resid_z of -0.24, indicating that the factor exposures can explain most of the move. The valid vix_equity_inverse channel suggests that the equity market's upside is accompanied by a decrease in volatility, which is consistent with the current RISK_ON regime.
- **Gap**: No gap: the move in dyn_pltr is largely explained by its factor exposures, with a small resid_z, indicating that the price move is consistent with the current market regime and channels.
- **India take**: The Indian transmission candidate, dyn_atherenerg_ns, has already reacted to the move in dyn_pltr, given its rho of 0.393. The metal_copper_channel, which is valid, may also influence Indian metal equities.
- Watch next: dyn_atherenerg_ns (up) — already moved; rho=0.393 with dyn_pltr
- **India receivers**: dyn_atherenerg_ns (rho 0.393, z 3.77)
- Source: Why is Wall Street ignoring the controversy surrounding Palantir? Expert says 'It's not a referendum on ethics' — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/why-is-wall-street-ignoring-the-controversy-surrounding-palantir-expert-says-its-not-a-referendum-on-ethics-11785936805785.html
- Source: Michael Burry warns of 1987-style crash as AI rally powers Wall Street; investor shorts Nvidia, Tesla, Palantir — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/michael-burry-warns-of-1987-style-crash-as-ai-rally-powers-wall-street-investor-shorts-nvidia-tesla-palantir-11785922333250.html
- Source: Palantir Short Sellers Take $3 Billion Hit After 30% Stock Surge — Mint Markets, 2026-08-04. https://www.livemint.com/market/palantir-short-sellers-take-3-billion-hit-after-30-stock-surge-11785872351134.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-01 (d=0.08), 2025-10-13 (d=0.13)

### [RED 5.17] dxy ↓
- dxy [FX]: last 99.69, z20 -2.17, zc -0.56, resid-z 0.43 [quiet], 1d -0.20%, 20d range extreme; |z20|=2.17
- **Mechanism**: The recent decline in the US Dollar Index (DXY) may propagate through the VALID gold_silver_comove channel, potentially leading to a move in monetary metals. However, the INVERTED safe_haven_gold channel suggests that the usual risk-off safe-haven bid for gold may not be present. The VALID metal_copper_channel could also play a role, as global copper leads Indian metal equities.
- **Gap**: No gap: The big raw move in DXY has a small resid_z of -0.92, indicating that the move is largely priced in and not an anomaly.
- **India take**: The Indian instrument that expresses this move is likely to be the MCX Gold or MCX Copper, but the weak dxy_inr_channel and inr_oil_channel suggest that the transmission to Indian markets may be limited. The metal_copper_channel, however, could lead to a move in Indian metal equities.
- Watch next: comex_gold (down) — not yet - watch; Historical analogues show a median decline of 1.82% in Comex gold prices 20 days after a similar DXY decline
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [AMBER 4.56] cross-asset · 4 series ↑
- ust_30y [RATES]: last 5.18, z20 0.89, zc -1.24, resid-z -0.09 [quiet], 1d -0.96%, 1y-pct=98
- tips_10y_real [RATES]: last 2.40, z20 0.53, zc -0.74, resid-z 0.20 [quiet], 1d -1.23%, 1y-pct=96
- dyn_bond [EQUITIES]: last 90.87, z20 -0.26, zc 0.11, resid-z 1.91 [unexplained], 1d 0.03%, 1y-pct=4
- ust_10y [RATES]: last 4.63, z20 0.13, zc -1.54, resid-z -0.59 [priced], 1d -1.49%, 1y-pct=96
- **Mechanism**: The recent decline in US Treasury yields, driven by easing oil prices and reduced expectations of a Federal Reserve interest rate hike, is propagating through the valid gold_silver_comove and metal_copper_channel, potentially influencing Indian metal equities. However, the primary driver of the move is the priced decline in Treasury yields, with the majority of the move explained by factor exposures.
- **Gap**: No gap: The decline in US Treasury yields is largely explained by factor exposures, with the majority of the move being priced in.
- **India take**: Indian government bond yields are trading flat ahead of the RBI MPC meeting outcome, but may react to the decline in US Treasury yields through the metal_copper_channel, potentially influencing Indian metal equities such as the Nifty Metal index.
- Watch next: dyn_bond (down) — not yet - watch; High resid_z value indicates an unexplained move
- Source: Treasury yields fall as oil dips on Strait of Hormuz hopes — Mint Markets, 2026-08-05. https://www.livemint.com/market/treasury-yields-fall-as-oil-dips-on-strait-of-hormuz-hopes-11785956691711.html
- Source: US Treasury yields fall as oil retreats on Iran deal hopes, Fed hike bets ease — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-treasury-yields-fall-as-oil-retreats-on-iran-deal-hopes-fed-hike-bets-ease/articleshow/132871326.cms
- Source: Indian bond yields trades flat ahead of RBI MPC meeting outcome. Experts decode the outlook — Mint Markets, 2026-08-04. https://www.livemint.com/market/stock-market-news/indian-bond-yields-trades-flat-ahead-of-rbi-mpc-meeting-outcome-experts-decode-the-outlook-11785831046953.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

## Watchlist (below surfacing floor)
dyn_msft ↑ (4.31), fx · 3 series ↑ (4.18), nifty_metal ↑ (4.14), dyn_thangamayl_ns ↓ (4.1), dyn_bac ↑ (3.78), dyn_lth ↑ (3.65), natgas ↓ (3.58), dyn_coin ↓ (3.5), asx_200 ↑ (3.41), dyn_cupid_ns ↑ (3.22), dyn_tech ↑ (2.87), usd_cny ↓ (2.56)

## India macro
- nifty_50: 24624.6504 (1d 0.04%, z20 1.92, flag amber)
- nifty_midcap_100: 63597.6016 (1d 0.18%, z20 1.74, flag amber)
- usd_inr: 95.1070 (1d -0.24%, z20 -1.86, flag red)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5827 (1d 0.14%, z20 -0.62, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI MPC decision T-2d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 81.3 — "Hormuz Bottleneck Pushes Indian Refiners Toward West African Grades"
- COALINDIA.NS (COAL INDIA LTD) score 79.1 — "Hormuz Bottleneck Pushes Indian Refiners Toward West African Grades"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 78.4 — "Hormuz Bottleneck Pushes Indian Refiners Toward West African Grades"
- INDIANB.NS (INDIAN BANK) score 62.1 — "BOFA CEO BACKS THREE FED RATE HIKES Bank of America CEO Brian Moynihan reiterated the bank"
- COIN (Coinbase Global, Inc.) score 52.4 — "Hormuz Crisis Is Rewriting the Global LPG Trade"
- TECHM.NS (TECH MAHINDRA LIMITED) score 48.6 — "Big Tech Turns to Fuel Cells to Power the AI Boom"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 47.4 — "Big Tech Turns to Fuel Cells to Power the AI Boom"
- BAC (Bank of America Corporation) score 46.5 — "BOFA CEO BACKS THREE FED RATE HIKES Bank of America CEO Brian Moynihan reiterated the bank"
- OHI (Omega Healthcare Investors, In) score 46.3 — "Aggressive options trading helped drive the S&P 500’s latest rally. What that means for in"
- HDB (HDFC Bank Limited) score 44.2 — "BOFA CEO BACKS THREE FED RATE HIKES Bank of America CEO Brian Moynihan reiterated the bank"
- TECH (Bio-Techne Corp) score 43.0 — "Big Tech Turns to Fuel Cells to Power the AI Boom"
- IDBI.NS (IDBI BANK LIMITED) score 43.0 — "BOFA CEO BACKS THREE FED RATE HIKES Bank of America CEO Brian Moynihan reiterated the bank"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 43.0 — "BOFA CEO BACKS THREE FED RATE HIKES Bank of America CEO Brian Moynihan reiterated the bank"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 41.5 — "BOFA CEO BACKS THREE FED RATE HIKES Bank of America CEO Brian Moynihan reiterated the bank"
- LTH (Life Time Group Holdings, Inc.) score 34.5 — "Bitcoin stabilizes above $64K as macro sentiment improves; Ethereum recovery remains weake"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 29.9 — "DIMON PUSHES AI SECURITY ALLIANCE JPMorgan CEO Jamie Dimon is urging more than 40 companie"
- CHKP (Check Point Software Technolog) score 29.5 — "Tips Music announces Rs 44 crore buyback at 12% premium. Check details"
- 301077.SZ (CHINASTARS) score 26.2 — "China Accelerates Its Economic Push Across Central Asia"
- BOND (PIMCO Active Bond Exchange-Tra) score 19.4 — "India bonds rally on 'dovish' RBI hold, lower oil prices"
- JUSTDIAL.BO (JUST DIAL LTD.) score 15.4 — "Missouri voters just rejected a bid to ditch income tax, while other tax votes loom in Flo"
- MS (Morgan Stanley) score 13.0 — "SPCX : JP MORGAN RAISES TARGET PRICE TO $240 FROM $225"
- JIOFIN.BO (Jio Financial Services Limited) score 12.5 — "US S&P JULY SERVICES PMI AT 54.6 VS 51.2 PRIOR *US S&P JULY COMPOSITE PMI AT 54.5 VS 51.9 "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.1 — "Top Gainers & Losers on 5 August: Hindustan Copper, OLA, HFCL, Mphasis, Tata Capital among"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 10.0 — "Market wrap: Shriram Finance, Grasim, TCS among top gainers and losers on Nifty and Sensex"
- VT (Vanguard Total World Stock Ind) score 9.2 — "Philippines Could Become the World's First Geologic Hydrogen Hub"
- PCJEWELLER.NS (PC JEWELLER LTD) score 8.7 — "Kalyan Jewellers shares extend slide, tumble 5% after Q1 results; down 11% in four days"
- PLTR (Palantir Technologies Inc.) score 8.2 — "Why is Wall Street ignoring the controversy surrounding Palantir? Expert says 'It's not a "
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.2 — "Vodafone Idea sets AGM date to declare financial statement for FY26. Details here"
- AMZN (Amazon.com, Inc.) score 8.2 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 8.1 — "Oil Ministry to deploy tactical teams for petrol pump inspections, says Team Bharat"
- NVDA (NVIDIA Corporation) score 7.5 — "NVDA - NVIDIA SHARES HIT HIGHEST IN OVER TWO MONTHS, LAST UP 4.3%"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.3 — "Adani Ent Share Price Live Updates: Adani Ent. News"
- MSFT (Microsoft Corporation) score 6.8 — "OPENAI DRIVES MOST OF MICROSOFT'S AI REVENUE Microsoft disclosed it generated $24.1 billio"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.5 — "HSBC picks ICICI Bank, Titan, 8 other stocks to ride a potential $25 billion FII inflow as"
- AAPL (Apple Inc.) score 6.2 — "AAPL - APPLE RAMPS UP FOR NEXT IPHONE Bank of America reiterated its Buy rating and $380 p"
- META (Meta) score 6.0 — "Explained: Why South Korea bought gold after 13 years and what it means for yellow metal i"
- GS (Goldman Sachs Group, Inc. (The) score 5.3 — "GOLDMAN STICKS TO PAYROLL FORECAST Goldman Sachs maintained its 75,000 July nonfarm payrol"
- INFY (Infosys Limited) score 4.4 — "Infosys Share Price Live Updates: Infosys Stock Details"
- THANGAMAYL.NS (THANGAMAYIL JEWELLERY LTD) score 2.5 — "Thangamayil share selloff continues: Stock drops 5% despite Rs 344 crore sales in first 3 "
- CUPID.NS (CUPID LIMITED) score 0.4 — "Cupid increases investment by $5 million in GII’s Healthcare-focused platform"

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