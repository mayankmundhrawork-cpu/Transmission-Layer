# Transmission Layer — board brief · 2026-08-05 10:47Z

data as of **2026-08-05** · 98 series · 20 red / 28 amber · 8 events surfaced (22 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.349, 3d in regime; vol-pct 0.365, breadth-off 0.333, Markov P(high-vol) 0.185)
- [INVERTED] **safe_haven_gold** — corr20 -0.4, corr60 -0.42, contra nifty_50 corr20=0.1, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.9, corr60 0.82, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.34, corr60 0.32, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.19, corr60 -0.05, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.81, corr60 -0.81, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.01, corr60 -0.02, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.18, corr60 -0.25, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.16, corr60 0.19, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 90** scanned series survive multiplicity control (effective p ≤ 0.0010380708664139426)
- **SETUP** nasdaq_100 → dyn_453950_ks: leads 1d (ccf 0.643, β 0.8755, p 0.0); driver zc 1.96 → expected 2.891%. Type hit-rate 0.822 (n=2885).
- **SETUP** sp500 → dyn_453950_ks: leads 1d (ccf 0.593, β 1.0788, p 0.0); driver zc 1.78 → expected 1.918%. Type hit-rate 0.822 (n=2885).
- **SETUP** dyn_vt → dyn_453950_ks: leads 1d (ccf 0.592, β 1.1206, p 0.0); driver zc 1.69 → expected 1.984%. Type hit-rate 0.822 (n=2885).
- **SETUP** dyn_vt → usd_brl: leads 1d (ccf -0.522, β -0.4267, p 0.0); driver zc 1.69 → expected -0.755%. Type hit-rate 0.822 (n=2885).
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.484, β 0.2629, p 0.0); driver zc 1.58 → expected 0.393%. Type hit-rate 0.822 (n=2885).
- **SETUP** dow_jones → dyn_453950_ks: leads 1d (ccf 0.475, β 0.9457, p 0.0); driver zc 1.67 → expected 1.622%. Type hit-rate 0.822 (n=2885).
- **SETUP** sp500 → usd_brl: leads 1d (ccf -0.446, β -0.3528, p 0.0); driver zc 1.78 → expected -0.627%. Type hit-rate 0.822 (n=2885).
- **SETUP** nasdaq_100 → usd_brl: leads 1d (ccf -0.427, β -0.2482, p 0.0); driver zc 1.96 → expected -0.819%. Type hit-rate 0.822 (n=2885).
- **SETUP** dow_jones → usd_brl: leads 1d (ccf -0.412, β -0.3555, p 0.0); driver zc 1.67 → expected -0.61%. Type hit-rate 0.822 (n=2885).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.358, β -2.3169, p 0.01056); driver zc 1.69 → expected -4.101%. Type hit-rate 0.822 (n=2885).
- **SETUP** dyn_vt → nifty_midcap_100: leads 1d (ccf 0.286, β 0.3501, p 0.0); driver zc 1.69 → expected 0.62%. Type hit-rate 0.822 (n=2885).
- **SETUP** ust_10y → eur_usd: leads 1d (ccf -0.28, β -0.1137, p 0.0); driver zc 1.58 → expected -0.17%. Type hit-rate 0.822 (n=2885).
- **SETUP** ust_10y → gbp_usd: leads 1d (ccf -0.28, β -0.1138, p 0.0); driver zc 1.58 → expected -0.17%. Type hit-rate 0.822 (n=2885).
- **SETUP** sp500 → nifty_midcap_100: leads 1d (ccf 0.261, β 0.3123, p 1e-05); driver zc 1.78 → expected 0.555%. Type hit-rate 0.822 (n=2885).
- **SETUP** dyn_vt → hang_seng: leads 1d (ccf 0.256, β 0.369, p 0.0); driver zc 1.69 → expected 0.653%. Type hit-rate 0.822 (n=2885).
- **SETUP** tips_10y_real → gbp_usd: leads 1d (ccf -0.25, β -0.0562, p 4e-05); driver zc 1.57 → expected -0.14%. Type hit-rate 0.822 (n=2885).
- Track record · residual_reversion: hit-rate **0.493** (n=1153) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.822** (n=2885) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.46] cross-asset · 12 series ↑
- dow_jones [INDICES]: last 54090.66, z20 4.48, zc 1.67, resid-z 0.68 [priced], 1d 1.72%, |z20|=4.48; 1y-pct=100
- comex_gold [COMMODITIES]: last 4212.90, z20 3.72, zc 1.99, resid-z -1.68 [unexplained], 1d 2.87%, |z20|=3.72; co-occur[gold_silver] same-direction (channel VALID)
- sp500 [INDICES]: last 7735.60, z20 3.68, zc 1.78, resid-z 0.82 [priced], 1d 1.78%, |z20|=3.68; 1y-pct=100
- russell_2000 [INDICES]: last 3037.07, z20 3.65, zc 1.48, resid-z -0.34 [quiet], 1d 1.85%, |z20|=3.65; 1y-pct=100
- dyn_vt [EQUITIES]: last 160.40, z20 3.55, zc 1.69, resid-z -2.02 [unexplained], 1d 1.77%, |z20|=3.55; 1y-pct=100
- stoxx_50 [INDICES]: last 6481.47, z20 2.82, zc -0.08, resid-z -0.93 [quiet], 1d -0.08%, |z20|=2.82; 1y-pct=99
- comex_silver [COMMODITIES]: last 61.42, z20 2.62, zc 0.83, resid-z -1.42 [quiet], 1d 2.28%, |z20|=2.62; co-occur[gold_silver] same-direction (channel VALID)
- cac_40 [INDICES]: last 8662.32, z20 2.61, zc -0.06, resid-z -0.94 [quiet], 1d -0.05%, |z20|=2.61; 1y-pct=99
- dax [INDICES]: last 26189.60, z20 2.51, zc -0.06, resid-z -0.78 [quiet], 1d -0.05%, |z20|=2.51; 1y-pct=99
- comex_copper [COMMODITIES]: last 6.64, z20 2.42, zc 0.14, resid-z -1.06 [quiet], 1d 0.32%, |z20|=2.42; 1y-pct=99; co-occur[metal_copper] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 68.59, z20 -1.34, zc n/a, resid-z n/a [quiet], 1d 0.58%, GSR<75 (extreme low)
- ftse_100 [INDICES]: last 10885.09, z20 1.34, zc 0.10, resid-z -0.25 [quiet], 1d 0.05%, 1y-pct=98
- **Mechanism**: The current move is driven by a cross-asset rally, with 12 series showing an upward trend, led by the Dow Jones and S&P 500. The move is largely priced, with a big raw move accompanied by small resid_z values, indicating that the market has already factored in the recent gains. The gold and silver markets are also showing a co-movement, with a VALID gold_silver_comove channel, suggesting that the monetary metals are rotating together.
- **Gap**: No gap: the current move is largely priced, with small resid_z values indicating that the market has already factored in the recent gains.
- **India take**: The Indian markets, particularly the Nifty 50 and Nifty Metal, have already reacted to the global cues, with the Nifty 50 slipping 0.18% and the Nifty Metal showing a gain. The metal sector is likely to continue its upward trend, driven by the commodity price movement.
- Watch next: nifty_50 (up) — already moved; reacted to global cues
- Watch next: nifty_metal (up) — already moved; reacted to commodity price movement
- **India receivers**: nifty_50 (rho 0.524, z 1.92); nifty_midcap_100 (rho 0.52, z 1.74); nifty_metal (rho 0.464, z 4.14); nifty_it (rho 0.351, z 1.62)
- Source: Michael Burry warns of 1987-style crash as AI rally powers Wall Street; investor shorts Nvidia, Tesla, Palantir — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/michael-burry-warns-of-1987-style-crash-as-ai-rally-powers-wall-street-investor-shorts-nvidia-tesla-palantir-11785922333250.html
- Source: Top Gainers & Losers on 5 August: Hindustan Copper, OLA, HFCL, Mphasis, Tata Capital among top gainers — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-5-august-hindustan-copper-ola-hfcl-mphasis-tata-capital-among-top-gainers-11785922141765.html
- Source: Explained: Why South Korea bought gold after 13 years and what it means for yellow metal investors? — ET Markets, 2026-08-05. https://economictimes.indiatimes.com/markets/commodities/news/explained-why-south-korea-bought-gold-after-13-years-and-what-it-means-for-yellow-metal-investors/articleshow/132907438.cms
- Historical analogues: 2024-10-09 (d=0.96), 2024-11-26 (d=1.02), 2025-10-31 (d=1.03)

