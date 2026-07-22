# Transmission Layer — board brief · 2026-07-22 00:16Z

data as of **2026-07-22** · 98 series · 7 red / 43 amber · 8 events surfaced (35 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 1.0, 1d in regime; vol-pct None, breadth-off 1.0, Markov P(high-vol) 0.043)
- [WEAK] **safe_haven_gold** — corr20 0.03, corr60 -0.44, contra nifty_50 corr20=0.13, last shift 2026-05-28. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.91, corr60 0.82, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.45, corr60 0.34, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.07, corr60 -0.01, last shift 2026-06-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.93, corr60 -0.81, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.02, corr60 -0.09, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.14, corr60 -0.28, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.26, corr60 0.25, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.0001446960878501713)
- **SETUP** dyn_coin → aud_usd: leads 1d (ccf 0.266, β 0.033, p 0.00018); driver zc 2.11 → expected 0.318%. Type hit-rate 0.818 (n=3077).
- Track record · residual_reversion: hit-rate **0.497** (n=1164) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=3077) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.722** (n=18) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.11] dyn_karurvysya_ns ↑
- dyn_karurvysya_ns [EQUITIES]: last 340.45, z20 7.11, zc 6.52, resid-z 6.50 [unexplained], 1d 13.11%, |z20|=7.11; 1y-pct=100
- **Mechanism**: The recent surge in Karur Vysya Bank's stock price can be attributed to its strong Q1 FY27 results, with a record profit of ₹756 crore and a net interest margin of 4.26%. This move is priced, given the bank's robust financial performance and the management's guidance on maintaining a net interest margin above 4% in Q2. The transmission candidates, such as dyn_indusindbk_bo and nifty_midcap_100, have already reacted to this news, indicating a priced move rather than an anomaly.
- **Gap**: No gap: the recent move in Karur Vysya Bank's stock price is largely explained by its strong Q1 FY27 results and the management's guidance, leaving no significant event-to-price gap.
- **India take**: The Indian instruments that express this move, such as dyn_indusindbk_bo and nifty_midcap_100, have already reacted to the news, while others like dyn_jiofin_bo and nifty_50 remain quiet. The transmission candidates with higher rho values, like dyn_havells_ns, have also reacted to the news.
- Watch next: dyn_indusindbk_bo (up) — already moved; reacted to Karur Vysya Bank's strong Q1 results
- Watch next: nifty_midcap_100 (up) — already moved; reacted to Karur Vysya Bank's strong Q1 results
- **India receivers**: dyn_indusindbk_bo (rho 0.535, z 1.99); nifty_midcap_100 (rho 0.49, z 1.36); dyn_jiofin_bo (rho 0.475, z 0.53); nifty_50 (rho 0.47, z 0.52)
- Source: Broker’s Call: Karur Vysya Bank (Buy) — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/brokers-call-karur-vysya-bank-buy/article71248725.ece
- Source: Karur Vysya Bank shares jump 13% after Q1 profit hits record ₹756 crore — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/karur-vysya-bank-shares-jump-96-after-q1-profit-hits-record-756-crore/article71248009.ece
- Source: Top Gainers & Losers on July 21: Karur Vysya Bank, TVS Motor, Zen Tech, Meesho, Thermax among top gainers today — Mint Markets, 2026-07-21. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-july-21-karur-vysya-bank-tvs-motor-zen-tech-meesho-thermax-among-top-gainers-today-11784625895681.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-02 (d=0.07), 2025-01-31 (d=0.09)

