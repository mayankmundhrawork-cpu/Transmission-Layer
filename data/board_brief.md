# Transmission Layer — board brief · 2026-11-12 02:21Z

data as of **2026-11-12** · 97 series · 11 red / 33 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.833, 6d in regime; vol-pct None, breadth-off 0.833, Markov P(high-vol) 0.206)
- [INVERTED] **safe_haven_gold** — corr20 -0.09, corr60 -0.2, contra nifty_50 corr20=0.29, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.87, corr60 0.84, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.12, corr60 0.12, last shift 2026-09-11. Channel: global copper leads Indian metal equities
- [INVERTED] **inr_oil_channel** — corr20 -0.31, corr60 0.05, last shift 2026-09-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.91, last shift 2026-09-24. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.19, corr60 -0.0, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.1, corr60 -0.1, last shift 2026-08-12. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.36, corr60 0.32, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.511** (n=1146) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.815** (n=2147) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.47] usd_inr ↓
- usd_inr [FX]: last 93.68, z20 -2.47, zc -0.59, resid-z -0.37 [quiet], 1d -0.26%, 20d range extreme; |z20|=2.47; co-occur[inr_oil] suppressed: channel INVERTED
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_havells_ns (rho -0.476 via usd_inr, z 2.05, reacted); nifty_it (rho -0.422 via usd_inr, z 0.49, quiet); dyn_indianb_ns (rho -0.396 via usd_inr, z 2.99, reacted); dyn_tataelxsi_ns (rho -0.392 via usd_inr, z 0.83, quiet); dyn_bajfinance_ns (rho -0.372 via usd_inr, z 2.22, reacted)
- **India receivers**: dyn_havells_ns (rho -0.476, z 2.05); nifty_it (rho -0.422, z 0.49); dyn_indianb_ns (rho -0.396, z 2.99); dyn_tataelxsi_ns (rho -0.392, z 0.83)
- Source: Sensex today | Stock Market Live Updates: Rupee closes Wednesday's session at 7-month high of 93.69 as FPI inflows, lower crude prices boost sentiment — BusinessLine Mkts, 2026-11-12. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-12-november-2026/article71689385.ece
- Source: Rupee closes at seven-month high of 93.69 as FPI inflows, lower crude prices boost sentiment — BusinessLine Mkts, 2026-11-11. https://www.thehindubusinessline.com/markets/forex/rupee-closes-at-seven-month-high-of-9369-as-fpi-inflows-lower-crude-prices-boost-sentiment/article71689839.ece
- Source: Rupee rises 7 paise to close at 93.70 against US dollar — BusinessLine Mkts, 2026-11-11. https://www.thehindubusinessline.com/markets/forex/rupee-rises-7-paise-to-close-at-9370-against-us-dollar/article71689281.ece
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
- **India take**: dyn_jiofin_bo (rho 0.825 via nifty_midcap_100, z 1.76, reacted); dyn_adanient_bo (rho 0.746 via nifty_metal, z 1.02, reacted); dyn_indusindbk_bo (rho 0.651 via nifty_midcap_100, z 1.6, reacted); dyn_indianb_ns (rho 0.613 via nifty_midcap_100, z 2.99, reacted); dyn_policybzr_ns (rho 0.531 via nifty_midcap_100, z -0.74, quiet)
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.505 vs nifty_50, historically leads by 5d
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.535 vs dyn_muthootfin_ns
- Watch next: dyn_policybzr_ns (co-move) — not yet - watch; rho 0.525 vs dyn_bajfinance_ns
- **India receivers**: dyn_jiofin_bo (rho 0.825, z 1.76); dyn_adanient_bo (rho 0.746, z 1.02); dyn_indusindbk_bo (rho 0.651, z 1.6); dyn_indianb_ns (rho 0.613, z 2.99)
- Source: Sensex today | Stock Market Live Updates: Buzzing stocks: Bajaj Finance, Tata Power, Adani Enterprises, Sandur Manganese, Alivus Life, Aurobindo Pharma — BusinessLine Mkts, 2026-11-12. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-12-november-2026/article71689385.ece
- Source: Buzzing stocks: Bajaj Finance, Tata Power, Adani Enterprises, Sandur Manganese, Alivus Life, Aurobindo Pharma — BusinessLine Mkts, 2026-11-12. https://www.thehindubusinessline.com/markets/buzzing-stocks-bajaj-finance-tata-power-adani-enterprises-sandur-manganese-alivus-life-aurobindo-pharma/article71692162.ece
- Source: Top stocks to watch today: Tata Power, Bajaj Finance, HAL, IRCTC shares in focus on Thursday, 12 November | Full list — Mint Markets, 2026-11-12. https://www.livemint.com/market/stock-market-news/top-stocks-to-watch-today-tata-power-bajaj-finance-hal-irctc-shares-in-focus-on-thursday-12-november-full-list-11794447178928.html
- Historical analogues: 2025-07-21 (d=1.09), 2025-12-23 (d=1.43), 2025-07-11 (d=1.45)

