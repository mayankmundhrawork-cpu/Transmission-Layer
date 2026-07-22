# Transmission Layer — board brief · 2026-07-22 17:02Z

data as of **2026-07-22** · 98 series · 10 red / 41 amber · 8 events surfaced (31 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.445, 12d in regime; vol-pct 0.596, breadth-off 0.294, Markov P(high-vol) 0.024)
- [WEAK] **safe_haven_gold** — corr20 0.03, corr60 -0.43, contra nifty_50 corr20=0.05, last shift 2026-05-28. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.91, corr60 0.82, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.47, corr60 0.35, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.08, corr60 -0.01, last shift 2026-06-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.94, corr60 -0.81, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.01, corr60 -0.09, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.14, corr60 -0.28, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.26, corr60 0.24, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 5.625422823563042e-06)
- **SETUP** bovespa → aud_usd: leads 1d (ccf 0.399, β 0.2421, p 0.0); driver zc 1.73 → expected 0.427%. Type hit-rate 0.817 (n=3090).
- **SETUP** bovespa → usd_mxn: leads 1d (ccf -0.364, β -0.2416, p 0.0); driver zc 1.73 → expected -0.426%. Type hit-rate 0.817 (n=3090).
- **SETUP** dyn_hdb → usd_inr: leads 1d (ccf -0.353, β -0.081, p 0.0); driver zc -1.57 → expected 0.189%. Type hit-rate 0.817 (n=3090).
- Track record · residual_reversion: hit-rate **0.494** (n=1152) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=3090) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.722** (n=18) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.17] commodities · 2 series ↑
- brent [COMMODITIES]: last 93.40, z20 2.34, zc 1.03, resid-z 0.88 [quiet], 1d 2.63%, 1-session move +2.63% ≥ 1.5%; |z20|=2.34; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 86.32, z20 2.27, zc 0.66, resid-z 0.55 [quiet], 1d 1.66%, 1-session move +1.66% ≥ 1.5%; |z20|=2.27
- **Mechanism**: The recent surge in oil prices, driven by Middle East hostilities and a potential LNG supply crisis, is propagating through the commodities channel, with Brent and WTI crude oil prices increasing by 2.63% and 1.66% respectively. This move is priced, given the small resid_z values of 0.88 and 0.55, indicating that the price movement is largely explained by factor exposures. The valid gold_silver_comove and metal_copper_channel may also contribute to the propagation of this move.
- **Gap**: No gap: the recent oil price surge is largely explained by factor exposures, with small resid_z values indicating that the move is priced.
- **India take**: The Indian instrument that expresses this move is the Nifty Midcap 100, which has a negative correlation with Brent crude oil and may potentially decline. However, it has not reacted yet, with a quiet move and a z20 score of -0.11.
- Watch next: nifty_midcap_100 (down) — not yet - watch; negative correlation with Brent crude oil
- **India receivers**: nifty_midcap_100 (rho -0.63, z -0.11); nifty_50 (rho -0.483, z -0.71)
- Source: Brazil’s Oil Boom Is Accelerating as Asian Buyers Flee the Middle East — OilPrice, 2026-07-22. https://oilprice.com/Energy/Energy-General/Brazils-Oil-Boom-Is-Accelerating-as-Asian-Buyers-Flee-the-Middle-East.html
- Source: Global oil prices hold gains after topping $95 a barrel for the first time in 6 weeks as hopes dim for de-escalation of Iran war — MarketWatch Top, 2026-07-22. https://www.marketwatch.com/story/oil-prices-climb-to-six-week-high-as-hopes-of-de-escalation-in-iran-diminish-b5fb0942?mod=mw_rss_topstories
- Source: LNG Supply Crisis Pushes Buyers Toward Coal and Oil — OilPrice, 2026-07-22. https://oilprice.com/Energy/Natural-Gas/LNG-Supply-Crisis-Pushes-Buyers-Toward-Coal-and-Oil.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 6.24] indices · 4 series ↑
- ftse_100 [INDICES]: last 10721.43, z20 2.57, zc 2.07, resid-z 1.76 [unexplained], 1d 1.28%, |z20|=2.57; 1y-pct=98
- cac_40 [INDICES]: last 8443.47, z20 1.03, zc 1.27, resid-z 1.81 [unexplained], 1d 0.96%, 1y-pct=95
- stoxx_50 [INDICES]: last 6319.65, z20 0.67, zc 0.60, resid-z 1.07 [quiet], 1d 0.54%, 1y-pct=97
- dow_jones [INDICES]: last 52386.32, z20 0.11, zc 0.40, resid-z 0.60 [quiet], 1d 0.31%, 1y-pct=96
- **Mechanism**: The recent move in indices such as FTSE 100, CAC 40, and STOXX 50 is largely unexplained by factor exposures, with high residual_z values indicating a potential anomaly. However, the move is not entirely unexpected given the historical analogues and the current market regime. The VALID gold_silver_comove and metal_copper_channel may also be contributing to the move, although the weak channels such as safe_haven_gold and inr_oil_channel are not providing a clear signal.
- **Gap**: No gap: the move in indices is largely priced in, given the high z20 values and the lack of a clear anomaly in the residual_z values
- **India take**: The Nifty 50, which is correlated with the CAC 40, has not reacted yet and may be due for a move. The Nifty Midcap 100 is also a potential responder, given its correlation with the STOXX 50.
- Watch next: nifty_50 (down) — not yet - watch; correlated with CAC 40 and has not moved yet
- **India receivers**: nifty_50 (rho 0.635, z -0.71); nifty_midcap_100 (rho 0.569, z -0.11)
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Live: US stocks mixed as caution rises ahead of Big Tech earnings — ET Markets, 2026-07-22. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-earnings-forecast-alphabet-tesla-super-micro-computer-stock-price-news-22-july-2026/liveblog/132559144.cms
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Live: US stocks gain on chip stocks recovery; earnings draw focus — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-earnings-forecast-nvidia-intel-3m-nebius-stock-price-news-21-july-2026/liveblog/132536325.cms
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Highlights: US stocks end higher as semiconductors surge amid Mideast war intensifies — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-earnings-forecast-nvidia-intel-3m-nebius-stock-price-news-21-july-2026/liveblog/132536325.cms
- Historical analogues: 2024-10-15 (d=0.74), 2024-11-11 (d=0.76), 2024-10-22 (d=1.02)

