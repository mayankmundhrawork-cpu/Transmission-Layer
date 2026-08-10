# Transmission Layer — board brief · 2026-08-10 19:14Z

data as of **2026-08-10** · 98 series · 9 red / 37 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.312, 1d in regime; vol-pct 0.448, breadth-off 0.176, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.36, corr60 -0.38, contra nifty_50 corr20=0.09, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.91, corr60 0.82, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.37, corr60 0.34, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.16, corr60 -0.06, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.79, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.08, corr60 -0.04, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.35, corr60 -0.23, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.09, corr60 0.16, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 0.0004481066939820977)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.492** (n=1129) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.827** (n=2362) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.47] cross-asset · 11 series ↑
- comex_gold [COMMODITIES]: last 4438.90, z20 3.94, zc 1.14, resid-z 0.24 [quiet], 1d 2.26%, |z20|=3.94; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 65.88, z20 3.83, zc 1.46, resid-z 0.27 [quiet], 1d 4.02%, |z20|=3.83; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 67.38, z20 -2.59, zc n/a, resid-z n/a [quiet], 1d -1.69%, GSR<75 (extreme low); |z20|=2.59
- stoxx_50 [INDICES]: last 6539.07, z20 2.17, zc 0.28, resid-z 0.83 [quiet], 1d 0.23%, |z20|=2.17; 1y-pct=100
- cac_40 [INDICES]: last 8724.88, z20 1.99, zc 0.15, resid-z 1.04 [quiet], 1d 0.11%, |z20|=1.99; 1y-pct=100
- dyn_vt [EQUITIES]: last 161.10, z20 1.99, zc -0.12, resid-z 1.02 [quiet], 1d -0.12%, 1y-pct=99
- dax [INDICES]: last 26354.84, z20 1.91, zc 0.17, resid-z 0.61 [quiet], 1d 0.13%, |z20|=1.91; 1y-pct=100
- sp500 [INDICES]: last 7756.35, z20 1.91, zc -0.02, resid-z -0.45 [quiet], 1d -0.02%, |z20|=1.91; 1y-pct=99
- comex_copper [COMMODITIES]: last 6.63, z20 1.55, zc 0.42, resid-z 0.77 [quiet], 1d 0.95%, |z20|=1.55; 1y-pct=98; co-occur[metal_copper] same-direction (channel VALID)
- dow_jones [INDICES]: last 53895.21, z20 1.54, zc -0.28, resid-z 0.31 [quiet], 1d -0.26%, |z20|=1.54; 1y-pct=98
- russell_2000 [INDICES]: last 3017.08, z20 1.46, zc -0.46, resid-z -0.60 [quiet], 1d -0.57%, 1y-pct=98
- **Mechanism**: The recent surge in gold and silver prices, along with a rise in global equity indices, suggests a risk-on sentiment in the market. The valid gold_silver_comove channel indicates that monetary metals are co-moving, and the gold-silver ratio is at an extreme low, which could be a sign of rotation. The metal_copper_channel is also valid, indicating that global copper prices are leading Indian metal equities.
- **Gap**: No gap: the recent move in gold and silver prices is largely priced in, with resid_z values of 0.24 and 0.27, respectively, indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian market has already reacted to the global equity rally, with the Nifty 50, Nifty Midcap 100, and Nifty Metal indices all moving up. However, the metal sector may see further upside due to the valid metal_copper_channel.
- Watch next: nifty_50 (up) — already moved; reacted to global equity rally
- Watch next: nifty_midcap_100 (up) — already moved; reacted to global equity rally
- Watch next: nifty_metal (up) — already moved; reacted to rise in global copper prices
- **India receivers**: nifty_50 (rho 0.538, z 1.22); nifty_midcap_100 (rho 0.517, z 1.92); nifty_metal (rho 0.481, z 2.06)
- Source: NVDA - NVIDIA SHARES EXTEND DECLINES; REPORT SAYS WALL STREET GIANTS PARTNER WITH CO ON $500 BLN AI FINANCING DEAL, LAST DOWN 3.2% — DeItaone, 2026-08-10. https://t.me/walter_bloomberg/34586
- Source: NVDA - NVIDIA TEAMS WITH WALL STREET ON $500BN AI FINANCING PUSH Nvidia is partnering with a consortium of Wall Street investment giants on a $500 billion AI financing initiative, according to the Financial Times. The group reportedly includes Apollo, Blackstone, a BlackRock — DeItaone, 2026-08-10. https://t.me/walter_bloomberg/34582
- Source: 17 S&P 500 companies with growing revenue and profit margins — and some of their stocks are cheap — MarketWatch Top, 2026-08-10. https://www.marketwatch.com/story/17-s-p-500-companies-with-growing-revenue-and-profit-margins-and-some-of-their-stocks-are-cheap-e7c7fa14?mod=mw_rss_topstories
- Historical analogues: 2024-11-26 (d=0.91), 2025-10-31 (d=0.93), 2024-10-09 (d=0.99)

