# Transmission Layer — board brief · 2026-08-24 09:02Z

data as of **2026-08-24** · 98 series · 16 red / 32 amber · 8 events surfaced (30 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.304, 2d in regime; vol-pct 0.274, breadth-off 0.333, Markov P(high-vol) 0.016)
- [WEAK] **safe_haven_gold** — corr20 -0.25, corr60 -0.39, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.76, corr60 0.86, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.17, corr60 0.41, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.08, corr60 -0.11, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.7, corr60 -0.83, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.1, corr60 -0.13, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.3, corr60 -0.21, last shift 2026-06-30. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.29, corr60 0.2, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.0018708734390282533)
- **SETUP** dyn_ms → nikkei_225: leads 1d (ccf 0.413, β 0.3414, p 0.0); driver zc 1.75 → expected 1.112%. Type hit-rate 0.816 (n=2478).
- **SETUP** dyn_ms → taiwan_weighted: leads 1d (ccf 0.386, β 0.317, p 0.0); driver zc 1.75 → expected 1.032%. Type hit-rate 0.816 (n=2478).
- **SETUP** bovespa → usd_mxn: leads 1d (ccf -0.37, β -0.2162, p 0.0); driver zc 1.75 → expected -0.397%. Type hit-rate 0.816 (n=2478).
- Track record · residual_reversion: hit-rate **0.493** (n=1101) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.816** (n=2478) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.06] cross-asset · 4 series ↑
- dyn_mrna [EQUITIES]: last 145.04, z20 4.40, zc 0.66, resid-z 4.54 [unexplained], 1d 8.79%, |z20|=4.40; 1y-pct=100
- dyn_coin [EQUITIES]: last 186.57, z20 4.00, zc 1.58, resid-z 2.63 [unexplained], 1d 8.25%, |z20|=4.00
- btc_usd [CRYPTO]: last 77088.94, z20 3.10, zc -0.35, resid-z 3.11 [unexplained], 1d -1.59%, |z20|=3.10
- eth_usd [CRYPTO]: last 2456.27, z20 2.81, zc -0.47, resid-z 2.06 [unexplained], 1d -2.35%, |z20|=2.81
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.61).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Global Market: European shares edge lower as investors await Iran sanctions details — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-european-shares-edge-lower-as-investors-await-iran-sanctions-details/articleshow/133457567.cms
- Source: Global Market: China’s property crisis deepens as Evergrande founder gets life sentence — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-chinas-property-crisis-deepens-as-evergrande-founder-gets-life-sentence/articleshow/133456559.cms
- Source: MSM Unify appoints Rishi Kapoor as CFO, plans for IPO across India and global markets — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/companies/msm-unify-appoints-rishi-kapoor-as-cfo-plans-for-ipo-across-india-and-global-markets/article71383434.ece
- Historical analogues: 2025-08-13 (d=0.61), 2025-05-09 (d=1.39), 2024-11-21 (d=1.44)

