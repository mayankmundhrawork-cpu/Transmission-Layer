# Transmission Layer — board brief · 2026-08-04 22:34Z

data as of **2026-08-04** · 98 series · 20 red / 30 amber · 8 events surfaced (22 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.321, 2d in regime; vol-pct 0.406, breadth-off 0.235, Markov P(high-vol) 0.185)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.42, contra nifty_50 corr20=0.1, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.93, corr60 0.82, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.35, corr60 0.33, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.18, corr60 -0.04, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.81, corr60 -0.81, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.08, corr60 -0.03, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.18, corr60 -0.25, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.26, corr60 0.2, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **5 of 90** scanned series survive multiplicity control (effective p ≤ 0.0010380708664139426)
- **SETUP** nasdaq_100 → dyn_453950_ks: leads 1d (ccf 0.643, β 0.8755, p 0.0); driver zc 1.96 → expected 2.891%. Type hit-rate 0.821 (n=2850).
- **SETUP** sp500 → dyn_453950_ks: leads 1d (ccf 0.593, β 1.0788, p 0.0); driver zc 1.78 → expected 1.918%. Type hit-rate 0.821 (n=2850).
- **SETUP** dyn_vt → dyn_453950_ks: leads 1d (ccf 0.592, β 1.1206, p 0.0); driver zc 1.69 → expected 1.984%. Type hit-rate 0.821 (n=2850).
- **SETUP** dyn_vt → aud_usd: leads 1d (ccf 0.565, β 0.3531, p 0.0); driver zc 1.69 → expected 0.625%. Type hit-rate 0.821 (n=2850).
- **SETUP** nasdaq_100 → taiwan_weighted: leads 1d (ccf 0.557, β 0.6391, p 0.0); driver zc 1.96 → expected 2.11%. Type hit-rate 0.821 (n=2850).
- **SETUP** dyn_vt → taiwan_weighted: leads 1d (ccf 0.541, β 0.8822, p 0.0); driver zc 1.69 → expected 1.562%. Type hit-rate 0.821 (n=2850).
- **SETUP** nasdaq_100 → nikkei_225: leads 1d (ccf 0.54, β 0.6141, p 0.0); driver zc 1.96 → expected 2.028%. Type hit-rate 0.821 (n=2850).
- **SETUP** sp500 → nikkei_225: leads 1d (ccf 0.537, β 0.825, p 0.0); driver zc 1.78 → expected 1.466%. Type hit-rate 0.821 (n=2850).
- **SETUP** dyn_vt → nikkei_225: leads 1d (ccf 0.535, β 0.8582, p 0.0); driver zc 1.69 → expected 1.519%. Type hit-rate 0.821 (n=2850).
- **SETUP** sp500 → taiwan_weighted: leads 1d (ccf 0.529, β 0.8374, p 0.0); driver zc 1.78 → expected 1.489%. Type hit-rate 0.821 (n=2850).
- **SETUP** dyn_vt → usd_brl: leads 1d (ccf -0.527, β -0.432, p 0.0); driver zc 1.69 → expected -0.765%. Type hit-rate 0.821 (n=2850).
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.484, β 0.2629, p 0.0); driver zc 1.58 → expected 0.393%. Type hit-rate 0.821 (n=2850).
- **SETUP** dyn_vt → usd_mxn: leads 1d (ccf -0.483, β -0.3139, p 0.0); driver zc 1.69 → expected -0.556%. Type hit-rate 0.821 (n=2850).
- **SETUP** dow_jones → dyn_453950_ks: leads 1d (ccf 0.475, β 0.9457, p 0.0); driver zc 1.67 → expected 1.622%. Type hit-rate 0.821 (n=2850).
- **SETUP** sp500 → aud_usd: leads 1d (ccf 0.469, β 0.2832, p 0.0); driver zc 1.78 → expected 0.503%. Type hit-rate 0.821 (n=2850).
- **SETUP** dow_jones → nikkei_225: leads 1d (ccf 0.467, β 0.7816, p 0.0); driver zc 1.67 → expected 1.341%. Type hit-rate 0.821 (n=2850).
- **SETUP** nasdaq_100 → aud_usd: leads 1d (ccf 0.452, β 0.2016, p 0.0); driver zc 1.96 → expected 0.666%. Type hit-rate 0.821 (n=2850).
- **SETUP** sp500 → usd_brl: leads 1d (ccf -0.451, β -0.3573, p 0.0); driver zc 1.78 → expected -0.635%. Type hit-rate 0.821 (n=2850).
- **SETUP** nasdaq_100 → usd_brl: leads 1d (ccf -0.434, β -0.2535, p 0.0); driver zc 1.96 → expected -0.837%. Type hit-rate 0.821 (n=2850).
- **SETUP** dow_jones → taiwan_weighted: leads 1d (ccf 0.429, β 0.7249, p 0.0); driver zc 1.67 → expected 1.243%. Type hit-rate 0.821 (n=2850).
- **SETUP** dow_jones → usd_brl: leads 1d (ccf -0.417, β -0.3607, p 0.0); driver zc 1.67 → expected -0.619%. Type hit-rate 0.821 (n=2850).
- **SETUP** nasdaq_100 → kospi: leads 1d (ccf 0.408, β 0.6698, p 0.0); driver zc 1.96 → expected 2.212%. Type hit-rate 0.821 (n=2850).
- **SETUP** dow_jones → aud_usd: leads 1d (ccf 0.4, β 0.2643, p 1e-05); driver zc 1.67 → expected 0.453%. Type hit-rate 0.821 (n=2850).
- **SETUP** nasdaq_100 → usd_mxn: leads 1d (ccf -0.397, β -0.1841, p 0.0); driver zc 1.96 → expected -0.608%. Type hit-rate 0.821 (n=2850).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.358, β -2.3256, p 0.01081); driver zc 1.69 → expected -4.117%. Type hit-rate 0.821 (n=2850).
- **SETUP** dyn_vt → gbp_usd: leads 1d (ccf 0.343, β 0.1548, p 0.0); driver zc 1.69 → expected 0.274%. Type hit-rate 0.821 (n=2850).
- **SETUP** dyn_vt → nifty_midcap_100: leads 1d (ccf 0.286, β 0.3523, p 0.0); driver zc 1.69 → expected 0.624%. Type hit-rate 0.821 (n=2850).
- **SETUP** ust_10y → eur_usd: leads 1d (ccf -0.28, β -0.1137, p 0.0); driver zc 1.58 → expected -0.17%. Type hit-rate 0.821 (n=2850).
- **SETUP** sp500 → nifty_midcap_100: leads 1d (ccf 0.262, β 0.3142, p 1e-05); driver zc 1.78 → expected 0.558%. Type hit-rate 0.821 (n=2850).
- **SETUP** dyn_vt → hang_seng: leads 1d (ccf 0.257, β 0.371, p 0.0); driver zc 1.69 → expected 0.657%. Type hit-rate 0.821 (n=2850).
- Track record · residual_reversion: hit-rate **0.495** (n=1144) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.821** (n=2850) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.36] cross-asset · 11 series ↑
- dow_jones [INDICES]: last 54090.66, z20 4.48, zc 1.67, resid-z 0.58 [priced], 1d 1.72%, |z20|=4.48; 1y-pct=100
- stoxx_50 [INDICES]: last 6489.45, z20 4.05, zc 1.02, resid-z -0.96 [quiet], 1d 0.98%, |z20|=4.05; 1y-pct=100
- sp500 [INDICES]: last 7735.60, z20 3.68, zc 1.78, resid-z 0.82 [priced], 1d 1.78%, |z20|=3.68; 1y-pct=100
- russell_2000 [INDICES]: last 3037.07, z20 3.65, zc 1.48, resid-z -0.38 [quiet], 1d 1.85%, |z20|=3.65; 1y-pct=100
- dyn_vt [EQUITIES]: last 160.40, z20 3.55, zc 1.69, resid-z -2.02 [unexplained], 1d 1.77%, |z20|=3.55; 1y-pct=100
- cac_40 [INDICES]: last 8659.35, z20 3.37, zc 0.63, resid-z -1.17 [quiet], 1d 0.53%, |z20|=3.37; 1y-pct=100
- dax [INDICES]: last 26221.66, z20 3.26, zc 1.02, resid-z -0.76 [quiet], 1d 0.85%, |z20|=3.26; 1y-pct=100
- comex_copper [COMMODITIES]: last 6.63, z20 2.83, zc 0.80, resid-z -0.93 [quiet], 1d 1.80%, |z20|=2.83; 1y-pct=99; co-occur[metal_copper] same-direction (channel VALID)
- comex_gold [COMMODITIES]: last 4132.70, z20 1.59, zc 1.75, resid-z -1.68 [unexplained], 1d 2.45%, |z20|=1.59
- ftse_100 [INDICES]: last 10890.11, z20 1.51, zc 0.53, resid-z -0.19 [quiet], 1d 0.30%, |z20|=1.51; 1y-pct=98
- gold_silver_ratio [DERIVED]: last 69.15, z20 -0.68, zc n/a, resid-z n/a [quiet], 1d -1.13%, GSR<75 (extreme low)
- **Mechanism**: The current move is driven by stellar earnings from AI-focused corporations, a drop in oil prices, and a favorable Treasury yield backdrop. This has led to a record high in US stocks, with the Dow and S&P 500 reaching new heights. The VALID vix_equity_inverse channel suggests that the current vol spike will lead to an equity drawdown, but the RISK_ON regime and VALID gold_silver_comove channel indicate a continued risk-on sentiment.
- **Gap**: No gap: The big raw move in US stocks is largely priced, with a small resid_z indicating that the move is mostly explained by factor exposures.
- **India take**: Indian instruments such as Nifty 50 and Nifty Midcap 100 have reacted to global cues, with a positive correlation to US and European markets. The Nifty Metal index has also reacted, driven by the VALID metal_copper_channel.
- Watch next: dow_jones (up) — already moved; Record high close
- Watch next: nifty_50 (up) — already moved; Reacted to global cues
- **India receivers**: nifty_50 (rho 0.528, z 2.07); nifty_midcap_100 (rho 0.519, z 1.75); nifty_metal (rho -0.432, z 3.69)
- Source: Musk: 'Not Out of the Question' That Starlink Would Deliver Majority of World Internet Within 10 Years — DeItaone, 2026-08-04. https://t.me/walter_bloomberg/34345
- Source: US stocks: Dow, S&P 500 close at record highs as AI earnings impress, oil prices tumble — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-dow-sp-500-close-at-record-highs-as-ai-earnings-impress-oil-prices-tumble/articleshow/132872181.cms
- Source: These charts suggest the S&P 500 is looking like a bargain. Take them with a grain of salt. — MarketWatch Top, 2026-08-04. https://www.marketwatch.com/story/these-charts-suggest-the-s-p-500-is-looking-like-a-bargain-take-them-with-a-grain-of-salt-f109548f?mod=mw_rss_topstories
- Historical analogues: 2024-10-09 (d=1.0), 2024-11-26 (d=1.05), 2025-10-31 (d=1.07)

