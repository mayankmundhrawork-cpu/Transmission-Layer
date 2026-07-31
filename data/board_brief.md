# Transmission Layer — board brief · 2026-07-31 21:52Z

data as of **2026-07-31** · 98 series · 12 red / 36 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.355, 2d in regime; vol-pct 0.357, breadth-off 0.353, Markov P(high-vol) 0.128)
- [INVERTED] **safe_haven_gold** — corr20 -0.47, corr60 -0.45, contra nifty_50 corr20=0.23, last shift 2026-06-08. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.82, last shift 2026-05-15. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.35, corr60 0.32, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.15, corr60 -0.06, last shift 2026-06-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.84, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.05, corr60 -0.04, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.13, corr60 -0.24, last shift 2026-05-08. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.26, corr60 0.2, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **5 of 90** scanned series survive multiplicity control (effective p ≤ 0.00244553738718456)
- **SETUP** dyn_coin → asx_200: leads 1d (ccf 0.323, β 0.0516, p 0.0); driver zc -2.26 → expected -0.548%. Type hit-rate 0.813 (n=3319).
- **SETUP** btc_usd → asx_200: leads 1d (ccf 0.311, β 0.0865, p 0.0); driver zc -1.51 → expected -0.239%. Type hit-rate 0.813 (n=3319).
- **SETUP** btc_usd → aud_usd: leads 1d (ccf 0.284, β 0.061, p 0.0); driver zc -1.51 → expected -0.168%. Type hit-rate 0.813 (n=3319).
- **SETUP** dyn_coin → aud_usd: leads 1d (ccf 0.264, β 0.0328, p 0.00021); driver zc -2.26 → expected -0.348%. Type hit-rate 0.813 (n=3319).
- **SETUP** btc_usd → usd_mxn: leads 1d (ccf -0.254, β -0.0606, p 7e-05); driver zc -1.51 → expected 0.167%. Type hit-rate 0.813 (n=3319).
- Track record · residual_reversion: hit-rate **0.487** (n=1145) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.813** (n=3319) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.02] cross-asset · 2 series ↑
- usd_jpy [FX]: last 157.40, z20 -7.19, zc -11.41, resid-z -10.81 [unexplained], 1d -3.61%, |z20|=7.19
- dyn_amzn [EQUITIES]: last 271.61, z20 3.84, zc 6.86, resid-z 1.43 [moved], 1d 15.33%, |z20|=3.84; 1y-pct=97
- **Mechanism**: The move in usd_jpy and dyn_amzn is driven by Amazon's strong quarterly report, which eased concerns about AI infrastructure spending. This has led to a surge in Amazon shares and a subsequent impact on the USD/JPY currency pair. The correlation between dyn_amzn and usd_jpy is likely due to the influence of US tech stocks on the broader market and currency movements.
- **Gap**: No gap: The big raw move in usd_jpy has a small resid_z, indicating that the move is largely priced in and not an anomaly.
- **India take**: The Indian instrument dyn_thangamayl_ns has reacted to the move in dyn_amzn, with a correlation of -0.36. The Nifty 50 may also be influenced by the risk-off safe-haven bid, although the dxy_inr_channel is currently weak.
- Watch next: usd_jpy (up) — already moved; Amazon's strong quarterly report has eased concerns about AI spending
- Watch next: dyn_amzn (up) — already moved; Strong quarterly report and upbeat outlook
- **India receivers**: dyn_thangamayl_ns (rho -0.36, z -3.89)
- Source: US stocks: US market ends higher as Amazon soothes AI jitters — ET Markets, 2026-07-31. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-us-market-ends-higher-as-amazon-soothes-ai-jitters/articleshow/132776618.cms
- Source: Amazon shares surge 13% as cloud growth eases AI spending fears — ET Markets, 2026-07-31. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/amazon-shares-surge-13-as-cloud-growth-eases-ai-spending-fears/articleshow/132772194.cms
- Source: AMAZON SHARES JUMP 15.2%, SET FOR BIGGEST PERCENTAGE GAIN SINCE 2012 — DeItaone, 2026-07-31. https://t.me/walter_bloomberg/34158
- Historical analogues: 2024-10-16 (d=0.15), 2024-11-21 (d=0.23), 2026-03-31 (d=0.24)

