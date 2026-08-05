# Transmission Layer — board brief · 2026-08-05 14:32Z

data as of **2026-08-05** · 98 series · 23 red / 26 amber · 8 events surfaced (23 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.335, 3d in regime; vol-pct 0.434, breadth-off 0.235, Markov P(high-vol) 0.056)
- [INVERTED] **safe_haven_gold** — corr20 -0.28, corr60 -0.38, contra nifty_50 corr20=0.09, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.9, corr60 0.82, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.38, corr60 0.33, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.22, corr60 -0.05, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.79, corr60 -0.8, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.04, corr60 -0.01, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.18, corr60 -0.25, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.16, corr60 0.19, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **4 of 90** scanned series survive multiplicity control (effective p ≤ 0.0020700059496057133)
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.484, β 0.2629, p 0.0); driver zc 1.58 → expected 0.393%. Type hit-rate 0.822 (n=2885).
- **SETUP** ust_10y → eur_usd: leads 1d (ccf -0.28, β -0.1137, p 0.0); driver zc 1.58 → expected -0.17%. Type hit-rate 0.822 (n=2885).
- **SETUP** ust_10y → gbp_usd: leads 1d (ccf -0.28, β -0.1138, p 0.0); driver zc 1.58 → expected -0.17%. Type hit-rate 0.822 (n=2885).
- **SETUP** tips_10y_real → gbp_usd: leads 1d (ccf -0.25, β -0.0562, p 4e-05); driver zc 1.57 → expected -0.14%. Type hit-rate 0.822 (n=2885).
- Track record · residual_reversion: hit-rate **0.494** (n=1156) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.822** (n=2885) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.75] cross-asset · 12 series ↑
- comex_gold [COMMODITIES]: last 4298.20, z20 5.77, zc 3.43, resid-z -1.68 [unexplained], 1d 4.95%, |z20|=5.77; co-occur[gold_silver] same-direction (channel VALID)
- dow_jones [INDICES]: last 54694.16, z20 4.31, zc 0.99, resid-z 1.45 [quiet], 1d 1.12%, |z20|=4.31; 1y-pct=100
- comex_silver [COMMODITIES]: last 62.83, z20 3.76, zc 1.69, resid-z -2.15 [unexplained], 1d 4.63%, |z20|=3.76; co-occur[gold_silver] same-direction (channel VALID)
- russell_2000 [INDICES]: last 3047.81, z20 3.19, zc 0.27, resid-z -0.10 [quiet], 1d 0.36%, |z20|=3.19; 1y-pct=100
- sp500 [INDICES]: last 7768.81, z20 3.11, zc 0.37, resid-z 0.82 [quiet], 1d 0.42%, |z20|=3.11; 1y-pct=100
- dyn_vt [EQUITIES]: last 160.96, z20 3.01, zc 0.27, resid-z -2.02 [unexplained], 1d 0.32%, |z20|=3.01; 1y-pct=100
- stoxx_50 [INDICES]: last 6489.53, z20 2.94, zc 0.05, resid-z -0.53 [quiet], 1d 0.04%, |z20|=2.94; 1y-pct=100
- comex_copper [COMMODITIES]: last 6.69, z20 2.79, zc 0.45, resid-z 0.04 [quiet], 1d 1.01%, |z20|=2.79; 1y-pct=100; co-occur[metal_copper] same-direction (channel VALID)
- cac_40 [INDICES]: last 8667.75, z20 2.66, zc 0.02, resid-z -0.49 [quiet], 1d 0.01%, |z20|=2.66; 1y-pct=100
- dax [INDICES]: last 26241.88, z20 2.65, zc 0.18, resid-z -0.30 [quiet], 1d 0.15%, |z20|=2.65; 1y-pct=100
- dyn_nvda [EQUITIES]: last 219.91, z20 2.49, zc 1.45, resid-z 0.55 [quiet], 1d 3.76%, |z20|=2.49; 1y-pct=96
- gold_silver_ratio [DERIVED]: last 68.40, z20 -1.55, zc n/a, resid-z n/a [quiet], 1d 0.31%, GSR<75 (extreme low); |z20|=1.55
- **Mechanism**: The recent move in US stock markets, driven by hopes of a Middle East peace breakthrough, has propagated through the VALID gold_silver_comove and metal_copper_channel, indicating a potential rotation in monetary metals and global copper leads. However, the INVERTED safe_haven_gold channel suggests a risk-off safe-haven bid, which could lead to a gold bid. The VALID vix_equity_inverse channel also indicates a potential equity drawdown due to a vol spike.
- **Gap**: No gap: the move in US stock markets has been largely priced in, with the Dow Jones and S&P 500 hitting record highs, and the corresponding Indian instruments such as Nifty 50 have already reacted.
- **India take**: The Indian instrument Nifty 50 has reacted to the global market trends, while Nifty Metal has also reacted due to its correlation with Comex Silver. However, Nifty FMCG has not yet moved, despite its correlation with Dyn NVDA.
- Watch next: nifty_50 (down) — already moved; reacted to global market trends
- **India receivers**: nifty_fmcg (rho -0.527, z 0.59); nifty_50 (rho 0.524, z 1.92); nifty_midcap_100 (rho 0.521, z 1.74); nifty_metal (rho 0.484, z 4.14)
- Source: Wall Street advances on Iran deal hopes, SpaceX and AMD dip — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/wall-street-advances-on-iran-deal-hopes-spacex-and-amd-dip-11785937674365.html
- Source: The S&P 500 just hit a new high. ‘Big Short’ investor Michael Burry thinks it could bring a 1987-style fall. — MarketWatch Top, 2026-08-05. https://www.marketwatch.com/story/the-s-p-500-just-hit-a-new-high-big-short-investor-michael-burry-thinks-it-could-bring-a-1987-style-fall-775c3b95?mod=mw_rss_topstories
- Source: US stocks: S&P 500, Dow hit record highs as Mideast hopes offset SpaceX, AMD drag — ET Markets, 2026-08-05. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-us-market-opens-higher-as-mideast-hopes-offset-spacex-amd-drag/articleshow/132932841.cms
- Historical analogues: 2024-11-26 (d=0.94), 2025-10-31 (d=1.04), 2024-10-15 (d=1.15)

