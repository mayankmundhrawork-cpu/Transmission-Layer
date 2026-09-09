# Transmission Layer — board brief · 2026-09-09 19:16Z

data as of **2026-09-09** · 98 series · 21 red / 32 amber · 8 events surfaced (36 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.515, 1d in regime; vol-pct 0.383, breadth-off 0.647, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.43, corr60 -0.39, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.87, corr60 0.87, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.05, corr60 0.33, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.26, corr60 0.1, last shift 2026-06-05. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.81, corr60 -0.84, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.13, corr60 -0.05, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.35, corr60 -0.17, last shift 2026-06-26. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.01, corr60 0.21, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 90** scanned series survive multiplicity control (effective p ≤ 0.000262240308841033)
- **SETUP** ftse_100 → asx_200: leads 1d (ccf 0.268, β 0.2736, p 0.02465); driver zc -2.71 → expected -0.372%. Type hit-rate 0.825 (n=2038).
- **SETUP** stoxx_50 → asx_200: leads 1d (ccf 0.255, β 0.1915, p 0.00947); driver zc -2.36 → expected -0.332%. Type hit-rate 0.825 (n=2038).
- **SETUP** dax → asx_200: leads 1d (ccf 0.254, β 0.1832, p 0.00615); driver zc -2.41 → expected -0.321%. Type hit-rate 0.825 (n=2038).
- Track record · residual_reversion: hit-rate **0.502** (n=1133) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.825** (n=2038) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.81] cross-asset · 5 series ↑
- dow_jones [INDICES]: last 52449.45, z20 -2.89, zc -0.78, resid-z -0.24 [quiet], 1d -0.64%, |z20|=2.89
- brent [COMMODITIES]: last 101.49, z20 2.88, zc 1.95, resid-z 0.93 [moved], 1d 3.65%, 1-session move +3.65% ≥ 1.5%; |z20|=2.88
- wti [COMMODITIES]: last 96.50, z20 2.68, zc 1.82, resid-z 0.96 [moved], 1d 3.73%, 1-session move +3.73% ≥ 1.5%; |z20|=2.68
- russell_2000 [INDICES]: last 2923.32, z20 -2.04, zc -1.06, resid-z -1.28 [quiet], 1d -1.25%, |z20|=2.04
- vix [INDICES]: last 16.19, z20 1.81, zc 0.39, resid-z n/a [quiet], 1d 2.99%, |z20|=1.81
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-10-18 (z-distance 0.4).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.667 vs dow_jones, historically leads by 5d
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.545 vs brent, historically leads by 4d
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.521 vs brent, historically leads by 5d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.547 vs dow_jones
- Watch next: dyn_nvda (inverse) — not yet - watch; rho -0.517 vs vix
- Source: Uganda Launches New Crude Grade as First Oil Exports Near — OilPrice, 2026-09-09. https://oilprice.com/Energy/Crude-Oil/Uganda-Launches-New-Crude-Grade-as-First-Oil-Exports-Near.html
- Source: Surging crude oil prices: Rupee breaches 95/dollar mark — BusinessLine Mkts, 2026-09-09. https://www.thehindubusinessline.com/markets/forex/surging-crude-oil-prices-rupee-breaches-95dollar-mark/article71448030.ece
- Source: Oil at $100? Why you should always have energy stocks in your 401(k). — MarketWatch Top, 2026-09-09. https://www.marketwatch.com/story/oil-at-100-why-you-should-always-have-energy-stocks-in-your-401-k-b82798f1?mod=mw_rss_topstories
- Historical analogues: 2024-10-18 (d=0.4), 2025-10-21 (d=0.51), 2026-05-22 (d=0.54)

