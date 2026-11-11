# Transmission Layer — board brief · 2026-11-11 01:21Z

data as of **2026-11-11** · 97 series · 8 red / 38 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.75, 5d in regime; vol-pct None, breadth-off 0.75, Markov P(high-vol) 0.221)
- [INVERTED] **safe_haven_gold** — corr20 -0.13, corr60 -0.21, contra nifty_50 corr20=0.29, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.9, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.12, corr60 0.12, last shift 2026-09-10. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.19, corr60 0.05, last shift 2026-09-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.9, last shift 2026-09-23. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.33, corr60 -0.0, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.1, corr60 -0.1, last shift 2026-08-12. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.34, corr60 0.3, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.508** (n=1129) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.819** (n=2158) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.15] cross-asset · 7 series ↑
- nifty_50 [INDICES]: last 25044.65, z20 2.81, zc 1.80, resid-z 2.78 [unexplained], 1d 0.06%, |z20|=2.81
- dyn_muthootfin_ns [EQUITIES]: last 2917.60, z20 2.64, zc 0.28, resid-z -0.76 [quiet], 1d 1.69%, |z20|=2.64
- dyn_bajfinance_ns [EQUITIES]: last 1064.85, z20 2.28, zc 0.74, resid-z -0.69 [quiet], 1d -2.11%, |z20|=2.28
- nifty_metal [INDICES]: last 12664.75, z20 2.22, zc 0.45, resid-z -1.15 [quiet], 1d -0.11%, |z20|=2.22
- dyn_jiofin_bo [EQUITIES]: last 229.95, z20 2.18, zc 0.25, resid-z -1.10 [quiet], 1d -0.28%, |z20|=2.18
- nifty_midcap_100 [INDICES]: last 61018.65, z20 2.09, zc 0.00, resid-z -2.77 [unexplained], 1d 0.66%, |z20|=2.09
- nifty_fmcg [INDICES]: last 46660.10, z20 1.91, zc 0.49, resid-z -1.60 [unexplained], 1d -0.27%, |z20|=1.91
- **Mechanism**: cross-asset · 7 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 1.08).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_adanient_bo (rho 0.735 via nifty_metal, z 1.06, reacted); dyn_indusindbk_bo (rho 0.634 via nifty_midcap_100, z 1.32, reacted); dyn_indianb_ns (rho 0.612 via nifty_midcap_100, z 4.09, reacted); dyn_policybzr_ns (rho 0.53 via nifty_midcap_100, z -1.36, reacted); midcap_largecap_ratio (rho 0.511 via nifty_midcap_100, z -1.5, reacted)
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.506 vs nifty_50, historically leads by 5d
- Watch next: taiwan_weighted (inverse) — not yet - watch; rho -0.534 vs nifty_50
- Watch next: dyn_tatatech_ns (co-move) — not yet - watch; rho 0.505 vs dyn_jiofin_bo
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.501 vs dyn_muthootfin_ns
- **India receivers**: dyn_adanient_bo (rho 0.735, z 1.06); dyn_indusindbk_bo (rho 0.634, z 1.32); dyn_indianb_ns (rho 0.612, z 4.09); dyn_policybzr_ns (rho 0.53, z -1.36)
- Source: Stock market outlook today, 11 Nov: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-11. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-11-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-11794357789353.html
- Source: Nifty PSU Bank Index Performance: Bank of India, UCO Bank among 7 stocks rebound 15–56% from 1-yr lows - here’s why — Mint Markets, 2026-11-10. https://www.livemint.com/market/stock-market-news/nifty-psu-bank-index-performance-bank-of-india-uco-bank-among-7-stocks-rebound-15-56-from-1-yr-lows-here-s-why-11794321816668.html
- Source: Mutual funds' Nifty 50 allocation falls to 21-year low in Q2 — BusinessLine Mkts, 2026-11-10. https://www.thehindubusinessline.com/markets/mutual-funds-nifty-50-allocation-falls-to-21-year-low/article71685515.ece
- Historical analogues: 2025-07-21 (d=1.08), 2025-07-11 (d=1.35), 2025-12-23 (d=1.37)

