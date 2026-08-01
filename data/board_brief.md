# Transmission Layer — board brief · 2026-08-01 06:49Z

data as of **2026-08-01** · 98 series · 12 red / 36 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.355, 2d in regime; vol-pct 0.357, breadth-off 0.353, Markov P(high-vol) 0.123)
- [INVERTED] **safe_haven_gold** — corr20 -0.47, corr60 -0.45, contra nifty_50 corr20=0.23, last shift 2026-06-09. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.82, last shift 2026-05-18. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.35, corr60 0.32, last shift 2026-05-15. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.15, corr60 -0.06, last shift 2026-06-05. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.84, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.05, corr60 -0.04, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.13, corr60 -0.24, last shift 2026-05-11. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.26, corr60 0.2, last shift 2026-04-17. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **5 of 90** scanned series survive multiplicity control (effective p ≤ 0.00244553738718456)
- **SETUP** dyn_coin → asx_200: leads 1d (ccf 0.32, β 0.0508, p 0.0); driver zc -2.26 → expected -0.539%. Type hit-rate 0.819 (n=3196).
- **SETUP** dyn_coin → aud_usd: leads 1d (ccf 0.262, β 0.0325, p 0.00024); driver zc -2.26 → expected -0.345%. Type hit-rate 0.819 (n=3196).
- Track record · residual_reversion: hit-rate **0.488** (n=1141) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.819** (n=3196) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.02] cross-asset · 2 series ↑
- usd_jpy [FX]: last 157.40, z20 -7.19, zc -11.76, resid-z -10.81 [unexplained], 1d -3.61%, |z20|=7.19
- dyn_amzn [EQUITIES]: last 271.61, z20 3.84, zc 6.70, resid-z 1.43 [moved], 1d 15.33%, |z20|=3.84; 1y-pct=97
- **Mechanism**: The move in Amazon shares, driven by strong cloud revenue growth, has propagated to the broader market through the tech sector, while the yen's intervention-driven rally has stalled, leading to a potential reversion in USD/JPY. The valid vix_equity_inverse channel suggests that the vol spike may lead to an equity drawdown, but the current move in Amazon and the overall market seems to be driven by fundamentals rather than risk-off sentiment.
- **Gap**: No gap: the big raw move in usd_jpy has a small resid_z, indicating it is largely priced in, while dyn_amzn's move is also largely explained by its fundamentals
- **India take**: The Indian transmission candidates, such as dyn_thangamayl_ns and dyn_cartrade_ns, have reacted or are quiet, respectively, suggesting that the move in Amazon has been partially transmitted to the Indian market, but the reaction is not uniform across all related stocks.
- Watch next: dyn_amzn (up) — already moved; strong cloud revenue growth
- Watch next: usd_jpy (down) — not yet - watch; yen's intervention-driven rally has stalled
- **India receivers**: dyn_thangamayl_ns (rho -0.365, z -3.89); dyn_cartrade_ns (rho -0.362, z -0.92)
- Source: Amazon soars as cloud revenue surge allays fears over ballooning AI bets — ET Markets, 2026-08-01. https://economictimes.indiatimes.com/markets/us-stocks/news/amazon-soars-as-cloud-revenue-surge-allays-fears-over-ballooning-ai-bets/articleshow/132780762.cms
- Source: Yen’s Intervention Rally Stalls as Traders Brace for More Action — Mint Markets, 2026-07-31. https://www.livemint.com/market/yens-intervention-rally-stalls-as-traders-brace-for-more-action-11785536147224.html
- Source: US stocks: US market ends higher as Amazon soothes AI jitters — ET Markets, 2026-07-31. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-us-market-ends-higher-as-amazon-soothes-ai-jitters/articleshow/132776618.cms
- Historical analogues: 2024-10-16 (d=0.15), 2024-11-21 (d=0.23), 2026-03-31 (d=0.24)

