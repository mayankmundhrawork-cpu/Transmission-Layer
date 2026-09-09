# Transmission Layer — board brief · 2026-09-09 08:57Z

data as of **2026-09-09** · 98 series · 14 red / 37 amber · 8 events surfaced (35 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.47, 1d in regime; vol-pct 0.274, breadth-off 0.667, Markov P(high-vol) 0.019)
- [INVERTED] **safe_haven_gold** — corr20 -0.45, corr60 -0.4, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.87, corr60 0.87, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 -0.05, corr60 0.31, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.22, corr60 0.09, last shift 2026-06-05. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.79, corr60 -0.84, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.15, corr60 -0.05, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.35, corr60 -0.17, last shift 2026-06-26. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.02, corr60 0.21, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.503** (n=1132) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.823** (n=2007) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.08] cross-asset · 4 series ↑
- brent [COMMODITIES]: last 99.97, z20 2.41, zc 1.12, resid-z 0.03 [quiet], 1d 2.09%, 1-session move +2.09% ≥ 1.5%; |z20|=2.41
- wti [COMMODITIES]: last 94.63, z20 2.18, zc 0.84, resid-z -0.12 [quiet], 1d 1.72%, 1-session move +1.72% ≥ 1.5%; |z20|=2.18
- dow_jones [INDICES]: last 52790.22, z20 -2.09, zc -0.59, resid-z -0.48 [quiet], 1d -1.17%, |z20|=2.09
- dyn_vt [EQUITIES]: last 160.93, z20 -0.04, zc -0.02, resid-z 1.64 [unexplained], 1d -0.49%, 1y-pct=95
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.671 vs dow_jones, historically leads by 5d
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.555 vs brent, historically leads by 4d
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.525 vs brent, historically leads by 5d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.569 vs brent
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.551 vs dyn_vt
- Source: Brent crude reaches $100 as war in Iran intensifies — MarketWatch Top, 2026-09-09. https://www.marketwatch.com/story/brent-crude-reaches-100-as-war-in-iran-intensifies-b73832e2?mod=mw_rss_topstories
- Source: Sensex, Nifty off day’s low, crude prices & IT stocks selloff weigh sentiment — BusinessLine Mkts, 2026-09-09. https://www.thehindubusinessline.com/markets/sensex-nifty-slump-as-crude-prices-surge-it-stocks-lead-selloff/article71446220.ece
- Source: Brent Breaks $100 for the First Time in Nearly Two Months — OilPrice, 2026-09-09. https://oilprice.com/Latest-Energy-News/World-News/Brent-Breaks-100-for-the-First-Time-in-Nearly-Two-Months.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-16 (d=0.36), 2025-10-21 (d=0.5)

### [RED 7.17] cross-asset · 3 series ↓
- dyn_techm_ns [EQUITIES]: last 1506.60, z20 -3.85, zc -2.13, resid-z -1.74 [unexplained], 1d -3.36%, |z20|=3.85
- nifty_it [INDICES]: last 28935.35, z20 -3.79, zc -2.13, resid-z -1.65 [unexplained], 1d -3.17%, |z20|=3.79
- dyn_tataelxsi_ns [EQUITIES]: last 3406.90, z20 -3.09, zc -1.42, resid-z -0.86 [quiet], 1d -2.44%, |z20|=3.09; 1y-pct=1
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.78).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tatatech_ns (rho 0.58 via nifty_it, z -1.22, reacted); nifty_50 (rho 0.481 via nifty_it, z -2.78, reacted)
- Watch next: shanghai_comp (inverse) — not yet - watch; rho -0.508 vs dyn_techm_ns, historically leads by 5d
- **India receivers**: dyn_tatatech_ns (rho 0.58, z -1.22); nifty_50 (rho 0.481, z -2.78)
- Source: IT stocks crash as Coforge leads selloff; Infosys, Tech Mahindra, HCL Tech, TCS slide — BusinessLine Mkts, 2026-09-09. https://www.thehindubusinessline.com/markets/it-stocks-crash-as-coforge-leads-selloff-infosys-tech-mahindra-hcl-tech-tcs-slide/article71445708.ece
- Source: Tech Mahindra Share Price Live Updates: Tech Mahindra's Price Movement Analysis — ET Markets, 2026-09-09. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tech-mahindra-share-price-live-09-sep-2026/liveblog/133950510.cms
- Source: Tech Mahindra Share Price Live Updates: Tech Mahindra's Price Movement Today — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tech-mahindra-stock-price-livestock-price-today-live-updates-08-sep-2026/liveblog/133905653.cms
- Historical analogues: 2025-08-13 (d=0.78), 2025-01-23 (d=0.84), 2025-12-30 (d=0.85)

