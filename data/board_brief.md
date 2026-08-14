# Transmission Layer — board brief · 2026-08-14 07:48Z

data as of **2026-08-14** · 98 series · 6 red / 37 amber · 8 events surfaced (21 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.207, 2d in regime; vol-pct 0.248, breadth-off 0.167, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.41, last shift 2026-06-08. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.85, last shift 2026-05-15. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.3, corr60 0.35, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.21, corr60 -0.12, last shift 2026-06-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.73, corr60 -0.8, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.09, corr60 -0.11, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.4, corr60 -0.21, last shift 2026-05-08. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.05, corr60 0.17, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 0.0007248582980661222)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.494** (n=1111) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=2489) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 8.82] cross-asset · 11 series ↑
- russell_2000 [INDICES]: last 3052.63, z20 1.86, zc 0.20, resid-z -0.70 [quiet], 1d 0.23%, |z20|=1.86; 1y-pct=100
- dyn_vt [EQUITIES]: last 162.38, z20 1.83, zc 0.64, resid-z 0.94 [quiet], 1d 0.53%, 1y-pct=100
- dyn_nvda [EQUITIES]: last 225.37, z20 1.78, zc 0.22, resid-z 1.25 [quiet], 1d 0.57%, 1y-pct=99
- nasdaq_100 [INDICES]: last 30085.28, z20 1.75, zc 0.85, resid-z 0.61 [quiet], 1d 1.15%, |z20|=1.75; 1y-pct=96
- sp500 [INDICES]: last 7798.86, z20 1.69, zc 0.81, resid-z -0.45 [quiet], 1d 0.65%, |z20|=1.69; 1y-pct=100
- stoxx_50 [INDICES]: last 6557.73, z20 1.43, zc 0.25, resid-z -0.61 [quiet], 1d 0.19%, 1y-pct=100
- dax [INDICES]: last 26463.87, z20 1.40, zc 0.87, resid-z -0.58 [quiet], 1d 0.62%, 1y-pct=100
- dow_jones [INDICES]: last 53834.58, z20 1.09, zc 0.16, resid-z -1.16 [quiet], 1d 0.12%, 1y-pct=98
- gold_silver_ratio [DERIVED]: last 68.01, z20 -0.94, zc n/a, resid-z n/a [quiet], 1d 1.11%, GSR<75 (extreme low)
- cac_40 [INDICES]: last 8655.24, z20 0.86, zc 0.07, resid-z -0.93 [quiet], 1d 0.05%, 1y-pct=97
- comex_copper [COMMODITIES]: last 6.58, z20 0.73, zc -0.10, resid-z -0.63 [quiet], 1d -0.23%, 1y-pct=96
- **Mechanism**: The current move is driven by the surge in technology stocks, particularly the addition of Reddit to the S&P 500 index, which has led to a record-high close for the S&P 500. This has resulted in a broad-based rally in equities, with the Russell 2000, Nasdaq 100, and Dow Jones all showing significant gains. The gold-silver ratio, which is at an extreme low, also suggests a risk-on environment.
- **Gap**: No gap: The current move in equities is largely priced in, with the resid_z values for most indices and stocks being relatively low, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instruments that express this move are the Nifty Midcap 100 and the Nifty 50, with the former having already reacted and the latter still quiet. The Nifty FMCG has also reacted, driven by its correlation with Dyn NVDA.
- Watch next: nifty_50 (up) — not yet - watch; The Nifty 50 has a correlation of 0.488 with the CAC 40, which has shown a quiet move so far.
- Watch next: nifty_midcap_100 (up) — already moved; The Nifty Midcap 100 has a correlation of 0.5 with the DAX, which has shown a significant move.
- **India receivers**: nifty_fmcg (rho -0.502, z -1.57); nifty_midcap_100 (rho 0.5, z 1.25); nifty_50 (rho 0.488, z 0.08); nifty_metal (rho -0.466, z 0.48)
- Source: Reddit gets S&P 500 boost: What investors need to know — ET Markets, 2026-08-14. https://economictimes.indiatimes.com/markets/us-stocks/news/reddit-gets-sampp-500-boost-what-investors-need-to-know/slideshow/133230670.cms
- Source: Reddit is joining the S&P 500 after months of speculation. Analysts have these concerns. — MarketWatch Top, 2026-08-14. https://www.marketwatch.com/story/reddit-is-joining-the-s-p-500-after-months-of-speculation-analysts-have-these-concerns-21f81f77?mod=mw_rss_topstories
- Source: US stocks: S&P 500 notches record-high close as rate-hike worries ease — ET Markets, 2026-08-13. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-sp-500-notches-record-high-close-as-rate-hike-worries-ease/articleshow/133223873.cms
- Historical analogues: 2024-10-15 (d=0.96), 2024-11-26 (d=0.96), 2024-10-04 (d=0.96)

