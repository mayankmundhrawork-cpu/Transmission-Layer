# Transmission Layer — board brief · 2026-11-04 12:03Z

data as of **2026-11-04** · 97 series · 7 red / 32 amber · 8 events surfaced (24 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.581, 1d in regime; vol-pct 0.662, breadth-off 0.5, Markov P(high-vol) 0.085)
- [INVERTED] **safe_haven_gold** — corr20 -0.61, corr60 -0.5, contra nifty_50 corr20=0.27, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.25, corr60 0.14, last shift 2026-09-10. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.01, corr60 0.07, last shift 2026-09-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.74, last shift 2026-09-16. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.33, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.13, corr60 -0.11, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.62, corr60 0.41, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **7 of 89** scanned series survive multiplicity control (effective p ≤ 0.005605629265529988)
- **SETUP** dxy → usd_jpy: leads 1d (ccf 0.648, β 0.9003, p 0.0); driver zc -1.7 → expected -0.455%. Type hit-rate 0.828 (n=1706).
- **SETUP** dxy → aud_usd: leads 1d (ccf -0.566, β -0.8344, p 0.0); driver zc -1.7 → expected 0.422%. Type hit-rate 0.828 (n=1706).
- **SETUP** vix → asx_200: leads 1d (ccf -0.495, β -0.0446, p 0.0); driver zc -1.53 → expected 0.565%. Type hit-rate 0.828 (n=1706).
- **SETUP** vix → nikkei_225: leads 1d (ccf -0.478, β -0.0864, p 0.0); driver zc -1.53 → expected 1.095%. Type hit-rate 0.828 (n=1706).
- **SETUP** vix → taiwan_weighted: leads 1d (ccf -0.435, β -0.0805, p 0.0); driver zc -1.53 → expected 1.02%. Type hit-rate 0.828 (n=1706).
- **SETUP** dxy → usd_mxn: leads 1d (ccf 0.435, β 0.6192, p 0.0); driver zc -1.7 → expected -0.313%. Type hit-rate 0.828 (n=1706).
- **SETUP** vix → aud_usd: leads 1d (ccf -0.432, β -0.0295, p 0.0); driver zc -1.53 → expected 0.374%. Type hit-rate 0.828 (n=1706).
- **SETUP** vix → usd_mxn: leads 1d (ccf 0.43, β 0.0283, p 0.0); driver zc -1.53 → expected -0.358%. Type hit-rate 0.828 (n=1706).
- **SETUP** vix → kospi: leads 1d (ccf -0.342, β -0.0944, p 0.0); driver zc -1.53 → expected 1.196%. Type hit-rate 0.828 (n=1706).
- **SETUP** dxy → usd_brl: leads 1d (ccf 0.268, β 0.5693, p 0.0); driver zc -1.7 → expected -0.288%. Type hit-rate 0.828 (n=1706).
- **SETUP** ftse_100 → asx_200: leads 1d (ccf 0.261, β 0.2651, p 0.02682); driver zc 1.55 → expected 0.326%. Type hit-rate 0.828 (n=1706).
- Track record · residual_reversion: hit-rate **0.509** (n=1120) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.828** (n=1706) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.529** (n=17) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.12] indices · 2 series ↑
- nifty_50 [INDICES]: last 23960.60, z20 3.28, zc 0.69, resid-z 2.20 [unexplained], 1d 0.63%, |z20|=3.28
- nifty_fmcg [INDICES]: last 46266.95, z20 2.55, zc 1.05, resid-z 1.36 [quiet], 1d 1.51%, |z20|=2.55
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-18 (z-distance 0.29).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.703 via nifty_50, z 1.25, reacted); dyn_bajfinance_ns (rho 0.63 via nifty_50, z 2.17, reacted); dyn_jiofin_bo (rho 0.612 via nifty_50, z 2.11, reacted); dyn_indusindbk_bo (rho 0.56 via nifty_50, z 0.13, quiet); nifty_metal (rho 0.551 via nifty_50, z 2.2, reacted)
- Watch next: india_vix (inverse) — not yet - watch; rho -0.703 vs nifty_50
- Watch next: dyn_indusindbk_bo (co-move) — not yet - watch; rho 0.56 vs nifty_50
- **India receivers**: nifty_midcap_100 (rho 0.703, z 1.25); dyn_bajfinance_ns (rho 0.63, z 2.17); dyn_jiofin_bo (rho 0.612, z 2.11); dyn_indusindbk_bo (rho 0.56, z 0.13)
- Source: US Midterm Election Results Impact Decoded: Can Sensex, Nifty hit new peak? Gold, silver rates rebound with Trump loss — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-news/us-midterm-election-results-impact-decoded-can-sensex-nifty-hit-new-peak-gold-silver-rates-rebound-with-trump-loss-11793788769424.html
- Source: Stock Market Rally: Bulls to stay? Nifty, Sensex gain 5.5% in 5 sessions; Can the momentum sustain? Key levels to watch — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-rally-bulls-to-stay-nifty-sensex-gain-5-5-in-5-sessions-can-the-momentum-sustain-key-levels-to-watch-11793787625537.html
- Source: Sensex today | Stock Market Highlights: Sensex, Nifty post longest winning streak in nearly 5 months on FPI inflow hopes — BusinessLine Mkts, 2026-11-04. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-4th-november-2026/article71661036.ece
- Historical analogues: 2025-07-18 (d=0.29), 2025-08-01 (d=0.88), 2025-07-11 (d=1.11)