### [RED 6.24] fx · 2 series ↓
- eur_usd [FX]: last 1.11, z20 -3.41, zc -2.04, resid-z -1.38 [moved], 1d -0.71%, |z20|=3.41; 1y-pct=0
- gbp_usd [FX]: last 1.33, z20 -1.67, zc -1.66, resid-z -2.11 [unexplained], 1d -0.61%, |z20|=1.67
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Sterling drops against firmer dollar as markets price in a hawkish Fed — ET Markets, 2026-11-11. https://economictimes.indiatimes.com/markets/forex/forex-news/sterling-drops-against-firmer-dollar-as-markets-price-in-a-hawkish-fed/articleshow/135738659.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [RED 5.95] dxy ↑
- dxy [FX]: last 102.87, z20 2.95, zc 0.01, resid-z 2.61 [unexplained], 1d 0.00%, 20d range extreme; |z20|=2.95; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.579 vs dxy, historically leads by 1d
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-10 (d=0.03), 2025-05-14 (d=0.06)

### [RED 5.64] usd_jpy ↑
- usd_jpy [FX]: last 159.81, z20 3.64, zc 1.39, resid-z 0.84 [quiet], 1d 0.70%, |z20|=3.64
- **Mechanism**: usd_jpy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho 0.4 via usd_jpy, z -0.33, quiet)
- **India receivers**: dyn_idbi_ns (rho 0.4, z -0.33)
- Source: Dollar near one-month high as yen edges toward 160 — ET Markets, 2026-11-12. https://economictimes.indiatimes.com/markets/forex/forex-news/dollar-near-one-month-high-as-yen-edges-toward-160/articleshow/135751707.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2025-07-30 (d=0.01)

### [AMBER 5.34] cross-asset · 3 series ↓
- eth_usd [CRYPTO]: last 2058.59, z20 -2.02, zc -0.23, resid-z 0.44 [quiet], 1d -0.88%, |z20|=2.02
- btc_usd [CRYPTO]: last 73898.89, z20 -1.56, zc -0.22, resid-z -0.15 [quiet], 1d -0.50%, |z20|=1.56
- dyn_coin [EQUITIES]: last 136.30, z20 -1.33, zc 0.66, resid-z 0.35 [quiet], 1d 3.16%, 1y-pct=1
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.33).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.749 vs eth_usd
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.537 vs eth_usd, historically leads by 1d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.708 vs eth_usd
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.668 vs eth_usd
- Watch next: vix (inverse) — not yet - watch; rho -0.59 vs eth_usd
- Source: Global Market Today: Asian stocks mixed as Nvidia turmoil hits AI-linked shares — ET Markets, 2026-11-12. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-today-us-stock-futures-fall-as-nvidia-turmoil-deepens/articleshow/135751953.cms
- Source: Global Power Grid Expansion Surges 50% to Record High — OilPrice, 2026-11-12. https://oilprice.com/Energy/Energy-General/Global-Power-Grid-Expansion-Surges-50-to-Record-High.html
- Source: How a Super El Niño Could Reshape Global Coal Markets — OilPrice, 2026-11-11. https://oilprice.com/Energy/Energy-General/How-a-Super-El-Nio-Could-Reshape-Global-Coal-Markets.html
- Historical analogues: 2026-05-22 (d=0.33), 2025-03-31 (d=0.41), 2025-10-22 (d=0.41)

### [RED 4.68] indices · 3 series ↑
- stoxx_50 [INDICES]: last 6392.53, z20 3.36, zc 1.06, resid-z 0.87 [quiet], 1d 1.02%, |z20|=3.36
- cac_40 [INDICES]: last 8330.49, z20 2.38, zc 0.72, resid-z 1.09 [quiet], 1d 0.63%, |z20|=2.38
- dax [INDICES]: last 26644.39, z20 2.37, zc 0.99, resid-z 1.49 [quiet], 1d 1.13%, |z20|=2.37; 1y-pct=100
- **Mechanism**: indices · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.502 via cac_40, z 2.09, reacted); nifty_fmcg (rho 0.501 via cac_40, z 2.1, reacted); nifty_midcap_100 (rho 0.497 via dax, z 2.18, reacted); dyn_jiofin_bo (rho 0.449 via cac_40, z 1.76, reacted); dyn_tataelxsi_ns (rho 0.447 via cac_40, z 0.83, quiet)
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.519 vs stoxx_50, historically leads by 5d
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.509 vs stoxx_50, historically leads by 2d
- **India receivers**: dyn_muthootfin_ns (rho 0.502, z 2.09); nifty_fmcg (rho 0.501, z 2.1); nifty_midcap_100 (rho 0.497, z 2.18); dyn_jiofin_bo (rho 0.449, z 1.76)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-16 (d=0.39), 2025-09-01 (d=0.4)