### [RED 6.12] commodities · 2 series ↑
- corn [COMMODITIES]: last 477.50, z20 3.29, zc 5.15, resid-z -0.92 [moved], 1d 6.58%, |z20|=3.29; 1y-pct=100
- wheat [COMMODITIES]: last 679.00, z20 0.96, zc 2.27, resid-z -0.00 [moved], 1d 4.02%, 1y-pct=98
- **Mechanism**: The recent surge in corn and wheat prices is driven by supply-side disruptions, particularly the USDA's cut in yield expectations due to heat waves, which has led to a risk-on sentiment in the commodities market. This move is priced, given the significant z20 levels and low resid_z values for both corn and wheat, indicating that the price movement is largely explained by factor exposures. The valid gold_silver_comove and metal_copper_channel suggest that the monetary metals and copper are co-moving, which may further support the commodities rally.
- **Gap**: No gap: the recent price move in corn and wheat is largely explained by factor exposures, with low resid_z values indicating that the move is priced
- **India take**: The Indian instrument dyn_lenskart_ns has already reacted, with a z20 value of 3.16, indicating that the transmission of the commodities move to the Indian market is underway. Other Indian metal equities may also be affected through the metal_copper_channel.
- Watch next: soybeans (up) — not yet - watch; high correlation with corn
- **India receivers**: dyn_lenskart_ns (rho 0.407, z 3.16)
- Source: Corn Jumps as USDA Cuts Yield More Than Expected Amid Heat Waves — Mint Markets, 2026-08-12. https://www.livemint.com/market/corn-jumps-as-usda-cuts-yield-more-than-expected-amid-heat-waves-11786572052753.html
- Source: WHEAT JUMPS AFTER RUSSIAN PORT STRIKE Wheat futures surged 2.4% after Ukrainian drones reportedly struck two grain terminals at Russia’s Novorossiysk port. The terminals handle roughly 15 million metric tons of grain exports annually, raising concerns over disruptions to — DeItaone, 2026-08-12. https://t.me/walter_bloomberg/34681
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [AMBER 5.89] commodities · 2 series ↑
- wti [COMMODITIES]: last 82.73, z20 0.05, zc 0.63, resid-z -0.41 [quiet], 1d 1.82%, 1-session move +1.82% ≥ 1.5%
- brent [COMMODITIES]: last 88.39, z20 0.04, zc 0.54, resid-z -0.39 [quiet], 1d 1.52%, 1-session move +1.52% ≥ 1.5%
- **Mechanism**: The recent surge in crude oil prices, driven by the US-Iran deadlock and Russia's record share of India's oil market, is propagating through the VALID metal_copper_channel and the VALID gold_silver_comove, as monetary metals co-move and global copper leads Indian metal equities. However, the resid_z values for WTI and Brent are -0.41 and -0.39, respectively, indicating that the big raw move is largely priced in.
- **Gap**: No gap: the move in crude oil prices is largely priced in, as evidenced by the low resid_z values for WTI and Brent
- **India take**: The Indian instrument that expresses this move is the nifty_midcap_100, which has already reacted to the surge in crude oil prices. The dyn_bharatcoal_ns, on the other hand, remains quiet, with a z20 of -0.84.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to WTI
- **India receivers**: nifty_midcap_100 (rho -0.423, z 1.25); dyn_bharatcoal_ns (rho -0.375, z -0.84)
- Source: Russia Captures Record Share of India’s Oil Market — OilPrice, 2026-08-14. https://oilprice.com/Latest-Energy-News/World-News/Russia-Captures-Record-Share-of-Indias-Oil-Market.html
- Source: Oil Prices Head for 4% Weekly Gain as U.S.-Iran Deadlock Drags On — OilPrice, 2026-08-14. https://oilprice.com/Latest-Energy-News/World-News/Oil-Prices-Head-for-4-Weekly-Gain-as-US-Iran-Deadlock-Drags-On.html
- Source: India’s Russian oil imports hit all-time high in July — BusinessLine Mkts, 2026-08-14. https://www.thehindubusinessline.com/markets/commodities/indias-russian-oil-imports-hit-all-time-high-in-july/article71344169.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 5.16] dyn_lenskart_ns ↑
- dyn_lenskart_ns [EQUITIES]: last 613.35, z20 3.16, zc 2.03, resid-z 1.68 [unexplained], 1d 2.76%, |z20|=3.16; 1y-pct=99
- **Mechanism**: The recent surge in Lenskart Solutions' stock price can be attributed to the company's strong Q1 results, which showed a near four-fold jump in profit, and the buzz around its potential MSCI inclusion. This positive news has led to increased investor interest, driving up the stock price. The VALID metal_copper_channel and vix_equity_inverse channels indicate a risk-on environment, which supports the stock's upward movement.
- **Gap**: No gap: the stock's price move is largely priced in, given the significant increase in profit and positive market sentiment
- **India take**: The Indian instrument that expresses this move is Lenskart Solutions, which has already reacted positively to the news, and other retail-focused stocks may follow suit. The Nifty Retail index may also be affected, potentially leading to a broader market impact.
- Watch next: Lenskart Solutions (up) — already moved; strong Q1 results and MSCI inclusion buzz
- Source: Lenskart Solutions among 7 stocks hitting 52-week highs; surge up to 20% in a month — ET Markets, 2026-08-13. https://economictimes.indiatimes.com/markets/stocks/news/lenskart-solutions-among-7-stocks-hitting-52-week-highs-surge-up-to-20-in-a-month/slideshow/133210592.cms
- Source: Lenskart shares soar after strong Q1 results and MSCI inclusion buzz — BusinessLine Mkts, 2026-08-13. https://www.thehindubusinessline.com/markets/lenskart-shares-zoom-nearly-7-to-fresh-52-week-high-after-strong-q1-results-and-msci-inclusion-buzz/article71339607.ece
- Source: Lenskart shares hit record high after Q1 profit jumps nearly four-fold; Motilal Oswal lifts target price — Mint Markets, 2026-08-13. https://www.livemint.com/market/stock-market-news/lenskart-shares-hit-record-high-after-q1-profit-jumps-nearly-four-fold-motilal-oswal-lifts-target-price-11786610679031.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

