# Transmission Layer — board brief · 2026-07-31 17:15Z

data as of **2026-07-31** · 98 series · 12 red / 35 amber · 8 events surfaced (24 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.379, 2d in regime; vol-pct 0.405, breadth-off 0.353, Markov P(high-vol) 0.112)
- [INVERTED] **safe_haven_gold** — corr20 -0.48, corr60 -0.46, contra nifty_50 corr20=0.23, last shift 2026-06-08. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.91, corr60 0.82, last shift 2026-05-15. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.35, corr60 0.32, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.15, corr60 -0.05, last shift 2026-06-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.95, corr60 -0.84, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.1, corr60 -0.06, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.17, corr60 -0.24, last shift 2026-05-08. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.29, corr60 0.21, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **7 of 90** scanned series survive multiplicity control (effective p ≤ 0.006933947606081237)
- **SETUP** dyn_coin → asx_200: leads 1d (ccf 0.323, β 0.0516, p 0.0); driver zc -2.26 → expected -0.549%. Type hit-rate 0.814 (n=3251).
- **SETUP** btc_usd → asx_200: leads 1d (ccf 0.311, β 0.0865, p 0.0); driver zc -1.61 → expected -0.254%. Type hit-rate 0.814 (n=3251).
- **SETUP** btc_usd → aud_usd: leads 1d (ccf 0.284, β 0.061, p 0.0); driver zc -1.61 → expected -0.179%. Type hit-rate 0.814 (n=3251).
- **SETUP** dyn_coin → aud_usd: leads 1d (ccf 0.264, β 0.0328, p 0.00021); driver zc -2.26 → expected -0.348%. Type hit-rate 0.814 (n=3251).
- **SETUP** btc_usd → usd_mxn: leads 1d (ccf -0.254, β -0.0606, p 7e-05); driver zc -1.61 → expected 0.178%. Type hit-rate 0.814 (n=3251).
- Track record · residual_reversion: hit-rate **0.487** (n=1145) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.814** (n=3251) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.69] fx · 4 series ↑
- eur_usd [FX]: last 1.15, z20 4.03, zc 1.38, resid-z 1.75 [unexplained], 1d 0.51%, |z20|=4.03
- usd_mxn [FX]: last 17.32, z20 -2.36, zc -1.56, resid-z -1.46 [moved], 1d -0.67%, |z20|=2.36
- aud_usd [FX]: last 0.70, z20 2.29, zc 2.20, resid-z 2.23 [unexplained], 1d 1.05%, |z20|=2.29
- gbp_usd [FX]: last 1.35, z20 1.54, zc 1.77, resid-z 2.02 [unexplained], 1d 0.80%, |z20|=1.54
- **Mechanism**: The recent surge in Euro zone and US bond yields, driven by renewed inflation concerns in the Middle East, has led to a significant increase in FX volatility, with EUR/USD, AUD/USD, and GBP/USD experiencing unexplained moves. The transmission of these moves to the Indian market is likely to be through the EUR/INR currency pair, which has a correlation coefficient of 0.434 with GBP/USD.
- **Gap**: No gap: The large raw moves in EUR/USD, AUD/USD, and GBP/USD are accompanied by small resid_z values, indicating that these moves are largely priced in and not anomalous.
- **India take**: The Indian instrument that expresses this move is EUR/INR, which has not reacted yet to the recent FX moves. A potential reaction in EUR/INR could be a buying opportunity in the Indian market, particularly in export-oriented sectors.
- Watch next: eur_inr (up) — not yet - watch; EUR/INR has not reacted yet to the recent FX moves
- **India receivers**: eur_inr (rho 0.434, z 0.67)
- Source: Global Market: Euro zone, US bond yields log biggest monthly rise since March on Middle East inflation concerns — ET Markets, 2026-07-31. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-us-bond-yields-log-biggest-monthly-rise-since-march-on-middle-east-inflation-concerns/articleshow/132761537.cms
- Source: UK bond yields and sterling dip after BoE holds rates steady — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/bonds/uk-bond-yields-and-sterling-dip-after-boe-holds-rates-steady/articleshow/132740517.cms
- Source: Digital euro app to incorporate highest accessibility standards — ECB press, 2026-07-30. https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260730~3b3bfbb565.en.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 7.27] cross-asset · 2 series ↑
- usd_jpy [FX]: last 159.41, z20 -4.44, zc -7.53, resid-z -7.17 [unexplained], 1d -2.38%, |z20|=4.44
- dyn_amzn [EQUITIES]: last 270.05, z20 3.63, zc 6.56, resid-z 0.16 [priced], 1d 14.67%, |z20|=3.63; 1y-pct=96
- **Mechanism**: The surge in Amazon shares due to strong cloud revenue growth and easing concerns over AI investments has triggered a cross-asset move, with USD/JPY also experiencing an unexplained move. This move is likely driven by the transmission of positive sentiment from the US equity market to the FX market. However, the big raw move in USD/JPY with a small resid_z suggests that it is PRICED, not an anomaly.
- **Gap**: No gap: the move in USD/JPY is largely explained by its correlation with the US equity market, and the resid_z is small, indicating that the move is PRICED.
- **India take**: The Indian instrument dyn_thangamayl_ns has reacted to the move in dyn_amzn, while dyn_cartrade_ns remains quiet. The move in Amazon shares may have a positive impact on Indian metal equities via the metal_copper_channel.
- Watch next: dyn_amzn (up) — already moved; strong earnings report
- Watch next: usd_jpy (up) — already moved; transmission of positive sentiment from US equity market
- **India receivers**: dyn_thangamayl_ns (rho -0.357, z -3.89); dyn_cartrade_ns (rho -0.353, z -0.92)
- Source: Amazon shares surge 13% as cloud growth eases AI spending fears — ET Markets, 2026-07-31. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/amazon-shares-surge-13-as-cloud-growth-eases-ai-spending-fears/articleshow/132772194.cms
- Source: Wall Street surges as Amazon rallies on strong earnings, chip stocks jump on optimism about AI returns — Mint Markets, 2026-07-31. https://www.livemint.com/market/stock-market-news/wall-street-surges-as-amazon-and-chip-stocks-jump-11785505690872.html
- Source: Amazon shares surge 11% after earnings while Apple slipped 8% in the US markets — Mint Markets, 2026-07-31. https://www.livemint.com/market/stock-market-news/amazon-shares-surge-11-pc-after-earnings-apple-stock-down-8-pc-results-chips-ai-cloud-business-artificial-intelligence-11785505618161.html
- Historical analogues: 2024-10-16 (d=0.15), 2024-11-21 (d=0.23), 2026-03-31 (d=0.24)