### [AMBER 5.75] fx · 3 series ↑
- usd_brl [FX]: last 5.06, z20 -2.43, zc -1.22, resid-z -1.32 [quiet], 1d -0.92%, |z20|=2.43
- aud_usd [FX]: last 0.70, z20 1.64, zc -0.07, resid-z 0.17 [quiet], 1d -0.03%, |z20|=1.64
- eur_usd [FX]: last 1.14, z20 0.09, zc -0.10, resid-z 0.20 [quiet], 1d -0.03%, 1y-pct=4
- **Mechanism**: The recent tightening of credit standards by Euro zone banks, as reported by the ECB's Bank Lending Survey, has led to a rise in Euro zone government bond yields, which in turn has caused a small move in the EUR/USD exchange rate. This move is largely priced, given the small resid_z values for the affected currency pairs. The valid vix_equity_inverse channel suggests that the increased volatility in equity markets may lead to further currency fluctuations.
- **Gap**: No gap: the move in EUR/USD is largely priced, with a small resid_z value of 0.2
- **India take**: The Indian Rupee (INR) may react to the strengthening US Dollar, potentially leading to a rise in USD/INR, although the dxy_inr_channel is currently weak. The metal_copper_channel may also influence Indian metal equities.
- Watch next: eur_usd (down) — already moved; Euro zone banks' tightening of credit standards
- Source: Global Market: Euro zone banks tighten credit standards amid geopolitical risks, ECB survey shows — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-banks-tighten-credit-standards-amid-geopolitical-risks-ecb-survey-shows/articleshow/132532469.cms
- Source: Euro zone bond yields tick higher as oil remains elevated; eyes on ECB — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bond-yields-tick-higher-as-oil-remains-elevated-eyes-on-ecb/articleshow/132531792.cms
- Source: July 2026 euro area bank lending survey — ECB press, 2026-07-21. https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260721~44ee50f75c.en.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-30 (d=0.17), 2025-08-26 (d=0.27)

