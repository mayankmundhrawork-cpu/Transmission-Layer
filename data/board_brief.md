# Transmission Layer — board brief · 2026-07-13 19:06Z

data as of **2026-07-13** · 92 series · 11 red / 30 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.419, 5d in regime; vol-pct 0.602, breadth-off 0.235, Markov P(high-vol) 0.019)
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

### [RED 7.44] commodities · 2 series ↑
- brent [COMMODITIES]: last 82.74, z20 1.61, zc -0.14, resid-z 0.01 [quiet], 1d 8.85%, 1-session move +8.85% ≥ 1.5%; |z20|=1.61
- wti [COMMODITIES]: last 77.61, z20 1.11, zc -0.36, resid-z -0.13 [quiet], 1d 8.68%, 1-session move +8.68% ≥ 1.5%
- **Mechanism**: The surge in oil prices is driven by the reimposition of the Iran blockade by the US, which has increased the risk of disruption to energy flows through the Strait of Hormuz. This has led to a sharp increase in brent and wti prices, with both experiencing a 1-session move of over 8%. The move is largely priced, as indicated by the small resid_z values of 0.01 and -0.13 for brent and wti respectively.
- **Gap**: No gap: the move in oil prices is largely explained by the reimposition of the Iran blockade and the resulting increase in risk of disruption to energy flows
- **India take**: The Indian instrument that expresses this move is the nifty_midcap_100, which has already reacted with a z20 score of 2.03. The metal_copper_channel, which is a valid channel, may also transmit the impact of higher oil prices to Indian metal equities.
- Watch next: brent (down) — already moved; mean reversion after sharp price surge
- Watch next: wti (down) — already moved; mean reversion after sharp price surge
- **India receivers**: nifty_midcap_100 (rho -0.508, z 2.03)
- Source: Oil Prices Surge 8% After Trump Reimposes Iran Blockade — OilPrice, 2026-07-13. https://oilprice.com/Latest-Energy-News/World-News/Oil-Prices-Surge-8-After-Trump-Reimposes-Iran-Blockade.html
- Source: Global oil prices top $82 a barrel, heading for biggest jump in 3 months after Trump reimposes Strait of Hormuz blockade — MarketWatch Top, 2026-07-13. https://www.marketwatch.com/story/oil-prices-surge-as-much-as-5-after-iran-declares-strait-of-hormuz-is-closed-6905599b?mod=mw_rss_topstories
- Source: Iraq’s Oil Lifeline Has Been Saved, But For How Long? — OilPrice, 2026-07-13. https://oilprice.com/Energy/Crude-Oil/Iraqs-Oil-Lifeline-Has-Been-Saved-But-For-How-Long.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

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

