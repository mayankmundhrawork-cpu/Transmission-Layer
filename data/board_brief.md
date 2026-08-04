# Transmission Layer — board brief · 2026-08-04 06:40Z

data as of **2026-08-04** · 98 series · 18 red / 27 amber · 8 events surfaced (21 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.475, 1d in regime; vol-pct 0.45, breadth-off 0.5, Markov P(high-vol) 0.07)
- [INVERTED] **safe_haven_gold** — corr20 -0.43, corr60 -0.44, contra nifty_50 corr20=0.18, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.82, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.32, corr60 0.32, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.16, corr60 -0.04, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.84, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.09, corr60 -0.03, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.18, corr60 -0.25, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.29, corr60 0.2, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **6 of 90** scanned series survive multiplicity control (effective p ≤ 0.0010380708664139426)
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.484, β 0.2629, p 0.0); driver zc 1.58 → expected 0.393%. Type hit-rate 0.815 (n=3075).
- **SETUP** dyn_amzn → taiwan_weighted: leads 1d (ccf 0.363, β 0.2869, p 0.0); driver zc 6.66 → expected 4.395%. Type hit-rate 0.815 (n=3075).
- **SETUP** dyn_coin → asx_200: leads 1d (ccf 0.322, β 0.05, p 0.0); driver zc -2.26 → expected -0.529%. Type hit-rate 0.815 (n=3075).
- Track record · residual_reversion: hit-rate **0.495** (n=1144) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.815** (n=3075) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.02] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.27, z20 2.89, zc 1.53, resid-z 1.91 [unexplained], 1d 1.15%, |z20|=2.89; 1y-pct=100
- ust_10y [RATES]: last 4.75, z20 2.37, zc 1.58, resid-z 2.16 [unexplained], 1d 1.50%, |z20|=2.37; 1y-pct=100
- tips_10y_real [RATES]: last 2.47, z20 2.09, zc 1.57, resid-z 2.22 [unexplained], 1d 2.49%, 1d move +6.0bps ≥ 5bps; |z20|=2.09; 1y-pct=100
- dyn_bond [EQUITIES]: last 90.32, z20 -2.02, zc -1.14, resid-z 0.50 [quiet], 1d -0.19%, |z20|=2.02; 1y-pct=0
- ust_2y [RATES]: last 4.28, z20 0.86, zc 0.93, resid-z 1.54 [unexplained], 1d 1.18%, 1y-pct=98
- **Mechanism**: The recent decline in US Treasury yields, driven by easing inflation concerns due to renewed Iran peace talks, has led to an unexplained move in the rates space, with ust_30y, ust_10y, and tips_10y_real showing significant z-scores. This move is likely to propagate through the validated channels, particularly the vix_equity_inverse and gold_silver_comove channels, which are currently active.
- **Gap**: No gap: The big raw move in US Treasury yields is largely priced, with resid_z values indicating that the move is mostly explained by factor exposures, leaving little room for an event-to-price gap.
- **India take**: The Indian instrument that expresses this move is the 10-year Government of India bond yield, which may react to the decline in US Treasury yields through the goi_ust_comove channel, although this channel is currently marked as insufficient data. Alternatively, the metal_copper_channel may transmit the move to Indian metal equities.
- Watch next: nifty_50 (down) — not yet - watch; Risk-on regime and potential transmission from US rates to Indian equities
- Source: US 10-year yield falls from 18-month high on Iran peace talk hopes — ET Markets, 2026-08-03. https://economictimes.indiatimes.com/markets/bonds/us-10-year-yield-falls-from-18-month-high-on-iran-peace-talk-hopes/articleshow/132831577.cms
- Source: Warsh tightened more by pausing than by lifting rates, this bond-market veteran argues. Here’s the math. — MarketWatch Top, 2026-08-03. https://www.marketwatch.com/story/warsh-tightened-more-by-pausing-than-by-lifting-rates-this-bond-market-veteran-argues-heres-the-math-31cb15a1?mod=mw_rss_topstories
- Source: BNP SEES FED HIKES PUSHING YIELDS HIGHER BNP Paribas expects U.S. Treasury yields to keep rising as markets price in future Fed rate hikes. The bank forecasts three Fed hikes starting in December, arguing investors will continue to question the Fed's credibility after last — DeItaone, 2026-08-03. https://t.me/walter_bloomberg/34210
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 8.36] cross-asset · 9 series ↑
- cac_40 [INDICES]: last 8626.25, z20 3.72, zc 0.32, resid-z 0.18 [quiet], 1d 1.37%, |z20|=3.72; 1y-pct=100
- stoxx_50 [INDICES]: last 6431.81, z20 3.17, zc 0.20, resid-z -0.13 [quiet], 1d 1.16%, |z20|=3.17; 1y-pct=100
- dax [INDICES]: last 26038.36, z20 2.90, zc 0.08, resid-z -0.25 [quiet], 1d 1.60%, |z20|=2.90; 1y-pct=100
- comex_copper [COMMODITIES]: last 6.60, z20 2.47, zc 0.37, resid-z -0.83 [quiet], 1d 0.85%, |z20|=2.47; 1y-pct=99; co-occur[metal_copper] same-direction (channel VALID)
- dow_jones [INDICES]: last 53184.43, z20 2.23, zc 0.47, resid-z 0.22 [quiet], 1d 1.33%, |z20|=2.23; 1y-pct=100
- sp500 [INDICES]: last 7599.97, z20 1.85, zc 0.67, resid-z 0.82 [quiet], 1d 1.47%, |z20|=1.85; 1y-pct=99
- dyn_vt [EQUITIES]: last 157.60, z20 1.44, zc 0.23, resid-z -2.02 [unexplained], 1d 1.11%, 1y-pct=95
- ftse_100 [INDICES]: last 10850.38, z20 1.38, zc -0.46, resid-z -0.48 [quiet], 1d -0.16%, 1y-pct=98
- gold_silver_ratio [DERIVED]: last 69.59, z20 -0.21, zc n/a, resid-z n/a [quiet], 1d -1.14%, GSR<75 (extreme low)
- **Mechanism**: The recent rally in global equities, led by the Dow Jones and S&P 500, is driven by easing geopolitical tensions in the Middle East and optimism about inflation easing, as expressed by Fed's Williams. This sentiment is transmitted to Indian markets through correlated instruments like Nifty 50 and Nifty Midcap 100.
- **Gap**: No gap: the big raw move in global equities is largely priced in, with most indices showing high z20 levels and low resid_z values, indicating that the move is explained by factor exposures.
- **India take**: Indian instruments like Nifty 50 and Nifty Midcap 100 have already reacted to the global equity rally, while Nifty Metal has also moved in response to the gold-silver ratio. However, the metal_copper_channel, which is a valid channel, suggests that global copper prices may lead Indian metal equities, potentially driving further moves in Nifty Metal.
- Watch next: nifty_50 (up) — already moved; reacted to global equity rally
- Watch next: nifty_midcap_100 (up) — already moved; reacted to global equity rally
- **India receivers**: nifty_50 (rho 0.539, z 1.6); nifty_midcap_100 (rho 0.535, z 1.46); nifty_metal (rho -0.423, z 3.04)
- Source: Traders in the world’s most important financial market are bracing for a wild stretch ahead — MarketWatch Top, 2026-08-03. https://www.marketwatch.com/story/traders-in-the-worlds-most-important-financial-market-are-bracing-for-a-wild-stretch-ahead-4a1507dc?mod=mw_rss_topstories
- Source: Wall Street rallies, Dow closes at record on Iran talks optimism — Mint Markets, 2026-08-03. https://www.livemint.com/market/wall-street-rallies-dow-closes-at-record-on-iran-talks-optimism-11785787392771.html
- Source: Wall Street climbs as crude oil prices plunge, Amazon jumps 3.8% — Mint Markets, 2026-08-03. https://www.livemint.com/market/stock-market-news/wall-street-climbs-as-crude-oil-prices-plunge-amazon-jumps-38-11785765123026.html
- Historical analogues: 2024-10-10 (d=0.85), 2024-10-03 (d=1.01), 2024-11-07 (d=1.05)

