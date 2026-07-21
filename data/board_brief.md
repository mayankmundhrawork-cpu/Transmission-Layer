# Transmission Layer — board brief · 2026-07-21 11:25Z

data as of **2026-07-21** · 98 series · 9 red / 40 amber · 8 events surfaced (32 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.5, 11d in regime; vol-pct 0.584, breadth-off 0.417, Markov P(high-vol) 0.058)
- [WEAK] **safe_haven_gold** — corr20 0.08, corr60 -0.43, contra nifty_50 corr20=0.14, last shift 2026-05-28. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.82, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.45, corr60 0.34, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.09, corr60 -0.0, last shift 2026-06-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.8, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.07, corr60 -0.07, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.14, corr60 -0.28, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.23, corr60 0.24, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **5 of 89** scanned series survive multiplicity control (effective p ≤ 0.005605629265529988)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.497** (n=1161) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=3097) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.722** (n=18) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.11] dyn_karurvysya_ns ↑
- dyn_karurvysya_ns [EQUITIES]: last 340.45, z20 7.11, zc 6.52, resid-z 6.62 [unexplained], 1d 13.11%, |z20|=7.11; 1y-pct=100
- **Mechanism**: The surge in Karur Vysya Bank's shares is driven by its stellar Q1 results, with a 45% year-on-year jump in net profit to ₹756 crore, supported by strong growth in net interest income and improved net interest margin. This move is largely priced, given the stock's high z20 level of 7.11 and significant residual component of 6.62. The valid channels, such as the gold_silver_comove and metal_copper_channel, do not directly influence this event, which is primarily driven by the bank's fundamentals.
- **Gap**: No gap: the move is largely explained by the bank's strong Q1 results and is reflected in the stock's price
- **India take**: The Indian instruments that express this move are dyn_indusindbk_bo, nifty_midcap_100, and dyn_havells_ns, which have already reacted to the news. The Nifty 50 has also shown some movement, but it remains quiet for now.
- Watch next: dyn_indusindbk_bo (up) — already moved; high correlation with dyn_karurvysya_ns
- **India receivers**: dyn_indusindbk_bo (rho 0.54, z 1.99); nifty_midcap_100 (rho 0.494, z 1.36); dyn_jiofin_bo (rho 0.479, z 0.53); nifty_50 (rho 0.474, z 0.52)
- Source: Karur Vysya Bank shares jump 13% after Q1 profit hits record ₹756 crore — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/karur-vysya-bank-shares-jump-96-after-q1-profit-hits-record-756-crore/article71248009.ece
- Source: Top Gainers & Losers on July 21: Karur Vysya Bank, TVS Motor, Zen Tech, Meesho, Thermax among top gainers today — Mint Markets, 2026-07-21. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-july-21-karur-vysya-bank-tvs-motor-zen-tech-meesho-thermax-among-top-gainers-today-11784625895681.html
- Source: Karur Vysya Bank shares soar 11% after stellar Q1 results. What investors should know — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/stocks/news/karur-vysya-bank-shares-soar-over-11-after-stellar-q1-results-what-investors-should-know/articleshow/132528372.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-02 (d=0.07), 2025-01-31 (d=0.09)

### [RED 7.45] dyn_qessf ↓
- dyn_qessf [EQUITIES]: last 0.19, z20 -5.45, zc 0.60, resid-z 1.05 [quiet], 1d -23.72%, |z20|=5.45
- **Mechanism**: The decline in dyn_qessf is largely priced, with a small resid_z of 1.05, indicating that the move is mostly explained by factor exposures. The vix_equity_inverse channel is valid, suggesting that the vol spike may lead to an equity drawdown. However, the metal_copper_channel and gold_silver_comove channels may also play a role in transmitting the move to Indian metal equities and monetary metals.
- **Gap**: No gap: the move in dyn_qessf is largely priced, with a small resid_z and a low r2 of 0.129, indicating that the price move is mostly explained by factor exposures.
- **India take**: The Indian instrument dyn_atherenerg_ns has already reacted to the move in dyn_qessf, with a rho of -0.358. Other Indian metal equities may also be affected through the metal_copper_channel.
- Watch next: dyn_atherenerg_ns (down) — already moved; reacted to dyn_qessf move
- **India receivers**: dyn_atherenerg_ns (rho -0.359, z 1.41)
- Source: Global Market: Private capital crucial to Europe's defence push as funding bottlenecks persist — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-private-capital-crucial-to-europes-defence-push-as-funding-bottlenecks-persist/articleshow/132528379.cms
- Source: West Asia conflict fuels defence stocks. Now comes the harder test — Mint Markets, 2026-07-20. https://www.livemint.com/market/stock-market-news/india-defence-stocks-rally-west-asia-conflict-next-leg-orders-or-execution-indigenization-procurement-11784518899336.html
- Source: HAL, BEL to Bharat Dynamics: Defence stocks dip after escalation in the US-Iran war — Mint Markets, 2026-07-20. https://www.livemint.com/market/stock-market-news/hal-bel-to-bharat-dynamics-defence-stocks-dip-after-escalation-in-the-us-iran-war-11784521448590.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-15 (d=0.32), 2024-11-14 (d=0.52)