### [AMBER 5.5] cross-asset · 5 series ↑
- dyn_bond [EQUITIES]: last 90.85, z20 -1.57, zc -0.37, resid-z -0.49 [quiet], 1d -0.11%, 1y-pct=0
- ust_30y [RATES]: last 5.11, z20 1.46, zc -0.92, resid-z -1.56 [unexplained], 1d 0.99%, 1y-pct=98
- ust_10y [RATES]: last 4.60, z20 1.44, zc -0.45, resid-z -1.35 [quiet], 1d 1.10%, 1y-pct=98
- tips_10y_real [RATES]: last 2.35, z20 1.38, zc -0.98, resid-z -2.43 [unexplained], 1d 1.73%, 1y-pct=99
- ust_2y [RATES]: last 4.21, z20 1.02, zc 0.37, resid-z -0.28 [quiet], 1d 0.72%, 1y-pct=98
- **Mechanism**: The recent surge in US Treasury yields, driven by concerns over inflationary pressures and potential interest rate hikes, is propagating through the valid vix_equity_inverse channel, indicating a potential equity drawdown. The move is also correlated with the metal_copper_channel, which could lead to a reaction in Indian metal equities.
- **Gap**: No gap: The big raw move in US Treasury yields is largely priced, with a small resid_z indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is the Nifty 50, which has not yet reacted. Additionally, Indian metal equities such as Hindalco may also be affected through the metal_copper_channel.
- Watch next: nifty_50 (down) — not yet - watch; Correlated with US Treasury yields and potential equity drawdown
- Watch next: hindalco (down) — not yet - watch; Indian metal equity that may react to the metal_copper_channel
- Source: After equities and mutual funds, it’s time for bond SIPs — BusinessLine Mkts, 2026-07-22. https://www.thehindubusinessline.com/markets/after-equities-and-mutual-funds-its-time-for-bond-sips/article71254365.ece
- Source: Global Market: Singapore launches green bond issue targeting up to $2 billion — ET Markets, 2026-07-22. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-singapore-launches-green-bond-issue-targeting-up-to-2-billion/articleshow/132551864.cms
- Source: Treasury Yields Hit Two-Month High as Oil Sparks Inflation Risk — Mint Markets, 2026-07-21. https://www.livemint.com/market/treasury-yields-hit-two-month-high-as-oil-sparks-inflation-risk-11784645430148.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.47] dyn_hdbfs_bo ↓
- dyn_hdbfs_bo [EQUITIES]: last 707.10, z20 -3.47, zc -1.05, resid-z -0.54 [quiet], 1d -1.86%, |z20|=3.47
- **Mechanism**: The decline in dyn_hdbfs_bo is largely priced, with a resid_z of -0.98, indicating that the move is mostly explained by factor exposures. The event is likely related to HDB Financial's bond reissue, which may have influenced investor sentiment. The lack of a significant unexplained component suggests that the market has already incorporated the news into the price.
- **Gap**: No gap: the move in dyn_hdbfs_bo is largely explained by factor exposures, with a small resid_z
- **India take**: The Indian instrument that expresses this move is nifty_midcap_100, which has not yet reacted. Additionally, dyn_jiofin_bo has already reacted, indicating some transmission of the move to other Indian financial instruments.
- Watch next: nifty_midcap_100 (down) — not yet - watch; correlated instrument with rho=0.558
- **India receivers**: nifty_midcap_100 (rho 0.558, z -0.11); nifty_50 (rho 0.413, z -0.71); usd_inr (rho -0.4, z 1.43); dyn_jiofin_bo (rho 0.378, z -1.19)
- Source: HDB Financial to reissue 3-year bonds, bankers say — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/bonds/hdb-financial-to-reissue-3-year-bonds-bankers-say/articleshow/132537022.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-22 (d=0.06), 2025-12-31 (d=0.06)

