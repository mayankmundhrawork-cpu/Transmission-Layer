# Transmission Layer — board brief · 2026-07-21 06:45Z

data as of **2026-07-21** · 98 series · 7 red / 39 amber · 8 events surfaced (33 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.515, 11d in regime; vol-pct 0.53, breadth-off 0.5, Markov P(high-vol) 0.058)
- [WEAK] **safe_haven_gold** — corr20 -0.0, corr60 -0.42, contra nifty_50 corr20=0.13, last shift 2026-05-28. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.93, corr60 0.82, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.42, corr60 0.33, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.07, corr60 0.0, last shift 2026-06-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.8, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.07, corr60 -0.07, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.14, corr60 -0.28, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.21, corr60 0.23, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **5 of 89** scanned series survive multiplicity control (effective p ≤ 0.005605629265529988)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.497** (n=1161) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.819** (n=3000) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.722** (n=18) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.77] dyn_karurvysya_ns ↑
- dyn_karurvysya_ns [EQUITIES]: last 332.60, z20 5.77, zc 0.91, resid-z 0.39 [quiet], 1d 7.36%, |z20|=5.77; 1y-pct=98
- **Mechanism**: The recent surge in Karur Vysya Bank shares is primarily driven by the bank's stellar Q1 results, which showed a 45% year-on-year jump in net profit. This move is largely priced in, given the bank's strong growth in net interest income, improved net interest margin, and stable asset quality. The move is not an anomaly, as the bank's fundamentals have improved significantly.
- **Gap**: No gap: The move is largely priced in, with a resid_z of 0.39, indicating that the majority of the move can be explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is the Nifty 50, which has a rho of 0.668 with dyn_karurvysya_ns. Other transmission candidates, such as Nifty Midcap 100, Dyn Indusindbk BO, and Dyn Indianb NS, have already reacted to the news.
- Watch next: nifty_50 (up) — not yet - watch; Historically leads by 3d, with a rho of 0.668 vs dyn_karurvysya_ns
- **India receivers**: nifty_50 (rho 0.668, z 0.4); nifty_midcap_100 (rho 0.637, z 1.27); dyn_jiofin_bo (rho 0.6, z -0.39); dyn_indusindbk_bo (rho 0.535, z 1.87)
- Source: Karur Vysya Bank shares soar 11% after stellar Q1 results. What investors should know — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/stocks/news/karur-vysya-bank-shares-soar-over-11-after-stellar-q1-results-what-investors-should-know/articleshow/132528372.cms
- Source: Karur Vysya Bank shares jump 9.6% after Q1 profit hits record ₹756 crore — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/karur-vysya-bank-shares-jump-96-after-q1-profit-hits-record-756-crore/article71248009.ece
- Source: Karur Vysya Bank shares surge over 10% after Q1 profit jumps 45%. Should investors buy, sell, or hold? — Mint Markets, 2026-07-21. https://www.livemint.com/market/stock-market-news/karur-vysya-bank-shares-surge-over-10-after-the-private-sector-lenders-q1-profit-jumps-45-details-here-11784607405700.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-02 (d=0.07), 2025-01-31 (d=0.09)

