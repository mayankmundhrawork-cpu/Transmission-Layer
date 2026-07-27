# Transmission Layer — board brief · 2026-07-27 19:03Z

data as of **2026-07-27** · 98 series · 8 red / 37 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.579, 1d in regime; vol-pct 0.747, breadth-off 0.412, Markov P(high-vol) 0.032)
- [INVERTED] **safe_haven_gold** — corr20 -0.36, corr60 -0.45, contra nifty_50 corr20=0.13, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.9, corr60 0.82, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.51, corr60 0.35, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.01, corr60 -0.05, last shift 2026-06-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.82, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.1, corr60 -0.09, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.14, corr60 -0.25, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.54, corr60 0.24, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.486** (n=1149) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=3209) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.27] cross-asset · 5 series ↑
- ust_2y [RATES]: last 4.37, z20 3.34, zc 1.08, resid-z 0.05 [quiet], 1d 1.39%, |z20|=3.34; 1y-pct=100
- ust_10y [RATES]: last 4.71, z20 2.25, zc 0.89, resid-z -0.10 [quiet], 1d 0.86%, |z20|=2.25; 1y-pct=100
- tips_10y_real [RATES]: last 2.43, z20 2.16, zc 0.99, resid-z -0.07 [quiet], 1d 1.67%, |z20|=2.16; 1y-pct=100
- ust_30y [RATES]: last 5.17, z20 1.63, zc 0.61, resid-z -0.15 [quiet], 1d 0.39%, |z20|=1.63; 1y-pct=99
- dyn_bond [EQUITIES]: last 90.78, z20 -1.10, zc 0.45, resid-z -0.45 [quiet], 1d 0.24%, 1y-pct=2
- **Mechanism**: The recent rise in US interest rates has led to bond investors hedging against potential rate shocks, causing a surge in demand for swaptions. This, combined with the decline in oil prices, has resulted in a decrease in India's 10-year bond yield, which is likely to propagate through the valid gold_silver_comove and metal_copper_channel, influencing Indian metal equities.
- **Gap**: No gap: the big raw move in US interest rates has a small resid_z, indicating that it is largely priced in, and the recent decline in oil prices has already led to a plunge in India's 10-year bond yield
- **India take**: The Indian 10-year bond yield has already reacted to the decline in oil prices, and Indian metal equities, such as those in the Nifty Metal index, may follow suit as global metal prices move in tandem with the valid metal_copper_channel.
- Watch next: nifty_metal (up) — not yet - watch; Indian metal equities tend to follow global metal prices
- Source: Bond investors, unsure about Fed policy outlook, hedge against US rate shock — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/bonds/bond-investors-unsure-about-fed-policy-outlook-hedge-against-us-rate-shock/articleshow/132665831.cms
- Source: India 10-year bond yield logs biggest plunge in 2 months as oil rally falters — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/bonds/india-10-year-bond-yield-logs-biggest-plunge-in-2-months-as-oil-rally-falters/articleshow/132661306.cms
- Source: For 44 years, this investor held aces in the long-bond game. He just folded. — MarketWatch Top, 2026-07-27. https://www.marketwatch.com/story/for-44-years-this-investor-held-aces-in-the-long-bond-game-he-just-folded-dcd39375?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [AMBER 6.56] commodities · 2 series ↑
- wti [COMMODITIES]: last 82.32, z20 0.73, zc -0.97, resid-z -0.93 [quiet], 1d -7.83%, 1-session move -7.83% ≥ 1.5%
- brent [COMMODITIES]: last 88.12, z20 0.71, zc -1.03, resid-z -1.22 [quiet], 1d -8.95%, 1-session move -8.95% ≥ 1.5%
- **Mechanism**: The recent drop in crude oil prices, triggered by the restart of Kazakhstan's CPC oil exports and easing US-Iran tensions, has led to a decrease in oil prices, which is likely to propagate through the valid metal_copper_channel and vix_equity_inverse channels. However, the inr_oil_channel, which would normally transmit oil price movements to the INR, is currently weak.
- **Gap**: No gap: The big raw move in oil prices has a small resid_z, indicating that it is largely priced in.
- **India take**: The Indian instruments that express this move are the Nifty Midcap 100 and Nifty 50, which have not yet reacted to the drop in oil prices. The rupee may also strengthen due to lower crude oil prices.
- Watch next: nifty_midcap_100 (up) — not yet - watch; Negative correlation with Brent
- **India receivers**: nifty_midcap_100 (rho -0.618, z -0.07); nifty_50 (rho -0.461, z -0.51); dyn_jiofin_bo (rho -0.456, z -0.46)
- Source: Kazakhstan Restarts CPC Oil Exports After Week-Long Black Sea Shutdown — OilPrice, 2026-07-27. https://oilprice.com/Latest-Energy-News/World-News/Kazakhstan-Restarts-CPC-Oil-Exports-After-Week-Long-Black-Sea-Shutdown.html
- Source: Gold, silver prices today: Comex gold and silver edge higher as easing US-Iran tensions cool oil prices — Mint Markets, 2026-07-27. https://www.livemint.com/market/commodities/gold-silver-prices-today-comex-gold-and-silver-edge-higher-as-easing-us-iran-tensions-cool-oil-prices-11785169046300.html
- Source: Falling crude, RBI assurance lift stocks, rupee and bonds — BusinessLine Mkts, 2026-07-27. https://www.thehindubusinessline.com/markets/falling-crude-rbi-assurance-lift-stocks-rupee-and-bonds/article71273385.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 5.65] dyn_cartrade_ns ↑
- dyn_cartrade_ns [EQUITIES]: last 2980.00, z20 3.65, zc -0.39, resid-z -0.87 [quiet], 1d 12.18%, |z20|=3.65
- **Mechanism**: The recent move in dyn_cartrade_ns is likely priced, given its small resid_z of -0.86, indicating that the move is largely explained by factor exposures. The metal_copper_channel, which is currently valid, may be a contributing factor to the move, as global copper prices can influence Indian metal equities. However, the lack of a strong correlation between dyn_cartrade_ns and other instruments, such as dow_jones, suggests that the move may be specific to the Indian market.
- **Gap**: No gap: the move in dyn_cartrade_ns is largely explained by factor exposures, with a small resid_z of -0.86, indicating that the price move is priced in.
- **India take**: The Indian instrument that expresses this move is the Nifty 50, which has already reacted with a 1% gain, snapping a five-session losing streak. Other Indian metal equities, such as those in the metal_copper_channel, may also be affected.
- Watch next: nifty_50 (up) — already moved; broader market momentum
- Source: Top Gainers & Losers on 27 July: CarTrade Tech, Laurus Labs, Infosys, Atul, TBO Tek, Anant Raj among top gainers — Mint Markets, 2026-07-27. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-27-july-cartrade-tech-laurus-labs-infosys-atul-tbo-tek-anant-raj-among-top-gainers-11785144447038.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-13 (d=0.0), 2025-07-18 (d=0.01)

