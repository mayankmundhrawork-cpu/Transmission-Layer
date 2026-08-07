# Transmission Layer — board brief · 2026-08-07 09:15Z

data as of **2026-08-07** · 98 series · 8 red / 29 amber · 8 events surfaced (15 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.404, 1d in regime; vol-pct 0.474, breadth-off 0.333, Markov P(high-vol) 0.025)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.4, contra nifty_50 corr20=0.06, last shift 2026-06-08. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.91, corr60 0.83, last shift 2026-05-15. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.42, corr60 0.34, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.19, corr60 -0.04, last shift 2026-06-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.79, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.03, corr60 -0.02, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.24, last shift 2026-05-08. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.12, corr60 0.17, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.494** (n=1159) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.833** (n=2380) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.34] cross-asset · 11 series ↑
- comex_gold [COMMODITIES]: last 4365.20, z20 4.27, zc 1.54, resid-z 2.33 [unexplained], 1d 2.90%, |z20|=4.27; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 64.67, z20 3.92, zc 1.95, resid-z 0.26 [priced], 1d 5.25%, |z20|=3.92; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 67.50, z20 -2.47, zc n/a, resid-z n/a [quiet], 1d -2.23%, GSR<75 (extreme low); |z20|=2.47
- stoxx_50 [INDICES]: last 6527.01, z20 2.44, zc 0.44, resid-z 1.22 [quiet], 1d 0.38%, |z20|=2.44; 1y-pct=100
- cac_40 [INDICES]: last 8716.16, z20 2.25, zc 0.25, resid-z 1.38 [quiet], 1d 0.19%, |z20|=2.25; 1y-pct=100
- dax [INDICES]: last 26316.02, z20 2.13, zc 0.87, resid-z 0.67 [quiet], 1d 0.67%, |z20|=2.13; 1y-pct=100
- comex_copper [COMMODITIES]: last 6.70, z20 2.13, zc 0.08, resid-z 0.28 [quiet], 1d 0.19%, |z20|=2.13; 1y-pct=99; co-occur[metal_copper] same-direction (channel VALID)
- dow_jones [INDICES]: last 53897.82, z20 2.05, zc -0.80, resid-z -0.88 [quiet], 1d -0.83%, |z20|=2.05; 1y-pct=99
- sp500 [INDICES]: last 7711.38, z20 2.02, zc -0.15, resid-z -1.21 [quiet], 1d -0.16%, |z20|=2.02; 1y-pct=99
- dyn_vt [EQUITIES]: last 159.94, z20 2.00, zc -0.13, resid-z -0.25 [quiet], 1d -0.14%, 1y-pct=99
- russell_2000 [INDICES]: last 3001.08, z20 1.23, zc -0.47, resid-z -0.41 [quiet], 1d -0.60%, 1y-pct=96
- **Mechanism**: The recent surge in gold prices is driven by a combination of factors, including firm spot demand, optimism over a potential diplomatic resolution in West Asia, and cooling US rate-hike expectations. This has led to an increase in investments in gold ETFs, with physically backed gold exchange-traded funds seeing positive inflows for the second week in a row. The gold-silver ratio, currently at an extreme low, also suggests a potential rotation into gold. The VALID gold_silver_comove channel indicates that monetary metals are co-moving, and the recent move in gold is likely to be followed by a move in silver.
- **Gap**: No gap: The big raw move in gold is largely priced, with a resid_z of 2.33, indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian instruments that express this move are the nifty_metal index, which has already reacted, and the MCX gold contract, which is trading around Rs 1,50,130 per 10 grams. The nifty_50 and nifty_midcap_100 indices have also reacted, with a rho of 0.537 and 0.513, respectively, via the cac_40 and dax indices.
- Watch next: comex_silver (up) — not yet - watch; Co-occurrence with gold and a VALID gold_silver_comove channel
- Watch next: nifty_metal (up) — already moved; Reaction to comex_silver move via a VALID metal_copper_channel
- **India receivers**: nifty_50 (rho 0.537, z 1.17); nifty_midcap_100 (rho 0.513, z 1.18); nifty_metal (rho 0.448, z 1.81)
- Source: Gold futures rise to Rs 1.50 lakh/10 gm on spot demand — BusinessLine Mkts, 2026-08-07. https://www.thehindubusinessline.com/markets/gold/gold-futures-rise-to-rs-150-lakh10-gm-on-spot-demand/article71316949.ece
- Source: What’s driving Gold above $4,200? Fed bets & West Asia hopes drive rally — BusinessLine Mkts, 2026-08-07. https://www.thehindubusinessline.com/markets/gold/whats-driving-gold-above-4200-fed-bets-west-asia-hopes-drive-rally/article71316659.ece
- Source: Investments in gold ETFs continue to be net positive for 2nd week in a row — BusinessLine Mkts, 2026-08-07. https://www.thehindubusinessline.com/markets/gold/investments-in-gold-etfs-continue-to-be-net-positive-for-2nd-week-in-a-row/article71316667.ece
- Historical analogues: 2024-11-26 (d=0.91), 2025-10-31 (d=0.93), 2024-10-09 (d=0.99)

