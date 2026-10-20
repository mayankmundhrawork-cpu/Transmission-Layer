# Transmission Layer — board brief · 2026-10-20 20:00Z

data as of **2026-10-20** · 97 series · 10 red / 29 amber · 8 events surfaced (28 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.659, 12d in regime; vol-pct 0.585, breadth-off 0.733, Markov P(high-vol) 0.014)
- [INVERTED] **safe_haven_gold** — corr20 -0.23, corr60 -0.38, contra nifty_50 corr20=0.41, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.8, corr60 0.82, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.26, corr60 0.21, last shift 2026-08-26. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.07, corr60 0.11, last shift 2026-09-01. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.74, corr60 -0.78, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.12, corr60 -0.0, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.18, corr60 -0.26, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.5, corr60 0.24, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.501** (n=1121) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=1915) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 7.09] commodities · 2 series ↑
- brent [COMMODITIES]: last 109.06, z20 1.72, zc -0.21, resid-z -0.34 [quiet], 1d -0.45%, |z20|=1.72
- wti [COMMODITIES]: last 98.14, z20 1.25, zc -2.13, resid-z -2.35 [unexplained], 1d -5.33%, 1-session move -5.33% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.604 vs brent, historically leads by 5d
- Watch next: brent_wti_spread (inverse) — not yet - watch; rho -0.391 vs wti, historically leads by 4d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.586 vs brent
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.564 vs brent
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.563 vs brent
- Source: Copper stays range bound as US tariff uncertainty, oil inflation risks weigh — ET Markets, 2026-10-20. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/copper-stays-range-bound-as-us-tariff-uncertainty-oil-inflation-risks-weigh/articleshow/135074839.cms
- Source: EU Stands Firm Against Arctic Oil and Gas Drilling Despite Energy Crisis — OilPrice, 2026-10-20. https://oilprice.com/Latest-Energy-News/World-News/EU-Stands-Firm-Against-Arctic-Oil-and-Gas-Drilling-Despite-Energy-Crisis.html
- Source: Chevron Moves to Take Over Russia's Most Prized Iraqi Oil Field — OilPrice, 2026-10-20. https://oilprice.com/Energy/Crude-Oil/Chevron-Moves-to-Take-Over-Russias-Most-Prized-Iraqi-Oil-Field.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

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

### [RED 5.68] dyn_justdial_bo ↑
- dyn_justdial_bo [EQUITIES]: last 732.55, z20 3.68, zc 0.82, resid-z 1.21 [quiet], 1d 2.82%, |z20|=3.68
- **Mechanism**: dyn_justdial_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.513 via dyn_justdial_bo, z 2.58, reacted); dyn_techm_ns (rho 0.505 via dyn_justdial_bo, z 3.49, reacted); nifty_50 (rho 0.454 via dyn_justdial_bo, z 0.13, quiet); dyn_tataelxsi_ns (rho 0.396 via dyn_justdial_bo, z 2.43, reacted); nifty_midcap_100 (rho 0.351 via dyn_justdial_bo, z -1.12, reacted)
- **India receivers**: nifty_it (rho 0.513, z 2.58); dyn_techm_ns (rho 0.505, z 3.49); nifty_50 (rho 0.454, z 0.13); dyn_tataelxsi_ns (rho 0.396, z 2.43)
- Source: Top stocks to buy for short term: Just Dial, BSE, Orient Hotels - Target price, stop-loss by Anand Rathi's expert — Mint Markets, 2026-10-20. https://www.livemint.com/market/stock-market-news/top-stocks-to-buy-for-short-term-just-dial-bse-orient-hotels-target-price-stop-loss-by-anand-rathis-expert-11792400725179.html
- Source: Just Dial shares skyrocket 13% as volume soars massively 115 times - More returns ahead or something else? Experts view — Mint Markets, 2026-10-19. https://www.livemint.com/market/stock-market-news/just-dial-shares-skyrocket-13-as-volume-soars-massively-115-times-more-returns-ahead-or-something-else-experts-view-11792394067468.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-18 (d=0.19), 2025-06-30 (d=0.52)

