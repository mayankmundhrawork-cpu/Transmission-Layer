# Transmission Layer — board brief · 2026-07-13 13:09Z

data as of **2026-07-13** · 92 series · 9 red / 29 amber · 8 events surfaced (19 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.426, 5d in regime; vol-pct 0.602, breadth-off 0.25, Markov P(high-vol) 0.019)
- [INVERTED] **safe_haven_gold** — corr20 -0.27, corr60 -0.45, contra nifty_50 corr20=0.42, last shift 2026-05-19. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.94, corr60 0.83, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.44, corr60 0.37, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.05, corr60 -0.03, last shift 2026-03-11. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.78, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.18, corr60 0.01, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.24, corr60 -0.26, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.19, corr60 0.25, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Events (ranked)

### [RED 16.4] dyn_justdial_bo ↑
- dyn_justdial_bo [EQUITIES]: last 677.50, z20 14.40, zc 1.84, resid-z 1.91 [unexplained], 1d 20.00%, |z20|=14.40
- **Mechanism**: The surge in Just Dial's stock price is driven by its strong Q1 results, including a 9.9% year-on-year increase in revenue and a 4.1% year-on-year rise in net profit, which has led to a re-rating of the stock. The appointment of a new CEO and CFO has also contributed to the positive sentiment. The move is partially priced, given the stock's z20 level of 14.40 and resid_z of 1.91, indicating that some of the move can be explained by factor exposures, but the unexplained component is still significant.
- **Gap**: No gap: the stock's move is largely driven by its strong Q1 results and new management appointments, which are priced in by the market
- **India take**: The Indian instrument that expresses this move is the Nifty 50, which has not yet reacted, but may follow suit given its historical lead over Just Dial. Other transmission candidates like Nifty Midcap 100 and Nifty FMCG have already reacted to the news.
- Watch next: nifty_50 (up) — not yet - watch; historically leads Just Dial by 1 day
- **India receivers**: nifty_50 (rho 0.603, z 0.86); nifty_midcap_100 (rho 0.576, z 2.03); dyn_indianb_ns (rho 0.542, z 0.37); nifty_fmcg (rho 0.432, z -1.42)
- Source: Just Dial share price skyrockets 17% on strong Q1 results, new CEO, CFO announcement. Do you own? — Mint Markets, 2026-07-13. https://www.livemint.com/market/stock-market-news/just-dial-share-price-skyrockets-17-on-strong-q1-results-new-ceo-cfo-announcement-do-you-own-11783922394287.html
- Source: Just Dial shares rocket 14% as profit rises to Rs 166 crore; revenue grows 10% YoY — ET Markets, 2026-07-13. https://economictimes.indiatimes.com/markets/stocks/news/just-dial-shares-rocket-14-as-profit-rises-to-rs-166-crore-revenue-grows-10-yoy/articleshow/132356592.cms
- Historical analogues: 2026-06-18 (d=0.19), 2025-06-30 (d=0.52), 2026-01-07 (d=0.52)

### [RED 6.87] dyn_kalyankjil_ns ↑
- dyn_kalyankjil_ns [EQUITIES]: last 511.70, z20 4.87, zc 0.80, resid-z 1.39 [quiet], 1d 7.47%, |z20|=4.87
- **Mechanism**: The surge in Kalyan Jewellers' share price is driven by strong Q1FY27 business update, robust demand, store expansion, and the company's asset-light franchise model. This move is priced, as indicated by the small resid_z of 1.39, suggesting that the factor exposures have largely explained the move. The valid metal_copper_channel and gold_silver_comove channels may also be contributing to the uptrend in the stock.
- **Gap**: No gap: the move is largely priced, with a small resid_z of 1.39, indicating that the factor exposures have explained the move
- **India take**: The Indian instruments that express this move are nifty_midcap_100, dyn_pcjeweller_ns, and dyn_swiggy_ns, which have already reacted to the surge in Kalyan Jewellers' share price. The Nifty 50 has also shown some movement, but its reaction has been relatively quiet so far.
- Watch next: nifty_midcap_100 (up) — already moved; rho=0.576 via dyn_kalyankjil_ns
- Watch next: dyn_pcjeweller_ns (up) — already moved; rho=0.445 via dyn_kalyankjil_ns
- Watch next: dyn_swiggy_ns (up) — already moved; rho=0.395 via dyn_kalyankjil_ns
- **India receivers**: nifty_midcap_100 (rho 0.576, z 2.03); dyn_indianb_ns (rho 0.497, z 0.37); dyn_pcjeweller_ns (rho 0.445, z 1.46); nifty_50 (rho 0.417, z 0.86)
- Source: Top Gainers & Losers on 13 July: Newgen Software, Kalyan Jewellers, TCS, Voltas, Paytm, Bajaj Auto among top gainers — Mint Markets, 2026-07-13. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-13-july-newgen-software-kalyan-jewellers-tcs-voltas-paytm-bajaj-auto-among-top-gainers-11783936105519.html
- Source: Kalyan Jewellers shares surge 12%, jump 50% in just 4 sessions; is there more steam left? — Mint Markets, 2026-07-13. https://www.livemint.com/market/stock-market-news/kalyan-jewellers-shares-surge-almost-10-jump-47-in-just-4-sessions-is-there-more-steam-left-11783922565597.html
- Source: 47% rally in 4 days! Kalyan Jewellers shares rise another 10%. Should you book profit? — ET Markets, 2026-07-13. https://economictimes.indiatimes.com/markets/stocks/news/47-rally-in-4-days-kalyan-jewellers-shares-rise-another-10-should-you-book-profit/articleshow/132357947.cms
- Historical analogues: 2026-01-07 (d=1.76), 2026-06-15 (d=1.78), 2025-07-02 (d=2.84)

