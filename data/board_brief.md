# Transmission Layer — board brief · 2026-07-28 11:39Z

data as of **2026-07-28** · 98 series · 10 red / 35 amber · 8 events surfaced (28 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.523, 3d in regime; vol-pct 0.713, breadth-off 0.333, Markov P(high-vol) 0.032)
- [INVERTED] **safe_haven_gold** — corr20 -0.32, corr60 -0.45, contra nifty_50 corr20=0.08, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.9, corr60 0.82, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.36, corr60 0.36, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.16, corr60 -0.03, last shift 2026-06-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.82, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.23, corr60 -0.08, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.07, corr60 -0.25, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.4, corr60 0.24, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.49** (n=1149) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=3179) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.25] dyn_coalindia_ns ↓
- dyn_coalindia_ns [EQUITIES]: last 410.40, z20 -5.25, zc -3.70, resid-z -2.42 [unexplained], 1d -4.00%, |z20|=5.25
- **Mechanism**: The decline in Coal India's shares is driven by weak operating performance, higher costs, and weaker-than-expected realisations, as flagged by brokerages. This move is unexplained by factor exposures, with a resid_z of -2.42. The metal_copper_channel, which is VALID, may transmit this move to other Indian metal equities. However, the lack of a clear channel for oil and INR may limit the transmission to other Indian instruments.
- **Gap**: No gap: the move in Coal India's shares is largely priced in, given the weak operating performance and brokerages' negative commentary
- **India take**: The Indian instrument that expresses this move is Coal India itself, which has already reacted with a 4% decline. Other metal equities, such as those in the Nifty Metal index, may also be affected.
- Watch next: nifty_metal (down) — not yet - watch; Coal India's weak operating performance may impact other metal stocks
- Source: Coal India shares fall 4% weighed by weak operating performance — BusinessLine Mkts, 2026-07-28. https://www.thehindubusinessline.com/markets/coal-india-shares-fall-over-3-after-q1-results-weak-operating-performance-weighs-on-stock/article71275552.ece
- Source: Coal India shares fall over 3% weighed by weak operating performance — BusinessLine Mkts, 2026-07-28. https://www.thehindubusinessline.com/markets/coal-india-shares-fall-over-3-after-q1-results-weak-operating-performance-weighs-on-stock/article71275552.ece
- Source: Coal India shares fall 2% after Q1 results. What are Jefferies, other brokerages saying? — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/news/coal-india-shares-fall-2-after-q1-results-what-are-jefferies-other-brokerages-saying/articleshow/132674703.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.03), 2024-11-07 (d=0.04)

