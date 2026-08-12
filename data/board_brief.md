# Transmission Layer — board brief · 2026-08-12 21:02Z

data as of **2026-08-12** · 98 series · 11 red / 32 amber · 8 events surfaced (20 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.243, 1d in regime; vol-pct 0.309, breadth-off 0.176, Markov P(high-vol) 0.011)
- [INVERTED] **safe_haven_gold** — corr20 -0.37, corr60 -0.41, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.81, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.31, corr60 0.36, last shift 2026-05-12. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.2, corr60 -0.07, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.74, corr60 -0.81, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.09, corr60 -0.06, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.4, corr60 -0.23, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.09, corr60 0.16, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 1.1947354217056727e-10)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.495** (n=1129) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.815** (n=2503) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.18] cross-asset · 13 series ↑
- comex_gold [COMMODITIES]: last 4468.40, z20 2.87, zc 1.20, resid-z 0.33 [quiet], 1d 1.95%, |z20|=2.87; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 65.47, z20 2.32, zc 0.41, resid-z -1.02 [quiet], 1d 1.08%, |z20|=2.32; co-occur[gold_silver] same-direction (channel VALID)
- russell_2000 [INDICES]: last 3045.74, z20 1.92, zc 0.51, resid-z 0.51 [quiet], 1d 0.62%, |z20|=1.92; 1y-pct=100
- dyn_nvda [EQUITIES]: last 224.13, z20 1.83, zc 1.22, resid-z 0.48 [quiet], 1d 3.05%, 1y-pct=98
- dyn_vt [EQUITIES]: last 161.55, z20 1.73, zc 0.53, resid-z 0.98 [quiet], 1d 0.46%, 1y-pct=100
- vix [INDICES]: last 14.55, z20 -1.59, zc -0.63, resid-z n/a [quiet], 1d -4.78%, |z20|=1.59; 1y-pct=4
- stoxx_50 [INDICES]: last 6530.18, z20 1.53, zc -0.41, resid-z -0.74 [quiet], 1d -0.32%, |z20|=1.53; 1y-pct=99
- sp500 [INDICES]: last 7748.71, z20 1.47, zc 0.32, resid-z -1.19 [quiet], 1d 0.27%, 1y-pct=99
- dax [INDICES]: last 26339.76, z20 1.44, zc -0.26, resid-z -0.28 [quiet], 1d -0.20%, 1y-pct=99
- cac_40 [INDICES]: last 8665.15, z20 1.13, zc -0.79, resid-z -1.02 [quiet], 1d -0.57%, 1y-pct=97
- comex_copper [COMMODITIES]: last 6.61, z20 1.12, zc -0.04, resid-z -0.12 [quiet], 1d -0.08%, 1y-pct=97
- dow_jones [INDICES]: last 53769.86, z20 1.11, zc -0.05, resid-z -0.63 [quiet], 1d -0.04%, 1y-pct=97
- gold_silver_ratio [DERIVED]: last 68.25, z20 -1.11, zc n/a, resid-z n/a [quiet], 1d 0.86%, GSR<75 (extreme low)
- **Mechanism**: The recent US inflation data matching expectations has led to a decrease in rate hike bets, causing gold prices to rise to a two-month peak. This, in turn, has triggered a co-movement in monetary metals, with silver also experiencing an uptrend. The VALID gold_silver_comove channel suggests that the ratio extremes are rotations, indicating a potential shift in investor sentiment towards safe-haven assets.
- **Gap**: No gap: The big raw move in gold and silver prices is PRICED, with resid_z values of 0.33 and -1.02, respectively, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instrument Nifty Metal has reacted to the increase in silver prices, with a z20 value of 1.46. The Nifty Midcap 100 has also reacted, with a z20 value of 1.79, due to its correlation with the DAX index.
- Watch next: comex_gold (up) — already moved; Spot gold rose 0.9% to $4468.40 per ounce
- Watch next: comex_silver (up) — already moved; Silver prices have increased due to the co-movement with gold
- Watch next: russell_2000 (up) — already moved; US stock markets closed higher on Wednesday, driven by strong AI infrastructure company earnings
- **India receivers**: nifty_midcap_100 (rho 0.512, z 1.79); nifty_fmcg (rho -0.509, z -1.82); nifty_50 (rho 0.488, z 0.52); nifty_metal (rho 0.479, z 1.46)
- Source: Investors are chasing the latest rally in gold as the yellow metal hits strongest level in 2 months — MarketWatch Top, 2026-08-12. https://www.marketwatch.com/story/investors-are-chasing-the-latest-rally-in-gold-as-the-yellow-metal-hits-strongest-level-in-2-months-dd0d5b18?mod=mw_rss_topstories
- Source: US stocks: S&P 500 ends higher as CoreWeave results fuel AI optimism — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-sp-500-ends-higher-as-coreweave-results-fuel-ai-optimism/articleshow/133192806.cms
- Source: Gold rises to over two-month peak as US inflation data dampens rate hike bets — Mint Markets, 2026-08-12. https://www.livemint.com/market/gold-rises-to-over-two-month-peak-as-us-inflation-data-dampens-rate-hike-bets-11786560770348.html
- Historical analogues: 2024-11-26 (d=0.92), 2025-10-31 (d=1.0), 2025-10-24 (d=1.11)

