# Transmission Layer — board brief · 2026-11-11 11:51Z

data as of **2026-11-11** · 97 series · 9 red / 34 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.562, 1d in regime; vol-pct 0.79, breadth-off 0.333, Markov P(high-vol) 0.221)
- [INVERTED] **safe_haven_gold** — corr20 -0.12, corr60 -0.22, contra nifty_50 corr20=0.29, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.9, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.12, corr60 0.12, last shift 2026-09-10. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.2, corr60 0.05, last shift 2026-09-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.9, last shift 2026-09-23. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.3, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.1, corr60 -0.1, last shift 2026-08-12. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.33, corr60 0.31, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **5 of 89** scanned series survive multiplicity control (effective p ≤ 0.005605629265529988)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.509** (n=1135) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=2123) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.79] usd_inr ↓
- usd_inr [FX]: last 93.68, z20 -2.79, zc -0.63, resid-z -0.75 [quiet], 1d -0.28%, 20d range extreme; |z20|=2.79; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_havells_ns (rho -0.416 via usd_inr, z 2.05, reacted); dyn_indusindbk_bo (rho -0.373 via usd_inr, z 1.6, reacted)
- **India receivers**: dyn_havells_ns (rho -0.416, z 2.05); dyn_indusindbk_bo (rho -0.373, z 1.6)
- Source: Rupee rises 7 paise to close at 93.70 against US dollar — BusinessLine Mkts, 2026-11-11. https://www.thehindubusinessline.com/markets/forex/rupee-rises-7-paise-to-close-at-9370-against-us-dollar/article71689281.ece
- Source: Rupee touches strongest since April as foreign inflows offset firm dollar — ET Markets, 2026-11-11. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-touches-strongest-since-april-as-foreign-inflows-offset-firm-dollar/articleshow/135734005.cms
- Source: Rupee rises 7 paise to 93.70 against US dollar in early trade — ET Markets, 2026-11-11. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-rises-7-paise-to-93-70-against-us-dollar-in-early-trade/articleshow/135726644.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 6.7] cross-asset · 6 series ↑
- nifty_50 [INDICES]: last 25255.05, z20 2.55, zc 1.80, resid-z 2.78 [unexplained], 1d 0.84%, |z20|=2.55
- nifty_metal [INDICES]: last 12787.40, z20 2.28, zc 0.45, resid-z -1.15 [quiet], 1d 0.97%, |z20|=2.28
- dyn_bajfinance_ns [EQUITIES]: last 1078.80, z20 2.22, zc 0.74, resid-z -0.69 [quiet], 1d 1.31%, |z20|=2.22
- nifty_midcap_100 [INDICES]: last 61515.05, z20 2.18, zc 0.00, resid-z -2.77 [unexplained], 1d 0.81%, |z20|=2.18
- nifty_fmcg [INDICES]: last 47188.90, z20 2.10, zc 0.49, resid-z -1.60 [unexplained], 1d 1.13%, |z20|=2.10
- dyn_muthootfin_ns [EQUITIES]: last 2900.00, z20 2.09, zc 0.28, resid-z -0.76 [quiet], 1d -0.60%, |z20|=2.09
- **Mechanism**: cross-asset · 6 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 1.09).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.818 via nifty_midcap_100, z 1.76, reacted); dyn_adanient_bo (rho 0.735 via nifty_metal, z 1.02, reacted); dyn_indusindbk_bo (rho 0.634 via nifty_midcap_100, z 1.6, reacted); dyn_indianb_ns (rho 0.612 via nifty_midcap_100, z 2.99, reacted); dyn_policybzr_ns (rho 0.53 via nifty_midcap_100, z -0.74, quiet)
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.506 vs nifty_50, historically leads by 5d
- Watch next: dyn_policybzr_ns (co-move) — not yet - watch; rho 0.524 vs dyn_bajfinance_ns
- Watch next: taiwan_weighted (inverse) — not yet - watch; rho -0.512 vs nifty_50
- **India receivers**: dyn_jiofin_bo (rho 0.818, z 1.76); dyn_adanient_bo (rho 0.735, z 1.02); dyn_indusindbk_bo (rho 0.634, z 1.6); dyn_indianb_ns (rho 0.612, z 2.99)
- Source: Nifty closes 0.84% higher, cooling off from intraday highs — BusinessLine Mkts, 2026-11-11. https://www.thehindubusinessline.com/markets/nifty-closes-084-higher-cooling-off-from-intraday-highs/article71689484.ece
- Source: Indices hold gains at noon; M&M, IndiGo top Nifty charts as IT stocks drag — BusinessLine Mkts, 2026-11-11. https://www.thehindubusinessline.com/markets/indices-hold-gains-at-noon-mm-indigo-top-nifty-charts-as-it-stocks-drag/article71688800.ece
- Source: Sensex today | Stock Market Highlights: Sensex closes 772 pts higher, Nifty ends above 25,250; M&M, IndiGo top gainers — BusinessLine Mkts, 2026-11-11. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-11th-november-2026/article71682389.ece
- Historical analogues: 2025-07-21 (d=1.09), 2025-12-23 (d=1.43), 2025-07-11 (d=1.45)

