# Transmission Layer — board brief · 2026-10-15 19:53Z

data as of **2026-10-15** · 97 series · 10 red / 28 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.673, 9d in regime; vol-pct 0.64, breadth-off 0.706, Markov P(high-vol) 0.02)
- [INVERTED] **safe_haven_gold** — corr20 -0.42, corr60 -0.43, contra nifty_50 corr20=0.38, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.88, corr60 0.84, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.22, corr60 0.21, last shift 2026-07-10. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.19, corr60 0.14, last shift 2026-08-25. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.78, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.12, corr60 -0.03, last shift 2026-08-11. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.24, corr60 -0.27, last shift 2026-08-21. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.75, corr60 0.23, last shift 2026-07-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **4 of 89** scanned series survive multiplicity control (effective p ≤ 0.003976751709788617)
- **SETUP** dow_jones → asx_200: leads 1d (ccf 0.591, β 0.492, p 0.0); driver zc 1.5 → expected 0.536%. Type hit-rate 0.824 (n=2203).
- **SETUP** dow_jones → nikkei_225: leads 1d (ccf 0.462, β 0.7761, p 0.0); driver zc 1.5 → expected 0.845%. Type hit-rate 0.824 (n=2203).
- **SETUP** dow_jones → usd_brl: leads 1d (ccf -0.415, β -0.3469, p 0.0); driver zc 1.5 → expected -0.378%. Type hit-rate 0.824 (n=2203).
- **SETUP** dow_jones → aud_usd: leads 1d (ccf 0.403, β 0.2608, p 1e-05); driver zc 1.5 → expected 0.284%. Type hit-rate 0.824 (n=2203).
- **SETUP** dow_jones → usd_mxn: leads 1d (ccf -0.38, β -0.2345, p 0.0); driver zc 1.5 → expected -0.255%. Type hit-rate 0.824 (n=2203).
- **SETUP** comex_gold → aud_usd: leads 1d (ccf 0.366, β 0.1567, p 0.0); driver zc 1.55 → expected 0.306%. Type hit-rate 0.824 (n=2203).
- **SETUP** dyn_coin → aud_usd: leads 1d (ccf 0.264, β 0.0319, p 0.00022); driver zc 1.55 → expected 0.225%. Type hit-rate 0.824 (n=2203).
- **SETUP** ftse_100 → asx_200: leads 1d (ccf 0.26, β 0.2666, p 0.02643); driver zc 1.57 → expected 0.286%. Type hit-rate 0.824 (n=2203).
- Track record · residual_reversion: hit-rate **0.496** (n=1143) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.824** (n=2203) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.19] cross-asset · 2 series ↑
- gold_silver_ratio [DERIVED]: last 72.81, z20 2.36, zc n/a, resid-z n/a [quiet], 1d -1.54%, GSR<75 (extreme low); |z20|=2.36
- comex_silver [COMMODITIES]: last 57.52, z20 -1.52, zc 1.22, resid-z 0.70 [quiet], 1d 3.55%, |z20|=1.52
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.827 vs comex_silver, historically leads by 4d
- Watch next: dyn_coin (co-move) — not yet - watch; rho 0.568 vs comex_silver, historically leads by 5d
- Watch next: comex_copper (inverse) — not yet - watch; rho -0.508 vs gold_silver_ratio, historically leads by 3d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.507 vs comex_silver
- Source: Silver futures rise to ₹2.08 lakh per kg — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/markets/gold/silver-futures-rise-to-208-lakh-per-kg/article71586939.ece
- Source: Silver futures plunge 4% on MCX ahead of US CPI; rising oil adds pressure — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/commodities/silver-futures-plunge-4-on-mcx-ahead-of-us-cpi-rising-oil-adds-pressure/articleshow/134946048.cms
- Source: SPOT SILVER FALLS NEARLY 3% TO $57.58/OZ — DeItaone, 2026-10-14. https://t.me/walter_bloomberg/37071
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-29 (d=0.06), 2025-08-12 (d=0.14)

