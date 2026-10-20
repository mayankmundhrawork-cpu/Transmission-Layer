# Transmission Layer — board brief · 2026-10-20 15:03Z

data as of **2026-10-20** · 97 series · 8 red / 28 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.662, 12d in regime; vol-pct 0.59, breadth-off 0.733, Markov P(high-vol) 0.017)
- [INVERTED] **safe_haven_gold** — corr20 -0.25, corr60 -0.39, contra nifty_50 corr20=0.41, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.82, corr60 0.83, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.26, corr60 0.21, last shift 2026-08-26. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.07, corr60 0.1, last shift 2026-09-01. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.75, corr60 -0.78, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.11, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.18, corr60 -0.26, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.49, corr60 0.24, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 4.761345828718788e-08)
- **SETUP** dow_jones → asx_200: leads 1d (ccf 0.592, β 0.49, p 0.0); driver zc 1.71 → expected 0.624%. Type hit-rate 0.814 (n=1946).
- **SETUP** dow_jones → nikkei_225: leads 1d (ccf 0.463, β 0.7792, p 0.0); driver zc 1.71 → expected 0.993%. Type hit-rate 0.814 (n=1946).
- **SETUP** dyn_jef → asx_200: leads 1d (ccf 0.453, β 0.1298, p 0.0); driver zc 2.08 → expected 0.622%. Type hit-rate 0.814 (n=1946).
- **SETUP** dyn_jef → nikkei_225: leads 1d (ccf 0.41, β 0.2364, p 0.0); driver zc 2.08 → expected 1.133%. Type hit-rate 0.814 (n=1946).
- **SETUP** dow_jones → usd_mxn: leads 1d (ccf -0.383, β -0.2355, p 0.0); driver zc 1.71 → expected -0.3%. Type hit-rate 0.814 (n=1946).
- **SETUP** dyn_jef → usd_mxn: leads 1d (ccf -0.28, β -0.0598, p 0.00016); driver zc 2.08 → expected -0.287%. Type hit-rate 0.814 (n=1946).
- Track record · residual_reversion: hit-rate **0.501** (n=1121) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.814** (n=1946) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.8] cross-asset · 3 series ↑
- dyn_techm_ns [EQUITIES]: last 1779.10, z20 3.49, zc -0.20, resid-z 0.71 [quiet], 1d -0.61%, |z20|=3.49; 1y-pct=99
- nifty_it [INDICES]: last 31516.30, z20 2.58, zc -0.63, resid-z 0.27 [quiet], 1d -1.28%, |z20|=2.58
- dyn_tataelxsi_ns [EQUITIES]: last 3790.00, z20 2.43, zc -0.61, resid-z 0.38 [quiet], 1d -1.56%, |z20|=2.43
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.78).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.521 via dyn_tataelxsi_ns, z 0.13, quiet); dyn_justdial_bo (rho 0.513 via nifty_it, z 3.68, reacted); nifty_fmcg (rho 0.489 via dyn_tataelxsi_ns, z -1.54, reacted); midcap_largecap_ratio (rho -0.439 via dyn_techm_ns, z -2.66, reacted); dyn_tatatech_ns (rho 0.404 via nifty_it, z -0.6, quiet)
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.514 vs nifty_it
- **India receivers**: nifty_50 (rho 0.521, z 0.13); dyn_justdial_bo (rho 0.513, z 3.68); nifty_fmcg (rho 0.489, z -1.54); midcap_largecap_ratio (rho -0.439, z -2.66)
- Source: What to do with IT stocks? TCS, HCL Tech, Wipro, Infosys, Tech Mahindra — Why experts are bullish after Accenture news — Mint Markets, 2026-10-19. https://www.livemint.com/market/stock-market-news/tcs-hcl-tech-wipro-infosys-to-tech-mahindra-experts-bullish-on-it-shares-after-accentures-shift-from-ai-investment-11792390800742.html
- Source: How to trade Tech Mahindra shares after 22% rally in 4 days? Technical expert weighs in — ET Markets, 2026-10-19. https://economictimes.indiatimes.com/markets/stocks/news/how-to-trade-tech-mahindra-shares-after-22-rally-in-4-days-technical-expert-weighs-in/articleshow/135041900.cms
- Source: Veteran SIP investors not deterred by stagnant market: Kotak Mahindra's's Harsha Upadhyaya — Mint Markets, 2026-10-19. https://www.livemint.com/market/veteran-sip-investors-not-deterred-by-stagnant-market-kotak-mahindrass-harsha-upadhyaya-11792308340457.html
- Historical analogues: 2025-08-13 (d=0.78), 2025-01-23 (d=0.84), 2025-12-30 (d=0.85)

