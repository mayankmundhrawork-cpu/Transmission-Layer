# Transmission Layer — board brief · 2026-10-08 11:20Z

data as of **2026-10-08** · 97 series · 17 red / 36 amber · 8 events surfaced (32 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.772, 4d in regime; vol-pct 0.711, breadth-off 0.833, Markov P(high-vol) 0.014)
- [INVERTED] **safe_haven_gold** — corr20 -0.36, corr60 -0.42, contra nifty_50 corr20=0.1, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.8, corr60 0.85, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.06, corr60 0.15, last shift 2026-07-10. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.12, corr60 0.13, last shift 2026-08-25. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.77, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [INVERTED] **dxy_inr_channel** — corr20 -0.25, corr60 -0.1, last shift 2026-08-11. Channel: broad dollar strength -> EM FX weakness incl INR
- [VALID] **real_rates_gold_inverse** — corr20 -0.33, corr60 -0.27, last shift 2026-08-11. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.54, corr60 0.19, last shift 2026-07-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.496** (n=1139) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.828** (n=2141) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.13] cross-asset · 2 series ↑
- gold_silver_ratio [DERIVED]: last 70.30, z20 2.30, zc n/a, resid-z n/a [quiet], 1d 1.70%, GSR<75 (extreme low); |z20|=2.30
- comex_silver [COMMODITIES]: last 58.88, z20 -1.91, zc -0.96, resid-z -1.28 [quiet], 1d -1.71%, |z20|=1.91
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.378 via gold_silver_ratio, z -2.07, reacted)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.561 vs comex_silver, historically leads by 1d
- Watch next: dyn_coin (co-move) — not yet - watch; rho 0.505 vs comex_silver, historically leads by 4d
- Watch next: btc_usd (co-move) — not yet - watch; rho 0.559 vs comex_silver
- **India receivers**: midcap_largecap_ratio (rho -0.378, z -2.07)
- Source: Gold prices near Rs 1.5 lakh/10 grams; silver rises as dollar eases from multi-month high. What lies ahead? — ET Markets, 2026-10-08. https://economictimes.indiatimes.com/markets/commodities/news/gold-prices-near-rs-1-5-lakh/10-grams-silver-rises-as-dollar-eases-from-multi-month-high-what-lies-ahead/articleshow/134779724.cms
- Source: Gold prices dip Rs 1,500/10 grams; silver down Rs 1,600/kg ahead of Fed minutes. Key levels to track — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/commodities/news/gold-prices-dip-rs-1500/10-grams-silver-down-rs-1600/kg-ahead-of-fed-minutes-key-levels-to-track/articleshow/134755973.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-29 (d=0.06), 2025-08-12 (d=0.14)

### [AMBER 7.84] cross-asset · 6 series ↑
- ust_30y [RATES]: last 5.64, z20 1.56, zc -0.44, resid-z -0.33 [quiet], 1d -0.35%, |z20|=1.56; 1y-pct=99
- dyn_bond [EQUITIES]: last 86.57, z20 -1.43, zc -0.25, resid-z 0.02 [quiet], 1d -0.09%, 1y-pct=1
- ust_10y [RATES]: last 5.27, z20 1.26, zc -0.72, resid-z -0.60 [quiet], 1d -0.75%, 1y-pct=98
- tips_10y_real [RATES]: last 2.91, z20 1.18, zc -0.69, resid-z -0.53 [quiet], 1d -1.36%, 1y-pct=98
- brent [COMMODITIES]: last 105.37, z20 0.69, zc 2.84, resid-z -0.42 [priced], 1d 5.16%, 1-session move +5.16% ≥ 1.5%; co-occur[inr_oil] suppressed: channel WEAK
- ust_2y [RATES]: last 4.79, z20 0.41, zc -0.77, resid-z -0.49 [quiet], 1d -1.03%, 1y-pct=96
- **Mechanism**: cross-asset · 6 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: wti (co-move) — not yet - watch; rho 0.504 vs ust_30y, historically leads by 3d
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.53 vs ust_30y
- Watch next: vix (co-move) — not yet - watch; rho 0.521 vs brent
- Source: India cuts back on costly Russian crude as West Asia flows recover — BusinessLine Mkts, 2026-10-08. https://www.thehindubusinessline.com/markets/commodities/india-shuns-costly-russian-crude-as-west-asia-flows-recover/article71558804.ece
- Source: Oil Jumps 5% as Iran Steps Up Attacks on Hormuz Tankers — OilPrice, 2026-10-08. https://oilprice.com/Latest-Energy-News/World-News/Oil-Jumps-2-as-Iran-Steps-Up-Attacks-on-Hormuz-Tankers.html
- Source: India's Inflation Likely Hit 5.4% in September as Oil Costs Bite — OilPrice, 2026-10-08. https://oilprice.com/Latest-Energy-News/World-News/Indias-Inflation-Likely-Hit-54-in-September-as-Oil-Costs-Bite.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.35), 2026-05-14 (d=0.69)

