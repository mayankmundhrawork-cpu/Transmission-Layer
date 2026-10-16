# Transmission Layer — board brief · 2026-10-16 14:49Z

data as of **2026-10-16** · 97 series · 16 red / 26 amber · 8 events surfaced (32 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.669, 10d in regime; vol-pct 0.632, breadth-off 0.706, Markov P(high-vol) 0.014)
- [INVERTED] **safe_haven_gold** — corr20 -0.44, corr60 -0.44, contra nifty_50 corr20=0.4, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.87, corr60 0.84, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.29, corr60 0.22, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.04, corr60 0.14, last shift 2026-08-26. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.78, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.1, corr60 -0.02, last shift 2026-08-12. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.05, corr60 -0.24, last shift 2026-08-10. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.78, corr60 0.26, last shift 2026-07-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.002977997490474893)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.501** (n=1144) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.815** (n=2083) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.35] cross-asset · 3 series ↑
- dyn_techm_ns [EQUITIES]: last 1790.00, z20 7.03, zc 4.43, resid-z 4.89 [unexplained], 1d 8.48%, |z20|=7.03; 1y-pct=100
- nifty_it [INDICES]: last 31924.10, z20 4.13, zc 2.32, resid-z 2.34 [unexplained], 1d 3.92%, |z20|=4.13
- dyn_tataelxsi_ns [EQUITIES]: last 3850.10, z20 3.62, zc 1.66, resid-z 1.84 [unexplained], 1d 4.06%, |z20|=3.62
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.78).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_justdial_bo (rho 0.559 via nifty_it, z 3.24, reacted); nifty_50 (rho 0.512 via dyn_tataelxsi_ns, z 0.82, quiet); nifty_fmcg (rho 0.468 via dyn_tataelxsi_ns, z -0.66, quiet); midcap_largecap_ratio (rho -0.439 via dyn_techm_ns, z -3.57, reacted); dyn_tatatech_ns (rho 0.392 via nifty_it, z 0.68, quiet)
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.512 vs dyn_tataelxsi_ns
- **India receivers**: dyn_justdial_bo (rho 0.559, z 3.24); nifty_50 (rho 0.512, z 0.82); nifty_fmcg (rho 0.468, z -0.66); midcap_largecap_ratio (rho -0.439, z -3.57)
- Source: Kotak Mahindra Bank among 5 stocks that hit 52-week highs & rallied up to 15% in a month — ET Markets, 2026-10-16. https://economictimes.indiatimes.com/markets/stocks/news/kotak-mahindra-bank-among-5-stocks-that-hit-52-week-highs-amp-rallied-up-to-15-in-a-month/slideshow/134995212.cms
- Source: Worst over for IT stocks? Experts analyse Q2 results of TCS, HCL, Tech Mahindra and others, suggest top picks — Mint Markets, 2026-10-16. https://www.livemint.com/market/stock-market-news/worst-over-for-it-stocks-experts-analyse-q2-results-of-tcs-hcl-tech-mahindra-and-others-suggest-top-picks-11792149864702.html
- Source: Market wrap: Tech Mahindra, TCS, InterGlobe, BSE top gainers and losers on Nifty and Sensex on Friday — ET Markets, 2026-10-16. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-tech-mahindra-tcs-interglobe-bse-top-gainers-and-losers-on-nifty-and-sensex-on-friday/articleshow/134992216.cms
- Historical analogues: 2025-08-13 (d=0.78), 2025-01-23 (d=0.84), 2025-12-30 (d=0.85)

