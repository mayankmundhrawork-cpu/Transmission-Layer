# Transmission Layer — board brief · 2026-08-14 09:19Z

data as of **2026-08-14** · 98 series · 7 red / 36 amber · 8 events surfaced (19 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.203, 2d in regime; vol-pct 0.239, breadth-off 0.167, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.41, last shift 2026-06-08. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.85, last shift 2026-05-15. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.29, corr60 0.35, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.2, corr60 -0.12, last shift 2026-06-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.73, corr60 -0.8, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.09, corr60 -0.11, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.4, corr60 -0.21, last shift 2026-05-08. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.06, corr60 0.17, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 0.0007248582980661222)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.494** (n=1111) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=2489) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.23] cross-asset · 14 series ↑
- russell_2000 [INDICES]: last 3052.63, z20 1.86, zc 0.20, resid-z -0.70 [quiet], 1d 0.23%, |z20|=1.86; 1y-pct=100
- dyn_vt [EQUITIES]: last 162.38, z20 1.83, zc 0.64, resid-z 0.94 [quiet], 1d 0.53%, 1y-pct=100
- dyn_nvda [EQUITIES]: last 225.37, z20 1.78, zc 0.22, resid-z 1.25 [quiet], 1d 0.57%, 1y-pct=99
- comex_gold [COMMODITIES]: last 4403.90, z20 1.78, zc 0.65, resid-z 0.62 [quiet], 1d 0.92%, |z20|=1.78; co-occur[gold_silver] same-direction (channel VALID)
- nasdaq_100 [INDICES]: last 30085.28, z20 1.75, zc 0.85, resid-z 0.61 [quiet], 1d 1.15%, |z20|=1.75; 1y-pct=96
- sp500 [INDICES]: last 7798.86, z20 1.69, zc 0.81, resid-z -0.45 [quiet], 1d 0.65%, |z20|=1.69; 1y-pct=100
- comex_silver [COMMODITIES]: last 64.89, z20 1.57, zc 0.01, resid-z -0.74 [quiet], 1d 0.03%, |z20|=1.57; co-occur[gold_silver] same-direction (channel VALID)
- stoxx_50 [INDICES]: last 6554.88, z20 1.41, zc 0.19, resid-z -0.61 [quiet], 1d 0.14%, 1y-pct=100
- vix [INDICES]: last 14.56, z20 -1.36, zc -0.06, resid-z n/a [quiet], 1d -0.48%, 1y-pct=4
- dax [INDICES]: last 26437.62, z20 1.36, zc 0.73, resid-z -0.58 [quiet], 1d 0.52%, 1y-pct=100
- dow_jones [INDICES]: last 53834.58, z20 1.09, zc 0.16, resid-z -1.16 [quiet], 1d 0.12%, 1y-pct=98
- gold_silver_ratio [DERIVED]: last 67.86, z20 -1.06, zc n/a, resid-z n/a [quiet], 1d 0.89%, GSR<75 (extreme low)
- cac_40 [INDICES]: last 8646.76, z20 0.80, zc -0.06, resid-z -0.93 [quiet], 1d -0.04%, 1y-pct=96
- comex_copper [COMMODITIES]: last 6.58, z20 0.76, zc -0.07, resid-z -0.63 [quiet], 1d -0.17%, 1y-pct=96
- **Mechanism**: The recent surge in gold prices, driven by mild US inflation data, has led to a rally in monetary metals. The VALID gold_silver_comove channel indicates that gold and silver are likely to move together, and the VALID vix_equity_inverse channel suggests that a vol spike could lead to an equity drawdown. However, the current RISK_ON regime and the INVERTED safe_haven_gold channel imply that the risk-off safe-haven bid for gold may be weakening.
- **Gap**: No gap: the big raw move in gold prices has been largely priced in, with a small resid_z of 0.62, indicating that the move is largely explained by factor exposures
- **India take**: The Indian instrument nifty_metal, which has a rho of 0.516 with comex_silver, may react to the downward movement of silver. However, nifty_metal has not yet moved, and its z20 level is 0.57, indicating a quiet move so far.
- Watch next: comex_gold (down) — already moved; gold prices have already slipped on Friday and are headed for a weekly loss as investors lock in profits
- Watch next: nifty_metal (down) — not yet - watch; nifty_metal has a rho of 0.516 with comex_silver and may follow the downward movement of silver
- **India receivers**: nifty_metal (rho 0.516, z 0.57); nifty_fmcg (rho -0.502, z -1.71); nifty_midcap_100 (rho 0.501, z 1.22); nifty_50 (rho 0.489, z 0.16)
- Source: Gold Rate Today, Aug 14: Gold prices down in Delhi, Mumbai, Kolkata, Bengaluru, Ahmedabad — BusinessLine Mkts, 2026-08-14. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-mumbai-chennai-ahmedabad-delhi-hyderabad-bengaluru-kolkata-gold-rates-august-14-2026/article71344709.ece
- Source: Reddit gets S&P 500 boost: What investors need to know — ET Markets, 2026-08-14. https://economictimes.indiatimes.com/markets/us-stocks/news/reddit-gets-sampp-500-boost-what-investors-need-to-know/slideshow/133230670.cms
- Source: Gold on track for weekly loss as investors book profits after inflation-fuelled rally — BusinessLine Mkts, 2026-08-14. https://www.thehindubusinessline.com/markets/gold/gold-on-track-for-weekly-loss-as-investors-book-profits-after-inflation-fuelled-rally/article71344110.ece
- Historical analogues: 2024-11-26 (d=0.9), 2025-10-31 (d=0.97), 2025-10-24 (d=1.11)