### [AMBER 6.32] cross-asset · 5 series ↑
- dyn_bond [EQUITIES]: last 90.97, z20 -2.39, zc -0.27, resid-z -0.30 [quiet], 1d -0.35%, |z20|=2.39; 1y-pct=1
- tips_10y_real [RATES]: last 2.31, z20 1.83, zc 0.00, resid-z 0.32 [quiet], 1d 0.00%, |z20|=1.83; 1y-pct=99
- ust_30y [RATES]: last 5.05, z20 1.68, zc -0.26, resid-z -0.05 [quiet], 1d -0.20%, |z20|=1.68; 1y-pct=96
- ust_10y [RATES]: last 4.54, z20 1.29, zc -0.43, resid-z -0.16 [quiet], 1d -0.44%, 1y-pct=95
- ust_2y [RATES]: last 4.16, z20 0.50, zc -0.91, resid-z -0.90 [quiet], 1d -1.19%, 1y-pct=96
- **Mechanism**: The recent surge in Eurozone bond yields, driven by escalating US-Iran tensions and concerns over global inflation, has led to a rise in US Treasury yields. This move is largely priced, with resid_z values indicating that the majority of the move can be explained by factor exposures. However, the correlation between US Treasury yields and Indian bond markets, as well as the potential impact of Japan's pension fund strategy on global capital flows, may contribute to the propagation of this move.
- **Gap**: No gap: the move in US Treasury yields is largely priced, with resid_z values close to zero, indicating that the majority of the move can be explained by factor exposures
- **India take**: The Indian 10-year government bond yield may react to the rise in US Treasury yields, potentially leading to a increase in yields. However, the impact of Japan's pension fund strategy on global capital flows and the Indian bond market is still uncertain.
- Watch next: dyn_bond (down) — already moved; High z20 level and low resid_z indicate a priced move
- Watch next: tips_10y_real (up) — already moved; High z20 level and positive resid_z indicate a partially unexplained move
- Source: Global Market: Eurozone bond yields climb as Middle East tensions rekindle inflation concerns — ET Markets, 2026-07-13. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-eurozone-bond-yields-climb-as-middle-east-tensions-rekindle-inflation-concerns/articleshow/132362710.cms
- Source: Global Market: Japan pension fund strategy may redraw global bond and currency markets — ET Markets, 2026-07-13. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japan-pension-fund-strategy-may-redraw-global-bond-and-currency-markets/articleshow/132359410.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.35] natgas ↓
- natgas [COMMODITIES]: last 2.88, z20 -3.35, zc -0.57, resid-z -0.91 [quiet], 1d -2.04%, |z20|=3.35
- **Mechanism**: The recent drop in natgas prices may propagate through the metal_copper_channel, as global copper leads Indian metal equities. However, the current move in natgas is quiet and priced, with a small resid_z of -0.91, indicating that the move is largely explained by factor exposures. The vix_equity_inverse channel may also play a role, as a vol spike could lead to an equity drawdown, but this is not directly related to natgas.
- **Gap**: No gap: the current move in natgas is priced, with a small resid_z and a low r2 value, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is likely to be the Nifty Metal index, which may react to the change in global copper prices. However, the reaction has not yet occurred.
- Watch next: nifty_50 (down) — not yet - watch; Risk-off sentiment may lead to a decline in Indian equities
- Source: EU's Russian LNG Imports Hit Record High Ahead of 2027 Ban — OilPrice, 2026-07-13. https://oilprice.com/Latest-Energy-News/World-News/EUs-Russian-LNG-Imports-Hit-Record-High-Ahead-of-2027-Ban.html
- Source: U.S. POWER COSTS SURGE TO MULTI-YEAR HIGHS Natural gas power costs hit $90 per megawatt-hour in 2026—the highest level in at least 17 years—as data-center demand accelerates. Solar and onshore wind costs also jumped more than 10%, reaching their highest levels since at least — DeItaone, 2026-07-13. https://t.me/walter_bloomberg/33579
- Source: European Natural Gas Prices Jump on Hormuz Escalation — OilPrice, 2026-07-13. https://oilprice.com/Latest-Energy-News/World-News/European-Natural-Gas-Prices-Jump-on-Hormuz-Escalation.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [AMBER 5.26] indices · 2 series ↓
- kospi [INDICES]: last 6904.41, z20 -2.43, zc 0.59, resid-z 0.53 [quiet], 1d -7.64%, |z20|=2.43
- nikkei_225 [INDICES]: last 67132.87, z20 -1.89, zc 0.69, resid-z 0.45 [quiet], 1d -2.08%, |z20|=1.89
- **Mechanism**: The decline in Kospi and Nikkei 225 indices is attributed to the rise in oil prices due to renewed Middle East conflict, which dims the corporate outlook and increases costs. This move is priced, as indicated by the relatively small resid_z values of 0.52 and 0.45 for Kospi and Nikkei 225, respectively. The move is also reflected in the quiet status of both indices, suggesting that the market has already factored in the news.
- **Gap**: No gap: The move in Kospi and Nikkei 225 is priced, with small resid_z values indicating that the market has already factored in the news.
- **India take**: The Indian instrument that expresses this move is Nifty Metal, which has a correlation coefficient of 0.568 with Kospi and has not yet reacted. Nifty 50, which has a correlation coefficient of 0.412 with Nikkei 225, is also a potential responder.
- Watch next: taiwan_weighted (down) — not yet - watch; Historically leads Kospi by 3 days and has a high correlation coefficient of 0.665
- Watch next: nifty_metal (down) — not yet - watch; Has a correlation coefficient of 0.568 with Kospi
- **India receivers**: nifty_metal (rho 0.568, z -0.48); nifty_midcap_100 (rho 0.429, z 2.03); nifty_50 (rho 0.412, z 0.86)
- Source: Global Market: Japan's Nikkei closes lower as oil price jump dims corporate outlook — ET Markets, 2026-07-13. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-closes-lower-as-oil-price-jump-dims-corporate-outlook/articleshow/132359942.cms