### [RED 5.15] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.63, z20 2.15, zc n/a, resid-z n/a [quiet], 1d -0.11%, 52-wk extreme (pct=99); |z20|=2.15; 1y-pct=99
- **Mechanism**: The midcap_largecap_ratio has reached a 52-wk extreme, with a z20 level of 1.97, indicating a potential overvaluation of midcaps relative to largecaps. This move is priced, as evidenced by the resid_z being None, suggesting that the current level is largely explained by factor exposures. The aftermath of similar events has seen a median decline of 1.35% in the midcap_largecap_ratio over the next 20 days. The RISK_ON regime and VALID channels such as gold_silver_comove and metal_copper_channel may influence the propagation of this move.
- **Gap**: No gap: the current level of midcap_largecap_ratio is largely explained by factor exposures, with no unexplained component (resid_z=None)
- **India take**: The Nifty Midcap 100 index has already reacted to this move, with a z20 level of 1.04, while other transmission candidates such as Dyn Fincables NS and Dyn IndianB NS have also reacted, with z20 levels of 2.41 and 1.4, respectively.
- Watch next: nifty_midcap_100 (down) — already moved; high correlation with midcap_largecap_ratio
- **India receivers**: nifty_midcap_100 (rho 0.53, z 1.25); dyn_bharatcoal_ns (rho 0.405, z -0.84); dyn_fincables_ns (rho 0.396, z 2.51); dyn_pcjeweller_ns (rho 0.371, z -0.01)
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
- **Mechanism**: rates · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.815 vs ust_30y, historically leads by 1d
- Watch next: brent (co-move) — not yet - watch; rho 0.534 vs ust_30y, historically leads by 3d
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.513 vs ust_30y, historically leads by 1d
- Watch next: wti (co-move) — not yet - watch; rho 0.508 vs ust_10y, historically leads by 3d
- Watch next: dyn_hdb (inverse) — not yet - watch; rho -0.521 vs tips_10y_real
- Source: AI-driven surge in bond yields could be next risk for markets and growth — BusinessLine Mkts, 2026-08-14. https://www.thehindubusinessline.com/markets/ai-driven-surge-in-bond-yields-could-be-next-risk-for-markets-and-growth/article71344109.ece
- Source: Indian bonds poised for positive start on lower oil prices, Treasury yields — BusinessLine Mkts, 2026-08-14. https://www.thehindubusinessline.com/markets/indian-bonds-poised-for-positive-start-on-lower-oil-prices-treasury-yields/article71343962.ece
- Source: Global Market: Japanese bond yields hold near highs as markets brace for BOJ rate hike — ET Markets, 2026-08-13. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japanese-bond-yields-hold-near-highs-as-markets-brace-for-boj-rate-hike/articleshow/133203276.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.25), 2026-03-30 (d=0.31)

