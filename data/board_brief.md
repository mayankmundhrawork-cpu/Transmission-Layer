# Transmission Layer — board brief · 2026-08-05 06:41Z

data as of **2026-08-05** · 98 series · 20 red / 25 amber · 8 events surfaced (17 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.483, 1d in regime; vol-pct 0.465, breadth-off 0.5, Markov P(high-vol) 0.185)
- [INVERTED] **safe_haven_gold** — corr20 -0.42, corr60 -0.43, contra nifty_50 corr20=0.07, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.91, corr60 0.82, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.36, corr60 0.32, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.21, corr60 -0.05, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.81, corr60 -0.81, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.01, corr60 -0.02, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.18, corr60 -0.25, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.21, corr60 0.19, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **4 of 90** scanned series survive multiplicity control (effective p ≤ 0.0010380708664139426)
- **SETUP** nasdaq_100 → dyn_453950_ks: leads 1d (ccf 0.643, β 0.8755, p 0.0); driver zc 1.96 → expected 2.891%. Type hit-rate 0.822 (n=2885).
- **SETUP** sp500 → dyn_453950_ks: leads 1d (ccf 0.593, β 1.0788, p 0.0); driver zc 1.78 → expected 1.918%. Type hit-rate 0.822 (n=2885).
- **SETUP** dyn_vt → dyn_453950_ks: leads 1d (ccf 0.592, β 1.1206, p 0.0); driver zc 1.69 → expected 1.984%. Type hit-rate 0.822 (n=2885).
- **SETUP** dyn_vt → usd_brl: leads 1d (ccf -0.521, β -0.4261, p 0.0); driver zc 1.69 → expected -0.754%. Type hit-rate 0.822 (n=2885).
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.484, β 0.2629, p 0.0); driver zc 1.58 → expected 0.393%. Type hit-rate 0.822 (n=2885).
- **SETUP** dow_jones → dyn_453950_ks: leads 1d (ccf 0.475, β 0.9457, p 0.0); driver zc 1.67 → expected 1.622%. Type hit-rate 0.822 (n=2885).
- **SETUP** sp500 → usd_brl: leads 1d (ccf -0.445, β -0.3522, p 0.0); driver zc 1.78 → expected -0.626%. Type hit-rate 0.822 (n=2885).
- **SETUP** nasdaq_100 → usd_brl: leads 1d (ccf -0.425, β -0.2476, p 0.0); driver zc 1.96 → expected -0.818%. Type hit-rate 0.822 (n=2885).
- **SETUP** dow_jones → usd_brl: leads 1d (ccf -0.411, β -0.3549, p 0.0); driver zc 1.67 → expected -0.609%. Type hit-rate 0.822 (n=2885).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.356, β -2.3022, p 0.01122); driver zc 1.69 → expected -4.075%. Type hit-rate 0.822 (n=2885).
- **SETUP** dyn_vt → nifty_metal: leads 1d (ccf 0.328, β 0.5156, p 2e-05); driver zc 1.69 → expected 0.913%. Type hit-rate 0.822 (n=2885).
- **SETUP** sp500 → nifty_metal: leads 1d (ccf 0.301, β 0.4603, p 0.0005); driver zc 1.78 → expected 0.818%. Type hit-rate 0.822 (n=2885).
- **SETUP** dyn_vt → nifty_midcap_100: leads 1d (ccf 0.285, β 0.3495, p 0.0); driver zc 1.69 → expected 0.619%. Type hit-rate 0.822 (n=2885).
- **SETUP** ust_10y → eur_usd: leads 1d (ccf -0.28, β -0.1137, p 0.0); driver zc 1.58 → expected -0.17%. Type hit-rate 0.822 (n=2885).
- **SETUP** ust_10y → gbp_usd: leads 1d (ccf -0.28, β -0.1138, p 0.0); driver zc 1.58 → expected -0.17%. Type hit-rate 0.822 (n=2885).
- **SETUP** nasdaq_100 → nifty_metal: leads 1d (ccf 0.262, β 0.2904, p 0.00131); driver zc 1.96 → expected 0.959%. Type hit-rate 0.822 (n=2885).
- **SETUP** sp500 → nifty_midcap_100: leads 1d (ccf 0.261, β 0.3117, p 1e-05); driver zc 1.78 → expected 0.554%. Type hit-rate 0.822 (n=2885).
- **SETUP** dyn_vt → hang_seng: leads 1d (ccf 0.256, β 0.3691, p 0.0); driver zc 1.69 → expected 0.653%. Type hit-rate 0.822 (n=2885).
- **SETUP** tips_10y_real → gbp_usd: leads 1d (ccf -0.25, β -0.0562, p 4e-05); driver zc 1.57 → expected -0.14%. Type hit-rate 0.822 (n=2885).
- Track record · residual_reversion: hit-rate **0.493** (n=1153) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.822** (n=2885) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.49] cross-asset · 12 series ↑
- dow_jones [INDICES]: last 54090.66, z20 4.48, zc 1.67, resid-z 0.68 [priced], 1d 1.72%, |z20|=4.48; 1y-pct=100
- comex_gold [COMMODITIES]: last 4227.60, z20 4.07, zc 2.24, resid-z -1.68 [unexplained], 1d 3.23%, |z20|=4.07; co-occur[gold_silver] same-direction (channel VALID)
- stoxx_50 [INDICES]: last 6489.45, z20 4.05, zc 1.02, resid-z -0.87 [quiet], 1d 0.98%, |z20|=4.05; 1y-pct=100
- sp500 [INDICES]: last 7735.60, z20 3.68, zc 1.78, resid-z 0.82 [priced], 1d 1.78%, |z20|=3.68; 1y-pct=100
- russell_2000 [INDICES]: last 3037.07, z20 3.65, zc 1.48, resid-z -0.34 [quiet], 1d 1.85%, |z20|=3.65; 1y-pct=100
- dyn_vt [EQUITIES]: last 160.40, z20 3.55, zc 1.69, resid-z -2.02 [unexplained], 1d 1.77%, |z20|=3.55; 1y-pct=100
- cac_40 [INDICES]: last 8659.35, z20 3.37, zc 0.63, resid-z -1.06 [quiet], 1d 0.53%, |z20|=3.37; 1y-pct=100
- dax [INDICES]: last 26221.66, z20 3.26, zc 1.02, resid-z -0.70 [quiet], 1d 0.85%, |z20|=3.26; 1y-pct=100
- comex_silver [COMMODITIES]: last 61.77, z20 2.90, zc 1.04, resid-z 0.79 [quiet], 1d 2.85%, |z20|=2.90; co-occur[gold_silver] same-direction (channel VALID)
- comex_copper [COMMODITIES]: last 6.65, z20 2.50, zc 0.21, resid-z -1.06 [quiet], 1d 0.47%, |z20|=2.50; 1y-pct=99; co-occur[metal_copper] same-direction (channel VALID)
- ftse_100 [INDICES]: last 10890.11, z20 1.51, zc 0.53, resid-z -0.12 [quiet], 1d 0.30%, |z20|=1.51; 1y-pct=98
- gold_silver_ratio [DERIVED]: last 68.44, z20 -1.51, zc n/a, resid-z n/a [quiet], 1d 0.36%, GSR<75 (extreme low); |z20|=1.51
- **Mechanism**: The recent surge in global indices such as the Dow Jones and S&P 500, coupled with a rise in commodities like gold and silver, is driven by a decline in oil prices and a softer dollar. This has created a risk-on sentiment, leading to an increase in equity markets. The VALID gold_silver_comove channel and the VALID metal_copper_channel suggest that monetary metals are co-moving, and global copper is leading Indian metal equities.
- **Gap**: No gap: The recent price moves in global indices and commodities are largely priced in, with the resid_z values indicating that the moves are largely explained by factor exposures.
- **India take**: The Indian market, as represented by the Nifty 50, has already reacted to the global cues, with a rho of 0.533 via the CAC 40. The Nifty Metal index has also reacted, with a rho of -0.445 via the gold_silver_ratio.
- Watch next: nifty_50 (up) — already moved; Reacted to global cues, with a rho of 0.533 via cac_40
- Watch next: comex_gold (up) — not yet - watch; Unexplained move with a resid_z of -1.68, potentially driven by safe-haven demand
- **India receivers**: nifty_50 (rho 0.533, z 1.71); nifty_midcap_100 (rho 0.526, z 1.6); nifty_metal (rho -0.445, z 2.96); nifty_it (rho 0.353, z 1.69)
- Source: RBI policy day puts markets on edge as Nifty opens flat; oil slump, Wall Street records lift sentiment — BusinessLine Mkts, 2026-08-05. https://www.thehindubusinessline.com/markets/stock-markets/rbi-policy-day-puts-markets-on-edge-as-nifty-opens-flat-oil-slump-wall-street-records-lift-sentiment/article71308011.ece
- Source: Gold extends gains on lower oil and softer dollar, markets await US jobs data — BusinessLine Mkts, 2026-08-05. https://www.thehindubusinessline.com/markets/gold/gold-extends-gains-on-lower-oil-and-softer-dollar-markets-await-us-jobs-data/article71307935.ece
- Source: Gold and silver prices today: Rates climb amid a decline in dollar, crude oil prices; investors focus on RBI MPC policy — Mint Markets, 2026-08-05. https://www.livemint.com/market/commodities/gold-and-silver-prices-today-rates-climb-amid-a-decline-in-dollar-crude-oil-prices-investors-focus-on-rbi-mpc-policy-11785900581248.html
- Historical analogues: 2024-10-09 (d=0.96), 2024-11-26 (d=1.02), 2025-10-31 (d=1.03)

