# Transmission Layer — board brief · 2026-11-04 00:35Z

data as of **2026-11-04** · 97 series · 5 red / 35 amber · 8 events surfaced (24 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.667, 4d in regime; vol-pct None, breadth-off 0.667, Markov P(high-vol) 0.085)
- [INVERTED] **safe_haven_gold** — corr20 -0.48, corr60 -0.46, contra nifty_50 corr20=0.25, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.89, corr60 0.84, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.17, corr60 0.12, last shift 2026-09-10. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.04, corr60 0.07, last shift 2026-09-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.74, last shift 2026-09-16. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.31, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.13, corr60 -0.11, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.56, corr60 0.37, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **6 of 89** scanned series survive multiplicity control (effective p ≤ 0.005605629265529988)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.504** (n=1122) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.827** (n=1680) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.529** (n=17) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.78] indices · 2 series ↑
- nifty_50 [INDICES]: last 23810.85, z20 3.95, zc 1.91, resid-z 2.21 [unexplained], 1d 1.58%, |z20|=3.95
- nifty_fmcg [INDICES]: last 45580.05, z20 1.95, zc 3.29, resid-z 3.06 [unexplained], 1d 3.65%, |z20|=1.95
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-18 (z-distance 0.29).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.701 via nifty_50, z 0.37, quiet); dyn_jiofin_bo (rho 0.632 via nifty_50, z 0.41, quiet); dyn_bajfinance_ns (rho 0.623 via nifty_50, z 0.99, quiet); dyn_indusindbk_bo (rho 0.56 via nifty_50, z -0.04, quiet); nifty_metal (rho 0.545 via nifty_50, z 0.61, quiet)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.701 vs nifty_50, historically leads by 3d
- Watch next: dyn_jiofin_bo (co-move) — not yet - watch; rho 0.632 vs nifty_50, historically leads by 3d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.703 vs nifty_50
- Watch next: dyn_bajfinance_ns (co-move) — not yet - watch; rho 0.623 vs nifty_50
- Watch next: dyn_indusindbk_bo (co-move) — not yet - watch; rho 0.56 vs nifty_50
- **India receivers**: nifty_midcap_100 (rho 0.701, z 0.37); dyn_jiofin_bo (rho 0.632, z 0.41); dyn_bajfinance_ns (rho 0.623, z 0.99); dyn_indusindbk_bo (rho 0.56, z -0.04)
- Source: US Midterm Election Results 2026 date today! What Trump's loss mean for gold, Sensex, Nifty, global markets, US bonds? — Mint Markets, 2026-11-03. https://www.livemint.com/market/stock-market-news/us-midterm-election-results-2026-date-today-what-trumps-loss-mean-for-gold-sensex-nifty-global-markets-us-bonds-11793715305962.html
- Source: Market wrap:  BSE, Nestle India, Power Grid, SBI top gainers and losers on Nifty and Sensex on Tuesday — ET Markets, 2026-11-03. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-bse-nestle-india-power-grid-sbi-top-gainers-and-losers-on-nifty-and-sensex-on-tuesday/articleshow/135495602.cms
- Source: Nifty crosses 23,800 for first time since August on falling crude prices, earnings boost — BusinessLine Mkts, 2026-11-03. https://www.thehindubusinessline.com/markets/nifty-crosses-23800-for-first-time-since-august-on-falling-crude-prices-earnings-boost/article71660642.ece
- Historical analogues: 2025-07-18 (d=0.29), 2025-08-01 (d=0.88), 2025-07-11 (d=1.11)

