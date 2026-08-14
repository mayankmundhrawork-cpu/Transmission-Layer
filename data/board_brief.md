# Transmission Layer — board brief · 2026-08-14 17:09Z

data as of **2026-08-14** · 98 series · 9 red / 34 amber · 8 events surfaced (19 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.208, 2d in regime; vol-pct 0.239, breadth-off 0.176, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.41, last shift 2026-06-08. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.85, last shift 2026-05-15. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.28, corr60 0.34, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.2, corr60 -0.12, last shift 2026-06-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.72, corr60 -0.81, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.08, corr60 -0.11, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.4, corr60 -0.21, last shift 2026-05-08. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.06, corr60 0.17, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.0007248582980661222)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.492** (n=1117) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=2521) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.84] cross-asset · 13 series ↑
- comex_gold [COMMODITIES]: last 4442.70, z20 2.06, zc 1.28, resid-z 0.62 [quiet], 1d 1.81%, |z20|=2.06; co-occur[gold_silver] same-direction (channel VALID)
- russell_2000 [INDICES]: last 3061.81, z20 1.84, zc 0.25, resid-z 0.95 [quiet], 1d 0.29%, |z20|=1.84; 1y-pct=100
- comex_silver [COMMODITIES]: last 65.12, z20 1.65, zc 0.16, resid-z -1.35 [quiet], 1d 0.38%, |z20|=1.65; co-occur[gold_silver] same-direction (channel VALID)
- dyn_nvda [EQUITIES]: last 225.29, z20 1.57, zc -0.00, resid-z 1.25 [quiet], 1d -0.00%, 1y-pct=98
- dyn_vt [EQUITIES]: last 162.07, z20 1.50, zc -0.25, resid-z 0.94 [quiet], 1d -0.20%, 1y-pct=99
- vix [INDICES]: last 14.44, z20 -1.43, zc -0.17, resid-z n/a [quiet], 1d -1.30%, 1y-pct=3
- sp500 [INDICES]: last 7780.45, z20 1.38, zc -0.30, resid-z -0.45 [quiet], 1d -0.24%, 1y-pct=99
- dax [INDICES]: last 26431.94, z20 1.35, zc 0.70, resid-z 0.59 [quiet], 1d 0.50%, 1y-pct=100
- stoxx_50 [INDICES]: last 6540.53, z20 1.29, zc -0.10, resid-z -0.12 [quiet], 1d -0.08%, 1y-pct=99
- comex_copper [COMMODITIES]: last 6.61, z20 0.94, zc 0.11, resid-z 0.10 [quiet], 1d 0.24%, 1y-pct=97
- dow_jones [INDICES]: last 53699.86, z20 0.85, zc -0.36, resid-z -0.31 [quiet], 1d -0.26%, 1y-pct=96
- gold_silver_ratio [DERIVED]: last 68.22, z20 -0.76, zc n/a, resid-z n/a [quiet], 1d 1.43%, GSR<75 (extreme low)
- cac_40 [INDICES]: last 8640.11, z20 0.76, zc -0.17, resid-z -0.29 [quiet], 1d -0.12%, 1y-pct=96
- **Mechanism**: The recent surge in gold prices, driven by a weaker dollar and easing Fed rate hike bets, has led to a co-movement in other monetary metals like silver. This has resulted in a quiet move in various indices and commodities, with a notable increase in the gold-silver ratio. The VALID gold_silver_comove channel suggests that the monetary metals are rotating, with gold outperforming silver.
- **Gap**: No gap: the big raw move in gold is PRICED due to weaker dollar and easing Fed rate hike bets, with a small resid_z of 0.62 indicating that the move is largely explained by factor exposures
- **India take**: The Indian instrument nifty_metal, which has a rho of 0.513 with comex_silver, is expected to react to the move in silver. However, it is currently quiet with a z20 of 0.45. The nifty_50, which has a rho of 0.489 with cac_40, is also quiet with a z20 of 0.16.
- Watch next: comex_gold (up) — already moved; priced move due to weaker dollar and easing Fed rate hike bets
- Watch next: comex_silver (up) — already moved; co-movement with gold due to VALID gold_silver_comove channel
- Watch next: russell_2000 (down) — not yet - watch; historical analogue suggests median -2.97% return over 20 days
- **India receivers**: nifty_metal (rho 0.513, z 0.45); nifty_midcap_100 (rho 0.498, z 1.06); nifty_fmcg (rho -0.495, z -1.62); nifty_50 (rho 0.489, z 0.16)
- Source: Gold jumps 9% in August as weaker dollar, easing Fed bets boost demand — Mint Markets, 2026-08-14. https://www.livemint.com/market/commodities/gold-jumps-9-in-august-as-weaker-dollar-easing-fed-bets-boost-demand-11786716604532.html
- Source: ‘Gold can become a key pillar of India’s growth story’ — BusinessLine Mkts, 2026-08-14. https://www.thehindubusinessline.com/markets/gold/gold-can-become-a-key-pillar-of-indias-growth-story/article71345065.ece
- Source: Reddit shares jump 15% as social media platform set to join S&P 500 — Mint Markets, 2026-08-14. https://www.livemint.com/market/stock-market-news/reddit-shares-jump-15-as-social-media-platform-set-to-join-s-p-500-11786715061238.html
- Historical analogues: 2024-11-26 (d=0.92), 2025-10-31 (d=1.0), 2025-10-24 (d=1.11)

