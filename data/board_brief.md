# Transmission Layer — board brief · 2026-07-28 06:46Z

data as of **2026-07-28** · 98 series · 9 red / 37 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.493, 3d in regime; vol-pct 0.487, breadth-off 0.5, Markov P(high-vol) 0.032)
- [INVERTED] **safe_haven_gold** — corr20 -0.36, corr60 -0.45, contra nifty_50 corr20=0.07, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.9, corr60 0.82, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.36, corr60 0.36, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.15, corr60 -0.03, last shift 2026-06-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.82, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.19, corr60 -0.07, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.07, corr60 -0.25, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.54, corr60 0.24, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.49** (n=1149) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=3205) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.74] dyn_coalindia_ns ↓
- dyn_coalindia_ns [EQUITIES]: last 412.40, z20 -4.74, zc -3.26, resid-z 0.09 [moved], 1d -3.53%, |z20|=4.74
- **Mechanism**: The recent decline in Coal India's stock price can be attributed to the company's weak operating performance, higher costs, and weaker-than-expected realisations in its Q1FY27 results. This news has led to a priced move, with the stock's resid_z being relatively small at 0.09, indicating that the move is largely explained by factor exposures. The metal_copper_channel, which is currently valid, may also play a role in transmitting global copper price movements to Indian metal equities, including Coal India.
- **Gap**: No gap: The stock's decline is largely explained by its weak Q1FY27 results and is consistent with the current market expectations, leaving no significant event-to-price gap.
- **India take**: The Indian instrument that expresses this move is Coal India itself, and it has already reacted to the news with a decline in its stock price. Other metal stocks in the Indian market may also be affected, particularly those with exposure to the copper market.
- Watch next: nifty_50 (down) — not yet - watch; Weaker-than-expected earnings from a key stock like Coal India could weigh on the broader market
- Source: Coal India shares fall over 3% weighed by weak operating performance — BusinessLine Mkts, 2026-07-28. https://www.thehindubusinessline.com/markets/coal-india-shares-fall-over-3-after-q1-results-weak-operating-performance-weighs-on-stock/article71275552.ece
- Source: Coal India shares fall 2% after Q1 results. What are Jefferies, other brokerages saying? — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/news/coal-india-shares-fall-2-after-q1-results-what-are-jefferies-other-brokerages-saying/articleshow/132674703.cms
- Source: Coal India Share Price Live Updates: Coal India Ltd Stock Details — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/coal-india-ltd-stock-price-livestock-price-today-live-updates-28-jul-2026/liveblog/132673965.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.03), 2024-11-07 (d=0.04)

### [RED 6.25] indices · 3 series ↓
- nikkei_225 [INDICES]: last 62313.21, z20 -2.93, zc -1.93, resid-z -1.34 [moved], 1d -4.03%, |z20|=2.93
- taiwan_weighted [INDICES]: last 41635.37, z20 -2.77, zc -1.98, resid-z -1.40 [moved], 1d -4.58%, |z20|=2.77
- kospi [INDICES]: last 6019.06, z20 -2.17, zc -2.49, resid-z -1.43 [moved], 1d -10.90%, |z20|=2.17
- **Mechanism**: The sharp decline in Japanese chip stocks, led by major chipmakers such as Kioxia, Tokyo Electron, and Advantest, has triggered a broader selloff in the Nikkei index, which has subsequently transmitted to other Asian markets, including Taiwan and Korea. This move is largely priced, given the relatively small resid_z values for the affected indices. The valid metal_copper_channel and vix_equity_inverse channels may also be contributing to the transmission of this move to Indian metal equities.
- **Gap**: No gap: the move in Nikkei and other Asian indices is largely priced, with small resid_z values indicating that the decline is largely explained by factor exposures.
- **India take**: Indian metal equities, such as those tracked by the nifty_metal index, have already reacted to the decline in Asian markets, with a rho of 0.491 with the kospi index. Other Indian transmission candidates, such as dyn_hdbfs_bo and dyn_techm_ns, have also reacted to the move in their respective correlated indices.
- Watch next: nifty_metal (down) — already moved; rho=0.491 with kospi
- **India receivers**: nifty_metal (rho 0.491, z -1.14); dyn_hdbfs_bo (rho 0.473, z -2.45); dyn_techm_ns (rho -0.418, z 2.17); dyn_pcjeweller_ns (rho 0.364, z -0.89)
- Source: Global Market: Japan’s Nikkei plunges over 4% as chip stocks track global tech selloff — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-plunges-over-4-as-chip-stocks-track-global-tech-selloff/articleshow/132676159.cms
- Source: Japan’s Nikkei tumbles over 3% as chip stock selloff deepens after Wall Street decline — BusinessLine Mkts, 2026-07-28. https://www.thehindubusinessline.com/markets/stock-markets/japans-nikkei-tumbles-over-3-as-chip-stock-selloff-deepens-after-wall-street-decline/article71275340.ece
- Source: Global Markets: Japan's Nikkei rises as oil falls before key earnings — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/us-stocks/news/global-markets-japans-nikkei-rises-as-oil-falls-before-key-earnings/articleshow/132654861.cms

