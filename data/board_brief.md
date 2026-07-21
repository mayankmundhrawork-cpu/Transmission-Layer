# Transmission Layer — board brief · 2026-07-21 17:03Z

data as of **2026-07-21** · 98 series · 12 red / 39 amber · 8 events surfaced (35 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.401, 11d in regime; vol-pct 0.509, breadth-off 0.294, Markov P(high-vol) 0.047)
- [WEAK] **safe_haven_gold** — corr20 0.04, corr60 -0.44, contra nifty_50 corr20=0.13, last shift 2026-05-28. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.93, corr60 0.82, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.45, corr60 0.34, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.11, corr60 -0.0, last shift 2026-06-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.93, corr60 -0.81, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.08, corr60 -0.07, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.14, corr60 -0.28, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.26, corr60 0.25, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.0001446960878501713)
- **SETUP** dyn_vt → asx_200: leads 1d (ccf 0.578, β 0.4654, p 0.0); driver zc 1.56 → expected 0.587%. Type hit-rate 0.817 (n=3132).
- **SETUP** dyn_vt → dyn_453950_ks: leads 1d (ccf 0.552, β 1.1234, p 0.0); driver zc 1.56 → expected 1.416%. Type hit-rate 0.817 (n=3132).
- **SETUP** dyn_vt → nikkei_225: leads 1d (ccf 0.47, β 0.8367, p 0.0); driver zc 1.56 → expected 1.055%. Type hit-rate 0.817 (n=3132).
- **SETUP** dyn_vt → gbp_usd: leads 1d (ccf 0.342, β 0.1524, p 0.0); driver zc 1.56 → expected 0.192%. Type hit-rate 0.817 (n=3132).
- **SETUP** dyn_coin → asx_200: leads 1d (ccf 0.318, β 0.0512, p 0.0); driver zc 2.62 → expected 0.613%. Type hit-rate 0.817 (n=3132).
- **SETUP** dyn_vt → nifty_midcap_100: leads 1d (ccf 0.298, β 0.3659, p 0.0); driver zc 1.56 → expected 0.461%. Type hit-rate 0.817 (n=3132).
- **SETUP** dyn_vt → nifty_50: leads 1d (ccf 0.293, β 0.2624, p 0.0); driver zc 1.56 → expected 0.331%. Type hit-rate 0.817 (n=3132).
- **SETUP** dyn_vt → hang_seng: leads 1d (ccf 0.273, β 0.3911, p 0.0); driver zc 1.56 → expected 0.493%. Type hit-rate 0.817 (n=3132).
- Track record · residual_reversion: hit-rate **0.497** (n=1162) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=3132) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.722** (n=18) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.11] dyn_karurvysya_ns ↑
- dyn_karurvysya_ns [EQUITIES]: last 340.45, z20 7.11, zc 6.52, resid-z 6.59 [unexplained], 1d 13.11%, |z20|=7.11; 1y-pct=100
- **Mechanism**: The recent surge in Karur Vysya Bank's stock price can be attributed to its strong Q1 FY27 results, with a record profit of ₹756 crore and a net interest margin of 4.26%. This move is priced, given the bank's robust financial performance and the management's guidance on maintaining a net interest margin above 4% in Q2. The transmission candidates, such as dyn_indusindbk_bo and nifty_midcap_100, have already reacted to this news, indicating a priced move rather than an anomaly.
- **Gap**: No gap: the recent move in Karur Vysya Bank's stock price is largely explained by its strong Q1 FY27 results and the management's guidance, leaving no significant event-to-price gap.
- **India take**: The Indian instruments that express this move, such as dyn_indusindbk_bo and nifty_midcap_100, have already reacted to the news, while others like dyn_jiofin_bo and nifty_50 remain quiet. The transmission candidates with higher rho values, like dyn_havells_ns, have also reacted to the news.
- Watch next: dyn_indusindbk_bo (up) — already moved; reacted to Karur Vysya Bank's strong Q1 results
- Watch next: nifty_midcap_100 (up) — already moved; reacted to Karur Vysya Bank's strong Q1 results
- **India receivers**: dyn_indusindbk_bo (rho 0.54, z 1.99); nifty_midcap_100 (rho 0.494, z 1.36); dyn_jiofin_bo (rho 0.479, z 0.53); nifty_50 (rho 0.474, z 0.52)
- Source: Broker’s Call: Karur Vysya Bank (Buy) — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/brokers-call-karur-vysya-bank-buy/article71248725.ece
- Source: Karur Vysya Bank shares jump 13% after Q1 profit hits record ₹756 crore — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/karur-vysya-bank-shares-jump-96-after-q1-profit-hits-record-756-crore/article71248009.ece
- Source: Top Gainers & Losers on July 21: Karur Vysya Bank, TVS Motor, Zen Tech, Meesho, Thermax among top gainers today — Mint Markets, 2026-07-21. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-july-21-karur-vysya-bank-tvs-motor-zen-tech-meesho-thermax-among-top-gainers-today-11784625895681.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-02 (d=0.07), 2025-01-31 (d=0.09)