### [AMBER 6.46] commodities · 2 series ↑
- brent [COMMODITIES]: last 78.73, z20 0.63, zc -0.14, resid-z 0.01 [quiet], 1d 3.58%, 1-session move +3.58% ≥ 1.5%; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 73.89, z20 0.24, zc -0.36, resid-z -0.13 [quiet], 1d 3.47%, 1-session move +3.47% ≥ 1.5%
- **Mechanism**: The recent surge in oil prices, led by Brent and WTI, is driven by supply-side factors such as Nigeria's increased oil production and Middle East risks. This move is largely priced in, with small resid_z values indicating that factor exposures can explain most of the price change. The valid metal_copper_channel and gold_silver_comove channels suggest that commodity prices are driving the narrative, rather than a broader risk-off sentiment.
- **Gap**: No gap: the move in oil prices is largely priced in, with small resid_z values and no significant unexplained component
- **India take**: The Indian instrument nifty_midcap_100 has already reacted to the WTI price move, and further downside is expected. The INR may also weaken due to higher oil prices, but the weak inr_oil_channel and dxy_inr_channel suggest that this relationship is not currently driving the price action.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to WTI price move
- **India receivers**: nifty_midcap_100 (rho -0.508, z 2.03)
- Source: Nigeria’s Oil Production Hits Six-Year High as Middle East Risks Return — OilPrice, 2026-07-13. https://oilprice.com/Latest-Energy-News/World-News/Nigerias-Oil-Production-Hits-Six-Year-High-as-Middle-East-Risks-Return.html
- Source: Sensex today | Stock Market Highlights: Stock markets end flat as West Asia tensions, higher oil prices weigh on sentiment — BusinessLine Mkts, 2026-07-13. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-13-july-2026/article71213684.ece
- Source: Oil pangs resurface for rupee, options market gauge signals bearish bias — ET Markets, 2026-07-13. https://economictimes.indiatimes.com/markets/forex/forex-news/oil-pangs-resurface-for-rupee-options-market-gauge-signals-bearish-bias/articleshow/132364812.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [AMBER 5.62] cross-asset · 5 series ↑
- sp500 [INDICES]: last 7575.38, z20 1.69, zc 0.52, resid-z 0.11 [quiet], 1d 0.42%, |z20|=1.69; 1y-pct=98
- vix [INDICES]: last 15.05, z20 -1.55, zc -0.59, resid-z n/a [quiet], 1d -4.99%, |z20|=1.55
- dow_jones [INDICES]: last 52640.31, z20 1.01, zc 0.36, resid-z -0.05 [quiet], 1d 0.29%, 1y-pct=98
- dyn_vt [EQUITIES]: last 157.60, z20 0.96, zc 0.45, resid-z -0.50 [quiet], 1d 0.38%, 1y-pct=96
- dyn_ms [EQUITIES]: last 222.28, z20 0.76, zc 0.04, resid-z 0.51 [quiet], 1d 0.07%, 1y-pct=98
- **Mechanism**: The recent escalation of US-Iran tensions has led to a rise in oil prices, which in turn has pressured chip stocks and contributed to a decline in US stock futures. This move is largely priced, as evidenced by the small resid_z values for the affected indices, including the S&P 500 and Dow Jones. The valid vix_equity_inverse channel suggests that the vol spike will lead to an equity drawdown, which is consistent with the current market sentiment.
- **Gap**: No gap: The current move is largely priced, with small resid_z values for the affected indices, indicating that the market has already incorporated the news into prices.
- **India take**: The Indian stock market is expected to open lower on Monday, amid cautiousness over the renewed geopolitical tensions in the Middle East, with the Nifty 50 index likely to react to the global risk-off sentiment. The metal_copper_channel may also transmit the global copper price move to Indian metal equities.
- Watch next: nifty_50 (down) — not yet - watch; Risk-off sentiment due to US-Iran tensions
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Live: US stock futures decline as US-Iran escalation rattles sentiment — ET Markets, 2026-07-13. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-earnings-forecast-micron-sk-hynix-deckers-outdoor-stock-price-news-13-july-2026/liveblog/132366645.cms
- Source: US Stock Market: Wall Street braces for pivotal week as earnings, inflation data and Middle East tensions come into focus — ET Markets, 2026-07-13. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stock-market-wall-street-braces-for-pivotal-week-as-earnings-inflation-data-and-middle-east-tensions-come-into-focus/articleshow/132357231.cms
- Source: US stock market to Kospi: Here’s world equity heatmap you should know before opening of the Indian stock market today — Mint Markets, 2026-07-13. https://www.livemint.com/market/stock-market-news/us-stock-market-to-kospi-here-s-world-equity-heatmap-you-should-know-before-opening-of-the-indian-stock-market-today-11783911043902.html
- Historical analogues: 2024-10-17 (d=0.41), 2026-05-22 (d=0.54), 2025-10-24 (d=0.58)

