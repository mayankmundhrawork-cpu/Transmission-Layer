# Transmission Layer — board brief · 2026-08-21 04:52Z

data as of **2026-08-21** · 98 series · 13 red / 24 amber · 8 events surfaced (21 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.292, 2d in regime; vol-pct 0.209, breadth-off 0.375, Markov P(high-vol) 0.025)
- [INVERTED] **safe_haven_gold** — corr20 -0.4, corr60 -0.41, contra nifty_50 corr20=0.02, last shift 2026-06-08. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.87, last shift 2026-01-29. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.22, corr60 0.37, last shift 2026-07-03. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.14, corr60 -0.13, last shift 2026-06-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.69, corr60 -0.83, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.03, corr60 -0.13, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.21, last shift 2026-06-25. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.25, corr60 0.22, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 0.0)
- **SETUP** dow_jones → nikkei_225: leads 1d (ccf 0.466, β 0.7872, p 0.0); driver zc -1.88 → expected -1.015%. Type hit-rate 0.819 (n=2375).
- **SETUP** dow_jones → taiwan_weighted: leads 1d (ccf 0.423, β 0.7098, p 0.0); driver zc -1.88 → expected -0.915%. Type hit-rate 0.819 (n=2375).
- **SETUP** dyn_ms → nikkei_225: leads 1d (ccf 0.416, β 0.3445, p 0.0); driver zc -1.84 → expected -1.082%. Type hit-rate 0.819 (n=2375).
- **SETUP** tips_10y_real → usd_jpy: leads 1d (ccf 0.409, β 0.1225, p 0.0); driver zc -1.66 → expected -0.305%. Type hit-rate 0.819 (n=2375).
- **SETUP** dow_jones → usd_brl: leads 1d (ccf -0.407, β -0.3515, p 0.0); driver zc -1.88 → expected 0.453%. Type hit-rate 0.819 (n=2375).
- **SETUP** dow_jones → aud_usd: leads 1d (ccf 0.397, β 0.2604, p 1e-05); driver zc -1.88 → expected -0.336%. Type hit-rate 0.819 (n=2375).
- **SETUP** dyn_ms → taiwan_weighted: leads 1d (ccf 0.392, β 0.322, p 0.0); driver zc -1.84 → expected -1.012%. Type hit-rate 0.819 (n=2375).
- **SETUP** dow_jones → usd_mxn: leads 1d (ccf -0.363, β -0.2365, p 0.0); driver zc -1.88 → expected 0.305%. Type hit-rate 0.819 (n=2375).
- **SETUP** dyn_coin → asx_200: leads 1d (ccf 0.314, β 0.0485, p 0.0); driver zc 1.52 → expected 0.371%. Type hit-rate 0.819 (n=2375).
- **SETUP** dyn_ms → aud_usd: leads 1d (ccf 0.276, β 0.0883, p 0.00287); driver zc -1.84 → expected -0.278%. Type hit-rate 0.819 (n=2375).
- **SETUP** dyn_jef → usd_mxn: leads 1d (ccf -0.261, β -0.0597, p 0.00022); driver zc -1.64 → expected 0.194%. Type hit-rate 0.819 (n=2375).
- Track record · residual_reversion: hit-rate **0.491** (n=1106) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.819** (n=2375) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.81] dyn_mrna ↑
- dyn_mrna [EQUITIES]: last 133.34, z20 7.81, zc 5.86, resid-z 11.29 [unexplained], 1d 35.87%, |z20|=7.81; 1y-pct=100
- **Mechanism**: dyn_mrna ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Moderna’s personalized mRNA shot could reshape the fight against skin cancer — but it may also be overhyped — MarketWatch Top, 2026-08-20. https://www.marketwatch.com/story/modernas-personalized-mrna-shot-could-reshape-the-fight-against-skin-cancer-but-it-may-also-be-overhyped-a6f1bc88?mod=mw_rss_topstories
- Source: Moderna’s Cancer Vaccine Breakthrough: What It Means for the Stock — ET Markets, 2026-08-20. https://economictimes.indiatimes.com/markets/us-stocks/news/modernas-cancer-vaccine-breakthrough-what-it-means-for-the-stock/slideshow/133367426.cms
- Source: Moderna’s 177% Surge Burns Shorts in ‘Painful’ $5.5 Billion Loss — Mint Markets, 2026-08-19. https://www.livemint.com/market/modernas-177-surge-burns-shorts-in-painful-5-5-billion-loss-11787175519880.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-16 (d=0.01), 2025-08-20 (d=0.01)

