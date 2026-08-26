# Transmission Layer — board brief · 2026-08-26 09:00Z

data as of **2026-08-26** · 98 series · 11 red / 37 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.205, 2d in regime; vol-pct 0.161, breadth-off 0.25, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.31, corr60 -0.4, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.77, corr60 0.86, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.15, corr60 0.36, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.0, corr60 -0.08, last shift 2026-07-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.65, corr60 -0.83, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [INVERTED] **dxy_inr_channel** — corr20 -0.25, corr60 -0.12, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.08, corr60 -0.1, last shift 2026-06-30. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.3, corr60 0.2, last shift 2026-07-08. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** dyn_bond → gbp_usd: leads 1d (ccf 0.3, β 0.4317, p 0.0); driver zc 1.69 → expected 0.221%. Type hit-rate 0.816 (n=2276).
- **SETUP** dyn_bond → eur_usd: leads 1d (ccf 0.25, β 0.3644, p 5e-05); driver zc 1.69 → expected 0.187%. Type hit-rate 0.816 (n=2276).
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

### [AMBER 7.44] cross-asset · 4 series ↑
- brent [COMMODITIES]: last 84.85, z20 -0.77, zc -1.63, resid-z -1.09 [moved], 1d -4.21%, 1-session move -4.21% ≥ 1.5%
- wti [COMMODITIES]: last 79.80, z20 -0.77, zc -1.27, resid-z -0.76 [quiet], 1d -3.11%, 1-session move -3.11% ≥ 1.5%
- dyn_vt [EQUITIES]: last 160.99, z20 0.57, zc 0.75, resid-z -0.42 [quiet], 1d 0.56%, 1y-pct=98
- dow_jones [INDICES]: last 53572.91, z20 0.30, zc 0.35, resid-z -0.77 [quiet], 1d 0.29%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.959 vs dyn_vt, historically leads by 5d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.944 vs dyn_vt, historically leads by 5d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.835 vs dyn_vt
- Watch next: vix (inverse) — not yet - watch; rho -0.812 vs dyn_vt
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.597 vs dyn_vt, historically leads by 5d
- Source: Oil prices extend slide as Iran and Oman eye temporary Hormuz deal — MarketWatch Top, 2026-08-26. https://www.marketwatch.com/story/oil-prices-extend-slide-as-iran-and-oman-eye-temporary-hormuz-deal-a86a86bf?mod=mw_rss_topstories
- Source: Japan to Unveil New Oil Diversification Strategy — OilPrice, 2026-08-26. https://oilprice.com/Latest-Energy-News/World-News/Japan-to-Unveil-New-Oil-Diversification-Strategy.html
- Source: Iran’s Tanker Blacklist Raises New Risks for Gulf Oil — OilPrice, 2026-08-26. https://oilprice.com/Latest-Energy-News/World-News/Irans-Tanker-Blacklist-Raises-New-Risks-for-Gulf-Oil.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-16 (d=0.36), 2025-10-21 (d=0.5)

### [RED 6.59] commodities · 2 series ↑
- corn [COMMODITIES]: last 528.50, z20 3.76, zc 4.39, resid-z 1.17 [moved], 1d 5.59%, |z20|=3.76; 1y-pct=100
- wheat [COMMODITIES]: last 716.00, z20 3.12, zc 2.91, resid-z 0.20 [moved], 1d 4.45%, |z20|=3.12; 1y-pct=100
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Govt lifts wheat export ban with immediate effect — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/economy/agri-business/govt-lifts-wheat-export-ban-with-immediate-effect/article71384020.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [RED 6.59] cross-asset · 4 series ↑
- dyn_mrna [EQUITIES]: last 158.87, z20 2.93, zc 1.12, resid-z -0.68 [quiet], 1d 14.39%, |z20|=2.93; 1y-pct=100
- dyn_coin [EQUITIES]: last 187.19, z20 2.66, zc 0.81, resid-z -0.65 [quiet], 1d 4.30%, |z20|=2.66
- btc_usd [CRYPTO]: last 78689.04, z20 2.17, zc 0.04, resid-z -0.37 [quiet], 1d 0.16%, |z20|=2.17
- eth_usd [CRYPTO]: last 2456.02, z20 1.91, zc 0.13, resid-z -0.70 [quiet], 1d 0.53%, |z20|=1.91
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-11 (z-distance 0.99).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.44 via btc_usd, z 2.18, reacted)
- **India receivers**: nifty_metal (rho 0.44, z 2.18)
- Source: Global Market: Fiscal dominance debate takes centre stage as government debt mounts — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-fiscal-dominance-debate-takes-centre-stage-as-government-debt-mounts/articleshow/133533749.cms
- Source: Sensex today | Stock Market Live: Sensex flat, Nifty slips as global cues improve — BusinessLine Mkts, 2026-08-26. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-26th-august-2026/article71389623.ece
- Source: Global Market: China, Hong Kong stocks rise as AI rebound boosts investor sentiment — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-hong-kong-stocks-rise-as-ai-rebound-boosts-investor-sentiment/articleshow/133531612.cms
- Historical analogues: 2025-08-11 (d=0.99), 2026-05-05 (d=1.18), 2024-10-31 (d=1.19)