### [AMBER 6.18] cross-asset · 5 series ↓
- russell_2000 [INDICES]: last 2942.33, z20 -2.25, zc -0.35, resid-z 1.55 [unexplained], 1d -0.67%, |z20|=2.25
- nasdaq_100 [INDICES]: last 28607.75, z20 -2.06, zc -1.09, resid-z 0.62 [quiet], 1d 0.05%, |z20|=2.06
- dyn_bond [EQUITIES]: last 91.12, z20 -1.31, zc 0.18, resid-z -0.49 [quiet], 1d -0.37%, 1y-pct=2
- tips_10y_real [RATES]: last 2.31, z20 0.76, zc -0.98, resid-z -2.43 [unexplained], 1d -1.70%, 1y-pct=97
- ust_2y [RATES]: last 4.18, z20 0.37, zc 0.37, resid-z -0.28 [quiet], 1d 0.48%, 1y-pct=96
- **Mechanism**: The recent decline in the Russell 2000 and Nasdaq 100 indices, along with a rise in real yields, may propagate through the valid gold_silver_comove and metal_copper_channel, potentially impacting Indian metal equities. The vix_equity_inverse channel also suggests a vol spike could lead to further equity drawdown. However, the weak and inverted channels, such as safe_haven_gold and real_rates_gold_inverse, are not available as mechanisms.
- **Gap**: No gap: the big raw move in russell_2000 has a relatively small resid_z, indicating it is largely priced in
- **India take**: The Indian instrument that expresses this move is the Nifty 50, which has not yet reacted. Metal equities such as Hindalco may also be impacted due to their exposure to global metal prices.
- Watch next: nifty_50 (down) — not yet - watch; potential risk-off sentiment
- Watch next: hindalco (down) — not yet - watch; exposure to metal equities
- Source: Mapping the Market: Nasdaq troubles run deeper that they appear — Mint Markets, 2026-07-21. https://www.livemint.com/market/mapping-the-market-nasdaq-troubles-run-deeper-that-they-appear-11784628120361.html
- Source: Euro zone bond yields tick higher as oil remains elevated; eyes on ECB — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bond-yields-tick-higher-as-oil-remains-elevated-eyes-on-ecb/articleshow/132531792.cms
- Source: Japan bond jitters overshadow Takaichi's first economic policy roadmap — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/bonds/japan-bond-jitters-overshadow-takaichis-first-economic-policy-roadmap/articleshow/132530718.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.42), 2025-05-20 (d=0.53)

### [AMBER 5.89] fx · 4 series ↑
- aud_usd [FX]: last 0.70, z20 2.23, zc 1.13, resid-z 1.28 [quiet], 1d 0.57%, |z20|=2.23
- usd_brl [FX]: last 5.09, z20 -1.73, zc -0.89, resid-z -1.08 [quiet], 1d -0.69%, |z20|=1.73
- usd_mxn [FX]: last 17.38, z20 -1.54, zc -1.93, resid-z -2.12 [unexplained], 1d -0.89%, |z20|=1.54
- eur_usd [FX]: last 1.14, z20 0.39, zc -0.11, resid-z 0.18 [quiet], 1d -0.04%, 1y-pct=5
- **Mechanism**: The recent tightening of credit standards by Euro zone banks, as reported by the ECB's Bank Lending Survey, has led to a rise in Euro zone government bond yields, which in turn has caused a moderate strengthening of the US dollar against certain currencies, including the Mexican peso and the Brazilian real. This move is largely priced, given the small resid_z values for most series, except for usd_mxn, which shows an unexplained move.
- **Gap**: No gap: the move in usd_mxn is unexplained, but the other series have small resid_z values, indicating that their moves are largely priced
- **India take**: The Indian instrument dyn_karurvysya_ns has reacted, with a rho of -0.371 via usd_mxn, and a z20 of 7.11, indicating a potential transmission of the US dollar strength to the Indian market
- Watch next: usd_mxn (down) — already moved; unexplained move with resid_z=-2.12
- **India receivers**: dyn_karurvysya_ns (rho -0.371, z 7.11)
- Source: Global Market: Euro zone banks tighten credit standards amid geopolitical risks, ECB survey shows — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-banks-tighten-credit-standards-amid-geopolitical-risks-ecb-survey-shows/articleshow/132532469.cms
- Source: Euro zone bond yields tick higher as oil remains elevated; eyes on ECB — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bond-yields-tick-higher-as-oil-remains-elevated-eyes-on-ecb/articleshow/132531792.cms
- Source: July 2026 euro area bank lending survey — ECB press, 2026-07-21. https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260721~44ee50f75c.en.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-19 (d=0.34), 2025-03-31 (d=0.34)

