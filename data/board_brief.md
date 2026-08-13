# Transmission Layer — board brief · 2026-08-13 07:50Z

data as of **2026-08-13** · 98 series · 9 red / 34 amber · 8 events surfaced (20 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.22, 2d in regime; vol-pct 0.274, breadth-off 0.167, Markov P(high-vol) 0.011)
- [INVERTED] **safe_haven_gold** — corr20 -0.39, corr60 -0.41, last shift 2026-06-05. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.85, last shift 2026-05-14. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.36, corr60 0.37, last shift 2026-05-13. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.17, corr60 -0.07, last shift 2026-06-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.74, corr60 -0.81, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.06, corr60 -0.06, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.4, corr60 -0.23, last shift 2026-05-14. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.04, corr60 0.17, last shift 2026-04-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.492** (n=1125) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.821** (n=2503) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.93] cross-asset · 13 series ↑
- comex_gold [COMMODITIES]: last 4431.50, z20 2.17, zc 0.35, resid-z 0.33 [quiet], 1d 0.51%, |z20|=2.17; co-occur[gold_silver] same-direction (channel VALID)
- russell_2000 [INDICES]: last 3045.74, z20 1.92, zc 0.51, resid-z 0.53 [quiet], 1d 0.62%, |z20|=1.92; 1y-pct=100
- dyn_nvda [EQUITIES]: last 224.13, z20 1.83, zc 1.21, resid-z 0.48 [quiet], 1d 3.05%, 1y-pct=98
- comex_silver [COMMODITIES]: last 64.87, z20 1.76, zc -0.42, resid-z -0.93 [quiet], 1d -1.04%, |z20|=1.76; co-occur[gold_silver] same-direction (channel VALID)
- dyn_vt [EQUITIES]: last 161.55, z20 1.73, zc 0.53, resid-z 0.98 [quiet], 1d 0.46%, 1y-pct=100
- stoxx_50 [INDICES]: last 6561.04, z20 1.63, zc 0.54, resid-z -0.56 [quiet], 1d 0.41%, |z20|=1.63; 1y-pct=100
- sp500 [INDICES]: last 7748.71, z20 1.47, zc 0.32, resid-z -1.19 [quiet], 1d 0.27%, 1y-pct=99
- dax [INDICES]: last 26426.15, z20 1.45, zc 0.49, resid-z -0.24 [quiet], 1d 0.36%, 1y-pct=100
- vix [INDICES]: last 14.67, z20 -1.42, zc 0.11, resid-z n/a [quiet], 1d 0.82%, 1y-pct=5
- cac_40 [INDICES]: last 8685.70, z20 1.15, zc 0.17, resid-z -0.72 [quiet], 1d 0.12%, 1y-pct=98
- dow_jones [INDICES]: last 53769.86, z20 1.11, zc -0.05, resid-z -0.49 [quiet], 1d -0.04%, 1y-pct=97
- gold_silver_ratio [DERIVED]: last 68.31, z20 -0.85, zc n/a, resid-z n/a [quiet], 1d 1.57%, GSR<75 (extreme low)
- comex_copper [COMMODITIES]: last 6.52, z20 0.46, zc -0.49, resid-z -0.18 [quiet], 1d -1.12%, 1y-pct=95
- **Mechanism**: The recent move in global markets is driven by a combination of factors, including a rally in monetary metals such as gold and silver, and a surge in equity markets. The VALID gold_silver_comove channel suggests that the co-movement between gold and silver is intact, which could lead to further rotations in the metal space. The VALID vix_equity_inverse channel also indicates that the recent spike in volatility could lead to an equity drawdown.
- **Gap**: No gap: the recent move in global markets is largely priced in, with most assets showing quiet moves and small resid_z values, indicating that the current prices reflect the underlying factors.
- **India take**: The Indian instrument nifty_metal, which is correlated with comex_silver, has not yet reacted to the move in global markets. The nifty_50, which is correlated with cac_40, is also quiet, suggesting that the Indian market has not yet fully priced in the global developments.
- Watch next: nifty_metal (up) — not yet - watch; correlated with comex_silver
- Watch next: nifty_fmcg (down) — already moved; correlated with dyn_nvda
- **India receivers**: nifty_metal (rho 0.522, z 0.82); nifty_fmcg (rho -0.516, z -1.4); nifty_midcap_100 (rho 0.512, z 1.47); nifty_50 (rho 0.489, z 0.18)
- Source: Stocks to buy: Nagaraj Shetti recommends Bank of Maharashtra, Hindustan Copper shares to buy in the short-term — Mint Markets, 2026-08-13. https://www.livemint.com/market/stock-market-news/stocks-to-buy-nagaraj-shetti-recommends-bank-of-maharashtra-hindustan-copper-shares-to-buy-in-the-shortterm-11786605083579.html
- Source: Lenskart’s Meller sunglasses are Ray-Ban of the future, says Jefferies. Here’s why Wall Street giant is bullish — ET Markets, 2026-08-13. https://economictimes.indiatimes.com/markets/stocks/news/lenskarts-meller-sunglasses-are-ray-ban-of-the-future-says-jefferies-heres-why-wall-street-giant-is-bullish/articleshow/133203250.cms
- Source: Gold touches two-month peak, then slips as traders pause for inflation cues — BusinessLine Mkts, 2026-08-13. https://www.thehindubusinessline.com/markets/gold/gold-touches-two-month-peak-then-slips-as-traders-pause-for-inflation-cues/article71339831.ece
- Historical analogues: 2024-11-26 (d=0.92), 2025-10-31 (d=1.0), 2025-10-24 (d=1.11)

