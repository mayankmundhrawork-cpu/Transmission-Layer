# Transmission Layer — board brief · 2026-09-18 08:59Z

data as of **2026-09-18** · 97 series · 10 red / 33 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.491, 2d in regime; vol-pct 0.231, breadth-off 0.75, Markov P(high-vol) 0.032)
- [INVERTED] **safe_haven_gold** — corr20 -0.49, corr60 -0.25, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.79, corr60 0.87, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.18, corr60 0.33, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.21, corr60 0.1, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.84, last shift 2026-07-24. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.09, corr60 -0.05, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.27, corr60 -0.07, last shift 2026-07-28. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.38, corr60 0.14, last shift 2026-07-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** sp500 → asx_200: leads 1d (ccf 0.572, β 0.4402, p 0.0); driver zc 1.53 → expected 0.497%. Type hit-rate 0.823 (n=2121).
- **SETUP** nasdaq_100 → asx_200: leads 1d (ccf 0.489, β 0.2799, p 0.0); driver zc 1.75 → expected 0.481%. Type hit-rate 0.823 (n=2121).
- **SETUP** dyn_bond → gbp_usd: leads 1d (ccf 0.305, β 0.432, p 0.0); driver zc 1.8 → expected 0.256%. Type hit-rate 0.823 (n=2121).
- Track record · residual_reversion: hit-rate **0.498** (n=1100) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.823** (n=2121) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.53] cross-asset · 10 series ↑
- tips_10y_real [RATES]: last 2.68, z20 2.77, zc 1.33, resid-z 0.46 [quiet], 1d 2.29%, 1d move +6.0bps ≥ 5bps; |z20|=2.77; 1y-pct=100
- ust_2y [RATES]: last 4.74, z20 2.41, zc 1.15, resid-z 0.04 [quiet], 1d 1.50%, |z20|=2.41; 1y-pct=100
- dyn_ms [EQUITIES]: last 203.48, z20 -2.33, zc 0.28, resid-z -0.58 [quiet], 1d 0.52%, |z20|=2.33
- ust_10y [RATES]: last 5.01, z20 2.12, zc 0.21, resid-z -0.58 [quiet], 1d 0.20%, |z20|=2.12; 1y-pct=100
- dow_jones [INDICES]: last 51776.48, z20 -1.93, zc 0.69, resid-z -0.57 [quiet], 1d 0.61%, |z20|=1.93
- ust_30y [RATES]: last 5.35, z20 1.57, zc -0.24, resid-z -0.64 [quiet], 1d -0.19%, |z20|=1.57; 1y-pct=98
- russell_2000 [INDICES]: last 2875.10, z20 -1.57, zc 0.50, resid-z -0.77 [quiet], 1d 0.57%, |z20|=1.57
- dyn_bond [EQUITIES]: last 89.08, z20 -1.11, zc 1.80, resid-z 0.19 [priced], 1d 0.59%, 1y-pct=2
- wti [COMMODITIES]: last 95.52, z20 0.41, zc -2.13, resid-z 0.53 [moved], 1d -6.27%, 1-session move -6.27% ≥ 1.5%
- brent [COMMODITIES]: last 98.54, z20 0.17, zc -2.28, resid-z 0.41 [priced], 1d -5.99%, 1-session move -5.99% ≥ 1.5%
- **Mechanism**: cross-asset · 10 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.468 via dyn_bond, z 0.64, quiet)
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.717 vs dyn_ms, historically leads by 4d
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.59 vs dyn_ms, historically leads by 4d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.766 vs dyn_ms
- Watch next: dyn_coin (co-move) — not yet - watch; rho 0.54 vs russell_2000, historically leads by 1d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.738 vs dyn_ms
- **India receivers**: midcap_largecap_ratio (rho 0.468, z 0.64)
- Source: Sensex today | Stock Market Live: Sensex, Nifty gain as lower oil prices and global cues offset IT, Tata stocks drag — BusinessLine Mkts, 2026-09-18. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-18th-september-2026/article71477821.ece
- Source: US Market: Nike’s position in Dow Jones index comes under pressure — ET Markets, 2026-09-18. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-market-nikes-position-in-dow-jones-index-comes-under-pressure/articleshow/134329444.cms
- Source: Rising oil, borrowing costs fuel stagflation fears for global economy — ET Markets, 2026-09-18. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/rising-oil-borrowing-costs-fuel-stagflation-fears-for-global-economy/articleshow/134329348.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-14 (d=0.79), 2025-05-15 (d=0.79)

