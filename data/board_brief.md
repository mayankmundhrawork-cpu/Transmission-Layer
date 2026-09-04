# Transmission Layer — board brief · 2026-09-04 08:50Z

data as of **2026-09-04** · 98 series · 7 red / 43 amber · 8 events surfaced (34 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.285, 2d in regime; vol-pct 0.153, breadth-off 0.417, Markov P(high-vol) 0.026)
- [INVERTED] **safe_haven_gold** — corr20 -0.46, corr60 -0.41, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.88, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.1, corr60 0.35, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.17, corr60 0.05, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.84, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.16, corr60 -0.08, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.23, corr60 -0.14, last shift 2026-06-30. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.02, corr60 0.23, last shift 2026-07-16. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 90** scanned series survive multiplicity control (effective p ≤ 0.0006496287948376533)
- **SETUP** dow_jones → asx_200: leads 1d (ccf 0.59, β 0.486, p 0.0); driver zc 1.57 → expected 0.573%. Type hit-rate 0.827 (n=1993).
- **SETUP** dow_jones → usd_brl: leads 1d (ccf -0.406, β -0.3447, p 0.0); driver zc 1.57 → expected -0.406%. Type hit-rate 0.827 (n=1993).
- Track record · residual_reversion: hit-rate **0.502** (n=1126) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.827** (n=1993) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.22] usd_jpy ↓
- usd_jpy [FX]: last 156.36, z20 -5.22, zc -2.97, resid-z -4.29 [unexplained], 1d -1.61%, |z20|=5.22
- **Mechanism**: usd_jpy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eur_usd (inverse) — not yet - watch; rho -0.561 vs usd_jpy
- Watch next: kospi (inverse) — not yet - watch; rho -0.514 vs usd_jpy
- Source: Global Market: JGB yields extend fall as stronger yen, hawkish BOJ outlook lift sentiment — ET Markets, 2026-09-04. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-jgb-yields-extend-fall-as-stronger-yen-hawkish-boj-outlook-lift-sentiment/articleshow/133753277.cms
- Source: Yen Rallies as Intervention, BOJ Rate Risk Weigh on Traders — Mint Markets, 2026-09-03. https://www.livemint.com/market/yen-rallies-as-intervention-boj-rate-risk-weigh-on-traders-11788476981657.html
- Source: Yen Rallies as Intervention, BOJ Rate Risk Weigh on Wary Traders — Mint Markets, 2026-09-03. https://www.livemint.com/market/yen-rallies-as-intervention-boj-rate-risk-weigh-on-wary-traders-11788476981201.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2024-11-08 (d=0.01)

### [RED 6.59] cross-asset · 5 series ↑
- ust_2y [RATES]: last 4.39, z20 2.66, zc 0.00, resid-z 0.16 [quiet], 1d 0.00%, |z20|=2.66; 1y-pct=99
- ust_10y [RATES]: last 4.79, z20 2.37, zc 0.00, resid-z 0.12 [quiet], 1d 0.00%, |z20|=2.37; 1y-pct=99
- dyn_bond [EQUITIES]: last 90.04, z20 -1.64, zc 0.52, resid-z 0.94 [quiet], 1d 0.17%, 1y-pct=1
- tips_10y_real [RATES]: last 2.45, z20 1.41, zc 0.24, resid-z 0.43 [quiet], 1d 0.41%, 1y-pct=99
- ust_30y [RATES]: last 5.27, z20 1.11, zc 0.00, resid-z 0.06 [quiet], 1d 0.00%, 1y-pct=98
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eur_usd (co-move) — not yet - watch; rho 0.38 vs ust_2y, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.51 vs dyn_bond
- Source: Sensex today | Stock Market Live: Sensex rises 530 pts, Nifty up 65 pts on easing US Treasury yields; SBI Life, HDFC Life top gainers — BusinessLine Mkts, 2026-09-04. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-4th-september-2026/article71425360.ece
- Source: US Market: Rising R-star adds to pressure on US Treasury yields as AI investment, borrowing lift demand for capital — ET Markets, 2026-09-04. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-market-rising-r-star-adds-to-pressure-on-us-treasury-yields-as-ai-investment-borrowing-lift-demand-for-capital/articleshow/133752321.cms
- Source: REC set to debut tokenised corporate bond sale next week, bankers say — BusinessLine Mkts, 2026-09-04. https://www.thehindubusinessline.com/markets/rec-set-to-debut-tokenised-corporate-bond-sale-next-week-bankers-say/article71426936.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [AMBER 5.3] cross-asset · 4 series ↑
- vix [INDICES]: last 14.18, z20 -1.64, zc -0.12, resid-z n/a [quiet], 1d -0.98%, |z20|=1.64; 1y-pct=2
- dyn_vt [EQUITIES]: last 161.75, z20 1.14, zc 1.42, resid-z -0.03 [quiet], 1d 1.02%, 1y-pct=98
- sp500 [INDICES]: last 7747.80, z20 0.85, zc 1.48, resid-z -0.24 [quiet], 1d 1.06%, 1y-pct=98
- dow_jones [INDICES]: last 53687.54, z20 0.54, zc 1.57, resid-z 0.71 [priced], 1d 1.18%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-10-17 (z-distance 0.46).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.655 vs vix, historically leads by 5d
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.64 vs dyn_vt, historically leads by 5d
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.537 vs dyn_vt, historically leads by 1d
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.51 vs dyn_vt
- Source: Global Market: Japan stocks rebound on Wall Street boost, SoftBank rally — ET Markets, 2026-09-04. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japan-stocks-rebound-on-wall-street-boost-softbank-rally/articleshow/133753108.cms
- Source: Robinhood stock surges: Why HOOD is rallying and what Wall Street sees next — ET Markets, 2026-09-04. https://economictimes.indiatimes.com/markets/us-stocks/news/robinhood-stock-surges-why-hood-is-rallying-and-what-wall-street-sees-next/slideshow/133752990.cms
- Source: Wall Street ends sharply higher as Waller remarks ease rate hike fears — Mint Markets, 2026-09-03. https://www.livemint.com/market/wall-street-ends-sharply-higher-as-waller-remarks-ease-rate-hike-fears-11788465720251.html
- Historical analogues: 2024-10-17 (d=0.46), 2025-10-21 (d=0.48), 2025-08-27 (d=0.53)