### [RED 9.32] dyn_pltr ↑
- dyn_pltr [EQUITIES]: last 162.63, z20 7.32, zc 8.98, resid-z -0.24 [moved], 1d 29.43%, |z20|=7.32
- **Mechanism**: The recent surge in dyn_pltr is driven by strong demand for AI-powered data analytics, with Palantir's stock jumping 27% after raising its full-year financial outlook. This move is priced, with a low resid_z of -0.24, indicating that the factor exposures explain the majority of the move. The VALID vix_equity_inverse channel suggests that the vol spike will lead to an equity drawdown, but the current RISK_ON regime may mitigate this effect.
- **Gap**: No gap: the move in dyn_pltr is largely explained by its factor exposures, with a low resid_z of -0.24, indicating that the price move is priced in.
- **India take**: The Indian instrument dyn_atherenerg_ns has already reacted, with a rho of 0.399 via dyn_pltr, and may continue to move in tandem with dyn_pltr. The metal_copper_channel may also play a role in transmitting the move to Indian metal equities.
- Watch next: dyn_atherenerg_ns (up) — already moved; rho=0.399 via dyn_pltr
- **India receivers**: dyn_atherenerg_ns (rho 0.399, z 3.77)
- Source: Michael Burry warns of 1987-style crash as AI rally powers Wall Street; investor shorts Nvidia, Tesla, Palantir — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/michael-burry-warns-of-1987-style-crash-as-ai-rally-powers-wall-street-investor-shorts-nvidia-tesla-palantir-11785922333250.html
- Source: Palantir Short Sellers Take $3 Billion Hit After 30% Stock Surge — Mint Markets, 2026-08-04. https://www.livemint.com/market/palantir-short-sellers-take-3-billion-hit-after-30-stock-surge-11785872351134.html
- Source: Palantir climbs 27% on 'otherworldly' AI demand; Karp tells shareholders business has 'Marxist' values — Mint Markets, 2026-08-04. https://www.livemint.com/market/stock-market-news/palantir-climbs-27-on-otherworldly-ai-demand-karp-tells-shareholders-business-has-marxist-values-11785861835803.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-01 (d=0.08), 2025-10-13 (d=0.13)

