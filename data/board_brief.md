# Transmission Layer — board brief · 2026-07-20 12:29Z

data as of **2026-07-20** · 98 series · 11 red / 36 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.503, 10d in regime; vol-pct 0.643, breadth-off 0.364, Markov P(high-vol) 0.058)
- [WEAK] **safe_haven_gold** — corr20 -0.0, corr60 -0.42, contra nifty_50 corr20=0.24, last shift 2026-05-28. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.82, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.43, corr60 0.38, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.09, corr60 -0.04, last shift 2026-06-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.8, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.06, corr60 -0.06, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.17, corr60 -0.27, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.21, corr60 0.23, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.0015243893761345273)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.492** (n=1156) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=3061) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.722** (n=18) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 5.61] cross-asset · 2 series ↑
- dyn_techm_ns [EQUITIES]: last 1575.40, z20 2.77, zc 2.21, resid-z 1.21 [moved], 1d 0.16%, |z20|=2.77
- nifty_it [INDICES]: last 29159.35, z20 1.77, zc 0.99, resid-z 0.43 [quiet], 1d -0.23%, |z20|=1.77
- **Mechanism**: The recent Q1 results of Indian banks and other companies have led to a mixed reaction in the market, with some stocks like ICICI Bank rising and others like HDFC Bank and Kotak Mahindra Bank declining. This has resulted in a cross-asset move, with dyn_techm_ns and nifty_it showing z20 levels of 2.7745 and 1.7668 respectively. The move in dyn_techm_ns is priced, given its small resid_z of 1.21, indicating that the move is largely explained by factor exposures. The metal_copper_channel and gold_silver_comove channels are valid and may be influencing the move.
- **Gap**: No gap: the move in dyn_techm_ns is priced, with a small resid_z of 1.21, indicating that the move is largely explained by factor exposures
- **India take**: The Indian instrument that expresses this move is dyn_tataelxsi_ns, which has already reacted with a rho of 0.704 with nifty_it. The Nifty IT index may also be influenced by the valid metal_copper_channel and gold_silver_comove channels.
- Watch next: dyn_tataelxsi_ns (up) — already moved; rho of 0.704 with nifty_it
- **India receivers**: dyn_tataelxsi_ns (rho 0.704, z -1.19)
- Source: Q1 Results Today Live: UltraTech PAT up, IOB, KVB Q1 PAT climb, Mahindra Logistics, Dynamic Cables & Shyam Metalics zoom, Paytm, Sobha, JP Power, Bluestone to announce Q1 results — BusinessLine Mkts, 2026-07-20. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-ultratech-cement-paytm-iob-karur-vysya-bank-shyam-metalics-sobha-jp-power-bluestone-hdfc-bank-kotak-icici-yes-bank-axis-bank-ril-results-20-july-2026/article71241085.ece
- Source: ICICI Bank gains while HDFC Bank, Axis Bank, Kotak Mahindra, Yes Bank decline after Q1 results — BusinessLine Mkts, 2026-07-20. https://www.thehindubusinessline.com/markets/stock-markets/bank-stocks-underperform-icici-bank-gains-while-hdfc-bank-axis-bank-kotak-mahindra-yes-bank-decline/article71243829.ece
- Source: Kotak Mahindra Bank shares fall over 3% despite Q1 profit growth. Analysts weigh in — ET Markets, 2026-07-20. https://economictimes.indiatimes.com/markets/stocks/news/kotak-mahindra-bank-shares-fall-over-3-after-q1-earnings-what-are-motilal-oswal-other-brokerages-saying/articleshow/132506336.cms
- Historical analogues: 2025-12-30 (d=0.52), 2025-08-13 (d=0.76), 2026-01-06 (d=0.77)

