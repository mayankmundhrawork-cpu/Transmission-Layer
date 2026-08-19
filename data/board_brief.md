# Transmission Layer — board brief · 2026-08-19 07:03Z

data as of **2026-08-19** · 98 series · 6 red / 36 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.452, 1d in regime; vol-pct 0.278, breadth-off 0.625, Markov P(high-vol) 0.02)
- [INVERTED] **safe_haven_gold** — corr20 -0.36, corr60 -0.41, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.87, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.27, corr60 0.4, last shift 2026-07-01. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.18, corr60 -0.11, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.72, corr60 -0.82, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.12, corr60 -0.11, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.19, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.0, corr60 0.22, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 2.2451983707760803e-06)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.493** (n=1116) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.83** (n=2360) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 6.07] cross-asset · 4 series ↑
- ust_30y [RATES]: last 5.31, z20 2.40, zc 1.46, resid-z 1.25 [quiet], 1d 1.14%, |z20|=2.40; 1y-pct=100
- ust_10y [RATES]: last 4.72, z20 1.35, zc 0.85, resid-z 0.60 [quiet], 1d 0.85%, 1y-pct=99
- tips_10y_real [RATES]: last 2.44, z20 1.06, zc 0.83, resid-z 0.48 [quiet], 1d 1.24%, 1y-pct=99
- dyn_bond [EQUITIES]: last 90.51, z20 -0.76, zc 0.33, resid-z 0.14 [quiet], 1d 0.10%, 1y-pct=2
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.578 vs ust_30y, historically leads by 3d
- Watch next: wti (co-move) — not yet - watch; rho 0.559 vs ust_30y, historically leads by 3d
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.541 vs ust_30y, historically leads by 1d
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.522 vs tips_10y_real, historically leads by 4d
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.517 vs ust_30y, historically leads by 1d
- Source: High Treasury yields put US fiscal outlook under spotlight — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/high-treasury-yields-put-us-fiscal-outlook-under-spotlight/articleshow/133337550.cms
- Source: Sensex today | Stock Market Live: Sensex slips 150 pts, Nifty below 24,100 as bond yield spike rattle markets; Brent crude climbs toward $92 — BusinessLine Mkts, 2026-08-19. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-19th-august-2026/article71360276.ece
- Source: Nifty slips for seventh day as crude surge, bond yield spike rattle markets — BusinessLine Mkts, 2026-08-19. https://www.thehindubusinessline.com/markets/stock-markets/nifty-slips-for-seventh-day-as-crude-surge-bond-yield-spike-rattle-markets/article71363259.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

### [RED 5.35] dyn_voltas_ns ↓
- dyn_voltas_ns [EQUITIES]: last 1222.80, z20 -3.35, zc -1.25, resid-z -0.24 [quiet], 1d -2.40%, |z20|=3.35; 1y-pct=0
- **Mechanism**: dyn_voltas_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bharatcoal_ns (rho 0.561 via dyn_voltas_ns, z -1.98, reacted); nifty_midcap_100 (rho 0.518 via dyn_voltas_ns, z 0.28, quiet); nifty_50 (rho 0.399 via dyn_voltas_ns, z -0.98, quiet); dyn_havells_ns (rho 0.387 via dyn_voltas_ns, z 0.47, quiet)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.518 vs dyn_voltas_ns, historically leads by 5d
- **India receivers**: dyn_bharatcoal_ns (rho 0.561, z -1.98); nifty_midcap_100 (rho 0.518, z 0.28); nifty_50 (rho 0.399, z -0.98); dyn_havells_ns (rho 0.387, z 0.47)
- Source: Voltas reported strong growth in June quarter, but failed to impress — Mint Markets, 2026-08-18. https://www.livemint.com/market/mark-to-market/voltas-strong-growth-fails-to-impress-operating-revenue-acs-home-appliances-other-businesses-engineering-products-11787031152020.html
- Source: Voltas among 4 F&O stocks with a sharp rise in futures open interest — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/stocks/news/voltas-among-4-fampo-stocks-with-a-sharp-rise-in-futures-open-interest/slideshow/133310686.cms
- Source: Voltas shares fall 4% as brokerages differ after Q1 results — BusinessLine Mkts, 2026-08-17. https://www.thehindubusinessline.com/markets/voltas-shares-fall-over-6-from-intraday-high-as-brokerages-differ-after-q1-results/article71355298.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-24 (d=0.0), 2024-11-14 (d=0.01)