### [RED 9.32] dyn_pltr ↑
- dyn_pltr [EQUITIES]: last 162.63, z20 7.32, zc 8.98, resid-z -0.24 [moved], 1d 29.43%, |z20|=7.32
- **Mechanism**: The surge in Palantir Technologies Inc.'s stock, driven by strong demand for its AI-powered data analytics platform, has triggered a risk-on sentiment in the market. This sentiment is propagating through the VALID vix_equity_inverse channel, where a vol spike is inversely related to equity drawdown. The metal_copper_channel is also a potential mechanism, given the global copper leads Indian metal equities.
- **Gap**: No gap: the big raw move in dyn_pltr is largely priced, with a small resid_z of -0.24, indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian instrument dyn_atherenerg_ns has already reacted to the move in dyn_pltr, given its rho of 0.403. Further reaction in Indian metal equities can be expected through the metal_copper_channel.
- Watch next: dyn_atherenerg_ns (up) — already moved; reacted to dyn_pltr
- **India receivers**: dyn_atherenerg_ns (rho 0.399, z 3.7)
- Source: Palantir Short Sellers Take $3 Billion Hit After 30% Stock Surge — Mint Markets, 2026-08-04. https://www.livemint.com/market/palantir-short-sellers-take-3-billion-hit-after-30-stock-surge-11785872351134.html
- Source: Palantir climbs 27% on 'otherworldly' AI demand; Karp tells shareholders business has 'Marxist' values — Mint Markets, 2026-08-04. https://www.livemint.com/market/stock-market-news/palantir-climbs-27-on-otherworldly-ai-demand-karp-tells-shareholders-business-has-marxist-values-11785861835803.html
- Source: Palantir stock jumps 27% after ‘otherworldly’ demand lifts outlook — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/palantir-stock-jumps-27-after-otherworldly-demand-lifts-outlook/articleshow/132866951.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-01 (d=0.08), 2025-10-13 (d=0.13)