### [RED 7.54] usd_inr ↑
- usd_inr [FX]: last 96.78, z20 2.54, zc 0.82, resid-z 0.63 [quiet], 1d 0.43%, 20d range extreme; |z20|=2.54; 1y-pct=99; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.413 via usd_inr, z -0.44, quiet); dyn_karurvysya_ns (rho -0.377 via usd_inr, z 0.57, quiet)
- **India receivers**: dyn_idbi_ns (rho -0.413, z -0.44); dyn_karurvysya_ns (rho -0.377, z 0.57)
- Source: RBI intervention halts rupee's slide to record low, risks linger — ET Markets, 2026-10-08. https://economictimes.indiatimes.com/markets/forex/rbi-intervention-halts-rupees-slide-to-record-low-risks-linger/articleshow/134788012.cms
- Source: Rupee falls 13 paise to close at 96.88 against US dollar — BusinessLine Mkts, 2026-10-08. https://www.thehindubusinessline.com/markets/forex/rupee-falls-13-paise-to-close-at-9688-against-us-dollar/article71559337.ece
- Source: INR vs USD: Rupee near 97/dollar; how TCS, Sun Pharma, Tata Steel, SRF may gain from weaker currency? Experts explain — Mint Markets, 2026-10-08. https://www.livemint.com/market/stock-market-news/inr-vs-usd-rupee-near-97-dollar-how-tcs-sun-pharma-tata-steel-srf-may-gain-from-weaker-currency-experts-explain-11791449213491.html
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2025-09-16 (d=0.01)

### [AMBER 6.31] cross-asset · 5 series ↓
- nifty_50 [INDICES]: last 22231.80, z20 -2.38, zc -2.29, resid-z -1.16 [moved], 1d -1.64%, |z20|=2.38; 1y-pct=0
- nifty_fmcg [INDICES]: last 43898.40, z20 -2.35, zc -2.25, resid-z -0.90 [priced], 1d -2.02%, |z20|=2.35; 1y-pct=0
- nifty_midcap_100 [INDICES]: last 57880.45, z20 -2.34, zc -2.65, resid-z -2.05 [unexplained], 1d -2.52%, |z20|=2.34
- india_vix [INDICES]: last 15.24, z20 2.19, zc 1.64, resid-z n/a [moved], 1d 9.74%, |z20|=2.19
- dyn_policybzr_ns [EQUITIES]: last 996.00, z20 -1.18, zc -1.16, resid-z 0.64 [quiet], 1d -4.23%, 1y-pct=1
- **Mechanism**: cross-asset · 5 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.6).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.64 via nifty_midcap_100, z -2.07, reacted); nifty_metal (rho 0.623 via nifty_midcap_100, z -3.61, reacted); dyn_jiofin_bo (rho 0.589 via nifty_50, z -1.94, reacted); dyn_indusindbk_bo (rho 0.546 via nifty_midcap_100, z -1.77, reacted); dyn_bajfinance_ns (rho -0.539 via india_vix, z -1.3, reacted)
- Watch next: ig_oas (inverse) — not yet - watch; rho -0.502 vs dyn_policybzr_ns
- **India receivers**: midcap_largecap_ratio (rho 0.64, z -2.07); nifty_metal (rho 0.623, z -3.61); dyn_jiofin_bo (rho 0.589, z -1.94); dyn_indusindbk_bo (rho 0.546, z -1.77)
- Source: Sensex today | Stock Market Highlights: Sensex tanks 1,045 pts, Nifty sheds 371 pts to close lower — BusinessLine Mkts, 2026-10-08. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-8th-october-2026/article71556978.ece
- Source: Stock market prediction for tomorrow: Sensex, Nifty outlook for Friday | Kospi, Taiwan cues to watch | 9 Oct 2026 — Mint Markets, 2026-10-08. https://www.livemint.com/market/stock-market-news/stock-market-prediction-for-tomorrow-sensex-nifty-outlook-for-friday-kospi-taiwan-cues-to-watch-9-oct-2026-11791453202525.html
- Source: Nifty falls below 22,300 at noon as Adani Stocks, ITC, Metals slide — BusinessLine Mkts, 2026-10-08. https://www.thehindubusinessline.com/markets/nifty-slides-below-22300-at-noon-adani-entities-itc-metal-stocks-take-a-beating/article71558794.ece
- Historical analogues: 2025-07-21 (d=0.6), 2025-07-14 (d=0.65), 2025-12-30 (d=1.12)