### [AMBER 5.08] fx · 3 series ↑
- aud_usd [FX]: last 0.70, z20 1.76, zc -0.21, resid-z -0.20 [quiet], 1d 0.09%, |z20|=1.76
- usd_brl [FX]: last 5.10, z20 -1.55, zc 0.57, resid-z 0.64 [quiet], 1d -0.24%, |z20|=1.55
- eur_usd [FX]: last 1.14, z20 0.23, zc -0.62, resid-z -0.67 [quiet], 1d -0.21%, 1y-pct=4
- **Mechanism**: The recent move in FX markets, particularly in aud_usd, usd_brl, and eur_usd, is driven by the ECB's survey showing slower price and wage growth in the Euro Zone, which may lead to the ECB keeping interest rates unchanged. This has resulted in a priced move, given the small resid_z values for these currency pairs. The metal_copper_channel and gold_silver_comove channels are valid and may influence the Indian metal equities and monetary metals markets.
- **Gap**: No gap: the move in FX markets is largely priced in, given the small resid_z values and the lack of significant unexplained components.
- **India take**: The Indian instrument dyn_ceatltd_ns has already reacted to the aud_usd move, and further moves in Indian metal equities may be influenced by the valid metal_copper_channel and gold_silver_comove channels. The INR may not be directly impacted due to the weak dxy_inr_channel and inr_oil_channel.
- Watch next: dyn_ceatltd_ns (down) — already moved; reacted to aud_usd move
- **India receivers**: dyn_ceatltd_ns (rho 0.364, z -1.56)
- Source: Global Market: Euro Zone firms see slower price and wage growth, ECB survey shows — ET Markets, 2026-07-20. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-firms-see-slower-price-and-wage-growth-ecb-survey-shows/articleshow/132510738.cms
- Historical analogues: 2026-07-07 (d=0.08), 2025-09-30 (d=0.17), 2025-08-26 (d=0.27)

