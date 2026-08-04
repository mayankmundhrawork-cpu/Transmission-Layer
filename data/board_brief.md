# Transmission Layer — board brief · 2026-08-04 14:38Z

data as of **2026-08-04** · 98 series · 22 red / 29 amber · 8 events surfaced (23 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.321, 2d in regime; vol-pct 0.406, breadth-off 0.235, Markov P(high-vol) 0.043)
- [INVERTED] **safe_haven_gold** — corr20 -0.41, corr60 -0.43, contra nifty_50 corr20=0.09, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.93, corr60 0.82, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.36, corr60 0.33, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.18, corr60 -0.04, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.93, corr60 -0.84, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.08, corr60 -0.03, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.18, corr60 -0.25, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.28, corr60 0.2, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **5 of 90** scanned series survive multiplicity control (effective p ≤ 0.0020015649532281188)
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.484, β 0.2629, p 0.0); driver zc 1.58 → expected 0.393%. Type hit-rate 0.821 (n=2850).
- Track record · residual_reversion: hit-rate **0.495** (n=1144) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.821** (n=2850) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.02] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.27, z20 2.89, zc 1.53, resid-z 1.91 [unexplained], 1d 1.15%, |z20|=2.89; 1y-pct=100
- ust_10y [RATES]: last 4.75, z20 2.37, zc 1.58, resid-z 2.16 [unexplained], 1d 1.50%, |z20|=2.37; 1y-pct=100
- tips_10y_real [RATES]: last 2.47, z20 2.09, zc 1.57, resid-z 2.22 [unexplained], 1d 2.49%, 1d move +6.0bps ≥ 5bps; |z20|=2.09; 1y-pct=100
- ust_2y [RATES]: last 4.28, z20 0.86, zc 0.93, resid-z 1.54 [unexplained], 1d 1.18%, 1y-pct=98
- dyn_bond [EQUITIES]: last 90.71, z20 -0.78, zc 1.52, resid-z 0.50 [priced], 1d 0.44%, 1y-pct=2
- **Mechanism**: The recent move in US Treasury yields, particularly the 10-year and 30-year yields, is driven by a decline in inflation concerns due to renewed discussions with Iran and a subsequent drop in oil prices. This move is also reflected in the unexplained component of the yields, as indicated by the resid_z values. The valid channel of vix_equity_inverse suggests that the decline in US Treasury yields could lead to a decrease in volatility, which in turn could support equity markets.
- **Gap**: No gap: The move in US Treasury yields is largely priced in, as indicated by the resid_z values, which are not exceptionally high given the magnitude of the move.
- **India take**: The Indian 10-year government bond yield, as expressed through the 6.94% 2036 government bond, may react to the decline in US Treasury yields, potentially leading to a decrease in Indian bond yields. However, the RBI's monetary policy decision and the large state bond auction may influence the market's reaction.
- Watch next: nifty_50 (up) — not yet - watch; US Treasury yield decline could lead to decreased volatility and support equity markets
- Source: Indian bond yields trades flat ahead of RBI MPC meeting outcome. Experts decode the outlook — Mint Markets, 2026-08-04. https://www.livemint.com/market/stock-market-news/indian-bond-yields-trades-flat-ahead-of-rbi-mpc-meeting-outcome-experts-decode-the-outlook-11785831046953.html
- Source: Global Market: Japan's 10-year bond yield climbs after weak auction signals soft demand — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-10-year-bond-yield-climbs-after-weak-auction-signals-soft-demand/articleshow/132852095.cms
- Source: US 10-year yield falls from 18-month high on Iran peace talk hopes — ET Markets, 2026-08-03. https://economictimes.indiatimes.com/markets/bonds/us-10-year-yield-falls-from-18-month-high-on-iran-peace-talk-hopes/articleshow/132831577.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 8.74] cross-asset · 11 series ↑
- stoxx_50 [INDICES]: last 6480.20, z20 3.86, zc 0.87, resid-z -0.42 [quiet], 1d 0.84%, |z20|=3.86; 1y-pct=100
- dow_jones [INDICES]: last 53827.45, z20 3.80, zc 1.19, resid-z 0.52 [quiet], 1d 1.22%, |z20|=3.80; 1y-pct=100
- cac_40 [INDICES]: last 8645.60, z20 3.19, zc 0.44, resid-z -0.85 [quiet], 1d 0.37%, |z20|=3.19; 1y-pct=100
- dax [INDICES]: last 26189.67, z20 3.15, zc 0.87, resid-z -0.28 [quiet], 1d 0.72%, |z20|=3.15; 1y-pct=100
- comex_copper [COMMODITIES]: last 6.66, z20 3.09, zc 0.99, resid-z 0.33 [quiet], 1d 2.24%, |z20|=3.09; 1y-pct=100; co-occur[metal_copper] same-direction (channel VALID)
- sp500 [INDICES]: last 7676.19, z20 2.81, zc 1.00, resid-z 0.82 [quiet], 1d 1.00%, |z20|=2.81; 1y-pct=100
- dyn_vt [EQUITIES]: last 159.24, z20 2.69, zc 0.99, resid-z -2.02 [unexplained], 1d 1.03%, |z20|=2.69; 1y-pct=99
- russell_2000 [INDICES]: last 3006.51, z20 2.23, zc 0.66, resid-z -0.58 [quiet], 1d 0.82%, |z20|=2.23; 1y-pct=97
- comex_gold [COMMODITIES]: last 4143.10, z20 1.82, zc 1.94, resid-z -1.68 [unexplained], 1d 2.71%, |z20|=1.82
- ftse_100 [INDICES]: last 10892.39, z20 1.52, zc 0.57, resid-z -0.15 [quiet], 1d 0.32%, |z20|=1.52; 1y-pct=98
- gold_silver_ratio [DERIVED]: last 69.23, z20 -0.59, zc n/a, resid-z n/a [quiet], 1d -1.03%, GSR<75 (extreme low)
- **Mechanism**: The recent surge in US stocks, led by the S&P 500 and Dow Jones, is driven by strong AI-linked earnings and hopes for a Middle East peace deal. This risk-on sentiment is also reflected in the increase in copper prices, which have reached a two-month high due to decreasing inventories. The VALID metal_copper_channel suggests that this move in copper prices may transmit to Indian metal equities.
- **Gap**: No gap: The recent move in US stocks and copper prices is largely priced in, with the resid_z values for most series being relatively low. The move is driven by fundamental factors such as strong earnings and decreasing inventories, rather than any unexpected events.
- **India take**: The Indian metal equities, as represented by nifty_metal, have already reacted to the increase in copper prices. The broader Indian market, as represented by nifty_50, has also reacted to the global risk-on sentiment.
- Watch next: nifty_metal (up) — already moved; Reacted to the increase in copper prices
- Watch next: nifty_50 (up) — already moved; Reacted to the global risk-on sentiment
- **India receivers**: nifty_50 (rho 0.534, z 2.07); nifty_midcap_100 (rho 0.521, z 1.75); nifty_metal (rho -0.431, z 3.69)
- Source: US stocks: S&P 500, Dow hit record highs on strong AI-linked earnings, Mideast deal hopes — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-sp-500-hits-record-high-on-strong-ai-linked-earnings-mideast-deal-hopes/articleshow/132862570.cms
- Source: Copper hits two-month high above $14,000 as inventories dip — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/commodities/news/copper-hits-two-month-high-above-14000-as-inventories-dip/articleshow/132862047.cms
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: Dow Jones, S&P 500 hit fresh all-time highs on AI earnings, Middle East peace hopes — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-war-hormuz-deal-crude-oil-fed-warsh-earnings-forecast-spacex-palantir-tech-caterpillar-marvell-chip-stock-price-news-4th-august-2026/liveblog/132860524.cms
- Historical analogues: 2024-10-09 (d=1.0), 2024-11-26 (d=1.05), 2025-10-31 (d=1.07)