### [RED 5.62] gold_silver_ratio ↓
- gold_silver_ratio [DERIVED]: last 65.54, z20 -2.62, zc n/a, resid-z n/a [quiet], 1d -2.47%, GSR<75 (extreme low); |z20|=2.62
- **Mechanism**: gold_silver_ratio ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.393 via gold_silver_ratio, z -1.01, reacted)
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.868 vs gold_silver_ratio
- Watch next: comex_copper (inverse) — not yet - watch; rho -0.62 vs gold_silver_ratio, historically leads by 3d
- **India receivers**: nifty_midcap_100 (rho -0.393, z -1.01)
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

### [RED 5.51] dxy ↑
- dxy [FX]: last 100.38, z20 2.51, zc 0.45, resid-z 2.15 [unexplained], 1d 0.16%, 20d range extreme; |z20|=2.51
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [RED 4.87] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 5760.00, z20 2.87, zc 0.85, resid-z 0.28 [quiet], 1d 3.04%, |z20|=2.87; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Gold and silver prices volatile amid a decline in oil prices, stable dollar; experts highlight key levels to watch — Mint Markets, 2026-09-18. https://www.livemint.com/market/commodities/gold-and-silver-prices-volatile-amid-a-decline-in-oil-prices-stable-dollar-experts-highlight-key-levels-to-watch-11789702442886.html
- Source: Apollo Micro Systems share price jumps 3.5% after recent fall | technical experts flag key levels — Mint Markets, 2026-09-17. https://www.livemint.com/market/stock-market-news/apollo-micro-systems-share-price-jumps-3-5-after-recent-fall-technical-experts-flag-key-levels-11789626185762.html
- Source: NSE IPO buzz lifts New India Assurance, IFCI up to 9% | What do technical experts say? — Mint Markets, 2026-09-17. https://www.livemint.com/market/stock-market-news/nse-ipo-buzz-lifts-new-india-assurance-ifci-up-to-9-what-do-technical-experts-say-11789623090580.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

### [RED 4.78] dyn_bac ↓
- dyn_bac [EQUITIES]: last 58.17, z20 -2.78, zc 0.25, resid-z -2.13 [unexplained], 1d 0.47%, |z20|=2.78
- **Mechanism**: dyn_bac ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: How Bessent, America's bond salesman, cornered Japan on big spending — ET Markets, 2026-09-18. https://economictimes.indiatimes.com/markets/us-stocks/news/how-bessent-americas-bond-salesman-cornered-japan-on-big-spending/articleshow/134326610.cms
- Source: America Is Paying a Lot for Fuel, Not Running Out of Gasoline — OilPrice, 2026-09-17. https://oilprice.com/Latest-Energy-News/World-News/America-Is-Paying-a-Lot-for-Fuel-Not-Running-Out-of-Gasoline.html
- Source: TRUMP: LOWER INTEREST RATES FOR UNITED STATES OF AMERICA, AND FAST — DeItaone, 2026-09-16. https://t.me/walter_bloomberg/35874
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

### [AMBER 4.62] cross-asset · 2 series ↓
- nifty_it [INDICES]: last 28707.80, z20 -1.79, zc -1.02, resid-z -1.38 [quiet], 1d -1.54%, |z20|=1.79
- dyn_tataelxsi_ns [EQUITIES]: last 3340.10, z20 -1.66, zc -0.70, resid-z -0.62 [quiet], 1d -1.23%, 1y-pct=0
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-31 (z-distance 0.34).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_techm_ns (rho 0.88 via nifty_it, z -1.16, reacted); dyn_tatatech_ns (rho 0.505 via nifty_it, z -2.58, reacted); nifty_50 (rho 0.461 via nifty_it, z -1.23, reacted)
- **India receivers**: dyn_techm_ns (rho 0.88, z -1.16); dyn_tatatech_ns (rho 0.505, z -2.58); nifty_50 (rho 0.461, z -1.23)
- Source: TCS, HCL Tech, Tata Elxsi, Route Mobile to Tech Mahindra: IT stocks dip up to 3% | Here's why — Mint Markets, 2026-09-18. https://www.livemint.com/market/stock-market-news/tcs-hcl-tech-tata-elxsi-route-mobile-to-tech-mahindra-it-stocks-dip-up-to-3-heres-why-11789704607651.html
- Historical analogues: 2025-07-31 (d=0.34), 2025-01-30 (d=0.36), 2025-07-09 (d=0.4)

