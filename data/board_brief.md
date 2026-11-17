# Transmission Layer — board brief · 2026-11-17 13:15Z

data as of **2026-11-17** · 97 series · 11 red / 32 amber · 8 events surfaced (23 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.652, 2d in regime; vol-pct 0.888, breadth-off 0.417, Markov P(high-vol) 0.034)
- [INVERTED] **safe_haven_gold** — corr20 -0.08, corr60 -0.21, contra nifty_50 corr20=0.32, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.88, corr60 0.84, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.15, corr60 0.1, last shift 2026-09-17. Channel: global copper leads Indian metal equities
- [INVERTED] **inr_oil_channel** — corr20 -0.32, corr60 0.03, last shift 2026-09-01. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.91, last shift 2026-09-23. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.26, corr60 0.0, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.05, corr60 -0.17, last shift 2026-08-11. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.36, corr60 0.32, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 0.0006738585313537104)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.51** (n=1158) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.819** (n=2044) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.62] rates · 4 series ↑
- tips_10y_real [RATES]: last 2.91, z20 2.95, zc 0.88, resid-z 0.62 [quiet], 1d 1.75%, 1d move +5.0bps ≥ 5bps; |z20|=2.95; 1y-pct=97
- ust_2y [RATES]: last 4.88, z20 2.05, zc 0.30, resid-z -0.11 [quiet], 1d 0.41%, |z20|=2.05; 1y-pct=98
- ust_30y [RATES]: last 5.47, z20 1.88, zc 0.83, resid-z 0.51 [quiet], 1d 0.74%, |z20|=1.88
- ust_10y [RATES]: last 5.15, z20 1.66, zc 0.88, resid-z 0.55 [quiet], 1d 0.98%, |z20|=1.66
- **Mechanism**: rates · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_tgt (inverse) — not yet - watch; rho -0.581 vs ust_30y
- Watch next: dyn_schd (inverse) — not yet - watch; rho -0.521 vs tips_10y_real
- Source: Rupee likely to open flat as dollar strength, US bond yields weigh on sentiment — BusinessLine Mkts, 2026-11-16. https://www.thehindubusinessline.com/markets/forex/rupee-likely-to-open-flat-as-dollar-strength-us-bond-yields-weigh-on-sentiment/article71706648.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.26), 2026-05-14 (d=0.57)