### [RED 6.94] dyn_301077_sz ↑
- dyn_301077_sz [EQUITIES]: last 24.63, z20 4.94, zc 4.42, resid-z 0.59 [moved], 1d 13.76%, |z20|=4.94
- **Mechanism**: The recent surge in dyn_301077_sz is largely priced, with a small resid_z of 0.59, indicating that the move is mostly explained by factor exposures. The VALID metal_copper_channel and VALID gold_silver_comove channels suggest that global commodity trends are influencing the move. However, the WEAK inr_oil_channel and WEAK dxy_inr_channel indicate that the Indian rupee and oil prices are not significantly impacting the move.
- **Gap**: No gap: the small resid_z of 0.59 indicates that the move is mostly explained by factor exposures, and there is no significant unexplained component.
- **India take**: The Indian instrument that expresses this move is likely to be metal equities, such as Hindalco or Tata Steel, which may react positively to the global commodity trends. However, the reaction may be muted due to the weak inr_oil_channel and dxy_inr_channel.
- Watch next: dyn_301077_sz (up) — already moved; resid_z is small, indicating the move is largely priced
- Source: Global Market: China stocks rise on AI optimism; Hong Kong shares mostly flat — ET Markets, 2026-08-13. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-rise-on-ai-optimism-hong-kong-shares-mostly-flat/articleshow/133199079.cms
- Source: Global Market: China stocks rise as tech shares lead gains ahead of US CPI — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-rise-as-tech-shares-lead-gains-ahead-of-us-cpi/articleshow/133172233.cms
- Historical analogues: 2026-06-18 (d=0.0), 2026-03-30 (d=0.02), 2026-06-03 (d=0.03)