### [RED 7.87] cross-asset · 3 series ↑
- comex_gold [COMMODITIES]: last 4597.70, z20 2.09, zc 1.15, resid-z 0.72 [quiet], 1d 1.80%, |z20|=2.09; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 69.03, z20 2.02, zc 0.56, resid-z 1.92 [unexplained], 1d 1.48%, |z20|=2.02; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 66.60, z20 -1.55, zc n/a, resid-z n/a [quiet], 1d 0.32%, GSR<75 (extreme low); |z20|=1.55
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.531 via comex_silver, z 0.88, quiet); dyn_stylebaaza_ns (rho -0.394 via gold_silver_ratio, z 1.97, reacted)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.659 vs comex_gold, historically leads by 1d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.575 vs comex_silver, historically leads by 4d
- Watch next: dax (co-move) — not yet - watch; rho 0.538 vs comex_gold, historically leads by 4d
- Watch next: nifty_metal (co-move) — not yet - watch; rho 0.531 vs comex_silver, historically leads by 4d
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.505 vs comex_silver
- **India receivers**: nifty_metal (rho 0.531, z 0.88); dyn_stylebaaza_ns (rho -0.394, z 1.97)
- Source: Gold heads for third weekly gain on softer dollar, lower US yields — BusinessLine Mkts, 2026-08-21. https://www.thehindubusinessline.com/markets/gold/gold-heads-for-third-weekly-gain-on-softer-dollar-lower-us-yields/article71372098.ece
- Source: MCX gold nears  ₹1,60,000, silver at  ₹2,45,000 amid positive global cues; experts highlight key levels to watch — Mint Markets, 2026-08-21. https://www.livemint.com/market/commodities/mcx-gold-nears-1-60-000-silver-at-2-45-000-amid-positive-global-cues-experts-highlight-key-levels-to-watch-11787283205483.html
- Source: Dividend alert! Last day to buy Senco Gold, NALCO and 8 other stocks for dividend rewards — ET Markets, 2026-08-21. https://economictimes.indiatimes.com/markets/stocks/news/dividend-alert-last-day-to-buy-senco-gold-nalco-among-10-stocks-for-dividend-rewards/articleshow/133390915.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 7.86] cross-asset · 3 series ↑
- btc_usd [CRYPTO]: last 74962.68, z20 4.54, zc 0.86, resid-z 2.80 [unexplained], 1d 3.10%, |z20|=4.54
- eth_usd [CRYPTO]: last 2352.92, z20 3.50, zc 0.29, resid-z 1.39 [quiet], 1d 1.48%, |z20|=3.50
- dyn_coin [EQUITIES]: last 172.46, z20 2.62, zc 1.52, resid-z 2.13 [unexplained], 1d 7.65%, |z20|=2.62
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.86).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: vix (inverse) — not yet - watch; rho -0.589 vs eth_usd
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.515 vs eth_usd
- Source: Global Market: KOSPI gains on chip boost; foreigners turn net buyers — ET Markets, 2026-08-21. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-kospi-gains-on-chip-boost-foreigners-turn-net-buyers/articleshow/133392890.cms
- Source: Welspun Corp shares surge 9% after Rs 17,200 crore order win; global order book hits record Rs 42,000 crore — ET Markets, 2026-08-21. https://economictimes.indiatimes.com/markets/stocks/news/welspun-corp-shares-in-focus-after-rs-17200-crore-order-global-order-book-hits-record-rs-42000-crore/articleshow/133392199.cms
- Source: MCX gold nears  ₹1,60,000, silver at  ₹2,45,000 amid positive global cues; experts highlight key levels to watch — Mint Markets, 2026-08-21. https://www.livemint.com/market/commodities/mcx-gold-nears-1-60-000-silver-at-2-45-000-amid-positive-global-cues-experts-highlight-key-levels-to-watch-11787283205483.html
- Historical analogues: 2025-08-13 (d=0.86), 2025-05-09 (d=1.97), 2024-11-13 (d=2.15)

### [RED 6.69] tips_10y_real ↓
- tips_10y_real [RATES]: last 2.35, z20 -3.69, zc -1.66, resid-z -1.10 [moved], 1d -2.49%, 1d move -6.0bps ≥ 5bps; |z20|=3.69
- **Mechanism**: tips_10y_real ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.866 vs tips_10y_real, historically leads by 1d
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.864 vs tips_10y_real, historically leads by 1d
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.759 vs tips_10y_real, historically leads by 1d
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.725 vs tips_10y_real
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.517 vs tips_10y_real
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-10 (d=0.0), 2025-05-22 (d=0.07)