### [AMBER 6.36] commodities · 2 series ↑
- wti [COMMODITIES]: last 81.34, z20 0.52, zc -0.48, resid-z -0.93 [quiet], 1d -1.54%, 1-session move -1.54% ≥ 1.5%
- brent [COMMODITIES]: last 86.63, z20 0.46, zc -0.52, resid-z -1.22 [quiet], 1d -1.96%, 1-session move -1.96% ≥ 1.5%
- **Mechanism**: The decline in oil prices, as seen in WTI and Brent, has led to a strengthening of the Indian rupee due to reduced import bills. This move is priced, as indicated by the small resid_z values for WTI and Brent, suggesting that the market has already accounted for the decline in oil prices.
- **Gap**: No gap: The move in oil prices is already reflected in the currency market, with the Indian rupee strengthening in response to the decline in oil prices.
- **India take**: The Indian rupee has reacted to the decline in oil prices, strengthening to its highest level in two weeks. Indian instruments such as Nifty Midcap 100 may also react positively due to their negative correlation with oil prices.
- Watch next: nifty_midcap_100 (up) — not yet - watch; Negative correlation with WTI and Brent
- **India receivers**: nifty_midcap_100 (rho -0.619, z 0.13); dyn_jiofin_bo (rho -0.456, z -0.19); nifty_50 (rho -0.455, z -0.64)
- Source: Rupee clings to two-week high as oil slides, intervention helps cement rise — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-clings-to-two-week-high-as-oil-slides-intervention-helps-cement-rise/articleshow/132682371.cms
- Source: Rupee clings to two-week high as oil price slide, intervention helps cement rise — BusinessLine Mkts, 2026-07-28. https://www.thehindubusinessline.com/markets/forex/rupee-clings-to-two-week-high-as-oil-slides-intervention-helps-cement-rise/article71276505.ece
- Source: Iran Races to Fortify Its Most Vital Oil Terminal as U.S. Threats Persist — OilPrice, 2026-07-28. https://oilprice.com/Latest-Energy-News/World-News/Iran-Races-to-Fortify-Its-Most-Vital-Oil-Terminal-as-US-Threats-Persist.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 6.25] indices · 3 series ↓
- nikkei_225 [INDICES]: last 62313.21, z20 -2.93, zc -1.93, resid-z -1.34 [moved], 1d -4.03%, |z20|=2.93
- taiwan_weighted [INDICES]: last 41635.37, z20 -2.77, zc -1.98, resid-z -1.40 [moved], 1d -4.58%, |z20|=2.77
- kospi [INDICES]: last 6019.06, z20 -2.17, zc -2.49, resid-z -1.43 [moved], 1d -10.90%, |z20|=2.17
- **Mechanism**: The sharp decline in Japanese chip stocks, led by major chipmakers such as Kioxia, Tokyo Electron, and Advantest, has triggered a broader selloff in the Nikkei index, which has subsequently transmitted to other Asian markets, including Taiwan and Korea. This move is largely priced, given the relatively small resid_z values for the affected indices. The valid metal_copper_channel and vix_equity_inverse channels may also be contributing to the transmission of this move to Indian metal equities.
- **Gap**: No gap: the move in Nikkei and other Asian indices is largely priced, with small resid_z values indicating that the decline is largely explained by factor exposures.
- **India take**: Indian metal equities, such as those tracked by the nifty_metal index, have already reacted to the decline in Asian markets, with a rho of 0.491 with the kospi index. Other Indian transmission candidates, such as dyn_hdbfs_bo and dyn_techm_ns, have also reacted to the move in their respective correlated indices.
- Watch next: nifty_metal (down) — already moved; rho=0.491 with kospi
- **India receivers**: nifty_metal (rho 0.498, z -1.35); dyn_hdbfs_bo (rho 0.467, z -2.33); dyn_techm_ns (rho -0.416, z 2.14); dyn_pcjeweller_ns (rho 0.377, z -1.11)
- Source: Global Market: Japan’s Nikkei plunges over 4% as chip stocks track global tech selloff — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-plunges-over-4-as-chip-stocks-track-global-tech-selloff/articleshow/132676159.cms
- Source: Japan’s Nikkei tumbles over 3% as chip stock selloff deepens after Wall Street decline — BusinessLine Mkts, 2026-07-28. https://www.thehindubusinessline.com/markets/stock-markets/japans-nikkei-tumbles-over-3-as-chip-stock-selloff-deepens-after-wall-street-decline/article71275340.ece
- Source: Global Markets: Japan's Nikkei rises as oil falls before key earnings — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/us-stocks/news/global-markets-japans-nikkei-rises-as-oil-falls-before-key-earnings/articleshow/132654861.cms