### [AMBER 5.33] cross-asset · 3 series ↓
- ust_2y [RATES]: last 4.59, z20 -2.01, zc -0.84, resid-z -0.81 [quiet], 1d 0.66%, |z20|=2.01
- ust_10y [RATES]: last 4.91, z20 -1.83, zc -0.75, resid-z -1.16 [quiet], 1d -0.61%, |z20|=1.83
- dyn_schd [EQUITIES]: last 35.54, z20 1.13, zc -1.17, resid-z -0.68 [quiet], 1d -1.00%, 1y-pct=98
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.735 vs ust_2y
- Watch next: dxy (inverse) — not yet - watch; rho -0.525 vs dyn_schd, historically leads by 4d
- Watch next: dyn_tgt (co-move) — not yet - watch; rho 0.599 vs dyn_schd
- Watch next: kospi (inverse) — not yet - watch; rho -0.539 vs dyn_schd
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.004 vs ust_2y, historically leads by 1d
- Source: Dividend investing in 2026: 5 stocks to know — Mint Markets, 2026-11-04. https://www.livemint.com/market/stock-market-news/dividend-investing-in-2026-5-stocks-to-know-11793705770748.html
- Source: US Treasury yields climb as strong jobs data, midterm polls weigh; 10-year yield eyes 5% again — ET Markets, 2026-11-03. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-treasury-yields-climb-as-strong-jobs-data-and-midterm-uncertainty-weigh-on-bonds/articleshow/135511549.cms
- Source: U.S. TREASURY YIELDS RISE SLIGHTLY AFTER ECONOMIC DATA; YIELD ON 10-YEAR TREASURY NOTE LAST UP 5.36 BASIS POINTS AT 4.948% TWO-YEAR U.S. TREASURY YIELDS LAST UP 3.13 BASIS POINTS AT 4.614% — DeItaone, 2026-11-03. https://t.me/walter_bloomberg/37973
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-12 (d=0.46), 2025-05-19 (d=1.07)

### [AMBER 5.29] indices · 3 series ↓
- sp500 [INDICES]: last 7568.58, z20 -1.98, zc 0.37, resid-z -2.23 [unexplained], 1d 0.36%, |z20|=1.98
- vix [INDICES]: last 20.81, z20 1.94, zc -0.17, resid-z n/a [quiet], 1d -1.61%, |z20|=1.94
- nasdaq_100 [INDICES]: last 28180.26, z20 -1.85, zc 0.38, resid-z -0.35 [quiet], 1d 0.68%, |z20|=1.85
- **Mechanism**: indices · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-20 (z-distance 0.14).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.732 vs sp500, historically leads by 2d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.825 vs sp500
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.704 vs sp500
- Source: S&P 500 is looking over the edge of a technical cliff — what happens if it falls off? — MarketWatch Top, 2026-11-03. https://www.marketwatch.com/story/s-p-500-is-looking-over-the-edge-of-a-technical-cliff-what-happens-if-it-falls-off-be97ebd9?mod=mw_rss_topstories
- Source: US stocks today: Nasdaq rebounds as chipmakers rally, Apple slides ahead of US midterm results — ET Markets, 2026-11-03. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-nasdaq-rebounds-as-chipmakers-rally-apple-slides-ahead-of-us-midterm-results/articleshow/135513181.cms
- Source: U.S. STOCK INDEXES EXTEND GAINS; S&P 500 UP 0.70%, NASDAQ UP 1.2% — DeItaone, 2026-11-03. https://t.me/walter_bloomberg/37987
- Historical analogues: 2026-05-20 (d=0.14), 2025-08-18 (d=0.18), 2025-10-23 (d=0.18)