### [RED 6.61] commodities · 2 series ↑
- corn [COMMODITIES]: last 481.75, z20 3.77, zc 5.89, resid-z 4.36 [unexplained], 1d 7.53%, |z20|=3.77; 1y-pct=100
- wheat [COMMODITIES]: last 691.25, z20 1.55, zc 3.33, resid-z 2.33 [unexplained], 1d 5.90%, |z20|=1.55; 1y-pct=99
- **Mechanism**: The recent surge in corn and wheat prices is driven by supply concerns, particularly the USDA's cut in yield forecasts due to heat waves, which has created a ripple effect in the commodities market. This move is unexplained by factor exposures, as indicated by the high resid_z values for corn and wheat. The VALID metal_copper_channel and gold_silver_comove channels may facilitate the transmission of this move to other markets.
- **Gap**: No gap: the big raw move in corn and wheat is largely priced, given the significant supply disruptions and yield cuts
- **India take**: The Indian instrument dyn_lenskart_ns has already reacted, given its correlation with wheat, but other Indian metal equities may also be affected through the metal_copper_channel
- Watch next: soybeans (up) — not yet - watch; high correlation with corn
- **India receivers**: dyn_lenskart_ns (rho 0.422, z 3.07)
- Source: Corn Jumps as USDA Cuts Yield More Than Expected Amid Heat Waves — Mint Markets, 2026-08-12. https://www.livemint.com/market/corn-jumps-as-usda-cuts-yield-more-than-expected-amid-heat-waves-11786572052753.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [RED 5.07] dyn_lenskart_ns ↑
- dyn_lenskart_ns [EQUITIES]: last 612.00, z20 3.07, zc 1.87, resid-z 1.51 [unexplained], 1d 2.53%, |z20|=3.07; 1y-pct=99
- **Mechanism**: The recent surge in Lenskart Solutions' stock price can be attributed to the company's strong Q1 results, which showed a near four-fold jump in profit, and the buzz around its potential MSCI inclusion. This positive news has led to increased investor interest, driving up the stock price. The VALID metal_copper_channel and vix_equity_inverse channels indicate a risk-on environment, which supports the stock's upward movement.
- **Gap**: No gap: the stock's price move is largely priced in, given the significant increase in profit and positive market sentiment
- **India take**: The Indian instrument that expresses this move is Lenskart Solutions, which has already reacted positively to the news, and other retail-focused stocks may follow suit. The Nifty Retail index may also be affected, potentially leading to a broader market impact.
- Watch next: Lenskart Solutions (up) — already moved; strong Q1 results and MSCI inclusion buzz
- Source: Lenskart Solutions among 7 stocks hitting 52-week highs; surge up to 20% in a month — ET Markets, 2026-08-13. https://economictimes.indiatimes.com/markets/stocks/news/lenskart-solutions-among-7-stocks-hitting-52-week-highs-surge-up-to-20-in-a-month/slideshow/133210592.cms
- Source: Lenskart shares soar after strong Q1 results and MSCI inclusion buzz — BusinessLine Mkts, 2026-08-13. https://www.thehindubusinessline.com/markets/lenskart-shares-zoom-nearly-7-to-fresh-52-week-high-after-strong-q1-results-and-msci-inclusion-buzz/article71339607.ece
- Source: Lenskart shares hit record high after Q1 profit jumps nearly four-fold; Motilal Oswal lifts target price — Mint Markets, 2026-08-13. https://www.livemint.com/market/stock-market-news/lenskart-shares-hit-record-high-after-q1-profit-jumps-nearly-four-fold-motilal-oswal-lifts-target-price-11786610679031.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

