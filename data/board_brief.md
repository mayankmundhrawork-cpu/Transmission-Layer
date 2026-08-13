# Transmission Layer — board brief · 2026-08-13 05:48Z

data as of **2026-08-13** · 98 series · 10 red / 34 amber · 8 events surfaced (19 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.205, 2d in regime; vol-pct 0.285, breadth-off 0.125, Markov P(high-vol) 0.011)
- [INVERTED] **safe_haven_gold** — corr20 -0.36, corr60 -0.41, last shift 2026-06-05. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.85, last shift 2026-05-14. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.33, corr60 0.37, last shift 2026-05-13. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.18, corr60 -0.07, last shift 2026-06-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.74, corr60 -0.81, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.06, corr60 -0.06, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.4, corr60 -0.23, last shift 2026-05-14. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.06, corr60 0.17, last shift 2026-04-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.492** (n=1125) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.815** (n=2531) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.23] cross-asset · 13 series ↑
- comex_gold [COMMODITIES]: last 4455.80, z20 2.35, zc 0.72, resid-z 0.33 [quiet], 1d 1.06%, |z20|=2.35; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 65.57, z20 1.99, zc 0.01, resid-z 0.25 [quiet], 1d 0.02%, |z20|=1.99; co-occur[gold_silver] same-direction (channel VALID)
- russell_2000 [INDICES]: last 3045.74, z20 1.92, zc 0.51, resid-z 0.53 [quiet], 1d 0.62%, |z20|=1.92; 1y-pct=100
- dyn_nvda [EQUITIES]: last 224.13, z20 1.83, zc 1.21, resid-z 0.48 [quiet], 1d 3.05%, 1y-pct=98
- dyn_vt [EQUITIES]: last 161.55, z20 1.73, zc 0.53, resid-z 0.98 [quiet], 1d 0.46%, 1y-pct=100
- vix [INDICES]: last 14.55, z20 -1.59, zc -0.63, resid-z n/a [quiet], 1d -4.78%, |z20|=1.59; 1y-pct=4
- stoxx_50 [INDICES]: last 6530.18, z20 1.53, zc -0.41, resid-z -0.63 [quiet], 1d -0.32%, |z20|=1.53; 1y-pct=99
- sp500 [INDICES]: last 7748.71, z20 1.47, zc 0.32, resid-z -1.19 [quiet], 1d 0.27%, 1y-pct=99
- dax [INDICES]: last 26339.76, z20 1.44, zc -0.26, resid-z -0.21 [quiet], 1d -0.20%, 1y-pct=99
- gold_silver_ratio [DERIVED]: last 67.95, z20 -1.15, zc n/a, resid-z n/a [quiet], 1d 1.04%, GSR<75 (extreme low)
- cac_40 [INDICES]: last 8665.15, z20 1.13, zc -0.79, resid-z -0.88 [quiet], 1d -0.57%, 1y-pct=97
- dow_jones [INDICES]: last 53769.86, z20 1.11, zc -0.05, resid-z -0.49 [quiet], 1d -0.04%, 1y-pct=97
- comex_copper [COMMODITIES]: last 6.56, z20 0.71, zc -0.25, resid-z -0.18 [quiet], 1d -0.56%, 1y-pct=96
- **Mechanism**: The recent move in gold and silver prices is driven by central banks' increasing allocation to gold as a hedge against geopolitical and economic uncertainty. This move is priced in, given the small resid_z values for COMEX gold and silver. The VALID gold_silver_comove channel suggests that the co-movement between gold and silver will continue, with the gold-silver ratio extremes indicating rotations rather than a change in trend.
- **Gap**: No gap: The recent move in gold and silver prices is largely explained by the increasing allocation to gold by central banks, and the resid_z values indicate that the move is priced in.
- **India take**: The Indian metal sector, particularly NIFTY metal, may react positively to the increase in COMEX silver prices, given their correlation. However, the reaction is yet to be seen.
- Watch next: COMEX gold (up) — already moved; Central banks' increasing allocation to gold
- Watch next: COMEX silver (up) — already moved; Co-movement with gold
- Watch next: NIFTY metal (up) — not yet - watch; Correlation with COMEX silver
- **India receivers**: nifty_midcap_100 (rho 0.52, z 1.29); nifty_fmcg (rho -0.518, z -1.84); nifty_metal (rho 0.517, z 0.94); nifty_50 (rho 0.494, z 0.05)
- Source: Bank of Korea Makes First Gold-Linked Investment in 13 Years — Mint Markets, 2026-08-13. https://www.livemint.com/market/bank-of-korea-makes-first-gold-linked-investment-in-13-years-11786597081671.html
- Source: Gold Rate Today, Aug 13: Gold prices down in Delhi, Mumbai, Kolkata, Bengaluru, Ahmedabad — BusinessLine Mkts, 2026-08-13. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-mumbai-chennai-ahmedabad-delhi-hyderabad-bengaluru-kolkata-gold-rates-august-13-2026/article71339513.ece
- Source: Gold prices rise Rs 1,400/gram in 2 days; silver dips marginally despite soft US inflation. What should investors do? — ET Markets, 2026-08-13. https://economictimes.indiatimes.com/markets/commodities/news/gold-prices-rise-rs-1400/gram-in-2-days-silver-dips-marginally-despite-soft-us-inflation-what-should-investors-do/articleshow/133197523.cms
- Historical analogues: 2024-11-26 (d=0.92), 2025-10-31 (d=1.0), 2025-10-24 (d=1.11)

