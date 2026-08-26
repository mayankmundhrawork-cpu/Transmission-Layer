# Transmission Layer — board brief · 2026-08-26 07:07Z

data as of **2026-08-26** · 98 series · 11 red / 36 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.266, 2d in regime; vol-pct 0.157, breadth-off 0.375, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.28, corr60 -0.4, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.77, corr60 0.87, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.12, corr60 0.35, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.03, corr60 -0.08, last shift 2026-07-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.65, corr60 -0.83, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [INVERTED] **dxy_inr_channel** — corr20 -0.27, corr60 -0.12, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.08, corr60 -0.1, last shift 2026-06-30. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.33, corr60 0.2, last shift 2026-07-08. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** dyn_bond → gbp_usd: leads 1d (ccf 0.3, β 0.4323, p 0.0); driver zc 1.69 → expected 0.222%. Type hit-rate 0.816 (n=2276).
- **SETUP** dyn_bond → eur_usd: leads 1d (ccf 0.25, β 0.3641, p 5e-05); driver zc 1.69 → expected 0.187%. Type hit-rate 0.816 (n=2276).
- Track record · residual_reversion: hit-rate **0.503** (n=1116) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.816** (n=2276) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.91] dyn_dks ↓
- dyn_dks [EQUITIES]: last 124.40, z20 -7.91, zc -11.45, resid-z -1.12 [moved], 1d -30.63%, |z20|=7.91; 1y-pct=0
- **Mechanism**: dyn_dks ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Dick’s Sporting Goods slumps after earnings miss: What’s next? — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/us-stocks/news/dicks-sporting-goods-slumps-after-earnings-miss-whats-next/slideshow/133532630.cms
- Source: Dick’s Sporting Goods’ epic drop hits other footwear giants, as shoppers sour on retro sneakers — MarketWatch Top, 2026-08-25. https://www.marketwatch.com/story/dicks-sporting-goods-stock-is-having-its-worst-day-ever-as-sneakers-arent-selling-without-deeper-discounts-5a868358?mod=mw_rss_topstories
- Source: Dick’s Sporting Goods’ stock is having its worst day ever, as sneakers aren’t selling without deeper discounts — MarketWatch Top, 2026-08-25. https://www.marketwatch.com/story/dicks-sporting-goods-stock-is-having-its-worst-day-ever-as-sneakers-arent-selling-without-deeper-discounts-5a868358?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-01 (d=0.0), 2025-08-15 (d=0.12)

### [AMBER 7.25] cross-asset · 4 series ↑
- brent [COMMODITIES]: last 85.62, z20 -0.59, zc -1.30, resid-z -1.09 [quiet], 1d -3.34%, 1-session move -3.34% ≥ 1.5%
- wti [COMMODITIES]: last 80.49, z20 -0.57, zc -0.93, resid-z -0.76 [quiet], 1d -2.27%, 1-session move -2.27% ≥ 1.5%
- dyn_vt [EQUITIES]: last 160.99, z20 0.57, zc 0.75, resid-z -0.42 [quiet], 1d 0.56%, 1y-pct=98
- dow_jones [INDICES]: last 53572.91, z20 0.30, zc 0.35, resid-z -0.77 [quiet], 1d 0.29%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.959 vs dyn_vt, historically leads by 5d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.944 vs dyn_vt, historically leads by 5d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.835 vs dyn_vt
- Watch next: vix (inverse) — not yet - watch; rho -0.804 vs dyn_vt
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.597 vs dyn_vt, historically leads by 5d
- Source: Indian refiners widen oil search as attacks hurt Russian flows — BusinessLine Mkts, 2026-08-26. https://www.thehindubusinessline.com/markets/commodities/indian-refiners-widen-oil-search-as-attacks-hurt-russian-flows/article71391698.ece
- Source: Oil Prices Fall as Iran-Oman Talks Fuel Hopes of Strait Reopening — OilPrice, 2026-08-26. https://oilprice.com/Latest-Energy-News/World-News/Oil-Prices-Fall-as-Iran-Oman-Talks-Fuel-Hopes-of-Strait-Reopening.html
- Source: Healthcare stock Park Medi World jumps 3%, rises for 5th consecutive session after this capex update | Details here — Mint Markets, 2026-08-26. https://www.livemint.com/market/stock-market-news/healthcare-stock-park-medi-world-jumps-3-rises-for-5th-consecutive-session-after-this-capex-update-details-here-11787724749621.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-16 (d=0.36), 2025-10-21 (d=0.5)