### [RED 4.73] dyn_dell ↑
- dyn_dell [EQUITIES]: last 515.94, z20 2.73, zc 0.53, resid-z 2.36 [unexplained], 1d 4.82%, |z20|=2.73; 1y-pct=100
- **Mechanism**: dyn_dell ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_coalindia_ns (rho 0.467 via dyn_dell, z 1.16, reacted); nifty_it (rho -0.444 via dyn_dell, z -0.55, quiet)
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.542 vs dyn_dell, historically leads by 5d
- **India receivers**: dyn_coalindia_ns (rho 0.467, z 1.16); nifty_it (rho -0.444, z -0.55)
- Source: Dell’s AI Boom: $95 billion backlog reshapes growth outlook — ET Markets, 2026-09-03. https://economictimes.indiatimes.com/markets/us-stocks/news/dells-ai-boom-95-billion-backlog-reshapes-growth-outlook/slideshow/133726366.cms
- Source: HPE follows in Dell’s footsteps as it rides the AI server boom to a big earnings beat — MarketWatch Top, 2026-09-02. https://www.marketwatch.com/story/hpe-follows-in-dells-footsteps-as-it-rides-the-ai-server-boom-to-a-big-earnings-beat-ec46eaea?mod=mw_rss_topstories
- Source: Dell stock price news: Shares jump 14% on record Q2 results as AI server demand surges — data details — Mint Markets, 2026-09-02. https://www.livemint.com/market/stock-market-news/dell-stock-price-news-shares-jump-14-on-record-q2-results-as-ai-server-demand-surges-data-details-11788356963938.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-08 (d=0.18), 2025-10-01 (d=0.3)

### [AMBER 4.66] commodities · 2 series ↑
- wti [COMMODITIES]: last 90.80, z20 1.83, zc -0.23, resid-z 0.36 [quiet], 1d -0.55%, |z20|=1.83
- brent [COMMODITIES]: last 95.21, z20 1.53, zc -0.14, resid-z 0.25 [quiet], 1d -0.32%, |z20|=1.53
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.679 vs wti
- Source: Brent Nears $96 as Iran Conflict Keeps Oil Market on Edge — OilPrice, 2026-09-04. https://oilprice.com/Latest-Energy-News/World-News/Brent-Nears-96-as-Iran-Conflict-Keeps-Oil-Market-on-Edge.html
- Source: Crude oil futures rise as Vance declines to give timeline to end US-Iran conflict — BusinessLine Mkts, 2026-09-04. https://www.thehindubusinessline.com/markets/commodities/crude-oil-futures-rise-as-vance-declines-to-give-timeline-to-end-us-iran-conflict/article71426962.ece
- Source: Rupee's inflow-linked, RBI-backed optimism faces oil test — BusinessLine Mkts, 2026-09-04. https://www.thehindubusinessline.com/markets/forex/rupees-inflow-linked-rbi-backed-optimism-faces-oil-test/article71426895.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 4.53] dyn_icicigi_bo ↓
- dyn_icicigi_bo [EQUITIES]: last 1513.00, z20 -2.53, zc -0.04, resid-z 0.03 [quiet], 1d -0.07%, |z20|=2.53; 1y-pct=0
- **Mechanism**: dyn_icicigi_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Eternal, ICICI Bank, 5 other largecap stocks with upside potential of up to 40%. Do you own any? — ET Markets, 2026-09-04. https://economictimes.indiatimes.com/markets/stocks/news/eternal-icici-bank-5-other-largecap-stocks-with-upside-potential-of-up-to-40-do-you-own-any/slideshow/133751438.cms
- Source: Explained: What $127 billion FCNR(B) inflows mean for ICICI Bank, HDFC Bank, other bank stocks — ET Markets, 2026-09-03. https://economictimes.indiatimes.com/markets/stocks/news/explained-what-127-billion-fcnrb-inflows-mean-for-icici-bank-hdfc-bank-other-bank-stocks/articleshow/133725930.cms
- Source: HDFC Bank is losing ground as Nifty’s top stock while ICICI Bank gains — BusinessLine Mkts, 2026-09-03. https://www.thehindubusinessline.com/markets/hdfc-bank-is-losing-ground-as-niftys-top-stock-while-icici-bank-gains/article71422302.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.0), 2025-05-30 (d=0.03)