### [RED 5.15] dyn_wit ↑
- dyn_wit [EQUITIES]: last 2.06, z20 3.15, zc 1.69, resid-z 0.76 [moved], 1d 6.48%, |z20|=3.15
- **Mechanism**: dyn_wit ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: What to do with IT stocks? TCS, HCL Tech, Wipro, Infosys, Tech Mahindra — Why experts are bullish after Accenture news — Mint Markets, 2026-10-19. https://www.livemint.com/market/stock-market-news/tcs-hcl-tech-wipro-infosys-to-tech-mahindra-experts-bullish-on-it-shares-after-accentures-shift-from-ai-investment-11792390800742.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-19 (d=0.04), 2025-08-21 (d=0.11)

### [RED 4.78] dow_jones ↑
- dow_jones [INDICES]: last 52491.76, z20 2.78, zc 1.36, resid-z 1.83 [unexplained], 1d 1.01%, |z20|=2.78
- **Mechanism**: dow_jones ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.9 vs dow_jones
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.688 vs dow_jones, historically leads by 1d
- Watch next: dyn_bond (co-move) — not yet - watch; rho 0.585 vs dow_jones, historically leads by 1d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.779 vs dow_jones
- Watch next: dyn_jef (co-move) — not yet - watch; rho 0.552 vs dow_jones, historically leads by 2d
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: US stocks open lower as AI stocks decline, oil prices rise — ET Markets, 2026-10-20. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-fed-rate-treasury-yields-earnings-forecast-nvidia-macys-gamestop-stock-price-news-20th-september-2026/liveblog/135069926.cms
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: S&P 500 Healthcare hits record high, Dow soars over 500 points — ET Markets, 2026-10-20. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-fed-rate-treasury-yields-earnings-forecast-nvidia-macys-gamestop-stock-price-news-20th-september-2026/liveblog/135069926.cms
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: S&P 500, Nasdaq climb as AI-linked stocks recover ahead of earnings — ET Markets, 2026-10-19. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-us-market-live-updates-nasdaq-sp-500-iran-israel-war-hormuz-deal-brent-crude-oil-fed-rate-inflation-treasury-yields-earnings-forecast-coreweave-broadcom-micron-stock-price-news-19th-october-2026/liveblog/135048592.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-28 (d=0.1), 2025-08-22 (d=0.11)

### [RED 4.78] gbp_usd ↑
- gbp_usd [FX]: last 1.34, z20 2.78, zc 0.91, resid-z 1.22 [quiet], 1d 0.33%, |z20|=2.78
- **Mechanism**: gbp_usd ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eur_usd (co-move) — not yet - watch; rho 0.846 vs gbp_usd
- Watch next: aud_usd (co-move) — not yet - watch; rho 0.607 vs gbp_usd, historically leads by 5d
- Source: Sterling hits 17-month high against euro — ET Markets, 2026-10-19. https://economictimes.indiatimes.com/markets/forex/forex-news/sterling-hits-17-month-high-against-euro/articleshow/135048275.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-03 (d=0.02), 2025-09-15 (d=0.02)

### [AMBER 4.36] dyn_meta ↓
- dyn_meta [EQUITIES]: last 693.68, z20 -2.36, zc -0.67, resid-z -1.39 [quiet], 1d -1.67%, |z20|=2.36
- **Mechanism**: dyn_meta ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Meta's AI spending, Muse assistant adoption in focus for quarterly results — ET Markets, 2026-10-20. https://economictimes.indiatimes.com/markets/us-stocks/news/metas-ai-spending-muse-assistant-adoption-in-focus-for-quarterly-results/articleshow/135068976.cms
- Source: Meta’s AI spending and Muse adoption set to test Zuckerberg’s strategy — ET Markets, 2026-10-20. https://economictimes.indiatimes.com/markets/us-stocks/news/metas-ai-spending-muse-assistant-adoption-in-focus-for-quarterly-results/articleshow/135068976.cms
- Source: US Market: Wall Street’s AI rally faces test as Meta earnings loom — ET Markets, 2026-10-19. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-market-wall-streets-ai-rally-faces-test-as-meta-earnings-loom/articleshow/135039431.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2025-10-09 (d=0.12)