### [AMBER 5.96] cross-asset · 5 series ↑
- ust_2y [RATES]: last 4.33, z20 2.03, zc -0.71, resid-z -1.16 [quiet], 1d -0.92%, |z20|=2.03; 1y-pct=99
- tips_10y_real [RATES]: last 2.43, z20 1.85, zc 0.00, resid-z -0.30 [quiet], 1d 0.00%, |z20|=1.85; 1y-pct=99
- ust_10y [RATES]: last 4.69, z20 1.72, zc -0.44, resid-z -0.72 [quiet], 1d -0.42%, |z20|=1.72; 1y-pct=99
- ust_30y [RATES]: last 5.16, z20 1.38, zc -0.30, resid-z -0.44 [quiet], 1d -0.19%, 1y-pct=99
- dyn_bond [EQUITIES]: last 90.79, z20 -1.09, zc 0.45, resid-z 0.09 [quiet], 1d 0.25%, 1y-pct=2
- **Mechanism**: The recent move in US Treasury yields, particularly the 2-year and 10-year yields, is driven by concerns over fiscal policy and uncertainty about future interest rate moves. This is reflected in the quiet moves of ust_2y, ust_10y, and ust_30y, with relatively low resid_z values, indicating that the moves are largely priced in. The valid channels, such as gold_silver_comove and metal_copper_channel, do not appear to be driving the current move, but the vix_equity_inverse channel suggests that equity markets may be due for a drawdown if volatility spikes.
- **Gap**: No gap: the moves in US Treasury yields are largely priced in, with low resid_z values and high r2 values, indicating that the market has already accounted for the current information.
- **India take**: The Indian market may react through the metal equities, such as those in the metal_copper_channel, but so far, there is no significant reaction. The Nifty 50 index may also be affected if the volatility spike materializes, leading to a drawdown.
- Watch next: nifty_50 (down) — not yet - watch; potential drawdown due to volatility spike
- Source: Global Market: Japan's 10-year bond yield climbs as fiscal concerns weigh on market ahead of BOJ meeting — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-10-year-bond-yield-climbs-as-fiscal-concerns-weigh-on-market-ahead-of-boj-meeting/articleshow/132680390.cms
- Source: JPMORGAN TURNS BULLISH ON STOCKS JPMorgan said its tactical positioning monitor is flashing a buy signal, pointing to further upside for the S&P 500. The bank expects lower bond yields, a weaker dollar, steady Fed policy, and strong earnings to support equities, while warning — DeItaone, 2026-07-27. https://t.me/walter_bloomberg/33969
- Source: Bond investors, unsure about Fed policy outlook, hedge against US rate shock — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/bonds/bond-investors-unsure-about-fed-policy-outlook-hedge-against-us-rate-shock/articleshow/132665831.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.42] dyn_eternal_ns ↑
- dyn_eternal_ns [EQUITIES]: last 307.50, z20 3.42, zc 1.92, resid-z 2.51 [unexplained], 1d 3.94%, |z20|=3.42
- **Mechanism**: The move in dyn_eternal_ns is driven by a bullish candlestick pattern, specifically a White Marubozu, which is a technical indicator suggesting a possible uptrend. This pattern, combined with the stock's appearance on the bullish scanner, has led to a surge in its price. The move is also correlated with other Indian instruments, such as nifty_midcap_100 and dyn_jiofin_bo, which have not yet moved, suggesting potential transmission effects.
- **Gap**: No gap: the big raw move in dyn_eternal_ns is accompanied by a relatively small resid_z, indicating that the move is largely priced in and not an anomaly.
- **India take**: The Indian instrument that expresses this move is dyn_havells_ns, which has already reacted, while other correlated instruments such as nifty_midcap_100 and dyn_jiofin_bo have not yet moved, suggesting potential transmission effects. The move may also impact the broader Indian market, with the Nifty 50 index potentially being affected.
- Watch next: nifty_midcap_100 (up) — not yet - watch; historical lead of 4d
- Watch next: dyn_jiofin_bo (up) — not yet - watch; historical lead of 3d
- **India receivers**: nifty_midcap_100 (rho 0.6, z 0.13); dyn_jiofin_bo (rho 0.517, z -0.19); nifty_50 (rho 0.497, z -0.64); dyn_havells_ns (rho 0.456, z 1.65)
- Source: Eternal among 4 stocks flashing bullish signals, hinting at a possible uptrend — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/news/eternal-among-4-stocks-flashing-bullish-signals-hinting-at-a-possible-uptrend/slideshow/132674117.cms
- Source: Market wrap: Eternal, HDFC Bank, Infosys among top gainers and losers on Nifty and Sensex on Monday — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-eternal-hdfc-bank-infosys-among-top-gainers-and-losers-on-nifty-and-sensex-on-monday/articleshow/132660092.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-28 (d=0.02), 2026-06-30 (d=0.04)

### [AMBER 5.18] indices · 2 series ↑
- nasdaq_100 [INDICES]: last 28036.41, z20 -2.35, zc -0.79, resid-z -1.60 [unexplained], 1d -0.33%, |z20|=2.35
- vix [INDICES]: last 18.90, z20 1.69, zc 0.15, resid-z n/a [quiet], 1d 1.23%, |z20|=1.69
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
- Source: Gold price outlook: Chris Wood of Jefferies says it's time to buy gold again; believes next rally could be bigger — Mint Markets, 2026-07-28. https://www.livemint.com/market/commodities/gold-price-outlook-chris-wood-of-jefferies-says-its-time-to-buy-gold-again-believes-next-rally-could-be-bigger-11785232982540.html
- Source: US Fed meeting begins today: Check date, time and where to watch Kevin Warsh's speech — Mint Markets, 2026-07-28. https://www.livemint.com/market/stock-market-news/us-fed-meeting-begins-today-check-date-time-and-where-to-watch-kevin-warshs-speech-11785222523367.html
- Source: HUL shares slide 5% after weaker-than-expected Q1; PAT dips 3% to Rs 2,673 crore on one-time credit — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/news/hul-shares-slide-5-after-weaker-than-expected-q1-pat-dips-3-to-rs-2673-crore-on-one-time-credit/articleshow/132676380.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.01), 2025-04-17 (d=0.02)

