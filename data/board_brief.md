# Transmission Layer — board brief · 2026-10-29 01:06Z

data as of **2026-10-29** · 97 series · 8 red / 34 amber · 8 events surfaced (28 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.667, 19d in regime; vol-pct None, breadth-off 0.667, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.35, corr60 -0.39, contra nifty_50 corr20=0.44, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.83, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.07, corr60 0.13, last shift 2026-09-04. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.04, corr60 0.07, last shift 2026-09-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.77, last shift 2026-09-10. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.27, corr60 -0.01, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.05, corr60 -0.16, last shift 2026-08-07. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.51, corr60 0.28, last shift 2026-07-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 1.7079810942011164e-05)
- **SETUP** bovespa → usd_brl: leads 1d (ccf -0.679, β -0.4712, p 0.0); driver zc -1.87 → expected 1.277%. Type hit-rate 0.835 (n=1702).
- Track record · residual_reversion: hit-rate **0.502** (n=1121) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.835** (n=1702) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.529** (n=17) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.58] equities · 2 series ↑
- dyn_jef [EQUITIES]: last 47.51, z20 3.75, zc 1.32, resid-z 1.18 [quiet], 1d 2.85%, |z20|=3.75
- dyn_gs [EQUITIES]: last 926.19, z20 3.68, zc 0.85, resid-z 0.99 [quiet], 1d 1.58%, |z20|=3.68
- **Mechanism**: equities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.358 via dyn_jef, z -0.82, quiet)
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.833 vs dyn_gs, historically leads by 2d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.81 vs dyn_gs, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.665 vs dyn_gs, historically leads by 4d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.626 vs dyn_gs, historically leads by 2d
- Watch next: dyn_bac (co-move) — not yet - watch; rho 0.513 vs dyn_jef, historically leads by 1d
- **India receivers**: dyn_indusindbk_bo (rho 0.358, z -0.82)
- Source: GOLDMAN SACHS SEES LIMITED FED HIKES, POTENTIAL STOCK MARKET RALLY Goldman Sachs expects just one additional Fed rate hike, compared with three currently priced by markets, suggesting the current tightening cycle could be among the smallest since 1983. Strategist Vickie Chang highlighted historicall — DeItaone, 2026-10-28. https://t.me/walter_bloomberg/37659
- Source: Potential Multibagger? Vodafone Idea shares are up 25% in 1 year, Jefferies sees 143% surge in bull case - Check target — Mint Markets, 2026-10-28. https://www.livemint.com/market/potential-multibagger-vodafone-idea-shares-are-up-25-in-1-year-jefferies-sees-143-surge-in-bull-case-check-target-11793178437047.html
- Source: Maruti Suzuki shares see target price cuts by Jefferies, Nomura, other brokerages after Q2 net profit drops 26% YoY. What’s ahead? — ET Markets, 2026-10-28. https://economictimes.indiatimes.com/markets/stocks/news/maruti-suzuki-shares-see-target-price-cuts-by-jefferies-nomura-other-brokerages-after-q2-net-profit-drops-26-yoy-whats-ahead/articleshow/135254335.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-04-01 (d=0.55), 2025-05-16 (d=0.58)

### [AMBER 5.65] cross-asset · 4 series ↓
- tips_10y_real [RATES]: last 2.64, z20 -1.99, zc -0.39, resid-z -1.15 [quiet], 1d -0.75%, |z20|=1.99
- ust_30y [RATES]: last 5.30, z20 -1.85, zc -0.22, resid-z -0.36 [quiet], 1d -0.19%, |z20|=1.85
- ust_10y [RATES]: last 4.99, z20 -1.84, zc -0.19, resid-z -0.57 [quiet], 1d -0.20%, |z20|=1.84
- dyn_schd [EQUITIES]: last 35.08, z20 1.29, zc -0.15, resid-z -0.75 [quiet], 1d -0.13%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: taiwan_weighted (inverse) — not yet - watch; rho -0.559 vs dyn_schd, historically leads by 5d
- Watch next: dxy (inverse) — not yet - watch; rho -0.514 vs dyn_schd, historically leads by 4d
- Watch next: kospi (inverse) — not yet - watch; rho -0.568 vs dyn_schd
- Watch next: nikkei_225 (inverse) — not yet - watch; rho -0.554 vs dyn_schd
- Watch next: dyn_ohi (co-move) — not yet - watch; rho 0.502 vs dyn_schd
- Source: YIELD ON 10-YEAR TREASURY NOTE LAST UP 4.11 BASIS POINTS AT 5.034% — DeItaone, 2026-10-28. https://t.me/walter_bloomberg/37696
- Source: Info Edge Q2 Results: Net profit plunges 93% YoY to Rs 334 crore, revenue rises 13%; co declares Rs 3/share interim dividend — ET Markets, 2026-10-28. https://economictimes.indiatimes.com/markets/stocks/earnings/info-edge-naukri-net-profit-plunges-93-yoy-to-rs-334-crore-revenue-rises-13-co-declares-rs-3/share-interim-dividend/articleshow/135261958.cms
- Source: Naukri brand parent Info Edge shares dip after  ₹3 per share dividend move | Check payment, record date, history, yield — Mint Markets, 2026-10-28. https://www.livemint.com/market/stock-market-news/naukri-brand-parent-info-edge-shares-dip-after-rs-3-per-share-dividend-move-check-payment-record-date-history-yield-11793178605612.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-12 (d=0.66), 2025-05-19 (d=1.13)

