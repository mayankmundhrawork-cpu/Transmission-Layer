# Transmission Layer — board brief · 2026-07-18 05:53Z

data as of **2026-07-18** · 98 series · 15 red / 29 amber · 8 events surfaced (28 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.57, 9d in regime; vol-pct 0.703, breadth-off 0.438, Markov P(high-vol) 0.057)
- [INVERTED] **safe_haven_gold** — corr20 0.01, corr60 -0.42, contra nifty_50 corr20=0.25, last shift 2026-05-22. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.82, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.43, corr60 0.38, last shift 2026-05-15. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.18, corr60 -0.06, last shift 2026-05-29. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.8, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.06, corr60 -0.06, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.17, corr60 -0.27, last shift 2026-05-11. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.21, corr60 0.23, last shift 2026-04-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **4 of 89** scanned series survive multiplicity control (effective p ≤ 0.001935206426436853)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.492** (n=1160) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=2985) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.632** (n=19) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.39] commodities · 2 series ↑
- brent [COMMODITIES]: last 88.09, z20 2.56, zc 2.21, resid-z 1.13 [moved], 1d 4.58%, 1-session move +4.58% ≥ 1.5%; |z20|=2.56; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 81.77, z20 2.39, zc 1.69, resid-z 0.74 [moved], 1d 3.57%, 1-session move +3.57% ≥ 1.5%; |z20|=2.39
- **Mechanism**: The recent surge in oil prices, driven by renewed US-Iran hostilities and the threat of Red Sea closure, has led to a significant increase in brent and wti prices. This move is largely priced, with resid_z values of 1.13 and 0.74, respectively, indicating that the move is mostly explained by factor exposures. The valid metal_copper_channel and gold_silver_comove channels may also contribute to the propagation of this move, as they are related to commodity prices.
- **Gap**: No gap: the move in oil prices is largely priced, with resid_z values indicating that the move is mostly explained by factor exposures
- **India take**: The Indian instrument that expresses this move is nifty_midcap_100, which has a negative correlation with wti. However, it has not reacted yet, and its z20 value of 0.11 indicates a quiet status. Additionally, India's proposed stricter vehicle emission rules may also impact oil consumption and prices in the country.
- Watch next: nifty_midcap_100 (down) — not yet - watch; negative correlation with wti
- **India receivers**: nifty_midcap_100 (rho -0.581, z 0.11)
- Source: Oil settles up on renewed US-Iran hostilities and threat of Red Sea closure — ET Markets, 2026-07-18. https://economictimes.indiatimes.com/markets/commodities/news/oil-settles-up-on-renewed-us-iran-hostilities-and-threat-of-red-sea-closure/articleshow/132474160.cms
- Source: US firms sign $60 billion Iraq deals to develop oil routes beyond Strait of Hormuz — BusinessLine Mkts, 2026-07-18. https://www.thehindubusinessline.com/news/world/us-firms-sign-60-billion-iraq-deals-to-develop-oil-routes-beyond-strait-of-hormuz/article71236916.ece
- Source: India Proposes Stricter Vehicle Emission Rules To Cut Oil Consumption — OilPrice, 2026-07-17. https://oilprice.com/Latest-Energy-News/World-News/India-Proposes-Stricter-Vehicle-Emission-Rules-To-Cut-Oil-Consumption.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 7.14] indices · 3 series ↓
- taiwan_weighted [INDICES]: last 42918.00, z20 -3.82, zc -4.41, resid-z -3.10 [unexplained], 1d -5.93%, |z20|=3.82
- nikkei_225 [INDICES]: last 64113.21, z20 -3.28, zc -2.03, resid-z -1.47 [moved], 1d -4.07%, |z20|=3.28
- kospi [INDICES]: last 6835.21, z20 -1.70, zc -1.45, resid-z -1.41 [quiet], 1d -6.17%, |z20|=1.70
- **Mechanism**: The decline in global equity markets, particularly in Japan's Nikkei and Taiwan's weighted index, is driven by escalating US-Iran tensions and elevated crude oil prices, leading to a risk-off sentiment. This sentiment is transmitted to Indian markets through channels such as the metal_copper_channel and gold_silver_comove, which are currently valid. The Indian metal sector, as represented by nifty_metal, has already reacted to this transmission with a z20 score of -1.1.
- **Gap**: No gap: The big raw moves in Nikkei and Taiwan indices have small resid_z values, indicating that the moves are largely priced and not anomalous.
- **India take**: The Indian metal sector, particularly nifty_metal, has already reacted to the global market decline, while other transmission candidates such as dyn_hdbfs_bo and dyn_ceatltd_ns remain quiet. The nifty_metal index has a z20 score of -1.1, indicating a decline in line with global market trends.
- Watch next: nifty_metal (down) — already moved; Transmission from Kospi
- Watch next: dyn_hdbfs_bo (down) — not yet - watch; Quiet despite Nikkei transmission
- **India receivers**: nifty_metal (rho 0.527, z -1.1); dyn_hdbfs_bo (rho 0.496, z -0.83); dyn_ceatltd_ns (rho 0.446, z -0.72); nifty_midcap_100 (rho 0.438, z 0.11)
- Source: US stock market to Nikkei: Here’s global equity heatmap you should know before opening of the Indian stock market today — Mint Markets, 2026-07-17. https://www.livemint.com/market/stock-market-news/us-stock-market-to-nikkei-here-s-global-equity-heatmap-you-should-know-before-opening-of-the-indian-stock-market-today-11784257058033.html
- Source: Global Markets: Japan's Nikkei drops nearly 3% as chip stocks slide despite robust TSMC results — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/us-stocks/news/global-markets-japans-nikkei-drops-nearly-3-as-chip-stocks-slide-despite-robust-tsmc-results/articleshow/132433045.cms