### [RED 7.16] cross-asset · 3 series ↓
- nifty_it [INDICES]: last 28913.95, z20 -3.84, zc -2.17, resid-z -1.37 [moved], 1d -3.24%, |z20|=3.84
- dyn_techm_ns [EQUITIES]: last 1508.00, z20 -3.80, zc -2.07, resid-z -1.51 [unexplained], 1d -3.27%, |z20|=3.80
- dyn_tataelxsi_ns [EQUITIES]: last 3383.00, z20 -3.40, zc -1.81, resid-z -1.00 [moved], 1d -3.12%, |z20|=3.40; 1y-pct=0
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.78).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tatatech_ns (rho 0.586 via nifty_it, z -1.39, reacted); nifty_50 (rho 0.507 via nifty_it, z -3.31, reacted)
- Watch next: shanghai_comp (inverse) — not yet - watch; rho -0.509 vs dyn_techm_ns, historically leads by 5d
- **India receivers**: dyn_tatatech_ns (rho 0.586, z -1.39); nifty_50 (rho 0.507, z -3.31)
- Source: IT stocks crash as Coforge, Infy, Tech Mahindra, HCL, TCS slide on H-1B visa fee hike — BusinessLine Mkts, 2026-09-09. https://www.thehindubusinessline.com/markets/it-stocks-crash-as-coforge-leads-selloff-infosys-tech-mahindra-hcl-tech-tcs-slide-h1-b-visa-in-focus/article71445708.ece
- Source: IT stocks crash as Coforge leads selloff; Infosys, Tech Mahindra, HCL Tech, TCS slide — BusinessLine Mkts, 2026-09-09. https://www.thehindubusinessline.com/markets/it-stocks-crash-as-coforge-leads-selloff-infosys-tech-mahindra-hcl-tech-tcs-slide/article71445708.ece
- Source: Tech Mahindra Share Price Live Updates: Tech Mahindra's Price Movement Analysis — ET Markets, 2026-09-09. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tech-mahindra-share-price-live-09-sep-2026/liveblog/133950510.cms
- Historical analogues: 2025-08-13 (d=0.78), 2025-01-23 (d=0.84), 2025-12-30 (d=0.85)

### [RED 6.97] cross-asset · 4 series ↓
- nifty_50 [INDICES]: last 23431.50, z20 -3.31, zc -1.64, resid-z -1.01 [moved], 1d -0.86%, |z20|=3.31
- india_vix [INDICES]: last 11.98, z20 2.51, zc 1.19, resid-z n/a [quiet], 1d 6.63%, |z20|=2.51
- nifty_midcap_100 [INDICES]: last 62592.20, z20 -2.37, zc -0.77, resid-z 0.31 [quiet], 1d -0.52%, |z20|=2.37
- dyn_jiofin_bo [EQUITIES]: last 231.00, z20 -1.88, zc -0.72, resid-z 0.66 [quiet], 1d -1.07%, 1y-pct=3
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-17 (z-distance 0.67).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.627 via nifty_50, z -1.87, reacted); dyn_indianb_ns (rho 0.563 via nifty_midcap_100, z -2.43, reacted); nifty_it (rho 0.507 via nifty_50, z -3.84, reacted); dyn_techm_ns (rho 0.465 via nifty_50, z -3.8, reacted); dyn_indusindbk_bo (rho 0.462 via nifty_50, z -0.15, quiet)
- **India receivers**: nifty_fmcg (rho 0.627, z -1.87); dyn_indianb_ns (rho 0.563, z -2.43); nifty_it (rho 0.507, z -3.84); dyn_techm_ns (rho 0.465, z -3.8)
- Source: Market wrap: Adani Ent, Max Healthcare, Infosys, HDFC Life among top gainers and losers on Nifty and Sensex on Wednesday — ET Markets, 2026-09-09. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-adani-ent-max-healthcare-infosys-hdfc-life-among-top-gainers-and-losers-on-nifty-and-sensex-on-wednesday/articleshow/133966457.cms
- Source: Sensex today | Stock Market Highlights: Sensex crashes 813 pts, Nifty closes at 23,431 as crude crosses $100 — BusinessLine Mkts, 2026-09-09. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-9th-september-2026/article71445394.ece
- Source: Stock Market prediction tomorrow: Sensex, Nifty outlook for Thu | Kospi, Taiwan Index, Nikkei cues to watch | 10 Sept — Mint Markets, 2026-09-09. https://www.livemint.com/market/stock-market-news/stock-market-prediction-tomorrow-sensex-nifty-outlook-for-thu-kospi-taiwan-index-nikkei-cues-to-watch-10-sept-11788948058132.html
- Historical analogues: 2025-07-17 (d=0.67), 2025-12-19 (d=1.13), 2024-11-07 (d=1.15)