### [RED 4.91] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1650.00, z20 2.91, zc -0.44, resid-z -0.61 [quiet], 1d -1.43%, |z20|=2.91; 1y-pct=97
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.416 via dyn_atherenerg_ns, z -1.11, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.416, z -1.11)
- Source: Ather Energy shares: 125% YTD returns! Experts give 'portfolio stock' tag after Q2 results 2026 | Target, stop-loss — Mint Markets, 2026-10-27. https://www.livemint.com/market/stock-market-news/ather-energy-shares-125-ytd-returns-experts-give-portfolio-stock-tag-after-q2-results-2026-target-stoploss-11793080902497.html
- Source: Ather achieves profitability milestone, supply ramp-up to pave the road ahead — Mint Markets, 2026-10-27. https://www.livemint.com/market/mark-to-market/ather-energy-q2-results-net-profit-revenue-growth-11793081766549.html
- Source: Ather Energy shares jump 5%, extend rally to 20% in two days after Q2 results. Can the run continue? — ET Markets, 2026-10-27. https://economictimes.indiatimes.com/markets/stocks/news/ather-energy-shares-jump-5-extend-rally-to-20-in-two-days-after-q2-results-can-the-run-continue/articleshow/135225009.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [AMBER 4.75] commodities · 2 series ↓
- wheat [COMMODITIES]: last 601.00, z20 -1.92, zc -0.03, resid-z -0.65 [quiet], 1d -0.04%, |z20|=1.92
- soybeans [COMMODITIES]: last 1234.75, z20 -1.55, zc -0.02, resid-z 0.36 [quiet], 1d -0.02%, |z20|=1.55
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Corn drops on US harvest pressure, wheat near 3-1/2-month low — BusinessLine Mkts, 2026-10-27. https://www.thehindubusinessline.com/markets/commodities/corn-drops-on-us-harvest-pressure-wheat-near-3-12-month-low/article71629668.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-16 (d=0.1), 2025-10-02 (d=0.31)

### [RED 4.72] dyn_sepn ↑
- dyn_sepn [EQUITIES]: last 44.23, z20 2.72, zc 0.05, resid-z 1.23 [quiet], 1d 0.20%, |z20|=2.72; 1y-pct=98
- **Mechanism**: dyn_sepn ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: US OCT CONSUMER CONFIDENCE INDEX 91.7 (CONSENSUS 81.0) VS SEPT REVISED 84.2 (PREVIOUS 81.9) - CONFERENCE BOARD — DeItaone, 2026-10-27. https://t.me/walter_bloomberg/37609
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-13 (d=0.0), 2025-05-01 (d=0.01)

### [RED 4.61] dyn_rs ↑
- dyn_rs [EQUITIES]: last 437.02, z20 2.61, zc 0.61, resid-z 1.53 [unexplained], 1d 0.98%, |z20|=2.61; 1y-pct=100
- **Mechanism**: dyn_rs ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Top 5 IPOs listing: Jio Platforms IPO vs Hyundai, Paytm, LIC and others | How Reliance company outshone others in gains — Mint Markets, 2026-10-28. https://www.livemint.com/market/stock-market-news/top-5-ipos-listing-jio-platforms-ipo-vs-hyundai-paytm-lic-and-others-how-reliance-company-outshone-others-in-gains-11793186868452.html
- Source: Sensex today | Stock Market Highlights: Sensex declines 353 points dragged by Reliance, IT stocks, rising crude oil prices — BusinessLine Mkts, 2026-10-28. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-28-october-2026/article71631075.ece
- Source: Jio IPO surge helps Reliance topple Tata as most valuable conglomerate in India — Mint Markets, 2026-10-28. https://www.livemint.com/market/stock-market-news/reliance-vs-tata-group-market-cap-jio-platforms-share-price-11793181248458.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-30 (d=0.02), 2026-03-31 (d=0.02)

