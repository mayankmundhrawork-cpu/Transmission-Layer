# Transmission Layer — board brief · 2026-07-24 11:17Z

data as of **2026-07-24** · 98 series · 6 red / 39 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.643, 2d in regime; vol-pct 0.702, breadth-off 0.583, Markov P(high-vol) 0.077)
- [INVERTED] **safe_haven_gold** — corr20 -0.35, corr60 -0.45, contra nifty_50 corr20=0.14, last shift 2026-06-01. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.9, corr60 0.82, last shift 2026-05-15. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.51, corr60 0.35, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.08, corr60 -0.03, last shift 2026-06-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.93, corr60 -0.82, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.11, corr60 -0.09, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [INVERTED] **real_rates_gold_inverse** — corr20 0.25, corr60 -0.24, last shift 2026-05-08. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.53, corr60 0.24, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** sp500 → aud_usd: leads 1d (ccf 0.458, β 0.2726, p 0.0); driver zc -1.55 → expected -0.33%. Type hit-rate 0.82 (n=3022).
- **SETUP** sp500 → nifty_midcap_100: leads 1d (ccf 0.269, β 0.3227, p 0.0); driver zc -1.55 → expected -0.391%. Type hit-rate 0.82 (n=3022).
- Track record · residual_reversion: hit-rate **0.491** (n=1162) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.82** (n=3022) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.706** (n=17) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.81] commodities · 2 series ↑
- wti [COMMODITIES]: last 89.81, z20 1.98, zc -0.80, resid-z 1.30 [quiet], 1d -2.58%, 1-session move -2.58% ≥ 1.5%; |z20|=1.98
- brent [COMMODITIES]: last 91.92, z20 1.33, zc -2.31, resid-z 1.65 [unexplained], 1d -8.71%, 1-session move -8.71% ≥ 1.5%; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: The recent surge in oil prices, driven by Middle East shipping risks and China's efforts to secure Russian oil, has led to a significant increase in WTI and Brent crude prices. This move is partially priced, with resid_z values of 1.3 and 1.65 for WTI and Brent, respectively, indicating that a portion of the move can be explained by factor exposures. However, the large raw moves in both WTI and Brent suggest that there may be an unexplained component to the price action.
- **Gap**: No gap: the large raw moves in WTI and Brent are partially explained by factor exposures, and the Indian instruments have already reacted to the price surge
- **India take**: The Indian instruments, such as nifty_midcap_100 and nifty_50, have already reacted to the surge in oil prices, and a sustained rally in oil prices is likely to weigh on Indian equities and the rupee. However, businesses linked to renewable energy and electric vehicles may benefit from the oil price surge.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to WTI price surge
- Watch next: nifty_50 (down) — already moved; reacted to WTI price surge
- Watch next: dyn_hdbfs_bo (down) — already moved; reacted to Brent price surge
- **India receivers**: nifty_midcap_100 (rho -0.639, z -1.28); nifty_50 (rho -0.467, z -1.94); dyn_indusindbk_bo (rho -0.465, z 0.01); dyn_hdbfs_bo (rho -0.461, z -2.88)
- Source: WTI Explodes Higher as Middle East Shipping Risks Multiply — OilPrice, 2026-07-24. https://oilprice.com/Energy/Energy-General/WTI-Explodes-Higher-as-Middle-East-Shipping-Risks-Multiply.html
- Source: RBI Intervention shields rupee in face of oil, hedging strain — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/forex/forex-news/rbi-intervention-shields-rupee-in-face-of-oil-hedging-strain/articleshow/132603138.cms
- Source: Experts warn sustained oil rally could weigh on stock markets, rupee; renewables, EVs may gain — BusinessLine Mkts, 2026-07-24. https://www.thehindubusinessline.com/markets/experts-warn-sustained-oil-rally-could-weigh-on-stock-markets-rupee-renewables-evs-may-gain/article71261679.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 7.55] cross-asset · 9 series ↑
- ust_2y [RATES]: last 4.31, z20 2.92, zc 0.91, resid-z 1.09 [quiet], 1d 1.17%, |z20|=2.92; 1y-pct=100
- nasdaq_100 [INDICES]: last 28456.53, z20 -2.23, zc -1.35, resid-z -0.53 [quiet], 1d -1.87%, |z20|=2.23
- dyn_bond [EQUITIES]: last 90.44, z20 -2.10, zc -1.07, resid-z -0.22 [quiet], 1d -0.31%, |z20|=2.10; 1y-pct=0
- ust_10y [RATES]: last 4.67, z20 2.05, zc 0.90, resid-z 0.85 [quiet], 1d 0.86%, |z20|=2.05; 1y-pct=99
- russell_2000 [INDICES]: last 2940.07, z20 -1.95, zc -0.54, resid-z 1.55 [unexplained], 1d -0.67%, |z20|=1.95
- dow_jones [INDICES]: last 51702.23, z20 -1.92, zc -1.35, resid-z 0.37 [quiet], 1d -0.99%, |z20|=1.92
- tips_10y_real [RATES]: last 2.39, z20 1.74, zc 0.49, resid-z 0.30 [quiet], 1d 0.84%, |z20|=1.74; 1y-pct=100
- ust_30y [RATES]: last 5.15, z20 1.60, zc 0.61, resid-z 0.37 [quiet], 1d 0.39%, |z20|=1.60; 1y-pct=99
- vix [INDICES]: last 18.80, z20 1.60, zc 0.05, resid-z n/a [quiet], 1d 0.53%, |z20|=1.60
- **Mechanism**: The recent spike in oil prices and Treasury yields has put Indian bonds under pressure, leading to a decline in bond prices and an increase in yields. This move is largely priced, given the big raw move in oil and rates with small resid_z values in key series such as ust_2y and nasdaq_100. However, the russell_2000 shows an unexplained move, suggesting some potential for further propagation through equity markets.
- **Gap**: No gap: the big raw move in oil and rates has been largely priced by the market, with small resid_z values in key series
- **India take**: The Indian 10-year government bond yield may react to the increase in US Treasury yields, while the Nifty 50 may follow global equity markets lower. The metal_copper_channel may also transmit global economic weakness to Indian metal equities.
- Watch next: nifty_50 (down) — not yet - watch; Indian equities may follow global equity markets lower
- Source: Why fixing the housing crisis for under-40s could trigger 10% Treasury yields — MarketWatch Top, 2026-07-24. https://www.marketwatch.com/story/why-fixing-the-housing-crisis-for-under-40s-could-trigger-10-treasury-yields-04c65b78?mod=mw_rss_topstories
- Source: Global market: Euro zone bond yields ease after multi-year highs as oil retreats below $100 — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-bond-yields-ease-after-multi-year-highs-as-oil-retreats-below-100/articleshow/132601832.cms
- Source: Oil shock, Treasury yield spike put Indian bonds under pressure before debt sale — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/bonds/oil-shock-treasury-yield-spike-put-indian-bonds-under-pressure-before-debt-sale/articleshow/132596731.cms
- Historical analogues: 2026-05-22 (d=0.4), 2026-05-14 (d=0.6), 2025-05-20 (d=0.7)