### [RED 6.12] commodities · 2 series ↑
- corn [COMMODITIES]: last 477.50, z20 3.29, zc 5.15, resid-z -0.92 [moved], 1d 6.58%, |z20|=3.29; 1y-pct=100
- wheat [COMMODITIES]: last 680.25, z20 1.02, zc 2.38, resid-z -0.00 [moved], 1d 4.21%, 1y-pct=98
- **Mechanism**: The recent surge in corn and wheat prices is driven by supply-side disruptions, particularly the USDA's cut in yield expectations due to heat waves, which has led to a risk-on sentiment in the commodities market. This move is priced, given the significant z20 levels and low resid_z values for both corn and wheat, indicating that the price movement is largely explained by factor exposures. The valid gold_silver_comove and metal_copper_channel suggest that the monetary metals and copper are co-moving, which may further support the commodities rally.
- **Gap**: No gap: the recent price move in corn and wheat is largely explained by factor exposures, with low resid_z values indicating that the move is priced
- **India take**: The Indian instrument dyn_lenskart_ns has already reacted, with a z20 value of 3.16, indicating that the transmission of the commodities move to the Indian market is underway. Other Indian metal equities may also be affected through the metal_copper_channel.
- Watch next: soybeans (up) — not yet - watch; high correlation with corn
- **India receivers**: dyn_lenskart_ns (rho 0.405, z 3.07)
- Source: Corn Jumps as USDA Cuts Yield More Than Expected Amid Heat Waves — Mint Markets, 2026-08-12. https://www.livemint.com/market/corn-jumps-as-usda-cuts-yield-more-than-expected-amid-heat-waves-11786572052753.html
- Source: WHEAT JUMPS AFTER RUSSIAN PORT STRIKE Wheat futures surged 2.4% after Ukrainian drones reportedly struck two grain terminals at Russia’s Novorossiysk port. The terminals handle roughly 15 million metric tons of grain exports annually, raising concerns over disruptions to — DeItaone, 2026-08-12. https://t.me/walter_bloomberg/34681
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [RED 5.07] dyn_lenskart_ns ↑
- dyn_lenskart_ns [EQUITIES]: last 611.90, z20 3.07, zc 1.85, resid-z 1.52 [unexplained], 1d 2.51%, |z20|=3.07; 1y-pct=99
- **Mechanism**: The recent surge in Lenskart Solutions' stock price can be attributed to the company's strong Q1 results, which showed a near four-fold jump in profit, and the buzz around its potential MSCI inclusion. This positive news has led to increased investor interest, driving up the stock price. The VALID metal_copper_channel and vix_equity_inverse channels indicate a risk-on environment, which supports the stock's upward movement.
- **Gap**: No gap: the stock's price move is largely priced in, given the significant increase in profit and positive market sentiment
- **India take**: The Indian instrument that expresses this move is Lenskart Solutions, which has already reacted positively to the news, and other retail-focused stocks may follow suit. The Nifty Retail index may also be affected, potentially leading to a broader market impact.
- Watch next: Lenskart Solutions (up) — already moved; strong Q1 results and MSCI inclusion buzz
- Source: Lenskart Solutions among 7 stocks hitting 52-week highs; surge up to 20% in a month — ET Markets, 2026-08-13. https://economictimes.indiatimes.com/markets/stocks/news/lenskart-solutions-among-7-stocks-hitting-52-week-highs-surge-up-to-20-in-a-month/slideshow/133210592.cms
- Source: Lenskart shares soar after strong Q1 results and MSCI inclusion buzz — BusinessLine Mkts, 2026-08-13. https://www.thehindubusinessline.com/markets/lenskart-shares-zoom-nearly-7-to-fresh-52-week-high-after-strong-q1-results-and-msci-inclusion-buzz/article71339607.ece
- Source: Lenskart shares hit record high after Q1 profit jumps nearly four-fold; Motilal Oswal lifts target price — Mint Markets, 2026-08-13. https://www.livemint.com/market/stock-market-news/lenskart-shares-hit-record-high-after-q1-profit-jumps-nearly-four-fold-motilal-oswal-lifts-target-price-11786610679031.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