### [AMBER 5.49] rates · 4 series ↑
- tips_10y_real [RATES]: last 2.31, z20 1.83, zc 0.00, resid-z 0.32 [quiet], 1d 0.00%, |z20|=1.83; 1y-pct=99
- ust_30y [RATES]: last 5.05, z20 1.68, zc -0.26, resid-z -0.05 [quiet], 1d -0.20%, |z20|=1.68; 1y-pct=96
- ust_10y [RATES]: last 4.54, z20 1.29, zc -0.43, resid-z -0.16 [quiet], 1d -0.44%, 1y-pct=95
- ust_2y [RATES]: last 4.16, z20 0.50, zc -0.91, resid-z -0.90 [quiet], 1d -1.19%, 1y-pct=96
- **Mechanism**: rates · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.678 vs tips_10y_real, historically leads by 1d
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.655 vs tips_10y_real, historically leads by 4d
- Watch next: wti (co-move) — not yet - watch; rho 0.585 vs ust_30y, historically leads by 3d
- Watch next: brent (co-move) — not yet - watch; rho 0.574 vs ust_30y, historically leads by 3d
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.556 vs tips_10y_real, historically leads by 4d
- Source: Global Market: Eurozone bond yields climb as Middle East tensions rekindle inflation concerns — ET Markets, 2026-07-13. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-eurozone-bond-yields-climb-as-middle-east-tensions-rekindle-inflation-concerns/articleshow/132362710.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.26), 2026-05-14 (d=0.57)

### [RED 5.45] commodities · 3 series ↑
- corn [COMMODITIES]: last 466.25, z20 4.13, zc 1.90, resid-z 1.74 [unexplained], 1d 6.45%, |z20|=4.13; 1y-pct=96
- wheat [COMMODITIES]: last 637.00, z20 2.97, zc 2.20, resid-z 1.72 [unexplained], 1d 0.79%, |z20|=2.97; 1y-pct=96
- soybeans [COMMODITIES]: last 1194.50, z20 1.82, zc 1.41, resid-z 1.48 [quiet], 1d -0.17%, |z20|=1.82
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_adanient_bo (rho -0.36 via soybeans, z 1.41, reacted)
- **India receivers**: dyn_adanient_bo (rho -0.36, z 1.41)
- Historical analogues: 2026-05-22 (d=0.0), 2024-08-30 (d=0.27), 2026-05-06 (d=0.32)