### [RED 7.56] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1466.30, z20 5.56, zc 4.69, resid-z 0.51 [moved], 1d 14.55%, |z20|=5.56; 1y-pct=100
- **Mechanism**: The surge in Ather Energy's stock price is driven by its strong Q1 FY27 results, which showed a significant narrowing in its net loss, signaling improved operating performance. This move is priced, given the stock's z20 level of 5.56 and a relatively low resid_z of 0.51, indicating that the move is largely explained by factor exposures. The metal_copper_channel, which is VALID, may also contribute to the move, as global copper leads Indian metal equities.
- **Gap**: No gap: the move in Ather Energy's stock is largely explained by its strong Q1 results and factor exposures, with a low resid_z indicating that the price move is priced
- **India take**: The Indian instrument that expresses this move is the Nifty Auto index, which may react positively to Ather Energy's strong results. The Nifty Auto index has not yet reacted, but is worth watching for potential upside.
- Watch next: nifty_50 (up) — not yet - watch; Improved sentiment from Ather Energy's results may lift the broader market
- Source: Multibagger stock Ather Energy share price soars 18% to record high post Q1 FY27 results: Should you buy? — Mint Markets, 2026-08-04. https://www.livemint.com/market/stock-market-news/multibagger-stock-ather-energy-share-price-soars-18-to-record-high-post-q1-fy27-results-should-you-buy-11785824415092.html
- Source: Ather Energy share price target goes up to Rs 1,714. What are CLSA, Nomura, and HSBC saying? — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/stocks/news/ather-energy-share-price-target-goes-up-to-rs-1714-what-are-clsa-nomura-and-hsbc-saying/articleshow/132848638.cms
- Source: Q1 Results Today Live: Bharti Airtel, ONGC, Pidilite, Marico, Nykaa, Bharti Hexacom, NHPC, MCX, Godrej Properties, Kalyan Jewellers, Alembic, RITES, Zydus Wellness to announce Q1 results, Ather Energy, KEI, Sundaram Finance shares gain after Q1, DLF, UPL, Nazara, IREDA in red — BusinessLine Mkts, 2026-08-04. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-bharti-airtel-ongc-pidilite-nykaa-marico-nhpc-mcx-godrej-properties-zydus-alembic-rites-kalyan-jewellers-uno-minda-tata-invest-united-breweries-results-04-august-2026/article71300717.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [RED 6.88] cross-asset · 2 series ↑
- dyn_amzn [EQUITIES]: last 284.02, z20 4.05, zc 6.66, resid-z 9.76 [unexplained], 1d 4.58%, |z20|=4.05; 1y-pct=100
- usd_jpy [FX]: last 157.64, z20 -3.43, zc 0.05, resid-z -5.83 [unexplained], 1d 0.04%, |z20|=3.43
- **Mechanism**: The recent surge in the yen, fueled by speculation of further intervention by Japanese authorities, has led to a significant move in the USD/JPY currency pair, which in turn has triggered a reaction in the US equities market, particularly in Amazon stocks. This cross-asset move is likely driven by the transmission of monetary policy and risk sentiment across markets. The verified transmission setup of ust_10y -> usd_jpy and dyn_amzn -> taiwan_weighted suggests a lead-lag relationship between these assets, which may be contributing to the current price action.
- **Gap**: No gap: the big raw move in USD/JPY and Amazon stocks is accompanied by a significant resid_z, indicating that the move is largely unexplained by factor exposures, but the magnitude of the move is not unusually large given the current market conditions and the transmission channels at play.
- **India take**: The Indian transmission candidates, such as dyn_muthootfin_ns and dyn_thangamayl_ns, have already reacted to the move in USD/JPY and Amazon stocks, respectively, suggesting that the Indian market has largely priced in the current developments. However, dyn_cartrade_ns remains quiet and may be worth watching for potential follow-through.
- Watch next: dyn_amzn (up) — already moved; resid_z=9.76 indicates an unexplained move
- Watch next: usd_jpy (down) — already moved; resid_z=-5.83 indicates an unexplained move
- **India receivers**: dyn_muthootfin_ns (rho -0.511, z -2.65); dyn_cartrade_ns (rho -0.369, z -0.34); dyn_thangamayl_ns (rho -0.368, z -3.12)
- Source: Yen surges to three-month peak, dollar pares losses after intervention — Mint Markets, 2026-08-03. https://www.livemint.com/market/yen-surges-to-three-month-peak-dollar-pares-losses-after-intervention-11785792603276.html
- Source: Yen Holds Steady in US Hours After Speculation of Intervention — Mint Markets, 2026-08-03. https://www.livemint.com/market/yen-holds-steady-in-us-hours-after-speculation-of-intervention-11785792595897.html
- Source: Oil drops, stocks gain amid Iran peace hopes; yen firms as investors watch for further intervention — Mint Markets, 2026-08-03. https://www.livemint.com/market/oil-drops-stocks-gain-amid-iran-peace-hopes-yen-firms-as-investors-watch-for-further-intervention-11785792593711.html
- Historical analogues: 2024-10-16 (d=0.15), 2024-11-21 (d=0.23), 2026-03-31 (d=0.24)

