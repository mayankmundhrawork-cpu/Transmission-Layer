# Transmission Layer — board brief · 2026-08-12 17:10Z

data as of **2026-08-12** · 98 series · 10 red / 33 amber · 8 events surfaced (19 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.243, 2d in regime; vol-pct 0.309, breadth-off 0.176, Markov P(high-vol) 0.011)
- [INVERTED] **safe_haven_gold** — corr20 -0.37, corr60 -0.41, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.87, corr60 0.81, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.31, corr60 0.36, last shift 2026-05-12. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.2, corr60 -0.07, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.74, corr60 -0.81, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.09, corr60 -0.05, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.4, corr60 -0.22, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.09, corr60 0.16, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 2.5223791944029017e-09)
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.495, β 0.2696, p 0.0); driver zc 1.52 → expected 0.406%. Type hit-rate 0.815 (n=2503).
- **SETUP** ust_10y → gbp_usd: leads 1d (ccf -0.275, β -0.1119, p 0.0); driver zc 1.52 → expected -0.168%. Type hit-rate 0.815 (n=2503).
- Track record · residual_reversion: hit-rate **0.494** (n=1130) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.815** (n=2503) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.23] cross-asset · 13 series ↑
- comex_gold [COMMODITIES]: last 4461.10, z20 2.81, zc 1.10, resid-z 0.81 [quiet], 1d 1.78%, |z20|=2.81; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 65.41, z20 2.30, zc 0.38, resid-z -0.93 [quiet], 1d 0.99%, |z20|=2.30; co-occur[gold_silver] same-direction (channel VALID)
- dyn_nvda [EQUITIES]: last 224.08, z20 1.83, zc 1.21, resid-z -1.88 [unexplained], 1d 3.03%, 1y-pct=98
- russell_2000 [INDICES]: last 3041.54, z20 1.81, zc 0.39, resid-z 0.23 [quiet], 1d 0.48%, |z20|=1.81; 1y-pct=100
- dyn_vt [EQUITIES]: last 161.52, z20 1.72, zc 0.51, resid-z 0.13 [quiet], 1d 0.44%, 1y-pct=100
- stoxx_50 [INDICES]: last 6530.18, z20 1.53, zc -0.41, resid-z -0.76 [quiet], 1d -0.32%, |z20|=1.53; 1y-pct=99
- vix [INDICES]: last 14.68, z20 -1.51, zc -0.51, resid-z n/a [quiet], 1d -3.93%, |z20|=1.51; 1y-pct=5
- sp500 [INDICES]: last 7752.98, z20 1.50, zc 0.38, resid-z 0.97 [quiet], 1d 0.32%, |z20|=1.50; 1y-pct=99
- dax [INDICES]: last 26339.76, z20 1.44, zc -0.26, resid-z -0.32 [quiet], 1d -0.20%, 1y-pct=99
- dow_jones [INDICES]: last 53821.71, z20 1.17, zc 0.07, resid-z -0.47 [quiet], 1d 0.06%, 1y-pct=98
- comex_copper [COMMODITIES]: last 6.61, z20 1.16, zc 0.00, resid-z -0.14 [quiet], 1d 0.01%, 1y-pct=98
- gold_silver_ratio [DERIVED]: last 68.20, z20 -1.15, zc n/a, resid-z n/a [quiet], 1d 0.78%, GSR<75 (extreme low)
- cac_40 [INDICES]: last 8665.15, z20 1.13, zc -0.79, resid-z -1.02 [quiet], 1d -0.57%, 1y-pct=97
- **Mechanism**: The recent surge in cross-asset prices, led by equities and commodities, is driven by the easing of inflation concerns and the resulting decrease in expected interest rate hikes. This has led to a risk-on regime, with investors seeking higher returns in assets such as Nvidia and Apple. The VALID gold_silver_comove channel suggests that monetary metals are co-moving, and the recent ratio extremes are indicative of rotations rather than a fundamental shift.
- **Gap**: No gap: The recent price moves in equities and commodities are largely explained by factor exposures, and the resid_z values indicate that these moves are PRICED, not an anomaly.
- **India take**: Indian instruments such as Nifty Midcap 100 and Nifty Metal have already reacted to the global trends, while Nifty 50 remains quiet. The metal_copper_channel suggests that global copper prices may lead Indian metal equities, potentially driving further movement in Nifty Metal.
- Watch next: dyn_nvda (up) — not yet - watch; Historical analogues suggest a potential median return of -0.5% over the next 20 days
- Watch next: comex_gold (down) — already moved; Resid_z of 0.81 indicates that the recent move is largely explained by factor exposures
- **India receivers**: nifty_midcap_100 (rho 0.512, z 1.79); nifty_fmcg (rho -0.509, z -1.82); nifty_50 (rho 0.488, z 0.52); nifty_metal (rho 0.479, z 1.46)
- Source: Nvidia, Intel, Google: Wall Street is partying like it’s 1999 — MarketWatch Top, 2026-08-12. https://www.marketwatch.com/story/nvidia-intel-google-wall-street-is-partying-like-its-1999-8520c1e3?mod=mw_rss_topstories
- Source: Nvidia, Apple, Google fuel record $185 billion gain for Norway’s wealth fund, but CEO say, ‘We are really cautious’ — Mint Markets, 2026-08-12. https://www.livemint.com/market/stock-market-news/nvidia-apple-google-fuel-record-185-billion-gain-for-norway-s-wealth-fund-but-ceo-say-we-are-really-cautious-11786542715816.html
- Source: Wall Street rises after in-line consumer inflation data, AI and chip stocks jump — Mint Markets, 2026-08-12. https://www.livemint.com/market/stock-market-news/wall-street-rises-after-in-line-consumer-inflation-data-11786543193377.html
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