### [RED 8.22] commodities · 2 series ↑
- brent [COMMODITIES]: last 91.34, z20 2.39, zc 0.90, resid-z 0.97 [quiet], 1d 2.38%, 1-session move +2.38% ≥ 1.5%; |z20|=2.39; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 84.49, z20 2.30, zc 0.59, resid-z 0.70 [quiet], 1d 1.51%, 1-session move +1.51% ≥ 1.5%; |z20|=2.30
- **Mechanism**: The recent surge in oil prices, led by Brent and WTI, is driven by geopolitical risks and threats to maritime traffic, which are weighing on market sentiment and pushing prices higher. The channel status indicates that the metal_copper_channel and gold_silver_comove are valid, but the inr_oil_channel is weak, suggesting that the usual relationship between oil prices and the Indian rupee may not hold. The vix_equity_inverse channel is also valid, indicating a potential inverse relationship between volatility and equity markets.
- **Gap**: No gap: the big raw move in oil prices is largely priced, with resid_z values of 0.97 and 0.7 for Brent and WTI, respectively, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is the nifty_midcap_100, which has already reacted to the WTI price surge, while the nifty_50 remains quiet. The INR may not weaken significantly due to the weak inr_oil_channel.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to WTI price surge
- **India receivers**: nifty_midcap_100 (rho -0.615, z 1.36); nifty_50 (rho -0.463, z 0.52)
- Source: An oil lifeline is under threat, and markets have yet to price in the growing crisis — MarketWatch Top, 2026-07-21. https://www.marketwatch.com/story/an-oil-lifeline-is-under-threat-and-markets-have-yet-to-price-in-the-growing-crisis-801d53b1?mod=mw_rss_topstories
- Source: Oil climbs as traders weigh slew of risks from Hormuz to Red Sea — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/commodities/oil-climbs-as-traders-weigh-slew-of-risks-from-hormuz-to-red-sea/article71250746.ece
- Source: Houthi Threats Ignite New Oil Price Surge — OilPrice, 2026-07-21. https://oilprice.com/Energy/Crude-Oil/Houthi-Threats-Ignite-New-Oil-Price-Surge.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 6.49] cross-asset · 3 series ↑
- dyn_coin [EQUITIES]: last 179.64, z20 3.17, zc 2.62, resid-z 0.20 [priced], 1d 11.97%, |z20|=3.17
- btc_usd [CRYPTO]: last 66515.99, z20 1.98, zc 0.93, resid-z 0.69 [quiet], 1d 1.97%, |z20|=1.98
- eth_usd [CRYPTO]: last 1925.90, z20 1.55, zc 0.29, resid-z -0.02 [quiet], 1d 1.16%, |z20|=1.55
- **Mechanism**: The recent move in dyn_coin, btc_usd, and eth_usd is largely priced, with resid_z values indicating that the majority of the move can be explained by factor exposures. However, the correlated instruments such as sp500, dyn_vt, and nasdaq_100 have not moved in tandem, suggesting a potential transmission setup. The valid channels, including gold_silver_comove, metal_copper_channel, and vix_equity_inverse, do not directly explain the current move but indicate a neutral regime with potential for volatility.
- **Gap**: No gap: The move in dyn_coin, btc_usd, and eth_usd is largely priced, with small resid_z values indicating that the majority of the move can be explained by factor exposures.
- **India take**: The Indian instrument nifty_50 may react to the global market moves, potentially through the metal_copper_channel, but has not yet shown a significant reaction. The usd_inr may also be affected by the global market trends, but the inr_oil_channel is currently weak.
- Watch next: sp500 (up) — not yet - watch; Historical lead of 4d and rho=0.57 vs eth_usd
- Watch next: dyn_vt (up) — not yet - watch; Historical lead of 4d and rho=0.553 vs eth_usd
- Source: Global Markets: London Stock Exchange to launch round-the-clock trading next year — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/us-stocks/news/global-markets-london-stock-exchange-to-launch-round-the-clock-trading-next-year/articleshow/132538012.cms
- Source: TRUMP PREPARES NEW ROUND OF TARIFFS President Donald Trump is reportedly preparing a new round of tariffs on dozens of countries ahead of the expiration of the current 10% global tariff this week. According to the Financial Times, the administration is considering keeping the — DeItaone, 2026-07-21. https://t.me/walter_bloomberg/33828
- Source: Global Market: Euro zone banks tighten credit standards amid geopolitical risks, ECB survey shows — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-banks-tighten-credit-standards-amid-geopolitical-risks-ecb-survey-shows/articleshow/132532469.cms
- Historical analogues: 2025-08-11 (d=0.92), 2024-10-31 (d=1.15), 2026-05-05 (d=1.26)

