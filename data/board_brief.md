# Transmission Layer — board brief · 2026-07-28 17:16Z

data as of **2026-07-28** · 98 series · 11 red / 35 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.476, 3d in regime; vol-pct 0.599, breadth-off 0.353, Markov P(high-vol) 0.02)
- [INVERTED] **safe_haven_gold** — corr20 -0.29, corr60 -0.44, contra nifty_50 corr20=0.08, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.9, corr60 0.82, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.35, corr60 0.36, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.28, corr60 0.01, last shift 2026-06-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.9, corr60 -0.82, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.1, corr60 -0.06, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.07, corr60 -0.25, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.39, corr60 0.24, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 90** scanned series survive multiplicity control (effective p ≤ 2.553706882757467e-05)
- **SETUP** dow_jones → dyn_453950_ks: leads 1d (ccf 0.432, β 0.9263, p 0.0); driver zc 1.64 → expected 1.177%. Type hit-rate 0.817 (n=3179).
- **SETUP** dow_jones → taiwan_weighted: leads 1d (ccf 0.428, β 0.7313, p 0.0); driver zc 1.64 → expected 0.929%. Type hit-rate 0.817 (n=3179).
- **SETUP** dow_jones → usd_brl: leads 1d (ccf -0.415, β -0.359, p 0.0); driver zc 1.64 → expected -0.456%. Type hit-rate 0.817 (n=3179).
- **SETUP** dow_jones → nikkei_225: leads 1d (ccf 0.413, β 0.7714, p 0.0); driver zc 1.64 → expected 0.98%. Type hit-rate 0.817 (n=3179).
- **SETUP** dow_jones → aud_usd: leads 1d (ccf 0.394, β 0.2589, p 1e-05); driver zc 1.64 → expected 0.329%. Type hit-rate 0.817 (n=3179).
- **SETUP** dow_jones → usd_mxn: leads 1d (ccf -0.348, β -0.2475, p 0.0); driver zc 1.64 → expected -0.315%. Type hit-rate 0.817 (n=3179).
- Track record · residual_reversion: hit-rate **0.491** (n=1151) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=3179) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.25] dyn_coalindia_ns ↓
- dyn_coalindia_ns [EQUITIES]: last 410.40, z20 -5.25, zc -3.70, resid-z -2.39 [unexplained], 1d -4.00%, |z20|=5.25
- **Mechanism**: The decline in Coal India's shares is driven by weak operating performance, higher costs, and weaker-than-expected realisations, despite a 16.6% YoY increase in capex. The metal_copper_channel, which is VALID, may transmit this move to other Indian metal equities. The vix_equity_inverse channel also suggests that the vol spike could lead to further equity drawdown.
- **Gap**: No gap: the move in Coal India's shares is largely priced in, given the weak operating performance and higher costs, with resid_z = -2.39 indicating some unexplained component but not a significant anomaly
- **India take**: The Indian instrument expressing this move is the Nifty Metal index, which may react negatively to the weak operating performance of Coal India. The Nifty Metal index has not yet reacted, but it is worth watching for potential downside.
- Watch next: nifty_metal (down) — not yet - watch; weak operating performance of Coal India may impact other metal stocks
- Source: Coal India Q1 capex rises 16.6% YoY to  ₹3,399 crore, beats quarterly target — Mint Markets, 2026-07-28. https://www.livemint.com/market/stock-market-news/coal-india-q1-capex-rises-16-6-yoy-to-rs-3-399-crore-in-beats-quarterly-target-11785250551117.html
- Source: Coal India shares fall 4% weighed by weak operating performance — BusinessLine Mkts, 2026-07-28. https://www.thehindubusinessline.com/markets/coal-india-shares-fall-over-3-after-q1-results-weak-operating-performance-weighs-on-stock/article71275552.ece
- Source: Coal India shares fall over 3% weighed by weak operating performance — BusinessLine Mkts, 2026-07-28. https://www.thehindubusinessline.com/markets/coal-india-shares-fall-over-3-after-q1-results-weak-operating-performance-weighs-on-stock/article71275552.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.03), 2024-11-07 (d=0.04)