### [RED 7.74] fx · 4 series ↑
- eur_usd [FX]: last 1.15, z20 4.08, zc 1.41, resid-z 1.73 [unexplained], 1d 0.52%, |z20|=4.08
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
- **India receivers**: eur_inr (rho 0.44, z 1.01)
- Source: Global Market: Euro zone, US bond yields log biggest monthly rise since March on Middle East inflation concerns — ET Markets, 2026-07-31. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-us-bond-yields-log-biggest-monthly-rise-since-march-on-middle-east-inflation-concerns/articleshow/132761537.cms
- Source: UK bond yields and sterling dip after BoE holds rates steady — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/bonds/uk-bond-yields-and-sterling-dip-after-boe-holds-rates-steady/articleshow/132740517.cms
- Source: Digital euro app to incorporate highest accessibility standards — ECB press, 2026-07-30. https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260730~3b3bfbb565.en.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 6.95] dyn_msft ↑
- dyn_msft [EQUITIES]: last 464.92, z20 4.95, zc 0.72, resid-z 6.76 [unexplained], 1d 3.06%, |z20|=4.95
- **Mechanism**: The surge in Microsoft's stock price is driven by its strong earnings report, which exceeded expectations and demonstrated the success of its AI investments. This move is likely to propagate through the valid vix_equity_inverse channel, as the vol spike is likely to lead to an equity drawdown. However, the current regime is neutral, which may limit the impact of this move.
- **Gap**: No gap: the big raw move in Microsoft's stock price is largely explained by its strong earnings report, with a resid_z of 6.76, indicating that the move is mostly priced in.
- **India take**: The Indian instrument dyn_thangamayl_ns has already reacted to the move in Microsoft's stock price, with a negative correlation of -0.387. This suggests that the Indian market has already factored in the implications of Microsoft's earnings report.
- Watch next: dyn_msft (up) — already moved; strong earnings report
- **India receivers**: dyn_thangamayl_ns (rho -0.387, z -3.89)
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
- **India receivers**: nifty_50 (rho 0.817, z 1.33); dyn_indianb_ns (rho 0.634, z 0.56); dyn_indusindbk_bo (rho 0.625, z -0.06); nifty_metal (rho 0.618, z 1.62)
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
- dax [INDICES]: last 25631.25, z20 1.42, zc 0.09, resid-z -0.24 [quiet], 1d 0.08%, 1y-pct=99
- stoxx_50 [INDICES]: last 6354.63, z20 1.32, zc 0.15, resid-z -0.20 [quiet], 1d 0.16%, 1y-pct=98
- dow_jones [INDICES]: last 52484.26, z20 0.29, zc 0.47, resid-z 0.22 [quiet], 1d 0.53%, 1y-pct=96
- **Mechanism**: cross-asset · 6 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-11-07 (z-distance 0.82).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.55 via cac_40, z 1.33, reacted); nifty_midcap_100 (rho 0.528 via dax, z 0.9, quiet)
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.671 vs comex_copper, historically leads by 4d
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.803 vs comex_copper
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.589 vs comex_copper, historically leads by 1d
- Watch next: vix (inverse) — not yet - watch; rho -0.56 vs comex_copper, historically leads by 3d
- Watch next: brent (inverse) — not yet - watch; rho -0.523 vs cac_40, historically leads by 5d
- **India receivers**: nifty_50 (rho 0.55, z 1.33); nifty_midcap_100 (rho 0.528, z 0.9)
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks seesaw as bond yields rise and AI spending surges — ET Markets, 2026-07-31. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-hormuz-deal-crude-oil-fed-warsh-earnings-forecast-amazon-apple-nvidia-amd-meta-chip-stock-price-news-31st-july-2026/liveblog/132767346.cms
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US market ends higher as Amazon eases AI spending jitters — ET Markets, 2026-07-31. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-hormuz-deal-crude-oil-fed-warsh-earnings-forecast-amazon-apple-nvidia-amd-meta-chip-stock-price-news-31st-july-2026/liveblog/132767346.cms
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: Nasdaq jumps over 2% as semiconductor stocks recover from rout — ET Markets, 2026-07-30. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-hormuz-deal-brent-crude-oil-fed-warsh-rate-earnings-forecast-microsoft-amd-apple-amazon-meta-chip-stock-price-news-30th-july-2026/liveblog/132739714.cms
- Historical analogues: 2024-11-07 (d=0.82), 2024-10-11 (d=0.99), 2024-10-04 (d=1.03)

