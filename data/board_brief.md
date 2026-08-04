# Transmission Layer — board brief · 2026-08-04 10:50Z

data as of **2026-08-04** · 98 series · 20 red / 28 amber · 8 events surfaced (23 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.37, 1d in regime; vol-pct 0.406, breadth-off 0.333, Markov P(high-vol) 0.07)
- [INVERTED] **safe_haven_gold** — corr20 -0.47, corr60 -0.45, contra nifty_50 corr20=0.19, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.82, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.34, corr60 0.32, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.16, corr60 -0.04, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.84, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.08, corr60 -0.03, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.18, corr60 -0.25, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.29, corr60 0.21, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **6 of 90** scanned series survive multiplicity control (effective p ≤ 0.0010380708664139426)
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.484, β 0.2629, p 0.0); driver zc 1.58 → expected 0.393%. Type hit-rate 0.821 (n=2850).
- **SETUP** dyn_amzn → taiwan_weighted: leads 1d (ccf 0.363, β 0.2869, p 0.0); driver zc 6.66 → expected 4.395%. Type hit-rate 0.821 (n=2850).
- **SETUP** dyn_coin → asx_200: leads 1d (ccf 0.322, β 0.05, p 0.0); driver zc -2.26 → expected -0.529%. Type hit-rate 0.821 (n=2850).
- **SETUP** dyn_coin → aud_usd: leads 1d (ccf 0.264, β 0.0328, p 0.00023); driver zc -2.26 → expected -0.348%. Type hit-rate 0.821 (n=2850).
- Track record · residual_reversion: hit-rate **0.495** (n=1144) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.821** (n=2850) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.02] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.27, z20 2.89, zc 1.53, resid-z 1.91 [unexplained], 1d 1.15%, |z20|=2.89; 1y-pct=100
- ust_10y [RATES]: last 4.75, z20 2.37, zc 1.58, resid-z 2.16 [unexplained], 1d 1.50%, |z20|=2.37; 1y-pct=100
- tips_10y_real [RATES]: last 2.47, z20 2.09, zc 1.57, resid-z 2.22 [unexplained], 1d 2.49%, 1d move +6.0bps ≥ 5bps; |z20|=2.09; 1y-pct=100
- dyn_bond [EQUITIES]: last 90.32, z20 -2.02, zc -1.14, resid-z 0.50 [quiet], 1d -0.19%, |z20|=2.02; 1y-pct=0
- ust_2y [RATES]: last 4.28, z20 0.86, zc 0.93, resid-z 1.54 [unexplained], 1d 1.18%, 1y-pct=98
- **Mechanism**: The recent move in US Treasury yields, particularly the 10-year and 30-year yields, is driven by a decline in inflation concerns due to renewed discussions with Iran, leading to a decrease in oil prices. This has caused a drop in US Treasury yields, which in turn may influence Indian government bond yields. However, the Indian bond market is currently cautious ahead of the RBI's monetary policy decision and a large state bond auction.
- **Gap**: No gap: The move in US Treasury yields is largely priced in, given the significant z20 levels and the fact that the resid_z values, although unexplained, are not unusually high, suggesting that the market has already adjusted to the new information.
- **India take**: The Indian 10-year government bond yield may react to the decline in US Treasury yields, potentially leading to a decrease in Indian bond yields. However, the outcome of the RBI's monetary policy decision and the large state bond auction will be key factors influencing the Indian bond market.
- Watch next: nifty_50 (down) — not yet - watch; Risk-off sentiment may lead to a decline in Indian equities
- Source: Indian bond yields trades flat ahead of RBI MPC meeting outcome. Experts decode the outlook — Mint Markets, 2026-08-04. https://www.livemint.com/market/stock-market-news/indian-bond-yields-trades-flat-ahead-of-rbi-mpc-meeting-outcome-experts-decode-the-outlook-11785831046953.html
- Source: Global Market: Japan's 10-year bond yield climbs after weak auction signals soft demand — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-10-year-bond-yield-climbs-after-weak-auction-signals-soft-demand/articleshow/132852095.cms
- Source: US 10-year yield falls from 18-month high on Iran peace talk hopes — ET Markets, 2026-08-03. https://economictimes.indiatimes.com/markets/bonds/us-10-year-yield-falls-from-18-month-high-on-iran-peace-talk-hopes/articleshow/132831577.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 8.06] cross-asset · 9 series ↑
- stoxx_50 [INDICES]: last 6460.73, z20 3.42, zc 0.47, resid-z -0.13 [quiet], 1d 0.45%, |z20|=3.42; 1y-pct=100
- dax [INDICES]: last 26121.24, z20 2.89, zc 0.38, resid-z -0.25 [quiet], 1d 0.32%, |z20|=2.89; 1y-pct=100
- cac_40 [INDICES]: last 8617.50, z20 2.77, zc -0.12, resid-z 0.18 [quiet], 1d -0.10%, |z20|=2.77; 1y-pct=99
- comex_copper [COMMODITIES]: last 6.62, z20 2.69, zc 0.55, resid-z -0.83 [quiet], 1d 1.24%, |z20|=2.69; 1y-pct=99; co-occur[metal_copper] same-direction (channel VALID)
- dow_jones [INDICES]: last 53184.43, z20 2.23, zc 0.47, resid-z 0.22 [quiet], 1d 1.33%, |z20|=2.23; 1y-pct=100
- sp500 [INDICES]: last 7599.97, z20 1.85, zc 0.67, resid-z 0.82 [quiet], 1d 1.47%, |z20|=1.85; 1y-pct=99
- ftse_100 [INDICES]: last 10889.22, z20 1.51, zc 0.64, resid-z -0.48 [quiet], 1d 0.36%, |z20|=1.51; 1y-pct=98
- dyn_vt [EQUITIES]: last 157.60, z20 1.44, zc 0.23, resid-z -2.02 [unexplained], 1d 1.11%, 1y-pct=95
- gold_silver_ratio [DERIVED]: last 69.69, z20 -0.10, zc n/a, resid-z n/a [quiet], 1d -1.00%, GSR<75 (extreme low)
- **Mechanism**: The recent surge in global equity markets, led by the Dow Jones and S&P 500, is driven by easing oil prices and strong tech earnings, which has lifted investor sentiment. This move is priced, with most indices showing a high r2 value, indicating that the move is largely explained by factor exposures. However, the dyn_vt equities show an unexplained move, which may be worth watching.
- **Gap**: No gap: the recent move in global equity markets is largely priced, with most indices showing a high r2 value and small resid_z values, indicating that the move is explained by factor exposures.
- **India take**: The Indian market, as represented by the nifty_50 and nifty_midcap_100, has already reacted to the global move, with both indices showing a high correlation with their respective global counterparts. The nifty_metal index has also reacted, driven by the co-movement of monetary metals.
- Watch next: nifty_50 (up) — already moved; high correlation with cac_40
- **India receivers**: nifty_50 (rho 0.546, z 2.07); nifty_midcap_100 (rho 0.528, z 1.75); nifty_metal (rho -0.43, z 3.69)
- Source: Explained: Why Dow Jones closed at lifetime high despite caution over AI frenzy — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/news/explained-why-dow-jones-closed-at-lifetime-high-despite-caution-over-ai-frenzy/articleshow/132850484.cms
- Source: SpaceX heads into first earnings report. Here are 5 things Wall Street is watching — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/news/spacex-heads-into-first-earnings-report-here-are-5-things-wall-street-is-watching/slideshow/132849006.cms
- Source: Traders in the world’s most important financial market are bracing for a wild stretch ahead — MarketWatch Top, 2026-08-03. https://www.marketwatch.com/story/traders-in-the-worlds-most-important-financial-market-are-bracing-for-a-wild-stretch-ahead-4a1507dc?mod=mw_rss_topstories
- Historical analogues: 2024-10-10 (d=0.85), 2024-10-03 (d=1.01), 2024-11-07 (d=1.05)

