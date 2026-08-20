# Transmission Layer — board brief · 2026-08-20 07:04Z

data as of **2026-08-20** · 98 series · 11 red / 31 amber · 8 events surfaced (22 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.27, 2d in regime; vol-pct 0.165, breadth-off 0.375, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.43, corr60 -0.41, last shift 2026-06-05. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.88, corr60 0.88, last shift 2026-02-05. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.22, corr60 0.4, last shift 2026-07-02. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.17, corr60 -0.12, last shift 2026-06-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.68, corr60 -0.82, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.01, corr60 -0.11, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.13, corr60 -0.16, last shift 2026-06-24. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.05, corr60 0.23, last shift 2026-04-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.0006496287948376533)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.491** (n=1116) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.828** (n=2407) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 36.35] cross-asset · 3 series ↑
- dyn_mrna [EQUITIES]: last 174.16, z20 33.03, zc 43.51, resid-z -0.64 [moved], 1d 176.63%, |z20|=33.03; 1y-pct=100
- eth_usd [CRYPTO]: last 2258.89, z20 3.84, zc -0.24, resid-z 6.31 [unexplained], 1d -1.57%, |z20|=3.84
- btc_usd [CRYPTO]: last 69740.53, z20 3.79, zc -0.10, resid-z 3.41 [unexplained], 1d -0.36%, |z20|=3.79
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.37).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_coin (co-move) — not yet - watch; rho 0.809 vs eth_usd, historically leads by 5d
- Watch next: vix (inverse) — not yet - watch; rho -0.574 vs eth_usd
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.509 vs btc_usd
- Source: Moderna’s 177% Surge Burns Shorts in ‘Painful’ $5.5 Billion Loss — Mint Markets, 2026-08-19. https://www.livemint.com/market/modernas-177-surge-burns-shorts-in-painful-5-5-billion-loss-11787175519880.html
- Source: Moderna’s cancer-vaccine breakthrough drives broad biopharma stock rally — MarketWatch Top, 2026-08-19. https://www.marketwatch.com/story/modernas-cancer-vaccine-breakthrough-drives-broad-biopharma-stock-rally-ff2816aa?mod=mw_rss_topstories
- Source: Moderna’s experimental vaccine prevents cancer recurrence, in ‘historic’ win for personalized medicine. Its stock soared. — MarketWatch Top, 2026-08-19. https://www.marketwatch.com/story/modernas-stock-doubles-on-promising-cancer-vaccine-results-896b1f2c?mod=mw_rss_topstories
- Historical analogues: 2025-08-13 (d=0.37), 2025-05-08 (d=1.1), 2024-11-07 (d=1.33)