### [AMBER 5.26] indices · 2 series ↓
- kospi [INDICES]: last 6904.41, z20 -2.43, zc 0.59, resid-z 0.52 [quiet], 1d -7.64%, |z20|=2.43
- nikkei_225 [INDICES]: last 67132.87, z20 -1.89, zc 0.69, resid-z 0.45 [quiet], 1d -2.08%, |z20|=1.89
- **Mechanism**: The decline in Kospi and Nikkei 225 indices is attributed to the rise in oil prices due to renewed Middle East conflict, which dims the corporate outlook and increases costs. This move is priced, as indicated by the relatively small resid_z values of 0.52 and 0.45 for Kospi and Nikkei 225, respectively. The move is also reflected in the quiet status of both indices, suggesting that the market has already factored in the news.
- **Gap**: No gap: The move in Kospi and Nikkei 225 is priced, with small resid_z values indicating that the market has already factored in the news.
- **India take**: The Indian instrument that expresses this move is Nifty Metal, which has a correlation coefficient of 0.568 with Kospi and has not yet reacted. Nifty 50, which has a correlation coefficient of 0.412 with Nikkei 225, is also a potential responder.
- Watch next: taiwan_weighted (down) — not yet - watch; Historically leads Kospi by 3 days and has a high correlation coefficient of 0.665
- Watch next: nifty_metal (down) — not yet - watch; Has a correlation coefficient of 0.568 with Kospi
- **India receivers**: nifty_metal (rho 0.568, z -0.48); nifty_midcap_100 (rho 0.429, z 2.03); nifty_50 (rho 0.412, z 0.86)
- Source: Global Market: Japan's Nikkei closes lower as oil price jump dims corporate outlook — ET Markets, 2026-07-13. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-closes-lower-as-oil-price-jump-dims-corporate-outlook/articleshow/132359942.cms

### [RED 5.22] natgas ↓
- natgas [COMMODITIES]: last 2.89, z20 -3.22, zc -0.57, resid-z -0.91 [quiet], 1d -1.63%, |z20|=3.22
- **Mechanism**: natgas ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: European Natural Gas Prices Jump on Hormuz Escalation — OilPrice, 2026-07-13. https://oilprice.com/Latest-Energy-News/World-News/European-Natural-Gas-Prices-Jump-on-Hormuz-Escalation.html
- Source: Oil and LNG Tankers Go Dark Again as Hormuz Crisis Deepens — OilPrice, 2026-07-13. https://oilprice.com/Latest-Energy-News/World-News/Oil-and-LNG-Tankers-Go-Dark-Again-as-Hormuz-Crisis-Deepens.html
- Source: India’s natural gas demand likely to decline by 8% in 2026 — BusinessLine Mkts, 2026-07-11. https://www.thehindubusinessline.com/markets/commodities/indias-natural-gas-demand-likely-to-decline-by-8-in-2026/article71210886.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

## Watchlist (below surfacing floor)
midcap_largecap_ratio ↑ (4.59), dyn_qessf ↓ (4.09), bovespa ↑ (4.01), gold_silver_ratio ↑ (3.97), dyn_meta ↑ (3.82), usd_inr ↑ (3.58), dyn_cupid_ns ↑ (3.21), shanghai_comp ↓ (3.12), cross-asset · 2 series ↑ (2.86), brent_wti_spread ↑ (2.47), sofr ↓ (2.19), nifty_it ↑ (2.13)

