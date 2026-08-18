# Transmission Layer — board brief · 2026-08-18 18:55Z

data as of **2026-08-18** · 98 series · 6 red / 34 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.213, 2d in regime; vol-pct 0.25, breadth-off 0.176, Markov P(high-vol) 0.019)
- [INVERTED] **safe_haven_gold** — corr20 -0.35, corr60 -0.4, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.84, corr60 0.87, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.29, corr60 0.37, last shift 2026-07-01. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.21, corr60 -0.11, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.72, corr60 -0.82, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.13, corr60 -0.11, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.19, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.0, corr60 0.22, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 1.0083597765664365e-06)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.493** (n=1115) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.827** (n=2371) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 5.18] dyn_lenskart_ns ↑
- dyn_lenskart_ns [EQUITIES]: last 628.00, z20 3.18, zc 2.37, resid-z 2.15 [unexplained], 1d 3.36%, |z20|=3.18; 1y-pct=99
- **Mechanism**: dyn_lenskart_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Lenskart shares gain over 5% to record high after incorporating new step-down subsidiary in China — Mint Markets, 2026-08-18. https://www.livemint.com/market/stock-market-news/lenskart-shares-gain-over-5-to-record-high-after-incorporating-new-step-down-subsidiary-in-china-11787043990119.html
- Source: Stocks to Watch, Aug 18: Paytm, Airtel, GMR Airports, Netweb Tech, SPR Auto, Lenskart, Manipal Health — BusinessLine Mkts, 2026-08-18. https://www.thehindubusinessline.com/markets/stock-markets/stocks-in-focus-paytm-airtel-gmr-airports-netweb-tech-spr-auto-lenskart-manipal-health-and-more/article71358731.ece
- Source: Stocks in focus: Paytm, Airtel, GMR Airports, Netweb Tech, SPR Auto, Lenskart, Manipal Health and more — BusinessLine Mkts, 2026-08-18. https://www.thehindubusinessline.com/markets/stock-markets/stocks-in-focus-paytm-airtel-gmr-airports-netweb-tech-spr-auto-lenskart-manipal-health-and-more/article71358731.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

### [RED 4.99] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.63, z20 1.99, zc n/a, resid-z n/a [quiet], 1d 0.11%, 52-wk extreme (pct=100); |z20|=1.99; 1y-pct=100
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.502 via midcap_largecap_ratio, z 0.54, quiet); dyn_bharatcoal_ns (rho 0.375 via midcap_largecap_ratio, z -1.34, reacted); dyn_fincables_ns (rho 0.361 via midcap_largecap_ratio, z 2.28, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.502 vs midcap_largecap_ratio, historically leads by 2d
- **India receivers**: nifty_midcap_100 (rho 0.502, z 0.54); dyn_bharatcoal_ns (rho 0.375, z -1.34); dyn_fincables_ns (rho 0.361, z 2.28)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 4.73] commodities · 2 series ↑
- corn [COMMODITIES]: last 487.75, z20 3.90, zc 3.82, resid-z 2.71 [unexplained], 1d 4.89%, |z20|=3.90; 1y-pct=100
- soybeans [COMMODITIES]: last 1215.25, z20 1.00, zc 1.17, resid-z 0.84 [quiet], 1d 1.19%, 1y-pct=97
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: wheat (co-move) — not yet - watch; rho 0.637 vs corn
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-20 (d=0.16), 2025-04-03 (d=0.17)

### [RED 4.65] dyn_stylebaaza_ns ↑
- dyn_stylebaaza_ns [EQUITIES]: last 402.65, z20 2.65, zc 1.34, resid-z 1.71 [unexplained], 1d 4.99%, |z20|=2.65; 1y-pct=96
- **Mechanism**: dyn_stylebaaza_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_pcjeweller_ns (rho 0.393 via dyn_stylebaaza_ns, z 0.05, quiet); dyn_adanient_bo (rho 0.374 via dyn_stylebaaza_ns, z -0.53, quiet); dyn_bharatcoal_ns (rho 0.352 via dyn_stylebaaza_ns, z -1.34, reacted)
- **India receivers**: dyn_pcjeweller_ns (rho 0.393, z 0.05); dyn_adanient_bo (rho 0.374, z -0.53); dyn_bharatcoal_ns (rho 0.352, z -1.34)
- Source: Sunshine Pictures IPO sees strong retail demand on Day 1 — BusinessLine Mkts, 2026-08-18. https://www.thehindubusinessline.com/markets/sunshine-pictures-ipo-sees-strong-retail-demand-on-day-1/article71360474.ece
- Source: Klarna trims full-year revenue, volume outlook as German retail weakens — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/us-stocks/news/klarna-trims-full-year-revenue-volume-outlook-as-german-retail-weakens/articleshow/133323113.cms
- Source: US Stock Market: Citadel Securities warns SEC rule change could hurt retail investors, market liquidity — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stock-market-citadel-securities-warns-sec-rule-change-could-hurt-retail-investors-market-liquidity/articleshow/133311215.cms
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-04 (d=0.01), 2025-02-20 (d=0.02)