### [RED 5.94] cross-asset · 3 series ↑
- dyn_coin [EQUITIES]: last 175.92, z20 2.63, zc 2.11, resid-z 0.20 [priced], 1d 9.66%, |z20|=2.63
- btc_usd [CRYPTO]: last 66623.32, z20 1.84, zc 0.23, resid-z 0.57 [quiet], 1d 0.49%, |z20|=1.84
- eth_usd [CRYPTO]: last 1937.41, z20 1.55, zc 0.18, resid-z -0.04 [quiet], 1d 0.72%, |z20|=1.55
- **Mechanism**: The recent cross-asset move in dyn_coin, btc_usd, and eth_usd is primarily driven by priced factors, with resid_z values indicating that the moves are largely explained by factor exposures. The valid vix_equity_inverse channel suggests that the current vol spike may lead to an equity drawdown, which could propagate to the Indian market through transmission candidates such as the Nifty 50. However, the weak channels, including safe_haven_gold, inr_oil_channel, and dxy_inr_channel, limit the potential for a significant risk-off safe-haven bid or EM FX weakness.
- **Gap**: No gap: the recent moves in dyn_coin, btc_usd, and eth_usd are largely priced, with small resid_z values indicating that the unexplained component is minimal.
- **India take**: The Indian instrument that expresses this move is the Nifty 50, which has not yet reacted to the potential equity drawdown. The metal_copper_channel, which is valid, could also transmit the move to Indian metal equities.
- Watch next: nifty_50 (down) — not yet - watch; potential equity drawdown due to vol spike
- Source: OIL HITS FIVE-WEEK HIGH ON MIDDLE EAST ESCALATION Oil prices rose about 2% to a five-week high as renewed U.S.-Iran attacks and Houthi threats to blockade Saudi shipping fueled concerns over global energy supplies. Brent crude climbed above $91 a barrel, while tankers carrying — DeItaone, 2026-07-21. https://t.me/walter_bloomberg/33846
- Source: Global Markets: London Stock Exchange to launch round-the-clock trading next year — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/us-stocks/news/global-markets-london-stock-exchange-to-launch-round-the-clock-trading-next-year/articleshow/132538012.cms
- Source: TRUMP PREPARES NEW ROUND OF TARIFFS President Donald Trump is reportedly preparing a new round of tariffs on dozens of countries ahead of the expiration of the current 10% global tariff this week. According to the Financial Times, the administration is considering keeping the — DeItaone, 2026-07-21. https://t.me/walter_bloomberg/33828
- Historical analogues: 2025-08-11 (d=0.85), 2024-10-31 (d=1.12), 2026-05-05 (d=1.27)

