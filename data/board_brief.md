# Transmission Layer — board brief · 2026-09-10 14:25Z

data as of **2026-09-10** · 98 series · 15 red / 35 amber · 8 events surfaced (23 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.647, 1d in regime; vol-pct 0.589, breadth-off 0.706, Markov P(high-vol) 0.018)
- [INVERTED] **safe_haven_gold** — corr20 -0.42, corr60 -0.32, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.79, corr60 0.85, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.13, corr60 0.29, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.27, corr60 0.14, last shift 2026-06-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.82, corr60 -0.85, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.11, corr60 -0.03, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.35, corr60 -0.17, last shift 2026-06-29. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.18, corr60 0.09, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** dyn_bond → eur_usd: leads 1d (ccf 0.253, β 0.3655, p 4e-05); driver zc -1.62 → expected -0.189%. Type hit-rate 0.819 (n=2095).
- Track record · residual_reversion: hit-rate **0.496** (n=1124) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.819** (n=2095) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.57] cross-asset · 7 series ↓
- vix [INDICES]: last 17.95, z20 4.23, zc 1.16, resid-z n/a [quiet], 1d 9.05%, |z20|=4.23
- brent [COMMODITIES]: last 104.78, z20 3.23, zc 1.57, resid-z 0.98 [moved], 1d 3.53%, 1-session move +3.53% ≥ 1.5%; |z20|=3.23
- dow_jones [INDICES]: last 52155.49, z20 -3.06, zc -0.52, resid-z 0.47 [quiet], 1d -0.43%, |z20|=3.06
- wti [COMMODITIES]: last 99.39, z20 2.92, zc 1.53, resid-z 0.99 [moved], 1d 3.48%, 1-session move +3.48% ≥ 1.5%; |z20|=2.92
- dyn_vt [EQUITIES]: last 158.85, z20 -2.48, zc -0.86, resid-z 1.64 [unexplained], 1d -0.65%, |z20|=2.48
- russell_2000 [INDICES]: last 2894.40, z20 -2.44, zc -0.75, resid-z -0.35 [quiet], 1d -0.92%, |z20|=2.44
- sp500 [INDICES]: last 7597.99, z20 -2.19, zc -0.67, resid-z -0.56 [quiet], 1d -0.50%, |z20|=2.19
- **Mechanism**: cross-asset · 7 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-21 (z-distance 0.44).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.554 vs brent, historically leads by 4d
- Watch next: dyn_ms (inverse) — not yet - watch; rho -0.537 vs vix, historically leads by 5d
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.526 vs brent, historically leads by 5d
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.504 vs dyn_vt, historically leads by 1d
- Watch next: comex_copper (inverse) — not yet - watch; rho -0.541 vs vix
- Source: Brent crude tops $105 a barrel as tanker attacks intensify in Middle East; Saudi output cut fuels concerns — Mint Markets, 2026-09-10. https://www.livemint.com/market/stock-market-news/brent-crude-tops-105-a-barrel-as-tanker-attacks-intensify-in-middle-east-saudi-output-cut-fuels-concerns-11789044497665.html
- Source: United States on track for record crude oil production in 2026 — EIA Today in Energy, 2026-09-10. https://www.eia.gov/todayinenergy/detail.php?id=68125
- Source: Wall Street slumps as Brent crude climbs above $105, wholesale inflation rises — Mint Markets, 2026-09-10. https://www.livemint.com/market/stock-market-news/wall-street-slumps-as-brent-crude-climbs-above-105-wholesale-inflation-rises-11789045482327.html
- Historical analogues: 2025-10-21 (d=0.44), 2026-05-22 (d=0.46), 2024-10-18 (d=0.51)