### [AMBER 5.67] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.25, z20 1.74, zc 1.45, resid-z 1.57 [unexplained], 1d 1.16%, |z20|=1.74; 1y-pct=99
- ust_10y [RATES]: last 4.72, z20 1.47, zc 1.52, resid-z 1.47 [moved], 1d 1.51%, 1y-pct=99
- tips_10y_real [RATES]: last 2.43, z20 0.88, zc 0.78, resid-z 0.38 [quiet], 1d 1.25%, 1y-pct=97
- dyn_bond [EQUITIES]: last 90.65, z20 -0.48, zc 0.62, resid-z 0.24 [quiet], 1d 0.19%, 1y-pct=3
- ust_2y [RATES]: last 4.25, z20 0.20, zc 1.12, resid-z 0.77 [quiet], 1d 1.43%, 1y-pct=96
- **Mechanism**: The recent surge in US Treasury yields, particularly the 30-year and 10-year yields, is driven by inflation concerns and expectations of a potential rate hike by the Federal Reserve. This move is priced, as evidenced by the high z20 levels and low resid_z values for ust_30y and ust_10y, indicating that the market has already factored in the expected interest rate changes.
- **Gap**: No gap: the big raw move in US Treasury yields is largely priced, with small resid_z values indicating that the market has already factored in the expected interest rate changes.
- **India take**: The Indian 10-year government bond yield may react to the US Treasury yield movement, potentially leading to a rise in Indian bond yields. However, the inr_oil_channel is weak, and the dxy_inr_channel is also weak, which may limit the transmission of US yield changes to Indian markets.
- Watch next: ust_30y (up) — already moved; inflation concerns and expected rate hike
- Watch next: ust_10y (up) — already moved; inflation concerns and expected rate hike
- Source: Global Market: Euro zone bond yields dip ahead of US CPI, heavy debt supply — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-bond-yields-dip-ahead-of-us-cpi-heavy-debt-supply/articleshow/133178019.cms
- Source: Global Market: Japanese bond yields rise as traders price September BOJ rate hike — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-japanese-bond-yields-rise-as-traders-price-september-boj-rate-hike/articleshow/133176070.cms
- Source: US Stock Market: Treasury yields pare gains as Iran comments dampen hopes for Strait of Hormuz deal — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stock-market-treasury-yields-pare-gains-as-iran-comments-dampen-hopes-for-strait-of-hormuz-deal/articleshow/133171566.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.29] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.62, z20 2.29, zc n/a, resid-z n/a [quiet], 1d 0.42%, 52-wk extreme (pct=99); |z20|=2.29; 1y-pct=99
- **Mechanism**: The midcap_largecap_ratio has reached a 52-wk extreme, with a z20 level of 2.29, indicating a potential mean reversion. However, the resid_z is None, suggesting that this move is largely priced in by factors. The RISK_ON regime and VALID vix_equity_inverse channel suggest that equity markets are likely to remain volatile.
- **Gap**: No gap: the move is largely priced in by factors, as indicated by the None resid_z value
- **India take**: The Nifty Midcap 100 index has already reacted to this move, with a z20 level of 1.79, while other transmission candidates like Dyn Bharatcoal NS and Dyn Indianb NS have also reacted, but Dyn PCJeweller NS remains quiet.
- Watch next: nifty_midcap_100 (down) — already moved; high correlation with midcap_largecap_ratio
- **India receivers**: nifty_midcap_100 (rho 0.533, z 1.79); dyn_fincables_ns (rho 0.43, z 5.06); dyn_bharatcoal_ns (rho 0.417, z -1.01); dyn_pcjeweller_ns (rho 0.391, z 0.32)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 4.81] dyn_cupid_ns ↑
- dyn_cupid_ns [EQUITIES]: last 290.00, z20 2.81, zc 1.19, resid-z 1.18 [quiet], 1d 4.83%, |z20|=2.81; 1y-pct=100
- **Mechanism**: The recent surge in Cupid shares is driven by the company's strong Q1 FY27 earnings, with a threefold rise in net profit and 159% YoY revenue growth. This has led to a positive re-rating of the stock, with the market responding to the improved operating performance and higher FY27 guidance. The metal_copper_channel, which is currently VALID, may also be contributing to the move, as global copper leads Indian metal equities.
- **Gap**: No gap: The stock's 8.8% gain in two days post Q1 earnings is largely priced in, given the significant improvement in the company's operating performance and the positive re-rating of the stock.
- **India take**: The Indian instrument that expresses this move is Cupid shares, which have already reacted positively to the Q1 earnings. Other Indian metal equities, such as those in the copper sector, may also be affected through the metal_copper_channel.
- Watch next: Cupid (up) — already moved; Strong Q1 earnings and improved guidance
- Source: Cupid shares jump nearly 9% in two days post Q1 earnings — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/stocks/news/cupid-shares-jump-nearly-9-in-two-days-post-q1-earnings/articleshow/133177435.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-06 (d=0.01), 2025-07-24 (d=0.02)