### [AMBER 5.45] cross-asset · 5 series ↑
- dyn_bond [EQUITIES]: last 90.96, z20 -1.52, zc -0.60, resid-z -0.49 [quiet], 1d -0.18%, 1y-pct=1
- ust_30y [RATES]: last 5.11, z20 1.46, zc -0.92, resid-z -1.56 [unexplained], 1d 0.99%, 1y-pct=98
- ust_10y [RATES]: last 4.60, z20 1.44, zc -0.45, resid-z -1.35 [quiet], 1d 1.10%, 1y-pct=98
- tips_10y_real [RATES]: last 2.35, z20 1.38, zc -0.98, resid-z -2.43 [unexplained], 1d 1.73%, 1y-pct=99
- ust_2y [RATES]: last 4.21, z20 1.02, zc 0.37, resid-z -0.28 [quiet], 1d 0.72%, 1y-pct=98
- **Mechanism**: The recent surge in crude oil prices has stoked concern about inflationary pressures, prompting a rise in US Treasury yields, particularly in the 10- and 30-year maturities. This move is largely priced, given the significant increase in oil prices and its impact on inflation expectations. However, the resid_z values for ust_30y, ust_10y, and tips_10y_real suggest some unexplained movement, potentially driven by market anticipation of the Federal Reserve's response to inflation risks.
- **Gap**: No gap: the move in US Treasury yields is largely explained by the surge in crude oil prices and its impact on inflation expectations, with resid_z values indicating some unexplained movement but not a significant anomaly
- **India take**: The Indian instrument that expresses this move is the 10-year GoI yield, which may react to the rise in US Treasury yields, particularly if the RBI decides to raise interest rates in response to inflation concerns. However, the current INR and oil price dynamics may influence the transmission of this move to the Indian market.
- Watch next: dyn_bond (down) — already moved; equity market reacting to rising yields
- Source: Treasury Yields Hit Two-Month High as Oil Sparks Inflation Risk — Mint Markets, 2026-07-21. https://www.livemint.com/market/treasury-yields-hit-two-month-high-as-oil-sparks-inflation-risk-11784645430148.html
- Source: ICICI Bank eyes $500 million dollar bond issue via GIFT City — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/bonds/icici-bank-eyes-500-million-dollar-bond-issue-via-gift-city/articleshow/132538886.cms
- Source: Shorter-dated US Treasury yields ease in line with lower oil price — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/bonds/shorter-dated-us-treasury-yields-ease-in-line-with-lower-oil-price/articleshow/132537161.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [AMBER 4.87] commodities · 2 series ↑
- brent [COMMODITIES]: last 91.54, z20 2.03, zc 0.00, resid-z 0.98 [quiet], 1d 0.00%, |z20|=2.03; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 84.65, z20 1.97, zc 0.00, resid-z 0.70 [quiet], 1d 0.00%, |z20|=1.97
- **Mechanism**: The recent rise in oil prices, led by brent and wti, is driven by geopolitical tensions and supply chain disruptions, particularly in the Hormuz shipping lane. This has led to a build-up in US crude oil inventories, which in turn has driven up oil prices. The move is largely priced, with resid_z values of 0.98 and 0.7 for brent and wti, respectively, indicating that the move is largely explained by factor exposures.
- **Gap**: No gap: the move in oil prices is largely priced, with small resid_z values indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is the nifty_midcap_100, which has already reacted to the brent price move. Further downside is expected in the nifty_midcap_100 due to its negative correlation with brent.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to brent price move
- **India receivers**: nifty_midcap_100 (rho -0.623, z 1.36)
- Source: China's Next Move Could Decide Where Oil Prices Go This Year — OilPrice, 2026-07-22. https://oilprice.com/Energy/Oil-Prices/Chinas-Next-Move-Could-Decide-Where-Oil-Prices-Go-This-Year.html
- Source: Stocks jump with chipmakers; oil rises to 5-week high — Mint Markets, 2026-07-21. https://www.livemint.com/market/stocks-jump-with-chipmakers-oil-rises-to-5-week-high-11784674672538.html
- Source: US Crude Oil Inventories Build As Hormuz Shipping Headache Drags On — OilPrice, 2026-07-21. https://oilprice.com/Latest-Energy-News/World-News/US-Crude-Oil-Inventories-Build-As-Hormuz-Shipping-Headache-Drags-On.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 4.74] dyn_hdb ↓
- dyn_hdb [EQUITIES]: last 23.75, z20 -2.74, zc 0.41, resid-z 0.54 [quiet], 1d 0.61%, |z20|=2.74; 1y-pct=4
- **Mechanism**: The decline in dyn_hdb is attributed to weaker-than-expected net interest margins in the June quarter, leading to a 7% fall in its shares over two trading sessions. This move is priced, given the relatively small resid_z of 0.54, indicating that the decline is largely explained by factor exposures. The valid vix_equity_inverse channel suggests that the vol spike may lead to an equity drawdown, potentially influencing correlated instruments like nifty_50.
- **Gap**: No gap: the decline in dyn_hdb is largely explained by factor exposures, with a small resid_z of 0.54, indicating that the move is priced.
- **India take**: The Indian instrument that expresses this move is nifty_50, which has a rho of 0.657 with dyn_hdb and has not yet reacted. Other transmission candidates like nifty_midcap_100 and dyn_indusindbk_bo have already reacted.
- Watch next: nifty_50 (down) — not yet - watch; historically leads by 1d
- **India receivers**: nifty_50 (rho 0.653, z 0.52); nifty_midcap_100 (rho 0.515, z 1.36); dyn_indusindbk_bo (rho 0.485, z 1.99)
- Source: HDFC Bank shares fall over 7 per cent in two days after Q1 earnings — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-fall-over-7-per-cent-in-two-days-after-q1-earnings/article71249104.ece
- Source: Sensex today | Stock Market Live: Sensex drops 250 pts, Nifty below 24,200; HDFC Bank lead losers — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-21st-may-2026/article71245381.ece
- Source: HDFC Bank shares fall for 2nd day but Jefferies, others brokerages remain bullish. Should you buy the dip? — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-bank-shares-fall-for-2nd-day-but-jefferies-others-brokerages-remain-bullish-should-you-buy-the-dip/articleshow/132528929.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [AMBER 4.47] dyn_havells_ns ↑
- dyn_havells_ns [EQUITIES]: last 1221.00, z20 2.47, zc 1.17, resid-z 1.32 [quiet], 1d 1.72%, |z20|=2.47
- **Mechanism**: The recent move in dyn_havells_ns is largely priced, with a small resid_z of 0.02, indicating that the current price reflects the factor exposures. The move is quiet, with a z20 level of 2.37, which is not unusually high. The correlated instruments, such as dyn_jiofin_bo and nifty_50, have not moved significantly, suggesting that the move in dyn_havells_ns is not part of a broader market trend.
- **Gap**: No gap: the move in dyn_havells_ns is largely priced, with a small resid_z and a z20 level that is not unusually high
- **India take**: The Indian instrument that expresses this move is nifty_midcap_100, which has already reacted. Other correlated instruments, such as dyn_jiofin_bo and nifty_50, have not moved significantly yet.
- Watch next: dyn_jiofin_bo (down) — not yet - watch; historically leads by 2d
- **India receivers**: dyn_jiofin_bo (rho 0.605, z 0.53); nifty_50 (rho 0.573, z 0.52); nifty_midcap_100 (rho 0.532, z 1.36); nifty_fmcg (rho 0.49, z -0.53)
- Source: Havells India’s margin recovery hinges on easing A&P spends, price hikes after weak Q1 — Mint Markets, 2026-07-20. https://www.livemint.com/market/mark-to-market/havells-q1fy27-results-margin-pressure-renewables-lloyd-growth-analysis-11784520642325.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-22 (d=0.01), 2025-06-30 (d=0.02)

