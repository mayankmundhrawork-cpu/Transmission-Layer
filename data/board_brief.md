# Transmission Layer — board brief · 2026-08-05 17:53Z

data as of **2026-08-05** · 98 series · 22 red / 25 amber · 8 events surfaced (20 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.3, 3d in regime; vol-pct 0.365, breadth-off 0.235, Markov P(high-vol) 0.053)
- [INVERTED] **safe_haven_gold** — corr20 -0.39, corr60 -0.41, contra nifty_50 corr20=0.09, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.87, corr60 0.81, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.41, corr60 0.34, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.22, corr60 -0.05, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.79, corr60 -0.8, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.03, corr60 -0.02, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.18, corr60 -0.25, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.14, corr60 0.18, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 90** scanned series survive multiplicity control (effective p ≤ 0.0010380708664139426)
- **SETUP** dyn_nvda → dyn_453950_ks: leads 1d (ccf 0.535, β 0.3772, p 0.0); driver zc 1.67 → expected 1.634%. Type hit-rate 0.821 (n=2921).
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.484, β 0.2629, p 0.0); driver zc 1.58 → expected 0.393%. Type hit-rate 0.821 (n=2921).
- **SETUP** ust_10y → eur_usd: leads 1d (ccf -0.28, β -0.1137, p 0.0); driver zc 1.58 → expected -0.17%. Type hit-rate 0.821 (n=2921).
- **SETUP** ust_10y → gbp_usd: leads 1d (ccf -0.28, β -0.1138, p 0.0); driver zc 1.58 → expected -0.17%. Type hit-rate 0.821 (n=2921).
- **SETUP** tips_10y_real → gbp_usd: leads 1d (ccf -0.25, β -0.0562, p 4e-05); driver zc 1.57 → expected -0.14%. Type hit-rate 0.821 (n=2921).
- Track record · residual_reversion: hit-rate **0.494** (n=1156) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.821** (n=2921) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 11.13] cross-asset · 13 series ↑
- comex_gold [COMMODITIES]: last 4309.90, z20 6.05, zc 3.63, resid-z -1.68 [unexplained], 1d 5.24%, |z20|=6.05; co-occur[gold_silver] same-direction (channel VALID)
- dow_jones [INDICES]: last 54585.02, z20 4.10, zc 0.81, resid-z 1.44 [quiet], 1d 0.92%, |z20|=4.10; 1y-pct=100
- comex_silver [COMMODITIES]: last 62.40, z20 3.41, zc 1.43, resid-z -2.73 [unexplained], 1d 3.91%, |z20|=3.41; co-occur[gold_silver] same-direction (channel VALID)
- comex_copper [COMMODITIES]: last 6.74, z20 3.20, zc 0.80, resid-z 1.10 [quiet], 1d 1.80%, |z20|=3.20; 1y-pct=100; co-occur[metal_copper] same-direction (channel VALID)
- sp500 [INDICES]: last 7741.68, z20 2.80, zc 0.06, resid-z 0.82 [quiet], 1d 0.07%, |z20|=2.80; 1y-pct=100
- dyn_vt [EQUITIES]: last 160.59, z20 2.79, zc 0.07, resid-z -2.02 [unexplained], 1d 0.08%, |z20|=2.79; 1y-pct=100
- stoxx_50 [INDICES]: last 6477.07, z20 2.75, zc -0.15, resid-z -0.50 [quiet], 1d -0.15%, |z20|=2.75; 1y-pct=99
- dyn_nvda [EQUITIES]: last 221.12, z20 2.68, zc 1.67, resid-z 0.55 [priced], 1d 4.33%, |z20|=2.68; 1y-pct=97
- cac_40 [INDICES]: last 8665.36, z20 2.64, zc -0.02, resid-z -0.36 [quiet], 1d -0.01%, |z20|=2.64; 1y-pct=99
- russell_2000 [INDICES]: last 3029.29, z20 2.51, zc -0.19, resid-z -0.50 [quiet], 1d -0.25%, |z20|=2.51; 1y-pct=99
- dax [INDICES]: last 26144.19, z20 2.39, zc -0.26, resid-z -0.42 [quiet], 1d -0.22%, |z20|=2.39; 1y-pct=99
- ftse_100 [INDICES]: last 10894.68, z20 1.40, zc 0.26, resid-z -0.21 [quiet], 1d 0.14%, 1y-pct=98
- gold_silver_ratio [DERIVED]: last 69.06, z20 -0.80, zc n/a, resid-z n/a [quiet], 1d 1.28%, GSR<75 (extreme low)
- **Mechanism**: The recent surge in gold and silver prices, driven by optimism over a potential US-Iran diplomatic breakthrough and a weaker US dollar, has created a ripple effect in the global markets. The VALID gold_silver_comove channel and metal_copper_channel are transmitting this move to other assets, including Indian metal equities. However, the INVERTED safe_haven_gold channel suggests that the risk-off safe-haven bid is not driving the gold price up, but rather the monetary metals co-move and global copper leads are.
- **Gap**: No gap: The big raw move in gold and silver prices is largely priced in, with resid_z values of -1.68 and -2.73, respectively, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian metal equities, such as those in the Nifty Metal index, have already reacted to the surge in gold and silver prices, with a z20 value of 4.14. The Nifty 50 index has also reacted, with a z20 value of 1.92.
- Watch next: nifty_metal (up) — reacted; rho=0.478 via comex_silver, z20=4.14
- Watch next: nifty_50 (up) — reacted; rho=0.524 via cac_40, z20=1.92
- **India receivers**: nifty_fmcg (rho -0.525, z 0.59); nifty_50 (rho 0.524, z 1.92); nifty_midcap_100 (rho 0.519, z 1.74); nifty_metal (rho 0.478, z 4.14)
- Source: Gold, silver prices today: Comex gold jumps $173, silver hits $63 as US-Iran peace hopes lift sentiment — Mint Markets, 2026-08-05. https://www.livemint.com/market/commodities/gold-silver-prices-today-comex-gold-jumps-173-silver-hits-63-as-us-iran-peace-hopes-lift-sentiment-11785946064993.html
- Source: SpaceX’s stock falls as Wall Street gets spooked by the extent of AI spending — MarketWatch Top, 2026-08-05. https://www.marketwatch.com/story/spacexs-stock-falls-as-wall-street-gets-spooked-by-the-extent-of-ai-spending-9ce9ddb8?mod=mw_rss_topstories
- Source: Nvidia’s stock is basking in the glow of a high-profile endorsement — MarketWatch Top, 2026-08-05. https://www.marketwatch.com/story/nvidias-stock-is-basking-in-the-glow-of-a-high-profile-endorsement-b7c48e7b?mod=mw_rss_topstories
- Historical analogues: 2024-11-26 (d=1.04), 2025-10-31 (d=1.11), 2024-10-15 (d=1.12)

