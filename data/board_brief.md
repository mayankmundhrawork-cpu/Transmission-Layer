# Transmission Layer — board brief · 2026-07-24 06:43Z

data as of **2026-07-24** · 98 series · 6 red / 42 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.718, 2d in regime; vol-pct 0.687, breadth-off 0.75, Markov P(high-vol) 0.077)
- [WEAK] **safe_haven_gold** — corr20 -0.16, corr60 -0.45, contra nifty_50 corr20=0.15, last shift 2026-06-01. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.9, corr60 0.82, last shift 2026-05-15. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.51, corr60 0.35, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.06, corr60 -0.03, last shift 2026-06-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.93, corr60 -0.82, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.11, corr60 -0.09, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [INVERTED] **real_rates_gold_inverse** — corr20 0.25, corr60 -0.24, last shift 2026-05-08. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.36, corr60 0.25, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 90** scanned series survive multiplicity control (effective p ≤ 7.187263180563619e-05)
- **SETUP** sp500 → aud_usd: leads 1d (ccf 0.459, β 0.2731, p 0.0); driver zc -1.55 → expected -0.331%. Type hit-rate 0.822 (n=2986).
- **SETUP** vix → aud_usd: leads 1d (ccf -0.399, β -0.0257, p 1e-05); driver zc 1.53 → expected -0.319%. Type hit-rate 0.822 (n=2986).
- Track record · residual_reversion: hit-rate **0.494** (n=1164) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.822** (n=2986) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.706** (n=17) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.79] cross-asset · 11 series ↓
- ust_2y [RATES]: last 4.31, z20 2.92, zc 0.91, resid-z 1.09 [quiet], 1d 1.17%, |z20|=2.92; 1y-pct=100
- nasdaq_100 [INDICES]: last 28456.53, z20 -2.23, zc -1.35, resid-z -0.53 [quiet], 1d -1.87%, |z20|=2.23
- dyn_bond [EQUITIES]: last 90.44, z20 -2.10, zc -1.07, resid-z -0.22 [quiet], 1d -0.31%, |z20|=2.10; 1y-pct=0
- ust_10y [RATES]: last 4.67, z20 2.05, zc 0.90, resid-z 0.85 [quiet], 1d 0.86%, |z20|=2.05; 1y-pct=99
- russell_2000 [INDICES]: last 2940.07, z20 -1.95, zc -0.54, resid-z 1.55 [unexplained], 1d -0.67%, |z20|=1.95
- dow_jones [INDICES]: last 51702.23, z20 -1.92, zc -1.35, resid-z 0.37 [quiet], 1d -0.99%, |z20|=1.92
- cac_40 [INDICES]: last 8280.76, z20 -1.76, zc -2.25, resid-z -0.69 [priced], 1d -1.86%, |z20|=1.76
- tips_10y_real [RATES]: last 2.39, z20 1.74, zc 0.49, resid-z 0.30 [quiet], 1d 0.84%, |z20|=1.74; 1y-pct=100
- stoxx_50 [INDICES]: last 6197.62, z20 -1.64, zc -2.16, resid-z -0.58 [priced], 1d -1.89%, |z20|=1.64
- ust_30y [RATES]: last 5.15, z20 1.60, zc 0.61, resid-z 0.37 [quiet], 1d 0.39%, |z20|=1.60; 1y-pct=99
- vix [INDICES]: last 18.70, z20 1.52, zc 1.53, resid-z n/a [moved], 1d 12.38%, |z20|=1.52
- **Mechanism**: The recent surge in oil prices and Treasury yields has put pressure on Indian bonds, leading to a decline in their value. This, combined with the Federal Reserve's anticipated rate hike, has caused a risk-off sentiment in the market, driving investors towards safe-haven assets. The VALID vix_equity_inverse channel suggests that the vol spike will lead to an equity drawdown, which is already being reflected in the prices of Indian equities such as Nifty 50 and Nifty Midcap 100.
- **Gap**: No gap: the big raw move in oil prices and Treasury yields is PRICED, with the resid_z values for most series being relatively small, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instruments such as Nifty 50 and Nifty Midcap 100 have already reacted to the global equity downturn, while Dyn Indusindbk Bo is yet to move. The metal_copper_channel may also lead to a move in Indian metal equities.
- Watch next: nifty_50 (down) — already moved; reacted to global equity downturn
- Watch next: nifty_midcap_100 (down) — already moved; reacted to global equity downturn
- Watch next: dyn_indusindbk_bo (down) — not yet - watch; quiet despite correlated instrument dow_jones moving down
- **India receivers**: nifty_50 (rho 0.66, z -2.42); nifty_midcap_100 (rho 0.602, z -2.0); dyn_indusindbk_bo (rho 0.568, z -0.0)
- Source: Oil shock, Treasury yield spike put Indian bonds under pressure before debt sale — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/bonds/oil-shock-treasury-yield-spike-put-indian-bonds-under-pressure-before-debt-sale/articleshow/132596731.cms
- Source: ICICI Bank prices $1 billion five-year dollar bond at tighter spread — BusinessLine Mkts, 2026-07-24. https://www.thehindubusinessline.com/markets/icici-bank-prices-1-billion-five-year-dollar-bond-at-tighter-spread/article71260840.ece
- Source: US stocks today: Nasdaq plunges 2% as tech earnings spark AI spending worries — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-today-us-stocks-fall-as-tech-earnings-spark-ai-spending-worries-and-oil-hits-100/articleshow/132591456.cms
- Historical analogues: 2024-10-11 (d=0.94), 2025-10-06 (d=1.24), 2024-10-02 (d=1.31)

