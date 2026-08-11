# Transmission Layer — board brief · 2026-08-11 13:39Z

data as of **2026-08-11** · 98 series · 7 red / 29 amber · 8 events surfaced (14 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.274, 2d in regime; vol-pct 0.348, breadth-off 0.2, Markov P(high-vol) 0.01)
- [INVERTED] **safe_haven_gold** — corr20 -0.35, corr60 -0.39, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.83, corr60 0.81, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.28, corr60 0.34, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.14, corr60 -0.08, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.79, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.08, corr60 -0.03, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.41, corr60 -0.25, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.01, corr60 0.16, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.49** (n=1134) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.815** (n=2482) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.02] cross-asset · 12 series ↑
- comex_gold [COMMODITIES]: last 4458.10, z20 3.36, zc 1.23, resid-z 1.08 [quiet], 1d 2.21%, |z20|=3.36; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 65.11, z20 2.60, zc -0.00, resid-z -1.87 [unexplained], 1d -0.00%, |z20|=2.60; co-occur[gold_silver] same-direction (channel VALID)
- stoxx_50 [INDICES]: last 6562.85, z20 2.09, zc 0.52, resid-z 0.26 [quiet], 1d 0.42%, |z20|=2.09; 1y-pct=100
- dyn_vt [EQUITIES]: last 161.32, z20 1.82, zc 0.24, resid-z 0.29 [quiet], 1d 0.22%, 1y-pct=100
- cac_40 [INDICES]: last 8735.70, z20 1.80, zc 0.15, resid-z -0.11 [quiet], 1d 0.11%, |z20|=1.80; 1y-pct=100
- dax [INDICES]: last 26413.80, z20 1.79, zc 0.44, resid-z 0.27 [quiet], 1d 0.34%, |z20|=1.79; 1y-pct=100
- dow_jones [INDICES]: last 54155.96, z20 1.67, zc 0.39, resid-z 0.35 [quiet], 1d 0.33%, |z20|=1.67; 1y-pct=99
- sp500 [INDICES]: last 7755.31, z20 1.67, zc 0.03, resid-z 0.23 [quiet], 1d 0.03%, |z20|=1.67; 1y-pct=99
- comex_copper [COMMODITIES]: last 6.66, z20 1.62, zc 0.44, resid-z 0.60 [quiet], 1d 0.99%, |z20|=1.62; 1y-pct=99
- russell_2000 [INDICES]: last 3017.40, z20 1.47, zc -0.45, resid-z -0.49 [quiet], 1d -0.56%, 1y-pct=98
- dyn_nvda [EQUITIES]: last 219.61, z20 1.39, zc 0.36, resid-z 0.64 [quiet], 1d 0.95%, 1y-pct=96
- gold_silver_ratio [DERIVED]: last 68.48, z20 -1.04, zc n/a, resid-z n/a [quiet], 1d 2.21%, GSR<75 (extreme low)
- **Mechanism**: The current move is driven by uncertainty over a potential peace deal in the Middle East, fuelling inflation fears and dampening risk appetite. This is reflected in the VALID gold_silver_comove channel, where corr20=0.83, indicating a strong co-movement between monetary metals. The metal_copper_channel is also VALID, with corr20=0.28, suggesting global copper leads Indian metal equities.
- **Gap**: No gap: the big raw move in comex_gold has a small resid_z, indicating it is PRICED, not an anomaly
- **India take**: The Indian instrument nifty_metal, which has a rho of 0.473 with comex_silver, has already reacted. The nifty_midcap_100, with a rho of 0.494 via dax, has also reacted.
- Watch next: comex_gold (up) — quiet; priced move with small resid_z
- Watch next: comex_silver (down) — unexplained; large negative resid_z
- **India receivers**: nifty_fmcg (rho -0.516, z -0.9); nifty_50 (rho 0.494, z 0.72); nifty_midcap_100 (rho 0.494, z 1.71); nifty_metal (rho 0.473, z 1.33)
- Source: US stock market today: Wall Street futures flat as Hormuz uncertainty fuels inflation fears — Mint Markets, 2026-08-11. https://www.livemint.com/market/stock-market-news/us-stock-market-today-wall-street-futures-flat-as-hormuz-uncertainty-fuels-inflation-fears-11786451402700.html
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US futures edge up as Hormuz progress weighs down oil prices — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-hormuz-deal-crude-oil-fed-warsh-rate-rocket-lab-amd-intel-spacex-chip-stock-price-news-11th-august-2026/liveblog/133154916.cms
- Source: NVDA - NVIDIA IS PLAYING A MUCH BIGGER AI GAME Wells Fargo reiterated Overweight on $NVDA with a $315 price target. The firm highlighted NVIDIA’s new $500B+ AI infrastructure financing partnership with Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs and KKR. Wells — DeItaone, 2026-08-11. https://t.me/walter_bloomberg/34610
- Historical analogues: 2024-11-26 (d=0.94), 2025-10-31 (d=1.04), 2024-10-15 (d=1.15)