### [RED 5.13] cross-asset · 3 series ↓
- gold_silver_ratio [DERIVED]: last 79.30, z20 1.81, zc n/a, resid-z n/a [quiet], 1d 0.05%, |z20|=1.81
- comex_silver [COMMODITIES]: last 49.72, z20 -1.75, zc -0.02, resid-z -0.61 [quiet], 1d -0.06%, |z20|=1.75; 1y-pct=1; co-occur[gold_silver] same-direction (channel VALID)
- comex_gold [COMMODITIES]: last 3942.70, z20 -1.71, zc -0.01, resid-z -2.77 [unexplained], 1d -0.02%, |z20|=1.71; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.529 vs comex_gold
- Source: ROI-As markets sway, safe havens shine. Except gold: McGeever — Mint Markets, 2026-11-03. https://www.livemint.com/market/roias-markets-sway-safe-havens-shine-except-gold-mcgeever-11793748689717.html
- Source: US Midterm Election Results 2026 date today! What Trump's loss mean for gold, Sensex, Nifty, global markets, US bonds? — Mint Markets, 2026-11-03. https://www.livemint.com/market/stock-market-news/us-midterm-election-results-2026-date-today-what-trumps-loss-mean-for-gold-sensex-nifty-global-markets-us-bonds-11793715305962.html
- Source: Indian gold demand down 30% in September quarter as high prices hurt jewellery sales — BusinessLine Mkts, 2026-11-03. https://www.thehindubusinessline.com/markets/gold/gold-demand-down-30-in-september-quarter-as-high-prices-hurt-jewellery-sales/article71660046.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [AMBER 4.75] cross-asset · 2 series ↓
- dyn_coin [EQUITIES]: last 145.56, z20 -1.92, zc 1.20, resid-z -1.49 [quiet], 1d 5.61%, 1y-pct=2
- btc_usd [CRYPTO]: last 76807.04, z20 -1.82, zc -0.45, resid-z 0.25 [quiet], 1d -0.93%, |z20|=1.82
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.06).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Global Diesel Crunch Set to Last Well Into 2027 — OilPrice, 2026-11-04. https://oilprice.com/Energy/Crude-Oil/Global-Diesel-Crunch-Set-to-Last-Well-Into-2027.html
- Source: IEA Warns Global Gas Crunch Could Last Well into 2027 — OilPrice, 2026-11-03. https://oilprice.com/Latest-Energy-News/World-News/IEA-Warns-Global-Gas-Crunch-Could-Last-Well-into-2027.html
- Source: US Midterm Election Results 2026 date today! What Trump's loss mean for gold, Sensex, Nifty, global markets, US bonds? — Mint Markets, 2026-11-03. https://www.livemint.com/market/stock-market-news/us-midterm-election-results-2026-date-today-what-trumps-loss-mean-for-gold-sensex-nifty-global-markets-us-bonds-11793715305962.html
- Historical analogues: 2026-05-22 (d=0.06), 2026-04-02 (d=0.26), 2025-08-19 (d=0.33)

### [RED 4.73] dyn_policybzr_ns ↓
- dyn_policybzr_ns [EQUITIES]: last 928.00, z20 -2.73, zc -0.12, resid-z -1.14 [quiet], 1d -0.32%, |z20|=2.73; 1y-pct=0
- **Mechanism**: dyn_policybzr_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho 0.577 via dyn_policybzr_ns, z 0.99, quiet); nifty_midcap_100 (rho 0.525 via dyn_policybzr_ns, z 0.37, quiet); nifty_50 (rho 0.491 via dyn_policybzr_ns, z 3.95, reacted); dyn_indusindbk_bo (rho 0.449 via dyn_policybzr_ns, z -0.04, quiet); nifty_metal (rho 0.371 via dyn_policybzr_ns, z 0.61, quiet)
- Watch next: dyn_bajfinance_ns (co-move) — not yet - watch; rho 0.577 vs dyn_policybzr_ns, historically leads by 5d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.725 vs dyn_policybzr_ns
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.525 vs dyn_policybzr_ns
- **India receivers**: dyn_bajfinance_ns (rho 0.577, z 0.99); nifty_midcap_100 (rho 0.525, z 0.37); nifty_50 (rho 0.491, z 3.95); dyn_indusindbk_bo (rho 0.449, z -0.04)
- Source: Broker’s call: PB Fintech (Buy) — BusinessLine Mkts, 2026-11-02. https://www.thehindubusinessline.com/markets/brokers-call-pb-fintech-buy/article71656563.ece
- Source: MobiKwik shares zoom 10% as fintech firm posts record Rs 12 crore profit in Q2 — ET Markets, 2026-11-02. https://economictimes.indiatimes.com/markets/stocks/news/mobikwik-shares-zoom-10-as-fintech-firm-posts-record-rs-12-crore-profit-in-q2/articleshow/135452378.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-16 (d=0.02), 2025-01-30 (d=0.03)