### [RED 6.74] dyn_msft ↑
- dyn_msft [EQUITIES]: last 461.86, z20 4.74, zc 0.56, resid-z 0.08 [quiet], 1d 2.39%, |z20|=4.74
- **Mechanism**: The recent surge in Microsoft's stock price, driven by its strong earnings report and AI advancements, has led to a notable increase in investor confidence. This confidence boost is likely to propagate through the valid vix_equity_inverse channel, potentially leading to a decrease in volatility and an increase in equity prices. The metal_copper_channel may also play a role, as global copper prices often lead Indian metal equities.
- **Gap**: No gap: The move in Microsoft's stock price is largely priced, with a small resid_z of 0.08, indicating that the majority of the move can be explained by factor exposures.
- **India take**: The Indian instrument dyn_thangamayl_ns has already reacted, with a rho of -0.377 via dyn_msft, and a z20 of -3.89. This suggests that the Indian market has already begun to respond to the surge in Microsoft's stock price.
- Watch next: nifty_50 (up) — not yet - watch; Potential decrease in volatility and increase in equity prices
- **India receivers**: dyn_thangamayl_ns (rho -0.377, z -3.89)
- Source: Microsoft's AI Bet Pays Off: Key Takeaways From Its Blockbuster Quarter — ET Markets, 2026-07-31. https://economictimes.indiatimes.com/markets/us-stocks/news/microsofts-ai-bet-pays-off-key-takeaways-from-its-blockbuster-quarter/slideshow/132757561.cms
- Source: Micron, Sandisk and other chip stocks get major boosts in the wake of Microsoft’s earnings — MarketWatch Top, 2026-07-30. https://www.marketwatch.com/story/micron-sandisk-and-other-chip-stocks-get-major-boosts-in-the-wake-of-microsofts-earnings-25460e61?mod=mw_rss_topstories
- Source: Why Microsoft’s stock soared to a historic gain after earnings — MarketWatch Top, 2026-07-30. https://www.marketwatch.com/story/why-microsofts-stock-is-soaring-toward-a-historic-gain-after-earnings-96cd5b1e?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.02), 2025-10-20 (d=0.06)

