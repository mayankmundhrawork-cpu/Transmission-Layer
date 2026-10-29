# Transmission Layer — board brief · 2026-10-29 18:27Z

data as of **2026-10-29** · 97 series · 10 red / 32 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.69, 19d in regime; vol-pct 0.674, breadth-off 0.706, Markov P(high-vol) 0.018)
- [INVERTED] **safe_haven_gold** — corr20 -0.35, corr60 -0.36, contra nifty_50 corr20=0.43, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.83, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.15, corr60 0.12, last shift 2026-09-04. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.05, corr60 0.07, last shift 2026-09-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.89, corr60 -0.76, last shift 2026-09-10. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.26, corr60 -0.01, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.05, corr60 -0.16, last shift 2026-08-07. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.49, corr60 0.29, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 0.0001506472847574436)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.502** (n=1124) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.835** (n=1702) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.529** (n=17) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.97] equities · 2 series ↑
- dyn_jef [EQUITIES]: last 48.62, z20 4.14, zc 1.01, resid-z 1.18 [quiet], 1d 2.34%, |z20|=4.14
- dyn_gs [EQUITIES]: last 926.22, z20 2.83, zc 0.06, resid-z 0.99 [quiet], 1d 0.11%, |z20|=2.83
- **Mechanism**: equities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.385 via dyn_jef, z 0.08, quiet)
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.823 vs dyn_gs, historically leads by 2d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.793 vs dyn_gs, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.662 vs dyn_gs, historically leads by 4d
- Watch next: dyn_bac (co-move) — not yet - watch; rho 0.525 vs dyn_jef, historically leads by 1d
- Watch next: dxy (inverse) — not yet - watch; rho -0.508 vs dyn_gs, historically leads by 2d
- **India receivers**: dyn_indusindbk_bo (rho 0.385, z 0.08)
- Source: HUL shares rise 3% after Q2 results. Jefferies, Nomura cut target price but forecast 29% upside potential — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/stocks/news/hul-shares-rise-3-after-q2-results-jefferies-nomura-cut-target-price-but-forecast-29-upside-potential/articleshow/135295044.cms
- Source: Jefferies initiates coverage on NSE with ‘Buy’; here’s why it sees fresh growth potential — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/stocks/news/jefferies-initiates-coverage-on-nse-with-buy-heres-why-it-sees-fresh-growth-potential/articleshow/135293157.cms
- Source: Potential LTCG tax cut could revive FIIs’ India bet, says Jefferies: Which stocks may benefit most? — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/stocks/news/potential-ltcg-tax-cut-could-revive-fiis-india-bet-says-jefferies-which-stocks-may-benefit-most/articleshow/135290083.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-04-01 (d=0.55), 2025-05-16 (d=0.58)

### [RED 5.83] dyn_cartrade_ns ↓
- dyn_cartrade_ns [EQUITIES]: last 2319.90, z20 -3.83, zc -1.33, resid-z -2.00 [unexplained], 1d -5.87%, |z20|=3.83
- **Mechanism**: dyn_cartrade_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: CarTrade Tech shares tank over 6% after Q2 results, but Nomura raises target price to Rs 3,377. Here’s why — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/stocks/news/cartrade-tech-shares-tank-over-6-after-q2-results-but-nomura-raises-target-price-to-rs-3377-heres-why/articleshow/135290221.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-13 (d=0.0), 2025-07-18 (d=0.01)

