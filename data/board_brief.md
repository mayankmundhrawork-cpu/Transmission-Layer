# Transmission Layer — board brief · 2026-08-20 18:57Z

data as of **2026-08-20** · 98 series · 12 red / 26 amber · 8 events surfaced (19 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.293, 2d in regime; vol-pct 0.232, breadth-off 0.353, Markov P(high-vol) 0.02)
- [INVERTED] **safe_haven_gold** — corr20 -0.34, corr60 -0.39, contra nifty_50 corr20=0.01, last shift 2026-06-05. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.89, corr60 0.88, last shift 2026-02-05. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.22, corr60 0.4, last shift 2026-07-02. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.16, corr60 -0.12, last shift 2026-06-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.68, corr60 -0.82, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.02, corr60 -0.11, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.13, corr60 -0.16, last shift 2026-06-24. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.21, corr60 0.24, last shift 2026-04-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.00016991335699589882)
- **SETUP** dow_jones → asx_200: leads 1d (ccf 0.593, β 0.4879, p 0.0); driver zc -1.74 → expected -0.582%. Type hit-rate 0.827 (n=2433).
- **SETUP** dow_jones → nikkei_225: leads 1d (ccf 0.466, β 0.7886, p 0.0); driver zc -1.74 → expected -0.941%. Type hit-rate 0.827 (n=2433).
- **SETUP** dyn_jef → asx_200: leads 1d (ccf 0.456, β 0.1309, p 0.0); driver zc -1.52 → expected -0.396%. Type hit-rate 0.827 (n=2433).
- **SETUP** dow_jones → taiwan_weighted: leads 1d (ccf 0.424, β 0.7139, p 0.0); driver zc -1.74 → expected -0.852%. Type hit-rate 0.827 (n=2433).
- **SETUP** dow_jones → usd_brl: leads 1d (ccf -0.407, β -0.3514, p 0.0); driver zc -1.74 → expected 0.419%. Type hit-rate 0.827 (n=2433).
- **SETUP** dow_jones → aud_usd: leads 1d (ccf 0.399, β 0.2623, p 1e-05); driver zc -1.74 → expected -0.313%. Type hit-rate 0.827 (n=2433).
- **SETUP** dow_jones → usd_mxn: leads 1d (ccf -0.362, β -0.2377, p 0.0); driver zc -1.74 → expected 0.283%. Type hit-rate 0.827 (n=2433).
- **SETUP** dyn_jef → usd_mxn: leads 1d (ccf -0.26, β -0.0597, p 0.00023); driver zc -1.52 → expected 0.181%. Type hit-rate 0.827 (n=2433).
- Track record · residual_reversion: hit-rate **0.491** (n=1116) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.827** (n=2433) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.88] dyn_mrna ↑
- dyn_mrna [EQUITIES]: last 135.97, z20 7.88, zc 5.93, resid-z -0.64 [moved], 1d 36.89%, |z20|=7.88; 1y-pct=100
- **Mechanism**: dyn_mrna ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Moderna’s Cancer Vaccine Breakthrough: What It Means for the Stock — ET Markets, 2026-08-20. https://economictimes.indiatimes.com/markets/us-stocks/news/modernas-cancer-vaccine-breakthrough-what-it-means-for-the-stock/slideshow/133367426.cms
- Source: Moderna’s 177% Surge Burns Shorts in ‘Painful’ $5.5 Billion Loss — Mint Markets, 2026-08-19. https://www.livemint.com/market/modernas-177-surge-burns-shorts-in-painful-5-5-billion-loss-11787175519880.html
- Source: Moderna’s cancer-vaccine breakthrough drives broad biopharma stock rally — MarketWatch Top, 2026-08-19. https://www.marketwatch.com/story/modernas-cancer-vaccine-breakthrough-drives-broad-biopharma-stock-rally-ff2816aa?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-16 (d=0.01), 2025-08-20 (d=0.01)