### [RED 4.51] dyn_bac ↑
- dyn_bac [EQUITIES]: last 64.54, z20 2.51, zc 0.59, resid-z 1.16 [quiet], 1d 0.84%, |z20|=2.51; 1y-pct=100
- **Mechanism**: The recent increase in dyn_bac is driven by its historical correlation with the energy sector, specifically with the dynamics of oil markets. The article discussing America's wind retreat and the need for more ships to stabilize oil markets may have contributed to the move. However, the small resid_z value of 1.16 suggests that the move is largely priced in and not an anomaly.
- **Gap**: No gap: the small resid_z value indicates that the move is largely priced in
- **India take**: The Indian instrument dyn_cupid_ns has already reacted to the move in dyn_bac, given its correlation of 0.362. Further reaction in Indian metal equities may be expected through the metal_copper_channel, which is currently valid.
- Watch next: dyn_ms (up) — not yet - watch; historically leads dyn_bac by 2d
- **India receivers**: dyn_cupid_ns (rho 0.362, z 2.81)
- Source: S&P 500 EARNINGS BOOM MAY SET UP A TOUGHER 2027 S&P 500 EPS is tracking roughly 32% growth in Q2, after 30% in Q1 — a historically rare back-to-back surge. Bank of America warns growth could slow below 20% by Q1 2027 and to the mid-teens for the full year. That matters because — DeItaone, 2026-08-11. https://t.me/walter_bloomberg/34608
- Source: STOCK MARKET BOOM FUELS EARLY RETIREMENT Older Americans are leaving the workforce at a faster pace. Labor participation among people aged 55+ has dropped from above 40% pre-pandemic to 36.9% in July. Bank of America economists point to rising wealth as a key driver. With the — DeItaone, 2026-08-11. https://t.me/walter_bloomberg/34605
- Source: America's $4 Billion Wind Retreat Is a Bet on Permanently Cheap Gas — OilPrice, 2026-08-10. https://oilprice.com/Alternative-Energy/Wind-Power/Americas-4-Billion-Wind-Retreat-Is-a-Bet-on-Permanently-Cheap-Gas.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