### [AMBER 4.58] cross-asset · 3 series ↑
- ust_30y [RATES]: last 5.25, z20 1.26, zc 0.98, resid-z 0.73 [quiet], 1d 0.77%, 1y-pct=99
- dyn_bond [EQUITIES]: last 90.53, z20 -0.69, zc 0.39, resid-z -0.48 [quiet], 1d 0.12%, 1y-pct=2
- ust_10y [RATES]: last 4.68, z20 0.39, zc 1.08, resid-z 1.15 [quiet], 1d 1.08%, 1y-pct=96
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: tips_10y_real (co-move) — not yet - watch; rho 0.688 vs ust_30y, historically leads by 1d
- Watch next: brent (co-move) — not yet - watch; rho 0.557 vs ust_30y, historically leads by 3d
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.53 vs ust_30y, historically leads by 1d
- Watch next: wti (co-move) — not yet - watch; rho 0.53 vs ust_30y, historically leads by 3d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.537 vs ust_30y
- Source: Kotak Mahindra Bank raises $650 million in debut dollar bond sale — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/bonds/kotak-mahindra-bank-raises-650-million-in-debut-dollar-bond-sale/articleshow/133327166.cms
- Source: 6% Treasury yields are the biggest risk facing stocks right now. Here’s why. — MarketWatch Top, 2026-08-18. https://www.marketwatch.com/story/6-treasury-yields-are-the-biggest-risk-facing-stocks-right-now-heres-why-04fb9bbe?mod=mw_rss_topstories
- Source: US Stocks: US market hits two-week lows as Iran tensions lift oil, bond yields — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-us-market-opens-lower-as-iran-stalemate-lifts-oil-yields/articleshow/133324329.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.12), 2025-04-23 (d=0.18)

### [AMBER 4.3] cross-asset · 4 series ↑
- russell_2000 [INDICES]: last 3023.29, z20 0.64, zc -0.97, resid-z -0.76 [quiet], 1d -1.12%, 1y-pct=96
- dyn_vt [EQUITIES]: last 160.15, z20 0.63, zc -1.41, resid-z 0.26 [quiet], 1d -1.04%, 1y-pct=96
- sp500 [INDICES]: last 7698.20, z20 0.62, zc -0.80, resid-z -0.50 [quiet], 1d -0.61%, 1y-pct=96
- dow_jones [INDICES]: last 53390.03, z20 0.36, zc -0.18, resid-z 0.36 [quiet], 1d -0.13%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.81 vs russell_2000, historically leads by 5d
- Watch next: brent (inverse) — not yet - watch; rho -0.651 vs dow_jones, historically leads by 3d
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.633 vs dyn_vt, historically leads by 5d
- Watch next: wti (inverse) — not yet - watch; rho -0.627 vs dow_jones, historically leads by 2d
- Watch next: ust_10y (inverse) — not yet - watch; rho -0.603 vs russell_2000, historically leads by 1d
- Source: Wall Street wants to turn sports betting into ETFs. Critics call it dangerous ‘nonsense.’ — MarketWatch Top, 2026-08-18. https://www.marketwatch.com/story/wall-street-wants-to-turn-sports-betting-into-etfs-critics-call-it-dangerous-nonsense-a83db946?mod=mw_rss_topstories
- Source: US stock market today: S&P 500, Nasdaq futures down up to 1% amid surging oil and bond yields — Mint Markets, 2026-08-18. https://www.livemint.com/market/us-stock-market-today-s-p-500-nasdaq-futures-down-up-to-1-amid-surging-oil-and-bond-yields-11787054644462.html
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US stock futures fall as fading Iran peace hopes lift oil prices, yields — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-war-hormuz-deal-brent-crude-oil-fed-warsh-rate-bonds-yields-micron-sandisk-amd-intel-chip-stock-price-news-18th-august-2026/liveblog/133322350.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-21 (d=0.44), 2024-10-11 (d=0.45)