### [RED 6.86] usd_inr ↓
- usd_inr [FX]: last 95.11, z20 -1.86, zc -0.55, resid-z -0.63 [quiet], 1d -0.24%, 20d range extreme; |z20|=1.86
- **Mechanism**: The recent decline in usd_inr is largely priced, given the small resid_z of -0.66, which suggests that the move is mostly explained by factor exposures. The drop in oil prices and a weakening dollar have contributed to the rupee's strength. However, the RBI's decision to maintain rates has restricted further growth. The valid channels, such as gold_silver_comove and metal_copper_channel, do not directly influence the usd_inr move, but the risk-on regime and the inverse safe_haven_gold channel indicate a broader market sentiment that supports the rupee's strength.
- **Gap**: No gap: the usd_inr move is largely priced, with a small resid_z and a big raw move, indicating that the market has already accounted for the factors driving the decline.
- **India take**: The Indian instrument dyn_havells_ns has already reacted to the usd_inr move, given its rho of 0.415. Other transmission candidates, such as dyn_bharatcoal_ns and eur_inr, remain quiet for now.
- Watch next: dyn_havells_ns (up) — already moved; rho=0.415 via usd_inr
- **India receivers**: dyn_havells_ns (rho 0.415, z 2.06); dyn_bharatcoal_ns (rho 0.408, z -0.99); eur_inr (rho 0.379, z 0.59)
- Source: Rupee hits one-month closing high as oil slide outweighs RBI pause — ET Markets, 2026-08-05. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-hits-one-month-closing-high-as-oil-slide-outweighs-rbi-pause/articleshow/132916592.cms
- Source: Rupee sails past 95 to one-month high, premiums drop before RBI decision — ET Markets, 2026-08-05. https://economictimes.indiatimes.com/markets/forex/rupee-sails-past-95-to-one-month-high-premiums-drop-before-rbi-decision/articleshow/132890285.cms
- Source: Rupee jumps 39 paise to 94.89 against US dollar ahead of RBI monetary policy decision — BusinessLine Mkts, 2026-08-05. https://www.thehindubusinessline.com/markets/forex/rupee-jumps-39-paise-to-9489-against-us-dollar-ahead-of-rbi-monetary-policy-decision/article71308047.ece
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2024-10-24 (d=0.01)

