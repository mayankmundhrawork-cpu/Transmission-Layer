# Transmission Layer — board brief · 2026-08-06 10:50Z

data as of **2026-08-06** · 98 series · 13 red / 29 amber · 8 events surfaced (17 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.395, 1d in regime; vol-pct 0.457, breadth-off 0.333, Markov P(high-vol) 0.062)
- [INVERTED] **safe_haven_gold** — corr20 -0.42, corr60 -0.41, contra nifty_50 corr20=0.08, last shift 2026-06-05. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.87, corr60 0.81, last shift 2026-05-14. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.3, corr60 0.32, last shift 2026-05-13. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.21, corr60 -0.06, last shift 2026-06-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.78, corr60 -0.8, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.03, corr60 -0.02, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [VALID] **real_rates_gold_inverse** — corr20 -0.32, corr60 -0.26, last shift 2026-05-14. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.16, corr60 0.18, last shift 2026-04-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 90** scanned series survive multiplicity control (effective p ≤ 0.00020725924734810164)
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.495, β 0.2704, p 0.0); driver zc -1.53 → expected -0.403%. Type hit-rate 0.829 (n=2684).
- **SETUP** ust_10y → gbp_usd: leads 1d (ccf -0.273, β -0.1111, p 0.0); driver zc -1.53 → expected 0.165%. Type hit-rate 0.829 (n=2684).
- Track record · residual_reversion: hit-rate **0.493** (n=1153) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.829** (n=2684) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.45] cross-asset · 12 series ↑
- comex_gold [COMMODITIES]: last 4327.40, z20 4.47, zc 0.91, resid-z 1.40 [quiet], 1d 1.92%, |z20|=4.47; co-occur[gold_silver] same-direction (channel VALID)
- dow_jones [INDICES]: last 54349.94, z20 3.66, zc 0.43, resid-z 0.96 [quiet], 1d 0.49%, |z20|=3.66; 1y-pct=100
- comex_copper [COMMODITIES]: last 6.81, z20 3.35, zc 0.72, resid-z 0.99 [quiet], 1d 1.63%, |z20|=3.35; 1y-pct=100; co-occur[metal_copper] same-direction (channel VALID)
- cac_40 [INDICES]: last 8729.39, z20 2.82, zc 0.89, resid-z -0.09 [quiet], 1d 0.69%, |z20|=2.82; 1y-pct=100
- stoxx_50 [INDICES]: last 6508.58, z20 2.70, zc 0.54, resid-z -0.26 [quiet], 1d 0.49%, |z20|=2.70; 1y-pct=100
- sp500 [INDICES]: last 7722.12, z20 2.58, zc -0.17, resid-z 3.71 [unexplained], 1d -0.19%, |z20|=2.58; 1y-pct=99
- dyn_vt [EQUITIES]: last 160.14, z20 2.53, zc -0.17, resid-z -0.90 [quiet], 1d -0.19%, |z20|=2.53; 1y-pct=99
- comex_silver [COMMODITIES]: last 62.04, z20 2.44, zc -0.03, resid-z -1.64 [unexplained], 1d -0.09%, |z20|=2.44; co-occur[gold_silver] same-direction (channel VALID)
- dyn_nvda [EQUITIES]: last 219.20, z20 2.37, zc 1.32, resid-z -1.09 [quiet], 1d 3.43%, |z20|=2.37; 1y-pct=95
- dax [INDICES]: last 26180.04, z20 2.11, zc 0.25, resid-z -0.30 [quiet], 1d 0.21%, |z20|=2.11; 1y-pct=99
- russell_2000 [INDICES]: last 3018.42, z20 2.11, zc -0.46, resid-z -0.61 [quiet], 1d -0.61%, |z20|=2.11; 1y-pct=99
- ftse_100 [INDICES]: last 10920.84, z20 1.43, zc 0.58, resid-z -0.26 [quiet], 1d 0.30%, 1y-pct=100
- **Mechanism**: The recent surge in gold prices, as seen in COMEX Gold and validated by the production of gold doré at the Altyn Tor Gold Project, is driving the current market move through the VALID gold_silver_comove channel. This is further supported by the increase in gold prices in India across all cities. The move is also correlated with other commodities such as COMEX Copper, which is moving in tandem with global copper leads in Indian metal equities through the VALID metal_copper_channel.
- **Gap**: No gap: the big raw move in COMEX Gold is PRICED, given its z20 level of 4.47 and resid_z of 1.4, indicating that the move is largely explained by factor exposures and not an anomaly.
- **India take**: The Indian instruments Nifty 50 and Nifty Metal have already reacted to the global market trends, with Nifty 50 having a rho of 0.537 with CAC 40 and Nifty Metal having a rho of 0.468 with COMEX Silver. The increase in gold prices in India is also reflected in the prices of 22-carat gold, which has increased by ₹265 per gram.
- Watch next: nifty_50 (up) — already moved; reacted to global market trends
- Watch next: nifty_metal (up) — already moved; reacted to increase in COMEX Copper prices
- **India receivers**: nifty_50 (rho 0.537, z 1.73); nifty_fmcg (rho -0.531, z 0.33); nifty_midcap_100 (rho 0.511, z 1.14); nifty_metal (rho 0.468, z 2.31)
- Source: Sandisk is falling after earnings. Here’s what Wall Street says. — MarketWatch Top, 2026-08-06. https://www.marketwatch.com/story/sandisk-is-falling-after-earnings-heres-what-wall-street-says-591537ec?mod=mw_rss_topstories
- Source: Deccan Gold Mines shares rally 13% after maiden gold doré production at Altyn Tor Project — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/stocks/earnings/deccan-gold-mines-shares-rally-13-after-maiden-gold-dor-production-at-altyn-tor-project/articleshow/132990723.cms
- Source: Today’s Gold Rate in India August 6: Gold prices up in Delhi, Mumbai, Kolkata, Bengaluru, Ahmedabad — BusinessLine Mkts, 2026-08-06. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-mumbai-chennai-ahmedabad-delhi-hyderabad-bengaluru-kolkata-gold-rates-august-6-2026/article71312427.ece
- Historical analogues: 2024-11-21 (d=0.98), 2025-10-31 (d=1.15), 2024-10-04 (d=1.15)

