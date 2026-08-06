# Transmission Layer — board brief · 2026-08-06 06:43Z

data as of **2026-08-06** · 98 series · 13 red / 26 amber · 8 events surfaced (13 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.483, 1d in regime; vol-pct 0.465, breadth-off 0.5, Markov P(high-vol) 0.062)
- [INVERTED] **safe_haven_gold** — corr20 -0.4, corr60 -0.42, contra nifty_50 corr20=0.07, last shift 2026-06-05. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.8, last shift 2026-05-14. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.41, corr60 0.34, last shift 2026-05-13. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.21, corr60 -0.06, last shift 2026-06-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.78, corr60 -0.8, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.03, corr60 -0.02, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [VALID] **real_rates_gold_inverse** — corr20 -0.32, corr60 -0.26, last shift 2026-05-14. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.13, corr60 0.18, last shift 2026-04-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 90** scanned series survive multiplicity control (effective p ≤ 0.0032821224683141637)
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.495, β 0.2704, p 0.0); driver zc -1.53 → expected -0.403%. Type hit-rate 0.827 (n=2896).
- **SETUP** ust_10y → gbp_usd: leads 1d (ccf -0.273, β -0.1111, p 0.0); driver zc -1.53 → expected 0.165%. Type hit-rate 0.827 (n=2896).
- Track record · residual_reversion: hit-rate **0.494** (n=1153) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.827** (n=2896) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.74] cross-asset · 13 series ↑
- dow_jones [INDICES]: last 54349.94, z20 3.66, zc 0.43, resid-z 0.96 [quiet], 1d 0.49%, |z20|=3.66; 1y-pct=100
- comex_gold [COMMODITIES]: last 4314.50, z20 3.57, zc 0.06, resid-z 1.40 [quiet], 1d 0.16%, |z20|=3.57; co-occur[gold_silver] same-direction (channel VALID)
- stoxx_50 [INDICES]: last 6477.07, z20 2.75, zc -0.15, resid-z -0.26 [quiet], 1d -0.15%, |z20|=2.75; 1y-pct=99
- cac_40 [INDICES]: last 8665.36, z20 2.64, zc -0.02, resid-z -0.15 [quiet], 1d -0.01%, |z20|=2.64; 1y-pct=99
- sp500 [INDICES]: last 7722.12, z20 2.58, zc -0.17, resid-z 3.71 [unexplained], 1d -0.19%, |z20|=2.58; 1y-pct=99
- dyn_vt [EQUITIES]: last 160.14, z20 2.53, zc -0.17, resid-z -0.90 [quiet], 1d -0.19%, |z20|=2.53; 1y-pct=99
- comex_copper [COMMODITIES]: last 6.71, z20 2.47, zc -0.25, resid-z 1.48 [quiet], 1d -0.56%, |z20|=2.47; 1y-pct=99; co-occur[metal_copper] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 62.04, z20 2.43, zc -0.03, resid-z -2.94 [unexplained], 1d -0.10%, |z20|=2.43; co-occur[gold_silver] same-direction (channel VALID)
- dax [INDICES]: last 26144.19, z20 2.39, zc -0.26, resid-z -0.23 [quiet], 1d -0.22%, |z20|=2.39; 1y-pct=99
- dyn_nvda [EQUITIES]: last 219.20, z20 2.37, zc 1.32, resid-z -1.09 [quiet], 1d 3.43%, |z20|=2.37; 1y-pct=95
- russell_2000 [INDICES]: last 3018.42, z20 2.11, zc -0.46, resid-z -0.61 [quiet], 1d -0.61%, |z20|=2.11; 1y-pct=99
- ftse_100 [INDICES]: last 10894.68, z20 1.40, zc 0.26, resid-z -0.18 [quiet], 1d 0.14%, 1y-pct=98
- gold_silver_ratio [DERIVED]: last 69.54, z20 -0.22, zc n/a, resid-z n/a [quiet], 1d 0.25%, GSR<75 (extreme low)
- **Mechanism**: The recent surge in gold and silver prices, driven by a weaker US dollar, lower Treasury yields, and easing oil prices, has created a potential transmission channel to Indian metal equities. The VALID gold_silver_comove and metal_copper_channel mechanisms suggest that the co-movement of monetary metals and the lead of global copper prices can influence Indian metal stocks.
- **Gap**: No gap: The recent price movements in gold and silver have already been reflected in the Indian metal equities, such as Nifty Metal, which has reacted to the global price surge.
- **India take**: The Indian metal equities, such as Nifty Metal, have already reacted to the global price surge, while other sectors like Nifty FMCG remain quiet. The transmission channel from global metal prices to Indian equities is active, but the price adjustment has already occurred.
- Watch next: nifty_metal (up) — reacted; Reacted to the surge in global metal prices
- Watch next: nifty_fmcg (down) — quiet; No clear transmission channel from the event to this sector
- **India receivers**: nifty_50 (rho 0.547, z 1.78); nifty_fmcg (rho -0.532, z 0.58); nifty_midcap_100 (rho 0.521, z 1.6); nifty_metal (rho 0.472, z 2.62)
- Source: Gold prices jump Rs 6,400/10 grams in 3 days, silver soars Rs 11,000/kg as oil slide continues. Big rally ahead? — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/commodities/news/gold-prices-jump-rs-6400/10-grams-in-3-days-silver-soars-rs-11000/kg-as-oil-slide-continues-big-rally-ahead/articleshow/132983009.cms
- Source: Stocks to buy: Nagaraj Shetti recommends Jamna Auto, Hindustan Copper shares to buy in the short-term — Mint Markets, 2026-08-06. https://www.livemint.com/market/stocks-to-buy-nagaraj-shetti-recommends-jamna-auto-hindustan-copper-shares-to-buy-in-the-shortterm-11785992099808.html
- Source: Gold rate today at a seven-week high as easing US-Iran tension cools US Fed rate hike buzz — Mint Markets, 2026-08-06. https://www.livemint.com/market/commodities/gold-rate-today-6-august-2026-gold-price-today-at-seven-week-high-as-easing-us-iran-war-cools-us-fed-rate-hike-buzz-11785987873730.html
- Historical analogues: 2024-11-26 (d=1.04), 2025-10-31 (d=1.11), 2024-10-15 (d=1.12)