### [AMBER 4.57] commodities · 2 series ↓
- wti [COMMODITIES]: last 85.96, z20 -1.74, zc 0.01, resid-z 0.82 [quiet], 1d 0.02%, |z20|=1.74
- brent [COMMODITIES]: last 92.15, z20 -1.63, zc 0.06, resid-z 1.09 [quiet], 1d 0.17%, |z20|=1.63; co-occur[inr_oil] suppressed: channel INVERTED
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.507 via wti, z 2.09, reacted)
- Watch next: vix (co-move) — not yet - watch; rho 0.561 vs brent, historically leads by 1d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.622 vs brent
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.572 vs brent
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.505 vs wti
- **India receivers**: dyn_muthootfin_ns (rho -0.507, z 2.09)
- Source: Oil prices drop more than $1 as hopes for Iran, Ukraine peace talks pressure markets — ET Markets, 2026-11-12. https://economictimes.indiatimes.com/markets/commodities/news/oil-prices-drop-more-than-1-as-hopes-for-iran-ukraine-peace-talks-pressure-markets/articleshow/135752159.cms
- Source: Sensex today | Stock Market Live Updates: Rupee closes Wednesday's session at 7-month high of 93.69 as FPI inflows, lower crude prices boost sentiment — BusinessLine Mkts, 2026-11-12. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-12-november-2026/article71689385.ece
- Source: Who Will Buy Sable’s Oil if California Keeps Closing Refineries? — OilPrice, 2026-11-12. https://oilprice.com/Energy/Crude-Oil/Who-Will-Buy-Sables-Oil-if-California-Keeps-Closing-Refineries.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

## Watchlist (below surfacing floor)
dyn_nvda ↓ (4.15), dyn_hdb ↑ (4.09), equities · 2 series ↑ (3.94), eur_inr ↓ (3.85), commodities · 2 series ↓ (3.78), natgas ↑ (3.68), dyn_tech ↑ (3.48), dyn_lth ↑ (3.46), dyn_schd ↑ (3.31), dyn_4417_t ↑ (2.94), cross-asset · 2 series ↑ (2.7), dyn_rs ↑ (2.41)