### [RED 4.68] dyn_ohi ↓
- dyn_ohi [EQUITIES]: last 46.33, z20 -2.68, zc -1.63, resid-z -0.48 [moved], 1d -2.23%, |z20|=2.68
- **Mechanism**: The decline in dyn_ohi is largely priced, with a small resid_z of -0.48, indicating that the move is mostly explained by factor exposures. The RISK_ON regime and VALID vix_equity_inverse channel suggest that the market is experiencing a risk-off sentiment, which is consistent with the decline in dyn_ohi. However, the broken channels, such as inr_oil_channel and dxy_inr_channel, limit the potential for further propagation of this move.
- **Gap**: No gap: the small resid_z and priced move suggest that the event is largely reflected in the current price
- **India take**: The Indian instrument nifty_fmcg, which has a rho of 0.363 with dyn_ohi, has not yet reacted to this move. The metal_copper_channel, which is VALID, may also influence Indian metal equities.
- Watch next: nifty_fmcg (down) — quiet; rho=0.363 via dyn_ohi
- **India receivers**: nifty_fmcg (rho 0.363, z -0.9)
- Source: Investors turn to riskier bets as large-cap funds see net outflows in July — Mint Markets, 2026-08-11. https://www.livemint.com/market/investors-turn-to-riskier-bets-as-large-cap-funds-see-net-outflows-in-july-sip-nfos-mutual-funds-equity-11786446157901.html
- Source: Sebi proposes to widen foreign investors' access to non-agricultural commodities derivatives — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/commodities/news/sebi-proposes-to-widen-foreign-investors-access-to-non-agricultural-commodities-derivatives/articleshow/133153234.cms
- Source: Don't worry about AI! Why PPFAS CIO Rajeev Thakkar wants Indian investors to read what tech analyst Benedict Evans said — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/stocks/news/dont-worry-about-ai-why-ppfas-cio-rajeev-thakkar-wants-indian-investors-to-read-what-tech-analyst-benedict-evans-said/articleshow/133152220.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2024-10-15 (d=0.09)

### [RED 4.64] dyn_cupid_ns ↑
- dyn_cupid_ns [EQUITIES]: last 276.65, z20 2.64, zc 1.31, resid-z 1.55 [unexplained], 1d 5.31%, |z20|=2.64; 1y-pct=100
- **Mechanism**: The recent surge in Cupid's Q1 FY27 profit, which tripled to Rs 44 crore, and the company's raised revenue and profit guidance for FY27, may have triggered a positive response in the stock. However, the stock's quiet move, with a low resid_z of 0.02, suggests that the move is largely priced in. The VALID metal_copper_channel and the company's strong financial performance may be contributing to the stock's upward momentum.
- **Gap**: No gap: the stock's move is largely priced in, with a low resid_z of 0.02 and a strong financial performance
- **India take**: The Indian instrument that expresses this move is the Nifty Midcap 100, which has already reacted with a rho of 0.357 via dyn_cupid_ns. The stock's strong financial performance and the VALID metal_copper_channel may continue to support the Nifty Midcap 100's upward momentum.
- Watch next: nifty_midcap_100 (up) — already moved; rho=0.357 via dyn_cupid_ns
- Source: Cupid shares fall 2% even as Q1 profit jumps 3x. What’s ahead for multibagger stock that rose 680% in a year? — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/news/cupid-shares-fall-2-even-as-q1-profit-jumps-3x-whats-ahead-for-multibagger-stock-that-rose-680-in-a-year/articleshow/133085241.cms
- Source: Q1 Results Highlights: BEML loss narrows to ₹27 cr, Eveready profit up 22%, Aditya Birla Fashion loss widens to ₹249 cr, Cupid profit nearly triples, Ceigall up 35% — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/stock-markets/q1-results-today-live-updates-delhivery-anant-raj-apollo-micro-systems-akums-drugs-pharma-aditya-birla-fashion-ceigall-pnc-infratech-oswal-pumps-results-08-august-2026/article71320548.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-06 (d=0.01), 2025-07-24 (d=0.02)