### [RED 7.57] commodities · 2 series ↑
- corn [COMMODITIES]: last 518.50, z20 4.74, zc 5.64, resid-z 0.49 [moved], 1d 7.18%, |z20|=4.74; 1y-pct=100
- wheat [COMMODITIES]: last 708.00, z20 3.13, zc 2.35, resid-z -0.26 [moved], 1d 3.89%, |z20|=3.13; 1y-pct=100
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Corn rockets to 3-year high as traders eye lower U.S. production — Mint Markets, 2026-08-24. https://www.livemint.com/market/corn-rockets-to-3-year-high-as-traders-eye-lower-u-s-production-11787533218087.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [RED 7.27] cross-asset · 6 series ↑
- comex_gold [COMMODITIES]: last 4698.60, z20 2.34, zc 0.91, resid-z 0.88 [quiet], 1d 1.61%, |z20|=2.34; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 68.89, z20 1.69, zc -0.32, resid-z -2.12 [unexplained], 1d -0.82%, |z20|=1.69; co-occur[gold_silver] same-direction (channel VALID)
- comex_copper [COMMODITIES]: last 6.61, z20 0.69, zc 0.18, resid-z 1.01 [quiet], 1d 0.40%, 1y-pct=97; co-occur[metal_copper] suppressed: channel WEAK
- dax [INDICES]: last 26152.97, z20 0.34, zc 0.08, resid-z 0.47 [quiet], 1d 0.06%, 1y-pct=96
- stoxx_50 [INDICES]: last 6462.34, z20 0.15, zc 0.00, resid-z 0.44 [quiet], 1d 0.00%, 1y-pct=95
- gold_silver_ratio [DERIVED]: last 68.20, z20 -0.12, zc n/a, resid-z n/a [quiet], 1d 2.45%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 6 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-30 (z-distance 0.59).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.487 via comex_silver, z 1.55, reacted); nifty_midcap_100 (rho 0.471 via dax, z 0.66, quiet); dyn_stylebaaza_ns (rho -0.424 via gold_silver_ratio, z 1.14, reacted)
- Watch next: ftse_100 (co-move) — not yet - watch; rho 0.601 vs dax, historically leads by 4d
- Watch next: vix (inverse) — not yet - watch; rho -0.583 vs stoxx_50, historically leads by 5d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.552 vs stoxx_50, historically leads by 5d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.547 vs comex_copper, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.533 vs dax, historically leads by 5d
- **India receivers**: nifty_metal (rho 0.487, z 1.55); nifty_midcap_100 (rho 0.471, z 0.66); dyn_stylebaaza_ns (rho -0.424, z 1.14)
- Source: Domestic silver futures rise to ₹2.46 lakh per kg — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/markets/gold/domestic-silver-futures-rise-to-246-lakh-per-kg/article71383712.ece
- Source: Gold futures rise to ₹1.63 lakh/10 gm on spot demand — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/markets/commodities/gold-futures-rise-to-163-lakh10-gm-on-spot-demand/article71383665.ece
- Source: Muthoot Finance, Manappuram Finance shares rally up to 11% in 4 days as gold crosses Rs 1.63 lakh — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/stocks/news/muthoot-finance-manappuram-finance-shares-rally-up-to-11-in-4-days-as-gold-crosses-rs-1-63-lakh/articleshow/133455929.cms
- Historical analogues: 2025-07-30 (d=0.59), 2026-04-02 (d=0.67), 2024-11-07 (d=0.8)

### [AMBER 7.05] commodities · 2 series ↑
- brent [COMMODITIES]: last 92.80, z20 1.22, zc -0.82, resid-z 0.33 [quiet], 1d -1.68%, 1-session move -1.68% ≥ 1.5%
- wti [COMMODITIES]: last 84.97, z20 0.80, zc -1.06, resid-z -0.12 [quiet], 1d -2.40%, 1-session move -2.40% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.598 vs brent, historically leads by 5d
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.581 vs brent, historically leads by 5d
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.55 vs brent, historically leads by 5d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.693 vs brent
- Watch next: cac_40 (inverse) — not yet - watch; rho -0.502 vs brent
- Source: Sensex today | Stock Market Live: Sensex falls 300 pts, Nifty near 24,150 as crude prices, West Asia tensions weigh — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-24-august-2026/article71380598.ece
- Source: Sensex today | Stock Market Live: Sensex, Nifty fall as high crude prices, weak global cues weigh — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-24-august-2026/article71380598.ece
- Source: Rain Industries share price: Petrochemical stock jumps 4% amid soaring crude oil prices on US-Iran war — Mint Markets, 2026-08-24. https://www.livemint.com/market/stock-market-news/rain-industries-share-price-petrochemical-stock-jumps-4-amid-soaring-crude-oil-prices-on-us-iran-war-11787549018567.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 5.68] dyn_muthootfin_ns ↑
- dyn_muthootfin_ns [EQUITIES]: last 3204.00, z20 3.68, zc 2.73, resid-z 3.61 [unexplained], 1d 6.02%, |z20|=3.68
- **Mechanism**: dyn_muthootfin_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.678 via dyn_muthootfin_ns, z 1.55, reacted); nifty_midcap_100 (rho 0.61 via dyn_muthootfin_ns, z 0.66, quiet); nifty_50 (rho 0.523 via dyn_muthootfin_ns, z -0.92, quiet); dyn_karurvysya_ns (rho 0.437 via dyn_muthootfin_ns, z 0.39, quiet); dyn_bharatcoal_ns (rho 0.435 via dyn_muthootfin_ns, z 1.96, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.61 vs dyn_muthootfin_ns, historically leads by 3d
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.523 vs dyn_muthootfin_ns, historically leads by 3d
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.596 vs dyn_muthootfin_ns
- **India receivers**: nifty_metal (rho 0.678, z 1.55); nifty_midcap_100 (rho 0.61, z 0.66); nifty_50 (rho 0.523, z -0.92); dyn_karurvysya_ns (rho 0.437, z 0.39)
- Source: Muthoot Finance, Manappuram Finance shares rally up to 11% in 4 days as gold crosses Rs 1.63 lakh — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/stocks/news/muthoot-finance-manappuram-finance-shares-rally-up-to-11-in-4-days-as-gold-crosses-rs-1-63-lakh/articleshow/133455929.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-22 (d=0.01), 2025-12-04 (d=0.01)

### [RED 4.6] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.64, z20 1.60, zc n/a, resid-z n/a [quiet], 1d 0.37%, 52-wk extreme (pct=100); |z20|=1.60; 1y-pct=100
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.489 via midcap_largecap_ratio, z 0.66, quiet); dyn_fincables_ns (rho 0.372 via midcap_largecap_ratio, z 1.17, reacted); dyn_bharatcoal_ns (rho 0.358 via midcap_largecap_ratio, z 1.96, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.489, z 0.66); dyn_fincables_ns (rho 0.372, z 1.17); dyn_bharatcoal_ns (rho 0.358, z 1.96)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 4.27] dyn_pcjeweller_ns ↑
- dyn_pcjeweller_ns [EQUITIES]: last 10.82, z20 4.27, zc 1.70, resid-z 2.34 [unexplained], 1d 5.87%, |z20|=4.27
- **Mechanism**: dyn_pcjeweller_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.375 via dyn_pcjeweller_ns, z 3.68, reacted)
- **India receivers**: dyn_muthootfin_ns (rho 0.375, z 3.68)
- Historical analogues: 2026-07-10 (d=0.0), 2024-10-01 (d=0.19), 2026-01-07 (d=0.32)