### [RED 6.59] cross-asset · 4 series ↑
- dyn_mrna [EQUITIES]: last 158.87, z20 2.93, zc 1.12, resid-z -0.68 [quiet], 1d 14.39%, |z20|=2.93; 1y-pct=100
- dyn_coin [EQUITIES]: last 187.19, z20 2.66, zc 0.81, resid-z -0.65 [quiet], 1d 4.30%, |z20|=2.66
- btc_usd [CRYPTO]: last 79045.63, z20 2.23, zc 0.16, resid-z -0.35 [quiet], 1d 0.57%, |z20|=2.23
- eth_usd [CRYPTO]: last 2465.44, z20 1.96, zc 0.24, resid-z -0.72 [quiet], 1d 1.01%, |z20|=1.96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-11 (z-distance 1.01).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.446 via btc_usd, z 1.75, reacted)
- **India receivers**: nifty_metal (rho 0.446, z 1.75)
- Source: Sensex today | Stock Market Live: Sensex flat, Nifty slips as global cues improve — BusinessLine Mkts, 2026-08-26. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-26th-august-2026/article71389623.ece
- Source: Global Market: China, Hong Kong stocks rise as AI rebound boosts investor sentiment — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-hong-kong-stocks-rise-as-ai-rebound-boosts-investor-sentiment/articleshow/133531612.cms
- Source: Can Wolfe’s upgrade push Moderna stock higher? — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/us-stocks/news/can-wolfes-upgrade-push-moderna-stock-higher/slideshow/133531310.cms
- Historical analogues: 2025-08-11 (d=1.01), 2026-05-05 (d=1.19), 2024-11-21 (d=1.22)

### [RED 6.53] commodities · 2 series ↑
- corn [COMMODITIES]: last 527.25, z20 3.69, zc 4.19, resid-z 1.17 [moved], 1d 5.34%, |z20|=3.69; 1y-pct=100
- wheat [COMMODITIES]: last 710.25, z20 2.81, zc 2.36, resid-z 0.20 [moved], 1d 3.61%, |z20|=2.81; 1y-pct=100
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Govt lifts wheat export ban with immediate effect — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/economy/agri-business/govt-lifts-wheat-export-ban-with-immediate-effect/article71384020.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [AMBER 5.54] fx · 3 series ↑
- aud_usd [FX]: last 0.72, z20 2.23, zc 0.73, resid-z -0.32 [quiet], 1d 0.38%, |z20|=2.23
- eur_usd [FX]: last 1.17, z20 1.54, zc 0.07, resid-z -0.29 [quiet], 1d 0.03%, |z20|=1.54
- usd_mxn [FX]: last 16.93, z20 -1.30, zc -0.21, resid-z 0.38 [quiet], 1d -0.08%, 1y-pct=0
- **Mechanism**: fx · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.511 via aud_usd, z 2.38, reacted)
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.603 vs aud_usd, historically leads by 1d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.567 vs eur_usd
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.503 vs eur_usd
- **India receivers**: dyn_muthootfin_ns (rho 0.511, z 2.38)
- Source: Euro zone yields dip from multi-year highs as oil falls on Iran sanctions — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/us-stocks/news/euro-zone-yields-dip-from-multi-year-highs-as-oil-falls-on-iran-sanctions/articleshow/133512503.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-02 (d=0.26), 2025-08-15 (d=0.26)