### [RED 6.14] gold_silver_ratio ↓
- gold_silver_ratio [DERIVED]: last 65.38, z20 -3.14, zc n/a, resid-z n/a [quiet], 1d -1.35%, GSR<75 (extreme low); |z20|=3.14
- **Mechanism**: gold_silver_ratio ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.377 via gold_silver_ratio, z -2.37, reacted); dyn_adanient_bo (rho -0.36 via gold_silver_ratio, z 1.26, reacted)
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.828 vs gold_silver_ratio
- **India receivers**: nifty_midcap_100 (rho -0.377, z -2.37); dyn_adanient_bo (rho -0.36, z 1.26)
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

### [RED 5.71] comex_copper ↑
- comex_copper [COMMODITIES]: last 6.86, z20 3.71, zc 0.82, resid-z 1.64 [unexplained], 1d 1.78%, |z20|=3.71; 1y-pct=100; co-occur[metal_copper] suppressed: channel WEAK
- **Mechanism**: comex_copper ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.546 vs comex_copper, historically leads by 1d
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.6 vs comex_copper
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.519 vs comex_copper
- Source: Copper Hits Record Highs While Smelters Lose Money on Every Ton — OilPrice, 2026-09-09. https://oilprice.com/Metals/Commodities/Copper-Hits-Record-Highs-While-Smelters-Lose-Money-on-Every-Ton.html
- Source: Copper prices likely to remain elevated till US President Donald Trump decides on tariffs — BusinessLine Mkts, 2026-09-09. https://www.thehindubusinessline.com/markets/commodities/copper-prices-likely-to-remain-elevated-till-us-president-donald-trump-decides-on-tariffs/article71447123.ece
- Source: Copper Surges Above $14,500 as Supply Squeeze Deepens — OilPrice, 2026-09-08. https://oilprice.com/Metals/Commodities/Copper-Surges-Above-14500-as-Supply-Squeeze-Deepens.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-15 (d=0.01), 2025-08-28 (d=0.02)

### [RED 5.54] dyn_meta ↑
- dyn_meta [EQUITIES]: last 655.07, z20 3.54, zc 2.97, resid-z 0.39 [moved], 1d 6.78%, |z20|=3.54
- **Mechanism**: dyn_meta ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.378 via dyn_meta, z -2.37, reacted); dyn_indianb_ns (rho 0.351 via dyn_meta, z -2.43, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.378, z -2.37); dyn_indianb_ns (rho 0.351, z -2.43)
- Source: US stocks fall as oil surges past $100 on deepening Middle East tensions, Meta jumps 5.5%, AMD gains 3.49% — Mint Markets, 2026-09-09. https://www.livemint.com/market/us-stocks-fall-as-oil-surges-past-100-on-deepening-middle-east-tensions-11788961419384.html
- Source: Meta’s stock jumps as new personal AI agent Muse addresses a major investor concern — MarketWatch Top, 2026-09-09. https://www.marketwatch.com/story/meta-stock-jumps-as-new-personal-ai-agent-muse-addresses-a-major-investor-concern-5ad0a373?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2024-10-21 (d=0.07)