### [RED 7.06] dyn_fincables_ns ↑
- dyn_fincables_ns [EQUITIES]: last 1268.50, z20 5.06, zc 1.22, resid-z 1.36 [quiet], 1d 5.02%, |z20|=5.06; 1y-pct=100
- **Mechanism**: The surge in Finolex Cables' shares is driven by its strong Q1 performance, with a 52.6% YoY rise in net profit and a 44.3% increase in revenue. This move is priced, given the significant jump in the company's financials, and is not an anomaly. The VALID metal_copper_channel and the reaction in midcap_largecap_ratio, nifty_midcap_100, and dyn_bharatcoal_ns suggest that the Indian market is responding to the positive earnings report.
- **Gap**: No gap: the move is priced due to the significant jump in Finolex Cables' financials
- **India take**: The Indian instruments such as midcap_largecap_ratio, nifty_midcap_100, and dyn_bharatcoal_ns have already reacted to the positive earnings report, indicating that the market has priced in the news. The Nifty Midcap 100 index has also moved in response to the strong Q1 performance of Finolex Cables.
- Watch next: nifty_midcap_100 (up) — already moved; reacted to Finolex Cables' strong Q1 performance
- **India receivers**: midcap_largecap_ratio (rho 0.43, z 2.29); nifty_midcap_100 (rho 0.429, z 1.79); dyn_bharatcoal_ns (rho 0.4, z -1.01)
- Source: Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410 — BusinessLine Mkts, 2026-08-12. https://www.thehindubusinessline.com/markets/stock-markets/finolex-cables-shares-jump-14-to-52-week-high-jefferies-lift-target-to-1410-maintains-accumulate/article71335064.ece
- Source: Finolex Cables shares jump 10% on strong Q1 performance; revenue crosses Rs 2,000 crore mark — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/stocks/news/finolex-cables-shares-jump-10-on-strong-q1-performance-revenue-crosses-rs-2000-crore-mark/articleshow/133172179.cms
- Source: Q1 Results Today Live: Tata Motors, Apollo Hospitals, HAL, Grasim GMR Airports, Lenskart, Abbott, VA Tech, IRCON, AIA, IRCTC, Sun TV, EID Parry to announce Q1 results, NBCC, Siemens, RVNL, Kalpataru, MRF, Zydus Lifesciences, KPI Green, Manappuram Finance in focus, TD Power Systems, Finolex shares hit 52-week high — BusinessLine Mkts, 2026-08-12. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-hal-grasim-ind-tata-motors-apollo-hospitals-gmr-airports-lenskart-gic-abbott-aia-engg-irctc-sun-tv-eid-parry-va-tech-ircon-titagarh-results-12-august-2026/article71332017.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-02-19 (d=0.0), 2025-02-07 (d=0.02)