### [AMBER 6.15] wti ↑
- wti [COMMODITIES]: last 86.51, z20 1.15, zc -0.63, resid-z 0.35 [quiet], 1d -1.50%, 1-session move -1.50% ≥ 1.5%
- **Mechanism**: wti ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.628 vs wti
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.507 vs wti
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.505 vs wti
- Source: Crude oil price: Futures decline as US threatens ‘toughest sanctions’ on Iran — BusinessLine Mkts, 2026-08-21. https://www.thehindubusinessline.com/markets/commodities/crude-oil-price-futures-decline-as-us-threatens-toughest-sanctions-on-iran/article71372160.ece
- Source: Nifty holds 24,000 as crude, bond yields keep bulls in check — BusinessLine Mkts, 2026-08-21. https://www.thehindubusinessline.com/markets/nifty-holds-24000-as-crude-bond-yields-keep-bulls-in-check/article71372134.ece
- Source: Markets poised for higher open amid caution over oil, bond stress — BusinessLine Mkts, 2026-08-21. https://www.thehindubusinessline.com/markets/markets-poised-for-higher-open-amid-caution-over-oil-bond-stress/article71372068.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

### [AMBER 6.01] fx · 4 series ↑
- eur_usd [FX]: last 1.17, z20 2.35, zc 0.50, resid-z 2.57 [unexplained], 1d 0.19%, |z20|=2.35
- aud_usd [FX]: last 0.71, z20 2.27, zc 0.42, resid-z 1.25 [quiet], 1d 0.26%, |z20|=2.27
- gbp_usd [FX]: last 1.36, z20 2.15, zc 0.73, resid-z 1.11 [quiet], 1d 0.31%, |z20|=2.15
- usd_mxn [FX]: last 16.93, z20 -1.71, zc -0.34, resid-z -1.37 [quiet], 1d -0.13%, |z20|=1.71; 1y-pct=0
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.581 via usd_mxn, z 1.55, reacted); nifty_midcap_100 (rho 0.428 via aud_usd, z 0.4, quiet); dyn_icicigi_bo (rho -0.408 via gbp_usd, z -1.05, reacted)
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.612 vs eur_usd, historically leads by 4d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.542 vs eur_usd
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.525 vs aud_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.581, z 1.55); nifty_midcap_100 (rho 0.428, z 0.4); dyn_icicigi_bo (rho -0.408, z -1.05)
- Source: Selloff in euro zone bonds pauses but oil prices keep up pressure — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/bonds/selloff-in-euro-zone-bonds-pauses-but-oil-prices-keep-up-pressure/articleshow/133341510.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 4.87] commodities · 2 series ↑
- corn [COMMODITIES]: last 501.25, z20 4.04, zc 3.66, resid-z 0.65 [moved], 1d 4.70%, |z20|=4.04; 1y-pct=100
- wheat [COMMODITIES]: last 703.75, z20 2.93, zc 1.77, resid-z 0.12 [moved], 1d 3.08%, |z20|=2.93; 1y-pct=99
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [RED 4.74] dxy ↓
- dxy [FX]: last 98.77, z20 -1.74, zc -0.37, resid-z -2.52 [unexplained], 1d -0.13%, 20d range extreme; |z20|=1.74
- **Mechanism**: dxy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

## Watchlist (below surfacing floor)
dyn_jef ↓ (4.21), dyn_lenskart_ns ↑ (4.17), midcap_largecap_ratio ↑ (4.06), dyn_stylebaaza_ns ↑ (3.97), dyn_cartrade_ns ↑ (3.51), dyn_icicigi_bo ↓ (3.05), dyn_tech ↑ (2.92), usd_cny ↓ (2.68), eur_inr ↑ (2.46), dyn_lth ↑ (2.44), dyn_tatatech_ns ↑ (2.29), nifty_fmcg ↓ (2.19)