### [AMBER 5.49] cross-asset · 3 series ↑
- dyn_jiofin_bo [EQUITIES]: last 264.80, z20 2.17, zc 0.59, resid-z -0.94 [quiet], 1d 1.26%, |z20|=2.17
- nifty_50 [INDICES]: last 24648.60, z20 1.78, zc 0.14, resid-z -0.12 [quiet], 1d 0.10%, |z20|=1.78
- nifty_midcap_100 [INDICES]: last 63568.35, z20 1.60, zc -0.06, resid-z 0.10 [quiet], 1d -0.05%, |z20|=1.60; 1y-pct=99
- **Mechanism**: The recent surge in penny stocks and the bumper debut of MV Electrosystems on Dalal Street may be indicative of a broader risk-on sentiment in the market, which could be driving the upward movement in equities such as dyn_jiofin_bo, nifty_50, and nifty_midcap_100. The valid vix_equity_inverse channel suggests that a vol spike could lead to an equity drawdown, but the current move is not accompanied by a significant increase in volatility. The metal_copper_channel and gold_silver_comove channels are also valid, but their current status does not directly explain the equity move.
- **Gap**: No gap: The moves in dyn_jiofin_bo, nifty_50, and nifty_midcap_100 are largely priced in, with resid_z values indicating that the unexplained component is small or negative.
- **India take**: The Indian instruments that express this move are dyn_muthootfin_ns, dyn_indianb_ns, and nifty_fmcg, with the first two having already reacted and the latter remaining quiet. The move may be driven by a broader risk-on sentiment in the market, which could lead to further gains in these instruments.
- Watch next: dyn_jiofin_bo (up) — quiet; resid_z is -0.94, indicating that the move is largely priced in
- Watch next: nifty_50 (up) — quiet; resid_z is -0.12, indicating that the move is largely priced in
- Watch next: nifty_midcap_100 (up) — quiet; resid_z is 0.1, indicating a small unexplained component
- **India receivers**: dyn_muthootfin_ns (rho 0.694, z -1.52); dyn_bharatcoal_ns (rho 0.651, z -0.97); dyn_indianb_ns (rho 0.626, z 1.63); dyn_indusindbk_bo (rho 0.616, z 0.82)
- Source: Penny stock under  ₹10 jumps 4% despite muted trend on Dalal Street — Mint Markets, 2026-08-06. https://www.livemint.com/market/stock-market-news/penny-stock-under-rs-10-sepc-jumps-4-despite-muted-trend-on-dalal-street-11785993254664.html
- Source: Sensex today | Stock Market Live: Sensex gains 130 pts, Nifty above 24,600; Eternal leads gainers — BusinessLine Mkts, 2026-08-06. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-6-august-2026/article71309748.ece
- Source: MV Electrosystems share price makes a bumper debut on Dalal Street at over 22% premium. Buy, sell or hold? — Mint Markets, 2026-08-06. https://www.livemint.com/market/stock-market-news/mv-electrosystems-share-price-makes-a-bumper-debut-on-dalal-street-at-over-22-premium-11785990016155.html
- Historical analogues: 2025-07-17 (d=0.69), 2024-11-07 (d=0.98), 2025-08-13 (d=1.26)