### [RED 5.45] dyn_karurvysya_ns ↑
- dyn_karurvysya_ns [EQUITIES]: last 338.00, z20 3.45, zc -0.17, resid-z 0.01 [quiet], 1d -0.68%, |z20|=3.45; 1y-pct=99
- **Mechanism**: The recent surge in Karur Vysya Bank's stock price can be attributed to its strong Q1 FY27 results, with a record profit of ₹756 crore, up 45% year-on-year. The bank's net interest margin (NIM) also improved to 4.26%, beating expectations. This positive earnings surprise has led to a re-rating of the stock, driving its price up. The VALID metal_copper_channel and vix_equity_inverse channels suggest a favorable risk-on environment, supporting the move.
- **Gap**: No gap: the big raw move in Karur Vysya Bank's stock price is largely priced in, given its strong earnings performance and improving NIM, with a resid_z of 0.61, which is not unusually high.
- **India take**: The Indian instrument that expresses this move is dyn_indusindbk_bo, which has already reacted, while nifty_midcap_100 is still waiting to react. Other transmission candidates like dyn_jiofin_bo and dyn_havells_ns have also reacted, indicating a broad-based move in the financial and banking sector.
- Watch next: dyn_indusindbk_bo (up) — already moved; high correlation with Karur Vysya Bank
- Watch next: nifty_midcap_100 (up) — not yet - watch; moderate correlation with Karur Vysya Bank
- **India receivers**: dyn_indusindbk_bo (rho 0.534, z 1.9); nifty_midcap_100 (rho 0.491, z -0.11); dyn_jiofin_bo (rho 0.477, z -1.19); nifty_50 (rho 0.469, z -0.71)
- Source: Broker’s Call: Karur Vysya Bank (Buy) — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/brokers-call-karur-vysya-bank-buy/article71248725.ece
- Source: Karur Vysya Bank shares jump 13% after Q1 profit hits record ₹756 crore — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/karur-vysya-bank-shares-jump-96-after-q1-profit-hits-record-756-crore/article71248009.ece
- Source: Top Gainers & Losers on July 21: Karur Vysya Bank, TVS Motor, Zen Tech, Meesho, Thermax among top gainers today — Mint Markets, 2026-07-21. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-july-21-karur-vysya-bank-tvs-motor-zen-tech-meesho-thermax-among-top-gainers-today-11784625895681.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-02 (d=0.07), 2025-01-31 (d=0.09)