### [RED 8.34] dyn_pltr ↑
- dyn_pltr [EQUITIES]: last 158.09, z20 6.34, zc 7.88, resid-z -0.24 [moved], 1d 25.82%, |z20|=6.34
- **Mechanism**: The recent surge in dyn_pltr, driven by Palantir's strong earnings and AI-driven growth, is likely to propagate through the VALID vix_equity_inverse channel, where a vol spike leads to an equity drawdown. However, given the RISK_ON regime and the priced nature of the move (resid_z = -0.24), the impact may be limited. The metal_copper_channel may also play a role, given the co-movement of monetary metals and the potential for rotations.
- **Gap**: No gap: the move is largely priced, with a small resid_z and a high z20 level, indicating that the market has already accounted for the earnings beat and growth outlook.
- **India take**: The Indian instrument dyn_atherenerg_ns has already reacted to the move in dyn_pltr, given its rho of 0.373. Further reaction may be limited, but Indian metal equities may still be influenced by the global copper lead through the metal_copper_channel.
- Watch next: dyn_atherenerg_ns (up) — already moved; reacted to dyn_pltr
- **India receivers**: dyn_atherenerg_ns (rho 0.373, z 5.33)
- Source: Earnings Beat: Can Palantir sustain its explosive AI-driven growth? — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/news/earnings-beat-can-palantir-sustain-its-explosive-ai-driven-growth/slideshow/132848124.cms
- Source: Palantir’s stock climbs after earnings, as AI drives turbocharged growth — MarketWatch Top, 2026-08-03. https://www.marketwatch.com/story/palantirs-stock-gains-as-ai-drives-turbocharged-growth-e006b70a?mod=mw_rss_topstories
- Source: Palantir’s stock gains as AI drives turbocharged growth — MarketWatch Top, 2026-08-03. https://www.marketwatch.com/story/palantirs-stock-gains-as-ai-drives-turbocharged-growth-e006b70a?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-01 (d=0.08), 2025-10-13 (d=0.13)

