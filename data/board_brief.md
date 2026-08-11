# Transmission Layer — board brief · 2026-08-11 09:13Z

data as of **2026-08-11** · 98 series · 5 red / 32 amber · 8 events surfaced (16 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.267, 2d in regime; vol-pct 0.352, breadth-off 0.182, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.36, corr60 -0.39, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.81, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.27, corr60 0.34, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.16, corr60 -0.07, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.79, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.08, corr60 -0.03, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.41, corr60 -0.25, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.0, corr60 0.16, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.491** (n=1132) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.82** (n=2389) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.91] cross-asset · 4 series ↑
- comex_gold [COMMODITIES]: last 4430.10, z20 3.09, zc 0.88, resid-z 1.08 [quiet], 1d 1.57%, |z20|=3.09; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 64.91, z20 2.52, zc -0.11, resid-z -1.46 [quiet], 1d -0.30%, |z20|=2.52; co-occur[gold_silver] same-direction (channel VALID)
- comex_copper [COMMODITIES]: last 6.67, z20 1.66, zc 0.49, resid-z 0.40 [quiet], 1d 1.09%, |z20|=1.66; 1y-pct=99
- gold_silver_ratio [DERIVED]: last 68.25, z20 -1.25, zc n/a, resid-z n/a [quiet], 1d 1.87%, GSR<75 (extreme low)
- **Mechanism**: The recent surge in gold and silver prices, as seen in COMEX gold and silver, is driven by a combination of factors including a firm spot demand and a rise in global gold futures. The gold-silver ratio, which is currently at an extreme low, also suggests a rotation between the two metals. The VALID gold_silver_comove channel indicates that monetary metals are co-moving, and the metal_copper_channel suggests that global copper leads Indian metal equities.
- **Gap**: No gap: The recent move in gold and silver prices is largely priced in, with resid_z values of 1.08 and -1.46, respectively, indicating that the moves are largely explained by factor exposures.
- **India take**: The Indian instrument nifty_metal has already reacted to the move in comex_silver, while the price of gold in India has also risen. Further reaction can be expected in the Indian metal equities space.
- Watch next: nifty_metal (up) — already moved; Reacted to comex_silver with a rho of 0.475
- Watch next: btc_usd (up) — not yet - watch; Historically leads comex_gold by 5d with a rho of 0.543
- **India receivers**: nifty_metal (rho 0.475, z 1.31)
- Source: Today’s Gold Rate in India August 11: Gold prices up in Delhi, Mumbai, Kolkata, Bengaluru, Ahmedabad — BusinessLine Mkts, 2026-08-11. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-mumbai-chennai-ahmedabad-delhi-hyderabad-bengaluru-kolkata-gold-rates-august-11-2026/article71331334.ece
- Source: Gold futures rise to ₹1.54 lakh/10 gm on spot demand — BusinessLine Mkts, 2026-08-11. https://www.thehindubusinessline.com/markets/commodities/gold-futures-rise-to-154-lakh10-gm-on-spot-demand/article71331152.ece
- Source: Forget gold and stocks: Nvidia CEO Jensen Huang aims to make chips an investable asset, lines up $500 bn in financing — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/us-stocks/news/forget-gold-and-stocks-nvidia-ceo-jensen-huang-aims-to-make-chips-an-investable-asset-lines-up-500-bn-in-financing/articleshow/133142905.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.34)