### [AMBER 4.79] cross-asset · 4 series ↑
- dyn_bond [EQUITIES]: last 90.56, z20 -1.12, zc -1.12, resid-z 0.00 [quiet], 1d -0.34%, 1y-pct=1
- tips_10y_real [RATES]: last 2.41, z20 0.66, zc 0.25, resid-z 0.01 [quiet], 1d 0.42%, 1y-pct=96
- ust_30y [RATES]: last 5.17, z20 0.64, zc -0.24, resid-z -0.75 [quiet], 1d -0.19%, 1y-pct=97
- ust_10y [RATES]: last 4.63, z20 0.07, zc 0.00, resid-z -0.28 [quiet], 1d 0.00%, 1y-pct=95
- **Mechanism**: The recent rise in US Treasury yields, driven by increasing oil prices and concerns about the Strait of Hormuz, is propagating through the VALID gold_silver_comove and metal_copper_channel, potentially impacting Indian metal equities. The RISK_ON regime, with a low probability of high-volatility, suggests a cautious market environment.
- **Gap**: No gap: The big raw move in US Treasury yields is largely priced, with small resid_z values indicating that the market has already accounted for the factors driving the move
- **India take**: Indian metal equities, such as those in the metal_copper_channel, may react to the global copper price movements, while the INR may weaken due to the potential increase in oil prices. The Nifty 50 may also be impacted by the risk-off sentiment, but has not reacted yet.
- Watch next: nifty_50 (down) — not yet - watch; Potential safe-haven bid in gold may lead to a risk-off sentiment, impacting Indian equities
- Watch next: usd_inr (up) — not yet - watch; Oil price increase may lead to a higher import bill, weakening the INR
- Source: As Alphabet burns through cash on AI, it’s turning back to the bond market — MarketWatch Top, 2026-08-06. https://www.marketwatch.com/story/as-alphabet-burns-through-cash-on-ai-its-turning-back-to-the-bond-market-04e85f31?mod=mw_rss_topstories
- Source: US Treasury yields rise as oil climbs before jobs report — Mint Markets, 2026-08-06. https://www.livemint.com/market/us-treasury-yields-rise-as-oil-climbs-before-jobs-report-11786043154633.html
- Source: Alphabet lures investors to mega bond deal with high premiums — Mint Markets, 2026-08-06. https://www.livemint.com/market/stock-market-news/alphabet-lures-investors-to-mega-bond-deal-with-high-premiums-11786034088038.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