### [RED 6.81] usd_inr ↓
- usd_inr [FX]: last 95.13, z20 -1.81, zc -0.49, resid-z -0.25 [quiet], 1d -0.21%, 20d range extreme; |z20|=1.81
- **Mechanism**: The recent decline in usd_inr is driven by lower oil prices and a dip in the U.S. dollar value, with the Indian rupee gaining strength ahead of the RBI's monetary policy decision. This move is priced, as indicated by the small resid_z of -0.25, suggesting that the market has already factored in the current factors. The VALID metal_copper_channel and gold_silver_comove channels may provide additional support to the rupee's strength.
- **Gap**: No gap: the current move in usd_inr is priced, with a small resid_z and a z20 level within historical ranges
- **India take**: The Indian instrument dyn_havells_ns has already reacted to the usd_inr move, while dyn_bharatcoal_ns and eur_inr remain quiet. The rupee's strength may continue to support Indian metal equities, such as dyn_havells_ns.
- Watch next: dyn_havells_ns (up) — already moved; reacted to usd_inr move
- **India receivers**: dyn_havells_ns (rho 0.416, z 1.99); dyn_bharatcoal_ns (rho 0.409, z -0.99); eur_inr (rho 0.381, z 0.41)
- Source: Rupee sails past 95 to one-month high, premiums drop before RBI decision — ET Markets, 2026-08-05. https://economictimes.indiatimes.com/markets/forex/rupee-sails-past-95-to-one-month-high-premiums-drop-before-rbi-decision/articleshow/132890285.cms
- Source: Rupee jumps 39 paise to 94.89 against US dollar ahead of RBI monetary policy decision — BusinessLine Mkts, 2026-08-05. https://www.thehindubusinessline.com/markets/forex/rupee-jumps-39-paise-to-9489-against-us-dollar-ahead-of-rbi-monetary-policy-decision/article71308047.ece
- Source: Rupee opens 46 paise higher against US dollar ahead of RBI Policy — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/rupee-opens-46-paise-higher-against-us-dollar-ahead-of-rbi-policy-11785901016627.html
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2024-10-24 (d=0.01)

