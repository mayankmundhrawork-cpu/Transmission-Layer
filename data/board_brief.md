# Transmission Layer — board brief · 2026-08-21 08:56Z

data as of **2026-08-21** · 98 series · 17 red / 23 amber · 8 events surfaced (21 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.229, 2d in regime; vol-pct 0.209, breadth-off 0.25, Markov P(high-vol) 0.025)
- [INVERTED] **safe_haven_gold** — corr20 -0.39, corr60 -0.39, contra nifty_50 corr20=0.03, last shift 2026-06-08. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.87, last shift 2026-01-29. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.24, corr60 0.37, last shift 2026-07-03. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.13, corr60 -0.13, last shift 2026-06-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.69, corr60 -0.83, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.05, corr60 -0.13, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.21, last shift 2026-06-25. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.25, corr60 0.2, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 0.0)
- **SETUP** dow_jones → asx_200: leads 1d (ccf 0.593, β 0.4867, p 0.0); driver zc -1.88 → expected -0.628%. Type hit-rate 0.821 (n=2333).
- **SETUP** dyn_ms → asx_200: leads 1d (ccf 0.489, β 0.1961, p 0.0); driver zc -1.84 → expected -0.616%. Type hit-rate 0.821 (n=2333).
- **SETUP** dow_jones → nikkei_225: leads 1d (ccf 0.466, β 0.7864, p 0.0); driver zc -1.88 → expected -1.014%. Type hit-rate 0.821 (n=2333).
- **SETUP** dow_jones → taiwan_weighted: leads 1d (ccf 0.422, β 0.7091, p 0.0); driver zc -1.88 → expected -0.914%. Type hit-rate 0.821 (n=2333).
- **SETUP** dyn_ms → nikkei_225: leads 1d (ccf 0.416, β 0.3441, p 0.0); driver zc -1.84 → expected -1.081%. Type hit-rate 0.821 (n=2333).
- **SETUP** tips_10y_real → usd_jpy: leads 1d (ccf 0.409, β 0.1225, p 0.0); driver zc -1.66 → expected -0.305%. Type hit-rate 0.821 (n=2333).
- **SETUP** dow_jones → aud_usd: leads 1d (ccf 0.395, β 0.2595, p 1e-05); driver zc -1.88 → expected -0.335%. Type hit-rate 0.821 (n=2333).
- **SETUP** dyn_ms → taiwan_weighted: leads 1d (ccf 0.391, β 0.3216, p 0.0); driver zc -1.84 → expected -1.01%. Type hit-rate 0.821 (n=2333).
- **SETUP** dow_jones → usd_mxn: leads 1d (ccf -0.362, β -0.2358, p 0.0); driver zc -1.88 → expected 0.304%. Type hit-rate 0.821 (n=2333).
- **SETUP** btc_usd → asx_200: leads 1d (ccf 0.309, β 0.0866, p 0.0); driver zc 2.07 → expected 0.666%. Type hit-rate 0.821 (n=2333).
- **SETUP** dyn_ms → aud_usd: leads 1d (ccf 0.274, β 0.0878, p 0.00306); driver zc -1.84 → expected -0.276%. Type hit-rate 0.821 (n=2333).
- Track record · residual_reversion: hit-rate **0.491** (n=1106) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.821** (n=2333) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 11.47] cross-asset · 4 series ↑
- dyn_mrna [EQUITIES]: last 133.34, z20 7.81, zc 5.86, resid-z 11.29 [unexplained], 1d 35.87%, |z20|=7.81; 1y-pct=100
- btc_usd [CRYPTO]: last 78647.45, z20 5.99, zc 2.07, resid-z 3.02 [unexplained], 1d 7.69%, |z20|=5.99
- eth_usd [CRYPTO]: last 2439.28, z20 4.17, zc 0.97, resid-z 1.49 [quiet], 1d 4.85%, |z20|=4.17
- dyn_coin [EQUITIES]: last 172.46, z20 2.62, zc 1.52, resid-z 2.13 [unexplained], 1d 7.65%, |z20|=2.62
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 1.45).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.384 via btc_usd, z 0.91, quiet)
- Watch next: vix (inverse) — not yet - watch; rho -0.579 vs eth_usd
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.507 vs eth_usd
- **India receivers**: nifty_metal (rho 0.384, z 0.91)
- Source: Crude oil price falls in futures trade on weak global cues — BusinessLine Mkts, 2026-08-21. https://www.thehindubusinessline.com/markets/commodities/crude-oil-price-falls-in-futures-trade-on-weak-global-cues/article71372686.ece
- Source: Nifty’s higher highs offer a bullish signal amid global turmoil — Mint Markets, 2026-08-21. https://www.livemint.com/market/stock-market-news/niftys-higher-highs-offer-a-bullish-signal-amid-global-turmoil-11787283025704.html
- Source: Bitcoin on Track for Biggest Weekly Gain in More Than Two Years — Mint Markets, 2026-08-21. https://www.livemint.com/market/bitcoin-on-track-for-biggest-weekly-gain-in-more-than-two-years-11787292175301.html
- Historical analogues: 2025-08-13 (d=1.45), 2025-05-09 (d=2.34), 2024-11-13 (d=2.6)

