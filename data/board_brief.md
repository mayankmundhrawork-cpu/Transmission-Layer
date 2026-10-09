# Transmission Layer — board brief · 2026-10-09 00:20Z

data as of **2026-10-09** · 97 series · 10 red / 37 amber · 8 events surfaced (28 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.0, 1d in regime; vol-pct None, breadth-off 0.0, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.33, corr60 -0.41, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.8, corr60 0.84, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.13, corr60 0.18, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.1, corr60 0.12, last shift 2026-08-19. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.77, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [INVERTED] **dxy_inr_channel** — corr20 -0.29, corr60 -0.11, last shift 2026-08-12. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.23, corr60 -0.27, last shift 2026-08-12. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.52, corr60 0.18, last shift 2026-07-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** dyn_nvda → aud_usd: leads 1d (ccf 0.34, β 0.0758, p 0.0); driver zc -1.53 → expected -0.22%. Type hit-rate 0.829 (n=2170).
- Track record · residual_reversion: hit-rate **0.496** (n=1140) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.829** (n=2170) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.47] usd_inr ↑
- usd_inr [FX]: last 96.76, z20 2.47, zc 0.77, resid-z 0.59 [quiet], 1d 0.40%, 20d range extreme; |z20|=2.47; 1y-pct=99
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.41 via usd_inr, z -0.44, quiet); dyn_karurvysya_ns (rho -0.375 via usd_inr, z 0.57, quiet)
- **India receivers**: dyn_idbi_ns (rho -0.41, z -0.44); dyn_karurvysya_ns (rho -0.375, z 0.57)
- Source: RBI intervention halts rupee's slide to record low, risks linger — ET Markets, 2026-10-08. https://economictimes.indiatimes.com/markets/forex/rbi-intervention-halts-rupees-slide-to-record-low-risks-linger/articleshow/134788012.cms
- Source: Rupee falls 13 paise to close at 96.88 against US dollar — BusinessLine Mkts, 2026-10-08. https://www.thehindubusinessline.com/markets/forex/rupee-falls-13-paise-to-close-at-9688-against-us-dollar/article71559337.ece
- Source: INR vs USD: Rupee near 97/dollar; how TCS, Sun Pharma, Tata Steel, SRF may gain from weaker currency? Experts explain — Mint Markets, 2026-10-08. https://www.livemint.com/market/stock-market-news/inr-vs-usd-rupee-near-97-dollar-how-tcs-sun-pharma-tata-steel-srf-may-gain-from-weaker-currency-experts-explain-11791449213491.html
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2025-09-16 (d=0.01)

### [AMBER 6.31] cross-asset · 5 series ↓
- nifty_50 [INDICES]: last 22231.80, z20 -2.38, zc -2.29, resid-z -2.38 [unexplained], 1d -1.64%, |z20|=2.38; 1y-pct=0
- nifty_fmcg [INDICES]: last 43898.40, z20 -2.35, zc -2.25, resid-z -0.77 [priced], 1d -2.02%, |z20|=2.35; 1y-pct=0
- nifty_midcap_100 [INDICES]: last 57880.45, z20 -2.34, zc -2.65, resid-z -2.22 [unexplained], 1d -2.52%, |z20|=2.34
- india_vix [INDICES]: last 15.24, z20 2.19, zc 1.64, resid-z n/a [moved], 1d 9.74%, |z20|=2.19
- dyn_policybzr_ns [EQUITIES]: last 996.00, z20 -1.18, zc -1.16, resid-z 0.59 [quiet], 1d -4.23%, 1y-pct=1
- **Mechanism**: cross-asset · 5 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.6).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.631 via nifty_midcap_100, z -2.07, reacted); nifty_metal (rho 0.621 via nifty_midcap_100, z -3.61, reacted); dyn_jiofin_bo (rho 0.587 via nifty_50, z -1.94, reacted); dyn_indusindbk_bo (rho 0.538 via nifty_midcap_100, z -1.77, reacted); dyn_bajfinance_ns (rho -0.538 via india_vix, z -1.3, reacted)
- **India receivers**: midcap_largecap_ratio (rho 0.631, z -2.07); nifty_metal (rho 0.621, z -3.61); dyn_jiofin_bo (rho 0.587, z -1.94); dyn_indusindbk_bo (rho 0.538, z -1.77)
- Source: Nifty hits 52-week low as crude, FII selling weigh — BusinessLine Mkts, 2026-10-08. https://www.thehindubusinessline.com/markets/nifty-hits-52-week-low-as-crude-fii-selling-weigh/article71559983.ece
- Source: Nifty hits intra-day high on open for the sixth time in 2026 — BusinessLine Mkts, 2026-10-08. https://www.thehindubusinessline.com/markets/nifty-hits-intra-day-high-on-open-for-the-sixth-time-in-2026/article71560509.ece
- Source: Nifty sinks to an 18-month low as rate fears bite — Mint Markets, 2026-10-08. https://www.livemint.com/market/nifty-50-performance-in-2026-fii-fpi-selling-inflation-rbi-nse-crude-oil-11791461972358.html
- Historical analogues: 2025-07-21 (d=0.6), 2025-07-14 (d=0.65), 2025-12-30 (d=1.12)