### [RED 7.74] fx · 4 series ↑
- eur_usd [FX]: last 1.15, z20 4.08, zc 1.40, resid-z 1.73 [unexplained], 1d 0.52%, |z20|=4.08
- usd_mxn [FX]: last 17.33, z20 -2.31, zc -1.52, resid-z -1.55 [unexplained], 1d -0.65%, |z20|=2.31
- aud_usd [FX]: last 0.70, z20 2.05, zc 2.00, resid-z 2.19 [unexplained], 1d 0.95%, |z20|=2.05
- gbp_usd [FX]: last 1.35, z20 1.75, zc 1.98, resid-z 2.26 [unexplained], 1d 0.89%, |z20|=1.75
- **Mechanism**: The recent surge in Euro zone and US bond yields, driven by renewed inflation concerns in the Middle East, has led to a rise in interest rate cut expectations, causing a big raw move in FX markets with small resid_z, indicating that the move is largely priced in. The Valid channels, such as gold_silver_comove and metal_copper_channel, are not directly related to the current FX move, but the Verified transmission setups, like btc_usd -> aud_usd and dyn_coin -> aud_usd, suggest potential follow-through effects.
- **Gap**: No gap: the big raw move in FX markets has small resid_z, indicating that the move is largely priced in
- **India take**: The Indian instrument eur_inr has reacted to the FX move, with a rho of 0.44 via gbp_usd, and a z20 of 1.01, indicating that the Indian market has already factored in the global FX trends. The metal_copper_channel, a Valid channel, may also influence Indian metal equities.
- Watch next: eur_usd (up) — already moved; reacted to Euro zone bond yields rise
- Watch next: usd_mxn (down) — already moved; reacted to US bond yields rise
- Watch next: aud_usd (up) — already moved; reacted to global risk sentiment
- Watch next: gbp_usd (up) — already moved; reacted to BoE holding rates steady
- **India receivers**: eur_inr (rho 0.44, z 1.01); nifty_metal (rho 0.375, z 1.62)
- Source: Global Market: Euro zone, US bond yields log biggest monthly rise since March on Middle East inflation concerns — ET Markets, 2026-07-31. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-us-bond-yields-log-biggest-monthly-rise-since-march-on-middle-east-inflation-concerns/articleshow/132761537.cms
- Source: UK bond yields and sterling dip after BoE holds rates steady — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/bonds/uk-bond-yields-and-sterling-dip-after-boe-holds-rates-steady/articleshow/132740517.cms
- Source: Digital euro app to incorporate highest accessibility standards — ECB press, 2026-07-30. https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260730~3b3bfbb565.en.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 6.95] dyn_msft ↑
- dyn_msft [EQUITIES]: last 464.92, z20 4.95, zc 0.71, resid-z 6.76 [unexplained], 1d 3.06%, |z20|=4.95
- **Mechanism**: The surge in Microsoft's stock price is driven by its strong earnings report, which exceeded expectations and demonstrated the success of its AI investments. This move is likely to propagate through the valid vix_equity_inverse channel, as the vol spike is likely to lead to an equity drawdown. However, the current regime is neutral, which may limit the impact of this move.
- **Gap**: No gap: the big raw move in Microsoft's stock price is largely explained by its strong earnings report, with a resid_z of 6.76, indicating that the move is mostly priced in.
- **India take**: The Indian instrument dyn_thangamayl_ns has already reacted to the move in Microsoft's stock price, with a negative correlation of -0.387. This suggests that the Indian market has already factored in the implications of Microsoft's earnings report.
- Watch next: dyn_msft (up) — already moved; strong earnings report
- **India receivers**: dyn_thangamayl_ns (rho -0.386, z -3.89)
- Source: Microsoft's AI Bet Pays Off: Key Takeaways From Its Blockbuster Quarter — ET Markets, 2026-07-31. https://economictimes.indiatimes.com/markets/us-stocks/news/microsofts-ai-bet-pays-off-key-takeaways-from-its-blockbuster-quarter/slideshow/132757561.cms
- Source: Micron, Sandisk and other chip stocks get major boosts in the wake of Microsoft’s earnings — MarketWatch Top, 2026-07-30. https://www.marketwatch.com/story/micron-sandisk-and-other-chip-stocks-get-major-boosts-in-the-wake-of-microsofts-earnings-25460e61?mod=mw_rss_topstories
- Source: Why Microsoft’s stock soared to a historic gain after earnings — MarketWatch Top, 2026-07-30. https://www.marketwatch.com/story/why-microsofts-stock-is-soaring-toward-a-historic-gain-after-earnings-96cd5b1e?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.02), 2025-10-20 (d=0.06)

