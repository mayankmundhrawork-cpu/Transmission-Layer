# Transmission Layer — board brief · 2026-08-17 10:47Z

data as of **2026-08-17** · 98 series · 10 red / 36 amber · 8 events surfaced (22 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.117, 2d in regime; vol-pct 0.235, breadth-off 0.0, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.36, corr60 -0.39, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.88, corr60 0.86, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.31, corr60 0.36, last shift 2026-07-01. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.21, corr60 -0.11, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.72, corr60 -0.81, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.1, corr60 -0.12, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.31, corr60 -0.2, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.03, corr60 0.23, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 4.761345828718788e-08)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.49** (n=1117) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.829** (n=2423) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.14] cross-asset · 13 series ↑
- russell_2000 [INDICES]: last 3068.24, z20 1.99, zc 0.43, resid-z 1.16 [quiet], 1d 0.50%, |z20|=1.99; 1y-pct=100
- comex_gold [COMMODITIES]: last 4453.60, z20 1.95, zc 1.29, resid-z -0.69 [quiet], 1d 1.67%, |z20|=1.95; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 65.75, z20 1.70, zc 0.52, resid-z -0.82 [quiet], 1d 1.16%, |z20|=1.70; co-occur[gold_silver] same-direction (channel VALID)
- dyn_vt [EQUITIES]: last 162.24, z20 1.56, zc -0.11, resid-z -0.85 [quiet], 1d -0.09%, 1y-pct=99
- dyn_nvda [EQUITIES]: last 225.16, z20 1.55, zc -0.03, resid-z -0.34 [quiet], 1d -0.06%, 1y-pct=98
- nasdaq_100 [INDICES]: last 30050.44, z20 1.53, zc -0.09, resid-z 0.20 [quiet], 1d -0.11%, |z20|=1.53; 1y-pct=95
- comex_copper [COMMODITIES]: last 6.70, z20 1.52, zc 0.66, resid-z 0.00 [quiet], 1d 1.48%, |z20|=1.52; 1y-pct=99
- sp500 [INDICES]: last 7786.01, z20 1.42, zc -0.21, resid-z 0.78 [quiet], 1d -0.17%, 1y-pct=99
- stoxx_50 [INDICES]: last 6561.93, z20 1.35, zc 0.46, resid-z -0.09 [quiet], 1d 0.34%, 1y-pct=100
- dax [INDICES]: last 26464.97, z20 1.29, zc 0.13, resid-z 0.65 [quiet], 1d 0.09%, 1y-pct=100
- gold_silver_ratio [DERIVED]: last 67.74, z20 -1.06, zc n/a, resid-z n/a [quiet], 1d 0.50%, GSR<75 (extreme low)
- dow_jones [INDICES]: last 53733.51, z20 0.88, zc -0.27, resid-z -0.15 [quiet], 1d -0.20%, 1y-pct=96
- cac_40 [INDICES]: last 8628.98, z20 0.60, zc -0.13, resid-z -0.29 [quiet], 1d -0.09%, 1y-pct=96
- **Mechanism**: cross-asset · 13 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-11-26 (z-distance 0.92).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.512 via comex_silver, z 0.93, quiet); nifty_midcap_100 (rho 0.492 via dax, z 1.0, reacted); nifty_fmcg (rho -0.49 via dyn_nvda, z -2.91, reacted); nifty_50 (rho 0.486 via cac_40, z -0.13, quiet); dyn_stylebaaza_ns (rho -0.361 via gold_silver_ratio, z 2.57, reacted)
- Watch next: brent (inverse) — not yet - watch; rho -0.646 vs dow_jones, historically leads by 3d
- Watch next: ust_10y (inverse) — not yet - watch; rho -0.624 vs russell_2000, historically leads by 1d
- Watch next: wti (inverse) — not yet - watch; rho -0.608 vs dow_jones, historically leads by 2d
- Watch next: tips_10y_real (inverse) — not yet - watch; rho -0.579 vs russell_2000, historically leads by 5d
- Watch next: vix (inverse) — not yet - watch; rho -0.747 vs russell_2000
- **India receivers**: nifty_metal (rho 0.512, z 0.93); nifty_midcap_100 (rho 0.492, z 1.0); nifty_fmcg (rho -0.49, z -2.91); nifty_50 (rho 0.486, z -0.13)
- Source: Neighbors in rural Texas county are not happy about Elon Musk’s plan to erect world’s largest building — MarketWatch Top, 2026-08-17. https://www.marketwatch.com/story/neighbors-in-rural-texas-county-are-not-happy-about-elon-musks-plan-to-erect-worlds-largest-building-2183edcb?mod=mw_rss_topstories
- Source: Sky Gold & Diamonds added to MSCI India domestic small cap index — BusinessLine Mkts, 2026-08-17. https://www.thehindubusinessline.com/companies/sky-gold-diamonds-added-to-msci-india-domestic-small-cap-index/article71355432.ece
- Source: Gold Rate Today, Aug 17: Gold prices up in Delhi, Mumbai, Kolkata, Bengaluru, Ahmedabad — BusinessLine Mkts, 2026-08-17. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-mumbai-chennai-ahmedabad-delhi-hyderabad-bengaluru-kolkata-gold-rates-august-17-2026/article71355125.ece
- Historical analogues: 2024-11-26 (d=0.92), 2025-10-31 (d=1.01), 2024-10-15 (d=1.11)