### [RED 9.6] cross-asset · 3 series ↑
- btc_usd [CRYPTO]: last 72472.68, z20 6.28, zc 1.40, resid-z 2.67 [unexplained], 1d 4.63%, |z20|=6.28
- eth_usd [CRYPTO]: last 2319.95, z20 5.04, zc 0.50, resid-z 1.43 [quiet], 1d 3.04%, |z20|=5.04
- dyn_coin [EQUITIES]: last 170.44, z20 2.33, zc 1.27, resid-z -0.31 [quiet], 1d 6.39%, |z20|=2.33
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 1.95).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: vix (inverse) — not yet - watch; rho -0.57 vs eth_usd
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.5 vs eth_usd
- Source: Crypto comeback? Bitcoin, ethereum are headed for their best day in months as investors flock to hard assets — MarketWatch Top, 2026-08-20. https://www.marketwatch.com/story/crypto-comeback-bitcoin-ethereum-are-headed-for-their-best-day-in-months-as-investors-flock-to-hard-assets-1573b803?mod=mw_rss_topstories
- Source: Bitcoin rallies past $70,000 as falling US yields, Trump's crypto meeting boost optimism — Mint Markets, 2026-08-20. https://www.livemint.com/market/cryptocurrency/bitcoin-rallies-past-70-000-as-falling-us-yields-trumps-crypto-meeting-boost-optimism-11787226673971.html
- Source: Is Bitcoin finally nearing a bottom? Bitwise CIO Matt Hougan answers — ET Markets, 2026-08-20. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/is-bitcoin-finally-nearing-a-bottom-bitwise-cio-matt-hougan-answers/articleshow/133374496.cms
- Historical analogues: 2025-08-13 (d=1.95), 2025-05-08 (d=2.85), 2024-11-13 (d=3.11)