### [AMBER 5.41] cross-asset · 3 series ↑
- dyn_jiofin_bo [EQUITIES]: last 264.00, z20 2.09, zc 0.45, resid-z 0.39 [quiet], 1d 0.96%, |z20|=2.09
- nifty_50 [INDICES]: last 24636.00, z20 1.73, zc 0.07, resid-z -0.12 [quiet], 1d 0.05%, |z20|=1.73
- nifty_midcap_100 [INDICES]: last 63324.85, z20 1.14, zc -0.58, resid-z -0.91 [quiet], 1d -0.43%, 1y-pct=98
- **Mechanism**: The recent move in dyn_jiofin_bo, nifty_50, and nifty_midcap_100 is largely priced, with resid_z values indicating that the big raw move has been explained by factor exposures. The move is likely driven by the RBI's marginal increase in real GDP growth projection for FY27, which has positively impacted the market. However, the lack of reaction in correlated instruments such as india_vix and nifty_fmcg suggests that the market is waiting for further cues.
- **Gap**: No gap: the move in dyn_jiofin_bo, nifty_50, and nifty_midcap_100 is largely explained by factor exposures, with resid_z values indicating that the big raw move is priced
- **India take**: The Indian instruments that express this move are dyn_muthootfin_ns, dyn_bharatcoal_ns, and nifty_metal, which have already reacted to the RBI's growth projection increase. However, dyn_indusindbk_bo and dyn_indianb_ns are still quiet and worth watching.
- Watch next: dyn_jiofin_bo (up) — quiet; resid_z=0.39, r2=0.587
- Watch next: nifty_50 (up) — quiet; resid_z=-0.12, r2=0.092
- Watch next: nifty_midcap_100 (up) — quiet; resid_z=-0.91, r2=0.636
- **India receivers**: dyn_muthootfin_ns (rho 0.692, z -1.76); dyn_bharatcoal_ns (rho 0.649, z -1.0); dyn_indusindbk_bo (rho 0.625, z -0.6); dyn_indianb_ns (rho 0.619, z 1.67)
- Source: Sensex today | Stock Market Live: Sensex up 374 pts; Nifty closes flat — BusinessLine Mkts, 2026-08-06. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-6-august-2026/article71309748.ece
- Source: Standard Chartered gets nod to launch wealth management services from GIFT City — BusinessLine Mkts, 2026-08-06. https://www.thehindubusinessline.com/money-and-banking/standard-chartered-gets-nod-to-launch-wealth-management-services-from-gift-city/article71313016.ece
- Source: DII holdings in Nifty-500 hit record 21%; FII ownership falls to all-time low of 17%: Motilal Oswal — BusinessLine Mkts, 2026-08-06. https://www.thehindubusinessline.com/markets/dii-holdings-in-nifty-500-hit-record-21-fii-ownership-falls-to-all-time-low-of-17-motilal-oswal/article71312576.ece
- Historical analogues: 2025-07-17 (d=0.69), 2024-11-07 (d=0.98), 2025-08-13 (d=1.26)