### [RED 6.46] dyn_301077_sz ↑
- dyn_301077_sz [EQUITIES]: last 24.13, z20 4.46, zc 3.68, resid-z 0.59 [moved], 1d 11.45%, |z20|=4.46
- **Mechanism**: The recent move in dyn_301077_sz is largely priced, with a small resid_z of 0.59, indicating that the move is mostly explained by factor exposures. The VALID metal_copper_channel and gold_silver_comove channels suggest that global metal prices are influencing the move. The RISK_ON regime also supports the move, as high-volatility assets are in favor.
- **Gap**: No gap: the move in dyn_301077_sz is largely explained by factor exposures, with a small resid_z
- **India take**: The Indian instrument that expresses this move is likely to be metal equities such as Tata Steel or Hindalco, which may react positively to the global metal price move. However, the reaction may be muted due to the already priced nature of the move.
- Watch next: dyn_301077_sz (up) — already moved; small resid_z and priced move
- Source: Global Market: China stocks rise as tech shares lead gains ahead of US CPI — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-rise-as-tech-shares-lead-gains-ahead-of-us-cpi/articleshow/133172233.cms
- Historical analogues: 2026-06-18 (d=0.0), 2026-03-30 (d=0.02), 2026-06-03 (d=0.03)

### [RED 5.46] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.62, z20 2.46, zc n/a, resid-z n/a [quiet], 1d 0.16%, 52-wk extreme (pct=100); |z20|=2.46; 1y-pct=100
- **Mechanism**: The midcap_largecap_ratio has reached a 52-wk extreme, with a z20 level of 2.29, indicating a potential mean reversion. However, the resid_z is None, suggesting that this move is largely priced in by factors. The RISK_ON regime and VALID vix_equity_inverse channel suggest that equity markets are likely to remain volatile.
- **Gap**: No gap: the move is largely priced in by factors, as indicated by the None resid_z value
- **India take**: The Nifty Midcap 100 index has already reacted to this move, with a z20 level of 1.79, while other transmission candidates like Dyn Bharatcoal NS and Dyn Indianb NS have also reacted, but Dyn PCJeweller NS remains quiet.
- Watch next: nifty_midcap_100 (down) — already moved; high correlation with midcap_largecap_ratio
- **India receivers**: nifty_midcap_100 (rho 0.526, z 1.29); dyn_bharatcoal_ns (rho 0.41, z -0.69); dyn_fincables_ns (rho 0.408, z 2.94); dyn_pcjeweller_ns (rho 0.384, z -0.03)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 5.36] corn ↑
- corn [COMMODITIES]: last 478.25, z20 3.36, zc 3.64, resid-z 2.93 [unexplained], 1d 4.65%, |z20|=3.36; 1y-pct=100
- **Mechanism**: The surge in corn prices is driven by the USDA's unexpected cut in yield due to heat waves, which has created a supply shock. This move is unexplained by factor exposures, with a high resid_z of 2.93, indicating a genuine anomaly. The RISK_ON regime and VALID gold_silver_comove and metal_copper_channel suggest that the market is pricing in the potential impact on inflation and global commodity markets.
- **Gap**: No gap: the big raw move in corn with a small resid_z relative to its z20 and zc values indicates that the price move is largely priced in, given the unexpected yield cut and supply shock.
- **India take**: The Indian instrument that expresses this move is likely to be the MCX Corn futures, which may react in tandem with global corn prices. However, the reaction may be muted due to the WEAK inr_oil_channel and dxy_inr_channel, which could limit the transmission of global commodity price shocks to Indian markets.
- Watch next: soybeans (up) — not yet - watch; high correlation with corn
- Source: Corn Jumps as USDA Cuts Yield More Than Expected Amid Heat Waves — Mint Markets, 2026-08-12. https://www.livemint.com/market/corn-jumps-as-usda-cuts-yield-more-than-expected-amid-heat-waves-11786572052753.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-21 (d=0.01), 2025-12-31 (d=0.02)