### [AMBER 5.4] cross-asset · 4 series ↑
- ust_30y [RATES]: last 5.25, z20 1.74, zc 1.45, resid-z 1.57 [unexplained], 1d 1.16%, |z20|=1.74; 1y-pct=99
- ust_10y [RATES]: last 4.70, z20 0.96, zc -0.42, resid-z -0.98 [quiet], 1d -0.42%, 1y-pct=98
- dyn_bond [EQUITIES]: last 90.54, z20 -0.80, zc 0.24, resid-z -0.57 [quiet], 1d 0.07%, 1y-pct=2
- tips_10y_real [RATES]: last 2.43, z20 0.80, zc 0.00, resid-z -0.59 [quiet], 1d 0.00%, 1y-pct=97
- **Mechanism**: The recent surge in US Treasury yields, particularly the 10-year yield reaching its highest level since 2007, is driving the current market move. This increase in yields is likely to impact Indian markets through the metal_copper_channel, which is currently valid. The rise in US yields may lead to a strengthening of the US dollar, which could negatively impact Indian metal equities.
- **Gap**: No gap: The big raw move in ust_30y with a resid_z of 1.57 is largely priced, given the recent surge in US Treasury yields and the historical analogue distances.
- **India take**: The Indian instrument that expresses this move is likely to be the metal equities, which may react negatively to the strengthening of the US dollar. However, the inr_oil_channel is weak, and the dxy_inr_channel is also weak, which may limit the transmission of the US yield surge to Indian markets.
- Watch next: dyn_bond (down) — not yet - watch; Historical analogues suggest a potential decline in dyn_bond
- Watch next: ust_30y (up) — already moved; The recent auction of 10-year US Treasuries resulted in the highest yield since 2007
- Source: US Sells 10-Year Debt at Highest Yields Since Financial Crisis — Mint Markets, 2026-08-12. https://www.livemint.com/market/us-sells-10-year-debt-at-highest-yields-since-financial-crisis-11786566124472.html
- Source: Canadian 10-year yield pulls back from 2-year high after tame U.S. inflation data — Mint Markets, 2026-08-12. https://www.livemint.com/market/canadian-10-year-yield-pulls-back-from-2-year-high-after-tame-u-s-inflation-data-11786560586614.html
- Source: TREASURY 10-YEAR NOTE AUCTION DRAWS HIGHEST YIELD SINCE 2007 — DeItaone, 2026-08-12. https://t.me/walter_bloomberg/34700
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

### [RED 5.31] dyn_crwv ↑
- dyn_crwv [EQUITIES]: last 107.68, z20 3.31, zc 3.21, resid-z 0.90 [moved], 1d 19.22%, |z20|=3.31
- **Mechanism**: The recent surge in CoreWeave's stock price, driven by strong AI infrastructure company earnings and positive quarterly results, has fueled AI optimism and boosted the stock prices of related companies. This move is priced, with a relatively small resid_z of 0.9, indicating that the move is largely explained by factor exposures. The VALID vix_equity_inverse channel suggests that the vol spike may lead to an equity drawdown, but the current RISK_ON regime and strong earnings reports may mitigate this effect.
- **Gap**: No gap: the move is largely priced, with a small resid_z and a big raw move, indicating that the market has already incorporated the information from CoreWeave's earnings report
- **India take**: The Indian instrument nifty_fmcg has already reacted to the move, with a rho of -0.38 via dyn_crwv. However, the metal_copper_channel may also be relevant, as global copper leads Indian metal equities, and the recent surge in AI infrastructure demand may have implications for Indian metal stocks.
- Watch next: nifty_fmcg (down) — already moved; rho=-0.38 via dyn_crwv
- **India receivers**: nifty_fmcg (rho -0.38, z -1.82)
- Source: US stocks: S&P 500 ends higher as CoreWeave results fuel AI optimism — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-sp-500-ends-higher-as-coreweave-results-fuel-ai-optimism/articleshow/133192806.cms
- Source: US stocks: CoreWeave, Super Micro surge on signs of sustained AI buildout — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-coreweave-super-micro-surge-on-signs-of-sustained-ai-buildout/articleshow/133187386.cms
- Source: CoreWeave’s stock is rocketing after earnings lead to praise from bulls and bears alike — MarketWatch Top, 2026-08-12. https://www.marketwatch.com/story/coreweaves-stock-is-rocketing-after-earnings-lead-to-praise-from-bulls-and-bears-alike-46c831e7?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-13 (d=0.01), 2025-08-05 (d=0.04)