### [RED 7.45] dyn_qessf ↓
- dyn_qessf [EQUITIES]: last 0.19, z20 -5.45, zc 0.60, resid-z 1.05 [quiet], 1d -23.72%, |z20|=5.45
- **Mechanism**: The decline in dyn_qessf is largely priced, with a small resid_z of 1.05, indicating that the move is mostly explained by factor exposures. The vix_equity_inverse channel is valid, suggesting that the vol spike may lead to an equity drawdown. However, the metal_copper_channel and gold_silver_comove channels may also play a role in transmitting the move to Indian metal equities and monetary metals.
- **Gap**: No gap: the move in dyn_qessf is largely priced, with a small resid_z and a low r2 of 0.129, indicating that the price move is mostly explained by factor exposures.
- **India take**: The Indian instrument dyn_atherenerg_ns has already reacted to the move in dyn_qessf, with a rho of -0.358. Other Indian metal equities may also be affected through the metal_copper_channel.
- Watch next: dyn_atherenerg_ns (down) — already moved; reacted to dyn_qessf move
- **India receivers**: dyn_atherenerg_ns (rho -0.358, z 1.27)
- Source: Global Market: Private capital crucial to Europe's defence push as funding bottlenecks persist — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-private-capital-crucial-to-europes-defence-push-as-funding-bottlenecks-persist/articleshow/132528379.cms
- Source: West Asia conflict fuels defence stocks. Now comes the harder test — Mint Markets, 2026-07-20. https://www.livemint.com/market/stock-market-news/india-defence-stocks-rally-west-asia-conflict-next-leg-orders-or-execution-indigenization-procurement-11784518899336.html
- Source: HAL, BEL to Bharat Dynamics: Defence stocks dip after escalation in the US-Iran war — Mint Markets, 2026-07-20. https://www.livemint.com/market/stock-market-news/hal-bel-to-bharat-dynamics-defence-stocks-dip-after-escalation-in-the-us-iran-war-11784521448590.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-15 (d=0.32), 2024-11-14 (d=0.52)

### [AMBER 6.18] cross-asset · 5 series ↓
- russell_2000 [INDICES]: last 2942.33, z20 -2.25, zc -0.35, resid-z 1.55 [unexplained], 1d -0.67%, |z20|=2.25
- nasdaq_100 [INDICES]: last 28607.75, z20 -2.06, zc -1.09, resid-z 0.62 [quiet], 1d 0.05%, |z20|=2.06
- dyn_bond [EQUITIES]: last 91.12, z20 -1.31, zc 0.18, resid-z -0.49 [quiet], 1d -0.37%, 1y-pct=2
- tips_10y_real [RATES]: last 2.31, z20 0.76, zc -0.98, resid-z -2.43 [unexplained], 1d -1.70%, 1y-pct=97
- ust_2y [RATES]: last 4.18, z20 0.37, zc 0.37, resid-z -0.28 [quiet], 1d 0.48%, 1y-pct=96
- **Mechanism**: The recent decline in Russell 2000 and Nasdaq 100 indices, along with a drop in dyn_bond and an increase in tips_10y_real, suggests a risk-off sentiment in the market. The valid vix_equity_inverse channel indicates a potential vol spike leading to equity drawdown, which could propagate to Indian markets through the metal_copper_channel. However, the weak inr_oil_channel and dxy_inr_channel suggest that the transmission to INR and Indian metal equities may be muted.
- **Gap**: No gap: the large raw move in russell_2000 and nasdaq_100 is accompanied by a relatively small resid_z, indicating that the move is largely priced in by the market.
- **India take**: The Indian instrument that expresses this move is the Nifty 50, which has not yet reacted. The metal_copper_channel could also transmit the risk-off sentiment to Indian metal equities.
- Watch next: nifty_50 (down) — not yet - watch; potential risk-off sentiment
- Watch next: india_vix (up) — not yet - watch; valid vix_equity_inverse channel
- Source: Lotus Petal opens first SSE bond issue since CSR rule change — BusinessLine Mkts, 2026-07-20. https://www.thehindubusinessline.com/markets/stock-markets/lotus-petal-opens-first-sse-bond-issue-since-csr-rule-change/article71245959.ece
- Source: Wall Street: S&P 500, Nasdaq rebound as chipmakers recover, investors brace for big tech earnings — Mint Markets, 2026-07-20. https://www.livemint.com/market/stock-market-news/us-stocks-rebound-as-chipmakers-recover-investors-brace-for-big-tech-earnings-11784555512184.html
- Source: The Titans of Nasdaq 100: Top companies ranked by market cap — ET Markets, 2026-07-20. https://economictimes.indiatimes.com/markets/us-stocks/news/the-titans-of-nasdaq-100-top-companies-ranked-by-market-cap/slideshow/132516440.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.42), 2025-05-20 (d=0.53)