### [AMBER 5.96] cross-asset · 5 series ↑
- ust_2y [RATES]: last 4.33, z20 2.03, zc -0.71, resid-z -1.16 [quiet], 1d -0.92%, |z20|=2.03; 1y-pct=99
- tips_10y_real [RATES]: last 2.43, z20 1.85, zc 0.00, resid-z -0.30 [quiet], 1d 0.00%, |z20|=1.85; 1y-pct=99
- ust_10y [RATES]: last 4.69, z20 1.72, zc -0.44, resid-z -0.72 [quiet], 1d -0.42%, |z20|=1.72; 1y-pct=99
- ust_30y [RATES]: last 5.16, z20 1.38, zc -0.30, resid-z -0.44 [quiet], 1d -0.19%, 1y-pct=99
- dyn_bond [EQUITIES]: last 90.79, z20 -1.09, zc 0.45, resid-z 0.09 [quiet], 1d 0.25%, 1y-pct=2
- **Mechanism**: The recent surge in US interest rates and uncertainty about Fed policy outlook have led to a rise in demand for swaptions, indicating growing apprehensions among bond investors. This has resulted in a priced move in US Treasury yields, with the 2-year, 10-year, and 30-year yields increasing. The move is largely explained by factor exposures, with small resid_z values indicating that the move is priced in.
- **Gap**: No gap: The move in US Treasury yields is largely explained by factor exposures, with small resid_z values indicating that the move is priced in.
- **India take**: The Indian 10-year bond yield has logged its biggest plunge in 2 months as the oil rally falters, and may react further to the priced move in US Treasury yields. Indian instruments such as the 10-year GoI bond may see increased demand due to the uncertainty about Fed policy outlook.
- Watch next: ust_2y (up) — already moved; Priced move due to rising interest rates and uncertainty about Fed policy
- Watch next: tips_10y_real (up) — already moved; Priced move due to rising interest rates and uncertainty about Fed policy
- Watch next: ust_10y (up) — already moved; Priced move due to rising interest rates and uncertainty about Fed policy
- Watch next: ust_30y (up) — already moved; Priced move due to rising interest rates and uncertainty about Fed policy
- Source: JPMORGAN TURNS BULLISH ON STOCKS JPMorgan said its tactical positioning monitor is flashing a buy signal, pointing to further upside for the S&P 500. The bank expects lower bond yields, a weaker dollar, steady Fed policy, and strong earnings to support equities, while warning — DeItaone, 2026-07-27. https://t.me/walter_bloomberg/33969
- Source: Bond investors, unsure about Fed policy outlook, hedge against US rate shock — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/bonds/bond-investors-unsure-about-fed-policy-outlook-hedge-against-us-rate-shock/articleshow/132665831.cms
- Source: India 10-year bond yield logs biggest plunge in 2 months as oil rally falters — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/bonds/india-10-year-bond-yield-logs-biggest-plunge-in-2-months-as-oil-rally-falters/articleshow/132661306.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.88] cross-asset · 3 series ↑
- nifty_it [INDICES]: last 30643.35, z20 2.56, zc 2.46, resid-z 0.78 [moved], 1d 4.08%, |z20|=2.56
- dyn_techm_ns [EQUITIES]: last 1637.50, z20 2.17, zc 2.14, resid-z 0.57 [moved], 1d 3.97%, |z20|=2.17
- dyn_tataelxsi_ns [EQUITIES]: last 3611.50, z20 0.08, zc 0.53, resid-z 2.70 [unexplained], 1d 1.61%, 1y-pct=4
- **Mechanism**: The recent move in Nifty IT and associated equities such as Dyn Techm and Dyn Tata Elxsi is largely priced, given the relatively low resid_z values. However, the unexplained component in Dyn Tata Elxsi, with a high resid_z of 2.7, suggests potential for further movement. The valid channels, such as gold_silver_comove and metal_copper_channel, do not directly influence the current move but indicate a broader risk-on environment.
- **Gap**: No gap: the current move in Nifty IT and associated equities is largely priced, with small resid_z values indicating that the big raw move is already reflected in prices.
- **India take**: The Indian instruments that express this move are Nifty IT and associated equities such as Dyn Techm and Dyn Tata Elxsi. While Nifty IT has already reacted, Dyn Tata Elxsi, with its high resid_z, is one to watch for potential further movement. Transmission candidates like Dyn Patanjali NS have already reacted, while others like Dyn Jiofin BO remain quiet.
- Watch next: nifty_it (up) — already moved; momentum above 55-day EMA
- Watch next: dyn_techm_ns (up) — already moved; follows Nifty IT momentum
- Watch next: dyn_tataelxsi_ns (up) — not yet - watch; unexplained move with high resid_z
- **India receivers**: dyn_patanjali_ns (rho 0.414, z -1.1); dyn_jiofin_bo (rho 0.392, z -0.1); nifty_50 (rho 0.362, z -0.4)
- Source: Tech Mahindra Share Price Live Updates: Tech Mahindra's Stock Surges Past Resistance — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tech-mahindra-stock-price-live-updates-28-jul-2026/liveblog/132674133.cms
- Source: Stocks to buy for short term: BHEL, Mahindra and Mahindra among 6 stocks experts recommend for next 1-2 weeks — Mint Markets, 2026-07-28. https://www.livemint.com/market/stock-market-news/stocks-to-buy-for-short-term-bhel-mahindra-and-mahindra-among-6-stocks-experts-recommend-for-next-1-2-weeks-11785165963810.html
- Historical analogues: 2025-08-13 (d=0.78), 2025-01-23 (d=0.84), 2025-12-30 (d=0.85)