### [AMBER 5.9] fx · 4 series ↑
- usd_brl [FX]: last 5.07, z20 -2.24, zc -1.40, resid-z -1.66 [unexplained], 1d -1.08%, |z20|=2.24
- aud_usd [FX]: last 0.70, z20 1.99, zc 0.88, resid-z 1.01 [quiet], 1d 0.45%, |z20|=1.99
- usd_mxn [FX]: last 17.39, z20 -1.51, zc -1.91, resid-z -2.12 [unexplained], 1d -0.88%, |z20|=1.51
- eur_usd [FX]: last 1.14, z20 0.03, zc -0.36, resid-z 0.02 [quiet], 1d -0.13%, 1y-pct=3
- **Mechanism**: The recent tightening of credit standards by Euro zone banks, as reported by the ECB's Bank Lending Survey, has led to a rise in Euro zone government bond yields, which in turn has caused a strengthening of the US dollar against certain currencies, including the Brazilian real and Mexican peso. This move is largely priced, with the residual z-scores indicating that the majority of the move can be explained by factor exposures.
- **Gap**: No gap: the move in usd_brl and usd_mxn is largely explained by their factor exposures, with residual z-scores of -1.66 and -2.12, respectively, indicating that the majority of the move is priced
- **India take**: The Indian instrument dyn_karurvysya_ns, which has a correlation of -0.369 with usd_mxn, has already reacted to the move. Other Indian metal equities may also be affected through the metal_copper_channel, which is a valid channel.
- Watch next: usd_brl (down) — already moved; tightening credit standards in Euro zone
- Watch next: usd_mxn (down) — already moved; strengthening US dollar
- **India receivers**: dyn_karurvysya_ns (rho -0.369, z 7.11)
- Source: Global Market: Euro zone banks tighten credit standards amid geopolitical risks, ECB survey shows — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-banks-tighten-credit-standards-amid-geopolitical-risks-ecb-survey-shows/articleshow/132532469.cms
- Source: Euro zone bond yields tick higher as oil remains elevated; eyes on ECB — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bond-yields-tick-higher-as-oil-remains-elevated-eyes-on-ecb/articleshow/132531792.cms
- Source: July 2026 euro area bank lending survey — ECB press, 2026-07-21. https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260721~44ee50f75c.en.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-19 (d=0.34), 2025-03-31 (d=0.34)

