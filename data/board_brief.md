# Transmission Layer — board brief · 2026-07-24 17:58Z

data as of **2026-07-24** · 98 series · 9 red / 32 amber · 8 events surfaced (28 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.57, 1d in regime; vol-pct 0.67, breadth-off 0.471, Markov P(high-vol) 0.032)
- [INVERTED] **safe_haven_gold** — corr20 -0.36, corr60 -0.45, contra nifty_50 corr20=0.13, last shift 2026-06-01. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.89, corr60 0.82, last shift 2026-05-15. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.51, corr60 0.35, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.07, corr60 -0.03, last shift 2026-06-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.82, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.12, corr60 -0.09, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [INVERTED] **real_rates_gold_inverse** — corr20 0.25, corr60 -0.24, last shift 2026-05-08. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.56, corr60 0.25, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** hy_oas → usd_brl: leads 1d (ccf 0.266, β 0.0929, p 4e-05); driver zc 2.46 → expected 0.312%. Type hit-rate 0.821 (n=3022).
- Track record · residual_reversion: hit-rate **0.491** (n=1163) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.821** (n=3022) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.706** (n=17) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.68] commodities · 2 series ↑
- brent [COMMODITIES]: last 96.31, z20 1.85, zc -1.15, resid-z -1.26 [quiet], 1d -4.35%, 1-session move -4.35% ≥ 1.5%; |z20|=1.85; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 88.87, z20 1.84, zc -1.12, resid-z -0.98 [quiet], 1d -3.60%, 1-session move -3.60% ≥ 1.5%; |z20|=1.84
- **Mechanism**: The recent surge in oil prices, driven by a potential supply-driven oil shock and the possibility of a 'super' El Niño event, is propagating through the commodities channel. However, the move is largely priced, with brent and wti showing small resid_z values of -1.26 and -0.98, respectively, indicating that the current price levels are largely explained by factor exposures.
- **Gap**: No gap: the current price levels of brent and wti are largely explained by factor exposures, with small resid_z values indicating that the move is priced
- **India take**: The Indian instruments, such as nifty_midcap_100 and nifty_50, have already reacted to the brent price movement, with a negative correlation. The dyn_hdbfs_bo has also reacted, with a z20 value of -2.88.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to brent price movement
- **India receivers**: nifty_midcap_100 (rho -0.656, z -1.28); nifty_50 (rho -0.504, z -1.94); dyn_hdbfs_bo (rho -0.487, z -2.88)
- Source: Oil Shock Could Turn Super El Niño Into an Inflation Problem Again — OilPrice, 2026-07-24. https://oilprice.com/Latest-Energy-News/World-News/Oil-Shock-Could-Turn-Super-El-Nio-Into-an-Inflation-Problem-Again.html
- Source: US Oil Drillers Take A Break As Oil Prices Hover Near $100 — OilPrice, 2026-07-24. https://oilprice.com/Energy/Crude-Oil/US-Oil-Drillers-Take-A-Break-As-Oil-Prices-Hover-Near-100.html
- Source: Saudi Red Sea Crude Exports Have Sank 41% Since March Peak — OilPrice, 2026-07-24. https://oilprice.com/Latest-Energy-News/World-News/Saudi-Red-Sea-Crude-Exports-Have-Sank-41-Since-March-Peak.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 6.85] cross-asset · 5 series ↑
- ust_2y [RATES]: last 4.31, z20 2.92, zc 0.91, resid-z 1.09 [quiet], 1d 1.17%, |z20|=2.92; 1y-pct=100
- ust_10y [RATES]: last 4.67, z20 2.05, zc 0.90, resid-z 0.85 [quiet], 1d 0.86%, |z20|=2.05; 1y-pct=99
- tips_10y_real [RATES]: last 2.39, z20 1.74, zc 0.49, resid-z 0.30 [quiet], 1d 0.84%, |z20|=1.74; 1y-pct=100
- dyn_bond [EQUITIES]: last 90.55, z20 -1.65, zc 0.41, resid-z -0.22 [quiet], 1d 0.12%, 1y-pct=0
- ust_30y [RATES]: last 5.15, z20 1.60, zc 0.61, resid-z 0.37 [quiet], 1d 0.39%, |z20|=1.60; 1y-pct=99
- **Mechanism**: The recent move in US Treasury yields, led by the 2-year and 10-year bonds, is driven by a repricing of interest rate expectations. This move is largely priced, as indicated by the relatively small resid_z values. The correlated instruments that have not moved, such as the 2s10s spread and the S&P 500, suggest that the current move is primarily driven by rate expectations rather than a broader risk-off sentiment.
- **Gap**: No gap: The move in US Treasury yields is largely priced, and the resid_z values are relatively small, indicating that the current price reflects the expected rate moves.
- **India take**: The Indian instrument that expresses this move is the 10-year Government of India bond yield, which may react to the transmission of US rate expectations. However, the GoI-UST comove channel is currently insufficiently calibrated, making it difficult to predict the exact reaction.
- Watch next: ust_2y (up) — already moved; Rate expectations repricing
- Watch next: ust_10y (up) — already moved; Rate expectations repricing
- Watch next: nifty_50 (down) — not yet - watch; Potential transmission of US rate expectations to Indian markets
- Source: Indonesia raises $1.03 billion in debut panda bond sale — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/bonds/indonesia-raises-1-03-billion-in-debut-panda-bond-sale/articleshow/132605293.cms
- Source: Why fixing the housing crisis for under-40s could trigger 10% Treasury yields — MarketWatch Top, 2026-07-24. https://www.marketwatch.com/story/why-fixing-the-housing-crisis-for-under-40s-could-trigger-10-treasury-yields-04c65b78?mod=mw_rss_topstories
- Source: Global market: Euro zone bond yields ease after multi-year highs as oil retreats below $100 — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-bond-yields-ease-after-multi-year-highs-as-oil-retreats-below-100/articleshow/132601832.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.45] usd_jpy ↑
- usd_jpy [FX]: last 163.81, z20 3.45, zc 1.44, resid-z 1.56 [unexplained], 1d 0.45%, |z20|=3.45; 1y-pct=100
- **Mechanism**: The USD/JPY surge is driven by Japan's ineffective measures to bolster the yen's value, surging oil prices, and the US Treasury Department's urging of the Bank of Japan to raise interest rates, leading to a broad weakening of the yen. This move is unexplained by factors, with a resid_z of 1.56, indicating a potential anomaly. The valid metal_copper_channel and vix_equity_inverse channels may transmit this move to Indian metal equities and equity markets, respectively.
- **Gap**: No gap: the big raw move in USD/JPY has a small resid_z relative to its z20 level, indicating the move is largely priced in
- **India take**: The Indian instrument that expresses this move is the Nifty 50, which may react negatively due to potential risk-off sentiment transmission. However, the metal_copper_channel may also lead to a reaction in Indian metal equities.
- Watch next: nifty_50 (down) — not yet - watch; potential risk-off sentiment transmission
- Source: Yen heads for biggest weekly drop since May despite Tokyo's support pledges — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/forex/forex-news/yen-heads-for-biggest-weekly-drop-since-may-despite-tokyos-support-pledges/articleshow/132606629.cms
- Source: Global Market: US urges BOJ to keep raising rates, flags persistent yen weakness despite narrower yield gap — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-us-urges-boj-to-keep-raising-rates-flags-persistent-yen-weakness-despite-narrower-yield-gap/articleshow/132596001.cms
- Source: Yen’s Slump Extends Beyond Dollar and Stokes Inflation Fears — Mint Markets, 2026-07-23. https://www.livemint.com/market/yens-slump-extends-beyond-dollar-and-stokes-inflation-fears-11784836659389.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2024-11-08 (d=0.01)