### [AMBER 4.47] dyn_coalindia_ns ↓
- dyn_coalindia_ns [EQUITIES]: last 392.00, z20 -2.47, zc -1.10, resid-z -1.05 [quiet], 1d -1.51%, |z20|=2.47
- **Mechanism**: dyn_coalindia_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Market wrap: Bharti Airtel, Tata Consumer, Asian Paints, Coal India top gainers and losers on Nifty and Sensex on Tuesday — ET Markets, 2026-10-27. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-bharti-airtel-tata-consumer-asian-paints-coal-india-top-gainers-and-losers-on-nifty-and-sensex-on-tuesday/articleshow/135234189.cms
- Source: Top dividend stocks to buy: PTC India, CESC, Vedanta, Coal India, HPCL offer up to 24% yield. Check full list here — Mint Markets, 2026-10-27. https://www.livemint.com/market/stock-market-news/top-dividend-stocks-to-buy-ptc-india-cesc-vedanta-coal-india-hpcl-offer-up-to-24-yield-check-full-list-here-11793085342244.html
- Source: Coal India Share Price Live Updates: Coal India  Faces Slight Price Drop — ET Markets, 2026-10-27. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/coal-india-ltd-share-price-live-updates-27-oct-2026/liveblog/135224568.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.03), 2025-07-04 (d=0.04)

### [AMBER 4.44] cross-asset · 2 series ↑
- comex_silver [COMMODITIES]: last 53.53, z20 -1.61, zc -0.02, resid-z -0.27 [quiet], 1d -0.04%, |z20|=1.61
- gold_silver_ratio [DERIVED]: last 75.65, z20 1.60, zc n/a, resid-z n/a [quiet], 1d 0.07%, |z20|=1.60
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.507 vs gold_silver_ratio, historically leads by 5d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.568 vs comex_silver
- Source: US Fed rate decision today: What investors should watch in gold, silver prices and market outlook — Mint Markets, 2026-10-28. https://www.livemint.com/market/stock-market-news/us-fed-rate-decision-today-what-investors-should-watch-in-gold-silver-prices-and-market-outlook-11793183747846.html
- Source: Silver futures decline to ₹1.95 lakh/kg — BusinessLine Mkts, 2026-10-28. https://www.thehindubusinessline.com/markets/gold/silver-futures-decline-to-195-lakhkg/article71635034.ece
- Source: Gold, silver prices crash up to 53% from January peak. Time to buy before Dhanteras, festive season? — ET Markets, 2026-10-28. https://economictimes.indiatimes.com/markets/commodities/news/gold-silver-prices-crash-up-to-53-from-january-peak-time-to-buy-before-dhanteras-festive-season/articleshow/135253262.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-29 (d=0.06), 2025-08-12 (d=0.14)

## Watchlist (below surfacing floor)
dyn_meta ↓ (4.4), dyn_cartrade_ns ↓ (4.36), dyn_tatatech_ns ↓ (4.12), dyn_tech ↑ (4.1), dyn_jiofin_bo ↓ (3.96), sofr ↑ (3.87), dyn_hdb ↓ (3.69), dyn_policybzr_ns ↓ (3.31), dyn_4417_t ↑ (3.28), bovespa ↓ (2.62), aud_usd ↑ (2.28), usd_brl ↑ (2.23)