### [RED 5.29] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.62, z20 2.29, zc n/a, resid-z n/a [quiet], 1d 0.42%, 52-wk extreme (pct=99); |z20|=2.29; 1y-pct=99
- **Mechanism**: The midcap_largecap_ratio has reached a 52-wk extreme, with a z20 level of 2.29, indicating a potential mean reversion. However, the resid_z is None, suggesting that this move is largely priced in by factors. The RISK_ON regime and VALID vix_equity_inverse channel suggest that equity markets are likely to remain volatile.
- **Gap**: No gap: the move is largely priced in by factors, as indicated by the None resid_z value
- **India take**: The Nifty Midcap 100 index has already reacted to this move, with a z20 level of 1.79, while other transmission candidates like Dyn Bharatcoal NS and Dyn Indianb NS have also reacted, but Dyn PCJeweller NS remains quiet.
- Watch next: nifty_midcap_100 (down) — already moved; high correlation with midcap_largecap_ratio
- **India receivers**: nifty_midcap_100 (rho 0.533, z 1.79); dyn_fincables_ns (rho 0.43, z 5.06); dyn_bharatcoal_ns (rho 0.417, z -1.01); dyn_pcjeweller_ns (rho 0.391, z 0.32)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 4.81] dyn_bac ↑
- dyn_bac [EQUITIES]: last 64.82, z20 2.81, zc 0.90, resid-z -0.26 [quiet], 1d 1.28%, |z20|=2.81; 1y-pct=100
- **Mechanism**: The recent surge in dyn_bac is driven by the strong earnings growth in the S&P 500, which has led to a historically rare back-to-back surge in Q1 and Q2. This has resulted in a priced move, with a small resid_z of 1.16, indicating that the move is largely explained by factor exposures. The metal_copper_channel and gold_silver_comove channels are valid, but the inr_oil_channel and dxy_inr_channel are weak, suggesting that the Indian transmission candidates may not be directly affected by the current move.
- **Gap**: No gap: the move in dyn_bac is largely priced, with a small resid_z of 1.16, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instrument dyn_cupid_ns has already reacted, with a rho of 0.369 via dyn_bac, and a z20 of 2.81. The metal_copper_channel may also transmit to Indian metal equities.
- Watch next: dyn_ms (up) — not yet - watch; historically leads dyn_bac by 2d
- **India receivers**: dyn_cupid_ns (rho 0.37, z 2.81)
- Source: S&P 500 EARNINGS BOOM MAY SET UP A TOUGHER 2027 S&P 500 EPS is tracking roughly 32% growth in Q2, after 30% in Q1 — a historically rare back-to-back surge. Bank of America warns growth could slow below 20% by Q1 2027 and to the mid-teens for the full year. That matters because — DeItaone, 2026-08-11. https://t.me/walter_bloomberg/34608
- Source: STOCK MARKET BOOM FUELS EARLY RETIREMENT Older Americans are leaving the workforce at a faster pace. Labor participation among people aged 55+ has dropped from above 40% pre-pandemic to 36.9% in July. Bank of America economists point to rising wealth as a key driver. With the — DeItaone, 2026-08-11. https://t.me/walter_bloomberg/34605
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

### [RED 4.81] dyn_cupid_ns ↑
- dyn_cupid_ns [EQUITIES]: last 290.00, z20 2.81, zc 1.19, resid-z 1.17 [quiet], 1d 4.83%, |z20|=2.81; 1y-pct=100
- **Mechanism**: The recent surge in Cupid shares is driven by the company's strong Q1 FY27 earnings, with a threefold rise in net profit and 159% YoY revenue growth. This has led to a positive re-rating of the stock, with the market responding to the improved operating performance and higher FY27 guidance. The metal_copper_channel, which is currently VALID, may also be contributing to the move, as global copper leads Indian metal equities.
- **Gap**: No gap: The stock's 8.8% gain in two days post Q1 earnings is largely priced in, given the significant improvement in the company's operating performance and the positive re-rating of the stock.
- **India take**: The Indian instrument that expresses this move is Cupid shares, which have already reacted positively to the Q1 earnings. Other Indian metal equities, such as those in the copper sector, may also be affected through the metal_copper_channel.
- Watch next: Cupid (up) — already moved; Strong Q1 earnings and improved guidance
- Source: Cupid shares jump nearly 9% in two days post Q1 earnings — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/stocks/news/cupid-shares-jump-nearly-9-in-two-days-post-q1-earnings/articleshow/133177435.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-06 (d=0.01), 2025-07-24 (d=0.02)