### [RED 6.12] fx · 3 series ↑
- usd_mxn [FX]: last 17.24, z20 -2.80, zc -1.20, resid-z 0.46 [quiet], 1d -0.52%, |z20|=2.80
- eur_usd [FX]: last 1.15, z20 2.36, zc 0.81, resid-z -1.11 [quiet], 1d 0.31%, |z20|=2.36
- aud_usd [FX]: last 0.71, z20 2.19, zc 1.07, resid-z -1.34 [quiet], 1d 0.75%, |z20|=2.19
- **Mechanism**: The recent decline in oil prices has led to a decrease in inflation concerns, prompting markets to pare expectations for further ECB rate hikes. This has resulted in a decline in Euro zone government bond yields, which in turn has caused a strengthening of the Euro against the US Dollar. This move is priced, with small resid_z values indicating that the factor exposures can explain the majority of the move.
- **Gap**: No gap: the move in eur_usd is largely explained by the decline in oil prices and the subsequent decrease in inflation concerns, with a small resid_z value indicating that the move is priced.
- **India take**: The Indian instrument dyn_muthootfin_ns has reacted to the move in usd_mxn, with a correlation coefficient of -0.516. The move in usd_mxn has been largely priced, with a small resid_z value, indicating that the Indian market has already reacted to the decline in oil prices and the subsequent decrease in inflation concerns.
- Watch next: eur_usd (up) — already moved; Euro zone bond yields decline
- **India receivers**: dyn_muthootfin_ns (rho -0.529, z -1.9)
- Source: Global Market: Euro zone bond yields decline as falling oil prices boost market sentiment — ET Markets, 2026-08-03. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-bond-yields-decline-as-falling-oil-prices-boost-market-sentiment/articleshow/132826355.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-02 (d=0.26), 2025-08-15 (d=0.26)