## India macro
- nifty_50: 22698.8496 (1d -0.22%, z20 0.10, flag none)
- nifty_midcap_100: 57268.4492 (1d 0.42%, z20 -1.11, flag none)
- usd_inr: 95.2100 (1d 0.03%, z20 -0.45, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5230 (1d 0.64%, z20 -1.10, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 95.8 — "Stock recommendations for 29 October from MarketSmith India"
- COALINDIA.NS (COAL INDIA LTD) score 95.6 — "Stock recommendations for 29 October from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 93.5 — "Stock recommendations for 29 October from MarketSmith India"
- INDIANB.NS (INDIAN BANK) score 64.6 — "INVESTORS PULL $18.5 BILLION FROM US STOCKS IN TWO WEEKS Bank of America clients sold a ne"
- BAC (Bank of America Corporation) score 58.6 — "INVESTORS PULL $18.5 BILLION FROM US STOCKS IN TWO WEEKS Bank of America clients sold a ne"
- TGT (Target Corporation) score 55.3 — "BESSENT: FED IS VERY ATTENTIVE TO BEING ABOVE INFLATION TARGET FOR A LONG TIME"
- COIN (Coinbase Global, Inc.) score 52.2 — "Sebi to review FPI rules, align with global norms"
- HDB (HDFC Bank Limited) score 50.0 — "INVESTORS PULL $18.5 BILLION FROM US STOCKS IN TWO WEEKS Bank of America clients sold a ne"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 49.5 — "INVESTORS PULL $18.5 BILLION FROM US STOCKS IN TWO WEEKS Bank of America clients sold a ne"
- IDBI.NS (IDBI BANK LIMITED) score 49.3 — "INVESTORS PULL $18.5 BILLION FROM US STOCKS IN TWO WEEKS Bank of America clients sold a ne"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 49.3 — "INVESTORS PULL $18.5 BILLION FROM US STOCKS IN TWO WEEKS Bank of America clients sold a ne"
- OHI (Omega Healthcare Investors, In) score 47.9 — "INVESTORS PULL $18.5 BILLION FROM US STOCKS IN TWO WEEKS Bank of America clients sold a ne"
- TECHM.NS (TECH MAHINDRA LIMITED) score 42.0 — "Broker’s Call: Lumax Auto Tech (Buy)"
- CHKP (Check Point Software Technolog) score 39.9 — "Top 2 stocks to buy for short-term: Zydus Life, Whirlpool by Nagaraj Shetti - Check stop l"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 37.8 — "Broker’s Call: Lumax Auto Tech (Buy)"
- TECH (Bio-Techne Corp) score 37.8 — "Broker’s Call: Lumax Auto Tech (Buy)"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 34.9 — "BESSENT: THINK WE ARE GETTING ENERGY SUPPLY SHOCK, THINK FED SHOULD HAVE AN OPEN MIND"
- LTH (Life Time Group Holdings, Inc.) score 27.0 — "BESSENT: FED IS VERY ATTENTIVE TO BEING ABOVE INFLATION TARGET FOR A LONG TIME"
- RS (Reliance, Inc.) score 25.0 — "Sensex today | Stock Market Highlights: Sensex declines 353 points dragged by Reliance, IT"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 24.1 — "How can US Fed FOMC meeting outcome impact Indian stock market? Sensex, Nifty to rise? Exp"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 23.8 — "Tata Consumer Share Price Live Updates: Tata Consumer's Price Movement Today"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 23.8 — "Tata Consumer Share Price Live Updates: Tata Consumer's Price Movement Today"
- BOND (PIMCO Active Bond Exchange-Tra) score 23.6 — "GUNDLACH RECOMMENDS 30% EQUITIES, 30% BONDS, 20% COMMODITIES, 20% DRY POWDER"
- 301077.SZ (CHINASTARS) score 21.8 — "WRIGHT SAYS CHINA LIKELY TO RESUME DIESEL EXPORTS"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 19.9 — "Expert view: Expect mid-teens earnings growth for Nifty companies in FY27 and FY28, says B"
- JIOFIN.BO (Jio Financial Services Limited) score 17.3 — "ALPHABET ($GOOGL) Q3 2026 EARNINGS Revenue: $127.58B vs. $127.93B est. — MISS EPS: $2.12 v"
- JUSTDIAL.BO (JUST DIAL LTD.) score 16.0 — "GOLDMAN SACHS SEES LIMITED FED HIKES, POTENTIAL STOCK MARKET RALLY Goldman Sachs expects j"
- BZ=F (Brent Crude Oil Last Day Finan) score 14.2 — "YIELD ON 10-YEAR TREASURY NOTE LAST UP 4.11 BASIS POINTS AT 5.034%"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 13.2 — "Q2 Results Highlights Oct 28: Adani Ports, Bandhan Bank, TVS Motor, HUL, JSW Energy, PVR I"
- JEF (Jefferies Financial Group Inc.) score 12.1 — "Potential Multibagger? Vodafone Idea shares are up 25% in 1 year, Jefferies sees 143% surg"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 12.1 — "Shriram Finance shares falls 5% as analysts cut targets after Q2 results"
- SEPN (Septerna, Inc.) score 11.2 — "Today’s Gold Rate, September 23: Check gold rates in Delhi, Mumbai, Chennai"
- SCHD (Schwab US Dividend Equity ETF) score 10.1 — "Info Edge Q2 Results: Net profit plunges 93% YoY to Rs 334 crore, revenue rises 13%; co de"
- META (Meta) score 9.9 — "AMD $META - AMD AND META ADVANCE STRATEGIC PARTNERSHIP TO POWER META’S SUPERINTELLIGENCE I"
- VT (Vanguard Total World Stock Ind) score 8.5 — "Bahri Profit Hits $1.36 Billion as the World Scrambles for Tankers"
- INFY (Infosys Limited) score 7.5 — "Infosys, TechM, TCS, other IT stocks plunge up to 5%, extend losses as global AI trade reb"
- GS (Goldman Sachs Group, Inc. (The) score 7.2 — "GOLDMAN SACHS SEES LIMITED FED HIKES, POTENTIAL STOCK MARKET RALLY Goldman Sachs expects j"
- SWIGGY.NS (SWIGGY LIMITED) score 2.9 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.9 — "MDR uncertainty, choppy markets cloud ₹33,600-crore fintech IPO pipeline"
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