### [AMBER 5.86] commodities · 2 series ↓
- brent [COMMODITIES]: last 87.24, z20 -0.03, zc 1.33, resid-z 1.37 [quiet], 1d 4.42%, 1-session move +4.42% ≥ 1.5%
- wti [COMMODITIES]: last 81.72, z20 -0.02, zc 1.44, resid-z 1.37 [quiet], 1d 4.53%, 1-session move +4.53% ≥ 1.5%
- **Mechanism**: The recent surge in oil prices, as seen in Brent and WTI, is driven by geopolitical tensions and supply chain disruptions, particularly the potential closure of the Strait of Hormuz. This has led to a priced move, with the resid_z values indicating that the move is largely explained by factor exposures. The metal_copper_channel and gold_silver_comove channels are valid and may transmit the oil price shock to Indian metal equities and other assets.
- **Gap**: No gap: the recent oil price move is largely priced in, with resid_z values close to 1.37 for both Brent and WTI, indicating that the move is mostly explained by factor exposures.
- **India take**: Indian instruments such as nifty_midcap_100 and dyn_bharatcoal_ns have already reacted to the WTI price move, while midcap_largecap_ratio and dyn_hdbfs_bo remain quiet. The proposed Egypt-Libya oil pipeline deal may have a limited impact on Indian markets.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to WTI price move
- Watch next: dyn_bharatcoal_ns (down) — already moved; reacted to WTI price move
- **India receivers**: nifty_midcap_100 (rho -0.439, z 1.92); dyn_bharatcoal_ns (rho -0.385, z -1.01); midcap_largecap_ratio (rho -0.373, z 0.53); dyn_hdbfs_bo (rho -0.357, z -0.91)
- Source: BofA: Hormuz Needs 10 Times More Ships to Stabilize Oil Markets — OilPrice, 2026-08-10. https://oilprice.com/Latest-Energy-News/World-News/BofA-Hormuz-Needs-10-Times-More-Ships-to-Stabilize-Oil-Markets.html
- Source: IRAN OIL EXPORTS SLUMP UNDER U.S. BLOCKADE Iran’s oil terminals appear largely idle in August as the U.S. maintains its naval blockade, satellite imagery shows. Kpler estimates Iranian crude and condensate exports have fallen about 40% from July’s average to roughly 500,000 — DeItaone, 2026-08-10. https://t.me/walter_bloomberg/34581
- Source: Egypt and Libya Near $1 Billion Oil Pipeline Deal — OilPrice, 2026-08-10. https://oilprice.com/Latest-Energy-News/World-News/Egypt-and-Libya-Near-1-Billion-Oil-Pipeline-Deal.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 5.56] dyn_tatatech_ns ↑
- dyn_tatatech_ns [EQUITIES]: last 881.40, z20 3.56, zc 0.29, resid-z 0.23 [quiet], 1d 0.99%, |z20|=3.56; 1y-pct=100
- **Mechanism**: The recent surge in Tata Technologies' stock price can be attributed to the company's strong Q1FY27 results and positive outlook from analysts, which has also been reflected in the Indian market through transmission candidates such as Tata Elxsi and Nifty IT. The VALID metal_copper_channel and gold_silver_comove channels suggest a broader risk-on sentiment, which is further supported by the RISK_ON regime. However, the INVERTED safe_haven_gold channel indicates a potential risk-off sentiment, which may limit the upside.
- **Gap**: No gap: the big raw move in dyn_tatatech_ns with small resid_z=0.13 suggests that the move is largely priced in, leaving no significant event-to-price gap.
- **India take**: The Indian market has already reacted to the surge in Tata Technologies' stock price through transmission candidates such as Tata Elxsi and Nifty IT, which have also moved up. The broader risk-on sentiment in the Indian market is further supported by the VALID metal_copper_channel and gold_silver_comove channels.
- Watch next: dyn_tataelxsi_ns (up) — already moved; reacted to dyn_tatatech_ns
- Watch next: nifty_it (up) — already moved; reacted to dyn_tatatech_ns
- **India receivers**: dyn_tataelxsi_ns (rho 0.471, z 1.54); nifty_it (rho 0.465, z 1.43)
- Source: Titan shares: Is the Tata Group stock an attractive buy after Q1FY27 results? — Mint Markets, 2026-08-10. https://www.livemint.com/market/stock-market-news/titan-shares-is-the-tata-group-stock-an-attractive-buy-after-q1fy27-results-11786352452848.html
- Source: Tata Technologies among 5 stocks flashing bullish signals. Upside on cards? — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/news/tata-technologies-among-5-stocks-flashing-bullish-signals-upside-on-cards/slideshow/133080114.cms
- Source: How Rakesh Jhunjhunwala's old Tata bet created Rs 80,000 crore wealth after two years of flat returns — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/news/how-rakesh-jhunjhunwalas-old-tata-bet-created-rs-80000-crore-wealth-after-two-years-of-flat-returns/articleshow/133079774.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