### [RED 5.87] dyn_ohi ↓
- dyn_ohi [EQUITIES]: last 43.75, z20 -3.87, zc -1.71, resid-z -1.07 [moved], 1d -2.28%, |z20|=3.87
- **Mechanism**: dyn_ohi ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Samsung just did something no tech company has ever done, but investors still aren’t satisfied — MarketWatch Top, 2026-10-08. https://www.marketwatch.com/story/samsung-just-did-something-no-tech-company-has-ever-done-and-investors-still-arent-satisfied-3ff5ecb2?mod=mw_rss_topstories
- Source: French bonds are suffering through their worst decade since 1803 — and investors are bracing for more pain — MarketWatch Top, 2026-10-08. https://www.marketwatch.com/story/french-bonds-are-suffering-through-its-worst-decade-since-1803-and-investors-are-bracing-for-more-pain-63df8fe7?mod=mw_rss_topstories
- Source: Stock market crash: Terrible Thursday for Sensex, Nifty as over  ₹7 lakh cr investors' wealth eroded - what went wrong? — Mint Markets, 2026-10-08. https://www.livemint.com/market/stock-market-news/stock-market-crash-terrible-thursday-for-sensex-nifty-as-over-rs-7-lakh-cr-investors-wealth-eroded-what-went-wrong-11791442321941.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2025-04-02 (d=0.09)

### [RED 5.85] dyn_adanient_bo ↓
- dyn_adanient_bo [EQUITIES]: last 2595.00, z20 -3.85, zc -2.05, resid-z -1.91 [unexplained], 1d -5.43%, |z20|=3.85
- **Mechanism**: dyn_adanient_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.539 via dyn_adanient_bo, z -3.61, reacted); nifty_midcap_100 (rho 0.387 via dyn_adanient_bo, z -2.34, reacted); nifty_50 (rho 0.374 via dyn_adanient_bo, z -2.38, reacted)
- **India receivers**: nifty_metal (rho 0.539, z -3.61); nifty_midcap_100 (rho 0.387, z -2.34); nifty_50 (rho 0.374, z -2.38)
- Source: Adani Group stocks tumble as market rout deepens; Adani Green, Adani Ent, others tank up to 10% — ET Markets, 2026-10-08. https://economictimes.indiatimes.com/markets/stocks/news/adani-group-stocks-tumble-as-market-rout-deepens-adani-green-adani-ent-others-tank-up-to-10/articleshow/134786010.cms
- Source: Nifty falls below 22,300 at noon as Adani Stocks, ITC, Metals slide — BusinessLine Mkts, 2026-10-08. https://www.thehindubusinessline.com/markets/nifty-slides-below-22300-at-noon-adani-entities-itc-metal-stocks-take-a-beating/article71558794.ece
- Source: Adani Power shares crash over 6%, down for second consecutive session - What tech charts signal? Experts decode — Mint Markets, 2026-10-08. https://www.livemint.com/market/stock-market-news/adani-power-shares-crash-over-6-down-for-second-consecutive-session-what-tech-charts-signal-experts-decode-11791446333802.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [RED 5.5] indices · 4 series ↓
- stoxx_50 [INDICES]: last 6105.03, z20 -3.84, zc -1.17, resid-z -2.07 [unexplained], 1d -1.22%, |z20|=3.84
- dax [INDICES]: last 24832.46, z20 -3.08, zc -1.04, resid-z -1.78 [unexplained], 1d -1.08%, |z20|=3.08
- cac_40 [INDICES]: last 7701.28, z20 -2.68, zc -0.92, resid-z -1.50 [unexplained], 1d -0.87%, |z20|=2.68; 1y-pct=0
- ftse_100 [INDICES]: last 10409.63, z20 -2.20, zc -0.64, resid-z -1.13 [quiet], 1d -0.47%, |z20|=2.20
- **Mechanism**: indices · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.429 via ftse_100, z -1.77, reacted); nifty_50 (rho 0.389 via ftse_100, z -2.38, reacted); dyn_tataelxsi_ns (rho 0.389 via ftse_100, z -1.98, reacted)
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.713 vs stoxx_50, historically leads by 5d
- Watch next: wti (inverse) — not yet - watch; rho -0.56 vs stoxx_50, historically leads by 4d
- Watch next: vix (inverse) — not yet - watch; rho -0.546 vs stoxx_50, historically leads by 5d
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.504 vs dax, historically leads by 2d
- Watch next: brent (inverse) — not yet - watch; rho -0.53 vs stoxx_50
- **India receivers**: dyn_indusindbk_bo (rho 0.429, z -1.77); nifty_50 (rho 0.389, z -2.38); dyn_tataelxsi_ns (rho 0.389, z -1.98)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-16 (d=0.34), 2024-11-21 (d=0.62)