### [RED 7.46] usd_inr ↓
- usd_inr [FX]: last 94.95, z20 -2.46, zc -0.40, resid-z -0.42 [quiet], 1d -0.21%, 20d range extreme; |z20|=2.46
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.371 via usd_inr, z -0.09, quiet); dyn_karurvysya_ns (rho -0.366 via usd_inr, z 2.99, reacted)
- **India receivers**: dyn_idbi_ns (rho -0.371, z -0.09); dyn_karurvysya_ns (rho -0.366, z 2.99)
- Source: Rupee rises 1.9% in a week, closes below 95 per dollar — ET Markets, 2026-10-16. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-rises-1-9-in-a-week-closes-below-95-per-dollar/articleshow/134996292.cms
- Source: Rupee posts best week in seven months, fundamentals key for lasting turnaround — ET Markets, 2026-10-16. https://economictimes.indiatimes.com/markets/forex/rupee-posts-best-week-in-seven-months-fundamentals-key-for-lasting-turnaround/articleshow/134991672.cms
- Source: Gold, Silver rebound on softer Dollar and falling yields; domestic gains capped by Rupee strength — BusinessLine Mkts, 2026-10-16. https://www.thehindubusinessline.com/markets/gold/gold-silver-rebound-on-softer-dollar-and-falling-yields-domestic-gains-capped-by-rupee-strength/article71591618.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [AMBER 5.95] wti ↑
- wti [COMMODITIES]: last 95.68, z20 0.95, zc -1.01, resid-z -1.41 [quiet], 1d -2.34%, 1-session move -2.34% ≥ 1.5%
- **Mechanism**: wti ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.854 vs wti
- Source: Ukraine Defies Trump With Renewed Attacks on Russian Oil Infrastructure — OilPrice, 2026-10-16. https://oilprice.com/Geopolitics/Europe/Ukraine-Defies-Trump-With-Renewed-Attacks-on-Russian-Oil-Infrastructure.html
- Source: Trump's Oil Price Strategy Faces Two Major Tests This Weekend — OilPrice, 2026-10-16. https://oilprice.com/Energy/Energy-General/Trumps-Oil-Price-Strategy-Faces-Two-Major-Tests-This-Weekend.html
- Source: Global Fuel Oil Shortage Deepens as Middle East and Russia Supplies Collapse — OilPrice, 2026-10-16. https://oilprice.com/Latest-Energy-News/World-News/Global-Fuel-Oil-Shortage-Deepens-as-Middle-East-and-Russia-Supplies-Collapse.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

### [RED 5.01] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 7380.00, z20 3.01, zc 4.54, resid-z -1.04 [moved], 1d 15.67%, |z20|=3.01; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Worst over for IT stocks? Experts analyse Q2 results of TCS, HCL, Tech Mahindra and others, suggest top picks — Mint Markets, 2026-10-16. https://www.livemint.com/market/stock-market-news/worst-over-for-it-stocks-experts-analyse-q2-results-of-tcs-hcl-tech-mahindra-and-others-suggest-top-picks-11792149864702.html
- Source: Stock to buy after SEBI CAS new rule: Experts bullish on Groww brand parent Billionbrains Garage Ventures shares; target — Mint Markets, 2026-10-16. https://www.livemint.com/market/stock-market-news/stock-to-buy-after-sebi-cas-new-rule-experts-bullish-on-groww-brand-parent-billionbrains-garage-ventures-shares-target-11792143458424.html
- Source: Gold vs silver vs platinum: Which metal saw biggest rally since last Dussehra? Experts explain outlook — Mint Markets, 2026-10-16. https://www.livemint.com/market/commodities/gold-vs-silver-vs-platinum-which-metal-saw-biggest-rally-since-last-dussehra-experts-explain-outlook-11792142307625.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

### [RED 4.99] dyn_karurvysya_ns ↑
- dyn_karurvysya_ns [EQUITIES]: last 355.65, z20 2.99, zc 1.49, resid-z 0.79 [quiet], 1d 2.89%, |z20|=2.99; 1y-pct=100
- **Mechanism**: dyn_karurvysya_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indianb_ns (rho 0.453 via dyn_karurvysya_ns, z 1.77, reacted); dyn_muthootfin_ns (rho 0.389 via dyn_karurvysya_ns, z -1.25, reacted); nifty_50 (rho 0.378 via dyn_karurvysya_ns, z 0.82, quiet); usd_inr (rho -0.366 via dyn_karurvysya_ns, z -2.46, reacted)
- **India receivers**: dyn_indianb_ns (rho 0.453, z 1.77); dyn_muthootfin_ns (rho 0.389, z -1.25); nifty_50 (rho 0.378, z 0.82); usd_inr (rho -0.366, z -2.46)
- Source: Karur Vysya Bank shares jump 6% to hit a 52-week high after Q2 results - Should you buy? Rationale, target price — Mint Markets, 2026-10-16. https://www.livemint.com/market/stock-market-news/karur-vysya-bank-shares-jump-6-to-hit-a-52-week-high-after-q2-results-should-you-buy-rationale-target-price-11792125152481.html
- Source: Karur Vysya Bank shares rally 6% after Q2 profit jumps 37% YoY — ET Markets, 2026-10-16. https://economictimes.indiatimes.com/markets/stocks/news/karur-vysya-bank-shares-rally-6-after-q2-profit-jumps-37-yoy/articleshow/134982900.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-02 (d=0.07), 2025-01-31 (d=0.09)