### [RED 5.83] dyn_hdb ↓
- dyn_hdb [EQUITIES]: last 23.59, z20 -3.83, zc 0.17, resid-z 0.54 [quiet], 1d -10.56%, |z20|=3.83; 1y-pct=2
- **Mechanism**: The recent decline in dyn_hdb is largely priced, with a resid_z of 0.54, indicating that the move is mostly explained by factor exposures. The vix_equity_inverse channel is valid, suggesting that the vol spike may lead to an equity drawdown. However, the weak channels, including safe_haven_gold, inr_oil_channel, and dxy_inr_channel, limit the potential for a significant risk-off move.
- **Gap**: No gap: The decline in dyn_hdb is largely priced, with a resid_z of 0.54, indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is the nifty_50, which has not yet reacted. Other transmission candidates, such as nifty_midcap_100 and dyn_indusindbk_bo, have already reacted.
- Watch next: nifty_50 (down) — not yet - watch; Historically leads dyn_hdb by 1d, with a rho of 0.669
- Watch next: india_vix (up) — not yet - watch; Historically leads dyn_hdb by 1d, with a rho of -0.535
- **India receivers**: nifty_50 (rho 0.669, z 0.4); nifty_midcap_100 (rho 0.524, z 1.27); dyn_indusindbk_bo (rho 0.485, z 1.87); dyn_jiofin_bo (rho 0.465, z -0.39)
- Source: Sensex today | Stock Market Live: Sensex drops 250 pts, Nifty below 24,200; HDFC Bank lead losers — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-21st-may-2026/article71245381.ece
- Source: HDFC Bank shares fall for 2nd day but Jefferies, others brokerages remain bullish. Should you buy the dip? — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-bank-shares-fall-for-2nd-day-but-jefferies-others-brokerages-remain-bullish-should-you-buy-the-dip/articleshow/132528929.cms
- Source: ICICI Bank wins analysts’ vote after Q1 show; HDFC Bank, Axis, Kotak & Yes Bank face scrutiny — ET Markets, 2026-07-21. https://economictimes.indiatimes.com/markets/stocks/news/icici-bank-wins-analysts-vote-after-q1-show-hdfc-bank-axis-kotak-yes-bank-face-scrutiny/articleshow/132528114.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [RED 5.0] dyn_nflx ↓
- dyn_nflx [EQUITIES]: last 67.57, z20 -3.00, zc -4.00, resid-z -2.77 [unexplained], 1d -1.99%, |z20|=3.00; 1y-pct=0
- **Mechanism**: The decline in dyn_nflx is unexplained by factor exposures, with a resid_z of -2.77, indicating a potential anomaly. The valid vix_equity_inverse channel suggests that the vol spike may lead to an equity drawdown. The metal_copper_channel also indicates a potential transmission to Indian metal equities.
- **Gap**: No gap: the big raw move in dyn_nflx has a small resid_z, but it is not an anomaly as the move is largely unexplained by factor exposures, suggesting it is priced
- **India take**: The Indian instrument that expresses this move is the nifty_50, which has not reacted yet. The metal_copper_channel suggests a potential transmission to Indian metal equities such as Hindalco or Tata Steel.
- Watch next: nifty_50 (down) — not yet - watch; Potential risk-off sentiment transmission
- Source: US stocks to buy for short term: From Nvidia to Netflix- Appreciate CEO suggests picking these 5 shares — Mint Markets, 2026-07-20. https://www.livemint.com/market/stock-market-news/us-stocks-to-buy-for-short-term-from-nvidia-to-netflix-appreciate-ceo-suggests-picking-these-5-shares-11784551408198.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-10 (d=0.03), 2025-04-01 (d=0.05)

