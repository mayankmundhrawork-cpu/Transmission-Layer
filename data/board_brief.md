# Transmission Layer — board brief · 2026-11-27 13:48Z

data as of **2026-11-27** · 97 series · 5 red / 31 amber · 8 events surfaced (23 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.764, 10d in regime; vol-pct 0.913, breadth-off 0.615, Markov P(high-vol) 0.21)
- [WEAK] **safe_haven_gold** — corr20 -0.18, corr60 -0.27, contra nifty_50 corr20=0.01, last shift 2026-09-09. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.93, corr60 0.89, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.42, corr60 0.26, last shift 2026-09-24. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.05, corr60 0.08, last shift 2026-09-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.9, last shift 2026-09-25. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.05, corr60 0.0, last shift 2026-10-13. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.18, corr60 -0.01, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.32, corr60 0.36, last shift 2026-10-09. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **5 of 88** scanned series survive multiplicity control (effective p ≤ 0.002527746855344626)
- **SETUP** dyn_hdb → usd_inr: leads 1d (ccf -0.373, β -0.0949, p 0.0); driver zc 1.55 → expected -0.269%. Type hit-rate 0.82 (n=2150).
- **SETUP** dyn_hdb → nifty_50: leads 1d (ccf 0.289, β 0.1549, p 1e-05); driver zc 1.55 → expected 0.438%. Type hit-rate 0.82 (n=2150).
- Track record · residual_reversion: hit-rate **0.51** (n=1143) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.82** (n=2150) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 6.47] natgas ↑
- natgas [COMMODITIES]: last 3.48, z20 1.47, zc -0.87, resid-z -0.58 [quiet], 1d -5.35%, 1-session move -5.35% ≥ 5.0%
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: gold_silver_ratio (co-move) — not yet - watch; rho 0.074 vs natgas, historically leads by 4d
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.063 vs natgas, historically leads by 4d
- Watch next: comex_gold (inverse) — not yet - watch; rho -0.043 vs natgas, historically leads by 4d
- Source: Iran Says LNG Carrier Exploded After Hitting a Mine in Hormuz — OilPrice, 2026-11-26. https://oilprice.com/Latest-Energy-News/World-News/Iran-Says-LNG-Carrier-Exploded-After-Hitting-a-Mine-in-Hormuz.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [AMBER 5.12] rates · 2 series ↑
- hy_oas [RATES]: last 3.72, z20 2.29, zc 0.71, resid-z 0.43 [quiet], 1d 2.48%, |z20|=2.29; 1y-pct=99
- ig_oas [RATES]: last 0.98, z20 2.17, zc 0.44, resid-z 0.00 [quiet], 1d 1.03%, |z20|=2.17; 1y-pct=99
- **Mechanism**: rates · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.474 via ig_oas, z -0.81, quiet)
- Watch next: vix (co-move) — not yet - watch; rho 0.574 vs hy_oas, historically leads by 5d
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.549 vs hy_oas
- Watch next: ust_2y (inverse) — not yet - watch; rho -0.536 vs hy_oas
- **India receivers**: midcap_largecap_ratio (rho -0.474, z -0.81)
- Source: U.S. $44 BILLION 7-YEAR TREASURY AUCTION TAILS AS DEMAND DISAPPOINTS The U.S. Treasury sold $44 billion in 7-year notes at a high yield of 4.708%, above the 4.698% when-issued yield before the auction. That represents a 1-basis-point tail, signaling weaker-than-expected demand. 🔸 Bid-to-cover ratio: — DeItaone, 2026-11-25. https://t.me/walter_bloomberg/39202
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-01 (d=0.48), 2026-07-01 (d=0.59)