### [RED 5.83] dyn_hdb ↓
- dyn_hdb [EQUITIES]: last 23.59, z20 -3.83, zc 0.17, resid-z 0.54 [quiet], 1d -10.56%, |z20|=3.83; 1y-pct=2
- **Mechanism**: The decline in dyn_hdb is driven by weaker-than-expected net interest margins in the June quarter, which has led to a negative reaction from investors. This move is priced, given the relatively small resid_z of 0.54, indicating that the factor exposures have largely explained the move. The correlation with nifty_50 and india_vix suggests that the Indian market is likely to follow this move.
- **Gap**: No gap: the move in dyn_hdb is largely explained by factor exposures, with a small resid_z of 0.54, indicating that the price move is priced in.
- **India take**: The Indian instrument that expresses this move is nifty_50, which has not yet reacted. Other transmission candidates such as nifty_midcap_100 and dyn_indusindbk_bo have already reacted, while dyn_jiofin_bo remains quiet.
- Watch next: nifty_50 (down) — not yet - watch; Historical lead of 1d and rho=0.669 vs dyn_hdb
- Watch next: india_vix (up) — not yet - watch; Historical lead of 1d and rho=-0.534 vs dyn_hdb
- **India receivers**: nifty_50 (rho 0.669, z 0.52); nifty_midcap_100 (rho 0.524, z 1.36); dyn_indusindbk_bo (rho 0.481, z 1.99); dyn_jiofin_bo (rho 0.465, z 0.53)
- Source: HDFC Bank shares fall over 7 per cent in two days after Q1 earnings — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-fall-over-7-per-cent-in-two-days-after-q1-earnings/article71249104.ece
- Source: Sensex today | Stock Market Live: Sensex drops 250 pts, Nifty below 24,200; HDFC Bank lead losers — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-21st-may-2026/article71245381.ece
- Source: HDFC Bank shares fall for 2nd day but Jefferies, others brokerages remain bullish. Should you buy the dip? — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-bank-shares-fall-for-2nd-day-but-jefferies-others-brokerages-remain-bullish-should-you-buy-the-dip/articleshow/132528929.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [AMBER 5.04] commodities · 2 series ↑
- brent [COMMODITIES]: last 90.30, z20 2.21, zc 0.46, resid-z 1.14 [quiet], 1d 1.21%, |z20|=2.21; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 83.47, z20 2.09, zc 0.11, resid-z 1.00 [quiet], 1d 0.29%, |z20|=2.09
- **Mechanism**: The recent rise in Brent and WTI crude oil prices, despite being largely priced in, may propagate through the metal_copper_channel, given its VALID status, potentially affecting Indian metal equities. However, the primary transmission candidate, inr_oil_channel, is WEAK, suggesting a less direct impact on the Indian rupee. The vix_equity_inverse channel may also play a role, as increased oil prices could lead to higher volatility and subsequent equity drawdowns.
- **Gap**: No gap: the move in Brent and WTI is largely priced in, with resid_z values of 1.14 and 1.0, respectively, indicating that the price movement is mostly explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is the Nifty Midcap 100, which has already reacted to the WTI price movement. The Indian rupee may also be affected, given its historical correlation with oil prices, but the weak inr_oil_channel suggests a less direct impact.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to WTI price movement
- **India receivers**: nifty_midcap_100 (rho -0.619, z 1.36)
- Source: Indian rupee gains as oil comes off; inflows, RBI intervention in focus — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/forex/forex-news/indian-rupee-gains-as-oil-comes-off-inflows-rbi-intervention-in-focus/articleshow/132534364.cms
- Source: India Keeps Buying Russian Oil at Near-Record Pace Despite Expired Waiver — OilPrice, 2026-07-21. https://oilprice.com/Latest-Energy-News/World-News/India-Keeps-Buying-Russian-Oil-at-Near-Record-Pace-Despite-Expired-Waiver.html
- Source: Rupee gains as oil comes off; inflows, RBI intervention in focus — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/forex/rupee-gains-as-oil-comes-off-inflows-rbi-intervention-in-focus/article71248851.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 5.0] dyn_nflx ↓
- dyn_nflx [EQUITIES]: last 67.57, z20 -3.00, zc -4.00, resid-z -2.77 [unexplained], 1d -1.99%, |z20|=3.00; 1y-pct=0
- **Mechanism**: The decline in dyn_nflx is unexplained by factor exposures, with a resid_z of -2.77, indicating a potential anomaly. The valid vix_equity_inverse channel suggests that the vol spike may lead to an equity drawdown. The metal_copper_channel also indicates a potential transmission to Indian metal equities.
- **Gap**: No gap: the big raw move in dyn_nflx has a small resid_z, but it is not an anomaly as the move is largely unexplained by factor exposures, suggesting it is priced
- **India take**: The Indian instrument that expresses this move is the nifty_50, which has not reacted yet. The metal_copper_channel suggests a potential transmission to Indian metal equities such as Hindalco or Tata Steel.
- Watch next: nifty_50 (down) — not yet - watch; Potential risk-off sentiment transmission
- Source: US stocks to buy for short term: From Nvidia to Netflix- Appreciate CEO suggests picking these 5 shares — Mint Markets, 2026-07-20. https://www.livemint.com/market/stock-market-news/us-stocks-to-buy-for-short-term-from-nvidia-to-netflix-appreciate-ceo-suggests-picking-these-5-shares-11784551408198.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-10 (d=0.03), 2025-04-01 (d=0.05)