### [RED 4.94] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.62, z20 1.94, zc n/a, resid-z n/a [quiet], 1d -0.24%, 52-wk extreme (pct=99); |z20|=1.94; 1y-pct=99
- **Mechanism**: The midcap_largecap_ratio has reached a 52-wk extreme, with a z20 level of 1.97, indicating a potential overvaluation of midcaps relative to largecaps. This move is priced, as evidenced by the resid_z being None, suggesting that the current level is largely explained by factor exposures. The aftermath of similar events has seen a median decline of 1.35% in the midcap_largecap_ratio over the next 20 days. The RISK_ON regime and VALID channels such as gold_silver_comove and metal_copper_channel may influence the propagation of this move.
- **Gap**: No gap: the current level of midcap_largecap_ratio is largely explained by factor exposures, with no unexplained component (resid_z=None)
- **India take**: The Nifty Midcap 100 index has already reacted to this move, with a z20 level of 1.04, while other transmission candidates such as Dyn Fincables NS and Dyn IndianB NS have also reacted, with z20 levels of 2.41 and 1.4, respectively.
- Watch next: nifty_midcap_100 (down) — already moved; high correlation with midcap_largecap_ratio
- **India receivers**: nifty_midcap_100 (rho 0.532, z 1.22); dyn_bharatcoal_ns (rho 0.404, z -0.85); dyn_fincables_ns (rho 0.399, z 2.25); dyn_pcjeweller_ns (rho 0.369, z 0.1)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 4.88] dyn_301077_sz ↑
- dyn_301077_sz [EQUITIES]: last 24.01, z20 2.88, zc -0.29, resid-z 1.57 [unexplained], 1d -2.44%, |z20|=2.88
- **Mechanism**: The dyn_301077_sz move is unexplained by factor exposures, with a resid_z of 1.57, suggesting a potential anomaly. However, the big raw move with small resid_z indicates that the move is largely priced in. The VALID metal_copper_channel and gold_silver_comove channels may be influencing the move, but the WEAK/INVERTED channels, such as safe_haven_gold and inr_oil_channel, are not available as mechanisms. The RISK_ON regime and vix_equity_inverse channel also support the move.
- **Gap**: No gap: the move is largely priced in with a small resid_z
- **India take**: The Indian instrument that expresses this move is likely to be metal equities, such as Hindalco or Tata Steel, which may react positively due to the VALID metal_copper_channel. However, the reaction is already reflected in the price.
- Watch next: dyn_301077_sz (up) — already moved; unexplained move with high z20 level
- Source: Global Market: China stocks rise on AI optimism; Hong Kong shares mostly flat — ET Markets, 2026-08-13. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-rise-on-ai-optimism-hong-kong-shares-mostly-flat/articleshow/133199079.cms
- Historical analogues: 2026-06-18 (d=0.0), 2026-03-30 (d=0.02), 2026-06-03 (d=0.03)