### [AMBER 4.9] cross-asset · 4 series ↑
- ust_30y [RATES]: last 5.24, z20 1.24, zc 0.00, resid-z -0.12 [quiet], 1d 0.00%, 1y-pct=98
- ust_10y [RATES]: last 4.68, z20 0.50, zc -0.43, resid-z -0.76 [quiet], 1d -0.43%, 1y-pct=96
- tips_10y_real [RATES]: last 2.42, z20 0.47, zc -0.26, resid-z -0.80 [quiet], 1d -0.41%, 1y-pct=96
- dyn_bond [EQUITIES]: last 90.64, z20 -0.36, zc -0.96, resid-z -0.56 [quiet], 1d -0.29%, 1y-pct=4
- **Mechanism**: The recent surge in bond yields, driven by AI hyperscalers' borrowing and governments' bond sales, has led to a rise in inflation-adjusted borrowing costs. This move is priced, with the resid_z values for ust_30y, ust_10y, tips_10y_real, and dyn_bond indicating that the big raw move is largely explained by factor exposures. The valid gold_silver_comove and metal_copper_channel suggest that monetary metals and global copper are co-moving, which may influence Indian metal equities.
- **Gap**: No gap: the move in bond yields is largely priced, with resid_z values indicating that the big raw move is explained by factor exposures
- **India take**: The Indian instrument that expresses this move is the 10-year Government of India bond yield, which may react to the global bond yield surge. However, the inr_oil_channel is weak, and the dxy_inr_channel is also weak, suggesting that the transmission to Indian markets may be limited.
- Watch next: dyn_lth (up) — not yet - watch; historically leads dyn_bond by 2d
- Source: Sebi broadens scope of online bond platforms, permits IFSCA-regulated products and tax-saving bonds — ET Markets, 2026-08-14. https://economictimes.indiatimes.com/markets/bonds/sebi-broadens-scope-of-online-bond-platforms-permits-ifsca-regulated-products-and-tax-saving-bonds/articleshow/133245588.cms
- Source: Bond yields are at multiyear highs, yet stocks have hit fresh records. Here’s how long the defiance can last. — MarketWatch Top, 2026-08-14. https://www.marketwatch.com/story/rates-are-at-multiyear-highs-yet-stocks-hit-fresh-records-heres-how-long-the-defiance-may-last-b29a5d14?mod=mw_rss_topstories
- Source: AI-driven surge in bond yields could be next risk for markets and growth — BusinessLine Mkts, 2026-08-14. https://www.thehindubusinessline.com/markets/ai-driven-surge-in-bond-yields-could-be-next-risk-for-markets-and-growth/article71344109.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

### [RED 4.88] dyn_301077_sz ↑
- dyn_301077_sz [EQUITIES]: last 24.01, z20 2.88, zc -0.29, resid-z 1.57 [unexplained], 1d -2.44%, |z20|=2.88
- **Mechanism**: The dyn_301077_sz move is unexplained by factor exposures, with a resid_z of 1.57, suggesting a potential anomaly. However, the big raw move with small resid_z indicates that the move is largely priced in. The VALID metal_copper_channel and gold_silver_comove channels may be influencing the move, but the WEAK/INVERTED channels, such as safe_haven_gold and inr_oil_channel, are not available as mechanisms. The RISK_ON regime and vix_equity_inverse channel also support the move.
- **Gap**: No gap: the move is largely priced in with a small resid_z
- **India take**: The Indian instrument that expresses this move is likely to be metal equities, such as Hindalco or Tata Steel, which may react positively due to the VALID metal_copper_channel. However, the reaction is already reflected in the price.
- Watch next: dyn_301077_sz (up) — already moved; unexplained move with high z20 level
- Source: Global Market: China stocks rise on AI optimism; Hong Kong shares mostly flat — ET Markets, 2026-08-13. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-rise-on-ai-optimism-hong-kong-shares-mostly-flat/articleshow/133199079.cms
- Historical analogues: 2026-06-18 (d=0.0), 2026-03-30 (d=0.02), 2026-06-03 (d=0.03)

