# Transmission Layer — board brief · 2026-09-25 20:03Z

data as of **2026-09-25** · 97 series · 7 red / 32 amber · 8 events surfaced (22 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.547, 6d in regime; vol-pct 0.38, breadth-off 0.714, Markov P(high-vol) 0.014)
- [INVERTED] **safe_haven_gold** — corr20 -0.54, corr60 -0.41, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.85, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 -0.02, corr60 0.24, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.02, corr60 0.12, last shift 2026-08-12. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.78, corr60 -0.78, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.13, corr60 -0.09, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.08, last shift 2026-08-05. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.43, corr60 0.22, last shift 2026-07-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.474, β 0.2528, p 0.0); driver zc 3.12 → expected 0.765%. Type hit-rate 0.828 (n=2367).
- **SETUP** ust_2y → eur_usd: leads 1d (ccf -0.359, β -0.1201, p 0.0); driver zc 2.28 → expected -0.357%. Type hit-rate 0.828 (n=2367).
- **SETUP** ust_10y → eur_usd: leads 1d (ccf -0.273, β -0.1104, p 0.0); driver zc 3.12 → expected -0.334%. Type hit-rate 0.828 (n=2367).
- Track record · residual_reversion: hit-rate **0.497** (n=1102) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.828** (n=2367) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.17] cross-asset · 5 series ↑
- tips_10y_real [RATES]: last 2.76, z20 2.24, zc 2.66, resid-z 2.44 [unexplained], 1d 4.94%, 1d move +13.0bps ≥ 5bps; |z20|=2.24; 1y-pct=100
- ust_10y [RATES]: last 5.11, z20 2.13, zc 3.12, resid-z 2.67 [unexplained], 1d 3.02%, |z20|=2.13; 1y-pct=100
- ust_30y [RATES]: last 5.40, z20 2.07, zc 2.73, resid-z 2.34 [unexplained], 1d 2.08%, |z20|=2.07; 1y-pct=100
- dyn_bond [EQUITIES]: last 87.70, z20 -1.94, zc 0.36, resid-z -0.20 [quiet], 1d 0.15%, 1y-pct=0
- ust_2y [RATES]: last 4.85, z20 1.87, zc 2.28, resid-z 1.58 [unexplained], 1d 2.97%, |z20|=1.87; 1y-pct=100
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: wti (co-move) — not yet - watch; rho 0.518 vs ust_30y, historically leads by 3d
- Watch next: brent (co-move) — not yet - watch; rho 0.591 vs ust_10y
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.544 vs ust_10y
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.511 vs ust_30y
- Source: YIELD ON 10-YEAR TREASURY NOTE HITS FRESH 19-YEAR HIGH AT 5.2297%; LAST UP 5.92 BASIS POINTS AT 5.221% — DeItaone, 2026-09-25. https://t.me/walter_bloomberg/36200
- Source: U.S. 30-YEAR BOND YIELD TOPS 5.5% FOR FIRST TIME SINCE 2004 — DeItaone, 2026-09-25. https://t.me/walter_bloomberg/36199
- Source: Why investors aren’t buying yet another attempt by the Treasury Department to calm the rattled bond market — MarketWatch Top, 2026-09-25. https://www.marketwatch.com/story/why-investors-arent-buying-yet-another-attempt-by-the-treasury-to-calm-the-rattled-bond-market-b168cac3?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 6.48] dyn_policybzr_ns ↓
- dyn_policybzr_ns [EQUITIES]: last 1166.00, z20 -4.48, zc -0.12, resid-z -1.24 [quiet], 1d -3.41%, |z20|=4.48; 1y-pct=0
- **Mechanism**: dyn_policybzr_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.601 via dyn_policybzr_ns, z -1.66, reacted); nifty_50 (rho 0.477 via dyn_policybzr_ns, z -1.34, reacted)
- Watch next: india_vix (inverse) — not yet - watch; rho -0.711 vs dyn_policybzr_ns
- **India receivers**: nifty_midcap_100 (rho 0.601, z -1.66); nifty_50 (rho 0.477, z -1.34)
- Source: How to trade PB Fintech shares after falling 12% from day’s high? This technical analyst explains — ET Markets, 2026-09-25. https://economictimes.indiatimes.com/markets/stocks/news/how-to-trade-pb-fintech-shares-after-falling-12-from-days-high-this-technical-analyst-explains/articleshow/134477427.cms
- Source: PB Fintech's 36% bloodbath rattles market, but Jefferies stays bullish. What does it see in Policybazaar parent? — ET Markets, 2026-09-25. https://economictimes.indiatimes.com/markets/stocks/news/pb-fintechs-36-bloodbath-rattles-market-but-jefferies-stays-bullish-what-does-it-see-in-policybazaar-parent/articleshow/134475050.cms
- Source: PB Fintech shares slump 40% in two sessions| What Jefferies, Morgan Stanley, BofA say on the stock — Mint Markets, 2026-09-25. https://www.livemint.com/market/stock-market-news/pb-fintech-shares-slump-40-in-two-sessions-what-jefferies-morgan-stanley-bofa-say-on-the-stock-11790308344209.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-16 (d=0.02), 2025-01-30 (d=0.03)