### [AMBER 6.64] commodities · 2 series ↑
- brent [COMMODITIES]: last 106.45, z20 0.81, zc -1.35, resid-z -0.96 [quiet], 1d -2.83%, 1-session move -2.83% ≥ 1.5%
- wti [COMMODITIES]: last 95.70, z20 0.62, zc -3.08, resid-z -2.96 [unexplained], 1d -7.68%, 1-session move -7.68% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.594 vs brent, historically leads by 5d
- Watch next: brent_wti_spread (inverse) — not yet - watch; rho -0.424 vs wti, historically leads by 4d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.595 vs brent
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.585 vs brent
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.574 vs brent
- Source: Shipping Crisis Forces Asian Crude Buyers to Use Smaller Tankers — OilPrice, 2026-10-20. https://oilprice.com/Latest-Energy-News/World-News/Shipping-Crisis-Forces-Asian-Crude-Buyers-to-Use-Smaller-Tankers.html
- Source: US stocks today: US stocks open lower as AI stocks decline, oil prices rise — ET Markets, 2026-10-20. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-us-stocks-open-lower-as-ai-stocks-decline-oil-prices-rise/articleshow/135071224.cms
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: US stocks open lower as AI stocks decline, oil prices rise — ET Markets, 2026-10-20. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-fed-rate-treasury-yields-earnings-forecast-nvidia-macys-gamestop-stock-price-news-20th-september-2026/liveblog/135069926.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 5.68] dyn_justdial_bo ↑
- dyn_justdial_bo [EQUITIES]: last 732.55, z20 3.68, zc 0.82, resid-z 1.21 [quiet], 1d 2.82%, |z20|=3.68
- **Mechanism**: dyn_justdial_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.513 via dyn_justdial_bo, z 2.58, reacted); dyn_techm_ns (rho 0.505 via dyn_justdial_bo, z 3.49, reacted); nifty_50 (rho 0.454 via dyn_justdial_bo, z 0.13, quiet); dyn_tataelxsi_ns (rho 0.396 via dyn_justdial_bo, z 2.43, reacted); nifty_midcap_100 (rho 0.351 via dyn_justdial_bo, z -1.12, reacted)
- **India receivers**: nifty_it (rho 0.513, z 2.58); dyn_techm_ns (rho 0.505, z 3.49); nifty_50 (rho 0.454, z 0.13); dyn_tataelxsi_ns (rho 0.396, z 2.43)
- Source: Top stocks to buy for short term: Just Dial, BSE, Orient Hotels - Target price, stop-loss by Anand Rathi's expert — Mint Markets, 2026-10-20. https://www.livemint.com/market/stock-market-news/top-stocks-to-buy-for-short-term-just-dial-bse-orient-hotels-target-price-stop-loss-by-anand-rathis-expert-11792400725179.html
- Source: Just Dial shares skyrocket 13% as volume soars massively 115 times - More returns ahead or something else? Experts view — Mint Markets, 2026-10-19. https://www.livemint.com/market/stock-market-news/just-dial-shares-skyrocket-13-as-volume-soars-massively-115-times-more-returns-ahead-or-something-else-experts-view-11792394067468.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-18 (d=0.19), 2025-06-30 (d=0.52)

### [RED 5.17] dow_jones ↑
- dow_jones [INDICES]: last 52628.00, z20 3.17, zc 1.71, resid-z 1.38 [moved], 1d 1.27%, |z20|=3.17
- **Mechanism**: dow_jones ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.758 vs dow_jones, historically leads by 1d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.913 vs dow_jones
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.696 vs dow_jones, historically leads by 1d
- Watch next: dyn_bond (co-move) — not yet - watch; rho 0.593 vs dow_jones, historically leads by 1d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.788 vs dow_jones
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: US stocks open lower as AI stocks decline, oil prices rise — ET Markets, 2026-10-20. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-fed-rate-treasury-yields-earnings-forecast-nvidia-macys-gamestop-stock-price-news-20th-september-2026/liveblog/135069926.cms
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: S&P 500, Nasdaq climb as AI-linked stocks recover ahead of earnings — ET Markets, 2026-10-19. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-us-market-live-updates-nasdaq-sp-500-iran-israel-war-hormuz-deal-brent-crude-oil-fed-rate-inflation-treasury-yields-earnings-forecast-coreweave-broadcom-micron-stock-price-news-19th-october-2026/liveblog/135048592.cms
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Highlights: Nasdaq leads Wall Street gains as chip, AI stocks rebound — ET Markets, 2026-10-19. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-us-market-live-updates-nasdaq-sp-500-iran-israel-war-hormuz-deal-brent-crude-oil-fed-rate-inflation-treasury-yields-earnings-forecast-coreweave-broadcom-micron-stock-price-news-19th-october-2026/liveblog/135048592.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-28 (d=0.1), 2025-08-22 (d=0.11)