### [AMBER 5.79] cross-asset · 3 series ↓
- eth_usd [CRYPTO]: last 2044.80, z20 -2.47, zc -0.12, resid-z -0.32 [quiet], 1d -0.47%, |z20|=2.47
- btc_usd [CRYPTO]: last 73390.90, z20 -1.92, zc -0.16, resid-z -0.06 [quiet], 1d -0.39%, |z20|=1.92
- dyn_coin [EQUITIES]: last 132.16, z20 -1.78, zc -0.60, resid-z 0.35 [quiet], 1d -2.89%, 1y-pct=0
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.12).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.756 vs eth_usd
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.739 vs eth_usd
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.523 vs eth_usd, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.666 vs eth_usd
- Watch next: vix (inverse) — not yet - watch; rho -0.588 vs eth_usd
- Source: U.S. Midterm Shake-Up Could Reshape Global Oil and Gas Markets — OilPrice, 2026-11-10. https://oilprice.com/Energy/Energy-General/US-Midterm-Shake-Up-Could-Reshape-Global-Oil-and-Gas-Markets.html
- Source: Iran War Set to Drive A Drop in Global Fossil Fuel Emissions in 2026 — OilPrice, 2026-11-10. https://oilprice.com/Latest-Energy-News/World-News/Iran-War-Set-to-Drive-A-Drop-in-Global-Fossil-Fuel-Emissions-in-2026.html
- Source: HYPERSCALE DATA SELLS REMAINING BITCOIN RESERVES TO REDUCE DEBT AND FUND MICHIGAN AI DATA CENTER HYPERSCALE DATA - SELLS 211.56 BITCOIN FOR GROSS PROCEEDS OF $16 MLN HYPERSCALE DATA - USES PROCEEDS TO PAY DOWN DEBT AND FUND MICHIGAN AI DATA CENTER DEVELOPMENT — DeItaone, 2026-11-10. https://t.me/walter_bloomberg/38295
- Historical analogues: 2026-05-22 (d=0.12), 2025-04-10 (d=0.5), 2025-10-16 (d=0.67)

### [RED 5.08] dyn_nvda ↓
- dyn_nvda [EQUITIES]: last 168.79, z20 -3.08, zc -1.30, resid-z 0.97 [quiet], 1d -5.53%, |z20|=3.08; 1y-pct=1
- **Mechanism**: dyn_nvda ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.653 vs dyn_nvda, historically leads by 5d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.562 vs dyn_nvda, historically leads by 5d
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.639 vs dyn_nvda
- Watch next: vix (inverse) — not yet - watch; rho -0.616 vs dyn_nvda
- Source: Meet the former prosecutor Nvidia hired to investigate the Jensen Huang spy scandal — MarketWatch Top, 2026-11-10. https://www.marketwatch.com/story/meet-the-former-prosecutor-nvidia-hired-to-investigate-the-jensen-huang-spy-scandal-e8078f67?mod=mw_rss_topstories
- Source: Nvidia could soon face tougher export rules, making it harder to sell chips to China — MarketWatch Top, 2026-11-10. https://www.marketwatch.com/story/nvidia-could-soon-face-tougher-export-rules-making-it-harder-to-sell-chips-to-china-69c88cc8?mod=mw_rss_topstories
- Source: NVIDIA SHARES FALL 7.06% TO SESSION LOW — DeItaone, 2026-11-10. https://t.me/walter_bloomberg/38359
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-24 (d=0.03), 2026-05-04 (d=0.03)

### [RED 4.92] equities · 2 series ↑
- dyn_indianb_ns [EQUITIES]: last 933.70, z20 4.09, zc 0.51, resid-z -0.16 [quiet], 1d 3.51%, |z20|=4.09
- dyn_karurvysya_ns [EQUITIES]: last 370.00, z20 2.01, zc 1.01, resid-z 0.92 [quiet], 1d -0.01%, |z20|=2.01; 1y-pct=99
- **Mechanism**: equities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.612 via dyn_indianb_ns, z 2.09, reacted); dyn_jiofin_bo (rho 0.587 via dyn_indianb_ns, z 2.18, reacted); dyn_bajfinance_ns (rho 0.525 via dyn_indianb_ns, z 2.28, reacted); nifty_50 (rho 0.516 via dyn_indianb_ns, z 2.81, reacted); dyn_muthootfin_ns (rho 0.492 via dyn_indianb_ns, z 2.64, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.612, z 2.09); dyn_jiofin_bo (rho 0.587, z 2.18); dyn_bajfinance_ns (rho 0.525, z 2.28); nifty_50 (rho 0.516, z 2.81)
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-04 (d=0.46), 2025-02-01 (d=0.51)