### [AMBER 6.1] wti ↑
- wti [COMMODITIES]: last 86.80, z20 1.10, zc 1.06, resid-z 1.36 [quiet], 1d 3.84%, 1-session move +3.84% ≥ 1.5%
- **Mechanism**: The recent surge in WTI prices is driven by supply disruptions and escalating U.S.-Iran hostilities, which have led to increased bullish bets by hedge funds. This move is priced, given the small resid_z of 1.36, indicating that the factor exposures have largely explained the price movement. The valid gold_silver_comove and metal_copper_channel may also contribute to the propagation of this move, as monetary metals and copper prices are influenced by global economic trends.
- **Gap**: No gap: the current WTI price move is largely explained by factor exposures, with a small resid_z of 1.36, indicating that the move is priced.
- **India take**: The Indian instrument that expresses this move is the nifty_midcap_100, which has a negative correlation with WTI. However, it has not reacted yet, given its quiet status. The midcap_largecap_ratio is also a transmission candidate, but it has not moved in response to the WTI surge.
- Watch next: brent (up) — not yet - watch; high correlation with WTI
- **India receivers**: nifty_midcap_100 (rho -0.479, z 0.9); midcap_largecap_ratio (rho -0.404, z -0.46)
- Source: Hedge Funds Add Bullish Bets on Oil at Fastest Pace Since March — Mint Markets, 2026-07-31. https://www.livemint.com/market/hedge-funds-add-bullish-bets-on-oil-at-fastest-pace-since-march-11785532739554.html
- Source: Oil Posts Biggest Monthly Jump Since March as Iran War Simmers — Mint Markets, 2026-07-31. https://www.livemint.com/market/oil-posts-biggest-monthly-jump-since-march-as-iran-war-simmers-11785529272579.html
- Source: Abqaiq Is a Warning That Oil Markets May Be Misreading — OilPrice, 2026-07-31. https://oilprice.com/Energy/Crude-Oil/Abqaiq-Is-a-Warning-That-Oil-Markets-May-Be-Misreading.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-08-30 (d=0.0), 2025-10-22 (d=0.01)