### [RED 5.77] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1467.00, z20 3.77, zc 0.35, resid-z 0.09 [quiet], 1d 1.14%, |z20|=3.77; 1y-pct=100
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
- dyn_bond [EQUITIES]: last 90.84, z20 -0.35, zc 0.00, resid-z 0.50 [quiet], 1d 0.00%, 1y-pct=4
- ust_2y [RATES]: last 4.25, z20 0.31, zc 0.93, resid-z 1.54 [unexplained], 1d -0.70%, 1y-pct=96
- **Mechanism**: The recent decline in US Treasury yields, driven by easing Fed hike bets and falling oil prices, is propagating through the valid gold_silver_comove and metal_copper_channel, potentially influencing Indian metal equities. However, the primary driver of the move is the priced adjustment in dyn_bond, which has a high r2 value, indicating that the move is largely explained by factor exposures.
- **Gap**: No gap: the big raw move in US Treasury yields has a relatively small resid_z, indicating that the move is largely priced and not an anomaly.
- **India take**: The Indian 10-year government bond yield is trading flat ahead of the RBI MPC meeting outcome, but may react to the decline in US Treasury yields through the goi_ust_comove channel, although this channel is currently insufficiently established.
- Watch next: nifty_metal (up) — not yet - watch; potential influence from metal_copper_channel
- Source: US Treasury yields fall as oil retreats on Iran deal hopes, Fed hike bets ease — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-treasury-yields-fall-as-oil-retreats-on-iran-deal-hopes-fed-hike-bets-ease/articleshow/132871326.cms
- Source: Indian bond yields trades flat ahead of RBI MPC meeting outcome. Experts decode the outlook — Mint Markets, 2026-08-04. https://www.livemint.com/market/stock-market-news/indian-bond-yields-trades-flat-ahead-of-rbi-mpc-meeting-outcome-experts-decode-the-outlook-11785831046953.html
- Source: Global Market: Japan's 10-year bond yield climbs after weak auction signals soft demand — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-10-year-bond-yield-climbs-after-weak-auction-signals-soft-demand/articleshow/132852095.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.61] dyn_pltr ↑
- dyn_pltr [EQUITIES]: last 161.51, z20 3.61, zc -0.14, resid-z -0.24 [quiet], 1d -0.71%, |z20|=3.61
- **Mechanism**: The recent surge in dyn_pltr is driven by strong AI-fuelled demand, with Palantir's stock price increasing by 30% in a single day. This move is priced, given the small resid_z of -0.24, indicating that the factor exposures have largely explained the move. The valid vix_equity_inverse channel suggests that the volatility spike is inversely related to equity drawdown, but the current RISK_ON regime and strong demand for AI-powered data analytics platforms may limit the impact of this channel.
- **Gap**: No gap: the move in dyn_pltr is largely priced, with a small resid_z and a strong narrative driven by AI demand
- **India take**: The Indian transmission candidate dyn_atherenerg_ns has already reacted to the move in dyn_pltr, with a rho of 0.394. Further moves in Indian metal equities may be influenced by the global copper channel, which is currently valid.
- Watch next: dyn_atherenerg_ns (up) — already moved; reacted to dyn_pltr move
- **India receivers**: dyn_atherenerg_ns (rho 0.394, z 3.77)
- Source: Michael Burry warns of 1987-style crash as AI rally powers Wall Street; investor shorts Nvidia, Tesla, Palantir — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/michael-burry-warns-of-1987-style-crash-as-ai-rally-powers-wall-street-investor-shorts-nvidia-tesla-palantir-11785922333250.html
- Source: Palantir Short Sellers Take $3 Billion Hit After 30% Stock Surge — Mint Markets, 2026-08-04. https://www.livemint.com/market/palantir-short-sellers-take-3-billion-hit-after-30-stock-surge-11785872351134.html
- Source: Palantir climbs 27% on 'otherworldly' AI demand; Karp tells shareholders business has 'Marxist' values — Mint Markets, 2026-08-04. https://www.livemint.com/market/stock-market-news/palantir-climbs-27-on-otherworldly-ai-demand-karp-tells-shareholders-business-has-marxist-values-11785861835803.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-01 (d=0.08), 2025-10-13 (d=0.13)