### [AMBER 4.59] cross-asset · 4 series ↑
- dyn_bond [EQUITIES]: last 90.54, z20 -0.93, zc 0.45, resid-z -0.39 [quiet], 1d 0.14%, 1y-pct=2
- ust_30y [RATES]: last 5.19, z20 0.77, zc -0.71, resid-z -0.57 [quiet], 1d -0.57%, 1y-pct=98
- tips_10y_real [RATES]: last 2.40, z20 0.25, zc -0.77, resid-z -0.36 [quiet], 1d -1.23%, 1y-pct=95
- ust_10y [RATES]: last 4.65, z20 0.23, zc -0.86, resid-z -0.43 [quiet], 1d -0.85%, 1y-pct=96
- **Mechanism**: The recent surge in oil prices, triggered by US President Donald Trump's stance on Iran and doubts over the reopening of the Strait of Hormuz, has led to an uptick in Euro zone bond yields. This has created a ripple effect in the global bond market, with US Treasury yields also rising. The mechanism for this move is the transmission of oil price shocks to interest rates, which is a well-established channel.
- **Gap**: No gap: the big raw move in bond yields is largely priced, with resid_z values for ust_30y and ust_10y at -0.57 and -0.43, respectively, indicating that the move is largely explained by factor exposures
- **India take**: The Indian 10-year government bond yield may react to this global trend, potentially leading to a rise in yields. However, the inr_oil_channel is weak, which may limit the transmission of oil price shocks to Indian bond yields.
- Watch next: ust_30y (up) — already moved; oil price surge
- Watch next: ust_10y (up) — already moved; oil price surge
- Source: TREASURY YIELDS AND DOLLAR RISE AS OIL CLIMBS Treasury yields and the dollar moved higher as rising oil prices fueled concerns over stalled U.S.-Iran negotiations on the Strait of Hormuz. Markets are increasing bets on a Fed rate hike in September. The 10-year Treasury yield — DeItaone, 2026-08-11. https://t.me/walter_bloomberg/34607
- Source: Euro zone bond yields rise as oil climbs on Hormuz doubts — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bond-yields-rise-as-oil-climbs-on-hormuz-doubts/articleshow/133146952.cms
- Source: The Bessent bond-market scorecard doesn’t look as strong as it once did — MarketWatch Top, 2026-08-11. https://www.marketwatch.com/story/the-bessent-bond-market-scorecard-doesnt-look-as-strong-as-it-once-did-afe2f93e?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