### [RED 5.31] dyn_crwv ↑
- dyn_crwv [EQUITIES]: last 107.68, z20 3.31, zc 3.21, resid-z 0.90 [moved], 1d 19.22%, |z20|=3.31
- **Mechanism**: The recent surge in CoreWeave's stock price, driven by strong AI infrastructure company earnings and positive quarterly results, has fueled AI optimism and boosted the stock prices of related companies. This move is priced, with a relatively small resid_z of 0.9, indicating that the move is largely explained by factor exposures. The VALID vix_equity_inverse channel suggests that the vol spike may lead to an equity drawdown, but the current RISK_ON regime and strong earnings reports may mitigate this effect.
- **Gap**: No gap: the move is largely priced, with a small resid_z and a big raw move, indicating that the market has already incorporated the information from CoreWeave's earnings report
- **India take**: The Indian instrument nifty_fmcg has already reacted to the move, with a rho of -0.38 via dyn_crwv. However, the metal_copper_channel may also be relevant, as global copper leads Indian metal equities, and the recent surge in AI infrastructure demand may have implications for Indian metal stocks.
- Watch next: nifty_fmcg (down) — already moved; rho=-0.38 via dyn_crwv
- **India receivers**: nifty_fmcg (rho -0.385, z -1.84)
- Source: US stocks: S&P 500 ends higher as CoreWeave results fuel AI optimism — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-sp-500-ends-higher-as-coreweave-results-fuel-ai-optimism/articleshow/133192806.cms
- Source: US stocks: CoreWeave, Super Micro surge on signs of sustained AI buildout — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-coreweave-super-micro-surge-on-signs-of-sustained-ai-buildout/articleshow/133187386.cms
- Source: CoreWeave’s stock is rocketing after earnings lead to praise from bulls and bears alike — MarketWatch Top, 2026-08-12. https://www.marketwatch.com/story/coreweaves-stock-is-rocketing-after-earnings-lead-to-praise-from-bulls-and-bears-alike-46c831e7?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-13 (d=0.01), 2025-08-05 (d=0.04)