### [AMBER 4.98] equities · 2 series ↓
- dyn_ms [EQUITIES]: last 167.53, z20 -2.15, zc -0.29, resid-z -1.14 [quiet], 1d -0.75%, |z20|=2.15
- dyn_gs [EQUITIES]: last 800.45, z20 -2.12, zc -0.25, resid-z -1.23 [quiet], 1d -0.69%, |z20|=2.12; 1y-pct=5
- **Mechanism**: equities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.828 vs dyn_gs, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.782 vs dyn_gs, historically leads by 5d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.778 vs dyn_gs
- Watch next: dax (co-move) — not yet - watch; rho 0.625 vs dyn_gs
- Source: Nifty 50 to hit 29,000? J.P. Morgan calls Indian stocks a 'safe haven' from AI trades; sees 12% upside. Key reasons — Mint Markets, 2026-11-26. https://www.livemint.com/market/stock-market-news/nifty-50-to-hit-29-000-j-p-morgan-calls-indian-stocks-a-safe-haven-from-ai-trades-sees-12-upside-key-reasons-11795710323279.html
- Source: CRWV - COREWEAVE BANKS PREPARE $4.5 BILLION LOAN SALE AS DEFAULT FEARS SURGE Morgan Stanley and MUFG are preparing to sell $4.5 billion in CoreWeave-linked debt as soon as next week, Bloomberg reports. The loan, backed by GPUs supporting a Meta data center project, is expected to carry investment-gr — DeItaone, 2026-11-25. https://t.me/walter_bloomberg/39209
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-13 (d=0.16), 2025-05-13 (d=0.23)

### [RED 4.68] dyn_chkp ↑
- dyn_chkp [EQUITIES]: last 163.83, z20 2.68, zc 1.05, resid-z 0.00 [quiet], 1d 2.82%, |z20|=2.68
- **Mechanism**: dyn_chkp ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: US stock market open or closed today Friday, 27 Nov? Check NYSE and Nasdaq trading schedule, holiday calendar — Mint Markets, 2026-11-27. https://www.livemint.com/market/stock-market-news/us-stock-market-open-or-closed-today-friday-27-nov-check-nyse-and-nasdaq-trading-schedule-holiday-calendar-11795773710345.html
- Source: Swami Ramdev fame company announces 2nd interim dividend; check amount, record date, history — Mint Markets, 2026-11-26. https://www.livemint.com/market/stock-market-news/swami-ramdev-fame-company-patanjali-foods-announces-2nd-interim-dividend-check-amount-record-date-history-11795691413030.html
- Source: Check Nifty target, Top Stocks to Buy: PL Capital adds HUL, Astral, Grindwell to high-conviction list | Full List — Mint Markets, 2026-11-26. https://www.livemint.com/market/stock-market-news/check-nifty-target-top-stocks-to-buy-pl-capital-adds-hul-astral-grindwell-to-high-conviction-list-full-list-11795685183310.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2025-05-20 (d=0.04)