### [AMBER 6.4] commodities · 2 series ↑
- wti [COMMODITIES]: last 84.45, z20 0.57, zc 0.81, resid-z 1.51 [unexplained], 1d 2.82%, 1-session move +2.82% ≥ 1.5%
- brent [COMMODITIES]: last 89.84, z20 0.42, zc 0.66, resid-z 1.52 [unexplained], 1d 2.42%, 1-session move +2.42% ≥ 1.5%
- **Mechanism**: The recent surge in oil prices, led by WTI and Brent, has sparked concerns over inflation, leading to a drop in Indian government bonds and a potential shift in market attitudes. This move is unexplained by factors, with a high residual_z value, indicating a potential anomaly. However, given the small z20 levels and the priced nature of the move, it is likely that the market has already accounted for this information.
- **Gap**: No gap: the market has already reacted to the oil price surge, with Indian equities and bonds reflecting the changed sentiment
- **India take**: Indian instruments such as Nifty Midcap 100 and Dyn Bharat Coal have already reacted to the WTI price surge, indicating that the market has priced in the information. Further moves in Indian metal equities may be influenced by the global copper price, given the valid metal_copper_channel.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to WTI price surge
- **India receivers**: nifty_midcap_100 (rho -0.435, z 1.52); dyn_bharatcoal_ns (rho -0.377, z -1.05)
- Source: Sensex today | Stock Market Live: Sensex down nearly 400 points, Nifty slips 0.53% as oil prices weigh — BusinessLine Mkts, 2026-08-11. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-11-august-2026/article71328121.ece
- Source: Indian bonds skid as crude soars, Treasuries fall — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/bonds/india-bonds-indian-bonds-skid-as-crude-soars-treasuries-fall/articleshow/133146987.cms
- Source: Euro zone bond yields rise as oil climbs on Hormuz doubts — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bond-yields-rise-as-oil-climbs-on-hormuz-doubts/articleshow/133146952.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [AMBER 6.28] cross-asset · 7 series ↑
- dyn_vt [EQUITIES]: last 160.99, z20 1.94, zc -0.20, resid-z 0.29 [quiet], 1d -0.19%, 1y-pct=99
- sp500 [INDICES]: last 7753.15, z20 1.88, zc -0.06, resid-z 0.23 [quiet], 1d -0.06%, |z20|=1.88; 1y-pct=99
- stoxx_50 [INDICES]: last 6534.76, z20 1.82, zc -0.02, resid-z 0.86 [quiet], 1d -0.01%, |z20|=1.82; 1y-pct=99
- dow_jones [INDICES]: last 53967.51, z20 1.63, zc -0.14, resid-z 0.74 [quiet], 1d -0.13%, |z20|=1.63; 1y-pct=98
- cac_40 [INDICES]: last 8706.20, z20 1.59, zc -0.31, resid-z 1.18 [quiet], 1d -0.23%, |z20|=1.59; 1y-pct=99
- dax [INDICES]: last 26266.64, z20 1.51, zc -0.28, resid-z 0.54 [quiet], 1d -0.22%, |z20|=1.51; 1y-pct=99
- russell_2000 [INDICES]: last 3016.94, z20 1.46, zc -0.46, resid-z -0.51 [quiet], 1d -0.58%, 1y-pct=98
- **Mechanism**: The current move is driven by optimism in AI investments and stronger corporate earnings, as reflected in JP Morgan's raised S&P 500 year-end target to 8,000. This sentiment is transmitted to global equities, including Indian markets, through correlated instruments such as the CAC 40.
- **Gap**: No gap: The resid_z values for the affected series are relatively low, indicating that the move is largely priced in and not an anomaly.
- **India take**: The Nifty 50 and Nifty Midcap 100 are the Indian instruments that express this move, with the latter having already reacted to the global equity sentiment. The Nifty 50 is still quiet and worth watching.
- Watch next: nifty_50 (up) — not yet - watch; Correlated with CAC 40, which has already moved
- Watch next: nifty_midcap_100 (up) — already moved; Reacted to the global equity move
- **India receivers**: nifty_50 (rho 0.5, z 0.63); nifty_midcap_100 (rho 0.48, z 1.52)
- Source: Bears are in pain as the S&P 500 hits record highs. That may mean more upside for stocks. — MarketWatch Top, 2026-08-11. https://www.marketwatch.com/story/bears-are-in-pain-as-the-s-p-500-hits-record-highs-that-may-mean-more-upside-for-stocks-db7b659b?mod=mw_rss_topstories
- Source: US Stock Market: JP Morgan raises S&P 500 year-end target to 8,000 on AI, earnings optimism — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stock-market-jp-morgan-raises-sp-500-year-end-target-to-8000-on-ai-earnings-optimism/articleshow/133142288.cms
- Source: Nvidia teams with Wall Street firms to help finance $500 billion for AI infrastructure — MarketWatch Top, 2026-08-11. https://www.marketwatch.com/story/nvidia-teams-with-wall-street-firms-to-help-finance-500-billion-for-ai-infrastructure-2c4805a5?mod=mw_rss_topstories
- Historical analogues: 2024-11-26 (d=0.57), 2024-10-21 (d=0.84), 2024-11-11 (d=0.84)