### [AMBER 4.88] cross-asset · 3 series ↑
- dyn_bond [EQUITIES]: last 90.93, z20 -1.56, zc -0.68, resid-z -0.49 [quiet], 1d -0.20%, 1y-pct=1
- tips_10y_real [RATES]: last 2.31, z20 0.76, zc -0.98, resid-z -2.43 [unexplained], 1d -1.70%, 1y-pct=97
- ust_2y [RATES]: last 4.18, z20 0.37, zc 0.37, resid-z -0.28 [quiet], 1d 0.48%, 1y-pct=96
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (inverse) — not yet - watch; rho -0.926 vs dyn_bond, historically leads by 1d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.671 vs dyn_bond, historically leads by 3d
- Watch next: ust_30y (inverse) — not yet - watch; rho -0.858 vs dyn_bond
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.557 vs dyn_bond, historically leads by 4d
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.515 vs tips_10y_real, historically leads by 4d
- Source: ICICI Bank eyes $500 million dollar bond issue via GIFT City — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/bonds/icici-bank-eyes-500-million-dollar-bond-issue-via-gift-city/articleshow/132538886.cms
- Source: Euro zone bond yields tick higher as oil remains elevated; eyes on ECB — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bond-yields-tick-higher-as-oil-remains-elevated-eyes-on-ecb/articleshow/132531792.cms
- Source: Japan bond jitters overshadow Takaichi's first economic policy roadmap — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/bonds/japan-bond-jitters-overshadow-takaichis-first-economic-policy-roadmap/articleshow/132530718.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.34), 2025-05-12 (d=0.56)

### [RED 4.77] dyn_nflx ↓
- dyn_nflx [EQUITIES]: last 66.87, z20 -2.77, zc -0.30, resid-z -2.77 [unexplained], 1d -1.08%, |z20|=2.77; 1y-pct=0
- **Mechanism**: The decline in dyn_nflx is unexplained by factor exposures, with a resid_z of -2.77, indicating a potential anomaly. The valid vix_equity_inverse channel suggests that the vol spike may lead to an equity drawdown. The metal_copper_channel also indicates a potential transmission to Indian metal equities.
- **Gap**: No gap: the big raw move in dyn_nflx has a small resid_z, but it is not an anomaly as the move is largely unexplained by factor exposures, suggesting it is priced
- **India take**: The Indian instrument that expresses this move is the nifty_50, which has not reacted yet. The metal_copper_channel suggests a potential transmission to Indian metal equities such as Hindalco or Tata Steel.
- Watch next: nifty_50 (down) — not yet - watch; Potential risk-off sentiment transmission
- Source: US stocks to buy for short term: From Nvidia to Netflix- Appreciate CEO suggests picking these 5 shares — Mint Markets, 2026-07-20. https://www.livemint.com/market/stock-market-news/us-stocks-to-buy-for-short-term-from-nvidia-to-netflix-appreciate-ceo-suggests-picking-these-5-shares-11784551408198.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-10 (d=0.03), 2025-04-01 (d=0.05)

### [RED 4.66] dyn_qessf ↓
- dyn_qessf [EQUITIES]: last 0.23, z20 -2.66, zc 0.60, resid-z 1.05 [quiet], 1d -8.09%, |z20|=2.66
- **Mechanism**: dyn_qessf ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_atherenerg_ns (rho -0.359 via dyn_qessf, z 1.41, reacted)
- **India receivers**: dyn_atherenerg_ns (rho -0.359, z 1.41)
- Source: Global Market: Private capital crucial to Europe's defence push as funding bottlenecks persist — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-private-capital-crucial-to-europes-defence-push-as-funding-bottlenecks-persist/articleshow/132528379.cms
- Source: West Asia conflict fuels defence stocks. Now comes the harder test — Mint Markets, 2026-07-20. https://www.livemint.com/market/stock-market-news/india-defence-stocks-rally-west-asia-conflict-next-leg-orders-or-execution-indigenization-procurement-11784518899336.html
- Source: HAL, BEL to Bharat Dynamics: Defence stocks dip after escalation in the US-Iran war — Mint Markets, 2026-07-20. https://www.livemint.com/market/stock-market-news/hal-bel-to-bharat-dynamics-defence-stocks-dip-after-escalation-in-the-us-iran-war-11784521448590.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-15 (d=0.32), 2024-11-14 (d=0.52)