### [AMBER 4.37] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1795.00, z20 2.37, zc 0.35, resid-z -0.35 [quiet], 1d 1.15%, |z20|=2.37; 1y-pct=100
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.372 via dyn_atherenerg_ns, z 0.37, quiet)
- **India receivers**: nifty_midcap_100 (rho 0.372, z 0.37)
- Source: Best EV stock to buy: Ather Energy vs Ola Electric Mobility; which is better profit-making deal? Investors guide, target — Mint Markets, 2026-11-02. https://www.livemint.com/market/stock-market-news/best-ev-stock-to-buy-ather-energy-vs-ola-electric-mobility-which-is-better-profit-making-deal-investors-guide-target-11793608999266.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [AMBER 4.28] dyn_jef ↑
- dyn_jef [EQUITIES]: last 48.59, z20 2.28, zc 0.19, resid-z -3.25 [unexplained], 1d 0.66%, |z20|=2.28
- **Mechanism**: dyn_jef ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.47 via dyn_jef, z -0.04, quiet)
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.625 vs dyn_jef, historically leads by 5d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.726 vs dyn_jef
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.571 vs dyn_jef
- **India receivers**: dyn_indusindbk_bo (rho 0.47, z -0.04)
- Source: ITC shares rise 2% after Q2 results. What are Jefferies, Nuvama and others saying? — ET Markets, 2026-11-03. https://economictimes.indiatimes.com/markets/stocks/news/itc-shares-rise-2-after-q2-results-what-are-jefferies-nuvama-and-others-saying/articleshow/135481293.cms
- Source: Delhivery shares soar 6% after Q2 results; JPMorgan, Jefferies, Kotak, Citi maintain buy calls — BusinessLine Mkts, 2026-11-02. https://www.thehindubusinessline.com/markets/delhivery-shares-jump-95-after-q2-results-jpmorgan-jefferies-kotak-citi-maintain-buy-calls/article71655384.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-01 (d=0.04), 2025-08-19 (d=0.07)

## Watchlist (below surfacing floor)
dyn_ohi ↑ (4.16), dyn_rs ↑ (3.81), comex_copper ↓ (3.79), shanghai_comp ↓ (3.77), corn ↓ (3.55), dyn_4417_t ↑ (3.53), dyn_sepn ↑ (3.33), rates · 2 series ↑ (3.25), dyn_tech ↑ (3.06), indices · 2 series ↑ (2.91), taiwan_weighted ↓ (2.89), dyn_techm_ns ↑ (2.82)