### [RED 6.27] dyn_msft ↑
- dyn_msft [EQUITIES]: last 487.60, z20 4.27, zc 0.72, resid-z 0.18 [quiet], 1d 4.92%, |z20|=4.27
- **Mechanism**: The recent surge in Microsoft's stock, erasing its year-to-date losses, is driven by its addition to Goldman Sachs' U.S. Conviction List and a broader rally in US hyperscalers. This move is unexplained by factor exposures, with a high resid_z of 6.76. The valid vix_equity_inverse channel suggests that the low volatility environment is contributing to the equity rally.
- **Gap**: No gap: the big raw move in Microsoft's stock is accompanied by a small z20 of 4.31, indicating that the move is largely priced in.
- **India take**: The Indian instrument dyn_thangamayl_ns has already reacted to the move in Microsoft's stock, with a negative rho of -0.383. Further reaction in Indian metal equities may be expected via the valid metal_copper_channel.
- Watch next: dyn_msft (up) — already moved; recent surge in stock price
- **India receivers**: dyn_thangamayl_ns (rho -0.382, z -3.12)
- Source: Microsoft’s stock is on a run not seen in 26 years — erasing its year-to-date losses — MarketWatch Top, 2026-08-03. https://www.marketwatch.com/story/microsofts-stock-is-on-a-run-not-seen-in-26-years-erasing-its-year-to-date-losses-d9827b6c?mod=mw_rss_topstories
- Source: SHARES OF US HYPERSCALERS CLIMB • META RISES 6.1% • MICROSOFT JUMPS 4.7% • AMAZON GAINS 4.6% — DeItaone, 2026-08-03. https://t.me/walter_bloomberg/34236
- Source: GOLDMAN REFRESHES U.S. CONVICTION LIST Goldman Sachs added Applied Materials ( $AMAT), Delta ( $DAL), Microsoft ( $MSFT), O'Reilly Automotive ( $ORLY), Viking Holdings ( $VIK) and UPS to its U.S. Conviction List. The firm removed Broadcom ( $AVGO), Dick's Sporting Goods ( — DeItaone, 2026-08-03. https://t.me/walter_bloomberg/34209
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.02), 2025-10-20 (d=0.06)