### [RED 7.04] indices · 5 series ↑
- ftse_100 [INDICES]: last 10878.93, z20 3.10, zc 1.10, resid-z 0.27 [quiet], 1d 0.90%, |z20|=3.10; 1y-pct=99
- dow_jones [INDICES]: last 52873.56, z20 1.43, zc 1.64, resid-z 1.03 [moved], 1d 1.27%, 1y-pct=98
- cac_40 [INDICES]: last 8459.41, z20 1.28, zc 0.64, resid-z -0.51 [quiet], 1d 0.63%, 1y-pct=96
- dax [INDICES]: last 25489.74, z20 1.16, zc 0.46, resid-z -0.35 [quiet], 1d 0.51%, 1y-pct=98
- stoxx_50 [INDICES]: last 6291.54, z20 0.03, zc 0.14, resid-z -1.21 [quiet], 1d 0.15%, 1y-pct=96
- **Mechanism**: The recent surge in US stocks, led by the Dow Jones, is driven by a pause in US-Iran hostilities and a positive sentiment ahead of a busy week of corporate earnings, economic data, and an interest-rate decision. This move is largely priced, with a small resid_z value indicating that the factor exposures explain most of the move. The valid vix_equity_inverse channel suggests that the vol spike is inversely related to equity drawdown, which may contribute to the current market sentiment.
- **Gap**: No gap: the move is largely priced, with small resid_z values for most indices, indicating that factor exposures explain most of the move
- **India take**: The Indian instrument nifty_50, which has a historical lead of 1d via cac_40, may react positively to the current market sentiment, although it has not moved yet. The nifty_midcap_100 may also be affected, given its correlation with stoxx_50.
- Watch next: nifty_50 (up) — not yet - watch; historical lead of 1d via cac_40
- **India receivers**: nifty_50 (rho 0.62, z -0.64); nifty_midcap_100 (rho 0.594, z 0.13)
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks turn positive as Dow surges 650 pts despite chip rout — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-hormuz-brent-crude-oil-fed-warsh-rate-hike-big-tech-earnings-amazon-meta-apple-microsoft-tesla-spacex-chip-stock-price-news-28th-june-2026/liveblog/132684702.cms
- Source: U.S. STOCKS EXTEND GAINS, DOW JONES UP 1.08% — DeItaone, 2026-07-27. https://t.me/walter_bloomberg/33935
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US market opens higher as pause in US-Iran hostilities lifts sentiment — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-fed-warsh-microsoft-amazon-meta-alphabet-tesla-chip-stock-price-news-27th-july-2026/liveblog/132661511.cms
- Historical analogues: 2024-11-11 (d=0.71), 2024-10-22 (d=0.96), 2024-11-21 (d=0.97)

### [RED 6.25] indices · 3 series ↓
- nikkei_225 [INDICES]: last 62313.21, z20 -2.93, zc -1.93, resid-z -1.93 [unexplained], 1d -4.03%, |z20|=2.93
- taiwan_weighted [INDICES]: last 41635.37, z20 -2.77, zc -1.98, resid-z -2.31 [unexplained], 1d -4.58%, |z20|=2.77
- kospi [INDICES]: last 6019.06, z20 -2.17, zc -2.49, resid-z -2.66 [unexplained], 1d -10.90%, |z20|=2.17
- **Mechanism**: The global chip selloff, led by losses on Wall Street, has transmitted to Asian markets, causing a sharp decline in semiconductor-related stocks and dragging down indices such as the Nikkei 225, Taiwan Weighted, and Kospi. This transmission is facilitated by verified lead-lag relationships, such as the Dow Jones leading the Taiwan Weighted and Nikkei 225.
- **Gap**: No gap: the big raw moves in Nikkei 225, Taiwan Weighted, and Kospi are accompanied by small resid_z values, indicating that the moves are largely priced and not anomalous
- **India take**: Indian metal equities, such as those in the Nifty Metal index, have already reacted to the global chip selloff, while other Indian stocks like HDFC Bank and Tech Mahindra have also moved in response to the transmission from Asian markets.
- Watch next: nifty_metal (down) — already moved; rho=0.498 via Kospi
- Watch next: dyn_hdbfs_bo (down) — already moved; rho=0.467 via Nikkei 225
- Watch next: dyn_techm_ns (up) — already moved; rho=-0.416 via Taiwan Weighted
- Watch next: dyn_pcjeweller_ns (down) — already moved; rho=0.377 via Taiwan Weighted
- **India receivers**: nifty_metal (rho 0.498, z -1.35); dyn_hdbfs_bo (rho 0.467, z -2.33); dyn_techm_ns (rho -0.416, z 2.14); dyn_pcjeweller_ns (rho 0.377, z -1.11)
- Source: GLOBAL CHIP SELLOFF DEEPENS Chip stocks extended losses across Asia after a sharp U.S. selloff, fueled by concerns over AI spending and China's technological progress. South Korea's Kospi plunged 10%, triggering two trading halts, while Japan's Nikkei fell 4%. U.S. chip stocks — DeItaone, 2026-07-28. https://t.me/walter_bloomberg/33992
- Source: Global Market: Japan’s Nikkei plunges over 4% as chip stocks track global tech selloff — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-plunges-over-4-as-chip-stocks-track-global-tech-selloff/articleshow/132676159.cms
- Source: Japan’s Nikkei tumbles over 3% as chip stock selloff deepens after Wall Street decline — BusinessLine Mkts, 2026-07-28. https://www.thehindubusinessline.com/markets/stock-markets/japans-nikkei-tumbles-over-3-as-chip-stock-selloff-deepens-after-wall-street-decline/article71275340.ece