### [AMBER 5.18] indices · 2 series ↑
- nasdaq_100 [INDICES]: last 28039.41, z20 -2.34, zc -0.79, resid-z 0.27 [quiet], 1d -0.32%, |z20|=2.34
- vix [INDICES]: last 19.28, z20 2.07, zc -0.06, resid-z n/a [quiet], 1d 3.77%, |z20|=2.07
- **Mechanism**: The Nasdaq 100 and VIX indices have moved in tandem, with the Nasdaq 100 rising and the VIX falling, as easing US-Iran tensions have improved investor risk appetite. This move is priced, given the relatively small resid_z values, indicating that the move is largely explained by factor exposures. The valid vix_equity_inverse channel suggests that the vol spike has led to an equity drawdown, but the current move is in the opposite direction, with vol easing and equities rising.
- **Gap**: No gap: the move is largely priced, with small resid_z values and a clear motivator in easing US-Iran tensions
- **India take**: The Indian instrument that expresses this move is the Nifty 50, which may react positively to the improved risk appetite, potentially leading to a rise in metal equities via the valid metal_copper_channel.
- Watch next: dow_jones (up) — not yet - watch; historically leads by 2d
- Source: US stock market today: S&P 500, Nasdaq futures jump up to 1.7% as oil prices tumble on easing US-Iran tensions — Mint Markets, 2026-07-27. https://www.livemint.com/market/stock-market-news/us-stock-market-today-s-p-500-nasdaq-futures-jump-up-to-1-7-as-oil-prices-tumble-on-easing-us-iran-tensions-11785151956723.html
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US market opens higher as pause in US-Iran hostilities lifts sentiment — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-fed-warsh-microsoft-amazon-meta-alphabet-tesla-chip-stock-price-news-27th-july-2026/liveblog/132661511.cms
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US market edges lower as chip stocks tumble ahead of earnings session — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-fed-warsh-microsoft-amazon-meta-alphabet-tesla-chip-stock-price-news-27th-july-2026/liveblog/132661511.cms
- Historical analogues: 2026-05-04 (d=0.12), 2025-10-23 (d=0.14), 2026-05-20 (d=0.14)