### [AMBER 4.26] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 7510.00, z20 2.26, zc 0.10, resid-z 2.82 [unexplained], 1d 0.54%, |z20|=2.26; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Hindustan Zinc shares: Experts bullish on Anil Agarwal-led metal stock after robust Q2 results 2026 | Target, stop-loss — Mint Markets, 2026-10-20. https://www.livemint.com/market/stock-market-news/hindustan-zinc-shares-experts-bullish-on-anil-agarwal-led-metal-stock-after-robust-q2-results-2026-target-stoploss-11792474520524.html
- Source: Why should you buy Vedanta shares despite strong Hindustan Zinc Q2 results 2026? Experts' views, target price — Mint Markets, 2026-10-20. https://www.livemint.com/market/stock-market-news/why-should-you-buy-vedanta-shares-despite-strong-hindustan-zinc-q2-results-2026-experts-views-target-price-stoploss-11792469059843.html
- Source: Oil Price Today (October 20): Crude oil nears $110 again as fresh attacks outweigh easing Russian sanctions. What are experts saying? — ET Markets, 2026-10-20. https://economictimes.indiatimes.com/markets/commodities/news/oil-price-today-october-20-crude-oil-nears-110-again-as-fresh-attacks-outweigh-easing-russian-sanctions-what-are-experts-saying/articleshow/135059918.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

## Watchlist (below surfacing floor)
dyn_bac ↓ (4.02), dyn_rs ↑ (4.01), nasdaq_100 ↓ (3.99), usd_inr ↓ (3.91), dyn_karurvysya_ns ↑ (3.88), commodities · 3 series ↓ (3.87), gold_silver_ratio ↑ (3.84), hy_oas ↑ (3.31), usd_cny ↓ (3.26), dyn_tech ↑ (3.04), indices · 2 series ↓ (3.01), dyn_jiofin_bo ↓ (2.95)