### [RED 5.97] cross-asset · 3 series ↑
- comex_copper [COMMODITIES]: last 6.83, z20 2.65, zc 0.81, resid-z 0.99 [quiet], 1d 1.78%, |z20|=2.65; 1y-pct=100; co-occur[metal_copper] suppressed: channel WEAK
- dax [INDICES]: last 26273.46, z20 0.60, zc 0.04, resid-z 0.36 [quiet], 1d 0.03%, 1y-pct=97
- stoxx_50 [INDICES]: last 6470.19, z20 0.07, zc 0.30, resid-z -0.53 [quiet], 1d 0.23%, 1y-pct=96
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-25 (z-distance 0.44).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.521 via dax, z 1.6, reacted)
- Watch next: sp500 (co-move) — not yet - watch; rho 0.623 vs stoxx_50, historically leads by 5d
- Watch next: vix (inverse) — not yet - watch; rho -0.603 vs stoxx_50, historically leads by 5d
- Watch next: gold_silver_ratio (inverse) — not yet - watch; rho -0.598 vs comex_copper, historically leads by 1d
- Watch next: ftse_100 (co-move) — not yet - watch; rho 0.596 vs dax, historically leads by 4d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.584 vs stoxx_50, historically leads by 5d
- **India receivers**: nifty_midcap_100 (rho 0.521, z 1.6)
- Source: Hindustan Copper share price in focus as OFS opens for retail investors today. Should you apply? — Mint Markets, 2026-08-26. https://www.livemint.com/market/stock-market-news/hindustan-copper-share-price-in-focus-as-ofs-opens-for-retail-investors-today-should-you-apply-11787713785032.html
- Source: Hindustan Copper shares in focus as OFS opens for retail investors. Here are all the details — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/stocks/news/hindustan-copper-shares-in-focus-as-ofs-opens-for-retail-investors-here-are-all-the-details/articleshow/133528239.cms
- Source: Hindustan Copper OFS opens for retail investors today. Should you apply in the metals major's offer? — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/stocks/news/hindustan-copper-ofs-opens-for-retail-investors-today-should-you-apply-in-the-metals-majors-offer/articleshow/133527323.cms
- Historical analogues: 2025-07-25 (d=0.44), 2025-10-14 (d=0.48), 2024-10-03 (d=0.55)