## India macro
- nifty_50: 24208.5996 (1d 0.01%, z20 0.86, flag none)
- nifty_midcap_100: 63062.3516 (1d 0.04%, z20 2.03, flag amber)
- usd_inr: 95.7200 (1d 0.35%, z20 1.58, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6050 (1d 0.03%, z20 1.59, flag red)
- Next India prints: India CPI T-0d · NSDL FPI flows T-0d · IMD weekly rainfall T-0d · India WPI T-1d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 33.8 — "US stock market to Kospi: Here’s world equity heatmap you should know before opening of th"
- COIN (Coinbase Global, Inc.) score 28.2 — "Global Market:  SK Hynix warns of historic memory chip shortage by 2027 as AI demand soars"
- HDB (HDFC Bank Limited) score 25.3 — "HDFC Bank shares drop 2%. What lies ahead as lender set to announce Q1 earnings this week?"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 24.1 — "HDFC Bank shares drop 2%. What lies ahead as lender set to announce Q1 earnings this week?"
- INDIANB.NS (INDIAN BANK) score 18.4 — "US stock market to Kospi: Here’s world equity heatmap you should know before opening of th"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 12.4 — "US Stock Market: Inflation gathers pace as tariffs, energy costs and AI investment lift pr"
- SKHYV (SK hynix Inc. American Deposit) score 10.7 — "Global Market:  SK Hynix warns of historic memory chip shortage by 2027 as AI demand soars"
- KALYANKJIL.NS (KALYAN JEWELLERS IND LTD) score 9.0 — "47% rally in 4 days! Kalyan Jewellers shares rise another 10%. Should you book profit?"
- CHKP (Check Point Software Technolog) score 8.7 — "Kusumgar IPO allotment to be finalised today. Here's GMP, how to check status"
- PCJEWELLER.NS (PC JEWELLER LTD) score 8.6 — "Q1 surprise sends jewellery stocks shining 40% in a month. Will the surge last in next qua"
- BOND (PIMCO Active Bond Exchange-Tra) score 8.3 — "India bonds fall as oil spike, Treasury rout weigh"
- VT (Vanguard Total World Stock Ind) score 5.4 — "US stock market to Kospi: Here’s world equity heatmap you should know before opening of th"
- SWIGGY.NS (SWIGGY LIMITED) score 4.2 — "Swiggy shares slide over 2% after FSSAI issues 9 notices over consumer complaints"
- META (Meta) score 3.9 — "The real worry for Indian metal stocks isn't FPI selling. It's more earnings downgrades."
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 3.5 — "Multibagger defence stock to raise  ₹3,322 crore through fresh equity issuance"
- BHARTIARTL.NS (BHARTI AIRTEL LIMITED) score 3.5 — "Mcap of 4 of top-10 most valued firms jumps ₹92,995 crore; HDFC Bank, Airtel top gainers"
- MU (Micron Technology, Inc.) score 3.3 — "SK Hynix makes US debut today. Will investors sell Micron to buy the AI memory leader?"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 3.2 — "Vedanta Aluminium, Adani Power, 4 other stocks with up to 24% upside. Do you own any?"
- CUPID.NS (CUPID LIMITED) score 3.0 — "Cupid shares fall 2% after 131% rally in 3 months; Stock reclassified to BSE Group ‘A’"
- JEF (Jefferies Financial Group Inc.) score 2.9 — "Greed and Fear report: Christopher Wood sees 'AI fatigue' setting in. Why Jefferies is tur"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 2.8 — "GE Vernova, Atlanta Electricals among top beneficiaries of India's transmission expansion"
- GS (Goldman Sachs Group, Inc. (The) score 2.5 — "Goldman Sachs pegs Nifty target at 26,500 by June 2027; lists 15 stocks from key themes"
- MCAP (MCAP Inc.) score 2.5 — "Mcap of 4 of top-10 most valued firms jumps ₹92,995 crore; HDFC Bank, Airtel top gainers"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 2.0 — "CarTrade Tech share price gains after UBS assigns ‘Buy’ call, sees over 42% upside potenti"
- JUSTDIAL.BO (JUST DIAL LTD.) score 2.0 — "Just Dial shares rocket 14% as profit rises to Rs 166 crore; revenue grows 10% YoY"
- DRREDDY.NS (DR. REDDY S LABORATORIES) score 1.9 — "Broker’s call: Dr Reddy’s Lab (Accumulate)"
- MS (Morgan Stanley) score 1.8 — "Morgan Stanley warns AI chip rally may be running out of steam"
- BLK (BlackRock, Inc.) score 1.5 — "SBI Funds IPO anchor book 20 times subscribed; draws Capital Group, BlackRock, Goldman, AD"
- KNACK.BO (KNACK PACKAGING LIMITED) score 1.5 — "Knack Packaging shares list at 11% premium; expert sees further upside"
- AVGO (Broadcom Inc.) score 1.1 — "Is Broadcom stock a buy after Apple's massive chip pact?"
- HLIO (Helios Technologies, Inc.) score 1.0 — "Adani flagship is the next big India pick for Singapore’s Helios"
- RIVN (Rivian Automotive, Inc.) score 0.8 — "Rivian's 75 million-share offering: Why Wall Street hit the sell button"
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 0.8 — "Cochin Shipyard shares dip 2% as govt’s OFS opens for retail investors today"
- WULF (TeraWulf Inc.) score 0.6 — "TeraWulf’s stock gains after a $19 billion deal with Anthropic"

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