### [RED 5.85] dyn_adanient_bo ↓
- dyn_adanient_bo [EQUITIES]: last 2595.00, z20 -3.85, zc -2.05, resid-z -2.04 [unexplained], 1d -5.43%, |z20|=3.85
- **Mechanism**: dyn_adanient_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.545 via dyn_adanient_bo, z -3.61, reacted); nifty_50 (rho 0.363 via dyn_adanient_bo, z -2.38, reacted); nifty_midcap_100 (rho 0.357 via dyn_adanient_bo, z -2.34, reacted)
- **India receivers**: nifty_metal (rho 0.545, z -3.61); nifty_50 (rho 0.363, z -2.38); nifty_midcap_100 (rho 0.357, z -2.34)
- Source: Adani Group's Group CFO Jugeshinder Robbie Singh on recent market volatility: 'Mood is ephemeral; stone is eternal' — Mint Markets, 2026-10-08. https://www.livemint.com/market/stock-market-news/adani-groups-group-cfo-jugeshinder-robbie-singh-on-recent-market-volatility-mood-is-ephemeral-stone-is-eternal-11791471088722.html
- Source: Market wrap: Infosys, Tech Mahindra, Adani Ent, ITC top gainers and losers on Nifty and Sensex on Thursday — ET Markets, 2026-10-08. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-infosys-tech-mahindra-adani-ent-itc-top-gainers-and-losers-on-nifty-and-sensex-on-thursday/articleshow/134788835.cms
- Source: Adani Group stocks tumble as market rout deepens; Adani Green, Adani Ent, others tank up to 10% — ET Markets, 2026-10-08. https://economictimes.indiatimes.com/markets/stocks/news/adani-group-stocks-tumble-as-market-rout-deepens-adani-green-adani-ent-others-tank-up-to-10/articleshow/134786010.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [AMBER 5.56] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.67, z20 1.63, zc 0.68, resid-z 0.09 [quiet], 1d 0.53%, |z20|=1.63; 1y-pct=100
- ust_10y [RATES]: last 5.28, z20 1.23, zc 0.18, resid-z -0.68 [quiet], 1d 0.19%, 1y-pct=98
- tips_10y_real [RATES]: last 2.92, z20 1.16, zc 0.18, resid-z -0.79 [quiet], 1d 0.34%, 1y-pct=98
- dyn_bond [EQUITIES]: last 86.90, z20 -0.98, zc 1.06, resid-z 0.48 [quiet], 1d 0.38%, 1y-pct=2
- ust_2y [RATES]: last 4.77, z20 0.15, zc -0.31, resid-z -1.30 [quiet], 1d -0.42%, 1y-pct=96
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.719 vs ust_30y, historically leads by 3d
- Watch next: wti (co-move) — not yet - watch; rho 0.517 vs ust_30y, historically leads by 3d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.556 vs ust_30y
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.54 vs ust_30y
- Source: Bond yields fell, as the Treasury market passed a crucial test of investor confidence — MarketWatch Top, 2026-10-08. https://www.marketwatch.com/story/the-treasury-market-is-facing-a-crucial-vote-of-investor-confidence-31fa8d41?mod=mw_rss_topstories
- Source: India's 10-year yield hits Dec 2023 peak as US debt rout, oil spike hurt — ET Markets, 2026-10-08. https://economictimes.indiatimes.com/markets/bonds/india-10-year-yield-hits-dec-2023-peak-as-us-debt-rout-oil-spike-hurt/articleshow/134789626.cms
- Source: U.K. 10-YEAR GILT YIELDS HIT 5.527%, HIGHEST SINCE 2007: LSEG U.K. 30-YEAR GILT YIELDS HIT 6.047%, HIGHEST SINCE 1998: LSEG — DeItaone, 2026-10-08. https://t.me/walter_bloomberg/36803
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.44] dyn_muthootfin_ns ↓
- dyn_muthootfin_ns [EQUITIES]: last 2559.60, z20 -3.44, zc -2.10, resid-z -1.06 [moved], 1d -3.57%, |z20|=3.44; 1y-pct=0
- **Mechanism**: dyn_muthootfin_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.474 via dyn_muthootfin_ns, z -2.34, reacted); nifty_50 (rho 0.445 via dyn_muthootfin_ns, z -2.38, reacted); nifty_metal (rho 0.434 via dyn_muthootfin_ns, z -3.61, reacted); dyn_bajfinance_ns (rho 0.382 via dyn_muthootfin_ns, z -1.3, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.474, z -2.34); nifty_50 (rho 0.445, z -2.38); nifty_metal (rho 0.434, z -3.61); dyn_bajfinance_ns (rho 0.382, z -1.3)
- Source: Muthoot Microfin AUM crosses ₹15,300 crore, cost of funds enters single digits — BusinessLine Mkts, 2026-10-08. https://www.thehindubusinessline.com/markets/stock-markets/muthoot-microfin-aum-crosses-15300-crore-cost-of-funds-enters-single-digits/article71559184.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-22 (d=0.01), 2025-12-04 (d=0.01)

