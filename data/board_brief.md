# Transmission Layer — board brief · 2026-09-10 19:08Z

data as of **2026-09-10** · 98 series · 16 red / 37 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.661, 1d in regime; vol-pct 0.557, breadth-off 0.765, Markov P(high-vol) 0.021)
- [INVERTED] **safe_haven_gold** — corr20 -0.45, corr60 -0.33, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.81, corr60 0.85, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.14, corr60 0.28, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.29, corr60 0.15, last shift 2026-06-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.83, corr60 -0.85, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.09, corr60 -0.02, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.35, corr60 -0.17, last shift 2026-06-29. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.14, corr60 0.09, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** dyn_jef → nikkei_225: leads 1d (ccf 0.397, β 0.2333, p 0.0); driver zc -1.53 → expected -0.752%. Type hit-rate 0.819 (n=2095).
- **SETUP** dyn_bond → eur_usd: leads 1d (ccf 0.253, β 0.3659, p 4e-05); driver zc -2.56 → expected -0.3%. Type hit-rate 0.819 (n=2095).
- Track record · residual_reversion: hit-rate **0.496** (n=1124) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.819** (n=2095) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 11.14] cross-asset · 7 series ↓
- vix [INDICES]: last 17.68, z20 3.81, zc 0.95, resid-z n/a [quiet], 1d 7.41%, |z20|=3.81
- brent [COMMODITIES]: last 106.94, z20 3.81, zc 2.51, resid-z 1.59 [unexplained], 1d 5.66%, 1-session move +5.66% ≥ 1.5%; |z20|=3.81
- dow_jones [INDICES]: last 51996.74, z20 -3.48, zc -0.89, resid-z 0.51 [quiet], 1d -0.73%, |z20|=3.48
- wti [COMMODITIES]: last 101.68, z20 3.46, zc 2.58, resid-z 1.66 [unexplained], 1d 5.86%, 1-session move +5.86% ≥ 1.5%; |z20|=3.46
- dyn_vt [EQUITIES]: last 158.46, z20 -2.95, zc -1.18, resid-z 1.64 [unexplained], 1d -0.89%, |z20|=2.95
- russell_2000 [INDICES]: last 2890.26, z20 -2.53, zc -0.87, resid-z -0.44 [quiet], 1d -1.06%, |z20|=2.53
- sp500 [INDICES]: last 7589.35, z20 -2.37, zc -0.82, resid-z -0.56 [quiet], 1d -0.62%, |z20|=2.37
- **Mechanism**: cross-asset · 7 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-21 (z-distance 0.44).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_ms (inverse) — not yet - watch; rho -0.552 vs vix, historically leads by 5d
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.538 vs brent, historically leads by 4d
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.516 vs brent, historically leads by 5d
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.514 vs dyn_vt, historically leads by 1d
- Watch next: dyn_nvda (inverse) — not yet - watch; rho -0.534 vs vix
- Source: EIA Raises 2027 U.S. Oil Output Forecast — OilPrice, 2026-09-10. https://oilprice.com/Latest-Energy-News/World-News/EIA-Raises-2027-US-Oil-Output-Forecast.html
- Source: US bond yields climb to multi-year highs as oil surge revives bets on higher Fed rates — ET Markets, 2026-09-10. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-bond-yields-climb-as-oil-surge-revives-bets-on-higher-fed-rates/articleshow/134023668.cms
- Source: Oil surges 5%, Brent and US crude both over $100 on more tanker attacks — ET Markets, 2026-09-10. https://economictimes.indiatimes.com/markets/commodities/news/oil-surges-5-brent-and-us-crude-both-over-100-on-more-tanker-attacks/articleshow/134023313.cms
- Historical analogues: 2025-10-21 (d=0.44), 2026-05-22 (d=0.46), 2024-10-18 (d=0.51)