### [RED 5.56] dyn_adanient_bo ↑
- dyn_adanient_bo [EQUITIES]: last 3136.50, z20 3.56, zc 0.37, resid-z 0.62 [quiet], 1d 0.97%, |z20|=3.56
- **Mechanism**: dyn_adanient_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.482 via dyn_adanient_bo, z -0.7, quiet); nifty_midcap_100 (rho 0.463 via dyn_adanient_bo, z 1.6, reacted); dyn_indusindbk_bo (rho 0.436 via dyn_adanient_bo, z -1.77, reacted)
- **India receivers**: nifty_50 (rho 0.482, z -0.7); nifty_midcap_100 (rho 0.463, z 1.6); dyn_indusindbk_bo (rho 0.436, z -1.77)
- Source: Adani Ports or Gujarat Pipavav: Which stock benefits more from Gujarat concession extensions? — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/stocks/news/adani-ports-or-gujarat-pipavav-which-stock-benefits-more-from-gujarat-concession-extensions/articleshow/133532117.cms
- Source: Gautam Adani's Adani Energy Solutions wins  ₹4,700 crore transmission project in Maharashtra | shares rise — Mint Markets, 2026-08-26. https://www.livemint.com/market/stock-market-news/gautam-adanis-adani-energy-solutions-wins-rs-4-700-crore-transmission-project-in-maharashtra-shares-rise-11787717367517.html
- Source: Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Stock Details — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/adani-ports-sez-share-price-live-updates-26-aug-2026/liveblog/133528313.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [AMBER 5.55] fx · 3 series ↑
- aud_usd [FX]: last 0.72, z20 2.23, zc 0.74, resid-z 0.89 [quiet], 1d 0.39%, |z20|=2.23
- eur_usd [FX]: last 1.17, z20 1.58, zc 0.14, resid-z 0.27 [quiet], 1d 0.05%, |z20|=1.58
- usd_mxn [FX]: last 16.93, z20 -1.33, zc -0.30, resid-z -0.25 [quiet], 1d -0.11%, 1y-pct=0
- **Mechanism**: fx · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.511 via aud_usd, z 2.4, reacted)
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.603 vs aud_usd, historically leads by 1d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.567 vs eur_usd
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.503 vs eur_usd
- **India receivers**: dyn_muthootfin_ns (rho 0.511, z 2.4)
- Source: Euro zone yields dip from multi-year highs as oil falls on Iran sanctions — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/us-stocks/news/euro-zone-yields-dip-from-multi-year-highs-as-oil-falls-on-iran-sanctions/articleshow/133512503.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-02 (d=0.26), 2025-08-15 (d=0.26)

### [RED 5.16] dyn_idbi_ns ↑
- dyn_idbi_ns [EQUITIES]: last 93.38, z20 5.16, zc 1.80, resid-z 1.90 [unexplained], 1d 5.74%, |z20|=5.16
- **Mechanism**: dyn_idbi_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.388 via dyn_idbi_ns, z 2.4, reacted); nifty_metal (rho 0.366 via dyn_idbi_ns, z 2.18, reacted)
- **India receivers**: dyn_muthootfin_ns (rho 0.388, z 2.4); nifty_metal (rho 0.366, z 2.18)
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-19 (d=0.01), 2025-09-30 (d=0.06)

## Watchlist (below surfacing floor)
cross-asset · 2 series ↓ (4.84), midcap_largecap_ratio ↑ (4.65), dyn_muthootfin_ns ↑ (4.4), dyn_bond ↑ (4.33), natgas ↑ (4.32), comex_gold ↑ (3.81), dyn_karurvysya_ns ↑ (3.8), dyn_icicigi_bo ↓ (3.42), rates · 2 series ↑ (3.39), dyn_lenskart_ns ↑ (3.29), dyn_stylebaaza_ns ↑ (3.22), gold_silver_ratio ↑ (3.15)

