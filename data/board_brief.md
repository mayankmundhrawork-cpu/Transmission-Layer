# Transmission Layer — board brief · 2026-08-14 11:08Z

data as of **2026-08-14** · 98 series · 8 red / 37 amber · 8 events surfaced (21 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.203, 2d in regime; vol-pct 0.239, breadth-off 0.167, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.41, last shift 2026-06-08. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.85, last shift 2026-05-15. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.3, corr60 0.35, last shift 2026-05-14. Channel: global copper leads Indian metal equities
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

### [RED 9.12] cross-asset · 14 series ↑
- russell_2000 [INDICES]: last 3052.63, z20 1.86, zc 0.20, resid-z -0.70 [quiet], 1d 0.23%, |z20|=1.86; 1y-pct=100
- dyn_vt [EQUITIES]: last 162.38, z20 1.83, zc 0.64, resid-z 0.94 [quiet], 1d 0.53%, 1y-pct=100
- comex_gold [COMMODITIES]: last 4406.00, z20 1.79, zc 0.69, resid-z 0.62 [quiet], 1d 0.97%, |z20|=1.79; co-occur[gold_silver] same-direction (channel VALID)
- dyn_nvda [EQUITIES]: last 225.37, z20 1.78, zc 0.22, resid-z 1.25 [quiet], 1d 0.57%, 1y-pct=99
- nasdaq_100 [INDICES]: last 30085.28, z20 1.75, zc 0.85, resid-z 0.61 [quiet], 1d 1.15%, |z20|=1.75; 1y-pct=96
- sp500 [INDICES]: last 7798.86, z20 1.69, zc 0.81, resid-z -0.45 [quiet], 1d 0.65%, |z20|=1.69; 1y-pct=100
- comex_silver [COMMODITIES]: last 64.79, z20 1.54, zc -0.05, resid-z -0.87 [quiet], 1d -0.12%, |z20|=1.54; co-occur[gold_silver] same-direction (channel VALID)
- stoxx_50 [INDICES]: last 6562.05, z20 1.47, zc 0.33, resid-z -0.61 [quiet], 1d 0.25%, 1y-pct=100
- dax [INDICES]: last 26489.56, z20 1.45, zc 1.01, resid-z -0.58 [quiet], 1d 0.72%, 1y-pct=100
- vix [INDICES]: last 14.53, z20 -1.37, zc -0.09, resid-z n/a [quiet], 1d -0.68%, 1y-pct=4
- dow_jones [INDICES]: last 53834.58, z20 1.09, zc 0.16, resid-z -1.16 [quiet], 1d 0.12%, 1y-pct=98
- gold_silver_ratio [DERIVED]: last 68.00, z20 -0.95, zc n/a, resid-z n/a [quiet], 1d 1.09%, GSR<75 (extreme low)
- cac_40 [INDICES]: last 8653.56, z20 0.85, zc 0.05, resid-z -0.93 [quiet], 1d 0.03%, 1y-pct=97
- comex_copper [COMMODITIES]: last 6.58, z20 0.75, zc -0.08, resid-z -0.63 [quiet], 1d -0.18%, 1y-pct=96
- **Mechanism**: The recent surge in commodity prices, particularly gold and silver, has triggered a risk-on sentiment in the market, as evidenced by the VALID gold_silver_comove channel and the quiet move in the russell_2000 and nasdaq_100 indices. However, the resid_z values for these indices are relatively low, indicating that the move is largely priced in.
- **Gap**: No gap: The recent move in the russell_2000 and nasdaq_100 indices is largely priced in, as indicated by their low resid_z values.
- **India take**: The Indian market has already reacted to the global cues, with the nifty_fmcg index moving in response to the dyn_nvda stock. The nifty_metal index, which is correlated with comex_silver, is still quiet and worth watching.
- Watch next: nifty_metal (up) — not yet - watch; Correlated with comex_silver, which has a high z20 value
- Watch next: nifty_fmcg (down) — already moved; Reacted to the move in dyn_nvda
- **India receivers**: nifty_metal (rho 0.515, z 0.45); nifty_fmcg (rho -0.502, z -1.62); nifty_midcap_100 (rho 0.494, z 1.06); nifty_50 (rho 0.489, z 0.16)
- Source: Top Gainers & Losers on 14 August: NALCO, HPCL, Tata Motors PV, Netweb Tech, Hindustan Copper among top losers — Mint Markets, 2026-08-14. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-14-august-nalco-hpcl-tata-motors-pv-netweb-tech-hindustan-copper-among-top-losers-11786700818338.html
- Source: Gold Rate Today, Aug 14: Gold prices down in Delhi, Mumbai, Kolkata, Bengaluru, Ahmedabad — BusinessLine Mkts, 2026-08-14. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-mumbai-chennai-ahmedabad-delhi-hyderabad-bengaluru-kolkata-gold-rates-august-14-2026/article71344709.ece
- Source: Reddit gets S&P 500 boost: What investors need to know — ET Markets, 2026-08-14. https://economictimes.indiatimes.com/markets/us-stocks/news/reddit-gets-sampp-500-boost-what-investors-need-to-know/slideshow/133230670.cms
- Historical analogues: 2024-11-26 (d=0.9), 2025-10-31 (d=0.97), 2025-10-24 (d=1.11)

### [RED 5.95] commodities · 2 series ↑
- corn [COMMODITIES]: last 476.00, z20 3.12, zc 4.89, resid-z -0.92 [moved], 1d 6.25%, |z20|=3.12; 1y-pct=99
- wheat [COMMODITIES]: last 679.00, z20 0.96, zc 2.27, resid-z -0.00 [moved], 1d 4.02%, 1y-pct=98
- **Mechanism**: The recent surge in corn and wheat prices is primarily driven by supply-side concerns, particularly the USDA's unexpected reduction in yield due to heat waves. This has led to a priced move, with the resid_z values indicating that the big raw move is largely explained by factor exposures. The valid gold_silver_comove and metal_copper_channel may also play a role in transmitting this move to other metals and potentially Indian metal equities.
- **Gap**: No gap: the move in corn and wheat is largely priced, with small resid_z values indicating that the move is explained by factor exposures
- **India take**: The Indian instrument dyn_lenskart_ns has already reacted, with a z20 value of 3.07, indicating some transmission of the commodities move to the Indian market. Further reaction may be seen in Indian metal equities via the metal_copper_channel.
- Watch next: soybeans (up) — not yet - watch; high correlation with corn
- **India receivers**: dyn_lenskart_ns (rho 0.403, z 3.07)
- Source: Corn Jumps as USDA Cuts Yield More Than Expected Amid Heat Waves — Mint Markets, 2026-08-12. https://www.livemint.com/market/corn-jumps-as-usda-cuts-yield-more-than-expected-amid-heat-waves-11786572052753.html
- Source: WHEAT JUMPS AFTER RUSSIAN PORT STRIKE Wheat futures surged 2.4% after Ukrainian drones reportedly struck two grain terminals at Russia’s Novorossiysk port. The terminals handle roughly 15 million metric tons of grain exports annually, raising concerns over disruptions to — DeItaone, 2026-08-12. https://t.me/walter_bloomberg/34681
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [RED 5.07] dyn_lenskart_ns ↑
- dyn_lenskart_ns [EQUITIES]: last 612.00, z20 3.07, zc 1.87, resid-z 1.59 [unexplained], 1d 2.53%, |z20|=3.07; 1y-pct=99
- **Mechanism**: The recent surge in Lenskart Solutions' stock price can be attributed to the company's strong Q1 results, which showed a near four-fold jump in profit, and the buzz around its potential MSCI inclusion. This positive news has led to increased investor interest, driving up the stock price. The VALID metal_copper_channel and vix_equity_inverse channels indicate a risk-on environment, which supports the stock's upward movement.
- **Gap**: No gap: the stock's price move is largely priced in, given the significant increase in profit and positive market sentiment
- **India take**: The Indian instrument that expresses this move is Lenskart Solutions, which has already reacted positively to the news, and other retail-focused stocks may follow suit. The Nifty Retail index may also be affected, potentially leading to a broader market impact.
- Watch next: Lenskart Solutions (up) — already moved; strong Q1 results and MSCI inclusion buzz
- Source: Lenskart Solutions among 7 stocks hitting 52-week highs; surge up to 20% in a month — ET Markets, 2026-08-13. https://economictimes.indiatimes.com/markets/stocks/news/lenskart-solutions-among-7-stocks-hitting-52-week-highs-surge-up-to-20-in-a-month/slideshow/133210592.cms
- Source: Lenskart shares soar after strong Q1 results and MSCI inclusion buzz — BusinessLine Mkts, 2026-08-13. https://www.thehindubusinessline.com/markets/lenskart-shares-zoom-nearly-7-to-fresh-52-week-high-after-strong-q1-results-and-msci-inclusion-buzz/article71339607.ece
- Source: Lenskart shares hit record high after Q1 profit jumps nearly four-fold; Motilal Oswal lifts target price — Mint Markets, 2026-08-13. https://www.livemint.com/market/stock-market-news/lenskart-shares-hit-record-high-after-q1-profit-jumps-nearly-four-fold-motilal-oswal-lifts-target-price-11786610679031.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

### [RED 4.88] dyn_301077_sz ↑
- dyn_301077_sz [EQUITIES]: last 24.01, z20 2.88, zc -0.29, resid-z 1.57 [unexplained], 1d -2.44%, |z20|=2.88
- **Mechanism**: The dyn_301077_sz move is unexplained by factor exposures, with a resid_z of 1.57, suggesting a potential anomaly. However, the big raw move with small resid_z indicates that the move is largely priced in. The VALID metal_copper_channel and gold_silver_comove channels may be influencing the move, but the WEAK/INVERTED channels, such as safe_haven_gold and inr_oil_channel, are not available as mechanisms. The RISK_ON regime and vix_equity_inverse channel also support the move.
- **Gap**: No gap: the move is largely priced in with a small resid_z
- **India take**: The Indian instrument that expresses this move is likely to be metal equities, such as Hindalco or Tata Steel, which may react positively due to the VALID metal_copper_channel. However, the reaction is already reflected in the price.
- Watch next: dyn_301077_sz (up) — already moved; unexplained move with high z20 level
- Source: Global Market: China stocks rise on AI optimism; Hong Kong shares mostly flat — ET Markets, 2026-08-13. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-rise-on-ai-optimism-hong-kong-shares-mostly-flat/articleshow/133199079.cms
- Historical analogues: 2026-06-18 (d=0.0), 2026-03-30 (d=0.02), 2026-06-03 (d=0.03)

### [RED 4.66] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.62, z20 1.66, zc n/a, resid-z n/a [quiet], 1d -0.41%, 52-wk extreme (pct=98); |z20|=1.66; 1y-pct=98
- **Mechanism**: The midcap_largecap_ratio has reached a 52-wk extreme, with a z20 level of 1.66, indicating a potential mean reversion. However, the resid_z is None, suggesting that the move is largely priced in by factor exposures. The valid channels, such as gold_silver_comove and metal_copper_channel, do not directly relate to the midcap_largecap_ratio, but the vix_equity_inverse channel may influence the broader equity market, including midcaps.
- **Gap**: No gap: the move is largely priced in by factor exposures, as indicated by the None resid_z value
- **India take**: The Nifty Midcap 100 index has already reacted to the midcap_largecap_ratio move, while other transmission candidates like Dyn Bharat Coal and Dyn Fincables have not yet reacted significantly. The Indian metal equities may be influenced by the global copper prices through the metal_copper_channel.
- Watch next: nifty_midcap_100 (down) — already moved; high correlation with midcap_largecap_ratio
- **India receivers**: nifty_midcap_100 (rho 0.535, z 1.06); dyn_bharatcoal_ns (rho 0.404, z -0.93); dyn_fincables_ns (rho 0.397, z 2.31); dyn_pcjeweller_ns (rho 0.364, z 0.27)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

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
- **India receivers**: nifty_fmcg (rho -0.38, z -1.62)
- Source: US stocks: S&P 500 ends higher as CoreWeave results fuel AI optimism — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-sp-500-ends-higher-as-coreweave-results-fuel-ai-optimism/articleshow/133192806.cms
- Source: US stocks: CoreWeave, Super Micro surge on signs of sustained AI buildout — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-coreweave-super-micro-surge-on-signs-of-sustained-ai-buildout/articleshow/133187386.cms
- Source: CoreWeave’s stock is rocketing after earnings lead to praise from bulls and bears alike — MarketWatch Top, 2026-08-12. https://www.marketwatch.com/story/coreweaves-stock-is-rocketing-after-earnings-lead-to-praise-from-bulls-and-bears-alike-46c831e7?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-13 (d=0.01), 2025-08-05 (d=0.04)

### [AMBER 4.31] dyn_fincables_ns ↑
- dyn_fincables_ns [EQUITIES]: last 1246.85, z20 2.31, zc -0.05, resid-z -0.10 [quiet], 1d -0.20%, |z20|=2.31; 1y-pct=99
- **Mechanism**: The recent surge in dyn_fincables_ns, despite being a quiet move with a relatively small resid_z, may propagate through the metal_copper_channel, given its VALID status and moderate correlation with Indian metal equities. This could lead to a reaction in related Indian instruments. However, the WEAK status of relevant channels such as inr_oil_channel and dxy_inr_channel limits the potential transmission mechanisms.
- **Gap**: No gap: the move in dyn_fincables_ns is largely priced, with a small resid_z and a moderate z20 level, indicating that the market has already accounted for the recent surge.
- **India take**: The Indian instrument nifty_midcap_100 has already reacted to the surge in dyn_fincables_ns, while dyn_bharatcoal_ns remains quiet. The midcap_largecap_ratio has also reacted, potentially indicating a broader impact on Indian equities.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to dyn_fincables_ns surge
- **India receivers**: nifty_midcap_100 (rho 0.417, z 1.06); midcap_largecap_ratio (rho 0.397, z 1.66); dyn_bharatcoal_ns (rho 0.38, z -0.93)
- Source: Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410 — BusinessLine Mkts, 2026-08-12. https://www.thehindubusinessline.com/markets/stock-markets/finolex-cables-shares-jump-14-to-52-week-high-jefferies-lift-target-to-1410-maintains-accumulate/article71335064.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-02-19 (d=0.0), 2025-02-07 (d=0.02)

## Watchlist (below surfacing floor)
dyn_ohi ↓ (4.05), nikkei_225 ↑ (3.73), dyn_bac ↑ (3.63), dyn_tatatech_ns ↑ (3.56), btc_usd ↓ (3.54), dyn_atherenerg_ns ↑ (3.33), fx · 2 series ↑ (3.14), dyn_tech ↑ (3.05), dyn_hdb ↓ (2.89), dyn_indusindbk_bo ↑ (2.7), usd_cny ↓ (2.65), indices · 2 series ↑ (2.6)

## India macro
- nifty_50: 24366.0000 (1d -0.12%, z20 0.16, flag none)
- nifty_midcap_100: 63782.6484 (1d -0.53%, z20 1.06, flag amber)
- usd_inr: 95.4150 (1d 0.07%, z20 -0.68, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6177 (1d -0.41%, z20 1.66, flag red)
- Next India prints: India WPI T-0d · NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 103.9 — "Q1 Results Today Live: BDL, Ashok Leyland, 3M India Q1 PAT rise y-o-y, Electrotherm, NATCO"
- INOXINDIA.NS (INOX INDIA LIMITED) score 102.9 — "Q1 Results Today Live: BDL, Ashok Leyland, 3M India Q1 PAT rise y-o-y, Electrotherm, NATCO"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 102.4 — "Q1 Results Today Live: BDL, Ashok Leyland, 3M India Q1 PAT rise y-o-y, Electrotherm, NATCO"
- INDIANB.NS (INDIAN BANK) score 72.7 — "Global Market | Bank of Japan could raise rates in September, eye faster hikes: Reports"
- BAC (Bank of America Corporation) score 57.0 — "Global Market | Bank of Japan could raise rates in September, eye faster hikes: Reports"
- TECHM.NS (TECH MAHINDRA LIMITED) score 56.9 — "Top Gainers & Losers on 14 August: NALCO, HPCL, Tata Motors PV, Netweb Tech, Hindustan Cop"
- COIN (Coinbase Global, Inc.) score 56.0 — "Global Market | Bank of Japan could raise rates in September, eye faster hikes: Reports"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 55.6 — "Top Gainers & Losers on 14 August: NALCO, HPCL, Tata Motors PV, Netweb Tech, Hindustan Cop"
- TECH (Bio-Techne Corp) score 55.0 — "Top Gainers & Losers on 14 August: NALCO, HPCL, Tata Motors PV, Netweb Tech, Hindustan Cop"
- OHI (Omega Healthcare Investors, In) score 53.0 — "Reddit gets S&P 500 boost: What investors need to know"
- HDB (HDFC Bank Limited) score 49.6 — "Global Market | Bank of Japan could raise rates in September, eye faster hikes: Reports"
- CHKP (Check Point Software Technolog) score 47.7 — "Behari Lal Engineering IPO Day 3: Issue booked 93.21x so far. Check GMP, subscriptions, ke"
- IDBI.NS (IDBI BANK LIMITED) score 45.0 — "Global Market | Bank of Japan could raise rates in September, eye faster hikes: Reports"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 45.0 — "Global Market | Bank of Japan could raise rates in September, eye faster hikes: Reports"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 44.8 — "Global Market | Bank of Japan could raise rates in September, eye faster hikes: Reports"
- LTH (Life Time Group Holdings, Inc.) score 37.9 — "Shiprocket IPO Day 3: GMP signals 38% listing premium, subscribed 3.16 times; should you s"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 32.0 — "Tata Steel to sell Jamshedpur Football and Sporting to Churchill club for ₹100"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 30.8 — "Adani Energy Solution shares end 2% higher after acquiring Vizag Power Transmission"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 28.0 — "Tata Steel to sell Jamshedpur Football and Sporting to Churchill club for ₹100"
- BOND (PIMCO Active Bond Exchange-Tra) score 27.7 — "Indian bonds poised for positive start on lower oil prices, Treasury yields"
- 301077.SZ (CHINASTARS) score 27.5 — "Unitree IPO: China’s humanoid robot starset for potentially explosive Shanghai debut"
- JIOFIN.BO (Jio Financial Services Limited) score 20.9 — "Crypto exchanges are evolving into financial superapps; traditional assets emerge as key g"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 18.9 — "Bharat Dynamics Q1 results: Profit sees sixfold increase, revenue surges 131% YoY"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.8 — "Muthoot Fincorp files draft papers for ₹3,000 crore IPO"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 15.8 — "Crypto exchanges are evolving into financial superapps; traditional assets emerge as key g"
- JUSTDIAL.BO (JUST DIAL LTD.) score 14.6 — "DEEPSEEK ANNOUNCES ADJUSTMENT TO API RPICING - STATEMENT"
- MS (Morgan Stanley) score 13.3 — "Tata Motors PV shares fall 5% after weak Q1 results. What are Morgan Stanley, Nomura, othe"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 11.3 — "Bharat Dynamics Q1 results: Profit sees sixfold increase, revenue surges 131% YoY"
- PCJEWELLER.NS (PC JEWELLER LTD) score 9.1 — "Brokerages initiate coverage on Vedanta Aluminium, Kalyan Jewellers, 3 other stocks with u"
- META (Meta) score 8.7 — "Nifty holds above 24,300 at midday as metals, IT drag; bulls eye 24,450"
- NVDA (NVIDIA Corporation) score 8.5 — "Alphabet’s stock slips as Nvidia’s $500 billion financing deal threatens custom chips"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.1 — "Adani Energy Solution shares end 2% higher after acquiring Vizag Power Transmission"
- AAPL (Apple Inc.) score 5.9 — "Nvidia, Apple, Google fuel record $185 billion gain for Norway’s wealth fund, but CEO say,"
- VT (Vanguard Total World Stock Ind) score 5.7 — "China’s next economic ambition: workshop for the Muslim world"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.7 — "Lenskart shares soar after strong Q1 results and MSCI inclusion buzz"
- INTC (Intel Corporation) score 4.4 — "PRESIDENT’S SCHEDULE — AUGUST 13, 2026 🔸 8:00 AM — Executive Time White House · Closed Pre"
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