### [RED 6.58] cross-asset · 4 series ↑
- dyn_bond [EQUITIES]: last 89.25, z20 -2.92, zc -1.62, resid-z 0.59 [priced], 1d -0.52%, |z20|=2.92; 1y-pct=0
- ust_10y [RATES]: last 4.80, z20 1.88, zc 0.22, resid-z -0.18 [quiet], 1d 0.42%, |z20|=1.88; 1y-pct=100
- ust_2y [RATES]: last 4.39, z20 1.80, zc 0.54, resid-z 0.16 [quiet], 1d 0.46%, |z20|=1.80; 1y-pct=99
- ust_30y [RATES]: last 5.25, z20 0.37, zc -0.25, resid-z -0.54 [quiet], 1d 0.19%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.354 via ust_2y, z 1.07, reacted)
- Watch next: tips_10y_real (inverse) — not yet - watch; rho -0.768 vs dyn_bond
- Watch next: dxy (inverse) — not yet - watch; rho -0.513 vs dyn_bond
- **India receivers**: midcap_largecap_ratio (rho -0.354, z 1.07)
- Source: Cash surplus softens India bond slide in oil-driven global rout — ET Markets, 2026-09-10. https://economictimes.indiatimes.com/markets/bonds/cash-surplus-softens-india-bond-slide-in-oil-driven-global-rout/articleshow/134009057.cms
- Source: Sebi completes first phase of Demat 2.0 bond pilot; secondary trading next: Tuhin Kanta Pandey — ET Markets, 2026-09-10. https://economictimes.indiatimes.com/markets/stocks/news/sebi-completes-first-phase-of-demat-2-0-bond-pilot-secondary-trading-next-tuhin-kanta-pandey/articleshow/134008996.cms
- Source: US Treasury yields hit highest level since 2023 as buyback disappoints — ET Markets, 2026-09-10. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-treasury-yields-hit-highest-level-since-2023-as-buyback-disappoints/articleshow/133996569.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-11 (d=0.3), 2025-05-08 (d=0.36)

### [RED 6.19] cross-asset · 3 series ↓
- nifty_it [INDICES]: last 28890.90, z20 -2.87, zc -0.05, resid-z -0.24 [quiet], 1d -0.08%, |z20|=2.87
- dyn_tataelxsi_ns [EQUITIES]: last 3409.00, z20 -2.33, zc 0.43, resid-z 0.63 [quiet], 1d 0.77%, |z20|=2.33; 1y-pct=1
- dyn_techm_ns [EQUITIES]: last 1525.80, z20 -2.23, zc 0.71, resid-z 0.47 [quiet], 1d 1.18%, |z20|=2.23
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.78).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tatatech_ns (rho 0.584 via nifty_it, z -1.77, reacted); nifty_50 (rho 0.512 via nifty_it, z -2.43, reacted)
- Watch next: shanghai_comp (inverse) — not yet - watch; rho -0.508 vs dyn_techm_ns, historically leads by 5d
- **India receivers**: dyn_tatatech_ns (rho 0.584, z -1.77); nifty_50 (rho 0.512, z -2.43)
- Source: IT stocks crash as Coforge, Infy, Tech Mahindra, HCL, TCS slide on H-1B visa fee hike — BusinessLine Mkts, 2026-09-09. https://www.thehindubusinessline.com/markets/it-stocks-crash-as-coforge-leads-selloff-infosys-tech-mahindra-hcl-tech-tcs-slide-h1-b-visa-in-focus/article71445708.ece
- Source: IT stocks crash as Coforge leads selloff; Infosys, Tech Mahindra, HCL Tech, TCS slide — BusinessLine Mkts, 2026-09-09. https://www.thehindubusinessline.com/markets/it-stocks-crash-as-coforge-leads-selloff-infosys-tech-mahindra-hcl-tech-tcs-slide/article71445708.ece
- Source: Tech Mahindra Share Price Live Updates: Tech Mahindra's Price Movement Analysis — ET Markets, 2026-09-09. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tech-mahindra-share-price-live-09-sep-2026/liveblog/133950510.cms
- Historical analogues: 2025-08-13 (d=0.78), 2025-01-23 (d=0.84), 2025-12-30 (d=0.85)