### [AMBER 5.04] commodities · 2 series ↑
- brent [COMMODITIES]: last 88.28, z20 2.21, zc 2.22, resid-z 1.14 [moved], 1d 0.20%, |z20|=2.21; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 81.47, z20 1.98, zc 2.13, resid-z 1.00 [moved], 1d -1.24%, |z20|=1.98
- **Mechanism**: The recent surge in crude oil prices, driven by renewed tensions and optimism surrounding U.S.-Iran negotiations, has led to a significant increase in India's crude oil import bill. This move is priced, with brent and wti showing small resid_z values of 1.14 and 1.0, respectively, indicating that the move is largely explained by factor exposures. The metal_copper_channel and gold_silver_comove channels are valid and may influence the price movement, but the primary driver is the crude oil price increase.
- **Gap**: No gap: the move in brent and wti is largely priced, with small resid_z values and a clear motivating news event (U.S.-Iran negotiations and India's crude oil import bill increase).
- **India take**: The Indian instrument that expresses this move is the nifty_midcap_100, which has already reacted to the wti price movement. The increase in India's crude oil import bill may also impact the Indian rupee and bond market, but the primary transmission candidate is the nifty_midcap_100.
- Watch next: nifty_midcap_100 (down) — already moved; reacted to wti price movement
- **India receivers**: nifty_midcap_100 (rho -0.602, z 1.08)
- Source: India bonds steady after swinging with oil — ET Markets, 2026-07-20. https://economictimes.indiatimes.com/markets/bonds/india-bonds-steady-after-swinging-with-oil/articleshow/132515342.cms
- Source: Oil prices reverse lower, after report of 10-day ceasefire proposal — MarketWatch Top, 2026-07-20. https://www.marketwatch.com/story/oil-prices-surge-stock-futures-dip-as-fighting-between-u-s-and-iran-intensifies-6fb37c79?mod=mw_rss_topstories
- Source: India’s Crude Oil Import Bill Soars 60% as Iran War Drives Prices Higher — OilPrice, 2026-07-20. https://oilprice.com/Latest-Energy-News/World-News/Indias-Crude-Oil-Import-Bill-Soars-60-as-Iran-War-Drives-Prices-Higher.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [AMBER 4.88] rates · 3 series ↑
- tips_10y_real [RATES]: last 2.35, z20 1.56, zc 0.74, resid-z 0.05 [quiet], 1d 1.29%, |z20|=1.56; 1y-pct=99
- ust_30y [RATES]: last 5.09, z20 1.47, zc 0.31, resid-z -0.18 [quiet], 1d 0.20%, 1y-pct=97
- ust_10y [RATES]: last 4.57, z20 1.18, zc 0.45, resid-z -0.21 [quiet], 1d 0.44%, 1y-pct=97
- **Mechanism**: The recent surge in global bond yields, driven by escalating U.S.-Iran tensions and higher oil prices, has led to a rise in Indian government bond yields. This increase in yields is attributed to the expected strain on India's import bill and government finances due to higher crude prices. The valid gold_silver_comove and metal_copper_channel suggest that monetary metals and global copper are co-moving, which may lead to a transmission of global economic trends to Indian metal equities.
- **Gap**: No gap: The recent move in Indian government bond yields is largely priced in, given the global economic trends and the valid channels. The resid_z values for the US Treasury yields are relatively low, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian 10-year bond yield has slumped to its lowest in nearly a month, and the Nifty 50 may react negatively to the higher crude prices and weaker INR. The metal_copper_channel suggests that global copper may lead Indian metal equities, which could be impacted by the higher crude prices.
- Watch next: nifty_50 (down) — not yet - watch; Higher crude prices may lead to a weaker INR and impact Indian equities
- Source: British government bond yields edge higher as Burnham becomes PM — ET Markets, 2026-07-20. https://economictimes.indiatimes.com/markets/bonds/british-government-bond-yields-edge-higher-as-burnham-becomes-pm/articleshow/132513109.cms
- Source: Global Market: German bond yields hit two-year high as oil surge fuels ECB rate hike bets — ET Markets, 2026-07-20. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-german-bond-yields-hit-two-year-high-as-oil-surge-fuels-ecb-rate-hike-bets/articleshow/132509565.cms
- Source: India 10-year bond slumps to lowest in nearly a month as Middle East oil risks heat up — ET Markets, 2026-07-20. https://economictimes.indiatimes.com/markets/bonds/india-10-year-bond-slumps-to-lowest-in-nearly-a-month-as-middle-east-oil-risks-heat-up/articleshow/132509213.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.25), 2026-03-30 (d=0.31)

### [RED 4.79] commodities · 3 series ↑
- corn [COMMODITIES]: last 475.00, z20 3.47, zc 0.58, resid-z 0.34 [quiet], 1d 6.80%, |z20|=3.47; 1y-pct=99
- wheat [COMMODITIES]: last 683.50, z20 2.21, zc 0.47, resid-z 0.33 [quiet], 1d 0.11%, |z20|=2.21; 1y-pct=100
- soybeans [COMMODITIES]: last 1219.50, z20 1.58, zc 0.78, resid-z 0.32 [quiet], 1d 1.25%, |z20|=1.58; 1y-pct=100
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_patanjali_ns (rho -0.501 via wheat, z -2.57, reacted); dyn_adanient_bo (rho -0.359 via soybeans, z 1.04, reacted)
- **India receivers**: dyn_patanjali_ns (rho -0.501, z -2.57); dyn_adanient_bo (rho -0.359, z 1.04)
- Historical analogues: 2026-05-22 (d=0.0), 2024-08-30 (d=0.27), 2026-05-06 (d=0.32)

### [RED 4.6] indices · 3 series ↓
- nikkei_225 [INDICES]: last 64113.21, z20 -3.28, zc -2.04, resid-z -1.47 [moved], 1d -4.07%, |z20|=3.28
- taiwan_weighted [INDICES]: last 42519.68, z20 -3.06, zc -4.81, resid-z -3.41 [unexplained], 1d -0.36%, |z20|=3.06
- kospi [INDICES]: last 6519.60, z20 -1.97, zc -1.50, resid-z -1.46 [moved], 1d -4.41%, |z20|=1.97
- **Mechanism**: indices · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.527 via kospi, z -0.36, quiet); dyn_hdbfs_bo (rho 0.491 via nikkei_225, z -1.52, reacted); dyn_ceatltd_ns (rho 0.469 via taiwan_weighted, z -1.56, reacted); nifty_midcap_100 (rho 0.437 via kospi, z 1.08, reacted); dyn_bhel_ns (rho 0.4 via taiwan_weighted, z 0.97, quiet)
- Watch next: nifty_metal (co-move) — not yet - watch; rho 0.527 vs kospi
- **India receivers**: nifty_metal (rho 0.527, z -0.36); dyn_hdbfs_bo (rho 0.491, z -1.52); dyn_ceatltd_ns (rho 0.469, z -1.56); nifty_midcap_100 (rho 0.437, z 1.08)

