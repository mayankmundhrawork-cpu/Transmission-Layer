# Transmission Layer — board brief · 2026-10-19 22:20Z

data as of **2026-10-19** · 97 series · 11 red / 27 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.784, 11d in regime; vol-pct 0.693, breadth-off 0.875, Markov P(high-vol) 0.022)
- [INVERTED] **safe_haven_gold** — corr20 -0.27, corr60 -0.37, contra nifty_50 corr20=0.4, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.84, corr60 0.83, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.24, corr60 0.2, last shift 2026-08-26. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.11, corr60 0.11, last shift 2026-09-01. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.78, corr60 -0.78, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.09, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.18, corr60 -0.26, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.54, corr60 0.23, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** ftse_100 → asx_200: leads 1d (ccf 0.264, β 0.2683, p 0.02588); driver zc -1.54 → expected -0.288%. Type hit-rate 0.81 (n=2022).
- Track record · residual_reversion: hit-rate **0.502** (n=1120) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.81** (n=2022) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.51] commodities · 2 series ↑
- brent [COMMODITIES]: last 109.09, z20 2.01, zc -0.31, resid-z 0.01 [quiet], 1d -0.70%, |z20|=2.01
- wti [COMMODITIES]: last 98.12, z20 1.68, zc -1.29, resid-z -0.99 [quiet], 1d -3.24%, 1-session move -3.24% ≥ 1.5%; |z20|=1.68
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.598 vs brent, historically leads by 5d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.587 vs brent
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.56 vs brent
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.558 vs brent
- Source: New Oil Fields Should Have to Build the Carbon Storage Market — OilPrice, 2026-10-19. https://oilprice.com/Energy/Energy-General/New-Oil-Fields-Should-Have-to-Build-the-Carbon-Storage-Market.html
- Source: Why Canadian Oil Is Lagging Even As Global Crude Soars — OilPrice, 2026-10-19. https://oilprice.com/Energy/Crude-Oil/Why-Canadian-Oil-Is-Lagging-Even-As-Global-Crude-Soars.html
- Source: Canada's Inflation Rises to 3.1% as Fuel Oil Prices Jump 58% — OilPrice, 2026-10-19. https://oilprice.com/Latest-Energy-News/World-News/Canadas-Inflation-Rises-to-31-as-Fuel-Oil-Prices-Jump-58.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 6.8] cross-asset · 3 series ↑
- dyn_techm_ns [EQUITIES]: last 1779.10, z20 3.49, zc -0.20, resid-z 0.68 [quiet], 1d -0.61%, |z20|=3.49; 1y-pct=99
- nifty_it [INDICES]: last 31516.30, z20 2.58, zc -0.63, resid-z 0.26 [quiet], 1d -1.28%, |z20|=2.58
- dyn_tataelxsi_ns [EQUITIES]: last 3790.00, z20 2.43, zc -0.61, resid-z 0.33 [quiet], 1d -1.56%, |z20|=2.43
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
- dyn_justdial_bo [EQUITIES]: last 732.55, z20 3.68, zc 0.82, resid-z 1.22 [quiet], 1d 2.82%, |z20|=3.68
- **Mechanism**: dyn_justdial_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.513 via dyn_justdial_bo, z 2.58, reacted); dyn_techm_ns (rho 0.505 via dyn_justdial_bo, z 3.49, reacted); nifty_50 (rho 0.454 via dyn_justdial_bo, z 0.13, quiet); dyn_tataelxsi_ns (rho 0.396 via dyn_justdial_bo, z 2.43, reacted); nifty_midcap_100 (rho 0.351 via dyn_justdial_bo, z -1.12, reacted)
- **India receivers**: nifty_it (rho 0.513, z 2.58); dyn_techm_ns (rho 0.505, z 3.49); nifty_50 (rho 0.454, z 0.13); dyn_tataelxsi_ns (rho 0.396, z 2.43)
- Source: Just Dial shares skyrocket 13% as volume soars massively 115 times - More returns ahead or something else? Experts view — Mint Markets, 2026-10-19. https://www.livemint.com/market/stock-market-news/just-dial-shares-skyrocket-13-as-volume-soars-massively-115-times-more-returns-ahead-or-something-else-experts-view-11792394067468.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-18 (d=0.19), 2025-06-30 (d=0.52)