## India macro
- nifty_50: 23810.8496 (1d 1.58%, z20 3.95, flag red)
- nifty_midcap_100: 58598.0508 (1d 1.06%, z20 0.37, flag none)
- usd_inr: 94.7254 (1d -0.19%, z20 -0.89, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4610 (1d -0.51%, z20 -1.68, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · AMFI SIP / MF flows T-5d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 90.8 — "India bonds end tad higher on softer oil"
- INOXINDIA.NS (INOX INDIA LIMITED) score 90.8 — "India bonds end tad higher on softer oil"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 89.5 — "India bonds end tad higher on softer oil"
- INDIANB.NS (INDIAN BANK) score 62.3 — "ECB: DECEMBER RATE HIKE NOW SEEN AS HIGHLY LIKELY Bundesbank President Joachim Nagel says "
- OHI (Omega Healthcare Investors, In) score 46.3 — "Wall Street's hidden bargains: 10 US largecap stocks trading at historic discount for inve"
- BAC (Bank of America Corporation) score 44.7 — "ECB: DECEMBER RATE HIKE NOW SEEN AS HIGHLY LIKELY Bundesbank President Joachim Nagel says "
- TECHM.NS (TECH MAHINDRA LIMITED) score 41.6 — "Anthropic’s IPO is a high-stakes referendum on Big Tech — and this chart proves it"
- HDB (HDFC Bank Limited) score 41.5 — "ECB: DECEMBER RATE HIKE NOW SEEN AS HIGHLY LIKELY Bundesbank President Joachim Nagel says "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.7 — "Anthropic’s IPO is a high-stakes referendum on Big Tech — and this chart proves it"
- TECH (Bio-Techne Corp) score 39.7 — "Anthropic’s IPO is a high-stakes referendum on Big Tech — and this chart proves it"
- TGT (Target Corporation) score 39.6 — "Marico share price: FMCG stock gains 8% on strong Q2 results, nears 52-week high - Buy or "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 39.3 — "ECB: DECEMBER RATE HIKE NOW SEEN AS HIGHLY LIKELY Bundesbank President Joachim Nagel says "
- IDBI.NS (IDBI BANK LIMITED) score 39.3 — "ECB: DECEMBER RATE HIKE NOW SEEN AS HIGHLY LIKELY Bundesbank President Joachim Nagel says "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 39.3 — "ECB: DECEMBER RATE HIKE NOW SEEN AS HIGHLY LIKELY Bundesbank President Joachim Nagel says "
- COIN (Coinbase Global, Inc.) score 33.7 — "Global Diesel Crunch Set to Last Well Into 2027"
- CHKP (Check Point Software Technolog) score 29.1 — "Nifty Expiry Today Prediction 3 Nov: Bulls back in action! Check support, resistance level"
- RS (Reliance, Inc.) score 27.9 — "Reliance shares see volume breakout: Is a trend reversal around the corner? Here’s what RI"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 26.6 — "ECB'S NAGEL: A RATE HIKE IN DECEMBER IS VERY LIKELY TO BE NECESSARY ECB'S NAGEL: INFLATION"
- 301077.SZ (CHINASTARS) score 26.6 — "US OFFICIALS HAVE HELD UP APPROVAL FOR AMERICAN CHIPMAKING EQUIPMENT NEEDED BY SK HYNIX TO"
- BOND (PIMCO Active Bond Exchange-Tra) score 25.2 — "India bonds end tad higher on softer oil"
- LTH (Life Time Group Holdings, Inc.) score 23.7 — "ANTHROPIC ENGINEERS FOUND CLAUDE CUTS TIME TAKEN TO DESIGN CHIPS COMPARED TO THEIR ESTIMAT"
- BZ=F (Brent Crude Oil Last Day Finan) score 15.6 — "U.S. TREASURY YIELDS RISE SLIGHTLY AFTER ECONOMIC DATA; YIELD ON 10-YEAR TREASURY NOTE LAS"
- JIOFIN.BO (Jio Financial Services Limited) score 15.2 — "AI BOOM: $10 TRILLION SPENDING WAVE RAISES FINANCIAL RISKS Former New York Fed President B"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 14.7 — "Q2 Results Today Live: SBI Q2 profit up 14%; Bajaj Finserv, Pfizer, Solar Ind Q2 earnings "
- SCHD (Schwab US Dividend Equity ETF) score 13.7 — "YEMEN WARNS: SAUDI ARAMCO FACILITIES AT RISK A Yemeni military source warned that Aramco f"
- SEPN (Septerna, Inc.) score 13.4 — "US FACTORY ORDERS SURGE 1.8%, BEATING EXPECTATIONS US factory orders rose 1.8% in Septembe"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 13.0 — "HDFC Bank share price gains 3% today: Here's why - Is the worst over after a 27% one-year "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.1 — "Market wrap:  RIL, Tata Steel, Infosys, ICICI Bank top gainers and losers on Nifty and Sen"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 11.1 — "Market wrap:  RIL, Tata Steel, Infosys, ICICI Bank top gainers and losers on Nifty and Sen"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 10.2 — "Utkarsh Small Finance Bank reports sixth consecutive quarterly loss"
- META (Meta) score 9.2 — "Q2 Results Today Live: SBI Q2 profit up 14%; Bajaj Finserv, Pfizer, Solar Ind Q2 earnings "
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.2 — "LTCG abolition may cost just Rs 40,000–50,000 crore, SBI estimates show"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.0 — "Diwali stock picks: Titan, Eternal, BSE to Adani Ports — 10 long-term bets by Motilal Oswa"
- VT (Vanguard Total World Stock Ind) score 7.8 — "ADNOC Chief Says World Has “Eroded Its Supply Buffers”"
- JEF (Jefferies Financial Group Inc.) score 7.5 — "ITC shares rise 2% after Q2 results. What are Jefferies, Nuvama and others saying?"
- GS (Goldman Sachs Group, Inc. (The) score 6.5 — "DEMOCRATIC SWEEP AT 73%. WALL STREET BRACES FOR MIDTERMS. Prediction markets price a 73% c"
- INFY (Infosys Limited) score 4.7 — "Market wrap:  RIL, Tata Steel, Infosys, ICICI Bank top gainers and losers on Nifty and Sen"
- AAPL (Apple Inc.) score 3.0 — "US stock futures mixed as Apple falls on margin warning, midterm results awaited"
- POLICYBZR.NS (PB FINTECH LIMITED) score 1.7 — "Broker’s call: PB Fintech (Buy)"
- SWIGGY.NS (SWIGGY LIMITED) score 0.7 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"

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