### [RED 5.52] cross-asset · 2 series ↑
- usd_jpy [FX]: last 157.48, z20 -2.69, zc -0.05, resid-z -0.12 [quiet], 1d -0.03%, |z20|=2.69
- dyn_amzn [EQUITIES]: last 276.94, z20 1.98, zc -0.07, resid-z 9.76 [unexplained], 1d -0.17%, 1y-pct=99
- **Mechanism**: The recent intervention by Tokyo has led to a surge in the yen, causing a ripple effect in the currency markets. The USD/JPY currency pair has moved in response, with a z20 score of -2.69, indicating a significant move. However, the resid_z score of -0.12 suggests that this move is largely priced in, with little unexplained component. The move in USD/JPY has also led to a reaction in the Indian currency market, with the dyn_muthootfin_ns reacting in tandem.
- **Gap**: No gap: the move in USD/JPY is largely priced in, with a small resid_z score, indicating that the market has already accounted for the intervention and its effects
- **India take**: The Indian instrument dyn_muthootfin_ns has already reacted to the move in USD/JPY, with a z20 score of -2.07. However, dyn_cartrade_ns remains quiet, with a z20 score of 0.63, and may be due for a reaction in the coming days.
- Watch next: dyn_amzn (up) — already moved; historical analogues suggest a median 12.86% move in the next 20 days
- **India receivers**: dyn_muthootfin_ns (rho -0.51, z -2.07); dyn_cartrade_ns (rho -0.358, z 0.63)
- Source: BOFA ANTICIPATE STRONGER JAPANESE YEN FOLLOWING INTERVENTION, CHANGE YEAR END DOLLAR/YEN FORECAST TO 149 FROM 152 - CURRENTLY TRADES AT 157.7 — DeItaone, 2026-08-05. https://t.me/walter_bloomberg/34369
- Source: US TREASURY SECRETARY BESSENT: UPTICK IN JAPAN'S INFLATION WAS RESULT OF WEAK YEN, ENERGY PRICES — DeItaone, 2026-08-04. https://t.me/walter_bloomberg/34358
- Source: Yen holds most gains as intervention keeps speculators on edge — Mint Markets, 2026-08-04. https://www.livemint.com/market/yen-holds-most-gains-as-intervention-keeps-speculators-on-edge-11785874259298.html
- Historical analogues: 2024-10-16 (d=0.15), 2024-11-21 (d=0.23), 2026-03-31 (d=0.24)

### [AMBER 5.43] cross-asset · 3 series ↑
- dyn_jiofin_bo [EQUITIES]: last 261.50, z20 2.11, zc -0.53, resid-z -1.01 [quiet], 1d -1.15%, |z20|=2.11
- nifty_50 [INDICES]: last 24624.65, z20 1.92, zc 0.05, resid-z 0.08 [quiet], 1d 0.04%, |z20|=1.92
- nifty_midcap_100 [INDICES]: last 63597.60, z20 1.74, zc 0.23, resid-z 0.26 [quiet], 1d 0.18%, |z20|=1.74; 1y-pct=99
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-17 (z-distance 0.69).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.695 via nifty_midcap_100, z -2.07, reacted); dyn_bharatcoal_ns (rho 0.641 via nifty_midcap_100, z -0.99, quiet); dyn_indianb_ns (rho 0.62 via nifty_midcap_100, z 1.07, reacted); dyn_indusindbk_bo (rho 0.619 via nifty_midcap_100, z 0.04, quiet); nifty_metal (rho 0.578 via nifty_midcap_100, z 4.14, reacted)
- Watch next: dyn_bharatcoal_ns (co-move) — not yet - watch; rho 0.641 vs nifty_midcap_100, historically leads by 0d
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.574 vs nifty_50, historically leads by 3d
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.571 vs nifty_50
- Watch next: dyn_indusindbk_bo (co-move) — not yet - watch; rho 0.533 vs dyn_jiofin_bo
- **India receivers**: dyn_muthootfin_ns (rho 0.695, z -2.07); dyn_bharatcoal_ns (rho 0.641, z -0.99); dyn_indianb_ns (rho 0.62, z 1.07); dyn_indusindbk_bo (rho 0.619, z 0.04)
- Source: Smallcaps hit all-time high even as Nifty, Sensex remain directionless — BusinessLine Mkts, 2026-08-05. https://www.thehindubusinessline.com/markets/smallcaps-hit-all-time-high-as-nifty-treads-water/article71309640.ece
- Source: Market wrap: Shriram Finance, Grasim, TCS among top gainers and losers on Nifty and Sensex on Wednesday — ET Markets, 2026-08-05. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-shriram-finance-grasim-tcs-among-top-gainers-and-losers-on-nifty-and-sensex-on-wednesday/articleshow/132918514.cms
- Source: Sensex today | Stock Market Highlights: Sensex rises 152 points, Nifty ends above 24,620 after RBI keeps repo rate unchanged — BusinessLine Mkts, 2026-08-05. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-5th-august-2026/article71306480.ece
- Historical analogues: 2025-07-17 (d=0.69), 2024-11-07 (d=0.98), 2025-08-13 (d=1.26)