### [AMBER 5.01] indices · 2 series ↓
- nasdaq_100 [INDICES]: last 29536.02, z20 -2.18, zc 0.84, resid-z -1.80 [unexplained], 1d 1.19%, |z20|=2.18
- russell_2000 [INDICES]: last 2727.92, z20 -2.03, zc 0.16, resid-z -0.02 [quiet], 1d 0.24%, |z20|=2.03
- **Mechanism**: indices · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.916 vs nasdaq_100
- Watch next: dyn_bond (co-move) — not yet - watch; rho 0.53 vs russell_2000, historically leads by 1d
- Watch next: ust_10y (inverse) — not yet - watch; rho -0.507 vs russell_2000, historically leads by 1d
- Source: US stocks today: Nasdaq leads Wall Street gains as chip, AI stocks rebound — ET Markets, 2026-10-19. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-nasdaq-leads-wall-street-gains-as-chip-ai-stocks-rebound/articleshow/135056194.cms
- Source: S&P 500, NASDAQ EXTEND GAINS; LAST UP 0.7% AND 1.4%, RESPECTIVELY — DeItaone, 2026-10-19. https://t.me/walter_bloomberg/37308
- Source: US stocks today: S&P 500, Nasdaq climb as AI-linked stocks recover ahead of earnings — ET Markets, 2026-10-19. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-sp-500-nasdaq-open-higher-as-ai-stocks-rebound-ahead-of-major-earnings/articleshow/135050156.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-18 (d=0.06), 2025-05-07 (d=0.12)

### [AMBER 4.85] cross-asset · 2 series ↓
- dyn_coin [EQUITIES]: last 168.45, z20 -2.01, zc -0.59, resid-z -1.10 [quiet], 1d -2.72%, |z20|=2.01
- eth_usd [CRYPTO]: last 2414.23, z20 -1.58, zc -0.06, resid-z -0.33 [quiet], 1d -0.23%, |z20|=1.58
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-04-03 (z-distance 0.11).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.575 vs eth_usd, historically leads by 1d
- Watch next: dxy (inverse) — not yet - watch; rho -0.513 vs eth_usd, historically leads by 1d
- Source: S&P Global flags potentially hidden AI debt at hyperscalers as AI spending surges — ET Markets, 2026-10-19. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/sp-global-flags-potentially-hidden-ai-debt-at-hyperscalers-as-ai-spending-surges/articleshow/135054758.cms
- Source: Why Canadian Oil Is Lagging Even As Global Crude Soars — OilPrice, 2026-10-19. https://oilprice.com/Energy/Crude-Oil/Why-Canadian-Oil-Is-Lagging-Even-As-Global-Crude-Soars.html
- Source: JPMORGAN FORECASTS 7% ANNUAL RETURNS FOR 60/40 PORTFOLIOS J.P. Morgan Asset Management projects a 7.0% annual return for a traditional 60/40 stock-bond portfolio over the next 10–15 years. Key annualized forecasts: 🔸 U.S. stocks: 7.5% 🔸 Global bonds: 5.3% 🔸 Private equity: 9.8% 🔸 Gold: 5.5% Adding d — DeItaone, 2026-10-19. https://t.me/walter_bloomberg/37316
- Historical analogues: 2025-04-03 (d=0.11), 2025-10-22 (d=0.25), 2025-10-30 (d=0.36)

### [RED 4.75] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 7530.00, z20 2.75, zc 0.37, resid-z 2.82 [unexplained], 1d 2.03%, |z20|=2.75; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Gold price to touch  ₹1.60 lakh by Dec 2026 end? Time to buy? What experts say to earn money from yellow metal deals — Mint Markets, 2026-10-19. https://www.livemint.com/market/commodities/gold-price-to-touch-rs-1-60-lakh-by-dec-2026-end-time-to-buy-what-experts-say-to-earn-money-from-yellow-metal-deals-11792405015486.html
- Source: IDBI Bank shares delivered almost no returns in 20 years. Can Fairfax deal finally turn stock around? Experts weigh in — Mint Markets, 2026-10-19. https://www.livemint.com/market/stock-market-news/idbi-bank-shares-delivered-almost-no-returns-in-20-years-can-fairfax-deal-finally-turn-stock-around-experts-weigh-in-11792400766427.html
- Source: Just Dial shares skyrocket 13% as volume soars massively 115 times - More returns ahead or something else? Experts view — Mint Markets, 2026-10-19. https://www.livemint.com/market/stock-market-news/just-dial-shares-skyrocket-13-as-volume-soars-massively-115-times-more-returns-ahead-or-something-else-experts-view-11792394067468.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