### [AMBER 4.44] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1478.70, z20 2.44, zc 0.54, resid-z 0.27 [quiet], 1d 1.75%, |z20|=2.44; 1y-pct=100
- **Mechanism**: The recent increase in mutual funds' stake in Ather Energy for the 5th straight quarter, coupled with the company's production facilities operating at full capacity and demand outpacing supply, suggests a potential bigger rally brewing. This move is likely priced, given the small resid_z of -0.55, indicating that the current price move is largely explained by factor exposures. The VALID metal_copper_channel may also play a role in transmitting global copper price movements to Indian metal equities, including Ather Energy.
- **Gap**: No gap: the current price move is largely explained by factor exposures, as indicated by the small resid_z of -0.55
- **India take**: The Indian instrument that expresses this move is Ather Energy's stock, which has already reacted with a quiet move. Other Indian metal equities, such as those in the Nifty Metal index, may also be affected through the metal_copper_channel.
- Watch next: nifty_50 (up) — not yet - watch; Potential rally in Ather Energy may spill over to the broader Indian market
- Source: Mutual funds increase stake in Ather Energy for 5th straight quarter. Bigger rally brewing? — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/stocks/news/mutual-funds-increase-stake-in-ather-energy-for-5th-straight-quarter-bigger-rally-brewing/articleshow/132981894.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [AMBER 4.34] cross-asset · 2 series ↑
- usd_jpy [FX]: last 158.36, z20 -1.51, zc 1.14, resid-z 1.08 [quiet], 1d 0.48%, |z20|=1.51
- dyn_amzn [EQUITIES]: last 272.20, z20 1.47, zc -0.08, resid-z -0.83 [quiet], 1d -0.17%, 1y-pct=97
- **Mechanism**: The recent intervention by Japan to support the yen has led to a sharp move in usd_jpy, which is now priced given its small resid_z. The move in dyn_amzn is also quiet with a significant resid_z, suggesting it may be driven by factors other than the yen intervention. The correlation between usd_jpy and dyn_amzn is not strong, but the historical analogues suggest a potential follow-through in the aftermath of similar events.
- **Gap**: No gap: the move in usd_jpy is priced given its small resid_z, and the move in dyn_amzn is not clearly driven by the yen intervention
- **India take**: The Indian instrument dyn_muthootfin_ns has reacted to the move in usd_jpy, while dyn_cartrade_ns remains quiet. The transmission candidates suggest a potential follow-through in Indian markets, particularly in metal equities via the metal_copper_channel.
- Watch next: usd_jpy (down) — already moved; intervention-driven move
- Watch next: dyn_amzn (up) — not yet - watch; historical analogue suggests potential follow-through
- **India receivers**: dyn_muthootfin_ns (rho -0.51, z -1.77); dyn_cartrade_ns (rho -0.354, z -0.12)
- Source: Global Market: Japan reveals record $40 billion yen-buying intervention as currency pressure persists — ET Markets, 2026-08-07. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-japan-reveals-record-40-billion-yen-buying-intervention-as-currency-pressure-persists/articleshow/133021238.cms
- Source: Yen Surrenders Nearly Half Its Gains from US-Japan Intervention — Mint Markets, 2026-08-07. https://www.livemint.com/market/yen-surrenders-nearly-half-its-gains-from-us-japan-intervention-11786062248662.html
- Source: Japan Carmakers See Yen Remaining Near Post-Intervention Levels — Mint Markets, 2026-08-06. https://www.livemint.com/market/japan-carmakers-see-yen-remaining-near-post-intervention-levels-11786051302266.html
- Historical analogues: 2024-10-16 (d=0.15), 2024-11-21 (d=0.23), 2026-03-31 (d=0.24)

### [AMBER 4.3] dyn_pltr ↑
- dyn_pltr [EQUITIES]: last 155.98, z20 2.30, zc -0.30, resid-z -0.06 [quiet], 1d -1.55%, |z20|=2.30
- **Mechanism**: The recent surge in dyn_pltr, driven by strong Q2 results, has triggered a risk-off regime, which may propagate through the VALID gold_silver_comove and metal_copper_channel, potentially influencing Indian metal equities. However, the resid_z of -0.06 suggests that the move is largely priced in, leaving limited room for further unexplained movement. The VALID vix_equity_inverse channel may also play a role, as increased volatility could lead to equity drawdowns.
- **Gap**: No gap: the move in dyn_pltr is largely priced in, with a resid_z of -0.06 and a z20 level of 2.30, indicating that the market has already accounted for the strong Q2 results.
- **India take**: The Indian instrument dyn_atherenerg_ns has already reacted, with a rho of 0.401 via dyn_pltr, and may continue to move in tandem with dyn_pltr. Other Indian metal equities may also be influenced through the metal_copper_channel.
- Watch next: dyn_atherenerg_ns (up) — already moved; rho=0.401 via dyn_pltr
- **India receivers**: dyn_atherenerg_ns (rho 0.404, z 2.44)
- Source: Why is Wall Street ignoring the controversy surrounding Palantir? Expert says 'It's not a referendum on ethics' — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/why-is-wall-street-ignoring-the-controversy-surrounding-palantir-expert-says-its-not-a-referendum-on-ethics-11785936805785.html
- Source: Michael Burry warns of 1987-style crash as AI rally powers Wall Street; investor shorts Nvidia, Tesla, Palantir — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/michael-burry-warns-of-1987-style-crash-as-ai-rally-powers-wall-street-investor-shorts-nvidia-tesla-palantir-11785922333250.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-01 (d=0.08), 2025-10-13 (d=0.13)