### [RED 4.89] dxy ↑
- dxy [FX]: last 101.48, z20 1.89, zc 0.15, resid-z -0.69 [quiet], 1d 0.05%, 20d range extreme; |z20|=1.89; 1y-pct=99
- **Mechanism**: The recent surge in the US Dollar Index (DXY) may propagate through the VALID gold_silver_comove channel, potentially leading to a decline in gold prices. However, the INVERTED safe_haven_gold channel suggests a risk-off safe-haven bid, which could support gold prices. The VALID metal_copper_channel may also influence Indian metal equities.
- **Gap**: No gap: The DXY move is largely priced, with a small resid_z of -0.69, indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian instrument that may express this move is the MCX Gold, which may decline if the gold_silver_comove channel dominates. However, the reaction is yet to be seen.
- Watch next: comex_gold (down) — not yet - watch; Historically leads DXY by 3 days
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [RED 4.65] dyn_ohi ↑
- dyn_ohi [EQUITIES]: last 51.73, z20 2.65, zc 1.14, resid-z -0.11 [quiet], 1d 1.49%, |z20|=2.65; 1y-pct=100
- **Mechanism**: The recent surge in dyn_ohi is accompanied by a low resid_z of -0.11, indicating that the move is largely priced in by factor exposures. The valid gold_silver_comove and metal_copper_channel suggest that monetary metals and global copper are co-moving, which may influence Indian metal equities. However, the weak inr_oil_channel and dxy_inr_channel imply that the transmission of oil price and dollar strength to INR is not robust.
- **Gap**: No gap: the low resid_z indicates that the move is largely explained by factor exposures
- **India take**: Indian metal equities, such as those in the Nifty Metal index, may react to the co-movement of monetary metals and global copper, while the INR may not weaken significantly due to the weak inr_oil_channel and dxy_inr_channel.
- Watch next: nifty_50 (down) — not yet - watch; Risk-off sentiment may lead to a decline in Indian equities
- Source: Gold, silver prices today: Comex gold rebounds above $4,070; silver at $59 as investors assess Middle East tensions — Mint Markets, 2026-07-24. https://www.livemint.com/market/commodities/gold-silver-prices-today-comex-gold-rebounds-above-4-070-silver-at-59-as-investors-assess-middle-east-tensions-11784905494690.html
- Source: US stocks mixed as oil retreats below $100, fresh tariffs and earnings keep investors on edge — Mint Markets, 2026-07-24. https://www.livemint.com/market/stock-market-news/us-stocks-mixed-as-investors-digest-fresh-earnings-trump-tariffs-in-focus-11784900781196.html
- Source: US stocks today: S&P 500, Nasdaq fall as investors juggle earnings, Mideast risks and tariffs — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-today-us-stocks-open-subdued-after-tech-rout-mideast-tariffs-in-focus/articleshow/132607371.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2024-10-15 (d=0.09)

