# Transmission Layer — board brief · 2026-11-27 22:41Z

data as of **2026-11-27** · 97 series · 7 red / 32 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.788, 10d in regime; vol-pct 0.87, breadth-off 0.706, Markov P(high-vol) 0.21)
- [WEAK] **safe_haven_gold** — corr20 -0.2, corr60 -0.28, contra nifty_50 corr20=0.0, last shift 2026-09-09. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.93, corr60 0.89, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.42, corr60 0.25, last shift 2026-09-24. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.04, corr60 0.07, last shift 2026-09-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.9, last shift 2026-09-25. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.03, corr60 0.01, last shift 2026-10-13. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.17, corr60 -0.01, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.34, corr60 0.38, last shift 2026-10-09. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 88** scanned series survive multiplicity control (effective p ≤ 0.0006496287948376533)
- **SETUP** dyn_hdb → usd_inr: leads 1d (ccf -0.373, β -0.0949, p 0.0); driver zc 1.57 → expected -0.272%. Type hit-rate 0.82 (n=2118).
- **SETUP** dyn_hdb → nifty_50: leads 1d (ccf 0.289, β 0.1549, p 1e-05); driver zc 1.57 → expected 0.444%. Type hit-rate 0.82 (n=2118).
- Track record · residual_reversion: hit-rate **0.509** (n=1144) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.82** (n=2118) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 5.89] wti ↓
- wti [COMMODITIES]: last 82.82, z20 -0.89, zc -0.85, resid-z 0.51 [quiet], 1d -1.90%, 1-session move -1.90% ≥ 1.5%
- **Mechanism**: wti ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_inoxindia_ns (rho -0.473 via wti, z 1.53, reacted); dyn_adanient_bo (rho -0.456 via wti, z -0.47, quiet); nifty_metal (rho -0.454 via wti, z -1.01, reacted); dyn_muthootfin_ns (rho -0.446 via wti, z -0.34, quiet); nifty_fmcg (rho -0.441 via wti, z 1.28, reacted)
- Watch next: brent (co-move) — not yet - watch; rho 0.759 vs wti
- **India receivers**: dyn_inoxindia_ns (rho -0.473, z 1.53); dyn_adanient_bo (rho -0.456, z -0.47); nifty_metal (rho -0.454, z -1.01); dyn_muthootfin_ns (rho -0.446, z -0.34)
- Source: OPEC+ set to keep oil production targets steady: Report — ET Markets, 2026-11-27. https://economictimes.indiatimes.com/markets/commodities/opec-set-to-keep-oil-production-targets-steady-report/articleshow/136232084.cms
- Source: OPEC+ Faces Growing Pressure As Iraq Pushes for Higher Quota — OilPrice, 2026-11-27. https://oilprice.com/Latest-Energy-News/World-News/OPEC-Faces-Growing-Pressure-As-Iraq-Pushes-for-Higher-Quota.html
- Source: The Oil Glut Everyone Expected Is Looking Increasingly Elusive — OilPrice, 2026-11-27. https://oilprice.com/Energy/Crude-Oil/The-Oil-Glut-Everyone-Expected-Is-Looking-Increasingly-Elusive.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

### [RED 5.09] dyn_chkp ↑
- dyn_chkp [EQUITIES]: last 168.70, z20 3.09, zc 1.01, resid-z 0.66 [quiet], 1d 3.01%, |z20|=3.09
- **Mechanism**: dyn_chkp ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: US stock market open or closed today Friday, 27 Nov? Check NYSE and Nasdaq trading schedule, holiday calendar — Mint Markets, 2026-11-27. https://www.livemint.com/market/stock-market-news/us-stock-market-open-or-closed-today-friday-27-nov-check-nyse-and-nasdaq-trading-schedule-holiday-calendar-11795773710345.html
- Source: Swami Ramdev fame company announces 2nd interim dividend; check amount, record date, history — Mint Markets, 2026-11-26. https://www.livemint.com/market/stock-market-news/swami-ramdev-fame-company-patanjali-foods-announces-2nd-interim-dividend-check-amount-record-date-history-11795691413030.html
- Source: Check Nifty target, Top Stocks to Buy: PL Capital adds HUL, Astral, Grindwell to high-conviction list | Full List — Mint Markets, 2026-11-26. https://www.livemint.com/market/stock-market-news/check-nifty-target-top-stocks-to-buy-pl-capital-adds-hul-astral-grindwell-to-high-conviction-list-full-list-11795685183310.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2025-05-20 (d=0.04)