### [AMBER 5.66] cross-asset · 3 series ↓
- eth_usd [CRYPTO]: last 2056.68, z20 -2.34, zc 0.08, resid-z -0.41 [quiet], 1d 0.32%, |z20|=2.34
- dyn_coin [EQUITIES]: last 132.16, z20 -1.78, zc -0.60, resid-z 0.35 [quiet], 1d -2.89%, 1y-pct=0
- btc_usd [CRYPTO]: last 73988.13, z20 -1.72, zc 0.15, resid-z -0.06 [quiet], 1d 0.36%, |z20|=1.72
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.13).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.755 vs eth_usd
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.738 vs eth_usd
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.522 vs eth_usd, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.665 vs eth_usd
- Watch next: vix (inverse) — not yet - watch; rho -0.581 vs eth_usd
- Source: U.S. Midterm Shake-Up Could Reshape Global Oil and Gas Markets — OilPrice, 2026-11-10. https://oilprice.com/Energy/Energy-General/US-Midterm-Shake-Up-Could-Reshape-Global-Oil-and-Gas-Markets.html
- Source: Iran War Set to Drive A Drop in Global Fossil Fuel Emissions in 2026 — OilPrice, 2026-11-10. https://oilprice.com/Latest-Energy-News/World-News/Iran-War-Set-to-Drive-A-Drop-in-Global-Fossil-Fuel-Emissions-in-2026.html
- Source: HYPERSCALE DATA SELLS REMAINING BITCOIN RESERVES TO REDUCE DEBT AND FUND MICHIGAN AI DATA CENTER HYPERSCALE DATA - SELLS 211.56 BITCOIN FOR GROSS PROCEEDS OF $16 MLN HYPERSCALE DATA - USES PROCEEDS TO PAY DOWN DEBT AND FUND MICHIGAN AI DATA CENTER DEVELOPMENT — DeItaone, 2026-11-10. https://t.me/walter_bloomberg/38295
- Historical analogues: 2026-05-22 (d=0.13), 2025-04-10 (d=0.44), 2025-03-31 (d=0.59)

### [RED 5.23] dxy ↑
- dxy [FX]: last 102.53, z20 2.23, zc 0.85, resid-z 2.61 [unexplained], 1d 0.30%, 20d range extreme; |z20|=2.23; 1y-pct=99
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.585 vs dxy, historically leads by 1d
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-10 (d=0.03), 2025-05-14 (d=0.06)