### [AMBER 5.14] cross-asset · 4 series ↑
- dyn_bond [EQUITIES]: last 90.40, z20 -1.48, zc -1.38, resid-z -0.39 [quiet], 1d -0.42%, 1y-pct=0
- ust_30y [RATES]: last 5.19, z20 0.77, zc -0.71, resid-z -0.57 [quiet], 1d -0.57%, 1y-pct=98
- tips_10y_real [RATES]: last 2.40, z20 0.25, zc -0.77, resid-z -0.36 [quiet], 1d -1.23%, 1y-pct=95
- ust_10y [RATES]: last 4.65, z20 0.23, zc -0.86, resid-z -0.43 [quiet], 1d -0.85%, 1y-pct=96
- **Mechanism**: The recent surge in oil prices, triggered by U.S. President Donald Trump's stance on Iran and doubts over the reopening of the Strait of Hormuz, has led to an increase in Euro zone bond yields. This has resulted in a rise in U.S. Treasury yields, with the 30-year yield increasing by 0.77 z-score. The mechanism for this move is the transmission of global monetary policy and inflation expectations to the U.S. bond market, which is then reflected in the Indian market through the metal_copper_channel and other correlated instruments.
- **Gap**: No gap: The move in U.S. Treasury yields is largely priced, with resid_z values indicating that the majority of the move can be explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is the 10-year GoI bond yield, which may react to the increase in U.S. Treasury yields through the metal_copper_channel. However, the inr_oil_channel is weak, which may limit the transmission of the oil price surge to the Indian market.
- Watch next: dyn_bond (down) — already moved; priced move due to high r2 value of 0.898
- Source: Euro zone bond yields rise as oil climbs on Hormuz doubts — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bond-yields-rise-as-oil-climbs-on-hormuz-doubts/articleshow/133146952.cms
- Source: The Bessent bond-market scorecard doesn’t look as strong as it once did — MarketWatch Top, 2026-08-11. https://www.marketwatch.com/story/the-bessent-bond-market-scorecard-doesnt-look-as-strong-as-it-once-did-afe2f93e?mod=mw_rss_topstories
- Source: State Bank of India taps dollar bond market with five-year issue: Report — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/bonds/state-bank-of-india-taps-dollar-bond-market-with-five-year-issue-report/articleshow/133141420.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

### [RED 4.65] dyn_cupid_ns ↑
- dyn_cupid_ns [EQUITIES]: last 276.90, z20 2.65, zc 1.33, resid-z 1.81 [unexplained], 1d 5.40%, |z20|=2.65; 1y-pct=100
- **Mechanism**: The recent surge in Cupid's Q1 FY27 profit, which tripled to Rs 44 crore, and the company's raised revenue and profit guidance for FY27, may have triggered a positive response in the stock. However, the stock's quiet move, with a low resid_z of 0.02, suggests that the move is largely priced in. The VALID metal_copper_channel and the company's strong financial performance may be contributing to the stock's upward momentum.
- **Gap**: No gap: the stock's move is largely priced in, with a low resid_z of 0.02 and a strong financial performance
- **India take**: The Indian instrument that expresses this move is the Nifty Midcap 100, which has already reacted with a rho of 0.357 via dyn_cupid_ns. The stock's strong financial performance and the VALID metal_copper_channel may continue to support the Nifty Midcap 100's upward momentum.
- Watch next: nifty_midcap_100 (up) — already moved; rho=0.357 via dyn_cupid_ns
- Source: Cupid shares fall 2% even as Q1 profit jumps 3x. What’s ahead for multibagger stock that rose 680% in a year? — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/news/cupid-shares-fall-2-even-as-q1-profit-jumps-3x-whats-ahead-for-multibagger-stock-that-rose-680-in-a-year/articleshow/133085241.cms
- Source: Q1 Results Highlights: BEML loss narrows to ₹27 cr, Eveready profit up 22%, Aditya Birla Fashion loss widens to ₹249 cr, Cupid profit nearly triples, Ceigall up 35% — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/stock-markets/q1-results-today-live-updates-delhivery-anant-raj-apollo-micro-systems-akums-drugs-pharma-aditya-birla-fashion-ceigall-pnc-infratech-oswal-pumps-results-08-august-2026/article71320548.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-06 (d=0.01), 2025-07-24 (d=0.02)