### [AMBER 5.65] cross-asset · 4 series ↓
- tips_10y_real [RATES]: last 2.64, z20 -1.99, zc -0.39, resid-z -1.15 [quiet], 1d -0.75%, |z20|=1.99
- ust_30y [RATES]: last 5.30, z20 -1.85, zc -0.22, resid-z -0.36 [quiet], 1d -0.19%, |z20|=1.85
- ust_10y [RATES]: last 4.99, z20 -1.84, zc -0.19, resid-z -0.57 [quiet], 1d -0.20%, |z20|=1.84
- dyn_schd [EQUITIES]: last 35.44, z20 1.54, zc 1.25, resid-z -0.75 [quiet], 1d 1.00%, 1y-pct=100
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dxy (inverse) — not yet - watch; rho -0.518 vs dyn_schd, historically leads by 4d
- Watch next: dyn_tgt (co-move) — not yet - watch; rho 0.584 vs dyn_schd
- Watch next: kospi (inverse) — not yet - watch; rho -0.558 vs dyn_schd
- Watch next: nikkei_225 (inverse) — not yet - watch; rho -0.518 vs dyn_schd
- Source: Q2 October dividend champions: Infosys, Colgate, HUL, CPCL, Coal India | Big payouts - amount, record date — Mint Markets, 2026-10-29. https://www.livemint.com/market/stock-market-news/october-dividend-champions-infosys-colgate-hul-chennai-petro-coal-india-announce-big-payouts-check-amount-record-11793286004751.html
- Source: Looking for income? These dividend stocks have high yields that seem well supported. — MarketWatch Top, 2026-10-29. https://www.marketwatch.com/story/looking-for-income-these-dividend-stocks-have-high-yields-that-seem-well-supported-81093bdf?mod=mw_rss_topstories
- Source: Coal India dividend 2026 declared - Check amount; PSU quarterly profit up 57% - When is record date? — Mint Markets, 2026-10-29. https://www.livemint.com/market/stock-market-news/coal-india-dividend-2026-declared-check-amount-psu-quarterly-profit-up-57-when-is-record-date-11793283032165.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-12 (d=0.66), 2025-05-19 (d=1.13)

### [AMBER 5.6] brent ↑
- brent [COMMODITIES]: last 110.64, z20 0.60, zc -1.90, resid-z -2.95 [unexplained], 1d -4.06%, 1-session move -4.06% ≥ 1.5%
- **Mechanism**: brent ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.429 via brent, z -0.5, quiet)
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.531 vs brent
- Watch next: sp500 (inverse) — not yet - watch; rho -0.529 vs brent
- Watch next: vix (co-move) — not yet - watch; rho 0.526 vs brent
- **India receivers**: nifty_midcap_100 (rho -0.429, z -0.5)
- Source: Mexico’s Richest Man Sells $1.15 Billion in Oil Stocks — OilPrice, 2026-10-29. https://oilprice.com/Latest-Energy-News/World-News/Mexicos-Richest-Man-Sells-115-Billion-in-Oil-Stocks.html
- Source: Europe to Release 42 Million Barrels of Oil — OilPrice, 2026-10-29. https://oilprice.com/Latest-Energy-News/World-News/Europe-to-Release-42-Million-Barrels-of-Oil.html
- Source: Sinopec Third-Quarter Profit Jumps 64% as Oil Prices Climb — OilPrice, 2026-10-29. https://oilprice.com/Latest-Energy-News/World-News/Sinopec-Third-Quarter-Profit-Jumps-64-as-Oil-Prices-Climb.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-14 (d=0.02), 2025-04-16 (d=0.04)