### [RED 6.58] cross-asset · 2 series ↑
- dyn_jiofin_bo [EQUITIES]: last 256.05, z20 3.74, zc 1.76, resid-z 2.42 [unexplained], 1d 3.71%, |z20|=3.74
- nifty_midcap_100 [INDICES]: last 62873.15, z20 0.90, zc 0.40, resid-z 0.05 [quiet], 1d 0.33%, 1y-pct=98
- **Mechanism**: The recent surge in Jio Financial Services' stock price can be attributed to the announcement of a record date for determining eligible shareholders for the final dividend of FY26. This news has led to a significant increase in the stock's price, with a z20 level of 3.74, indicating a strong upward move. The resid_z of 2.36 suggests that a portion of this move is unexplained by factors, potentially indicating a speculative or sentiment-driven component.
- **Gap**: No gap: the big raw move in Jio Financial Services' stock price is largely priced in, given the significant z20 level and the fact that the stock has already reacted to the news.
- **India take**: The Indian instrument that expresses this move is the Nifty 50, which has already reacted with a z20 of 1.33. Other related instruments such as Nifty Metal and Bharat Coal have also reacted, while Indian Bank and IndusInd Bank remain quiet.
- Watch next: dyn_jiofin_bo (up) — already moved; record date announcement for dividend
- **India receivers**: nifty_50 (rho 0.824, z 1.33); dyn_indianb_ns (rho 0.625, z 0.56); dyn_indusindbk_bo (rho 0.62, z -0.06); nifty_metal (rho 0.601, z 1.62)
- Source: Jio Financial Services declares record date to finalise eligible shareholders for FY26 final dividend — Mint Markets, 2026-07-31. https://www.livemint.com/market/stock-market-news/jio-financial-services-declares-record-date-to-finalise-eligible-shareholders-for-fy26-final-dividend-11785505871823.html
- Historical analogues: 2025-07-15 (d=0.22), 2024-10-01 (d=0.26), 2025-05-30 (d=0.49)

### [RED 6.43] dxy ↓
- dxy [FX]: last 99.80, z20 -3.43, zc -0.55, resid-z -2.49 [unexplained], 1d -0.21%, 20d range extreme; |z20|=3.43
- **Mechanism**: The recent decline in the US Dollar Index (DXY) has created a potential transmission opportunity, with historically correlated instruments such as UST 2Y yields yet to move. The DXY's unexplained move, as indicated by its resid_z score, may propagate through the gold_silver_comove and metal_copper_channel, which are currently valid. However, the dxy_inr_channel is weak, which may limit the transmission to Indian markets.
- **Gap**: No gap: the DXY's move is largely unexplained, but its resid_z score is -2.49, which is not extreme enough to indicate a significant anomaly
- **India take**: The Indian instrument that may express this move is the Nifty 50, which has a historical correlation with gold. However, the dxy_inr_channel is weak, which may limit the transmission. The Nifty 50 has not reacted yet, and its movement will be watched closely.
- Watch next: ust_2y (down) — not yet - watch; historically leads DXY by 3 days
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [RED 6.32] cross-asset · 6 series ↑
- comex_copper [COMMODITIES]: last 6.51, z20 2.17, zc 0.43, resid-z -0.05 [quiet], 1d 0.98%, |z20|=2.17; 1y-pct=97; co-occur[metal_copper] same-direction (channel VALID)
- cac_40 [INDICES]: last 8516.90, z20 2.02, zc 0.41, resid-z 0.30 [quiet], 1d 0.37%, |z20|=2.02; 1y-pct=98
- ftse_100 [INDICES]: last 10876.26, z20 1.72, zc -0.33, resid-z -0.39 [quiet], 1d -0.19%, |z20|=1.72; 1y-pct=98
- dax [INDICES]: last 25631.25, z20 1.42, zc 0.08, resid-z -0.24 [quiet], 1d 0.08%, 1y-pct=99
- stoxx_50 [INDICES]: last 6354.63, z20 1.32, zc 0.15, resid-z -0.20 [quiet], 1d 0.16%, 1y-pct=98
- dow_jones [INDICES]: last 52484.26, z20 0.29, zc 0.47, resid-z 0.22 [quiet], 1d 0.53%, 1y-pct=96
- **Mechanism**: The recent surge in US stocks, driven by strong earnings from tech giants like Amazon and Microsoft, has led to a rise in bond yields, which in turn has affected the global markets. The VALID vix_equity_inverse channel suggests that the vol spike will lead to an equity drawdown, while the VALID metal_copper_channel indicates that global copper leads Indian metal equities. The NEUTRAL regime and the lack of a clear risk-off or risk-on tone suggest that the markets are in a state of flux.
- **Gap**: No gap: the big raw move in global markets has been largely priced in, with resid_z values close to zero for most series, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian market, as represented by the nifty_50, has already reacted to the global cues, while the nifty_midcap_100 remains quiet. The metal_copper_channel suggests that Indian metal equities may follow the lead of global copper prices.
- Watch next: nifty_50 (down) — already moved; reacted to global cues
- **India receivers**: nifty_50 (rho 0.538, z 1.33); nifty_midcap_100 (rho 0.513, z 0.9)
- Source: Dow Jones, S&P 500, Nasdaq: Stocks rise on tech earnings; bond yields hit multi-year highs — BusinessLine Mkts, 2026-08-01. https://www.thehindubusinessline.com/markets/dow-jones-sp-500-nasdaq-stocks-rise-on-tech-earnings-bond-yields-hit-multi-year-highs/article71293452.ece
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks seesaw as bond yields rise and AI spending surges — ET Markets, 2026-07-31. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-hormuz-deal-crude-oil-fed-warsh-earnings-forecast-amazon-apple-nvidia-amd-meta-chip-stock-price-news-31st-july-2026/liveblog/132767346.cms
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US market ends higher as Amazon eases AI spending jitters — ET Markets, 2026-07-31. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-hormuz-deal-crude-oil-fed-warsh-earnings-forecast-amazon-apple-nvidia-amd-meta-chip-stock-price-news-31st-july-2026/liveblog/132767346.cms
- Historical analogues: 2024-11-07 (d=0.82), 2024-10-11 (d=0.99), 2024-10-04 (d=1.03)