### [RED 5.55] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.63, z20 2.55, zc n/a, resid-z n/a [quiet], 1d 0.21%, 52-wk extreme (pct=100); |z20|=2.55; 1y-pct=100
- **Mechanism**: The midcap_largecap_ratio has reached a 52-wk extreme, with a z20 level of 2.29, indicating a potential mean reversion. However, the resid_z is None, suggesting that this move is largely priced in by factors. The RISK_ON regime and VALID vix_equity_inverse channel suggest that equity markets are likely to remain volatile.
- **Gap**: No gap: the move is largely priced in by factors, as indicated by the None resid_z value
- **India take**: The Nifty Midcap 100 index has already reacted to this move, with a z20 level of 1.79, while other transmission candidates like Dyn Bharatcoal NS and Dyn Indianb NS have also reacted, but Dyn PCJeweller NS remains quiet.
- Watch next: nifty_midcap_100 (down) — already moved; high correlation with midcap_largecap_ratio
- **India receivers**: nifty_midcap_100 (rho 0.527, z 1.47); dyn_bharatcoal_ns (rho 0.41, z -0.66); dyn_fincables_ns (rho 0.407, z 2.94); dyn_pcjeweller_ns (rho 0.382, z -0.06)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 5.31] dyn_crwv ↑
- dyn_crwv [EQUITIES]: last 107.68, z20 3.31, zc 3.21, resid-z 0.90 [moved], 1d 19.22%, |z20|=3.31
- **Mechanism**: The recent surge in CoreWeave's stock price, driven by strong AI infrastructure company earnings and positive quarterly results, has fueled AI optimism and boosted the stock prices of related companies. This move is priced, with a relatively small resid_z of 0.9, indicating that the move is largely explained by factor exposures. The VALID vix_equity_inverse channel suggests that the vol spike may lead to an equity drawdown, but the current RISK_ON regime and strong earnings reports may mitigate this effect.
- **Gap**: No gap: the move is largely priced, with a small resid_z and a big raw move, indicating that the market has already incorporated the information from CoreWeave's earnings report
- **India take**: The Indian instrument nifty_fmcg has already reacted to the move, with a rho of -0.38 via dyn_crwv. However, the metal_copper_channel may also be relevant, as global copper leads Indian metal equities, and the recent surge in AI infrastructure demand may have implications for Indian metal stocks.
- Watch next: nifty_fmcg (down) — already moved; rho=-0.38 via dyn_crwv
- **India receivers**: nifty_fmcg (rho -0.384, z -1.4)
- Source: US stocks: S&P 500 ends higher as CoreWeave results fuel AI optimism — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-sp-500-ends-higher-as-coreweave-results-fuel-ai-optimism/articleshow/133192806.cms
- Source: US stocks: CoreWeave, Super Micro surge on signs of sustained AI buildout — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-coreweave-super-micro-surge-on-signs-of-sustained-ai-buildout/articleshow/133187386.cms
- Source: CoreWeave’s stock is rocketing after earnings lead to praise from bulls and bears alike — MarketWatch Top, 2026-08-12. https://www.marketwatch.com/story/coreweaves-stock-is-rocketing-after-earnings-lead-to-praise-from-bulls-and-bears-alike-46c831e7?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-13 (d=0.01), 2025-08-05 (d=0.04)

### [RED 5.14] corn ↑
- corn [COMMODITIES]: last 476.25, z20 3.14, zc 3.30, resid-z 2.93 [unexplained], 1d 4.21%, |z20|=3.14; 1y-pct=99
- **Mechanism**: The recent surge in corn prices is driven by the USDA's unexpected reduction in yield due to heat waves, which has created a supply shock. This shock is likely to propagate through the metal_copper_channel, given the VALID status of this channel, and potentially impact Indian metal equities. The RISK_ON regime, indicated by a low probability of high volatility, also supports this move.
- **Gap**: No gap: the big raw move in corn with a relatively small resid_z of 2.93 suggests that the price move is largely priced in, given the significant reduction in yield.
- **India take**: The Indian instrument that expresses this move is likely to be the metal equities, such as Hindalco or Tata Steel, which may react positively to the supply shock in the global copper market. However, they have not reacted yet.
- Watch next: soybeans (up) — not yet - watch; high correlation with corn
- Source: Corn Jumps as USDA Cuts Yield More Than Expected Amid Heat Waves — Mint Markets, 2026-08-12. https://www.livemint.com/market/corn-jumps-as-usda-cuts-yield-more-than-expected-amid-heat-waves-11786572052753.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-21 (d=0.01), 2025-12-31 (d=0.02)