### [AMBER 5.76] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.23, z20 1.83, zc 1.53, resid-z 1.91 [unexplained], 1d -0.76%, |z20|=1.83; 1y-pct=99
- ust_10y [RATES]: last 4.70, z20 1.32, zc 1.58, resid-z 2.16 [unexplained], 1d -1.05%, 1y-pct=99
- tips_10y_real [RATES]: last 2.43, z20 1.16, zc 1.57, resid-z 2.22 [unexplained], 1d -1.62%, 1y-pct=98
- dyn_bond [EQUITIES]: last 90.83, z20 -0.43, zc 2.00, resid-z 0.50 [priced], 1d 0.58%, 1y-pct=4
- ust_2y [RATES]: last 4.25, z20 0.31, zc 0.93, resid-z 1.54 [unexplained], 1d -0.70%, 1y-pct=96
- **Mechanism**: The recent decline in US Treasury yields, driven by easing Fed hike bets and falling oil prices, is propagating through the valid gold_silver_comove and metal_copper_channel, potentially influencing Indian metal equities. However, the primary driver of the move is the priced adjustment in dyn_bond, which has a high r2 value, indicating that the move is largely explained by factor exposures.
- **Gap**: No gap: the big raw move in US Treasury yields has a relatively small resid_z, indicating that the move is largely priced and not an anomaly.
- **India take**: The Indian 10-year government bond yield is trading flat ahead of the RBI MPC meeting outcome, but may react to the decline in US Treasury yields through the goi_ust_comove channel, although this channel is currently insufficiently established.
- Watch next: nifty_metal (up) — not yet - watch; potential influence from metal_copper_channel
- Source: US Treasury yields fall as oil retreats on Iran deal hopes, Fed hike bets ease — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-treasury-yields-fall-as-oil-retreats-on-iran-deal-hopes-fed-hike-bets-ease/articleshow/132871326.cms
- Source: Indian bond yields trades flat ahead of RBI MPC meeting outcome. Experts decode the outlook — Mint Markets, 2026-08-04. https://www.livemint.com/market/stock-market-news/indian-bond-yields-trades-flat-ahead-of-rbi-mpc-meeting-outcome-experts-decode-the-outlook-11785831046953.html
- Source: Global Market: Japan's 10-year bond yield climbs after weak auction signals soft demand — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-10-year-bond-yield-climbs-after-weak-auction-signals-soft-demand/articleshow/132852095.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.7] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1463.10, z20 3.70, zc 0.27, resid-z 4.91 [unexplained], 1d 0.88%, |z20|=3.70; 1y-pct=100
- **Mechanism**: The recent surge in Ather Energy's stock price can be attributed to the company's narrowing quarterly loss, which has ignited investor interest and driven up the stock price. This move is propagated through the metal_copper_channel, where global copper leads Indian metal equities, and the vix_equity_inverse channel, where a vol spike leads to an equity drawdown. However, given the stock's significant move and relatively low resid_z, this move appears to be largely priced in.
- **Gap**: No gap: The stock's 14-18% surge following the Q1 results appears to be a priced reaction to the company's improving operating performance, with a relatively low resid_z of 4.91 indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is Ather Energy's stock itself, which has already reacted with a significant surge in price. Other Indian metal equities may also be affected through the metal_copper_channel.
- Watch next: nifty_50 (up) — not yet - watch; Potential spill-over effect from Ather Energy's surge
- Source: Ather Energy shares jump 14% after Q1 loss narrows — BusinessLine Mkts, 2026-08-04. https://www.thehindubusinessline.com/markets/ather-energy-shares-jump-18-to-fresh-52-week-high-after-q1-loss-narrows/article71303894.ece
- Source: Ather Energy's tapering losses put stock in fast lane, but is the rally justified? — Mint Markets, 2026-08-04. https://www.livemint.com/market/mark-to-market/ather-energy-electric-vehicles-ev-q1fy27-ebitda-operating-losses-ev-sales-hero-motocorp-11785824423599.html
- Source: Multibagger stock Ather Energy share price soars 18% to record high post Q1 FY27 results: Should you buy? — Mint Markets, 2026-08-04. https://www.livemint.com/market/stock-market-news/multibagger-stock-ather-energy-share-price-soars-18-to-record-high-post-q1-fy27-results-should-you-buy-11785824415092.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [AMBER 5.58] cross-asset · 3 series ↑
- dyn_jiofin_bo [EQUITIES]: last 262.90, z20 2.26, zc -0.28, resid-z 1.44 [quiet], 1d -0.62%, |z20|=2.26
- nifty_50 [INDICES]: last 24574.35, z20 1.71, zc -0.23, resid-z -1.06 [quiet], 1d -0.16%, |z20|=1.71
- nifty_midcap_100 [INDICES]: last 63521.60, z20 1.60, zc 0.08, resid-z 0.52 [quiet], 1d 0.06%, |z20|=1.60; 1y-pct=99
- **Mechanism**: The recent RBI MPC outcome, which kept policy rates unchanged and raised the economic growth forecast for FY27, has led to a surge in rate-sensitive stocks. This move is propagating through the transmission channels, such as the verified setup of sp500 leading nifty_midcap_100, and the valid metal_copper_channel. The residual reversion signal, although having a low hit-rate of 0.493, also supports this move.
- **Gap**: No gap: the big raw move in rate-sensitive stocks is largely priced, with a relatively small resid_z value, indicating that the market has already factored in the RBI MPC outcome.
- **India take**: The Indian instrument that expresses this move is the nifty_midcap_100, which has already reacted to the RBI MPC outcome. Other transmission candidates, such as dyn_muthootfin_ns and nifty_metal, have also reacted.
- Watch next: nifty_50 (up) — not yet - watch; low r2 value of 0.078 indicates unexplained movement
- Watch next: nifty_midcap_100 (up) — already moved; high z20 level of 1.60 and reacted transmission candidates
- **India receivers**: dyn_muthootfin_ns (rho 0.692, z -1.9); dyn_bharatcoal_ns (rho 0.64, z -0.99); dyn_indusindbk_bo (rho 0.621, z 0.39); dyn_indianb_ns (rho 0.618, z 1.18)
- Source: Rate-sensitive stocks rise after RBI MPC outcome; Nifty Auto hits record high, Nifty Realty up over 2.5% — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/rate-sensitive-stocks-rise-after-rbi-mpc-outcome-nifty-auto-hits-record-high-nifty-realty-up-over-25-11785910914631.html
- Source: Sensex-Nifty 50 divergence persists after RBI policy decision: Here's what investors need to understand — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/sensex-nifty-50-divergence-persists-heres-what-investors-need-to-understand-11785909230271.html
- Source: NSE SME stock jumps 8% despite muted trend on Dalal Street; here's why — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/nse-sme-stock-agarwal-toughened-glass-india-jumps-8-despite-muted-trend-on-dalal-street-heres-why-11785907015592.html
- Historical analogues: 2025-07-17 (d=0.69), 2024-11-07 (d=0.98), 2025-08-13 (d=1.26)