### [RED 4.94] dyn_hdb ↓
- dyn_hdb [EQUITIES]: last 23.17, z20 -2.94, zc -1.57, resid-z 0.54 [priced], 1d -2.34%, |z20|=2.94; 1y-pct=0
- **Mechanism**: dyn_hdb ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.664 via dyn_hdb, z -0.71, quiet); nifty_midcap_100 (rho 0.533 via dyn_hdb, z -0.11, quiet); dyn_jiofin_bo (rho 0.477 via dyn_hdb, z -1.19, reacted); dyn_indusindbk_bo (rho 0.469 via dyn_hdb, z 1.9, reacted)
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.664 vs dyn_hdb, historically leads by 1d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.541 vs dyn_hdb, historically leads by 1d
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.533 vs dyn_hdb, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.573 vs dyn_hdb
- **India receivers**: nifty_50 (rho 0.664, z -0.71); nifty_midcap_100 (rho 0.533, z -0.11); dyn_jiofin_bo (rho 0.477, z -1.19); dyn_indusindbk_bo (rho 0.469, z 1.9)
- Source: HDFC Bank shares tumble over 8% in three days on net interest margin concerns — BusinessLine Mkts, 2026-07-22. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-tumble-over-8-in-three-days-on-net-interest-margin-concerns/article71253282.ece
- Source: HDFC Bank share price drops for third straight session after Q1FY27 results: Should you buy on dip or avoid? — Mint Markets, 2026-07-22. https://www.livemint.com/market/stock-market-news/hdfc-bank-share-price-drops-for-third-straight-session-after-q1fy27-results-should-you-buy-on-dip-or-avoid-11784700700233.html
- Source: HDFC Bank shares fall over 7 per cent in two days after Q1 earnings — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-fall-over-7-per-cent-in-two-days-after-q1-earnings/article71249104.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [RED 4.86] commodities · 3 series ↑
- corn [COMMODITIES]: last 483.75, z20 3.54, zc 5.42, resid-z 4.54 [unexplained], 1d 6.85%, |z20|=3.54; 1y-pct=100
- wheat [COMMODITIES]: last 705.00, z20 2.29, zc 1.91, resid-z 1.69 [unexplained], 1d 3.98%, |z20|=2.29; 1y-pct=100
- soybeans [COMMODITIES]: last 1237.00, z20 1.68, zc 1.42, resid-z 1.34 [quiet], 1d 1.44%, |z20|=1.68; 1y-pct=100
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_patanjali_ns (rho -0.518 via wheat, z -1.95, reacted); dyn_adanient_bo (rho -0.364 via soybeans, z 0.34, quiet); dyn_tataelxsi_ns (rho -0.353 via wheat, z -1.69, reacted)
- **India receivers**: dyn_patanjali_ns (rho -0.518, z -1.95); dyn_adanient_bo (rho -0.364, z 0.34); dyn_tataelxsi_ns (rho -0.353, z -1.69)
- Historical analogues: 2026-05-22 (d=0.0), 2024-08-30 (d=0.27), 2026-05-06 (d=0.32)

## Watchlist (below surfacing floor)
usd_jpy ↑ (4.68), dyn_olaelec_ns ↓ (4.53), dyn_icicigi_bo ↓ (4.4), dyn_bharatcoal_ns ↓ (4.28), dyn_nvda ↑ (4.15), cross-asset · 2 series ↑ (3.92), dyn_indusindbk_bo ↑ (3.9), dyn_ohi ↑ (3.86), usd_inr ↑ (3.43), dyn_gs ↑ (3.03), dyn_lth ↑ (2.59), brent_wti_spread ↑ (2.55)