### [AMBER 4.71] commodities · 2 series ↓
- wti [COMMODITIES]: last 86.62, z20 -1.88, zc 0.00, resid-z -0.43 [quiet], 1d 0.00%, |z20|=1.88
- brent [COMMODITIES]: last 92.28, z20 -1.85, zc 0.01, resid-z -0.56 [quiet], 1d 0.02%, |z20|=1.85; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.5 via wti, z 2.64, reacted)
- Watch next: vix (co-move) — not yet - watch; rho 0.556 vs brent, historically leads by 1d
- Watch next: dyn_gs (inverse) — not yet - watch; rho -0.551 vs brent
- Watch next: dyn_demz (inverse) — not yet - watch; rho -0.55 vs wti
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.507 vs wti
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.503 vs wti
- **India receivers**: dyn_muthootfin_ns (rho -0.5, z 2.64)
- Source: Middle East Oil Flows Far from Normal Despite Signs of Oversupply — OilPrice, 2026-11-11. https://oilprice.com/Energy/Crude-Oil/Middle-East-Oil-Flows-Far-from-Normal-Despite-Signs-of-Oversupply.html
- Source: South Sudan Courts Oil Investors as Sudan’s Warring Forces Take Their Share — OilPrice, 2026-11-11. https://oilprice.com/Energy/Crude-Oil/South-Sudan-Courts-Oil-Investors-as-Sudans-Warring-Forces-Take-Their-Share.html
- Source: A ‘Geologic Freak’ in Arkansas Is Big Oil’s New Lithium Bet — OilPrice, 2026-11-10. https://oilprice.com/Metals/Commodities/A-Geologic-Freak-in-Arkansas-Is-Big-Oils-New-Lithium-Bet.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [AMBER 4.5] dyn_hdb ↑
- dyn_hdb [EQUITIES]: last 25.99, z20 2.50, zc 0.36, resid-z 1.20 [quiet], 1d 0.70%, |z20|=2.50
- **Mechanism**: dyn_hdb ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.373 via dyn_hdb, z 2.64, reacted); nifty_50 (rho 0.37 via dyn_hdb, z 2.81, reacted)
- **India receivers**: dyn_muthootfin_ns (rho 0.373, z 2.64); nifty_50 (rho 0.37, z 2.81)
- Source: Retail investors shed stocks, but crowd into Reliance, HDFC Bank — Mint Markets, 2026-11-10. https://www.livemint.com/market/stock-market-news/retail-investors-reliance-hdfc-bank-fpis-stock-markets-india-11794288650697.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [RED 4.43] indices · 3 series ↑
- stoxx_50 [INDICES]: last 6337.48, z20 3.11, zc 0.73, resid-z 1.51 [unexplained], 1d 0.75%, |z20|=3.11
- cac_40 [INDICES]: last 8293.51, z20 2.51, zc 0.79, resid-z 1.42 [quiet], 1d 0.73%, |z20|=2.51
- dax [INDICES]: last 26387.94, z20 1.91, zc 0.36, resid-z 1.51 [unexplained], 1d 0.46%, |z20|=1.91; 1y-pct=98
- **Mechanism**: indices · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.535 via cac_40, z 2.64, reacted); nifty_midcap_100 (rho 0.497 via dax, z 2.09, reacted); nifty_fmcg (rho 0.496 via cac_40, z 1.91, reacted); dyn_jiofin_bo (rho 0.464 via cac_40, z 2.18, reacted); dyn_tataelxsi_ns (rho 0.436 via cac_40, z 0.96, quiet)
- Watch next: ftse_100 (co-move) — not yet - watch; rho 0.705 vs stoxx_50, historically leads by 2d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.594 vs stoxx_50, historically leads by 5d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.533 vs stoxx_50, historically leads by 5d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.504 vs stoxx_50, historically leads by 5d
- **India receivers**: dyn_muthootfin_ns (rho 0.535, z 2.64); nifty_midcap_100 (rho 0.497, z 2.09); nifty_fmcg (rho 0.496, z 1.91); dyn_jiofin_bo (rho 0.464, z 2.18)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-16 (d=0.39), 2025-09-01 (d=0.4)