### [RED 5.62] dxy ↓
- dxy [FX]: last 101.36, z20 -2.62, zc -1.70, resid-z -0.88 [moved], 1d -0.51%, 20d range extreme; |z20|=2.62
- **Mechanism**: dxy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.55 vs dxy, historically leads by 1d
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-10 (d=0.03), 2025-05-14 (d=0.06)

### [RED 5.39] fx · 2 series ↑
- gbp_usd [FX]: last 1.35, z20 2.55, zc 1.66, resid-z 3.06 [unexplained], 1d 0.56%, |z20|=2.55
- eur_usd [FX]: last 1.13, z20 1.94, zc 1.91, resid-z 3.06 [unexplained], 1d 0.58%, |z20|=1.94
- **Mechanism**: fx · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.351 via eur_usd, z 1.87, reacted)
- **India receivers**: dyn_muthootfin_ns (rho 0.351, z 1.87)
- Source: Euro zone inflation hits 4% for first time in three years as interest rate hike looms — CNBC Economy, 2026-11-04. https://www.cnbc.com/2026/11/04/euro-zone-cpi-inflation-october-ecb-rate-hike.html
- Source: META HOLDS CALLS FOR MULTI TRANCHE DOLLAR AND EURO BOND SALE — DeItaone, 2026-11-02. https://t.me/walter_bloomberg/37925
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [AMBER 5.33] cross-asset · 3 series ↓
- ust_2y [RATES]: last 4.59, z20 -2.01, zc -0.84, resid-z -0.81 [quiet], 1d 0.66%, |z20|=2.01
- ust_10y [RATES]: last 4.91, z20 -1.83, zc -0.75, resid-z -1.16 [quiet], 1d -0.61%, |z20|=1.83
- dyn_schd [EQUITIES]: last 35.54, z20 1.13, zc -1.17, resid-z -0.68 [quiet], 1d -1.00%, 1y-pct=98
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.735 vs ust_2y
- Watch next: dyn_tgt (co-move) — not yet - watch; rho 0.599 vs dyn_schd
- Watch next: kospi (inverse) — not yet - watch; rho -0.543 vs dyn_schd
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.004 vs ust_2y, historically leads by 1d
- Source: How Indian Metals & Ferro Alloys shares performed post Q2; profit up 51%,  ₹5 dividend; what drove performance? — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-news/how-indian-metals-ferro-alloys-shares-performed-post-q2-results-profit-up-51-rs-5-dividend-what-drove-performa-11793789113686.html
- Source: Eurozone bond yields steady as investors await inflation data; US Treasury yields ease after midterm elections — ET Markets, 2026-11-04. https://economictimes.indiatimes.com/markets/us-stocks/news/eurozone-bond-yields-steady-as-investors-await-inflation-data-us-treasury-yields-ease-after-midterm-elections/articleshow/135535574.cms
- Source: Small-cap stock with 1:10 split, 1:2 bonus shares and dividend history jumps 4% after Q2 results; do you own it? — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-news/smallcap-stock-with-1-10-stock-split-1-2-bonus-shares-dividend-history-jumps-4-after-q2-results-2026-do-you-own-11793784583281.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-12 (d=0.46), 2025-05-19 (d=1.07)