### [RED 4.25] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 3670.60, z20 -0.93, zc 0.58, resid-z -2.50 [unexplained], 1d 1.39%, 1y-pct=2; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 44.05, z20 -0.83, zc 1.13, resid-z 1.96 [unexplained], 1d 4.67%, 1y-pct=2; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 83.33, z20 0.59, zc n/a, resid-z n/a [quiet], 1d -3.14%, 1y-pct=98
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.602 via comex_gold, z -0.34, quiet)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.602 vs comex_gold, historically leads by 4d
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.6 vs comex_gold, historically leads by 4d
- Watch next: shanghai_comp (co-move) — not yet - watch; rho 0.532 vs comex_silver, historically leads by 1d
- Watch next: btc_usd (co-move) — not yet - watch; rho 0.553 vs comex_silver
- Watch next: dax (co-move) — not yet - watch; rho 0.545 vs comex_gold
- **India receivers**: dyn_muthootfin_ns (rho 0.602, z -0.34)
- Source: Jaipur leads jewellery searches with 78% growth, Delhi tops gold testing centre searches at 58%, says report — Mint Markets, 2026-11-27. https://www.livemint.com/market/commodities/jaipur-leads-jewellery-searches-with-78-growth-delhi-tops-gold-testing-centre-searches-at-58-says-report-11795779411777.html
- Source: RBI gold share in forex reserves falls below 14% after price correction — BusinessLine Mkts, 2026-11-27. https://www.thehindubusinessline.com/data-stories/data-focus/rbi-gold-share-in-forex-reserves-falls-below-14-after-price-correction/article71750525.ece
- Source: Silver rate today 27 November: MCX Price 6% upper circuit at  ₹1.54 lakh/kg, up  ₹8,500 in a day | Right time to buy? — Mint Markets, 2026-11-27. https://www.livemint.com/market/commodities/silver-rate-today-27-november-mcx-price-6-upper-circuit-at-rs-1-54-lakh-kg-up-rs-8-500-in-a-day-right-time-to-buy-11795772565257.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 4.18] bovespa ↑
- bovespa [INDICES]: last 181859.91, z20 4.18, zc 1.49, resid-z 0.77 [quiet], 1d 2.86%, |z20|=4.18
- **Mechanism**: bovespa ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_atherenerg_ns (rho -0.598 via bovespa, z 0.41, quiet)
- Watch next: dyn_atherenerg_ns (inverse) — not yet - watch; rho -0.598 vs bovespa, historically leads by 4d
- Watch next: usd_brl (co-move) — not yet - watch; rho 0.03 vs bovespa, historically leads by 1d
- **India receivers**: dyn_atherenerg_ns (rho -0.598, z 0.41)
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-12 (d=1.03), 2025-01-30 (d=1.08)

### [AMBER 4.14] equities · 2 series ↓
- dyn_crwv [EQUITIES]: last 42.54, z20 -1.31, zc -0.02, resid-z -1.48 [quiet], 1d -0.15%, 1y-pct=0
- dyn_nvda [EQUITIES]: last 149.29, z20 -1.09, zc -0.63, resid-z -1.67 [unexplained], 1d -3.92%, 1y-pct=1
- **Mechanism**: equities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: btc_usd (co-move) — not yet - watch; rho 0.61 vs dyn_nvda, historically leads by 5d
- Watch next: eth_usd (co-move) — not yet - watch; rho 0.577 vs dyn_nvda, historically leads by 5d
- Watch next: vix (inverse) — not yet - watch; rho -0.656 vs dyn_nvda
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.566 vs dyn_nvda
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.561 vs dyn_nvda
- Source: Nvidia’s stock has tumbled 27% over one chaotic month. The next big test lies in the week ahead — MarketWatch Top, 2026-11-27. https://www.marketwatch.com/story/nvidias-stock-has-tumbled-27-over-one-chaotic-month-the-next-big-test-lies-in-the-week-ahead-06449777?mod=mw_rss_topstories
- Source: Nvidia stock plunges 35% from record high: Is it a buying opportunity? — ET Markets, 2026-11-27. https://economictimes.indiatimes.com/markets/us-stocks/news/nvidia-stock-plunges-35-from-record-high-is-it-a-buying-opportunity/slideshow/136209377.cms
- Source: Huawei guilty on 10 counts in US trial; Nvidia’s Jensen Huang returns: SCMP’s 7 highlights — SCMP Economy, 2026-11-27. https://www.scmp.com/news/world/article/3375979/huawei-guilty-10-counts-us-trial-nvidias-jensen-huang-returns-scmps-7-highlights
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-25 (d=0.23), 2025-10-20 (d=0.37)