### [RED 7.33] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1454.80, z20 5.33, zc 4.61, resid-z 5.07 [unexplained], 1d 14.31%, |z20|=5.33; 1y-pct=100
- **Mechanism**: The surge in Ather Energy's stock price is driven by the company's narrowing quarterly loss, which has ignited investor optimism about its future prospects. This move is propagated through the metal_copper_channel, where global copper leads Indian metal equities, and the vix_equity_inverse channel, which indicates a decrease in volatility. The RISK_ON regime also supports this move.
- **Gap**: No gap: the 14% jump in Ather Energy's stock price is largely priced in, given the significant narrowing of its quarterly loss and the resulting investor enthusiasm
- **India take**: The Indian instrument that expresses this move is the Nifty Auto index, which may react positively to Ather Energy's improved performance. However, the reaction is not yet visible, and the index is still watching the developments
- Watch next: nifty_50 (up) — not yet - watch; Ather Energy's stock surge may lead to a broader market rally
- Source: Ather Energy shares jump 14% after Q1 loss narrows — BusinessLine Mkts, 2026-08-04. https://www.thehindubusinessline.com/markets/ather-energy-shares-jump-18-to-fresh-52-week-high-after-q1-loss-narrows/article71303894.ece
- Source: Ather Energy's tapering losses put stock in fast lane, but is the rally justified? — Mint Markets, 2026-08-04. https://www.livemint.com/market/mark-to-market/ather-energy-electric-vehicles-ev-q1fy27-ebitda-operating-losses-ev-sales-hero-motocorp-11785824423599.html
- Source: Multibagger stock Ather Energy share price soars 18% to record high post Q1 FY27 results: Should you buy? — Mint Markets, 2026-08-04. https://www.livemint.com/market/stock-market-news/multibagger-stock-ather-energy-share-price-soars-18-to-record-high-post-q1-fy27-results-should-you-buy-11785824415092.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [AMBER 6.79] commodities · 2 series ↓
- brent [COMMODITIES]: last 79.94, z20 -0.96, zc -1.16, resid-z -0.81 [quiet], 1d -4.57%, 1-session move -4.57% ≥ 1.5%
- wti [COMMODITIES]: last 76.15, z20 -0.83, zc -1.54, resid-z -0.97 [moved], 1d -5.22%, 1-session move -5.22% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.472 via wti, z 1.75, reacted); midcap_largecap_ratio (rho -0.427 via wti, z -0.68, quiet)
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.532 vs brent, historically leads by 5d
- **India receivers**: nifty_midcap_100 (rho -0.472, z 1.75); midcap_largecap_ratio (rho -0.427, z -0.68)
- Source: India's HPCL Snaps Up Nigerian Crude To Dodge The Hormuz Bottleneck — OilPrice, 2026-08-04. https://oilprice.com/Latest-Energy-News/World-News/Indias-HPCL-Snaps-Up-Nigerian-Crude-To-Dodge-The-Hormuz-Bottleneck.html
- Source: Oil prices take a dive as Qatar and Bessent note talks to reopen Strait of Hormuz — MarketWatch Top, 2026-08-04. https://www.marketwatch.com/story/oil-prices-rise-after-vessel-reports-being-hit-in-strait-of-hormuz-db6ce867?mod=mw_rss_topstories
- Source: Markets dip as profit-taking and oil prices weigh ahead of RBI decision — BusinessLine Mkts, 2026-08-04. https://www.thehindubusinessline.com/markets/markets-dip-as-profit-taking-and-oil-prices-weigh-ahead-of-rbi-decision/article71305441.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 6.39] cross-asset · 3 series ↑
- dyn_jiofin_bo [EQUITIES]: last 264.55, z20 3.07, zc 0.43, resid-z 1.45 [quiet], 1d 0.97%, |z20|=3.07
- nifty_50 [INDICES]: last 24614.90, z20 2.07, zc -0.88, resid-z -1.09 [quiet], 1d -0.64%, |z20|=2.07
- nifty_midcap_100 [INDICES]: last 63484.05, z20 1.75, zc -0.36, resid-z 0.44 [quiet], 1d -0.29%, |z20|=1.75; 1y-pct=99
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-17 (z-distance 0.69).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.692 via nifty_midcap_100, z -2.93, reacted); dyn_bharatcoal_ns (rho 0.631 via nifty_midcap_100, z -1.19, reacted); dyn_indianb_ns (rho 0.62 via nifty_midcap_100, z 0.71, quiet); dyn_indusindbk_bo (rho 0.614 via nifty_midcap_100, z 0.24, quiet); nifty_metal (rho 0.582 via nifty_midcap_100, z 3.69, reacted)
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.574 vs nifty_50, historically leads by 3d
- Watch next: dyn_indianb_ns (co-move) — not yet - watch; rho 0.545 vs dyn_jiofin_bo, historically leads by 1d
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.574 vs nifty_50
- Watch next: dyn_indusindbk_bo (co-move) — not yet - watch; rho 0.532 vs dyn_jiofin_bo
- **India receivers**: dyn_muthootfin_ns (rho 0.692, z -2.93); dyn_bharatcoal_ns (rho 0.631, z -1.19); dyn_indianb_ns (rho 0.62, z 0.71); dyn_indusindbk_bo (rho 0.614, z 0.24)
- Source: Traders on edge! Why Nifty jumped 150 points in final minutes again — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/stocks/news/traders-on-edge-why-nifty-jumped-150-points-in-final-minutes-again/articleshow/132862330.cms
- Source: Market wrap: RIL, Hindalco, Trent among top gainers and losers on Nifty and Sensex on Tuesday — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-ril-hindalco-trent-among-top-gainers-and-losers-on-nifty-and-sensex-on-tuesday/articleshow/132861901.cms
- Source: India's new closing auction stokes sharp Nifty swings, options volatility on weekly expiry — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/stocks/news/indias-new-closing-auction-stokes-sharp-nifty-swings-options-volatility-on-weekly-expiry/articleshow/132861816.cms
- Historical analogues: 2025-07-17 (d=0.69), 2024-11-07 (d=0.98), 2025-08-13 (d=1.26)

