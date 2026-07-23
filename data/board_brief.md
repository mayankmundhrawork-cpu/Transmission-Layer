# Transmission Layer — board brief · 2026-07-23 17:06Z

data as of **2026-07-23** · 98 series · 10 red / 38 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.672, 1d in regime; vol-pct 0.756, breadth-off 0.588, Markov P(high-vol) 0.096)
- [WEAK] **safe_haven_gold** — corr20 -0.18, corr60 -0.46, contra nifty_50 corr20=0.09, last shift 2026-05-29. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.82, last shift 2026-05-14. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.5, corr60 0.34, last shift 2026-05-13. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.05, corr60 -0.03, last shift 2026-06-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.82, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.05, corr60 -0.09, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.24, corr60 -0.27, last shift 2026-05-14. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.33, corr60 0.24, last shift 2026-04-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 90** scanned series survive multiplicity control (effective p ≤ 0.0001446960878501713)
- **SETUP** sp500 → asx_200: leads 1d (ccf 0.573, β 0.4439, p 0.0); driver zc -1.59 → expected -0.551%. Type hit-rate 0.82 (n=3066).
- **SETUP** sp500 → taiwan_weighted: leads 1d (ccf 0.516, β 0.8138, p 0.0); driver zc -1.59 → expected -1.01%. Type hit-rate 0.82 (n=3066).
- **SETUP** vix → asx_200: leads 1d (ccf -0.487, β -0.0415, p 0.0); driver zc 2.1 → expected -0.706%. Type hit-rate 0.82 (n=3066).
- **SETUP** sp500 → nikkei_225: leads 1d (ccf 0.466, β 0.7916, p 0.0); driver zc -1.59 → expected -0.983%. Type hit-rate 0.82 (n=3066).
- **SETUP** sp500 → usd_brl: leads 1d (ccf -0.444, β -0.3473, p 0.0); driver zc -1.59 → expected 0.431%. Type hit-rate 0.82 (n=3066).
- **SETUP** vix → taiwan_weighted: leads 1d (ccf -0.413, β -0.0704, p 5e-05); driver zc 2.1 → expected -1.197%. Type hit-rate 0.82 (n=3066).
- **SETUP** vix → usd_brl: leads 1d (ccf 0.408, β 0.0347, p 0.0); driver zc 2.1 → expected 0.589%. Type hit-rate 0.82 (n=3066).
- **SETUP** sp500 → kospi: leads 1d (ccf 0.366, β 0.7437, p 0.0); driver zc -1.59 → expected -0.923%. Type hit-rate 0.82 (n=3066).
- **SETUP** vix → nikkei_225: leads 1d (ccf -0.366, β -0.0677, p 0.00659); driver zc 2.1 → expected -1.151%. Type hit-rate 0.82 (n=3066).
- **SETUP** vix → kospi: leads 1d (ccf -0.336, β -0.0744, p 1e-05); driver zc 2.1 → expected -1.265%. Type hit-rate 0.82 (n=3066).
- **SETUP** vix → india_vix: leads 1d (ccf 0.323, β 0.2078, p 0.01124); driver zc 2.1 → expected 3.533%. Type hit-rate 0.82 (n=3066).
- **SETUP** dax → asx_200: leads 1d (ccf 0.283, β 0.2095, p 0.00193); driver zc -2.12 → expected -0.372%. Type hit-rate 0.82 (n=3066).
- **SETUP** stoxx_50 → asx_200: leads 1d (ccf 0.262, β 0.1958, p 0.00678); driver zc -2.16 → expected -0.37%. Type hit-rate 0.82 (n=3066).
- Track record · residual_reversion: hit-rate **0.492** (n=1167) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.82** (n=3066) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.722** (n=18) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.07] cross-asset · 11 series ↓
- nasdaq_100 [INDICES]: last 28442.54, z20 -2.27, zc -1.39, resid-z 0.46 [quiet], 1d -1.92%, |z20|=2.27
- vix [INDICES]: last 19.47, z20 2.19, zc 2.10, resid-z n/a [moved], 1d 17.01%, 1-session move +17.01% ≥ 15.0%; |z20|=2.19
- russell_2000 [INDICES]: last 2935.05, z20 -2.17, zc -0.68, resid-z 1.36 [quiet], 1d -0.84%, |z20|=2.17
- dyn_bond [EQUITIES]: last 90.44, z20 -2.10, zc -1.07, resid-z -0.11 [quiet], 1d -0.31%, |z20|=2.10; 1y-pct=0
- ust_2y [RATES]: last 4.26, z20 2.01, zc 0.92, resid-z 1.09 [quiet], 1d 1.19%, |z20|=2.01; 1y-pct=99
- dow_jones [INDICES]: last 51737.63, z20 -1.82, zc -1.26, resid-z 0.60 [quiet], 1d -0.92%, |z20|=1.82
- cac_40 [INDICES]: last 8280.76, z20 -1.76, zc -2.25, resid-z -0.67 [priced], 1d -1.86%, |z20|=1.76
- ust_10y [RATES]: last 4.63, z20 1.71, zc 0.67, resid-z 0.94 [quiet], 1d 0.65%, |z20|=1.71; 1y-pct=99
- stoxx_50 [INDICES]: last 6197.62, z20 -1.64, zc -2.16, resid-z -0.59 [priced], 1d -1.89%, |z20|=1.64
- tips_10y_real [RATES]: last 2.37, z20 1.58, zc 0.49, resid-z 0.64 [quiet], 1d 0.85%, |z20|=1.58; 1y-pct=100
- ust_30y [RATES]: last 5.13, z20 1.54, zc 0.61, resid-z 0.79 [quiet], 1d 0.39%, |z20|=1.54; 1y-pct=99
- **Mechanism**: The current market move is driven by a cross-asset decline, with 11 series showing a downward trend, led by the Nasdaq 100 and Russell 2000. The VIX has spiked, indicating increased volatility. The move is largely priced, with most series showing a low resid_z, indicating that the move is explained by factor exposures.
- **Gap**: No gap: the current market move is largely priced, with most series showing a low resid_z, indicating that the move is explained by factor exposures.
- **India take**: The Indian market has already reacted to the global market decline, with the Nifty 50 and Nifty Midcap 100 showing a downward trend. The India VIX has also shown an increase in volatility.
- Watch next: nifty_50 (down) — already moved; reacted to global market decline
- Watch next: nifty_midcap_100 (down) — already moved; reacted to global market decline
- **India receivers**: nifty_50 (rho 0.639, z -1.55); nifty_midcap_100 (rho 0.586, z -1.35)
- Source: Nasdaq tops profit estimates on high-profile listings, robust data revenue — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/us-stocks/news/nasdaq-tops-profit-estimates-on-high-profile-listings-robust-data-revenue/articleshow/132585994.cms
- Source: Kuwait raises $6 billion in three-tranche bond sale, finance ministry says — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/bonds/kuwait-raises-6-billion-in-three-tranche-bond-sale-finance-ministry-says/articleshow/132581123.cms
- Source: Malaysia launches dollar Islamic bond for infra and government projects, term sheet shows — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/bonds/malaysia-launches-dollar-islamic-bond-for-infra-and-government-projects-term-sheet-shows/articleshow/132580993.cms
- Historical analogues: 2024-10-11 (d=0.94), 2025-10-06 (d=1.24), 2024-10-02 (d=1.31)