### [RED 4.66] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.62, z20 1.66, zc n/a, resid-z n/a [quiet], 1d -0.41%, 52-wk extreme (pct=98); |z20|=1.66; 1y-pct=98
- **Mechanism**: The midcap_largecap_ratio has reached a 52-wk extreme, with a z20 level of 1.66, indicating a potential mean reversion. However, the resid_z is None, suggesting that the move is largely priced in by factor exposures. The valid channels, such as gold_silver_comove and metal_copper_channel, do not directly relate to the midcap_largecap_ratio, but the vix_equity_inverse channel may influence the broader equity market, including midcaps.
- **Gap**: No gap: the move is largely priced in by factor exposures, as indicated by the None resid_z value
- **India take**: The Nifty Midcap 100 index has already reacted to the midcap_largecap_ratio move, while other transmission candidates like Dyn Bharat Coal and Dyn Fincables have not yet reacted significantly. The Indian metal equities may be influenced by the global copper prices through the metal_copper_channel.
- Watch next: nifty_midcap_100 (down) — already moved; high correlation with midcap_largecap_ratio
- **India receivers**: nifty_midcap_100 (rho 0.535, z 1.06); dyn_bharatcoal_ns (rho 0.404, z -0.93); dyn_fincables_ns (rho 0.397, z 2.31); dyn_pcjeweller_ns (rho 0.364, z 0.27)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [AMBER 3.76] dyn_bac ↑
- dyn_bac [EQUITIES]: last 64.46, z20 1.76, zc 0.40, resid-z 0.55 [quiet], 1d 0.59%, 1y-pct=99
- **Mechanism**: The recent move in dyn_bac is driven by its correlation with global markets, particularly the dow_jones and cac_40, which have historically led dyn_bac by 1-2 days. The current quiet move in dyn_bac, with a resid_z of 0.55, suggests that the move is not entirely explained by factor exposures, but the small resid_z relative to the move size indicates that the move is largely priced in.
- **Gap**: No gap: the move in dyn_bac is largely priced in, given its small resid_z relative to the move size.
- **India take**: The Indian instrument dyn_cupid_ns, which is correlated with dyn_bac, has already reacted with a z20 of 2.01. The recent news of Bank of America acquiring a stake in Jio Credit may also have a positive impact on the Indian market.
- Watch next: dyn_ms (up) — not yet - watch; historically leads dyn_bac by 2d
- **India receivers**: dyn_cupid_ns (rho 0.359, z 2.01)
- Source: America’s Authoritarian Adversaries Are Forging a New Power Bloc — OilPrice, 2026-08-13. https://oilprice.com/Geopolitics/North-America/Americas-Authoritarian-Adversaries-Are-Forging-a-New-Power-Bloc.html
- Source: Jio Financial shares jump 3% as Bank of America set to acquire 50% stake in Jio Credit for Rs 18,268 crore — ET Markets, 2026-08-13. https://economictimes.indiatimes.com/markets/stocks/news/jio-financial-shares-in-focus-as-bank-of-america-set-to-acquire-50-stake-in-jio-credit-for-rs-18268-crore/articleshow/133197203.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

### [RED 3.75] usd_brl ↑
- usd_brl [FX]: last 5.24, z20 3.75, zc 1.00, resid-z 0.89 [quiet], 1d 0.80%, |z20|=3.75
- **Mechanism**: usd_brl ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.548 via usd_brl, z -1.66, reacted); nifty_50 (rho -0.353 via usd_brl, z 0.16, quiet); dyn_hdbfs_bo (rho -0.353 via usd_brl, z -0.21, quiet)
- **India receivers**: dyn_muthootfin_ns (rho -0.548, z -1.66); nifty_50 (rho -0.353, z 0.16); dyn_hdbfs_bo (rho -0.353, z -0.21)
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-30 (d=0.0), 2026-05-05 (d=0.01)

## Watchlist (below surfacing floor)
nikkei_225 ↑ (3.73), dyn_tatatech_ns ↑ (3.56), dyn_atherenerg_ns ↑ (3.33), fx · 2 series ↑ (2.92), dyn_lth ↑ (2.79), dyn_indusindbk_bo ↑ (2.7), usd_cny ↓ (2.69), dyn_tech ↑ (2.66), indices · 2 series ↑ (2.6), bovespa ↓ (2.6), dyn_hdb ↓ (2.58), eur_inr ↑ (2.41)