### [RED 4.93] gbp_usd ↑
- gbp_usd [FX]: last 1.34, z20 2.93, zc 1.06, resid-z 1.45 [quiet], 1d 0.38%, |z20|=2.93
- **Mechanism**: gbp_usd ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eur_usd (co-move) — not yet - watch; rho 0.847 vs gbp_usd
- Watch next: aud_usd (co-move) — not yet - watch; rho 0.612 vs gbp_usd, historically leads by 5d
- Source: Sterling hits 17-month high against euro — ET Markets, 2026-10-19. https://economictimes.indiatimes.com/markets/forex/forex-news/sterling-hits-17-month-high-against-euro/articleshow/135048275.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-03 (d=0.02), 2025-09-15 (d=0.02)

### [RED 4.78] usd_cny ↓
- usd_cny [FX]: last 6.67, z20 -4.78, zc -3.75, resid-z -5.46 [unexplained], 1d -0.37%, |z20|=4.78; 1y-pct=0
- **Mechanism**: usd_cny ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-09-25 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-09-25 (d=0.0), 2025-08-22 (d=0.01), 2026-05-05 (d=0.01)

### [AMBER 4.3] dyn_wit ↑
- dyn_wit [EQUITIES]: last 1.97, z20 2.30, zc 0.56, resid-z 0.76 [quiet], 1d 2.13%, |z20|=2.30
- **Mechanism**: dyn_wit ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: What to do with IT stocks? TCS, HCL Tech, Wipro, Infosys, Tech Mahindra — Why experts are bullish after Accenture news — Mint Markets, 2026-10-19. https://www.livemint.com/market/stock-market-news/tcs-hcl-tech-wipro-infosys-to-tech-mahindra-experts-bullish-on-it-shares-after-accentures-shift-from-ai-investment-11792390800742.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-19 (d=0.04), 2025-08-21 (d=0.11)

### [AMBER 4.29] dyn_meta ↓
- dyn_meta [EQUITIES]: last 694.88, z20 -2.29, zc -0.60, resid-z -1.39 [quiet], 1d -1.50%, |z20|=2.29
- **Mechanism**: dyn_meta ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Meta's AI spending, Muse assistant adoption in focus for quarterly results — ET Markets, 2026-10-20. https://economictimes.indiatimes.com/markets/us-stocks/news/metas-ai-spending-muse-assistant-adoption-in-focus-for-quarterly-results/articleshow/135068976.cms
- Source: US Market: Wall Street’s AI rally faces test as Meta earnings loom — ET Markets, 2026-10-19. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-market-wall-streets-ai-rally-faces-test-as-meta-earnings-loom/articleshow/135039431.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2025-10-09 (d=0.12)

## Watchlist (below surfacing floor)
dyn_rs ↑ (4.28), dyn_4417_t ↑ (4.26), dyn_karurvysya_ns ↑ (3.88), gold_silver_ratio ↑ (3.74), usd_inr ↓ (3.7), nasdaq_100 ↓ (3.59), commodities · 3 series ↓ (3.42), hy_oas ↑ (3.31), indices · 2 series ↓ (3.01), dyn_jiofin_bo ↓ (2.95), midcap_largecap_ratio ↓ (2.66), eur_usd ↓ (2.43)