### [RED 7.41] dyn_qessf ↓
- dyn_qessf [EQUITIES]: last 0.17, z20 -5.41, zc -3.96, resid-z -0.72 [moved], 1d -25.39%, |z20|=5.41
- **Mechanism**: The decline in dyn_qessf is driven by a priced move, with a small resid_z of -0.72, indicating that the move is largely explained by factor exposures. The RISK_OFF regime and the VALID vix_equity_inverse channel suggest that the equity market is experiencing a drawdown due to a vol spike. The metal_copper_channel also indicates that global copper leads Indian metal equities, which may be contributing to the decline.
- **Gap**: No gap: the move in dyn_qessf is largely priced, with a small resid_z and a significant z20 level of -5.41, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is the Nifty 50, which has not yet reacted. The metal_copper_channel suggests that Indian metal equities, such as those in the Nifty Metal index, may also be affected.
- Watch next: nifty_50 (down) — not yet - watch; risk-off regime and vol spike
- Source: Ashish Kacholia exits defence stock that rallied 108% in Q1. Do you own it? — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/stocks/news/ashish-kacholia-exits-defence-stock-that-rallied-108-in-q1-do-you-own-it/articleshow/132597323.cms
- Source: Multibagger defence stock Apollo Micro Systems to be in focus tomorrow; here's why — Mint Markets, 2026-07-22. https://www.livemint.com/market/stock-market-news/multibagger-defence-stock-apollo-micro-systems-to-be-in-focus-tomorrow-heres-why-11784728706086.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-15 (d=0.32), 2024-11-14 (d=0.52)