### [RED 7.35] usd_inr ↓
- usd_inr [FX]: last 93.46, z20 -2.35, zc -1.90, resid-z -1.54 [unexplained], 1d -0.83%, 20d range extreme; |z20|=2.35
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_havells_ns (rho -0.479 via usd_inr, z 1.55, reacted); dyn_indianb_ns (rho -0.433 via usd_inr, z 1.56, reacted); nifty_it (rho -0.387 via usd_inr, z -1.48, reacted); dyn_bajfinance_ns (rho -0.383 via usd_inr, z 1.69, reacted); dyn_jiofin_bo (rho -0.358 via usd_inr, z 1.21, reacted)
- **India receivers**: dyn_havells_ns (rho -0.479, z 1.55); dyn_indianb_ns (rho -0.433, z 1.56); nifty_it (rho -0.387, z -1.48); dyn_bajfinance_ns (rho -0.383, z 1.69)
- Source: Rupee rises 43 paise to close at 93.51 (provisional) against US dollar — BusinessLine Mkts, 2026-11-17. https://www.thehindubusinessline.com/markets/forex/rupee-rises-43-paise-to-close-at-9351-provisional-against-us-dollar/article71711397.ece
- Source: Robust inflows, pullback in shorts lift rupee to seven-month peak — ET Markets, 2026-11-17. https://economictimes.indiatimes.com/markets/forex/forex-news/robust-inflows-pullback-in-shorts-lift-rupee-to-seven-month-peak/articleshow/135921416.cms
- Source: Rupee rises 31 paise to 93.63 against US dollar in early trade — BusinessLine Mkts, 2026-11-17. https://www.thehindubusinessline.com/markets/forex/rupee-rises-31-paise-to-9363-against-us-dollar-in-early-trade/article71710364.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [AMBER 6.53] cross-asset · 7 series ↓
- dyn_nvda [EQUITIES]: last 156.16, z20 -2.20, zc -0.49, resid-z -0.50 [quiet], 1d -4.11%, |z20|=2.20; 1y-pct=0
- btc_usd [CRYPTO]: last 64999.52, z20 -2.15, zc 0.07, resid-z -1.19 [quiet], 1d 0.22%, |z20|=2.15
- eth_usd [CRYPTO]: last 1821.00, z20 -2.00, zc 0.02, resid-z -0.81 [quiet], 1d 0.09%, |z20|=2.00
- dyn_coin [EQUITIES]: last 119.83, z20 -1.98, zc -0.49, resid-z -0.11 [quiet], 1d -6.13%, 1y-pct=0
- sp500 [INDICES]: last 7420.19, z20 -1.78, zc -0.30, resid-z -0.25 [quiet], 1d -1.87%, |z20|=1.78
- russell_2000 [INDICES]: last 2743.39, z20 -1.55, zc -0.21, resid-z 0.30 [quiet], 1d -1.69%, |z20|=1.55
- nasdaq_100 [INDICES]: last 27204.77, z20 -1.55, zc -0.57, resid-z -1.47 [quiet], 1d -2.64%, |z20|=1.55
- **Mechanism**: cross-asset · 7 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.27).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho -0.425 via dyn_nvda, z 1.69, reacted)
- Watch next: dyn_rs (co-move) — not yet - watch; rho 0.606 vs russell_2000, historically leads by 4d
- Watch next: dyn_bac (co-move) — not yet - watch; rho 0.543 vs russell_2000, historically leads by 2d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.519 vs dyn_nvda
- **India receivers**: dyn_bajfinance_ns (rho -0.425, z 1.69)
- Source: UK Pushes for Global Levies on Polluting Industries — OilPrice, 2026-11-17. https://oilprice.com/Latest-Energy-News/World-News/UK-Pushes-for-Global-Levies-on-Polluting-Industries.html
- Source: South Korean shares close at over 9-month low on Nvidia caution — ET Markets, 2026-11-17. https://economictimes.indiatimes.com/markets/us-stocks/news/south-korean-shares-close-at-over-9-month-low-on-nvidia-caution/articleshow/135914599.cms
- Source: Oil Prices Slide as Global Glut Fears Eclipse Hormuz Attacks — OilPrice, 2026-11-17. https://oilprice.com/Latest-Energy-News/World-News/Oil-Prices-Slide-as-Global-Glut-Fears-Eclipse-Hormuz-Attacks.html
- Historical analogues: 2026-05-22 (d=0.27), 2025-10-21 (d=0.7), 2026-04-02 (d=1.07)