## India macro
- nifty_50: 22888.9492 (1d -1.11%, z20 0.13, flag none)
- nifty_midcap_100: 58483.4492 (1d -1.09%, z20 -1.12, flag none)
- usd_inr: 94.7900 (1d -0.20%, z20 -1.91, flag amber)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5551 (1d 0.02%, z20 -2.66, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 81.7 — "Indian govt’s price correction of ethanol from maize may help balance distortion"
- INDIANB.NS (INDIAN BANK) score 80.9 — "Indian govt’s price correction of ethanol from maize may help balance distortion"
- INOXINDIA.NS (INOX INDIA LIMITED) score 76.2 — "Indian govt’s price correction of ethanol from maize may help balance distortion"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 75.9 — "Indian govt’s price correction of ethanol from maize may help balance distortion"
- BAC (Bank of America Corporation) score 73.5 — "Multibagger: Union Bank of India shares up 300% in 5 years; can rally accelerate after Q2 "
- HDB (HDFC Bank Limited) score 68.2 — "Multibagger: Union Bank of India shares up 300% in 5 years; can rally accelerate after Q2 "
- IDBI.NS (IDBI BANK LIMITED) score 65.2 — "Multibagger: Union Bank of India shares up 300% in 5 years; can rally accelerate after Q2 "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 65.2 — "Multibagger: Union Bank of India shares up 300% in 5 years; can rally accelerate after Q2 "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 65.2 — "Multibagger: Union Bank of India shares up 300% in 5 years; can rally accelerate after Q2 "
- TECHM.NS (TECH MAHINDRA LIMITED) score 53.2 — "Investors’ search for safety has made toothpaste stocks more expensive than tech"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 51.3 — "Investors’ search for safety has made toothpaste stocks more expensive than tech"
- TECH (Bio-Techne Corp) score 51.3 — "Investors’ search for safety has made toothpaste stocks more expensive than tech"
- OHI (Omega Healthcare Investors, In) score 48.2 — "Investors’ search for safety has made toothpaste stocks more expensive than tech"
- COIN (Coinbase Global, Inc.) score 48.0 — "IMF sees milder global slowdown as AI boom offsets war hit — warns resilience is nearing l"
- CHKP (Check Point Software Technolog) score 36.9 — "Titan Q2 results 2026 date: Check Rekha Jhujhunwala portfolio stock returns, target, suppo"
- BOND (PIMCO Active Bond Exchange-Tra) score 34.4 — "BESSENT: PEOPLE ARE COMING IN TO BOND MARKET AT A PRICE -2WAY TV"
- TGT (Target Corporation) score 32.9 — "Titan Q2 results 2026 date: Check Rekha Jhujhunwala portfolio stock returns, target, suppo"
- RS (Reliance, Inc.) score 22.8 — "Reliance Jio IPO: Massive bids top $25 bn amount for anchor book! How Mukesh Ambani firm a"
- 301077.SZ (CHINASTARS) score 22.2 — "CHINA'S COMMERCE MINISTRY, ON US ORDER ON DEEPSEEK: CHINA FIRMLY OPPOSES THIS"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 20.0 — "Oil Price Today (October 20): Crude oil nears $110 again as fresh attacks outweigh easing "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 19.5 — "US ENERGY UNDER SECRETARY HAUSTVEIT SAYS DIESEL PRICES ARE HIGHER THAN ANYONE WANTS RIGHT "
- LTH (Life Time Group Holdings, Inc.) score 18.7 — "Wall Street rebounds from lows as upbeat earnings, falling oil prices lift sentiment; Micr"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 15.4 — "Bajaj Finance vs IREDA vs Reliance's Jio Financial: Top financial stock to buy after Q2 re"
- JIOFIN.BO (Jio Financial Services Limited) score 15.0 — "It’s no secret what the best financial advice for retirement is — but most people ignore i"
- SEPN (Septerna, Inc.) score 14.8 — "GOLDMAN SACHS: U.S. GDP HOLDS STRONG DESPITE HOUSING SLUMP U.S. housing starts plunged 5.2"
- BZ=F (Brent Crude Oil Last Day Finan) score 14.4 — "AMZN - AMAZON GOES BIG ON HOLIDAY HIRING AS U.S. RETAIL PULLS BACK Amazon plans to hire ov"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 13.0 — "Bajaj Finance vs IREDA vs Reliance's Jio Financial: Top financial stock to buy after Q2 re"
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.4 — "It’s not just California’s billionaire tax. Wealth is on the ballot in the midterm electio"
- META (Meta) score 11.1 — "Meta’s AI spending and Muse adoption set to test Zuckerberg’s strategy"
- GS (Goldman Sachs Group, Inc. (The) score 9.8 — "GOLDMAN SACHS: U.S. GDP HOLDS STRONG DESPITE HOUSING SLUMP U.S. housing starts plunged 5.2"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.5 — "Tata Group stock to buy on Dussehra 2026 for money gains - Check target, stop loss by Choi"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.5 — "Tata Group stock to buy on Dussehra 2026 for money gains - Check target, stop loss by Choi"
- VT (Vanguard Total World Stock Ind) score 7.4 — "In charts: How one of the world's biggest economies got trapped by debt"
- NVDA (NVIDIA Corporation) score 5.5 — "DEEPSEEK AND HUAWEI ARE COLLABORATING ON NEW AI CHIP DESIGNS TO CHALLENGE NVIDIA - THE IN "
- JEF (Jefferies Financial Group Inc.) score 5.2 — "ICICI Bank share price target after Q2 results: What are Jefferies, other analysts saying?"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.2 — "Dussehra 2026 special: Top 3 stocks to buy; ICICI Bank, Adani Ports, Reliance Industries |"
- WIT (Wipro Limited) score 3.1 — "What to do with IT stocks? TCS, HCL Tech, Wipro, Infosys, Tech Mahindra — Why experts are "
- DELL (Dell Technologies Inc.) score 0.9 — "Michael Dell Says in Interview That Just-in-Time Manufacturing Provides a Cushion if AI Bo"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.7 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
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