### [RED 5.07] midcap_largecap_ratio ↓
- midcap_largecap_ratio [DERIVED]: last 2.60, z20 -2.07, zc n/a, resid-z n/a [quiet], 1d -0.89%, break below 100-DMA; |z20|=2.07
- **Mechanism**: midcap_largecap_ratio ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.631 via midcap_largecap_ratio, z -2.34, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.631, z -2.34)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 4.84] indices · 4 series ↓
- stoxx_50 [INDICES]: last 6133.89, z20 -3.17, zc -0.72, resid-z -0.37 [quiet], 1d -0.75%, |z20|=3.17
- dax [INDICES]: last 24823.64, z20 -3.13, zc -1.08, resid-z -1.01 [quiet], 1d -1.12%, |z20|=3.13
- cac_40 [INDICES]: last 7731.87, z20 -2.44, zc -0.51, resid-z 0.01 [quiet], 1d -0.48%, |z20|=2.44; 1y-pct=1
- ftse_100 [INDICES]: last 10441.37, z20 -1.88, zc -0.22, resid-z -0.10 [quiet], 1d -0.16%, |z20|=1.88
- **Mechanism**: indices · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tataelxsi_ns (rho 0.459 via dax, z -1.98, reacted); dyn_indusindbk_bo (rho 0.395 via ftse_100, z -1.77, reacted); dyn_voltas_ns (rho 0.391 via ftse_100, z -2.08, reacted)
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.708 vs stoxx_50, historically leads by 5d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.559 vs stoxx_50, historically leads by 5d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.527 vs stoxx_50, historically leads by 5d
- Watch next: wti (inverse) — not yet - watch; rho -0.508 vs stoxx_50, historically leads by 4d
- Watch next: asx_200 (co-move) — not yet - watch; rho 0.433 vs ftse_100, historically leads by 1d
- **India receivers**: dyn_tataelxsi_ns (rho 0.459, z -1.98); dyn_indusindbk_bo (rho 0.395, z -1.77); dyn_voltas_ns (rho 0.391, z -2.08)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-16 (d=0.34), 2024-11-21 (d=0.62)