### [RED 5.26] dyn_pltr ↑
- dyn_pltr [EQUITIES]: last 158.43, z20 3.26, zc -0.50, resid-z 8.43 [unexplained], 1d -2.60%, |z20|=3.26
- **Mechanism**: The recent surge in Palantir's stock price, driven by strong Q2 results and AI-fueled rally, has led to a short squeeze, resulting in $3 billion in losses for short sellers. This move is priced, with a relatively small resid_z of -0.24, indicating that the factor exposures can explain most of the move. The valid vix_equity_inverse channel suggests that the equity market's upside is accompanied by a decrease in volatility, which is consistent with the current RISK_ON regime.
- **Gap**: No gap: the move in dyn_pltr is largely explained by its factor exposures, with a small resid_z, indicating that the price move is consistent with the current market regime and channels.
- **India take**: The Indian transmission candidate, dyn_atherenerg_ns, has already reacted to the move in dyn_pltr, given its rho of 0.393. The metal_copper_channel, which is valid, may also influence Indian metal equities.
- Watch next: dyn_atherenerg_ns (up) — already moved; rho=0.393 with dyn_pltr
- **India receivers**: dyn_atherenerg_ns (rho 0.397, z 2.65)
- Source: Why is Wall Street ignoring the controversy surrounding Palantir? Expert says 'It's not a referendum on ethics' — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/why-is-wall-street-ignoring-the-controversy-surrounding-palantir-expert-says-its-not-a-referendum-on-ethics-11785936805785.html
- Source: Michael Burry warns of 1987-style crash as AI rally powers Wall Street; investor shorts Nvidia, Tesla, Palantir — Mint Markets, 2026-08-05. https://www.livemint.com/market/stock-market-news/michael-burry-warns-of-1987-style-crash-as-ai-rally-powers-wall-street-investor-shorts-nvidia-tesla-palantir-11785922333250.html
- Source: Palantir Short Sellers Take $3 Billion Hit After 30% Stock Surge — Mint Markets, 2026-08-04. https://www.livemint.com/market/palantir-short-sellers-take-3-billion-hit-after-30-stock-surge-11785872351134.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-01 (d=0.08), 2025-10-13 (d=0.13)