### [AMBER 4.81] indices · 2 series ↓
- sp500 [INDICES]: last 7568.58, z20 -1.98, zc 0.37, resid-z -2.23 [unexplained], 1d 0.36%, |z20|=1.98
- nasdaq_100 [INDICES]: last 28180.26, z20 -1.85, zc 0.38, resid-z -0.35 [quiet], 1d 0.68%, |z20|=1.85
- **Mechanism**: indices · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.732 vs sp500, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.843 vs sp500
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.825 vs sp500
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.704 vs sp500
- Source: US bond yields fall; Nasdaq, Dow Jones futures slip 2% as Democrats set for big win in US midterm elections — ET Markets, 2026-11-04. https://economictimes.indiatimes.com/markets/us-stocks/news/us-bond-yields-fall-nasdaq-dow-jones-futures-slip-2-as-democrats-set-for-big-win-in-us-midterm-elections/articleshow/135527339.cms
- Source: US midterm elections: Early Democratic wins rattle Wall Street — ET Markets, 2026-11-04. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-midterm-elections-early-democratic-wins-rattle-wall-street/articleshow/135523666.cms
- Source: Stock market outlook today, 4 Nov: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-4-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-11793752972780.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-07 (d=0.06), 2026-05-15 (d=0.07)

### [RED 4.49] indices · 3 series ↑
- cac_40 [INDICES]: last 8141.73, z20 3.17, zc 1.93, resid-z -0.56 [moved], 1d 1.51%, |z20|=3.17
- stoxx_50 [INDICES]: last 6255.41, z20 2.55, zc 2.00, resid-z -1.06 [moved], 1d 1.80%, |z20|=2.55
- dax [INDICES]: last 26247.33, z20 2.53, zc 1.62, resid-z -1.02 [moved], 1d 1.48%, |z20|=2.53
- **Mechanism**: indices · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.549 via dax, z 1.25, reacted); nifty_50 (rho 0.494 via cac_40, z 3.28, reacted); nifty_fmcg (rho 0.461 via cac_40, z 2.55, reacted); dyn_muthootfin_ns (rho 0.449 via stoxx_50, z 1.87, reacted); dyn_tataelxsi_ns (rho 0.431 via cac_40, z 0.6, quiet)
- Watch next: ftse_100 (co-move) — not yet - watch; rho 0.789 vs cac_40, historically leads by 5d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.593 vs stoxx_50, historically leads by 5d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.535 vs dax, historically leads by 5d
- Watch next: wti (inverse) — not yet - watch; rho -0.531 vs stoxx_50, historically leads by 4d
- **India receivers**: nifty_midcap_100 (rho 0.549, z 1.25); nifty_50 (rho 0.494, z 3.28); nifty_fmcg (rho 0.461, z 2.55); dyn_muthootfin_ns (rho 0.449, z 1.87)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-16 (d=0.39), 2025-09-01 (d=0.4)