### [AMBER 5.03] cross-asset · 4 series ↑
- ust_30y [RATES]: last 5.24, z20 1.37, zc -0.23, resid-z -0.75 [quiet], 1d -0.19%, 1y-pct=99
- ust_10y [RATES]: last 4.70, z20 0.96, zc -0.42, resid-z -0.98 [quiet], 1d -0.42%, 1y-pct=98
- dyn_bond [EQUITIES]: last 90.54, z20 -0.80, zc 0.24, resid-z -0.57 [quiet], 1d 0.07%, 1y-pct=2
- tips_10y_real [RATES]: last 2.43, z20 0.80, zc 0.00, resid-z -0.59 [quiet], 1d 0.00%, 1y-pct=97
- **Mechanism**: The recent rise in US bond yields, particularly the 10-year yield reaching its highest level since 2007, is driving the current market move. This increase in yields is likely due to expectations of further monetary tightening and fiscal concerns, which is also affecting the Indian market through the transmission of global rates. The VALID gold_silver_comove and metal_copper_channel are potential channels for this transmission, but the primary driver is the global rate environment.
- **Gap**: No gap: The big raw move in US bond yields is largely priced in, with resid_z values indicating that the moves are mostly explained by factor exposures.
- **India take**: The Indian market is likely to react to the global rate environment, with potential impacts on Indian bond yields and the equity market. However, the reaction may be muted due to the already high yields in the Indian market. The MCX gold and silver prices are lacklustre, indicating that the Indian market is not yet reacting strongly to the global developments.
- Watch next: ust_30y (down) — already moved; High US bond yields are pricing in expected rate hikes
- Watch next: dyn_bond (down) — already moved; Equity market is reacting to higher US bond yields
- Watch next: tips_10y_real (down) — already moved; Real yields are rising in line with nominal yields
- Source: Global Market: Japanese bond yields hold near highs as markets brace for BOJ rate hike — ET Markets, 2026-08-13. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japanese-bond-yields-hold-near-highs-as-markets-brace-for-boj-rate-hike/articleshow/133203276.cms
- Source: Gold and silver trade lacklustre on MCX despite soft US inflation data; elevated dollar, bond yields weigh — Mint Markets, 2026-08-13. https://www.livemint.com/market/commodities/gold-and-silver-prices-today-rates-lacklustre-on-mcx-despite-soft-us-inflation-data-elevated-dollar-bond-yields-weigh-11786591359947.html
- Source: US Sells 10-Year Debt at Highest Yields Since Financial Crisis — Mint Markets, 2026-08-12. https://www.livemint.com/market/us-sells-10-year-debt-at-highest-yields-since-financial-crisis-11786566124472.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

### [RED 4.94] dyn_fincables_ns ↑
- dyn_fincables_ns [EQUITIES]: last 1252.40, z20 2.94, zc -0.51, resid-z -0.64 [quiet], 1d -2.16%, |z20|=2.94; 1y-pct=99
- **Mechanism**: dyn_fincables_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.427 via dyn_fincables_ns, z 1.47, reacted); midcap_largecap_ratio (rho 0.407 via dyn_fincables_ns, z 2.55, reacted); dyn_bharatcoal_ns (rho 0.378 via dyn_fincables_ns, z -0.66, quiet)
- **India receivers**: nifty_midcap_100 (rho 0.427, z 1.47); midcap_largecap_ratio (rho 0.407, z 2.55); dyn_bharatcoal_ns (rho 0.378, z -0.66)
- Source: Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410 — BusinessLine Mkts, 2026-08-12. https://www.thehindubusinessline.com/markets/stock-markets/finolex-cables-shares-jump-14-to-52-week-high-jefferies-lift-target-to-1410-maintains-accumulate/article71335064.ece
- Source: Finolex Cables shares jump 10% on strong Q1 performance; revenue crosses Rs 2,000 crore mark — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/stocks/news/finolex-cables-shares-jump-10-on-strong-q1-performance-revenue-crosses-rs-2000-crore-mark/articleshow/133172179.cms
- Source: Q1 Results Today Live: Tata Motors, Apollo Hospitals, HAL, Grasim GMR Airports, Lenskart, Abbott, VA Tech, IRCON, AIA, IRCTC, Sun TV, EID Parry to announce Q1 results, NBCC, Siemens, RVNL, Kalpataru, MRF, Zydus Lifesciences, KPI Green, Manappuram Finance in focus, TD Power Systems, Finolex shares hit 52-week high — BusinessLine Mkts, 2026-08-12. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-hal-grasim-ind-tata-motors-apollo-hospitals-gmr-airports-lenskart-gic-abbott-aia-engg-irctc-sun-tv-eid-parry-va-tech-ircon-titagarh-results-12-august-2026/article71332017.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-02-19 (d=0.0), 2025-02-07 (d=0.02)