### [AMBER 4.71] commodities · 2 series ↑
- brent [COMMODITIES]: last 88.36, z20 1.87, zc -0.36, resid-z 1.14 [quiet], 1d -0.96%, |z20|=1.87; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 82.03, z20 1.79, zc -0.56, resid-z 1.00 [quiet], 1d -1.44%, |z20|=1.79
- **Mechanism**: The recent move in commodities, specifically brent and wti, is driven by geopolitical tensions in the Middle East, with prices retreating on reports of potential ceasefire negotiations. However, the big raw move with small resid_z suggests that the price move is largely priced in, with brent and wti having z20 levels of 1.8736 and 1.7874, respectively, and relatively small resid_z values of 1.14 and 1.0.
- **Gap**: No gap: the move in brent and wti is largely explained by their factor exposures, with small resid_z values indicating that the price move is mostly priced in.
- **India take**: The Indian instrument that expresses this move is the nifty_midcap_100, which has already reacted with a rho of -0.62 via brent. The move in commodities may lead to a decrease in the nifty_midcap_100.
- Watch next: nifty_midcap_100 (down) — already moved; rho=-0.62 via brent
- **India receivers**: nifty_midcap_100 (rho -0.62, z 1.27)
- Source: Oil Reverses Gains on Renewed Hope of Peace in Iran — OilPrice, 2026-07-21. https://oilprice.com/Latest-Energy-News/World-News/Oil-Reverses-Gains-on-Renewed-Hope-of-Peace-in-Iran.html
- Source: Goldman Warns Oil Could Hit $120 as Middle East War Drags On — OilPrice, 2026-07-21. https://oilprice.com/Latest-Energy-News/World-News/Goldman-Warns-Oil-Could-Hit-120-as-Middle-East-War-Drags-On.html
- Source: Crude oil futures trade lower on possible ceasefire reports — BusinessLine Mkts, 2026-07-21. https://www.thehindubusinessline.com/markets/commodities/crude-oil-futures-trade-lower-on-possible-ceasefire-reports/article71247995.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [AMBER 4.47] dyn_techm_ns ↑
- dyn_techm_ns [EQUITIES]: last 1587.20, z20 2.47, zc 0.38, resid-z 1.21 [quiet], 1d 0.75%, |z20|=2.47
- **Mechanism**: dyn_techm_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.904 via dyn_techm_ns, z 1.44, reacted); dyn_tataelxsi_ns (rho 0.478 via dyn_techm_ns, z -1.4, reacted)
- **India receivers**: nifty_it (rho 0.904, z 1.44); dyn_tataelxsi_ns (rho 0.478, z -1.4)
- Source: Q1 Results Today Highlights: UltraTech profit rises; IOB, KVB and Sobha post strong Q1 growth; Mahindra Logistics, Dynamic Cables, Jaiprakash Power, Shyam Metalics surge — BusinessLine Mkts, 2026-07-20. https://www.thehindubusinessline.com/markets/q1-results-today-highlights-cement-paytm-iob-karur-vysya-bank-shyam-metalics-sobha-jp-power-bluestone-hdfc-bank-kotak-icici-yes-bank-axis-bank-ril-results-20-july-2026/article71241085.ece
- Source: Q1 Results Today Live: UltraTech PAT up, IOB, KVB Q1 PAT climb, Mahindra Logistics, Dynamic Cables & Shyam Metalics zoom, Paytm, Sobha, JP Power, Bluestone to announce Q1 results — BusinessLine Mkts, 2026-07-20. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-ultratech-cement-paytm-iob-karur-vysya-bank-shyam-metalics-sobha-jp-power-bluestone-hdfc-bank-kotak-icici-yes-bank-axis-bank-ril-results-20-july-2026/article71241085.ece
- Source: ICICI Bank gains while HDFC Bank, Axis Bank, Kotak Mahindra, Yes Bank decline after Q1 results — BusinessLine Mkts, 2026-07-20. https://www.thehindubusinessline.com/markets/stock-markets/bank-stocks-underperform-icici-bank-gains-while-hdfc-bank-axis-bank-kotak-mahindra-yes-bank-decline/article71243829.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-11 (d=0.03), 2025-02-10 (d=0.09)