### [RED 6.86] usd_inr ↓
- usd_inr [FX]: last 95.11, z20 -1.86, zc -0.54, resid-z -0.71 [quiet], 1d -0.23%, 20d range extreme; |z20|=1.86
- **Mechanism**: The recent decline in usd_inr is largely priced, given the small resid_z of -0.66, which suggests that the move is mostly explained by factor exposures. The drop in oil prices and a weakening dollar have contributed to the rupee's strength. However, the RBI's decision to maintain rates has restricted further growth. The valid channels, such as gold_silver_comove and metal_copper_channel, do not directly influence the usd_inr move, but the risk-on regime and the inverse safe_haven_gold channel indicate a broader market sentiment that supports the rupee's strength.
- **Gap**: No gap: the usd_inr move is largely priced, with a small resid_z and a big raw move, indicating that the market has already accounted for the factors driving the decline.
- **India take**: The Indian instrument dyn_havells_ns has already reacted to the usd_inr move, given its rho of 0.415. Other transmission candidates, such as dyn_bharatcoal_ns and eur_inr, remain quiet for now.
- Watch next: dyn_havells_ns (up) — already moved; rho=0.415 via usd_inr
- **India receivers**: dyn_havells_ns (rho 0.415, z 2.06); dyn_bharatcoal_ns (rho 0.408, z -0.99); eur_inr (rho 0.379, z 0.63)
- Source: Rupee hits one-month closing high as oil slide outweighs RBI pause — ET Markets, 2026-08-05. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-hits-one-month-closing-high-as-oil-slide-outweighs-rbi-pause/articleshow/132916592.cms
- Source: Rupee sails past 95 to one-month high, premiums drop before RBI decision — ET Markets, 2026-08-05. https://economictimes.indiatimes.com/markets/forex/rupee-sails-past-95-to-one-month-high-premiums-drop-before-rbi-decision/articleshow/132890285.cms
- Source: Rupee jumps 39 paise to 94.89 against US dollar ahead of RBI monetary policy decision — BusinessLine Mkts, 2026-08-05. https://www.thehindubusinessline.com/markets/forex/rupee-jumps-39-paise-to-9489-against-us-dollar-ahead-of-rbi-monetary-policy-decision/article71308047.ece
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2024-10-24 (d=0.01)