### [RED 4.24] dyn_idbi_ns ↑
- dyn_idbi_ns [EQUITIES]: last 88.70, z20 4.24, zc 3.66, resid-z 2.77 [unexplained], 1d 7.86%, |z20|=4.24
- **Mechanism**: dyn_idbi_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.409 via dyn_idbi_ns, z 3.68, reacted); dyn_voltas_ns (rho 0.386 via dyn_idbi_ns, z -1.39, reacted); dyn_bharatcoal_ns (rho 0.367 via dyn_idbi_ns, z 1.96, reacted); nifty_midcap_100 (rho 0.365 via dyn_idbi_ns, z 0.66, quiet); nifty_metal (rho 0.363 via dyn_idbi_ns, z 1.55, reacted)
- **India receivers**: dyn_muthootfin_ns (rho 0.409, z 3.68); dyn_voltas_ns (rho 0.386, z -1.39); dyn_bharatcoal_ns (rho 0.367, z 1.96); nifty_midcap_100 (rho 0.365, z 0.66)
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-19 (d=0.01), 2025-09-30 (d=0.06)

## Watchlist (below surfacing floor)
dyn_lenskart_ns ↑ (4.21), cross-asset · 3 series ↑ (4.1), cross-asset · 2 series ↑ (3.46), fx · 2 series ↑ (3.38), dyn_cartrade_ns ↑ (3.23), dyn_tech ↑ (3.02), dyn_icicigi_bo ↓ (2.97), tips_10y_real ↓ (2.88), dyn_lth ↑ (2.74), brent_wti_spread ↑ (2.6), fx · 2 series ↑ (2.56), usd_cny ↓ (2.21)