### [RED 6.61] commodities · 3 series ↑
- corn [COMMODITIES]: last 489.00, z20 3.29, zc 4.29, resid-z 0.14 [moved], 1d 5.39%, |z20|=3.29; 1y-pct=100
- soybeans [COMMODITIES]: last 1247.75, z20 1.65, zc 0.82, resid-z 0.02 [quiet], 1d 0.83%, |z20|=1.65; 1y-pct=100
- wheat [COMMODITIES]: last 700.00, z20 1.62, zc 0.25, resid-z -0.88 [quiet], 1d 0.54%, |z20|=1.62; 1y-pct=99
- **Mechanism**: The recent surge in commodity prices, particularly wheat, corn, and soybeans, is driven by supply concerns due to scorching heat in key US wheat-growing states and escalating attacks between Russia and Ukraine, which puts exports at risk. This move is largely priced, given the small resid_z values for these commodities. The valid gold_silver_comove and metal_copper_channel may also play a role in transmitting this move to Indian metal equities.
- **Gap**: No gap: the move is largely priced, with small resid_z values for the affected commodities
- **India take**: Indian metal equities, such as those represented by dyn_patanjali_ns and dyn_adanient_bo, have already reacted to the commodity price surge. Further moves may be driven by the valid metal_copper_channel and gold_silver_comove channels.
- Watch next: dyn_patanjali_ns (down) — already moved; reacted to wheat price move
- Watch next: dyn_adanient_bo (down) — already moved; reacted to soybeans price move
- **India receivers**: dyn_patanjali_ns (rho -0.515, z -1.36); dyn_adanient_bo (rho -0.378, z -1.42)
- Source: Heat Worries US Wheat Farmers Just as Crop Prices Surge — Mint Markets, 2026-07-23. https://www.livemint.com/market/heat-worries-us-wheat-farmers-just-as-crop-prices-surge-11784841971254.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-08-30 (d=0.27), 2026-05-06 (d=0.32)

### [RED 5.32] usd_jpy ↑
- usd_jpy [FX]: last 163.76, z20 3.32, zc 1.33, resid-z 1.74 [unexplained], 1d 0.41%, |z20|=3.32; 1y-pct=100
- **Mechanism**: usd_jpy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: asx_200 (inverse) — not yet - watch; rho -0.521 vs usd_jpy, historically leads by 2d
- Watch next: eur_usd (inverse) — not yet - watch; rho -0.518 vs usd_jpy, historically leads by 1d
- Source: Global Market: US urges BOJ to keep raising rates, flags persistent yen weakness despite narrower yield gap — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-us-urges-boj-to-keep-raising-rates-flags-persistent-yen-weakness-despite-narrower-yield-gap/articleshow/132596001.cms
- Source: Yen’s Slump Extends Beyond Dollar and Stokes Inflation Fears — Mint Markets, 2026-07-23. https://www.livemint.com/market/yens-slump-extends-beyond-dollar-and-stokes-inflation-fears-11784836659389.html
- Source: Dollar hits new 40-year high versus yen, euro softer after ECB stands pat on rates — Mint Markets, 2026-07-23. https://www.livemint.com/market/dollar-hits-new-40-year-high-versus-yen-euro-softer-after-ecb-stands-pat-on-rates-11784833989812.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2024-11-08 (d=0.01)