### [RED 6.84] usd_inr ↓
- usd_inr [FX]: last 95.12, z20 -1.84, zc -0.52, resid-z -0.66 [quiet], 1d -0.22%, 20d range extreme; |z20|=1.84; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: The recent decline in usd_inr is largely priced, given the small resid_z of -0.66, which suggests that the move is mostly explained by factor exposures. The drop in oil prices and a weakening dollar have contributed to the rupee's strength. However, the RBI's decision to maintain rates has restricted further growth. The valid channels, such as gold_silver_comove and metal_copper_channel, do not directly influence the usd_inr move, but the risk-on regime and the inverse safe_haven_gold channel indicate a broader market sentiment that supports the rupee's strength.
- **Gap**: No gap: the usd_inr move is largely priced, with a small resid_z and a big raw move, indicating that the market has already accounted for the factors driving the decline.
- **India take**: The Indian instrument dyn_havells_ns has already reacted to the usd_inr move, given its rho of 0.415. Other transmission candidates, such as dyn_bharatcoal_ns and eur_inr, remain quiet for now.
- Watch next: dyn_havells_ns (up) — already moved; rho=0.415 via usd_inr
- **India receivers**: dyn_havells_ns (rho 0.415, z 2.06); dyn_bharatcoal_ns (rho 0.408, z -0.99); eur_inr (rho 0.381, z 0.37)
- Source: Rupee hits one-month closing high as oil slide outweighs RBI pause — ET Markets, 2026-08-05. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-hits-one-month-closing-high-as-oil-slide-outweighs-rbi-pause/articleshow/132916592.cms
- Source: Rupee sails past 95 to one-month high, premiums drop before RBI decision — ET Markets, 2026-08-05. https://economictimes.indiatimes.com/markets/forex/rupee-sails-past-95-to-one-month-high-premiums-drop-before-rbi-decision/articleshow/132890285.cms
- Source: Rupee jumps 39 paise to 94.89 against US dollar ahead of RBI monetary policy decision — BusinessLine Mkts, 2026-08-05. https://www.thehindubusinessline.com/markets/forex/rupee-jumps-39-paise-to-9489-against-us-dollar-ahead-of-rbi-monetary-policy-decision/article71308047.ece
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2024-10-24 (d=0.01)