### [RED 5.26] dyn_pltr ↑
- dyn_pltr [EQUITIES]: last 158.43, z20 3.26, zc -0.50, resid-z 8.43 [unexplained], 1d -2.60%, |z20|=3.26
- **Mechanism**: The recent surge in Palantir's stock price, driven by strong Q2 results and AI-fueled rally, has led to a short squeeze, resulting in $3 billion in losses for short sellers. This move is priced, with a relatively small resid_z of -0.24, indicating that the factor exposures can explain most of the move. The valid vix_equity_inverse channel suggests that the equity market's upside is accompanied by a decrease in volatility, which is consistent with the current RISK_ON regime.
- **Gap**: No gap: the move in dyn_pltr is largely explained by its factor exposures, with a small resid_z, indicating that the price move is consistent with the current market regime and channels.
- **India take**: The Indian transmission candidate, dyn_atherenerg_ns, has already reacted to the move in dyn_pltr, given its rho of 0.393. The metal_copper_channel, which is valid, may also influence Indian metal equities.
- Watch next: dyn_atherenerg_ns (up) — already moved; rho=0.393 with dyn_pltr
- **India receivers**: dyn_atherenerg_ns (rho 0.396, z 2.46)
- Source: Why is Wall Street ignoring the controversy surrounding Palantir? Expert says 'It's not a referendum on ethics' — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/why-is-wall-street-ignoring-the-controversy-surrounding-palantir-expert-says-its-not-a-referendum-on-ethics-11785936805785.html
- Source: Michael Burry warns of 1987-style crash as AI rally powers Wall Street; investor shorts Nvidia, Tesla, Palantir — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/michael-burry-warns-of-1987-style-crash-as-ai-rally-powers-wall-street-investor-shorts-nvidia-tesla-palantir-11785922333250.html
- Source: Palantir Short Sellers Take $3 Billion Hit After 30% Stock Surge — Mint Markets, 2026-08-04. https://www.livemint.com/market/palantir-short-sellers-take-3-billion-hit-after-30-stock-surge-11785872351134.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-01 (d=0.08), 2025-10-13 (d=0.13)

### [AMBER 4.88] cross-asset · 2 series ↑
- usd_jpy [FX]: last 157.84, z20 -2.05, zc 0.18, resid-z 0.13 [quiet], 1d 0.09%, |z20|=2.05
- dyn_amzn [EQUITIES]: last 272.60, z20 1.69, zc -0.74, resid-z -1.63 [unexplained], 1d -1.74%, 1y-pct=97
- **Mechanism**: The recent strengthening of the yen, driven by Japanese investors' return to overseas bonds and foreign investors' return to Japanese long-term bonds, has led to a move in usd_jpy. This, in turn, has correlated with a move in dyn_amzn, potentially due to transmission through global markets. However, the resid_z values suggest that the move in usd_jpy is largely priced, while the move in dyn_amzn is unexplained by factors.
- **Gap**: No gap: the move in usd_jpy is largely priced, and the correlated move in dyn_amzn is unexplained but does not represent a significant event-to-price gap
- **India take**: The Indian transmission candidates, such as dyn_muthootfin_ns and dyn_thangamayl_ns, have already reacted to the move in usd_jpy, while dyn_cartrade_ns remains quiet. Further reaction in Indian markets may be limited due to the priced nature of the usd_jpy move.
- Watch next: dyn_amzn (up) — not yet - watch; unexplained move with high historical hit-rate-up
- **India receivers**: dyn_muthootfin_ns (rho -0.507, z -1.76); dyn_cartrade_ns (rho -0.361, z -0.12); dyn_thangamayl_ns (rho -0.356, z -1.52)
- Source: Japanese investors return to overseas bonds as stronger yen, higher yields boost demand — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/bonds/japanese-investors-return-to-overseas-bonds-as-stronger-yen-higher-yields-boost-demand/articleshow/132980557.cms
- Source: Yen firms after landmark intervention, dollar near lows on optimism over Iran talks — Mint Markets, 2026-08-05. https://www.livemint.com/market/yen-firms-after-landmark-intervention-dollar-near-lows-on-optimism-over-iran-talks-11785963413851.html
- Source: BOFA ANTICIPATE STRONGER JAPANESE YEN FOLLOWING INTERVENTION, CHANGE YEAR END DOLLAR/YEN FORECAST TO 149 FROM 152 - CURRENTLY TRADES AT 157.7 — DeItaone, 2026-08-05. https://t.me/walter_bloomberg/34369
- Historical analogues: 2024-10-16 (d=0.15), 2024-11-21 (d=0.23), 2026-03-31 (d=0.24)