### [AMBER 4.46] dyn_hdbfs_bo ↓
- dyn_hdbfs_bo [EQUITIES]: last 720.50, z20 -2.46, zc -0.57, resid-z -0.50 [quiet], 1d -1.04%, |z20|=2.46
- **Mechanism**: The recent decline in dyn_hdbfs_bo is largely priced, with a resid_z of -0.5, indicating that the move is mostly explained by factor exposures. The VALID vix_equity_inverse channel suggests that the vol spike may lead to an equity drawdown, which could be a contributing factor to the decline. However, the metal_copper_channel and gold_silver_comove channels do not provide a clear mechanism for this specific move.
- **Gap**: No gap: the move in dyn_hdbfs_bo is largely priced, with a small resid_z and no clear unexplained component
- **India take**: The Nifty Midcap 100 has already reacted to the decline in dyn_hdbfs_bo, while the Nifty 50 and USD-INR remain quiet. The decline in dyn_hdbfs_bo may have implications for other Indian metal equities, such as Dyn Ceat Ltd NS, which has also reacted to the move.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to dyn_hdbfs_bo decline
- **India receivers**: nifty_midcap_100 (rho 0.545, z 1.36); usd_inr (rho -0.406, z 0.97); nifty_50 (rho 0.398, z 0.52); dyn_ceatltd_ns (rho 0.383, z -1.47)
- Source: HDB Financial to reissue 3-year bonds, bankers say — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/bonds/hdb-financial-to-reissue-3-year-bonds-bankers-say/articleshow/132537022.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-22 (d=0.06), 2025-12-31 (d=0.06)