### [RED 4.58] cross-asset · 2 series ↑
- comex_copper [COMMODITIES]: last 6.53, z20 3.75, zc 1.60, resid-z -0.14 [priced], 1d 3.65%, |z20|=3.75; 1y-pct=98
- gold_silver_ratio [DERIVED]: last 68.59, z20 -0.19, zc n/a, resid-z n/a [quiet], 1d -2.84%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho -0.358 via gold_silver_ratio, z 0.37, quiet)
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.822 vs comex_copper
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.682 vs comex_copper
- Watch next: sp500 (co-move) — not yet - watch; rho 0.603 vs comex_copper
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.554 vs comex_copper
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.525 vs comex_copper
- **India receivers**: nifty_metal (rho -0.358, z 0.37)
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.14), 2024-08-30 (d=0.15)

## Watchlist (below surfacing floor)
dyn_havells_ns ↑ (4.47), commodities · 3 series ↑ (4.36), dyn_pypl ↑ (4.35), dyn_techm_ns ↑ (4.28), dyn_icicigi_bo ↓ (4.15), nikkei_225 ↓ (3.52), usd_cny ↓ (3.18), usd_inr ↑ (3.13), dyn_ohi ↑ (3.03), dyn_bac ↑ (3.01), dyn_inoxindia_ns ↑ (2.93), cross-asset · 2 series ↑ (2.83)