### [RED 9.32] dyn_pltr ↑
- dyn_pltr [EQUITIES]: last 162.63, z20 7.32, zc 8.98, resid-z -0.24 [moved], 1d 29.43%, |z20|=7.32
- **Mechanism**: The surge in Palantir Technologies Inc.'s stock, driven by strong demand for its AI-powered data analytics platform, has triggered a risk-on sentiment in the market. This sentiment is propagating through the VALID vix_equity_inverse channel, where a vol spike is inversely related to equity drawdown. The metal_copper_channel is also a potential mechanism, given the global copper leads Indian metal equities.
- **Gap**: No gap: the big raw move in dyn_pltr is largely priced, with a small resid_z of -0.24, indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian instrument dyn_atherenerg_ns has already reacted to the move in dyn_pltr, given its rho of 0.403. Further reaction in Indian metal equities can be expected through the metal_copper_channel.
- Watch next: dyn_atherenerg_ns (up) — already moved; reacted to dyn_pltr
- **India receivers**: dyn_atherenerg_ns (rho 0.403, z 5.33)
- Source: Palantir Short Sellers Take $3 Billion Hit After 30% Stock Surge — Mint Markets, 2026-08-04. https://www.livemint.com/market/palantir-short-sellers-take-3-billion-hit-after-30-stock-surge-11785872351134.html
- Source: Palantir climbs 27% on 'otherworldly' AI demand; Karp tells shareholders business has 'Marxist' values — Mint Markets, 2026-08-04. https://www.livemint.com/market/stock-market-news/palantir-climbs-27-on-otherworldly-ai-demand-karp-tells-shareholders-business-has-marxist-values-11785861835803.html
- Source: Palantir stock jumps 27% after ‘otherworldly’ demand lifts outlook — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/palantir-stock-jumps-27-after-otherworldly-demand-lifts-outlook/articleshow/132866951.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-01 (d=0.08), 2025-10-13 (d=0.13)