### [RED 5.61] cross-asset · 2 series ↓
- nifty_50 [INDICES]: last 23542.80, z20 -2.78, zc -0.74, resid-z 0.12 [quiet], 1d -0.39%, |z20|=2.78
- dyn_jiofin_bo [EQUITIES]: last 231.65, z20 -1.78, zc -0.54, resid-z 0.07 [quiet], 1d -0.79%, 1y-pct=4
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-06 (z-distance 0.09).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.62 via nifty_50, z -1.76, reacted); nifty_midcap_100 (rho 0.612 via nifty_50, z -1.95, reacted); nifty_it (rho 0.481 via nifty_50, z -3.79, reacted); dyn_indianb_ns (rho 0.468 via dyn_jiofin_bo, z -2.34, reacted); dyn_indusindbk_bo (rho 0.467 via nifty_50, z 0.25, quiet)
- **India receivers**: nifty_fmcg (rho 0.62, z -1.76); nifty_midcap_100 (rho 0.612, z -1.95); nifty_it (rho 0.481, z -3.79); dyn_indianb_ns (rho 0.468, z -2.34)
- Source: Sensex, Nifty off day’s low, crude prices & IT stocks selloff weigh sentiment — BusinessLine Mkts, 2026-09-09. https://www.thehindubusinessline.com/markets/sensex-nifty-slump-as-crude-prices-surge-it-stocks-lead-selloff/article71446220.ece
- Source: Sensex today | Stock Market Live: Sensex drops over 650 points, Nifty slips below 23,500 as IT stocks fall — BusinessLine Mkts, 2026-09-09. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-9th-september-2026/article71445394.ece
- Source: Sensex, Nifty tumble in early trade amid escalating tensions in West Asia, higher oil prices — BusinessLine Mkts, 2026-09-09. https://www.thehindubusinessline.com/markets/sensex-nifty-tumble-in-early-trade-amid-escalating-tensions-in-west-asia-higher-oil-prices/article71445759.ece
- Historical analogues: 2025-08-06 (d=0.09), 2025-07-29 (d=0.53), 2025-07-18 (d=0.65)

### [RED 5.28] usd_jpy ↓
- usd_jpy [FX]: last 153.58, z20 -3.28, zc -0.18, resid-z -0.22 [quiet], 1d -0.18%, |z20|=3.28
- **Mechanism**: usd_jpy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eur_usd (inverse) — not yet - watch; rho -0.539 vs usd_jpy
- Source: Bessent says ‘I am the house now.’ What it means for the yen — and U.S. stocks. — MarketWatch Top, 2026-09-09. https://www.marketwatch.com/story/bessent-says-i-am-the-house-now-what-it-means-for-the-yen-and-u-s-stocks-9ef63bc3?mod=mw_rss_topstories
- Source: Global Market: Japan bond yields ease as yen strength tempers BOJ tightening bets — ET Markets, 2026-09-09. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japan-bond-yields-ease-as-yen-strength-tempers-boj-tightening-bets/articleshow/133952201.cms
- Source: Yen holds near seven-month high as US dollar steadies — Mint Markets, 2026-09-08. https://www.livemint.com/market/yen-holds-near-seven-month-high-as-us-dollar-steadies-11788897469720.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2024-11-08 (d=0.01)