## India macro
- nifty_50: 24193.9492 (1d -0.18%, z20 0.52, flag none)
- nifty_midcap_100: 62976.5000 (1d 0.25%, z20 1.36, flag amber)
- usd_inr: 96.2350 (1d -0.05%, z20 1.13, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6030 (1d 0.44%, z20 0.94, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 77.5 — "Global Market: Indonesia appoints banks for inaugural yuan-denominated panda bond issue"
- INOXINDIA.NS (INOX INDIA LIMITED) score 68.3 — "India signed 8.4 mtpa of long term LNG contracts in 2025: GIIGNL"
- HDB (HDFC Bank Limited) score 68.1 — "Global Market: Indonesia appoints banks for inaugural yuan-denominated panda bond issue"
- BAC (Bank of America Corporation) score 63.7 — "Global Market: Indonesia appoints banks for inaugural yuan-denominated panda bond issue"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 63.5 — "Global Market: Indonesia appoints banks for inaugural yuan-denominated panda bond issue"
- IDBI.NS (IDBI BANK LIMITED) score 53.5 — "Global Market: Indonesia appoints banks for inaugural yuan-denominated panda bond issue"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 48.7 — "Global Markets: Japan's Nikkei rallies after steep decline as focus turns to tech results"
- COIN (Coinbase Global, Inc.) score 45.6 — "Global Market: Ant International raises $1.2 billion to fuel global expansion"
- TECHM.NS (TECH MAHINDRA LIMITED) score 37.2 — "Global Markets: Japan's Nikkei rallies after steep decline as focus turns to tech results"
- CHKP (Check Point Software Technolog) score 23.5 — "Metalic Technoforge IPO Day 1: Issue subscribed 28% so far. Check GMP, issue details"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 22.5 — "India signed 8.4 mtpa of long term LNG contracts in 2025: GIIGNL"
- OHI (Omega Healthcare Investors, In) score 21.6 — "Alpha Wealth 2.0: Why some investors keep finding the next opportunity before everyone els"
- BOND (PIMCO Active Bond Exchange-Tra) score 21.4 — "Global Market: Japan's Takaichi unveils growth blueprint, reiterates investment push amid "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 18.5 — "'What if my father was a plumber?' Why Warren Buffett calls himself one of the world’s 10 "
- VT (Vanguard Total World Stock Ind) score 15.6 — "'What if my father was a plumber?' Why Warren Buffett calls himself one of the world’s 10 "
- ICICIGI.BO (ICICI Lombard General Insuranc) score 11.9 — "Cause for concern? HDFC Bank is lagging ICICI Bank where it matters as investors count Rs "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 11.8 — "Global Market: Indonesia appoints banks for inaugural yuan-denominated panda bond issue"
- GS (Goldman Sachs Group, Inc. (The) score 11.6 — "Inflation is broadening out, says Goldman economist"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.5 — "Adani Energy Q1 Results: Profit zooms 124% YoY to Rs 1,149 crore; revenue jumps 42%"
- JIOFIN.BO (Jio Financial Services Limited) score 9.4 — "FRENCH FOREIGN MINISTER BARROT: TWO EMBASSY OFFICIALS WERE SERIOUSLY INTIMIDATED BY IRANIA"
- META (Meta) score 8.9 — "Metalic Technoforge IPO Day 1: Issue subscribed 28% so far. Check GMP, issue details"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.5 — "Expert view: Overweight on diversified financials, automobiles, new age tech firms, says N"
- MS (Morgan Stanley) score 8.3 — "Bigger crash ahead? JPMorgan CEO Dimon says he won't buy stocks at current prices, says ma"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.9 — "Lumentum’s stock just got a lot more interesting — and Barclays has turned bullish"
- NVDA (NVIDIA Corporation) score 5.7 — "Nvidia among 6 megacaps that Morningstar says are undervalued. See full list"
- PCJEWELLER.NS (PC JEWELLER LTD) score 5.5 — "Bluestone Jewellery shares jump over 19% in biggest one-day gain since listing after Q1 re"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 5.5 — "Global Market: Private capital crucial to Europe's defence push as funding bottlenecks per"
- NFLX (Netflix, Inc.) score 5.0 — "US stocks to buy for short term: From Nvidia to Netflix- Appreciate CEO suggests picking t"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 4.8 — "Tata Technologies Q1 Results: Profit rises 6% to Rs 180 crore"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 4.5 — "Atlanta Electricals shares slide 5% despite strong Q1 results; stock hits lower band"
- SKHYV (SK hynix Inc. American Deposit) score 4.5 — "SKHY – SK HYNIX DOWN 0.7% IN PREMARKET SK Hynix shares are slipping 0.7% in premarket afte"
- BHEL.NS (BHEL) score 4.3 — "BHEL share price: Brokerages see up to 23% upside after Maharatna PSU posts first Q1 profi"
- WIT (Wipro Limited) score 4.1 — "Stocks to watch: Reliance Industries, Wipro, CEAT among shares in focus today; check list "
- AAPL (Apple Inc.) score 4.1 — "Dollar wavers as markets grapple with Gulf tensions"
- PYPL (PayPal Holdings, Inc.) score 3.0 — "How PayPal went from Wall Street favorite to unwilling merger target"
- CEATLTD.NS (CEAT LIMITED) score 2.3 — "Top Gainers & Losers on 20 July: Axis Bank, HDFC Bank, Ceat, India Cements, OLA, HFCL amon"
- KO (Coca-Cola Company (The)) score 1.7 — "Coca-Cola names JPMorgan, Citi as bankers for India bottling unit IPO"
- BIOCON.BO (BIOCON LTD.) score 1.0 — "Mylan exits Biocon, sells entire 5.64% stake for ₹3,679 crore via block deals"
- CUPID.NS (CUPID LIMITED) score 0.7 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 0.5 — "Patanjali Foods share price crashes 20%, extending losses for third straight session; what"

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