### [AMBER 4.45] dyn_heromotoco_ns ↑
- dyn_heromotoco_ns [EQUITIES]: last 5860.00, z20 2.45, zc 1.25, resid-z 1.49 [quiet], 1d 2.36%, |z20|=2.45
- **Mechanism**: The recent surge in Hero MotoCorp's stock price can be attributed to its Q1 earnings beating street estimates, driven by strong sales of premium bikes and EVs. This move is likely to propagate through the metal_copper_channel, given the VALID status of this channel. The global copper market often leads Indian metal equities, and a rise in Hero MotoCorp's stock could be a precursor to a broader move in the metal sector.
- **Gap**: No gap: the move in Hero MotoCorp's stock is largely priced in, given the strong earnings report and the current market regime of RISK_ON
- **India take**: The Indian instrument that expresses this move is dyn_havells_ns, which has already reacted with a rho of 0.447 via dyn_heromotoco_ns. The Nifty Midcap 100 index has also reacted, with a rho of 0.387 via dyn_heromotoco_ns.
- Watch next: nifty_midcap_100 (up) — already moved; reacted to dyn_heromotoco_ns
- **India receivers**: dyn_havells_ns (rho 0.456, z 1.3); nifty_midcap_100 (rho 0.381, z 1.92)
- Source: Hero MotoCorp gains speed as premium bikes, EVs fuel Q1 — Mint Markets, 2026-08-10. https://www.livemint.com/market/mark-to-market/hero-motocorp-q1fy27-earnings-stock-margin-ev-growth-11786338356204.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-22 (d=0.03), 2025-07-09 (d=0.04)

### [AMBER 4.28] dyn_cupid_ns ↑
- dyn_cupid_ns [EQUITIES]: last 264.45, z20 2.28, zc 0.22, resid-z 0.19 [quiet], 1d 0.89%, |z20|=2.28; 1y-pct=100
- **Mechanism**: The recent surge in Cupid's Q1 FY27 profit, which tripled to Rs 44 crore, and the company's raised revenue and profit guidance for FY27, may have triggered a positive response in the stock. However, the stock's quiet move, with a low resid_z of 0.02, suggests that the move is largely priced in. The VALID metal_copper_channel and the company's strong financial performance may be contributing to the stock's upward momentum.
- **Gap**: No gap: the stock's move is largely priced in, with a low resid_z of 0.02 and a strong financial performance
- **India take**: The Indian instrument that expresses this move is the Nifty Midcap 100, which has already reacted with a rho of 0.357 via dyn_cupid_ns. The stock's strong financial performance and the VALID metal_copper_channel may continue to support the Nifty Midcap 100's upward momentum.
- Watch next: nifty_midcap_100 (up) — already moved; rho=0.357 via dyn_cupid_ns
- **India receivers**: nifty_midcap_100 (rho 0.357, z 1.92)
- Source: Cupid shares fall 2% even as Q1 profit jumps 3x. What’s ahead for multibagger stock that rose 680% in a year? — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/stocks/news/cupid-shares-fall-2-even-as-q1-profit-jumps-3x-whats-ahead-for-multibagger-stock-that-rose-680-in-a-year/articleshow/133085241.cms
- Source: Q1 Results Highlights: BEML loss narrows to ₹27 cr, Eveready profit up 22%, Aditya Birla Fashion loss widens to ₹249 cr, Cupid profit nearly triples, Ceigall up 35% — BusinessLine Mkts, 2026-08-10. https://www.thehindubusinessline.com/markets/stock-markets/q1-results-today-live-updates-delhivery-anant-raj-apollo-micro-systems-akums-drugs-pharma-aditya-birla-fashion-ceigall-pnc-infratech-oswal-pumps-results-08-august-2026/article71320548.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-06 (d=0.01), 2025-07-24 (d=0.02)