### [RED 4.62] gold_silver_ratio ↑
- gold_silver_ratio [DERIVED]: last 72.75, z20 1.62, zc n/a, resid-z n/a [quiet], 1d -0.82%, GSR<75 (extreme low); |z20|=1.62
- **Mechanism**: gold_silver_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (inverse) — not yet - watch; rho -0.53 vs gold_silver_ratio, historically leads by 3d
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

### [AMBER 4.36] dyn_bac ↓
- dyn_bac [EQUITIES]: last 50.39, z20 -2.36, zc -0.97, resid-z 0.59 [quiet], 1d -1.64%, |z20|=2.36
- **Mechanism**: dyn_bac ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Why Invading Iran Could Become America's Biggest Military Mistake — OilPrice, 2026-10-19. https://oilprice.com/Energy/Energy-General/Why-Invading-Iran-Could-Become-Americas-Biggest-Military-Mistake.html
- Source: Colombia’s Critical Minerals Could Be a Game Changer for America — OilPrice, 2026-10-19. https://oilprice.com/Energy/Energy-General/Colombias-Critical-Minerals-Could-Be-a-Game-Changer-for-America.html
- Source: Elon Musk pledges a share of SpaceX company to 'every kid in America' — ET Markets, 2026-10-19. https://economictimes.indiatimes.com/markets/us-stocks/news/elon-musk-pledges-a-share-of-spacex-company-to-every-kid-in-america/articleshow/135048478.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-23 (d=0.03), 2025-03-31 (d=0.12)

## Watchlist (below surfacing floor)
dyn_rs ↑ (4.22), dyn_301077_sz ↓ (4.17), dyn_wit ↑ (4.04), usd_inr ↓ (3.92), dyn_karurvysya_ns ↑ (3.88), hy_oas ↑ (3.54), commodities · 3 series ↓ (3.51), usd_cny ↓ (3.06), eur_usd ↓ (2.82), dyn_dell ↓ (2.7), midcap_largecap_ratio ↓ (2.66), asx_200 ↑ (2.56)