### [RED 7.24] cross-asset · 4 series ↑
- dyn_bond [EQUITIES]: last 88.99, z20 -3.58, zc -2.56, resid-z 0.59 [priced], 1d -0.82%, |z20|=3.58; 1y-pct=0
- ust_10y [RATES]: last 4.80, z20 1.88, zc 0.22, resid-z -0.18 [quiet], 1d 0.42%, |z20|=1.88; 1y-pct=100
- ust_2y [RATES]: last 4.39, z20 1.80, zc 0.54, resid-z 0.16 [quiet], 1d 0.46%, |z20|=1.80; 1y-pct=99
- ust_30y [RATES]: last 5.25, z20 0.37, zc -0.25, resid-z -0.54 [quiet], 1d 0.19%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.354 via ust_2y, z 1.07, reacted)
- Watch next: tips_10y_real (inverse) — not yet - watch; rho -0.738 vs dyn_bond
- Watch next: dxy (inverse) — not yet - watch; rho -0.523 vs dyn_bond
- **India receivers**: midcap_largecap_ratio (rho -0.354, z 1.07)
- Source: Treasury yields surge after poor 30-year auction and new buyback operation fail to calm market — MarketWatch Top, 2026-09-10. https://www.marketwatch.com/story/treasury-yields-surge-toward-the-danger-zone-for-stocks-as-inflation-pressures-heat-up-fe0f9aa6?mod=mw_rss_topstories
- Source: OBPPs pitch investor protection mechanism for retail bond investors — BusinessLine Mkts, 2026-09-10. https://www.thehindubusinessline.com/markets/obpps-pitch-investor-protection-mechanism-for-retail-bond-investors/article71453206.ece
- Source: US bond yields climb to multi-year highs as oil surge revives bets on higher Fed rates — ET Markets, 2026-09-10. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-bond-yields-climb-as-oil-surge-revives-bets-on-higher-fed-rates/articleshow/134023668.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-11 (d=0.3), 2025-05-08 (d=0.36)

### [RED 6.19] cross-asset · 3 series ↓
- nifty_it [INDICES]: last 28890.90, z20 -2.87, zc -0.05, resid-z -0.23 [quiet], 1d -0.08%, |z20|=2.87
- dyn_tataelxsi_ns [EQUITIES]: last 3409.00, z20 -2.33, zc 0.43, resid-z 0.66 [quiet], 1d 0.77%, |z20|=2.33; 1y-pct=1
- dyn_techm_ns [EQUITIES]: last 1525.80, z20 -2.23, zc 0.71, resid-z 0.52 [quiet], 1d 1.18%, |z20|=2.23
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
- nifty_midcap_100 [INDICES]: last 62360.45, z20 -2.48, zc -0.55, resid-z -0.98 [quiet], 1d -0.37%, |z20|=2.48
- nifty_50 [INDICES]: last 23477.80, z20 -2.43, zc 0.35, resid-z 0.79 [quiet], 1d 0.20%, |z20|=2.43
- dyn_jiofin_bo [EQUITIES]: last 231.15, z20 -1.73, zc 0.04, resid-z -0.39 [quiet], 1d 0.06%, 1y-pct=4
- india_vix [INDICES]: last 11.74, z20 1.59, zc -0.27, resid-z n/a [quiet], 1d -1.53%, |z20|=1.59
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-17 (z-distance 0.67).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.624 via nifty_50, z -1.78, reacted); dyn_indianb_ns (rho 0.556 via nifty_midcap_100, z -2.1, reacted); nifty_it (rho 0.512 via nifty_50, z -2.87, reacted); dyn_techm_ns (rho 0.483 via nifty_50, z -2.23, reacted); dyn_indusindbk_bo (rho 0.462 via nifty_50, z -0.62, quiet)
- **India receivers**: nifty_fmcg (rho 0.624, z -1.78); dyn_indianb_ns (rho 0.556, z -2.1); nifty_it (rho 0.512, z -2.87); dyn_techm_ns (rho 0.483, z -2.23)
- Source: 'Buy' Nephrocare Health Services for 16% upside, says ICICI Securities; check share price target — Mint Markets, 2026-09-10. https://www.livemint.com/market/stock-market-news/buy-nephrocare-health-services-for-16-upside-says-icici-securities-check-share-price-target-11789044057519.html
- Source: CAS stays, but derivatives settlement may change, says Sebi chief Tuhin Kanta Pandey after another 1,000-point Sensex swing — ET Markets, 2026-09-10. https://economictimes.indiatimes.com/markets/stocks/news/cas-stays-but-derivatives-settlement-may-change-says-sebi-chief-tuhin-kanta-pandey-after-another-1000-point-sensex-swing/articleshow/134006996.cms
- Source: SPCX - UK DEEPENS SPACEX RELIANCE WITH $40 MILLION SATELLITE SPEND Britain has spent nearly $40 million on SpaceX satellite services, becoming the first country outside the U.S. to publicly acknowledge adopting Starshield. The UK military operates roughly 1,000 Starshield and 500 Starlink terminals, — DeItaone, 2026-09-10. https://t.me/walter_bloomberg/35581
- Historical analogues: 2025-07-17 (d=0.67), 2025-12-19 (d=1.13), 2024-11-07 (d=1.15)