### [AMBER 5.16] cross-asset · 2 series ↑
- nifty_it [INDICES]: last 30408.55, z20 2.32, zc 1.98, resid-z 1.85 [unexplained], 1d 3.28%, |z20|=2.32
- dyn_techm_ns [EQUITIES]: last 1635.20, z20 2.14, zc 2.06, resid-z 1.80 [unexplained], 1d 3.82%, |z20|=2.14
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.52).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tataelxsi_ns (rho 0.683 via nifty_it, z -0.21, quiet); nifty_50 (rho 0.358 via nifty_it, z -0.64, quiet)
- Watch next: dyn_tataelxsi_ns (co-move) — not yet - watch; rho 0.683 vs nifty_it
- **India receivers**: dyn_tataelxsi_ns (rho 0.683, z -0.21); nifty_50 (rho 0.358, z -0.64)
- Source: Tech Mahindra Share Price Live Updates: Tech Mahindra's Stock Surges Past Resistance — ET Markets, 2026-07-28. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tech-mahindra-stock-price-live-updates-28-jul-2026/liveblog/132674133.cms
- Source: Stocks to buy for short term: BHEL, Mahindra and Mahindra among 6 stocks experts recommend for next 1-2 weeks — Mint Markets, 2026-07-28. https://www.livemint.com/market/stock-market-news/stocks-to-buy-for-short-term-bhel-mahindra-and-mahindra-among-6-stocks-experts-recommend-for-next-1-2-weeks-11785165963810.html
- Historical analogues: 2025-12-30 (d=0.52), 2025-08-13 (d=0.76), 2026-01-06 (d=0.77)

## Watchlist (below surfacing floor)
dxy ↑ (4.93), dyn_cartrade_ns ↑ (4.67), dyn_infy ↑ (4.48), dyn_ohi ↑ (3.93), gold_silver_ratio ↑ (3.75), dyn_hdb ↓ (3.75), natgas ↓ (3.7), asx_200 ↑ (3.62), indices · 2 series ↑ (3.6), dyn_bac ↑ (3.55), dyn_301077_sz ↓ (3.27), dyn_tech ↑ (2.8)