### [RED 5.77] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1467.00, z20 3.77, zc 0.35, resid-z 0.28 [quiet], 1d 1.14%, |z20|=3.77; 1y-pct=100
- **Mechanism**: The recent surge in Ather Energy's stock price can be attributed to the company's narrowing quarterly loss, which has ignited investor interest. The stock's move is largely priced, given the small resid_z value of 0.09, indicating that the move is largely explained by factor exposures. The VALID metal_copper_channel may also be contributing to the stock's upward momentum, as global copper leads Indian metal equities.
- **Gap**: No gap: the stock's move is largely priced, with a small resid_z value and a significant portion of the move explained by factor exposures
- **India take**: The Indian instrument that expresses this move is the Nifty Metal index, which may react positively to the surge in Ather Energy's stock price. However, the reaction is not yet evident, and the index is still watching for further developments.
- Watch next: nifty_50 (up) — not yet - watch; Risk-on regime and potential co-movement with metal equities
- Source: Ather Energy shares jump 14% after Q1 loss narrows — BusinessLine Mkts, 2026-08-04. https://www.thehindubusinessline.com/markets/ather-energy-shares-jump-18-to-fresh-52-week-high-after-q1-loss-narrows/article71303894.ece
- Source: Ather Energy's tapering losses put stock in fast lane, but is the rally justified? — Mint Markets, 2026-08-04. https://www.livemint.com/market/mark-to-market/ather-energy-electric-vehicles-ev-q1fy27-ebitda-operating-losses-ev-sales-hero-motocorp-11785824423599.html
- Source: Multibagger stock Ather Energy share price soars 18% to record high post Q1 FY27 results: Should you buy? — Mint Markets, 2026-08-04. https://www.livemint.com/market/stock-market-news/multibagger-stock-ather-energy-share-price-soars-18-to-record-high-post-q1-fy27-results-should-you-buy-11785824415092.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [AMBER 5.76] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.23, z20 1.83, zc 1.53, resid-z 1.91 [unexplained], 1d -0.76%, |z20|=1.83; 1y-pct=99
- ust_10y [RATES]: last 4.70, z20 1.32, zc 1.58, resid-z 2.16 [unexplained], 1d -1.05%, 1y-pct=99
- tips_10y_real [RATES]: last 2.43, z20 1.16, zc 1.57, resid-z 2.22 [unexplained], 1d -1.62%, 1y-pct=98
- ust_2y [RATES]: last 4.25, z20 0.31, zc 0.93, resid-z 1.54 [unexplained], 1d -0.70%, 1y-pct=96
- dyn_bond [EQUITIES]: last 90.88, z20 -0.23, zc 0.14, resid-z 0.50 [quiet], 1d 0.04%, 1y-pct=4
- **Mechanism**: The recent decline in US Treasury yields, triggered by easing inflation worries and reduced expectations of a Federal Reserve interest rate hike, is propagating through the VALID gold_silver_comove and metal_copper_channel, influencing Indian metal equities. The transmission setup ust_10y -> usd_jpy, with a lead of 1 day and a beta of 0.2629, also supports this mechanism.
- **Gap**: No gap: The big raw move in US Treasury yields is largely priced, with resid_z values indicating that the moves are mostly explained by factor exposures.
- **India take**: The Indian 10-year government bond yield, currently at 6.8346%, may react to the decline in US Treasury yields, potentially leading to a decrease in Indian bond yields. However, the RBI's monetary policy decision and the large state bond auction may influence the outcome.
- Watch next: nifty_50 (down) — not yet - watch; Risk-off sentiment may lead to a decline in Indian equities
- Source: US Treasury yields fall as oil retreats on Iran deal hopes, Fed hike bets ease — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-treasury-yields-fall-as-oil-retreats-on-iran-deal-hopes-fed-hike-bets-ease/articleshow/132871326.cms
- Source: Indian bond yields trades flat ahead of RBI MPC meeting outcome. Experts decode the outlook — Mint Markets, 2026-08-04. https://www.livemint.com/market/stock-market-news/indian-bond-yields-trades-flat-ahead-of-rbi-mpc-meeting-outcome-experts-decode-the-outlook-11785831046953.html
- Source: Global Market: Japan's 10-year bond yield climbs after weak auction signals soft demand — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-10-year-bond-yield-climbs-after-weak-auction-signals-soft-demand/articleshow/132852095.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [AMBER 5.43] cross-asset · 3 series ↑
- dyn_jiofin_bo [EQUITIES]: last 261.50, z20 2.11, zc -0.53, resid-z -0.93 [quiet], 1d -1.15%, |z20|=2.11
- nifty_50 [INDICES]: last 24624.65, z20 1.92, zc 0.05, resid-z -0.10 [quiet], 1d 0.04%, |z20|=1.92
- nifty_midcap_100 [INDICES]: last 63597.60, z20 1.74, zc 0.23, resid-z 0.11 [quiet], 1d 0.18%, |z20|=1.74; 1y-pct=99
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
- usd_jpy [FX]: last 157.69, z20 -2.57, zc 0.18, resid-z 0.22 [quiet], 1d 0.10%, |z20|=2.57
- dyn_amzn [EQUITIES]: last 271.77, z20 1.63, zc -0.87, resid-z 9.76 [unexplained], 1d -2.04%, 1y-pct=96
- **Mechanism**: The recent intervention by Tokyo has led to a sharp move in usd_jpy, which has not been fully explained by factor exposures, as evidenced by a resid_z of 0.22. This move is likely to propagate through the verified transmission setup of ust_10y -> usd_jpy, which has a lead-lag relationship with a ccf of 0.484. The RISK_ON regime and the VALID vix_equity_inverse channel also support this propagation.
- **Gap**: No gap: the big raw move in usd_jpy has a small resid_z, indicating that it is PRICED, not an anomaly.
- **India take**: The Indian instrument dyn_muthootfin_ns has already reacted to the move in usd_jpy, given its rho of -0.507. However, dyn_cartrade_ns, which is correlated with dyn_amzn, remains quiet.
- Watch next: dyn_amzn (up) — already moved; unexplained move with high resid_z
- **India receivers**: dyn_muthootfin_ns (rho -0.507, z -2.07); dyn_cartrade_ns (rho -0.358, z 0.63)
- Source: BOFA ANTICIPATE STRONGER JAPANESE YEN FOLLOWING INTERVENTION, CHANGE YEAR END DOLLAR/YEN FORECAST TO 149 FROM 152 - CURRENTLY TRADES AT 157.7 — DeItaone, 2026-08-05. https://t.me/walter_bloomberg/34369
- Source: US TREASURY SECRETARY BESSENT: UPTICK IN JAPAN'S INFLATION WAS RESULT OF WEAK YEN, ENERGY PRICES — DeItaone, 2026-08-04. https://t.me/walter_bloomberg/34358
- Source: Yen holds most gains as intervention keeps speculators on edge — Mint Markets, 2026-08-04. https://www.livemint.com/market/yen-holds-most-gains-as-intervention-keeps-speculators-on-edge-11785874259298.html
- Historical analogues: 2024-10-16 (d=0.15), 2024-11-21 (d=0.23), 2026-03-31 (d=0.24)