### [RED 4.51] dyn_fincables_ns ↑
- dyn_fincables_ns [EQUITIES]: last 1264.45, z20 2.51, zc 0.29, resid-z 0.35 [quiet], 1d 1.21%, |z20|=2.51; 1y-pct=99
- **Mechanism**: The recent surge in dyn_fincables_ns, despite being a big raw move, is largely priced in with a small resid_z of 0.35, indicating that the move is mostly explained by factor exposures. The metal_copper_channel, which is currently valid, may play a role in transmitting this move to Indian metal equities. However, the lack of a clear channel for direct transmission to Indian markets means the mechanism is not straightforward.
- **Gap**: No gap: the move in dyn_fincables_ns is largely priced in with a small resid_z, indicating no significant anomaly.
- **India take**: The Indian instrument nifty_midcap_100, which has a rho of 0.414 with dyn_fincables_ns, has already reacted to the move. Additionally, midcap_largecap_ratio has also reacted, while dyn_bharatcoal_ns remains quiet.
- Watch next: nifty_midcap_100 (down) — already moved; rho=0.414 via dyn_fincables_ns
- **India receivers**: nifty_midcap_100 (rho 0.414, z 1.25); midcap_largecap_ratio (rho 0.396, z 2.15); dyn_bharatcoal_ns (rho 0.38, z -0.84)
- Source: Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410 — BusinessLine Mkts, 2026-08-12. https://www.thehindubusinessline.com/markets/stock-markets/finolex-cables-shares-jump-14-to-52-week-high-jefferies-lift-target-to-1410-maintains-accumulate/article71335064.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-02-19 (d=0.0), 2025-02-07 (d=0.02)

## Watchlist (below surfacing floor)
dyn_crwv ↑ (4.42), dyn_ohi ↓ (4.05), dyn_cupid_ns ↑ (3.97), nikkei_225 ↑ (3.73), comex_gold ↑ (3.69), dyn_bac ↑ (3.63), dyn_tatatech_ns ↑ (3.5), dyn_atherenerg_ns ↑ (3.39), dyn_tech ↑ (3.05), fx · 2 series ↑ (3.01), dyn_hdb ↓ (2.89), dyn_lth ↑ (2.59)