### [RED 7.33] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1454.80, z20 5.33, zc 4.61, resid-z 5.06 [unexplained], 1d 14.31%, |z20|=5.33; 1y-pct=100
- **Mechanism**: The surge in Ather Energy's stock price is driven by the company's narrowing quarterly loss, which has ignited investor optimism about its future prospects. This move is propagated through the metal_copper_channel, where global copper leads Indian metal equities, and the vix_equity_inverse channel, which indicates a decrease in volatility. The RISK_ON regime also supports this move.
- **Gap**: No gap: the 14% jump in Ather Energy's stock price is largely priced in, given the significant narrowing of its quarterly loss and the resulting investor enthusiasm
- **India take**: The Indian instrument that expresses this move is the Nifty Auto index, which may react positively to Ather Energy's improved performance. However, the reaction is not yet visible, and the index is still watching the developments
- Watch next: nifty_50 (up) — not yet - watch; Ather Energy's stock surge may lead to a broader market rally
- Source: Ather Energy shares jump 14% after Q1 loss narrows — BusinessLine Mkts, 2026-08-04. https://www.thehindubusinessline.com/markets/ather-energy-shares-jump-18-to-fresh-52-week-high-after-q1-loss-narrows/article71303894.ece
- Source: Ather Energy's tapering losses put stock in fast lane, but is the rally justified? — Mint Markets, 2026-08-04. https://www.livemint.com/market/mark-to-market/ather-energy-electric-vehicles-ev-q1fy27-ebitda-operating-losses-ev-sales-hero-motocorp-11785824423599.html
- Source: Multibagger stock Ather Energy share price soars 18% to record high post Q1 FY27 results: Should you buy? — Mint Markets, 2026-08-04. https://www.livemint.com/market/stock-market-news/multibagger-stock-ather-energy-share-price-soars-18-to-record-high-post-q1-fy27-results-should-you-buy-11785824415092.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [AMBER 6.95] commodities · 2 series ↓
- brent [COMMODITIES]: last 78.86, z20 -1.12, zc -1.49, resid-z -0.79 [quiet], 1d -5.86%, 1-session move -5.86% ≥ 1.5%
- wti [COMMODITIES]: last 75.34, z20 -0.97, zc -1.84, resid-z -0.85 [moved], 1d -6.22%, 1-session move -6.22% ≥ 1.5%
- **Mechanism**: The recent drop in Brent and WTI crude oil prices can be attributed to the build-up of US crude oil inventories and the potential for a peaceful resolution in the Iran conflict, which has led to a decrease in oil prices. This move is largely priced, as indicated by the relatively small resid_z values for both Brent and WTI. The valid gold_silver_comove and metal_copper_channel suggest that the decline in oil prices may have a ripple effect on other commodities, but the weak inr_oil_channel and dxy_inr_channel imply that the impact on the Indian rupee may be limited.
- **Gap**: No gap: the move in oil prices is largely priced, with small resid_z values indicating that the decline is largely explained by factor exposures
- **India take**: The Indian instrument nifty_midcap_100 has already reacted to the move in WTI, while the midcap_largecap_ratio remains quiet. The metal_copper_channel may lead to a decline in Indian metal equities.
- Watch next: nifty_midcap_100 (down) — already moved; negative correlation with WTI
- **India receivers**: nifty_midcap_100 (rho -0.465, z 1.75); midcap_largecap_ratio (rho -0.427, z -0.68)
- Source: US Crude Oil Inventories Build As Washington Talks Up Potential Peace Deal — OilPrice, 2026-08-04. https://oilprice.com/Latest-Energy-News/World-News/US-Crude-Oil-Inventories-Build-As-Washington-Talks-Up-Potential-Peace-Deal.html
- Source: US stocks: Dow, S&P 500 close at record highs as AI earnings impress, oil prices tumble — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-dow-sp-500-close-at-record-highs-as-ai-earnings-impress-oil-prices-tumble/articleshow/132872181.cms
- Source: China's EV Boom Is Quietly Undermining Oil's Biggest Chokepoint — OilPrice, 2026-08-04. https://oilprice.com/Energy/Energy-General/Chinas-EV-Boom-Is-Quietly-Undermining-Oils-Biggest-Chokepoint.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 6.39] cross-asset · 3 series ↑
- dyn_jiofin_bo [EQUITIES]: last 264.55, z20 3.07, zc 0.43, resid-z 1.44 [quiet], 1d 0.97%, |z20|=3.07
- nifty_50 [INDICES]: last 24614.90, z20 2.07, zc -0.88, resid-z -1.10 [quiet], 1d -0.64%, |z20|=2.07
- nifty_midcap_100 [INDICES]: last 63484.05, z20 1.75, zc -0.36, resid-z 0.52 [quiet], 1d -0.29%, |z20|=1.75; 1y-pct=99
- **Mechanism**: The recent volatility in the Nifty 50, triggered by the new Closing Auction Session, has led to a surge in the index's value, with a sharp swing of nearly 150 points in the final minutes of trading. This move is largely priced, given the small resid_z values for the Nifty 50 and other correlated instruments. The metal_copper_channel and vix_equity_inverse channels are valid and may influence the propagation of this move.
- **Gap**: No gap: the move in Nifty 50 is largely priced, with a small resid_z value of -1.11, indicating that the factor exposures explain most of the move
- **India take**: The Indian instruments that express this move include the Nifty Midcap 100 and the Nifty Metal index, which have reacted to the volatility in the Nifty 50. The dyn_muthootfin_ns and dyn_bharatcoal_ns have also reacted, while the dyn_indianb_ns and dyn_indusindbk_bo remain quiet.
- Watch next: nifty_50 (down) — already moved; expiry-day volatility and new closing auction system
- **India receivers**: dyn_muthootfin_ns (rho 0.692, z -2.93); dyn_bharatcoal_ns (rho 0.631, z -1.19); dyn_indianb_ns (rho 0.62, z 0.71); dyn_indusindbk_bo (rho 0.614, z 0.24)
- Source: Closing auction: Nifty swings on Day 2 raise eyebrows — BusinessLine Mkts, 2026-08-04. https://www.thehindubusinessline.com/markets/stock-markets/closing-auction-under-scanner-after-second-day-of-sharp-nifty-swings/article71306295.ece
- Source: Traders on edge! Why Nifty jumped 150 points in final minutes again — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/stocks/news/traders-on-edge-why-nifty-jumped-150-points-in-final-minutes-again/articleshow/132862330.cms
- Source: Market wrap: RIL, Hindalco, Trent among top gainers and losers on Nifty and Sensex on Tuesday — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-ril-hindalco-trent-among-top-gainers-and-losers-on-nifty-and-sensex-on-tuesday/articleshow/132861901.cms
- Historical analogues: 2025-07-17 (d=0.69), 2024-11-07 (d=0.98), 2025-08-13 (d=1.26)