### [AMBER 5.49] wti ↓
- wti [COMMODITIES]: last 92.75, z20 -0.49, zc 2.16, resid-z -0.71 [priced], 1d 5.06%, 1-session move +5.06% ≥ 1.5%
- **Mechanism**: wti ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.911 vs wti
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.513 vs wti
- Source: India cuts back on costly Russian crude as West Asia flows recover — BusinessLine Mkts, 2026-10-08. https://www.thehindubusinessline.com/markets/commodities/india-shuns-costly-russian-crude-as-west-asia-flows-recover/article71558804.ece
- Source: Oil Jumps 5% as Iran Steps Up Attacks on Hormuz Tankers — OilPrice, 2026-10-08. https://oilprice.com/Latest-Energy-News/World-News/Oil-Jumps-2-as-Iran-Steps-Up-Attacks-on-Hormuz-Tankers.html
- Source: India's Inflation Likely Hit 5.4% in September as Oil Costs Bite — OilPrice, 2026-10-08. https://oilprice.com/Latest-Energy-News/World-News/Indias-Inflation-Likely-Hit-54-in-September-as-Oil-Costs-Bite.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

## Watchlist (below surfacing floor)
dyn_muthootfin_ns ↓ (5.44), dyn_tgt ↓ (5.36), midcap_largecap_ratio ↓ (5.07), dxy ↑ (4.63), dyn_sepn ↓ (4.61), indices · 2 series ↑ (4.6), hang_seng ↓ (4.59), shanghai_comp ↓ (4.31), dyn_4417_t ↑ (4.3), dyn_coalindia_ns ↓ (4.23), dyn_techm_ns ↓ (4.13), natgas ↑ (4.03)