### [AMBER 4.52] cross-asset · 3 series ↓
- dyn_coin [EQUITIES]: last 106.96, z20 -1.20, zc 0.28, resid-z 0.25 [quiet], 1d 3.12%, 1y-pct=1
- btc_usd [CRYPTO]: last 59669.28, z20 -1.14, zc -0.61, resid-z 0.25 [quiet], 1d -1.36%, 1y-pct=1
- eth_usd [CRYPTO]: last 1655.74, z20 -1.12, zc -0.51, resid-z 0.07 [quiet], 1d -1.90%, 1y-pct=4
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-30 (z-distance 0.16).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.636 vs dyn_coin, historically leads by 5d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.567 vs dyn_coin, historically leads by 1d
- Watch next: vix (inverse) — not yet - watch; rho -0.546 vs dyn_coin, historically leads by 2d
- Watch next: brent (inverse) — not yet - watch; rho -0.52 vs btc_usd, historically leads by 3d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.645 vs dyn_coin
- Source: Gold prices rise in India and China after hitting 15-month low as physical demand improves despite global rate concerns — Mint Markets, 2026-11-27. https://www.livemint.com/market/commodities/gold-prices-rise-in-india-and-china-after-hitting-15-month-low-as-physical-demand-improves-despite-global-rate-concerns-11795802897456.html
- Source: Indian retail investors post $353 million in gains from global stocks: Vested report — BusinessLine Mkts, 2026-11-27. https://www.thehindubusinessline.com/markets/indian-retail-investors-post-353-million-in-gains-from-global-stocks-vested-report/article71751389.ece
- Source: Global electricity generation more than doubled from 2000 to 2025 — EIA Today in Energy, 2026-11-27. https://www.eia.gov/todayinenergy/detail.php?id=68525
- Historical analogues: 2025-10-30 (d=0.16), 2025-10-22 (d=0.28), 2025-12-29 (d=0.32)

### [RED 4.23] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 3674.60, z20 -0.91, zc 0.63, resid-z -0.31 [quiet], 1d 1.50%, 1y-pct=2; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 43.91, z20 -0.86, zc 1.05, resid-z 1.40 [quiet], 1d 4.34%, 1y-pct=2; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 83.68, z20 0.69, zc n/a, resid-z n/a [quiet], 1d -2.72%, 1y-pct=98
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.602 via comex_gold, z -0.34, quiet)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.602 vs comex_gold, historically leads by 4d
- Watch next: shanghai_comp (co-move) — not yet - watch; rho 0.523 vs comex_silver, historically leads by 1d
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.515 vs gold_silver_ratio, historically leads by 5d
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.505 vs comex_silver, historically leads by 5d
- Watch next: dax (co-move) — not yet - watch; rho 0.55 vs comex_gold
- **India receivers**: dyn_muthootfin_ns (rho 0.602, z -0.34)
- Source: Gold pares gains as Fed hike risks linger, eyes first weekly rise in three weeks — Mint Markets, 2026-11-27. https://www.livemint.com/market/gold-pares-gains-as-fed-hike-risks-linger-eyes-first-weekly-rise-in-three-weeks-11795807102935.html
- Source: Gold pares gains as Fed-hike risks linger, eyes first weekly rise in three weeks — ET Markets, 2026-11-27. https://economictimes.indiatimes.com/markets/commodities/gold-pares-gains-as-fed-hike-risks-linger-eyes-first-weekly-rise-in-three-weeks/articleshow/136231951.cms
- Source: Gold prices rise in India and China after hitting 15-month low as physical demand improves despite global rate concerns — Mint Markets, 2026-11-27. https://www.livemint.com/market/commodities/gold-prices-rise-in-india-and-china-after-hitting-15-month-low-as-physical-demand-improves-despite-global-rate-concerns-11795802897456.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [AMBER 3.8] equities · 2 series ↓
- dyn_crwv [EQUITIES]: last 44.14, z20 -0.97, zc -0.01, resid-z 0.23 [quiet], 1d 3.69%, 1y-pct=2
- dyn_nvda [EQUITIES]: last 150.62, z20 -0.94, zc -0.62, resid-z -1.36 [quiet], 1d 0.88%, 1y-pct=1
- **Mechanism**: equities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.848 vs dyn_nvda
- Watch next: sp500 (co-move) — not yet - watch; rho 0.785 vs dyn_nvda
- Watch next: vix (inverse) — not yet - watch; rho -0.651 vs dyn_nvda
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.565 vs dyn_nvda
- Source: These stocks soared the most during a wild week highlighted by Huang’s return to Nvidia — MarketWatch Top, 2026-11-27. https://www.marketwatch.com/story/these-stocks-soared-the-most-during-a-wild-week-highlighted-by-huangs-return-to-nvidia-578b3f9a?mod=mw_rss_topstories
- Source: Nvidia’s stock has tumbled 27% over one chaotic month. The next big test lies in the week ahead — MarketWatch Top, 2026-11-27. https://www.marketwatch.com/story/nvidias-stock-has-tumbled-27-over-one-chaotic-month-the-next-big-test-lies-in-the-week-ahead-06449777?mod=mw_rss_topstories
- Source: NVDA - NVIDIA BLACKWELL CHIPS FOUND AT CHINESE DATA CENTER LINKED TO MEGASPEED Two Chinese companies installed restricted Nvidia Blackwell hardware at a Shanghai data center linked to Alice Huang and Megaspeed, according to Bloomberg. Regulatory filings identify a GB300 NVL72 rack and a GB200 server — DeItaone, 2026-11-27. https://t.me/walter_bloomberg/39227
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-25 (d=0.23), 2025-10-20 (d=0.37)