### [AMBER 6.38] commodities · 2 series ↓
- brent [COMMODITIES]: last 97.40, z20 -0.55, zc -3.03, resid-z -3.07 [unexplained], 1d -8.63%, 1-session move -8.63% ≥ 1.5%
- wti [COMMODITIES]: last 92.29, z20 -0.52, zc -0.87, resid-z -0.89 [quiet], 1d -2.45%, 1-session move -2.45% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.548 vs brent, historically leads by 5d
- Watch next: dax (inverse) — not yet - watch; rho -0.524 vs brent, historically leads by 5d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.688 vs brent
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.57 vs brent
- Source: Dollar dips as oil eases, yen jumps on Japan remarks — Mint Markets, 2026-09-25. https://www.livemint.com/market/dollar-dips-as-oil-eases-yen-jumps-on-japan-remarks-11790363504649.html
- Source: Venezuela Oil Output Could Hit 1.8 Million Bpd By 2030, Rystad Says — OilPrice, 2026-09-25. https://oilprice.com/Energy/Crude-Oil/Venezuela-Oil-Output-Could-Hit-18-Million-Bpd-By-2030-Rystad-Says.html
- Source: U.S. Oil, Gas Drilling Perks Up As Pressure Mounts — OilPrice, 2026-09-25. https://oilprice.com/Energy/Crude-Oil/US-Oil-Gas-Drilling-Perks-Up-As-Pressure-Mounts.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-31 (d=0.05), 2025-04-29 (d=0.06)

