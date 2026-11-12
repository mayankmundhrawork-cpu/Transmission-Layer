# Transmission Layer — board brief · 2026-11-12 01:55Z

data as of **2026-11-12** · 97 series · 10 red / 35 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.833, 6d in regime; vol-pct None, breadth-off 0.833, Markov P(high-vol) 0.206)
- [INVERTED] **safe_haven_gold** — corr20 -0.09, corr60 -0.2, contra nifty_50 corr20=0.29, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.88, corr60 0.84, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.12, corr60 0.12, last shift 2026-09-11. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.2, corr60 0.05, last shift 2026-09-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.91, last shift 2026-09-24. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.33, corr60 -0.0, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.1, corr60 -0.1, last shift 2026-08-12. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.36, corr60 0.32, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.511** (n=1145) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=2149) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

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
- Source: Sensex today | Stock Market Live Updates: Rupee closes Wednesday's session at 7-month high of 93.69 as FPI inflows, lower crude prices boost sentiment — BusinessLine Mkts, 2026-11-12. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-12-november-2026/article71689385.ece
- Source: Bajaj Finance unveils share sale to raise up to $1.25 billion — ET Markets, 2026-11-12. https://economictimes.indiatimes.com/markets/stocks/news/bajaj-finance-unveils-share-sale-to-raise-up-to-1-25-billion/articleshow/135751856.cms
- Source: Stock market outlook today, 12 Nov: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-12. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-12-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-11794444171874.html
- Historical analogues: 2025-07-21 (d=1.09), 2025-12-23 (d=1.43), 2025-07-11 (d=1.45)

### [RED 5.92] dxy ↑
- dxy [FX]: last 102.85, z20 2.92, zc 0.01, resid-z 2.61 [unexplained], 1d 0.00%, 20d range extreme; |z20|=2.92; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.579 vs dxy, historically leads by 1d
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-10 (d=0.03), 2025-05-14 (d=0.06)

### [AMBER 5.43] cross-asset · 3 series ↓
- eth_usd [CRYPTO]: last 2048.08, z20 -2.11, zc -0.36, resid-z 0.41 [quiet], 1d -1.39%, |z20|=2.11
- btc_usd [CRYPTO]: last 73599.46, z20 -1.67, zc -0.40, resid-z -0.17 [quiet], 1d -0.90%, |z20|=1.67
- dyn_coin [EQUITIES]: last 136.30, z20 -1.33, zc 0.66, resid-z 0.35 [quiet], 1d 3.16%, 1y-pct=1
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.26).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.748 vs eth_usd
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.536 vs eth_usd, historically leads by 1d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.707 vs eth_usd
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.668 vs eth_usd
- Watch next: vix (inverse) — not yet - watch; rho -0.59 vs eth_usd
- Source: Global Market Today: Asian stocks mixed as Nvidia turmoil hits AI-linked shares — ET Markets, 2026-11-12. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-today-us-stock-futures-fall-as-nvidia-turmoil-deepens/articleshow/135751953.cms
- Source: Global Power Grid Expansion Surges 50% to Record High — OilPrice, 2026-11-12. https://oilprice.com/Energy/Energy-General/Global-Power-Grid-Expansion-Surges-50-to-Record-High.html
- Source: How a Super El Niño Could Reshape Global Coal Markets — OilPrice, 2026-11-11. https://oilprice.com/Energy/Energy-General/How-a-Super-El-Nio-Could-Reshape-Global-Coal-Markets.html
- Historical analogues: 2026-05-22 (d=0.26), 2025-04-10 (d=0.43), 2025-10-22 (d=0.48)

### [RED 5.38] usd_jpy ↑
- usd_jpy [FX]: last 159.68, z20 3.38, zc 1.22, resid-z 0.80 [quiet], 1d 0.61%, |z20|=3.38
- **Mechanism**: usd_jpy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho 0.402 via usd_jpy, z -0.33, quiet)
- **India receivers**: dyn_idbi_ns (rho 0.402, z -0.33)
- Source: Dollar near one-month high as yen edges toward 160 — ET Markets, 2026-11-12. https://economictimes.indiatimes.com/markets/forex/forex-news/dollar-near-one-month-high-as-yen-edges-toward-160/articleshow/135751707.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2025-07-30 (d=0.01)