### [RED 7.41] dyn_qessf ↓
- dyn_qessf [EQUITIES]: last 0.17, z20 -5.41, zc -3.96, resid-z -0.72 [moved], 1d -25.39%, |z20|=5.41
- **Mechanism**: The decline in dyn_qessf is largely priced, with a resid_z of -0.72, indicating that the move is mostly explained by factor exposures. The valid metal_copper_channel and gold_silver_comove channels suggest that global metal prices and monetary metals co-movement are influencing the move. However, the broken channels, such as safe_haven_gold and inr_oil_channel, are not available as mechanisms to explain the move.
- **Gap**: No gap: the decline in dyn_qessf is largely priced, with a small resid_z
- **India take**: The Indian instrument that expresses this move is the Nifty Metal index, which has not reacted yet. The recent news about Apollo Micro Systems and HFCL's defence and aerospace growth potential may also influence the Indian metal equities.
- Watch next: nifty_50 (down) — not yet - watch; RISK_OFF regime and valid vix_equity_inverse channel
- Source: Ashish Kacholia exits defence stock that rallied 108% in Q1. Do you own it? — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/stocks/news/ashish-kacholia-exits-defence-stock-that-rallied-108-in-q1-do-you-own-it/articleshow/132597323.cms
- Source: Multibagger defence stock Apollo Micro Systems to be in focus tomorrow; here's why — Mint Markets, 2026-07-22. https://www.livemint.com/market/stock-market-news/multibagger-defence-stock-apollo-micro-systems-to-be-in-focus-tomorrow-heres-why-11784728706086.html
- Source: HFCL's X-factor is defence & aerospace? Deven Choksey sees another 66% upside potential, here's why — ET Markets, 2026-07-22. https://economictimes.indiatimes.com/markets/stocks/news/hfcls-x-factor-is-defence-aerospace-deven-choksey-sees-another-66-upside-potential-heres-why/articleshow/132553438.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-15 (d=0.32), 2024-11-14 (d=0.52)