### [RED 4.81] dyn_bac ↑
- dyn_bac [EQUITIES]: last 64.82, z20 2.81, zc 0.90, resid-z -0.26 [quiet], 1d 1.28%, |z20|=2.81; 1y-pct=100
- **Mechanism**: dyn_bac ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cupid_ns (rho 0.382 via dyn_bac, z 2.4, reacted)
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.64 vs dyn_bac, historically leads by 2d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.603 vs dyn_bac
- **India receivers**: dyn_cupid_ns (rho 0.382, z 2.4)
- Source: Jio Financial shares jump 3% as Bank of America set to acquire 50% stake in Jio Credit for Rs 18,268 crore — ET Markets, 2026-08-13. https://economictimes.indiatimes.com/markets/stocks/news/jio-financial-shares-in-focus-as-bank-of-america-set-to-acquire-50-stake-in-jio-credit-for-rs-18268-crore/articleshow/133197203.cms
- Source: S&P 500 EARNINGS BOOM MAY SET UP A TOUGHER 2027 S&P 500 EPS is tracking roughly 32% growth in Q2, after 30% in Q1 — a historically rare back-to-back surge. Bank of America warns growth could slow below 20% by Q1 2027 and to the mid-teens for the full year. That matters because — DeItaone, 2026-08-11. https://t.me/walter_bloomberg/34608
- Source: STOCK MARKET BOOM FUELS EARLY RETIREMENT Older Americans are leaving the workforce at a faster pace. Labor participation among people aged 55+ has dropped from above 40% pre-pandemic to 36.9% in July. Bank of America economists point to rising wealth as a key driver. With the — DeItaone, 2026-08-11. https://t.me/walter_bloomberg/34605
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

## Watchlist (below surfacing floor)
indices · 2 series ↑ (4.45), dyn_ohi ↓ (4.44), dyn_cupid_ns ↑ (4.4), dyn_tatatech_ns ↑ (3.8), dyn_atherenerg_ns ↑ (3.6), dyn_tech ↑ (3.46), bovespa ↓ (3.1), dyn_coin ↓ (3.02), dyn_hdb ↓ (2.92), indices · 2 series ↑ (2.54), dyn_icicigi_bo ↓ (2.49), dyn_lth ↑ (2.24)