### [RED 5.52] cross-asset · 3 series ↓
- gold_silver_ratio [DERIVED]: last 77.13, z20 2.20, zc n/a, resid-z n/a [quiet], 1d 1.76%, |z20|=2.20
- comex_silver [COMMODITIES]: last 52.12, z20 -2.15, zc -1.10, resid-z -0.87 [quiet], 1d -2.50%, |z20|=2.15; co-occur[gold_silver] same-direction (channel VALID)
- comex_gold [COMMODITIES]: last 4019.90, z20 -2.02, zc -0.67, resid-z 1.08 [quiet], 1d -0.78%, |z20|=2.02; 1y-pct=5; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.568 vs comex_silver, historically leads by 5d
- Watch next: comex_copper (inverse) — not yet - watch; rho -0.545 vs gold_silver_ratio
- Source: Karwa Chauth today but gold, silver rates not glittering — will prices rebound or pain will continue till Diwali? — Mint Markets, 2026-10-29. https://www.livemint.com/market/commodities/karwa-chauth-today-but-gold-silver-rates-not-glittering-will-prices-rebound-or-pain-will-continue-till-diwali-11793271194604.html
- Source: Today’s Gold Rate in India October 29: Gold prices up in Coimbatore, Nagpur, Visakhapatnam, Surat, Jaipur — BusinessLine Mkts, 2026-10-29. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-coimbatore-nagpur-visakhapatnam-surat-jaipur-lucknow-chandigarh-gold-rates-other-cities-october-29-2026/article71639624.ece
- Source: Today’s Gold Rate in India October 29: Gold prices up in Delhi, Mumbai, Kolkata, Chennai, Bengaluru — BusinessLine Mkts, 2026-10-29. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-delhi-mumbai-kolkata-chennai-bengaluru-hyderabad-pune-gold-rates-metro-cities-october-29-2026/article71639623.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 4.73] dyn_lth ↑
- dyn_lth [EQUITIES]: last 44.44, z20 2.73, zc 1.29, resid-z 0.17 [quiet], 1d 3.01%, |z20|=2.73
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Suzlon Energy Q2 Results: Profit plunges 69% YoY to Rs 394 crore due to one-time deferred tax — ET Markets, 2026-10-29. https://economictimes.indiatimes.com/markets/stocks/earnings/suzlon-energy-q2-results-profit-plunges-69-yoy-to-rs-394-crore-revenue-rises-26/articleshow/135304125.cms
- Source: Diwali 2026: MCX Muhurat Trading - Date is 8 Nov 2026; check time for special, trading, client mode modification session — Mint Markets, 2026-10-29. https://www.livemint.com/market/stock-market-news/diwali-2026-mcx-muhurat-trading-date-is-8-nov-2026-check-time-for-special-trading-client-mode-modification-session-11793258582748.html
- Source: Sanofi Consumer share price jumps 11% after strong Q3 results | Is it time to book profits? Check target, rationale — Mint Markets, 2026-10-29. https://www.livemint.com/market/stock-market-news/sanofi-consumer-share-price-jumps-11-after-strong-q3-results-is-it-time-to-book-profits-check-target-rationale-11793249979630.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-17 (d=0.02), 2025-12-31 (d=0.02)

### [AMBER 4.36] dyn_rs ↑
- dyn_rs [EQUITIES]: last 437.82, z20 2.36, zc 0.09, resid-z 1.53 [unexplained], 1d 0.15%, |z20|=2.36; 1y-pct=100
- **Mechanism**: dyn_rs ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Jio Platforms first Q2 results after bumper listing: check date; Reliance firm’s earnings in focus; key numbers to watch — Mint Markets, 2026-10-29. https://www.livemint.com/market/stock-market-news/jio-platforms-first-q2-results-after-bumper-listing-check-date-reliance-firm-s-earnings-in-focus-key-numbers-to-watch-11793290112398.html
- Source: Reliance Power shares on fire! Anil Ambani’s stock jumps 9.22%, but remains down 59% in a year - should you buy? — Mint Markets, 2026-10-29. https://www.livemint.com/market/stock-market-news/reliance-power-shares-on-fire-anil-ambani-s-stock-jumps-9-22-but-remains-down-59-in-a-year-should-you-buy-11793273904768.html
- Source: Reliance Jio Platforms shares vs Bharti Airtel vs Vodafone Idea: Top telecom stock to buy? What experts suggest — Mint Markets, 2026-10-29. https://www.livemint.com/market/stock-market-news/reliance-jio-platforms-shares-vs-bharti-airtel-vs-vodafone-idea-top-telecom-stock-to-buy-what-experts-suggest-11793262195751.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-30 (d=0.02), 2026-03-31 (d=0.02)