### [RED 5.16] commodities · 3 series ↑
- corn [COMMODITIES]: last 463.00, z20 3.84, zc 1.90, resid-z 1.73 [unexplained], 1d 5.71%, |z20|=3.84
- wheat [COMMODITIES]: last 635.25, z20 2.84, zc 2.20, resid-z 1.72 [unexplained], 1d 0.51%, |z20|=2.84
- soybeans [COMMODITIES]: last 1193.50, z20 1.79, zc 1.41, resid-z 1.47 [quiet], 1d -0.25%, |z20|=1.79
- **Mechanism**: The recent surge in commodity prices, particularly corn, wheat, and soybeans, is driven by unexplained factors, as indicated by their high resid_z values. This move may propagate through the VALID gold_silver_comove channel, as monetary metals often co-move with commodities. However, the INVERTED safe_haven_gold channel suggests a risk-off environment, which may not support further commodity price increases.
- **Gap**: No gap: the big raw move in commodities has a small resid_z, indicating it is PRICED, not an anomaly
- **India take**: The Indian instrument dyn_adanient_bo, which has a negative correlation with soybeans, has already reacted to the commodity price surge. Further moves in Indian metal equities may be influenced by the global copper price, as indicated by the VALID metal_copper_channel.
- Watch next: corn (up) — already moved; high z20 value
- Watch next: wheat (up) — already moved; high z20 value
- Watch next: soybeans (up) — quiet; low z20 value
- **India receivers**: dyn_adanient_bo (rho -0.36, z 1.41)
- Historical analogues: 2026-05-22 (d=0.0), 2024-08-30 (d=0.27), 2026-05-06 (d=0.32)

### [RED 4.71] dyn_qessf ↓
- dyn_qessf [EQUITIES]: last 0.24, z20 -2.71, zc 0.30, resid-z 0.84 [quiet], 1d -10.43%, |z20|=2.71
- **Mechanism**: The decline in dyn_qessf is largely priced, with a small resid_z of 0.84, indicating that the move is mostly explained by factor exposures. The event is likely driven by the announcement of Apollo Micro Systems' fresh equity issuance, which may have led to a reevaluation of the stock's value. The metal_copper_channel and gold_silver_comove channels are valid, but their connection to dyn_qessf is not direct.
- **Gap**: No gap: the move in dyn_qessf is largely priced, with a small resid_z and a low r2 of 0.12, indicating that the event is mostly reflected in the current price
- **India take**: The Indian instrument dyn_atherenerg_ns has already reacted, given its rho of -0.358 with dyn_qessf. The valid metal_copper_channel and gold_silver_comove channels may have indirect implications for Indian metal equities.
- Watch next: dyn_atherenerg_ns (down) — already moved; rho=-0.358 via dyn_qessf
- **India receivers**: dyn_atherenerg_ns (rho -0.358, z 1.38)
- Source: Multibagger defence stock to raise  ₹3,322 crore through fresh equity issuance — Mint Markets, 2026-07-12. https://www.livemint.com/market/stock-market-news/multibagger-defence-stock-apollo-micro-systems-to-raise-3-322-crore-through-fresh-equity-issuance-11783836726858.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-15 (d=0.32), 2024-11-14 (d=0.52)

## Watchlist (below surfacing floor)
midcap_largecap_ratio ↑ (4.59), dyn_meta ↑ (4.55), cross-asset · 3 series ↑ (4.21), gold_silver_ratio ↑ (3.99), dyn_cupid_ns ↑ (3.21), shanghai_comp ↓ (3.12), brent_wti_spread ↑ (2.94), cross-asset · 2 series ↑ (2.86), dyn_coin ↓ (2.34), sofr ↓ (2.19), nifty_it ↑ (2.13), bovespa ↑ (1.96)