### [AMBER 5.94] brent ↓
- brent [COMMODITIES]: last 80.65, z20 -0.94, zc 0.39, resid-z -0.62 [quiet], 1d 1.63%, 1-session move +1.63% ≥ 1.5%; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: The recent decline in Brent crude oil prices is likely to propagate through the metal_copper_channel, given its VALID status and correlation with global copper prices, which in turn can influence Indian metal equities. However, the primary transmission candidate, inr_oil_channel, is WEAK, suggesting a less direct impact on the Indian rupee. The RISK_ON regime and VALID vix_equity_inverse channel also indicate a potential for volatility to decrease, supporting a positive outlook for equities.
- **Gap**: No gap: brent's move is largely priced, with a resid_z of -0.62, indicating that the decline is mostly explained by factor exposures
- **India take**: The Indian instrument that expresses this move is the nifty_midcap_100, which has already reacted to the brent decline. The midcap_largecap_ratio, another transmission candidate, remains quiet, suggesting a potential for further movement.
- Watch next: nifty_midcap_100 (up) — already moved; reacted to brent decline
- **India receivers**: nifty_midcap_100 (rho -0.451, z 1.74); midcap_largecap_ratio (rho -0.381, z -0.62)
- Source: Rupee hits one-month closing high as oil slide outweighs RBI pause — ET Markets, 2026-08-05. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-hits-one-month-closing-high-as-oil-slide-outweighs-rbi-pause/articleshow/132916592.cms
- Source: Oil Erases Decline as Traders Weigh Fresh Houthi Threat — Mint Markets, 2026-08-05. https://www.livemint.com/market/oil-erases-decline-as-traders-weigh-fresh-houthi-threat-11785917157048.html
- Source: India bonds jump as oil crashes, dovish RBI may further boost rally — ET Markets, 2026-08-05. https://economictimes.indiatimes.com/markets/bonds/india-bonds-jump-as-oil-crashes-dovish-rbi-may-further-boost-rally/articleshow/132899559.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.0), 2024-10-18 (d=0.02)

### [RED 5.77] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1467.00, z20 3.77, zc 0.35, resid-z 0.21 [quiet], 1d 1.14%, |z20|=3.77; 1y-pct=100
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Ather Energy shares jump 14% after Q1 loss narrows — BusinessLine Mkts, 2026-08-04. https://www.thehindubusinessline.com/markets/ather-energy-shares-jump-18-to-fresh-52-week-high-after-q1-loss-narrows/article71303894.ece
- Source: Ather Energy's tapering losses put stock in fast lane, but is the rally justified? — Mint Markets, 2026-08-04. https://www.livemint.com/market/mark-to-market/ather-energy-electric-vehicles-ev-q1fy27-ebitda-operating-losses-ev-sales-hero-motocorp-11785824423599.html
- Source: Multibagger stock Ather Energy share price soars 18% to record high post Q1 FY27 results: Should you buy? — Mint Markets, 2026-08-04. https://www.livemint.com/market/stock-market-news/multibagger-stock-ather-energy-share-price-soars-18-to-record-high-post-q1-fy27-results-should-you-buy-11785824415092.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

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