### [RED 5.08] dyn_nvda ↓
- dyn_nvda [EQUITIES]: last 168.79, z20 -3.08, zc -1.30, resid-z 0.97 [quiet], 1d -5.53%, |z20|=3.08; 1y-pct=1
- **Mechanism**: dyn_nvda ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.653 vs dyn_nvda, historically leads by 5d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.562 vs dyn_nvda, historically leads by 5d
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.639 vs dyn_nvda
- Watch next: vix (inverse) — not yet - watch; rho -0.621 vs dyn_nvda
- Source: Once AI darling of shareholders, Nvidia sued by own stock buyers over CEO Jensen Huang affair; $420 bn lost in 2 days — Mint Markets, 2026-11-11. https://www.livemint.com/market/stock-market-news/once-ai-darling-of-shareholders-nvidia-sued-by-own-stock-buyers-over-ceo-jensen-huang-affair-420-bn-lost-in-2-days-11794377931484.html
- Source: Nvidia Stock Sell-Off Deepens: Spy scandal, price target cuts put AI giant under pressure — ET Markets, 2026-11-11. https://economictimes.indiatimes.com/markets/us-stocks/news/nvidia-stock-sell-off-deepens-spy-scandal-price-target-cuts-put-ai-giant-under-pressure/slideshow/135728557.cms
- Source: AI stock Nvidia crashed but Netweb Technologies shares jumped 8% today after falling 13% in 1 month? Reasons; target — Mint Markets, 2026-11-11. https://www.livemint.com/market/stock-market-news/ai-stock-nvidia-crashed-but-netweb-technologies-shares-jumped-8-today-after-falling-13-in-1-month-reasons-target-11794375606908.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-24 (d=0.03), 2026-05-04 (d=0.03)

### [AMBER 4.67] commodities · 2 series ↓
- wti [COMMODITIES]: last 86.73, z20 -1.84, zc 0.26, resid-z -0.67 [quiet], 1d 0.80%, |z20|=1.84
- brent [COMMODITIES]: last 92.79, z20 -1.77, zc 0.44, resid-z -0.90 [quiet], 1d 1.42%, |z20|=1.77; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.499 via wti, z 2.09, reacted)
- Watch next: vix (co-move) — not yet - watch; rho 0.545 vs brent, historically leads by 1d
- Watch next: dyn_gs (inverse) — not yet - watch; rho -0.552 vs brent
- Watch next: dyn_demz (inverse) — not yet - watch; rho -0.548 vs wti
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.527 vs brent
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.504 vs wti
- **India receivers**: dyn_muthootfin_ns (rho -0.499, z 2.09)
- Source: Argentina, Malaysia overtake Indonesia as top veg oil exporters to India — BusinessLine Mkts, 2026-11-11. https://www.thehindubusinessline.com/economy/agri-business/argentina-malaysia-overtake-indonesia-as-top-veg-oil-exporters-to-india/article71689201.ece
- Source: IndiGo shares surge past analyst target as falling crude, Q2 beat draw buyers — BusinessLine Mkts, 2026-11-11. https://www.thehindubusinessline.com/markets/stock-markets/indigo-surges-past-analyst-target-as-crude-slide-and-q2-beat-draw-buyers/article71688766.ece
- Source: Should you invest in HPCL, BPCL, IOCL and other OMC stocks now as oil not on the boil anymore; slips below $90/barrel — Mint Markets, 2026-11-11. https://www.livemint.com/market/stock-market-news/should-you-invest-in-hpcl-bpcl-iocl-and-other-omc-stocks-now-as-oil-not-on-the-boil-anymore-slips-below-90barrel-11794381942470.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [AMBER 4.5] dyn_hdb ↑
- dyn_hdb [EQUITIES]: last 25.99, z20 2.50, zc 0.36, resid-z 1.20 [quiet], 1d 0.70%, |z20|=2.50
- **Mechanism**: dyn_hdb ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: usd_inr (rho -0.217 via dyn_hdb, leads 1d, z -2.79, reacted); dyn_muthootfin_ns (rho 0.373 via dyn_hdb, z 2.09, reacted); nifty_50 (rho 0.37 via dyn_hdb, z 2.55, reacted)
- **India receivers**: usd_inr (rho -0.217, z -2.79); dyn_muthootfin_ns (rho 0.373, z 2.09); nifty_50 (rho 0.37, z 2.55)
- Source: HDFC Bank shares cross ₹811 as shareholders approve Bagchi’s appointment — BusinessLine Mkts, 2026-11-11. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-cross-811-as-shareholders-approve-bagchis-appointment/article71688704.ece
- Source: Retail investors shed stocks, but crowd into Reliance, HDFC Bank — Mint Markets, 2026-11-10. https://www.livemint.com/market/stock-market-news/retail-investors-reliance-hdfc-bank-fpis-stock-markets-india-11794288650697.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [AMBER 4.43] usd_jpy ↑
- usd_jpy [FX]: last 159.11, z20 2.43, zc 1.49, resid-z 1.45 [quiet], 1d 0.71%, |z20|=2.43
- **Mechanism**: usd_jpy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho 0.394 via usd_jpy, z -0.33, quiet)
- **India receivers**: dyn_idbi_ns (rho 0.394, z -0.33)
- Source: Top Yen Forecaster Predicts 147 Per Dollar as Rate Gap Narrows — Mint Markets, 2026-11-09. https://www.livemint.com/market/top-yen-forecaster-predicts-147-per-dollar-as-rate-gap-narrows-11794259355721.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2025-07-30 (d=0.01)