### [RED 7.9] cross-asset · 3 series ↑
- dyn_techm_ns [EQUITIES]: last 1650.00, z20 4.59, zc 2.75, resid-z 1.92 [unexplained], 1d 4.75%, |z20|=4.59
- dyn_tataelxsi_ns [EQUITIES]: last 3700.00, z20 3.51, zc 0.85, resid-z 0.08 [quiet], 1d 2.12%, |z20|=3.51
- nifty_it [INDICES]: last 30719.80, z20 3.38, zc 1.08, resid-z -0.07 [quiet], 1d 1.82%, |z20|=3.38
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.78).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_justdial_bo (rho 0.502 via nifty_it, z 1.06, reacted); nifty_fmcg (rho 0.5 via dyn_tataelxsi_ns, z -0.45, quiet); nifty_50 (rho 0.491 via dyn_techm_ns, z 0.37, quiet); dyn_tatatech_ns (rho 0.479 via nifty_it, z 1.53, reacted); midcap_largecap_ratio (rho -0.418 via dyn_techm_ns, z -3.43, reacted)
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.5 vs dyn_tataelxsi_ns
- **India receivers**: dyn_justdial_bo (rho 0.502, z 1.06); nifty_fmcg (rho 0.5, z -0.45); nifty_50 (rho 0.491, z 0.37); dyn_tatatech_ns (rho 0.479, z 1.53)
- Source: Q2 Results Highlights, 15 Oct: Wipro PAT rises 9% year-on-year; Tech Mahindra profit jumps 32.7%; Nestlé shares tank after Q2 results; IIFL Finance, IRFC, Polycab, KVB and HDFC AMC report higher PAT; Heritage Foods posts decline — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/markets/q2-results-highlights-wipro-nestle-india-tech-mahindra-jio-financial-persistent-systems-irfc-polycab-hdfc-amc-tata-communication-results-groww-tata-tech-leela-emmvee-15-october-2026/article71586591.ece
- Source: Q2 results: Tech Mahindra dividend, bonus shares - Double delight for 7 lakh investors | Payout, ratio, record date — Mint Markets, 2026-10-15. https://www.livemint.com/market/stock-market-news/q2-results-tech-mahindra-dividend-bonus-shares-double-delight-for-7-lakh-investors-payout-ratio-record-date-11792060760425.html
- Source: Tech Mahindra announces 1:1 bonus issue, Rs 15 interim dividend; check record date — ET Markets, 2026-10-15. https://economictimes.indiatimes.com/markets/stocks/earnings/tech-mahindra-announces-11-bonus-issue-rs-15-interim-dividend-check-record-date/articleshow/134968892.cms
- Historical analogues: 2025-08-13 (d=0.78), 2025-01-23 (d=0.84), 2025-12-30 (d=0.85)