### [RED 5.45] cross-asset · 2 series ↑
- usd_jpy [FX]: last 157.61, z20 -2.61, zc 0.09, resid-z -0.01 [quiet], 1d 0.05%, |z20|=2.61
- dyn_amzn [EQUITIES]: last 277.43, z20 2.39, zc -0.22, resid-z 9.76 [unexplained], 1d -2.32%, |z20|=2.39; 1y-pct=99
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-10-16 (z-distance 0.15).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.507 via usd_jpy, z -1.9, reacted); dyn_cartrade_ns (rho -0.362 via dyn_amzn, z 0.71, quiet)
- Watch next: gbp_usd (inverse) — not yet - watch; rho -0.516 vs usd_jpy, historically leads by 1d
- Watch next: taiwan_weighted (inverse) — not yet - watch; rho -0.504 vs usd_jpy, historically leads by 1d
- Watch next: kospi (inverse) — not yet - watch; rho -0.611 vs usd_jpy
- **India receivers**: dyn_muthootfin_ns (rho -0.507, z -1.9); dyn_cartrade_ns (rho -0.362, z 0.71)
- Source: US TREASURY SECRETARY BESSENT: UPTICK IN JAPAN'S INFLATION WAS RESULT OF WEAK YEN, ENERGY PRICES — DeItaone, 2026-08-04. https://t.me/walter_bloomberg/34358
- Source: Yen holds most gains as intervention keeps speculators on edge — Mint Markets, 2026-08-04. https://www.livemint.com/market/yen-holds-most-gains-as-intervention-keeps-speculators-on-edge-11785874259298.html
- Source: BOFA: TARGET FX VOLATILITY, NOT THE WHOLE MARKET Bank of America says investors should focus on specific currency pairs—not broad FX volatility—if the Fed resumes rate hikes. The bank highlights Japanese yen and British pound pairs as the strongest opportunities. Historically, — DeItaone, 2026-08-04. https://t.me/walter_bloomberg/34270
- Historical analogues: 2024-10-16 (d=0.15), 2024-11-21 (d=0.23), 2026-03-31 (d=0.24)