### [RED 7.07] cross-asset · 3 series ↑
- comex_gold [COMMODITIES]: last 4550.40, z20 2.02, zc 0.79, resid-z -0.53 [quiet], 1d 1.36%, |z20|=2.02; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 67.11, z20 1.68, zc 0.85, resid-z -1.10 [quiet], 1d 2.09%, |z20|=1.68; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 67.81, z20 -0.75, zc n/a, resid-z n/a [quiet], 1d -0.72%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.526 via comex_silver, z 0.66, quiet); dyn_stylebaaza_ns (rho -0.375 via gold_silver_ratio, z 2.38, reacted)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.652 vs comex_gold, historically leads by 1d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.59 vs comex_silver, historically leads by 4d
- Watch next: dax (co-move) — not yet - watch; rho 0.547 vs comex_gold, historically leads by 4d
- Watch next: nifty_metal (co-move) — not yet - watch; rho 0.526 vs comex_silver, historically leads by 4d
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.508 vs comex_gold
- **India receivers**: nifty_metal (rho 0.526, z 0.66); dyn_stylebaaza_ns (rho -0.375, z 2.38)
- Source: Gold Rate Today, Aug 20: Gold prices up in Delhi, Mumbai, Kolkata, Bengaluru, Ahmedabad — BusinessLine Mkts, 2026-08-20. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-mumbai-chennai-ahmedabad-delhi-hyderabad-bengaluru-kolkata-gold-rates-august-20-2026/article71368051.ece
- Source: Aditya Birla Capital to enter gold loan market, targets 200-300 branches by March 2027 — BusinessLine Mkts, 2026-08-20. https://www.thehindubusinessline.com/markets/gold/aditya-birla-capital-to-enter-gold-loan-market-targets-1000-branches/article71367805.ece
- Source: Muthoot Finance, Manappuram, other gold financier stocks jump up to 4% as gold prices rise above Rs 1.58 lakh/10 grams — ET Markets, 2026-08-20. https://economictimes.indiatimes.com/markets/stocks/news/muthoot-finance-manappuram-other-gold-financier-stocks-jump-up-to-4-as-gold-prices-rise-above-rs-1-58-lakh/10-grams/articleshow/133364875.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.26] fx · 4 series ↑
- eur_usd [FX]: last 1.17, z20 2.60, zc 2.87, resid-z -0.66 [moved], 1d 0.92%, |z20|=2.60
- aud_usd [FX]: last 0.71, z20 2.12, zc 1.13, resid-z -0.49 [quiet], 1d 0.59%, |z20|=2.12
- gbp_usd [FX]: last 1.36, z20 2.04, zc 1.32, resid-z -0.54 [quiet], 1d 0.55%, |z20|=2.04
- usd_mxn [FX]: last 16.95, z20 -1.78, zc -1.80, resid-z 0.28 [moved], 1d -0.63%, |z20|=1.78; 1y-pct=0
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.588 via usd_mxn, z 0.72, quiet); nifty_midcap_100 (rho 0.422 via aud_usd, z 0.97, quiet); dyn_icicigi_bo (rho -0.388 via gbp_usd, z -0.04, quiet)
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.597 vs eur_usd, historically leads by 4d
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.555 vs eur_usd, historically leads by 5d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.561 vs eur_usd
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.531 vs aud_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.588, z 0.72); nifty_midcap_100 (rho 0.422, z 0.97); dyn_icicigi_bo (rho -0.388, z -0.04)
- Source: Selloff in euro zone bonds pauses but oil prices keep up pressure — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/bonds/selloff-in-euro-zone-bonds-pauses-but-oil-prices-keep-up-pressure/articleshow/133341510.cms
- Source: ECB'S LANE: EURO ZONE INFLATION ONE PERCENTAGE POINT ABOVE ECB'S 2% TARGET IS A LOT — DeItaone, 2026-08-18. https://t.me/walter_bloomberg/34837
- Source: Euro zone bonds join global selloff, long-end yields at multi-year highs — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bonds-join-global-selloff-long-end-yields-at-multi-year-highs/articleshow/133321858.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 5.91] commodities · 3 series ↑
- corn [COMMODITIES]: last 501.50, z20 4.59, zc 4.70, resid-z 0.91 [moved], 1d 6.03%, |z20|=4.59; 1y-pct=100
- wheat [COMMODITIES]: last 696.75, z20 2.28, zc 1.33, resid-z 0.37 [quiet], 1d 2.43%, |z20|=2.28; 1y-pct=99
- soybeans [COMMODITIES]: last 1239.75, z20 1.95, zc 1.40, resid-z 1.24 [quiet], 1d 1.43%, |z20|=1.95; 1y-pct=99
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [RED 4.99] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.64, z20 1.99, zc n/a, resid-z n/a [quiet], 1d 0.25%, 52-wk extreme (pct=100); |z20|=1.99; 1y-pct=100
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.506 via midcap_largecap_ratio, z 0.97, quiet); dyn_bharatcoal_ns (rho 0.389 via midcap_largecap_ratio, z -0.98, quiet); dyn_fincables_ns (rho 0.355 via midcap_largecap_ratio, z 1.5, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.506 vs midcap_largecap_ratio, historically leads by 2d
- **India receivers**: nifty_midcap_100 (rho 0.506, z 0.97); dyn_bharatcoal_ns (rho 0.389, z -0.98); dyn_fincables_ns (rho 0.355, z 1.5)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 4.87] dxy ↓
- dxy [FX]: last 98.78, z20 -1.87, zc -0.15, resid-z -0.15 [quiet], 1d -0.05%, 20d range extreme; |z20|=1.87
- **Mechanism**: dxy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [AMBER 4.46] cross-asset · 4 series ↑
- russell_2000 [INDICES]: last 3032.84, z20 0.80, zc 0.41, resid-z 0.57 [quiet], 1d 0.50%, 1y-pct=97
- dyn_vt [EQUITIES]: last 160.73, z20 0.74, zc 0.52, resid-z -1.75 [unexplained], 1d 0.42%, 1y-pct=97
- sp500 [INDICES]: last 7708.03, z20 0.62, zc 0.28, resid-z -0.98 [quiet], 1d 0.21%, 1y-pct=96
- dow_jones [INDICES]: last 53467.34, z20 0.39, zc 0.33, resid-z -0.22 [quiet], 1d 0.23%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.819 vs russell_2000, historically leads by 5d
- Watch next: brent (inverse) — not yet - watch; rho -0.661 vs dow_jones, historically leads by 3d
- Watch next: wti (inverse) — not yet - watch; rho -0.634 vs dow_jones, historically leads by 2d
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.608 vs dyn_vt, historically leads by 5d
- Watch next: ust_10y (inverse) — not yet - watch; rho -0.581 vs russell_2000, historically leads by 1d
- Source: World's Largest Electric Plane Flies for 27 Minutes on $5 of Power — OilPrice, 2026-08-19. https://oilprice.com/Latest-Energy-News/World-News/Worlds-Largest-Electric-Plane-Flies-for-27-Minutes-on-5-of-Power.html
- Source: Korean investors dump home stocks for US ones, buy same names at a premium | Is KOSPI-style crash coming to Wall Street? — Mint Markets, 2026-08-19. https://www.livemint.com/market/stock-market-news/korean-investors-dump-home-stocks-for-us-buying-same-names-at-a-premium-is-wall-street-headed-for-kospi-style-crash-11787150873908.html
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US futures steady after tech rout; Iran tensions, retail earnings in focus — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-war-hormuz-deal-crude-oil-fed-warsh-rate-hike-moderna-nvidia-micron-sandisk-chip-stock-price-news-19th-august-2026/liveblog/133348429.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-21 (d=0.44), 2024-10-11 (d=0.45)