### [RED 8.63] cross-asset · 5 series ↑
- comex_gold [COMMODITIES]: last 4638.90, z20 2.34, zc 1.74, resid-z 0.72 [priced], 1d 2.71%, |z20|=2.34; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 69.83, z20 2.25, zc 1.01, resid-z -0.90 [quiet], 1d 2.66%, |z20|=2.25; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 66.43, z20 -1.70, zc n/a, resid-z n/a [quiet], 1d 0.05%, GSR<75 (extreme low); |z20|=1.70
- comex_copper [COMMODITIES]: last 6.58, z20 0.57, zc 0.86, resid-z 0.46 [quiet], 1d 1.91%, 1y-pct=95
- stoxx_50 [INDICES]: last 6448.23, z20 0.09, zc 0.52, resid-z 0.18 [quiet], 1d 0.41%, 1y-pct=95
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-31 (z-distance 0.46).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.535 via comex_silver, z 0.91, quiet); dyn_stylebaaza_ns (rho -0.381 via gold_silver_ratio, z 1.7, reacted)
- Watch next: cac_40 (co-move) — not yet - watch; rho 0.874 vs stoxx_50, historically leads by 2d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.609 vs stoxx_50, historically leads by 5d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.607 vs comex_copper, historically leads by 1d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.576 vs comex_copper, historically leads by 1d
- Watch next: vix (inverse) — not yet - watch; rho -0.576 vs comex_copper, historically leads by 3d
- **India receivers**: nifty_metal (rho 0.535, z 0.91); dyn_stylebaaza_ns (rho -0.381, z 1.7)
- Source: Gold climbs to near three-month peak after US Treasury move — BusinessLine Mkts, 2026-08-21. https://www.thehindubusinessline.com/markets/gold/gold-climbs-to-near-three-month-peak-after-us-treasury-move/article71372830.ece
- Source: Silver price rises ₹2,369 to ₹2.45 lakh per kg — BusinessLine Mkts, 2026-08-21. https://www.thehindubusinessline.com/markets/gold/silver-price-rises-2369-to-245-lakh-per-kg/article71372688.ece
- Source: MCX shares jump 8% in 3 days as gold, silver futures rise. What lies ahead for investors? — ET Markets, 2026-08-21. https://economictimes.indiatimes.com/markets/stocks/news/mcx-shares-jump-8-in-3-days-as-gold-silver-futures-rise-what-lies-ahead-for-investors/articleshow/133396946.cms
- Historical analogues: 2025-10-31 (d=0.46), 2025-07-28 (d=0.56), 2026-03-31 (d=0.69)

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

### [AMBER 6.06] wti ↑
- wti [COMMODITIES]: last 86.17, z20 1.06, zc -0.79, resid-z 0.35 [quiet], 1d -1.89%, 1-session move -1.89% ≥ 1.5%
- **Mechanism**: wti ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.35 via wti, z 0.6, quiet); dyn_voltas_ns (rho -0.35 via wti, z -1.88, reacted)
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.627 vs wti
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.506 vs wti
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.504 vs wti
- **India receivers**: nifty_midcap_100 (rho -0.35, z 0.6); dyn_voltas_ns (rho -0.35, z -1.88)
- Source: China’s Oil Imports Set to Rebound as Refiners Hunt for New Supply — OilPrice, 2026-08-21. https://oilprice.com/Latest-Energy-News/World-News/Chinas-Oil-Imports-Set-to-Rebound-as-Refiners-Hunt-for-New-Supply.html
- Source: India bonds hang tight before supply as oil stalls — ET Markets, 2026-08-21. https://economictimes.indiatimes.com/markets/bonds/india-bonds-hang-tight-before-supply-as-oil-stalls/articleshow/133397733.cms
- Source: Nifty flatlines near 24,232 at midday; crude surge caps gains, Power Grid shines — BusinessLine Mkts, 2026-08-21. https://www.thehindubusinessline.com/markets/nifty-flatlines-near-24232-at-midday-crude-surge-caps-gains-power-grid-shines/article71372689.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