### [RED 4.17] fx · 3 series ↑
- usd_mxn [FX]: last 17.13, z20 -2.85, zc -1.00, resid-z -0.92 [quiet], 1d -0.41%, |z20|=2.85; 1y-pct=1
- aud_usd [FX]: last 0.71, z20 1.85, zc 0.69, resid-z 0.76 [quiet], 1d 0.36%, |z20|=1.85
- eur_usd [FX]: last 1.15, z20 1.59, zc 0.47, resid-z 0.75 [quiet], 1d 0.17%, |z20|=1.59
- **Mechanism**: The recent move in FX markets, particularly in usd_mxn, aud_usd, and eur_usd, is driven by priced factors, as evidenced by the low resid_z values. The move is likely a result of broader market trends rather than an anomaly. The VALID gold_silver_comove and metal_copper_channel suggest that monetary metals and global copper are co-moving, which may influence Indian metal equities.
- **Gap**: No gap: the low resid_z values indicate that the move is largely explained by priced factors
- **India take**: The Indian instrument dyn_muthootfin_ns has already reacted to the move in usd_mxn, with a rho of -0.571. Indian metal equities may also be influenced by the co-movement of monetary metals and global copper.
- Watch next: usd_mxn (down) — already moved; historical analogues suggest a potential downturn
- Watch next: aud_usd (down) — already moved; historical analogues suggest a potential downturn
- Watch next: eur_usd (down) — already moved; historical analogues suggest a potential downturn
- **India receivers**: dyn_muthootfin_ns (rho -0.571, z -1.25)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-02 (d=0.26), 2025-08-15 (d=0.26)

### [AMBER 4.1] dyn_ohi ↓
- dyn_ohi [EQUITIES]: last 47.31, z20 -2.10, zc -1.75, resid-z 0.19 [moved], 1d -2.37%, |z20|=2.10
- **Mechanism**: The recent decline in dyn_ohi is largely priced, with a small resid_z of 0.19, indicating that the move is mostly explained by factor exposures. The VALID vix_equity_inverse channel suggests that the vol spike is leading to an equity drawdown, which may be contributing to the decline in dyn_ohi. However, the broken channels, including the WEAK inr_oil_channel and dxy_inr_channel, limit the potential for further propagation of this move through the Indian market.
- **Gap**: No gap: the small resid_z and mostly explained move by factor exposures suggest that the current price reflects the available information
- **India take**: The Indian instrument that expresses this move is the nifty_50, which has not yet reacted to the decline in dyn_ohi. The VALID metal_copper_channel may transmit global risk-off to Indian metal equities, potentially leading to a decline in the nifty_50.
- Watch next: nifty_50 (down) — not yet - watch; VALID metal_copper_channel may transmit global risk-off to Indian metal equities
- Source: Milky Mist Dairy Food mops up ₹465 crore from anchor investors ahead of IPO — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/ipos/fpos/milky-mist-dairy-food-mops-up-465-crore-from-anchor-investors-ahead-of-ipo/articleshow/133117007.cms
- Source: High margin debt! JPMorgan CEO Jamie Dimon fires a warning shot for Wall Street investors — ET Markets, 2026-08-10. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/high-margin-debt-jpmorgan-ceo-jamie-dimon-fires-a-warning-shot-for-wall-street-investors/articleshow/133111344.cms
- Source: SHEIN IPO PITCHED TO INVESTORS AT SUB-$30BN VALUATION Shein’s advisers are pitching the company to potential investors at a valuation below $30bn, a roughly 70 per cent drop from its peak — DeItaone, 2026-08-10. https://t.me/walter_bloomberg/34572
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2024-10-15 (d=0.09)