### [RED 6.26] cross-asset · 3 series ↑
- dyn_jiofin_bo [EQUITIES]: last 263.50, z20 2.94, zc 0.25, resid-z 2.39 [unexplained], 1d 0.57%, |z20|=2.94
- nifty_50 [INDICES]: last 24508.95, z20 1.60, zc -1.46, resid-z 0.42 [quiet], 1d -1.07%, |z20|=1.60
- nifty_midcap_100 [INDICES]: last 63330.45, z20 1.46, zc -0.67, resid-z -0.10 [quiet], 1d -0.53%, 1y-pct=99
- **Mechanism**: The recent move in dyn_jiofin_bo is driven by its high z20 level of 2.94, indicating a significant deviation from its historical mean. This move is unexplained by factor exposures, as evidenced by its high resid_z of 2.39. The correlated instruments, such as india_vix and dyn_indianb_ns, have not moved in tandem, suggesting a potential transmission opportunity. The valid channels, including gold_silver_comove and metal_copper_channel, may influence the Indian metal equities, while the vix_equity_inverse channel indicates a potential vol spike -> equity drawdown scenario.
- **Gap**: No gap: The move in dyn_jiofin_bo is largely priced in, given its high z20 level and significant resid_z, indicating that the market has already accounted for the underlying factors driving the move.
- **India take**: The Indian instrument dyn_muthootfin_ns, which is correlated with nifty_midcap_100, has already reacted with a z20 of -2.65. Other transmission candidates, such as dyn_bharatcoal_ns and nifty_metal, have also reacted, suggesting that the move has been partially transmitted to the Indian market.
- Watch next: dyn_jiofin_bo (up) — already moved; high z20 level and resid_z
- **India receivers**: dyn_muthootfin_ns (rho 0.688, z -2.65); dyn_bharatcoal_ns (rho 0.628, z -1.28); dyn_indianb_ns (rho 0.62, z 0.61); dyn_indusindbk_bo (rho 0.611, z 0.24)
- Source: Sensex today | Stock Market Live: Sensex flat, Nifty down 200 pts to 24,560 as CAS correction weighs; RBI MPC meet outcome in focus — BusinessLine Mkts, 2026-08-04. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-4th-august-2026/article71301258.ece
- Source: Textile stock under  ₹100 hits 10% upper circuit despite muted trend on Dalal Street — Mint Markets, 2026-08-04. https://www.livemint.com/market/stock-market-news/textile-stock-under-100-aastha-spintex-hits-10-upper-circuit-despite-muted-trend-on-dalal-street-11785818344958.html
- Source: Sensex rises over 100 points, but Nifty50 slips near 24,600. What’s driving the divergence? — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/stocks/news/sensex-rises-over-100-points-but-nifty50-slips-near-24600-heres-why/articleshow/132845868.cms
- Historical analogues: 2025-07-17 (d=0.69), 2024-11-07 (d=0.98), 2025-08-13 (d=1.26)