### [RED 4.15] indices · 2 series ↑
- dax [INDICES]: last 26052.73, z20 3.32, zc 1.53, resid-z 2.13 [unexplained], 1d 1.36%, |z20|=3.32
- cac_40 [INDICES]: last 7975.82, z20 2.29, zc 1.42, resid-z 1.82 [unexplained], 1d 1.13%, |z20|=2.29
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.555 via dax, z 1.29, reacted); nifty_fmcg (rho 0.523 via cac_40, z -0.28, quiet); nifty_midcap_100 (rho 0.509 via dax, z -0.5, quiet); dyn_tataelxsi_ns (rho 0.436 via cac_40, z 1.1, reacted)
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.904 vs dax
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.583 vs dax, historically leads by 5d
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.506 vs dax, historically leads by 2d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.503 vs dax, historically leads by 5d
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.5 vs dax, historically leads by 5d
- **India receivers**: nifty_50 (rho 0.555, z 1.29); nifty_fmcg (rho 0.523, z -0.28); nifty_midcap_100 (rho 0.509, z -0.5); dyn_tataelxsi_ns (rho 0.436, z 1.1)
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-26 (d=0.23), 2025-08-11 (d=0.25)

## Watchlist (below surfacing floor)
dyn_tech ↑ (3.75), shanghai_comp ↓ (3.55), usd_cny ↓ (3.38), dyn_jiofin_bo ↓ (3.38), dyn_4417_t ↑ (3.33), eur_usd ↓ (3.22), dyn_hdb ↓ (3.19), dyn_techm_ns ↑ (2.95), usd_brl ↑ (2.91), dyn_atherenerg_ns ↑ (2.5), dyn_sepn ↑ (2.49), bovespa ↓ (2.45)