### [RED 4.68] indices · 3 series ↑
- stoxx_50 [INDICES]: last 6392.53, z20 3.36, zc 1.06, resid-z 0.80 [quiet], 1d 1.02%, |z20|=3.36
- cac_40 [INDICES]: last 8330.49, z20 2.38, zc 0.72, resid-z 1.00 [quiet], 1d 0.63%, |z20|=2.38
- dax [INDICES]: last 26644.39, z20 2.37, zc 0.99, resid-z 1.39 [quiet], 1d 1.13%, |z20|=2.37; 1y-pct=100
- **Mechanism**: indices · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.502 via cac_40, z 2.09, reacted); nifty_fmcg (rho 0.501 via cac_40, z 2.1, reacted); nifty_midcap_100 (rho 0.497 via dax, z 2.18, reacted); dyn_jiofin_bo (rho 0.449 via cac_40, z 1.76, reacted); dyn_tataelxsi_ns (rho 0.447 via cac_40, z 0.83, quiet)
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.519 vs stoxx_50, historically leads by 5d
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.509 vs stoxx_50, historically leads by 2d
- **India receivers**: dyn_muthootfin_ns (rho 0.502, z 2.09); nifty_fmcg (rho 0.501, z 2.1); nifty_midcap_100 (rho 0.497, z 2.18); dyn_jiofin_bo (rho 0.449, z 1.76)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-16 (d=0.39), 2025-09-01 (d=0.4)

### [AMBER 4.63] commodities · 2 series ↓
- wti [COMMODITIES]: last 85.48, z20 -1.80, zc 0.00, resid-z 0.62 [quiet], 1d 0.00%, |z20|=1.80
- brent [COMMODITIES]: last 91.57, z20 -1.69, zc 0.00, resid-z 0.90 [quiet], 1d 0.00%, |z20|=1.69; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.507 via wti, z 2.09, reacted)
- Watch next: vix (co-move) — not yet - watch; rho 0.564 vs brent, historically leads by 1d
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.578 vs brent
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.507 vs wti
- Watch next: sp500 (inverse) — not yet - watch; rho -0.504 vs wti
- **India receivers**: dyn_muthootfin_ns (rho -0.507, z 2.09)
- Source: Sensex today | Stock Market Live Updates: Rupee closes Wednesday's session at 7-month high of 93.69 as FPI inflows, lower crude prices boost sentiment — BusinessLine Mkts, 2026-11-12. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-12-november-2026/article71689385.ece
- Source: Who Will Buy Sable’s Oil if California Keeps Closing Refineries? — OilPrice, 2026-11-12. https://oilprice.com/Energy/Crude-Oil/Who-Will-Buy-Sables-Oil-if-California-Keeps-Closing-Refineries.html
- Source: Oil Steadies After Slump as Iran War Talks Make Little Progress — Mint Markets, 2026-11-11. https://www.livemint.com/market/oil-steadies-after-slump-as-iran-war-talks-make-little-progress-11794439901889.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [AMBER 4.16] usd_inr ↓
- usd_inr [FX]: last 93.93, z20 -2.16, zc -0.05, resid-z -0.33 [quiet], 1d -0.02%, |z20|=2.16; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_havells_ns (rho -0.473 via usd_inr, z 2.05, reacted); nifty_it (rho -0.42 via usd_inr, z 0.49, quiet); dyn_indianb_ns (rho -0.395 via usd_inr, z 2.99, reacted); dyn_tataelxsi_ns (rho -0.391 via usd_inr, z 0.83, quiet); dyn_bajfinance_ns (rho -0.37 via usd_inr, z 2.22, reacted)
- **India receivers**: dyn_havells_ns (rho -0.473, z 2.05); nifty_it (rho -0.42, z 0.49); dyn_indianb_ns (rho -0.395, z 2.99); dyn_tataelxsi_ns (rho -0.391, z 0.83)
- Source: Sensex today | Stock Market Live Updates: Rupee closes Wednesday's session at 7-month high of 93.69 as FPI inflows, lower crude prices boost sentiment — BusinessLine Mkts, 2026-11-12. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-12-november-2026/article71689385.ece
- Source: Rupee closes at seven-month high of 93.69 as FPI inflows, lower crude prices boost sentiment — BusinessLine Mkts, 2026-11-11. https://www.thehindubusinessline.com/markets/forex/rupee-closes-at-seven-month-high-of-9369-as-fpi-inflows-lower-crude-prices-boost-sentiment/article71689839.ece
- Source: Rupee rises 7 paise to close at 93.70 against US dollar — BusinessLine Mkts, 2026-11-11. https://www.thehindubusinessline.com/markets/forex/rupee-rises-7-paise-to-close-at-9370-against-us-dollar/article71689281.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [AMBER 4.15] dyn_nvda ↓
- dyn_nvda [EQUITIES]: last 173.85, z20 -2.15, zc 0.66, resid-z 0.97 [quiet], 1d 2.94%, |z20|=2.15; 1y-pct=3
- **Mechanism**: dyn_nvda ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.819 vs dyn_nvda, historically leads by 3d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.735 vs dyn_nvda, historically leads by 4d
- Watch next: vix (inverse) — not yet - watch; rho -0.674 vs dyn_nvda
- Source: Nvidia’s stock drops as the board reportedly prepares to remove CEO Jensen Huang — MarketWatch Top, 2026-11-12. https://www.marketwatch.com/story/nvidias-stock-drops-as-the-board-reportedly-prepares-to-remove-ceo-jensen-huang-9edee58d?mod=mw_rss_topstories
- Source: Global Market Today: Asian stocks mixed as Nvidia turmoil hits AI-linked shares — ET Markets, 2026-11-12. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-today-us-stock-futures-fall-as-nvidia-turmoil-deepens/articleshow/135751953.cms
- Source: Nasdaq futures fall as Nvidia sinks 8% after hours on report board may oust Huang — MarketWatch Top, 2026-11-12. https://www.marketwatch.com/story/nasdaq-futures-fall-as-nvidia-sinks-8-after-hours-on-report-board-may-oust-huang-e99b898d?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-24 (d=0.03), 2026-05-04 (d=0.03)