### [RED 6.7] commodities · 3 series ↑
- corn [COMMODITIES]: last 490.50, z20 3.38, zc 4.55, resid-z 0.14 [moved], 1d 5.71%, |z20|=3.38; 1y-pct=100
- soybeans [COMMODITIES]: last 1253.50, z20 1.79, zc 1.28, resid-z 0.02 [quiet], 1d 1.29%, |z20|=1.79; 1y-pct=100
- wheat [COMMODITIES]: last 705.25, z20 1.74, zc 0.60, resid-z -0.88 [quiet], 1d 1.29%, |z20|=1.74; 1y-pct=99
- **Mechanism**: The recent surge in commodity prices, particularly wheat, corn, and soybeans, is driven by supply concerns due to scorching heat in key US wheat-growing states and escalating attacks between Russia and Ukraine, which put exports at risk. This move is priced, as evidenced by the low resid_z values for these commodities. The valid metal_copper_channel and gold_silver_comove channels may transmit this move to Indian metal equities and monetary metals.
- **Gap**: No gap: the current price move is largely explained by the factors, with low resid_z values indicating that the move is priced
- **India take**: Indian instruments such as dyn_patanjali_ns and dyn_adanient_bo have already reacted to the commodity price movement, reflecting the transmission of global commodity trends to Indian markets. The metal_copper_channel may further influence Indian metal equities.
- Watch next: dyn_patanjali_ns (down) — already moved; reacted to wheat price movement
- Watch next: dyn_adanient_bo (down) — already moved; reacted to soybeans price movement
- **India receivers**: dyn_patanjali_ns (rho -0.517, z -1.51); dyn_adanient_bo (rho -0.373, z -1.43)
- Source: Heat Worries US Wheat Farmers Just as Crop Prices Surge — Mint Markets, 2026-07-23. https://www.livemint.com/market/heat-worries-us-wheat-farmers-just-as-crop-prices-surge-11784841971254.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-08-30 (d=0.27), 2026-05-06 (d=0.32)

### [AMBER 5.74] indices · 3 series ↓
- nifty_50 [INDICES]: last 23707.80, z20 -2.42, zc -0.87, resid-z 0.45 [quiet], 1d -0.68%, |z20|=2.42
- nifty_midcap_100 [INDICES]: last 61320.80, z20 -2.00, zc -0.65, resid-z -0.59 [quiet], 1d -0.61%, |z20|=2.00
- india_vix [INDICES]: last 14.20, z20 1.65, zc 0.92, resid-z n/a [quiet], 1d 5.38%, |z20|=1.65
- **Mechanism**: The current market downturn is driven by a combination of factors, including oil prices exceeding $100 per barrel and FII selling, which has led to a broad-based sell-off in the Indian stock markets. The Nifty 50 and Sensex indices have declined significantly, with the Nifty 50 falling below key support levels. The valid vix_equity_inverse channel suggests that the vol spike will lead to an equity drawdown, which is consistent with the current market movement.
- **Gap**: No gap: the big raw move in Nifty 50 is largely priced, with a resid_z of 0.45, indicating that the move is mostly explained by factor exposures
- **India take**: The Indian instruments that express this move are dyn_jiofin_bo and dyn_adanient_bo, which have already reacted with z20 scores of -1.3 and -1.43, respectively. The Nifty 50 and Nifty Midcap 100 indices have also declined, with the Nifty 50 falling below key support levels.
- Watch next: nifty_50 (down) — already moved; oil prices and FII selling
- Watch next: nifty_midcap_100 (down) — already moved; broader market decline
- **India receivers**: dyn_jiofin_bo (rho 0.896, z -1.3); dyn_indusindbk_bo (rho 0.688, z -0.0); dyn_indianb_ns (rho 0.638, z -0.07); dyn_eternal_ns (rho 0.637, z -0.42)
- Source: Sensex today | Stock Market Live: Sensex down 700 pts, Nifty near 23,650; IndiGo, Infosys drops 2%, Meesho falls 6% post Q2 results — BusinessLine Mkts, 2026-07-24. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-24th-july-2026/article71257579.ece
- Source: Why is market falling today? Sensex slumps over 850 points: 7 key factors behind Rs 5 lakh crore rout — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/stocks/news/why-is-market-falling-today-sensex-drops-over-700-points-nifty-below-23700-7-key-factors-behind-d-street-selloff/articleshow/132595743.cms
- Source: Nifty slips below key support as crude tops $100, tech selloff rattles global markets — BusinessLine Mkts, 2026-07-24. https://www.thehindubusinessline.com/markets/stock-markets/nifty-slips-below-key-support-as-crude-tops-100-tech-selloff-rattles-global-markets/article71260841.ece
- Historical analogues: 2025-07-21 (d=0.56), 2025-07-14 (d=0.79), 2025-12-29 (d=1.03)