### [RED 5.5] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.67, z20 2.50, zc n/a, resid-z n/a [quiet], 1d 0.35%, 52-wk extreme (pct=100); |z20|=2.50; 1y-pct=100
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.44 via midcap_largecap_ratio, z -2.37, reacted); nifty_50 (rho -0.433 via midcap_largecap_ratio, z -3.31, reacted); nifty_fmcg (rho -0.426 via midcap_largecap_ratio, z -1.87, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.44, z -2.37); nifty_50 (rho -0.433, z -3.31); nifty_fmcg (rho -0.426, z -1.87)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 5.46] dyn_hdb ↓
- dyn_hdb [EQUITIES]: last 22.08, z20 -3.46, zc -1.23, resid-z -0.32 [quiet], 1d -1.76%, |z20|=3.46; 1y-pct=0
- **Mechanism**: dyn_hdb ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.607 via dyn_hdb, z -3.31, reacted); nifty_it (rho 0.531 via dyn_hdb, z -3.84, reacted); dyn_techm_ns (rho 0.462 via dyn_hdb, z -3.8, reacted); dyn_jiofin_bo (rho 0.391 via dyn_hdb, z -1.88, reacted); dyn_bharatcoal_ns (rho 0.383 via dyn_hdb, z -0.1, quiet)
- **India receivers**: nifty_50 (rho 0.607, z -3.31); nifty_it (rho 0.531, z -3.84); dyn_techm_ns (rho 0.462, z -3.8); dyn_jiofin_bo (rho 0.391, z -1.88)
- Source: HDFC Bank shares fall 2% to fresh 52-week low; here’s why — BusinessLine Mkts, 2026-09-09. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-fall-2-to-fresh-52-week-low-heres-why/article71446043.ece
- Source: HDFC Bank shares trade flat as MCLR cut, gold loan growth in focus — BusinessLine Mkts, 2026-09-08. https://www.thehindubusinessline.com/markets/hdfc-bank-shares-trade-flat-as-mclr-cut-gold-loan-growth-remain-in-focus/article71441333.ece
- Source: HDFC Bank Share Price Live Updates: HDFC Bank's Performance Overview — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/hdfc-bank-stock-price-livestock-price-today-live-updates-08-sep-2026/liveblog/133905624.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

## Watchlist (below surfacing floor)
dyn_coalindia_ns ↑ (5.41), cross-asset · 3 series ↑ (5.29), usd_jpy ↓ (5.21), indices · 4 series ↓ (5.07), dyn_qcom ↑ (4.9), dyn_pcjeweller_ns ↑ (4.66), dyn_indianb_ns ↓ (4.43), dyn_lth ↓ (4.05), dyn_icicigi_bo ↓ (3.96), dyn_lenskart_ns ↑ (3.53), usd_cny ↓ (2.8), wheat ↑ (2.63)