### [RED 6.58] cross-asset · 2 series ↑
- dyn_jiofin_bo [EQUITIES]: last 256.05, z20 3.74, zc 1.76, resid-z 2.36 [unexplained], 1d 3.71%, |z20|=3.74
- nifty_midcap_100 [INDICES]: last 62873.15, z20 0.90, zc 0.40, resid-z 0.18 [quiet], 1d 0.33%, 1y-pct=98
- **Mechanism**: The recent surge in Jio Financial Services' stock price can be attributed to the announcement of a record date for determining eligible shareholders for the final dividend of FY26. This news has led to a significant increase in the stock's price, with a z20 level of 3.74, indicating a strong upward move. The resid_z of 2.36 suggests that a portion of this move is unexplained by factors, potentially indicating a speculative or sentiment-driven component.
- **Gap**: No gap: the big raw move in Jio Financial Services' stock price is largely priced in, given the significant z20 level and the fact that the stock has already reacted to the news.
- **India take**: The Indian instrument that expresses this move is the Nifty 50, which has already reacted with a z20 of 1.33. Other related instruments such as Nifty Metal and Bharat Coal have also reacted, while Indian Bank and IndusInd Bank remain quiet.
- Watch next: dyn_jiofin_bo (up) — already moved; record date announcement for dividend
- **India receivers**: nifty_50 (rho 0.817, z 1.33); dyn_indianb_ns (rho 0.634, z 0.56); dyn_indusindbk_bo (rho 0.625, z -0.06); nifty_metal (rho 0.618, z 1.62)
- Source: Jio Financial Services declares record date to finalise eligible shareholders for FY26 final dividend — Mint Markets, 2026-07-31. https://www.livemint.com/market/stock-market-news/jio-financial-services-declares-record-date-to-finalise-eligible-shareholders-for-fy26-final-dividend-11785505871823.html
- Historical analogues: 2025-07-15 (d=0.22), 2024-10-01 (d=0.26), 2025-05-30 (d=0.49)

### [RED 6.39] cross-asset · 2 series ↓
- dyn_coin [EQUITIES]: last 146.20, z20 -3.56, zc -2.26, resid-z -0.79 [moved], 1d -10.62%, |z20|=3.56; 1y-pct=2
- btc_usd [CRYPTO]: last 62826.41, z20 -1.61, zc -1.61, resid-z -1.38 [moved], 1d -2.93%, |z20|=1.61
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.09).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eth_usd (co-move) — not yet - watch; rho 0.772 vs dyn_coin
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.508 vs btc_usd
- Source: Global wheat output may drop 24 million tonnes next season on Iran war, El Nino impacts — BusinessLine Mkts, 2026-07-31. https://www.thehindubusinessline.com/economy/agri-business/global-wheat-output-may-drop-24-million-tonnes-next-season-on-iran-war-el-nino-impacts/article71290391.ece
- Source: Bloomberg again defers decision on including Indian government bonds in Global Aggregate Index — Mint Markets, 2026-07-31. https://www.livemint.com/market/bonds/bloomberg-again-defers-decision-on-including-indian-government-bonds-in-global-aggregate-index-11785502421270.html
- Source: Global Coal Consumption Hits Record Even as Coal Power Declines — OilPrice, 2026-07-31. https://oilprice.com/Energy/Coal/Global-Coal-Consumption-Hits-Record-Even-as-Coal-Power-Declines.html
- Historical analogues: 2026-05-22 (d=0.09), 2026-04-02 (d=0.17), 2025-10-22 (d=0.31)