### [RED 3.77] corn ↑
- corn [COMMODITIES]: last 462.75, z20 3.77, zc 0.95, resid-z 0.90 [quiet], 1d 5.23%, |z20|=3.77
- **Mechanism**: corn ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_inoxindia_ns (rho -0.427 via corn, z 1.53, reacted); eur_inr (rho 0.377 via corn, z -1.24, reacted)
- Watch next: wheat (co-move) — not yet - watch; rho 0.677 vs corn
- **India receivers**: dyn_inoxindia_ns (rho -0.427, z 1.53); eur_inr (rho 0.377, z -1.24)
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-21 (d=0.01), 2025-12-31 (d=0.02)

### [AMBER 3.7] dyn_tgt ↑
- dyn_tgt [EQUITIES]: last 172.31, z20 1.70, zc -0.98, resid-z -1.55 [unexplained], 1d 0.05%, 1y-pct=99
- **Mechanism**: dyn_tgt ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_ohi (co-move) — not yet - watch; rho 0.513 vs dyn_tgt, historically leads by 3d
- Source: Up 57% YTD! Healthcare stock shows resilience against the Indian stock market crash; should you buy? Target, stop-loss — Mint Markets, 2026-11-27. https://www.livemint.com/market/stock-market-news/up-55-ytd-healthcare-stock-park-medi-world-shows-resilience-against-the-indian-stock-market-crash-should-you-buy-11795765259630.html
- Source: Check Nifty target, Top Stocks to Buy: PL Capital adds HUL, Astral, Grindwell to high-conviction list | Full List — Mint Markets, 2026-11-26. https://www.livemint.com/market/stock-market-news/check-nifty-target-top-stocks-to-buy-pl-capital-adds-hul-astral-grindwell-to-high-conviction-list-full-list-11795685183310.html
- Source: BPCL vs IOCL vs HPCL: Jefferies names its top OMC stocks to buy as crude prices fall | Check target prices, rationale — Mint Markets, 2026-11-26. https://www.livemint.com/market/stock-market-news/bpcl-vs-iocl-vs-hpcl-jefferies-names-its-top-omc-stocks-to-buy-as-crude-prices-fall-check-target-prices-rationale-11795681099588.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.01), 2025-09-30 (d=0.01)