### [RED 6.42] cross-asset · 2 series ↑
- dyn_techm_ns [EQUITIES]: last 1571.00, z20 3.59, zc 2.15, resid-z 1.06 [moved], 1d 4.02%, |z20|=3.59
- nifty_it [INDICES]: last 29178.55, z20 1.96, zc 0.89, resid-z 0.28 [quiet], 1d 1.59%, |z20|=1.96
- **Mechanism**: The recent rally in IT stocks, led by a 2.3% gain in the Nifty IT index, has lifted sentiment across the broader Indian stock market, with the benchmark indices rallying more than 1% each. This move is priced, with a small resid_z of 1.06 for dyn_techm_ns, indicating that the factor exposures have largely explained the move. The VALID gold_silver_comove and metal_copper_channel suggest a positive correlation between monetary metals and Indian metal equities, which may contribute to the rally.
- **Gap**: No gap: the recent move in IT stocks is largely explained by factor exposures, with a small resid_z of 1.06, indicating that the move is priced.
- **India take**: The Indian instrument that expresses this move is the Nifty IT index, which has already reacted with a 2.3% gain. Other Indian instruments, such as dyn_tataelxsi_ns, have also reacted, with a rho of 0.706 via nifty_it.
- Watch next: dyn_techm_ns (up) — already moved; Q1 results and IT stock rally
- **India receivers**: dyn_tataelxsi_ns (rho 0.706, z -1.51); nifty_50 (rho 0.35, z 1.61)
- Source: Q1 Results Today Live: HDFC Bank, ICICI Bank, Axis Bank, Kotak Mahindra Bank, PNB, IDBI Bank, Yes Bank, JK Cement, India Cements to announce Q1 results — BusinessLine Mkts, 2026-07-18. https://www.thehindubusinessline.com/markets/stock-markets/q1-results-today-live-updates-hdfc-bank-icici-bank-axis-bank-kotak-mahindra-bank-pnb-idbi-bank-yes-bank-jk-cement-india-cement-results-18-july-2026/article71237100.ece
- Source: Infosys, TCS, HCL Technologies to Tech Mahindra: Why are IT stocks rising today? — Mint Markets, 2026-07-17. https://www.livemint.com/market/stock-market-news/infosys-tcs-hcl-technologies-to-tech-mahindra-why-are-it-stocks-rising-today-11784271768196.html
- Source: Tech Mahindra shares jump on Q1 results; analysts split on valuation — BusinessLine Mkts, 2026-07-17. https://www.thehindubusinessline.com/markets/stock-markets/tech-mahindra-surges-on-strong-q1-results-analysts-split-on-valuation/article71232908.ece
- Historical analogues: 2025-12-30 (d=0.52), 2025-08-13 (d=0.76), 2026-01-06 (d=0.77)