### [AMBER 4.46] dyn_lenskart_ns ↑
- dyn_lenskart_ns [EQUITIES]: last 640.10, z20 2.46, zc 0.05, resid-z 0.88 [quiet], 1d 0.08%, |z20|=2.46; 1y-pct=99
- **Mechanism**: dyn_lenskart_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/stocks/news/lenskart-solutions-among-4-stocks-to-hit-52-week-highs-amp-surge-up-to-25-in-a-month/slideshow/133348316.cms
- Source: Lenskart shares gain over 5% to record high after incorporating new step-down subsidiary in China — Mint Markets, 2026-08-18. https://www.livemint.com/market/stock-market-news/lenskart-shares-gain-over-5-to-record-high-after-incorporating-new-step-down-subsidiary-in-china-11787043990119.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

## Watchlist (below surfacing floor)
dyn_stylebaaza_ns ↑ (4.38), rates · 2 series ↑ (4.35), dyn_meta ↓ (4.0), dyn_tech ↑ (3.99), dyn_hdb ↓ (2.95), indices · 2 series ↑ (2.92), usd_cny ↓ (2.72), eur_inr ↑ (2.72), dyn_tatatech_ns ↑ (2.62), ig_oas ↑ (2.47), dyn_lth ↑ (2.44), dyn_voltas_ns ↓ (2.39)