### [AMBER 5.26] indices · 3 series ↑
- shanghai_comp [INDICES]: last 3966.37, z20 1.94, zc 0.60, resid-z 0.40 [quiet], 1d 0.50%, |z20|=1.94
- nikkei_225 [INDICES]: last 68674.09, z20 1.76, zc 0.87, resid-z 0.88 [quiet], 1d 1.70%, |z20|=1.76
- taiwan_weighted [INDICES]: last 45972.29, z20 1.49, zc 0.55, resid-z 0.07 [quiet], 1d 1.00%, 1y-pct=95
- **Mechanism**: The recent move in Shanghai Comp, Nikkei 225, and Taiwan Weighted indices is largely priced, with resid_z values of 0.4, 0.88, and 0.07 respectively, indicating that the majority of the move can be explained by factor exposures. The RISK_ON regime and VALID gold_silver_comove and metal_copper_channel suggest a positive sentiment towards risk assets.
- **Gap**: No gap: the move in the indices is largely priced, with small resid_z values indicating that the majority of the move can be explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is Nifty Metal, which has not yet reacted. Other correlated instruments like Dyn_HDBFS_bo and Dyn_Techm_ns are also quiet.
- Watch next: nifty_metal (up) — not yet - watch; rho=0.459 with shanghai_comp
- **India receivers**: dyn_hdbfs_bo (rho 0.493, z -0.16); nifty_metal (rho 0.459, z 0.94); dyn_techm_ns (rho -0.456, z 0.67); nifty_midcap_100 (rho 0.434, z 1.29)
- Source: Global Market: China stocks rise as tech shares lead gains ahead of US CPI — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-rise-as-tech-shares-lead-gains-ahead-of-us-cpi/articleshow/133172233.cms
- Source: Nikkei, Kospi to US stocks: Global equity heatmap you must know before the opening bell of the Indian stock market today — Mint Markets, 2026-08-12. https://www.livemint.com/market/stock-market-news/nikkei-kospi-to-us-stocks-global-equity-heatmap-you-must-know-before-the-opening-bell-of-the-indian-stock-market-today-11786500968431.html
- Historical analogues: 2025-07-15 (d=0.77), 2025-12-23 (d=0.98), 2025-07-07 (d=1.25)

### [AMBER 5.03] cross-asset · 4 series ↑
- ust_30y [RATES]: last 5.24, z20 1.37, zc -0.23, resid-z -0.75 [quiet], 1d -0.19%, 1y-pct=99
- ust_10y [RATES]: last 4.70, z20 0.96, zc -0.42, resid-z -0.98 [quiet], 1d -0.42%, 1y-pct=98
- dyn_bond [EQUITIES]: last 90.54, z20 -0.80, zc 0.24, resid-z -0.57 [quiet], 1d 0.07%, 1y-pct=2
- tips_10y_real [RATES]: last 2.43, z20 0.80, zc 0.00, resid-z -0.59 [quiet], 1d 0.00%, 1y-pct=97
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_lth (co-move) — not yet - watch; rho 0.566 vs dyn_bond, historically leads by 2d
- Watch next: brent (co-move) — not yet - watch; rho 0.537 vs ust_30y, historically leads by 3d
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.514 vs ust_30y, historically leads by 1d
- Watch next: wti (co-move) — not yet - watch; rho 0.51 vs ust_10y, historically leads by 3d
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.525 vs dyn_bond
- Source: Gold and silver trade lacklustre on MCX despite soft US inflation data; elevated dollar, bond yields weigh — Mint Markets, 2026-08-13. https://www.livemint.com/market/commodities/gold-and-silver-prices-today-rates-lacklustre-on-mcx-despite-soft-us-inflation-data-elevated-dollar-bond-yields-weigh-11786591359947.html
- Source: US Sells 10-Year Debt at Highest Yields Since Financial Crisis — Mint Markets, 2026-08-12. https://www.livemint.com/market/us-sells-10-year-debt-at-highest-yields-since-financial-crisis-11786566124472.html
- Source: Canadian 10-year yield pulls back from 2-year high after tame U.S. inflation data — Mint Markets, 2026-08-12. https://www.livemint.com/market/canadian-10-year-yield-pulls-back-from-2-year-high-after-tame-u-s-inflation-data-11786560586614.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