### [RED 5.98] dyn_lth ↑
- dyn_lth [EQUITIES]: last 44.91, z20 3.98, zc 1.23, resid-z -0.11 [quiet], 1d 2.63%, |z20|=3.98; 1y-pct=100
- **Mechanism**: The recent surge in dyn_lth is not accompanied by a significant resid_z, indicating that the move is largely priced in by the market. The valid metal_copper_channel and gold_silver_comove channels suggest that monetary metals and global copper are co-moving, which could be influencing the dyn_lth. However, the weak inr_oil_channel and dxy_inr_channel imply that the Indian market may not be directly impacted by these global trends.
- **Gap**: No gap: The dyn_lth move is largely priced in, with a small resid_z of -0.11, indicating no significant unexplained component.
- **India take**: The Indian market may express this move through metal equities, such as those in the metal_copper_channel, but the weak inr_oil_channel and dxy_inr_channel suggest that the impact may be limited. The Nifty 50 may be a responder to this trend, but it has not yet moved significantly.
- Watch next: nifty_50 (down) — not yet - watch; Potential risk-off sentiment due to weaker-than-expected earnings
- Watch next: hindustan_unilever (down) — already moved; Weaker-than-expected Q1 earnings
- Source: Gold price outlook: Chris Wood of Jefferies says it's time to buy gold again; believes next rally could be bigger — Mint Markets, 2026-07-28. https://www.livemint.com/market/commodities/gold-price-outlook-chris-wood-of-jefferies-says-its-time-to-buy-gold-again-believes-next-rally-could-be-bigger-11785232982540.html
- Source: US Fed meeting begins today: Check date, time and where to watch Kevin Warsh's speech — Mint Markets, 2026-07-28. https://www.livemint.com/market/stock-market-news/us-fed-meeting-begins-today-check-date-time-and-where-to-watch-kevin-warshs-speech-11785222523367.html
- Source: HUL shares slide 5% after weaker-than-expected Q1; PAT dips 3% to Rs 2,673 crore on one-time credit — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/news/hul-shares-slide-5-after-weaker-than-expected-q1-pat-dips-3-to-rs-2673-crore-on-one-time-credit/articleshow/132676380.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.01), 2025-04-17 (d=0.02)