### [RED 8.8] commodities · 2 series ↑
- brent [COMMODITIES]: last 100.74, z20 2.97, zc 2.64, resid-z 1.67 [unexplained], 1d 7.09%, 1-session move +7.09% ≥ 1.5%; |z20|=2.97; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 92.35, z20 2.91, zc 2.56, resid-z 1.38 [moved], 1d 6.36%, 1-session move +6.36% ≥ 1.5%; |z20|=2.91
- **Mechanism**: The recent surge in Brent and WTI crude oil prices is driven by supply concerns due to escalating attacks on commercial shipping in the Red Sea, which has led to a risk-off sentiment in the market. This sentiment is further reinforced by the lack of discounts on Russian crude oil for September deliveries, indicating a potential supply crunch. The valid gold_silver_comove and metal_copper_channel suggest that monetary metals and copper are co-moving, which may lead to further price increases in these commodities.
- **Gap**: No gap: the big raw move in Brent and WTI crude oil prices is largely priced, with resid_z values of 1.67 and 1.38, respectively, indicating that the price movement is largely explained by factor exposures.
- **India take**: The Indian instruments such as nifty_midcap_100, nifty_50, and dyn_hdbfs_bo have already reacted to the surge in crude oil prices, with negative correlations to brent crude. The dyn_indusindbk_bo has not yet reacted and is worth watching.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to brent crude price increase
- Watch next: nifty_50 (down) — already moved; reacted to brent crude price increase
- Watch next: dyn_hdbfs_bo (down) — already moved; reacted to brent crude price increase
- **India receivers**: nifty_midcap_100 (rho -0.663, z -1.35); nifty_50 (rho -0.505, z -1.55); dyn_hdbfs_bo (rho -0.494, z -3.95); dyn_indusindbk_bo (rho -0.493, z 0.31)
- Source: Global oil tops $100 after Houthis strike Saudi tankers and Trump threatens ‘military punishment’ on Iran — MarketWatch Top, 2026-07-23. https://www.marketwatch.com/story/oil-nears-100-a-barrel-after-houthis-claim-strikes-on-saudi-arabian-tankers-4d9949c2?mod=mw_rss_topstories
- Source: Brent Tops $100 as Houthi Attacks Push Oil Rally Into Triple Digits — OilPrice, 2026-07-23. https://oilprice.com/Energy/Oil-Prices/Brent-Tops-100-as-Houthi-Attacks-Push-Oil-Rally-Into-Triple-Digits.html
- Source: No discounts on Russian crude for September deliveries: BPCL — BusinessLine Mkts, 2026-07-23. https://www.thehindubusinessline.com/markets/commodities/no-discounts-on-russian-crude-for-september-deliveries-bpcl/article71258631.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 7.41] dyn_qessf ↓
- dyn_qessf [EQUITIES]: last 0.17, z20 -5.41, zc -3.99, resid-z 0.41 [moved], 1d -25.39%, |z20|=5.41
- **Mechanism**: The decline in dyn_qessf is driven by its high z20 level, indicating a significant move in the equities space. However, with a resid_z of 0.41, the move is largely priced in by factor exposures. The valid metal_copper_channel and gold_silver_comove channels suggest that global commodity trends may influence Indian metal equities, but the weak inr_oil_channel and dxy_inr_channel indicate that the transmission to Indian markets may be muted.
- **Gap**: No gap: the move in dyn_qessf is largely priced in by factor exposures, with a resid_z of 0.41 indicating a relatively small unexplained component
- **India take**: Indian defence and aerospace stocks, such as Apollo Micro Systems and HFCL, may be in focus due to recent announcements and brokerage coverage. However, the broader Indian market, as represented by the nifty_50, has not yet reacted significantly to the decline in dyn_qessf.
- Watch next: nifty_50 (down) — not yet - watch; Risk-off sentiment may lead to a decline in Indian equities
- Source: Multibagger defence stock Apollo Micro Systems to be in focus tomorrow; here's why — Mint Markets, 2026-07-22. https://www.livemint.com/market/stock-market-news/multibagger-defence-stock-apollo-micro-systems-to-be-in-focus-tomorrow-heres-why-11784728706086.html
- Source: HFCL's X-factor is defence & aerospace? Deven Choksey sees another 66% upside potential, here's why — ET Markets, 2026-07-22. https://economictimes.indiatimes.com/markets/stocks/news/hfcls-x-factor-is-defence-aerospace-deven-choksey-sees-another-66-upside-potential-heres-why/articleshow/132553438.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-15 (d=0.32), 2024-11-14 (d=0.52)