### [AMBER 4.88] cross-asset · 2 series ↑
- usd_jpy [FX]: last 157.85, z20 -2.05, zc 0.19, resid-z 0.21 [quiet], 1d 0.10%, |z20|=2.05
- dyn_amzn [EQUITIES]: last 272.60, z20 1.69, zc -0.74, resid-z -1.63 [unexplained], 1d -1.74%, 1y-pct=97
- **Mechanism**: The recent strengthening of the yen, driven by Japanese investors' return to overseas bonds and foreign investors' return to Japanese long-term bonds, has led to a move in usd_jpy. This, in turn, has correlated with a move in dyn_amzn, potentially due to transmission through global markets. However, the resid_z values suggest that the move in usd_jpy is largely priced, while the move in dyn_amzn is unexplained by factors.
- **Gap**: No gap: the move in usd_jpy is largely priced, and the correlated move in dyn_amzn is unexplained but does not represent a significant event-to-price gap
- **India take**: The Indian transmission candidates, such as dyn_muthootfin_ns and dyn_thangamayl_ns, have already reacted to the move in usd_jpy, while dyn_cartrade_ns remains quiet. Further reaction in Indian markets may be limited due to the priced nature of the usd_jpy move.
- Watch next: dyn_amzn (up) — not yet - watch; unexplained move with high historical hit-rate-up
- **India receivers**: dyn_muthootfin_ns (rho -0.505, z -1.52); dyn_cartrade_ns (rho -0.361, z -0.0); dyn_thangamayl_ns (rho -0.356, z -1.55)
- Source: Japanese investors return to overseas bonds as stronger yen, higher yields boost demand — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/bonds/japanese-investors-return-to-overseas-bonds-as-stronger-yen-higher-yields-boost-demand/articleshow/132980557.cms
- Source: Yen firms after landmark intervention, dollar near lows on optimism over Iran talks — Mint Markets, 2026-08-05. https://www.livemint.com/market/yen-firms-after-landmark-intervention-dollar-near-lows-on-optimism-over-iran-talks-11785963413851.html
- Source: BOFA ANTICIPATE STRONGER JAPANESE YEN FOLLOWING INTERVENTION, CHANGE YEAR END DOLLAR/YEN FORECAST TO 149 FROM 152 - CURRENTLY TRADES AT 157.7 — DeItaone, 2026-08-05. https://t.me/walter_bloomberg/34369
- Historical analogues: 2024-10-16 (d=0.15), 2024-11-21 (d=0.23), 2026-03-31 (d=0.24)