### [RED 5.15] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.67, z20 2.15, zc n/a, resid-z n/a [quiet], 1d 0.17%, 52-wk extreme (pct=99); |z20|=2.15; 1y-pct=99
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.454 via midcap_largecap_ratio, z -1.95, reacted); nifty_50 (rho -0.427 via midcap_largecap_ratio, z -2.78, reacted); nifty_fmcg (rho -0.421 via midcap_largecap_ratio, z -1.76, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.454, z -1.95); nifty_50 (rho -0.427, z -2.78); nifty_fmcg (rho -0.421, z -1.76)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [AMBER 5.07] cross-asset · 3 series ↑
- ust_2y [RATES]: last 4.37, z20 1.75, zc 0.54, resid-z 0.16 [quiet], 1d 0.69%, |z20|=1.75; 1y-pct=98
- ust_10y [RATES]: last 4.78, z20 1.64, zc 0.22, resid-z -0.18 [quiet], 1d 0.21%, |z20|=1.64; 1y-pct=99
- dyn_bond [EQUITIES]: last 90.00, z20 -1.45, zc -0.03, resid-z 0.59 [quiet], 1d -0.05%, 1y-pct=1
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: tips_10y_real (co-move) — not yet - watch; rho 0.74 vs ust_2y
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.511 vs ust_2y
- Source: US bond yields near 5%: What it could mean for stocks, corporate borrowing and the economy — ET Markets, 2026-09-09. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-bond-yields-near-5-what-it-could-mean-for-stocks-corporate-borrowing-and-the-economy/articleshow/133957322.cms
- Source: Global Market: Japan bond yields ease as yen strength tempers BOJ tightening bets — ET Markets, 2026-09-09. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japan-bond-yields-ease-as-yen-strength-tempers-boj-tightening-bets/articleshow/133952201.cms
- Source: Five pressure points to watch as Treasury yields creep toward 5% — ET Markets, 2026-09-08. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/five-pressure-points-to-watch-as-treasury-yields-creep-toward-5/slideshow/133929693.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-11 (d=0.24), 2025-05-15 (d=0.38)

### [RED 5.01] dyn_qcom ↑
- dyn_qcom [EQUITIES]: last 174.09, z20 3.01, zc 0.05, resid-z 0.37 [quiet], 1d 3.17%, |z20|=3.01
- **Mechanism**: dyn_qcom ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.513 vs dyn_qcom, historically leads by 2d
- Source: Qualcomm-Amazon AI deal: Why the chipmaker’s stock surged — ET Markets, 2026-09-09. https://economictimes.indiatimes.com/markets/us-stocks/news/qualcomm-amazon-ai-deal-why-the-chipmakers-stock-surged/slideshow/133955258.cms
- Source: Qualcomm stock jumps 9% on AI chip deal with Amazon, hits 2-month high — Mint Markets, 2026-09-08. https://www.livemint.com/market/stock-market-news/qualcomm-stock-jumps-9-on-ai-chip-deal-with-amazon-hits-2-month-high-11788882415437.html
- Source: Qualcomm’s stock climbs as Amazon chip deal offers investors much-needed good news — MarketWatch Top, 2026-09-08. https://www.marketwatch.com/story/qualcomms-stock-climbs-as-amazon-chip-deal-offers-investors-some-much-needed-good-news-5b6a95ca?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.02), 2026-05-04 (d=0.1)

### [RED 4.86] gold_silver_ratio ↓
- gold_silver_ratio [DERIVED]: last 66.10, z20 -1.86, zc n/a, resid-z n/a [quiet], 1d -0.26%, GSR<75 (extreme low); |z20|=1.86
- **Mechanism**: gold_silver_ratio ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.401 via gold_silver_ratio, z -1.95, reacted)
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.824 vs gold_silver_ratio
- **India receivers**: nifty_midcap_100 (rho -0.401, z -1.95)
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

## Watchlist (below surfacing floor)
dyn_pcjeweller_ns ↑ (4.64), dyn_hdb ↓ (4.63), comex_copper ↑ (4.6), commodities · 2 series ↑ (4.5), dxy ↓ (4.45), dyn_indianb_ns ↓ (4.34), dyn_icicigi_bo ↓ (4.33), dyn_coalindia_ns ↑ (3.69), dyn_lenskart_ns ↑ (3.59), indices · 3 series ↓ (3.38), dyn_muthootfin_ns ↓ (3.13), indices · 2 series ↑ (2.57)