### [RED 4.6] dyn_qessf ↓
- dyn_qessf [EQUITIES]: last 0.21, z20 -2.60, zc -0.96, resid-z -0.72 [quiet], 1d -6.01%, |z20|=2.60
- **Mechanism**: dyn_qessf ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Ashish Kacholia exits defence stock that rallied 108% in Q1. Do you own it? — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/stocks/news/ashish-kacholia-exits-defence-stock-that-rallied-108-in-q1-do-you-own-it/articleshow/132597323.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-15 (d=0.32), 2024-11-14 (d=0.52)

### [AMBER 4.23] nasdaq_100 ↓
- nasdaq_100 [INDICES]: last 28319.45, z20 -2.23, zc -0.33, resid-z -0.53 [quiet], 1d -0.48%, |z20|=2.23
- **Mechanism**: nasdaq_100 ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.912 vs nasdaq_100
- Watch next: vix (inverse) — not yet - watch; rho -0.766 vs nasdaq_100
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.564 vs nasdaq_100
- Watch next: eth_usd (co-move) — not yet - watch; rho 0.533 vs nasdaq_100
- Source: US stocks today: S&P 500, Nasdaq fall as investors juggle earnings, Mideast risks and tariffs — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-today-us-stocks-open-subdued-after-tech-rout-mideast-tariffs-in-focus/articleshow/132607371.cms
- Source: US stock market today: S&P 500, Nasdaq futures edge higher as oil retreats; Intel jumps 4% — Mint Markets, 2026-07-24. https://www.livemint.com/market/stock-market-news/us-stock-market-today-s-p-500-nasdaq-futures-edge-higher-as-oil-retreats-intel-jumps-4-11784894223255.html
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Live: US stocks mixed as investors juggle earnings, Mideast risks and tariffs; oil slides 4% — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-earnings-forecast-intel-oracle-stock-price-news-2nd-july-2026/liveblog/132605239.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.0), 2025-10-07 (d=0.02)