### [RED 7.52] cross-asset · 3 series ↑
- comex_gold [COMMODITIES]: last 4575.10, z20 2.17, zc 1.11, resid-z -0.53 [quiet], 1d 1.91%, |z20|=2.17; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 68.00, z20 1.96, zc 1.40, resid-z 0.59 [quiet], 1d 3.45%, |z20|=1.96; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 67.28, z20 -1.21, zc n/a, resid-z n/a [quiet], 1d -1.49%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.524 via comex_silver, z 0.57, quiet); dyn_stylebaaza_ns (rho 0.444 via comex_silver, z 2.54, reacted)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.648 vs comex_gold, historically leads by 1d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.569 vs comex_silver, historically leads by 4d
- Watch next: dax (co-move) — not yet - watch; rho 0.528 vs comex_gold, historically leads by 4d
- Watch next: nifty_metal (co-move) — not yet - watch; rho 0.524 vs comex_silver, historically leads by 4d
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.501 vs comex_silver
- **India receivers**: nifty_metal (rho 0.524, z 0.57); dyn_stylebaaza_ns (rho 0.444, z 2.54)
- Source: Gold reclaims momentum as US Treasury move sparks bullion rush, gains 2% in a day — BusinessLine Mkts, 2026-08-20. https://www.thehindubusinessline.com/markets/gold/gold-reclaims-momentum-as-us-treasury-move-sparks-bullion-rush-gains-2-in-a-day/article71369610.ece
- Source: Keralam gold jewellery trade bets big on Onam sales — BusinessLine Mkts, 2026-08-20. https://www.thehindubusinessline.com/markets/gold/kerala-gold-jewellery-trade-bets-big-on-onam-sales/article71368561.ece
- Source: Gold rises ₹264 to ₹1.58 lakh/10g on weak US dollar — BusinessLine Mkts, 2026-08-20. https://www.thehindubusinessline.com/markets/gold/gold-rises-264-to-158-lakh10g-on-weak-us-dollar/article71368617.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.17] fx · 4 series ↑
- eur_usd [FX]: last 1.17, z20 2.50, zc 2.69, resid-z 2.72 [unexplained], 1d 0.86%, |z20|=2.50
- gbp_usd [FX]: last 1.36, z20 2.24, zc 1.62, resid-z 1.60 [unexplained], 1d 0.67%, |z20|=2.24
- aud_usd [FX]: last 0.71, z20 1.89, zc 0.87, resid-z 0.93 [quiet], 1d 0.45%, |z20|=1.89
- usd_mxn [FX]: last 16.96, z20 -1.77, zc -1.76, resid-z -1.32 [moved], 1d -0.61%, |z20|=1.77; 1y-pct=0
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.585 via usd_mxn, z 0.49, quiet); dyn_hdbfs_bo (rho 0.412 via aud_usd, z 1.16, reacted); dyn_icicigi_bo (rho -0.393 via gbp_usd, z -0.67, quiet); nifty_midcap_100 (rho -0.37 via usd_mxn, z 0.63, quiet)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.544 vs eur_usd, historically leads by 5d
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.534 vs aud_usd
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.512 vs eur_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.585, z 0.49); dyn_hdbfs_bo (rho 0.412, z 1.16); dyn_icicigi_bo (rho -0.393, z -0.67); nifty_midcap_100 (rho -0.37, z 0.63)
- Source: Selloff in euro zone bonds pauses but oil prices keep up pressure — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/bonds/selloff-in-euro-zone-bonds-pauses-but-oil-prices-keep-up-pressure/articleshow/133341510.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [AMBER 6.11] brent ↑
- brent [COMMODITIES]: last 93.80, z20 1.11, zc 1.10, resid-z 0.44 [quiet], 1d 2.38%, 1-session move +2.38% ≥ 1.5%
- **Mechanism**: brent ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_voltas_ns (rho -0.392 via brent, z -2.68, reacted)
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.56 vs brent, historically leads by 5d
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.53 vs brent, historically leads by 5d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.658 vs brent
- Watch next: cac_40 (inverse) — not yet - watch; rho -0.507 vs brent
- **India receivers**: dyn_voltas_ns (rho -0.392, z -2.68)
- Source: China Is Squeezing India Out of Russia’s Oil Trade — OilPrice, 2026-08-20. https://oilprice.com/Latest-Energy-News/World-News/China-Is-Squeezing-India-Out-of-Russias-Oil-Trade.html
- Source: Crude oil prices surge to near one-month high as US prepares sweeping sanctions on Iran — Mint Markets, 2026-08-20. https://www.livemint.com/market/commodities/crude-oil-prices-surge-to-near-one-month-high-as-us-prepares-sweeping-sanctions-on-iran-11787244062232.html
- Source: Norway’s Oil Output Falls Nearly 200,000 Bpd as Gulf Supply Crisis Drags On — OilPrice, 2026-08-20. https://oilprice.com/Energy/Crude-Oil/Norways-Oil-Output-Falls-Nearly-200000-Bpd-as-Gulf-Supply-Crisis-Drags-On.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.0), 2024-10-18 (d=0.02)

### [RED 6.0] commodities · 3 series ↑
- corn [COMMODITIES]: last 502.50, z20 4.69, zc 4.86, resid-z 3.76 [unexplained], 1d 6.24%, |z20|=4.69; 1y-pct=100
- wheat [COMMODITIES]: last 699.50, z20 2.43, zc 1.55, resid-z 1.37 [moved], 1d 2.83%, |z20|=2.43; 1y-pct=99
- soybeans [COMMODITIES]: last 1236.00, z20 1.82, zc 1.10, resid-z 0.93 [quiet], 1d 1.12%, |z20|=1.82; 1y-pct=99
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_lenskart_ns (rho 0.36 via wheat, z 3.15, reacted)
- **India receivers**: dyn_lenskart_ns (rho 0.36, z 3.15)
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [RED 5.15] dyn_lenskart_ns ↑
- dyn_lenskart_ns [EQUITIES]: last 656.65, z20 3.15, zc 1.65, resid-z 1.58 [unexplained], 1d 2.67%, |z20|=3.15; 1y-pct=99
- **Mechanism**: dyn_lenskart_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/stocks/news/lenskart-solutions-among-4-stocks-to-hit-52-week-highs-amp-surge-up-to-25-in-a-month/slideshow/133348316.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