### [RED 4.54] dyn_icicigi_bo ↓
- dyn_icicigi_bo [EQUITIES]: last 1624.85, z20 -2.54, zc -0.44, resid-z -0.49 [quiet], 1d 0.78%, |z20|=2.54; 1y-pct=1
- **Mechanism**: dyn_icicigi_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-24 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.425 via dyn_icicigi_bo, z 1.08, reacted); dyn_indianb_ns (rho 0.371 via dyn_icicigi_bo, z 1.34, reacted); dyn_adanient_bo (rho 0.358 via dyn_icicigi_bo, z 1.04, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.425, z 1.08); dyn_indianb_ns (rho 0.371, z 1.34); dyn_adanient_bo (rho 0.358, z 1.04)
- Source: ICICI Bank gains while HDFC Bank, Axis Bank, Kotak Mahindra, Yes Bank decline after Q1 results — BusinessLine Mkts, 2026-07-20. https://www.thehindubusinessline.com/markets/stock-markets/bank-stocks-underperform-icici-bank-gains-while-hdfc-bank-axis-bank-kotak-mahindra-yes-bank-decline/article71243829.ece
- Source: ICICI beats HDFC on growth, margins in Q1. Is the lead sustainable? — Mint Markets, 2026-07-20. https://www.livemint.com/market/mark-to-market/icici-bank-hdfc-bank-q1fy27-loan-growth-nim-roa-casa-ldr-deposits-banking-rajiv-kumar-sashidhar-jagdishan-11784525565979.html
- Source: Stocks to buy or sell: Dharmesh Shah of ICICI Sec suggests buying Piramal Pharma on 20 July — Mint Markets, 2026-07-20. https://www.livemint.com/market/stock-market-news/stocks-to-buy-or-sell-dharmesh-shah-of-icici-sec-suggests-buying-piramal-pharma-on-20-july-11784519588311.html
- Historical analogues: 2026-06-24 (d=0.0), 2025-05-30 (d=0.03), 2026-01-07 (d=0.04)

### [RED 4.53] nasdaq_100 ↓
- nasdaq_100 [INDICES]: last 28590.24, z20 -2.53, zc -1.10, resid-z -1.07 [quiet], 1d -1.50%, |z20|=2.53
- **Mechanism**: nasdaq_100 ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.91 vs nasdaq_100
- Watch next: vix (inverse) — not yet - watch; rho -0.757 vs nasdaq_100
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.747 vs nasdaq_100
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.646 vs nasdaq_100
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.547 vs nasdaq_100
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Live: US stocks climb ahead of this week's megacap earnings — ET Markets, 2026-07-20. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-earnings-forecast-alphabet-tesla-intel-ibm-stock-price-news-20-july-2026/liveblog/132515320.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.0), 2025-10-07 (d=0.02)

## Watchlist (below surfacing floor)
shanghai_comp ↓ (4.48), gold_silver_ratio ↑ (4.13), natgas ↓ (3.56), dyn_ohi ↑ (3.55), usd_inr ↑ (3.54), dyn_bhel_ns ↑ (2.97), brent_wti_spread ↑ (2.96), dyn_nflx ↓ (2.9), usd_cny ↓ (2.89), dyn_pypl ↑ (2.82), dyn_patanjali_ns ↓ (2.57), cross-asset · 2 series ↑ (2.26)