## India macro
- nifty_50: 24171.5508 (1d -0.33%, z20 -0.92, flag none)
- nifty_midcap_100: 63757.3008 (1d 0.03%, z20 0.66, flag amber)
- usd_inr: 95.7300 (1d -0.04%, z20 0.63, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6377 (1d 0.37%, z20 1.60, flag red)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 77.2 — "MSM Unify appoints Rishi Kapoor as CFO, plans for IPO across India and global markets"
- INOXINDIA.NS (INOX INDIA LIMITED) score 75.4 — "MSM Unify appoints Rishi Kapoor as CFO, plans for IPO across India and global markets"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 75.1 — "MSM Unify appoints Rishi Kapoor as CFO, plans for IPO across India and global markets"
- INDIANB.NS (INDIAN BANK) score 72.5 — "IndusInd Bank Share Price Live Updates: IndusInd Bank  Daily Performance"
- BAC (Bank of America Corporation) score 60.0 — "IndusInd Bank Share Price Live Updates: IndusInd Bank  Daily Performance"
- BOND (PIMCO Active Bond Exchange-Tra) score 58.0 — "Global Market: AI debt boom tests investor appetite as tech bond issuance surges"
- HDB (HDFC Bank Limited) score 55.5 — "IndusInd Bank Share Price Live Updates: IndusInd Bank  Daily Performance"
- IDBI.NS (IDBI BANK LIMITED) score 53.2 — "IndusInd Bank Share Price Live Updates: IndusInd Bank  Daily Performance"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 53.2 — "IndusInd Bank Share Price Live Updates: IndusInd Bank  Daily Performance"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 53.2 — "IndusInd Bank Share Price Live Updates: IndusInd Bank  Daily Performance"
- COIN (Coinbase Global, Inc.) score 47.7 — "Global Market: Shein valuation falls 70% from peak as Hong Kong IPO targets $1.77 billion"
- TECHM.NS (TECH MAHINDRA LIMITED) score 42.4 — "Global Market: AI debt boom tests investor appetite as tech bond issuance surges"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 40.8 — "Global Market: AI debt boom tests investor appetite as tech bond issuance surges"
- TECH (Bio-Techne Corp) score 40.7 — "Global Market: AI debt boom tests investor appetite as tech bond issuance surges"
- OHI (Omega Healthcare Investors, In) score 34.2 — "Did you get Lalithaa Jewellery Mart IPO? Shares up 36% from IPO price -What's next for inv"
- CHKP (Check Point Software Technolog) score 27.7 — "IPO: Share price band  ₹300, GMP  ₹313 - Check last date to apply, allotment and listing d"
- LTH (Life Time Group Holdings, Inc.) score 26.9 — "Augmont Enterprises IPO day 2: Issue subscribed over 9 times; GMP signals nearly 50% listi"
- PCJEWELLER.NS (PC JEWELLER LTD) score 18.9 — "Lalithaa Jewellery shares list at 32% premium, Horizon Ind makes muted debut: Should you b"
- 301077.SZ (CHINASTARS) score 18.2 — "Global Market: China’s property crisis deepens as Evergrande founder gets life sentence"
- JIOFIN.BO (Jio Financial Services Limited) score 18.1 — "IPO GMP Today Live Updates: Symbiotec Pharmalab, Skyways Air Services IPO Day 1 bidding be"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 12.2 — "Markets brace for more hawkish ECB as energy risks threaten to keep inflation elevated"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 11.8 — "How retail F&O participation changed after Sebi tightened rules, in charts"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 10.9 — "Stocks to buy in 2026 for long term: Jubilant FoodWorks, Max Financial among 5 stocks that"
- MS (Morgan Stanley) score 10.0 — "JPMorgan’s Copthall Mauritius to argue SEBI violation was technical, not manipulative"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.3 — "Tata Steel Share Price Live Updates: Tata Steel's Market Update: Today's Gains vs. Long-Te"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 9.1 — "Muthoot Finance, Manappuram Finance shares rally up to 11% in 4 days as gold crosses Rs 1."
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 9.0 — "Coal India Share Price Live Updates: Coal India Ltd's Price Breakout Signals Strength"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 8.9 — "Tata Steel Share Price Live Updates: Tata Steel's Market Update: Today's Gains vs. Long-Te"
- VT (Vanguard Total World Stock Ind) score 7.4 — "Super El Niño Threatens Food, Water and Trade Worldwide"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.3 — "ICICI Bank Share Price Live Updates: ICICI Bank News"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.7 — "SEBI rejects settlement bids by Adani-linked funds"
- META (Meta) score 6.3 — "Nifty slips below 24,200 as banks drag; metals, IT buck trend"
- JEF (Jefferies Financial Group Inc.) score 5.9 — "Why Jefferies’ Chris Wood sees gold as the second-best hedge amid Iran war and fiscal risk"
- MRNA (Moderna, Inc.) score 5.0 — "Moderna’s personalized mRNA shot could reshape the fight against skin cancer — but it may "
- JUSTDIAL.BO (JUST DIAL LTD.) score 4.1 — "Did Goodluck India shares really crash 66% in just one day? Here's how the bonus math work"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 3.8 — "Bharat Coking Coal shares jump over 7%. What's behind the sharp surge?"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.5 — "Lenskart Large Trade: 2.6% equity traded in a $300 million block deal; Softbank Vision lik"
- VOLTAS.NS (VOLTAS LTD) score 1.1 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.2 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.2 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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