### [AMBER 4.35] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1840.00, z20 2.35, zc 0.77, resid-z 0.42 [quiet], 1d 2.51%, |z20|=2.35; 1y-pct=100
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.381 via dyn_atherenerg_ns, z 1.25, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.381, z 1.25)
- Source: Diwali stock picks, Samvat 2083: Park Medi, HDFC, Paytm, Meesho, Ather among Ventura picks- Which offers highest upside? — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-news/diwali-stock-picks-samvat-2083-park-medi-hdfc-paytm-meesho-ather-among-ventura-picks-which-offers-highest-upside-11793775881503.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [AMBER 4.28] dyn_jef ↑
- dyn_jef [EQUITIES]: last 48.59, z20 2.28, zc 0.19, resid-z -3.25 [unexplained], 1d 0.66%, |z20|=2.28
- **Mechanism**: dyn_jef ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.475 via dyn_jef, z 0.13, quiet)
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.625 vs dyn_jef, historically leads by 5d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.726 vs dyn_jef
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.571 vs dyn_jef
- **India receivers**: dyn_indusindbk_bo (rho 0.475, z 0.13)
- Source: Bajaj Finserv shares rise 2%, extend gains after Q2 results. Why Jefferies reduced target price but still sees 34% upside — ET Markets, 2026-11-04. https://economictimes.indiatimes.com/markets/stocks/news/bajaj-finserv-shares-rise-2-extend-gains-after-q2-results-why-jefferies-reduced-target-price-but-still-sees-34-upside/articleshow/135524029.cms
- Source: Emcure Pharma shares hit 10% upper circuit after FY27 guidance hike; Jefferies raises target price by 8% — ET Markets, 2026-11-04. https://economictimes.indiatimes.com/markets/stocks/news/emcure-pharma-shares-hit-10-upper-circuit-after-fy27-guidance-hike-jefferies-raises-target-price-by-8/articleshow/135523159.cms
- Source: ITC shares rise 2% after Q2 results. What are Jefferies, Nuvama and others saying? — ET Markets, 2026-11-03. https://economictimes.indiatimes.com/markets/stocks/news/itc-shares-rise-2-after-q2-results-what-are-jefferies-nuvama-and-others-saying/articleshow/135481293.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-01 (d=0.04), 2025-08-19 (d=0.07)

## Watchlist (below surfacing floor)
dyn_bajfinance_ns ↑ (4.17), dyn_ohi ↑ (4.16), dyn_jiofin_bo ↑ (4.11), dyn_coin ↓ (3.92), dyn_rs ↑ (3.81), corn ↓ (3.54), dyn_4417_t ↑ (3.54), dyn_policybzr_ns ↓ (3.41), dyn_sepn ↑ (3.33), rates · 2 series ↑ (3.25), dyn_tech ↑ (3.06), dyn_techm_ns ↑ (2.69)