### [RED 5.39] usd_jpy ↑
- usd_jpy [FX]: last 163.79, z20 3.39, zc 1.39, resid-z -0.77 [quiet], 1d 0.43%, |z20|=3.39; 1y-pct=100
- **Mechanism**: usd_jpy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: asx_200 (inverse) — not yet - watch; rho -0.522 vs usd_jpy, historically leads by 2d
- Source: Global Market: US urges BOJ to keep raising rates, flags persistent yen weakness despite narrower yield gap — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-us-urges-boj-to-keep-raising-rates-flags-persistent-yen-weakness-despite-narrower-yield-gap/articleshow/132596001.cms
- Source: Yen’s Slump Extends Beyond Dollar and Stokes Inflation Fears — Mint Markets, 2026-07-23. https://www.livemint.com/market/yens-slump-extends-beyond-dollar-and-stokes-inflation-fears-11784836659389.html
- Source: Dollar hits new 40-year high versus yen, euro softer after ECB stands pat on rates — Mint Markets, 2026-07-23. https://www.livemint.com/market/dollar-hits-new-40-year-high-versus-yen-euro-softer-after-ecb-stands-pat-on-rates-11784833989812.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2024-11-08 (d=0.01)

### [AMBER 5.08] commodities · 2 series ↑
- brent [COMMODITIES]: last 99.77, z20 2.25, zc -0.24, resid-z 1.65 [unexplained], 1d -0.91%, |z20|=2.25; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 91.20, z20 2.17, zc -0.33, resid-z 1.30 [quiet], 1d -1.07%, |z20|=2.17
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.662 via brent, z -2.0, reacted); nifty_50 (rho -0.519 via brent, z -2.42, reacted); dyn_indusindbk_bo (rho -0.503 via brent, z -0.0, quiet)
- Watch next: dyn_indusindbk_bo (inverse) — not yet - watch; rho -0.503 vs brent
- **India receivers**: nifty_midcap_100 (rho -0.662, z -2.0); nifty_50 (rho -0.519, z -2.42); dyn_indusindbk_bo (rho -0.503, z -0.0)
- Source: Global Market: Japanese investors dump overseas bonds as rising crude revives inflation fears — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japanese-investors-dump-overseas-bonds-as-rising-crude-revives-inflation-fears/articleshow/132597360.cms
- Source: Oil Tops $100 as Supply Crisis Deepens — OilPrice, 2026-07-24. https://oilprice.com/Latest-Energy-News/World-News/Oil-Tops-100-as-Supply-Crisis-Deepens.html
- Source: Global Market: China, Hong Kong stocks slide as oil surge fuels inflation concerns — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-hong-kong-stocks-slide-as-oil-surge-fuels-inflation-concerns/articleshow/132597129.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [AMBER 4.44] dyn_hdb ↓
- dyn_hdb [EQUITIES]: last 23.15, z20 -2.44, zc -0.10, resid-z -0.99 [quiet], 1d -0.15%, |z20|=2.44; 1y-pct=0
- **Mechanism**: dyn_hdb ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.66 via dyn_hdb, z -2.42, reacted); nifty_midcap_100 (rho 0.528 via dyn_hdb, z -2.0, reacted); dyn_jiofin_bo (rho 0.482 via dyn_hdb, z -1.3, reacted)
- **India receivers**: nifty_50 (rho 0.66, z -2.42); nifty_midcap_100 (rho 0.528, z -2.0); dyn_jiofin_bo (rho 0.482, z -1.3)
- Source: HDFC Bank shares fall as 3 US law firms launch probe over alleged federal law violations — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-bank-shares-fall-as-3-us-law-firms-launch-probe-over-alleged-federal-law-violations/articleshow/132598223.cms
- Source: HDFC Bank, 3 other bank stocks wipe out Rs 1.5 lakh crore of investors' wealth after Q1. Time to buy the dip? — ET Markets, 2026-07-24. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-bank-3-other-bank-stocks-wipe-out-rs-1-5-lakh-crore-of-investors-wealth-after-q1-time-to-buy-the-dip/articleshow/132596148.cms
- Source: HDFC Bank shares slide 10% in four day after Q1 results but brokerages see up to 40% upside. Here’s why — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-bank-shares-slide-10-in-four-day-after-q1-results-but-brokerages-see-up-to-40-upside-heres-why/articleshow/132573294.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [AMBER 4.2] dyn_bharatcoal_ns ↓
- dyn_bharatcoal_ns [EQUITIES]: last 34.42, z20 -2.20, zc -0.43, resid-z n/a [quiet], 1d -1.21%, |z20|=2.20
- **Mechanism**: dyn_bharatcoal_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Q1 Results Today Live: Shriram Finance, TCP, BoB, Hindustan Zinc, ACC, Dalmia Bharat, Jindal Steel, Lodha, SBI Life, CG Power, NTPC, SAIL, Welspun Corp to announce Q1 results, Cipla & Sona BLW shares up, Infosys, IndiGo & Meesho shares down after Q1 — BusinessLine Mkts, 2026-07-24. https://www.thehindubusinessline.com/markets/fy27-q1-results-today-live-updates-shriram-finance-hindustan-zinc-dalmia-bharat-tata-consumer-jindal-steel-lodha-laurus-labs-sbi-life-cg-power-ntpc-infosys-indigo-cipla-results-24-july-2026/article71257341.ece
- Source: Sotefin Bharat IPO listing: Shares hit upper circuit after listing at a 10% premium; details here — Mint Markets, 2026-07-23. https://www.livemint.com/market/ipo/sotefin-bharat-ipo-listing-shares-hit-upper-circuit-after-listing-at-a-10-premium-details-here-11784782273860.html
- Source: Sotefin Bharat shares set for BSE SME debut today. GMP signals muted listing — ET Markets, 2026-07-23. https://economictimes.indiatimes.com/markets/stocks/news/sotefin-bharat-shares-set-for-bse-sme-debut-today-gmp-signals-muted-listing/articleshow/132571290.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-11 (d=0.3), 2026-07-03 (d=0.75)