### [RED 5.12] dyn_thangamayl_ns ↓
- dyn_thangamayl_ns [EQUITIES]: last 4717.50, z20 -3.12, zc -0.53, resid-z -2.34 [unexplained], 1d -4.99%, |z20|=3.12
- **Mechanism**: dyn_thangamayl_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho -0.374 via dyn_thangamayl_ns, z 2.94, reacted)
- **India receivers**: dyn_jiofin_bo (rho -0.374, z 2.94)
- Source: Thangamayil share selloff continues: Stock drops 5% despite Rs 344 crore sales in first 3 days of August — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/stocks/news/thangamayil-share-selloff-continues-stock-drops-5-despite-rs-344-crore-sales-in-first-3-days-of-august/articleshow/132847383.cms
- Source: Thangamayil Jewellery shares crash 32% in a week. What should investors do? — ET Markets, 2026-08-03. https://economictimes.indiatimes.com/markets/stocks/news/thangamayil-jewellery-shares-crash-32-in-a-week-what-should-investors-do/articleshow/132821479.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-29 (d=0.01), 2026-06-11 (d=0.01)

### [AMBER 4.81] fx · 2 series ↑
- usd_mxn [FX]: last 17.31, z20 -1.98, zc 0.04, resid-z -1.35 [quiet], 1d 0.02%, |z20|=1.98
- eur_usd [FX]: last 1.15, z20 1.86, zc -0.75, resid-z 1.62 [unexplained], 1d -0.29%, |z20|=1.86
- **Mechanism**: fx · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.523 via usd_mxn, z -2.65, reacted)
- Watch next: usd_brl (co-move) — not yet - watch; rho 0.771 vs usd_mxn, historically leads by 3d
- Watch next: gbp_usd (inverse) — not yet - watch; rho -0.627 vs usd_mxn, historically leads by 5d
- **India receivers**: dyn_muthootfin_ns (rho -0.523, z -2.65)
- Source: Global Market: Euro zone bond yields decline as falling oil prices boost market sentiment — ET Markets, 2026-08-03. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-bond-yields-decline-as-falling-oil-prices-boost-market-sentiment/articleshow/132826355.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-05 (d=0.17), 2025-09-05 (d=0.21)

## Watchlist (below surfacing floor)
dyn_muthootfin_ns ↓ (4.65), dyn_coin ↓ (4.63), dyn_chkp ↓ (4.59), dyn_aapl ↓ (4.15), asx_200 ↑ (3.45), dyn_tech ↑ (3.39), dyn_lth ↑ (3.07), nifty_metal ↑ (3.04), ust_2s10s ↑ (2.86), dyn_icicigi_bo ↓ (2.65), dyn_cupid_ns ↑ (2.28), dyn_301077_sz ↓ (2.26)