### [AMBER 4.44] dyn_ohi ↓
- dyn_ohi [EQUITIES]: last 45.86, z20 -2.44, zc 0.45, resid-z -2.98 [unexplained], 1d 0.64%, |z20|=2.44
- **Mechanism**: The decline in dyn_ohi is driven by its unexplained component, resid_z, which is -2.98, indicating a move not fully accounted for by factor exposures. This move may propagate through the metal_copper_channel, given its VALID status and correlation with global copper. However, the RISK_ON regime and INVERTED safe_haven_gold channel suggest a complex environment. The vix_equity_inverse channel, which is VALID, may also play a role in transmitting the move to equity markets.
- **Gap**: No gap: the dyn_ohi move is largely unexplained by factors, but its magnitude is not unusually large given its z20 level, and nifty_fmcg has already reacted
- **India take**: The Indian instrument nifty_fmcg, which has a rho of 0.364 with dyn_ohi, has already reacted to the move. Further transmission may occur through the metal_copper_channel, affecting Indian metal equities.
- Watch next: nifty_fmcg (down) — already moved; rho=0.364 with dyn_ohi
- **India receivers**: nifty_fmcg (rho 0.364, z -1.82)
- Source: Investors are chasing the latest rally in gold as the yellow metal hits strongest level in 2 months — MarketWatch Top, 2026-08-12. https://www.marketwatch.com/story/investors-are-chasing-the-latest-rally-in-gold-as-the-yellow-metal-hits-strongest-level-in-2-months-dd0d5b18?mod=mw_rss_topstories
- Source: Oil prices edge up as investors weigh US-Iran talks deadlock against lower demand — Mint Markets, 2026-08-12. https://www.livemint.com/market/oil-prices-edge-up-as-investors-weigh-us-iran-talks-deadlock-against-lower-demand-11786561800055.html
- Source: Cisco stock rises ahead of Q4 earnings as investors focus on AI networking demand — Mint Markets, 2026-08-12. https://www.livemint.com/market/stock-market-news/cisco-stock-rises-ahead-of-q4-earnings-as-investors-focus-on-ai-networking-demand-11786556085300.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2024-10-15 (d=0.09)

## Watchlist (below surfacing floor)
dyn_atherenerg_ns ↑ (4.41), corn ↑ (3.82), fx · 2 series ↑ (3.76), shanghai_comp ↑ (3.59), dyn_tech ↑ (3.46), dyn_tatatech_ns ↑ (3.41), usd_brl ↑ (3.16), bovespa ↓ (3.1), dyn_coin ↓ (3.02), dyn_hdb ↓ (2.92), dyn_indianb_ns ↑ (2.46), dyn_icicigi_bo ↓ (2.45)