### [RED 4.58] dyn_hdb ↓
- dyn_hdb [EQUITIES]: last 23.88, z20 -2.58, zc 0.77, resid-z 0.54 [quiet], 1d 1.17%, |z20|=2.58; 1y-pct=5
- **Mechanism**: dyn_hdb ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.653 via dyn_hdb, z 0.52, quiet); nifty_midcap_100 (rho 0.518 via dyn_hdb, z 1.36, reacted); dyn_indusindbk_bo (rho 0.497 via dyn_hdb, z 1.99, reacted); dyn_jiofin_bo (rho 0.462 via dyn_hdb, z 0.53, quiet)
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.653 vs dyn_hdb, historically leads by 1d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.532 vs dyn_hdb, historically leads by 1d
- Watch next: cac_40 (co-move) — not yet - watch; rho 0.621 vs dyn_hdb
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.597 vs dyn_hdb
- **India receivers**: nifty_50 (rho 0.653, z 0.52); nifty_midcap_100 (rho 0.518, z 1.36); dyn_indusindbk_bo (rho 0.497, z 1.99); dyn_jiofin_bo (rho 0.462, z 0.53)
- Source: HDFC Bank shares fall over 7 per cent in two days after Q1 earnings — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-fall-over-7-per-cent-in-two-days-after-q1-earnings/article71249104.ece
- Source: Sensex today | Stock Market Live: Sensex drops 250 pts, Nifty below 24,200; HDFC Bank lead losers — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-21st-may-2026/article71245381.ece
- Source: HDFC Bank shares fall for 2nd day but Jefferies, others brokerages remain bullish. Should you buy the dip? — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-bank-shares-fall-for-2nd-day-but-jefferies-others-brokerages-remain-bullish-should-you-buy-the-dip/articleshow/132528929.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

## Watchlist (below surfacing floor)
commodities · 3 series ↑ (4.48), dyn_havells_ns ↑ (4.47), dyn_hdbfs_bo ↓ (4.46), dyn_techm_ns ↑ (4.28), dyn_icicigi_bo ↓ (4.15), comex_copper ↑ (4.1), dyn_bac ↑ (3.62), nikkei_225 ↓ (3.52), natgas ↓ (3.51), dyn_ohi ↑ (3.4), usd_inr ↑ (3.11), usd_cny ↓ (3.04)