### [RED 5.03] commodities · 2 series ↑
- corn [COMMODITIES]: last 503.25, z20 4.20, zc 3.99, resid-z 0.65 [moved], 1d 5.12%, |z20|=4.20; 1y-pct=100
- wheat [COMMODITIES]: last 703.25, z20 2.90, zc 1.73, resid-z 0.12 [moved], 1d 3.00%, |z20|=2.90; 1y-pct=99
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [RED 4.92] dxy ↓
- dxy [FX]: last 98.64, z20 -1.92, zc -0.74, resid-z -2.52 [unexplained], 1d -0.26%, 20d range extreme; |z20|=1.92
- **Mechanism**: dxy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [RED 4.66] dyn_lenskart_ns ↑
- dyn_lenskart_ns [EQUITIES]: last 661.05, z20 2.66, zc 0.57, resid-z 0.33 [quiet], 1d 0.95%, |z20|=2.66; 1y-pct=99
- **Mechanism**: dyn_lenskart_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/stocks/news/lenskart-solutions-among-4-stocks-to-hit-52-week-highs-amp-surge-up-to-25-in-a-month/slideshow/133348316.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

### [RED 4.35] fx · 4 series ↑
- aud_usd [FX]: last 0.72, z20 2.68, zc 0.85, resid-z 1.15 [quiet], 1d 0.52%, |z20|=2.68
- eur_usd [FX]: last 1.17, z20 2.51, zc 0.77, resid-z 0.73 [quiet], 1d 0.30%, |z20|=2.51
- gbp_usd [FX]: last 1.37, z20 2.34, zc 1.02, resid-z 0.94 [quiet], 1d 0.44%, |z20|=2.34; 1y-pct=96
- usd_mxn [FX]: last 16.90, z20 -1.89, zc -0.80, resid-z -0.69 [quiet], 1d -0.32%, |z20|=1.89; 1y-pct=0
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.589 via usd_mxn, z 1.49, reacted); nifty_midcap_100 (rho 0.426 via aud_usd, z 0.6, quiet); dyn_icicigi_bo (rho -0.407 via gbp_usd, z -1.15, reacted)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.552 vs eur_usd
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.523 vs aud_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.589, z 1.49); nifty_midcap_100 (rho 0.426, z 0.6); dyn_icicigi_bo (rho -0.407, z -1.15)
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

## Watchlist (below surfacing floor)
midcap_largecap_ratio ↑ (4.27), dyn_jef ↓ (4.21), dyn_bharatcoal_ns ↑ (4.03), dyn_stylebaaza_ns ↑ (3.7), dyn_cartrade_ns ↑ (3.68), dyn_icicigi_bo ↓ (3.15), dyn_tech ↑ (2.92), usd_cny ↓ (2.75), eur_inr ↑ (2.63), dyn_lth ↑ (2.44), dyn_tatatech_ns ↑ (2.27), nifty_fmcg ↓ (2.12)