### [RED 6.17] cross-asset · 6 series ↑
- cac_40 [INDICES]: last 8516.90, z20 2.02, zc 0.41, resid-z 0.45 [quiet], 1d 0.37%, |z20|=2.02; 1y-pct=98
- comex_copper [COMMODITIES]: last 6.47, z20 1.76, zc 0.14, resid-z -0.27 [quiet], 1d 0.33%, |z20|=1.76; 1y-pct=95; co-occur[metal_copper] same-direction (channel VALID)
- ftse_100 [INDICES]: last 10876.26, z20 1.72, zc -0.33, resid-z -0.16 [quiet], 1d -0.19%, |z20|=1.72; 1y-pct=98
- dax [INDICES]: last 25631.25, z20 1.42, zc 0.09, resid-z -0.10 [quiet], 1d 0.08%, 1y-pct=99
- stoxx_50 [INDICES]: last 6354.63, z20 1.32, zc 0.15, resid-z -0.03 [quiet], 1d 0.16%, 1y-pct=98
- dow_jones [INDICES]: last 52467.57, z20 0.25, zc 0.44, resid-z 0.52 [quiet], 1d 0.50%, 1y-pct=96
- **Mechanism**: cross-asset · 6 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-11-07 (z-distance 0.82).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.55 via cac_40, z 1.33, reacted); nifty_midcap_100 (rho 0.528 via dax, z 0.9, quiet)
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.807 vs comex_copper
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.588 vs comex_copper, historically leads by 1d
- Watch next: vix (inverse) — not yet - watch; rho -0.556 vs comex_copper, historically leads by 3d
- Watch next: wti (inverse) — not yet - watch; rho -0.537 vs cac_40, historically leads by 5d
- Watch next: brent (inverse) — not yet - watch; rho -0.523 vs cac_40, historically leads by 5d
- **India receivers**: nifty_50 (rho 0.55, z 1.33); nifty_midcap_100 (rho 0.528, z 0.9)
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks seesaw as bond yields rise and AI spending surges — ET Markets, 2026-07-31. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-hormuz-deal-crude-oil-fed-warsh-earnings-forecast-amazon-apple-nvidia-amd-meta-chip-stock-price-news-31st-july-2026/liveblog/132767346.cms
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: Nasdaq jumps over 2% as semiconductor stocks recover from rout — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-hormuz-deal-brent-crude-oil-fed-warsh-rate-earnings-forecast-microsoft-amd-apple-amazon-meta-chip-stock-price-news-30th-july-2026/liveblog/132739714.cms
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US market ends sharply higher as Microsoft rally fuels strong gain — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-hormuz-deal-brent-crude-oil-fed-warsh-rate-earnings-forecast-microsoft-amd-apple-amazon-meta-chip-stock-price-news-30th-july-2026/liveblog/132739714.cms
- Historical analogues: 2024-11-07 (d=0.82), 2024-10-11 (d=0.99), 2024-10-04 (d=1.03)