### [RED 5.48] fx · 4 series ↓
- usd_mxn [FX]: last 17.70, z20 3.82, zc 1.39, resid-z 1.70 [unexplained], 1d 0.90%, |z20|=3.82
- aud_usd [FX]: last 0.70, z20 -2.60, zc -0.09, resid-z 0.14 [quiet], 1d -0.07%, |z20|=2.60
- gbp_usd [FX]: last 1.32, z20 -2.48, zc 0.13, resid-z 0.21 [quiet], 1d 0.06%, |z20|=2.48
- eur_usd [FX]: last 1.14, z20 -2.10, zc 0.44, resid-z 0.83 [quiet], 1d 0.15%, |z20|=2.10; 1y-pct=4
- **Mechanism**: fx · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.498 via usd_mxn, z -4.48, reacted); dyn_icicigi_bo (rho -0.496 via gbp_usd, z 1.06, reacted); dyn_muthootfin_ns (rho 0.466 via aud_usd, z -0.33, quiet); dyn_inoxindia_ns (rho 0.437 via aud_usd, z 0.13, quiet); nifty_50 (rho 0.388 via eur_usd, z -1.34, reacted)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.534 vs aud_usd, historically leads by 3d
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.402 vs eur_usd, historically leads by 1d
- **India receivers**: dyn_policybzr_ns (rho -0.498, z -4.48); dyn_icicigi_bo (rho -0.496, z 1.06); dyn_muthootfin_ns (rho 0.466, z -0.33); dyn_inoxindia_ns (rho 0.437, z 0.13)
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 5.05] natgas ↑
- natgas [COMMODITIES]: last 3.23, z20 3.05, zc -0.41, resid-z -0.83 [quiet], 1d -1.97%, |z20|=3.05
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.441 via natgas, z -4.48, reacted)
- Watch next: gold_silver_ratio (co-move) — not yet - watch; rho 0.131 vs natgas, historically leads by 4d
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.086 vs natgas, historically leads by 4d
- **India receivers**: dyn_policybzr_ns (rho -0.441, z -4.48)
- Source: Why Record Heat Failed to Lift U.S. Natural Gas Prices — OilPrice, 2026-09-25. https://oilprice.com/Latest-Energy-News/World-News/Why-Record-Heat-Failed-to-Lift-US-Natural-Gas-Prices.html
- Source: Henry Hub natural gas prices this summer were 6% lower than last summer — EIA Today in Energy, 2026-09-25. https://www.eia.gov/todayinenergy/detail.php?id=68204
- Source: U.S. to Back Argentina’s First LNG Export Project With $6 Billion Loan — OilPrice, 2026-09-24. https://oilprice.com/Latest-Energy-News/World-News/US-to-Back-Argentinas-First-LNG-Export-Project-With-6-Billion-Loan.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [AMBER 4.78] indices · 2 series ↑
- nasdaq_100 [INDICES]: last 30601.51, z20 1.95, zc 0.32, resid-z 0.30 [quiet], 1d 0.40%, |z20|=1.95; 1y-pct=99
- sp500 [INDICES]: last 7742.32, z20 1.21, zc 0.61, resid-z 0.43 [quiet], 1d 0.50%, 1y-pct=96
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.923 vs nasdaq_100, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.652 vs nasdaq_100, historically leads by 2d
- Watch next: brent (inverse) — not yet - watch; rho -0.612 vs sp500, historically leads by 2d
- Watch next: wti (inverse) — not yet - watch; rho -0.585 vs sp500, historically leads by 2d
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.663 vs nasdaq_100
- Source: Nike’s stock is one of the worst in the S&P 500 — and BofA says it’s not done sliding — MarketWatch Top, 2026-09-25. https://www.marketwatch.com/story/nikes-stock-is-one-of-the-worst-in-the-s-p-500-and-bofa-says-its-not-done-sliding-c99a9107?mod=mw_rss_topstories
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks open higher as AI enthusiasm eases worries over higher oil prices, yields — ET Markets, 2026-09-25. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-us-stock-market-live-updates-nasdaq-sp-500-iran-israel-war-hormuz-deal-brent-crude-oil-inflation-fed-rate-hike-earnings-forecast-nvidia-amd-micron-ai-chip-stock-price-news-25-september-2026/liveblog/134487023.cms
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: AI boom raises ‘too-big-to-fail’ concerns, says Fed's Jeff Schmid; Dow surges 400 pts — ET Markets, 2026-09-25. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-us-stock-market-live-updates-nasdaq-sp-500-iran-israel-war-hormuz-deal-brent-crude-oil-inflation-fed-rate-hike-earnings-forecast-nvidia-amd-micron-ai-chip-stock-price-news-25-september-2026/liveblog/134487023.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-07 (d=0.06), 2026-05-15 (d=0.07)

### [RED 4.72] dyn_indusindbk_bo ↓
- dyn_indusindbk_bo [EQUITIES]: last 912.50, z20 -2.72, zc -0.27, resid-z -1.30 [quiet], 1d -0.84%, |z20|=2.72
- **Mechanism**: dyn_indusindbk_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.459 via dyn_indusindbk_bo, z -1.66, reacted); nifty_50 (rho 0.421 via dyn_indusindbk_bo, z -1.34, reacted); nifty_metal (rho 0.374 via dyn_indusindbk_bo, z -0.21, quiet)
- **India receivers**: nifty_midcap_100 (rho 0.459, z -1.66); nifty_50 (rho 0.421, z -1.34); nifty_metal (rho 0.374, z -0.21)
- Source: IndusInd Bank Share Price Live Updates: IndusInd Bank News — ET Markets, 2026-09-25. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/indusind-bank-stock-price-today-live-25-sep-2026/liveblog/134474146.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-15 (d=0.01), 2026-06-19 (d=0.02)