### [RED 4.58] dyn_tatatech_ns ↓
- dyn_tatatech_ns [EQUITIES]: last 730.40, z20 -2.58, zc -1.98, resid-z -1.70 [unexplained], 1d -3.74%, |z20|=2.58
- **Mechanism**: dyn_tatatech_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.505 via dyn_tatatech_ns, z -1.79, reacted); dyn_tataelxsi_ns (rho 0.437 via dyn_tatatech_ns, z -1.66, reacted); dyn_techm_ns (rho 0.388 via dyn_tatatech_ns, z -1.16, reacted)
- **India receivers**: nifty_it (rho 0.505, z -1.79); dyn_tataelxsi_ns (rho 0.437, z -1.66); dyn_techm_ns (rho 0.388, z -1.16)
- Source: Beyond Tata Sons listing boost, Tata Chemicals investors face earnings pressure — Mint Markets, 2026-09-18. https://www.livemint.com/market/mark-to-market/rbi-tata-sons-listing-tata-chemicals-shares-soda-ash-earnings-11789715166120.html
- Source: Sensex today | Stock Market Live: Sensex, Nifty gain as lower oil prices and global cues offset IT, Tata stocks drag — BusinessLine Mkts, 2026-09-18. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-18th-september-2026/article71477821.ece
- Source: Tata Group stocks shed $3.2 billion in market cap amid rift over Tata Sons listing — Mint Markets, 2026-09-18. https://www.livemint.com/market/stock-market-news/tata-group-stocks-shed-3-2-billion-in-market-cap-amid-tata-sons-rift-11789717385957.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

### [AMBER 4.35] dyn_jef ↓
- dyn_jef [EQUITIES]: last 47.87, z20 -2.35, zc 0.39, resid-z -0.65 [quiet], 1d 1.10%, |z20|=2.35
- **Mechanism**: dyn_jef ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Jefferies hikes Navin Fluorine share price target, forecasts 14% upside. 4 reasons why — ET Markets, 2026-09-18. https://economictimes.indiatimes.com/markets/stocks/news/jefferies-hikes-navin-fluorine-share-price-target-forecasts-14-upside-4-reasons-why/articleshow/134328838.cms
- Source: AI’s 3 musketeers are hitting the brakes. Why Jefferies’ Chris Wood sees India midcap stocks regaining favour — ET Markets, 2026-09-18. https://economictimes.indiatimes.com/markets/stocks/news/ais-3-musketeers-are-hitting-the-brakes-why-jefferies-chris-wood-sees-india-midcap-stocks-regaining-favour/articleshow/134326201.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-01 (d=0.04), 2025-08-19 (d=0.07)

## Watchlist (below surfacing floor)
commodities · 2 series ↑ (4.05), midcap_largecap_ratio ↑ (3.64), fx · 2 series ↓ (3.52), ig_oas ↓ (3.45), dyn_voltas_ns ↓ (3.39), dyn_tech ↑ (2.98), dyn_icicigi_bo ↓ (2.93), usd_cny ↓ (2.87), comex_copper ↑ (2.85), ust_2s10s ↓ (2.74), soybeans ↑ (2.73), dyn_hdb ↓ (2.58)