### [RED 7.65] usd_inr ↓
- usd_inr [FX]: last 95.04, z20 -2.65, zc -0.48, resid-z -0.51 [quiet], 1d -0.25%, 20d range extreme; |z20|=2.65
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_karurvysya_ns (rho -0.369 via usd_inr, z 2.27, reacted); dyn_idbi_ns (rho -0.358 via usd_inr, z -0.4, quiet)
- **India receivers**: dyn_karurvysya_ns (rho -0.369, z 2.27); dyn_idbi_ns (rho -0.358, z -0.4)
- Source: Rupee ends flat, anchored by RBI intervention in face of global strains — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/markets/forex/rupee-ends-flat-anchored-by-rbi-intervention-in-face-of-global-strains/article71546994.ece
- Source: Gap-Up fades as IT and HDFC Bank drag Nifty to near-flat; crude, Rupee weigh — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/markets/gap-up-fades-as-it-and-hdfc-bank-drag-nifty-to-near-flat-crude-rupee-weigh/article71546207.ece
- Source: Rupee trades in narrow range against US dollar in early trade — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/markets/forex/rupee-trades-in-narrow-range-against-us-dollar-in-early-trade/article71545849.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 6.43] midcap_largecap_ratio ↓
- midcap_largecap_ratio [DERIVED]: last 2.57, z20 -3.43, zc n/a, resid-z n/a [quiet], 1d -1.97%, break below 100-DMA; |z20|=3.43
- **Mechanism**: midcap_largecap_ratio ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.523 via midcap_largecap_ratio, z -0.72, quiet); dyn_techm_ns (rho -0.418 via midcap_largecap_ratio, z 4.59, reacted); dyn_cartrade_ns (rho 0.375 via midcap_largecap_ratio, z -0.01, quiet)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.523 vs midcap_largecap_ratio, historically leads by 2d
- **India receivers**: nifty_midcap_100 (rho 0.523, z -0.72); dyn_techm_ns (rho -0.418, z 4.59); dyn_cartrade_ns (rho 0.375, z -0.01)
- Historical analogues: 2025-12-31 (d=0.0), 2025-07-03 (d=0.11), 2025-07-23 (d=0.2)

### [RED 5.08] dyn_301077_sz ↓
- dyn_301077_sz [EQUITIES]: last 19.80, z20 -3.08, zc -0.97, resid-z -0.36 [quiet], 1d -2.80%, |z20|=3.08; 1y-pct=5
- **Mechanism**: dyn_301077_sz ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: India poised to fill fuel export gap as China suspends October shipments — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/markets/commodities/india-poised-to-fill-fuel-export-gap-as-china-suspends-october-shipments/article71546098.ece
- Source: Global Market: China stocks fall as hot US inflation data revives rate hike fears — ET Markets, 2026-10-15. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-fall-as-hot-us-inflation-data-revives-rate-hike-fears/articleshow/134957483.cms
- Source: Global Market: China stocks slip as AI selloff deepens, mixed inflation data weighs — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-slip-as-ai-selloff-deepens-mixed-inflation-data-weighs/articleshow/134933453.cms
- Historical analogues: 2026-06-18 (d=0.0), 2026-03-30 (d=0.02), 2026-06-03 (d=0.03)

### [RED 4.92] shanghai_comp ↓
- shanghai_comp [INDICES]: last 3706.48, z20 -2.92, zc -2.24, resid-z -1.24 [moved], 1d -1.61%, |z20|=2.92; 1y-pct=0
- **Mechanism**: shanghai_comp ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_inoxindia_ns (rho 0.391 via shanghai_comp, z -1.48, reacted)
- Watch next: nikkei_225 (co-move) — not yet - watch; rho 0.638 vs shanghai_comp, historically leads by 2d
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.509 vs shanghai_comp, historically leads by 1d
- **India receivers**: dyn_inoxindia_ns (rho 0.391, z -1.48)
- Source: Global Market: China stocks fall as hot US inflation data revives rate hike fears — ET Markets, 2026-10-15. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-fall-as-hot-us-inflation-data-revives-rate-hike-fears/articleshow/134957483.cms
- Source: Global Market: China stocks slip as AI selloff deepens, mixed inflation data weighs — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-slip-as-ai-selloff-deepens-mixed-inflation-data-weighs/articleshow/134933453.cms
- Historical analogues: 2026-06-18 (d=0.0), 2025-12-19 (d=0.02), 2025-09-25 (d=0.03)

### [RED 4.72] dyn_dell ↓
- dyn_dell [EQUITIES]: last 464.18, z20 -4.72, zc -1.48, resid-z -0.21 [quiet], 1d -8.61%, |z20|=4.72
- **Mechanism**: dyn_dell ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.614 vs dyn_dell, historically leads by 5d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.558 vs dyn_dell, historically leads by 5d
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-08 (d=0.18), 2025-10-01 (d=0.3)