### [AMBER 5.49] brent ↑
- brent [COMMODITIES]: last 86.89, z20 0.49, zc -0.45, resid-z -1.22 [quiet], 1d -1.66%, 1-session move -1.66% ≥ 1.5%
- **Mechanism**: The recent rise in Brent crude oil prices may propagate through the metal_copper_channel, as global copper leads Indian metal equities, potentially impacting the Indian market. However, the inr_oil_channel is weak, which may limit the transmission of oil price movements to the Indian rupee. The vix_equity_inverse channel is valid, suggesting that a vol spike could lead to an equity drawdown, but its relevance to the current oil price move is uncertain.
- **Gap**: No gap: the move in Brent crude oil prices is largely priced, with a small resid_z of -1.22, indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian instrument that may express this move is the Nifty Midcap 100, which has a correlation of -0.618 with Brent crude oil prices, but it has not reacted yet. The Nifty 50 and Dyn Jiofin BO are also potential transmission candidates, but they are quiet for now.
- Watch next: nifty_midcap_100 (down) — not yet - watch; correlated with Brent crude oil prices
- **India receivers**: nifty_midcap_100 (rho -0.618, z -0.03); nifty_50 (rho -0.458, z -0.4); dyn_jiofin_bo (rho -0.456, z -0.1)
- Source: Saudi Arabia Weighs Higher Asia Crude Prices as Red Sea Shipping Costs Rise — OilPrice, 2026-07-28. https://oilprice.com/Latest-Energy-News/World-News/Saudi-Arabia-Weighs-Higher-Asia-Crude-Prices-as-Red-Sea-Shipping-Costs-Rise.html
- Source: Govt bonds rise as oil, US yields fall; state supply looms — BusinessLine Mkts, 2026-07-28. https://www.thehindubusinessline.com/markets/stock-markets/govt-bonds-rise-as-oil-us-yields-fall-state-supply-looms/article71275644.ece
- Source: Australia weighs first new oil refinery in over 60 years to strengthen energy security — BusinessLine Mkts, 2026-07-28. https://www.thehindubusinessline.com/news/world/australia-weighs-first-new-oil-refinery-in-over-60-years-to-strengthen-energy-security/article71275426.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.0), 2024-10-18 (d=0.02)