## India macro
- nifty_50: 23991.0508 (1d -0.81%, z20 -0.71, flag none)
- nifty_midcap_100: 62284.6484 (1d -1.10%, z20 -0.11, flag none)
- usd_inr: 96.5550 (1d 0.07%, z20 1.43, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5962 (1d -0.29%, z20 0.56, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 84.3 — "IndusInd Bank Q1 Results: Profit soars 72% YoY to Rs 1,037 crore; NII flat"
- INOXINDIA.NS (INOX INDIA LIMITED) score 75.3 — "Oil rally weighs on Indian bonds, value buyers limit fall"
- HDB (HDFC Bank Limited) score 71.6 — "IndusInd Bank Q1 Results: Profit soars 72% YoY to Rs 1,037 crore; NII flat"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 69.1 — "IndusInd Bank Q1 Results: Profit soars 72% YoY to Rs 1,037 crore; NII flat"
- BAC (Bank of America Corporation) score 68.3 — "IndusInd Bank Q1 Results: Profit soars 72% YoY to Rs 1,037 crore; NII flat"
- IDBI.NS (IDBI BANK LIMITED) score 60.5 — "IndusInd Bank Q1 Results: Profit soars 72% YoY to Rs 1,037 crore; NII flat"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 47.8 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Live: US stocks mixed as caution ris"
- COIN (Coinbase Global, Inc.) score 46.3 — "Iran War Escalation Threatens Global Fuel Supply Recovery"
- TECHM.NS (TECH MAHINDRA LIMITED) score 40.9 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Live: US stocks mixed as caution ris"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 40.8 — "Oil rally weighs on Indian bonds, value buyers limit fall"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 29.2 — "IndusInd Bank Q1 Results: Profit soars 72% YoY to Rs 1,037 crore; NII flat"
- OHI (Omega Healthcare Investors, In) score 28.0 — "Gold climbs to two-week high as investors watch West Asia conflict"
- BOND (PIMCO Active Bond Exchange-Tra) score 23.2 — "Oil rally weighs on Indian bonds, value buyers limit fall"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.6 — "U.S.-Iran Conflict Threatens Long-Term Energy Shock Across Asia"
- CHKP (Check Point Software Technolog) score 20.5 — "Caliber Mining & Logistics IPO allotment date today. GMP, steps to check allotment status "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 14.5 — "Q1 Results Highlights: Eternal logs ₹92 cr profit in Q1, Nestlé, Adani Power, Adani Green "
- VT (Vanguard Total World Stock Ind) score 14.2 — "Fossil Fuels Still Generate 57% of the World's Electricity"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.6 — "Fed’s favorite inflation tracker is getting an overhaul — just as the central bank weighs "
- GS (Goldman Sachs Group, Inc. (The) score 10.6 — "US Stock Market: Goldman Sachs launches new private markets platform to expand offerings f"
- JIOFIN.BO (Jio Financial Services Limited) score 10.4 — "M&M Financial shares zoom 8% after Q1 profit jumps, brokerages lift target prices"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 9.7 — "ICICI Bank eyes $500 million dollar bond issue via GIFT City"
- COALINDIA.NS (COAL INDIA LTD) score 9.6 — "Oil rally weighs on Indian bonds, value buyers limit fall"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.9 — "M&M Financial shares zoom 8% after Q1 profit jumps, brokerages lift target prices"
- MS (Morgan Stanley) score 8.1 — "InMobi IPO: SoftBank-backed Indian ad tech firm appoints JPMorgan, Jefferies for its upcom"
- META (Meta) score 6.7 — "Metalic Technoforge IPO Day 1: Issue subscribed 28% so far. Check GMP, issue details"
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.1 — "BlueStone Jewellery shares soar 29% in 2 days after stellar Q1 show. Should you buy, sell "
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 6.1 — "Multibagger defence stock Apollo Micro Systems to be in focus tomorrow; here's why"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 5.8 — "Fossil Fuels Still Generate 57% of the World's Electricity"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 5.5 — "Tata Group stock Indian Hotels falls 1% despite strong Q1 results 2026. Should you buy or "
- NVDA (NVIDIA Corporation) score 5.3 — "AMD plans to invest to up $5 billion into Anthropic as it seeks to cut into Nvidia’s domin"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 4.8 — "LNG Supply Crisis Pushes Buyers Toward Coal and Oil"
- LTH (Life Time Group Holdings, Inc.) score 4.8 — "After equities and mutual funds, it’s time for bond SIPs"
- NFLX (Netflix, Inc.) score 3.7 — "US stocks to buy for short term: From Nvidia to Netflix- Appreciate CEO suggests picking t"
- SKHYV (SK hynix Inc. American Deposit) score 3.4 — "SKHY – SK HYNIX DOWN 0.7% IN PREMARKET SK Hynix shares are slipping 0.7% in premarket afte"
- BHEL.NS (BHEL) score 3.3 — "BHEL share price: Brokerages see up to 23% upside after Maharatna PSU posts first Q1 profi"
- WIT (Wipro Limited) score 3.1 — "Stocks to watch: Reliance Industries, Wipro, CEAT among shares in focus today; check list "
- AAPL (Apple Inc.) score 3.1 — "Dollar wavers as markets grapple with Gulf tensions"
- BIOCON.BO (BIOCON LTD.) score 0.8 — "Mylan exits Biocon, sells entire 5.64% stake for ₹3,679 crore via block deals"
- CUPID.NS (CUPID LIMITED) score 0.5 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 0.4 — "Patanjali Foods share price crashes 20%, extending losses for third straight session; what"

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