### [RED 5.41] dyn_hdb ↓
- dyn_hdb [EQUITIES]: last 21.78, z20 -3.41, zc -0.94, resid-z -0.32 [quiet], 1d -1.36%, |z20|=3.41; 1y-pct=0
- **Mechanism**: dyn_hdb ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.595 via dyn_hdb, z -2.43, reacted); nifty_it (rho 0.524 via dyn_hdb, z -2.87, reacted); dyn_techm_ns (rho 0.435 via dyn_hdb, z -2.23, reacted); dyn_jiofin_bo (rho 0.388 via dyn_hdb, z -1.73, reacted); dyn_bharatcoal_ns (rho 0.381 via dyn_hdb, z -0.87, quiet)
- **India receivers**: nifty_50 (rho 0.595, z -2.43); nifty_it (rho 0.524, z -2.87); dyn_techm_ns (rho 0.435, z -2.23); dyn_jiofin_bo (rho 0.388, z -1.73)
- Source: HDFC Bank shares rebound from fresh 52-week low: What is driving the stock? — BusinessLine Mkts, 2026-09-10. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-hit-fresh-52-week-low-for-second-straight-day-what-is-driving-the-stock/article71450256.ece
- Source: HDFC Bank shares fall 2% to fresh 52-week low; here’s why — BusinessLine Mkts, 2026-09-09. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-fall-2-to-fresh-52-week-low-heres-why/article71446043.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [AMBER 5.16] commodities · 3 series ↑
- soybeans [COMMODITIES]: last 1331.75, z20 1.84, zc 2.73, resid-z 2.41 [unexplained], 1d 2.82%, |z20|=1.84; 1y-pct=100
- corn [COMMODITIES]: last 533.50, z20 1.71, zc 4.00, resid-z 3.22 [unexplained], 1d 5.07%, |z20|=1.71; 1y-pct=100
- wheat [COMMODITIES]: last 741.50, z20 0.93, zc 1.94, resid-z 1.89 [unexplained], 1d 4.25%, 1y-pct=98
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Wheat falls amid profit-taking, Black Sea war headlines — Mint Markets, 2026-09-09. https://www.livemint.com/market/wheat-falls-amid-profit-taking-black-sea-war-headlines-11788979794916.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [RED 5.01] indices · 4 series ↓
- dax [INDICES]: last 25399.61, z20 -3.34, zc -0.69, resid-z -0.02 [quiet], 1d -0.69%, |z20|=3.34
- ftse_100 [INDICES]: last 10611.46, z20 -3.32, zc -0.63, resid-z -0.18 [quiet], 1d -0.55%, |z20|=3.32
- stoxx_50 [INDICES]: last 6277.25, z20 -2.71, zc -0.57, resid-z 0.19 [quiet], 1d -0.54%, |z20|=2.71
- cac_40 [INDICES]: last 8121.29, z20 -2.24, zc -0.40, resid-z 0.61 [quiet], 1d -0.43%, |z20|=2.24
- **Mechanism**: indices · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.5 via ftse_100, z -2.87, reacted); nifty_midcap_100 (rho 0.488 via dax, z -2.48, reacted); dyn_techm_ns (rho 0.401 via ftse_100, z -2.23, reacted); nifty_50 (rho 0.395 via ftse_100, z -2.43, reacted); dyn_indusindbk_bo (rho 0.359 via ftse_100, z -0.62, quiet)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.555 vs stoxx_50, historically leads by 1d
- Watch next: dyn_jef (co-move) — not yet - watch; rho 0.582 vs dax
- **India receivers**: nifty_it (rho 0.5, z -2.87); nifty_midcap_100 (rho 0.488, z -2.48); dyn_techm_ns (rho 0.401, z -2.23); nifty_50 (rho 0.395, z -2.43)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-16 (d=0.34), 2024-10-24 (d=0.48)