### [AMBER 4.46] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.61, z20 1.46, zc n/a, resid-z n/a [quiet], 1d 0.46%, 52-wk extreme (pct=98); 1y-pct=98
- **Mechanism**: The midcap_largecap_ratio has risen, indicating a potential shift in market sentiment towards midcaps. This move is priced, with a resid_z of None, suggesting that the move is largely explained by factor exposures. The valid gold_silver_comove and metal_copper_channel may influence the transmission of this move to Indian markets.
- **Gap**: No gap: the move is priced with a resid_z of None, indicating that the current price reflects the known factors
- **India take**: The Nifty Midcap 100 and Dyn PC Jeweller have already reacted to the midcap_largecap_ratio move, while Dyn Bharat Coal remains quiet. The Indian market may see further adjustments in midcap stocks.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to midcap_largecap_ratio move
- **India receivers**: nifty_midcap_100 (rho 0.535, z 1.71); dyn_bharatcoal_ns (rho 0.465, z -1.02); dyn_pcjeweller_ns (rho 0.415, z 0.72)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [AMBER 4.39] dyn_bac ↑
- dyn_bac [EQUITIES]: last 64.15, z20 2.39, zc 0.32, resid-z -0.22 [quiet], 1d 0.45%, |z20|=2.39; 1y-pct=100
- **Mechanism**: The recent move in dyn_bac is largely priced, with a small resid_z of -0.22, indicating that the move is mostly explained by factor exposures. The correlated instrument dyn_ms has not moved yet, but historically leads dyn_bac by 2 days. The RISK_ON regime and VALID vix_equity_inverse channel suggest that the market is positioned for further risk-on moves.
- **Gap**: No gap: the move in dyn_bac is largely priced, with a small resid_z and a high r2 value of 0.147
- **India take**: The Indian instrument dyn_cupid_ns has already reacted, with a rho of 0.367 via dyn_bac, and a z20 of 2.64. Further moves in dyn_bac may be transmitted to Indian metal equities via the VALID metal_copper_channel.
- Watch next: dyn_ms (up) — not yet - watch; historically leads dyn_bac by 2 days
- **India receivers**: dyn_cupid_ns (rho 0.367, z 2.64)
- Source: S&P 500 EARNINGS BOOM MAY SET UP A TOUGHER 2027 S&P 500 EPS is tracking roughly 32% growth in Q2, after 30% in Q1 — a historically rare back-to-back surge. Bank of America warns growth could slow below 20% by Q1 2027 and to the mid-teens for the full year. That matters because — DeItaone, 2026-08-11. https://t.me/walter_bloomberg/34608
- Source: STOCK MARKET BOOM FUELS EARLY RETIREMENT Older Americans are leaving the workforce at a faster pace. Labor participation among people aged 55+ has dropped from above 40% pre-pandemic to 36.9% in July. Bank of America economists point to rising wealth as a key driver. With the — DeItaone, 2026-08-11. https://t.me/walter_bloomberg/34605
- Source: America's $4 Billion Wind Retreat Is a Bet on Permanently Cheap Gas — OilPrice, 2026-08-10. https://oilprice.com/Alternative-Energy/Wind-Power/Americas-4-Billion-Wind-Retreat-Is-a-Bet-on-Permanently-Cheap-Gas.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

### [AMBER 4.34] dyn_tatatech_ns ↑
- dyn_tatatech_ns [EQUITIES]: last 865.20, z20 2.34, zc -0.49, resid-z -0.74 [quiet], 1d -1.59%, |z20|=2.34; 1y-pct=99
- **Mechanism**: The recent surge in dyn_tatatech_ns is largely priced, with a small resid_z of 0.15, indicating that the move is mostly explained by factor exposures. The metal_copper_channel, which is currently valid, may provide a mechanism for this move to propagate, given the global copper leads Indian metal equities. However, the lack of a strong channel connecting dyn_tatatech_ns to other assets limits the potential for further propagation.
- **Gap**: No gap: the move in dyn_tatatech_ns is largely priced, with a small resid_z and no clear dislocation from historical analogues
- **India take**: Indian instruments such as dyn_tataelxsi_ns and nifty_it have already reacted to the move in dyn_tatatech_ns, given their correlations of 0.467 and 0.461, respectively. Further reaction is unlikely, given the priced nature of the move.
- Watch next: dyn_tataelxsi_ns (up) — already moved; rho=0.467 with dyn_tatatech_ns
- **India receivers**: dyn_tataelxsi_ns (rho 0.467, z 1.46); nifty_it (rho 0.457, z 1.44)
- Source: Tata Consumer Share Price Live Updates: Tata Consumer's Current Market Position — ET Markets, 2026-08-11. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tata-consumer-share-price-live-updates-11-aug-2026/liveblog/133140823.cms
- Source: Titan shares: Is the Tata Group stock an attractive buy after Q1FY27 results? — Mint Markets, 2026-08-10. https://www.livemint.com/market/stock-market-news/titan-shares-is-the-tata-group-stock-an-attractive-buy-after-q1fy27-results-11786352452848.html
- Source: Tata Technologies among 5 stocks flashing bullish signals. Upside on cards? — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/news/tata-technologies-among-5-stocks-flashing-bullish-signals-upside-on-cards/slideshow/133080114.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