### [RED 7.33] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1454.80, z20 5.33, zc 4.61, resid-z 4.76 [unexplained], 1d 14.31%, |z20|=5.33; 1y-pct=100
- **Mechanism**: The surge in Ather Energy's stock price is driven by the company's improving operating performance, specifically the narrowing of its operating losses and the achievement of Ebitda profit, which has ignited investor interest and led to a sharp increase in the stock price. This move is propagated through the metal_copper_channel, where global copper leads Indian metal equities, and the vix_equity_inverse channel, where a vol spike leads to an equity drawdown. However, the resid_z of 4.76 indicates that a significant portion of the move is unexplained by factor exposures, suggesting that the stock's rally may be overextended.
- **Gap**: No gap: the stock's price move is largely priced in, given the significant improvement in the company's operating performance and the bullish views of global brokerages
- **India take**: The Indian instrument that expresses this move is Ather Energy Ltd, which has already reacted with a sharp increase in its stock price. Other Indian metal equities, such as those in the Nifty Metal index, may also be affected by this move.
- Watch next: nifty_50 (up) — not yet - watch; Ather Energy's rally may have a positive impact on the broader Indian market
- Source: Ather Energy's tapering losses put stock in fast lane, but is the rally justified? — Mint Markets, 2026-08-04. https://www.livemint.com/market/mark-to-market/ather-energy-electric-vehicles-ev-q1fy27-ebitda-operating-losses-ev-sales-hero-motocorp-11785824423599.html
- Source: Multibagger stock Ather Energy share price soars 18% to record high post Q1 FY27 results: Should you buy? — Mint Markets, 2026-08-04. https://www.livemint.com/market/stock-market-news/multibagger-stock-ather-energy-share-price-soars-18-to-record-high-post-q1-fy27-results-should-you-buy-11785824415092.html
- Source: Ather Energy share price target goes up to Rs 1,714. What are CLSA, Nomura, and HSBC saying? — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/stocks/news/ather-energy-share-price-target-goes-up-to-rs-1714-what-are-clsa-nomura-and-hsbc-saying/articleshow/132848638.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [RED 6.88] cross-asset · 2 series ↑
- dyn_amzn [EQUITIES]: last 284.02, z20 4.05, zc 6.66, resid-z 9.76 [unexplained], 1d 4.58%, |z20|=4.05; 1y-pct=100
- usd_jpy [FX]: last 157.80, z20 -3.32, zc 0.18, resid-z 0.22 [quiet], 1d 0.14%, |z20|=3.32
- **Mechanism**: The recent surge in Amazon's market value, driven by strong earnings and increased investor confidence in artificial intelligence, has led to a rise in dyn_amzn. This move is unexplained by factor exposures, with a high resid_z of 9.76. The coordinated US-Japan yen-buying intervention has also triggered a sharp rebound in the Japanese currency, resulting in a quiet move in usd_jpy with a low resid_z of 0.22, indicating that the move is largely priced in.
- **Gap**: No gap: the move in dyn_amzn is largely unexplained by factor exposures, but the resid_z for usd_jpy is low, indicating that the move is priced in.
- **India take**: The Indian instrument dyn_muthootfin_ns has reacted to the move in usd_jpy, while dyn_cartrade_ns and dyn_thangamayl_ns have not yet reacted to the move in dyn_amzn. The transmission candidates suggest that the Indian market may follow the lead of the US market, particularly in response to the yen intervention.
- Watch next: taiwan_weighted (down) — not yet - watch; historically leads usd_jpy by 1d
- **India receivers**: dyn_muthootfin_ns (rho -0.512, z -2.93); dyn_cartrade_ns (rho -0.37, z 0.18); dyn_thangamayl_ns (rho -0.368, z -3.12)
- Source: What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/us-markets-academy/what-bubble-amazon-enters-3-trillion-market-cap-club-ceo-highlights-striking-ai-demand/articleshow/132854970.cms
- Source: Global Market: US-Japan coordinated yen intervention raises pressure on bears, but BOJ policy holds the key — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-us-japan-coordinated-yen-intervention-raises-pressure-on-bears-but-boj-policy-holds-the-key/articleshow/132850399.cms
- Source: Yen surges to three-month peak, dollar pares losses after intervention — Mint Markets, 2026-08-03. https://www.livemint.com/market/yen-surges-to-three-month-peak-dollar-pares-losses-after-intervention-11785792603276.html
- Historical analogues: 2024-10-16 (d=0.15), 2024-11-21 (d=0.23), 2026-03-31 (d=0.24)