### [AMBER 6.14] cross-asset · 4 series ↓
- nifty_midcap_100 [INDICES]: last 62360.45, z20 -2.48, zc -0.55, resid-z -0.94 [quiet], 1d -0.37%, |z20|=2.48
- nifty_50 [INDICES]: last 23477.80, z20 -2.43, zc 0.35, resid-z 0.68 [quiet], 1d 0.20%, |z20|=2.43
- dyn_jiofin_bo [EQUITIES]: last 231.15, z20 -1.73, zc 0.04, resid-z -0.42 [quiet], 1d 0.06%, 1y-pct=4
- india_vix [INDICES]: last 11.74, z20 1.59, zc -0.27, resid-z n/a [quiet], 1d -1.53%, |z20|=1.59
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-17 (z-distance 0.67).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.624 via nifty_50, z -1.78, reacted); dyn_indianb_ns (rho 0.556 via nifty_midcap_100, z -2.1, reacted); nifty_it (rho 0.512 via nifty_50, z -2.87, reacted); dyn_techm_ns (rho 0.483 via nifty_50, z -2.23, reacted); dyn_indusindbk_bo (rho 0.462 via nifty_50, z -0.62, quiet)
- **India receivers**: nifty_fmcg (rho 0.624, z -1.78); dyn_indianb_ns (rho 0.556, z -2.1); nifty_it (rho 0.512, z -2.87); dyn_techm_ns (rho 0.483, z -2.23)
- Source: 'Buy' Nephrocare Health Services for 16% upside, says ICICI Securities; check share price target — Mint Markets, 2026-09-10. https://www.livemint.com/market/stock-market-news/buy-nephrocare-health-services-for-16-upside-says-icici-securities-check-share-price-target-11789044057519.html
- Source: CAS stays, but derivatives settlement may change, says Sebi chief Tuhin Kanta Pandey after another 1,000-point Sensex swing — ET Markets, 2026-09-10. https://economictimes.indiatimes.com/markets/stocks/news/cas-stays-but-derivatives-settlement-may-change-says-sebi-chief-tuhin-kanta-pandey-after-another-1000-point-sensex-swing/articleshow/134006996.cms
- Source: Sensex, Nifty snap 3-session losing streak as CAS recovery lifts indices — BusinessLine Mkts, 2026-09-10. https://www.thehindubusinessline.com/markets/sensex-nifty-snap-3-session-losing-streak-as-cas-recovery-lifts-indices/article71451277.ece
- Historical analogues: 2025-07-17 (d=0.67), 2025-12-19 (d=1.13), 2024-11-07 (d=1.15)

### [RED 5.27] dyn_hdb ↓
- dyn_hdb [EQUITIES]: last 21.83, z20 -3.27, zc -0.77, resid-z -0.32 [quiet], 1d -1.11%, |z20|=3.27; 1y-pct=0
- **Mechanism**: dyn_hdb ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.599 via dyn_hdb, z -2.43, reacted); nifty_it (rho 0.526 via dyn_hdb, z -2.87, reacted); dyn_techm_ns (rho 0.439 via dyn_hdb, z -2.23, reacted); dyn_jiofin_bo (rho 0.39 via dyn_hdb, z -1.73, reacted); dyn_bharatcoal_ns (rho 0.38 via dyn_hdb, z -0.87, quiet)
- **India receivers**: nifty_50 (rho 0.599, z -2.43); nifty_it (rho 0.526, z -2.87); dyn_techm_ns (rho 0.439, z -2.23); dyn_jiofin_bo (rho 0.39, z -1.73)
- Source: HDFC Bank shares rebound from fresh 52-week low: What is driving the stock? — BusinessLine Mkts, 2026-09-10. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-hit-fresh-52-week-low-for-second-straight-day-what-is-driving-the-stock/article71450256.ece
- Source: HDFC Bank shares fall 2% to fresh 52-week low; here’s why — BusinessLine Mkts, 2026-09-09. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-fall-2-to-fresh-52-week-low-heres-why/article71446043.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [RED 5.03] indices · 4 series ↓
- ftse_100 [INDICES]: last 10609.30, z20 -3.36, zc -0.66, resid-z -0.39 [quiet], 1d -0.57%, |z20|=3.36
- dax [INDICES]: last 25414.16, z20 -3.28, zc -0.64, resid-z -0.18 [quiet], 1d -0.63%, |z20|=3.28
- stoxx_50 [INDICES]: last 6272.06, z20 -2.80, zc -0.65, resid-z -0.16 [quiet], 1d -0.63%, |z20|=2.80
- cac_40 [INDICES]: last 8124.23, z20 -2.22, zc -0.37, resid-z 0.38 [quiet], 1d -0.40%, |z20|=2.22
- **Mechanism**: indices · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.5 via ftse_100, z -2.87, reacted); nifty_midcap_100 (rho 0.488 via dax, z -2.48, reacted); dyn_techm_ns (rho 0.4 via ftse_100, z -2.23, reacted); nifty_50 (rho 0.395 via ftse_100, z -2.43, reacted); dyn_indusindbk_bo (rho 0.359 via ftse_100, z -0.62, quiet)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.567 vs stoxx_50, historically leads by 1d
- Watch next: dyn_jef (co-move) — not yet - watch; rho 0.576 vs dax
- **India receivers**: nifty_it (rho 0.5, z -2.87); nifty_midcap_100 (rho 0.488, z -2.48); dyn_techm_ns (rho 0.4, z -2.23); nifty_50 (rho 0.395, z -2.43)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-16 (d=0.34), 2024-10-24 (d=0.48)