### [RED 5.25] commodities · 3 series ↑
- corn [COMMODITIES]: last 490.25, z20 3.93, zc 4.56, resid-z -0.40 [moved], 1d 5.83%, |z20|=3.93; 1y-pct=100
- soybeans [COMMODITIES]: last 1225.75, z20 1.41, zc 2.06, resid-z -0.18 [moved], 1d 2.08%, 1y-pct=98
- wheat [COMMODITIES]: last 684.00, z20 1.30, zc 1.64, resid-z -0.87 [moved], 1d 2.93%, 1y-pct=99
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_lenskart_ns (rho 0.362 via wheat, z 3.06, reacted); dyn_coalindia_ns (rho -0.355 via corn, z -2.4, reacted)
- **India receivers**: dyn_lenskart_ns (rho 0.362, z 3.06); dyn_coalindia_ns (rho -0.355, z -2.4)
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [RED 5.06] dyn_lenskart_ns ↑
- dyn_lenskart_ns [EQUITIES]: last 638.95, z20 3.06, zc 1.04, resid-z 2.21 [unexplained], 1d 1.68%, |z20|=3.06; 1y-pct=99
- **Mechanism**: dyn_lenskart_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Lenskart shares gain over 5% to record high after incorporating new step-down subsidiary in China — Mint Markets, 2026-08-18. https://www.livemint.com/market/stock-market-news/lenskart-shares-gain-over-5-to-record-high-after-incorporating-new-step-down-subsidiary-in-china-11787043990119.html
- Source: Stocks to Watch, Aug 18: Paytm, Airtel, GMR Airports, Netweb Tech, SPR Auto, Lenskart, Manipal Health — BusinessLine Mkts, 2026-08-18. https://www.thehindubusinessline.com/markets/stock-markets/stocks-in-focus-paytm-airtel-gmr-airports-netweb-tech-spr-auto-lenskart-manipal-health-and-more/article71358731.ece
- Source: Stocks in focus: Paytm, Airtel, GMR Airports, Netweb Tech, SPR Auto, Lenskart, Manipal Health and more — BusinessLine Mkts, 2026-08-18. https://www.thehindubusinessline.com/markets/stock-markets/stocks-in-focus-paytm-airtel-gmr-airports-netweb-tech-spr-auto-lenskart-manipal-health-and-more/article71358731.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

### [RED 4.99] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.63, z20 1.99, zc n/a, resid-z n/a [quiet], 1d 0.17%, 52-wk extreme (pct=100); |z20|=1.99; 1y-pct=100
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.502 via midcap_largecap_ratio, z 0.28, quiet); dyn_bharatcoal_ns (rho 0.386 via midcap_largecap_ratio, z -1.98, reacted); dyn_fincables_ns (rho 0.355 via midcap_largecap_ratio, z 1.67, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.502 vs midcap_largecap_ratio, historically leads by 2d
- **India receivers**: nifty_midcap_100 (rho 0.502, z 0.28); dyn_bharatcoal_ns (rho 0.386, z -1.98); dyn_fincables_ns (rho 0.355, z 1.67)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 4.65] dyn_stylebaaza_ns ↑
- dyn_stylebaaza_ns [EQUITIES]: last 422.75, z20 2.65, zc 1.32, resid-z 1.71 [unexplained], 1d 4.99%, |z20|=2.65; 1y-pct=100
- **Mechanism**: dyn_stylebaaza_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_pcjeweller_ns (rho 0.392 via dyn_stylebaaza_ns, z 0.36, quiet); dyn_adanient_bo (rho 0.356 via dyn_stylebaaza_ns, z -1.14, reacted)
- **India receivers**: dyn_pcjeweller_ns (rho 0.392, z 0.36); dyn_adanient_bo (rho 0.356, z -1.14)
- Source: Sunshine Pictures IPO sees strong retail demand on Day 1 — BusinessLine Mkts, 2026-08-18. https://www.thehindubusinessline.com/markets/sunshine-pictures-ipo-sees-strong-retail-demand-on-day-1/article71360474.ece
- Source: Klarna trims full-year revenue, volume outlook as German retail weakens — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/us-stocks/news/klarna-trims-full-year-revenue-volume-outlook-as-german-retail-weakens/articleshow/133323113.cms
- Source: US Stock Market: Citadel Securities warns SEC rule change could hurt retail investors, market liquidity — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stock-market-citadel-securities-warns-sec-rule-change-could-hurt-retail-investors-market-liquidity/articleshow/133311215.cms
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-04 (d=0.01), 2025-02-20 (d=0.02)