### [RED 6.71] fx · 4 series ↑
- aud_usd [FX]: last 0.71, z20 3.04, zc 2.07, resid-z 1.91 [unexplained], 1d 0.91%, |z20|=3.04
- usd_mxn [FX]: last 17.00, z20 -1.98, zc -0.42, resid-z -0.35 [quiet], 1d -0.16%, |z20|=1.98; 1y-pct=0
- gbp_usd [FX]: last 1.36, z20 1.88, zc 1.22, resid-z 1.08 [quiet], 1d 0.51%, |z20|=1.88
- eur_usd [FX]: last 1.16, z20 1.72, zc 1.57, resid-z 1.43 [moved], 1d 0.52%, |z20|=1.72
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.553 via usd_mxn, z -0.87, quiet); eur_inr (rho 0.483 via gbp_usd, z 3.56, reacted); dyn_icicigi_bo (rho -0.419 via gbp_usd, z -0.43, quiet); nifty_midcap_100 (rho -0.355 via usd_mxn, z 1.0, reacted)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.507 vs aud_usd, historically leads by 5d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.515 vs eur_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.553, z -0.87); eur_inr (rho 0.483, z 3.56); dyn_icicigi_bo (rho -0.419, z -0.43); nifty_midcap_100 (rho -0.355, z 1.0)
- Source: Global Market: Euro zone bond yields hover near 15-year highs as Middle East war fuels inflation fears — ET Markets, 2026-08-17. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-bond-yields-hover-near-15-year-highs-as-middle-east-war-fuels-inflation-fears/articleshow/133293555.cms
- Source: Philip R. Lane: The rise in defence spending and the euro area economy — ECB press, 2026-08-17. https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260817~1f9f7149c9.en.pdf
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 5.12] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.63, z20 2.12, zc n/a, resid-z n/a [quiet], 1d 0.37%, 52-wk extreme (pct=99); |z20|=2.12; 1y-pct=99
- **Mechanism**: The midcap_largecap_ratio has reached a 52-week extreme, with a z20 level of 1.77, indicating a significant move. However, the resid_z is None, suggesting that this move is largely priced in by factor exposures. The RISK_ON regime and VALID vix_equity_inverse channel suggest that the market is positioned for a potential drawdown, but the midcap_largecap_ratio's move may not be an anomaly.
- **Gap**: No gap: the midcap_largecap_ratio's move is largely priced in by factor exposures, as indicated by the None resid_z value
- **India take**: The Nifty Midcap 100 index, which has a correlation of 0.531 with the midcap_largecap_ratio, has not yet reacted and is a potential responder. Other Indian transmission candidates like Dyn Bharatcoal NS and Dyn Fincables NS have already reacted.
- Watch next: nifty_midcap_100 (down) — not yet - watch; historically leads by 2d
- **India receivers**: nifty_midcap_100 (rho 0.533, z 1.0); dyn_bharatcoal_ns (rho 0.42, z -1.1); dyn_fincables_ns (rho 0.408, z 2.68); dyn_pcjeweller_ns (rho 0.374, z 0.66)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 4.81] commodities · 2 series ↑
- corn [COMMODITIES]: last 485.25, z20 3.98, zc 4.47, resid-z 1.25 [moved], 1d 5.72%, |z20|=3.98; 1y-pct=100
- wheat [COMMODITIES]: last 683.50, z20 1.22, zc 0.67, resid-z 1.20 [quiet], 1d 1.30%, 1y-pct=99
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_lenskart_ns (rho 0.397 via wheat, z 2.27, reacted)
- Watch next: soybeans (co-move) — not yet - watch; rho 0.718 vs corn
- **India receivers**: dyn_lenskart_ns (rho 0.397, z 2.27)
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [RED 4.57] dyn_stylebaaza_ns ↑
- dyn_stylebaaza_ns [EQUITIES]: last 383.50, z20 2.57, zc 1.37, resid-z 1.69 [unexplained], 1d 5.00%, |z20|=2.57
- **Mechanism**: dyn_stylebaaza_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_pcjeweller_ns (rho 0.439 via dyn_stylebaaza_ns, z 0.66, quiet); dyn_bharatcoal_ns (rho 0.402 via dyn_stylebaaza_ns, z -1.1, reacted); dyn_adanient_bo (rho 0.392 via dyn_stylebaaza_ns, z -0.53, quiet); dyn_fincables_ns (rho 0.376 via dyn_stylebaaza_ns, z 2.68, reacted); nifty_midcap_100 (rho 0.362 via dyn_stylebaaza_ns, z 1.0, reacted)
- **India receivers**: dyn_pcjeweller_ns (rho 0.439, z 0.66); dyn_bharatcoal_ns (rho 0.402, z -1.1); dyn_adanient_bo (rho 0.392, z -0.53); dyn_fincables_ns (rho 0.376, z 2.68)
- Source: Halwasiya buys 45 lakh shares of Baazar Style Retail for ₹163 crore in block deal — BusinessLine Mkts, 2026-08-17. https://www.thehindubusinessline.com/markets/stock-markets/halwasiya-buys-45-lakh-shares-of-baazar-style-retail-for-163-crore-in-block-deal/article71355344.ece
- Source: Baazar Style Retail shares hit 5% upper circuit on reports of Aditya Halwasia buying company shares worth  ₹163 crore — Mint Markets, 2026-08-17. https://www.livemint.com/market/stock-market-news/baazar-style-retail-shares-hit-5-upper-circuit-on-reports-of-aditya-halwasia-buying-company-shares-worth-163-crore-11786948034095.html
- Source: Gold Rises to Near $4,400 as Weak Retail Data Weighs on Dollar — Mint Markets, 2026-08-17. https://www.livemint.com/market/gold-rises-to-near-4-400-as-weak-retail-data-weighs-on-dollar-11786937454532.html
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-04 (d=0.01), 2025-02-20 (d=0.02)