### [RED 4.87] gold_silver_ratio ↑
- gold_silver_ratio [DERIVED]: last 72.70, z20 1.87, zc n/a, resid-z n/a [quiet], 1d -0.91%, GSR<75 (extreme low); |z20|=1.87
- **Mechanism**: gold_silver_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (inverse) — not yet - watch; rho -0.532 vs gold_silver_ratio, historically leads by 3d
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.518 vs gold_silver_ratio, historically leads by 5d
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

### [RED 4.66] dyn_lth ↑
- dyn_lth [EQUITIES]: last 41.62, z20 2.66, zc 1.19, resid-z 0.60 [quiet], 1d 2.61%, |z20|=2.66
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Goodluck India stock hits a new all-time high: is the stock worth watching? — Mint Markets, 2026-10-16. https://www.livemint.com/market/stock-market-news/goodluck-india-stock-price-should-you-buy-goodluck-india-stock-11792065784978.html
- Source: Nifty hits intra-day high on open for the sixth time in 2026 — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/markets/nifty-hits-intra-day-high-on-open-for-the-sixth-time-in-2026/article71560509.ece
- Source: Big pharma stocks close near all-time highs as tech selloff pushes investors toward safer bets — MarketWatch Top, 2026-10-15. https://www.marketwatch.com/story/big-pharma-stocks-near-all-time-highs-as-tech-selloff-pushes-investors-toward-safer-bets-0a5d5d07?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-17 (d=0.02), 2025-12-31 (d=0.02)

### [RED 4.59] dyn_rs ↑
- dyn_rs [EQUITIES]: last 416.21, z20 2.59, zc 1.47, resid-z 0.49 [quiet], 1d 2.35%, |z20|=2.59; 1y-pct=100
- **Mechanism**: dyn_rs ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Jio Platforms IPO: Ambani taps massive Reliance workforce to boost offering — BusinessLine Mkts, 2026-10-16. https://www.thehindubusinessline.com/markets/jio-platforms-ipo-ambani-taps-massive-reliance-workforce-to-boost-offering/article71593138.ece
- Source: Mukesh Ambani taps massive Reliance Industries workforce to boost record Jio IPO — Mint Markets, 2026-10-16. https://www.livemint.com/market/ipo/jio-platforms-ipo-shares-for-reliance-industries-employees-11792141480138.html
- Source: Mukesh Ambani taps massive Reliance workforce to boost Jio’s record IPO — ET Markets, 2026-10-16. https://economictimes.indiatimes.com/markets/stocks/news/mukesh-ambani-taps-massive-reliance-workforce-to-boost-jios-record-ipo/articleshow/134988928.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-30 (d=0.02), 2026-03-31 (d=0.02)

## Watchlist (below surfacing floor)
dyn_wit ↑ (4.59), dyn_hdb ↑ (4.57), dow_jones ↑ (4.56), shanghai_comp ↓ (4.3), nasdaq_100 ↓ (4.07), usd_cny ↓ (4.05), commodities · 3 series ↓ (3.75), rates · 3 series ↑ (3.7), midcap_largecap_ratio ↓ (3.57), dyn_muthootfin_ns ↓ (3.25), dyn_justdial_bo ↑ (3.24), dyn_dell ↓ (3.2)