## India macro
- nifty_50: 22231.8008 (1d -1.64%, z20 -2.38, flag amber)
- nifty_midcap_100: 57880.4492 (1d -2.52%, z20 -2.34, flag amber)
- usd_inr: 96.7800 (1d 0.43%, z20 2.54, flag red)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6035 (1d -0.89%, z20 -2.07, flag red)
- Next India prints: AMFI SIP / MF flows T-0d · NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 91.7 — "Indian stock markets set for weak opening as global cues turn negative"
- COALINDIA.NS (COAL INDIA LTD) score 90.4 — "Indian stock markets set for weak opening as global cues turn negative"
- INOXINDIA.NS (INOX INDIA LIMITED) score 90.3 — "Indian stock markets set for weak opening as global cues turn negative"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 88.4 — "Indian stock markets set for weak opening as global cues turn negative"
- BAC (Bank of America Corporation) score 76.2 — "Top stocks to buy for short term: Kotak Neo's expert suggests IndiGo, Union Bank of India,"
- HDB (HDFC Bank Limited) score 72.5 — "Top stocks to buy for short term: Kotak Neo's expert suggests IndiGo, Union Bank of India,"
- IDBI.NS (IDBI BANK LIMITED) score 70.2 — "Top stocks to buy for short term: Kotak Neo's expert suggests IndiGo, Union Bank of India,"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 70.2 — "Top stocks to buy for short term: Kotak Neo's expert suggests IndiGo, Union Bank of India,"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 70.2 — "Top stocks to buy for short term: Kotak Neo's expert suggests IndiGo, Union Bank of India,"
- COIN (Coinbase Global, Inc.) score 64.1 — "Indian stock markets set for weak opening as global cues turn negative"
- BOND (PIMCO Active Bond Exchange-Tra) score 49.4 — "Global Market: JGB yields fall as 30-year bond yield retreats from record high"
- OHI (Omega Healthcare Investors, In) score 47.8 — "Japanese investors sell foreign bonds for third straight week as Treasury yields jump"
- TECHM.NS (TECH MAHINDRA LIMITED) score 46.2 — "TCS, Infosys, HCL Tech, other IT stocks jump up to 3% despite weak market sentiment. What "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 38.9 — "TCS, Infosys, HCL Tech, other IT stocks jump up to 3% despite weak market sentiment. What "
- TECH (Bio-Techne Corp) score 38.9 — "TCS, Infosys, HCL Tech, other IT stocks jump up to 3% despite weak market sentiment. What "
- TGT (Target Corporation) score 38.8 — "Top stocks to buy for short term: Kotak Neo's expert suggests IndiGo, Union Bank of India,"
- CHKP (Check Point Software Technolog) score 34.9 — "Jefferies cuts target prices for BSE, Turtlemint & other stocks ahead of Q2 results. Check"
- LTH (Life Time Group Holdings, Inc.) score 28.4 — "TCS, Infosys, HCL Tech, other IT stocks jump up to 3% despite weak market sentiment. What "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 26.2 — "Where could Suzlon Energy share price be in the next 5 years?"
- SEPN (Septerna, Inc.) score 25.7 — "Rs 13,000 crore blow in September! Why Indian financial stocks are fastest to sell for FII"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 24.6 — "TCS Q2 results 2026 today: Should you buy IT giant stock ahead of earnings, dividend annou"
- 301077.SZ (CHINASTARS) score 18.4 — "Global Market: China stocks slide as tech valuations face earnings test"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 14.9 — "Tata Power shares hits 52-week low; announced Ocean Sun deal buzz"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 14.9 — "Tata Power shares hits 52-week low; announced Ocean Sun deal buzz"
- JIOFIN.BO (Jio Financial Services Limited) score 14.3 — "Rs 13,000 crore blow in September! Why Indian financial stocks are fastest to sell for FII"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 13.7 — "This Adani Group share is among Jefferies India's top 3 picks despite the RBI's 25 bps Rep"
- JUSTDIAL.BO (JUST DIAL LTD.) score 13.2 — "Samsung just did something no tech company has ever done, but investors still aren’t satis"
- JEF (Jefferies Financial Group Inc.) score 13.1 — "RBI rate hike done. Now what’s ahead for bank stocks? Jefferies, other brokerages weigh in"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.5 — "Stock split, spin-off: Last chance to buy these stocks today - Check record date, share pe"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 11.8 — "Muthoot Microfin AUM crosses ₹15,300 crore, cost of funds enters single digits"
- META (Meta) score 9.2 — "Shyam Metalics Q2 volumes shine; capex, value addition central to medium-term growth"
- VT (Vanguard Total World Stock Ind) score 9.1 — "TRUMP: WE SHOULD HAVE THE LOWEST INTEREST RATE IN THE WORLD"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 8.0 — "Landmark Group raises Rs 330 crore SBI finance for Gurugram project"
- NVDA (NVIDIA Corporation) score 7.6 — "Microsoft and Nvidia are teaming up on a supercharged AI laptop"
- RS (Reliance, Inc.) score 5.5 — "Reliance shares may be a cheaper way to buy Jio Platforms after its listing"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 5.2 — "Trent’s Rs 1.80 lakh crore rout from peak: Has Q2 just flipped the script for Tata group’s"
- POLICYBZR.NS (PB FINTECH LIMITED) score 4.5 — "Pine Labs, CAMS, Moneyview, other fintech stocks rally up to 11% after RBI MPC move. Here’"
- GS (Goldman Sachs Group, Inc. (The) score 4.3 — "TSLA - GOLDMAN: TESLA’S AI STORY MATTERS MORE THAN Q3 EARNINGS Goldman Sachs reiterated it"
- DELL (Dell Technologies Inc.) score 1.0 — "Piero Cipollone: Interview with Corriere della Sera"
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