## India macro
- nifty_50: 24237.4492 (1d 0.02%, z20 -0.43, flag none)
- nifty_midcap_100: 63694.2500 (1d 0.04%, z20 0.60, flag amber)
- usd_inr: 95.7230 (1d 0.24%, z20 0.32, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6279 (1d 0.02%, z20 1.27, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 107.1 — "Bharat Coking Coal shares jump over 7%. What's behind the sharp surge?"
- INOXINDIA.NS (INOX INDIA LIMITED) score 103.3 — "India bonds hang tight before supply as oil stalls"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 102.7 — "India bonds hang tight before supply as oil stalls"
- INDIANB.NS (INDIAN BANK) score 98.7 — "PSU banks offer highest alpha potential; IT faces uncertainty: Omniscience Capital"
- BOND (PIMCO Active Bond Exchange-Tra) score 82.3 — "US Treasury bond buybacks spark fresh fears over dollar weakness"
- BAC (Bank of America Corporation) score 79.2 — "PSU banks offer highest alpha potential; IT faces uncertainty: Omniscience Capital"
- HDB (HDFC Bank Limited) score 73.4 — "PSU banks offer highest alpha potential; IT faces uncertainty: Omniscience Capital"
- IDBI.NS (IDBI BANK LIMITED) score 68.8 — "PSU banks offer highest alpha potential; IT faces uncertainty: Omniscience Capital"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 68.8 — "PSU banks offer highest alpha potential; IT faces uncertainty: Omniscience Capital"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 68.8 — "PSU banks offer highest alpha potential; IT faces uncertainty: Omniscience Capital"
- COIN (Coinbase Global, Inc.) score 57.9 — "Crude oil price falls in futures trade on weak global cues"
- TECHM.NS (TECH MAHINDRA LIMITED) score 52.1 — "Netweb Tech shares rise 4% as Nomura, Goldman Sachs invest in Rs 1,200 crore QIP"
- OHI (Omega Healthcare Investors, In) score 51.3 — "Walmart stock selloff explained: Here’s what spooked investors"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 49.9 — "Netweb Tech shares rise 4% as Nomura, Goldman Sachs invest in Rs 1,200 crore QIP"
- TECH (Bio-Techne Corp) score 49.8 — "Netweb Tech shares rise 4% as Nomura, Goldman Sachs invest in Rs 1,200 crore QIP"
- CHKP (Check Point Software Technolog) score 40.8 — "Sunshine Pictures IPO GMP signals 20% listing pop. Here's how to check allotment status on"
- LTH (Life Time Group Holdings, Inc.) score 36.9 — "Gaja Alternative Asset Management IPO Day 3: Issue subscribed nearly 2.5 times; GMP at 11%"
- 301077.SZ (CHINASTARS) score 24.0 — "China’s Oil Imports Set to Rebound as Refiners Hunt for New Supply"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.3 — "These three copper stocks are riding India’s energy expansion. Should you invest?"
- PCJEWELLER.NS (PC JEWELLER LTD) score 21.1 — "Shankesh Jewellers IPO allotment to be finalised today. Latest GMP, step-by-step guide to "
- JIOFIN.BO (Jio Financial Services Limited) score 20.2 — "FIIs pour Rs 6,535 crore into Indian financial stocks. What else are they buying this mont"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.3 — "Muthoot, Manappuram Finance shares jump up to 7% in 2 days as gold crosses Rs 1.6 lakh/10 "
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 16.0 — "Bharat Coking Coal shares jump over 7%. What's behind the sharp surge?"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 15.8 — "FIIs pour Rs 6,535 crore into Indian financial stocks. What else are they buying this mont"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 14.7 — "Tata Steel, Adani Ports among top 10 stocks downgraded by Motilal Oswal after Q1 results"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.9 — "Tata Steel, Adani Ports among top 10 stocks downgraded by Motilal Oswal after Q1 results"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 13.6 — "88% retail investors lost money in F&O trading in FY26: Sebi"
- JEF (Jefferies Financial Group Inc.) score 11.8 — "Why Jefferies’ Chris Wood sees gold as the second-best hedge amid Iran war and fiscal risk"
- MS (Morgan Stanley) score 11.8 — "SEBI’s swift ban on JPMorgan unit seen as warning to traders"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 11.4 — "Tata Steel, Adani Ports among top 10 stocks downgraded by Motilal Oswal after Q1 results"
- MRNA (Moderna, Inc.) score 9.9 — "Moderna’s personalized mRNA shot could reshape the fight against skin cancer — but it may "
- ICICIGI.BO (ICICI Lombard General Insuranc) score 9.6 — "ICICI Bank, Federal Bank among top bank picks by Axis Direct after Q1 earnings season"
- META (Meta) score 8.6 — "Silver futures jump nearly 1% to ₹2.38 lakh/kg as US Treasury move boosts precious metals"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.3 — "Did Goodluck India shares really crash 66% in just one day? Here's how the bonus math work"
- VT (Vanguard Total World Stock Ind) score 7.8 — "Beijing Bets on Fossil Fuels Even as It Leads the World in Renewables"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 7.7 — "Bharat Coking Coal shares jump over 7%. What's behind the sharp surge?"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.1 — "Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month"
- VOLTAS.NS (VOLTAS LTD) score 2.2 — "Voltas reported strong growth in June quarter, but failed to impress"
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