## India macro
- nifty_50: 23431.5000 (1d -0.86%, z20 -3.31, flag red)
- nifty_midcap_100: 62592.1992 (1d -0.52%, z20 -2.37, flag amber)
- usd_inr: 95.1300 (1d 0.68%, z20 -0.08, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6713 (1d 0.35%, z20 2.50, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · India CPI T-5d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 82.6 — "Top stocks in focus today: Investors must watch Coal India, Shakti Pumps, Wipro shares on "
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 79.3 — "Top stocks in focus today: Investors must watch Coal India, Shakti Pumps, Wipro shares on "
- COALINDIA.NS (COAL INDIA LTD) score 79.1 — "Top stocks in focus today: Investors must watch Coal India, Shakti Pumps, Wipro shares on "
- INDIANB.NS (INDIAN BANK) score 59.8 — "US MORTGAGE DEMAND FALLS AS RATES HIT 6.85% US mortgage applications fell 2.7% last week, "
- BAC (Bank of America Corporation) score 54.4 — "TRUMP’S WEDNESDAY CALENDAR 11:00 AM — Intelligence briefing, White House Afternoon — Trave"
- COIN (Coinbase Global, Inc.) score 50.3 — "PIMCO: HIGH BOND YIELDS CHALLENGE STOCKS PIMCO says bonds are becoming more attractive aft"
- HDB (HDFC Bank Limited) score 49.4 — "US MORTGAGE DEMAND FALLS AS RATES HIT 6.85% US mortgage applications fell 2.7% last week, "
- IDBI.NS (IDBI BANK LIMITED) score 44.6 — "US MORTGAGE DEMAND FALLS AS RATES HIT 6.85% US mortgage applications fell 2.7% last week, "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 44.6 — "US MORTGAGE DEMAND FALLS AS RATES HIT 6.85% US mortgage applications fell 2.7% last week, "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 44.6 — "US MORTGAGE DEMAND FALLS AS RATES HIT 6.85% US mortgage applications fell 2.7% last week, "
- TECHM.NS (TECH MAHINDRA LIMITED) score 42.9 — "Graphite India rallies 15%, HEG surges as GrafTech announces 30% price hike"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 42.8 — "Graphite India rallies 15%, HEG surges as GrafTech announces 30% price hike"
- TECH (Bio-Techne Corp) score 42.8 — "Graphite India rallies 15%, HEG surges as GrafTech announces 30% price hike"
- OHI (Omega Healthcare Investors, In) score 42.5 — "Top stocks in focus today: Investors must watch Coal India, Shakti Pumps, Wipro shares on "
- BOND (PIMCO Active Bond Exchange-Tra) score 39.0 — "PIMCO: HIGH BOND YIELDS CHALLENGE STOCKS PIMCO says bonds are becoming more attractive aft"
- CHKP (Check Point Software Technolog) score 35.3 — "₹60 per share dividend alert! Check last date to buy - Record date soon; check payment tim"
- 301077.SZ (CHINASTARS) score 27.6 — "GBA integration may help mainland China’s philanthropy sector learn from Hong Kong"
- LTH (Life Time Group Holdings, Inc.) score 24.9 — "IRAN EXPANDS MARITIME RESTRICTED ZONE Iran’s Revolutionary Guards said a new maritime rest"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 23.2 — "Oil at $100? Why you should always have energy stocks in your 401(k)."
- PCJEWELLER.NS (PC JEWELLER LTD) score 12.2 — "PC Jeweller shares jump 4%, surge 38% in one week. What's polishing the stock's shine?"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 11.6 — "Market wrap: Adani Ent, Max Healthcare, Infosys, HDFC Life among top gainers and losers on"
- MS (Morgan Stanley) score 10.5 — "MORGAN STANLEY SEES OIL TRADERS CUTTING LONG-TERM RISK Oil traders are reducing longer-ter"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 9.1 — "Stocks to Watch, Sep 7: 3 Tata group cos, 4 Railway stocks, 2 shipping sector, 3 Pharma ma"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.9 — "Multibagger Stocks: 14 microcaps surged up to 355% in just 6 months"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 8.6 — "Kenya withdraws Tata Group’s century-old soda ash mining concession"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 8.6 — "Kenya withdraws Tata Group’s century-old soda ash mining concession"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 8.2 — "‘We fear financial exploitation’: Who will manage our finances if my wife and I become inc"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.9 — "ICICI Prudential AMC gets RBI approval to buy up to 9.95% stake in Kotak and 3 other banks"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 7.4 — "Top stocks in focus today: Investors must watch Coal India, Shakti Pumps, Wipro shares on "
- META (Meta) score 7.2 — "US stocks fall as oil surges past $100 on deepening Middle East tensions, Meta jumps 5.5%,"
- JIOFIN.BO (Jio Financial Services Limited) score 6.0 — "‘We fear financial exploitation’: Who will manage our finances if my wife and I become inc"
- VT (Vanguard Total World Stock Ind) score 5.2 — "Uganda Set to Become World's Newest Oil Exporter in Early 2027"
- NVDA (NVIDIA Corporation) score 5.1 — "NVDA - NVIDIA: NEEDHAM STAYS BULLISH AFTER $12.9B HUGGING FACE DEAL Needham reiterated its"
- IFCI.NS (IFCI LTD) score 4.3 — "IFCI share price down today- drops 14% in 2 days- Why is the stock falling?"
- QCOM (QUALCOMM Incorporated) score 3.3 — "Qualcomm-Amazon AI deal: Why the chipmaker’s stock surged"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 1.4 — "Lenskart Solutions among 4 stocks to hit 52-week highs & rallied up to 22% in a month"
- DELL (Dell Technologies Inc.) score 1.2 — "Dell’s AI Boom: $95 billion backlog reshapes growth outlook"
- DKS (Dick's Sporting Goods Inc) score 0.2 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- MRNA (Moderna, Inc.) score 0.1 — "Can Wolfe’s upgrade push Moderna stock higher?"
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