### [RED 4.32] kospi ↓
- kospi [INDICES]: last 5484.38, z20 -4.32, zc -3.35, resid-z -1.66 [unexplained], 1d -8.73%, |z20|=4.32
- **Mechanism**: kospi ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho 0.486 via kospi, z -0.56, quiet); dyn_techm_ns (rho -0.407 via kospi, z 4.59, reacted); nifty_it (rho -0.383 via kospi, z 3.38, reacted)
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.928 vs kospi, historically leads by 2d
- Watch next: nikkei_225 (co-move) — not yet - watch; rho 0.832 vs kospi, historically leads by 2d
- **India receivers**: dyn_bajfinance_ns (rho 0.486, z -0.56); dyn_techm_ns (rho -0.407, z 4.59); nifty_it (rho -0.383, z 3.38)
- Historical analogues: 2026-07-10 (d=0.0), 2026-04-02 (d=0.01), 2025-04-01 (d=0.04)

## Watchlist (below surfacing floor)
rates · 4 series ↑ (4.29), dow_jones ↑ (4.23), dyn_nvda ↓ (4.17), soybeans ↓ (4.15), dyn_hdb ↑ (4.13), dyn_rs ↑ (3.59), eur_usd ↓ (3.01), dyn_4417_t ↑ (3.01), dxy ↑ (2.68), dyn_tech ↑ (2.62), dyn_jiofin_bo ↓ (2.34), dyn_karurvysya_ns ↑ (2.27)