### [RED 5.32] dyn_adanient_bo ↑
- dyn_adanient_bo [EQUITIES]: last 3128.00, z20 3.32, zc 0.26, resid-z 1.77 [unexplained], 1d 0.69%, |z20|=3.32
- **Mechanism**: dyn_adanient_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.485 via dyn_adanient_bo, z -0.64, quiet); nifty_midcap_100 (rho 0.463 via dyn_adanient_bo, z 1.51, reacted); dyn_indusindbk_bo (rho 0.442 via dyn_adanient_bo, z -1.12, reacted)
- **India receivers**: nifty_50 (rho 0.485, z -0.64); nifty_midcap_100 (rho 0.463, z 1.51); dyn_indusindbk_bo (rho 0.442, z -1.12)
- Source: Adani Ports or Gujarat Pipavav: Which stock benefits more from Gujarat concession extensions? — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/stocks/news/adani-ports-or-gujarat-pipavav-which-stock-benefits-more-from-gujarat-concession-extensions/articleshow/133532117.cms
- Source: Gautam Adani's Adani Energy Solutions wins  ₹4,700 crore transmission project in Maharashtra | shares rise — Mint Markets, 2026-08-26. https://www.livemint.com/market/stock-market-news/gautam-adanis-adani-energy-solutions-wins-rs-4-700-crore-transmission-project-in-maharashtra-shares-rise-11787717367517.html
- Source: Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Stock Details — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/adani-ports-sez-share-price-live-updates-26-aug-2026/liveblog/133528313.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [AMBER 4.99] cross-asset · 2 series ↓
- dyn_techm_ns [EQUITIES]: last 1569.90, z20 -2.16, zc -1.24, resid-z 0.44 [quiet], 1d -1.88%, |z20|=2.16
- nifty_it [INDICES]: last 30363.45, z20 -1.60, zc -0.92, resid-z 0.04 [quiet], 1d -1.33%, |z20|=1.60
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.52).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tataelxsi_ns (rho 0.605 via nifty_it, z -1.37, reacted); dyn_tatatech_ns (rho 0.509 via nifty_it, z -0.43, quiet); nifty_50 (rho 0.478 via nifty_it, z -0.64, quiet)
- Watch next: dyn_tatatech_ns (co-move) — not yet - watch; rho 0.509 vs nifty_it, historically leads by 3d
- **India receivers**: dyn_tataelxsi_ns (rho 0.605, z -1.37); dyn_tatatech_ns (rho 0.509, z -0.43); nifty_50 (rho 0.478, z -0.64)
- Source: Tech Mahindra Share Price Live Updates: Tech Mahindra's Daily Performance — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tech-mahindra-stock-price-live-updates-26-aug-2026/liveblog/133527928.cms
- Historical analogues: 2025-12-30 (d=0.52), 2025-08-13 (d=0.76), 2026-01-06 (d=0.77)

### [RED 4.93] dyn_idbi_ns ↑
- dyn_idbi_ns [EQUITIES]: last 92.95, z20 4.93, zc 1.65, resid-z -0.32 [moved], 1d 5.25%, |z20|=4.93
- **Mechanism**: dyn_idbi_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.389 via dyn_idbi_ns, z 2.38, reacted)
- **India receivers**: dyn_muthootfin_ns (rho 0.389, z 2.38)
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-19 (d=0.01), 2025-09-30 (d=0.06)

## Watchlist (below surfacing floor)
midcap_largecap_ratio ↑ (4.54), natgas ↑ (4.51), dyn_muthootfin_ns ↑ (4.38), dyn_bond ↑ (4.33), comex_gold ↑ (3.83), comex_copper ↑ (3.6), rates · 2 series ↑ (3.39), dyn_karurvysya_ns ↑ (3.37), dyn_lenskart_ns ↑ (3.29), dyn_stylebaaza_ns ↑ (3.12), gold_silver_ratio ↑ (3.11), dyn_tech ↑ (2.99)