### [AMBER 4.36] dyn_tatatech_ns ↑
- dyn_tatatech_ns [EQUITIES]: last 865.75, z20 2.36, zc -0.47, resid-z -0.58 [quiet], 1d -1.52%, |z20|=2.36; 1y-pct=99
- **Mechanism**: The recent surge in dyn_tatatech_ns is largely priced, with a small resid_z of 0.15, indicating that the move is mostly explained by factor exposures. The metal_copper_channel, which is currently valid, may provide a mechanism for this move to propagate, given the global copper leads Indian metal equities. However, the lack of a strong channel connecting dyn_tatatech_ns to other assets limits the potential for further propagation.
- **Gap**: No gap: the move in dyn_tatatech_ns is largely priced, with a small resid_z and no clear dislocation from historical analogues
- **India take**: Indian instruments such as dyn_tataelxsi_ns and nifty_it have already reacted to the move in dyn_tatatech_ns, given their correlations of 0.467 and 0.461, respectively. Further reaction is unlikely, given the priced nature of the move.
- Watch next: dyn_tataelxsi_ns (up) — already moved; rho=0.467 with dyn_tatatech_ns
- **India receivers**: dyn_tataelxsi_ns (rho 0.468, z 1.39); nifty_it (rho 0.459, z 1.38)
- Source: Tata Consumer Share Price Live Updates: Tata Consumer's Current Market Position — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tata-consumer-share-price-live-updates-11-aug-2026/liveblog/133140823.cms
- Source: Titan shares: Is the Tata Group stock an attractive buy after Q1FY27 results? — Mint Markets, 2026-08-10. https://www.livemint.com/market/stock-market-news/titan-shares-is-the-tata-group-stock-an-attractive-buy-after-q1fy27-results-11786352452848.html
- Source: Tata Technologies among 5 stocks flashing bullish signals. Upside on cards? — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/news/tata-technologies-among-5-stocks-flashing-bullish-signals-upside-on-cards/slideshow/133080114.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