### [AMBER 4.56] cross-asset · 4 series ↑
- ust_30y [RATES]: last 5.18, z20 0.89, zc -1.20, resid-z -0.09 [quiet], 1d -0.96%, 1y-pct=98
- tips_10y_real [RATES]: last 2.40, z20 0.53, zc -0.74, resid-z 0.20 [quiet], 1d -1.23%, 1y-pct=96
- dyn_bond [EQUITIES]: last 90.87, z20 -0.26, zc 0.11, resid-z 1.91 [unexplained], 1d 0.03%, 1y-pct=4
- ust_10y [RATES]: last 4.63, z20 0.13, zc -1.53, resid-z -0.59 [priced], 1d -1.49%, 1y-pct=96
- **Mechanism**: The recent decline in oil prices has eased inflation concerns, leading to a fall in Japanese government bond yields and a subsequent decrease in US Treasury yields. This decrease in yields has resulted in a priced move in the ust_10y, with a small resid_z of -0.59, indicating that the move is largely explained by factor exposures. The dyn_bond, on the other hand, has an unexplained move with a resid_z of 1.91, suggesting that there may be other factors at play.
- **Gap**: No gap: the moves in ust_10y and ust_30y are priced, with small resid_z values, indicating that the market has already incorporated the news into prices
- **India take**: The Indian 10-year government bond yield may react to the decline in US Treasury yields, potentially leading to a decrease in yields. The RBI's dovish stance and falling oil prices have already supported a bond rally in India, and this trend may continue if global yields remain low.
- Watch next: dyn_bond (down) — not yet - watch; unexplained move with high resid_z
- Source: RBI policy-led India bond rally continues; Friday's debt sale in focus — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/bonds/rbi-policy-led-india-bond-rally-continues-fridays-debt-sale-in-focus/articleshow/132993202.cms
- Source: Global Market: Japanese bond yields fall as lower oil prices ease inflation concerns — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japanese-bond-yields-fall-as-lower-oil-prices-ease-inflation-concerns/articleshow/132991673.cms
- Source: Treasury yields fall as oil dips on Strait of Hormuz hopes — Mint Markets, 2026-08-05. https://www.livemint.com/market/treasury-yields-fall-as-oil-dips-on-strait-of-hormuz-hopes-11785956691711.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

### [AMBER 4.46] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1445.00, z20 2.46, zc -0.53, resid-z -0.74 [quiet], 1d -1.75%, |z20|=2.46; 1y-pct=99
- **Mechanism**: The recent surge in Ather Energy's stock price can be attributed to the company's narrowing quarterly loss and increased stake by mutual funds, which has led to a positive sentiment among investors. This move is likely to propagate through the metal_copper_channel, given the VALID status of this channel. The vix_equity_inverse channel also suggests that the low volatility environment is supporting the equity rally.
- **Gap**: No gap: The stock has already reacted to the news with a 14% jump, and the resid_z of -0.74 indicates that the move is largely explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is Ather Energy's stock itself, which has already reacted to the news. Other metal-related stocks in the Indian market may also be watched for potential upside.
- Watch next: nifty_50 (up) — not yet - watch; Positive sentiment in Ather Energy may spill over to the broader market
- Source: Mutual funds increase stake in Ather Energy for 5th straight quarter. Bigger rally brewing? — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/stocks/news/mutual-funds-increase-stake-in-ather-energy-for-5th-straight-quarter-bigger-rally-brewing/articleshow/132981894.cms
- Source: Ather Energy shares jump 14% after Q1 loss narrows — BusinessLine Mkts, 2026-08-04. https://www.thehindubusinessline.com/markets/ather-energy-shares-jump-18-to-fresh-52-week-high-after-q1-loss-narrows/article71303894.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [AMBER 4.31] dyn_msft ↑
- dyn_msft [EQUITIES]: last 487.46, z20 2.31, zc -0.28, resid-z 0.46 [quiet], 1d -1.09%, |z20|=2.31
- **Mechanism**: dyn_msft ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_thangamayl_ns (rho -0.391 via dyn_msft, z -1.52, reacted)
- **India receivers**: dyn_thangamayl_ns (rho -0.391, z -1.52)
- Source: OPENAI DRIVES MOST OF MICROSOFT'S AI REVENUE Microsoft disclosed it generated $24.1 billion in AI revenue from OpenAI in the year ended June, suggesting the ChatGPT maker accounts for more than half—and possibly around 70%—of its AI business. The figures highlight Microsoft's — DeItaone, 2026-08-05. https://t.me/walter_bloomberg/34422
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.02), 2025-10-20 (d=0.06)