### [RED 6.32] cross-asset · 2 series ↑
- usd_jpy [FX]: last 157.57, z20 -3.49, zc -0.01, resid-z 0.05 [quiet], 1d -0.01%, |z20|=3.49
- dyn_amzn [EQUITIES]: last 278.03, z20 2.43, zc -0.20, resid-z 9.76 [unexplained], 1d -2.11%, |z20|=2.43; 1y-pct=99
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-10-16 (z-distance 0.15).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.51 via usd_jpy, z -2.93, reacted); dyn_cartrade_ns (rho -0.36 via dyn_amzn, z 0.18, quiet)
- Watch next: taiwan_weighted (inverse) — not yet - watch; rho -0.508 vs usd_jpy, historically leads by 1d
- Watch next: gbp_usd (inverse) — not yet - watch; rho -0.5 vs usd_jpy, historically leads by 1d
- Watch next: kospi (inverse) — not yet - watch; rho -0.613 vs usd_jpy
- **India receivers**: dyn_muthootfin_ns (rho -0.51, z -2.93); dyn_cartrade_ns (rho -0.36, z 0.18)
- Source: BOFA: TARGET FX VOLATILITY, NOT THE WHOLE MARKET Bank of America says investors should focus on specific currency pairs—not broad FX volatility—if the Fed resumes rate hikes. The bank highlights Japanese yen and British pound pairs as the strongest opportunities. Historically, — DeItaone, 2026-08-04. https://t.me/walter_bloomberg/34270
- Source: What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/us-markets-academy/what-bubble-amazon-enters-3-trillion-market-cap-club-ceo-highlights-striking-ai-demand/articleshow/132854970.cms
- Source: Global Market: US-Japan coordinated yen intervention raises pressure on bears, but BOJ policy holds the key — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-us-japan-coordinated-yen-intervention-raises-pressure-on-bears-but-boj-policy-holds-the-key/articleshow/132850399.cms
- Historical analogues: 2024-10-16 (d=0.15), 2024-11-21 (d=0.23), 2026-03-31 (d=0.24)