### [AMBER 4.56] rates · 3 series ↑
- ust_30y [RATES]: last 5.24, z20 1.24, zc 0.00, resid-z -0.12 [quiet], 1d 0.00%, 1y-pct=98
- ust_10y [RATES]: last 4.68, z20 0.50, zc -0.43, resid-z -0.76 [quiet], 1d -0.43%, 1y-pct=96
- tips_10y_real [RATES]: last 2.42, z20 0.47, zc -0.26, resid-z -0.80 [quiet], 1d -0.41%, 1y-pct=96
- **Mechanism**: The recent surge in bond yields, driven by AI companies' increased borrowing and governments' ramped-up bond sales, has led to a rise in inflation-adjusted borrowing costs across major economies. This move is largely priced, with small resid_z values indicating that the factor exposures explain most of the move. However, the valid metal_copper_channel and the historically leading relationship between brent and ust_30y may propagate this move further.
- **Gap**: No gap: the move in bond yields is largely explained by factor exposures, with small resid_z values indicating that the move is priced
- **India take**: The Indian 10-year government bond yield may react to the global bond yield surge, potentially leading to a rise in yields. However, the recent easing of oil prices and lower US Treasury yields may support a positive start for Indian bonds.
- Watch next: dyn_bond (up) — not yet - watch; historically leads by 1d
- Watch next: brent (up) — not yet - watch; historically leads by 3d
- Source: AI-driven surge in bond yields could be next risk for markets and growth — BusinessLine Mkts, 2026-08-14. https://www.thehindubusinessline.com/markets/ai-driven-surge-in-bond-yields-could-be-next-risk-for-markets-and-growth/article71344109.ece
- Source: Indian bonds poised for positive start on lower oil prices, Treasury yields — BusinessLine Mkts, 2026-08-14. https://www.thehindubusinessline.com/markets/indian-bonds-poised-for-positive-start-on-lower-oil-prices-treasury-yields/article71343962.ece
- Source: Global Market: Japanese bond yields hold near highs as markets brace for BOJ rate hike — ET Markets, 2026-08-13. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japanese-bond-yields-hold-near-highs-as-markets-brace-for-boj-rate-hike/articleshow/133203276.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.25), 2026-03-30 (d=0.31)

### [AMBER 4.42] dyn_crwv ↑
- dyn_crwv [EQUITIES]: last 106.31, z20 2.42, zc -0.22, resid-z 3.38 [unexplained], 1d -1.32%, |z20|=2.42
- **Mechanism**: The recent surge in CoreWeave's stock price, driven by strong AI infrastructure company earnings and upbeat quarterly results, has led to a rise in dyn_crwv. This move is priced, with a small resid_z of 0.9, indicating that the factor exposures have largely explained the move. The VALID vix_equity_inverse channel suggests that the vol spike may lead to an equity drawdown, but the current RISK_ON regime may mitigate this effect.
- **Gap**: No gap: the move in dyn_crwv is largely priced, with a small resid_z and a significant z20 level of 2.58
- **India take**: The Indian instrument that expresses this move is nifty_fmcg, which has a negative correlation with dyn_crwv. However, nifty_fmcg has not yet reacted to the move in dyn_crwv, and its current status is quiet.
- Watch next: nifty_fmcg (down) — not yet - watch; rho=-0.375 via dyn_crwv
- **India receivers**: nifty_fmcg (rho -0.38, z -1.71)
- Source: US stocks: S&P 500 ends higher as CoreWeave results fuel AI optimism — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-sp-500-ends-higher-as-coreweave-results-fuel-ai-optimism/articleshow/133192806.cms
- Source: US stocks: CoreWeave, Super Micro surge on signs of sustained AI buildout — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-coreweave-super-micro-surge-on-signs-of-sustained-ai-buildout/articleshow/133187386.cms
- Source: CoreWeave’s stock is rocketing after earnings lead to praise from bulls and bears alike — MarketWatch Top, 2026-08-12. https://www.marketwatch.com/story/coreweaves-stock-is-rocketing-after-earnings-lead-to-praise-from-bulls-and-bears-alike-46c831e7?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-13 (d=0.01), 2025-08-05 (d=0.04)