### [AMBER 4.44] dyn_hdb ↓
- dyn_hdb [EQUITIES]: last 23.15, z20 -2.44, zc -0.10, resid-z -0.99 [quiet], 1d -0.15%, |z20|=2.44; 1y-pct=0
- **Mechanism**: dyn_hdb ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.664 via dyn_hdb, z -1.94, reacted); nifty_midcap_100 (rho 0.531 via dyn_hdb, z -1.28, reacted); dyn_jiofin_bo (rho 0.482 via dyn_hdb, z -0.92, quiet)
- Watch next: cac_40 (co-move) — not yet - watch; rho 0.57 vs dyn_hdb
- **India receivers**: nifty_50 (rho 0.664, z -1.94); nifty_midcap_100 (rho 0.531, z -1.28); dyn_jiofin_bo (rho 0.482, z -0.92)
- Source: HDFC Bank shares fall as 3 US law firms launch probe over alleged federal law violations — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-bank-shares-fall-as-3-us-law-firms-launch-probe-over-alleged-federal-law-violations/articleshow/132598223.cms
- Source: HDFC Bank Share Price Live Updates: HDFC Bank Dividend Updates — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/hdfc-bank-share-price-live-24-jul-2026/liveblog/132596375.cms
- Source: HDFC Bank, 3 other bank stocks wipe out Rs 1.5 lakh crore of investors' wealth after Q1. Time to buy the dip? — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-bank-3-other-bank-stocks-wipe-out-rs-1-5-lakh-crore-of-investors-wealth-after-q1-time-to-buy-the-dip/articleshow/132596148.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [AMBER 4.17] dyn_ohi ↑
- dyn_ohi [EQUITIES]: last 50.97, z20 2.17, zc 0.56, resid-z -0.11 [quiet], 1d 0.72%, |z20|=2.17; 1y-pct=100
- **Mechanism**: dyn_ohi ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Elon Musk loses $19 billion after Tesla shares plunge 14%. What’s spooking investors? — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/us-stocks/news/elon-musk-loses-19-billion-after-tesla-shares-plunge-14-whats-spooking-investors/articleshow/132602375.cms
- Source: Global Market: European shares steady, set for weekly loss as oil surge, earnings keep investors cautious — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-european-shares-steady-set-for-weekly-loss-as-oil-surge-earnings-keep-investors-cautious/articleshow/132601866.cms
- Source: US investors rethink bonds' role as inflation reshapes portfolios — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/bonds/us-investors-rethink-bonds-role-as-inflation-reshapes-portfolios/articleshow/132599340.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2024-10-15 (d=0.09)

### [AMBER 3.98] nikkei_225 ↓
- nikkei_225 [INDICES]: last 64604.84, z20 -1.98, zc -1.49, resid-z 0.72 [quiet], 1d -2.74%, |z20|=1.98
- **Mechanism**: nikkei_225 ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_hdbfs_bo (rho 0.463 via nikkei_225, z -2.88, reacted); nifty_metal (rho 0.443 via nikkei_225, z -1.61, reacted)
- **India receivers**: dyn_hdbfs_bo (rho 0.463, z -2.88); nifty_metal (rho 0.443, z -1.61)
- Source: Japan's Nikkei falls more than 2% on AI spending worries — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/us-stocks/news/japans-nikkei-falls-more-than-2-on-ai-spending-worries/articleshow/132594822.cms
- Source: Japan's Nikkei rises as chip shares gain, BOJ's rate hike prospects weigh — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/us-stocks/news/japans-nikkei-rises-as-chip-shares-gain-bojs-rate-hike-prospects-weigh/articleshow/132572655.cms
- Source: Asian stocks today: Kospi, Nikkei surge up to 4% as semiconductor stocks rally; SK Hynix, Samsung lead — Mint Markets, 2026-07-23. https://www.livemint.com/market/stock-market-news/asian-stocks-today-kospi-nikkei-surge-up-to-4-as-semiconductor-stocks-rally-sk-hynix-samsung-lead-11784770474517.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-21 (d=0.23), 2026-06-11 (d=0.6)