### [RED 4.81] dyn_qcom ↑
- dyn_qcom [EQUITIES]: last 178.48, z20 2.81, zc 0.57, resid-z 0.37 [quiet], 1d 1.18%, |z20|=2.81
- **Mechanism**: dyn_qcom ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: aud_usd (inverse) — not yet - watch; rho -0.314 vs dyn_qcom, historically leads by 1d
- Source: Qualcomm-Amazon AI deal: Why the chipmaker’s stock surged — ET Markets, 2026-09-09. https://economictimes.indiatimes.com/markets/us-stocks/news/qualcomm-amazon-ai-deal-why-the-chipmakers-stock-surged/slideshow/133955258.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.02), 2026-05-04 (d=0.1)

## Watchlist (below surfacing floor)
dyn_coalindia_ns ↑ (4.72), hang_seng ↓ (4.7), dyn_meta ↑ (4.4), dyn_lth ↓ (4.3), gold_silver_ratio ↑ (4.19), usd_jpy ↓ (4.12), dyn_indianb_ns ↓ (4.1), dyn_pcjeweller_ns ↑ (4.1), midcap_largecap_ratio ↑ (4.07), dyn_icicigi_bo ↓ (3.96), asx_200 ↓ (3.47), dyn_atherenerg_ns ↑ (3.22)