### [RED 4.55] gold_silver_ratio ↑
- gold_silver_ratio [DERIVED]: last 69.73, z20 1.55, zc n/a, resid-z n/a [quiet], 1d 0.03%, GSR<75 (extreme low); |z20|=1.55
- **Mechanism**: gold_silver_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (inverse) — not yet - watch; rho -0.5 vs gold_silver_ratio
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

## Watchlist (below surfacing floor)
dyn_ohi ↓ (4.41), cross-asset · 3 series ↑ (4.39), shanghai_comp ↓ (4.31), dyn_coalindia_ns ↓ (4.23), dyn_4417_t ↑ (4.22), dyn_techm_ns ↓ (4.13), dyn_jiofin_bo ↓ (3.94), nifty_metal ↓ (3.61), eur_usd ↓ (3.48), dyn_hdb ↓ (3.47), dyn_justdial_bo ↓ (2.97), hang_seng ↓ (2.59)

## India macro
- nifty_50: 22231.8008 (1d -1.64%, z20 -2.38, flag amber)
- nifty_midcap_100: 57880.4492 (1d -2.52%, z20 -2.34, flag amber)
- usd_inr: 96.7568 (1d 0.40%, z20 2.47, flag red)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6035 (1d -0.89%, z20 -2.07, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · India CPI T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 85.5 — "India at an inflection point in private credit space: What is creating the opportunity?"
- INOXINDIA.NS (INOX INDIA LIMITED) score 85.4 — "India at an inflection point in private credit space: What is creating the opportunity?"
- INDIANB.NS (INDIAN BANK) score 84.7 — "Rates, inflation and AI emerge as key risks for global growth: Deutsche Bank Survey"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 83.7 — "India at an inflection point in private credit space: What is creating the opportunity?"
- BAC (Bank of America Corporation) score 72.0 — "Federal Reserve Board announces enforcement action against American Express Company to add"
- HDB (HDFC Bank Limited) score 67.8 — "Rates, inflation and AI emerge as key risks for global growth: Deutsche Bank Survey"
- IDBI.NS (IDBI BANK LIMITED) score 64.8 — "Rates, inflation and AI emerge as key risks for global growth: Deutsche Bank Survey"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 64.8 — "Rates, inflation and AI emerge as key risks for global growth: Deutsche Bank Survey"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 64.8 — "Rates, inflation and AI emerge as key risks for global growth: Deutsche Bank Survey"
- COIN (Coinbase Global, Inc.) score 57.5 — "Rates, inflation and AI emerge as key risks for global growth: Deutsche Bank Survey"
- OHI (Omega Healthcare Investors, In) score 46.0 — "OPENAI RECENTLY TOLD INVESTORS ITS REVENUES WERE APPROACHING $50BN ON AN ANNUALISED BASIS "
- TECHM.NS (TECH MAHINDRA LIMITED) score 45.6 — "Tech stocks drag Nasdaq lower on report of OpenAI revenue fall, high yields"
- BOND (PIMCO Active Bond Exchange-Tra) score 44.5 — "Bond yields fell, as the Treasury market passed a crucial test of investor confidence"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.1 — "Tech stocks drag Nasdaq lower on report of OpenAI revenue fall, high yields"
- TECH (Bio-Techne Corp) score 39.1 — "Tech stocks drag Nasdaq lower on report of OpenAI revenue fall, high yields"
- TGT (Target Corporation) score 39.0 — "FED'S MUSALEM SIGNALS MORE RATE HIKES MAY BE NEEDED Fed's Alberto Musalem says inflation r"
- CHKP (Check Point Software Technolog) score 31.7 — "TCS dividend payout decoded: Check 3-year dividends, yield and stock returns of IT bellwet"
- LTH (Life Time Group Holdings, Inc.) score 29.0 — "TRUMP: WE WILL NOT BE ATTACKING IRAN AT ANY TIME PRIOR TO MIDTERM ELECTIONS TO BE HELD IN "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 26.1 — "IRAN REFUSES TO ABANDON URANIUM ENRICHMENT Iran's atomic energy chief Mohammad Eslami says"
- SEPN (Septerna, Inc.) score 24.6 — "OPENAI RECENTLY TOLD INVESTORS ITS REVENUES WERE APPROACHING $50BN ON AN ANNUALISED BASIS "
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 22.6 — "Nifty falls 15% YTD: Top experts reveal stock market outlook, their preferred sectors now"
- 301077.SZ (CHINASTARS) score 18.1 — "CHINA STEPS UP ECONOMIC TALKS WITH UK AND EU Chinese Vice Premier He Lifeng called for str"
- JIOFIN.BO (Jio Financial Services Limited) score 14.5 — "CHINA STEPS UP ECONOMIC TALKS WITH UK AND EU Chinese Vice Premier He Lifeng called for str"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 14.1 — "TCS share price expectations for tomorrow: How Q2 results 2026 will impact Tata stock on F"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 14.1 — "TCS share price expectations for tomorrow: How Q2 results 2026 will impact Tata stock on F"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 14.0 — "Market wrap: Infosys, Tech Mahindra, Adani Ent, ITC top gainers and losers on Nifty and Se"
- JUSTDIAL.BO (JUST DIAL LTD.) score 13.6 — "World’s Top Crude Trader Isn’t Ruling Out $200 Oil Just Yet"
- BZ=F (Brent Crude Oil Last Day Finan) score 13.0 — "ORCL - ORACLE SHARES SET FOR BIGGEST ONE-DAY DROP IN 12-WEEKS, LAST DOWN 6%"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 12.3 — "LAGARDE TOLD EURO FINANCE CHIEF: NO SENSE OF BROADENING PRICES *LAGARDE TO EURO FINANCE CH"
- JEF (Jefferies Financial Group Inc.) score 11.6 — "RBI rate hike done. Now what’s ahead for bank stocks? Jefferies, other brokerages weigh in"
- META (Meta) score 9.1 — "US President Donald Trump buys $1 million-plus stakes in Meta, Microsoft, McDonald’s; adds"
- VT (Vanguard Total World Stock Ind) score 9.0 — "World’s Top Crude Trader Isn’t Ruling Out $200 Oil Just Yet"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 9.0 — "LAGARDE TOLD EURO FINANCE CHIEF: NO SENSE OF BROADENING PRICES *LAGARDE TO EURO FINANCE CH"
- NVDA (NVIDIA Corporation) score 8.7 — "NVIDIA-BACKED FIRMUS SET TO POSTPONE AUSTRALIA IPO"
- RS (Reliance, Inc.) score 5.8 — "Reliance Drives India’s Venezuelan Oil Imports to Seven-Year High"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 5.5 — "UK Retailers Push to Cut Green Levies as Power Bills Top £440 Million"
- GS (Goldman Sachs Group, Inc. (The) score 4.8 — "Goldman Sachs sees 26% return for Asian equities, bets big on tech earnings surge"
- POLICYBZR.NS (PB FINTECH LIMITED) score 3.9 — "Pine Labs, CAMS, Moneyview, other fintech stocks rally up to 11% after RBI MPC move. Here’"
- DELL (Dell Technologies Inc.) score 0.9 — "Piero Cipollone: Interview with Corriere della Sera"
- VOLTAS.NS (VOLTAS LTD) score 0.1 — "Voltas’s market share is growing. Will margins follow?"

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