### [RED 5.95] fx · 3 series ↑
- usd_mxn [FX]: last 17.26, z20 -2.63, zc -0.55, resid-z -0.38 [quiet], 1d -0.25%, |z20|=2.63
- eur_usd [FX]: last 1.15, z20 2.25, zc -0.37, resid-z -0.54 [quiet], 1d -0.14%, |z20|=2.25
- aud_usd [FX]: last 0.70, z20 1.98, zc -0.09, resid-z -0.12 [quiet], 1d -0.07%, |z20|=1.98
- **Mechanism**: fx · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.518 via usd_mxn, z -2.93, reacted)
- Watch next: usd_brl (co-move) — not yet - watch; rho 0.756 vs usd_mxn, historically leads by 3d
- Watch next: gbp_usd (inverse) — not yet - watch; rho -0.619 vs usd_mxn, historically leads by 5d
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.518 vs aud_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.518, z -2.93)
- Source: Global Market: Euro zone bond yields decline as falling oil prices boost market sentiment — ET Markets, 2026-08-03. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-bond-yields-decline-as-falling-oil-prices-boost-market-sentiment/articleshow/132826355.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-02 (d=0.26), 2025-08-15 (d=0.26)

## Watchlist (below surfacing floor)
dyn_msft ↑ (5.29), dyn_thangamayl_ns ↓ (5.12), dyn_muthootfin_ns ↓ (4.93), dyn_bac ↑ (4.0), dyn_coin ↓ (3.96), nifty_metal ↑ (3.69), natgas ↓ (3.56), asx_200 ↑ (3.45), dyn_lth ↑ (3.15), dyn_tech ↑ (3.15), usd_cny ↓ (3.09), ust_2s10s ↑ (2.86)

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
- INOXINDIA.NS (INOX INDIA LIMITED) score 73.4 — "India Expands Oil Storage Sites After Shock Supply Disruption"
- COALINDIA.NS (COAL INDIA LTD) score 71.6 — "India Expands Oil Storage Sites After Shock Supply Disruption"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 70.5 — "India Expands Oil Storage Sites After Shock Supply Disruption"
- INDIANB.NS (INDIAN BANK) score 56.1 — "BOFA: TARGET FX VOLATILITY, NOT THE WHOLE MARKET Bank of America says investors should foc"
- COIN (Coinbase Global, Inc.) score 50.8 — "Global Market: China stocks rebound on AI, chip rally; Hong Kong shares slip"
- TECHM.NS (TECH MAHINDRA LIMITED) score 42.0 — "BARCLAYS: S&P 500 EARNINGS CRUSH EXPECTATIONS Barclays says 85% of S&P 500 companies have "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 40.3 — "BARCLAYS: S&P 500 EARNINGS CRUSH EXPECTATIONS Barclays says 85% of S&P 500 companies have "
- BAC (Bank of America Corporation) score 39.7 — "BOFA: TARGET FX VOLATILITY, NOT THE WHOLE MARKET Bank of America says investors should foc"
- HDB (HDFC Bank Limited) score 38.9 — "BOFA: TARGET FX VOLATILITY, NOT THE WHOLE MARKET Bank of America says investors should foc"
- OHI (Omega Healthcare Investors, In) score 37.7 — "BOFA: TARGET FX VOLATILITY, NOT THE WHOLE MARKET Bank of America says investors should foc"
- IDBI.NS (IDBI BANK LIMITED) score 37.2 — "BOFA: TARGET FX VOLATILITY, NOT THE WHOLE MARKET Bank of America says investors should foc"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 37.2 — "BOFA: TARGET FX VOLATILITY, NOT THE WHOLE MARKET Bank of America says investors should foc"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 35.1 — "BOFA: TARGET FX VOLATILITY, NOT THE WHOLE MARKET Bank of America says investors should foc"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 34.6 — "Ather Energy shares jump 14% after Q1 loss narrows"
- TECH (Bio-Techne Corp) score 34.3 — "BARCLAYS: S&P 500 EARNINGS CRUSH EXPECTATIONS Barclays says 85% of S&P 500 companies have "
- CHKP (Check Point Software Technolog) score 30.6 — "Dhaval Packaging IPO allotment to be finalised today. Here's GMP, how to check status onli"
- LTH (Life Time Group Holdings, Inc.) score 27.2 — "Dow Jones| Nasdaq | US Stock Market Today | Live: Dow Jones, S&P 500 hit fresh all-time hi"
- BOND (PIMCO Active Bond Exchange-Tra) score 22.7 — "India bonds rise on position building ahead of RBI policy"
- 301077.SZ (CHINASTARS) score 17.9 — "US DRAFTING BAN ON CHINA DATA CENTER COMPONENTS: REUTERS"
- JUSTDIAL.BO (JUST DIAL LTD.) score 12.2 — "Ather Energy's tapering losses put stock in fast lane, but is the rally justified?"
- AMZN (Amazon.com, Inc.) score 11.2 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- MS (Morgan Stanley) score 10.8 — "U.S. TIGHTENS ROBOT IMPORT RULES The FCC will restrict imports of certain foreign-made adv"
- JIOFIN.BO (Jio Financial Services Limited) score 10.7 — "Jio Financial Services Share Price Live Updates: Jio Financial Services sees a slight dip "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.3 — "Tata Steel Share Price Live Updates: Tata Steel's Price Movement Today"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.9 — "Adani Ent Share Price Live Updates: Adani Ent. News"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 9.9 — "Jio Financial Services Share Price Live Updates: Jio Financial Services sees a slight dip "
- PCJEWELLER.NS (PC JEWELLER LTD) score 9.4 — "Kalyan Jewellers Q1 Results: Net profit jumps 32% YoY to  ₹349 crore; margins contract"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 8.4 — "Coal India Share Price Live Updates: Coal India  Market Performance"
- MSFT (Microsoft Corporation) score 7.9 — "SHARES OF US HYPERSCALERS CLIMB • META RISES 6.1% • MICROSOFT JUMPS 4.7% • AMAZON GAINS 4."
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.6 — "Maharatna PSU stock Power Finance Corporation to declare Q1 results 2026, interim dividend"
- AAPL (Apple Inc.) score 7.2 — "Apple suffers worst rout since 2025 on disappointing outlook"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.5 — "ICICI Securities initiates coverage on 7 PSU banks with positive valuations"
- GS (Goldman Sachs Group, Inc. (The) score 5.9 — "Global Market: Goldman Sachs sees Brent crude trading at $80-$90 until Iran conflict outlo"
- VT (Vanguard Total World Stock Ind) score 5.8 — "Traders in the world’s most important financial market are bracing for a wild stretch ahea"
- META (Meta) score 5.7 — "META INVITED TO WHITE HOUSE TUESDAY TO DISCUSS AI SAFETY TESTING BY U.S. GOVERNMENT - COMP"
- INFY (Infosys Limited) score 4.9 — "Infosys Share Price Live Updates: Infosys market movement today"
- PLTR (Palantir Technologies Inc.) score 3.5 — "Palantir’s stock climbs after earnings, as AI drives turbocharged growth"
- THANGAMAYL.NS (THANGAMAYIL JEWELLERY LTD) score 3.4 — "Thangamayil share selloff continues: Stock drops 5% despite Rs 344 crore sales in first 3 "
- NVDA (NVIDIA Corporation) score 3.2 — "Did China build a top-tier AI model by itself? A new report suggests Nvidia chips played a"
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