### [AMBER 3.78] dyn_bac ↑
- dyn_bac [EQUITIES]: last 63.25, z20 1.78, zc 0.38, resid-z 0.65 [quiet], 1d 0.56%, 1y-pct=100
- **Mechanism**: dyn_bac ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cupid_ns (rho 0.397 via dyn_bac, z 3.48, reacted)
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.614 vs dyn_bac, historically leads by 2d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.577 vs dyn_bac, historically leads by 1d
- **India receivers**: dyn_cupid_ns (rho 0.397, z 3.48)
- Source: BOFA: S&P 500 HITS 2026 TARGET Bank of America said the S&P 500 has reached its 2026 target of 7,741, but technical indicators suggest the rally could extend toward 8,000, 8,234 and potentially 8,541. The bank sees 7,500 as key support but warns that weak August-October — DeItaone, 2026-08-05. https://t.me/walter_bloomberg/34414
- Source: BOFA CEO BACKS THREE FED RATE HIKES Bank of America CEO Brian Moynihan reiterated the bank's forecast for three Fed rate hikes in September, October and December, saying the labor market remains strong while inflation still needs to ease. He also noted that spending patterns — DeItaone, 2026-08-05. https://t.me/walter_bloomberg/34406
- Source: AAPL - APPLE RAMPS UP FOR NEXT IPHONE Bank of America reiterated its Buy rating and $380 price target after Apple's purchase commitments surged 28% to $57 billion, signaling an iPhone production ramp and component stockpiling ahead of the next launch. Apple also warned of chip — DeItaone, 2026-08-05. https://t.me/walter_bloomberg/34396
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

## Watchlist (below surfacing floor)
natgas ↓ (3.69), dyn_lth ↑ (3.65), fx · 3 series ↑ (3.54), usd_inr ↓ (3.53), dyn_coin ↓ (3.5), dyn_cupid_ns ↑ (3.48), gold_silver_ratio ↑ (3.06), asx_200 ↑ (2.95), dyn_tech ↑ (2.87), usd_cny ↓ (2.64), dyn_icicigi_bo ↓ (2.4), nifty_metal ↑ (2.31)