### [AMBER 4.83] cross-asset · 3 series ↑
- ust_30y [RATES]: last 5.28, z20 1.51, zc -0.71, resid-z -1.41 [quiet], 1d -0.56%, |z20|=1.51; 1y-pct=99
- ust_10y [RATES]: last 4.71, z20 0.98, zc -0.21, resid-z -0.85 [quiet], 1d -0.21%, 1y-pct=98
- dyn_bond [EQUITIES]: last 90.63, z20 -0.12, zc -1.21, resid-z 0.22 [quiet], 1d -0.37%, 1y-pct=4
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: tips_10y_real (co-move) — not yet - watch; rho 0.699 vs ust_30y, historically leads by 1d
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.534 vs ust_30y, historically leads by 1d
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.576 vs ust_10y
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.52 vs ust_30y
- Source: US Treasury's Bessent says upsized bond buybacks could increase further — ET Markets, 2026-08-20. https://economictimes.indiatimes.com/markets/us-stocks/news/us-treasurys-bessent-says-upsized-bond-buybacks-could-increase-further/articleshow/133384876.cms
- Source: US Treasury to double long-term bond buybacks as Bessent signals fiscal consolidation and focus on debt — Mint Markets, 2026-08-20. https://www.livemint.com/market/stock-market-news/us-treasury-to-double-long-term-bond-buybacks-as-bessent-signals-fiscal-consolidation-and-focus-on-debt-11787243166974.html
- Source: US Treasury to double long-term bond buybacks; Bessent signals fiscal push as each could top $4 billion — Mint Markets, 2026-08-20. https://www.livemint.com/market/stock-market-news/us-treasury-to-double-long-term-bond-buybacks-as-bessent-signals-fiscal-consolidation-and-focus-on-debt-11787243166974.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.12), 2025-04-23 (d=0.18)

## Watchlist (below surfacing floor)
dyn_stylebaaza_ns ↑ (4.54), midcap_largecap_ratio ↑ (4.39), dyn_meta ↓ (4.13), dyn_jef ↓ (4.12), usd_cny ↓ (3.39), dyn_tech ↑ (3.21), eur_inr ↑ (2.74), indices · 2 series ↑ (2.68), dyn_voltas_ns ↓ (2.68), dyn_icicigi_bo ↓ (2.67), dyn_tatatech_ns ↑ (2.51), dyn_lth ↑ (2.27)