### [AMBER 4.4] dyn_coalindia_ns ↓
- dyn_coalindia_ns [EQUITIES]: last 398.95, z20 -2.40, zc -1.67, resid-z -0.19 [moved], 1d -1.95%, |z20|=2.40
- **Mechanism**: dyn_coalindia_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bharatcoal_ns (rho 0.452 via dyn_coalindia_ns, z -1.98, reacted); usd_inr (rho 0.408 via dyn_coalindia_ns, z 0.14, quiet)
- **India receivers**: dyn_bharatcoal_ns (rho 0.452, z -1.98); usd_inr (rho 0.408, z 0.14)
- Source: Sensex today | Stock Market Live: Sensex falls 350 points, Nifty trades near 24,050; Powergrid, Coal India lead losers — BusinessLine Mkts, 2026-08-19. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-19th-august-2026/article71360276.ece
- Source: Coal India Share Price Live Updates: Coal India Ltd Trading Below Key Support Level — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/coal-india-ltd-stock-price-livestock-price-today-live-updates-19-aug-2026/liveblog/133335803.cms
- Source: Coal India Share Price Live Updates: Coal India  Current Trading Status — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/coal-india-ltd-stock-price-live-updates-18-aug-2026/liveblog/133310012.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.03), 2024-11-07 (d=0.04)

### [AMBER 4.26] cross-asset · 4 series ↑
- dyn_vt [EQUITIES]: last 160.06, z20 0.60, zc -1.49, resid-z 1.41 [quiet], 1d -1.09%, 1y-pct=96
- sp500 [INDICES]: last 7693.26, z20 0.59, zc -0.88, resid-z 0.14 [quiet], 1d -0.67%, 1y-pct=96
- russell_2000 [INDICES]: last 3017.63, z20 0.52, zc -1.13, resid-z -0.92 [quiet], 1d -1.31%, 1y-pct=96
- dow_jones [INDICES]: last 53346.60, z20 0.31, zc -0.30, resid-z 0.25 [quiet], 1d -0.21%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.942 vs dyn_vt, historically leads by 5d
- Watch next: brent (inverse) — not yet - watch; rho -0.662 vs dow_jones, historically leads by 3d
- Watch next: wti (inverse) — not yet - watch; rho -0.645 vs dow_jones, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.829 vs dyn_vt
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.627 vs dyn_vt, historically leads by 5d
- Source: What does a hit film about the Iraq war say about Chinese views of the world? — SCMP Economy, 2026-08-19. https://www.scmp.com/news/china/diplomacy/article/3364464/what-does-hit-film-about-iraq-war-say-about-chinese-views-world?utm_source=rss_feed
- Source: TECH SELLOFF HITS WALL STREET AS YIELDS SURGE Wall Street closed lower as rising oil prices and Middle East tensions pushed Treasury yields sharply higher, pressuring technology stocks. The Nasdaq fell 1.3%, while the S&P 500 lost 0.7%. Semiconductors led declines as higher — DeItaone, 2026-08-18. https://t.me/walter_bloomberg/34867
- Source: US stocks: Tech selloff weighs down Wall Street as bond yields climb — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-tech-selloff-weighs-down-wall-street-as-bond-yields-climb/articleshow/133332021.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-21 (d=0.44), 2024-10-11 (d=0.45)

## Watchlist (below surfacing floor)
dyn_meta ↓ (4.22), dxy ↓ (4.14), gold_silver_ratio ↑ (3.83), dyn_bac ↑ (3.32), dyn_lth ↑ (3.19), dyn_coin ↓ (3.08), dyn_hdb ↓ (3.06), dyn_tech ↑ (2.88), nifty_fmcg ↓ (2.79), dyn_icicigi_bo ↓ (2.76), dyn_tatatech_ns ↑ (2.48), dyn_idbi_ns ↓ (2.03)