### [AMBER 4.36] dxy ↓
- dxy [FX]: last 99.45, z20 -1.36, zc -0.67, resid-z 0.10 [quiet], 1d -0.22%, 20d range extreme
- **Mechanism**: The recent decline in the US Dollar Index (DXY) may propagate through the metal_copper_channel, a VALID channel, potentially leading to a move in Indian metal equities. The DXY decline, although priced with a small resid_z of 0.1, could still influence global copper prices, which in turn affect Indian metal equities. The VALID gold_silver_comove channel also suggests that monetary metals may co-move, potentially impacting the Indian market.
- **Gap**: No gap: The DXY move is priced with a small resid_z of 0.1, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is likely to be the Indian metal equities, such as Hindalco or Tata Steel, which may react to the potential move in global copper prices. However, the reaction has not occurred yet.
- Watch next: comex_gold (down) — not yet - watch; Historical analogues show a median decline of 1.82% in comex_gold 20 days after a similar DXY decline
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [AMBER 4.07] dyn_tech ↑
- dyn_tech [EQUITIES]: last 72.42, z20 2.07, zc 0.15, resid-z -0.38 [quiet], 1d 0.35%, |z20|=2.07; 1y-pct=100
- **Mechanism**: dyn_tech ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_inoxindia_ns (rho -0.392 via dyn_tech, z -0.16, quiet)
- **India receivers**: dyn_inoxindia_ns (rho -0.392, z -0.16)
- Source: Sensex today | Stock Market LIVE: Sensex down 280 pts as markets close, Nifty down 80 pts to 24,287.65; Infosys, HCL Tech are top losers — BusinessLine Mkts, 2026-08-17. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-17th-august-2026/article71354693.ece
- Source: Top Gainers & Losers on 17 August: NMDC Steel, LG Electronics, BSE, Tata Tech, Infosys, Voltas among top losers — Mint Markets, 2026-08-17. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-17-august-nmdc-steel-lg-electronics-bse-tata-tech-infosys-voltas-among-top-losers-11786961037869.html
- Source: US Stock Market: Tiger Global trims big tech bets, adds AMD and SpaceX in Q2 — ET Markets, 2026-08-17. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stock-market-tiger-global-trims-big-tech-bets-adds-amd-and-spacex-in-q2/articleshow/133286709.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.0), 2025-05-19 (d=0.0)