### [RED 5.03] dyn_ohi ↑
- dyn_ohi [EQUITIES]: last 47.85, z20 3.03, zc 1.08, resid-z -1.10 [quiet], 1d 1.40%, |z20|=3.03
- **Mechanism**: dyn_ohi ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.375 via dyn_ohi, z 1.07, reacted)
- **India receivers**: midcap_largecap_ratio (rho -0.375, z 1.07)
- Source: Top stocks in focus tomorrow: Investors must watch Fino Payments, KIMS, Texmaco Rail shares on Fri, 11 Sept | Triggers — Mint Markets, 2026-09-10. https://www.livemint.com/market/stock-market-news/top-stocks-in-focus-tomorrow-investors-must-watch-fino-payments-kims-texmaco-rail-shares-on-fri-11-sept-triggers-11789037727262.html
- Source: Investors flock to small, mid-cap funds, lured by strong recent gains — Mint Markets, 2026-09-10. https://www.livemint.com/market/investors-flock-to-small-mid-cap-funds-lured-by-strong-recent-gains-markets-mutual-funds-returns-11789036597511.html
- Source: SIP inflows hit record high in August: Can Indian stock market investors keep the momentum going? — Mint Markets, 2026-09-10. https://www.livemint.com/market/stock-market-news/sip-inflows-hit-record-high-in-august-can-indian-stock-market-investors-keep-the-momentum-going-amfi-data-11789039524267.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2024-10-15 (d=0.09)

### [AMBER 4.88] commodities · 3 series ↑
- corn [COMMODITIES]: last 530.00, z20 1.56, zc 3.46, resid-z 2.95 [unexplained], 1d 4.38%, |z20|=1.56; 1y-pct=100
- soybeans [COMMODITIES]: last 1318.00, z20 1.55, zc 1.70, resid-z 1.55 [unexplained], 1d 1.76%, |z20|=1.55; 1y-pct=100
- wheat [COMMODITIES]: last 728.25, z20 0.57, zc 1.09, resid-z 1.12 [quiet], 1d 2.39%, 1y-pct=96
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Wheat falls amid profit-taking, Black Sea war headlines — Mint Markets, 2026-09-09. https://www.livemint.com/market/wheat-falls-amid-profit-taking-black-sea-war-headlines-11788979794916.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

## Watchlist (below surfacing floor)
dyn_coalindia_ns ↑ (4.72), hang_seng ↓ (4.7), dyn_meta ↑ (4.66), usd_jpy ↓ (4.29), dyn_indianb_ns ↓ (4.1), dyn_pcjeweller_ns ↑ (4.1), midcap_largecap_ratio ↑ (4.07), gold_silver_ratio ↑ (4.03), dyn_lth ↓ (4.03), dyn_icicigi_bo ↓ (3.96), asx_200 ↓ (3.47), dyn_atherenerg_ns ↑ (3.22)