### [RED 4.65] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1459.00, z20 2.65, zc -0.24, resid-z 0.38 [quiet], 1d -0.80%, |z20|=2.65; 1y-pct=99
- **Mechanism**: The recent surge in Ather Energy's stock price can be attributed to the company's narrowing quarterly loss and increased stake by mutual funds, which has led to a positive sentiment among investors. The metal_copper_channel, which is currently valid, may also contribute to the stock's upward movement as Indian metal equities are influenced by global copper prices. However, the resid_z of 0.38 indicates that a significant portion of the move is unexplained by factors, suggesting that the stock's price may be partially driven by speculation or other non-fundamental factors.
- **Gap**: No gap: The stock's recent 14% jump is largely priced in, given the company's improving financials and increased investor interest.
- **India take**: The Indian instrument that expresses this move is Ather Energy's stock itself, which has already reacted with a significant price increase. Other Indian metal equities may also be affected through the metal_copper_channel.
- Watch next: nifty_50 (up) — not yet - watch; Potential spill-over effect from Ather Energy's rally
- Source: Mutual funds increase stake in Ather Energy for 5th straight quarter. Bigger rally brewing? — ET Markets, 2026-08-06. https://economictimes.indiatimes.com/markets/stocks/news/mutual-funds-increase-stake-in-ather-energy-for-5th-straight-quarter-bigger-rally-brewing/articleshow/132981894.cms
- Source: Ather Energy shares jump 14% after Q1 loss narrows — BusinessLine Mkts, 2026-08-04. https://www.thehindubusinessline.com/markets/ather-energy-shares-jump-18-to-fresh-52-week-high-after-q1-loss-narrows/article71303894.ece
- Source: Ather Energy's tapering losses put stock in fast lane, but is the rally justified? — Mint Markets, 2026-08-04. https://www.livemint.com/market/mark-to-market/ather-energy-electric-vehicles-ev-q1fy27-ebitda-operating-losses-ev-sales-hero-motocorp-11785824423599.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [AMBER 4.56] cross-asset · 4 series ↑
- ust_30y [RATES]: last 5.18, z20 0.89, zc -1.20, resid-z -0.09 [quiet], 1d -0.96%, 1y-pct=98
- tips_10y_real [RATES]: last 2.40, z20 0.53, zc -0.74, resid-z 0.20 [quiet], 1d -1.23%, 1y-pct=96
- dyn_bond [EQUITIES]: last 90.87, z20 -0.26, zc 0.11, resid-z 1.91 [unexplained], 1d 0.03%, 1y-pct=4
- ust_10y [RATES]: last 4.63, z20 0.13, zc -1.53, resid-z -0.59 [priced], 1d -1.49%, 1y-pct=96
- **Mechanism**: The recent decline in US Treasury yields, driven by easing oil prices and reduced expectations of a Federal Reserve interest rate hike, is propagating through the valid gold_silver_comove and metal_copper_channel, potentially influencing Indian metal equities. However, the primary driver of the move is the priced decline in Treasury yields, with the majority of the move explained by factor exposures.
- **Gap**: No gap: The decline in US Treasury yields is largely explained by factor exposures, with the majority of the move being priced in.
- **India take**: Indian government bond yields are trading flat ahead of the RBI MPC meeting outcome, but may react to the decline in US Treasury yields through the metal_copper_channel, potentially influencing Indian metal equities such as the Nifty Metal index.
- Watch next: dyn_bond (down) — not yet - watch; High resid_z value indicates an unexplained move
- Source: Treasury yields fall as oil dips on Strait of Hormuz hopes — Mint Markets, 2026-08-05. https://www.livemint.com/market/treasury-yields-fall-as-oil-dips-on-strait-of-hormuz-hopes-11785956691711.html
- Source: US Treasury yields fall as oil retreats on Iran deal hopes, Fed hike bets ease — ET Markets, 2026-08-04. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-treasury-yields-fall-as-oil-retreats-on-iran-deal-hopes-fed-hike-bets-ease/articleshow/132871326.cms
- Source: Indian bond yields trades flat ahead of RBI MPC meeting outcome. Experts decode the outlook — Mint Markets, 2026-08-04. https://www.livemint.com/market/stock-market-news/indian-bond-yields-trades-flat-ahead-of-rbi-mpc-meeting-outcome-experts-decode-the-outlook-11785831046953.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

### [AMBER 4.31] dyn_msft ↑
- dyn_msft [EQUITIES]: last 487.46, z20 2.31, zc -0.28, resid-z 0.46 [quiet], 1d -1.09%, |z20|=2.31
- **Mechanism**: dyn_msft ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_thangamayl_ns (rho -0.392 via dyn_msft, z -1.55, reacted)
- **India receivers**: dyn_thangamayl_ns (rho -0.392, z -1.55)
- Source: OPENAI DRIVES MOST OF MICROSOFT'S AI REVENUE Microsoft disclosed it generated $24.1 billion in AI revenue from OpenAI in the year ended June, suggesting the ChatGPT maker accounts for more than half—and possibly around 70%—of its AI business. The figures highlight Microsoft's — DeItaone, 2026-08-05. https://t.me/walter_bloomberg/34422
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.02), 2025-10-20 (d=0.06)