### [AMBER 4.29] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1526.00, z20 2.29, zc 1.25, resid-z 0.90 [quiet], 1d 4.08%, |z20|=2.29; 1y-pct=100
- **Mechanism**: The surge in Ather Energy's shares is driven by the government's extension of subsidies for electric two-wheelers until FY28, which has improved sentiment towards the sector. This move is likely to propagate through the metal_copper_channel, as global copper leads Indian metal equities. The VALID gold_silver_comove channel also supports the move, as monetary metals co-move and ratio extremes are rotations.
- **Gap**: No gap: the move in Ather Energy's shares is PRICED, given the small resid_z of 0.93 and the significant z20 level of 2.29, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is Tata Motors, which has a significant exposure to the electric vehicle sector. The stock has likely reacted positively to the news, given the improved sentiment towards the sector.
- Watch next: ola_electric (up) — already moved; similar business exposure to EV subsidies
- Source: Ola Electric, Ather Energy shares surge up to 5% as EV subsidies extended to FY28 — Mint Markets, 2026-08-11. https://www.livemint.com/market/stock-market-news/ola-electric-ather-energy-shares-surge-up-to-5-as-ev-subsidies-extended-to-fy28-11786439521082.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

## Watchlist (below surfacing floor)
fx · 2 series ↑ (3.42), dyn_tech ↑ (3.24), dyn_coin ↓ (3.21), usd_cny ↓ (3.1), dyn_icicigi_bo ↓ (2.5), dyn_idbi_ns ↓ (2.5), dyn_pltr ↑ (2.22), dyn_lth ↓ (2.17), bovespa ↓ (1.88), nifty_midcap_100 ↑ (1.71), asx_200 ↑ (1.67), dyn_amzn ↑ (1.16)