### [RED 6.21] cross-asset · 2 series ↑
- usd_jpy [FX]: last 157.73, z20 -3.37, zc 0.12, resid-z 0.30 [quiet], 1d 0.09%, |z20|=3.37
- dyn_amzn [EQUITIES]: last 277.43, z20 2.39, zc -0.22, resid-z 9.76 [unexplained], 1d -2.32%, |z20|=2.39; 1y-pct=99
- **Mechanism**: The recent surge in Amazon's market value, driven by strong earnings and increased investor confidence in artificial intelligence, has led to a significant move in dyn_amzn. This move, with a high resid_z of 9.76, indicates an unexplained component that is not priced in by factor exposures. The correlated instruments, such as taiwan_weighted, gbp_usd, and kospi, have not moved yet, suggesting a potential transmission setup. The verified transmission setup of ust_10y -> usd_jpy, with a lead of 1d, may also contribute to the propagation of this move.
- **Gap**: No gap: the big raw move in dyn_amzn is accompanied by a small resid_z in usd_jpy, indicating that the move is largely priced in by factor exposures
- **India take**: The Indian instrument dyn_muthootfin_ns, which is correlated with usd_jpy, has already reacted with a z20 of -2.93. Another Indian instrument, dyn_cartrade_ns, which is correlated with dyn_amzn, remains quiet with a z20 of 0.18.
- Watch next: taiwan_weighted (down) — not yet - watch; historically leads by 1d and correlated with usd_jpy
- **India receivers**: dyn_muthootfin_ns (rho -0.512, z -2.93); dyn_cartrade_ns (rho -0.36, z 0.18)
- Source: Yen holds most gains as intervention keeps speculators on edge — Mint Markets, 2026-08-04. https://www.livemint.com/market/yen-holds-most-gains-as-intervention-keeps-speculators-on-edge-11785874259298.html
- Source: BOFA: TARGET FX VOLATILITY, NOT THE WHOLE MARKET Bank of America says investors should focus on specific currency pairs—not broad FX volatility—if the Fed resumes rate hikes. The bank highlights Japanese yen and British pound pairs as the strongest opportunities. Historically, — DeItaone, 2026-08-04. https://t.me/walter_bloomberg/34270
- Source: What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/us-markets-academy/what-bubble-amazon-enters-3-trillion-market-cap-club-ceo-highlights-striking-ai-demand/articleshow/132854970.cms
- Historical analogues: 2024-10-16 (d=0.15), 2024-11-21 (d=0.23), 2026-03-31 (d=0.24)