## Watchlist (below surfacing floor)
indices · 3 series ↑ (4.28), dyn_tech ↑ (4.12), natgas ↑ (4.0), equities · 2 series ↑ (3.94), dyn_atherenerg_ns ↑ (3.6), eur_inr ↓ (3.59), dyn_lth ↑ (3.59), dyn_schd ↑ (3.09), dyn_4417_t ↑ (3.03), cross-asset · 2 series ↑ (2.7), asx_200 ↑ (2.64), hy_oas ↑ (2.34)

## India macro
- nifty_50: 25255.0508 (1d 0.84%, z20 2.55, flag red)
- nifty_midcap_100: 61515.0508 (1d 0.81%, z20 2.18, flag amber)
- usd_inr: 93.6800 (1d -0.28%, z20 -2.79, flag red)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4358 (1d -0.03%, z20 -1.37, flag none)
- Next India prints: NSDL FPI flows T-0d · India CPI T-1d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 77.9 — "India’s rich pivot to real estate after stock returns falter"
- INOXINDIA.NS (INOX INDIA LIMITED) score 76.0 — "India’s rich pivot to real estate after stock returns falter"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 75.8 — "India’s rich pivot to real estate after stock returns falter"
- INDIANB.NS (INDIAN BANK) score 55.1 — "ICICI Bank Share Price Live Updates: ICICI Bank's Price Movement Today"
- BAC (Bank of America Corporation) score 48.5 — "ICICI Bank Share Price Live Updates: ICICI Bank's Price Movement Today"
- TECHM.NS (TECH MAHINDRA LIMITED) score 39.6 — "Matrimony.com to acquire 50% stake in astrology tech firm Astro-Vision, reports Q2 PAT up "
- HDB (HDFC Bank Limited) score 39.5 — "ICICI Bank Share Price Live Updates: ICICI Bank's Price Movement Today"
- TGT (Target Corporation) score 39.4 — "TD Power shares up 350% up in 3 years, jumps 5% today as Sensex, Nifty jump massively | Mo"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.0 — "Matrimony.com to acquire 50% stake in astrology tech firm Astro-Vision, reports Q2 PAT up "
- TECH (Bio-Techne Corp) score 39.0 — "Matrimony.com to acquire 50% stake in astrology tech firm Astro-Vision, reports Q2 PAT up "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 37.2 — "ICICI Bank Share Price Live Updates: ICICI Bank's Price Movement Today"
- IDBI.NS (IDBI BANK LIMITED) score 37.2 — "ICICI Bank Share Price Live Updates: ICICI Bank's Price Movement Today"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 37.2 — "ICICI Bank Share Price Live Updates: ICICI Bank's Price Movement Today"
- NVDA (NVIDIA Corporation) score 35.8 — "AI stock Nvidia crashed but Netweb Technologies shares jumped 8% today after falling 13% i"
- 301077.SZ (CHINASTARS) score 33.7 — "Written in bone: China bets on ancient scripts for modern soft power"
- OHI (Omega Healthcare Investors, In) score 30.1 — "Sensex, Nifty hit eight-month high as foreign investors return"
- COIN (Coinbase Global, Inc.) score 25.0 — "Iran War Set to Drive A Drop in Global Fossil Fuel Emissions in 2026"
- CHKP (Check Point Software Technolog) score 24.6 — "ONGC dividend 2026: Last day to buy today | Check dividend payout, record date, history, y"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.2 — "Why KPI Green Energy, Waaree Energies shares are rising today; over 5% jump amid post Diwa"
- BOND (PIMCO Active Bond Exchange-Tra) score 18.6 — "Bond yields spike most since tariff meltdown on rate-hike bets"
- LTH (Life Time Group Holdings, Inc.) score 17.7 — "U.S. 10-YEAR TREASURY YIELD RISES BACK TO 5% FOR FIRST TIME IN 12 DAYS"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 17.3 — "Bajaj Auto Share Price Live Updates: Centre's EV push puts electric mobility stocks in the"
- SCHD (Schwab US Dividend Equity ETF) score 13.6 — "ONGC dividend 2026: Last day to buy today | Check dividend payout, record date, history, y"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.6 — "Top stocks to watch today: Cochin Shipyard, MRF, Tata Power shares in focus on Wednesday, "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.6 — "Top stocks to watch today: Cochin Shipyard, MRF, Tata Power shares in focus on Wednesday, "
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 13.4 — "Trump says Iran war ‘effectively over’: How's it likely to impact Sensex, Nifty, gold and "
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 12.4 — "Stocks to watch, Nov 11: Gokaldas Exports, Matrimony.com, BHEL, Bajaj Finserv, Jyothy Lab,"
- BZ=F (Brent Crude Oil Last Day Finan) score 10.7 — "ONGC dividend 2026: Last day to buy today | Check dividend payout, record date, history, y"
- JIOFIN.BO (Jio Financial Services Limited) score 9.5 — "Jio Financial Services Share Price Live Updates: Market Movement: Jio Financial Services"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.5 — "Adani Ent Share Price Live Updates: Adani Enterprises  Market Performance"
- RS (Reliance, Inc.) score 7.0 — "AMFI Rejig: Reliance's Jio Platforms, NSE, Lenskart, LG among 7 stocks set for large cap u"
- META (Meta) score 6.8 — "Gold vs silver vs copper vs platinum: Which metal could deliver the biggest returns in Sam"
- DEMZ (Democratic Large Cap Core ETF) score 6.5 — "DEMOCRATIC SENATE LEADER SCHUMER CALLS TRUMP'S DEFENSE OF NVIDIA'S HUANG "TROUBLING" SCHUM"
- JEF (Jefferies Financial Group Inc.) score 5.7 — "RIL, HDFC, Axis Bank, IndiGo, more: List of 12 stocks from Jefferies; shares to gain as FP"
- GS (Goldman Sachs Group, Inc. (The) score 5.3 — "Why Goldman Sachs is now changing its Federal Reserve interest-rate forecast"
- JUSTDIAL.BO (JUST DIAL LTD.) score 4.5 — "These 12 midcap stocks rally up to 30% in just one month"
- SEPN (Septerna, Inc.) score 3.8 — "Promoter shareholding in listed companies hits three-year high at 41.93% in September quar"
- VT (Vanguard Total World Stock Ind) score 3.5 — "Anthropic's potential mega IPO joins ranks of world's biggest stock market listings"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.3 — "Broker’s call: PB Fintech (Buy)"
- SWIGGY.NS (SWIGGY LIMITED) score 0.1 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"

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