### [AMBER 6.01] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.21, z20 2.08, zc 0.25, resid-z 1.09 [quiet], 1d 0.19%, |z20|=2.08; 1y-pct=100
- dyn_bond [EQUITIES]: last 90.49, z20 -1.70, zc -1.15, resid-z 0.13 [quiet], 1d -0.33%, 1y-pct=0
- ust_10y [RATES]: last 4.68, z20 1.39, zc 0.22, resid-z 1.94 [unexplained], 1d 0.21%, 1y-pct=99
- tips_10y_real [RATES]: last 2.41, z20 1.11, zc 0.00, resid-z 1.88 [unexplained], 1d 0.00%, 1y-pct=98
- ust_2y [RATES]: last 4.23, z20 0.15, zc 0.18, resid-z 2.50 [unexplained], 1d 0.24%, 1y-pct=96
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.593 vs ust_30y
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.528 vs dyn_bond
- Watch next: brent (co-move) — not yet - watch; rho 0.524 vs ust_30y
- Watch next: sp500 (inverse) — not yet - watch; rho -0.51 vs ust_10y
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.505 vs dyn_bond
- Source: TREASURY SELLOFF GATHERS MOMENTUM U.S. Treasury yields climbed across the curve after Fed officials Lorie Logan and Beth Hammack defended their calls for a 25 bp rate hike, boosting expectations of near-term tightening. The 10-year Treasury yield rose to 4.737%, its highest — DeItaone, 2026-07-31. https://t.me/walter_bloomberg/34157
- Source: US 10-YEAR TREASURY YIELDS RISE TO 4.7388%, HIGHEST SINCE JANUARY 2025 — DeItaone, 2026-07-31. https://t.me/walter_bloomberg/34156
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks seesaw as bond yields rise and AI spending surges — ET Markets, 2026-07-31. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-hormuz-deal-crude-oil-fed-warsh-earnings-forecast-amazon-apple-nvidia-amd-meta-chip-stock-price-news-31st-july-2026/liveblog/132767346.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

## Watchlist (below surfacing floor)
dyn_thangamayl_ns ↓ (5.89), dyn_coin ↓ (5.56), gold_silver_ratio ↑ (4.22), dyn_lth ↑ (4.0), dyn_meta ↓ (3.85), dyn_cupid_ns ↑ (3.68), dyn_tech ↑ (3.4), dyn_bac ↑ (3.07), dyn_icicigi_bo ↓ (3.02), usd_cny ↓ (3.0), dyn_301077_sz ↓ (2.79), dyn_ohi ↑ (2.66)