## Watchlist (below surfacing floor)
nifty_50 ↓ (3.94), dyn_patanjali_ns ↓ (3.36), dyn_bac ↑ (3.24), usd_inr ↑ (3.2), gold_silver_ratio ↑ (3.14), dyn_infy ↓ (3.06), eur_usd ↓ (3.0), dyn_icicigi_bo ↓ (2.9), dyn_hdbfs_bo ↓ (2.88), dyn_aapl ↑ (2.66), dyn_lth ↑ (2.56), dyn_havells_ns ↑ (2.34)

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
- INDIANB.NS (INDIAN BANK) score 91.0 — "HDFC Bank Share Price Live Updates: HDFC Bank Dividend Updates"
- INOXINDIA.NS (INOX INDIA LIMITED) score 85.2 — "Indiabulls share price jumps despite stock market crash; here's why"
- HDB (HDFC Bank Limited) score 71.4 — "HDFC Bank Share Price Live Updates: HDFC Bank Dividend Updates"
- BAC (Bank of America Corporation) score 69.2 — "HDFC Bank Share Price Live Updates: HDFC Bank Dividend Updates"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 68.0 — "HDFC Bank Share Price Live Updates: HDFC Bank Dividend Updates"
- IDBI.NS (IDBI BANK LIMITED) score 62.3 — "HDFC Bank Share Price Live Updates: HDFC Bank Dividend Updates"
- COIN (Coinbase Global, Inc.) score 60.6 — "Global Market: ECB signals future debate on raising bank reserve requirements to reduce ce"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 58.3 — "Indiabulls share price jumps despite stock market crash; here's why"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 51.5 — "Xtranet Technologies IPO Day 2: Issue subscribed 1.76x so far. GMP hints 6% listing gain. "
- TECHM.NS (TECH MAHINDRA LIMITED) score 48.5 — "Xtranet Technologies IPO Day 2: Issue subscribed 1.76x so far. GMP hints 6% listing gain. "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 41.5 — "HDFC Bank Share Price Live Updates: HDFC Bank Dividend Updates"
- COALINDIA.NS (COAL INDIA LTD) score 37.5 — "Indiabulls share price jumps despite stock market crash; here's why"
- OHI (Omega Healthcare Investors, In) score 31.6 — "US investors rethink bonds' role as inflation reshapes portfolios"
- BOND (PIMCO Active Bond Exchange-Tra) score 25.9 — "US investors rethink bonds' role as inflation reshapes portfolios"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 25.2 — "Juniper Green Energy to open Rs 1,800-cr IPO on July 30"
- CHKP (Check Point Software Technolog) score 24.9 — "Cube Highways Trust InvIT IPO Day 3: Issue subscribed 1.67x so far. Check GMP, issue detai"
- INFY (Infosys Limited) score 18.1 — "Infosys shares dip after Q1 results; brokerages trim target prices"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 14.6 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Trading Update"
- JUSTDIAL.BO (JUST DIAL LTD.) score 12.2 — "Why Jefferies’ Chris Wood, billionaire John Paulson say gold’s long term bull market is ju"
- LTH (Life Time Group Holdings, Inc.) score 12.1 — "SBI Funds Management shares fall below IPO price, but brokerages remain bullish. Time to b"
- JIOFIN.BO (Jio Financial Services Limited) score 11.3 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Financial Snapshot"
- VT (Vanguard Total World Stock Ind) score 10.3 — "U.S. Refinery Utilization Hits 96.2% as Fuel Markets Tighten Worldwide"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 10.3 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Financial Snapshot"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 10.2 — "ICICI Bank prices $1 billion debt in largest dollar issue by Indian private lender"
- GS (Goldman Sachs Group, Inc. (The) score 8.6 — "Oil Price Today (July 23): Crude oil crosses $95 as US strikes enter 12th day. Why Goldman"
- MS (Morgan Stanley) score 8.1 — "Infosys shares fall 3% as JPMorgan downgrades stock, Jefferies cuts target after Q1 result"
- META (Meta) score 8.0 — "Sensex today | Stock Market Highlights: Sensex, Nifty decline for fifth straight session; "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 7.6 — "Tata Consumer Q1 Results: Net profit rises 28% YoY to Rs 427 crore, revenue up 12%"
- ETERNAL.NS (ETERNAL LIMITED) score 5.8 — "Top Gaines & Losers on 24 July: Syrma SGS Tech, HFCL, Swiggy, Eternal, Hero MotoCorp among"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 5.7 — "Q1 Results Today Live: Shriram Finance, TCP, BoB, Hindustan Zinc, ACC, Dalmia Bharat, Jind"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 5.0 — "Ashish Kacholia exits defence stock that rallied 108% in Q1. Do you own it?"
- PCJEWELLER.NS (PC JEWELLER LTD) score 4.8 — "Bluestone Jewellery shares rocket 36% in just three days after Q1 results. Can the momentu"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 4.7 — "IEX Q1 results: Net profit grows 12% YoY to  ₹135 crore; electricity volumes rise 16%"
- NVDA (NVIDIA Corporation) score 4.5 — "AMD’s rivalry with Nvidia is increasingly moving into a new realm"
- AAPL (Apple Inc.) score 3.8 — "FORD WILL USE APPLE SOFTWARE IN NEW SELF-DRIVING SYSTEM: NYT"
- INDIGOPNTS.NS (INDIGO PAINTS LIMITED) score 3.8 — "IndiGo faces rough weather in Q1, hit by skyrocketing fuel prices"
- NFLX (Netflix, Inc.) score 2.5 — "US stocks to buy for short term: From Nvidia to Netflix- Appreciate CEO suggests picking t"
- WIT (Wipro Limited) score 2.1 — "Stocks to watch: Reliance Industries, Wipro, CEAT among shares in focus today; check list "
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 1.1 — "Newly-listed SME stock DSM Fresh Foods jumps over 30% in 2 days after reporting a 58% YoY "
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