### [RED 5.9] fx · 2 series ↓
- eur_usd [FX]: last 1.10, z20 -3.07, zc -0.77, resid-z -0.68 [quiet], 1d -0.29%, |z20|=3.07; 1y-pct=0
- gbp_usd [FX]: last 1.32, z20 -2.51, zc -0.49, resid-z -0.38 [quiet], 1d -0.19%, |z20|=2.51; 1y-pct=2
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Boris Vujčić: Risks and resilience in the euro area financial system — ECB press, 2026-11-16. https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp261116~db374b56ab.en.html
- Source: Yen steady against euro and dollar after soft Japanese GDP data — Mint Markets, 2026-11-16. https://www.livemint.com/market/yen-steady-against-euro-and-dollar-after-soft-japanese-gdp-data-11794791270301.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [RED 5.61] dyn_kaynes_ns ↓
- dyn_kaynes_ns [EQUITIES]: last 2858.00, z20 -3.61, zc -1.50, resid-z -1.72 [unexplained], 1d -4.09%, |z20|=3.61; 1y-pct=0
- **Mechanism**: dyn_kaynes_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-01-23 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.368 via dyn_kaynes_ns, z 1.58, reacted); nifty_metal (rho 0.359 via dyn_kaynes_ns, z 0.84, quiet); dyn_tatatech_ns (rho 0.358 via dyn_kaynes_ns, z -0.55, quiet); dyn_jiofin_bo (rho 0.35 via dyn_kaynes_ns, z 1.21, reacted)
- **India receivers**: nifty_fmcg (rho 0.368, z 1.58); nifty_metal (rho 0.359, z 0.84); dyn_tatatech_ns (rho 0.358, z -0.55); dyn_jiofin_bo (rho 0.35, z 1.21)
- Source: Kaynes Technology stock in pain as Street falls out of love — Mint Markets, 2026-11-17. https://www.livemint.com/market/mark-to-market/kaynes-technology-stock-q2-results-smart-meter-sales-crash-11794899402071.html
- Source: Kaynes Technology shares extend losses, fall another 4%; should investors worry about its Q2 performance? — Mint Markets, 2026-11-17. https://www.livemint.com/market/stock-market-news/kaynes-technology-shares-extend-losses-fall-another-4-should-investors-worry-about-its-q2-performance-11794900682488.html
- Source: Amber Enterprises shares resume losing run, tank over 8% after weak Q2 from peer Kaynes Technology. Is more fall ahead? — Mint Markets, 2026-11-16. https://www.livemint.com/market/stock-market-news/amber-enterprises-shares-resume-losing-run-tank-over-8-after-weak-q2-from-peer-kaynes-technology-is-more-fall-ahead-11794813833370.html
- Historical analogues: 2026-01-23 (d=0.0), 2025-01-23 (d=0.01), 2026-01-06 (d=0.02)

### [RED 5.47] dyn_blln ↓
- dyn_blln [EQUITIES]: last 96.10, z20 -3.47, zc -1.53, resid-z -0.57 [moved], 1d -8.61%, |z20|=3.47
- **Mechanism**: dyn_blln ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Australia sells A$6 billion of new 2057 Treasury bond — ET Markets, 2026-11-17. https://economictimes.indiatimes.com/markets/bonds/australia-sells-a6-billion-of-new-2057-treasury-bond/articleshow/135910893.cms
- Source: Why Iraq Just Fast-Tracked Chevron’s Takeover Of A 14-Billion-Barrel Supergiant — OilPrice, 2026-11-17. https://oilprice.com/Energy/Energy-General/Why-Iraq-Just-Fast-Tracked-Chevrons-Takeover-Of-A-14-Billion-Barrel-Supergiant.html
- Source: NVDA - JENSEN HUANG TRANSFERRED OVER $10 BILLION IN NVIDIA STOCK TO FAMILY TRUST BEFORE DOWNFALL Former Nvidia CEO Jensen Huang and his wife transferred nearly 60 million shares, worth over $10.5 billion, into an irrevocable family trust in March, according to SEC filings reviewed by Barron's. The t — DeItaone, 2026-11-16. https://t.me/walter_bloomberg/38619

### [RED 5.33] dxy ↑
- dxy [FX]: last 103.57, z20 2.33, zc 0.06, resid-z 0.14 [quiet], 1d 0.02%, 20d range extreme; |z20|=2.33; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-10 (d=0.03), 2025-05-14 (d=0.06)