### [RED 5.74] shanghai_comp ↓
- shanghai_comp [INDICES]: last 3764.63, z20 -3.74, zc -2.61, resid-z -3.15 [unexplained], 1d -3.03%, |z20|=3.74
- **Mechanism**: The Shanghai Composite's decline is driven by concerns over liquidity crunch due to CXMT's $8.6 billion IPO and a pipeline of large listings, which has triggered heavy selling in AI and semiconductor stocks. This move is unexplained by factor exposures, with a resid_z of -1.76. The valid vix_equity_inverse channel suggests that the vol spike will lead to equity drawdown, potentially transmitting to Indian markets.
- **Gap**: No gap: the big raw move in Shanghai Composite is largely priced, with a z20 of -3.74 and a resid_z of -1.76, indicating that the move is mostly explained by the liquidity concerns and tech sell-off
- **India take**: The Indian instruments that express this move are the midcap_largecap_ratio and dyn_hdbfs_bo, both of which have already reacted with a z20 of -1.34 and -1.06, respectively. The metal_copper_channel may also transmit the move to Indian metal equities.
- Watch next: nifty_50 (down) — not yet - watch; Indian equities often follow Chinese market trends
- **India receivers**: midcap_largecap_ratio (rho 0.396, z -1.34); dyn_hdbfs_bo (rho 0.36, z -0.83)
- Source: Global Market: China stocks face steep weekly losses as CXMT IPO sparks liquidity crunch fears — ET Markets, 2026-07-17. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-face-steep-weekly-losses-as-cxmt-ipo-sparks-liquidity-crunch-fears/articleshow/132453628.cms
- Source: Global Market:  China stocks slide as tech sell-off hits mainland markets; Alibaba lifts Hong Kong shares — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-slide-as-tech-sell-off-hits-mainland-markets-alibaba-lifts-hong-kong-shares/articleshow/132431074.cms
- Historical analogues: 2026-06-18 (d=0.0), 2025-12-19 (d=0.02), 2025-09-25 (d=0.03)

### [RED 5.56] dyn_icicigi_bo ↓
- dyn_icicigi_bo [EQUITIES]: last 1612.30, z20 -3.56, zc -0.41, resid-z -0.56 [quiet], 1d -0.67%, |z20|=3.56; 1y-pct=0
- **Mechanism**: The decline in dyn_icicigi_bo is likely due to the upcoming Q1 results of ICICI Bank, which may lead to a reevaluation of the bank's stock price. The move is currently priced, with a small resid_z of -0.56, indicating that the decline is largely explained by factor exposures. The VALID vix_equity_inverse channel suggests that a vol spike could lead to an equity drawdown, which may be a contributing factor to the decline.
- **Gap**: No gap: the decline in dyn_icicigi_bo is largely explained by factor exposures, with a small resid_z of -0.56, indicating that the move is PRICED
- **India take**: The Indian instrument that expresses this move is nifty_midcap_100, which has a rho of 0.429 with dyn_icicigi_bo. However, it has not reacted yet, and is currently quiet with a z20 of 0.11.
- Watch next: nifty_midcap_100 (down) — not yet - watch; rho=0.429 via dyn_icicigi_bo
- **India receivers**: nifty_midcap_100 (rho 0.429, z 0.11); dyn_indianb_ns (rho 0.368, z 0.3); dyn_adanient_bo (rho 0.358, z 0.8)
- Source: Q1 Results Today Live: HDFC Bank, ICICI Bank, Axis Bank, Kotak Mahindra Bank, PNB, IDBI Bank, Yes Bank, JK Cement, India Cements to announce Q1 results — BusinessLine Mkts, 2026-07-18. https://www.thehindubusinessline.com/markets/stock-markets/q1-results-today-live-updates-hdfc-bank-icici-bank-axis-bank-kotak-mahindra-bank-pnb-idbi-bank-yes-bank-jk-cement-india-cement-results-18-july-2026/article71237100.ece
- Source: ICICI Bank Q1 results preview: Net profit seen up 3.1% YoY to  ₹13,164 crore; NIMs, asset quality may remain stable — Mint Markets, 2026-07-18. https://www.livemint.com/market/stock-market-news/icici-bank-q1-results-preview-net-profit-seen-up-3-1-yoy-to-rs-13-164-crore-nims-asset-quality-may-remain-stable-11784280397246.html
- Source: Q1 results 2026: HDFC Bank to ICICI Bank, Axis Bank among over 20 companies to declare Q1 earnings today; full list here — Mint Markets, 2026-07-18. https://www.livemint.com/market/stock-market-news/q1-results-2026-hdfc-bank-to-icici-bank-axis-bank-among-companies-to-declare-q1-earnings-today-18-july-full-list-here-11784312775848.html
- Historical analogues: 2026-06-24 (d=0.0), 2025-05-30 (d=0.03), 2026-01-07 (d=0.04)