### [AMBER 5.96] cross-asset · 5 series ↑
- ust_2y [RATES]: last 4.33, z20 2.03, zc -0.71, resid-z -1.16 [quiet], 1d -0.92%, |z20|=2.03; 1y-pct=99
- tips_10y_real [RATES]: last 2.43, z20 1.85, zc 0.00, resid-z -0.30 [quiet], 1d 0.00%, |z20|=1.85; 1y-pct=99
- ust_10y [RATES]: last 4.69, z20 1.72, zc -0.44, resid-z -0.72 [quiet], 1d -0.42%, |z20|=1.72; 1y-pct=99
- ust_30y [RATES]: last 5.16, z20 1.38, zc -0.30, resid-z -0.44 [quiet], 1d -0.19%, 1y-pct=99
- dyn_bond [EQUITIES]: last 91.08, z20 -0.46, zc 1.08, resid-z 0.09 [quiet], 1d 0.31%, 1y-pct=3
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (inverse) — not yet - watch; rho -0.566 vs tips_10y_real, historically leads by 4d
- Watch next: ust_2s10s (inverse) — not yet - watch; rho -0.543 vs ust_2y, historically leads by 1d
- Watch next: wti (co-move) — not yet - watch; rho 0.514 vs ust_10y, historically leads by 3d
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.544 vs ust_2y
- Watch next: brent (co-move) — not yet - watch; rho 0.501 vs ust_10y
- Source: Global Market: Japan's 10-year bond yield climbs as fiscal concerns weigh on market ahead of BOJ meeting — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-10-year-bond-yield-climbs-as-fiscal-concerns-weigh-on-market-ahead-of-boj-meeting/articleshow/132680390.cms
- Source: JPMORGAN TURNS BULLISH ON STOCKS JPMorgan said its tactical positioning monitor is flashing a buy signal, pointing to further upside for the S&P 500. The bank expects lower bond yields, a weaker dollar, steady Fed policy, and strong earnings to support equities, while warning — DeItaone, 2026-07-27. https://t.me/walter_bloomberg/33969
- Source: Bond investors, unsure about Fed policy outlook, hedge against US rate shock — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/bonds/bond-investors-unsure-about-fed-policy-outlook-hedge-against-us-rate-shock/articleshow/132665831.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [AMBER 5.96] commodities · 2 series ↑
- wti [COMMODITIES]: last 78.43, z20 0.13, zc -1.58, resid-z -1.24 [moved], 1d -5.06%, 1-session move -5.06% ≥ 1.5%
- brent [COMMODITIES]: last 83.38, z20 0.10, zc -1.51, resid-z -1.47 [moved], 1d -5.64%, 1-session move -5.64% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.607 via brent, z 0.13, quiet); dyn_jiofin_bo (rho -0.449 via brent, z -0.19, quiet)
- Watch next: nifty_midcap_100 (inverse) — not yet - watch; rho -0.602 vs wti
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.556 vs wti
- Watch next: india_vix (co-move) — not yet - watch; rho 0.521 vs brent
- **India receivers**: nifty_midcap_100 (rho -0.607, z 0.13); dyn_jiofin_bo (rho -0.449, z -0.19)
- Source: Forget oil. A surging El Niño could kill Fed rate cuts — and these stocks stand to win. — MarketWatch Top, 2026-07-28. https://www.marketwatch.com/story/forget-oil-a-surging-el-nino-could-kill-fed-rate-cuts-and-these-stocks-stand-to-win-41f8e67f?mod=mw_rss_topstories
- Source: Oil Prices Retreat, But the Strait of Hormuz Remains the Wild Card — OilPrice, 2026-07-28. https://oilprice.com/Energy/Energy-General/Oil-Prices-Retreat-But-the-Strait-of-Hormuz-Remains-the-Wild-Card.html
- Source: Economists Cut India’s GDP Growth Forecast on Oil Price Shock — OilPrice, 2026-07-28. https://oilprice.com/Latest-Energy-News/World-News/Economists-Cut-Indias-GDP-Growth-Forecast-on-Oil-Price-Shock.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 5.58] dyn_infy ↑
- dyn_infy [EQUITIES]: last 12.21, z20 3.58, zc 1.51, resid-z 1.60 [unexplained], 1d 4.36%, |z20|=3.58
- **Mechanism**: dyn_infy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.584 via dyn_infy, leads 1d, z 2.32, reacted); dyn_techm_ns (rho 0.566 via dyn_infy, leads 1d, z 2.14, reacted); dyn_tataelxsi_ns (rho 0.386 via dyn_infy, z -0.21, quiet)
- **India receivers**: nifty_it (rho 0.584, z 2.32); dyn_techm_ns (rho 0.566, z 2.14); dyn_tataelxsi_ns (rho 0.386, z -0.21)
- Source: TCS, Infosys, Coforge, other IT stocks rally up to 10% after Nvidia-led chip rout. Is AI trade ending? — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/news/tcs-infosys-coforge-other-it-stocks-rally-up-to-10-after-nvidia-led-chip-rout-is-ai-trade-ending/articleshow/132675510.cms
- Source: Coforge, Infosys to TCS: IT stocks rally as US software stocks outperform SOX last night; Nifty IT index jumps around 3% — Mint Markets, 2026-07-28. https://www.livemint.com/market/stock-market-news/coforge-infosys-to-tcs-it-stocks-rally-as-us-software-stocks-outperform-sox-last-night-nifty-it-index-jumps-around-3-11785209354512.html
- Source: Infosys Share Price Live Updates: Sensex trades flat, Nifty near 24,000 ahead of US Fed meet; IT pack shines — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/infosys-stock-price-livestock-price-today-live-updates-28-jul-2026/liveblog/132673920.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-20 (d=0.01), 2024-10-15 (d=0.02)