### [AMBER 5.91] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.20, z20 1.98, zc 3.20, resid-z 2.97 [unexplained], 1d 2.16%, |z20|=1.98; 1y-pct=100
- dyn_bond [EQUITIES]: last 90.40, z20 -1.93, zc -1.48, resid-z -0.31 [quiet], 1d -0.42%, 1y-pct=0
- ust_10y [RATES]: last 4.67, z20 1.32, zc 1.37, resid-z 1.42 [quiet], 1d 1.30%, 1y-pct=98
- tips_10y_real [RATES]: last 2.41, z20 1.17, zc 0.00, resid-z -0.30 [quiet], 1d 0.00%, 1y-pct=98
- ust_2y [RATES]: last 4.22, z20 0.06, zc -0.73, resid-z -0.50 [quiet], 1d -0.94%, 1y-pct=96
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: wti (co-move) — not yet - watch; rho 0.519 vs ust_30y, historically leads by 3d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.605 vs ust_30y
- Watch next: brent (co-move) — not yet - watch; rho 0.533 vs ust_30y
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.531 vs dyn_bond
- Watch next: sp500 (inverse) — not yet - watch; rho -0.523 vs ust_10y
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks seesaw as bond yields rise and AI spending surges — ET Markets, 2026-07-31. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-hormuz-deal-crude-oil-fed-warsh-earnings-forecast-amazon-apple-nvidia-amd-meta-chip-stock-price-news-31st-july-2026/liveblog/132767346.cms
- Source: India bonds log first monthly loss in four as surging oil, Treasury yields sting — ET Markets, 2026-07-31. https://economictimes.indiatimes.com/markets/bonds/india-bonds-log-first-monthly-loss-in-four-as-surging-oil-treasury-yields-sting/articleshow/132767310.cms
- Source: State Bank of India's perpetual bond demand seen spurring more issuances, bankers say — ET Markets, 2026-07-31. https://economictimes.indiatimes.com/markets/bonds/state-bank-of-indias-perpetual-bond-demand-seen-spurring-more-issuances-bankers-say/articleshow/132767274.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.89] dyn_thangamayl_ns ↓
- dyn_thangamayl_ns [EQUITIES]: last 5226.50, z20 -3.89, zc -1.06, resid-z -2.21 [unexplained], 1d -10.00%, |z20|=3.89
- **Mechanism**: dyn_thangamayl_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho -0.368 via dyn_thangamayl_ns, z 3.74, reacted)
- **India receivers**: dyn_jiofin_bo (rho -0.368, z 3.74)
- Source: KGSMA seek BIS probe into counterfeit hallmarked gold jewellery in Kerala — BusinessLine Mkts, 2026-07-31. https://www.thehindubusinessline.com/markets/gold/kgsma-seek-bis-probe-into-counterfeit-hallmarked-gold-jewellery-in-kerala/article71291226.ece
- Source: Thangamayil Jewellery shares crash 19% in 2 days on weak Q2 outlook. What did the company say? — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/stocks/news/thangamayil-jewellery-shares-crash-19-in-2-days-on-weak-q2-outlook-what-did-the-company-say/articleshow/132728014.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-29 (d=0.01), 2026-06-11 (d=0.01)

## Watchlist (below surfacing floor)
gold_silver_ratio ↑ (4.38), dyn_aapl ↓ (4.35), dyn_meta ↓ (4.12), dyn_lth ↑ (3.94), dyn_cupid_ns ↑ (3.68), dyn_tech ↑ (3.47), dyn_bac ↑ (3.24), usd_cny ↓ (3.23), ust_2s10s ↑ (3.09), dyn_icicigi_bo ↓ (3.02), dyn_301077_sz ↓ (2.79), dxy ↓ (2.74)