## India macro
- nifty_50: 22888.9492 (1d -1.11%, z20 0.13, flag none)
- nifty_midcap_100: 58483.4492 (1d -1.09%, z20 -1.12, flag none)
- usd_inr: 94.9150 (1d 0.41%, z20 -1.92, flag amber)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5551 (1d 0.02%, z20 -2.66, flag red)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 82.8 — "Jio Platforms IPO listing: Can Reliance overtake Tata Group as India’s largest conglomerat"
- INDIANB.NS (INDIAN BANK) score 82.0 — "GOLDMAN SACHS ON GOLD: ESTIMATES CENTRAL BANK PURCHASES OF 79 TONNES IN AUGUST, WELL ABOVE"
- INOXINDIA.NS (INOX INDIA LIMITED) score 78.4 — "Jio Platforms IPO listing: Can Reliance overtake Tata Group as India’s largest conglomerat"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 78.0 — "Jio Platforms IPO listing: Can Reliance overtake Tata Group as India’s largest conglomerat"
- BAC (Bank of America Corporation) score 75.2 — "GOLDMAN SACHS ON GOLD: ESTIMATES CENTRAL BANK PURCHASES OF 79 TONNES IN AUGUST, WELL ABOVE"
- HDB (HDFC Bank Limited) score 69.7 — "GOLDMAN SACHS ON GOLD: ESTIMATES CENTRAL BANK PURCHASES OF 79 TONNES IN AUGUST, WELL ABOVE"
- IDBI.NS (IDBI BANK LIMITED) score 66.0 — "GOLDMAN SACHS ON GOLD: ESTIMATES CENTRAL BANK PURCHASES OF 79 TONNES IN AUGUST, WELL ABOVE"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 66.0 — "GOLDMAN SACHS ON GOLD: ESTIMATES CENTRAL BANK PURCHASES OF 79 TONNES IN AUGUST, WELL ABOVE"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 66.0 — "GOLDMAN SACHS ON GOLD: ESTIMATES CENTRAL BANK PURCHASES OF 79 TONNES IN AUGUST, WELL ABOVE"
- TECHM.NS (TECH MAHINDRA LIMITED) score 61.1 — "Q2 Results Today Highlights: UltraTech Q2 profit declines q-o-q, Hindustan Zinc, Union Ban"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 58.9 — "Q2 Results Today Highlights: UltraTech Q2 profit declines q-o-q, Hindustan Zinc, Union Ban"
- TECH (Bio-Techne Corp) score 58.9 — "Q2 Results Today Highlights: UltraTech Q2 profit declines q-o-q, Hindustan Zinc, Union Ban"
- COIN (Coinbase Global, Inc.) score 51.3 — "JPMORGAN FORECASTS 7% ANNUAL RETURNS FOR 60/40 PORTFOLIOS J.P. Morgan Asset Management pro"
- OHI (Omega Healthcare Investors, In) score 45.8 — "Jio IPO: LIC, BlackRock, Fidelity, GIC among 212 anchor investors to pour Rs 8,110 crore"
- BOND (PIMCO Active Bond Exchange-Tra) score 34.3 — "FRENCH 10-YEAR BOND YIELDS RISE FURTHER, UP 16 BPS AT 4.94%"
- CHKP (Check Point Software Technolog) score 32.0 — "Muhurat Trading 2026: BSE, NSE announce date and timings of special session. Check details"
- TGT (Target Corporation) score 29.3 — "When should you dump your target-date funds?"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 21.3 — "IDBI Bank shares delivered almost no returns in 20 years. Can Fairfax deal finally turn st"
- RS (Reliance, Inc.) score 21.3 — "Already a hit? Reliance's Jio Platforms gets  ₹8,110 cr from anchor investors; LIC, New Wo"
- LTH (Life Time Group Holdings, Inc.) score 20.8 — "U.S. HOUSING MARKET CONFIDENCE HITS 14-YEAR LOW U.S. homebuilder sentiment fell to 29 in O"
- 301077.SZ (CHINASTARS) score 19.2 — "China’s Solar Exports Keep Falling as Beijing Mulls Export Controls"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 18.1 — "RUSSIA'S LAVROV: WE ARE NOT INTERESTED IN ENERGY PRICES VOLATILITY"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 17.8 — "Q2 Results Today Highlights: UltraTech Q2 profit declines q-o-q, Hindustan Zinc, Union Ban"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 14.8 — "Q2 Results Today Highlights: UltraTech Q2 profit declines q-o-q, Hindustan Zinc, Union Ban"
- SEPN (Septerna, Inc.) score 14.7 — "WHITE HOUSE WARNS U.S. INFLATION NEEDS MORE WORK White House economic adviser Kevin Hasset"
- JIOFIN.BO (Jio Financial Services Limited) score 13.7 — "Retiring abroad? Don’t cut these financial ties to the U.S."
- BZ=F (Brent Crude Oil Last Day Finan) score 10.7 — "S&P 500, NASDAQ EXTEND GAINS; LAST UP 0.7% AND 1.4%, RESPECTIVELY"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.6 — "Jio Platforms IPO listing: Can Reliance overtake Tata Group as India’s largest conglomerat"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 10.6 — "Jio Platforms IPO listing: Can Reliance overtake Tata Group as India’s largest conglomerat"
- META (Meta) score 9.0 — "TSX pulls back from three-week high as financials, metal miners fall"
- GS (Goldman Sachs Group, Inc. (The) score 8.7 — "GOLDMAN SACHS ON GOLD: ESTIMATES CENTRAL BANK PURCHASES OF 79 TONNES IN AUGUST, WELL ABOVE"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.0 — "PC Jeweller shares soar 26% in just two sessions. Here’s what’s triggering the sharp surge"
- VT (Vanguard Total World Stock Ind) score 7.9 — "Already a hit? Reliance's Jio Platforms gets  ₹8,110 cr from anchor investors; LIC, New Wo"
- NVDA (NVIDIA Corporation) score 6.8 — "DEEPSEEK AND HUAWEI ARE COLLABORATING ON NEW AI CHIP DESIGNS TO CHALLENGE NVIDIA - THE IN "
- JEF (Jefferies Financial Group Inc.) score 6.4 — "ICICI Bank share price target after Q2 results: What are Jefferies, other analysts saying?"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.3 — "Nifty falls below 22,300 at noon as Adani Stocks, ITC, Metals slide"
- WIT (Wipro Limited) score 3.8 — "What to do with IT stocks? TCS, HCL Tech, Wipro, Infosys, Tech Mahindra — Why experts are "
- DELL (Dell Technologies Inc.) score 1.1 — "Michael Dell Says in Interview That Just-in-Time Manufacturing Provides a Cushion if AI Bo"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.9 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
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