### [AMBER 4.28] dyn_techm_ns ↑
- dyn_techm_ns [EQUITIES]: last 1577.40, z20 2.28, zc 0.03, resid-z -0.00 [quiet], 1d 0.06%, |z20|=2.28
- **Mechanism**: The recent surge in dyn_techm_ns is largely priced, with a small resid_z of -0.0, indicating that the move is largely explained by factor exposures. The valid vix_equity_inverse channel suggests that the equity drawdown is accompanied by a vol spike, which may be driving the move. However, the weak dxy_inr_channel and real_rates_gold_inverse channels are not available as mechanisms to propagate this move.
- **Gap**: No gap: the move in dyn_techm_ns is largely priced, with a small resid_z and a quiet move label
- **India take**: The Indian instrument nifty_it has already reacted to the move in dyn_techm_ns, given its high correlation of 0.897. Additionally, dyn_tataelxsi_ns has also reacted, with a correlation of 0.48.
- Watch next: nifty_it (down) — already moved; high correlation with dyn_techm_ns
- **India receivers**: nifty_it (rho 0.897, z 1.34); dyn_tataelxsi_ns (rho 0.48, z -1.53)
- Source: Mahindra Finance Q1 Results: Profit jumps 75% to Rs 927 crore on higher interest margin, lower provisions — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/stocks/earnings/mahindra-finance-q1-results-profit-jumps-75-to-rs-927-crore-on-higher-interest-margin-lower-provisions/articleshow/132540799.cms
- Source: Q1 Results Today Highlights: UltraTech profit rises; IOB, KVB and Sobha post strong Q1 growth; Mahindra Logistics, Dynamic Cables, Jaiprakash Power, Shyam Metalics surge — BusinessLine Mkts, 2026-07-20. https://www.thehindubusinessline.com/markets/q1-results-today-highlights-cement-paytm-iob-karur-vysya-bank-shyam-metalics-sobha-jp-power-bluestone-hdfc-bank-kotak-icici-yes-bank-axis-bank-ril-results-20-july-2026/article71241085.ece
- Source: Q1 Results Today Live: UltraTech PAT up, IOB, KVB Q1 PAT climb, Mahindra Logistics, Dynamic Cables & Shyam Metalics zoom, Paytm, Sobha, JP Power, Bluestone to announce Q1 results — BusinessLine Mkts, 2026-07-20. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-ultratech-cement-paytm-iob-karur-vysya-bank-shyam-metalics-sobha-jp-power-bluestone-hdfc-bank-kotak-icici-yes-bank-axis-bank-ril-results-20-july-2026/article71241085.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-11 (d=0.03), 2025-02-10 (d=0.09)

## Watchlist (below surfacing floor)
dyn_qessf ↓ (4.22), dyn_icicigi_bo ↓ (4.15), dyn_nflx ↓ (4.03), dyn_ohi ↑ (3.87), commodities · 3 series ↑ (3.85), dyn_bac ↑ (3.5), gold_silver_ratio ↑ (3.02), usd_inr ↑ (2.97), dyn_inoxindia_ns ↑ (2.93), fx · 2 series ↑ (2.85), cross-asset · 2 series ↑ (2.83), dyn_adanient_bo ↑ (2.82)