### [AMBER 3.98] nikkei_225 ↓
- nikkei_225 [INDICES]: last 64604.84, z20 -1.98, zc -1.49, resid-z -1.49 [quiet], 1d -2.74%, |z20|=1.98
- **Mechanism**: nikkei_225 ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_hdbfs_bo (rho 0.463 via nikkei_225, z -2.88, reacted); nifty_metal (rho 0.443 via nikkei_225, z -1.61, reacted)
- **India receivers**: dyn_hdbfs_bo (rho 0.463, z -2.88); nifty_metal (rho 0.443, z -1.61)
- Source: Japan's Nikkei falls more than 2% on AI spending worries — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/us-stocks/news/japans-nikkei-falls-more-than-2-on-ai-spending-worries/articleshow/132594822.cms
- Source: Japan's Nikkei rises as chip shares gain, BOJ's rate hike prospects weigh — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/us-stocks/news/japans-nikkei-rises-as-chip-shares-gain-bojs-rate-hike-prospects-weigh/articleshow/132572655.cms
- Source: Asian stocks today: Kospi, Nikkei surge up to 4% as semiconductor stocks rally; SK Hynix, Samsung lead — Mint Markets, 2026-07-23. https://www.livemint.com/market/stock-market-news/asian-stocks-today-kospi-nikkei-surge-up-to-4-as-semiconductor-stocks-rally-sk-hynix-samsung-lead-11784770474517.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-21 (d=0.23), 2026-06-11 (d=0.6)

## Watchlist (below surfacing floor)
dyn_hdb ↓ (3.96), nifty_50 ↓ (3.94), commodities · 2 series ↑ (3.92), eur_usd ↓ (3.73), dyn_bac ↑ (3.67), dyn_patanjali_ns ↓ (3.36), dyn_aapl ↑ (3.25), usd_inr ↑ (3.2), wheat ↑ (3.06), gold_silver_ratio ↓ (3.02), dyn_lth ↑ (3.01), dyn_nflx ↓ (2.92)