## India macro
- nifty_50: 24211.7500 (1d 0.55%, z20 -0.43, flag none)
- nifty_midcap_100: 63914.9492 (1d 0.80%, z20 0.97, flag amber)
- usd_inr: 95.6250 (1d -0.20%, z20 -0.02, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6398 (1d 0.25%, z20 1.99, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 100.3 — "Coal India Share Price Live Updates: Coal India Ltd Stock Details"
- INOXINDIA.NS (INOX INDIA LIMITED) score 98.0 — "Coal India Share Price Live Updates: Coal India Ltd Stock Details"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 97.3 — "Coal India Share Price Live Updates: Coal India Ltd Stock Details"
- INDIANB.NS (INDIAN BANK) score 86.6 — "HDFC Bank Share Price Live Updates: HDFC Bank's Current Trading Status"
- BAC (Bank of America Corporation) score 69.7 — "HDFC Bank Share Price Live Updates: HDFC Bank's Current Trading Status"
- HDB (HDFC Bank Limited) score 63.4 — "HDFC Bank Share Price Live Updates: HDFC Bank's Current Trading Status"
- BOND (PIMCO Active Bond Exchange-Tra) score 60.2 — "Gold rebounds above Rs 1.58 lakh/10 grams as US bond yields decline. What lies ahead?"
- IDBI.NS (IDBI BANK LIMITED) score 58.6 — "HDFC Bank Share Price Live Updates: HDFC Bank's Current Trading Status"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 58.6 — "HDFC Bank Share Price Live Updates: HDFC Bank's Current Trading Status"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 58.6 — "HDFC Bank Share Price Live Updates: HDFC Bank's Current Trading Status"
- COIN (Coinbase Global, Inc.) score 54.8 — "Global Market: Standard Chartered expands hedge fund offerings as investors seek protectio"
- TECHM.NS (TECH MAHINDRA LIMITED) score 49.0 — "Can Turtlemint Fintech shares rally to Rs 190? Why Jefferies initiated coverage on the sto"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 47.5 — "Can Turtlemint Fintech shares rally to Rs 190? Why Jefferies initiated coverage on the sto"
- TECH (Bio-Techne Corp) score 47.3 — "Can Turtlemint Fintech shares rally to Rs 190? Why Jefferies initiated coverage on the sto"
- OHI (Omega Healthcare Investors, In) score 41.6 — "Global Market: Standard Chartered expands hedge fund offerings as investors seek protectio"
- CHKP (Check Point Software Technolog) score 38.9 — "Horizon Industrial Parks IPO allotment likely to be out today. Latest GMP, step-by-step gu"
- LTH (Life Time Group Holdings, Inc.) score 35.2 — "Shiprocket shares jump 6% as Goldman Sachs acquires Rs 53 crore stake. Time to buy or book"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.7 — "A $420 camera for $10: China’s young consumers would rather rent than buy. Beijing has a p"
- JIOFIN.BO (Jio Financial Services Limited) score 20.6 — "TRUMP ANNOUNCES MAJOR ECONOMIC CAMPAIGN AGAINST IRAN President Trump announced sweeping ne"
- PCJEWELLER.NS (PC JEWELLER LTD) score 19.3 — "Lalithaa Jewellery Mart IPO GMP jumps, allotment date in focus after strong subscription s"
- 301077.SZ (CHINASTARS) score 19.0 — "Coking coal market poised to be volatile in the short-term on China mine mishap, steel out"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 16.3 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 15.9 — "Coal India Share Price Live Updates: Coal India Ltd Stock Details"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 15.3 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 15.0 — "Why Jefferies sees limited upside in Bajaj Housing Finance despite its fast-growing loan b"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 14.9 — "TRUMP ANNOUNCES MAJOR ECONOMIC CAMPAIGN AGAINST IRAN President Trump announced sweeping ne"
- MS (Morgan Stanley) score 10.8 — "Power Finance Corporation and REC shares fall up to 3% after Morgan Stanley downgrade"
- MRNA (Moderna, Inc.) score 10.6 — "Moderna’s 177% Surge Burns Shorts in ‘Painful’ $5.5 Billion Loss"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.3 — "The national debt just hit $40 trillion. Here’s how it can hurt Americans."
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.8 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Current Price Update"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 8.7 — "Korean investors dump home stocks for US ones, buy same names at a premium | Is KOSPI-styl"
- JEF (Jefferies Financial Group Inc.) score 8.0 — "Why Jefferies sees limited upside in Bajaj Housing Finance despite its fast-growing loan b"
- META (Meta) score 7.9 — "Metal stock to be in focus on Thursday after this Capex expansion update. Details here"
- VT (Vanguard Total World Stock Ind) score 7.8 — "World's Largest Electric Plane Flies for 27 Minutes on $5 of Power"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.7 — "ICICI Bank Share Price Live Updates: ICICI Bank's Current Price and Daily Change"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 6.5 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.0 — "Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month"
- VOLTAS.NS (VOLTAS LTD) score 2.8 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.5 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.4 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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