### [RED 5.64] usd_jpy ↑
- usd_jpy [FX]: last 163.72, z20 3.64, zc 0.88, resid-z 0.42 [quiet], 1d 0.33%, |z20|=3.64; 1y-pct=100
- **Mechanism**: The USD/JPY move is driven by US-Iran tensions and inflation fears, which have increased investor caution and supported the safe-haven dollar. The Japanese yen's slide to a forty-year low is also attributed to the Bank of Japan's monetary policy and the country's trade-weighted exchange rate index hitting fresh record lows. The metal_copper_channel and gold_silver_comove channels are valid and may influence the propagation of this move.
- **Gap**: No gap: the USD/JPY move is largely priced in, given the small resid_z of 0.42 and the significant z20 level of 3.635308850068377, indicating that the move is largely explained by factor exposures
- **India take**: The Indian Rupee (INR) may weaken against the US Dollar (USD) due to the broad dollar strength and the country's import bill. The metal_copper_channel may also influence Indian metal equities, such as those in the Nifty Metal index.
- Watch next: nifty_50 (down) — not yet - watch; Risk-off sentiment may lead to a decline in Indian equities
- Source: US-Iran tensions underpin dollar as yen nears 40-year low — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/forex/forex-news/us-iran-tensions-underpin-dollar-as-yen-nears-40-year-low/articleshow/132570439.cms
- Source: Yen’s Slump in Trade-Weighted Gauge Shows Its Broad-Based Drop — Mint Markets, 2026-07-23. https://www.livemint.com/market/yens-slump-in-trade-weighted-gauge-shows-its-broad-based-drop-11784768496092.html
- Source: Yen Rebound Ebbs After Brief Rally on Outlook for BOJ Rate Hikes — Mint Markets, 2026-07-22. https://www.livemint.com/market/yen-rebound-ebbs-after-brief-rally-on-outlook-for-boj-rate-hikes-11784754197557.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2024-11-08 (d=0.01)