## India macro
- nifty_50: 24232.8008 (1d 0.00%, z20 -0.45, flag none)
- nifty_midcap_100: 63570.2500 (1d -0.15%, z20 0.40, flag amber)
- usd_inr: 95.7050 (1d 0.22%, z20 0.28, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6233 (1d -0.16%, z20 1.06, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 105.2 — "India’s BSE cleared as eligible exchange for FTSE Russell equity indices"
- INOXINDIA.NS (INOX INDIA LIMITED) score 103.3 — "India’s BSE cleared as eligible exchange for FTSE Russell equity indices"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 102.7 — "India’s BSE cleared as eligible exchange for FTSE Russell equity indices"
- INDIANB.NS (INDIAN BANK) score 90.3 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 2"
- BOND (PIMCO Active Bond Exchange-Tra) score 77.4 — "Markets poised for higher open amid caution over oil, bond stress"
- BAC (Bank of America Corporation) score 71.1 — "IndusInd Bank Share Price Live Updates: Trading Performance of IndusInd Bank"
- HDB (HDFC Bank Limited) score 65.1 — "IndusInd Bank Share Price Live Updates: Trading Performance of IndusInd Bank"
- IDBI.NS (IDBI BANK LIMITED) score 60.3 — "IndusInd Bank Share Price Live Updates: Trading Performance of IndusInd Bank"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 60.3 — "IndusInd Bank Share Price Live Updates: Trading Performance of IndusInd Bank"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 60.2 — "IndusInd Bank Share Price Live Updates: Trading Performance of IndusInd Bank"
- COIN (Coinbase Global, Inc.) score 55.1 — "Hormuz Oil Crisis Accelerates Global EV Sales"
- TECHM.NS (TECH MAHINDRA LIMITED) score 49.0 — "General Atlantic sells 8.75% stake in KFin Technologies for ₹1,400 crore"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 47.8 — "General Atlantic sells 8.75% stake in KFin Technologies for ₹1,400 crore"
- TECH (Bio-Techne Corp) score 47.6 — "General Atlantic sells 8.75% stake in KFin Technologies for ₹1,400 crore"
- OHI (Omega Healthcare Investors, In) score 47.2 — "88% retail investors lost money in F&O trading in FY26: Sebi"
- LTH (Life Time Group Holdings, Inc.) score 38.4 — "Gaja Alternative Asset Management IPO Day 3: Issue subscribed nearly 2.5 times; GMP at 11%"
- CHKP (Check Point Software Technolog) score 38.4 — "Stocks to watch: HAL, RailTel, Tata Motors PV among shares in focus today; check list here"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.2 — "These three copper stocks are riding India’s energy expansion. Should you invest?"
- JIOFIN.BO (Jio Financial Services Limited) score 21.0 — "FIIs pour Rs 6,535 crore into Indian financial stocks. What else are they buying this mont"
- PCJEWELLER.NS (PC JEWELLER LTD) score 20.9 — "Shankesh Jewellers IPO allotment expected today; GMP signals modest listing gains. Here's "
- 301077.SZ (CHINASTARS) score 20.8 — "China’s ‘smart’ diabetes probiotics; life sentence for Hui Ka-yan: SCMP’s 7 highlights"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 16.5 — "FIIs pour Rs 6,535 crore into Indian financial stocks. What else are they buying this mont"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 15.9 — "PNB Housing Finance among 5 F&O stocks with a sharp rise in futures open interest"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 14.6 — "Coking Coal Prices Surge 25%, Squeezing India's Steelmakers"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 14.2 — "Stocks to watch: HAL, RailTel, Tata Motors PV among shares in focus today; check list here"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 14.2 — "88% retail investors lost money in F&O trading in FY26: Sebi"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.4 — "Stocks to watch: HAL, RailTel, Tata Motors PV among shares in focus today; check list here"
- MS (Morgan Stanley) score 12.3 — "SEBI’s swift ban on JPMorgan unit seen as warning to traders"
- MRNA (Moderna, Inc.) score 10.3 — "Moderna’s personalized mRNA shot could reshape the fight against skin cancer — but it may "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.8 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ's trading session summary"
- META (Meta) score 9.0 — "Silver futures jump nearly 1% to ₹2.38 lakh/kg as US Treasury move boosts precious metals"
- JEF (Jefferies Financial Group Inc.) score 8.2 — "Turtlemint shares soar 4% as Jefferies initiates buy call, sets ₹190 target"
- VT (Vanguard Total World Stock Ind) score 8.1 — "Beijing Bets on Fossil Fuels Even as It Leads the World in Renewables"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.9 — "ICICI Bank Share Price Live Updates: ICICI Bank Price Update"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.6 — "The national debt just hit $40 trillion. Here’s how it can hurt Americans."
- BHARATFORG.BO (BHARAT FORGE LTD.) score 6.9 — "Coforge shares jump 3% after IT major launches private equity unit"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.2 — "Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month"
- VOLTAS.NS (VOLTAS LTD) score 2.3 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.4 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.3 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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