### [AMBER 5.43] cross-asset · 3 series ↑
- dyn_jiofin_bo [EQUITIES]: last 261.50, z20 2.11, zc -0.53, resid-z -1.00 [quiet], 1d -1.15%, |z20|=2.11
- nifty_50 [INDICES]: last 24624.65, z20 1.92, zc 0.05, resid-z -1.06 [quiet], 1d 0.04%, |z20|=1.92
- nifty_midcap_100 [INDICES]: last 63597.60, z20 1.74, zc 0.23, resid-z 0.18 [quiet], 1d 0.18%, |z20|=1.74; 1y-pct=99
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-17 (z-distance 0.69).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.695 via nifty_midcap_100, z -2.07, reacted); dyn_bharatcoal_ns (rho 0.641 via nifty_midcap_100, z -0.99, quiet); dyn_indianb_ns (rho 0.62 via nifty_midcap_100, z 1.07, reacted); dyn_indusindbk_bo (rho 0.619 via nifty_midcap_100, z 0.04, quiet); nifty_metal (rho 0.578 via nifty_midcap_100, z 4.14, reacted)
- Watch next: dyn_bharatcoal_ns (co-move) — not yet - watch; rho 0.641 vs nifty_midcap_100, historically leads by 0d
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.574 vs nifty_50, historically leads by 3d
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.579 vs nifty_50
- Watch next: dyn_indusindbk_bo (co-move) — not yet - watch; rho 0.533 vs dyn_jiofin_bo
- **India receivers**: dyn_muthootfin_ns (rho 0.695, z -2.07); dyn_bharatcoal_ns (rho 0.641, z -0.99); dyn_indianb_ns (rho 0.62, z 1.07); dyn_indusindbk_bo (rho 0.619, z 0.04)
- Source: Sensex rises 152 points, Nifty closes above 24,600 as market trims gains. What lies ahead? — ET Markets, 2026-08-05. https://economictimes.indiatimes.com/markets/stocks/news/sensex-rises-152-points-nifty-closes-above-24600-as-market-trims-gains-what-lies-ahead/articleshow/132915892.cms
- Source: Sensex today | Stock Market Live: Sensex, Nifty slip into the red by mid-session; RBI keeps repo rate unchanged at 5.25% — BusinessLine Mkts, 2026-08-05. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-5th-august-2026/article71306480.ece
- Source: Sensex gains 150 points, Nifty 50 ends flat above 24,600 after RBI MPC keeps interest rates unchanged — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/sensex-gains-150-points-nifty-50-ends-flat-above-24-600-after-rbi-mpc-keeps-interest-rates-unchanged-11785922265051.html
- Historical analogues: 2025-07-17 (d=0.69), 2024-11-07 (d=0.98), 2025-08-13 (d=1.26)