## India macro
- nifty_50: 24282.4004 (1d -0.21%, z20 -0.64, flag none)
- nifty_midcap_100: 64186.1016 (1d 0.04%, z20 1.51, flag amber)
- usd_inr: 95.4020 (1d -0.34%, z20 -0.36, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6433 (1d 0.25%, z20 1.54, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 85.0 — "IndusInd Bank Share Price Live Updates: IndusInd Bank's Current Price and Market Performan"
- INOXINDIA.NS (INOX INDIA LIMITED) score 78.8 — "Coal India Share Price Live Updates: Coal India  Experiences Slight Decrease"
- COALINDIA.NS (COAL INDIA LTD) score 77.6 — "Coal India Share Price Live Updates: Coal India  Experiences Slight Decrease"
- BAC (Bank of America Corporation) score 76.6 — "IndusInd Bank Share Price Live Updates: IndusInd Bank's Current Price and Market Performan"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 76.2 — "Coal India Share Price Live Updates: Coal India  Experiences Slight Decrease"
- HDB (HDFC Bank Limited) score 71.5 — "IndusInd Bank Share Price Live Updates: IndusInd Bank's Current Price and Market Performan"
- IDBI.NS (IDBI BANK LIMITED) score 65.8 — "IndusInd Bank Share Price Live Updates: IndusInd Bank's Current Price and Market Performan"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 65.8 — "IndusInd Bank Share Price Live Updates: IndusInd Bank's Current Price and Market Performan"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 65.8 — "IndusInd Bank Share Price Live Updates: IndusInd Bank's Current Price and Market Performan"
- BOND (PIMCO Active Bond Exchange-Tra) score 62.7 — "Yes, Federal, RBL put dollar bond plans on hold"
- TECHM.NS (TECH MAHINDRA LIMITED) score 55.2 — "HCL Tech Share Price Live Updates: HCL Tech Market Movement"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 54.2 — "HCL Tech Share Price Live Updates: HCL Tech Market Movement"
- TECH (Bio-Techne Corp) score 54.1 — "HCL Tech Share Price Live Updates: HCL Tech Market Movement"
- COIN (Coinbase Global, Inc.) score 51.5 — "Global Market: Ueda’s Jackson Hole absence puts focus on BOJ’s September rate decision"
- OHI (Omega Healthcare Investors, In) score 46.8 — "Gold consolidates after 5-day rally as investors eye Fed rate clues"
- LTH (Life Time Group Holdings, Inc.) score 34.0 — "Global Market: China, Hong Kong stocks rise as AI rebound boosts investor sentiment"
- CHKP (Check Point Software Technolog) score 31.9 — "ABH Healthcare IPO Day 3: Issue booked 83% so far. Check GMP, issue details"
- 301077.SZ (CHINASTARS) score 24.5 — "Global Market: China, Hong Kong stocks rise as AI rebound boosts investor sentiment"
- NVDA (NVIDIA Corporation) score 23.2 — "Nasdaq futures fall before Nvidia, oil declines: Markets wrap"
- JIOFIN.BO (Jio Financial Services Limited) score 20.1 — "ONGC Share Price Live Updates: ONGC's Financial Snapshot"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 18.6 — "Pernia’s Pop-Up Studio parent Purple Style Labs sets IPO price band at Rs 546–575; subscri"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 17.4 — "TRUMP ADMINISTRATION HAS SENT TO CONGRESS AGREEMENT ON CIVIL NUCLEAR ENERGY WITH SAUDI ARA"
- MS (Morgan Stanley) score 16.8 — "Stanley Druckenmiller leads doubters who think Bessent's bond ploys will fail"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.6 — "Bajaj Finance Share Price Live Updates: Bajaj Finance's Performance Snapshot"
- PCJEWELLER.NS (PC JEWELLER LTD) score 16.0 — "Shankesh Jewellers, Sunshine Pictures make a decent debut with 2% listing gains"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 14.8 — "ONGC Share Price Live Updates: ONGC's Financial Snapshot"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 11.4 — "Adani Ent Share Price Live Updates: Adani Ent. Stock Details"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.2 — "Tata Consumer Share Price Live Updates: Tata Consumer's Price Movement Signals Weakness"
- META (Meta) score 10.0 — "Hindustan Copper OFS opens for retail investors today. Should you apply in the metals majo"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.9 — "Tata Consumer Share Price Live Updates: Tata Consumer's Price Movement Signals Weakness"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 8.0 — "ICICI Bank Share Price Live Updates: ICICI Bank Shows Strong Market Performance"
- VT (Vanguard Total World Stock Ind) score 7.8 — "Healthcare stock Park Medi World jumps 3%, rises for 5th consecutive session after this ca"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 6.8 — "Coal India Share Price Live Updates: Coal India  Experiences Slight Decrease"
- JUSTDIAL.BO (JUST DIAL LTD.) score 6.5 — "U.S. HOME PRICES BEAT EXPECTATIONS IN JUNE U.S. 20-city home prices rose 0.2% month-over-m"
- DKS (Dick's Sporting Goods Inc) score 5.5 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.4 — "From IPO mockery to Rs 1 lakh crore m-cap: Why investors are still betting on Lenskart’s v"
- MRNA (Moderna, Inc.) score 4.2 — "Can Wolfe’s upgrade push Moderna stock higher?"
- VOLTAS.NS (VOLTAS LTD) score 0.7 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.1 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.1 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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