### [AMBER 4.03] dyn_tech ↑
- dyn_tech [EQUITIES]: last 72.62, z20 2.03, zc 0.62, resid-z 0.33 [quiet], 1d 0.07%, |z20|=2.03; 1y-pct=100
- **Mechanism**: dyn_tech ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: The S&P 500’s newest tech stock is now its best performer — MarketWatch Top, 2026-09-24. https://www.marketwatch.com/story/the-s-p-500s-newest-tech-stock-is-now-its-best-performer-5bfeb6e2?mod=mw_rss_topstories
- Source: Top stocks in focus today: Investors must watch Sterlite Tech, Nykaa, JSW Cement shares on Fri, 25 Sept | Triggers — Mint Markets, 2026-09-24. https://www.livemint.com/market/stock-market-news/top-stocks-in-focus-tomorrow-investors-must-watch-sterlite-tech-nykaa-jsw-cement-shares-on-fri-25-sept-triggers-11790254286938.html
- Source: IT dividend heavyweights compared: TCS, Infosys, HCL Tech, Wipro, Accelya Solutions - Which IT stock has highest yield? — Mint Markets, 2026-09-24. https://www.livemint.com/market/stock-market-news/it-dividend-heavyweights-compared-tcs-infosys-hcl-tech-wipro-accelya-solutions-which-it-stock-has-highest-yield-11790235272610.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.0), 2025-05-19 (d=0.0)

## Watchlist (below surfacing floor)
gold_silver_ratio ↓ (3.9), hang_seng ↓ (3.8), dyn_meta ↑ (3.65), comex_copper ↑ (3.46), dyn_jiofin_bo ↓ (3.39), hy_oas ↑ (3.38), dyn_4417_t ↑ (3.31), dyn_voltas_ns ↓ (3.2), sofr ↑ (1.94), taiwan_weighted ↑ (1.89), usd_brl ↑ (1.78), commodities · 2 series ↑ (1.76)