### [AMBER 3.78] dyn_bac ↑
- dyn_bac [EQUITIES]: last 64.49, z20 1.78, zc 0.43, resid-z -1.09 [quiet], 1d 0.62%, 1y-pct=99
- **Mechanism**: The recent increase in dyn_bac is driven by its historical correlation with global equities, particularly dow_jones and cac_40, which have not yet moved in tandem. The RISK_ON regime and VALID vix_equity_inverse channel suggest a potential for further equity upside, which could propagate to dyn_bac. However, the quiet move in dyn_bac with a low resid_z of -1.09 indicates that the current price move is largely explained by factor exposures and may not be an anomaly.
- **Gap**: No gap: the current price move in dyn_bac is largely explained by factor exposures, as indicated by a low resid_z of -1.09 and a high r2 of 0.107.
- **India take**: The Indian instrument dyn_cupid_ns has already reacted to the move in dyn_bac, given its correlation of 0.374. Further upside in global equities could lead to additional gains in dyn_cupid_ns.
- Watch next: dyn_ms (up) — not yet - watch; historically leads dyn_bac by 2d
- Source: Just 7% of America’s Nuclear Fuel Comes From Home — OilPrice, 2026-08-15. https://oilprice.com/Alternative-Energy/Nuclear-Power/Just-7-of-Americas-Nuclear-Fuel-Comes-From-Home.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

## Watchlist (below surfacing floor)
eur_inr ↑ (3.56), cross-asset · 2 series ↑ (3.45), dyn_lth ↑ (3.3), dyn_tatatech_ns ↑ (3.01), indices · 2 series ↑ (2.95), dyn_coin ↓ (2.95), nifty_fmcg ↓ (2.91), usd_brl ↑ (2.87), dyn_fincables_ns ↑ (2.68), dyn_icicigi_bo ↓ (2.43), indices · 2 series ↑ (2.37), dyn_lenskart_ns ↑ (2.27)