## India macro
- nifty_50: 25255.0508 (1d 0.84%, z20 2.55, flag red)
- nifty_midcap_100: 61515.0508 (1d 0.81%, z20 2.18, flag amber)
- usd_inr: 93.6800 (1d -0.26%, z20 -2.47, flag red)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4358 (1d -0.03%, z20 -1.37, flag none)
- Next India prints: India CPI T-0d · NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 75.3 — "Stock recommendations for 12 November from MarketSmith India"
- INOXINDIA.NS (INOX INDIA LIMITED) score 72.7 — "Stock recommendations for 12 November from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 72.5 — "Stock recommendations for 12 November from MarketSmith India"
- NVDA (NVIDIA Corporation) score 57.7 — "LUTNICK STALLED TRUMP'S NVIDIA–CHINA CHIP CURBS AFTER OVAL TALKS- AXIOS"
- INDIANB.NS (INDIAN BANK) score 52.7 — "MARSH PUSHES FED TO EASE BANK CAPITAL RULES FOR AI LOANS Marsh ($MRSH) is lobbying US regu"
- BAC (Bank of America Corporation) score 47.0 — "MARSH PUSHES FED TO EASE BANK CAPITAL RULES FOR AI LOANS Marsh ($MRSH) is lobbying US regu"
- HDB (HDFC Bank Limited) score 40.1 — "MARSH PUSHES FED TO EASE BANK CAPITAL RULES FOR AI LOANS Marsh ($MRSH) is lobbying US regu"
- TGT (Target Corporation) score 38.0 — "BAIRD SLASHES NVIDIA PRICE TARGET 60%, WARNS OF AI SLOWDOWN Baird downgraded Nvidia ($NVDA"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 37.1 — "MARSH PUSHES FED TO EASE BANK CAPITAL RULES FOR AI LOANS Marsh ($MRSH) is lobbying US regu"
- IDBI.NS (IDBI BANK LIMITED) score 37.1 — "MARSH PUSHES FED TO EASE BANK CAPITAL RULES FOR AI LOANS Marsh ($MRSH) is lobbying US regu"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 37.1 — "MARSH PUSHES FED TO EASE BANK CAPITAL RULES FOR AI LOANS Marsh ($MRSH) is lobbying US regu"
- TECHM.NS (TECH MAHINDRA LIMITED) score 36.3 — "HCL Tech Share Price Highlights: HCL Tech Stock Price History"
- 301077.SZ (CHINASTARS) score 36.1 — "LUTNICK STALLED TRUMP'S NVIDIA–CHINA CHIP CURBS AFTER OVAL TALKS- AXIOS"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 35.8 — "HCL Tech Share Price Highlights: HCL Tech Stock Price History"
- TECH (Bio-Techne Corp) score 35.8 — "HCL Tech Share Price Highlights: HCL Tech Stock Price History"
- OHI (Omega Healthcare Investors, In) score 27.1 — "Market angst is driving investors into low-volatility stocks as AI trade stumbles"
- COIN (Coinbase Global, Inc.) score 24.7 — "Global Power Grid Expansion Surges 50% to Record High"
- CHKP (Check Point Software Technolog) score 23.3 — "Top 2 stocks to buy for short-term: Canara Bank, Pine Labs by Nagaraj Shetti - Check stop "
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 22.9 — "Top stocks to watch today: Tata Power, Bajaj Finance, HAL, IRCTC shares in focus on Thursd"
- LTH (Life Time Group Holdings, Inc.) score 22.2 — "AXIOS: LUTNICK BLOCKED TRUMP'S NVIDIA–CHINA CHIP CRACKDOWN Commerce Secretary Howard Lutni"
- BOND (PIMCO Active Bond Exchange-Tra) score 20.9 — "Falling oil prices are no longer enough to bring down borrowing costs in the world’s most "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.4 — "Bloom Energy’s stock rallies as data-center jitters subside"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 18.6 — "Top stocks to watch today: Tata Power, Bajaj Finance, HAL, IRCTC shares in focus on Thursd"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 16.7 — "Top stocks to watch today: Tata Power, Bajaj Finance, HAL, IRCTC shares in focus on Thursd"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 16.7 — "Top stocks to watch today: Tata Power, Bajaj Finance, HAL, IRCTC shares in focus on Thursd"
- SCHD (Schwab US Dividend Equity ETF) score 13.7 — "Edelweiss Alternatives’ H1FY27 profit rises 35% to ₹169 crore; declares ₹7 interim dividen"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 11.6 — "Trump says Iran war ‘effectively over’: How's it likely to impact Sensex, Nifty, gold and "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 11.3 — "Buzzing stocks: Bajaj Finance, Tata Power, Adani Enterprises, Sandur Manganese, Alivus Lif"
- BZ=F (Brent Crude Oil Last Day Finan) score 11.3 — "CRWV - COREWEAVE SHARES EXTEND GAINS TO TOUCH A TWO WEEK HIGH; LAST UP 20.8%"
- CRWV (CoreWeave, Inc.) score 10.5 — "COREWEAVE SHARES FOLLOW NVIDIA LOWER, DOWN 6%"
- JIOFIN.BO (Jio Financial Services Limited) score 9.2 — "Fairfax Financial likely to exit IIFL Finance, sources say"
- RS (Reliance, Inc.) score 6.1 — "AMFI Rejig: Reliance's Jio Platforms, NSE, Lenskart, LG among 7 stocks set for large cap u"
- META (Meta) score 6.0 — "Gold vs silver vs copper vs platinum: Which metal could deliver the biggest returns in Sam"
- JUSTDIAL.BO (JUST DIAL LTD.) score 5.8 — "Sandisk’s stock just staged a big gain. Here’s how it could march even higher."
- DEMZ (Democratic Large Cap Core ETF) score 5.6 — "DEMOCRATIC SENATE LEADER SCHUMER CALLS TRUMP'S DEFENSE OF NVIDIA'S HUANG "TROUBLING" SCHUM"
- JEF (Jefferies Financial Group Inc.) score 4.9 — "RIL, HDFC, Axis Bank, IndiGo, more: List of 12 stocks from Jefferies; shares to gain as FP"
- GS (Goldman Sachs Group, Inc. (The) score 4.6 — "Why Goldman Sachs is now changing its Federal Reserve interest-rate forecast"
- SEPN (Septerna, Inc.) score 3.3 — "Promoter shareholding in listed companies hits three-year high at 41.93% in September quar"
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