## India macro
- nifty_50: 23146.1504 (1d 0.65%, z20 0.82, flag none)
- nifty_midcap_100: 59130.8516 (1d -0.10%, z20 -0.70, flag none)
- usd_inr: 94.9500 (1d -0.21%, z20 -2.46, flag red)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5547 (1d -0.75%, z20 -3.57, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 117.7 — "Indian bonds hang tight ahead of supply"
- INOXINDIA.NS (INOX INDIA LIMITED) score 112.2 — "Indian bonds hang tight ahead of supply"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 111.3 — "Indian bonds hang tight ahead of supply"
- INDIANB.NS (INDIAN BANK) score 110.0 — "Indian bonds hang tight ahead of supply"
- BAC (Bank of America Corporation) score 99.9 — "ICICI Bank Q2 Results Preview: PAT, NII may rise up to 21% YoY; margins, deposit growth in"
- HDB (HDFC Bank Limited) score 93.3 — "ICICI Bank Q2 Results Preview: PAT, NII may rise up to 21% YoY; margins, deposit growth in"
- IDBI.NS (IDBI BANK LIMITED) score 88.4 — "ICICI Bank Q2 Results Preview: PAT, NII may rise up to 21% YoY; margins, deposit growth in"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 88.4 — "ICICI Bank Q2 Results Preview: PAT, NII may rise up to 21% YoY; margins, deposit growth in"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 88.4 — "ICICI Bank Q2 Results Preview: PAT, NII may rise up to 21% YoY; margins, deposit growth in"
- TECHM.NS (TECH MAHINDRA LIMITED) score 85.5 — "Tech Mahindra dividend, bonus share 2026: Double delight for investors this Diwali | Shoul"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 82.5 — "Tech Mahindra dividend, bonus share 2026: Double delight for investors this Diwali | Shoul"
- TECH (Bio-Techne Corp) score 82.5 — "Tech Mahindra dividend, bonus share 2026: Double delight for investors this Diwali | Shoul"
- COIN (Coinbase Global, Inc.) score 70.8 — "China's central bank to boost support for global investors in financial markets"
- OHI (Omega Healthcare Investors, In) score 64.1 — "Tech Mahindra dividend, bonus share 2026: Double delight for investors this Diwali | Shoul"
- CHKP (Check Point Software Technolog) score 46.4 — "Already up 86% in 6 months, ICICI Direct still sees another 39% upside in this small-cap s"
- TGT (Target Corporation) score 45.2 — "Stock to buy after SEBI CAS new rule: Experts bullish on Groww brand parent Billionbrains "
- BOND (PIMCO Active Bond Exchange-Tra) score 40.7 — "Indian bonds hang tight ahead of supply"
- RS (Reliance, Inc.) score 31.5 — "Mukesh Ambani taps massive Reliance workforce to boost Jio’s record IPO"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 29.2 — "Gold vs silver vs platinum: Which metal saw biggest rally since last Dussehra? Experts exp"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 28.9 — "BoE's Bailey says energy price pass-through remains limited, rate risks persist"
- LTH (Life Time Group Holdings, Inc.) score 26.6 — "Goodluck India stock hits a new all-time high: is the stock worth watching?"
- JIOFIN.BO (Jio Financial Services Limited) score 25.2 — "China's central bank to boost support for global investors in financial markets"
- 301077.SZ (CHINASTARS) score 24.8 — "China's central bank to boost support for global investors in financial markets"
- SEPN (Septerna, Inc.) score 24.3 — "10 stocks held by 100+ MF schemes in September rally up to 205% in CY26; 6 turn multibagge"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 19.4 — "Bajaj Housing Finance Q2 Results: PAT rises 18% YoY to Rs 757 crore, AUM grows 25%"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 18.8 — "Tata Consumer Share Price Live Updates: Tata Consumer Stock Details"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 18.8 — "Tata Consumer Share Price Live Updates: Tata Consumer Stock Details"
- BZ=F (Brent Crude Oil Last Day Finan) score 18.8 — "Rupee posts best week in seven months, fundamentals key for lasting turnaround"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.6 — "Bajaj Housing Finance Q2 Results: PAT rises 18% YoY to Rs 757 crore, AUM grows 25%"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 11.5 — "Nifty falls below 22,300 at noon as Adani Stocks, ITC, Metals slide"
- NVDA (NVIDIA Corporation) score 10.3 — "GERMANY PLANS MAJOR AI PARTNERSHIP WITH NVIDIA — HANDELSBLATT German Chancellor Friedrich "
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.1 — "Don’t ditch tech stocks just yet. Make these moves to take advantage of the latest AI rese"
- VT (Vanguard Total World Stock Ind) score 8.7 — "U.S. Wants World Bank to Drop Ban on Upstream Oil and Gas Funding"
- GS (Goldman Sachs Group, Inc. (The) score 8.6 — "Wipro shares rise over 2% as Q2 revenue grows 9% YoY. What are Nomura, Goldman Sachs analy"
- META (Meta) score 8.4 — "Gold vs silver vs platinum: Which metal saw biggest rally since last Dussehra? Experts exp"
- JEF (Jefferies Financial Group Inc.) score 7.1 — "Jefferies technical analyst finds an encouraging development in Thursday rebound, setting "
- WIT (Wipro Limited) score 6.4 — "Wipro shares rise 5%, up 15% so far in October - Should you buy this IT stock after Q2 res"
- POLICYBZR.NS (PB FINTECH LIMITED) score 1.9 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
- DELL (Dell Technologies Inc.) score 0.2 — "Piero Cipollone: Interview with Corriere della Sera"
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