## India macro
- nifty_50: 23787.0000 (1d -0.35%, z20 -1.94, flag amber)
- nifty_midcap_100: 61682.1016 (1d -0.02%, z20 -1.28, flag none)
- usd_inr: 96.5520 (1d -0.01%, z20 1.20, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5931 (1d 0.33%, z20 0.44, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 89.4 — "Bank of Baroda Q1 results Highlights: PSU Bank posts 72% decline in net profit at  ₹1278 c"
- INOXINDIA.NS (INOX INDIA LIMITED) score 84.9 — "How scrap is at the centre of India’s changing metals growth story"
- HDB (HDFC Bank Limited) score 71.0 — "Bank of Baroda Q1 results Highlights: PSU Bank posts 72% decline in net profit at  ₹1278 c"
- BAC (Bank of America Corporation) score 70.9 — "Bank of Baroda Q1 results Highlights: PSU Bank posts 72% decline in net profit at  ₹1278 c"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 67.8 — "Bank of Baroda Q1 results Highlights: PSU Bank posts 72% decline in net profit at  ₹1278 c"
- IDBI.NS (IDBI BANK LIMITED) score 62.5 — "Bank of Baroda Q1 results Highlights: PSU Bank posts 72% decline in net profit at  ₹1278 c"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 59.7 — "How scrap is at the centre of India’s changing metals growth story"
- COIN (Coinbase Global, Inc.) score 58.9 — "Trump's new global tariff draws rebukes from trade partners over forced labor justificatio"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 51.3 — "Market wrap: HCLTech, Bajaj Finance, Eternal among top gainers and losers on Nifty and Sen"
- TECHM.NS (TECH MAHINDRA LIMITED) score 48.5 — "Market wrap: HCLTech, Bajaj Finance, Eternal among top gainers and losers on Nifty and Sen"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 42.9 — "Bank of Baroda Q1 results Highlights: PSU Bank posts 72% decline in net profit at  ₹1278 c"
- COALINDIA.NS (COAL INDIA LTD) score 40.2 — "How scrap is at the centre of India’s changing metals growth story"
- OHI (Omega Healthcare Investors, In) score 35.7 — "Kalind shares jump 5% on ex-bonus, ex-split day; investors see 86% price adjustment"
- BOND (PIMCO Active Bond Exchange-Tra) score 26.3 — "India bonds end three-day losing streak but post second straight weekly decline"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 23.6 — "Juniper Green Energy to open Rs 1,800-cr IPO on July 30"
- CHKP (Check Point Software Technolog) score 23.4 — "Cube Highways Trust InvIT IPO Day 3: Issue subscribed 1.67x so far. Check GMP, issue detai"
- INFY (Infosys Limited) score 16.9 — "Infosys shares dip after Q1 results; brokerages trim target prices"
- LTH (Life Time Group Holdings, Inc.) score 16.4 — "Quote of the day by John Rogers: "All of us, all of the time, have to be on guard against "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 13.7 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Trading Update"
- JUSTDIAL.BO (JUST DIAL LTD.) score 13.4 — "Kalind shares jump 5% on ex-bonus, ex-split day; investors see 86% price adjustment"
- VT (Vanguard Total World Stock Ind) score 10.7 — "How the U.S. Became the World's LNG Superpower"
- JIOFIN.BO (Jio Financial Services Limited) score 10.6 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Financial Snapshot"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 9.6 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Financial Snapshot"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 9.5 — "ICICI Bank prices $1 billion debt in largest dollar issue by Indian private lender"
- META (Meta) score 8.5 — "How scrap is at the centre of India’s changing metals growth story"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 8.1 — "Q1 Results Today Highlights: Tata Consumer con. PAT up 28.4%, ACC PAT declines 61.5%, Shri"
- GS (Goldman Sachs Group, Inc. (The) score 8.1 — "Oil Price Today (July 23): Crude oil crosses $95 as US strikes enter 12th day. Why Goldman"
- MS (Morgan Stanley) score 7.6 — "Infosys shares fall 3% as JPMorgan downgrades stock, Jefferies cuts target after Q1 result"
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.5 — "Sebi clears IPOs of Intellius Recode, Nityas Gems & Jewellery"
- ETERNAL.NS (ETERNAL LIMITED) score 6.4 — "Market wrap: HCLTech, Bajaj Finance, Eternal among top gainers and losers on Nifty and Sen"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 5.3 — "Q1 Results Today Live: Shriram Finance, TCP, BoB, Hindustan Zinc, ACC, Dalmia Bharat, Jind"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 4.7 — "Ashish Kacholia exits defence stock that rallied 108% in Q1. Do you own it?"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 4.4 — "IEX Q1 results: Net profit grows 12% YoY to  ₹135 crore; electricity volumes rise 16%"
- NVDA (NVIDIA Corporation) score 4.2 — "AMD’s rivalry with Nvidia is increasingly moving into a new realm"
- AAPL (Apple Inc.) score 3.6 — "FORD WILL USE APPLE SOFTWARE IN NEW SELF-DRIVING SYSTEM: NYT"
- INDIGOPNTS.NS (INDIGO PAINTS LIMITED) score 3.6 — "IndiGo faces rough weather in Q1, hit by skyrocketing fuel prices"
- NFLX (Netflix, Inc.) score 3.3 — "Losing Wall Street binge premium! Why are Netflix shares in a freefall this year?"
- WIT (Wipro Limited) score 1.9 — "Stocks to watch: Reliance Industries, Wipro, CEAT among shares in focus today; check list "
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 1.0 — "Newly-listed SME stock DSM Fresh Foods jumps over 30% in 2 days after reporting a 58% YoY "
- CUPID.NS (CUPID LIMITED) score 0.3 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"

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