## India macro
- nifty_50: 22888.9492 (1d -1.11%, z20 0.13, flag none)
- nifty_midcap_100: 58483.4492 (1d -1.09%, z20 -1.12, flag none)
- usd_inr: 94.9150 (1d -0.07%, z20 -1.70, flag amber)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5551 (1d 0.02%, z20 -2.66, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 84.6 — "Multibagger: Union Bank of India shares up 300% in 5 years; can rally accelerate after Q2 "
- INDIANB.NS (INDIAN BANK) score 83.9 — "Multibagger: Union Bank of India shares up 300% in 5 years; can rally accelerate after Q2 "
- INOXINDIA.NS (INOX INDIA LIMITED) score 78.9 — "Multibagger: Union Bank of India shares up 300% in 5 years; can rally accelerate after Q2 "
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 78.6 — "Multibagger: Union Bank of India shares up 300% in 5 years; can rally accelerate after Q2 "
- BAC (Bank of America Corporation) score 77.1 — "Multibagger: Union Bank of India shares up 300% in 5 years; can rally accelerate after Q2 "
- HDB (HDFC Bank Limited) score 71.5 — "Multibagger: Union Bank of India shares up 300% in 5 years; can rally accelerate after Q2 "
- IDBI.NS (IDBI BANK LIMITED) score 68.4 — "Multibagger: Union Bank of India shares up 300% in 5 years; can rally accelerate after Q2 "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 68.4 — "Multibagger: Union Bank of India shares up 300% in 5 years; can rally accelerate after Q2 "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 68.4 — "Multibagger: Union Bank of India shares up 300% in 5 years; can rally accelerate after Q2 "
- TECHM.NS (TECH MAHINDRA LIMITED) score 54.7 — "UltraTech Cement Q2 net profit up 21% in September quarter"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 52.8 — "UltraTech Cement Q2 net profit up 21% in September quarter"
- TECH (Bio-Techne Corp) score 52.8 — "UltraTech Cement Q2 net profit up 21% in September quarter"
- COIN (Coinbase Global, Inc.) score 50.4 — "IMF sees milder global slowdown as AI boom offsets war hit — warns resilience is nearing l"
- OHI (Omega Healthcare Investors, In) score 48.5 — "Reliance Jio IPO: Massive bids top $25 bn amount for anchor book! How Mukesh Ambani firm a"
- CHKP (Check Point Software Technolog) score 38.7 — "Titan Q2 results 2026 date: Check Rekha Jhujhunwala portfolio stock returns, target, suppo"
- TGT (Target Corporation) score 34.5 — "Titan Q2 results 2026 date: Check Rekha Jhujhunwala portfolio stock returns, target, suppo"
- BOND (PIMCO Active Bond Exchange-Tra) score 34.0 — "French bond yields near 24-year high as new protests loom"
- RS (Reliance, Inc.) score 24.0 — "Reliance Jio IPO: Massive bids top $25 bn amount for anchor book! How Mukesh Ambani firm a"
- 301077.SZ (CHINASTARS) score 21.2 — "China Moves to Rein In Its Booming Hydrogen Industry"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 21.0 — "Oil Price Today (October 20): Crude oil nears $110 again as fresh attacks outweigh easing "
- LTH (Life Time Group Holdings, Inc.) score 18.6 — "TRUMP ON ZELENSKYY'S COMMENTS: TIME FOR SOMEONE ELSE TO NEGOTIATE ON BEHALF OF UKRAINE"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 17.3 — "Gold Holds Decline as Energy-Led Inflation Weighs on Rate Path"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 16.2 — "Bajaj Finance vs IREDA vs Reliance's Jio Financial: Top financial stock to buy after Q2 re"
- JIOFIN.BO (Jio Financial Services Limited) score 14.6 — "US Stocks: GE Aerospace raises 2026 profit forecast as services strength drives growth"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 13.6 — "Bajaj Finance vs IREDA vs Reliance's Jio Financial: Top financial stock to buy after Q2 re"
- SEPN (Septerna, Inc.) score 13.4 — "UltraTech Cement Q2 net profit up 21% in September quarter"
- BZ=F (Brent Crude Oil Last Day Finan) score 10.9 — "HEDGE FUNDS DUMP TECH STOCKS AT FASTEST PACE IN A DECADE Goldman Sachs reports that hedge "
- META (Meta) score 10.6 — "Meta's AI spending, Muse assistant adoption in focus for quarterly results"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.0 — "Tata Group stock to buy on Dussehra 2026 for money gains - Check target, stop loss by Choi"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 10.0 — "Tata Group stock to buy on Dussehra 2026 for money gains - Check target, stop loss by Choi"
- GS (Goldman Sachs Group, Inc. (The) score 9.2 — "It’s a rough housing market, and Goldman Sachs expects it to get worse"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.8 — "Top stocks to buy for short term: Just Dial, BSE, Orient Hotels - Target price, stop-loss "
- VT (Vanguard Total World Stock Ind) score 6.7 — "Already a hit? Reliance's Jio Platforms gets  ₹8,110 cr from anchor investors; LIC, New Wo"
- NVDA (NVIDIA Corporation) score 5.8 — "DEEPSEEK AND HUAWEI ARE COLLABORATING ON NEW AI CHIP DESIGNS TO CHALLENGE NVIDIA - THE IN "
- JEF (Jefferies Financial Group Inc.) score 5.5 — "ICICI Bank share price target after Q2 results: What are Jefferies, other analysts saying?"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.5 — "Dussehra 2026 special: Top 3 stocks to buy; ICICI Bank, Adani Ports, Reliance Industries |"
- WIT (Wipro Limited) score 3.3 — "What to do with IT stocks? TCS, HCL Tech, Wipro, Infosys, Tech Mahindra — Why experts are "
- DELL (Dell Technologies Inc.) score 0.9 — "Michael Dell Says in Interview That Just-in-Time Manufacturing Provides a Cushion if AI Bo"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.8 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
- VOLTAS.NS (VOLTAS LTD) score 0.0 — "Voltas’s market share is growing. Will margins follow?"

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