### [RED 5.32] dyn_pltr ↑
- dyn_pltr [EQUITIES]: last 159.00, z20 3.32, zc -0.44, resid-z -0.24 [quiet], 1d -2.25%, |z20|=3.32
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
- dxy [FX]: last 99.69, z20 -2.17, zc -0.55, resid-z -0.92 [quiet], 1d -0.20%, 20d range extreme; |z20|=2.17
- **Mechanism**: dxy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.505 vs dxy, historically leads by 3d
- Watch next: eth_usd (inverse) — not yet - watch; rho -0.518 vs dxy
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

## Watchlist (below surfacing floor)
dyn_msft ↑ (4.35), nifty_metal ↑ (4.14), dyn_thangamayl_ns ↓ (4.1), fx · 3 series ↑ (4.08), dyn_bac ↑ (4.03), dyn_lth ↑ (3.42), asx_200 ↑ (3.41), dyn_cupid_ns ↑ (3.22), dyn_coin ↓ (3.09), dyn_tech ↑ (3.09), usd_cny ↓ (2.8), dyn_icicigi_bo ↓ (2.18)

## India macro
- nifty_50: 24624.6504 (1d 0.04%, z20 1.92, flag amber)
- nifty_midcap_100: 63597.6016 (1d 0.18%, z20 1.74, flag amber)
- usd_inr: 95.1100 (1d -0.23%, z20 -1.86, flag red)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5827 (1d 0.14%, z20 -0.62, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI MPC decision T-2d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 85.0 — "Hormuz Bottleneck Pushes Indian Refiners Toward West African Grades"
- COALINDIA.NS (COAL INDIA LTD) score 82.8 — "Hormuz Bottleneck Pushes Indian Refiners Toward West African Grades"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 82.0 — "Hormuz Bottleneck Pushes Indian Refiners Toward West African Grades"
- INDIANB.NS (INDIAN BANK) score 63.0 — "AAPL - APPLE RAMPS UP FOR NEXT IPHONE Bank of America reiterated its Buy rating and $380 p"
- COIN (Coinbase Global, Inc.) score 53.8 — "How Ozempic maker Novo Nordisk blew its lead in GLP-1 weight-loss drugs. Can Europe compet"
- TECHM.NS (TECH MAHINDRA LIMITED) score 47.8 — "PB Fintech Q1 Results: Policybazaar parent's profit soars 92% to Rs 163 crore as insurance"
- BAC (Bank of America Corporation) score 46.6 — "AAPL - APPLE RAMPS UP FOR NEXT IPHONE Bank of America reiterated its Buy rating and $380 p"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 46.5 — "PB Fintech Q1 Results: Policybazaar parent's profit soars 92% to Rs 163 crore as insurance"
- OHI (Omega Healthcare Investors, In) score 45.3 — "AI DRIVES MARKETS TO NEW HIGHS S&P 500 futures rose 0.4% on Wednesday, putting the index o"
- HDB (HDFC Bank Limited) score 44.2 — "AAPL - APPLE RAMPS UP FOR NEXT IPHONE Bank of America reiterated its Buy rating and $380 p"
- IDBI.NS (IDBI BANK LIMITED) score 42.9 — "AAPL - APPLE RAMPS UP FOR NEXT IPHONE Bank of America reiterated its Buy rating and $380 p"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 42.9 — "AAPL - APPLE RAMPS UP FOR NEXT IPHONE Bank of America reiterated its Buy rating and $380 p"
- TECH (Bio-Techne Corp) score 41.9 — "PB Fintech Q1 Results: Policybazaar parent's profit soars 92% to Rs 163 crore as insurance"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 41.4 — "AAPL - APPLE RAMPS UP FOR NEXT IPHONE Bank of America reiterated its Buy rating and $380 p"
- LTH (Life Time Group Holdings, Inc.) score 34.0 — "It’s the worst time in years to invest in AI credit markets: ‘Almost no upside and plenty "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 31.3 — "DIMON PUSHES AI SECURITY ALLIANCE JPMorgan CEO Jamie Dimon is urging more than 40 companie"
- CHKP (Check Point Software Technolog) score 29.8 — "RBI MPC meeting outcome today: Check date, time, and where to watch Governor Sanjay Malhot"
- 301077.SZ (CHINASTARS) score 26.4 — "Pentagon drafting a new U.S. nuclear strategy in case of regional war with China or Russia"
- BOND (PIMCO Active Bond Exchange-Tra) score 20.3 — "India bonds rally on 'dovish' RBI hold, lower oil prices"
- JUSTDIAL.BO (JUST DIAL LTD.) score 15.1 — "GOLDMAN STICKS TO PAYROLL FORECAST Goldman Sachs maintained its 75,000 July nonfarm payrol"
- MS (Morgan Stanley) score 13.6 — "SPCX : JP MORGAN RAISES TARGET PRICE TO $240 FROM $225"
- JIOFIN.BO (Jio Financial Services Limited) score 13.1 — "US S&P JULY SERVICES PMI AT 54.6 VS 51.2 PRIOR *US S&P JULY COMPOSITE PMI AT 54.5 VS 51.9 "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.6 — "Top Gainers & Losers on 5 August: Hindustan Copper, OLA, HFCL, Mphasis, Tata Capital among"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 10.5 — "Market wrap: Shriram Finance, Grasim, TCS among top gainers and losers on Nifty and Sensex"
- PCJEWELLER.NS (PC JEWELLER LTD) score 9.1 — "Kalyan Jewellers shares extend slide, tumble 5% after Q1 results; down 11% in four days"
- PLTR (Palantir Technologies Inc.) score 8.6 — "Why is Wall Street ignoring the controversy surrounding Palantir? Expert says 'It's not a "
- VT (Vanguard Total World Stock Ind) score 8.6 — "Central banks made the highest purchase of gold in June for 2026, says World Gold Council"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.6 — "Vodafone Idea sets AGM date to declare financial statement for FY26. Details here"
- AMZN (Amazon.com, Inc.) score 8.6 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 8.5 — "Oil Ministry to deploy tactical teams for petrol pump inspections, says Team Bharat"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.7 — "Adani Ent Share Price Live Updates: Adani Ent. News"
- NVDA (NVIDIA Corporation) score 6.9 — "Nvidia’s stock is basking in the glow of a high-profile endorsement"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.8 — "HSBC picks ICICI Bank, Titan, 8 other stocks to ride a potential $25 billion FII inflow as"
- AAPL (Apple Inc.) score 6.5 — "AAPL - APPLE RAMPS UP FOR NEXT IPHONE Bank of America reiterated its Buy rating and $380 p"
- META (Meta) score 6.2 — "Explained: Why South Korea bought gold after 13 years and what it means for yellow metal i"
- MSFT (Microsoft Corporation) score 6.1 — "SHARES OF US HYPERSCALERS CLIMB • META RISES 6.1% • MICROSOFT JUMPS 4.7% • AMAZON GAINS 4."
- GS (Goldman Sachs Group, Inc. (The) score 5.5 — "GOLDMAN STICKS TO PAYROLL FORECAST Goldman Sachs maintained its 75,000 July nonfarm payrol"
- INFY (Infosys Limited) score 4.7 — "Infosys Share Price Live Updates: Infosys Stock Details"
- THANGAMAYL.NS (THANGAMAYIL JEWELLERY LTD) score 2.6 — "Thangamayil share selloff continues: Stock drops 5% despite Rs 344 crore sales in first 3 "
- CUPID.NS (CUPID LIMITED) score 0.5 — "Cupid increases investment by $5 million in GII’s Healthcare-focused platform"

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