### [AMBER 4.28] dyn_msft ↑
- dyn_msft [EQUITIES]: last 499.86, z20 2.28, zc 0.67, resid-z -0.53 [quiet], 1d 2.54%, |z20|=2.28
- **Mechanism**: The recent surge in Microsoft's stock price, driven by its AI revenue disclosure, is likely to propagate through the VALID metal_copper_channel, as global copper leads Indian metal equities. However, the resid_z of -0.53 suggests that the move is largely priced in, leaving limited room for further unexplained growth. The RISK_ON regime and VALID vix_equity_inverse channel also support the notion that the market has already factored in the positive news.
- **Gap**: No gap: the resid_z of -0.53 indicates that the move is largely priced in, leaving limited room for further unexplained growth
- **India take**: The Indian instrument that expresses this move is likely to be the Nifty Metal index, which may react positively to the global copper lead, although it has not yet done so. The Hindalco or Tata Steel stocks could also be affected, given their exposure to the metal sector.
- Watch next: nifty_50 (up) — not yet - watch; Indian metal equities may follow global copper's lead
- Source: OPENAI DRIVES MOST OF MICROSOFT'S AI REVENUE Microsoft disclosed it generated $24.1 billion in AI revenue from OpenAI in the year ended June, suggesting the ChatGPT maker accounts for more than half—and possibly around 70%—of its AI business. The figures highlight Microsoft's — DeItaone, 2026-08-05. https://t.me/walter_bloomberg/34422
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.02), 2025-10-20 (d=0.06)

### [AMBER 3.99] dyn_coin ↓
- dyn_coin [EQUITIES]: last 145.35, z20 -1.99, zc -0.61, resid-z 0.03 [quiet], 1d -3.03%, 1y-pct=1
- **Mechanism**: The recent decline in dyn_coin is a priced move with a small resid_z of 0.03, indicating that the move is largely explained by factor exposures. The lack of a significant unexplained component suggests that the move is not an anomaly. The valid channels, such as the gold_silver_comove and metal_copper_channel, do not appear to be driving the move in dyn_coin. Instead, the move may be related to the overall market sentiment, with the European blue-chip earnings growth and the resilience of Singapore's banks contributing to a positive outlook.
- **Gap**: No gap: the move in dyn_coin is largely priced, with a small resid_z and no significant unexplained component.
- **India take**: The Indian instrument that expresses this move is likely to be the metal equities, which may react in tandem with the global metal prices. However, the reaction is yet to be seen.
- Watch next: btc_usd (down) — not yet - watch; high correlation with dyn_coin
- Source: Global Market: European bluechip earnings set for strongest growth since 2022 as energy sector powers profits — ET Markets, 2026-08-07. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-european-bluechip-earnings-set-for-strongest-growth-since-2022-as-energy-sector-powers-profits/articleshow/133028458.cms
- Source: Global Market: Singapore's OCBC, UOB Q2 profits rise as wealth business cushions impact of lower interest rates — ET Markets, 2026-08-07. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-singapores-ocbc-uob-q2-profits-rise-as-wealth-business-cushions-impact-of-lower-interest-rates/articleshow/133027993.cms
- Source: Global Market: China’s July exports top forecasts as AI boom and pre-tariff rush fuel trade growth — ET Markets, 2026-08-07. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-chinas-july-exports-top-forecasts-as-ai-boom-and-pre-tariff-rush-fuel-trade-growth/articleshow/133026299.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-03 (d=0.0), 2025-08-08 (d=0.08)