## Watchlist (below surfacing floor)
dyn_ohi ↑ (4.17), nikkei_225 ↓ (3.98), dyn_patanjali_ns ↓ (3.51), gold_silver_ratio ↑ (3.49), usd_inr ↑ (3.17), eur_usd ↓ (3.1), dyn_infy ↓ (3.06), dyn_hdbfs_bo ↓ (2.96), dyn_icicigi_bo ↓ (2.95), dyn_aapl ↑ (2.66), dyn_lth ↑ (2.56), brent_wti_spread ↑ (2.54)

## India macro
- nifty_50: 23707.8008 (1d -0.68%, z20 -2.42, flag amber)
- nifty_midcap_100: 61320.8008 (1d -0.61%, z20 -2.00, flag amber)
- usd_inr: 96.5270 (1d -0.03%, z20 1.17, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5865 (1d 0.07%, z20 0.08, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 87.8 — "Caliber Mining and Logistics IPO listing date today. GMP, experts signal debut at decent p"
- INOXINDIA.NS (INOX INDIA LIMITED) score 81.8 — "Stock recommendations for 24 July from MarketSmith India"
- HDB (HDFC Bank Limited) score 69.4 — "Three bank stocks FIIs quietly bought in June quarter. Should you take a closer look?"
- BAC (Bank of America Corporation) score 66.0 — "Three bank stocks FIIs quietly bought in June quarter. Should you take a closer look?"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 65.8 — "Three bank stocks FIIs quietly bought in June quarter. Should you take a closer look?"
- IDBI.NS (IDBI BANK LIMITED) score 59.9 — "Three bank stocks FIIs quietly bought in June quarter. Should you take a closer look?"
- COIN (Coinbase Global, Inc.) score 58.1 — "US SETS NEW 10%-12.5% TARIFFS AS GLOBAL 10% PENALTY EXPIRES"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 53.6 — "Stock recommendations for 24 July from MarketSmith India"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 48.6 — "Xtranet Technologies IPO Day 2: Issue subscribed 1.38x so far. GMP hints 6% listing gain. "
- TECHM.NS (TECH MAHINDRA LIMITED) score 45.5 — "Xtranet Technologies IPO Day 2: Issue subscribed 1.38x so far. GMP hints 6% listing gain. "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 38.1 — "Three bank stocks FIIs quietly bought in June quarter. Should you take a closer look?"
- COALINDIA.NS (COAL INDIA LTD) score 31.9 — "Stock recommendations for 24 July from MarketSmith India"
- OHI (Omega Healthcare Investors, In) score 29.9 — "Sensex crashes 900 points, Nifty 50 nears 23,600; investors lose  ₹6 lakh crore. Why is ma"
- CHKP (Check Point Software Technolog) score 25.0 — "Stocks to watch: NTPC, Shriram Finance, Infosys among shares in focus today; check list he"
- BOND (PIMCO Active Bond Exchange-Tra) score 25.0 — "ICICI Bank prices $1 billion five-year dollar bond at tighter spread"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.1 — "The AI Paradox Reshaping Clean Energy Research"
- INFY (Infosys Limited) score 17.8 — "Stocks to watch: NTPC, Shriram Finance, Infosys among shares in focus today; check list he"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 15.2 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Trading Update"
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.7 — "Trump's new global tariff draws rebukes from trade partners over forced-labor justificatio"
- VT (Vanguard Total World Stock Ind) score 10.8 — "U.S. Refinery Utilization Hits 96.2% as Fuel Markets Tighten Worldwide"
- LTH (Life Time Group Holdings, Inc.) score 10.6 — "Gold prices fall Rs 3,500/10 gram in 2 days, silver down Rs 8,700/kg as oil hits $100 agai"
- JIOFIN.BO (Jio Financial Services Limited) score 9.7 — "Are you looking for financial advice? This is the best way to ask for it."
- ICICIGI.BO (ICICI Lombard General Insuranc) score 9.6 — "ICICI Bank prices $1 billion five-year dollar bond at tighter spread"
- GS (Goldman Sachs Group, Inc. (The) score 9.0 — "Oil Price Today (July 23): Crude oil crosses $95 as US strikes enter 12th day. Why Goldman"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.7 — "Are you looking for financial advice? This is the best way to ask for it."
- MS (Morgan Stanley) score 8.5 — "Infosys shares fall 3% as JPMorgan downgrades stock, Jefferies cuts target after Q1 result"
- META (Meta) score 7.3 — "Gold prices fall Rs 3,500/10 gram in 2 days, silver down Rs 8,700/kg as oil hits $100 agai"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 6.0 — "Q1 Results Today Live: Shriram Finance, TCP, BoB, Hindustan Zinc, ACC, Dalmia Bharat, Jind"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 5.9 — "Q1 results 2026: NTPC, Tata Consumer, Bank of Baroda, REC, Hind Zinc, among 80+ companies "
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 5.2 — "Ashish Kacholia exits defence stock that rallied 108% in Q1. Do you own it?"
- PCJEWELLER.NS (PC JEWELLER LTD) score 5.0 — "Bluestone Jewellery shares rocket 36% in just three days after Q1 results. Can the momentu"
- ETERNAL.NS (ETERNAL LIMITED) score 5.0 — "Stocks to Watch, July 24: Infosys, Shadowfax, Akums, Swiggy and Eternal"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 4.9 — "IEX Q1 results: Net profit grows 12% YoY to  ₹135 crore; electricity volumes rise 16%"
- NVDA (NVIDIA Corporation) score 4.7 — "AMD’s rivalry with Nvidia is increasingly moving into a new realm"
- AAPL (Apple Inc.) score 4.0 — "FORD WILL USE APPLE SOFTWARE IN NEW SELF-DRIVING SYSTEM: NYT"
- NFLX (Netflix, Inc.) score 2.6 — "US stocks to buy for short term: From Nvidia to Netflix- Appreciate CEO suggests picking t"
- WIT (Wipro Limited) score 2.2 — "Stocks to watch: Reliance Industries, Wipro, CEAT among shares in focus today; check list "
- BIOCON.BO (BIOCON LTD.) score 1.5 — "Stocks to buy for short term: Biocon among 3 shares Ajit Mishra of Religare Broking recomm"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 1.1 — "Newly-listed SME stock DSM Fresh Foods jumps over 30% in 2 days after reporting a 58% YoY "
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