### [AMBER 4.09] dyn_pcjeweller_ns ↑
- dyn_pcjeweller_ns [EQUITIES]: last 11.46, z20 2.09, zc 2.60, resid-z 2.74 [unexplained], 1d 8.94%, |z20|=2.09
- **Mechanism**: dyn_pcjeweller_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bharatcoal_ns (rho 0.364 via dyn_pcjeweller_ns, z -0.13, quiet); dyn_muthootfin_ns (rho 0.353 via dyn_pcjeweller_ns, z -0.45, quiet)
- **India receivers**: dyn_bharatcoal_ns (rho 0.364, z -0.13); dyn_muthootfin_ns (rho 0.353, z -0.45)
- Source: PC Jeweller clears debt to one more bank, nears debt-free status — BusinessLine Mkts, 2026-09-03. https://www.thehindubusinessline.com/markets/gold/pc-jeweller-clears-debt-to-one-more-bank-nears-debt-free-status/article71423219.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-01-07 (d=0.32), 2025-02-06 (d=0.36)

### [AMBER 3.75] dyn_nvda ↑
- dyn_nvda [EQUITIES]: last 228.40, z20 1.75, zc 0.53, resid-z 0.94 [quiet], 1d 1.78%, 1y-pct=99
- **Mechanism**: dyn_nvda ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_inoxindia_ns (rho 0.381 via dyn_nvda, z 2.5, reacted); midcap_largecap_ratio (rho 0.365 via dyn_nvda, z 0.17, quiet)
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.627 vs dyn_nvda, historically leads by 4d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.601 vs dyn_nvda, historically leads by 4d
- **India receivers**: dyn_inoxindia_ns (rho 0.381, z 2.5); midcap_largecap_ratio (rho 0.365, z 0.17)
- Source: Nvidia takes back control of the AI trade as Big Tech nears record highs — MarketWatch Top, 2026-09-03. https://www.marketwatch.com/story/nvidia-takes-back-control-of-the-ai-trade-as-big-tech-nears-record-highs-c0dfed9d?mod=mw_rss_topstories
- Source: US stocks rise as Fed Governor signals possible rate pause; Nvidia, Snowflake rally — Mint Markets, 2026-09-03. https://www.livemint.com/market/stock-market-news/us-stocks-climb-after-fed-governor-s-comments-on-holding-rates-steady-11788443392991.html
- Source: Here’s what Nvidia’s $13 billion Hugging Face deal means for the world of AI — MarketWatch Top, 2026-09-03. https://www.marketwatch.com/story/heres-what-nvidias-13-billion-hugging-face-deal-means-for-the-world-of-ai-360e9fd1?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-24 (d=0.03), 2026-05-04 (d=0.03)

## Watchlist (below surfacing floor)
gold_silver_ratio ↓ (3.74), usd_inr ↓ (3.63), dyn_havells_ns ↓ (3.57), nifty_50 ↓ (3.53), dyn_tech ↑ (3.3), midcap_largecap_ratio ↑ (3.17), bovespa ↑ (2.62), fx · 2 series ↑ (2.54), dyn_inoxindia_ns ↑ (2.5), dyn_atherenerg_ns ↑ (2.49), indices · 2 series ↓ (2.47), dyn_tataelxsi_ns ↓ (2.26)