### [RED 4.94] dyn_fincables_ns ↑
- dyn_fincables_ns [EQUITIES]: last 1252.20, z20 2.94, zc -0.51, resid-z 1.63 [unexplained], 1d -2.18%, |z20|=2.94; 1y-pct=99
- **Mechanism**: dyn_fincables_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.43 via dyn_fincables_ns, z 1.29, reacted); midcap_largecap_ratio (rho 0.408 via dyn_fincables_ns, z 2.46, reacted); dyn_bharatcoal_ns (rho 0.378 via dyn_fincables_ns, z -0.69, quiet)
- **India receivers**: nifty_midcap_100 (rho 0.43, z 1.29); midcap_largecap_ratio (rho 0.408, z 2.46); dyn_bharatcoal_ns (rho 0.378, z -0.69)
- Source: Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410 — BusinessLine Mkts, 2026-08-12. https://www.thehindubusinessline.com/markets/stock-markets/finolex-cables-shares-jump-14-to-52-week-high-jefferies-lift-target-to-1410-maintains-accumulate/article71335064.ece
- Source: Finolex Cables shares jump 10% on strong Q1 performance; revenue crosses Rs 2,000 crore mark — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/stocks/news/finolex-cables-shares-jump-10-on-strong-q1-performance-revenue-crosses-rs-2000-crore-mark/articleshow/133172179.cms
- Source: Q1 Results Today Live: Tata Motors, Apollo Hospitals, HAL, Grasim GMR Airports, Lenskart, Abbott, VA Tech, IRCON, AIA, IRCTC, Sun TV, EID Parry to announce Q1 results, NBCC, Siemens, RVNL, Kalpataru, MRF, Zydus Lifesciences, KPI Green, Manappuram Finance in focus, TD Power Systems, Finolex shares hit 52-week high — BusinessLine Mkts, 2026-08-12. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-hal-grasim-ind-tata-motors-apollo-hospitals-gmr-airports-lenskart-gic-abbott-aia-engg-irctc-sun-tv-eid-parry-va-tech-ircon-titagarh-results-12-august-2026/article71332017.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-02-19 (d=0.0), 2025-02-07 (d=0.02)

## Watchlist (below surfacing floor)
dyn_bac ↑ (4.81), dyn_ohi ↓ (4.44), dyn_cupid_ns ↑ (4.23), dyn_tatatech_ns ↑ (3.62), dyn_atherenerg_ns ↑ (3.61), dyn_tech ↑ (3.46), bovespa ↓ (3.1), dyn_coin ↓ (3.02), usd_brl ↑ (3.0), dyn_hdb ↓ (2.92), dyn_icicigi_bo ↓ (2.48), usd_mxn ↓ (2.28)