### [RED 4.78] commodities · 3 series ↑
- corn [COMMODITIES]: last 488.00, z20 3.47, zc 4.47, resid-z 3.80 [unexplained], 1d 5.63%, |z20|=3.47; 1y-pct=100
- wheat [COMMODITIES]: last 701.50, z20 1.86, zc -0.26, resid-z -0.40 [quiet], 1d -0.60%, |z20|=1.86; 1y-pct=99
- soybeans [COMMODITIES]: last 1245.75, z20 1.73, zc 1.02, resid-z 0.73 [quiet], 1d 1.03%, |z20|=1.73; 1y-pct=100
- **Mechanism**: The recent surge in commodity prices, particularly corn, wheat, and soybeans, is driven by a combination of factors, including supply and demand imbalances and market sentiment. The move is largely priced, with a significant portion of the price action explained by factor exposures. However, the unexplained component, as measured by resid_z, suggests that there may be some residual momentum that could drive further price action. The valid gold_silver_comove and metal_copper_channel suggest that monetary metals and global copper prices may influence Indian metal equities.
- **Gap**: No gap: the move in commodity prices is largely priced, with a significant portion of the price action explained by factor exposures
- **India take**: The Indian instruments that express this move are dyn_patanjali_ns and dyn_tataelxsi_ns, which have already reacted to the surge in wheat prices, while dyn_adanient_bo remains quiet despite its exposure to soybeans
- Watch next: corn (up) — already moved; high z20 score and low resid_z indicate a priced move
- Watch next: wheat (up) — not yet - watch; unexplained move with high resid_z suggests potential for further price action
- Watch next: soybeans (up) — quiet; low z20 score and low resid_z indicate a quiet market
- **India receivers**: dyn_patanjali_ns (rho -0.518, z -1.64); dyn_adanient_bo (rho -0.393, z -1.73); dyn_tataelxsi_ns (rho -0.358, z -1.71)
- Historical analogues: 2026-05-22 (d=0.0), 2024-08-30 (d=0.27), 2026-05-06 (d=0.32)