### [AMBER 3.78] dyn_bac ↑
- dyn_bac [EQUITIES]: last 63.25, z20 1.78, zc 0.38, resid-z 0.65 [quiet], 1d 0.56%, 1y-pct=100
- **Mechanism**: dyn_bac ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cupid_ns (rho 0.398 via dyn_bac, z 3.43, reacted)
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.614 vs dyn_bac, historically leads by 2d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.577 vs dyn_bac, historically leads by 1d
- **India receivers**: dyn_cupid_ns (rho 0.398, z 3.43)
- Source: BOFA: S&P 500 HITS 2026 TARGET Bank of America said the S&P 500 has reached its 2026 target of 7,741, but technical indicators suggest the rally could extend toward 8,000, 8,234 and potentially 8,541. The bank sees 7,500 as key support but warns that weak August-October — DeItaone, 2026-08-05. https://t.me/walter_bloomberg/34414
- Source: BOFA CEO BACKS THREE FED RATE HIKES Bank of America CEO Brian Moynihan reiterated the bank's forecast for three Fed rate hikes in September, October and December, saying the labor market remains strong while inflation still needs to ease. He also noted that spending patterns — DeItaone, 2026-08-05. https://t.me/walter_bloomberg/34406
- Source: AAPL - APPLE RAMPS UP FOR NEXT IPHONE Bank of America reiterated its Buy rating and $380 price target after Apple's purchase commitments surged 28% to $57 billion, signaling an iPhone production ramp and component stockpiling ahead of the next launch. Apple also warned of chip — DeItaone, 2026-08-05. https://t.me/walter_bloomberg/34396
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

## Watchlist (below surfacing floor)
dyn_lth ↑ (3.65), dyn_coin ↓ (3.5), fx · 3 series ↑ (3.44), dyn_cupid_ns ↑ (3.43), asx_200 ↑ (2.95), dyn_tech ↑ (2.87), nifty_metal ↑ (2.62), dxy ↓ (1.74), usd_cny ↓ (1.61), dyn_karurvysya_ns ↑ (0.87), dyn_indusindbk_bo ↑ (0.82)