## India macro
- nifty_50: 23983.9492 (1d -0.05%, z20 -0.64, flag none)
- nifty_midcap_100: 62421.4492 (1d 0.22%, z20 0.13, flag none)
- usd_inr: 95.8420 (1d -0.75%, z20 -0.14, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6026 (1d 0.27%, z20 0.85, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 73.1 — "IndusInd Bank Share Price Live Updates: IndusInd Bank  Price and SMA Overview"
- INOXINDIA.NS (INOX INDIA LIMITED) score 64.4 — "India's IPO market to stay resilient with over 70 firms awaiting SEBI clearance: Report"
- BAC (Bank of America Corporation) score 60.6 — "IndusInd Bank Share Price Live Updates: IndusInd Bank  Price and SMA Overview"
- HDB (HDFC Bank Limited) score 59.8 — "IndusInd Bank Share Price Live Updates: IndusInd Bank  Price and SMA Overview"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 57.6 — "IndusInd Bank Share Price Live Updates: IndusInd Bank  Price and SMA Overview"
- IDBI.NS (IDBI BANK LIMITED) score 55.4 — "IndusInd Bank Share Price Live Updates: IndusInd Bank  Price and SMA Overview"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 53.8 — "India's IPO market to stay resilient with over 70 firms awaiting SEBI clearance: Report"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 51.3 — "From AI boom to valuation worries: Why investors are rethinking big tech bets"
- TECHM.NS (TECH MAHINDRA LIMITED) score 51.1 — "From AI boom to valuation worries: Why investors are rethinking big tech bets"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 47.1 — "IndusInd Bank Share Price Live Updates: IndusInd Bank  Price and SMA Overview"
- COALINDIA.NS (COAL INDIA LTD) score 45.6 — "India's IPO market to stay resilient with over 70 firms awaiting SEBI clearance: Report"
- COIN (Coinbase Global, Inc.) score 45.3 — "Global Market: Barclays posts robust H1 results, raises guidance on investment banking mom"
- OHI (Omega Healthcare Investors, In) score 30.7 — "From AI boom to valuation worries: Why investors are rethinking big tech bets"
- LTH (Life Time Group Holdings, Inc.) score 24.4 — "HUL shares slide over 6% after weaker-than-expected Q1; PAT dips 3% to Rs 2,673 crore on o"
- CHKP (Check Point Software Technolog) score 23.9 — "Poojaa Precision Engg IPO Day 1: Issue subscribed 3.34x so far. GMP hints 86% listing gain"
- BOND (PIMCO Active Bond Exchange-Tra) score 22.0 — "Global Market: Japan's 10-year bond yield climbs as fiscal concerns weigh on market ahead "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.8 — "Suzlon Energy Q1 Results: Net profit falls 6% YoY to Rs 305 crore; stock sinks 7%"
- TECH (Bio-Techne Corp) score 20.0 — "From AI boom to valuation worries: Why investors are rethinking big tech bets"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 16.5 — "Tata Power shares get Equal Weight rating from Morgan Stanley with target price of Rs 399"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 12.2 — "Bharat Electronics Q1 sends mixed signals; prospects intact"
- INFY (Infosys Limited) score 11.6 — "Infosys Share Price Live Updates: Sensex trades flat, Nifty near 24,000 ahead of US Fed me"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 11.3 — "Adani Energy’s Rs 3,500 crore QIP oversubscribed 3.1 times as FIIs, MFs and  Azim Premji f"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.9 — "Global markets: Shein will struggle to justify up to $50 billion Hong Kong IPO valuation"
- JIOFIN.BO (Jio Financial Services Limited) score 8.4 — "My financial adviser is against a withdrawal plan for my $2.3 million portfolio. Is he mak"
- 301077.SZ (CHINASTARS) score 8.4 — "South Korea’s KOSPI falls 11 % as China chip threat hits SK Hynix, Samsung"
- MS (Morgan Stanley) score 7.7 — "Tata Power shares get Equal Weight rating from Morgan Stanley with target price of Rs 399"
- VT (Vanguard Total World Stock Ind) score 7.5 — "TRUMP ON FED: WE SHOULD HAVE WORLD'S LOWEST INTEREST RATE"
- META (Meta) score 7.0 — "Metalic Technoforge SME IPO listing: Shares list at a 13% premium to the issue price, trim"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 6.7 — "My financial adviser is against a withdrawal plan for my $2.3 million portfolio. Is he mak"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.3 — "Vedanta Aluminium shares in a sweet spot, says ICICI Securities; initiates coverage with B"
- GS (Goldman Sachs Group, Inc. (The) score 6.0 — "GOLDMAN WARNS MACRO RISKS RISING Goldman Sachs said rising oil volatility is shifting inve"
- NVDA (NVIDIA Corporation) score 5.3 — "TCS, Infosys, Coforge, other IT stocks rally up to 10% after Nvidia-led chip rout. Is AI t"
- ETERNAL.NS (ETERNAL LIMITED) score 4.5 — "Eternal among 4 stocks flashing bullish signals, hinting at a possible uptrend"
- PCJEWELLER.NS (PC JEWELLER LTD) score 3.7 — "Keralam jewellers seek review of gold, silver import duty structure"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 3.5 — "India’s electricity shortages more than doubled during January-May 2026: IEA"
- 688188.SS (SHANGHAI BOCHU ELECTRONIC TECH) score 2.4 — "China's memory chipmaker CXMT shares soar in its blockbuster share listing in Shanghai"
- AAPL (Apple Inc.) score 1.5 — "FORD WILL USE APPLE SOFTWARE IN NEW SELF-DRIVING SYSTEM: NYT"
- NFLX (Netflix, Inc.) score 1.4 — "Losing Wall Street binge premium! Why are Netflix shares in a freefall this year?"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 0.4 — "Newly-listed SME stock DSM Fresh Foods jumps over 30% in 2 days after reporting a 58% YoY "
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