### [AMBER 4.93] cross-asset · 3 series ↑
- nifty_50 [INDICES]: last 24343.65, z20 1.61, zc 1.41, resid-z 1.84 [unexplained], 1d 1.13%, |z20|=1.61
- dyn_indusindbk_bo [EQUITIES]: last 1027.20, z20 1.45, zc 0.72, resid-z -0.34 [quiet], 1d 1.32%, 1y-pct=100
- nifty_midcap_100 [INDICES]: last 62369.75, z20 0.11, zc -0.62, resid-z -2.55 [unexplained], 1d -0.58%, 1y-pct=96
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-18 (z-distance 0.85).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.902 via nifty_50, z 1.28, reacted); dyn_indianb_ns (rho 0.631 via nifty_midcap_100, z 0.3, quiet); dyn_ceatltd_ns (rho 0.608 via nifty_midcap_100, z -0.72, quiet); nifty_metal (rho 0.597 via nifty_midcap_100, z -1.1, reacted); dyn_adanient_bo (rho 0.59 via nifty_midcap_100, z 0.8, quiet)
- Watch next: india_vix (inverse) — not yet - watch; rho -0.746 vs nifty_50, historically leads by 3d
- Watch next: dyn_indianb_ns (co-move) — not yet - watch; rho 0.631 vs nifty_midcap_100, historically leads by 1d
- Watch next: dyn_ceatltd_ns (co-move) — not yet - watch; rho 0.608 vs nifty_midcap_100, historically leads by 3d
- Watch next: dax (co-move) — not yet - watch; rho 0.545 vs nifty_50, historically leads by 2d
- Watch next: cac_40 (co-move) — not yet - watch; rho 0.636 vs nifty_50
- **India receivers**: dyn_jiofin_bo (rho 0.902, z 1.28); dyn_indianb_ns (rho 0.631, z 0.3); dyn_ceatltd_ns (rho 0.608, z -0.72); nifty_metal (rho 0.597, z -1.1)
- Source: NIfty IT logs best weekly gains since Oct 2025 — ET Markets, 2026-07-18. https://economictimes.indiatimes.com/markets/stocks/news/nifty-it-logs-best-weekly-gains-since-oct-2025/articleshow/132473695.cms
- Source: Market wrap: Top gainers and losers on Nifty and Sensex today — ET Markets, 2026-07-17. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-top-gainers-and-losers-on-nifty-and-sensex-today/articleshow/132460186.cms
- Source: Sensex today | Stock Market Highlights: Sensex jumps 965 pts, Nifty ends above 24,334; financials rally ahead of key earnings — BusinessLine Mkts, 2026-07-17. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-17th-july-2026/article71229818.ece
- Historical analogues: 2025-07-18 (d=0.85), 2025-07-11 (d=1.33), 2025-05-30 (d=1.51)

### [RED 4.9] dyn_nflx ↓
- dyn_nflx [EQUITIES]: last 68.86, z20 -2.90, zc -4.06, resid-z 0.65 [moved], 1d -7.38%, |z20|=2.90; 1y-pct=0
- **Mechanism**: dyn_nflx ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Why Netflix’s AI push isn’t reviving the stock — Mint Markets, 2026-07-18. https://www.livemint.com/market/stock-market-news/why-netflix-s-ai-push-isn-t-reviving-the-stock-11784341921233.html
- Source: Netflix shares tumble 13% after weak sales forecast, hit 22-month low — Mint Markets, 2026-07-17. https://www.livemint.com/market/netflix-shares-tumble-13-after-weak-sales-forecast-hit-22-month-low-11784295044711.html
- Source: Netflix shares tumble over 10% as slowing growth, less viewership data spook investors — ET Markets, 2026-07-17. https://economictimes.indiatimes.com/markets/us-stocks/news/netflix-shares-tumble-over-10-as-slowing-growth-less-viewership-data-spook-investors/articleshow/132465122.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-10 (d=0.03), 2025-04-01 (d=0.05)