### [AMBER 3.8] dyn_tgt ↑
- dyn_tgt [EQUITIES]: last 172.16, z20 1.80, zc -0.99, resid-z 1.94 [unexplained], 1d -2.22%, 1y-pct=99
- **Mechanism**: dyn_tgt ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_ohi (co-move) — not yet - watch; rho 0.512 vs dyn_tgt, historically leads by 3d
- Source: Up 57% YTD! Healthcare stock shows resilience against the Indian stock market crash; should you buy? Target, stop-loss — Mint Markets, 2026-11-27. https://www.livemint.com/market/stock-market-news/up-55-ytd-healthcare-stock-park-medi-world-shows-resilience-against-the-indian-stock-market-crash-should-you-buy-11795765259630.html
- Source: Check Nifty target, Top Stocks to Buy: PL Capital adds HUL, Astral, Grindwell to high-conviction list | Full List — Mint Markets, 2026-11-26. https://www.livemint.com/market/stock-market-news/check-nifty-target-top-stocks-to-buy-pl-capital-adds-hul-astral-grindwell-to-high-conviction-list-full-list-11795685183310.html
- Source: BPCL vs IOCL vs HPCL: Jefferies names its top OMC stocks to buy as crude prices fall | Check target prices, rationale — Mint Markets, 2026-11-26. https://www.livemint.com/market/stock-market-news/bpcl-vs-iocl-vs-hpcl-jefferies-names-its-top-omc-stocks-to-buy-as-crude-prices-fall-check-target-prices-rationale-11795681099588.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.01), 2025-09-30 (d=0.01)

## Watchlist (below surfacing floor)
dyn_coin ↓ (3.5), usd_cny ↓ (3.1), dyn_lth ↑ (3.06), dyn_techm_ns ↑ (3.03), dyn_cochinship_ns ↓ (2.74), dyn_2545_tw ↓ (2.56), dyn_4417_t ↑ (2.49), usd_mxn ↑ (2.48), dyn_eternal_ns ↑ (2.38), corn ↑ (2.31), dyn_idbi_ns ↓ (2.15), fx · 2 series ↓ (2.02)