## India macro
- nifty_50: 24271.9492 (1d -0.26%, z20 -0.70, flag none)
- nifty_midcap_100: 64219.1484 (1d 0.09%, z20 1.60, flag amber)
- usd_inr: 95.4020 (1d -0.34%, z20 -0.36, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6458 (1d 0.35%, z20 1.65, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 86.5 — "Nifty 50 stuck below 25,000: Is the IPO boom this year a reason behind the poor show of th"
- INOXINDIA.NS (INOX INDIA LIMITED) score 81.4 — "Coal India Share Price Live Updates: Coal India  Price and Returns Analysis"
- COALINDIA.NS (COAL INDIA LTD) score 80.2 — "Coal India Share Price Live Updates: Coal India  Price and Returns Analysis"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 78.9 — "Coal India Share Price Live Updates: Coal India  Price and Returns Analysis"
- BAC (Bank of America Corporation) score 77.2 — "Dmart owner eyes debt market comeback after 7-year hiatus, bankers say"
- HDB (HDFC Bank Limited) score 72.2 — "Dmart owner eyes debt market comeback after 7-year hiatus, bankers say"
- IDBI.NS (IDBI BANK LIMITED) score 66.6 — "Dmart owner eyes debt market comeback after 7-year hiatus, bankers say"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 66.6 — "Dmart owner eyes debt market comeback after 7-year hiatus, bankers say"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 66.6 — "Dmart owner eyes debt market comeback after 7-year hiatus, bankers say"
- BOND (PIMCO Active Bond Exchange-Tra) score 61.6 — "Yes, Federal, RBL put dollar bond plans on hold"
- TECHM.NS (TECH MAHINDRA LIMITED) score 54.2 — "HCL Tech Share Price Live Updates: HCL Tech Market Movement"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 53.2 — "HCL Tech Share Price Live Updates: HCL Tech Market Movement"
- TECH (Bio-Techne Corp) score 53.2 — "HCL Tech Share Price Live Updates: HCL Tech Market Movement"
- COIN (Coinbase Global, Inc.) score 51.6 — "Global Market: Fiscal dominance debate takes centre stage as government debt mounts"
- OHI (Omega Healthcare Investors, In) score 45.9 — "Gold consolidates after 5-day rally as investors eye Fed rate clues"
- LTH (Life Time Group Holdings, Inc.) score 33.3 — "Global Market: China, Hong Kong stocks rise as AI rebound boosts investor sentiment"
- CHKP (Check Point Software Technolog) score 32.3 — "Madhur Knit Crafts IPO Day 3: Issue booked 55% so far. GMP hints 16% listing pop. Check ke"
- 301077.SZ (CHINASTARS) score 24.1 — "Global Market: China, Hong Kong stocks rise as AI rebound boosts investor sentiment"
- NVDA (NVIDIA Corporation) score 22.8 — "Nasdaq futures fall before Nvidia, oil declines: Markets wrap"
- JIOFIN.BO (Jio Financial Services Limited) score 19.7 — "ONGC Share Price Live Updates: ONGC's Financial Snapshot"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 18.3 — "Pernia’s Pop-Up Studio parent Purple Style Labs sets IPO price band at Rs 546–575; subscri"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 17.1 — "TRUMP ADMINISTRATION HAS SENT TO CONGRESS AGREEMENT ON CIVIL NUCLEAR ENERGY WITH SAUDI ARA"
- MS (Morgan Stanley) score 16.5 — "Stanley Druckenmiller leads doubters who think Bessent's bond ploys will fail"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.3 — "Bajaj Finance Share Price Live Updates: Bajaj Finance's Performance Snapshot"
- PCJEWELLER.NS (PC JEWELLER LTD) score 15.7 — "Shankesh Jewellers, Sunshine Pictures make a decent debut with 2% listing gains"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 14.6 — "ONGC Share Price Live Updates: ONGC's Financial Snapshot"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 13.2 — "Adani Ent Share Price Live Updates: Adani Enterprises  Market Performance"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.0 — "Tata Consumer Share Price Live Updates: Tata Consumer's Price Movement Signals Weakness"
- META (Meta) score 9.8 — "Hindustan Copper OFS opens for retail investors today. Should you apply in the metals majo"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.7 — "Tata Consumer Share Price Live Updates: Tata Consumer's Price Movement Signals Weakness"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.8 — "ICICI Bank Share Price Live Updates: ICICI Bank Shows Strong Market Performance"
- VT (Vanguard Total World Stock Ind) score 7.7 — "Healthcare stock Park Medi World jumps 3%, rises for 5th consecutive session after this ca"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 7.6 — "Coal India Share Price Live Updates: Coal India  Price and Returns Analysis"
- JUSTDIAL.BO (JUST DIAL LTD.) score 6.4 — "U.S. HOME PRICES BEAT EXPECTATIONS IN JUNE U.S. 20-city home prices rose 0.2% month-over-m"
- DKS (Dick's Sporting Goods Inc) score 5.4 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.3 — "From IPO mockery to Rs 1 lakh crore m-cap: Why investors are still betting on Lenskart’s v"
- MRNA (Moderna, Inc.) score 4.1 — "Can Wolfe’s upgrade push Moderna stock higher?"
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