### [RED 5.42] dyn_eternal_ns ↑
- dyn_eternal_ns [EQUITIES]: last 307.50, z20 3.42, zc 1.92, resid-z 2.59 [unexplained], 1d 3.94%, |z20|=3.42
- **Mechanism**: dyn_eternal_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.6 via dyn_eternal_ns, z 0.13, quiet); dyn_jiofin_bo (rho 0.517 via dyn_eternal_ns, z -0.19, quiet); nifty_50 (rho 0.497 via dyn_eternal_ns, z -0.64, quiet); dyn_havells_ns (rho 0.456 via dyn_eternal_ns, z 1.65, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.6 vs dyn_eternal_ns, historically leads by 4d
- Watch next: dyn_jiofin_bo (co-move) — not yet - watch; rho 0.517 vs dyn_eternal_ns, historically leads by 3d
- **India receivers**: nifty_midcap_100 (rho 0.6, z 0.13); dyn_jiofin_bo (rho 0.517, z -0.19); nifty_50 (rho 0.497, z -0.64); dyn_havells_ns (rho 0.456, z 1.65)
- Source: Market wrap: TCS, Eternal, HUL, BEL among top gainers and losers on Nifty and Sensex on Tuesday — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-tcs-eternal-hul-bel-among-top-gainers-and-losers-on-nifty-and-sensex-on-tuesday/articleshow/132684231.cms
- Source: Eternal among 4 stocks flashing bullish signals, hinting at a possible uptrend — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/news/eternal-among-4-stocks-flashing-bullish-signals-hinting-at-a-possible-uptrend/slideshow/132674117.cms
- Source: Market wrap: Eternal, HDFC Bank, Infosys among top gainers and losers on Nifty and Sensex on Monday — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-eternal-hdfc-bank-infosys-among-top-gainers-and-losers-on-nifty-and-sensex-on-monday/articleshow/132660092.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-28 (d=0.02), 2026-06-30 (d=0.04)

## Watchlist (below surfacing floor)
cross-asset · 2 series ↑ (5.16), dyn_cartrade_ns ↑ (4.67), nasdaq_100 ↓ (4.29), natgas ↓ (3.89), dyn_ohi ↑ (3.83), gold_silver_ratio ↑ (3.72), dyn_tech ↑ (3.72), asx_200 ↑ (3.62), dyn_bac ↑ (3.61), dyn_aapl ↑ (3.53), commodities · 2 series ↑ (3.41), dyn_301077_sz ↓ (3.27)

## India macro
- nifty_50: 23983.9492 (1d -0.05%, z20 -0.64, flag none)
- nifty_midcap_100: 62421.4492 (1d 0.22%, z20 0.13, flag none)
- usd_inr: 95.8420 (1d -0.75%, z20 -0.14, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6026 (1d 0.27%, z20 0.85, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 74.3 — "MORGAN STANLEY STAYS BULLISH ON AI Morgan Stanley says the AI supply chain still offers at"
- INOXINDIA.NS (INOX INDIA LIMITED) score 67.1 — "Economists Cut India’s GDP Growth Forecast on Oil Price Shock"
- BAC (Bank of America Corporation) score 61.4 — "MORGAN STANLEY STAYS BULLISH ON AI Morgan Stanley says the AI supply chain still offers at"
- HDB (HDFC Bank Limited) score 60.6 — "MORGAN STANLEY STAYS BULLISH ON AI Morgan Stanley says the AI supply chain still offers at"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 58.6 — "MORGAN STANLEY STAYS BULLISH ON AI Morgan Stanley says the AI supply chain still offers at"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 57.0 — "Economists Cut India’s GDP Growth Forecast on Oil Price Shock"
- IDBI.NS (IDBI BANK LIMITED) score 56.5 — "MORGAN STANLEY STAYS BULLISH ON AI Morgan Stanley says the AI supply chain still offers at"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 53.6 — "MORGAN STANLEY STAYS BULLISH ON AI Morgan Stanley says the AI supply chain still offers at"
- TECHM.NS (TECH MAHINDRA LIMITED) score 53.4 — "MORGAN STANLEY STAYS BULLISH ON AI Morgan Stanley says the AI supply chain still offers at"
- COALINDIA.NS (COAL INDIA LTD) score 49.2 — "Economists Cut India’s GDP Growth Forecast on Oil Price Shock"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 48.7 — "MORGAN STANLEY STAYS BULLISH ON AI Morgan Stanley says the AI supply chain still offers at"
- COIN (Coinbase Global, Inc.) score 45.0 — "GLOBAL CHIP SELLOFF DEEPENS Chip stocks extended losses across Asia after a sharp U.S. sel"
- OHI (Omega Healthcare Investors, In) score 30.1 — "Nasdaq 100 heads for correction as AI worries rattle investors"
- LTH (Life Time Group Holdings, Inc.) score 24.1 — "Adani Energy Solution QIP to raise ₹3,500 cr oversubscribed three times"
- TECH (Bio-Techne Corp) score 24.0 — "MORGAN STANLEY STAYS BULLISH ON AI Morgan Stanley says the AI supply chain still offers at"
- CHKP (Check Point Software Technolog) score 22.6 — "Poojaa Precision Engg IPO Day 1: Issue subscribed 3.34x so far. GMP hints 86% listing gain"
- BOND (PIMCO Active Bond Exchange-Tra) score 21.8 — "India bonds pause rally as large debt supply, Fed decision loom"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.7 — "Adani Energy Solution QIP to raise ₹3,500 cr oversubscribed three times"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 17.7 — "Tata Power Targets 2032 for India's First Private Nuclear Plant"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 12.5 — "Coal India Q1 capex rises 16.6% YoY to  ₹3,399 crore, beats quarterly target"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 11.7 — "Adani Energy Solution QIP to raise ₹3,500 cr oversubscribed three times"
- INFY (Infosys Limited) score 11.0 — "Infosys Share Price Live Updates: Sensex trades flat, Nifty near 24,000 ahead of US Fed me"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.5 — "Why Did Trump Just Give Saudi Arabia the Fast Track to a Nuclear Weapon?"
- JIOFIN.BO (Jio Financial Services Limited) score 9.0 — "Coforge Q1 Results: Profit soars 63% to Rs 519 crore driven by Encora acquisition, AI-led "
- 301077.SZ (CHINASTARS) score 9.0 — "GLOBAL CHIP SELLOFF DEEPENS Chip stocks extended losses across Asia after a sharp U.S. sel"
- META (Meta) score 8.7 — "META - *META, BLACKROCK TO DEVELOP DATA CENTER CAMPUS IN EL PASO, TEXAS"
- MS (Morgan Stanley) score 8.3 — "MORGAN STANLEY STAYS BULLISH ON AI Morgan Stanley says the AI supply chain still offers at"
- VT (Vanguard Total World Stock Ind) score 7.1 — "TRUMP ON FED: WE SHOULD HAVE WORLD'S LOWEST INTEREST RATE"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 6.3 — "My financial adviser is against a withdrawal plan for my $2.3 million portfolio. Is he mak"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.0 — "Vedanta Aluminium shares in a sweet spot, says ICICI Securities; initiates coverage with B"
- GS (Goldman Sachs Group, Inc. (The) score 5.7 — "GOLDMAN WARNS MACRO RISKS RISING Goldman Sachs said rising oil volatility is shifting inve"
- ETERNAL.NS (ETERNAL LIMITED) score 5.2 — "Market wrap: TCS, Eternal, HUL, BEL among top gainers and losers on Nifty and Sensex on Tu"
- NVDA (NVIDIA Corporation) score 5.0 — "TCS, Infosys, Coforge, other IT stocks rally up to 10% after Nvidia-led chip rout. Is AI t"
- PCJEWELLER.NS (PC JEWELLER LTD) score 3.5 — "Keralam jewellers seek review of gold, silver import duty structure"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 3.3 — "India’s electricity shortages more than doubled during January-May 2026: IEA"
- 688188.SS (SHANGHAI BOCHU ELECTRONIC TECH) score 2.3 — "China's memory chipmaker CXMT shares soar in its blockbuster share listing in Shanghai"
- AAPL (Apple Inc.) score 1.4 — "FORD WILL USE APPLE SOFTWARE IN NEW SELF-DRIVING SYSTEM: NYT"
- NFLX (Netflix, Inc.) score 1.3 — "Losing Wall Street binge premium! Why are Netflix shares in a freefall this year?"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 0.4 — "Newly-listed SME stock DSM Fresh Foods jumps over 30% in 2 days after reporting a 58% YoY "
- CUPID.NS (CUPID LIMITED) score 0.1 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"

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