### [RED 5.37] cross-asset · 2 series ↑
- usd_jpy [FX]: last 157.75, z20 -2.53, zc 0.25, resid-z 0.23 [quiet], 1d 0.14%, |z20|=2.53
- dyn_amzn [EQUITIES]: last 277.43, z20 2.39, zc -0.22, resid-z 9.76 [unexplained], 1d -2.32%, |z20|=2.39; 1y-pct=99
- **Mechanism**: The recent coordinated intervention by Tokyo has led to a surge in the yen, with the usd_jpy experiencing a significant move. However, the resid_z of 0.23 indicates that this move is largely priced in, given the current factor exposures. The dyn_amzn, on the other hand, has an unexplained move with a resid_z of 9.76, suggesting that this move may not be fully priced in.
- **Gap**: No gap: the move in usd_jpy is largely priced in, while the move in dyn_amzn is unexplained but has already occurred
- **India take**: The Indian instrument dyn_muthootfin_ns has reacted to the move in usd_jpy, with a rho of -0.506 and a z20 of -2.07. However, dyn_cartrade_ns, which is correlated with dyn_amzn, remains quiet with a z20 of 0.63.
- Watch next: dyn_amzn (up) — already moved; unexplained move with high resid_z
- **India receivers**: dyn_muthootfin_ns (rho -0.506, z -2.07); dyn_cartrade_ns (rho -0.361, z 0.63)
- Source: US TREASURY SECRETARY BESSENT: UPTICK IN JAPAN'S INFLATION WAS RESULT OF WEAK YEN, ENERGY PRICES — DeItaone, 2026-08-04. https://t.me/walter_bloomberg/34358
- Source: Yen holds most gains as intervention keeps speculators on edge — Mint Markets, 2026-08-04. https://www.livemint.com/market/yen-holds-most-gains-as-intervention-keeps-speculators-on-edge-11785874259298.html
- Source: BOFA: TARGET FX VOLATILITY, NOT THE WHOLE MARKET Bank of America says investors should focus on specific currency pairs—not broad FX volatility—if the Fed resumes rate hikes. The bank highlights Japanese yen and British pound pairs as the strongest opportunities. Historically, — DeItaone, 2026-08-04. https://t.me/walter_bloomberg/34270
- Historical analogues: 2024-10-16 (d=0.15), 2024-11-21 (d=0.23), 2026-03-31 (d=0.24)

## Watchlist (below surfacing floor)
dyn_msft ↑ (5.15), fx · 3 series ↑ (4.25), dyn_infy ↑ (4.19), nifty_metal ↑ (4.14), dyn_thangamayl_ns ↓ (4.1), dyn_muthootfin_ns ↓ (4.07), dyn_bac ↑ (3.67), dyn_coin ↓ (3.55), asx_200 ↑ (3.41), dyn_lth ↑ (3.38), dyn_cupid_ns ↑ (3.22), dyn_tech ↑ (3.17)