## India macro
- nifty_50: 24193.9492 (1d -0.18%, z20 0.52, flag none)
- nifty_midcap_100: 62976.5000 (1d 0.25%, z20 1.36, flag amber)
- usd_inr: 96.2250 (1d -0.06%, z20 1.11, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6030 (1d 0.44%, z20 0.94, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 79.4 — "Bandhan Bank Q1 profit jumps 35% as provisions decline sharply"
- INOXINDIA.NS (INOX INDIA LIMITED) score 70.7 — "India bonds fall as Middle East escalation drives oil above $90"
- HDB (HDFC Bank Limited) score 69.6 — "Bandhan Bank Q1 profit jumps 35% as provisions decline sharply"
- BAC (Bank of America Corporation) score 65.4 — "Bandhan Bank Q1 profit jumps 35% as provisions decline sharply"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 65.2 — "Bandhan Bank Q1 profit jumps 35% as provisions decline sharply"
- IDBI.NS (IDBI BANK LIMITED) score 55.7 — "Bandhan Bank Q1 profit jumps 35% as provisions decline sharply"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 48.1 — "Biotech IPO Gains Crush AI Listings With Standout 55% Return"
- COIN (Coinbase Global, Inc.) score 45.2 — "TRUMP PREPARES NEW ROUND OF TARIFFS President Donald Trump is reportedly preparing a new r"
- TECHM.NS (TECH MAHINDRA LIMITED) score 38.2 — "Biotech IPO Gains Crush AI Listings With Standout 55% Return"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 27.3 — "India bonds fall as Middle East escalation drives oil above $90"
- BOND (PIMCO Active Bond Exchange-Tra) score 24.3 — "India bonds fall as Middle East escalation drives oil above $90"
- OHI (Omega Healthcare Investors, In) score 23.5 — "Tesla earnings are on deck, and investors will be looking to settle this major debate"
- CHKP (Check Point Software Technolog) score 22.2 — "Metalic Technoforge IPO Day 1: Issue subscribed 28% so far. Check GMP, issue details"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.6 — "Adani Energy Solutions among 4 large-caps that hit 52-week highs & rallied up to 16% in a "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 16.2 — "Bandhan Bank Q1 profit jumps 35% as provisions decline sharply"
- VT (Vanguard Total World Stock Ind) score 15.8 — "India Became World's Top Long-Term LNG Buyer in 2025, GIIGNL Says"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 12.3 — "ICICI Bank eyes $500 million dollar bond issue via GIFT City"
- GS (Goldman Sachs Group, Inc. (The) score 11.0 — "Inflation is broadening out, says Goldman economist"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 11.0 — "Adani Energy Solutions among 4 large-caps that hit 52-week highs & rallied up to 16% in a "
- JIOFIN.BO (Jio Financial Services Limited) score 10.9 — "TRUMP PREPARES NEW ROUND OF TARIFFS President Donald Trump is reportedly preparing a new r"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 10.0 — "TRUMP PREPARES NEW ROUND OF TARIFFS President Donald Trump is reportedly preparing a new r"
- META (Meta) score 8.4 — "Metalic Technoforge IPO Day 1: Issue subscribed 28% so far. Check GMP, issue details"
- MS (Morgan Stanley) score 7.8 — "Bigger crash ahead? JPMorgan CEO Dimon says he won't buy stocks at current prices, says ma"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.5 — "Lumentum’s stock just got a lot more interesting — and Barclays has turned bullish"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 6.3 — "UK Scraps 5% VAT on Electricity"
- NVDA (NVIDIA Corporation) score 5.4 — "Nvidia among 6 megacaps that Morningstar says are undervalued. See full list"
- PCJEWELLER.NS (PC JEWELLER LTD) score 5.2 — "Bluestone Jewellery shares jump over 19% in biggest one-day gain since listing after Q1 re"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 5.2 — "Global Market: Private capital crucial to Europe's defence push as funding bottlenecks per"
- NFLX (Netflix, Inc.) score 4.7 — "US stocks to buy for short term: From Nvidia to Netflix- Appreciate CEO suggests picking t"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 4.6 — "Tata Technologies Q1 Results: Profit rises 6% to Rs 180 crore"
- SKHYV (SK hynix Inc. American Deposit) score 4.3 — "SKHY – SK HYNIX DOWN 0.7% IN PREMARKET SK Hynix shares are slipping 0.7% in premarket afte"
- BHEL.NS (BHEL) score 4.1 — "BHEL share price: Brokerages see up to 23% upside after Maharatna PSU posts first Q1 profi"
- WIT (Wipro Limited) score 3.9 — "Stocks to watch: Reliance Industries, Wipro, CEAT among shares in focus today; check list "
- AAPL (Apple Inc.) score 3.9 — "Dollar wavers as markets grapple with Gulf tensions"
- PYPL (PayPal Holdings, Inc.) score 2.9 — "How PayPal went from Wall Street favorite to unwilling merger target"
- CEATLTD.NS (CEAT LIMITED) score 2.2 — "Top Gainers & Losers on 20 July: Axis Bank, HDFC Bank, Ceat, India Cements, OLA, HFCL amon"
- KO (Coca-Cola Company (The)) score 1.6 — "Coca-Cola names JPMorgan, Citi as bankers for India bottling unit IPO"
- BIOCON.BO (BIOCON LTD.) score 0.9 — "Mylan exits Biocon, sells entire 5.64% stake for ₹3,679 crore via block deals"
- CUPID.NS (CUPID LIMITED) score 0.6 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"
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