### [RED 6.09] fx · 3 series ↑
- usd_mxn [FX]: last 17.25, z20 -2.77, zc -0.68, resid-z -0.43 [quiet], 1d -0.30%, |z20|=2.77
- eur_usd [FX]: last 1.15, z20 2.43, zc -0.19, resid-z -0.38 [quiet], 1d -0.07%, |z20|=2.43
- aud_usd [FX]: last 0.70, z20 2.24, zc 0.07, resid-z 0.05 [quiet], 1d 0.05%, |z20|=2.24
- **Mechanism**: The recent decline in oil prices has led to a decrease in inflation concerns, prompting markets to pare expectations for further ECB rate hikes. This has resulted in a decline in Euro zone government bond yields, which in turn has caused a strengthening of the Euro against the US Dollar. This move is priced, with small resid_z values indicating that the factor exposures can explain the majority of the move.
- **Gap**: No gap: the move in eur_usd is largely explained by the decline in oil prices and the subsequent decrease in inflation concerns, with a small resid_z value indicating that the move is priced.
- **India take**: The Indian instrument dyn_muthootfin_ns has reacted to the move in usd_mxn, with a correlation coefficient of -0.516. The move in usd_mxn has been largely priced, with a small resid_z value, indicating that the Indian market has already reacted to the decline in oil prices and the subsequent decrease in inflation concerns.
- Watch next: eur_usd (up) — already moved; Euro zone bond yields decline
- **India receivers**: dyn_muthootfin_ns (rho -0.516, z -2.93)
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