## India macro
- nifty_50: 24435.9492 (1d -0.15%, z20 0.52, flag none)
- nifty_midcap_100: 64024.1484 (1d 0.28%, z20 1.79, flag amber)
- usd_inr: 95.3200 (1d -0.08%, z20 -1.02, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6201 (1d 0.42%, z20 2.29, flag red)
- Next India prints: India CPI T-0d · NSDL FPI flows T-0d · India WPI T-2d · RBI Weekly Statistical Supplement T-2d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 88.6 — "Nippon India launches Income Plus Arbitrage Omni Fund of Fund"
- INOXINDIA.NS (INOX INDIA LIMITED) score 88.2 — "Nippon India launches Income Plus Arbitrage Omni Fund of Fund"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 87.6 — "Nippon India launches Income Plus Arbitrage Omni Fund of Fund"
- INDIANB.NS (INDIAN BANK) score 66.8 — "SPCX - NORGES BANK REPORTS SHARE STAKE OF 7.3 MLN CLASS A SHARES IN SPACEX - SEC FILING"
- BAC (Bank of America Corporation) score 55.2 — "UKRAINIAN DRONES OVERWHELM U.S. FORCES IN WAR GAME Ukrainian drone operators overwhelmed U"
- TECHM.NS (TECH MAHINDRA LIMITED) score 54.2 — "Q1 Results Today Highlights: Tata Motors, HAL, Grasim Industries, Eureka Forbes, Lenskart,"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 53.4 — "Q1 Results Today Highlights: Tata Motors, HAL, Grasim Industries, Eureka Forbes, Lenskart,"
- TECH (Bio-Techne Corp) score 52.5 — "Q1 Results Today Highlights: Tata Motors, HAL, Grasim Industries, Eureka Forbes, Lenskart,"
- OHI (Omega Healthcare Investors, In) score 51.8 — "Investors are chasing the latest rally in gold as the yellow metal hits strongest level in"
- HDB (HDFC Bank Limited) score 49.6 — "SPCX - NORGES BANK REPORTS SHARE STAKE OF 7.3 MLN CLASS A SHARES IN SPACEX - SEC FILING"
- COIN (Coinbase Global, Inc.) score 48.4 — "Refinery Attacks Deepen Global Diesel Supply Crunch"
- IDBI.NS (IDBI BANK LIMITED) score 45.5 — "SPCX - NORGES BANK REPORTS SHARE STAKE OF 7.3 MLN CLASS A SHARES IN SPACEX - SEC FILING"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 45.5 — "SPCX - NORGES BANK REPORTS SHARE STAKE OF 7.3 MLN CLASS A SHARES IN SPACEX - SEC FILING"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 45.2 — "SPCX - NORGES BANK REPORTS SHARE STAKE OF 7.3 MLN CLASS A SHARES IN SPACEX - SEC FILING"
- CHKP (Check Point Software Technolog) score 42.4 — "Shiprocket IPO Day 1: Issue subscribed 97% so far. GMP hints 31% listing pop. Check review"
- LTH (Life Time Group Holdings, Inc.) score 36.7 — "SAUDI SUPERTANKER RETURNS TO KEY OIL TERMINAL A supertanker has been spotted at Saudi Arab"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 33.3 — "ENERGY COULD REIGNITE INFLATION IN AUGUST Falling energy prices helped cool July inflation"
- 301077.SZ (CHINASTARS) score 26.1 — "Now China wants to become the shop floor for the Muslim world"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 25.3 — "From Trent to Titan: Over 15 Tata Group stocks more than doubled investors' wealth during "
- BOND (PIMCO Active Bond Exchange-Tra) score 23.9 — "Axis Bank raises $300 million via bonds"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 19.5 — "From Trent to Titan: Over 15 Tata Group stocks more than doubled investors' wealth during "
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 18.7 — "Quote of the day by Richard Thaler: "If we use prediction as the measure of a model, tradi"
- JUSTDIAL.BO (JUST DIAL LTD.) score 15.4 — "Miss just 5 best days of Nifty and lose big: How 21-year data from 2005-2026 shows cost of"
- JIOFIN.BO (Jio Financial Services Limited) score 15.1 — "US Sells 10-Year Debt at Highest Yields Since Financial Crisis"
- MS (Morgan Stanley) score 14.3 — "SPCX - MORGAN STANLEY: SPACEX LOCK-UP IS A BUYING OPPORTUNITY Morgan Stanley reiterated Ov"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 12.8 — "US Sells 10-Year Debt at Highest Yields Since Financial Crisis"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 12.3 — "After Mahanadi, Coal India's SECL invites banker pitches for proposed  ₹10,000 crore IPO"
- NVDA (NVIDIA Corporation) score 12.3 — "Alphabet’s stock slips as Nvidia’s $500 billion financing deal threatens custom chips"
- PCJEWELLER.NS (PC JEWELLER LTD) score 10.6 — "Motilal Oswal bullish on jewellery stocks; picks Titan, Kalyan Jewellers as top bets, sees"
- AAPL (Apple Inc.) score 8.5 — "Nvidia, Apple, Google fuel record $185 billion gain for Norway’s wealth fund, but CEO say,"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 8.5 — "ideaForge Technology shares drop over 9% in two days. JM Financial downgrades rating"
- META (Meta) score 7.6 — "Investors are chasing the latest rally in gold as the yellow metal hits strongest level in"
- VT (Vanguard Total World Stock Ind) score 7.2 — "Now China wants to become the shop floor for the Muslim world"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.4 — "QIP fundraising hits one-year high, Adani firms dominate"
- INTC (Intel Corporation) score 5.2 — "Nvidia, Intel, Google: Wall Street is partying like it’s 1999"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.6 — "ICICI Bank Share Price Live Updates: ICICI Bank Stock Details"
- CRWV (CoreWeave, Inc.) score 2.7 — "US stocks: S&P 500 ends higher as CoreWeave results fuel AI optimism"
- FINCABLES.NS (FINOLEX CABLES LTD) score 2.7 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 2.4 — "Cupid shares jump nearly 9% in two days post Q1 earnings"
- PLTR (Palantir Technologies Inc.) score 2.3 — "Palantir’s stock stages best week since 2024 — showing it’s no longer an AI loser"

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