### [AMBER 6.1] wti ↑
- wti [COMMODITIES]: last 86.80, z20 1.10, zc 1.06, resid-z 1.36 [quiet], 1d 3.84%, 1-session move +3.84% ≥ 1.5%
- **Mechanism**: The recent surge in WTI prices is driven by supply disruptions and escalating U.S.-Iran hostilities, which have led to increased bullish bets by hedge funds. This move is priced, given the small resid_z of 1.36, indicating that the factor exposures have largely explained the price movement. The valid gold_silver_comove and metal_copper_channel may also contribute to the propagation of this move, as monetary metals and copper prices are influenced by global economic trends.
- **Gap**: No gap: the current WTI price move is largely explained by factor exposures, with a small resid_z of 1.36, indicating that the move is priced.
- **India take**: The Indian instrument that expresses this move is the nifty_midcap_100, which has a negative correlation with WTI. However, it has not reacted yet, given its quiet status. The midcap_largecap_ratio is also a transmission candidate, but it has not moved in response to the WTI surge.
- Watch next: brent (up) — not yet - watch; high correlation with WTI
- **India receivers**: nifty_midcap_100 (rho -0.491, z 0.9); midcap_largecap_ratio (rho -0.404, z -0.46)
- Source: Hedge Funds Add Bullish Bets on Oil at Fastest Pace Since March — Mint Markets, 2026-07-31. https://www.livemint.com/market/hedge-funds-add-bullish-bets-on-oil-at-fastest-pace-since-march-11785532739554.html
- Source: Oil Posts Biggest Monthly Jump Since March as Iran War Simmers — Mint Markets, 2026-07-31. https://www.livemint.com/market/oil-posts-biggest-monthly-jump-since-march-as-iran-war-simmers-11785529272579.html
- Source: Abqaiq Is a Warning That Oil Markets May Be Misreading — OilPrice, 2026-07-31. https://oilprice.com/Energy/Crude-Oil/Abqaiq-Is-a-Warning-That-Oil-Markets-May-Be-Misreading.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-08-30 (d=0.0), 2025-10-22 (d=0.01)