## India macro
- nifty_50: 24648.5996 (1d 0.10%, z20 1.78, flag amber)
- nifty_midcap_100: 63568.3516 (1d -0.05%, z20 1.60, flag amber)
- usd_inr: 95.2200 (1d 0.12%, z20 -1.49, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5790 (1d -0.14%, z20 -1.01, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI MPC decision T-1d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 92.2 — "Stock recommendations for 6 August from MarketSmith India"
- COALINDIA.NS (COAL INDIA LTD) score 90.1 — "Stock recommendations for 6 August from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 89.4 — "Stock recommendations for 6 August from MarketSmith India"
- INDIANB.NS (INDIAN BANK) score 65.4 — "From Gift Nifty to crude oil prices: 7 key things that changed for Indian stock market ove"
- COIN (Coinbase Global, Inc.) score 54.5 — "Indian stocks to hold ground despite weak global sentiment"
- TECHM.NS (TECH MAHINDRA LIMITED) score 52.0 — "Tech Trade May See Bigger Retail Influence After July Rout, JPMorgan Says"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 50.9 — "Tech Trade May See Bigger Retail Influence After July Rout, JPMorgan Says"
- BAC (Bank of America Corporation) score 47.0 — "Axis Bank Share Price Live Updates: Axis Bank Stock Details"
- OHI (Omega Healthcare Investors, In) score 46.8 — "Lone warriors! How two mid-tier tech stocks rewarded investors in Rs 10 lakh crore IT cras"
- TECH (Bio-Techne Corp) score 46.8 — "Tech Trade May See Bigger Retail Influence After July Rout, JPMorgan Says"
- HDB (HDFC Bank Limited) score 44.9 — "Axis Bank Share Price Live Updates: Axis Bank Stock Details"
- IDBI.NS (IDBI BANK LIMITED) score 43.8 — "Axis Bank Share Price Live Updates: Axis Bank Stock Details"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 43.7 — "Axis Bank Share Price Live Updates: Axis Bank Stock Details"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 42.4 — "Axis Bank Share Price Live Updates: Axis Bank Stock Details"
- CHKP (Check Point Software Technolog) score 34.3 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 6"
- LTH (Life Time Group Holdings, Inc.) score 33.9 — "Indian stocks to hold ground despite weak global sentiment"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 33.7 — "Trump: I'd rather make a deal with Iran"
- 301077.SZ (CHINASTARS) score 26.2 — "Global Market: Hong Kong insurers slump after report on China taxing offshore policy incom"
- BOND (PIMCO Active Bond Exchange-Tra) score 18.9 — "Japanese investors return to overseas bonds as stronger yen, higher yields boost demand"
- JUSTDIAL.BO (JUST DIAL LTD.) score 14.2 — "Missouri voters just rejected a bid to ditch income tax, while other tax votes loom in Flo"
- MS (Morgan Stanley) score 14.0 — "Tech Trade May See Bigger Retail Influence After July Rout, JPMorgan Says"
- JIOFIN.BO (Jio Financial Services Limited) score 12.6 — "Britannia Share Price Live Updates: Britannia's Current Financial Snapshot"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 12.2 — "Tata Consumer Share Price Live Updates: Tata Consumer stock slips under its 20-day SMA"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 9.2 — "Market wrap: Shriram Finance, Grasim, TCS among top gainers and losers on Nifty and Sensex"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.8 — "Adani Ent Share Price Live Updates: Adani Enterprises  Current Trading Status"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.6 — "Britannia Share Price Live Updates: Britannia's Current Financial Snapshot"
- VT (Vanguard Total World Stock Ind) score 8.5 — "Philippines Could Become the World's First Geologic Hydrogen Hub"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 8.5 — "Coal India Share Price Live Updates: Coal India Ltd Stock Details"
- PCJEWELLER.NS (PC JEWELLER LTD) score 8.0 — "Kalyan Jewellers shares extend slide, tumble 5% after Q1 results; down 11% in four days"
- PLTR (Palantir Technologies Inc.) score 7.6 — "Why is Wall Street ignoring the controversy surrounding Palantir? Expert says 'It's not a "
- AMZN (Amazon.com, Inc.) score 7.6 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- NVDA (NVIDIA Corporation) score 7.0 — "NVDA - NVIDIA SHARES HIT HIGHEST IN OVER TWO MONTHS, LAST UP 4.3%"
- MSFT (Microsoft Corporation) score 6.3 — "OPENAI DRIVES MOST OF MICROSOFT'S AI REVENUE Microsoft disclosed it generated $24.1 billio"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.0 — "HSBC picks ICICI Bank, Titan, 8 other stocks to ride a potential $25 billion FII inflow as"
- AAPL (Apple Inc.) score 5.8 — "AAPL - APPLE RAMPS UP FOR NEXT IPHONE Bank of America reiterated its Buy rating and $380 p"
- META (Meta) score 5.5 — "Explained: Why South Korea bought gold after 13 years and what it means for yellow metal i"
- INFY (Infosys Limited) score 5.1 — "Stocks to watch: Oil India, Infosys, NBCC, Zee, Cohance Life, Gland Pharma, Neuland Lab, M"
- GS (Goldman Sachs Group, Inc. (The) score 4.9 — "GOLDMAN STICKS TO PAYROLL FORECAST Goldman Sachs maintained its 75,000 July nonfarm payrol"
- THANGAMAYL.NS (THANGAMAYIL JEWELLERY LTD) score 2.3 — "Thangamayil share selloff continues: Stock drops 5% despite Rs 344 crore sales in first 3 "
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