## India macro
- nifty_50: 24636.0000 (1d 0.05%, z20 1.73, flag amber)
- nifty_midcap_100: 63324.8516 (1d -0.43%, z20 1.14, flag amber)
- usd_inr: 95.2000 (1d 0.11%, z20 -1.53, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5704 (1d -0.47%, z20 -1.66, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI MPC decision T-1d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 94.6 — "Today’s Gold Rate in India August 6: Gold prices up in Delhi, Mumbai, Kolkata, Bengaluru, "
- COALINDIA.NS (COAL INDIA LTD) score 92.7 — "Today’s Gold Rate in India August 6: Gold prices up in Delhi, Mumbai, Kolkata, Bengaluru, "
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 92.0 — "Today’s Gold Rate in India August 6: Gold prices up in Delhi, Mumbai, Kolkata, Bengaluru, "
- INDIANB.NS (INDIAN BANK) score 66.9 — "Small-cap stock jumps 3% following Indian stock market rebound"
- COIN (Coinbase Global, Inc.) score 59.3 — "Sensex, Nifty open flat as RBI holds rates, global cues stay mixed"
- TECHM.NS (TECH MAHINDRA LIMITED) score 53.9 — "Global Market: China stocks hold steady as gold miners gain, tech shares slip; Hong Kong d"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 52.9 — "Global Market: China stocks hold steady as gold miners gain, tech shares slip; Hong Kong d"
- OHI (Omega Healthcare Investors, In) score 51.0 — "Juniper Green Energy shares list at 9% premium; Should investors buy sell or hold?"
- TECH (Bio-Techne Corp) score 48.9 — "Global Market: China stocks hold steady as gold miners gain, tech shares slip; Hong Kong d"
- BAC (Bank of America Corporation) score 46.2 — "Global Market: SoftBank's AI strategy stays on course despite flat OpenAI valuation in Q1"
- HDB (HDFC Bank Limited) score 44.2 — "Global Market: SoftBank's AI strategy stays on course despite flat OpenAI valuation in Q1"
- IDBI.NS (IDBI BANK LIMITED) score 43.1 — "Global Market: SoftBank's AI strategy stays on course despite flat OpenAI valuation in Q1"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 43.0 — "Global Market: SoftBank's AI strategy stays on course despite flat OpenAI valuation in Q1"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 41.7 — "Global Market: SoftBank's AI strategy stays on course despite flat OpenAI valuation in Q1"
- LTH (Life Time Group Holdings, Inc.) score 34.6 — "DII holdings in Nifty-500 hit record 21%; FII ownership falls to all-time low of 17%: Moti"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 34.4 — "Juniper Green Energy shares list at 9% premium; Should investors buy sell or hold?"
- CHKP (Check Point Software Technolog) score 32.9 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 6"
- 301077.SZ (CHINASTARS) score 28.2 — "Global Market: China stocks hold steady as gold miners gain, tech shares slip; Hong Kong d"
- BOND (PIMCO Active Bond Exchange-Tra) score 21.2 — "Global Market: Japanese bond yields fall as lower oil prices ease inflation concerns"
- JUSTDIAL.BO (JUST DIAL LTD.) score 14.7 — "Swiggy shares jump nearly 3% as company targets Rs 10,000 crore adjusted EBITDA by FY31"
- MS (Morgan Stanley) score 14.5 — "Somebody will disrupt the market! Why JPMorgan CEO Jamie Dimon is raising alarm over high "
- JIOFIN.BO (Jio Financial Services Limited) score 14.1 — "Can Tips Music's Rs 44 crore share buyback boost its share price? Here's what JM Financial"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.8 — "Can Tata Sons stay unlisted? Here's what RBI Governor Sanjay Malhotra said"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 9.3 — "Can Tips Music's Rs 44 crore share buyback boost its share price? Here's what JM Financial"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 8.9 — "Market wrap: Shriram Finance, Grasim, TCS among top gainers and losers on Nifty and Sensex"
- PCJEWELLER.NS (PC JEWELLER LTD) score 8.7 — "Top Gainers & Losers on 6 August: Navin Fluorine, Tata Tech, HAL, Pine Labs, Kalyan Jewell"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.4 — "Adani Ent Share Price Live Updates: Adani Enterprises  Current Trading Status"
- VT (Vanguard Total World Stock Ind) score 8.2 — "Philippines Could Become the World's First Geologic Hydrogen Hub"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 8.1 — "Coal India Share Price Live Updates: Coal India Ltd Stock Details"
- PLTR (Palantir Technologies Inc.) score 7.3 — "Why is Wall Street ignoring the controversy surrounding Palantir? Expert says 'It's not a "
- AMZN (Amazon.com, Inc.) score 7.3 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- NVDA (NVIDIA Corporation) score 6.7 — "NVDA - NVIDIA SHARES HIT HIGHEST IN OVER TWO MONTHS, LAST UP 4.3%"
- META (Meta) score 6.3 — "META AI MODEL ACCESSED INTERNET, HACKED A COMPANY: INFORMATION"
- MSFT (Microsoft Corporation) score 6.0 — "OPENAI DRIVES MOST OF MICROSOFT'S AI REVENUE Microsoft disclosed it generated $24.1 billio"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.8 — "HSBC picks ICICI Bank, Titan, 8 other stocks to ride a potential $25 billion FII inflow as"
- AAPL (Apple Inc.) score 5.5 — "AAPL - APPLE RAMPS UP FOR NEXT IPHONE Bank of America reiterated its Buy rating and $380 p"
- INFY (Infosys Limited) score 4.9 — "Stocks to watch: Oil India, Infosys, NBCC, Zee, Cohance Life, Gland Pharma, Neuland Lab, M"
- GS (Goldman Sachs Group, Inc. (The) score 4.7 — "GOLDMAN STICKS TO PAYROLL FORECAST Goldman Sachs maintained its 75,000 July nonfarm payrol"
- THANGAMAYL.NS (THANGAMAYIL JEWELLERY LTD) score 2.2 — "Thangamayil share selloff continues: Stock drops 5% despite Rs 344 crore sales in first 3 "
- CUPID.NS (CUPID LIMITED) score 0.4 — "Cupid increases investment by $5 million in GII’s Healthcare-focused platform"

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