## India macro
- nifty_50: 23477.8008 (1d 0.20%, z20 -2.43, flag amber)
- nifty_midcap_100: 62360.4492 (1d -0.37%, z20 -2.48, flag amber)
- usd_inr: 95.4400 (1d 0.65%, z20 0.49, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6561 (1d -0.57%, z20 1.07, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · India CPI T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 87.1 — "India’s CAS liquidity concerns not unique, says Sebi chief"
- COALINDIA.NS (COAL INDIA LTD) score 84.4 — "IEA: Global Coal Demand Set to Hit Record High as Iran War Chokes LNG Supply"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 83.5 — "India’s CAS liquidity concerns not unique, says Sebi chief"
- COIN (Coinbase Global, Inc.) score 57.7 — "HOUTHIS CLOSE IN ON KEY RED SEA CHOKEPOINT Iran-aligned Houthis have seized Yemen’s port c"
- INDIANB.NS (INDIAN BANK) score 55.9 — "META - JPMORGAN TURNS BULLISH ON META’S AI POTENTIAL JPMorgan upgraded Meta to Overweight "
- OHI (Omega Healthcare Investors, In) score 52.7 — "Top stocks in focus today: Investors must watch Fino Payments, KIMS, Texmaco Rail shares o"
- BAC (Bank of America Corporation) score 51.9 — "WHITE HOUSE: WILL ISSUE $500 OBAMACARE REFUNDS TO NEARLY 1 MILLION AMERICANS"
- HDB (HDFC Bank Limited) score 44.9 — "META - JPMORGAN TURNS BULLISH ON META’S AI POTENTIAL JPMorgan upgraded Meta to Overweight "
- CHKP (Check Point Software Technolog) score 44.6 — "Why $500 checks won’t help Americans facing 15% increases in Obamacare premiums next year"
- BOND (PIMCO Active Bond Exchange-Tra) score 43.4 — "WALL STREET SEES 5% TREASURY YIELD RISK A Reuters poll found 17 of 31 bond strategists see"
- IDBI.NS (IDBI BANK LIMITED) score 40.1 — "META - JPMORGAN TURNS BULLISH ON META’S AI POTENTIAL JPMorgan upgraded Meta to Overweight "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 40.1 — "META - JPMORGAN TURNS BULLISH ON META’S AI POTENTIAL JPMorgan upgraded Meta to Overweight "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 40.1 — "META - JPMORGAN TURNS BULLISH ON META’S AI POTENTIAL JPMorgan upgraded Meta to Overweight "
- TECHM.NS (TECH MAHINDRA LIMITED) score 36.8 — "Market wrap:  HDFC Life, Power Grid, HCL Tech, Hindalco top gainers and losers on Nifty an"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 36.7 — "Market wrap:  HDFC Life, Power Grid, HCL Tech, Hindalco top gainers and losers on Nifty an"
- TECH (Bio-Techne Corp) score 36.7 — "Market wrap:  HDFC Life, Power Grid, HCL Tech, Hindalco top gainers and losers on Nifty an"
- LTH (Life Time Group Holdings, Inc.) score 29.1 — "PRESIDENT TRUMP — THURSDAY SCHEDULE 8:00 AM CT — Executive Time — Dallas 12:00 PM CT — Tou"
- 301077.SZ (CHINASTARS) score 27.3 — "25 dead after fire on board foreign-flagged cargo ship in China’s Qingdao"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 24.9 — "US, IRAN PREPARE FOR PROTRACTED WAR Iran and the U.S. are reportedly preparing for a poten"
- JUSTDIAL.BO (JUST DIAL LTD.) score 15.2 — "The likelihood of a Fed interest rate hike next week just got a lot higher"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 14.8 — "Adani Ports executives settle SEBI proceedings in PMC projects case"
- MS (Morgan Stanley) score 12.1 — "AAPL - MORGAN STANLEY SEES “APPLE AI” BULL CASE STRENGTHENING Morgan Stanley analyst Erik "
- PCJEWELLER.NS (PC JEWELLER LTD) score 10.6 — "PC Jeweller share price shines for second session | What's behind the rally?"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 10.2 — "OBPPs pitch investor protection fund for retail bond investors"
- JIOFIN.BO (Jio Financial Services Limited) score 9.6 — "SPCX - UK DEEPENS SPACEX RELIANCE WITH $40 MILLION SATELLITE SPEND Britain has spent nearl"
- SEPN (Septerna, Inc.) score 8.7 — "Stock Market prediction today: Sensex, Nifty outlook for Friday | Kospi, Taiwan Index, Nik"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 8.6 — "This Tata Group stock surges 10% today amid a spurt in volume despite a weak stock market "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 8.6 — "This Tata Group stock surges 10% today amid a spurt in volume despite a weak stock market "
- META (Meta) score 8.5 — "META - JPMORGAN TURNS BULLISH ON META’S AI POTENTIAL JPMorgan upgraded Meta to Overweight "
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.4 — "Running the numbers on Trump’s $5,000 dividend proposal, from its cost to the impact on av"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.2 — "'Buy' Nephrocare Health Services for 16% upside, says ICICI Securities; check share price "
- NVDA (NVIDIA Corporation) score 6.9 — "Why are big chip stocks under pressure? SK Hynix, AMD, Intel, Nvidia fall up to 6.5%; is t"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 6.9 — "IEA: Global Coal Demand Set to Hit Record High as Iran War Chokes LNG Supply"
- VT (Vanguard Total World Stock Ind) score 5.0 — "NSE slashes IPO ambitions as world’s biggest options boom fades"
- JEF (Jefferies Financial Group Inc.) score 4.5 — "Vodafone Idea shares price in focus as Jefferies initiates coverage with Buy rating. Why a"
- QCOM (QUALCOMM Incorporated) score 2.6 — "Qualcomm-Amazon AI deal: Why the chipmaker’s stock surged"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 1.1 — "Lenskart Solutions among 4 stocks to hit 52-week highs & rallied up to 22% in a month"
- DELL (Dell Technologies Inc.) score 0.9 — "Dell’s AI Boom: $95 billion backlog reshapes growth outlook"
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