### [RED 4.99] dxy ↑
- dxy [FX]: last 101.52, z20 1.99, zc 0.12, resid-z 0.08 [quiet], 1d 0.05%, 20d range extreme; |z20|=1.99; 1y-pct=99
- **Mechanism**: The recent surge in the US Dollar Index (DXY) may propagate through the VALID gold_silver_comove channel, potentially leading to a decline in gold prices. However, the INVERTED safe_haven_gold channel suggests a risk-off safe-haven bid, which could support gold prices. The VALID metal_copper_channel may also influence Indian metal equities.
- **Gap**: No gap: The DXY move is largely priced, with a small resid_z of -0.69, indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian instrument that may express this move is the MCX Gold, which may decline if the gold_silver_comove channel dominates. However, the reaction is yet to be seen.
- Watch next: comex_gold (down) — not yet - watch; Historically leads DXY by 3 days
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [RED 4.52] dyn_lth ↑
- dyn_lth [EQUITIES]: last 43.31, z20 2.52, zc 0.45, resid-z 0.13 [quiet], 1d 2.33%, |z20|=2.52; 1y-pct=100
- **Mechanism**: The recent increase in dyn_lth is a priced move with a small resid_z of 0.13, indicating that the move is largely explained by factor exposures. The metal_copper_channel is a valid mechanism that could propagate this move to Indian metal equities. However, the inr_oil_channel is weak, which could limit the transmission of the move to Indian markets.
- **Gap**: No gap: the move in dyn_lth is largely priced with a small resid_z
- **India take**: The Indian instrument that expresses this move is the Nifty Metal index, which has not yet reacted. The metal_copper_channel could transmit the move to Indian metal equities.
- Watch next: nifty_metal (up) — not yet - watch; global copper leads Indian metal equities
- Source: ‘Time will tell whether that was a good bet’: My adviser got me a full SpaceX IPO allocation. Was I lucky? — MarketWatch Top, 2026-07-27. https://www.marketwatch.com/story/time-will-tell-whether-that-was-a-good-bet-my-adviser-got-me-a-full-spacex-ipo-allocation-was-i-lucky-7f319645?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.01), 2025-04-17 (d=0.02)

### [AMBER 4.31] dyn_infy ↑
- dyn_infy [EQUITIES]: last 11.70, z20 2.31, zc 1.47, resid-z -0.73 [quiet], 1d 5.31%, |z20|=2.31
- **Mechanism**: dyn_infy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.561 via dyn_infy, leads 1d, z 1.49, reacted); dyn_techm_ns (rho 0.542 via dyn_infy, leads 1d, z 1.45, reacted); dyn_tataelxsi_ns (rho 0.384 via dyn_infy, z -0.48, quiet)
- **India receivers**: nifty_it (rho 0.561, z 1.49); dyn_techm_ns (rho 0.542, z 1.45); dyn_tataelxsi_ns (rho 0.384, z -0.48)
- Source: Market wrap: Eternal, HDFC Bank, Infosys among top gainers and losers on Nifty and Sensex on Monday — ET Markets, 2026-07-27. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-eternal-hdfc-bank-infosys-among-top-gainers-and-losers-on-nifty-and-sensex-on-monday/articleshow/132660092.cms
- Source: Top Gainers & Losers on 27 July: CarTrade Tech, Laurus Labs, Infosys, Atul, TBO Tek, Anant Raj among top gainers — Mint Markets, 2026-07-27. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-27-july-cartrade-tech-laurus-labs-infosys-atul-tbo-tek-anant-raj-among-top-gainers-11785144447038.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-20 (d=0.01), 2024-10-15 (d=0.02)