### [AMBER 4.88] rates · 3 series ↑
- tips_10y_real [RATES]: last 2.35, z20 1.56, zc 0.74, resid-z 0.05 [quiet], 1d 1.29%, |z20|=1.56; 1y-pct=99
- ust_30y [RATES]: last 5.09, z20 1.47, zc 0.30, resid-z -0.18 [quiet], 1d 0.20%, 1y-pct=97
- ust_10y [RATES]: last 4.57, z20 1.18, zc 0.45, resid-z -0.21 [quiet], 1d 0.44%, 1y-pct=97
- **Mechanism**: The recent surge in Japanese bond yields, driven by rising oil prices and fiscal concerns, has led to a global market reaction, with US Treasury yields (ust_10y, ust_30y) increasing. This move is largely priced, as evidenced by the low resid_z values (0.05, -0.18, -0.21) for the affected series, indicating that the factor exposures can explain most of the move.
- **Gap**: No gap: the move in US Treasury yields is largely explained by factor exposures, with low resid_z values indicating that the move is priced
- **India take**: The Indian 10-year government bond yield may react to this global trend, potentially leading to an increase in yields. However, the inr_oil_channel is weak, which may limit the transmission of global oil price shocks to Indian markets.
- Watch next: ust_2y (up) — not yet - watch; historically leads by 1d
- Source: Global Market: Japanese bond yields climb as oil surge and fiscal concerns weigh on market — ET Markets, 2026-07-16. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japanese-bond-yields-climb-as-oil-surge-and-fiscal-concerns-weigh-on-market/articleshow/132431940.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.25), 2026-03-30 (d=0.31)

## Watchlist (below surfacing floor)
gold_silver_ratio ↑ (4.83), commodities · 3 series ↑ (4.54), nasdaq_100 ↓ (4.53), dyn_qessf ↓ (4.34), dyn_aapl ↑ (3.98), dyn_bac ↑ (3.75), dyn_patanjali_ns ↓ (3.59), dyn_ohi ↑ (3.55), usd_inr ↑ (3.53), dyn_bhel_ns ↑ (3.34), dyn_pypl ↑ (2.82), dyn_adanient_bo ↑ (2.8)