## India macro
- nifty_50: 23140.5000 (1d 0.34%, z20 -1.34, flag none)
- nifty_midcap_100: 60901.9492 (1d -0.15%, z20 -1.66, flag amber)
- usd_inr: 95.8020 (1d 0.06%, z20 0.87, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6318 (1d -0.48%, z20 -1.37, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 90.5 — "Liqvd Digital India IPO subscribed 5.08 times on final day"
- INOXINDIA.NS (INOX INDIA LIMITED) score 89.4 — "Liqvd Digital India IPO subscribed 5.08 times on final day"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 88.9 — "Liqvd Digital India IPO subscribed 5.08 times on final day"
- INDIANB.NS (INDIAN BANK) score 61.1 — "US Federal Reserve plans to raise bank oversight thresholds, sources say"
- COIN (Coinbase Global, Inc.) score 54.0 — "Global Market: VLCC rates hit record as Saudi crude flows jump"
- OHI (Omega Healthcare Investors, In) score 53.0 — "BSE cautions investors as international ETFs trade at steep premiums to NAV"
- HDB (HDFC Bank Limited) score 48.5 — "US Federal Reserve plans to raise bank oversight thresholds, sources say"
- BAC (Bank of America Corporation) score 46.5 — "US Federal Reserve plans to raise bank oversight thresholds, sources say"
- CHKP (Check Point Software Technolog) score 43.9 — "Upcoming dividend stocks: SAIL, IGL, NMDC among 3 PSU stocks with record dates ahead- Chec"
- TECHM.NS (TECH MAHINDRA LIMITED) score 42.6 — "ArMee Infotech IPO Day 3: Issue sees 2.44x subscription; GMP at 5%"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 42.6 — "ArMee Infotech IPO Day 3: Issue sees 2.44x subscription; GMP at 5%"
- TECH (Bio-Techne Corp) score 42.6 — "ArMee Infotech IPO Day 3: Issue sees 2.44x subscription; GMP at 5%"
- IDBI.NS (IDBI BANK LIMITED) score 40.4 — "US Federal Reserve plans to raise bank oversight thresholds, sources say"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 40.4 — "US Federal Reserve plans to raise bank oversight thresholds, sources say"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 40.4 — "US Federal Reserve plans to raise bank oversight thresholds, sources say"
- 301077.SZ (CHINASTARS) score 38.1 — "Xi ends 3-day Trump visit with promise to meet again in November in China"
- BOND (PIMCO Active Bond Exchange-Tra) score 36.3 — "U.S. 30-YEAR BOND YIELD TOPS 5.5% FOR FIRST TIME SINCE 2004"
- SEPN (Septerna, Inc.) score 32.2 — "U.S. CONSUMER SENTIMENT SLIDES AS INFLATION FEARS RISE University of Michigan consumer sen"
- LTH (Life Time Group Holdings, Inc.) score 31.3 — "U.S. CONSUMER SENTIMENT SLIDES AS INFLATION FEARS RISE University of Michigan consumer sen"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.5 — "5 Energy Stocks Positioned for a Prolonged Iran War"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 17.7 — "Stocks to watch today, September 25: Tata Group, Lemon Tree Hotels, PB Fintech, JSW Cement"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 17.7 — "Stocks to watch today, September 25: Tata Group, Lemon Tree Hotels, PB Fintech, JSW Cement"
- JIOFIN.BO (Jio Financial Services Limited) score 17.1 — "Financial stocks lead correction as insurance overhaul plan sparks fears"
- BZ=F (Brent Crude Oil Last Day Finan) score 16.7 — "YIELD ON 10-YEAR TREASURY NOTE LAST UP 4.45 BASIS POINTS AT 5.207%"
- POLICYBZR.NS (PB FINTECH LIMITED) score 13.5 — "Stocks to watch today, September 25: Tata Group, Lemon Tree Hotels, PB Fintech, JSW Cement"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 12.9 — "Adani Ports SEZ Share Price Highlights: Adani Ports SEZ Stock Price History"
- META (Meta) score 12.7 — "Gold price outlook: MCX gold slips for the week as US Fed rate hike bets rise; what’s next"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 11.2 — "JAPANESE, US FINANCE CHIEFS DISCUSS YEN DEPRECIATION: KYODO"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.2 — "Just One Commodity Vessel Left the Strait of Hormuz on Wednesday"
- MS (Morgan Stanley) score 8.8 — "‘We were wrong.’ Why Morgan Stanley changed its tune on the U.S. dollar — and what it expe"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.8 — "ICICI Lombard General Insurance among 3 stocks showing White Marubozu Pattern"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 7.5 — "World heads into food crises 'blind' as U.S. aid cuts squeeze UN food agency, experts warn"
- VT (Vanguard Total World Stock Ind) score 7.4 — "Beyond high-profile wars, a worldwide battle for critical minerals"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 7.4 — "Retail investors raise stakes in 10 smallcaps; 3 turn multibaggers in 3 months"
- GS (Goldman Sachs Group, Inc. (The) score 4.6 — "Goldman Sachs buys stake in Firstcry brand parent owner Brainbees Solutions | Check price,"
- PINELABS.NS (PINE LABS LIMITED) score 3.9 — "Pine Labs shares: Over 25% up in a month; Motilal Oswal sees 30% more upside | Buy rating "
- NVDA (NVIDIA Corporation) score 3.1 — "FORMER OPENAI DATA CENTER CHIEF CHRIS MALONE IS NOW AT NVIDIA - THE INFORMATION"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 2.6 — "ADIA sells 2.01% stake in Lenskart Solutions for ₹2,390 crore"
- VOLTAS.NS (VOLTAS LTD) score 1.4 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 0.8 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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