### [AMBER 4.37] dyn_havells_ns ↑
- dyn_havells_ns [EQUITIES]: last 1220.00, z20 2.37, zc 0.97, resid-z 0.02 [quiet], 1d 1.44%, |z20|=2.37
- **Mechanism**: The recent move in dyn_havells_ns is largely priced, with a small resid_z of 0.02, indicating that the current price reflects the factor exposures. The move is quiet, with a z20 level of 2.37, which is not unusually high. The correlated instruments, such as dyn_jiofin_bo and nifty_50, have not moved significantly, suggesting that the move in dyn_havells_ns is not part of a broader market trend.
- **Gap**: No gap: the move in dyn_havells_ns is largely priced, with a small resid_z and a z20 level that is not unusually high
- **India take**: The Indian instrument that expresses this move is nifty_midcap_100, which has already reacted. Other correlated instruments, such as dyn_jiofin_bo and nifty_50, have not moved significantly yet.
- Watch next: dyn_jiofin_bo (down) — not yet - watch; historically leads by 2d
- **India receivers**: dyn_jiofin_bo (rho 0.598, z -0.39); nifty_50 (rho 0.58, z 0.4); nifty_midcap_100 (rho 0.537, z 1.27); nifty_fmcg (rho 0.493, z -0.66)
- Source: Havells India’s margin recovery hinges on easing A&P spends, price hikes after weak Q1 — Mint Markets, 2026-07-20. https://www.livemint.com/market/mark-to-market/havells-q1fy27-results-margin-pressure-renewables-lloyd-growth-analysis-11784520642325.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-22 (d=0.01), 2025-06-30 (d=0.02)

## Watchlist (below surfacing floor)
dyn_pypl ↑ (4.35), commodities · 3 series ↑ (4.29), dyn_icicigi_bo ↓ (4.18), shanghai_comp ↓ (3.59), nikkei_225 ↓ (3.52), gold_silver_ratio ↑ (3.26), usd_cny ↓ (3.23), usd_inr ↑ (3.13), dyn_adanient_bo ↑ (3.1), dyn_ohi ↑ (3.03), dyn_bac ↑ (3.01), fx · 2 series ↑ (2.99)