## India macro
- nifty_50: 24508.9492 (1d -1.07%, z20 1.60, flag amber)
- nifty_midcap_100: 63330.4492 (1d -0.53%, z20 1.46, flag amber)
- usd_inr: 95.3550 (1d -0.05%, z20 -1.44, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5840 (1d 0.55%, z20 -0.38, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI MPC decision T-3d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 67.5 — "Stock recommendations for 4 August from MarketSmith India"
- COALINDIA.NS (COAL INDIA LTD) score 65.6 — "Stock recommendations for 4 August from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 64.4 — "Stock recommendations for 4 August from MarketSmith India"
- INDIANB.NS (INDIAN BANK) score 55.4 — "From Gift Nifty to RBI MPC meeting, crude oil prices: 8 key things that changed for Indian"
- COIN (Coinbase Global, Inc.) score 46.5 — "Big Oil Warns Global Fuel Stocks Are Running Dangerously Low"
- TECHM.NS (TECH MAHINDRA LIMITED) score 41.1 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Current Price and Market Performan"
- BAC (Bank of America Corporation) score 39.7 — "Kotak Bank Share Price Live Updates: Kotak Bank's Price Movement Today"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.4 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Current Price and Market Performan"
- HDB (HDFC Bank Limited) score 38.8 — "Kotak Bank Share Price Live Updates: Kotak Bank's Price Movement Today"
- IDBI.NS (IDBI BANK LIMITED) score 37.0 — "Kotak Bank Share Price Live Updates: Kotak Bank's Price Movement Today"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 37.0 — "Kotak Bank Share Price Live Updates: Kotak Bank's Price Movement Today"
- OHI (Omega Healthcare Investors, In) score 35.4 — "Oil drops, stocks gain amid Iran peace hopes; yen firms as investors watch for further int"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 34.8 — "Kotak Bank Share Price Live Updates: Kotak Bank's Price Movement Today"
- TECH (Bio-Techne Corp) score 32.9 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Current Price and Market Performan"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 32.1 — "Ather Energy shares zoom 18% after Q1 results. Why is it Nomura's top 2-wheeler pick?"
- CHKP (Check Point Software Technolog) score 30.9 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 4"
- LTH (Life Time Group Holdings, Inc.) score 24.1 — "Russia Is Running Out of Soldiers, Oil, and Time"
- BOND (PIMCO Active Bond Exchange-Tra) score 21.4 — "India bonds pause before RBI policy, debt supply"
- 301077.SZ (CHINASTARS) score 17.2 — "KMT accuses Taiwan’s government of failing to uphold South China Sea claims"
- MS (Morgan Stanley) score 11.7 — "U.S. TIGHTENS ROBOT IMPORT RULES The FCC will restrict imports of certain foreign-made adv"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.2 — "Tata Steel Share Price Live Updates: Tata Steel's Price Movement Today"
- AMZN (Amazon.com, Inc.) score 11.0 — "Wall Street climbs as crude oil prices plunge, Amazon jumps 5.3%"
- JIOFIN.BO (Jio Financial Services Limited) score 10.5 — "Power Grid Share Price Live Updates: Power Grid's Financial Snapshot"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.1 — "Delayed justice in market violation cases makes a pittance of penalties"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 9.7 — "Power Grid Share Price Live Updates: Power Grid's Financial Snapshot"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 9.1 — "Coal India Share Price Live Updates: Coal India  Market Performance"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.7 — "Adani Total Gas raises CNG prices by ₹4 per kg amid rising LNG costs"
- MSFT (Microsoft Corporation) score 8.5 — "SHARES OF US HYPERSCALERS CLIMB • META RISES 6.1% • MICROSOFT JUMPS 4.7% • AMAZON GAINS 4."
- AAPL (Apple Inc.) score 7.7 — "Apple suffers worst rout since 2025 on disappointing outlook"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.2 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Marks New 52-Week High"
- VT (Vanguard Total World Stock Ind) score 6.3 — "Traders in the world’s most important financial market are bracing for a wild stretch ahea"
- META (Meta) score 6.1 — "META INVITED TO WHITE HOUSE TUESDAY TO DISCUSS AI SAFETY TESTING BY U.S. GOVERNMENT - COMP"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.9 — "SBI, HDFC Bank, to ICICI Bank, Axis Bank: Bank stocks fall ahead of RBI monetary policy de"
- PCJEWELLER.NS (PC JEWELLER LTD) score 5.9 — "Q1 Results Today Live: Bharti Airtel, ONGC, Pidilite, Marico, Nykaa, Bharti Hexacom, NHPC,"
- GS (Goldman Sachs Group, Inc. (The) score 5.3 — "GOLDMAN REFRESHES U.S. CONVICTION LIST Goldman Sachs added Applied Materials ( $AMAT), Del"
- INFY (Infosys Limited) score 5.3 — "Infosys Share Price Live Updates: Infosys market movement today"
- PLTR (Palantir Technologies Inc.) score 3.8 — "Palantir’s stock climbs after earnings, as AI drives turbocharged growth"
- THANGAMAYL.NS (THANGAMAYIL JEWELLERY LTD) score 3.7 — "Thangamayil share selloff continues: Stock drops 5% despite Rs 344 crore sales in first 3 "
- NVDA (NVIDIA Corporation) score 3.4 — "Did China build a top-tier AI model by itself? A new report suggests Nvidia chips played a"
- CUPID.NS (CUPID LIMITED) score 0.6 — "Cupid increases investment by $5 million in GII’s Healthcare-focused platform"

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