## India macro
- nifty_50: 24208.5996 (1d 0.01%, z20 0.86, flag none)
- nifty_midcap_100: 63062.3516 (1d 0.04%, z20 2.03, flag amber)
- usd_inr: 95.6200 (1d 0.24%, z20 1.36, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6050 (1d 0.03%, z20 1.59, flag red)
- Next India prints: India CPI T-0d · NSDL FPI flows T-0d · IMD weekly rainfall T-0d · India WPI T-1d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 36.0 — "Broker’s call: Indian Bank (Buy)"
- COIN (Coinbase Global, Inc.) score 29.6 — "Global Emissions Hit Another Record High Despite Clean Energy Boom"
- HDB (HDFC Bank Limited) score 25.9 — "Broker’s call: Indian Bank (Buy)"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 24.8 — "Broker’s call: Indian Bank (Buy)"
- INDIANB.NS (INDIAN BANK) score 20.3 — "Broker’s call: Indian Bank (Buy)"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 13.7 — "Global Emissions Hit Another Record High Despite Clean Energy Boom"
- SKHYV (SK hynix Inc. American Deposit) score 13.1 — "SK HYNIX VOLATILITY GOES BOTH WAYS SK Hynix plunged a record 15%, dragging the Kospi down "
- KALYANKJIL.NS (KALYAN JEWELLERS IND LTD) score 8.5 — "47% rally in 4 days! Kalyan Jewellers shares rise another 10%. Should you book profit?"
- CHKP (Check Point Software Technolog) score 8.2 — "Kusumgar IPO allotment to be finalised today. Here's GMP, how to check status"
- PCJEWELLER.NS (PC JEWELLER LTD) score 8.1 — "Q1 surprise sends jewellery stocks shining 40% in a month. Will the surge last in next qua"
- BOND (PIMCO Active Bond Exchange-Tra) score 7.8 — "India bonds fall as oil spike, Treasury rout weigh"
- VT (Vanguard Total World Stock Ind) score 6.1 — "Masdar Secures $5.1 Billion for World’s Largest Solar-and-Battery Project"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 5.9 — "HCL Tech Q1 Results 2026: PAT jumps 20%, revenue rises 14%; board declares  ₹12 interim di"
- META (Meta) score 4.6 — "Meta and Amazon are leading a trillion-dollar Big Tech spending spree"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 4.3 — "BAHRAIN SAYS ITS AIR DEFENCES INTERCEPTED AND DESTROYED SEVERAL IRANIAN AERIAL ATTACKS ON "
- MU (Micron Technology, Inc.) score 4.1 — "Micron and other chip stocks feel the pain of imported volatility — blame SK Hynix"
- SWIGGY.NS (SWIGGY LIMITED) score 4.0 — "Swiggy shares slide over 2% after FSSAI issues 9 notices over consumer complaints"
- MS (Morgan Stanley) score 3.7 — "MORGAN STANLEY EXPECTS US HYPERSCALER CAPEX TO REACH $1.2 TRLN BY 2027 MORGAN STANLEY EXPE"
- BHARTIARTL.NS (BHARTI AIRTEL LIMITED) score 3.3 — "Mcap of 4 of top-10 most valued firms jumps ₹92,995 crore; HDFC Bank, Airtel top gainers"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 3.1 — "Vedanta Aluminium, Adani Power, 4 other stocks with up to 24% upside. Do you own any?"
- CUPID.NS (CUPID LIMITED) score 2.8 — "Cupid shares fall 2% after 131% rally in 3 months; Stock reclassified to BSE Group ‘A’"
- JEF (Jefferies Financial Group Inc.) score 2.7 — "Greed and Fear report: Christopher Wood sees 'AI fatigue' setting in. Why Jefferies is tur"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 2.6 — "GE Vernova, Atlanta Electricals among top beneficiaries of India's transmission expansion"
- GS (Goldman Sachs Group, Inc. (The) score 2.4 — "Goldman Sachs pegs Nifty target at 26,500 by June 2027; lists 15 stocks from key themes"
- MCAP (MCAP Inc.) score 2.4 — "Mcap of 4 of top-10 most valued firms jumps ₹92,995 crore; HDFC Bank, Airtel top gainers"
- JUSTDIAL.BO (JUST DIAL LTD.) score 1.9 — "Just Dial shares rocket 14% as profit rises to Rs 166 crore; revenue grows 10% YoY"
- DRREDDY.NS (DR. REDDY S LABORATORIES) score 1.8 — "Broker’s call: Dr Reddy’s Lab (Accumulate)"
- BLK (BlackRock, Inc.) score 1.4 — "SBI Funds IPO anchor book 20 times subscribed; draws Capital Group, BlackRock, Goldman, AD"
- KNACK.BO (KNACK PACKAGING LIMITED) score 1.4 — "Knack Packaging shares list at 11% premium; expert sees further upside"
- AVGO (Broadcom Inc.) score 1.0 — "Is Broadcom stock a buy after Apple's massive chip pact?"
- HLIO (Helios Technologies, Inc.) score 0.9 — "Adani flagship is the next big India pick for Singapore’s Helios"
- RIVN (Rivian Automotive, Inc.) score 0.8 — "Rivian's 75 million-share offering: Why Wall Street hit the sell button"
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 0.7 — "Cochin Shipyard shares dip 2% as govt’s OFS opens for retail investors today"
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