## India macro
- nifty_50: 24343.6504 (1d 1.13%, z20 1.61, flag amber)
- nifty_midcap_100: 62369.7500 (1d -0.58%, z20 0.11, flag amber)
- usd_inr: 96.2700 (1d -0.24%, z20 1.53, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5621 (1d -1.68%, z20 -1.34, flag none)
- Next India prints: NSDL FPI flows T-2d · IMD weekly rainfall T-2d · RBI Weekly Statistical Supplement T-6d · Kharif sowing data T-6d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 76.4 — "Agentic AI, alternative data and SIFs take centre stage at Indian Institutional Quant Conf"
- INDIANB.NS (INDIAN BANK) score 69.5 — "TRUMP MEDIA TARGETS WALL STREET Trump Media is reportedly seeking up to $100,000 a month t"
- HDB (HDFC Bank Limited) score 61.7 — "TRUMP MEDIA TARGETS WALL STREET Trump Media is reportedly seeking up to $100,000 a month t"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 53.6 — "TRUMP MEDIA TARGETS WALL STREET Trump Media is reportedly seeking up to $100,000 a month t"
- COIN (Coinbase Global, Inc.) score 48.7 — "Japan's LNG Giant Weighs U.S. IPO to Accelerate Global Expansion"
- BAC (Bank of America Corporation) score 44.7 — "TRUMP MEDIA TARGETS WALL STREET Trump Media is reportedly seeking up to $100,000 a month t"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 43.9 — "19 (mostly) tech stocks that have fallen at least 25% in July"
- IDBI.NS (IDBI BANK LIMITED) score 32.4 — "TRUMP MEDIA TARGETS WALL STREET Trump Media is reportedly seeking up to $100,000 a month t"
- CHKP (Check Point Software Technolog) score 26.4 — "Xtranet Technologies announces IPO dates for launch next week. Check details"
- BOND (PIMCO Active Bond Exchange-Tra) score 23.1 — "Fairfax picks up half of 3-year government bonds at auction"
- VT (Vanguard Total World Stock Ind) score 21.5 — "The World Cup–winning side will make $50 million — and the IRS gets a cut"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 17.3 — "Look on the bright side: Energy companies are booming"
- TECHM.NS (TECH MAHINDRA LIMITED) score 14.6 — "19 (mostly) tech stocks that have fallen at least 25% in July"
- JIOFIN.BO (Jio Financial Services Limited) score 14.2 — "A bad health diagnosis will upend your financial plan, but you can set it right again"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 14.2 — "A bad health diagnosis will upend your financial plan, but you can set it right again"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.2 — "Tata Technologies Q1 Results: Profit rises 6% to Rs 180 crore"
- SKHYV (SK hynix Inc. American Deposit) score 9.6 — "SKHY – SK HYNIX DOWN 0.7% IN PREMARKET SK Hynix shares are slipping 0.7% in premarket afte"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.5 — "HORMUZ TRAFFIC HITS 3-WEEK LOW Confirmed crossings via the Strait of Hormuz dropped to a 3"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 9.2 — "Q1 results 2026: HDFC Bank to ICICI Bank, Axis Bank among over 20 companies to declare Q1 "
- WIT (Wipro Limited) score 8.7 — "Stocks to watch: Reliance Industries, Wipro, CEAT among shares in focus today; check list "
- NFLX (Netflix, Inc.) score 8.6 — "Why Netflix’s AI push isn’t reviving the stock"
- META (Meta) score 7.8 — "U.S. JUDGE WILL NOT BLOCK META PLATFORMS LAYOFFS IN NOVEL AI DISCRIMINATION CASE"
- BHEL.NS (BHEL) score 7.5 — "BHEL hits 52-week high before retreating; analysts split as Q1 profit ends eight-year wait"
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.1 — "India's gold jewellery demand revives as prices stabilise; festive orders pick up: WGC"
- OHI (Omega Healthcare Investors, In) score 5.6 — "These three large-cap stocks look cheap. Here's why investors should look closer"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.5 — "Adani Ent Share Price Live Updates: Adani Enterprises  Current Price Update"
- AAPL (Apple Inc.) score 4.5 — "APPLE CLOSES IN ON NVIDIA $AAPL is on the verge of reclaiming the title of the world’s mos"
- NVDA (NVIDIA Corporation) score 4.5 — "APPLE CLOSES IN ON NVIDIA $AAPL is on the verge of reclaiming the title of the world’s mos"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 4.3 — "KUWAIT DEFENCE MINISTRY SAYS IRANIAN 'AGGRESSION' ON THURSDAY TARGETED NUMBER OF VITAL FAC"
- MS (Morgan Stanley) score 3.9 — "Dimon-led JPMorgan poised to become world's first $1 trillion bank"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 3.6 — "KUWAIT SAYS ELECTRICAL AND DESALINATION POWER PLANT DAMAGED IN IRANIAN ATTACK - ELECTRICIT"
- KALYANKJIL.NS (KALYAN JEWELLERS IND LTD) score 3.4 — "Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. T"
- GS (Goldman Sachs Group, Inc. (The) score 3.3 — "Crude oil prices rise for 4th session amid escalating US-Iran war; Brent likely to hit $11"
- CEATLTD.NS (CEAT LIMITED) score 3.1 — "CEAT share price slumps over 9% on Q1 results. Should you buy, sell or hold?"
- SWIGGY.NS (SWIGGY LIMITED) score 3.1 — "Stocks to buy for short term: Swiggy among 3 shares Amol Athawale of Kotak Securities reco"
- MU (Micron Technology, Inc.) score 2.3 — "Micron has turned into ‘the most important stock in the market.’ So is it time to worry?"
- PYPL (PayPal Holdings, Inc.) score 2.2 — "US stocks today: US stocks rise with earnings in focus; PayPal jumps on takeover bid repor"
- BIOCON.BO (BIOCON LTD.) score 2.1 — "Mylan exits Biocon, sells entire 5.64% stake for ₹3,679 crore via block deals"
- CUPID.NS (CUPID LIMITED) score 1.4 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 1.0 — "Patanjali Foods share price crashes 20%, extending losses for third straight session; what"

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