## India macro
- nifty_50: 24239.5000 (1d -0.39%, z20 0.86, flag none)
- nifty_midcap_100: 62818.7500 (1d 0.63%, z20 1.08, flag amber)
- usd_inr: 96.4450 (1d -0.21%, z20 1.54, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5916 (1d 1.02%, z20 0.29, flag none)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 63.1 — "Q1 Results Today Highlights: Kotak Mahindra, YES Bank drive Q1 with 23%, 34% profit jump; "
- INOXINDIA.NS (INOX INDIA LIMITED) score 59.2 — "Gold recycling in India is growing, but far from mainstream"
- HDB (HDFC Bank Limited) score 57.5 — "Q1 Results Today Highlights: Kotak Mahindra, YES Bank drive Q1 with 23%, 34% profit jump; "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 51.7 — "Q1 Results Today Highlights: Kotak Mahindra, YES Bank drive Q1 with 23%, 34% profit jump; "
- BAC (Bank of America Corporation) score 46.4 — "Q1 Results Today Highlights: Kotak Mahindra, YES Bank drive Q1 with 23%, 34% profit jump; "
- COIN (Coinbase Global, Inc.) score 39.8 — "​5 global market themes investors will track this week"
- IDBI.NS (IDBI BANK LIMITED) score 39.2 — "Q1 Results Today Highlights: Kotak Mahindra, YES Bank drive Q1 with 23%, 34% profit jump; "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 37.0 — "Xtranet Technologies plans ₹167-crore IPO to fund expansion and debt repayment"
- TECHM.NS (TECH MAHINDRA LIMITED) score 22.6 — "Xtranet Technologies plans ₹167-crore IPO to fund expansion and debt repayment"
- BOND (PIMCO Active Bond Exchange-Tra) score 20.7 — "India 10-year bond slumps to lowest in nearly a month as Middle East oil risks heat up"
- CHKP (Check Point Software Technolog) score 19.6 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 2"
- VT (Vanguard Total World Stock Ind) score 13.7 — "Alpine Texworld IPO listing in focus. Here's what GMP signals ahead of debut"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 12.4 — "Q1 Results Today Highlights: Kotak Mahindra, YES Bank drive Q1 with 23%, 34% profit jump; "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 11.2 — "Europe's Heatwave Is Becoming an Energy Crisis"
- JIOFIN.BO (Jio Financial Services Limited) score 8.4 — "A bad health diagnosis will upend your financial plan, but you can set it right again"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.4 — "A bad health diagnosis will upend your financial plan, but you can set it right again"
- OHI (Omega Healthcare Investors, In) score 8.3 — "Rs 91,000 crore wipeout: What spooked HDFC Bank, Axis Bank and Kotak investors even as cre"
- JUSTDIAL.BO (JUST DIAL LTD.) score 6.6 — "Did Scientists Just Solve The Biggest Mystery Holding Back Solid-State Batteries"
- META (Meta) score 6.6 — "L&T bags mega orders in metals and minerals business from public and private sector compan"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 6.0 — "Tata Technologies Q1 Results: Profit rises 6% to Rs 180 crore"
- SKHYV (SK hynix Inc. American Deposit) score 5.7 — "SKHY – SK HYNIX DOWN 0.7% IN PREMARKET SK Hynix shares are slipping 0.7% in premarket afte"
- BHEL.NS (BHEL) score 5.4 — "BHEL share price: Brokerages see up to 23% upside after Maharatna PSU posts first Q1 profi"
- WIT (Wipro Limited) score 5.1 — "Stocks to watch: Reliance Industries, Wipro, CEAT among shares in focus today; check list "
- NFLX (Netflix, Inc.) score 5.1 — "Why Netflix’s AI push isn’t reviving the stock"
- GS (Goldman Sachs Group, Inc. (The) score 4.9 — "Goldman Sachs initiates coverage on Sansera Engineering, 3 other auto ancillary stocks wit"
- PCJEWELLER.NS (PC JEWELLER LTD) score 4.6 — "PC Jeweller shares jump 6%: What’s driving the rally after 220% gains in 3 years?"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 4.6 — "HAL, BEL to Bharat Dynamics: Defence stocks dip after escalation in the US-Iran war"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 3.3 — "Adani Ent Share Price Live Updates: Adani Enterprises  Current Price Update"
- CEATLTD.NS (CEAT LIMITED) score 2.8 — "Top Gainers & Losers on 20 July: Axis Bank, HDFC Bank, Ceat, India Cements, OLA, HFCL amon"
- AAPL (Apple Inc.) score 2.6 — "APPLE CLOSES IN ON NVIDIA $AAPL is on the verge of reclaiming the title of the world’s mos"
- NVDA (NVIDIA Corporation) score 2.6 — "APPLE CLOSES IN ON NVIDIA $AAPL is on the verge of reclaiming the title of the world’s mos"
- MS (Morgan Stanley) score 2.3 — "Dimon-led JPMorgan poised to become world's first $1 trillion bank"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 2.1 — "KUWAIT SAYS ELECTRICAL AND DESALINATION POWER PLANT DAMAGED IN IRANIAN ATTACK - ELECTRICIT"
- KALYANKJIL.NS (KALYAN JEWELLERS IND LTD) score 2.0 — "Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. T"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 2.0 — "Havells India’s margin recovery hinges on easing A&P spends, price hikes after weak Q1"
- RS (Reliance, Inc.) score 2.0 — "Reliance Industries share price rises after Q1 results. Should you buy or sell the stock?"
- PYPL (PayPal Holdings, Inc.) score 1.3 — "US stocks today: US stocks rise with earnings in focus; PayPal jumps on takeover bid repor"
- BIOCON.BO (BIOCON LTD.) score 1.2 — "Mylan exits Biocon, sells entire 5.64% stake for ₹3,679 crore via block deals"
- CUPID.NS (CUPID LIMITED) score 0.8 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 0.6 — "Patanjali Foods share price crashes 20%, extending losses for third straight session; what"

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