## India macro
- nifty_50: 23960.5996 (1d 0.63%, z20 3.28, flag red)
- nifty_midcap_100: 59514.3008 (1d 1.56%, z20 1.25, flag none)
- usd_inr: 94.6400 (1d -0.09%, z20 -0.92, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4838 (1d 0.93%, z20 -1.11, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · AMFI SIP / MF flows T-5d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 99.2 — "SEBI signs MoU with Digital India BHASHINI div to provide services in regional languages"
- INOXINDIA.NS (INOX INDIA LIMITED) score 99.2 — "SEBI signs MoU with Digital India BHASHINI div to provide services in regional languages"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 98.1 — "SEBI signs MoU with Digital India BHASHINI div to provide services in regional languages"
- INDIANB.NS (INDIAN BANK) score 65.7 — "Diwali 2026: Will banking stocks shine in Samvat 2083? Analysts list top picks"
- OHI (Omega Healthcare Investors, In) score 47.5 — "BLS Polymers shares jump 7% for second day, hit record high; stock rallies 92% over IPO pr"
- BAC (Bank of America Corporation) score 46.0 — "Diwali 2026: Will banking stocks shine in Samvat 2083? Analysts list top picks"
- HDB (HDFC Bank Limited) score 45.1 — "Diwali 2026: Will banking stocks shine in Samvat 2083? Analysts list top picks"
- TGT (Target Corporation) score 43.5 — "MCX vs NSE vs BSE: Which is best exchange stock to buy after Q2 Results 2026? Experts' vie"
- TECHM.NS (TECH MAHINDRA LIMITED) score 41.3 — "ideaForge Technology shares: Drone stock jumps 5%; delivers 48% YTD returns | Should you b"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 41.2 — "Diwali 2026: Will banking stocks shine in Samvat 2083? Analysts list top picks"
- IDBI.NS (IDBI BANK LIMITED) score 41.2 — "Diwali 2026: Will banking stocks shine in Samvat 2083? Analysts list top picks"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 41.2 — "Diwali 2026: Will banking stocks shine in Samvat 2083? Analysts list top picks"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.5 — "ideaForge Technology shares: Drone stock jumps 5%; delivers 48% YTD returns | Should you b"
- TECH (Bio-Techne Corp) score 39.5 — "ideaForge Technology shares: Drone stock jumps 5%; delivers 48% YTD returns | Should you b"
- COIN (Coinbase Global, Inc.) score 33.1 — "India’s VC funding declines 3% even as global investments surge 137%: GlobalData"
- CHKP (Check Point Software Technolog) score 30.0 — "ITC shares continue to rise after Q2 results 2026; jumps 3% today | More rally to come? Ch"
- 301077.SZ (CHINASTARS) score 29.7 — "China stocks struggle near one-year lows despite fresh government support measures"
- BOND (PIMCO Active Bond Exchange-Tra) score 27.6 — "US bond yields fall; Nasdaq, Dow Jones futures slip 2% as Democrats set for big win in US "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 26.8 — "Diwali stock picks, Samvat 2083: Park Medi, HDFC, Paytm, Meesho, Ather among Ventura picks"
- RS (Reliance, Inc.) score 25.9 — "How Jio is unlocking hidden value for Reliance shareholders"
- LTH (Life Time Group Holdings, Inc.) score 22.2 — "Euro zone inflation hits 4% for first time in three years as interest rate hike looms"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 19.1 — "Bajaj Finserv shares rise 2%, extend gains after Q2 results. Why Jefferies reduced target "
- JIOFIN.BO (Jio Financial Services Limited) score 17.6 — "SEBI signs MoU with Digital India BHASHINI div to provide services in regional languages"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 14.6 — "MCX vs NSE vs BSE: Which is best exchange stock to buy after Q2 Results 2026? Experts' vie"
- SCHD (Schwab US Dividend Equity ETF) score 14.3 — "Small-cap stock with 1:10 split, 1:2 bonus shares and dividend history jumps 4% after Q2 r"
- BZ=F (Brent Crude Oil Last Day Finan) score 14.0 — "U.S. TREASURY YIELDS RISE SLIGHTLY AFTER ECONOMIC DATA; YIELD ON 10-YEAR TREASURY NOTE LAS"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 12.1 — "Democrats win the House and Senate. Here’s what it means for your finances."
- SEPN (Septerna, Inc.) score 12.0 — "US FACTORY ORDERS SURGE 1.8%, BEATING EXPECTATIONS US factory orders rose 1.8% in Septembe"
- META (Meta) score 11.2 — "Meta raises $15 billion through bond sale to fund AI infrastructure expansion"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.0 — "Muhurat Trading Picks: Tata Steel, Coal India to BEL - HDFC Sec recommends these 10 stocks"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 11.0 — "Muhurat Trading Picks: Tata Steel, Coal India to BEL - HDFC Sec recommends these 10 stocks"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.2 — "Samvat 2083 stock picks! Adani Power, Coal India, 8 others to add in your portfolio this f"
- JEF (Jefferies Financial Group Inc.) score 8.7 — "Emcure Pharma shares hit 10% upper circuit after FY27 guidance hike; Jefferies raises targ"
- VT (Vanguard Total World Stock Ind) score 8.0 — "China Now Home to Nearly Half of World's Clean Industrial Plants"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.3 — "LTCG abolition may cost just Rs 40,000–50,000 crore, SBI estimates show"
- GS (Goldman Sachs Group, Inc. (The) score 6.8 — "The AI trade has been ‘sold to death’ but Goldman strategist highlights silver lining from"
- INFY (Infosys Limited) score 4.2 — "Market wrap:  RIL, Tata Steel, Infosys, ICICI Bank top gainers and losers on Nifty and Sen"
- DEMZ (Democratic Large Cap Core ETF) score 2.9 — "Kopsi, Taiwan, other Asian stocks tumble after US midterm elections signal Democratic vict"
- POLICYBZR.NS (PB FINTECH LIMITED) score 1.5 — "Broker’s call: PB Fintech (Buy)"
- SWIGGY.NS (SWIGGY LIMITED) score 0.7 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"

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