## India macro
- nifty_50: 24173.9004 (1d -0.27%, z20 0.40, flag none)
- nifty_midcap_100: 62934.5000 (1d 0.18%, z20 1.27, flag amber)
- usd_inr: 96.2400 (1d -0.05%, z20 1.13, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6034 (1d 0.45%, z20 0.96, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 70.6 — "SBI Funds Management IPO listing date today. GMP, analysts signal strong debut of shares i"
- INOXINDIA.NS (INOX INDIA LIMITED) score 65.2 — "Transition VC launches ₹1,500 cr Fund II to double down on India’s energy transition oppor"
- HDB (HDFC Bank Limited) score 62.9 — "Karur Vysya Bank net profit surges 45% to Rs 756 crore in Q1, asset quality sees slight sl"
- BAC (Bank of America Corporation) score 58.3 — "Karur Vysya Bank net profit surges 45% to Rs 756 crore in Q1, asset quality sees slight sl"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 58.1 — "Karur Vysya Bank net profit surges 45% to Rs 756 crore in Q1, asset quality sees slight sl"
- IDBI.NS (IDBI BANK LIMITED) score 47.6 — "Karur Vysya Bank net profit surges 45% to Rs 756 crore in Q1, asset quality sees slight sl"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 43.6 — "Millworks Technologies shares make stellar debut, list at 90% premium on BSE SME"
- COIN (Coinbase Global, Inc.) score 39.3 — "Global Market:  Japan's Nikkei rebounds as bargain buying lifts stocks after sharp weekly "
- TECHM.NS (TECH MAHINDRA LIMITED) score 31.6 — "Millworks Technologies shares make stellar debut, list at 90% premium on BSE SME"
- CHKP (Check Point Software Technolog) score 22.5 — "Triveni Engineering demerger: Last day to buy stock to get Triveni Power Transmission shar"
- OHI (Omega Healthcare Investors, In) score 18.4 — "India’s demat boom hits a trading slowdown as retail investors step away"
- BOND (PIMCO Active Bond Exchange-Tra) score 18.2 — "Lotus Petal opens first SSE bond issue since CSR rule change"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 17.2 — "Transition VC launches ₹1,500 cr Fund II to double down on India’s energy transition oppor"
- VT (Vanguard Total World Stock Ind) score 15.3 — "Alpine Texworld shares list flat at IPO price of Rs 105 on BSE, NSE"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 15.2 — "Transition VC launches ₹1,500 cr Fund II to double down on India’s energy transition oppor"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 12.4 — "Cause for concern? HDFC Bank is lagging ICICI Bank where it matters as investors count Rs "
- JIOFIN.BO (Jio Financial Services Limited) score 9.8 — "FRENCH FOREIGN MINISTER BARROT: TWO EMBASSY OFFICIALS WERE SERIOUSLY INTIMIDATED BY IRANIA"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.9 — "Expert view: Overweight on diversified financials, automobiles, new age tech firms, says N"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.3 — "Lumentum’s stock just got a lot more interesting — and Barclays has turned bullish"
- META (Meta) score 8.2 — "Market Trading Guide: Lloyds Metals among 2 stock recommendations for Tuesday"
- GS (Goldman Sachs Group, Inc. (The) score 7.2 — "Paytm shares gain 3% after Q1 results. What are Goldman Sachs, Citi and CLSA saying?"
- NVDA (NVIDIA Corporation) score 6.0 — "Nvidia among 6 megacaps that Morningstar says are undervalued. See full list"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.7 — "Stocks to watch: Bajaj Auto, Adani Energy, Paytm among shares in focus today; check list h"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 5.7 — "Global Market: Private capital crucial to Europe's defence push as funding bottlenecks per"
- MS (Morgan Stanley) score 5.5 — "MORGAN STANLEY: DIESEL MARKET STAYS TIGHT Morgan Stanley says Europe’s record-high diesel "
- NFLX (Netflix, Inc.) score 5.2 — "US stocks to buy for short term: From Nvidia to Netflix- Appreciate CEO suggests picking t"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 5.1 — "Tata Technologies Q1 Results: Profit rises 6% to Rs 180 crore"
- PCJEWELLER.NS (PC JEWELLER LTD) score 4.7 — "BlueStone Jewellery shares to be in focus on Tuesday as company turns profitable in Q1, re"
- SKHYV (SK hynix Inc. American Deposit) score 4.7 — "SKHY – SK HYNIX DOWN 0.7% IN PREMARKET SK Hynix shares are slipping 0.7% in premarket afte"
- BHEL.NS (BHEL) score 4.5 — "BHEL share price: Brokerages see up to 23% upside after Maharatna PSU posts first Q1 profi"
- WIT (Wipro Limited) score 4.3 — "Stocks to watch: Reliance Industries, Wipro, CEAT among shares in focus today; check list "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 4.0 — "Karur Vysya Bank net profit surges 45% to Rs 756 crore in Q1, asset quality sees slight sl"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 3.7 — "ETMarkets Smart Talk | Power, electricals and cooling could be biggest winners of India’s "
- AAPL (Apple Inc.) score 3.2 — "Dollar near one-week high as markets grapple with Gulf tensions"
- CEATLTD.NS (CEAT LIMITED) score 2.4 — "Top Gainers & Losers on 20 July: Axis Bank, HDFC Bank, Ceat, India Cements, OLA, HFCL amon"
- PYPL (PayPal Holdings, Inc.) score 2.1 — "Global Market: PayPal takeover talks intensify as board mulls improved bid"
- KO (Coca-Cola Company (The)) score 1.8 — "Coca-Cola names JPMorgan, Citi as bankers for India bottling unit IPO"
- BIOCON.BO (BIOCON LTD.) score 1.0 — "Mylan exits Biocon, sells entire 5.64% stake for ₹3,679 crore via block deals"
- CUPID.NS (CUPID LIMITED) score 0.7 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"
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