## India macro
- nifty_50: 24366.6992 (1d 0.20%, z20 1.33, flag none)
- nifty_midcap_100: 62873.1484 (1d 0.33%, z20 0.90, flag amber)
- usd_inr: 95.3800 (1d -0.36%, z20 -1.29, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5803 (1d 0.12%, z20 -0.46, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 77.4 — "State Bank of India's perpetual bond demand seen spurring more issuances, bankers say"
- COALINDIA.NS (COAL INDIA LTD) score 73.2 — "State Bank of India's perpetual bond demand seen spurring more issuances, bankers say"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 72.6 — "State Bank of India's perpetual bond demand seen spurring more issuances, bankers say"
- INDIANB.NS (INDIAN BANK) score 72.5 — "US TREASURY HAS INFORMED BANKS THAT IT MAY INTERVENE IN YEN MARKET ON FRIDAY - SOURCE FAMI"
- COIN (Coinbase Global, Inc.) score 57.3 — "Bloomberg delays India bonds inclusion in global index as investors seek proof reforms wor"
- BAC (Bank of America Corporation) score 56.7 — "US TREASURY HAS INFORMED BANKS THAT IT MAY INTERVENE IN YEN MARKET ON FRIDAY - SOURCE FAMI"
- TECHM.NS (TECH MAHINDRA LIMITED) score 56.0 — "US wheat falls on technical trading"
- HDB (HDFC Bank Limited) score 54.5 — "US TREASURY HAS INFORMED BANKS THAT IT MAY INTERVENE IN YEN MARKET ON FRIDAY - SOURCE FAMI"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 54.0 — "US wheat falls on technical trading"
- OHI (Omega Healthcare Investors, In) score 52.9 — "TRADERS BRACE FOR S&P 500 VOLATILITY Investors are increasing hedges against broader S&P 5"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 52.6 — "US TREASURY HAS INFORMED BANKS THAT IT MAY INTERVENE IN YEN MARKET ON FRIDAY - SOURCE FAMI"
- IDBI.NS (IDBI BANK LIMITED) score 51.6 — "US TREASURY HAS INFORMED BANKS THAT IT MAY INTERVENE IN YEN MARKET ON FRIDAY - SOURCE FAMI"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 47.9 — "US TREASURY HAS INFORMED BANKS THAT IT MAY INTERVENE IN YEN MARKET ON FRIDAY - SOURCE FAMI"
- TECH (Bio-Techne Corp) score 39.8 — "US wheat falls on technical trading"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 29.0 — "TREASURY SELLOFF GATHERS MOMENTUM U.S. Treasury yields climbed across the curve after Fed "
- BOND (PIMCO Active Bond Exchange-Tra) score 28.9 — "State Bank of India's perpetual bond demand seen spurring more issuances, bankers say"
- LTH (Life Time Group Holdings, Inc.) score 28.7 — "U.S. CONSUMER SENTIMENT TOPS ESTIMATES University of Michigan consumer sentiment rose to 5"
- CHKP (Check Point Software Technolog) score 28.1 — "Stocks to watch: Maruti Suzuki, IOC, Tata Steel among shares in focus today; check list he"
- 301077.SZ (CHINASTARS) score 21.8 — "Did China build a top-tier AI model by itself? A new report suggests Nvidia chips played a"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 18.4 — "Top Gainers & Losers on 31 July: Bajaj Finance, Hyundai Motor, GAIL, Tata Motors, Redingto"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 17.2 — "Adani Energy plans another share sale by early next fiscal year"
- MS (Morgan Stanley) score 16.0 — "MARKET MOVERS 🟢 UPGRADES $BAX: Citigroup upgraded to Neutral; PT raised to $28 from $17 $C"
- AAPL (Apple Inc.) score 13.9 — "Supply-chain legend Tim Cook finally meets his match with Apple’s memory crunch"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 12.1 — "Global Coal Consumption Hits Record Even as Coal Power Declines"
- AMZN (Amazon.com, Inc.) score 11.4 — "Dow Jones| Nasdaq | US Stock Market Today | Live: US market ends higher as Amazon eases AI"
- JIOFIN.BO (Jio Financial Services Limited) score 11.2 — "Jio Financial Services declares record date to finalise eligible shareholders for FY26 fin"
- MSFT (Microsoft Corporation) score 10.8 — "Microsoft's AI Bet Pays Off: Key Takeaways From Its Blockbuster Quarter"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.3 — "South Korea’s chip giants just logged their biggest rally ever. What it means for the glob"
- GS (Goldman Sachs Group, Inc. (The) score 9.6 — "TRADERS BRACE FOR S&P 500 VOLATILITY Investors are increasing hedges against broader S&P 5"
- META (Meta) score 9.4 — "Global Market: China's factory activity contracts unexpectedly in July; metal, commodity s"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 9.4 — "Jio Financial Services declares record date to finalise eligible shareholders for FY26 fin"
- INFY (Infosys Limited) score 9.3 — "Kospi’s mammoth 17% surge spells caution for Indian IT stocks. Why TCS, Infosys, others ar"
- PCJEWELLER.NS (PC JEWELLER LTD) score 8.8 — "KGSMA seek BIS probe into counterfeit hallmarked gold jewellery in Kerala"
- VT (Vanguard Total World Stock Ind) score 8.7 — "U.S. TREASURY CHIEF ON IRAN: WE ARE SEARCHING FOR THEIR ASSETS ALL AROUND THE WORLD U.S. T"
- NVDA (NVIDIA Corporation) score 7.4 — "Did China build a top-tier AI model by itself? A new report suggests Nvidia chips played a"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.1 — "Higher oil prices could push Fed to resume rate hikes later this year: ICICI Bank report"
- THANGAMAYL.NS (THANGAMAYIL JEWELLERY LTD) score 4.1 — "KGSMA seek BIS probe into counterfeit hallmarked gold jewellery in Kerala"
- ETERNAL.NS (ETERNAL LIMITED) score 3.9 — "Zepto IPO hurdle revives investor interest in Swiggy, Eternal; shares set for best month i"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 2.0 — "LT Foods shares jump 4% on strong Q1 results; stock outperforms market"
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