## India macro
- nifty_50: 22997.3496 (1d 1.66%, z20 0.37, flag none)
- nifty_midcap_100: 59192.0000 (1d -0.35%, z20 -0.72, flag none)
- usd_inr: 95.0450 (1d -0.25%, z20 -2.65, flag red)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5739 (1d -1.97%, z20 -3.43, flag red)
- Next India prints: NSDL FPI flows T-0d · India trade / CAD data T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 111.1 — "Indian markets eye gap-up opening; crude, bond yields and RBI policy remain key"
- INOXINDIA.NS (INOX INDIA LIMITED) score 107.0 — "Indian markets eye gap-up opening; crude, bond yields and RBI policy remain key"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 105.9 — "Indian markets eye gap-up opening; crude, bond yields and RBI policy remain key"
- INDIANB.NS (INDIAN BANK) score 100.6 — "Indian markets eye gap-up opening; crude, bond yields and RBI policy remain key"
- BAC (Bank of America Corporation) score 91.6 — "U.S. CONSIDERS USING “MOTHER OF ALL BOMBS” AGAINST IRAN The Pentagon has reportedly develo"
- HDB (HDFC Bank Limited) score 84.8 — "HDFC AMC net profit up 4% on better earnings"
- IDBI.NS (IDBI BANK LIMITED) score 80.1 — "20 Stocks to watch today: HDFC Bank, ICICI life, Wipro, DLF, Ola Electric & Gland Pharma"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 80.1 — "20 Stocks to watch today: HDFC Bank, ICICI life, Wipro, DLF, Ola Electric & Gland Pharma"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 80.1 — "20 Stocks to watch today: HDFC Bank, ICICI life, Wipro, DLF, Ola Electric & Gland Pharma"
- TECHM.NS (TECH MAHINDRA LIMITED) score 74.4 — "Dow Jones| Nasdaq | US Stock Market Today | Live: Dow, S&P 500 rise as falling Treasury yi"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 73.1 — "Dow Jones| Nasdaq | US Stock Market Today | Live: Dow, S&P 500 rise as falling Treasury yi"
- TECH (Bio-Techne Corp) score 73.1 — "Dow Jones| Nasdaq | US Stock Market Today | Live: Dow, S&P 500 rise as falling Treasury yi"
- COIN (Coinbase Global, Inc.) score 62.6 — "IEA SAYS OIL RELEASE ANNOUNCED IN MARCH TO EXCEED 400M BARRELS *IEA NATIONS WILLING TO TAK"
- OHI (Omega Healthcare Investors, In) score 57.8 — "Sebi writes to IRDAI to include investors' insurance policy details in consolidated accoun"
- TGT (Target Corporation) score 42.8 — "U.S. CONSIDERS USING “MOTHER OF ALL BOMBS” AGAINST IRAN The Pentagon has reportedly develo"
- CHKP (Check Point Software Technolog) score 39.6 — "Newly listed stock has 30% upside potential! JM Financial issues buy call; Check target pr"
- BOND (PIMCO Active Bond Exchange-Tra) score 38.6 — "Indian markets eye gap-up opening; crude, bond yields and RBI policy remain key"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 33.5 — "IEA TO ACCELERATE OIL RESERVE RELEASES AS DIESEL SUPPLY TIGHTENS The International Energy "
- RS (Reliance, Inc.) score 28.5 — "Jio Platforms IPO: Uday Kotak draws interesting link between Reliance’s 1977 listing and J"
- SEPN (Septerna, Inc.) score 28.1 — "Pernod Ricard India sales grow 19% in Sept qtr; IPO plan awaits board approval"
- LTH (Life Time Group Holdings, Inc.) score 27.6 — "IT stocks: Accenture Q4 results, FY27 outlook lifts sentiment as Indian IT Q2 earnings nea"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 24.7 — "Reliance Jio IPO to be listed soon: Why a 12% tariff hike may be coming in 3-4 months? Exp"
- 301077.SZ (CHINASTARS) score 24.0 — "EU BEGINS ASSESSING ADDITIONAL SECTORS FOR CHINA TRADE QUOTAS"
- JIOFIN.BO (Jio Financial Services Limited) score 23.6 — "Jio Financial Services Q2 Results: PAT drops 51% YoY to Rs 340 crore; NII soars 165%"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 19.4 — "Tata Elxsi vs Tata Tech: Which Tata Group's stock wins Q2 results report card? Profit, rev"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 19.4 — "Tata Elxsi vs Tata Tech: Which Tata Group's stock wins Q2 results report card? Profit, rev"
- BZ=F (Brent Crude Oil Last Day Finan) score 17.9 — "PHILADELPHIA SEMICONDUCTOR INDEX HITS LOWEST IN NEARLY A MONTH, LAST DOWN 3.6%"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 17.6 — "Bajaj Finance gains on strong asset growth"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 15.5 — "Bajaj Finance gains on strong asset growth"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 12.7 — "Market Trading Guide: Adani Power among 2 stock recommendations for Friday"
- VT (Vanguard Total World Stock Ind) score 10.4 — "U.S. Wants World Bank to Drop Ban on Upstream Oil and Gas Funding"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.9 — "Sensex on fire! 1,500-point rally puts bulls back in the driver’s seat. What just happened"
- NVDA (NVIDIA Corporation) score 8.3 — "SHARES OF US CHIP-RELATED COMPANIES FALL NVIDIA DOWN 3% AMD FALLS 5% INTEL DOWN 5.9% MARVE"
- GS (Goldman Sachs Group, Inc. (The) score 7.1 — "Tata Tech shares rally 8% after Q2 results, but Goldman Sachs and JM Financial stay bearis"
- JEF (Jefferies Financial Group Inc.) score 6.1 — "Aditya Birla Capital shares: Up 30% in one year! Jefferies sees 25% more upside; should yo"
- META (Meta) score 5.7 — "IT stocks lift Nifty as Adani, Metal stocks slide amid global sellof"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 4.4 — "Bajaj Broking rolls out algorithm trading platform for retail investors"
- POLICYBZR.NS (PB FINTECH LIMITED) score 2.3 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
- DELL (Dell Technologies Inc.) score 0.2 — "Piero Cipollone: Interview with Corriere della Sera"
- VOLTAS.NS (VOLTAS LTD) score 0.0 — "Voltas’s market share is growing. Will margins follow?"

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