### [RED 5.27] dxy ↓
- dxy [FX]: last 99.64, z20 -2.27, zc -0.71, resid-z -0.92 [quiet], 1d -0.25%, 20d range extreme; |z20|=2.27
- **Mechanism**: dxy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.504 vs dxy, historically leads by 3d
- Watch next: eth_usd (inverse) — not yet - watch; rho -0.508 vs dxy
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

## Watchlist (below surfacing floor)
fx · 3 series ↑ (4.46), dyn_msft ↑ (4.4), nifty_metal ↑ (4.14), dyn_thangamayl_ns ↓ (4.1), dyn_muthootfin_ns ↓ (4.07), dyn_bac ↑ (3.93), natgas ↓ (3.51), asx_200 ↑ (3.41), dyn_coin ↓ (3.33), dyn_cupid_ns ↑ (3.22), dyn_tech ↑ (3.2), dyn_lth ↑ (3.05)

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
- INOXINDIA.NS (INOX INDIA LIMITED) score 80.6 — "INDIA CONSIDERS GAS CONSUMER LEVIES TO FUND $42 BILLION EXPANSION OF STRATEGIC FUEL RESERV"
- COALINDIA.NS (COAL INDIA LTD) score 78.3 — "INDIA CONSIDERS GAS CONSUMER LEVIES TO FUND $42 BILLION EXPANSION OF STRATEGIC FUEL RESERV"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 77.4 — "INDIA CONSIDERS GAS CONSUMER LEVIES TO FUND $42 BILLION EXPANSION OF STRATEGIC FUEL RESERV"
- INDIANB.NS (INDIAN BANK) score 60.9 — "DIMON PUSHES AI SECURITY ALLIANCE JPMorgan CEO Jamie Dimon is urging more than 40 companie"
- COIN (Coinbase Global, Inc.) score 54.5 — "Bharat International Rice Conference to drive global rice trade dialogue in October"
- TECHM.NS (TECH MAHINDRA LIMITED) score 48.3 — "Broker’s Call: Dixon Technologies (Buy)"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 47.0 — "Broker’s Call: Dixon Technologies (Buy)"
- BAC (Bank of America Corporation) score 45.0 — "DIMON PUSHES AI SECURITY ALLIANCE JPMorgan CEO Jamie Dimon is urging more than 40 companie"
- OHI (Omega Healthcare Investors, In) score 43.7 — "LIC OFS gets strong response from retail investors, subscribed 1.82 times the base size"
- HDB (HDFC Bank Limited) score 42.6 — "DIMON PUSHES AI SECURITY ALLIANCE JPMorgan CEO Jamie Dimon is urging more than 40 companie"
- TECH (Bio-Techne Corp) score 42.2 — "Broker’s Call: Dixon Technologies (Buy)"
- IDBI.NS (IDBI BANK LIMITED) score 41.3 — "DIMON PUSHES AI SECURITY ALLIANCE JPMorgan CEO Jamie Dimon is urging more than 40 companie"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 41.2 — "DIMON PUSHES AI SECURITY ALLIANCE JPMorgan CEO Jamie Dimon is urging more than 40 companie"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 39.6 — "DIMON PUSHES AI SECURITY ALLIANCE JPMorgan CEO Jamie Dimon is urging more than 40 companie"
- LTH (Life Time Group Holdings, Inc.) score 33.1 — "ZELENSKIY SAYS UKRAINE'S AIR DEFENCE SUPPLIES LEVEL THREE TIMES LOWER COMPARED TO LAST YEA"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 32.4 — "DIMON PUSHES AI SECURITY ALLIANCE JPMorgan CEO Jamie Dimon is urging more than 40 companie"
- CHKP (Check Point Software Technolog) score 30.8 — "RBI MPC meeting outcome today: Check date, time, and where to watch Governor Sanjay Malhot"
- 301077.SZ (CHINASTARS) score 27.2 — "Pentagon drafting a new U.S. nuclear strategy in case of regional war with China or Russia"
- BOND (PIMCO Active Bond Exchange-Tra) score 21.0 — "India bonds rally on 'dovish' RBI hold, lower oil prices"
- JUSTDIAL.BO (JUST DIAL LTD.) score 14.5 — "SPCX - MIZUHO REAFFIRMS OUTPERFORM ON SPACEX Mizuho reiterated its Outperform rating and $"
- MS (Morgan Stanley) score 14.1 — "SPCX : JP MORGAN RAISES TARGET PRICE TO $240 FROM $225"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 12.0 — "Top Gainers & Losers on 5 August: Hindustan Copper, OLA, HFCL, Mphasis, Tata Capital among"
- JIOFIN.BO (Jio Financial Services Limited) score 11.4 — "Vodafone Idea sets AGM date to declare financial statement for FY26. Details here"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 10.8 — "Market wrap: Shriram Finance, Grasim, TCS among top gainers and losers on Nifty and Sensex"
- PCJEWELLER.NS (PC JEWELLER LTD) score 9.4 — "Kalyan Jewellers shares extend slide, tumble 5% after Q1 results; down 11% in four days"
- VT (Vanguard Total World Stock Ind) score 8.9 — "Central banks made the highest purchase of gold in June for 2026, says World Gold Council"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.9 — "Vodafone Idea sets AGM date to declare financial statement for FY26. Details here"
- AMZN (Amazon.com, Inc.) score 8.9 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.9 — "Adani Ent Share Price Live Updates: Adani Ent. News"
- PLTR (Palantir Technologies Inc.) score 7.9 — "Michael Burry warns of 1987-style crash as AI rally powers Wall Street; investor shorts Nv"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 7.7 — "Bharat International Rice Conference to drive global rice trade dialogue in October"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.1 — "HSBC picks ICICI Bank, Titan, 8 other stocks to ride a potential $25 billion FII inflow as"
- META (Meta) score 6.4 — "Explained: Why South Korea bought gold after 13 years and what it means for yellow metal i"
- MSFT (Microsoft Corporation) score 6.3 — "SHARES OF US HYPERSCALERS CLIMB • META RISES 6.1% • MICROSOFT JUMPS 4.7% • AMAZON GAINS 4."
- NVDA (NVIDIA Corporation) score 6.1 — "Michael Burry warns of 1987-style crash as AI rally powers Wall Street; investor shorts Nv"
- AAPL (Apple Inc.) score 5.7 — "Apple suffers worst rout since 2025 on disappointing outlook"
- INFY (Infosys Limited) score 4.8 — "Infosys Share Price Live Updates: Infosys Stock Details"
- GS (Goldman Sachs Group, Inc. (The) score 4.7 — "Global Market: Goldman Sachs sees Brent crude trading at $80-$90 until Iran conflict outlo"
- THANGAMAYL.NS (THANGAMAYIL JEWELLERY LTD) score 2.7 — "Thangamayil share selloff continues: Stock drops 5% despite Rs 344 crore sales in first 3 "
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