### [RED 3.99] indices · 3 series ↑
- ftse_100 [INDICES]: last 10801.15, z20 2.68, zc 1.14, resid-z 0.74 [quiet], 1d 0.60%, |z20|=2.68; 1y-pct=98
- dax [INDICES]: last 25426.61, z20 1.01, zc 1.32, resid-z 1.09 [quiet], 1d 1.31%, 1y-pct=98
- stoxx_50 [INDICES]: last 6297.21, z20 0.18, zc 1.08, resid-z 0.75 [quiet], 1d 0.26%, 1y-pct=96
- **Mechanism**: indices · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.588 via stoxx_50, z -0.07, quiet); nifty_50 (rho 0.566 via dax, z -0.51, quiet)
- Watch next: cac_40 (co-move) — not yet - watch; rho 0.684 vs ftse_100, historically leads by 3d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.6 vs dax, historically leads by 5d
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.535 vs ftse_100, historically leads by 5d
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.573 vs dax
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.566 vs dax
- **India receivers**: nifty_midcap_100 (rho 0.588, z -0.07); nifty_50 (rho 0.566, z -0.51)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-16 (d=0.34), 2025-12-01 (d=0.45)

## Watchlist (below surfacing floor)
dyn_ohi ↑ (3.96), dyn_hdb ↓ (3.75), nikkei_225 ↓ (3.66), natgas ↓ (3.58), dyn_bac ↑ (3.49), gold_silver_ratio ↑ (3.46), dyn_tech ↑ (3.06), commodities · 2 series ↑ (2.95), asx_200 ↑ (2.74), dyn_hdbfs_bo ↓ (2.55), dyn_icicigi_bo ↓ (2.54), usd_jpy ↑ (2.51)