### [AMBER 5.18] indices · 2 series ↑
- nasdaq_100 [INDICES]: last 28036.41, z20 -2.35, zc -0.79, resid-z -1.60 [unexplained], 1d -0.33%, |z20|=2.35
- vix [INDICES]: last 18.67, z20 1.53, zc -0.06, resid-z n/a [quiet], 1d 0.48%, |z20|=1.53
- **Mechanism**: The Nasdaq 100's unexplained move is driven by easing US-Iran tensions, which have improved investor risk appetite, as evidenced by the sharp increase in US stock futures. This risk-on sentiment is likely to propagate through the valid vix_equity_inverse channel, where a vol spike typically leads to an equity drawdown, but in this case, the vol spike is absent, and equities are rising. The metal_copper_channel may also play a role, as global copper leads Indian metal equities, and the improved risk appetite could boost copper prices, which in turn could support Indian metal equities.
- **Gap**: No gap: The Nasdaq 100's move is largely priced, with a resid_z of -1.6, indicating that the majority of the move can be explained by factor exposures, and the remaining unexplained component is not unusually large.
- **India take**: The Indian instrument that expresses this move is the Nifty 50, which may react positively to the improved risk appetite and potential boost to copper prices. However, it has not yet reacted, and its response is worth watching.
- Watch next: nifty_50 (up) — not yet - watch; Improved risk appetite and potential boost to copper prices
- Source: US stock market today: S&P 500, Nasdaq futures jump up to 1.7% as oil prices tumble on easing US-Iran tensions — Mint Markets, 2026-07-27. https://www.livemint.com/market/stock-market-news/us-stock-market-today-s-p-500-nasdaq-futures-jump-up-to-1-7-as-oil-prices-tumble-on-easing-us-iran-tensions-11785151956723.html
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US market opens higher as pause in US-Iran hostilities lifts sentiment — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-fed-warsh-microsoft-amazon-meta-alphabet-tesla-chip-stock-price-news-27th-july-2026/liveblog/132661511.cms
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US market edges lower as chip stocks tumble ahead of earnings session — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-fed-warsh-microsoft-amazon-meta-alphabet-tesla-chip-stock-price-news-27th-july-2026/liveblog/132661511.cms
- Historical analogues: 2026-05-04 (d=0.12), 2025-10-23 (d=0.14), 2026-05-20 (d=0.14)

### [RED 5.18] dyn_lth ↑
- dyn_lth [EQUITIES]: last 43.75, z20 3.18, zc 0.45, resid-z -0.11 [quiet], 1d 3.35%, |z20|=3.18; 1y-pct=100
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: HUL shares slide 5% after weaker-than-expected Q1; PAT dips 3% to Rs 2,673 crore on one-time credit — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/news/hul-shares-slide-5-after-weaker-than-expected-q1-pat-dips-3-to-rs-2673-crore-on-one-time-credit/articleshow/132676380.cms
- Source: TRUMP: LET'S GET RID OF DAYLIGHT SAVINGS TIME — DeItaone, 2026-07-27. https://t.me/walter_bloomberg/33971
- Source: ‘Time will tell whether that was a good bet’: My adviser got me a full SpaceX IPO allocation. Was I lucky? — MarketWatch Top, 2026-07-27. https://www.marketwatch.com/story/time-will-tell-whether-that-was-a-good-bet-my-adviser-got-me-a-full-spacex-ipo-allocation-was-i-lucky-7f319645?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.01), 2025-04-17 (d=0.02)