## India macro
- nifty_50: 22936.7500 (1d 1.05%, z20 1.29, flag none)
- nifty_midcap_100: 57836.8008 (1d 0.99%, z20 -0.50, flag none)
- usd_inr: 95.2100 (1d 0.03%, z20 -0.45, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5216 (1d -0.06%, z20 -1.02, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 104.0 — "MSCI Rejig: LIC, Meesho likely to enter India Standard Index; OFSS, Siemens Energy may be "
- COALINDIA.NS (COAL INDIA LTD) score 103.8 — "MSCI Rejig: LIC, Meesho likely to enter India Standard Index; OFSS, Siemens Energy may be "
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 102.0 — "MSCI Rejig: LIC, Meesho likely to enter India Standard Index; OFSS, Siemens Energy may be "
- INDIANB.NS (INDIAN BANK) score 76.9 — "ECB PRESIDENT LAGARDE TO STEP DOWN EARLY IN FEBRUARY 2027 European Central Bank President "
- BAC (Bank of America Corporation) score 66.1 — "ECB PRESIDENT LAGARDE TO STEP DOWN EARLY IN FEBRUARY 2027 European Central Bank President "
- TGT (Target Corporation) score 59.0 — "Top 3 stocks to buy tomorrow: Kotak Mahindra Bank, Nykaa, Eternal by market expert; check "
- HDB (HDFC Bank Limited) score 58.8 — "ECB PRESIDENT LAGARDE TO STEP DOWN EARLY IN FEBRUARY 2027 European Central Bank President "
- OHI (Omega Healthcare Investors, In) score 58.7 — "Jio Q2 Preview: First results after listing. What should investors expect?"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 58.4 — "ECB PRESIDENT LAGARDE TO STEP DOWN EARLY IN FEBRUARY 2027 European Central Bank President "
- IDBI.NS (IDBI BANK LIMITED) score 58.2 — "ECB PRESIDENT LAGARDE TO STEP DOWN EARLY IN FEBRUARY 2027 European Central Bank President "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 58.2 — "ECB PRESIDENT LAGARDE TO STEP DOWN EARLY IN FEBRUARY 2027 European Central Bank President "
- COIN (Coinbase Global, Inc.) score 53.4 — "Global Market: Japan's Nikkei rises on Advantest forecast; Samsung slump caps gains"
- TECHM.NS (TECH MAHINDRA LIMITED) score 48.0 — "TCS, Infosys, HCL Tech: Anthropic revenue soars 14-fold in H1 2026 - Can Indian IT stocks "
- CHKP (Check Point Software Technolog) score 45.2 — "Top 3 stocks to buy tomorrow: Kotak Mahindra Bank, Nykaa, Eternal by market expert; check "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 41.5 — "TCS, Infosys, HCL Tech: Anthropic revenue soars 14-fold in H1 2026 - Can Indian IT stocks "
- TECH (Bio-Techne Corp) score 41.5 — "TCS, Infosys, HCL Tech: Anthropic revenue soars 14-fold in H1 2026 - Can Indian IT stocks "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 35.4 — "Tata Power, JSW Energy, Torrent Power: Ambit sees buying opportunity in power stocks after"
- BOND (PIMCO Active Bond Exchange-Tra) score 27.7 — "ECB PRESIDENT LAGARDE TO STEP DOWN EARLY IN FEBRUARY 2027 European Central Bank President "
- LTH (Life Time Group Holdings, Inc.) score 27.7 — "Suzlon Energy Q2 Results: Profit plunges 69% YoY to Rs 394 crore due to one-time deferred "
- RS (Reliance, Inc.) score 25.9 — "Reliance Power shares on fire! Anil Ambani’s stock jumps 9.22%, but remains down 59% in a "
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 25.1 — "Paras Healthcare shares: After IPO listing gains, check what's happening with stock - Buy,"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 23.0 — "Tata Power, JSW Energy, Torrent Power: Ambit sees buying opportunity in power stocks after"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 23.0 — "Tata Power, JSW Energy, Torrent Power: Ambit sees buying opportunity in power stocks after"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 22.6 — "ESAF Small Finance Bank posts Rs 160 crore Q2 profit as asset quality improves"
- 301077.SZ (CHINASTARS) score 21.2 — "Global Market: China’s yuan hits four-year high against dollar after Fed holds rates"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 17.8 — "Sensex today | Stock Market Highlights: Sensex settles 905 pts higher, Nifty ends above 22"
- JIOFIN.BO (Jio Financial Services Limited) score 16.6 — "Piero Cipollone: Next-day securities settlement, tokenisation and the transformation of Eu"
- SCHD (Schwab US Dividend Equity ETF) score 14.4 — "Godrej Consumer Q2 Results: Profit rises 14% YoY to Rs 523 crore, revenue jumps 19%; co de"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 14.1 — "ESAF Small Finance Bank posts Rs 160 crore Q2 profit as asset quality improves"
- JEF (Jefferies Financial Group Inc.) score 14.0 — "Top stock to buy today: Jefferies India sees 29% upside in NSE share price in upside scena"
- JUSTDIAL.BO (JUST DIAL LTD.) score 13.5 — "GOLDMAN SACHS SEES LIMITED FED HIKES, POTENTIAL STOCK MARKET RALLY Goldman Sachs expects j"
- SEPN (Septerna, Inc.) score 12.4 — "US inflation heats up in September; consumer spending rises"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.0 — "YIELD ON 10-YEAR TREASURY NOTE LAST UP 4.11 BASIS POINTS AT 5.034%"
- META (Meta) score 8.4 — "AMD $META - AMD AND META ADVANCE STRATEGIC PARTNERSHIP TO POWER META’S SUPERINTELLIGENCE I"
- INFY (Infosys Limited) score 8.3 — "TCS, Infosys, HCL Tech: Anthropic revenue soars 14-fold in H1 2026 - Can Indian IT stocks "
- VT (Vanguard Total World Stock Ind) score 7.2 — "Bahri Profit Hits $1.36 Billion as the World Scrambles for Tankers"
- GS (Goldman Sachs Group, Inc. (The) score 6.1 — "GOLDMAN SACHS SEES LIMITED FED HIKES, POTENTIAL STOCK MARKET RALLY Goldman Sachs expects j"
- SWIGGY.NS (SWIGGY LIMITED) score 2.5 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.7 — "MDR uncertainty, choppy markets cloud ₹33,600-crore fintech IPO pipeline"
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