## India macro
- nifty_50: 24366.6992 (1d 0.20%, z20 1.33, flag none)
- nifty_midcap_100: 62873.1484 (1d 0.33%, z20 0.90, flag amber)
- usd_inr: 95.3700 (1d -0.37%, z20 -1.31, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5803 (1d 0.12%, z20 -0.46, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 80.9 — "State Bank of India's perpetual bond demand seen spurring more issuances, bankers say"
- COALINDIA.NS (COAL INDIA LTD) score 76.6 — "State Bank of India's perpetual bond demand seen spurring more issuances, bankers say"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 75.9 — "State Bank of India's perpetual bond demand seen spurring more issuances, bankers say"
- INDIANB.NS (INDIAN BANK) score 73.7 — "State Bank of India's perpetual bond demand seen spurring more issuances, bankers say"
- COIN (Coinbase Global, Inc.) score 59.9 — "Bloomberg delays India bonds inclusion in global index as investors seek proof reforms wor"
- TECHM.NS (TECH MAHINDRA LIMITED) score 57.5 — "US stock market today: S&P 500, Nasdaq futures extend rally on strong tech earnings; Amazo"
- BAC (Bank of America Corporation) score 57.2 — "State Bank of India's perpetual bond demand seen spurring more issuances, bankers say"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 55.4 — "US stock market today: S&P 500, Nasdaq futures extend rally on strong tech earnings; Amazo"
- HDB (HDFC Bank Limited) score 54.9 — "State Bank of India's perpetual bond demand seen spurring more issuances, bankers say"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 52.9 — "State Bank of India's perpetual bond demand seen spurring more issuances, bankers say"
- OHI (Omega Healthcare Investors, In) score 52.1 — "KOREAN CHIP STOCKS STAGE RECORD REBOUND SK Hynix surged 30% and Samsung Electronics jumped"
- IDBI.NS (IDBI BANK LIMITED) score 51.9 — "State Bank of India's perpetual bond demand seen spurring more issuances, bankers say"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 48.0 — "State Bank of India's perpetual bond demand seen spurring more issuances, bankers say"
- TECH (Bio-Techne Corp) score 40.6 — "US stock market today: S&P 500, Nasdaq futures extend rally on strong tech earnings; Amazo"
- BOND (PIMCO Active Bond Exchange-Tra) score 30.2 — "State Bank of India's perpetual bond demand seen spurring more issuances, bankers say"
- CHKP (Check Point Software Technolog) score 29.4 — "Stocks to watch: Maruti Suzuki, IOC, Tata Steel among shares in focus today; check list he"
- LTH (Life Time Group Holdings, Inc.) score 29.0 — "Maruti Suzuki Q1 Results: Revenue rises 36% to Rs 52,456 crore on all-time high volumes"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 28.3 — "The Drone Attack That Exposed Egypt’s Energy Defenses"
- 301077.SZ (CHINASTARS) score 21.8 — "China's crude oil imports fell in the second quarter"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 19.2 — "Top Gainers & Losers on 31 July: Bajaj Finance, Hyundai Motor, GAIL, Tata Motors, Redingto"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 18.0 — "Adani Energy plans another share sale by early next fiscal year"
- MS (Morgan Stanley) score 16.8 — "MARKET MOVERS 🟢 UPGRADES $BAX: Citigroup upgraded to Neutral; PT raised to $28 from $17 $C"
- AAPL (Apple Inc.) score 13.5 — "US stocks: Nasdaq leads US market gains as Amazon rally offsets Apple decline"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 12.6 — "Global Coal Consumption Hits Record Even as Coal Power Declines"
- JIOFIN.BO (Jio Financial Services Limited) score 11.7 — "Jio Financial Services declares record date to finalise eligible shareholders for FY26 fin"
- MSFT (Microsoft Corporation) score 11.3 — "Microsoft's AI Bet Pays Off: Key Takeaways From Its Blockbuster Quarter"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.8 — "South Korea’s chip giants just logged their biggest rally ever. What it means for the glob"
- META (Meta) score 9.8 — "Global Market: China's factory activity contracts unexpectedly in July; metal, commodity s"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 9.8 — "Jio Financial Services declares record date to finalise eligible shareholders for FY26 fin"
- INFY (Infosys Limited) score 9.7 — "Kospi’s mammoth 17% surge spells caution for Indian IT stocks. Why TCS, Infosys, others ar"
- PCJEWELLER.NS (PC JEWELLER LTD) score 9.3 — "KGSMA seek BIS probe into counterfeit hallmarked gold jewellery in Kerala"
- GS (Goldman Sachs Group, Inc. (The) score 9.0 — "PRICE TARGET CUT $AAPL: Goldman Sachs PT cut to $360 from $370; JP Morgan PT cut to $340 f"
- AMZN (Amazon.com, Inc.) score 8.8 — "AMZN - PIPER RAISES AMAZON PT AFTER STRONG AWS QUARTER Piper Sandler raised its Amazon pri"
- VT (Vanguard Total World Stock Ind) score 8.0 — "Apple set to lose $500 billion in value: Can Nvidia reclaim the world’s most valuable comp"
- NVDA (NVIDIA Corporation) score 6.7 — "Apple set to lose $500 billion in value: Can Nvidia reclaim the world’s most valuable comp"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.4 — "Higher oil prices could push Fed to resume rate hikes later this year: ICICI Bank report"
- THANGAMAYL.NS (THANGAMAYIL JEWELLERY LTD) score 4.2 — "KGSMA seek BIS probe into counterfeit hallmarked gold jewellery in Kerala"
- ETERNAL.NS (ETERNAL LIMITED) score 4.1 — "Zepto IPO hurdle revives investor interest in Swiggy, Eternal; shares set for best month i"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 2.1 — "LT Foods shares jump 4% on strong Q1 results; stock outperforms market"
- CUPID.NS (CUPID LIMITED) score 1.4 — "Cupid increases investment by $5 million in GII’s Healthcare-focused platform"

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