### [RED 4.62] dxy ↑
- dxy [FX]: last 101.41, z20 1.62, zc 0.85, resid-z 0.73 [quiet], 1d 0.27%, 20d range extreme; |z20|=1.62; 1y-pct=99
- **Mechanism**: The recent surge in DXY has been largely priced in, with a resid_z of 0.73 indicating that most of the move can be explained by factor exposures. However, the historically high z20 level of 1.6238575832728155 and the extreme 20d range may still have implications for correlated instruments. The VALID gold_silver_comove and metal_copper_channel may transmit the dollar strength to the Indian metal equities and commodities market.
- **Gap**: No gap: the big raw move in DXY has a small resid_z, indicating the move is largely priced in
- **India take**: The Indian metal equities, such as those in the Nifty Metal index, may react to the dollar strength through the metal_copper_channel. However, the reaction may be limited due to the WEAK dxy_inr_channel and inr_oil_channel.
- Watch next: comex_gold (down) — not yet - watch; historically leads by 3d and negatively correlated with DXY
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [AMBER 4.47] dyn_hdb ↓
- dyn_hdb [EQUITIES]: last 23.11, z20 -2.47, zc -0.18, resid-z 0.29 [quiet], 1d -0.28%, |z20|=2.47; 1y-pct=0
- **Mechanism**: dyn_hdb ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.658 via dyn_hdb, z -1.55, reacted); nifty_midcap_100 (rho 0.526 via dyn_hdb, z -1.35, reacted); dyn_jiofin_bo (rho 0.475 via dyn_hdb, z -1.62, reacted)
- Watch next: india_vix (inverse) — not yet - watch; rho -0.538 vs dyn_hdb, historically leads by 1d
- **India receivers**: nifty_50 (rho 0.658, z -1.55); nifty_midcap_100 (rho 0.526, z -1.35); dyn_jiofin_bo (rho 0.475, z -1.62)
- Source: HDFC Bank shares slide 10% in four day after Q1 results but brokerages see up to 40% upside. Here’s why — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-bank-shares-slide-10-in-four-day-after-q1-results-but-brokerages-see-up-to-40-upside-heres-why/articleshow/132573294.cms
- Source: HDFC Bank shares slide 10% in four days after Q1 results but brokerages see up to 40% upside. Here’s why — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-bank-shares-slide-10-in-four-day-after-q1-results-but-brokerages-see-up-to-40-upside-heres-why/articleshow/132573294.cms
- Source: HDFC Bank shares tumble over 8% in three days on net interest margin concerns — BusinessLine Mkts, 2026-07-22. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-tumble-over-8-in-three-days-on-net-interest-margin-concerns/article71253282.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [AMBER 4.19] dyn_bharatcoal_ns ↓
- dyn_bharatcoal_ns [EQUITIES]: last 34.80, z20 -2.19, zc -0.12, resid-z n/a [quiet], 1d -0.34%, |z20|=2.19
- **Mechanism**: dyn_bharatcoal_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Sotefin Bharat IPO listing: Shares hit upper circuit after listing at a 10% premium; details here — Mint Markets, 2026-07-23. https://www.livemint.com/market/ipo/sotefin-bharat-ipo-listing-shares-hit-upper-circuit-after-listing-at-a-10-premium-details-here-11784782273860.html
- Source: Sotefin Bharat shares set for BSE SME debut today. GMP signals muted listing — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/stocks/news/sotefin-bharat-shares-set-for-bse-sme-debut-today-gmp-signals-muted-listing/articleshow/132571290.cms
- Source: Bharat Coking Coal shares fall 7% after Q1FY27 net loss — BusinessLine Mkts, 2026-07-22. https://www.thehindubusinessline.com/markets/bharat-coking-coal-shares-fall-8-after-q1fy27-net-loss/article71252055.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-11 (d=0.3), 2026-07-03 (d=0.75)

## Watchlist (below surfacing floor)
dyn_ohi ↑ (3.99), dyn_hdbfs_bo ↓ (3.95), gold_silver_ratio ↑ (3.64), dyn_patanjali_ns ↓ (3.64), dyn_icicigi_bo ↓ (3.58), nifty_50 ↓ (3.55), usd_inr ↑ (3.33), dyn_infy ↓ (3.24), brent_wti_spread ↑ (3.1), dyn_aapl ↑ (2.6), dyn_atherenerg_ns ↑ (2.59), dyn_karurvysya_ns ↑ (2.58)