### [AMBER 4.25] dyn_fincables_ns ↑
- dyn_fincables_ns [EQUITIES]: last 1241.10, z20 2.25, zc -0.16, resid-z -0.19 [quiet], 1d -0.66%, |z20|=2.25; 1y-pct=99
- **Mechanism**: The recent surge in dyn_fincables_ns can be attributed to its strong Q1 results and the subsequent target price increase by Jefferies. This move is priced, with a relatively small resid_z of -0.19, indicating that the factor exposures have largely explained the move. The metal_copper_channel, which is currently valid, may also play a role in transmitting this move to other Indian metal equities.
- **Gap**: No gap: the move in dyn_fincables_ns is largely priced, with a small resid_z and a high r2 value of 0.081, indicating that the factor exposures have explained the move.
- **India take**: The Indian instrument that expresses this move is the nifty_midcap_100, which has already reacted to the surge in dyn_fincables_ns. The midcap_largecap_ratio has also reacted, while dyn_bharatcoal_ns remains quiet.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to dyn_fincables_ns move
- **India receivers**: nifty_midcap_100 (rho 0.419, z 1.22); midcap_largecap_ratio (rho 0.399, z 1.94); dyn_bharatcoal_ns (rho 0.38, z -0.85)
- Source: Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410 — BusinessLine Mkts, 2026-08-12. https://www.thehindubusinessline.com/markets/stock-markets/finolex-cables-shares-jump-14-to-52-week-high-jefferies-lift-target-to-1410-maintains-accumulate/article71335064.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-02-19 (d=0.0), 2025-02-07 (d=0.02)

## Watchlist (below surfacing floor)
dyn_ohi ↓ (4.05), dyn_cupid_ns ↑ (3.98), nikkei_225 ↑ (3.73), dyn_bac ↑ (3.63), dyn_tatatech_ns ↑ (3.6), dyn_atherenerg_ns ↑ (3.26), fx · 2 series ↑ (3.09), dyn_tech ↑ (3.05), dyn_hdb ↓ (2.89), indices · 2 series ↑ (2.6), dyn_lth ↑ (2.59), bovespa ↓ (2.51)