## India macro
- nifty_50: 23542.8008 (1d -0.39%, z20 -2.78, flag red)
- nifty_midcap_100: 62779.7500 (1d -0.22%, z20 -1.95, flag amber)
- usd_inr: 95.0000 (1d 0.54%, z20 -0.31, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6666 (1d 0.17%, z20 2.15, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · India CPI T-5d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 78.4 — "India has 123 million tonnes of coal reserves, enough for 51 days: G Kishan Reddy"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 74.7 — "India has 123 million tonnes of coal reserves, enough for 51 days: G Kishan Reddy"
- COALINDIA.NS (COAL INDIA LTD) score 74.5 — "India has 123 million tonnes of coal reserves, enough for 51 days: G Kishan Reddy"
- INDIANB.NS (INDIAN BANK) score 56.2 — "Why is Indian stock market down? 3 key factors explained - Top losers contributing to the "
- COIN (Coinbase Global, Inc.) score 50.2 — "QNu Labs raises ₹200 crore to scale quantum-safe cybersecurity globally"
- BAC (Bank of America Corporation) score 49.1 — "HDFC Bank shares fall 2% to fresh 52-week low; here’s why"
- HDB (HDFC Bank Limited) score 44.6 — "HDFC Bank shares fall 2% to fresh 52-week low; here’s why"
- TECHM.NS (TECH MAHINDRA LIMITED) score 43.1 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Price Movement Analysis"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 43.0 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Price Movement Analysis"
- TECH (Bio-Techne Corp) score 43.0 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Price Movement Analysis"
- OHI (Omega Healthcare Investors, In) score 42.6 — "​6 superstar investors, 6 big bets of Madhusudan Kela, Ashish Kacholia & others"
- IDBI.NS (IDBI BANK LIMITED) score 40.4 — "HDFC Bank shares fall 2% to fresh 52-week low; here’s why"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 40.4 — "HDFC Bank shares fall 2% to fresh 52-week low; here’s why"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 40.4 — "HDFC Bank shares fall 2% to fresh 52-week low; here’s why"
- BOND (PIMCO Active Bond Exchange-Tra) score 35.4 — "Global Market: Japan bond yields ease as yen strength tempers BOJ tightening bets"
- CHKP (Check Point Software Technolog) score 34.8 — "Karamtara Engineering IPO Day 1: Issue booked 4.74x so far. Check key dates, review, issue"
- 301077.SZ (CHINASTARS) score 28.4 — "Global Market: China inflation rises in August, but weak demand remains a concern"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 23.4 — "Pakistan’s Energy Crisis Set to Ease as Qatari LNG Breaks Through Hormuz"
- LTH (Life Time Group Holdings, Inc.) score 22.1 — "Astec Lifesciences share price skyrockets 17% despite weak sentiments on D-Street. Do you "
- PCJEWELLER.NS (PC JEWELLER LTD) score 13.5 — "PC Jeweller shares jump 4%, surge 38% in one week. What's polishing the stock's shine?"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 11.7 — "Adani Airports to raise Rs 9,825 crore from Temasek, BlackRock, Premji Invest and Alpha Wa"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 10.0 — "Stocks to Watch, Sep 7: 3 Tata group cos, 4 Railway stocks, 2 shipping sector, 3 Pharma ma"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.5 — "Kenya withdraws Tata Group’s century-old soda ash mining concession"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.5 — "Kenya withdraws Tata Group’s century-old soda ash mining concession"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.8 — "Wheels India share price hits a 52-week high, jumps over 55% in just 6 sessions- Should yo"
- MS (Morgan Stanley) score 8.4 — "JPMorgan, Jane Street probes show India scrutinizing Wall Street"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.9 — "Stocks in focus today: Enviro Infra, NLC India, Berger Paints, Sanofi India, Fusion Financ"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 6.0 — "India has 123 million tonnes of coal reserves, enough for 51 days: G Kishan Reddy"
- META (Meta) score 5.8 — "India Gold Metaverse appoints Chand as MD of BullionX"
- VT (Vanguard Total World Stock Ind) score 5.7 — "Uganda Set to Become World's Newest Oil Exporter in Early 2027"
- NVDA (NVIDIA Corporation) score 5.7 — "NVDA - NVIDIA: NEEDHAM STAYS BULLISH AFTER $12.9B HUGGING FACE DEAL Needham reiterated its"
- JIOFIN.BO (Jio Financial Services Limited) score 5.6 — "US JOBS BLOW PAST EXPECTATIONS 🔸 August Nonfarm Payrolls: +162K vs +55K expected — a major"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.5 — "Axis Bank to ICICI Bank - Why banking stocks are falling today?"
- IFCI.NS (IFCI LTD) score 4.8 — "IFCI share price down today- drops 14% in 2 days- Why is the stock falling?"
- QCOM (QUALCOMM Incorporated) score 3.6 — "Qualcomm-Amazon AI deal: Why the chipmaker’s stock surged"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 1.6 — "Lenskart Solutions among 4 stocks to hit 52-week highs & rallied up to 22% in a month"
- DELL (Dell Technologies Inc.) score 1.3 — "Dell’s AI Boom: $95 billion backlog reshapes growth outlook"
- DKS (Dick's Sporting Goods Inc) score 0.2 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- MRNA (Moderna, Inc.) score 0.2 — "Can Wolfe’s upgrade push Moderna stock higher?"
- VOLTAS.NS (VOLTAS LTD) score 0.0 — "Voltas reported strong growth in June quarter, but failed to impress"

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