### [AMBER 5.29] indices · 3 series ↓
- kospi [INDICES]: last 4965.31, z20 -1.97, zc -0.78, resid-z -0.18 [quiet], 1d -2.65%, |z20|=1.97
- taiwan_weighted [INDICES]: last 40146.34, z20 -1.90, zc -0.90, resid-z 0.78 [quiet], 1d -2.18%, |z20|=1.90
- nikkei_225 [INDICES]: last 58965.48, z20 -1.59, zc -0.56, resid-z 0.36 [quiet], 1d -1.17%, |z20|=1.59
- **Mechanism**: indices · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.545 via kospi, z -1.35, reacted); nifty_50 (rho -0.514 via taiwan_weighted, z 1.56, reacted); nifty_it (rho -0.451 via kospi, z -1.48, reacted); nifty_midcap_100 (rho 0.45 via nikkei_225, z 1.43, reacted); dyn_idbi_ns (rho 0.437 via nikkei_225, z -0.23, quiet)
- **India receivers**: midcap_largecap_ratio (rho 0.545, z -1.35); nifty_50 (rho -0.514, z 1.56); nifty_it (rho -0.451, z -1.48); nifty_midcap_100 (rho 0.45, z 1.43)
- Source: Stock market outlook today,17 Nov:Sensex, Nifty prediction-DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-17. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-17-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-cue-11794875550779.html
- Source: Stock market outlook today,16 Nov: Sensex, Nifty prediction-DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-16. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-16-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-11794789061627.html
- Source: JAPAN'S NIKKEI AVERAGE FUTURES UP 0.75% IN EARLY TRADE — DeItaone, 2026-11-15. https://t.me/walter_bloomberg/38547

## Watchlist (below surfacing floor)
cross-asset · 3 series ↓ (5.11), cross-asset · 3 series ↑ (5.03), comex_copper ↓ (4.22), dyn_tech ↑ (3.24), eur_inr ↓ (3.19), dyn_atherenerg_ns ↑ (3.14), dyn_4417_t ↑ (2.87), dyn_schd ↑ (2.82), dyn_lth ↑ (2.71), aud_usd ↓ (2.6), shanghai_comp ↓ (2.35), dyn_karurvysya_ns ↑ (2.14)