### [RED 6.39] cross-asset · 3 series ↑
- dyn_jiofin_bo [EQUITIES]: last 264.55, z20 3.07, zc 0.43, resid-z 1.39 [quiet], 1d 0.97%, |z20|=3.07
- nifty_50 [INDICES]: last 24614.90, z20 2.07, zc -0.88, resid-z 0.42 [quiet], 1d -0.64%, |z20|=2.07
- nifty_midcap_100 [INDICES]: last 63484.05, z20 1.75, zc -0.36, resid-z 0.38 [quiet], 1d -0.29%, |z20|=1.75; 1y-pct=99
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-17 (z-distance 0.69).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.692 via nifty_midcap_100, z -2.93, reacted); dyn_bharatcoal_ns (rho 0.631 via nifty_midcap_100, z -1.19, reacted); dyn_indianb_ns (rho 0.62 via nifty_midcap_100, z 0.71, quiet); dyn_indusindbk_bo (rho 0.614 via nifty_midcap_100, z 0.24, quiet); nifty_metal (rho 0.582 via nifty_midcap_100, z 3.69, reacted)
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.574 vs nifty_50, historically leads by 3d
- Watch next: dyn_indianb_ns (co-move) — not yet - watch; rho 0.545 vs dyn_jiofin_bo, historically leads by 1d
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.566 vs nifty_50
- Watch next: dyn_indusindbk_bo (co-move) — not yet - watch; rho 0.532 vs dyn_jiofin_bo
- **India receivers**: dyn_muthootfin_ns (rho 0.692, z -2.93); dyn_bharatcoal_ns (rho 0.631, z -1.19); dyn_indianb_ns (rho 0.62, z 0.71); dyn_indusindbk_bo (rho 0.614, z 0.24)
- Source: Sensex today | Stock Market Highlights: Markets end in the red; Sensex drops 210 points, Nifty slips 159 — BusinessLine Mkts, 2026-08-04. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-4th-august-2026/article71301258.ece
- Source: Sensex falls 210 points, Nifty closes below 24,650 as market snaps 4-day gaining streak — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/stocks/news/sensex-falls-210-points-nifty-closes-below-24650-as-market-snaps-4-day-gaining-streak/articleshow/132856959.cms
- Source: What is the Nifty-Gold ratio signalling now? Could a new bull run in Indian equities be next? — Mint Markets, 2026-08-04. https://www.livemint.com/market/stock-market-news/what-is-the-nifty-gold-ratio-signalling-now-could-a-new-bull-run-in-indian-equities-be-next-gold-price-outlook-11785836014645.html
- Historical analogues: 2025-07-17 (d=0.69), 2024-11-07 (d=0.98), 2025-08-13 (d=1.26)

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