## India macro
- nifty_50: 23364.6992 (1d 0.40%, z20 -1.23, flag none)
- nifty_midcap_100: 61992.3984 (1d 0.91%, z20 -1.01, flag none)
- usd_inr: 95.8850 (1d -0.26%, z20 1.10, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6533 (1d 0.50%, z20 0.64, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 75.8 — "IndiGo shares rise 2% after India’s largest airline hikes excess baggage and priority serv"
- COALINDIA.NS (COAL INDIA LTD) score 75.7 — "IndiGo shares rise 2% after India’s largest airline hikes excess baggage and priority serv"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 73.3 — "IndiGo shares rise 2% after India’s largest airline hikes excess baggage and priority serv"
- INDIANB.NS (INDIAN BANK) score 65.7 — "Bank of Japan increases interest rates to a 31-year high of 1.25%"
- BAC (Bank of America Corporation) score 59.4 — "Bank of Japan increases interest rates to a 31-year high of 1.25%"
- COIN (Coinbase Global, Inc.) score 57.9 — "Global Market: South Korean shares jump nearly 2% as chip stocks rally"
- HDB (HDFC Bank Limited) score 50.8 — "Bank of Japan increases interest rates to a 31-year high of 1.25%"
- OHI (Omega Healthcare Investors, In) score 50.3 — "2026’s Best IPO: 325% gain in 7 sessions and now a third consecutive 5% lower circuit. Wha"
- IDBI.NS (IDBI BANK LIMITED) score 47.5 — "Bank of Japan increases interest rates to a 31-year high of 1.25%"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 47.5 — "Bank of Japan increases interest rates to a 31-year high of 1.25%"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 47.5 — "Bank of Japan increases interest rates to a 31-year high of 1.25%"
- BOND (PIMCO Active Bond Exchange-Tra) score 41.7 — "How Bessent, America's bond salesman, cornered Japan on big spending"
- CHKP (Check Point Software Technolog) score 41.0 — "NSE IPO Day 2: Issue subcribed 55% so far. GMP hints 8% listing pop. Check review, key dat"
- SEPN (Septerna, Inc.) score 31.5 — "Elevate Campuses IPO price band set at Rs 343–362; Rs 2,100 crore issue opens September 23"
- TECHM.NS (TECH MAHINDRA LIMITED) score 31.2 — "TCS, HCL Tech, Tata Elxsi, Route Mobile to Tech Mahindra: IT stocks dip up to 3% | Here's "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 31.2 — "TCS, HCL Tech, Tata Elxsi, Route Mobile to Tech Mahindra: IT stocks dip up to 3% | Here's "
- TECH (Bio-Techne Corp) score 31.2 — "TCS, HCL Tech, Tata Elxsi, Route Mobile to Tech Mahindra: IT stocks dip up to 3% | Here's "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 28.3 — "Tata Consumer Share Price Live Updates: Tata Consumer's Trading Insights"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 28.3 — "Tata Consumer Share Price Live Updates: Tata Consumer's Trading Insights"
- LTH (Life Time Group Holdings, Inc.) score 27.1 — "Bank of Maharashtra's first-ever overseas bond issuance of $500 mn gets 3 times subscripti"
- 301077.SZ (CHINASTARS) score 25.1 — "Global Market: China stocks rally 1% as Trump-Xi meeting raises trade hopes"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.9 — "Adani Energy Solutions among 4 stocks closing above VWAP"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 13.1 — "Final day to buy Hero Motors, SS Retail, Jindal Supreme: Which issue has highest IPO GMP? "
- BZ=F (Brent Crude Oil Last Day Finan) score 12.6 — "Dividend record date alert: Last chance to buy today - Maharashtra Scooters, Dixon, Concor"
- MS (Morgan Stanley) score 11.0 — "Global Market: J.P. Morgan sees BoE rates rising amid renewed inflation risks"
- JIOFIN.BO (Jio Financial Services Limited) score 10.9 — "Skyways Air Services share price surges 15% after Q1 results, dividend announcements | All"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.7 — "Up over 65% from IPO price in just 3 days! What is driving Glass Wall Systems share price?"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 8.7 — "Gold and silver prices volatile amid a decline in oil prices, stable dollar; experts highl"
- VT (Vanguard Total World Stock Ind) score 8.4 — "Park Medi World shares jump over 37% in 6 months; now launches this new program at Signatu"
- NVDA (NVIDIA Corporation) score 7.7 — "ALTMAN AND HUANG SET TO JOIN XI AT WHITE HOUSE DINNER OpenAI CEO Sam Altman and Nvidia CEO"
- PCJEWELLER.NS (PC JEWELLER LTD) score 7.4 — "Gold jewellery sector seeks MDR exemption on high-value UPI transactions"
- JEF (Jefferies Financial Group Inc.) score 7.2 — "AI’s 3 musketeers are hitting the brakes. Why Jefferies’ Chris Wood sees India midcap stoc"
- META (Meta) score 6.9 — "Metal stocks to buy: Tata Steel, JSW Steel among Motilal Oswal’s top picks, up to 17% upsi"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 5.2 — "PNB Housing Finance among 4 F&O stocks with a sharp rise in futures open interest"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 4.9 — "Adani Energy Solutions among 4 stocks closing above VWAP"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.1 — "HDFC Bank is winning the mutual fund vote over ICICI Bank. Can the shift last?"
- VOLTAS.NS (VOLTAS LTD) score 0.8 — "Voltas among 7 stocks hitting 52-week low; slipped up to 10% in a month"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 0.7 — "Stocks to watch, Sept 15: HDFC Bank, BSE, broking firms, HCL Tech, Deccan Gold Mines, CESC"
- DELL (Dell Technologies Inc.) score 0.4 — "Why Dell and HPE were the S&P 500’s top-performing stocks today"
- DKS (Dick's Sporting Goods Inc) score 0.0 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"

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