### [RED 5.09] dyn_eternal_ns ↑
- dyn_eternal_ns [EQUITIES]: last 305.40, z20 3.09, zc 1.57, resid-z -1.21 [moved], 1d 3.23%, |z20|=3.09
- **Mechanism**: dyn_eternal_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.601 via dyn_eternal_ns, z -0.03, quiet); dyn_jiofin_bo (rho 0.522 via dyn_eternal_ns, z -0.1, quiet); nifty_50 (rho 0.51 via dyn_eternal_ns, z -0.4, quiet); dyn_havells_ns (rho 0.458 via dyn_eternal_ns, z 1.49, reacted); dyn_indusindbk_bo (rho 0.456 via dyn_eternal_ns, z -0.1, quiet)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.601 vs dyn_eternal_ns, historically leads by 4d
- Watch next: dyn_jiofin_bo (co-move) — not yet - watch; rho 0.522 vs dyn_eternal_ns, historically leads by 3d
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.51 vs dyn_eternal_ns, historically leads by 4d
- **India receivers**: nifty_midcap_100 (rho 0.601, z -0.03); dyn_jiofin_bo (rho 0.522, z -0.1); nifty_50 (rho 0.51, z -0.4); dyn_havells_ns (rho 0.458, z 1.49)
- Source: Eternal among 4 stocks flashing bullish signals, hinting at a possible uptrend — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/news/eternal-among-4-stocks-flashing-bullish-signals-hinting-at-a-possible-uptrend/slideshow/132674117.cms
- Source: Market wrap: Eternal, HDFC Bank, Infosys among top gainers and losers on Nifty and Sensex on Monday — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-eternal-hdfc-bank-infosys-among-top-gainers-and-losers-on-nifty-and-sensex-on-monday/articleshow/132660092.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-28 (d=0.02), 2026-06-30 (d=0.04)

## Watchlist (below surfacing floor)
dyn_cartrade_ns ↑ (5.03), dyn_infy ↑ (4.48), indices · 3 series ↑ (3.99), dyn_ohi ↑ (3.93), gold_silver_ratio ↑ (3.88), dyn_hdb ↓ (3.75), asx_200 ↑ (3.62), natgas ↓ (3.61), dyn_bac ↑ (3.55), dyn_301077_sz ↓ (3.29), commodities · 2 series ↑ (3.02), dyn_tech ↑ (2.8)