## Watchlist (below surfacing floor)
dyn_msft ↑ (5.15), dyn_thangamayl_ns ↓ (5.12), dyn_muthootfin_ns ↓ (4.93), dyn_infy ↑ (4.19), nifty_metal ↑ (3.69), dyn_bac ↑ (3.67), dyn_coin ↓ (3.55), asx_200 ↑ (3.45), dyn_lth ↑ (3.38), dyn_tech ↑ (3.17), usd_cny ↓ (2.7), dyn_havells_ns ↑ (2.66)

## India macro
- nifty_50: 24614.9004 (1d -0.64%, z20 2.07, flag amber)
- nifty_midcap_100: 63484.0508 (1d -0.29%, z20 1.75, flag amber)
- usd_inr: 95.3680 (1d -0.04%, z20 -1.41, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5791 (1d 0.36%, z20 -0.68, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI MPC decision T-3d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 71.8 — "Worst of FPI equity selling may be over for India: Report"
- COALINDIA.NS (COAL INDIA LTD) score 70.2 — "Worst of FPI equity selling may be over for India: Report"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 69.2 — "Worst of FPI equity selling may be over for India: Report"
- INDIANB.NS (INDIAN BANK) score 57.7 — "MARKET MOVERS 🟢 UPGRADES $PLTR: Deutsche Bank upgraded to Buy $REPL: Leerink Partners upgr"
- COIN (Coinbase Global, Inc.) score 48.0 — "Apollo Global debt deal fees and insurance earnings rise, asset sales drag"
- BAC (Bank of America Corporation) score 42.6 — "Fishlike Nanorobots Could Become America’s Answer to China’s Lithium Grip"
- TECHM.NS (TECH MAHINDRA LIMITED) score 41.8 — "IRAN'S FOREIGN MINISTER SPOKESPERSON SAYS TALKS WITH OMAN ASSESSED AS 'POSITIVE' AT BOTH T"
- HDB (HDFC Bank Limited) score 40.8 — "MARKET MOVERS 🟢 UPGRADES $PLTR: Deutsche Bank upgraded to Buy $REPL: Leerink Partners upgr"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 40.3 — "IRAN'S FOREIGN MINISTER SPOKESPERSON SAYS TALKS WITH OMAN ASSESSED AS 'POSITIVE' AT BOTH T"
- IDBI.NS (IDBI BANK LIMITED) score 39.2 — "MARKET MOVERS 🟢 UPGRADES $PLTR: Deutsche Bank upgraded to Buy $REPL: Leerink Partners upgr"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 39.2 — "MARKET MOVERS 🟢 UPGRADES $PLTR: Deutsche Bank upgraded to Buy $REPL: Leerink Partners upgr"
- OHI (Omega Healthcare Investors, In) score 38.8 — "CIO WARNS AI RALLY RELIES ON INVESTOR FAITH Hirtle CIO Brad Conger warns the AI trade is e"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 37.3 — "MARKET MOVERS 🟢 UPGRADES $PLTR: Deutsche Bank upgraded to Buy $REPL: Leerink Partners upgr"
- TECH (Bio-Techne Corp) score 34.7 — "IRAN'S FOREIGN MINISTER SPOKESPERSON SAYS TALKS WITH OMAN ASSESSED AS 'POSITIVE' AT BOTH T"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 32.1 — "Ather Energy shares jump 14% after Q1 loss narrows"
- CHKP (Check Point Software Technolog) score 28.3 — "Dhaval Packaging IPO allotment to be finalised today. Here's GMP, how to check status onli"
- LTH (Life Time Group Holdings, Inc.) score 26.2 — "FED'S PAULSON: THIS IS A COMPLICATED TIME FOR MONETARY POLICY - CNBC PAULSON: INFLATION IS"
- BOND (PIMCO Active Bond Exchange-Tra) score 21.1 — "India bonds rise on position building ahead of RBI policy"
- 301077.SZ (CHINASTARS) score 20.4 — "China's EV Boom Is Quietly Undermining Oil's Biggest Chokepoint"
- MS (Morgan Stanley) score 12.9 — "LIFE: Deutsche Bank PT raised to $40 from $30; Barclays PT raised to $37 from $27 $LIND: B"
- JUSTDIAL.BO (JUST DIAL LTD.) score 12.3 — "S&P 500 BREAKS OUT, RECORD HIGH IN SIGHT The S&P 500 has regained momentum, closing just 0"
- AMZN (Amazon.com, Inc.) score 10.4 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- JIOFIN.BO (Jio Financial Services Limited) score 9.9 — "Jio Financial Services Share Price Live Updates: Jio Financial Services sees a slight dip "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.6 — "Tata Steel Share Price Live Updates: Tata Steel's Price Movement Today"
- VT (Vanguard Total World Stock Ind) score 9.2 — "Musk: 'Not Out of the Question' That Starlink Would Deliver Majority of World Internet Wit"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.2 — "Adani Ent Share Price Live Updates: Adani Ent. News"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 9.2 — "Jio Financial Services Share Price Live Updates: Jio Financial Services sees a slight dip "
- PCJEWELLER.NS (PC JEWELLER LTD) score 8.7 — "Kalyan Jewellers Q1 Results: Net profit jumps 32% YoY to  ₹349 crore; margins contract"
- PLTR (Palantir Technologies Inc.) score 8.1 — "Palantir Short Sellers Take $3 Billion Hit After 30% Stock Surge"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 7.8 — "Coal India Share Price Live Updates: Coal India  Market Performance"
- MSFT (Microsoft Corporation) score 7.3 — "SHARES OF US HYPERSCALERS CLIMB • META RISES 6.1% • MICROSOFT JUMPS 4.7% • AMAZON GAINS 4."
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.1 — "Maharatna PSU stock Power Finance Corporation to declare Q1 results 2026, interim dividend"
- AAPL (Apple Inc.) score 6.6 — "Apple suffers worst rout since 2025 on disappointing outlook"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.0 — "ICICI Securities initiates coverage on 7 PSU banks with positive valuations"
- NVDA (NVIDIA Corporation) score 5.9 — "NVDA - SPACEX CEO ELON MUSK SAYS GOING FORWARD, WE'VE DECIDED TO BUILD EXCLUSIVELY ON NVID"
- GS (Goldman Sachs Group, Inc. (The) score 5.4 — "Global Market: Goldman Sachs sees Brent crude trading at $80-$90 until Iran conflict outlo"
- META (Meta) score 5.3 — "META INVITED TO WHITE HOUSE TUESDAY TO DISCUSS AI SAFETY TESTING BY U.S. GOVERNMENT - COMP"
- INFY (Infosys Limited) score 4.5 — "Infosys Share Price Live Updates: Infosys market movement today"
- THANGAMAYL.NS (THANGAMAYIL JEWELLERY LTD) score 3.2 — "Thangamayil share selloff continues: Stock drops 5% despite Rs 344 crore sales in first 3 "
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