## India macro
- nifty_50: 24344.0996 (1d -0.21%, z20 0.08, flag none)
- nifty_midcap_100: 63916.9492 (1d -0.32%, z20 1.25, flag amber)
- usd_inr: 95.4225 (1d 0.08%, z20 -0.66, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6256 (1d -0.11%, z20 2.15, flag red)
- Next India prints: India WPI T-0d · NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 104.2 — "India's coal demand seen at 1.6 billion tonnes by 2030 as govt pushes market-driven trade:"
- INOXINDIA.NS (INOX INDIA LIMITED) score 103.2 — "India's coal demand seen at 1.6 billion tonnes by 2030 as govt pushes market-driven trade:"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 102.7 — "India's coal demand seen at 1.6 billion tonnes by 2030 as govt pushes market-driven trade:"
- INDIANB.NS (INDIAN BANK) score 72.0 — "How Indian stock market evolved since 1991: Sensex’s journey from 1,000 to 86,000"
- TECHM.NS (TECH MAHINDRA LIMITED) score 56.7 — "Jefferies’ Chris Wood spots a hidden risk in Big Tech’s $165 billion AI capex race"
- BAC (Bank of America Corporation) score 55.8 — "Quest Global said to pick banks for $1 billion India IPO"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 55.4 — "Jefferies’ Chris Wood spots a hidden risk in Big Tech’s $165 billion AI capex race"
- OHI (Omega Healthcare Investors, In) score 54.7 — "Reddit gets S&P 500 boost: What investors need to know"
- TECH (Bio-Techne Corp) score 54.7 — "Jefferies’ Chris Wood spots a hidden risk in Big Tech’s $165 billion AI capex race"
- COIN (Coinbase Global, Inc.) score 53.7 — "Global Market: China, Hong Kong stocks fall as liquidity tightens ahead of Unitree IPO"
- HDB (HDFC Bank Limited) score 49.2 — "Honasa shares hit 52-week high as JM Financial, HDFC Securities turn bullish"
- CHKP (Check Point Software Technolog) score 47.2 — "Behari Lal Engineering IPO Day 3: Issue booked 29.88x so far. Check GMP, subscriptions, ke"
- IDBI.NS (IDBI BANK LIMITED) score 44.4 — "Quest Global said to pick banks for $1 billion India IPO"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 44.4 — "Quest Global said to pick banks for $1 billion India IPO"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 44.2 — "Quest Global said to pick banks for $1 billion India IPO"
- LTH (Life Time Group Holdings, Inc.) score 39.1 — "Shiprocket IPO Day 3: GMP signals 38% listing premium, subscribed 3.16 times; should you s"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 30.8 — "OpenAI revenue doubles to over $40 billion as IPO plans gather pace"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 30.0 — "Stocks to watch: Ashok Leyland, Bharat Dynamics, Tata Motors PV among shares in focus toda"
- BOND (PIMCO Active Bond Exchange-Tra) score 28.6 — "Indian bonds poised for positive start on lower oil prices, Treasury yields"
- 301077.SZ (CHINASTARS) score 27.4 — "Global Market: China, Hong Kong stocks fall as liquidity tightens ahead of Unitree IPO"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 25.8 — "Stocks to watch: Ashok Leyland, Bharat Dynamics, Tata Motors PV among shares in focus toda"
- JIOFIN.BO (Jio Financial Services Limited) score 20.5 — "Britannia Share Price Live Updates: Britannia's Financial Snapshot"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 17.4 — "Explained: Why Balrampur Chini, Dhampur Sugar, Dalmia Bharat & other sugar stocks are up 1"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 17.4 — "Muthoot Fincorp files draft papers for ₹3,000 crore IPO"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 15.3 — "Britannia Share Price Live Updates: Britannia's Financial Snapshot"
- JUSTDIAL.BO (JUST DIAL LTD.) score 15.1 — "DEEPSEEK ANNOUNCES ADJUSTMENT TO API RPICING - STATEMENT"
- MS (Morgan Stanley) score 13.7 — "Tata Motors PV shares fall 5% after weak Q1 results. What are Morgan Stanley, Nomura, othe"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 9.6 — "Explained: Why Balrampur Chini, Dhampur Sugar, Dalmia Bharat & other sugar stocks are up 1"
- PCJEWELLER.NS (PC JEWELLER LTD) score 9.4 — "Brokerages initiate coverage on Vedanta Aluminium, Kalyan Jewellers, 3 other stocks with u"
- META (Meta) score 9.0 — "Nifty holds above 24,300 at midday as metals, IT drag; bulls eye 24,450"
- NVDA (NVIDIA Corporation) score 8.8 — "Alphabet’s stock slips as Nvidia’s $500 billion financing deal threatens custom chips"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.3 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Achieves Significant Price Movem"
- AAPL (Apple Inc.) score 6.1 — "Nvidia, Apple, Google fuel record $185 billion gain for Norway’s wealth fund, but CEO say,"
- VT (Vanguard Total World Stock Ind) score 5.9 — "China’s next economic ambition: workshop for the Muslim world"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.9 — "Lenskart shares soar after strong Q1 results and MSCI inclusion buzz"
- INTC (Intel Corporation) score 4.5 — "PRESIDENT’S SCHEDULE — AUGUST 13, 2026 🔸 8:00 AM — Executive Time White House · Closed Pre"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 2.5 — "ICICI Bank Share Price Live Updates: ICICI Bank Stock Details"
- CRWV (CoreWeave, Inc.) score 2.0 — "US stocks: S&P 500 ends higher as CoreWeave results fuel AI optimism"
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