### [AMBER 6.01] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.21, z20 2.08, zc 0.25, resid-z 1.09 [quiet], 1d 0.19%, |z20|=2.08; 1y-pct=100
- dyn_bond [EQUITIES]: last 90.49, z20 -1.70, zc -1.16, resid-z 0.13 [quiet], 1d -0.33%, 1y-pct=0
- ust_10y [RATES]: last 4.68, z20 1.39, zc 0.22, resid-z 1.94 [unexplained], 1d 0.21%, 1y-pct=99
- tips_10y_real [RATES]: last 2.41, z20 1.11, zc 0.00, resid-z 1.88 [unexplained], 1d 0.00%, 1y-pct=98
- ust_2y [RATES]: last 4.23, z20 0.15, zc 0.18, resid-z 2.50 [unexplained], 1d 0.24%, 1y-pct=96
- **Mechanism**: The recent surge in US Treasury yields, particularly the 10-year note reaching its highest level since January 2025, is driving the current market move. This increase in yields is attributed to fears of rising oil prices fueling inflation, which may prompt the Federal Reserve to hike interest rates. The mechanism of transmission is through the valid channel of gold_silver_comove and metal_copper_channel, which may lead to a rotation in Indian metal equities.
- **Gap**: No gap: The big raw move in US Treasury yields is largely priced, with resid_z values indicating that the moves are mostly explained by factor exposures.
- **India take**: The Indian 10-year government bond yield may react to the US Treasury yield surge, potentially leading to a rise in sovereign bond yields. The deferment of India's entry into the Bloomberg Global Aggregate Index may also contribute to this increase.
- Watch next: nifty_50 (down) — not yet - watch; Risk-off sentiment may lead to a decline in Indian equities
- Source: Dow Jones, S&P 500, Nasdaq: Stocks rise on tech earnings; bond yields hit multi-year highs — BusinessLine Mkts, 2026-08-01. https://www.thehindubusinessline.com/markets/dow-jones-sp-500-nasdaq-stocks-rise-on-tech-earnings-bond-yields-hit-multi-year-highs/article71293452.ece
- Source: Fed chief Warsh faces hard choice on inflation after bond market's 'red flag' — ET Markets, 2026-08-01. https://economictimes.indiatimes.com/markets/us-stocks/news/fed-chief-warsh-faces-hard-choice-on-inflation-after-bond-markets-red-flag/articleshow/132780818.cms
- Source: Bloomberg delays India’s entry to global bond index yet again — ET Markets, 2026-08-01. https://economictimes.indiatimes.com/markets/bonds/bloomberg-delays-indias-entry-to-global-bond-index-yet-again/articleshow/132779829.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

## Watchlist (below surfacing floor)
dyn_thangamayl_ns ↓ (5.89), dyn_coin ↓ (5.56), gold_silver_ratio ↑ (4.22), dyn_lth ↑ (4.0), dyn_meta ↓ (3.85), dyn_cupid_ns ↑ (3.68), dyn_tech ↑ (3.4), dyn_icicigi_bo ↓ (3.02), usd_cny ↓ (3.0), dyn_ohi ↑ (2.66), ust_2s10s ↑ (2.6), dyn_patanjali_ns ↓ (2.52)