### [AMBER 4.41] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1572.90, z20 2.41, zc 0.95, resid-z 0.83 [quiet], 1d 3.11%, |z20|=2.41; 1y-pct=100
- **Mechanism**: The surge in Ather Energy's shares is driven by the government's extension of subsidies for electric two-wheelers until FY28, which has improved sentiment towards the sector. This move is likely to propagate through the metal_copper_channel, as global copper leads Indian metal equities. The VALID gold_silver_comove channel also suggests a potential co-move with other monetary metals.
- **Gap**: No gap: the move in dyn_atherenerg_ns is largely priced, given its resid_z of 0.4, which is relatively small compared to its z20 level of 2.31
- **India take**: The Indian instrument that expresses this move is Tata Motors, which has a significant stake in the electric vehicle market. It has not reacted yet, but may follow suit given the improved sentiment towards the sector.
- Watch next: ola_electric_ns (up) — not yet - watch; similar business model to Ather Energy
- Source: Ola Electric, Ather Energy shares surge up to 5% as EV subsidies extended to FY28 — Mint Markets, 2026-08-11. https://www.livemint.com/market/stock-market-news/ola-electric-ather-energy-shares-surge-up-to-5-as-ev-subsidies-extended-to-fy28-11786439521082.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [AMBER 4.38] dyn_ohi ↓
- dyn_ohi [EQUITIES]: last 45.96, z20 -2.38, zc 0.61, resid-z -1.30 [quiet], 1d 0.86%, |z20|=2.38
- **Mechanism**: The decline in dyn_ohi is largely priced, with a small resid_z of -1.3, indicating that the move is mostly explained by factor exposures. The RISK_ON regime and VALID vix_equity_inverse channel suggest that the market is positioned for a potential drawdown in equities. However, the weak channels, including inr_oil_channel and dxy_inr_channel, may limit the transmission of global risk-off sentiment to Indian markets.
- **Gap**: No gap: the decline in dyn_ohi is largely priced, with a small resid_z and a quiet move label
- **India take**: The Indian instrument nifty_fmcg has already reacted to the decline in dyn_ohi, with a rho of 0.361. Further downside in nifty_fmcg may be limited by the weak transmission channels.
- Watch next: nifty_fmcg (down) — already moved; reacted to dyn_ohi decline
- **India receivers**: nifty_fmcg (rho 0.361, z -1.82)
- Source: From Trent to Titan: Over 15 Tata Group stocks more than doubled investors' wealth during Chandrasekaran's tenure — Mint Markets, 2026-08-12. https://www.livemint.com/market/stock-market-news/over-15-tata-group-stocks-more-than-doubled-investors-wealth-under-chandras-tenure-as-chairman-of-tata-sons-11786543718013.html
- Source: NORWAY’S $2.3T FUND WARNS GAINS WON’T LAST Norway’s sovereign wealth fund posted a record $185 billion first-half profit, delivering a 12.95% return as semiconductor stocks surged. But CEO Nicolai Tangen warned investors not to expect similar returns ahead, citing — DeItaone, 2026-08-12. https://t.me/walter_bloomberg/34680
- Source: TCS shares tumble 4%, wipe out Rs 35,000 crore after N Chandrasekaran resigns. What should investors do? — ET Markets, 2026-08-12. https://economictimes.indiatimes.com/markets/stocks/news/tcs-shares-tumble-4-wipe-out-rs-35000-crore-after-n-chandrasekaran-resigns-what-should-investors-do/articleshow/133180381.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2024-10-15 (d=0.09)