## India macro
- nifty_50: 24366.0000 (1d -0.12%, z20 0.16, flag none)
- nifty_midcap_100: 63782.6484 (1d -0.53%, z20 1.06, flag amber)
- usd_inr: 95.4150 (1d 0.07%, z20 -0.68, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6177 (1d -0.41%, z20 1.66, flag red)
- Next India prints: India WPI T-0d · NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 108.9 — "WeWork Global sells 2.5% stake in WeWork India Management for Rs 244 crore"
- INOXINDIA.NS (INOX INDIA LIMITED) score 107.9 — "WeWork Global sells 2.5% stake in WeWork India Management for Rs 244 crore"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 107.5 — "WeWork Global sells 2.5% stake in WeWork India Management for Rs 244 crore"
- INDIANB.NS (INDIAN BANK) score 70.6 — "Sebi proposes easier digital KYC for Indians living abroad"
- OHI (Omega Healthcare Investors, In) score 56.0 — "Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks edge lower as investors weigh "
- COIN (Coinbase Global, Inc.) score 54.8 — "WeWork Global sells 2.5% stake in WeWork India Management for Rs 244 crore"
- TECHM.NS (TECH MAHINDRA LIMITED) score 54.7 — "Technocraft Ventures ends debut day with 47% gains; LEAP India settles 9% below listing pr"
- BAC (Bank of America Corporation) score 53.8 — "Global Market | Bank of Japan could raise rates in September, eye faster hikes: Reports"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 53.4 — "Technocraft Ventures ends debut day with 47% gains; LEAP India settles 9% below listing pr"
- TECH (Bio-Techne Corp) score 52.9 — "Technocraft Ventures ends debut day with 47% gains; LEAP India settles 9% below listing pr"
- HDB (HDFC Bank Limited) score 46.8 — "Global Market | Bank of Japan could raise rates in September, eye faster hikes: Reports"
- CHKP (Check Point Software Technolog) score 45.0 — "Behari Lal Engineering IPO Day 3: Issue booked 93.21x so far. Check GMP, subscriptions, ke"
- IDBI.NS (IDBI BANK LIMITED) score 42.5 — "Global Market | Bank of Japan could raise rates in September, eye faster hikes: Reports"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 42.5 — "Global Market | Bank of Japan could raise rates in September, eye faster hikes: Reports"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 42.3 — "Global Market | Bank of Japan could raise rates in September, eye faster hikes: Reports"
- LTH (Life Time Group Holdings, Inc.) score 38.7 — "Still trying to time the stock market? This chart shows why it’s tougher than you think."
- TATAELXSI.NS (TATA ELXSI LIMITED) score 32.2 — "Under Chandrasekaran, as Tata stocks changed, so did their investors"
- BOND (PIMCO Active Bond Exchange-Tra) score 30.1 — "Sebi broadens scope of online bond platforms, permits IFSCA-regulated products and tax-sav"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 29.1 — "Adani Energy Solution shares end 2% higher after acquiring Vizag Power Transmission"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 28.4 — "Under Chandrasekaran, as Tata stocks changed, so did their investors"
- 301077.SZ (CHINASTARS) score 25.9 — "Unitree IPO: China’s humanoid robot starset for potentially explosive Shanghai debut"
- JIOFIN.BO (Jio Financial Services Limited) score 21.7 — "I have $10 million and pay two advisers for financial help, but still have questions"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 18.8 — "India's Coal Demand Set to Hit 1.6 Billion Tons by 2030"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 15.9 — "I have $10 million and pay two advisers for financial help, but still have questions"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 15.9 — "Muthoot Fincorp files draft papers for ₹3,000 crore IPO"
- JUSTDIAL.BO (JUST DIAL LTD.) score 13.8 — "DEEPSEEK ANNOUNCES ADJUSTMENT TO API RPICING - STATEMENT"
- MS (Morgan Stanley) score 12.5 — "Tata Motors PV shares fall 5% after weak Q1 results. What are Morgan Stanley, Nomura, othe"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 10.7 — "Bharat Dynamics Q1 results: Profit sees sixfold increase, revenue surges 131% YoY"
- META (Meta) score 9.2 — "Pulse of the Street: Tata jitters, metal rout weigh on Indian equities"
- PCJEWELLER.NS (PC JEWELLER LTD) score 8.6 — "Brokerages initiate coverage on Vedanta Aluminium, Kalyan Jewellers, 3 other stocks with u"
- NVDA (NVIDIA Corporation) score 8.0 — "Alphabet’s stock slips as Nvidia’s $500 billion financing deal threatens custom chips"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.6 — "Adani Energy Solution shares end 2% higher after acquiring Vizag Power Transmission"
- RDDT (Reddit, Inc.) score 5.8 — "Reddit shares surge 14% on S&P 500 inclusion, replacing AvalonBay"
- AAPL (Apple Inc.) score 5.6 — "Nvidia, Apple, Google fuel record $185 billion gain for Norway’s wealth fund, but CEO say,"
- VT (Vanguard Total World Stock Ind) score 5.4 — "China’s next economic ambition: workshop for the Muslim world"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.4 — "Lenskart shares soar after strong Q1 results and MSCI inclusion buzz"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 2.3 — "ICICI Bank Share Price Live Updates: ICICI Bank Stock Details"
- CRWV (CoreWeave, Inc.) score 1.8 — "US stocks: S&P 500 ends higher as CoreWeave results fuel AI optimism"
- FINCABLES.NS (FINOLEX CABLES LTD) score 1.7 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 1.6 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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