## India macro
- nifty_50: 25607.1992 (1d -1.07%, z20 0.88, flag none)
- nifty_midcap_100: 61847.1484 (1d 0.10%, z20 0.85, flag none)
- usd_inr: 92.8700 (1d 0.69%, z20 -1.27, flag none)
- goi_10y: 7.3800 (1d 4.53%, z20 3.03, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.1400 (1d -5.73%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4152 (1d 1.19%, z20 -0.81, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 81.5 — "Mahanadi Coalfields set for Mumbai debut after ₹8,981 crore IPO"
- INOXINDIA.NS (INOX INDIA LIMITED) score 74.9 — "Indian bonds decline ahead of fresh debt sale as elevated oil prices fan inflation worries"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 74.7 — "Indian bonds decline ahead of fresh debt sale as elevated oil prices fan inflation worries"
- INDIANB.NS (INDIAN BANK) score 62.8 — "Indian bonds decline ahead of fresh debt sale as elevated oil prices fan inflation worries"
- NVDA (NVIDIA Corporation) score 57.3 — "TRUMP: WILL PROBABLY SPEAK TO NVIDIA'S HUANG SOON"
- BAC (Bank of America Corporation) score 44.6 — "Banking stocks hit the accelerator! Nifty Bank index up 18% in 1 month; HDFC Bank, SBI, IC"
- HDB (HDFC Bank Limited) score 41.9 — "Banking stocks hit the accelerator! Nifty Bank index up 18% in 1 month; HDFC Bank, SBI, IC"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 38.5 — "Banking stocks hit the accelerator! Nifty Bank index up 18% in 1 month; HDFC Bank, SBI, IC"
- IDBI.NS (IDBI BANK LIMITED) score 38.5 — "Banking stocks hit the accelerator! Nifty Bank index up 18% in 1 month; HDFC Bank, SBI, IC"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 38.5 — "Banking stocks hit the accelerator! Nifty Bank index up 18% in 1 month; HDFC Bank, SBI, IC"
- TGT (Target Corporation) score 32.6 — "Up 57% YTD! Healthcare stock shows resilience against the Indian stock market crash; shoul"
- TECHM.NS (TECH MAHINDRA LIMITED) score 31.9 — "Stocks in focus, Nov 27: TVS group companies, NSE, Omnitech, Texmaco Rail, Waaree Renewabl"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 30.0 — "Stocks in focus, Nov 27: TVS group companies, NSE, Omnitech, Texmaco Rail, Waaree Renewabl"
- TECH (Bio-Techne Corp) score 30.0 — "Stocks in focus, Nov 27: TVS group companies, NSE, Omnitech, Texmaco Rail, Waaree Renewabl"
- OHI (Omega Healthcare Investors, In) score 29.5 — "Tata Steel-Apollo deal tests power of minority investors"
- 2545.TW (HUANG HSIANG CONSTRUCTION) score 26.2 — "TRUMP: WILL PROBABLY SPEAK TO NVIDIA'S HUANG SOON"
- BLLN (BillionToOne, Inc.) score 25.8 — "India’s forex reserves fall by $4.44 billion to $700.90 billion, RBI data shows"
- 301077.SZ (CHINASTARS) score 25.7 — "China’s factories are growing profits again, but the AI boom is picking the winners"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.0 — "Small-cap, big jump! Waaree Renewable shares rise 14% on this order win; energy stock stil"
- COIN (Coinbase Global, Inc.) score 19.8 — "Gokaldas Exports to Trident: Textile stocks gain up to 8% as global brands turn to India; "
- CHKP (Check Point Software Technolog) score 19.4 — "US stock market open or closed today Friday, 27 Nov? Check NYSE and Nasdaq trading schedul"
- LTH (Life Time Group Holdings, Inc.) score 19.1 — "Gold price today 27 November 2026: MCX gold rate jumps but still 31% down from record high"
- BOND (PIMCO Active Bond Exchange-Tra) score 18.4 — "Indian bonds decline ahead of fresh debt sale as elevated oil prices fan inflation worries"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 16.4 — "Tata Steel-Apollo deal tests power of minority investors"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 16.4 — "Tata Steel-Apollo deal tests power of minority investors"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 11.8 — "Multibagger stock to buy: SG Mart shares rise 4% despite 5800% rally in 5 years | Buy, sel"
- META (Meta) score 11.4 — "Sensex slips, Nifty flat as IT stocks fall; metals, Titan gain"
- TATASTEEL.BO (TATA STEEL LTD.) score 10.8 — "Tata Steel-Apollo deal tests power of minority investors"
- JIOFIN.BO (Jio Financial Services Limited) score 10.3 — "Jio Financial Services Share Price Highlights: Jio Financial Services Stock Price History"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 10.3 — "Gold finance stocks rally! Manappuram, Muthoot Finance gain up to 4% as MCX gold prices re"
- BZ=F (Brent Crude Oil Last Day Finan) score 10.0 — "1:1 bonus share by famous IT company with 25% returns in 6 months: Check last day to buy, "
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.2 — "Gold finance stocks rally! Manappuram, Muthoot Finance gain up to 4% as MCX gold prices re"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.1 — "New-home sales just hit a 2026 high as builders dangle low mortgages and Black Friday deal"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.8 — "Eternal, Adani Enterprises among 10 stocks with highest FII buying in Q2. How many do you "
- MS (Morgan Stanley) score 5.4 — "A big shift for gold trading? JPMorgan, HSBC and StoneX complete first digital gold deals-"
- CRWV (CoreWeave, Inc.) score 5.3 — "CRWV - COREWEAVE BONDS PLUNGE AS 2031 YIELD SURGES TO 17.91% CoreWeave's debt is coming un"
- GS (Goldman Sachs Group, Inc. (The) score 4.0 — "SPY $QQQ - GOLDMAN WARNS IT'S TOO EARLY TO BUY THE AI SELLOFF Goldman Sachs strategist Chr"
- ETERNAL.NS (ETERNAL LIMITED) score 2.8 — "Eternal, Adani Enterprises among 10 stocks with highest FII buying in Q2. How many do you "
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 1.5 — "BEML, BEL, HAL, Cochin Shipyard, Bharat Dynamics shares: Defence stocks rise up to 14%; he"
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