## India macro
- nifty_50: 24231.8496 (1d 0.64%, z20 -0.35, flag none)
- nifty_midcap_100: 63668.2500 (1d 0.41%, z20 0.63, flag amber)
- usd_inr: 95.6950 (1d -0.13%, z20 0.12, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6275 (1d -0.22%, z20 1.39, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 103.6 — "China Is Squeezing India Out of Russia’s Oil Trade"
- INOXINDIA.NS (INOX INDIA LIMITED) score 101.6 — "China Is Squeezing India Out of Russia’s Oil Trade"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 100.9 — "China Is Squeezing India Out of Russia’s Oil Trade"
- INDIANB.NS (INDIAN BANK) score 89.5 — "Upstox begins talks with investment banks for $350-400 million IPO; crosses 2 crore custom"
- BOND (PIMCO Active Bond Exchange-Tra) score 76.6 — "Dow Jones| Nasdaq | US Stock Market Today | Live: Dow, Nasdaq slump over 1% as bond yields"
- BAC (Bank of America Corporation) score 71.8 — "Upstox begins talks with investment banks for $350-400 million IPO; crosses 2 crore custom"
- HDB (HDFC Bank Limited) score 66.2 — "Augmont Enterprises mops up Rs 246 crore in anchor round ahead of IPO; Nomura, HDFC MF amo"
- IDBI.NS (IDBI BANK LIMITED) score 60.9 — "Upstox begins talks with investment banks for $350-400 million IPO; crosses 2 crore custom"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 60.9 — "Upstox begins talks with investment banks for $350-400 million IPO; crosses 2 crore custom"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 60.8 — "Upstox begins talks with investment banks for $350-400 million IPO; crosses 2 crore custom"
- COIN (Coinbase Global, Inc.) score 56.2 — "Global Market: European blue-chip earnings outlook improves as recovery broadens"
- TECHM.NS (TECH MAHINDRA LIMITED) score 48.4 — "General Atlantic Singapore sells Rs 1,400 crore KFin Technologies stake; Invesco, Mirae As"
- OHI (Omega Healthcare Investors, In) score 47.6 — "Augmont Enterprises mops up Rs 246 crore in anchor round ahead of IPO; Nomura, HDFC MF amo"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 47.0 — "General Atlantic Singapore sells Rs 1,400 crore KFin Technologies stake; Invesco, Mirae As"
- TECH (Bio-Techne Corp) score 46.9 — "General Atlantic Singapore sells Rs 1,400 crore KFin Technologies stake; Invesco, Mirae As"
- LTH (Life Time Group Holdings, Inc.) score 40.0 — "Social Security union says it needs $3 billion and another 20,000 workers to fix long wait"
- CHKP (Check Point Software Technolog) score 35.6 — "IPOs GMP comparison: Check grey market winner - Shankesh Jewellers vs Sunshine Pictures vs"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.3 — "The energy market’s rising ‘crack spread’ is threatening to break the American consumer"
- JIOFIN.BO (Jio Financial Services Limited) score 22.1 — "Tourism Finance Corporation among 6 financial services stocks to hit 52-week highs & surge"
- PCJEWELLER.NS (PC JEWELLER LTD) score 21.9 — "Keralam gold jewellery trade bets big on Onam sales"
- 301077.SZ (CHINASTARS) score 20.8 — "Kazakhstan Caught in the Middle of the U.S.-China AI Rivalry"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 17.0 — "Tourism Finance Corporation among 6 financial services stocks to hit 52-week highs & surge"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 16.1 — "Coking Coal Prices Surge 25%, Squeezing India's Steelmakers"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 15.3 — "Tourism Finance Corporation among 6 financial services stocks to hit 52-week highs & surge"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 14.5 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 14.5 — "UPI adoption accelerates in capital markets, led by brokers and rising retail participatio"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.6 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- MS (Morgan Stanley) score 12.4 — "Treasury’s buyback blitz may end up driving bond yields higher, warns JPMorgan. Here’s its"
- MRNA (Moderna, Inc.) score 10.3 — "Moderna’s Cancer Vaccine Breakthrough: What It Means for the Stock"
- META (Meta) score 9.9 — "Silver futures jump nearly 1% to ₹2.38 lakh/kg as US Treasury move boosts precious metals"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.7 — "Gautam Adani’s big comeback: Adani Enterprises eyes Nifty crown"
- JEF (Jefferies Financial Group Inc.) score 9.0 — "Turtlemint shares soar 4% as Jefferies initiates buy call, sets ₹190 target"
- VT (Vanguard Total World Stock Ind) score 8.9 — "Beijing Bets on Fossil Fuels Even as It Leads the World in Renewables"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 8.7 — "ICICI Bank Share Price Live Updates: ICICI Bank Price Update"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.3 — "The national debt just hit $40 trillion. Here’s how it can hurt Americans."
- BHARATFORG.BO (BHARAT FORGE LTD.) score 7.6 — "Coforge shares jump 3% after IT major launches private equity unit"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.5 — "Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month"
- VOLTAS.NS (VOLTAS LTD) score 2.5 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.4 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.4 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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