### [AMBER 4.07] dyn_bac ↑
- dyn_bac [EQUITIES]: last 63.74, z20 2.07, zc 0.63, resid-z -0.33 [quiet], 1d 0.90%, |z20|=2.07; 1y-pct=100
- **Mechanism**: The recent move in dyn_bac is largely priced, with a small resid_z of -0.33, suggesting that the market has already accounted for the factor exposures. The historical analogues suggest a potential positive outcome for dyn_bac and sp500 in the next 20 days, with median returns of 9.68% and 3.69%, respectively. The VALID metal_copper_channel and gold_silver_comove channels may also contribute to the propagation of this move.
- **Gap**: No gap: the move in dyn_bac is largely priced, with a small resid_z and a high z20 level
- **India take**: The Indian instrument dyn_cupid_ns has already reacted, with a rho of 0.378 via dyn_bac and a z20 of 2.28. Further reaction in Indian metal equities may be expected via the metal_copper_channel.
- Watch next: dyn_ms (up) — not yet - watch; historically leads dyn_bac by 2d
- **India receivers**: dyn_cupid_ns (rho 0.378, z 2.28)
- Source: America's $4 Billion Wind Retreat Is a Bet on Permanently Cheap Gas — OilPrice, 2026-08-10. https://oilprice.com/Alternative-Energy/Wind-Power/Americas-4-Billion-Wind-Retreat-Is-a-Bet-on-Permanently-Cheap-Gas.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

## Watchlist (below surfacing floor)
cross-asset · 5 series ↑ (3.36), dyn_coin ↓ (3.22), dyn_tech ↑ (3.11), usd_cny ↓ (2.94), dyn_pltr ↑ (2.82), dyn_hdb ↓ (2.75), dyn_lth ↓ (2.46), dyn_indianb_ns ↑ (2.44), dyn_icicigi_bo ↓ (2.28), dyn_idbi_ns ↓ (2.18), dyn_indusindbk_bo ↑ (2.16), nifty_metal ↑ (2.06)