## India macro
- nifty_50: 23872.1992 (1d -0.52%, z20 -1.55, flag amber)
- nifty_midcap_100: 61695.6992 (1d -0.95%, z20 -1.35, flag none)
- usd_inr: 96.5630 (1d 0.23%, z20 1.33, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5844 (1d -0.43%, z20 -0.04, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 86.4 — "Updated: Indian bonds fall for third session as oil prices near $100 a barrel"
- INOXINDIA.NS (INOX INDIA LIMITED) score 84.1 — "Updated: Indian bonds fall for third session as oil prices near $100 a barrel"
- HDB (HDFC Bank Limited) score 68.9 — "ECB reveals shortlisted designs for new banknotes and launches public survey"
- BAC (Bank of America Corporation) score 66.1 — "ECB reveals shortlisted designs for new banknotes and launches public survey"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 65.9 — "ECB reveals shortlisted designs for new banknotes and launches public survey"
- IDBI.NS (IDBI BANK LIMITED) score 59.2 — "ECB reveals shortlisted designs for new banknotes and launches public survey"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 52.0 — "Updated: Indian bonds fall for third session as oil prices near $100 a barrel"
- COIN (Coinbase Global, Inc.) score 51.5 — "Global oil tops $100 after Houthis strike Saudi tankers and Trump threatens ‘military puni"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 48.9 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Live: US stocks fall as Big Tech ear"
- TECHM.NS (TECH MAHINDRA LIMITED) score 45.3 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Live: US stocks fall as Big Tech ear"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 34.4 — "ECB reveals shortlisted designs for new banknotes and launches public survey"
- OHI (Omega Healthcare Investors, In) score 28.5 — "Eternal’s investors can prepare for more positive earnings surprises"
- COALINDIA.NS (COAL INDIA LTD) score 27.3 — "Updated: Indian bonds fall for third session as oil prices near $100 a barrel"
- BOND (PIMCO Active Bond Exchange-Tra) score 25.1 — "Updated: Indian bonds fall for third session as oil prices near $100 a barrel"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 23.0 — "SBI Mutual Fund trims stake in Ather Energy to 5% after partial profit booking. Details he"
- CHKP (Check Point Software Technolog) score 21.7 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 2"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 16.2 — "Market wrap: Adani Enterprises, IndiGo, Bajaj Auto among top gainers and losers on Nifty a"
- VT (Vanguard Total World Stock Ind) score 12.3 — "U.S. Refinery Utilization Hits 96.2% as Fuel Markets Tighten Worldwide"
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.1 — "Bonus bonanza! This textile player announced 1:1 bonus issue, dividend just 14 sessions af"
- JIOFIN.BO (Jio Financial Services Limited) score 11.1 — "Are you looking for financial advice? This is the best way to ask for it."
- GS (Goldman Sachs Group, Inc. (The) score 10.2 — "Oil Price Today (July 23): Crude oil crosses $95 as US strikes enter 12th day. Why Goldman"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 9.9 — "Are you looking for financial advice? This is the best way to ask for it."
- LTH (Life Time Group Holdings, Inc.) score 8.6 — "Lohia Corp IPO: Issue receives modest response on Day 1, subscribed 0.40 times; GMP signal"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 8.6 — "ICICI Bank sets initial guidance for first dollar bond in nearly 9 years, bankers say"
- INFY (Infosys Limited) score 7.8 — "Infosys Q1 results: Profit up 12% YoY; announces new CEO designate; key takeaways of June-"
- MS (Morgan Stanley) score 7.4 — "AI stocks are echoing a 1990s market split. JPMorgan warns the next few weeks are critical"
- META (Meta) score 6.1 — "The Metals Selloff Is Creating New Winners And Losers"
- PCJEWELLER.NS (PC JEWELLER LTD) score 5.7 — "Bluestone Jewellery shares rocket 36% in just three days after Q1 results. Can the momentu"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 5.7 — "Sotefin Bharat shares set for BSE SME debut today. GMP signals muted listing"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 5.6 — "IEX Q1 results: Net profit grows 12% YoY to  ₹135 crore; electricity volumes rise 16%"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 4.8 — "Multibagger defence stock Apollo Micro Systems to be in focus tomorrow; here's why"
- ETERNAL.NS (ETERNAL LIMITED) score 4.6 — "Eternal’s investors can prepare for more positive earnings surprises"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 4.4 — "Tata Group stock Indian Hotels falls 1% despite strong Q1 results 2026. Should you buy or "
- NVDA (NVIDIA Corporation) score 4.2 — "AMD plans to invest to up $5 billion into Anthropic as it seeks to cut into Nvidia’s domin"
- NFLX (Netflix, Inc.) score 3.0 — "US stocks to buy for short term: From Nvidia to Netflix- Appreciate CEO suggests picking t"
- WIT (Wipro Limited) score 2.5 — "Stocks to watch: Reliance Industries, Wipro, CEAT among shares in focus today; check list "
- AAPL (Apple Inc.) score 2.4 — "Dollar wavers as markets grapple with Gulf tensions"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 1.3 — "Newly-listed SME stock DSM Fresh Foods jumps over 30% in 2 days after reporting a 58% YoY "
- BIOCON.BO (BIOCON LTD.) score 0.6 — "Mylan exits Biocon, sells entire 5.64% stake for ₹3,679 crore via block deals"
- CUPID.NS (CUPID LIMITED) score 0.4 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"

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