### [AMBER 3.62] dyn_lth ↑
- dyn_lth [EQUITIES]: last 48.47, z20 1.62, zc -0.11, resid-z -0.37 [quiet], 1d 1.38%, 1y-pct=100
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_ohi (co-move) — not yet - watch; rho 0.577 vs dyn_lth, historically leads by 5d
- Source: Silver rate today 27 November: MCX Price 6% upper circuit at  ₹1.54 lakh/kg, up  ₹8,500 in a day | Right time to buy? — Mint Markets, 2026-11-27. https://www.livemint.com/market/commodities/silver-rate-today-27-november-mcx-price-6-upper-circuit-at-rs-1-54-lakh-kg-up-rs-8-500-in-a-day-right-time-to-buy-11795772565257.html
- Source: Why IT stocks are down today? TCS, Infosys, Wipro lead losses as Sensex, Nifty fall | Time to buy for returns ahead? — Mint Markets, 2026-11-27. https://www.livemint.com/market/stock-market-news/why-it-stocks-are-down-today-tcs-infosys-wipro-lead-losses-as-sensex-nifty-fall-time-to-buy-for-returns-ahead-11795755363384.html
- Source: Gold price today 27 November 2026: MCX gold rate jumps but still 31% down from record high; is it the right time to buy? — Mint Markets, 2026-11-27. https://www.livemint.com/market/commodities/gold-price-today-27-november-2026-mcx-gold-rate-jumps-but-still-31-down-from-record-high-is-it-the-right-time-to-buy-11795752383038.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-17 (d=0.02), 2025-12-31 (d=0.02)

## Watchlist (below surfacing floor)
natgas ↑ (3.6), dyn_tech ↑ (3.47), tips_10y_real ↓ (3.09), dyn_techm_ns ↑ (3.03), rates · 2 series ↑ (2.84), soybeans ↑ (2.75), dyn_cochinship_ns ↓ (2.74), bovespa ↑ (2.72), usd_mxn ↑ (2.62), dyn_2545_tw ↓ (2.56), dyn_4417_t ↑ (2.49), dyn_eternal_ns ↑ (2.38)