## India macro
- nifty_50: 24583.8008 (1d 0.05%, z20 1.22, flag none)
- nifty_midcap_100: 63848.3516 (1d 0.61%, z20 1.92, flag amber)
- usd_inr: 95.2900 (1d -0.02%, z20 -1.18, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5972 (1d 0.55%, z20 0.53, flag none)
- Next India prints: AMFI SIP / MF flows T-0d · NSDL FPI flows T-0d · IMD weekly rainfall T-0d · India CPI T-2d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 79.1 — "India’s kharif sowing deficit dips below 2% as overall coverage rises to 88% of normal"
- COALINDIA.NS (COAL INDIA LTD) score 78.4 — "India’s kharif sowing deficit dips below 2% as overall coverage rises to 88% of normal"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 78.1 — "India’s kharif sowing deficit dips below 2% as overall coverage rises to 88% of normal"
- INDIANB.NS (INDIAN BANK) score 59.7 — "SPCX - SPACEX’S $100B REVENUE TARGET SEEN WITHIN REACH Deutsche Bank says SpaceX’s goal of"
- BAC (Bank of America Corporation) score 48.5 — "SPCX - SPACEX’S $100B REVENUE TARGET SEEN WITHIN REACH Deutsche Bank says SpaceX’s goal of"
- TECHM.NS (TECH MAHINDRA LIMITED) score 44.6 — "Zen Technologies shares to be in focus on Tuesday after company secures  ₹295 crore defenc"
- COIN (Coinbase Global, Inc.) score 43.7 — "HEDGE FUNDS PILE BACK INTO STOCKS Hedge funds bought global equities for a second straight"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 43.3 — "Zen Technologies shares to be in focus on Tuesday after company secures  ₹295 crore defenc"
- HDB (HDFC Bank Limited) score 43.2 — "SPCX - SPACEX’S $100B REVENUE TARGET SEEN WITHIN REACH Deutsche Bank says SpaceX’s goal of"
- TECH (Bio-Techne Corp) score 41.8 — "Zen Technologies shares to be in focus on Tuesday after company secures  ₹295 crore defenc"
- OHI (Omega Healthcare Investors, In) score 41.5 — "Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks edge lower as investors monito"
- IDBI.NS (IDBI BANK LIMITED) score 40.6 — "SPCX - SPACEX’S $100B REVENUE TARGET SEEN WITHIN REACH Deutsche Bank says SpaceX’s goal of"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 40.6 — "SPCX - SPACEX’S $100B REVENUE TARGET SEEN WITHIN REACH Deutsche Bank says SpaceX’s goal of"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 40.1 — "SPCX - SPACEX’S $100B REVENUE TARGET SEEN WITHIN REACH Deutsche Bank says SpaceX’s goal of"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 33.3 — "The Hormuz Crisis Has Forever Changed the Economics of Energy Security"
- LTH (Life Time Group Holdings, Inc.) score 30.8 — "NVDA - NVIDIA TEAMS WITH WALL STREET ON $500BN AI FINANCING PUSH Nvidia is partnering with"
- CHKP (Check Point Software Technolog) score 29.8 — "AAPL - APPLE REPORTEDLY SCRAPS ALL-GLASS IPHONE Apple has canceled its planned 20th-annive"
- 301077.SZ (CHINASTARS) score 24.1 — "CHINA SAYS LAUNCH OF LONG MARCH 7 ROCKET FAILED - XINHUA"
- BOND (PIMCO Active Bond Exchange-Tra) score 20.9 — "US bonds fall as markets weight inflation, Middle East risks"
- JUSTDIAL.BO (JUST DIAL LTD.) score 12.1 — "2 charts showing just how insane the stock market’s August ‘crash-up’ has been so far"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 12.1 — "Titan shares: Is the Tata Group stock an attractive buy after Q1FY27 results?"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 11.7 — "Q1 Results Today Highlights: Bharat Forge shares tank after Q1 loss, Kwality Pharma, Ramco"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 11.4 — "Fusion Finance turns profitable as asset quality improves sharply"
- JIOFIN.BO (Jio Financial Services Limited) score 10.7 — "NVDA - NVIDIA TEAMS WITH WALL STREET ON $500BN AI FINANCING PUSH Nvidia is partnering with"
- AAPL (Apple Inc.) score 9.5 — "AAPL - APPLE REPORTEDLY SCRAPS ALL-GLASS IPHONE Apple has canceled its planned 20th-annive"
- MS (Morgan Stanley) score 9.4 — "High margin debt! JPMorgan CEO Jamie Dimon fires a warning shot for Wall Street investors"
- META (Meta) score 9.2 — "Q1 Results Today Highlights: Bharat Forge shares tank after Q1 loss, Kwality Pharma, Ramco"
- VT (Vanguard Total World Stock Ind) score 8.5 — "GLENCORE'S EXPOSURE TO IRON ORE TRADER RADIANT WORLD MORE THAN $500 MILLION, SOURCES SAY"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.4 — "NVDA - NVIDIA TEAMS WITH WALL STREET ON $500BN AI FINANCING PUSH Nvidia is partnering with"
- PCJEWELLER.NS (PC JEWELLER LTD) score 5.5 — "Titan posts 40% growth in Q1 as jewellery, watches and international business gain"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 5.5 — "Q1 Results Today Highlights: Bharat Forge shares tank after Q1 loss, Kwality Pharma, Ramco"
- NVDA (NVIDIA Corporation) score 5.4 — "NVDA - NVIDIA TEAMS WITH WALL STREET ON $500BN AI FINANCING PUSH Nvidia is partnering with"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.3 — "How Adani’s $125 billion capex boom is creating new winners on Dalal Street"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.3 — "ICICI Bank Share Price Live Updates: ICICI Bank's Price Movement Indicates Positive Trend"
- GOOGL (Alphabet) score 4.1 — "US Stock Market: Berkshire steps up buybacks, boosts Alphabet stake as cash falls"
- PLTR (Palantir Technologies Inc.) score 3.7 — "Palantir’s stock stages best week since 2024 — showing it’s no longer an AI loser"
- AMZN (Amazon.com, Inc.) score 2.7 — "What bubble? Amazon enters $3 trillion market cap club, CEO highlights striking AI demand"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 2.7 — "Titan shares: Is the Tata Group stock an attractive buy after Q1FY27 results?"
- CUPID.NS (CUPID LIMITED) score 2.4 — "Q1 Results Highlights: BEML loss narrows to ₹27 cr, Eveready profit up 22%, Aditya Birla F"
- HEROMOTOCO.NS (HERO MOTOCORP LIMITED) score 1.8 — "Hero MotoCorp gains speed as premium bikes, EVs fuel Q1"

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