## India macro
- nifty_50: 25387.4004 (1d 0.38%, z20 1.56, flag amber)
- nifty_midcap_100: 61728.4492 (1d 0.25%, z20 1.43, flag none)
- usd_inr: 93.4600 (1d -0.83%, z20 -2.35, flag red)
- goi_10y: 7.3800 (1d 4.53%, z20 3.03, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.1400 (1d -5.73%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4315 (1d -0.13%, z20 -1.35, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 82.7 — "Traders pour cash into BlackRock’s India ETF as AI rout deepens"
- INOXINDIA.NS (INOX INDIA LIMITED) score 79.9 — "Traders pour cash into BlackRock’s India ETF as AI rout deepens"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 78.1 — "Traders pour cash into BlackRock’s India ETF as AI rout deepens"
- NVDA (NVIDIA Corporation) score 58.3 — "Nvidia Earnings Preview: 6 key factors investors will watch"
- INDIANB.NS (INDIAN BANK) score 53.9 — "IndusInd Bank Share Price Highlights: IndusInd Bank Stock Price History"
- BAC (Bank of America Corporation) score 48.6 — "IndusInd Bank Share Price Highlights: IndusInd Bank Stock Price History"
- TECHM.NS (TECH MAHINDRA LIMITED) score 45.6 — "Nifty holds green as crude slide cushions Wall Street tech shock"
- HDB (HDFC Bank Limited) score 43.2 — "IndusInd Bank Share Price Highlights: IndusInd Bank Stock Price History"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 43.1 — "Nifty holds green as crude slide cushions Wall Street tech shock"
- TECH (Bio-Techne Corp) score 43.1 — "Nifty holds green as crude slide cushions Wall Street tech shock"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 39.5 — "IndusInd Bank Share Price Highlights: IndusInd Bank Stock Price History"
- IDBI.NS (IDBI BANK LIMITED) score 39.5 — "IndusInd Bank Share Price Highlights: IndusInd Bank Stock Price History"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 39.5 — "IndusInd Bank Share Price Highlights: IndusInd Bank Stock Price History"
- TGT (Target Corporation) score 34.5 — "U.S. INTELLIGENCE WARNS IRAN MAY BE PLANNING DIRTY BOMB OR CHEMICAL ATTACK IN WASHINGTON U"
- OHI (Omega Healthcare Investors, In) score 28.5 — "Nvidia Earnings Preview: 6 key factors investors will watch"
- COIN (Coinbase Global, Inc.) score 25.5 — "India ETFs among global winners in October as AI-hardware sell-off hits Taiwan, Korea"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.6 — "Making a comeback! Down 60% in 1 year, strong rally seen ahead for renewable energy stock "
- CHKP (Check Point Software Technolog) score 21.4 — "HDFC Bank vs Axis Bank: Both shares recover after Q2 sell-off; which banking stock offers "
- 301077.SZ (CHINASTARS) score 20.6 — "China charges veteran nuclear expert Gu Jun with taking ‘huge’ bribes"
- LTH (Life Time Group Holdings, Inc.) score 18.9 — "FMCG stocks recover from six-month correction; Anand Rathi picks 4 stocks for up to 57% gr"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 17.5 — "Tata Chemicals share price jumps 9%: Volume surge, Tata Sons listing buzz behind the Tata "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 17.5 — "Tata Chemicals share price jumps 9%: Volume surge, Tata Sons listing buzz behind the Tata "
- BOND (PIMCO Active Bond Exchange-Tra) score 15.8 — "Indian bonds gain as oil slide eases rate hike concerns"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 14.5 — "Why Silver rates crashed from record high of  ₹4 lakh per kg price to below  ₹1.75 lakh? E"
- BLLN (BillionToOne, Inc.) score 14.0 — "Australia sells A$6 billion of new 2057 Treasury bond"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 13.5 — "After IDBI Bank stake buy, now Fairfax set to sell 13.25% stake in IIFL Finance via  ₹3,45"
- JIOFIN.BO (Jio Financial Services Limited) score 12.4 — "Jio Financial Services Share Price Highlights: Jio Financial Services Stock Price History"
- BZ=F (Brent Crude Oil Last Day Finan) score 10.2 — "NVIDIA SHARES EXTEND LOSSES; LAST DOWN 4.2%"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.7 — "Why Iraq Just Fast-Tracked Chevron’s Takeover Of A 14-Billion-Barrel Supergiant"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 8.3 — "After IDBI Bank stake buy, now Fairfax set to sell 13.25% stake in IIFL Finance via  ₹3,45"
- SCHD (Schwab US Dividend Equity ETF) score 7.6 — "Mahanadi Coalfields IPO: Dividend king in the making? What top official says about Coal In"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.1 — "Stock Market Live Updates | Opening Bell: Sensex gains over 200 pts, Nifty above 25,300; I"
- MS (Morgan Stanley) score 6.9 — "JPM $BAC $WFC $USB $COF - MULTIPLE U.S. BANKS FACE SERVICE DISRUPTION REPORTS Several majo"
- GS (Goldman Sachs Group, Inc. (The) score 5.0 — "GOLDMAN SACHS CUTS OIL PRICE FORECASTS FOR 2026 AND 2027 Goldman Sachs has lowered its Bre"
- META (Meta) score 4.8 — "Metal stock jumps 17%, inches close to 52-week high after this CAPEX update; will the rall"
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 4.4 — "Kaynes Technology shares extend losses, fall another 4%; should investors worry about its "
- CRWV (CoreWeave, Inc.) score 3.0 — "COREWEAVE SHARES FOLLOW NVIDIA LOWER, DOWN 6%"
- ETERNAL.NS (ETERNAL LIMITED) score 2.7 — "Eternal among 5 stocks hitting 52-week highs; stock rallies up to 15% in a month"
- RS (Reliance, Inc.) score 2.5 — "Reliance Industries shares rebound 15% in November, add  ₹2.38 lakh crore in market value;"
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 1.2 — "Cochin Shipyard dividend 2026: Last day to buy today | Check record date, payout amount, h"

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