## India macro
- nifty_50: 24193.9492 (1d -0.18%, z20 0.52, flag none)
- nifty_midcap_100: 62976.5000 (1d 0.25%, z20 1.36, flag amber)
- usd_inr: 96.2250 (1d -0.27%, z20 0.97, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6030 (1d 0.44%, z20 0.94, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 74.1 — "Bandhan Bank Q1 profit jumps 35% as provisions decline sharply"
- INOXINDIA.NS (INOX INDIA LIMITED) score 66.9 — "India Pulls Back From Iraqi Oil as Hormuz Turns Too Dangerous"
- HDB (HDFC Bank Limited) score 64.9 — "Bandhan Bank Q1 profit jumps 35% as provisions decline sharply"
- BAC (Bank of America Corporation) score 61.0 — "Bandhan Bank Q1 profit jumps 35% as provisions decline sharply"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 60.8 — "Bandhan Bank Q1 profit jumps 35% as provisions decline sharply"
- IDBI.NS (IDBI BANK LIMITED) score 51.9 — "Bandhan Bank Q1 profit jumps 35% as provisions decline sharply"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 44.9 — "Biotech IPO Gains Crush AI Listings With Standout 55% Return"
- COIN (Coinbase Global, Inc.) score 43.1 — "OIL HITS FIVE-WEEK HIGH ON MIDDLE EAST ESCALATION Oil prices rose about 2% to a five-week "
- TECHM.NS (TECH MAHINDRA LIMITED) score 35.7 — "Biotech IPO Gains Crush AI Listings With Standout 55% Return"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 26.4 — "India Pulls Back From Iraqi Oil as Hormuz Turns Too Dangerous"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 23.1 — "CME feeder cattle futures slump on hot weather, grain prices"
- OHI (Omega Healthcare Investors, In) score 22.9 — "Cube Highways Trust collects Rs 1,687 crore from anchor investors ahead of IPO"
- BOND (PIMCO Active Bond Exchange-Tra) score 22.7 — "India bonds fall as Middle East escalation drives oil above $90"
- CHKP (Check Point Software Technolog) score 20.7 — "Metalic Technoforge IPO Day 1: Issue subscribed 28% so far. Check GMP, issue details"
- VT (Vanguard Total World Stock Ind) score 16.7 — "Fossil Fuels Still Generate 57% of the World's Electricity"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 15.1 — "Bandhan Bank Q1 profit jumps 35% as provisions decline sharply"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 11.4 — "ICICI Bank eyes $500 million dollar bond issue via GIFT City"
- JIOFIN.BO (Jio Financial Services Limited) score 11.1 — "U.S. SENATOR COLLINS SAYS SOME MILITARY SERVICES FACE NEAR-TERM SOLVENCY CHALLENGES"
- GS (Goldman Sachs Group, Inc. (The) score 10.2 — "Inflation is broadening out, says Goldman economist"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.2 — "Adani Energy Solutions among 4 large-caps that hit 52-week highs & rallied up to 16% in a "
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 9.3 — "TRUMP PREPARES NEW ROUND OF TARIFFS President Donald Trump is reportedly preparing a new r"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.0 — "TRUMP ON HOUTHI BLOCKADE: IF SOMETHING HAPPENS WE'LL JUST HAVE TO TAKE CARE OF BUSINESS"
- META (Meta) score 7.8 — "Metalic Technoforge IPO Day 1: Issue subscribed 28% so far. Check GMP, issue details"
- MS (Morgan Stanley) score 7.3 — "Bigger crash ahead? JPMorgan CEO Dimon says he won't buy stocks at current prices, says ma"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 6.9 — "Fossil Fuels Still Generate 57% of the World's Electricity"
- NVDA (NVIDIA Corporation) score 5.0 — "Nvidia among 6 megacaps that Morningstar says are undervalued. See full list"
- PCJEWELLER.NS (PC JEWELLER LTD) score 4.9 — "Bluestone Jewellery shares jump over 19% in biggest one-day gain since listing after Q1 re"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 4.8 — "Global Market: Private capital crucial to Europe's defence push as funding bottlenecks per"
- NFLX (Netflix, Inc.) score 4.4 — "US stocks to buy for short term: From Nvidia to Netflix- Appreciate CEO suggests picking t"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 4.3 — "Tata Technologies Q1 Results: Profit rises 6% to Rs 180 crore"
- SKHYV (SK hynix Inc. American Deposit) score 4.0 — "SKHY – SK HYNIX DOWN 0.7% IN PREMARKET SK Hynix shares are slipping 0.7% in premarket afte"
- BHEL.NS (BHEL) score 3.8 — "BHEL share price: Brokerages see up to 23% upside after Maharatna PSU posts first Q1 profi"
- WIT (Wipro Limited) score 3.6 — "Stocks to watch: Reliance Industries, Wipro, CEAT among shares in focus today; check list "
- AAPL (Apple Inc.) score 3.6 — "Dollar wavers as markets grapple with Gulf tensions"
- PYPL (PayPal Holdings, Inc.) score 2.7 — "How PayPal went from Wall Street favorite to unwilling merger target"
- CEATLTD.NS (CEAT LIMITED) score 2.0 — "Top Gainers & Losers on 20 July: Axis Bank, HDFC Bank, Ceat, India Cements, OLA, HFCL amon"
- KO (Coca-Cola Company (The)) score 1.5 — "Coca-Cola names JPMorgan, Citi as bankers for India bottling unit IPO"
- BIOCON.BO (BIOCON LTD.) score 0.9 — "Mylan exits Biocon, sells entire 5.64% stake for ₹3,679 crore via block deals"
- CUPID.NS (CUPID LIMITED) score 0.6 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 0.4 — "Patanjali Foods share price crashes 20%, extending losses for third straight session; what"

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