## Watchlist (below surfacing floor)
dyn_msft ↑ (5.15), dyn_infy ↑ (4.19), dyn_thangamayl_ns ↓ (4.1), dyn_bac ↑ (3.67), dyn_coin ↓ (3.55), asx_200 ↑ (3.41), dyn_lth ↑ (3.38), dyn_tech ↑ (3.17), nifty_metal ↑ (2.96), dyn_cupid_ns ↑ (2.58), dyn_indusindbk_bo ↑ (2.39), usd_cny ↓ (1.98)

## India macro
- nifty_50: 24574.3496 (1d -0.16%, z20 1.71, flag amber)
- nifty_midcap_100: 63521.6016 (1d 0.06%, z20 1.60, flag amber)
- usd_inr: 95.1325 (1d -0.21%, z20 -1.81, flag red)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5849 (1d 0.22%, z20 -0.47, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI MPC decision T-2d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 77.4 — "From Gift Nifty to RBI MPC meeting outcome, oil prices: 8 key things that changed for Indi"
- COALINDIA.NS (COAL INDIA LTD) score 74.9 — "From Gift Nifty to RBI MPC meeting outcome, oil prices: 8 key things that changed for Indi"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 74.0 — "From Gift Nifty to RBI MPC meeting outcome, oil prices: 8 key things that changed for Indi"
- INDIANB.NS (INDIAN BANK) score 60.4 — "From Gift Nifty to RBI MPC meeting outcome, oil prices: 8 key things that changed for Indi"
- COIN (Coinbase Global, Inc.) score 49.4 — "Middle East War Triggers New Global Refining Boom"
- BAC (Bank of America Corporation) score 44.4 — "TRUMP CLAIMS RECORD POLL NUMBERS Trump says his “real” poll numbers are the highest they’v"
- TECHM.NS (TECH MAHINDRA LIMITED) score 43.6 — "Stocks to watch: Bharti Airtel, Nykaa, PB Fintech, BSE among shares in focus today; check "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 42.2 — "Stocks to watch: Bharti Airtel, Nykaa, PB Fintech, BSE among shares in focus today; check "
- OHI (Omega Healthcare Investors, In) score 41.9 — "Gold and silver prices today: Rates climb amid a decline in dollar, crude oil prices; inve"
- HDB (HDFC Bank Limited) score 41.7 — "Axis Bank Share Price Live Updates: Axis Bank's Recent Performance"
- IDBI.NS (IDBI BANK LIMITED) score 40.3 — "Axis Bank Share Price Live Updates: Axis Bank's Recent Performance"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 40.3 — "Axis Bank Share Price Live Updates: Axis Bank's Recent Performance"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 38.5 — "Axis Bank Share Price Live Updates: Axis Bank's Recent Performance"
- TECH (Bio-Techne Corp) score 37.1 — "Stocks to watch: Bharti Airtel, Nykaa, PB Fintech, BSE among shares in focus today; check "
- CHKP (Check Point Software Technolog) score 33.2 — "RBI MPC meeting outcome today: Check date, time, and where to watch Governor Sanjay Malhot"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 30.6 — "US TREASURY SECRETARY BESSENT: UPTICK IN JAPAN'S INFLATION WAS RESULT OF WEAK YEN, ENERGY "
- LTH (Life Time Group Holdings, Inc.) score 28.2 — "RBI MPC meeting outcome today: Check date, time, and where to watch Governor Sanjay Malhot"
- 301077.SZ (CHINASTARS) score 20.9 — "China, Turkey Relations Strained After EV Investment Fallout"
- BOND (PIMCO Active Bond Exchange-Tra) score 20.5 — "Oil tumble to support Indian bonds; RBI policy guidance stays large driver"
- MS (Morgan Stanley) score 11.9 — "LIFE: Deutsche Bank PT raised to $40 from $30; Barclays PT raised to $37 from $27 $LIND: B"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.9 — "Tata Steel Share Price Live Updates: Tata Steel Stock Details"
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.4 — "S&P 500 BREAKS OUT, RECORD HIGH IN SIGHT The S&P 500 has regained momentum, closing just 0"
- AMZN (Amazon.com, Inc.) score 9.6 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 9.5 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Price Movement"
- JIOFIN.BO (Jio Financial Services Limited) score 9.2 — "Jio Financial Services Share Price Live Updates: Jio Financial Services sees a slight dip "
- PCJEWELLER.NS (PC JEWELLER LTD) score 9.1 — "Kalyan Jewellers slips 3% as Q1 margin pressure overshadows 32% jump in net profit"
- VT (Vanguard Total World Stock Ind) score 8.6 — "Musk: 'Not Out of the Question' That Starlink Would Deliver Majority of World Internet Wit"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.5 — "Adani Ent Share Price Live Updates: Adani Ent. News"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.5 — "Jio Financial Services Share Price Live Updates: Jio Financial Services sees a slight dip "
- PLTR (Palantir Technologies Inc.) score 7.4 — "Palantir Short Sellers Take $3 Billion Hit After 30% Stock Surge"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 7.2 — "Coal India Share Price Live Updates: Coal India  Market Performance"
- MSFT (Microsoft Corporation) score 6.7 — "SHARES OF US HYPERSCALERS CLIMB • META RISES 6.1% • MICROSOFT JUMPS 4.7% • AMAZON GAINS 4."
- AAPL (Apple Inc.) score 6.1 — "Apple suffers worst rout since 2025 on disappointing outlook"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.5 — "ICICI Securities initiates coverage on 7 PSU banks with positive valuations"
- NVDA (NVIDIA Corporation) score 5.5 — "NVDA - SPACEX CEO ELON MUSK SAYS GOING FORWARD, WE'VE DECIDED TO BUILD EXCLUSIVELY ON NVID"
- INFY (Infosys Limited) score 5.2 — "Infosys Share Price Live Updates: Infosys Stock Details"
- GS (Goldman Sachs Group, Inc. (The) score 5.0 — "Global Market: Goldman Sachs sees Brent crude trading at $80-$90 until Iran conflict outlo"
- META (Meta) score 4.9 — "META INVITED TO WHITE HOUSE TUESDAY TO DISCUSS AI SAFETY TESTING BY U.S. GOVERNMENT - COMP"
- THANGAMAYL.NS (THANGAMAYIL JEWELLERY LTD) score 2.9 — "Thangamayil share selloff continues: Stock drops 5% despite Rs 344 crore sales in first 3 "
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