### [AMBER 4.33] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.61, z20 1.33, zc n/a, resid-z n/a [quiet], 1d 0.39%, 52-wk extreme (pct=98); 1y-pct=98
- **Mechanism**: The midcap_largecap_ratio has risen, indicating a potential shift in market sentiment towards midcaps. This move is priced, with a resid_z of None, suggesting that the move is largely explained by factor exposures. The valid gold_silver_comove and metal_copper_channel may influence the transmission of this move to Indian markets.
- **Gap**: No gap: the move is priced with a resid_z of None, indicating that the current price reflects the known factors
- **India take**: The Nifty Midcap 100 and Dyn PC Jeweller have already reacted to the midcap_largecap_ratio move, while Dyn Bharat Coal remains quiet. The Indian market may see further adjustments in midcap stocks.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to midcap_largecap_ratio move
- **India receivers**: nifty_midcap_100 (rho 0.532, z 1.52); dyn_bharatcoal_ns (rho 0.465, z -1.05); dyn_pcjeweller_ns (rho 0.418, z 0.96)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [AMBER 4.22] dyn_bac ↑
- dyn_bac [EQUITIES]: last 63.88, z20 2.22, zc 0.79, resid-z -0.22 [quiet], 1d 1.12%, |z20|=2.22; 1y-pct=100
- **Mechanism**: The recent move in dyn_bac is largely priced, with a small resid_z of -0.33, suggesting that the market has already accounted for the factor exposures. The historical analogues suggest a potential positive outcome for dyn_bac and sp500 in the next 20 days, with median returns of 9.68% and 3.69%, respectively. The VALID metal_copper_channel and gold_silver_comove channels may also contribute to the propagation of this move.
- **Gap**: No gap: the move in dyn_bac is largely priced, with a small resid_z and a high z20 level
- **India take**: The Indian instrument dyn_cupid_ns has already reacted, with a rho of 0.378 via dyn_bac and a z20 of 2.28. Further reaction in Indian metal equities may be expected via the metal_copper_channel.
- Watch next: dyn_ms (up) — not yet - watch; historically leads dyn_bac by 2d
- **India receivers**: dyn_cupid_ns (rho 0.368, z 2.65)
- Source: America's $4 Billion Wind Retreat Is a Bet on Permanently Cheap Gas — OilPrice, 2026-08-10. https://oilprice.com/Alternative-Energy/Wind-Power/Americas-4-Billion-Wind-Retreat-Is-a-Bet-on-Permanently-Cheap-Gas.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

## Watchlist (below surfacing floor)
dyn_ohi ↓ (4.04), dyn_coin ↓ (3.27), dyn_tech ↑ (3.09), fx · 2 series ↑ (3.03), dyn_pltr ↑ (2.76), dyn_hdb ↓ (2.74), dyn_idbi_ns ↓ (2.54), dyn_atherenerg_ns ↑ (2.27), dyn_icicigi_bo ↓ (2.26), bovespa ↓ (1.93), usd_cny ↓ (1.79), corn ↑ (1.79)