## India macro
- nifty_50: 23477.8008 (1d 0.20%, z20 -2.43, flag amber)
- nifty_midcap_100: 62360.4492 (1d -0.37%, z20 -2.48, flag amber)
- usd_inr: 95.4300 (1d 0.64%, z20 0.48, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6561 (1d -0.57%, z20 1.07, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · India CPI T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 89.1 — "Explained: Why US ETFs listed in India are trading at steep 65% premiums over the iNAV. Sh"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 85.3 — "Explained: Why US ETFs listed in India are trading at steep 65% premiums over the iNAV. Sh"
- COALINDIA.NS (COAL INDIA LTD) score 85.2 — "Explained: Why US ETFs listed in India are trading at steep 65% premiums over the iNAV. Sh"
- INDIANB.NS (INDIAN BANK) score 58.5 — "META - JPMORGAN TURNS BULLISH ON META’S AI POTENTIAL JPMorgan upgraded Meta to Overweight "
- COIN (Coinbase Global, Inc.) score 56.2 — "HOUTHIS SEIZE STRATEGIC RED SEA CITY Iran-backed Houthis have seized Yemen’s Mocha, accord"
- BAC (Bank of America Corporation) score 51.1 — "META - JPMORGAN TURNS BULLISH ON META’S AI POTENTIAL JPMorgan upgraded Meta to Overweight "
- OHI (Omega Healthcare Investors, In) score 47.8 — "Bitcoin consolidates near $78,000 as investors await key US inflation, Fed cues"
- HDB (HDFC Bank Limited) score 46.9 — "META - JPMORGAN TURNS BULLISH ON META’S AI POTENTIAL JPMorgan upgraded Meta to Overweight "
- CHKP (Check Point Software Technolog) score 45.6 — "Nuvama says 'Buy' Marico; check 12-month price target, stock performance, shareholding pat"
- IDBI.NS (IDBI BANK LIMITED) score 42.0 — "META - JPMORGAN TURNS BULLISH ON META’S AI POTENTIAL JPMorgan upgraded Meta to Overweight "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 42.0 — "META - JPMORGAN TURNS BULLISH ON META’S AI POTENTIAL JPMorgan upgraded Meta to Overweight "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 42.0 — "META - JPMORGAN TURNS BULLISH ON META’S AI POTENTIAL JPMorgan upgraded Meta to Overweight "
- BOND (PIMCO Active Bond Exchange-Tra) score 40.2 — "Sebi completes first phase of Demat 2.0 bond pilot; secondary trading next: Tuhin Kanta Pa"
- TECHM.NS (TECH MAHINDRA LIMITED) score 38.5 — "Market wrap:  HDFC Life, Power Grid, HCL Tech, Hindalco top gainers and losers on Nifty an"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 38.4 — "Market wrap:  HDFC Life, Power Grid, HCL Tech, Hindalco top gainers and losers on Nifty an"
- TECH (Bio-Techne Corp) score 38.4 — "Market wrap:  HDFC Life, Power Grid, HCL Tech, Hindalco top gainers and losers on Nifty an"
- 301077.SZ (CHINASTARS) score 28.5 — "25 dead after fire on board foreign-flagged cargo ship in China’s Qingdao"
- LTH (Life Time Group Holdings, Inc.) score 27.3 — "Sensex today | Stock Market Highlights: Sensex rises 138 pts, Nifty closes at 23,477 as cr"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 23.9 — "Ather Energy shares rise 3% as Nomura raises target price; stock up nearly 200% in 1 year"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 14.5 — "Karan Adani settles PMC Projects case with Sebi by paying Rs 13.65 lakh"
- JUSTDIAL.BO (JUST DIAL LTD.) score 13.8 — "TotalEnergies to Bring New Angola Discovery Online in Just Three Months"
- MS (Morgan Stanley) score 11.6 — "META - JPMORGAN TURNS BULLISH ON META’S AI POTENTIAL JPMorgan upgraded Meta to Overweight "
- PCJEWELLER.NS (PC JEWELLER LTD) score 11.1 — "PC Jeweller share price shines for second session | What's behind the rally?"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.0 — "This Tata Group stock surges 10% today amid a spurt in volume despite a weak stock market "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.0 — "This Tata Group stock surges 10% today amid a spurt in volume despite a weak stock market "
- JIOFIN.BO (Jio Financial Services Limited) score 9.0 — "META - JPMORGAN TURNS BULLISH ON META’S AI POTENTIAL JPMorgan upgraded Meta to Overweight "
- META (Meta) score 8.9 — "META - JPMORGAN TURNS BULLISH ON META’S AI POTENTIAL JPMorgan upgraded Meta to Overweight "
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 8.5 — "Mobile chain SS Retail to raise ₹500 crore via IPO"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.7 — "Running the numbers on Trump’s $5,000 dividend proposal, from its cost to the impact on av"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.6 — "'Buy' Nephrocare Health Services for 16% upside, says ICICI Securities; check share price "
- NVDA (NVIDIA Corporation) score 6.2 — "HUAWEI HIKES AI CHIP PRICES 60% Huawei has reportedly raised the price of its Ascend 950DT"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 6.1 — "Top stocks in focus today: Investors must watch Coal India, Shakti Pumps, Wipro shares on "
- SEPN (Septerna, Inc.) score 6.0 — "Textile company Sonaselection India sets IPO price band at ₹94-99/share; issue to open on "
- VT (Vanguard Total World Stock Ind) score 5.3 — "NSE slashes IPO ambitions as world’s biggest options boom fades"
- JEF (Jefferies Financial Group Inc.) score 4.7 — "Vodafone Idea shares price in focus as Jefferies initiates coverage with Buy rating. Why a"
- QCOM (QUALCOMM Incorporated) score 2.7 — "Qualcomm-Amazon AI deal: Why the chipmaker’s stock surged"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 1.2 — "Lenskart Solutions among 4 stocks to hit 52-week highs & rallied up to 22% in a month"
- DELL (Dell Technologies Inc.) score 1.0 — "Dell’s AI Boom: $95 billion backlog reshapes growth outlook"
- DKS (Dick's Sporting Goods Inc) score 0.2 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- VOLTAS.NS (VOLTAS LTD) score 0.0 — "Voltas reported strong growth in June quarter, but failed to impress"

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