### [AMBER 4.26] dyn_voltas_ns ↓
- dyn_voltas_ns [EQUITIES]: last 1252.90, z20 -2.26, zc -0.56, resid-z -0.23 [quiet], 1d -1.11%, |z20|=2.26; 1y-pct=4
- **Mechanism**: dyn_voltas_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bharatcoal_ns (rho 0.578 via dyn_voltas_ns, z -1.34, reacted); nifty_midcap_100 (rho 0.518 via dyn_voltas_ns, z 0.54, quiet); nifty_50 (rho 0.394 via dyn_voltas_ns, z -0.62, quiet); dyn_havells_ns (rho 0.372 via dyn_voltas_ns, z 1.27, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.518 vs dyn_voltas_ns, historically leads by 5d
- **India receivers**: dyn_bharatcoal_ns (rho 0.578, z -1.34); nifty_midcap_100 (rho 0.518, z 0.54); nifty_50 (rho 0.394, z -0.62); dyn_havells_ns (rho 0.372, z 1.27)
- Source: Voltas reported strong growth in June quarter, but failed to impress — Mint Markets, 2026-08-18. https://www.livemint.com/market/mark-to-market/voltas-strong-growth-fails-to-impress-operating-revenue-acs-home-appliances-other-businesses-engineering-products-11787031152020.html
- Source: Voltas among 4 F&O stocks with a sharp rise in futures open interest — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/stocks/news/voltas-among-4-fampo-stocks-with-a-sharp-rise-in-futures-open-interest/slideshow/133310686.cms
- Source: Voltas shares fall 4% as brokerages differ after Q1 results — BusinessLine Mkts, 2026-08-17. https://www.thehindubusinessline.com/markets/voltas-shares-fall-over-6-from-intraday-high-as-brokerages-differ-after-q1-results/article71355298.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-24 (d=0.0), 2024-11-14 (d=0.01)

### [AMBER 4.14] dyn_meta ↓
- dyn_meta [EQUITIES]: last 545.46, z20 -2.14, zc -1.64, resid-z -0.10 [moved], 1d -4.13%, |z20|=2.14; 1y-pct=2
- **Mechanism**: dyn_meta ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.393 via dyn_meta, z 0.54, quiet); dyn_hdbfs_bo (rho 0.375 via dyn_meta, z 1.04, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.393, z 0.54); dyn_hdbfs_bo (rho 0.375, z 1.04)
- Source: META - META PLATFORMS SHARES TOUCH OVER TWO-WEEK LOW, LAST DOWN 3.8% — DeItaone, 2026-08-18. https://t.me/walter_bloomberg/34845
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2024-10-21 (d=0.07)

## Watchlist (below surfacing floor)
dyn_tech ↑ (3.37), gold_silver_ratio ↑ (3.24), dyn_lth ↑ (3.19), nifty_fmcg ↓ (3.17), dyn_bac ↑ (3.16), dyn_hdb ↓ (3.04), dyn_coin ↓ (3.01), dyn_tatatech_ns ↑ (2.84), dyn_idbi_ns ↓ (2.55), fx · 2 series ↑ (2.49), dyn_icicigi_bo ↓ (2.46), dyn_fincables_ns ↑ (2.28)