## India macro
- nifty_50: 25607.1992 (1d -1.07%, z20 0.88, flag none)
- nifty_midcap_100: 61847.1484 (1d 0.10%, z20 0.85, flag none)
- usd_inr: 92.9800 (1d 0.80%, z20 -1.13, flag none)
- goi_10y: 7.3800 (1d 4.53%, z20 3.03, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.1400 (1d -5.73%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4152 (1d 1.19%, z20 -0.81, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 79.8 — "Mahanadi Coalfields shares make muted debut on stock exchanges"
- INOXINDIA.NS (INOX INDIA LIMITED) score 72.7 — "Indian retail investors post $353 million in gains from global stocks: Vested report"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 72.6 — "Indian retail investors post $353 million in gains from global stocks: Vested report"
- INDIANB.NS (INDIAN BANK) score 61.6 — "HDFC Bank Share Price Highlights: HDFC Bank Stock Price History"
- NVDA (NVIDIA Corporation) score 55.6 — "NVDA - *NVIDIA BLACKWELL CHIPS SURFACE AT CHINA SITE TIED TO MEGASPEED *TWO CHINESE FIRMS "
- BAC (Bank of America Corporation) score 44.0 — "HDFC Bank Share Price Highlights: HDFC Bank Stock Price History"
- HDB (HDFC Bank Limited) score 41.4 — "HDFC Bank Share Price Highlights: HDFC Bank Stock Price History"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 38.3 — "HDFC Bank Share Price Highlights: HDFC Bank Stock Price History"
- IDBI.NS (IDBI BANK LIMITED) score 38.3 — "HDFC Bank Share Price Highlights: HDFC Bank Stock Price History"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 38.3 — "HDFC Bank Share Price Highlights: HDFC Bank Stock Price History"
- OHI (Omega Healthcare Investors, In) score 31.0 — "Missing best days costs small-cap investors dearly: Abakkus"
- TGT (Target Corporation) score 30.9 — "OPEC+ set to keep oil production targets steady: Report"
- TECHM.NS (TECH MAHINDRA LIMITED) score 30.3 — "UltraTech Cem Share Price Highlights: UltraTech Cem. Stock Price History"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 28.6 — "UltraTech Cem Share Price Highlights: UltraTech Cem. Stock Price History"
- TECH (Bio-Techne Corp) score 28.6 — "UltraTech Cem Share Price Highlights: UltraTech Cem. Stock Price History"
- BLLN (BillionToOne, Inc.) score 27.6 — "SPY $QQQ - GOLDMAN SACHS WARNS OF $100 BILLION IN AUTOMATED STOCK SELLING AHEAD Goldman Sa"
- 301077.SZ (CHINASTARS) score 27.6 — "NVDA - *NVIDIA BLACKWELL CHIPS SURFACE AT CHINA SITE TIED TO MEGASPEED *TWO CHINESE FIRMS "
- 2545.TW (HUANG HSIANG CONSTRUCTION) score 26.0 — "NVDA - NVIDIA BLACKWELL CHIPS FOUND AT CHINESE DATA CENTER LINKED TO MEGASPEED Two Chinese"
- COIN (Coinbase Global, Inc.) score 22.2 — "SPY $QQQ - GOLDMAN SACHS WARNS OF $100 BILLION IN AUTOMATED STOCK SELLING AHEAD Goldman Sa"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 20.0 — "Tata Motors PV Share Price Highlights: Tata Motors PV Stock Price History"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 20.0 — "Tata Motors PV Share Price Highlights: Tata Motors PV Stock Price History"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 19.4 — "Broker’s call: Siemens Energy (Buy)"
- LTH (Life Time Group Holdings, Inc.) score 18.5 — "MCX gold prices rebound over  ₹8,300 in two sessions, set to snap 2-week losing streak; wh"
- CHKP (Check Point Software Technolog) score 17.8 — "US stock market open or closed today Friday, 27 Nov? Check NYSE and Nasdaq trading schedul"
- BOND (PIMCO Active Bond Exchange-Tra) score 16.9 — "Indian bonds decline ahead of fresh debt sale as elevated oil prices fan inflation worries"
- TATASTEEL.BO (TATA STEEL LTD.) score 14.9 — "Tata Motors PV Share Price Highlights: Tata Motors PV Stock Price History"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 10.8 — "Multibagger stock to buy: SG Mart shares rise 4% despite 5800% rally in 5 years | Buy, sel"
- JIOFIN.BO (Jio Financial Services Limited) score 10.5 — "WMT $COST $AMZN - BLACK FRIDAY SPENDING SET TO RISE DESPITE CONSUMER FINANCIAL PRESSURE U."
- META (Meta) score 10.4 — "Sensex slips, Nifty flat as IT stocks fall; metals, Titan gain"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 9.4 — "Gold finance stocks rally! Manappuram, Muthoot Finance gain up to 4% as MCX gold prices re"
- BZ=F (Brent Crude Oil Last Day Finan) score 9.2 — "1:1 bonus share by famous IT company with 25% returns in 6 months: Check last day to buy, "
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.5 — "WMT $COST $AMZN - BLACK FRIDAY SPENDING SET TO RISE DESPITE CONSUMER FINANCIAL PRESSURE U."
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 6.6 — "Gold finance stocks rally! Manappuram, Muthoot Finance gain up to 4% as MCX gold prices re"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.3 — "Eternal, Adani Enterprises among 10 stocks with highest FII buying in Q2. How many do you "
- MS (Morgan Stanley) score 5.0 — "A big shift for gold trading? JPMorgan, HSBC and StoneX complete first digital gold deals-"
- CRWV (CoreWeave, Inc.) score 4.9 — "CRWV - COREWEAVE BONDS PLUNGE AS 2031 YIELD SURGES TO 17.91% CoreWeave's debt is coming un"
- GS (Goldman Sachs Group, Inc. (The) score 4.6 — "SPY $QQQ - GOLDMAN SACHS WARNS OF $100 BILLION IN AUTOMATED STOCK SELLING AHEAD Goldman Sa"
- ETERNAL.NS (ETERNAL LIMITED) score 2.6 — "Eternal, Adani Enterprises among 10 stocks with highest FII buying in Q2. How many do you "
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 1.4 — "BEML, BEL, HAL, Cochin Shipyard, Bharat Dynamics shares: Defence stocks rise up to 14%; he"
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 0.8 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "

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