## India macro
- nifty_50: 24355.8008 (1d -0.33%, z20 0.18, flag none)
- nifty_midcap_100: 63945.9492 (1d -0.12%, z20 1.47, flag amber)
- usd_inr: 95.4075 (1d 0.03%, z20 -0.78, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6255 (1d 0.21%, z20 2.55, flag red)
- Next India prints: NSDL FPI flows T-0d · India WPI T-1d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 92.6 — "LEAP India IPO listing on Friday; GMP signals modest listing pop. Details here"
- INOXINDIA.NS (INOX INDIA LIMITED) score 92.3 — "LEAP India IPO listing on Friday; GMP signals modest listing pop. Details here"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 91.7 — "LEAP India IPO listing on Friday; GMP signals modest listing pop. Details here"
- INDIANB.NS (INDIAN BANK) score 73.0 — "Multibagger stock jumps over 8% in bear-hit Indian markets"
- BAC (Bank of America Corporation) score 56.6 — "Stocks to buy: Nagaraj Shetti recommends Bank of Maharashtra, Hindustan Copper shares to b"
- COIN (Coinbase Global, Inc.) score 52.6 — "Global Market: China stocks rise on AI optimism; Hong Kong shares mostly flat"
- HDB (HDFC Bank Limited) score 52.5 — "Stocks to buy: Nagaraj Shetti recommends Bank of Maharashtra, Hindustan Copper shares to b"
- TECHM.NS (TECH MAHINDRA LIMITED) score 51.8 — "HCL Tech Share Price Live Updates: HCL Tech Stock Details"
- CHKP (Check Point Software Technolog) score 51.0 — "IPO GMP Today Live Updates: Dhoot Transmission, Milky Mist, Shiprocket & Behari Lal IPOs i"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 50.1 — "HCL Tech Share Price Live Updates: HCL Tech Stock Details"
- TECH (Bio-Techne Corp) score 49.3 — "HCL Tech Share Price Live Updates: HCL Tech Stock Details"
- OHI (Omega Healthcare Investors, In) score 48.7 — "Credent Connect N Care raises Rs 26.53 crore from 10 anchor investors; Sunil Singhania's A"
- IDBI.NS (IDBI BANK LIMITED) score 47.8 — "Stocks to buy: Nagaraj Shetti recommends Bank of Maharashtra, Hindustan Copper shares to b"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 47.8 — "Stocks to buy: Nagaraj Shetti recommends Bank of Maharashtra, Hindustan Copper shares to b"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 47.6 — "Stocks to buy: Nagaraj Shetti recommends Bank of Maharashtra, Hindustan Copper shares to b"
- LTH (Life Time Group Holdings, Inc.) score 37.0 — "Mutual Funds hit all-time high net inflows of ₹85.75 lakh crore in July 2026: Report"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 30.9 — "Trump’s Bosnia Power Play Puts an Opaque Energy Deal at the Center"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 29.7 — "Which Tata stocks look attractive now? Jefferies picks 4; flags TCS and 2 others"
- BOND (PIMCO Active Bond Exchange-Tra) score 25.5 — "Global Market: Japanese bond yields hold near highs as markets brace for BOJ rate hike"
- 301077.SZ (CHINASTARS) score 25.5 — "Global Market: China stocks rise on AI optimism; Hong Kong shares mostly flat"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 24.4 — "Which Tata stocks look attractive now? Jefferies picks 4; flags TCS and 2 others"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 19.8 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Stock Details"
- JIOFIN.BO (Jio Financial Services Limited) score 18.5 — "Will Bharti Airtel’s ARPU increase after scrapping Rs 299, other popular prepaid plans? Wh"
- JUSTDIAL.BO (JUST DIAL LTD.) score 15.8 — "Grasim Inds Share Price Live Updates: Grasim Industries Sees Price Adjustment"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 15.5 — "Will Bharti Airtel’s ARPU increase after scrapping Rs 299, other popular prepaid plans? Wh"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 13.1 — "India’s planned coal mine capacity nearly doubles to 638 mtpa in 2025"
- MS (Morgan Stanley) score 12.9 — "SPCX - MORGAN STANLEY: SPACEX LOCK-UP IS A BUYING OPPORTUNITY Morgan Stanley reiterated Ov"
- NVDA (NVIDIA Corporation) score 11.0 — "Alphabet’s stock slips as Nvidia’s $500 billion financing deal threatens custom chips"
- PCJEWELLER.NS (PC JEWELLER LTD) score 9.5 — "Motilal Oswal bullish on jewellery stocks; picks Titan, Kalyan Jewellers as top bets, sees"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 8.6 — "Bharat Heavy Electricals among 5 stocks showing bullish RSI upswing"
- META (Meta) score 7.9 — "Sensex, Nifty slip at open; cement, metals drag as Apollo Hospitals leads gains"
- AAPL (Apple Inc.) score 7.7 — "Nvidia, Apple, Google fuel record $185 billion gain for Norway’s wealth fund, but CEO say,"
- VT (Vanguard Total World Stock Ind) score 7.5 — "China’s next economic ambition: workshop for the Muslim world"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.9 — "Reliance Industries, Adani Enterprises among 10 stocks with highest DII buying up to Rs 22"
- INTC (Intel Corporation) score 4.7 — "Nvidia, Intel, Google: Wall Street is partying like it’s 1999"
- GS (Goldman Sachs Group, Inc. (The) score 3.6 — "Lenskart Solutions shares jump 7% after Q1 results; Jefferies, Goldman Sachs, 3 others rai"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.2 — "ICICI Bank Share Price Live Updates: ICICI Bank Stock Details"
- CRWV (CoreWeave, Inc.) score 2.5 — "US stocks: S&P 500 ends higher as CoreWeave results fuel AI optimism"
- FINCABLES.NS (FINOLEX CABLES LTD) score 2.4 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
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