## India macro
- nifty_50: 24003.6504 (1d 0.99%, z20 -0.51, flag none)
- nifty_midcap_100: 62286.1484 (1d 0.98%, z20 -0.07, flag none)
- usd_inr: 95.9000 (1d -1.01%, z20 0.11, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5949 (1d -0.01%, z20 0.47, flag none)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 65.7 — "TSLA - *DEUTSCHE BANK CUTS TESLA PRICE TARGET TO $420 *DEUTSCHE BANK MAINTAINS BUY RATING "
- INOXINDIA.NS (INOX INDIA LIMITED) score 60.8 — "Crude tumbles as US-Iran pause eases pressure, but risks to India’s oil supply remain"
- BAC (Bank of America Corporation) score 55.6 — "TSLA - *DEUTSCHE BANK CUTS TESLA PRICE TARGET TO $420 *DEUTSCHE BANK MAINTAINS BUY RATING "
- HDB (HDFC Bank Limited) score 54.6 — "TSLA - *DEUTSCHE BANK CUTS TESLA PRICE TARGET TO $420 *DEUTSCHE BANK MAINTAINS BUY RATING "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 52.1 — "TSLA - *DEUTSCHE BANK CUTS TESLA PRICE TARGET TO $420 *DEUTSCHE BANK MAINTAINS BUY RATING "
- IDBI.NS (IDBI BANK LIMITED) score 49.4 — "TSLA - *DEUTSCHE BANK CUTS TESLA PRICE TARGET TO $420 *DEUTSCHE BANK MAINTAINS BUY RATING "
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 48.3 — "Crude tumbles as US-Iran pause eases pressure, but risks to India’s oil supply remain"
- COIN (Coinbase Global, Inc.) score 40.6 — "AMZN - AMAZON: LEO WILL PARTNER WITH MOBILE NETWORK OPERATORS TO EXTEND MOBILE CONNECTIVIT"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 39.8 — "TSLA - *DEUTSCHE BANK CUTS TESLA PRICE TARGET TO $420 *DEUTSCHE BANK MAINTAINS BUY RATING "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.1 — "Xtranet Technologies IPO closes 12x subscribed; HNIs steal the show at 26x"
- COALINDIA.NS (COAL INDIA LTD) score 38.7 — "Crude tumbles as US-Iran pause eases pressure, but risks to India’s oil supply remain"
- TECHM.NS (TECH MAHINDRA LIMITED) score 37.7 — "Xtranet Technologies IPO closes 12x subscribed; HNIs steal the show at 26x"
- OHI (Omega Healthcare Investors, In) score 23.6 — "BITCOIN RISES AS TENSIONS EASE Bitcoin gained 0.5% as risk sentiment improved after Presid"
- BOND (PIMCO Active Bond Exchange-Tra) score 21.4 — "Bond investors, unsure about Fed policy outlook, hedge against US rate shock"
- LTH (Life Time Group Holdings, Inc.) score 17.4 — "BITCOIN RISES AS TENSIONS EASE Bitcoin gained 0.5% as risk sentiment improved after Presid"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 16.6 — "GOLDMAN SEES GAS PRICE RISKS Goldman Sachs maintained its Q3 2026 TTF gas forecast at €60/"
- CHKP (Check Point Software Technolog) score 14.4 — "Cube Highways Trust InvIT IPO: Focus shifts to allotment date. Latest GMP, step-by-step gu"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.6 — "Tata Power board okays raising Rs 4,500 cr via NCDs"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.5 — "Global markets: Shein will struggle to justify up to $50 billion Hong Kong IPO valuation"
- INFY (Infosys Limited) score 10.3 — "Top Gainers & Losers on 27 July: CarTrade Tech, Laurus Labs, Infosys, Atul, TBO Tek, Anant"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.7 — "Adani Energy launches Rs 3,500 crore QIP, sets floor price at Rs 1,698 per share"
- JIOFIN.BO (Jio Financial Services Limited) score 8.7 — "AMZN - AMAZON: LEO WILL PARTNER WITH MOBILE NETWORK OPERATORS TO EXTEND MOBILE CONNECTIVIT"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 7.4 — "Q1 Results Today Highlights: BEL & Canara Bank Q1 PAT up, P N Gadgil PAT jumps 51%, HUDCO "
- VT (Vanguard Total World Stock Ind) score 6.7 — "Mangalam Worldwide Q1 Results: Profit rises 19% to Rs 12 crore"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 6.7 — "From financials to industrials: Here's how Nifty 500 composition has shifted over the year"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.2 — "ICICI Bank Share Price Highlights: ICICI Bank Stock Price History"
- META (Meta) score 6.1 — "India's next commodity cycle could be driven by scrap as organised metal recycling gains m"
- GS (Goldman Sachs Group, Inc. (The) score 6.0 — "GOLDMAN SEES GAS PRICE RISKS Goldman Sachs maintained its Q3 2026 TTF gas forecast at €60/"
- MS (Morgan Stanley) score 5.8 — "SPCX - MORGAN STANLEY SEES STARSHIP MILESTONE Morgan Stanley said SpaceX's Starship Flight"
- ETERNAL.NS (ETERNAL LIMITED) score 4.1 — "Market wrap: Eternal, HDFC Bank, Infosys among top gainers and losers on Nifty and Sensex "
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 4.1 — "India’s electricity shortages more than doubled during January-May 2026: IEA"
- NVDA (NVIDIA Corporation) score 4.1 — "NVDA - *NVIDIA MAKES INVESTMENT IN SAFE SUPERINTELLIGENCE; NO TERMS"
- PCJEWELLER.NS (PC JEWELLER LTD) score 3.2 — "Sebi clears IPOs of Intellius Recode, Nityas Gems & Jewellery"
- 688188.SS (SHANGHAI BOCHU ELECTRONIC TECH) score 2.9 — "China's memory chipmaker CXMT shares soar in its blockbuster share listing in Shanghai"
- INDIGOPNTS.NS (INDIGO PAINTS LIMITED) score 2.7 — "Sensex jumps 530 pts as crude retreat; IndiGo, Tata Consumer lead gains"
- TECH (Bio-Techne Corp) score 2.4 — "Big Tech is forcing consumers to pay for its AI boom. Voters are pushing back."
- AAPL (Apple Inc.) score 1.8 — "FORD WILL USE APPLE SOFTWARE IN NEW SELF-DRIVING SYSTEM: NYT"
- NFLX (Netflix, Inc.) score 1.6 — "Losing Wall Street binge premium! Why are Netflix shares in a freefall this year?"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 0.5 — "Newly-listed SME stock DSM Fresh Foods jumps over 30% in 2 days after reporting a 58% YoY "
- CUPID.NS (CUPID LIMITED) score 0.2 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"

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