## India macro
- nifty_50: 24287.6504 (1d -0.32%, z20 -0.13, flag none)
- nifty_midcap_100: 63814.1484 (1d 0.05%, z20 1.00, flag amber)
- usd_inr: 95.5920 (1d 0.20%, z20 -0.28, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6274 (1d 0.37%, z20 2.12, flag red)
- Next India prints: NSDL FPI flows T-0d · India trade / CAD data T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 85.8 — "Coal India Share Price Live Updates: Coal India  Price and Volume Overview"
- INOXINDIA.NS (INOX INDIA LIMITED) score 85.2 — "Coal India Share Price Live Updates: Coal India  Price and Volume Overview"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 85.0 — "Coal India Share Price Live Updates: Coal India  Price and Volume Overview"
- INDIANB.NS (INDIAN BANK) score 54.7 — "Indian Oil Giant Secures U.S. License to Return to Venezuela"
- COIN (Coinbase Global, Inc.) score 40.8 — "Global Market: European shares climb despite geopolitical risks; miners lead gains"
- TECHM.NS (TECH MAHINDRA LIMITED) score 38.7 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Stock Performance Today"
- BAC (Bank of America Corporation) score 38.2 — "Yes Bank makes bond market comeback years after AT1 write-off"
- OHI (Omega Healthcare Investors, In) score 37.2 — "Bitcoin hovers near $63K ahead of Fed rate decision as investors assess liquidity outlook"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 37.1 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Stock Performance Today"
- TECH (Bio-Techne Corp) score 36.8 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Stock Performance Today"
- CHKP (Check Point Software Technolog) score 36.3 — "Horizon Industrial Parks’ Rs 2,600 crore IPO opens. Check GMP, price band and other key de"
- HDB (HDFC Bank Limited) score 32.5 — "Yes Bank makes bond market comeback years after AT1 write-off"
- IDBI.NS (IDBI BANK LIMITED) score 30.2 — "Yes Bank makes bond market comeback years after AT1 write-off"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 30.2 — "Yes Bank makes bond market comeback years after AT1 write-off"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 30.1 — "Yes Bank makes bond market comeback years after AT1 write-off"
- LTH (Life Time Group Holdings, Inc.) score 23.5 — "‘I’m running out of time’: I sold my $300,000 rental property at a $75,000 loss. Should I "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 22.0 — "Top Gainers & Losers on 17 August: NMDC Steel, LG Electronics, BSE, Tata Tech, Infosys, Vo"
- BOND (PIMCO Active Bond Exchange-Tra) score 21.8 — "Global Market: Euro zone bond yields hover near 15-year highs as Middle East war fuels inf"
- 301077.SZ (CHINASTARS) score 20.4 — "Global Market: China, Hong Kong stocks rise as chipmakers rally on strong earnings"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 19.9 — "Top Gainers & Losers on 17 August: NMDC Steel, LG Electronics, BSE, Tata Tech, Infosys, Vo"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 17.4 — "India's steel pipe makers tap West Asia as all eyes on energy transport"
- JIOFIN.BO (Jio Financial Services Limited) score 14.4 — "Zaggle Prepaid Ocean Services crashes 20%, hits lower circuit after Q1 PAT declines 33% Yo"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 11.9 — "Coal India Share Price Live Updates: Coal India  Price and Volume Overview"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 10.4 — "Tata Consumer Share Price Live Updates: Tata Consumer's Financial Snapshot"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 10.4 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Trading Update"
- PCJEWELLER.NS (PC JEWELLER LTD) score 9.4 — "Shankesh Jewellers IPO opens tomorrow. GMP, size, review, other details about  ₹367 crore "
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.2 — "Just 7% of America’s Nuclear Fuel Comes From Home"
- MS (Morgan Stanley) score 6.7 — "Tata Motors PV shares fall 5% after weak Q1 results. What are Morgan Stanley, Nomura, othe"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 6.6 — "Cement makers face a forgettable H1FY27 as prices weaken and costs rise"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.0 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ News"
- NVDA (NVIDIA Corporation) score 5.8 — "NVDA - NVIDIA EYES $3 BILLION SB ENERGY INVESTMENT Nvidia is reportedly in talks to invest"
- META (Meta) score 4.9 — "Pulse of the Street: Tata jitters, metal rout weigh on Indian equities"
- VT (Vanguard Total World Stock Ind) score 3.9 — "Neighbors in rural Texas county are not happy about Elon Musk’s plan to erect world’s larg"
- RDDT (Reddit, Inc.) score 3.1 — "Reddit shares surge 14% on S&P 500 inclusion, replacing AvalonBay"
- AAPL (Apple Inc.) score 3.0 — "Nvidia, Apple, Google fuel record $185 billion gain for Norway’s wealth fund, but CEO say,"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 2.4 — "Lenskart shares soar after strong Q1 results and MSCI inclusion buzz"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 2.2 — "ICICI Bank Share Price Live Updates: ICICI Bank's Market Movement Today"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 2.0 — "Baazar Style Retail shares hit 5% upper circuit on reports of Aditya Halwasia buying compa"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.9 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.8 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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