## India macro
- nifty_50: 24366.6992 (1d 0.20%, z20 1.33, flag none)
- nifty_midcap_100: 62873.1484 (1d 0.33%, z20 0.90, flag amber)
- usd_inr: 95.3800 (1d -0.36%, z20 -1.29, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5803 (1d 0.12%, z20 -0.46, flag none)
- Next India prints: NSDL FPI flows T-2d · IMD weekly rainfall T-2d · RBI MPC decision T-6d · RBI Weekly Statistical Supplement T-6d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 76.0 — "Strong earnings, FPI inflows keep Indian equities resilient despite global risks"
- INDIANB.NS (INDIAN BANK) score 72.5 — "Bank credit to industry up 19%, personal loans stay strong"
- COALINDIA.NS (COAL INDIA LTD) score 72.2 — "Strong earnings, FPI inflows keep Indian equities resilient despite global risks"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 71.6 — "Strong earnings, FPI inflows keep Indian equities resilient despite global risks"
- COIN (Coinbase Global, Inc.) score 55.6 — "Strong earnings, FPI inflows keep Indian equities resilient despite global risks"
- BAC (Bank of America Corporation) score 54.0 — "Bank credit to industry up 19%, personal loans stay strong"
- TECHM.NS (TECH MAHINDRA LIMITED) score 53.3 — "Dow Jones, S&P 500, Nasdaq: Stocks rise on tech earnings; bond yields hit multi-year highs"
- HDB (HDFC Bank Limited) score 52.0 — "Bank credit to industry up 19%, personal loans stay strong"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 51.6 — "Dow Jones, S&P 500, Nasdaq: Stocks rise on tech earnings; bond yields hit multi-year highs"
- IDBI.NS (IDBI BANK LIMITED) score 50.4 — "Bank credit to industry up 19%, personal loans stay strong"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 50.3 — "Bank credit to industry up 19%, personal loans stay strong"
- OHI (Omega Healthcare Investors, In) score 49.5 — "Stock market timings change from Monday, August 3: Everything investors and traders need t"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 45.9 — "Bank credit to industry up 19%, personal loans stay strong"
- TECH (Bio-Techne Corp) score 38.5 — "Dow Jones, S&P 500, Nasdaq: Stocks rise on tech earnings; bond yields hit multi-year highs"
- BOND (PIMCO Active Bond Exchange-Tra) score 30.5 — "Bloomberg delays India’s entry to global bond index yet again"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 29.6 — "U.S., ISRAEL WEIGH STRIKES ON IRAN ENERGY SITES The U.S. and Israel are preparing a potent"
- LTH (Life Time Group Holdings, Inc.) score 27.4 — "Bitcoin slips below $63,000 to a two-week low as weak Coinbase earnings and fading optimis"
- CHKP (Check Point Software Technolog) score 25.8 — "Stocks to watch: Maruti Suzuki, IOC, Tata Steel among shares in focus today; check list he"
- 301077.SZ (CHINASTARS) score 20.0 — "Did China build a top-tier AI model by itself? A new report suggests Nvidia chips played a"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 16.9 — "Top Gainers & Losers on 31 July: Bajaj Finance, Hyundai Motor, GAIL, Tata Motors, Redingto"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 15.8 — "Adani Energy plans another share sale by early next fiscal year"
- MS (Morgan Stanley) score 14.7 — "MARKET MOVERS 🟢 UPGRADES $BAX: Citigroup upgraded to Neutral; PT raised to $28 from $17 $C"
- AAPL (Apple Inc.) score 13.8 — "Apple set to lose nearly $500 billion in value after weak forecast"
- AMZN (Amazon.com, Inc.) score 11.5 — "Amazon soars as cloud revenue surge allays fears over ballooning AI bets"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 11.1 — "Global Coal Consumption Hits Record Even as Coal Power Declines"
- JIOFIN.BO (Jio Financial Services Limited) score 10.3 — "Jio Financial Services declares record date to finalise eligible shareholders for FY26 fin"
- MSFT (Microsoft Corporation) score 9.9 — "Microsoft's AI Bet Pays Off: Key Takeaways From Its Blockbuster Quarter"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.4 — "South Korea’s chip giants just logged their biggest rally ever. What it means for the glob"
- VT (Vanguard Total World Stock Ind) score 9.0 — "5 World Market themes for the week ahead"
- GS (Goldman Sachs Group, Inc. (The) score 8.8 — "TRADERS BRACE FOR S&P 500 VOLATILITY Investors are increasing hedges against broader S&P 5"
- META (Meta) score 8.6 — "Global Market: China's factory activity contracts unexpectedly in July; metal, commodity s"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.6 — "Jio Financial Services declares record date to finalise eligible shareholders for FY26 fin"
- INFY (Infosys Limited) score 8.5 — "Kospi’s mammoth 17% surge spells caution for Indian IT stocks. Why TCS, Infosys, others ar"
- PCJEWELLER.NS (PC JEWELLER LTD) score 8.1 — "KGSMA seek BIS probe into counterfeit hallmarked gold jewellery in Kerala"
- NVDA (NVIDIA Corporation) score 6.8 — "Did China build a top-tier AI model by itself? A new report suggests Nvidia chips played a"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.7 — "Higher oil prices could push Fed to resume rate hikes later this year: ICICI Bank report"
- THANGAMAYL.NS (THANGAMAYIL JEWELLERY LTD) score 3.7 — "KGSMA seek BIS probe into counterfeit hallmarked gold jewellery in Kerala"
- ETERNAL.NS (ETERNAL LIMITED) score 3.6 — "Zepto IPO hurdle revives investor interest in Swiggy, Eternal; shares set for best month i"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 1.9 — "LT Foods shares jump 4% on strong Q1 results; stock outperforms market"
- CUPID.NS (CUPID LIMITED) score 1.3 — "Cupid increases investment by $5 million in GII’s Healthcare-focused platform"

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