### [AMBER 5.55] fx · 3 series ↑
- usd_mxn [FX]: last 17.29, z20 -2.23, zc -0.19, resid-z -0.24 [quiet], 1d -0.08%, |z20|=2.23
- eur_usd [FX]: last 1.15, z20 2.10, zc -0.52, resid-z -0.43 [quiet], 1d -0.20%, |z20|=2.10
- aud_usd [FX]: last 0.70, z20 1.86, zc -0.16, resid-z -0.10 [quiet], 1d -0.12%, |z20|=1.86
- **Mechanism**: fx · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.521 via usd_mxn, z -2.93, reacted)
- Watch next: usd_brl (co-move) — not yet - watch; rho 0.771 vs usd_mxn, historically leads by 3d
- Watch next: gbp_usd (inverse) — not yet - watch; rho -0.626 vs usd_mxn, historically leads by 5d
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.518 vs aud_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.521, z -2.93)
- Source: Global Market: Euro zone bond yields decline as falling oil prices boost market sentiment — ET Markets, 2026-08-03. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-bond-yields-decline-as-falling-oil-prices-boost-market-sentiment/articleshow/132826355.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-02 (d=0.26), 2025-08-15 (d=0.26)

### [AMBER 5.16] wti ↑
- wti [COMMODITIES]: last 81.77, z20 0.16, zc 0.63, resid-z 0.65 [quiet], 1d 2.14%, 1-session move +2.14% ≥ 1.5%
- **Mechanism**: wti ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.502 via wti, z 1.75, reacted); midcap_largecap_ratio (rho -0.397 via wti, z -0.68, quiet)
- Watch next: brent (co-move) — not yet - watch; rho 0.968 vs wti
- **India receivers**: nifty_midcap_100 (rho -0.502, z 1.75); midcap_largecap_ratio (rho -0.397, z -0.68)
- Source: Oil prices rise after vessel reports being hit in Strait of Hormuz — MarketWatch Top, 2026-08-04. https://www.marketwatch.com/story/oil-prices-rise-after-vessel-reports-being-hit-in-strait-of-hormuz-db6ce867?mod=mw_rss_topstories
- Source: BP Earnings Surge to $5.7 Billion on Oil Price and Refining Boom — OilPrice, 2026-08-04. https://oilprice.com/Latest-Energy-News/World-News/BP-Earnings-Surge-to-57-Billion-on-Oil-Price-and-Refining-Boom.html
- Source: Saudi Aramco’s Adjusted Profit Jumps 33% as Oil Prices Surge — OilPrice, 2026-08-04. https://oilprice.com/Latest-Energy-News/World-News/Saudi-Aramcos-Adjusted-Profit-Jumps-33-as-Oil-Prices-Surge.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