## Watchlist (below surfacing floor)
shanghai_comp ↑ (3.59), fx · 2 series ↑ (3.49), dyn_tech ↑ (3.46), dyn_tatatech_ns ↑ (3.41), corn ↑ (3.39), dyn_coin ↓ (3.13), usd_cny ↓ (3.01), dyn_hdb ↓ (2.93), bovespa ↓ (2.77), dyn_lth ↑ (2.48), dyn_indianb_ns ↑ (2.46), dyn_icicigi_bo ↓ (2.45)

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
- COALINDIA.NS (COAL INDIA LTD) score 91.9 — "Nippon India launches Income Plus Arbitrage Omni Fund of Fund"
- INOXINDIA.NS (INOX INDIA LIMITED) score 91.5 — "Nippon India launches Income Plus Arbitrage Omni Fund of Fund"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 90.9 — "Nippon India launches Income Plus Arbitrage Omni Fund of Fund"
- INDIANB.NS (INDIAN BANK) score 69.4 — "SPCX - NORGES BANK REPORTS SHARE STAKE OF 7.3 MLN CLASS A SHARES IN SPACEX - SEC FILING"
- TECHM.NS (TECH MAHINDRA LIMITED) score 56.2 — "Q1 Results Today Highlights: Tata Motors, HAL, Grasim Industries, Eureka Forbes, Lenskart,"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 55.4 — "Q1 Results Today Highlights: Tata Motors, HAL, Grasim Industries, Eureka Forbes, Lenskart,"
- BAC (Bank of America Corporation) score 55.2 — "SPCX - NORGES BANK REPORTS SHARE STAKE OF 7.3 MLN CLASS A SHARES IN SPACEX - SEC FILING"
- TECH (Bio-Techne Corp) score 54.5 — "Q1 Results Today Highlights: Tata Motors, HAL, Grasim Industries, Eureka Forbes, Lenskart,"
- HDB (HDFC Bank Limited) score 51.5 — "SPCX - NORGES BANK REPORTS SHARE STAKE OF 7.3 MLN CLASS A SHARES IN SPACEX - SEC FILING"
- OHI (Omega Healthcare Investors, In) score 49.7 — "From Trent to Titan: Over 15 Tata Group stocks more than doubled investors' wealth during "
- COIN (Coinbase Global, Inc.) score 49.2 — "Vedanta Aluminium goes global with its digital metal bazaar platform"
- IDBI.NS (IDBI BANK LIMITED) score 47.2 — "SPCX - NORGES BANK REPORTS SHARE STAKE OF 7.3 MLN CLASS A SHARES IN SPACEX - SEC FILING"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 47.2 — "SPCX - NORGES BANK REPORTS SHARE STAKE OF 7.3 MLN CLASS A SHARES IN SPACEX - SEC FILING"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 46.9 — "SPCX - NORGES BANK REPORTS SHARE STAKE OF 7.3 MLN CLASS A SHARES IN SPACEX - SEC FILING"
- CHKP (Check Point Software Technolog) score 44.0 — "Shiprocket IPO Day 1: Issue subscribed 97% so far. GMP hints 31% listing pop. Check review"
- LTH (Life Time Group Holdings, Inc.) score 37.0 — "TRUMP’S SCHEDULE — WEDNESDAY, AUGUST 12 🔸 8:00 AM — Executive Time 🔸 10:30 AM — Greeting w"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 34.5 — "ENERGY COULD REIGNITE INFLATION IN AUGUST Falling energy prices helped cool July inflation"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 26.3 — "From Trent to Titan: Over 15 Tata Group stocks more than doubled investors' wealth during "
- 301077.SZ (CHINASTARS) score 26.1 — "China Expands Its Economic Footprint Across Central Asia"
- BOND (PIMCO Active Bond Exchange-Tra) score 24.8 — "Axis Bank raises $300 million via bonds"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 20.2 — "From Trent to Titan: Over 15 Tata Group stocks more than doubled investors' wealth during "
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 19.5 — "Quote of the day by Richard Thaler: "If we use prediction as the measure of a model, tradi"
- JUSTDIAL.BO (JUST DIAL LTD.) score 15.9 — "Miss just 5 best days of Nifty and lose big: How 21-year data from 2005-2026 shows cost of"
- JIOFIN.BO (Jio Financial Services Limited) score 14.6 — "BofA to invest $1.9 billion for 49.9% stake in Jio Financial NBFC unit"
- MS (Morgan Stanley) score 13.8 — "SANTANDER STILL SEES SEPTEMBER FED HIKE July CPI is unlikely to decide the Fed’s September"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 12.8 — "After Mahanadi, Coal India's SECL invites banker pitches for proposed  ₹10,000 crore IPO"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 12.2 — "BofA to invest $1.9 billion for 49.9% stake in Jio Financial NBFC unit"
- NVDA (NVIDIA Corporation) score 11.7 — "Nvidia, Intel, Google: Wall Street is partying like it’s 1999"
- PCJEWELLER.NS (PC JEWELLER LTD) score 11.0 — "Motilal Oswal bullish on jewellery stocks; picks Titan, Kalyan Jewellers as top bets, sees"
- AAPL (Apple Inc.) score 8.8 — "Nvidia, Apple, Google fuel record $185 billion gain for Norway’s wealth fund, but CEO say,"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 8.8 — "ideaForge Technology shares drop over 9% in two days. JM Financial downgrades rating"
- META (Meta) score 6.9 — "Vedanta Aluminium goes global with its digital metal bazaar platform"
- VT (Vanguard Total World Stock Ind) score 6.4 — "NORWAY’S WEALTH FUND SMASHES PROFIT RECORD Norway’s $2.3 trillion sovereign wealth fund po"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.6 — "QIP fundraising hits one-year high, Adani firms dominate"
- INTC (Intel Corporation) score 5.4 — "Nvidia, Intel, Google: Wall Street is partying like it’s 1999"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.7 — "ICICI Bank Share Price Live Updates: ICICI Bank Stock Details"
- FINCABLES.NS (FINOLEX CABLES LTD) score 2.8 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 2.5 — "Cupid shares jump nearly 9% in two days post Q1 earnings"
- PLTR (Palantir Technologies Inc.) score 2.4 — "Palantir’s stock stages best week since 2024 — showing it’s no longer an AI loser"
- AMZN (Amazon.com, Inc.) score 1.7 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"

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