### [AMBER 4.18] usd_inr ↓
- usd_inr [FX]: last 93.92, z20 -2.18, zc -0.07, resid-z 0.04 [quiet], 1d -0.03%, |z20|=2.18; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_havells_ns (rho -0.418 via usd_inr, z 2.52, reacted); dyn_indusindbk_bo (rho -0.375 via usd_inr, z 1.32, reacted); nifty_it (rho -0.35 via usd_inr, z 0.71, quiet)
- **India receivers**: dyn_havells_ns (rho -0.418, z 2.52); dyn_indusindbk_bo (rho -0.375, z 1.32); nifty_it (rho -0.35, z 0.71)
- Source: Weekly Rupee View: Poised for further gains — BusinessLine Mkts, 2026-11-10. https://www.thehindubusinessline.com/portfolio/technical-analysis/weekly-rupee-viewpoised-for-further-gains/article71685989.ece
- Source: Rupee’s 5-day winning streak ends with the currency closing at ₹93.93 — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/forex/rupees-5-day-winning-streak-ends-with-the-currency-closing-at-9393/article71683133.ece
- Source: FPI investments in FAR G-Secs rise nearly ₹8,000 cr as rupee gains, bond yields ease — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/fpi-investments-in-far-g-secs-rise-nearly-8000-cr-as-rupee-gains-bond-yields-ease/article71682301.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

## Watchlist (below surfacing floor)
dyn_tech ↑ (4.12), usd_jpy ↑ (4.05), natgas ↑ (3.89), dyn_atherenerg_ns ↑ (3.74), dyn_lth ↑ (3.59), comex_copper ↓ (3.51), dyn_schd ↑ (3.09), dyn_4417_t ↑ (3.04), comex_silver ↓ (2.85), cross-asset · 2 series ↑ (2.84), eur_inr ↓ (2.56), dyn_havells_ns ↑ (2.52)