## Watchlist (below surfacing floor)
dyn_thangamayl_ns ↓ (5.12), brent ↓ (5.11), dyn_muthootfin_ns ↓ (4.93), dyn_coin ↓ (4.63), dyn_chkp ↓ (4.59), dyn_aapl ↓ (4.15), nifty_metal ↑ (3.69), asx_200 ↑ (3.45), dyn_bac ↑ (3.45), dyn_tech ↑ (3.39), dyn_lth ↑ (3.07), ust_2s10s ↑ (2.86)

## India macro
- nifty_50: 24614.9004 (1d -0.64%, z20 2.07, flag amber)
- nifty_midcap_100: 63484.0508 (1d -0.29%, z20 1.75, flag amber)
- usd_inr: 95.3775 (1d -0.03%, z20 -1.39, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5791 (1d 0.36%, z20 -0.68, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI MPC decision T-3d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 68.9 — "Indian bond yields trades flat ahead of RBI MPC meeting outcome. Experts decode the outloo"
- COALINDIA.NS (COAL INDIA LTD) score 67.0 — "Indian bond yields trades flat ahead of RBI MPC meeting outcome. Experts decode the outloo"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 65.9 — "Indian bond yields trades flat ahead of RBI MPC meeting outcome. Experts decode the outloo"
- INDIANB.NS (INDIAN BANK) score 57.2 — "Indian bond yields trades flat ahead of RBI MPC meeting outcome. Experts decode the outloo"
- COIN (Coinbase Global, Inc.) score 52.7 — "Global Market: China stocks rebound on AI, chip rally; Hong Kong shares slip"
- TECHM.NS (TECH MAHINDRA LIMITED) score 42.5 — "Epack Prefab Technologies shares rally 10% after Q1 revenue jumps 24%"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 40.8 — "Epack Prefab Technologies shares rally 10% after Q1 revenue jumps 24%"
- BAC (Bank of America Corporation) score 40.2 — "ICICI Securities initiates coverage on 7 PSU banks with positive valuations"
- HDB (HDFC Bank Limited) score 39.3 — "ICICI Securities initiates coverage on 7 PSU banks with positive valuations"
- IDBI.NS (IDBI BANK LIMITED) score 37.5 — "ICICI Securities initiates coverage on 7 PSU banks with positive valuations"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 37.5 — "ICICI Securities initiates coverage on 7 PSU banks with positive valuations"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 35.4 — "ICICI Securities initiates coverage on 7 PSU banks with positive valuations"
- OHI (Omega Healthcare Investors, In) score 35.0 — "LIC OFS: Non-retail portion fully subscribed on Day 1. Here’s what investors should know"
- TECH (Bio-Techne Corp) score 34.5 — "Epack Prefab Technologies shares rally 10% after Q1 revenue jumps 24%"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 33.8 — "Ather Energy's tapering losses put stock in fast lane, but is the rally justified?"
- CHKP (Check Point Software Technolog) score 31.7 — "Dhaval Packaging IPO allotment to be finalised today. Here's GMP, how to check status onli"
- LTH (Life Time Group Holdings, Inc.) score 25.1 — "Explained: Why Dow Jones closed at lifetime high despite caution over AI frenzy"
- BOND (PIMCO Active Bond Exchange-Tra) score 22.6 — "Global Market: Japan's 10-year bond yield climbs after weak auction signals soft demand"
- 301077.SZ (CHINASTARS) score 17.5 — "Global Market: China stocks rebound on AI, chip rally; Hong Kong shares slip"
- JUSTDIAL.BO (JUST DIAL LTD.) score 12.7 — "Ather Energy's tapering losses put stock in fast lane, but is the rally justified?"
- AMZN (Amazon.com, Inc.) score 11.6 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- MS (Morgan Stanley) score 11.2 — "U.S. TIGHTENS ROBOT IMPORT RULES The FCC will restrict imports of certain foreign-made adv"
- JIOFIN.BO (Jio Financial Services Limited) score 11.1 — "Jio Financial Services Share Price Live Updates: Jio Financial Services sees a slight dip "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.7 — "Tata Steel Share Price Live Updates: Tata Steel's Price Movement Today"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.3 — "Adani Ent Share Price Live Updates: Adani Ent. News"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 10.3 — "Jio Financial Services Share Price Live Updates: Jio Financial Services sees a slight dip "
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 8.8 — "Coal India Share Price Live Updates: Coal India  Market Performance"
- MSFT (Microsoft Corporation) score 8.2 — "SHARES OF US HYPERSCALERS CLIMB • META RISES 6.1% • MICROSOFT JUMPS 4.7% • AMAZON GAINS 4."
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.9 — "Maharatna PSU stock Power Finance Corporation to declare Q1 results 2026, interim dividend"
- PCJEWELLER.NS (PC JEWELLER LTD) score 7.7 — "Top Gainers & Losers on 4 August: LIC, Dabur India, Urban Company, DLF, PB Fintech, Kalyan"
- AAPL (Apple Inc.) score 7.4 — "Apple suffers worst rout since 2025 on disappointing outlook"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.7 — "ICICI Securities initiates coverage on 7 PSU banks with positive valuations"
- GS (Goldman Sachs Group, Inc. (The) score 6.1 — "Global Market: Goldman Sachs sees Brent crude trading at $80-$90 until Iran conflict outlo"
- VT (Vanguard Total World Stock Ind) score 6.0 — "Traders in the world’s most important financial market are bracing for a wild stretch ahea"
- META (Meta) score 5.9 — "META INVITED TO WHITE HOUSE TUESDAY TO DISCUSS AI SAFETY TESTING BY U.S. GOVERNMENT - COMP"
- INFY (Infosys Limited) score 5.1 — "Infosys Share Price Live Updates: Infosys market movement today"
- PLTR (Palantir Technologies Inc.) score 3.6 — "Palantir’s stock climbs after earnings, as AI drives turbocharged growth"
- THANGAMAYL.NS (THANGAMAYIL JEWELLERY LTD) score 3.6 — "Thangamayil share selloff continues: Stock drops 5% despite Rs 344 crore sales in first 3 "
- NVDA (NVIDIA Corporation) score 3.3 — "Did China build a top-tier AI model by itself? A new report suggests Nvidia chips played a"
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