### [AMBER 3.73] natgas ↓
- natgas [COMMODITIES]: last 2.65, z20 -1.73, zc 0.08, resid-z -0.80 [quiet], 1d 0.27%, |z20|=1.73; 1y-pct=3
- **Mechanism**: The recent decline in natgas prices may propagate through the metal_copper_channel, as global copper leads Indian metal equities. However, the current move in natgas is largely priced, with a resid_z of -0.8, indicating that the unexplained component is relatively small. The valid gold_silver_comove channel may also play a role, as monetary metals co-move and ratio extremes are rotations.
- **Gap**: No gap: the current move in natgas is largely priced, with a small resid_z
- **India take**: The Indian instrument that expresses this move is the Nifty Metal index, which may react to the decline in natgas prices through the metal_copper_channel. However, it has not reacted yet.
- Watch next: nifty_metal (down) — not yet - watch; Indian metal equities may follow global copper
- Source: Middle East War Throws LNG’s Growth Story Into Doubt — OilPrice, 2026-08-05. https://oilprice.com/Energy/Natural-Gas/Middle-East-War-Throws-LNGs-Growth-Story-Into-Doubt.html
- Source: The U.S.-Canada natural gas and electricity trade value rose in 2025 — EIA Today in Energy, 2026-08-05. https://www.eia.gov/todayinenergy/detail.php?id=
- Source: INDIA CONSIDERS GAS CONSUMER LEVIES TO FUND $42 BILLION EXPANSION OF STRATEGIC FUEL RESERVES, SOURCES SAY PLANNED LPG, LNG LEVIES COULD RAISE $1.5 BILLION ANNUALLY FOR BUILDING RESERVES, SOURCES SAY — DeItaone, 2026-08-05. https://t.me/walter_bloomberg/34366
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

## Watchlist (below surfacing floor)
fx · 2 series ↑ (3.69), dyn_bac ↑ (3.5), dyn_indianb_ns ↑ (3.43), dyn_tech ↑ (2.59), dyn_icicigi_bo ↓ (2.55), dyn_cupid_ns ↑ (2.52), asx_200 ↑ (2.32), dyn_lth ↑ (2.22), usd_cny ↓ (1.94), corn ↑ (1.84), nifty_metal ↑ (1.81), nifty_it ↑ (1.5)