## India macro
- nifty_50: 24052.5000 (1d -0.42%, z20 -0.98, flag none)
- nifty_midcap_100: 63371.6484 (1d -0.26%, z20 0.28, flag amber)
- usd_inr: 95.7300 (1d 0.04%, z20 0.14, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6347 (1d 0.17%, z20 1.99, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 89.4 — "India's Closing Auction Session turmoil clouds BSE’s growth outlook"
- INOXINDIA.NS (INOX INDIA LIMITED) score 89.0 — "India's Closing Auction Session turmoil clouds BSE’s growth outlook"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 88.0 — "India's Closing Auction Session turmoil clouds BSE’s growth outlook"
- INDIANB.NS (INDIAN BANK) score 76.1 — "Axis Bank Share Price Live Updates: Axis Bank's Market Update"
- BAC (Bank of America Corporation) score 62.5 — "Axis Bank Share Price Live Updates: Axis Bank's Market Update"
- HDB (HDFC Bank Limited) score 55.5 — "Axis Bank Share Price Live Updates: Axis Bank's Market Update"
- IDBI.NS (IDBI BANK LIMITED) score 50.7 — "Axis Bank Share Price Live Updates: Axis Bank's Market Update"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 50.7 — "Axis Bank Share Price Live Updates: Axis Bank's Market Update"
- COIN (Coinbase Global, Inc.) score 50.7 — "L&T Technology Services bags $75-million deal from global technology major"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 50.7 — "Axis Bank Share Price Live Updates: Axis Bank's Market Update"
- TECHM.NS (TECH MAHINDRA LIMITED) score 49.5 — "L&T Technology Services shares jump 3% after bagging $75 million deal"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 47.6 — "L&T Technology Services shares jump 3% after bagging $75 million deal"
- TECH (Bio-Techne Corp) score 47.4 — "L&T Technology Services shares jump 3% after bagging $75 million deal"
- OHI (Omega Healthcare Investors, In) score 42.3 — "Meta is facing its ‘Big Tobacco’ moment — and investors can profit"
- BOND (PIMCO Active Bond Exchange-Tra) score 39.7 — "Gold edges below $4,400 as traders eye slump in long-dated bonds"
- CHKP (Check Point Software Technolog) score 37.0 — "Horizon Industrial Parks IPO Day 3: Issue subscribed 27% so far. Check GMP, review - apply"
- LTH (Life Time Group Holdings, Inc.) score 29.7 — "Gold extends losses, falls to nearly Rs 1.54 lakh/10 gm. Time to buy?"
- 301077.SZ (CHINASTARS) score 21.5 — "China’s Solar Exports Fell 21.4% in July"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.3 — "The U.S. Is Quietly Building a New Energy Foothold in Iraq"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 19.5 — "Tata Consumer Share Price Live Updates: Tata Consumer Trading Below Key Support Level"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 18.2 — "Tata Consumer Share Price Live Updates: Tata Consumer Trading Below Key Support Level"
- JIOFIN.BO (Jio Financial Services Limited) score 18.0 — "Vijay Kedia buys Rs 33 crore stake in Zaggle Prepaid Ocean Services via bulk deal, stock s"
- PCJEWELLER.NS (PC JEWELLER LTD) score 16.0 — "Shankesh Jewellers IPO day 2: Issue sees decent buying, GMP signals modest listing gains; "
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 14.2 — "Bharat Value Fund bets ₹300 crore for undisclosed stake in Big Mishra Pedha"
- MS (Morgan Stanley) score 11.1 — "ANTHROPIC LINES UP $10B+ CREDIT AHEAD OF IPO Anthropic’s revolving credit facility is set "
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 10.9 — "Jio Financial Services Share Price Live Updates: Jio Financial Services Stock Details"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.6 — "Ashok Leyland just had a record June quarter. So why did the margin fall a full point?"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 10.6 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Sees Minor Drop in Price"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.6 — "IGL, MGL to Adani Total Gas: City gas distributor stocks rise up to 4%; here's why"
- NVDA (NVIDIA Corporation) score 7.6 — "NVDA - BOFA: NVIDIA COULD BE UP TO 50% UNDERVALUED Bank of America says Nvidia may trade a"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.2 — "ICICI Bank shares slip 0.52% in early trade, despite yearly gains"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 7.2 — "Bharat Value Fund bets ₹300 crore for undisclosed stake in Big Mishra Pedha"
- VT (Vanguard Total World Stock Ind) score 6.7 — "What does a hit film about the Iraq war say about Chinese views of the world?"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 6.6 — "Sunshine Pictures IPO sees strong retail demand on Day 1"
- META (Meta) score 5.8 — "Meta is facing its ‘Big Tobacco’ moment — and investors can profit"
- AAPL (Apple Inc.) score 4.2 — "AAPL - APPLE OVERHAULS EU APP STORE FEES Apple is revamping its EU App Store terms from Oc"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.9 — "Lenskart shares gain over 5% to record high after incorporating new step-down subsidiary i"
- VOLTAS.NS (VOLTAS LTD) score 3.5 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.6 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.5 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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