## India macro
- nifty_50: 25044.6504 (1d 0.06%, z20 2.81, flag red)
- nifty_midcap_100: 61018.6484 (1d 0.66%, z20 2.09, flag amber)
- usd_inr: 93.9180 (1d -0.03%, z20 -2.18, flag amber)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4364 (1d 0.60%, z20 -1.50, flag none)
- Next India prints: NSDL FPI flows T-0d · India CPI T-1d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 67.4 — "China’s Coal Buyers Resist Waiver Demands in New Indonesian Deals"
- INOXINDIA.NS (INOX INDIA LIMITED) score 65.3 — "Nifty PSU Bank Index Performance: Bank of India, UCO Bank among 7 stocks rebound 15–56% fr"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 65.0 — "Nifty PSU Bank Index Performance: Bank of India, UCO Bank among 7 stocks rebound 15–56% fr"
- INDIANB.NS (INDIAN BANK) score 49.9 — "Defaults Rattle Brazil’s Shadow Banks, Spark Regulatory Scrutiny"
- BAC (Bank of America Corporation) score 43.7 — "Iran: Rezaei to Al Mayadeen: We asked the Americans to provide a frank and clear response "
- TECHM.NS (TECH MAHINDRA LIMITED) score 38.3 — "DEMOCRATIC SENATE LEADER SCHUMER CALLS TRUMP'S DEFENSE OF NVIDIA'S HUANG "TROUBLING" SCHUM"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 37.6 — "DEMOCRATIC SENATE LEADER SCHUMER CALLS TRUMP'S DEFENSE OF NVIDIA'S HUANG "TROUBLING" SCHUM"
- TECH (Bio-Techne Corp) score 37.6 — "DEMOCRATIC SENATE LEADER SCHUMER CALLS TRUMP'S DEFENSE OF NVIDIA'S HUANG "TROUBLING" SCHUM"
- NVDA (NVIDIA Corporation) score 36.3 — "NVIDIA SHARES EXTENDS LOSSES; LAST DOWN 5.4%"
- 301077.SZ (CHINASTARS) score 36.2 — "NVDA - NVIDIA CEO'S ALLEGED AFFAIR AIDED $7.5 BILLION IN CHIP SHIPMENTS TO CHINA The Infor"
- TGT (Target Corporation) score 35.9 — "Anthropic targets $90 billion IPO at $1.4 trillion valuation"
- HDB (HDFC Bank Limited) score 32.6 — "Defaults Rattle Brazil’s Shadow Banks, Spark Regulatory Scrutiny"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 31.2 — "Defaults Rattle Brazil’s Shadow Banks, Spark Regulatory Scrutiny"
- IDBI.NS (IDBI BANK LIMITED) score 31.2 — "Defaults Rattle Brazil’s Shadow Banks, Spark Regulatory Scrutiny"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 31.2 — "Defaults Rattle Brazil’s Shadow Banks, Spark Regulatory Scrutiny"
- OHI (Omega Healthcare Investors, In) score 29.9 — "South Sudan Courts Oil Investors as Sudan’s Warring Forces Take Their Share"
- COIN (Coinbase Global, Inc.) score 27.7 — "Iran War Set to Drive A Drop in Global Fossil Fuel Emissions in 2026"
- CHKP (Check Point Software Technolog) score 21.7 — "HUL dividend 2026: Tomorrow is the last day to buy | Check payout amount, record date, his"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.3 — "Midterm Results Could Trip Trump’s Energy Independence Plans"
- LTH (Life Time Group Holdings, Inc.) score 19.5 — "U.S. 10-YEAR TREASURY YIELD RISES BACK TO 5% FOR FIRST TIME IN 12 DAYS"
- BOND (PIMCO Active Bond Exchange-Tra) score 18.4 — "Patna Municipal Corporation lists Bihar’s first municipal bond on NSE"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 13.6 — "Upcoming IPOs: SEBI clears 8 issues, including Mahanadi Coalfields, Veritas Finance and Sa"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 12.6 — "Gold rates today 10 Nov Tuesday: Can price rise to  ₹1.48 lakh per 10 gm? What experts say"
- SCHD (Schwab US Dividend Equity ETF) score 11.7 — "HUL dividend 2026: Tomorrow is the last day to buy | Check payout amount, record date, his"
- BZ=F (Brent Crude Oil Last Day Finan) score 10.7 — "NVIDIA SHARES EXTENDS LOSSES; LAST DOWN 5.4%"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 10.4 — "Upcoming IPOs: SEBI clears 8 issues, including Mahanadi Coalfields, Veritas Finance and Sa"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.5 — "Tata Steel’s domestic business shines in Q2; Netherlands uncertainty poses risk"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.5 — "Tata Steel’s domestic business shines in Q2; Netherlands uncertainty poses risk"
- JIOFIN.BO (Jio Financial Services Limited) score 9.4 — "NVDA - NVIDIA DOWNGRADED TO HOLD AS $165 BILLION AI FINANCING EXPOSURE RAISES CONCERNS Ale"
- RS (Reliance, Inc.) score 7.7 — "AMFI Rejig: Reliance's Jio Platforms, NSE, Lenskart, LG among 7 stocks set for large cap u"
- META (Meta) score 7.6 — "Gold vs silver vs copper vs platinum: Which metal could deliver the biggest returns in Sam"
- DEMZ (Democratic Large Cap Core ETF) score 7.2 — "DEMOCRATIC SENATE LEADER SCHUMER CALLS TRUMP'S DEFENSE OF NVIDIA'S HUANG "TROUBLING" SCHUM"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.1 — "Stocks in focus: SBI, L&T, Alkem Lab, Adani Enterprises, BEL, GRSE, BHEL, Waaree Renewable"
- JEF (Jefferies Financial Group Inc.) score 5.2 — "Easing oil, bond yields to support bank margins, RBI rate hikes likely in Dec: Jefferies"
- GS (Goldman Sachs Group, Inc. (The) score 4.8 — "Global equities to rely on earnings growth as investor risk appetite weakens: Goldman Sach"
- SEPN (Septerna, Inc.) score 4.2 — "Promoter shareholding in listed companies hits three-year high at 41.93% in September quar"
- VT (Vanguard Total World Stock Ind) score 3.9 — "Anthropic's potential mega IPO joins ranks of world's biggest stock market listings"
- JUSTDIAL.BO (JUST DIAL LTD.) score 3.9 — "Actor Justin Baldoni quietly sold his L.A. home for $2.1 million after moving to Nashville"
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