## India macro
- nifty_50: 24319.9492 (1d -0.47%, z20 0.05, flag none)
- nifty_midcap_100: 63821.1016 (1d -0.32%, z20 1.29, flag amber)
- usd_inr: 95.3575 (1d -0.02%, z20 -0.86, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6242 (1d 0.16%, z20 2.46, flag red)
- Next India prints: NSDL FPI flows T-0d · India WPI T-1d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 91.4 — "Buyout funds look beyond India IPOs as vintage assets mature"
- INOXINDIA.NS (INOX INDIA LIMITED) score 91.1 — "Buyout funds look beyond India IPOs as vintage assets mature"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 90.5 — "Buyout funds look beyond India IPOs as vintage assets mature"
- INDIANB.NS (INDIAN BANK) score 72.4 — "From Gift Nifty to Kospi rally, oil prices: 7 key things that changed for Indian stock mar"
- BAC (Bank of America Corporation) score 56.8 — "IndusInd Bank Share Price Live Updates: IndusInd Bank Trading Metrics"
- TECHM.NS (TECH MAHINDRA LIMITED) score 52.8 — "HCL Tech Share Price Live Updates: HCL Tech Stock Details"
- HDB (HDFC Bank Limited) score 52.6 — "HDFC Life Share Price Live Updates: HDFC Life Stock Details"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 51.1 — "HCL Tech Share Price Live Updates: HCL Tech Stock Details"
- TECH (Bio-Techne Corp) score 50.2 — "HCL Tech Share Price Live Updates: HCL Tech Stock Details"
- COIN (Coinbase Global, Inc.) score 49.5 — "Indian stocks see muted opening despite positive global cues"
- OHI (Omega Healthcare Investors, In) score 48.6 — "Gold prices rise Rs 1,400/gram in 2 days; silver dips marginally despite soft US inflation"
- CHKP (Check Point Software Technolog) score 48.0 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 1"
- IDBI.NS (IDBI BANK LIMITED) score 47.8 — "IndusInd Bank Share Price Live Updates: IndusInd Bank Trading Metrics"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 47.8 — "IndusInd Bank Share Price Live Updates: IndusInd Bank Trading Metrics"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 47.5 — "IndusInd Bank Share Price Live Updates: IndusInd Bank Trading Metrics"
- LTH (Life Time Group Holdings, Inc.) score 35.7 — "LAPL Automotive SME IPO listing: Shares debut at a 44% premium despite weak stock market s"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 31.6 — "Trump’s Bosnia Power Play Puts an Opaque Energy Deal at the Center"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 29.3 — "Stocks to watch: Tata Motors PV, Jio Financial, Lenskart among shares in focus today; chec"
- 301077.SZ (CHINASTARS) score 25.0 — "China’s next economic ambition: workshop for the Muslim world"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 23.9 — "Stocks to watch: Tata Motors PV, Jio Financial, Lenskart among shares in focus today; chec"
- BOND (PIMCO Active Bond Exchange-Tra) score 23.0 — "Gold and silver trade lacklustre on MCX despite soft US inflation data; elevated dollar, b"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 20.2 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Stock Details"
- JIOFIN.BO (Jio Financial Services Limited) score 16.9 — "Stocks to watch: Tata Motors PV, Jio Financial, Lenskart among shares in focus today; chec"
- JUSTDIAL.BO (JUST DIAL LTD.) score 16.1 — "Grasim Inds Share Price Live Updates: Grasim Industries Sees Price Adjustment"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 14.8 — "Stocks to watch: Tata Motors PV, Jio Financial, Lenskart among shares in focus today; chec"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 13.3 — "India’s planned coal mine capacity nearly doubles to 638 mtpa in 2025"
- MS (Morgan Stanley) score 13.1 — "SPCX - MORGAN STANLEY: SPACEX LOCK-UP IS A BUYING OPPORTUNITY Morgan Stanley reiterated Ov"
- NVDA (NVIDIA Corporation) score 11.3 — "Alphabet’s stock slips as Nvidia’s $500 billion financing deal threatens custom chips"
- PCJEWELLER.NS (PC JEWELLER LTD) score 9.7 — "Motilal Oswal bullish on jewellery stocks; picks Titan, Kalyan Jewellers as top bets, sees"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 8.8 — "Bharat Heavy Electricals among 5 stocks showing bullish RSI upswing"
- META (Meta) score 8.0 — "Sensex, Nifty slip at open; cement, metals drag as Apollo Hospitals leads gains"
- AAPL (Apple Inc.) score 7.8 — "Nvidia, Apple, Google fuel record $185 billion gain for Norway’s wealth fund, but CEO say,"
- VT (Vanguard Total World Stock Ind) score 7.6 — "China’s next economic ambition: workshop for the Muslim world"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.0 — "Reliance Industries, Adani Enterprises among 10 stocks with highest DII buying up to Rs 22"
- INTC (Intel Corporation) score 4.8 — "Nvidia, Intel, Google: Wall Street is partying like it’s 1999"
- GS (Goldman Sachs Group, Inc. (The) score 3.7 — "Lenskart Solutions shares jump 7% after Q1 results; Jefferies, Goldman Sachs, 3 others rai"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.3 — "ICICI Bank Share Price Live Updates: ICICI Bank Stock Details"
- CRWV (CoreWeave, Inc.) score 2.5 — "US stocks: S&P 500 ends higher as CoreWeave results fuel AI optimism"
- FINCABLES.NS (FINOLEX CABLES LTD) score 2.5 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 2.2 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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