## India macro
- nifty_50: 24471.6992 (1d -0.46%, z20 0.72, flag none)
- nifty_midcap_100: 63848.3008 (1d -0.00%, z20 1.71, flag amber)
- usd_inr: 95.4250 (1d 0.23%, z20 -0.92, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6091 (1d 0.46%, z20 1.46, flag amber)
- Next India prints: NSDL FPI flows T-0d · India CPI T-1d · India WPI T-3d · RBI Weekly Statistical Supplement T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 90.1 — "Don't worry about AI! Why PPFAS CIO Rajeev Thakkar wants Indian investors to read what tec"
- COALINDIA.NS (COAL INDIA LTD) score 89.5 — "Don't worry about AI! Why PPFAS CIO Rajeev Thakkar wants Indian investors to read what tec"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 89.3 — "Don't worry about AI! Why PPFAS CIO Rajeev Thakkar wants Indian investors to read what tec"
- INDIANB.NS (INDIAN BANK) score 71.2 — "STOCK MARKET BOOM FUELS EARLY RETIREMENT Older Americans are leaving the workforce at a fa"
- BAC (Bank of America Corporation) score 56.9 — "STOCK MARKET BOOM FUELS EARLY RETIREMENT Older Americans are leaving the workforce at a fa"
- HDB (HDFC Bank Limited) score 51.6 — "STOCK MARKET BOOM FUELS EARLY RETIREMENT Older Americans are leaving the workforce at a fa"
- IDBI.NS (IDBI BANK LIMITED) score 49.5 — "STOCK MARKET BOOM FUELS EARLY RETIREMENT Older Americans are leaving the workforce at a fa"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 49.5 — "STOCK MARKET BOOM FUELS EARLY RETIREMENT Older Americans are leaving the workforce at a fa"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 49.0 — "STOCK MARKET BOOM FUELS EARLY RETIREMENT Older Americans are leaving the workforce at a fa"
- TECHM.NS (TECH MAHINDRA LIMITED) score 48.6 — "Don't worry about AI! Why PPFAS CIO Rajeev Thakkar wants Indian investors to read what tec"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 47.5 — "Don't worry about AI! Why PPFAS CIO Rajeev Thakkar wants Indian investors to read what tec"
- TECH (Bio-Techne Corp) score 46.3 — "Don't worry about AI! Why PPFAS CIO Rajeev Thakkar wants Indian investors to read what tec"
- OHI (Omega Healthcare Investors, In) score 45.2 — "Don't worry about AI! Why PPFAS CIO Rajeev Thakkar wants Indian investors to read what tec"
- COIN (Coinbase Global, Inc.) score 44.0 — "Global Market: European shares edge higher as energy stocks gain on Middle East uncertaint"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 39.3 — "Global Market: European shares edge higher as energy stocks gain on Middle East uncertaint"
- CHKP (Check Point Software Technolog) score 37.2 — "Milky Mist IPO Day 1: Issue booked 65% so far. Check GMP, key dates, review, issue details"
- LTH (Life Time Group Holdings, Inc.) score 30.5 — "PRESIDENT’S CALENDAR — TUESDAY, AUGUST 11 🔸 8:00 AM — Executive Time 🔸 9:00 AM — In-Town P"
- BOND (PIMCO Active Bond Exchange-Tra) score 24.2 — "Indian bonds slip as crude hovers near $90"
- 301077.SZ (CHINASTARS) score 22.1 — "China’s Teapot Refiners Poised to Ramp Up Iranian Oil Buying"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.2 — "Q1 Results Today Live: NBCC (India) PAT up 32% y-o-y, Siemens, RVNL, Kalpataru Q1 profit r"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 14.4 — "Bharat Forge’s cost pressures dampen defence-driven euphoria"
- PCJEWELLER.NS (PC JEWELLER LTD) score 13.0 — "Lalithaa Jewellery’s ₹1,700 crore IPO opens August 17; price band fixed at ₹190-201"
- JUSTDIAL.BO (JUST DIAL LTD.) score 12.0 — "My wife’s Social Security is just $900. Should she claim her spousal benefit at 62 or wait"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.0 — "Tata Consumer Share Price Live Updates: Tata Consumer's Current Market Position"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 10.2 — "ideaForge Technology shares slide 5% after Q1 gross profit margin falls 49%"
- JIOFIN.BO (Jio Financial Services Limited) score 9.9 — "Jio Financial Services Share Price Live Updates: Jio Financial Services News"
- MS (Morgan Stanley) score 9.8 — "SPCX - SPACEX: MORGAN STANLEY SEES $300 TARGET, $600 BULL CASE Morgan Stanley maintains it"
- NVDA (NVIDIA Corporation) score 8.3 — "NVDA - NVIDIA IS PLAYING A MUCH BIGGER AI GAME Wells Fargo reiterated Overweight on $NVDA "
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.0 — "Jio Financial Services Share Price Live Updates: Jio Financial Services News"
- AAPL (Apple Inc.) score 7.9 — "AAPL - APPLE REPORTEDLY SCRAPS ALL-GLASS IPHONE Apple has canceled its planned 20th-annive"
- META (Meta) score 7.7 — "Q1 Results Today Highlights: Bharat Forge shares tank after Q1 loss, Kwality Pharma, Ramco"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.3 — "QIP fundraising hits one-year high, Adani firms dominate"
- VT (Vanguard Total World Stock Ind) score 7.1 — "GLENCORE'S EXPOSURE TO IRON ORE TRADER RADIANT WORLD MORE THAN $500 MILLION, SOURCES SAY"
- INTC (Intel Corporation) score 5.7 — "Intel’s $15 billion stock sale. Why shares fell despite AI boom"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.6 — "ICICI Bank Share Price Live Updates: ICICI Bank's Price Movement Indicates Positive Trend"
- GOOGL (Alphabet) score 3.5 — "US Stock Market: Berkshire steps up buybacks, boosts Alphabet stake as cash falls"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 3.2 — "Tata Consumer Share Price Live Updates: Tata Consumer's Current Market Position"
- PLTR (Palantir Technologies Inc.) score 3.1 — "Palantir’s stock stages best week since 2024 — showing it’s no longer an AI loser"
- AMZN (Amazon.com, Inc.) score 2.2 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- CUPID.NS (CUPID LIMITED) score 2.0 — "Q1 Results Highlights: BEML loss narrows to ₹27 cr, Eveready profit up 22%, Aditya Birla F"

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