## India macro
- nifty_50: 24154.9004 (1d -0.55%, z20 -0.62, flag none)
- nifty_midcap_100: 63535.3984 (1d -0.44%, z20 0.54, flag amber)
- usd_inr: 95.6700 (1d 0.23%, z20 -0.06, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6303 (1d 0.11%, z20 1.99, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 88.3 — "Indian govt does not see much impact on kharif crops from El Nino as sowing deficit narrow"
- INOXINDIA.NS (INOX INDIA LIMITED) score 87.9 — "Indian govt does not see much impact on kharif crops from El Nino as sowing deficit narrow"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 86.8 — "Indian govt does not see much impact on kharif crops from El Nino as sowing deficit narrow"
- INDIANB.NS (INDIAN BANK) score 73.4 — "NVDA - BOFA: NVIDIA COULD BE UP TO 50% UNDERVALUED Bank of America says Nvidia may trade a"
- BAC (Bank of America Corporation) score 60.5 — "NVDA - BOFA: NVIDIA COULD BE UP TO 50% UNDERVALUED Bank of America says Nvidia may trade a"
- HDB (HDFC Bank Limited) score 54.7 — "NVDA - BOFA: NVIDIA COULD BE UP TO 50% UNDERVALUED Bank of America says Nvidia may trade a"
- IDBI.NS (IDBI BANK LIMITED) score 49.3 — "NVDA - BOFA: NVIDIA COULD BE UP TO 50% UNDERVALUED Bank of America says Nvidia may trade a"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 49.3 — "NVDA - BOFA: NVIDIA COULD BE UP TO 50% UNDERVALUED Bank of America says Nvidia may trade a"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 49.2 — "NVDA - BOFA: NVIDIA COULD BE UP TO 50% UNDERVALUED Bank of America says Nvidia may trade a"
- COIN (Coinbase Global, Inc.) score 47.2 — "YARDENI: 5% TREASURY YIELD IS THE KEY LINE Ed Yardeni isn’t alarmed by surging global bond"
- OHI (Omega Healthcare Investors, In) score 44.2 — "NVDA - BOFA: NVIDIA COULD BE UP TO 50% UNDERVALUED Bank of America says Nvidia may trade a"
- TECHM.NS (TECH MAHINDRA LIMITED) score 43.7 — "AAPL - APPLE OVERHAULS EU APP STORE FEES Apple is revamping its EU App Store terms from Oc"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 41.5 — "AAPL - APPLE OVERHAULS EU APP STORE FEES Apple is revamping its EU App Store terms from Oc"
- TECH (Bio-Techne Corp) score 41.3 — "AAPL - APPLE OVERHAULS EU APP STORE FEES Apple is revamping its EU App Store terms from Oc"
- BOND (PIMCO Active Bond Exchange-Tra) score 38.3 — "YARDENI: 5% TREASURY YIELD IS THE KEY LINE Ed Yardeni isn’t alarmed by surging global bond"
- CHKP (Check Point Software Technolog) score 33.8 — "Can you get a piece of State Farm’s $5 billion cash-back dividend? Here’s how to check."
- LTH (Life Time Group Holdings, Inc.) score 29.0 — "TRUMP’S TUESDAY SCHEDULE: President Trump’s schedule for Tuesday, August 18 centers on a s"
- 301077.SZ (CHINASTARS) score 24.1 — "China’s Solar Exports Fell 21.4% in July"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 19.7 — "Tata Consumer Share Price Live Updates: Tata Consumer's Market Close"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 18.5 — "Top Gainers & Losers on 18 August: PTC Industries, Inox Wind, Mphasis, Tata Elxsi, Suzlon "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 18.2 — "Tata Consumer Share Price Live Updates: Tata Consumer's Market Close"
- JIOFIN.BO (Jio Financial Services Limited) score 15.8 — "Gambling is everywhere. How do financial advisers keep clients from going overboard?"
- PCJEWELLER.NS (PC JEWELLER LTD) score 14.7 — "Lalithaa Jewellery IPO Day 2: Subscribed 3.07x overall"
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.9 — "Ashok Leyland just had a record June quarter. So why did the margin fall a full point?"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 11.5 — "Romania Restarts Coal Plant as Danube Drought Forces Nuclear Shutdown"
- MS (Morgan Stanley) score 11.4 — "PRICE TARGET RAISED • $ANF: PT raised to $126 from $110 by JPMorgan • $CPB: PT raised to $"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 11.1 — "Gambling is everywhere. How do financial advisers keep clients from going overboard?"
- NVDA (NVIDIA Corporation) score 8.6 — "NVDA - BOFA: NVIDIA COULD BE UP TO 50% UNDERVALUED Bank of America says Nvidia may trade a"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.6 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Trading Update"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 7.4 — "Sunshine Pictures IPO sees strong retail demand on Day 1"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.0 — "ICICI Bank Share Price Highlights: ICICI Bank Stock Price History"
- VT (Vanguard Total World Stock Ind) score 6.4 — "US 10-YEAR YIELD HITS 19-MONTH HIGH The 10-year Treasury yield climbed to 4.75%, its highe"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 5.8 — "Jeff Currie: Forget $91 Brent, The Real Crisis Is $170 Diesel"
- META (Meta) score 5.5 — "META - META PLATFORMS SHARES TOUCH OVER TWO-WEEK LOW, LAST DOWN 3.8%"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.2 — "Adani flagship eyes India’s Nifty crown after years of turmoil"
- AAPL (Apple Inc.) score 4.7 — "AAPL - APPLE OVERHAULS EU APP STORE FEES Apple is revamping its EU App Store terms from Oc"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.4 — "Lenskart shares gain over 5% to record high after incorporating new step-down subsidiary i"
- VOLTAS.NS (VOLTAS LTD) score 4.0 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.7 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.6 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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