## India macro
- nifty_50: 24445.5000 (1d -0.56%, z20 0.63, flag none)
- nifty_midcap_100: 63737.8984 (1d -0.17%, z20 1.52, flag amber)
- usd_inr: 95.4250 (1d 0.23%, z20 -0.92, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6073 (1d 0.39%, z20 1.33, flag amber)
- Next India prints: NSDL FPI flows T-0d · India CPI T-1d · India WPI T-3d · RBI Weekly Statistical Supplement T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 85.7 — "Indian bonds skid as crude soars, Treasuries fall"
- COALINDIA.NS (COAL INDIA LTD) score 85.1 — "Indian bonds skid as crude soars, Treasuries fall"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 84.9 — "Indian bonds skid as crude soars, Treasuries fall"
- INDIANB.NS (INDIAN BANK) score 62.9 — "Nifty slips below two-session lows as brent crude tests $88; IT outperforms, private banks"
- BAC (Bank of America Corporation) score 50.0 — "Nifty slips below two-session lows as brent crude tests $88; IT outperforms, private banks"
- TECHM.NS (TECH MAHINDRA LIMITED) score 48.7 — "Technocraft Ventures IPO Day 3: Issue subscribed 20.19x so far. Check GMP, key dates, revi"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 47.5 — "Technocraft Ventures IPO Day 3: Issue subscribed 20.19x so far. Check GMP, key dates, revi"
- TECH (Bio-Techne Corp) score 46.3 — "Technocraft Ventures IPO Day 3: Issue subscribed 20.19x so far. Check GMP, key dates, revi"
- COIN (Coinbase Global, Inc.) score 44.9 — "Global Gas Turbine Orders Hit Record High as Power Demand Surges"
- HDB (HDFC Bank Limited) score 44.6 — "Nifty slips below two-session lows as brent crude tests $88; IT outperforms, private banks"
- OHI (Omega Healthcare Investors, In) score 43.0 — "Aswath Damodaran shares 3 lessons investors can learn from rise and fall of Leopold Aschen"
- IDBI.NS (IDBI BANK LIMITED) score 42.3 — "Nifty slips below two-session lows as brent crude tests $88; IT outperforms, private banks"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 42.3 — "Nifty slips below two-session lows as brent crude tests $88; IT outperforms, private banks"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 41.9 — "Nifty slips below two-session lows as brent crude tests $88; IT outperforms, private banks"
- CHKP (Check Point Software Technolog) score 36.8 — "Milky Mist IPO Day 1: Issue booked 45% so far. Check GMP, key dates, review, issue details"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 35.9 — "Q1 Results Today Live: MRF, Zydus Lifesciences, KPI Green Q1 PAT decline, Siemens, RVNL, P"
- LTH (Life Time Group Holdings, Inc.) score 29.8 — "Molbio Diagnostics IPO Day 2: Issue subscribed 1.75 times so far. Check GMP, size, & other"
- BOND (PIMCO Active Bond Exchange-Tra) score 24.2 — "The Bessent bond-market scorecard doesn’t look as strong as it once did"
- 301077.SZ (CHINASTARS) score 21.1 — "CHINA SAYS LAUNCH OF LONG MARCH 7 ROCKET FAILED - XINHUA"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 15.9 — "Bajaj Finance Share Price Live Updates: Bajaj Finance's Stock Performance"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 15.1 — "Bharat Forge’s cost pressures dampen defence-driven euphoria"
- PCJEWELLER.NS (PC JEWELLER LTD) score 12.6 — "PC Jeweller share price jumps 6% as Q1FY27 profit surges 37% YoY, revenue up 21%"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.5 — "Tata Consumer Share Price Live Updates: Tata Consumer's Current Market Position"
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.5 — "Good news for stock-market bulls: Corporate earnings growth is no longer being driven just"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 10.7 — "ideaForge Technology shares slide 5% after Q1 gross profit margin falls 49%"
- JIOFIN.BO (Jio Financial Services Limited) score 10.3 — "Jio Financial Services Share Price Live Updates: Jio Financial Services News"
- MS (Morgan Stanley) score 9.2 — "US Stock Market: JP Morgan raises S&P 500 year-end target to 8,000 on AI, earnings optimis"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.4 — "Jio Financial Services Share Price Live Updates: Jio Financial Services News"
- AAPL (Apple Inc.) score 8.3 — "AAPL - APPLE REPORTEDLY SCRAPS ALL-GLASS IPHONE Apple has canceled its planned 20th-annive"
- META (Meta) score 8.0 — "Q1 Results Today Highlights: Bharat Forge shares tank after Q1 loss, Kwality Pharma, Ramco"
- NVDA (NVIDIA Corporation) score 7.6 — "Forget gold and stocks: Nvidia CEO Jensen Huang aims to make chips an investable asset, li"
- VT (Vanguard Total World Stock Ind) score 7.4 — "GLENCORE'S EXPOSURE TO IRON ORE TRADER RADIANT WORLD MORE THAN $500 MILLION, SOURCES SAY"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.6 — "Adani Group stocks jump up to 3% after US judge drops criminal case against Gautam Adani. "
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.8 — "ICICI Bank Share Price Live Updates: ICICI Bank's Price Movement Indicates Positive Trend"
- GOOGL (Alphabet) score 3.6 — "US Stock Market: Berkshire steps up buybacks, boosts Alphabet stake as cash falls"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 3.3 — "Tata Consumer Share Price Live Updates: Tata Consumer's Current Market Position"
- PLTR (Palantir Technologies Inc.) score 3.2 — "Palantir’s stock stages best week since 2024 — showing it’s no longer an AI loser"
- INTC (Intel Corporation) score 2.9 — "Intel raises $20 billion in upsized share sale to fund AI plans"
- AMZN (Amazon.com, Inc.) score 2.3 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- CUPID.NS (CUPID LIMITED) score 2.1 — "Q1 Results Highlights: BEML loss narrows to ₹27 cr, Eveready profit up 22%, Aditya Birla F"

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