## India macro
- nifty_50: 24540.1504 (1d -0.39%, z20 1.17, flag none)
- nifty_midcap_100: 63399.5000 (1d 0.12%, z20 1.18, flag amber)
- usd_inr: 95.2500 (1d 0.18%, z20 -1.27, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5835 (1d 0.51%, z20 -0.54, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI MPC decision T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 101.8 — "LEAP India IPO Day 1: Issue subscribed 6% so far. GMP hints 12% listing gain. Check key da"
- COALINDIA.NS (COAL INDIA LTD) score 100.2 — "LEAP India IPO Day 1: Issue subscribed 6% so far. GMP hints 12% listing gain. Check key da"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 99.7 — "LEAP India IPO Day 1: Issue subscribed 6% so far. GMP hints 12% listing gain. Check key da"
- INDIANB.NS (INDIAN BANK) score 71.1 — "ECB publishes consolidated banking data for end-March 2026"
- TECHM.NS (TECH MAHINDRA LIMITED) score 63.0 — "Aegeus Technologies IPO allotment to be finalised today. Here's GMP, how to check status o"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 62.2 — "Aegeus Technologies IPO allotment to be finalised today. Here's GMP, how to check status o"
- TECH (Bio-Techne Corp) score 59.0 — "Aegeus Technologies IPO allotment to be finalised today. Here's GMP, how to check status o"
- OHI (Omega Healthcare Investors, In) score 57.7 — "AI frenzy spooks investors but JPMorgan CEO Jamie Dimon says spending boom likely to pay o"
- COIN (Coinbase Global, Inc.) score 56.6 — "Global Market: China’s July exports top forecasts as AI boom and pre-tariff rush fuel trad"
- BAC (Bank of America Corporation) score 52.5 — "ECB publishes consolidated banking data for end-March 2026"
- HDB (HDFC Bank Limited) score 49.9 — "ECB publishes consolidated banking data for end-March 2026"
- IDBI.NS (IDBI BANK LIMITED) score 48.1 — "ECB publishes consolidated banking data for end-March 2026"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 48.1 — "ECB publishes consolidated banking data for end-March 2026"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 47.1 — "ECB publishes consolidated banking data for end-March 2026"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 41.0 — "Adani Green Energy shares can rally up to 23%. Why Axis Capital, Elara initiated coverage"
- LTH (Life Time Group Holdings, Inc.) score 35.4 — "Small-cap stock close to life-time high after Q1 results 2026, jumps 3% in opening bell"
- CHKP (Check Point Software Technolog) score 35.4 — "LEAP India IPO Day 1: Issue subscribed 6% so far. GMP hints 12% listing gain. Check key da"
- 301077.SZ (CHINASTARS) score 27.5 — "Global Market: China’s July exports top forecasts as AI boom and pre-tariff rush fuel trad"
- BOND (PIMCO Active Bond Exchange-Tra) score 26.3 — "Indian bonds buckle under oil spike, fresh debt sale"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 15.8 — "Tata Motors PV Share Price Live Updates: Tata Motors PV Climbs Past 100-Day Simple Moving "
- MS (Morgan Stanley) score 14.6 — "AI frenzy spooks investors but JPMorgan CEO Jamie Dimon says spending boom likely to pay o"
- JIOFIN.BO (Jio Financial Services Limited) score 14.2 — "IT stocks lead Nifty gains as financials bleed; West Asia, crude oil weigh on mood"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 13.9 — "Sensex today | Stock Market Live: Sensex down 500 pts, Nifty slips to 24,530; Siemens Ener"
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.8 — "Swiggy shares jump nearly 3% as company targets Rs 10,000 crore adjusted EBITDA by FY31"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 10.3 — "IT stocks lead Nifty gains as financials bleed; West Asia, crude oil weigh on mood"
- VT (Vanguard Total World Stock Ind) score 9.3 — "India tops world in IPO count, ranks third in fundraising in FY26: SEBI Annual Report"
- PCJEWELLER.NS (PC JEWELLER LTD) score 9.0 — "Kalyan Jewellers shares jump 5% after Jefferies starts coverage with 'Buy'. More upside af"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.8 — "Adani Green Energy shares can rally up to 23%. Why Axis Capital, Elara initiated coverage"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.6 — "ICICI Bank Share Price Live Updates: ICICI Bank Market Performance"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 6.6 — "Coal India Share Price Live Updates: Coal India Ltd Stock Details"
- PLTR (Palantir Technologies Inc.) score 5.9 — "Why is Wall Street ignoring the controversy surrounding Palantir? Expert says 'It's not a "
- AMZN (Amazon.com, Inc.) score 5.9 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- NVDA (NVIDIA Corporation) score 5.4 — "NVDA - NVIDIA SHARES HIT HIGHEST IN OVER TWO MONTHS, LAST UP 4.3%"
- META (Meta) score 5.1 — "META AI MODEL ACCESSED INTERNET, HACKED A COMPANY: INFORMATION"
- MSFT (Microsoft Corporation) score 4.9 — "OPENAI DRIVES MOST OF MICROSOFT'S AI REVENUE Microsoft disclosed it generated $24.1 billio"
- AAPL (Apple Inc.) score 4.5 — "AAPL - APPLE RAMPS UP FOR NEXT IPHONE Bank of America reiterated its Buy rating and $380 p"
- SNDK (Sandisk Corporation) score 4.2 — "US stocks mixed as investors await Iran deal details, Western Digital plunges 18.5%, Sandi"
- GOOGL (Alphabet) score 4.1 — "Alphabet seeks up to $25 billion in US bond sale to fund AI spending"
- INFY (Infosys Limited) score 4.0 — "Stocks to watch: Oil India, Infosys, NBCC, Zee, Cohance Life, Gland Pharma, Neuland Lab, M"
- CUPID.NS (CUPID LIMITED) score 0.3 — "Cupid increases investment by $5 million in GII’s Healthcare-focused platform"

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