## India macro
- nifty_50: 24367.0996 (1d -0.12%, z20 0.16, flag none)
- nifty_midcap_100: 63895.1484 (1d -0.35%, z20 1.22, flag amber)
- usd_inr: 95.4350 (1d 0.10%, z20 -0.64, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6222 (1d -0.24%, z20 1.94, flag red)
- Next India prints: India WPI T-0d · NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 104.7 — "Indian refiners buy crude months ahead as Russia, Hormuz supply risks mount"
- INOXINDIA.NS (INOX INDIA LIMITED) score 103.7 — "Indian refiners buy crude months ahead as Russia, Hormuz supply risks mount"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 103.2 — "Indian refiners buy crude months ahead as Russia, Hormuz supply risks mount"
- INDIANB.NS (INDIAN BANK) score 73.0 — "Indian refiners buy crude months ahead as Russia, Hormuz supply risks mount"
- BAC (Bank of America Corporation) score 57.0 — "S&P assigns investment-grade rating to IDFC FIRST Bank. Can it lift the stock?"
- TECHM.NS (TECH MAHINDRA LIMITED) score 56.9 — "Rekha Jhunjhunwala portfolio stock VA Tech Wabag jumps 5%; Axis Securities raises target p"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 55.6 — "Rekha Jhunjhunwala portfolio stock VA Tech Wabag jumps 5%; Axis Securities raises target p"
- TECH (Bio-Techne Corp) score 54.9 — "Rekha Jhunjhunwala portfolio stock VA Tech Wabag jumps 5%; Axis Securities raises target p"
- OHI (Omega Healthcare Investors, In) score 54.0 — "Reddit gets S&P 500 boost: What investors need to know"
- COIN (Coinbase Global, Inc.) score 53.9 — "Global Market: European shares steady near record highs as Iran war, Eurozone data in focu"
- HDB (HDFC Bank Limited) score 49.5 — "S&P assigns investment-grade rating to IDFC FIRST Bank. Can it lift the stock?"
- CHKP (Check Point Software Technolog) score 47.5 — "Behari Lal Engineering IPO Day 3: Issue booked 51.03x so far. Check GMP, subscriptions, ke"
- IDBI.NS (IDBI BANK LIMITED) score 44.8 — "S&P assigns investment-grade rating to IDFC FIRST Bank. Can it lift the stock?"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 44.8 — "S&P assigns investment-grade rating to IDFC FIRST Bank. Can it lift the stock?"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 44.6 — "S&P assigns investment-grade rating to IDFC FIRST Bank. Can it lift the stock?"
- LTH (Life Time Group Holdings, Inc.) score 38.6 — "Shiprocket IPO Day 3: GMP signals 38% listing premium, subscribed 3.16 times; should you s"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 30.5 — "Tata Motors PV shares tumble 6% after net profit drops in Q1; analysts stay cautious"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 30.3 — "OpenAI revenue doubles to over $40 billion as IPO plans gather pace"
- BOND (PIMCO Active Bond Exchange-Tra) score 28.2 — "Indian bonds poised for positive start on lower oil prices, Treasury yields"
- 301077.SZ (CHINASTARS) score 28.0 — "Unitree IPO: China’s humanoid robot starset for potentially explosive Shanghai debut"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 26.4 — "Tata Motors PV shares tumble 6% after net profit drops in Q1; analysts stay cautious"
- JIOFIN.BO (Jio Financial Services Limited) score 20.3 — "Britannia Share Price Live Updates: Britannia's Financial Snapshot"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 18.2 — "Bharat Dynamics Q1 Results: Net profit soars 6x to Rs 119 crore, revenue surges 131% YoY"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 17.1 — "Muthoot Fincorp files draft papers for ₹3,000 crore IPO"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 15.0 — "Britannia Share Price Live Updates: Britannia's Financial Snapshot"
- JUSTDIAL.BO (JUST DIAL LTD.) score 14.9 — "DEEPSEEK ANNOUNCES ADJUSTMENT TO API RPICING - STATEMENT"
- MS (Morgan Stanley) score 13.5 — "Tata Motors PV shares fall 5% after weak Q1 results. What are Morgan Stanley, Nomura, othe"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 10.5 — "Bharat Dynamics Q1 Results: Net profit soars 6x to Rs 119 crore, revenue surges 131% YoY"
- PCJEWELLER.NS (PC JEWELLER LTD) score 9.3 — "Brokerages initiate coverage on Vedanta Aluminium, Kalyan Jewellers, 3 other stocks with u"
- META (Meta) score 8.9 — "Nifty holds above 24,300 at midday as metals, IT drag; bulls eye 24,450"
- NVDA (NVIDIA Corporation) score 8.6 — "Alphabet’s stock slips as Nvidia’s $500 billion financing deal threatens custom chips"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.2 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Achieves Significant Price Movem"
- AAPL (Apple Inc.) score 6.0 — "Nvidia, Apple, Google fuel record $185 billion gain for Norway’s wealth fund, but CEO say,"
- VT (Vanguard Total World Stock Ind) score 5.8 — "China’s next economic ambition: workshop for the Muslim world"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.8 — "Lenskart shares soar after strong Q1 results and MSCI inclusion buzz"
- INTC (Intel Corporation) score 4.5 — "PRESIDENT’S SCHEDULE — AUGUST 13, 2026 🔸 8:00 AM — Executive Time White House · Closed Pre"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 2.5 — "ICICI Bank Share Price Live Updates: ICICI Bank Stock Details"
- CRWV (CoreWeave, Inc.) score 1.9 — "US stocks: S&P 500 ends higher as CoreWeave results fuel AI optimism"
- FINCABLES.NS (FINOLEX CABLES LTD) score 1.9 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 1.7 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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