## Watchlist (below surfacing floor)
dyn_hdb ↑ (4.09), equities · 2 series ↑ (3.94), eur_inr ↓ (3.87), commodities · 2 series ↓ (3.74), natgas ↑ (3.64), dyn_tech ↑ (3.48), dyn_lth ↑ (3.46), dyn_schd ↑ (3.31), eur_usd ↓ (3.18), dyn_4417_t ↑ (2.94), cross-asset · 2 series ↑ (2.7), dyn_rs ↑ (2.41)

## India macro
- nifty_50: 25255.0508 (1d 0.84%, z20 2.55, flag red)
- nifty_midcap_100: 61515.0508 (1d 0.81%, z20 2.18, flag amber)
- usd_inr: 93.9250 (1d -0.02%, z20 -2.16, flag amber)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4358 (1d -0.03%, z20 -1.37, flag none)
- Next India prints: India CPI T-0d · NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 75.6 — "Stock recommendations for 12 November from MarketSmith India"
- INOXINDIA.NS (INOX INDIA LIMITED) score 73.0 — "Stock recommendations for 12 November from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 72.8 — "Stock recommendations for 12 November from MarketSmith India"
- INDIANB.NS (INDIAN BANK) score 52.9 — "MARSH PUSHES FED TO EASE BANK CAPITAL RULES FOR AI LOANS Marsh ($MRSH) is lobbying US regu"
- BAC (Bank of America Corporation) score 47.2 — "MARSH PUSHES FED TO EASE BANK CAPITAL RULES FOR AI LOANS Marsh ($MRSH) is lobbying US regu"
- NVDA (NVIDIA Corporation) score 41.9 — "COREWEAVE CEO SAYS NVIDIA IS NOT ONE PERSON; WILL CONTINUE TO BE A GREAT PARTNER FOR US - "
- HDB (HDFC Bank Limited) score 40.2 — "MARSH PUSHES FED TO EASE BANK CAPITAL RULES FOR AI LOANS Marsh ($MRSH) is lobbying US regu"
- TGT (Target Corporation) score 38.2 — "BAIRD SLASHES NVIDIA PRICE TARGET 60%, WARNS OF AI SLOWDOWN Baird downgraded Nvidia ($NVDA"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 37.3 — "MARSH PUSHES FED TO EASE BANK CAPITAL RULES FOR AI LOANS Marsh ($MRSH) is lobbying US regu"
- IDBI.NS (IDBI BANK LIMITED) score 37.3 — "MARSH PUSHES FED TO EASE BANK CAPITAL RULES FOR AI LOANS Marsh ($MRSH) is lobbying US regu"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 37.3 — "MARSH PUSHES FED TO EASE BANK CAPITAL RULES FOR AI LOANS Marsh ($MRSH) is lobbying US regu"
- TECHM.NS (TECH MAHINDRA LIMITED) score 36.5 — "HCL Tech Share Price Highlights: HCL Tech Stock Price History"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 35.9 — "HCL Tech Share Price Highlights: HCL Tech Stock Price History"
- TECH (Bio-Techne Corp) score 35.9 — "HCL Tech Share Price Highlights: HCL Tech Stock Price History"
- 301077.SZ (CHINASTARS) score 34.2 — "BESSENT CONFRONTS LUTNICK OVER NVIDIA CHINA CHIP SCANDAL Treasury Secretary Scott Bessent "
- OHI (Omega Healthcare Investors, In) score 27.2 — "Market angst is driving investors into low-volatility stocks as AI trade stumbles"
- COIN (Coinbase Global, Inc.) score 24.8 — "Global Power Grid Expansion Surges 50% to Record High"
- CHKP (Check Point Software Technolog) score 23.4 — "Top 2 stocks to buy for short-term: Canara Bank, Pine Labs by Nagaraj Shetti - Check stop "
- BOND (PIMCO Active Bond Exchange-Tra) score 21.0 — "Falling oil prices are no longer enough to bring down borrowing costs in the world’s most "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.5 — "Bloom Energy’s stock rallies as data-center jitters subside"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 19.9 — "Adani to finance Chile copper project to secure long-term supply for Mundra smelter"
- LTH (Life Time Group Holdings, Inc.) score 19.2 — "Sensex today | Stock Market Live Updates: Rupee closes Wednesday's session at 7-month high"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 15.7 — "Adani to finance Chile copper project to secure long-term supply for Mundra smelter"
- SCHD (Schwab US Dividend Equity ETF) score 13.7 — "Edelweiss Alternatives’ H1FY27 profit rises 35% to ₹169 crore; declares ₹7 interim dividen"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.7 — "Tata Steel Share Price Highlights: Tata Steel Stock Price History"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.7 — "Tata Steel Share Price Highlights: Tata Steel Stock Price History"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 11.7 — "Trump says Iran war ‘effectively over’: How's it likely to impact Sensex, Nifty, gold and "
- BZ=F (Brent Crude Oil Last Day Finan) score 11.4 — "CRWV - COREWEAVE SHARES EXTEND GAINS TO TOUCH A TWO WEEK HIGH; LAST UP 20.8%"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.4 — "Adani to finance Chile copper project to secure long-term supply for Mundra smelter"
- JIOFIN.BO (Jio Financial Services Limited) score 9.2 — "Fairfax Financial likely to exit IIFL Finance, sources say"
- CRWV (CoreWeave, Inc.) score 7.5 — "US stocks end higher as CoreWeave results ease AI spending worries: Stock Market Highlight"
- RS (Reliance, Inc.) score 6.1 — "AMFI Rejig: Reliance's Jio Platforms, NSE, Lenskart, LG among 7 stocks set for large cap u"
- META (Meta) score 6.0 — "Gold vs silver vs copper vs platinum: Which metal could deliver the biggest returns in Sam"
- JUSTDIAL.BO (JUST DIAL LTD.) score 5.9 — "Sandisk’s stock just staged a big gain. Here’s how it could march even higher."
- DEMZ (Democratic Large Cap Core ETF) score 5.7 — "DEMOCRATIC SENATE LEADER SCHUMER CALLS TRUMP'S DEFENSE OF NVIDIA'S HUANG "TROUBLING" SCHUM"
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