## India macro
- nifty_50: 24026.7500 (1d 0.13%, z20 -0.40, flag none)
- nifty_midcap_100: 62347.8008 (1d 0.10%, z20 -0.03, flag none)
- usd_inr: 95.7425 (1d -0.85%, z20 -0.31, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5949 (1d -0.03%, z20 0.41, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 71.4 — "MACQUARIE SEES OIL GLUT ON US-IRAN DEAL Macquarie expects the oil market to swing into sur"
- INOXINDIA.NS (INOX INDIA LIMITED) score 62.3 — "Stock recommendations for 28 July from MarketSmith India"
- BAC (Bank of America Corporation) score 60.4 — "MACQUARIE SEES OIL GLUT ON US-IRAN DEAL Macquarie expects the oil market to swing into sur"
- HDB (HDFC Bank Limited) score 59.5 — "MACQUARIE SEES OIL GLUT ON US-IRAN DEAL Macquarie expects the oil market to swing into sur"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 57.3 — "MACQUARIE SEES OIL GLUT ON US-IRAN DEAL Macquarie expects the oil market to swing into sur"
- IDBI.NS (IDBI BANK LIMITED) score 54.9 — "MACQUARIE SEES OIL GLUT ON US-IRAN DEAL Macquarie expects the oil market to swing into sur"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 51.1 — "Stock recommendations for 28 July from MarketSmith India"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 49.6 — "Poonawalla Vision Fund invests ₹230 crore in Lohum Cleantech"
- TECHM.NS (TECH MAHINDRA LIMITED) score 49.4 — "Stocks to buy for short term: BHEL, Mahindra and Mahindra among 6 stocks experts recommend"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 46.3 — "MACQUARIE SEES OIL GLUT ON US-IRAN DEAL Macquarie expects the oil market to swing into sur"
- COALINDIA.NS (COAL INDIA LTD) score 42.5 — "Stock recommendations for 28 July from MarketSmith India"
- COIN (Coinbase Global, Inc.) score 42.3 — "US stocks to Asian markets today: Global equity heatmap you may like to know before Dalal "
- OHI (Omega Healthcare Investors, In) score 25.9 — "Global Market: Samsung, SK Hynix plunge up to 11% as investors reassess AI chip boom"
- BOND (PIMCO Active Bond Exchange-Tra) score 22.0 — "Govt bonds rise as oil, US yields fall; state supply looms"
- CHKP (Check Point Software Technolog) score 21.9 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 2"
- LTH (Life Time Group Holdings, Inc.) score 21.4 — "TRUMP: LET'S GET RID OF DAYLIGHT SAVINGS TIME"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 18.7 — "Australia weighs first new oil refinery in over 60 years to strengthen energy security"
- TECH (Bio-Techne Corp) score 16.8 — "Poonawalla Vision Fund invests ₹230 crore in Lohum Cleantech"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 14.2 — "Tata Motors PV Share Price Live Updates: Tata Motors PV Stock Details"
- INFY (Infosys Limited) score 12.2 — "Infosys Share Price Live Updates: Sensex trades flat, Nifty near 24,000 ahead of US Fed me"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.8 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Current Price Update"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 10.7 — "Coal India Share Price Live Updates: Coal India Ltd Stock Details"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.4 — "Global markets: Shein will struggle to justify up to $50 billion Hong Kong IPO valuation"
- VT (Vanguard Total World Stock Ind) score 7.9 — "TRUMP ON FED: WE SHOULD HAVE WORLD'S LOWEST INTEREST RATE"
- JIOFIN.BO (Jio Financial Services Limited) score 7.8 — "AMZN - AMAZON: LEO WILL PARTNER WITH MOBILE NETWORK OPERATORS TO EXTEND MOBILE CONNECTIVIT"
- META (Meta) score 7.4 — "Metalic Technoforge SME IPO listing: Shares list at a 13% premium to the issue price, trim"
- MS (Morgan Stanley) score 7.0 — "MORGAN STANLEY RAISES ISM FORECAST Morgan Stanley lifted its July ISM Manufacturing PMI fo"
- GS (Goldman Sachs Group, Inc. (The) score 6.3 — "GOLDMAN WARNS MACRO RISKS RISING Goldman Sachs said rising oil volatility is shifting inve"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 6.0 — "From financials to industrials: Here's how Nifty 500 composition has shifted over the year"
- 301077.SZ (CHINASTARS) score 5.7 — "South Korea’s KOSPI falls over 7% as China chip threat hits SK Hynix, Samsung"
- NVDA (NVIDIA Corporation) score 5.6 — "TCS, Infosys, Coforge, other IT stocks rally up to 10% after Nvidia-led chip rout. Is AI t"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.6 — "ICICI Bank Share Price Highlights: ICICI Bank Stock Price History"
- ETERNAL.NS (ETERNAL LIMITED) score 4.7 — "Eternal among 4 stocks flashing bullish signals, hinting at a possible uptrend"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 3.7 — "India’s electricity shortages more than doubled during January-May 2026: IEA"
- PCJEWELLER.NS (PC JEWELLER LTD) score 2.9 — "Sebi clears IPOs of Intellius Recode, Nityas Gems & Jewellery"
- 688188.SS (SHANGHAI BOCHU ELECTRONIC TECH) score 2.5 — "China's memory chipmaker CXMT shares soar in its blockbuster share listing in Shanghai"
- AAPL (Apple Inc.) score 1.6 — "FORD WILL USE APPLE SOFTWARE IN NEW SELF-DRIVING SYSTEM: NYT"
- NFLX (Netflix, Inc.) score 1.5 — "Losing Wall Street binge premium! Why are Netflix shares in a freefall this year?"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 0.5 — "Newly-listed SME stock DSM Fresh Foods jumps over 30% in 2 days after reporting a 58% YoY "
- CUPID.NS (CUPID LIMITED) score 0.1 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"

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