## India macro
- nifty_50: 23945.8008 (1d 0.30%, z20 -1.53, flag amber)
- nifty_midcap_100: 63069.3008 (1d -0.26%, z20 -2.09, flag amber)
- usd_inr: 94.4850 (1d -0.00%, z20 -1.63, flag amber)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6338 (1d -0.56%, z20 0.17, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 83.9 — "Stock recommendations for 4 September from MarketSmith India"
- COALINDIA.NS (COAL INDIA LTD) score 82.4 — "Stock recommendations for 4 September from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 80.9 — "Stock recommendations for 4 September from MarketSmith India"
- INDIANB.NS (INDIAN BANK) score 80.7 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 4"
- BAC (Bank of America Corporation) score 69.4 — "HDFC Bank Share Price Live Updates: India's balance of payments likely to post $60-65 bn s"
- HDB (HDFC Bank Limited) score 62.2 — "HDFC Bank Share Price Live Updates: India's balance of payments likely to post $60-65 bn s"
- COIN (Coinbase Global, Inc.) score 59.5 — "Nifty, Sensex likely to open higher amid positive global cues"
- IDBI.NS (IDBI BANK LIMITED) score 59.3 — "HDFC Bank Share Price Live Updates: India's balance of payments likely to post $60-65 bn s"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 59.3 — "HDFC Bank Share Price Live Updates: India's balance of payments likely to post $60-65 bn s"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 59.3 — "HDFC Bank Share Price Live Updates: India's balance of payments likely to post $60-65 bn s"
- BOND (PIMCO Active Bond Exchange-Tra) score 56.9 — "Fresh debt supply to provide directional cue for India bonds"
- CHKP (Check Point Software Technolog) score 47.3 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 4"
- TECHM.NS (TECH MAHINDRA LIMITED) score 39.3 — "Paluck Technologies, Complete Sports and Management SME shares to list today: GMP signals "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.0 — "Paluck Technologies, Complete Sports and Management SME shares to list today: GMP signals "
- TECH (Bio-Techne Corp) score 39.0 — "Paluck Technologies, Complete Sports and Management SME shares to list today: GMP signals "
- OHI (Omega Healthcare Investors, In) score 36.9 — "Tesla investors await updates on Cybercab robotaxi touted as the ‘future of transport’"
- LTH (Life Time Group Holdings, Inc.) score 32.6 — "Paluck Technologies, Complete Sports and Management SME shares to list today: GMP signals "
- 301077.SZ (CHINASTARS) score 26.4 — "U.S.-Venezuela Oil Deal Threatens China’s Oil-Backed Loans"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.5 — "Penny stock under 10 rupees: Upper circuit — Leather share jumps 74% in 4 sessions | Back-"
- PCJEWELLER.NS (PC JEWELLER LTD) score 19.4 — "Priority Jewels IPO listing today: Will the jewellery maker deliver gains? Here's what GMP"
- NVDA (NVIDIA Corporation) score 15.8 — "Nvidia takes back control of the AI trade as Big Tech nears record highs"
- JIOFIN.BO (Jio Financial Services Limited) score 15.4 — "JM Financial initiates coverage on OnEMI Technology with Buy call, sees 28% upside"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 13.4 — "Retail sugar price drops 3.85% to ₹62.57/kg in a week: Govt data"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.9 — "Adani Ports’ rising volumes, overseas push to keep growth story intact"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 10.7 — "Stocks in focus: IEX, PowerGrid, RVNL, APSEZ, Bharat Forge, HEG, brokerage stocks,Cipla am"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.4 — "Tata Chemicals shares fall 3% after Kenya orders end to operations. Here’s why"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 10.4 — "Tata Chemicals shares fall 3% after Kenya orders end to operations. Here’s why"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 9.7 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Price Decline Report"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.2 — "TRUMP: I JUST WANT THE WAR ENDED IN UKRAINE"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 8.2 — "JM Financial initiates coverage on OnEMI Technology with Buy call, sees 28% upside"
- MS (Morgan Stanley) score 8.0 — "Cipla slips after Qilu Pembrolizumab deal; Morgan Stanley flags crowded field"
- VT (Vanguard Total World Stock Ind) score 7.2 — "Jindal Worldwide stock hits upper circuit - What's behind the share price jump?"
- META (Meta) score 6.5 — "Gold vs Silver: Which precious metal offers a better bet for investors after the recent co"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.2 — "Eternal, ICICI Bank, 5 other largecap stocks with upside potential of up to 40%. Do you ow"
- DELL (Dell Technologies Inc.) score 4.2 — "Dell’s AI Boom: $95 billion backlog reshapes growth outlook"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 2.3 — "Lenskart shares to rally 40%? Nomura initiates coverage with Buy, says its growth journey "
- HEROMOTOCO.NS (HERO MOTOCORP LIMITED) score 1.9 — "August sales: Hero MotoCorp’s weak show no reason to ring alarm bells on auto sector slowd"
- DKS (Dick's Sporting Goods Inc) score 0.7 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- MRNA (Moderna, Inc.) score 0.5 — "Can Wolfe’s upgrade push Moderna stock higher?"
- VOLTAS.NS (VOLTAS LTD) score 0.1 — "Voltas reported strong growth in June quarter, but failed to impress"

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