## India macro
- nifty_50: 24624.6504 (1d 0.04%, z20 1.92, flag amber)
- nifty_midcap_100: 63597.6016 (1d 0.18%, z20 1.74, flag amber)
- usd_inr: 95.1200 (1d -0.22%, z20 -1.84, flag red)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5827 (1d 0.14%, z20 -0.62, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI MPC decision T-2d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 79.4 — "MapMyIndia shares drop 8% despite strong Q1 earnings; PAT jumps 8% YoY"
- COALINDIA.NS (COAL INDIA LTD) score 77.0 — "MapMyIndia shares drop 8% despite strong Q1 earnings; PAT jumps 8% YoY"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 76.1 — "MapMyIndia shares drop 8% despite strong Q1 earnings; PAT jumps 8% YoY"
- INDIANB.NS (INDIAN BANK) score 61.1 — "HSBC picks ICICI Bank, Titan, 8 other stocks to ride a potential $25 billion FII inflow as"
- COIN (Coinbase Global, Inc.) score 55.5 — "Global Market: China stocks hit one-week high as chip rally offsets optical module slump"
- TECHM.NS (TECH MAHINDRA LIMITED) score 45.9 — "Sterlite Tech, HFCL gain 5% each on reports of US ban on Chinese data centre devices"
- BAC (Bank of America Corporation) score 45.7 — "HSBC picks ICICI Bank, Titan, 8 other stocks to ride a potential $25 billion FII inflow as"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 44.6 — "Sterlite Tech, HFCL gain 5% each on reports of US ban on Chinese data centre devices"
- OHI (Omega Healthcare Investors, In) score 44.3 — "MCX shares fall 4% after Q1 profit falls 22% QoQ to Rs 413 crore. What should investors do"
- HDB (HDFC Bank Limited) score 43.1 — "HSBC picks ICICI Bank, Titan, 8 other stocks to ride a potential $25 billion FII inflow as"
- IDBI.NS (IDBI BANK LIMITED) score 41.7 — "HSBC picks ICICI Bank, Titan, 8 other stocks to ride a potential $25 billion FII inflow as"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 41.7 — "HSBC picks ICICI Bank, Titan, 8 other stocks to ride a potential $25 billion FII inflow as"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 40.0 — "HSBC picks ICICI Bank, Titan, 8 other stocks to ride a potential $25 billion FII inflow as"
- TECH (Bio-Techne Corp) score 39.6 — "Sterlite Tech, HFCL gain 5% each on reports of US ban on Chinese data centre devices"
- CHKP (Check Point Software Technolog) score 31.9 — "RBI MPC meeting outcome today: Check date, time, and where to watch Governor Sanjay Malhot"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 31.5 — "Essar Energy Transition secures $400 million in financing"
- LTH (Life Time Group Holdings, Inc.) score 30.1 — "RBI's status quo on rates to support housing demand, keep real estate sentiment intact: In"
- 301077.SZ (CHINASTARS) score 24.1 — "Global Market: China stocks hit one-week high as chip rally offsets optical module slump"
- BOND (PIMCO Active Bond Exchange-Tra) score 20.7 — "India bonds jump as oil crashes, dovish RBI may further boost rally"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 12.4 — "Top Gainers & Losers on 5 August: Hindustan Copper, OLA, HFCL, Mphasis, Tata Capital among"
- MS (Morgan Stanley) score 11.5 — "LIFE: Deutsche Bank PT raised to $40 from $30; Barclays PT raised to $37 from $27 $LIND: B"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.9 — "S&P 500 BREAKS OUT, RECORD HIGH IN SIGHT The S&P 500 has regained momentum, closing just 0"
- JIOFIN.BO (Jio Financial Services Limited) score 10.8 — "Global Market: China's services growth slows to 10-month low in July; weak demand weighs o"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 10.2 — "ICICI Bank, Bajaj Finance among Axis Securities’ top 8 largecap stock picks for August"
- PCJEWELLER.NS (PC JEWELLER LTD) score 9.7 — "Kalyan Jewellers shares extend slide, tumble 5% after Q1 results; down 11% in four days"
- VT (Vanguard Total World Stock Ind) score 9.2 — "Central banks made the highest purchase of gold in June for 2026, says World Gold Council"
- AMZN (Amazon.com, Inc.) score 9.2 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.2 — "Adani Ent Share Price Live Updates: Adani Ent. News"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.2 — "Jio Financial Services Share Price Live Updates: Jio Financial Services sees a slight dip "
- PLTR (Palantir Technologies Inc.) score 8.2 — "Michael Burry warns of 1987-style crash as AI rally powers Wall Street; investor shorts Nv"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.3 — "HSBC picks ICICI Bank, Titan, 8 other stocks to ride a potential $25 billion FII inflow as"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 7.0 — "Coal India Share Price Live Updates: Coal India  Market Performance"
- META (Meta) score 6.7 — "Explained: Why South Korea bought gold after 13 years and what it means for yellow metal i"
- MSFT (Microsoft Corporation) score 6.5 — "SHARES OF US HYPERSCALERS CLIMB • META RISES 6.1% • MICROSOFT JUMPS 4.7% • AMAZON GAINS 4."
- NVDA (NVIDIA Corporation) score 6.3 — "Michael Burry warns of 1987-style crash as AI rally powers Wall Street; investor shorts Nv"
- AAPL (Apple Inc.) score 5.9 — "Apple suffers worst rout since 2025 on disappointing outlook"
- INFY (Infosys Limited) score 5.0 — "Infosys Share Price Live Updates: Infosys Stock Details"
- GS (Goldman Sachs Group, Inc. (The) score 4.8 — "Global Market: Goldman Sachs sees Brent crude trading at $80-$90 until Iran conflict outlo"
- THANGAMAYL.NS (THANGAMAYIL JEWELLERY LTD) score 2.8 — "Thangamayil share selloff continues: Stock drops 5% despite Rs 344 crore sales in first 3 "
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