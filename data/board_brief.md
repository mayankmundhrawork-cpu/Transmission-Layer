# Transmission Layer — board brief · 2026-09-24 09:17Z

data as of **2026-09-24** · 97 series · 10 red / 38 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.662, 1d in regime; vol-pct 0.507, breadth-off 0.818, Markov P(high-vol) 0.027)
- [INVERTED] **safe_haven_gold** — corr20 -0.53, corr60 -0.36, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.84, corr60 0.85, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 -0.05, corr60 0.23, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.1, corr60 0.12, last shift 2026-08-11. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.78, corr60 -0.8, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.01, corr60 -0.08, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.08, corr60 -0.04, last shift 2026-08-04. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.4, corr60 0.16, last shift 2026-07-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **4 of 89** scanned series survive multiplicity control (effective p ≤ 0.002288413662045352)
- **SETUP** russell_2000 → nikkei_225: leads 1d (ccf 0.499, β 0.6046, p 0.0); driver zc -1.61 → expected -1.087%. Type hit-rate 0.823 (n=2389).
- **SETUP** russell_2000 → taiwan_weighted: leads 1d (ccf 0.462, β 0.5439, p 0.0); driver zc -1.61 → expected -0.978%. Type hit-rate 0.823 (n=2389).
- **SETUP** russell_2000 → kospi: leads 1d (ccf 0.353, β 0.6293, p 0.0); driver zc -1.61 → expected -1.132%. Type hit-rate 0.823 (n=2389).
- Track record · residual_reversion: hit-rate **0.495** (n=1095) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.823** (n=2389) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 16.91] cross-asset · 3 series ↓
- dyn_policybzr_ns [EQUITIES]: last 1282.30, z20 -13.59, zc -11.19, resid-z -15.88 [unexplained], 1d -32.02%, |z20|=13.59; 1y-pct=0
- nifty_midcap_100 [INDICES]: last 61097.80, z20 -1.63, zc -2.85, resid-z -1.92 [unexplained], 1d -2.07%, |z20|=1.63
- india_vix [INDICES]: last 12.69, z20 1.52, zc 3.98, resid-z n/a [moved], 1d 22.58%, 1-session move +22.58% ≥ 15.0%; |z20|=1.52
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-07 (z-distance 0.05).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho -0.666 via india_vix, z -1.62, reacted); midcap_largecap_ratio (rho 0.59 via nifty_midcap_100, z -0.38, quiet); nifty_metal (rho 0.53 via nifty_midcap_100, z -0.43, quiet); dyn_jiofin_bo (rho 0.529 via nifty_midcap_100, z -1.44, reacted); dyn_indianb_ns (rho 0.5 via nifty_midcap_100, z -1.71, reacted)
- Watch next: midcap_largecap_ratio (co-move) — not yet - watch; rho 0.59 vs nifty_midcap_100
- Watch next: nifty_metal (co-move) — not yet - watch; rho 0.53 vs nifty_midcap_100
- **India receivers**: nifty_50 (rho -0.666, z -1.62); midcap_largecap_ratio (rho 0.59, z -0.38); nifty_metal (rho 0.53, z -0.43); dyn_jiofin_bo (rho 0.529, z -1.44)
- Source: IRDAI shocker! From ICICI Bank to PB Fintech - A look at most and least impacted bank, NBFC and insurance stocks — Mint Markets, 2026-09-24. https://www.livemint.com/market/stock-market-news/irdai-shocker-from-icici-bank-to-pb-fintech-a-look-at-most-and-least-impacted-bank-nbfc-and-insurance-stocks-11790239361588.html
- Source: Info Edge shares plunge 7% as bloodbath in PB Fintech shares wipes off Rs 1,809 crore from recruiter's stake. What lies ahead? — ET Markets, 2026-09-24. https://economictimes.indiatimes.com/markets/stocks/news/info-edge-shares-plunge-7-as-bloodbath-in-pb-fintech-shares-wipes-off-rs-1809-crore-from-recruiters-stake-what-lies-ahead/articleshow/134456914.cms
- Source: ₹85,000 crore gone! PB Fintech to HDFC Bank — these 5 financial stocks witness highest wealth erosion on IRDAI's move — Mint Markets, 2026-09-24. https://www.livemint.com/market/stock-market-news/rs-85-000-crore-gone-pb-fintech-to-hdfc-bank-these-5-financial-stocks-witness-highest-wealth-erosion-on-irdais-move-11790233480906.html
- Historical analogues: 2025-07-07 (d=0.05), 2025-12-31 (d=0.21), 2025-07-21 (d=0.35)

### [RED 10.13] natgas ↑
- natgas [COMMODITIES]: last 3.18, z20 5.13, zc 1.61, resid-z 0.92 [moved], 1d 5.09%, 1-session move +5.09% ≥ 5.0%; |z20|=5.13
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: gold_silver_ratio (co-move) — not yet - watch; rho 0.049 vs natgas, historically leads by 4d
- Source: Southeast Asia Keeps Building Gas Plants Despite Hormuz LNG Shock — OilPrice, 2026-09-24. https://oilprice.com/Latest-Energy-News/World-News/Southeast-Asia-Keeps-Building-Gas-Plants-Despite-Hormuz-LNG-Shock.html
- Source: Hormuz Supply Crisis to Change LNG Market Forever — OilPrice, 2026-09-23. https://oilprice.com/Energy/Natural-Gas/Hormuz-Supply-Crisis-to-Change-LNG-Market-Forever.html
- Source: TotalEnergies to Develop Offshore Gas Field to Boost Nigeria LNG Supply — OilPrice, 2026-09-23. https://oilprice.com/Latest-Energy-News/World-News/TotalEnergies-to-Develop-Offshore-Gas-Field-to-Boost-Nigeria-LNG-Supply.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [RED 7.79] fx · 4 series ↓
- usd_mxn [FX]: last 17.56, z20 4.13, zc 3.73, resid-z 3.72 [unexplained], 1d 1.59%, |z20|=4.13
- gbp_usd [FX]: last 1.32, z20 -3.36, zc -2.34, resid-z -2.54 [unexplained], 1d -0.83%, |z20|=3.36
- aud_usd [FX]: last 0.70, z20 -3.31, zc -2.70, resid-z -2.76 [unexplained], 1d -1.16%, |z20|=3.31
- eur_usd [FX]: last 1.14, z20 -2.88, zc -2.00, resid-z -1.81 [unexplained], 1d -0.60%, |z20|=2.88; 1y-pct=2
- **Mechanism**: fx · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.517 via usd_mxn, z -13.59, reacted); dyn_icicigi_bo (rho -0.484 via gbp_usd, z 1.44, reacted); dyn_muthootfin_ns (rho 0.46 via aud_usd, z -0.5, quiet); dyn_inoxindia_ns (rho -0.458 via usd_mxn, z -0.77, quiet); nifty_50 (rho 0.373 via eur_usd, z -1.62, reacted)
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.413 vs eur_usd, historically leads by 1d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.51 vs gbp_usd
- **India receivers**: dyn_policybzr_ns (rho -0.517, z -13.59); dyn_icicigi_bo (rho -0.484, z 1.44); dyn_muthootfin_ns (rho 0.46, z -0.5); dyn_inoxindia_ns (rho -0.458, z -0.77)
- Source: Philip R. Lane: The Outlook for the Euro Area Economy — ECB press, 2026-09-23. https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260923_1~ac21bf46e3.en.pdf
- Source: Almost ten million people took part in ECB survey on new euro banknotes — ECB press, 2026-09-23. https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260923~6ebddaf01e.en.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [AMBER 7.76] cross-asset · 9 series ↑
- dyn_ms [EQUITIES]: last 198.43, z20 -2.27, zc -0.47, resid-z -1.67 [unexplained], 1d -0.89%, |z20|=2.27
- dyn_bond [EQUITIES]: last 88.13, z20 -1.85, zc -3.06, resid-z 0.59 [priced], 1d -1.03%, 1y-pct=0
- russell_2000 [INDICES]: last 2838.83, z20 -1.77, zc -1.61, resid-z -1.73 [unexplained], 1d -1.80%, |z20|=1.77
- dow_jones [INDICES]: last 51523.30, z20 -1.61, zc -0.85, resid-z 0.59 [quiet], 1d -0.66%, |z20|=1.61
- ust_2y [RATES]: last 4.71, z20 1.27, zc -0.80, resid-z -1.41 [quiet], 1d -1.05%, 1y-pct=98
- tips_10y_real [RATES]: last 2.63, z20 1.22, zc 0.20, resid-z -0.25 [quiet], 1d 0.38%, 1y-pct=99
- ust_10y [RATES]: last 4.96, z20 1.00, zc 0.00, resid-z -0.34 [quiet], 1d 0.00%, 1y-pct=97
- ust_30y [RATES]: last 5.29, z20 0.26, zc 0.00, resid-z -0.16 [quiet], 1d 0.00%, 1y-pct=96
- brent [COMMODITIES]: last 100.28, z20 0.12, zc -0.99, resid-z 0.91 [quiet], 1d -2.72%, 1-session move -2.72% ≥ 1.5%
- **Mechanism**: cross-asset · 9 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.742 vs dyn_ms, historically leads by 4d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.722 vs dyn_ms, historically leads by 4d
- Watch next: dyn_dell (co-move) — not yet - watch; rho 0.61 vs dyn_ms, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.583 vs dyn_ms, historically leads by 4d
- Watch next: wti (inverse) — not yet - watch; rho -0.517 vs dyn_bond, historically leads by 3d
- Source: Morgan Stanley: Diesel Export Ban Would Push U.S. Gas Prices Higher — OilPrice, 2026-09-24. https://oilprice.com/Latest-Energy-News/World-News/Morgan-Stanley-Says-Diesel-Export-Ban-Would-Push-US-Gas-Prices-Higher.html
- Source: US Market: Is 6% the new threshold for Treasury yields? — ET Markets, 2026-09-24. https://economictimes.indiatimes.com/markets/us-stocks/news/us-market-is-6-the-new-threshold-for-treasury-yields/articleshow/134456819.cms
- Source: Sensex slides 813 points, financial stocks tumble as crude oil and bond yields pressure markets — BusinessLine Mkts, 2026-09-24. https://www.thehindubusinessline.com/markets/sensex-slides-813-points-financial-stocks-tumble-as-crude-oil-and-bond-yields-pressure-markets/article71503302.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-14 (d=0.65), 2025-05-12 (d=0.74)

### [RED 5.49] dxy ↑
- dxy [FX]: last 101.19, z20 2.49, zc 0.25, resid-z 0.54 [quiet], 1d 0.09%, 20d range extreme; |z20|=2.49; 1y-pct=95
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [AMBER 5.16] cross-asset · 2 series ↑
- nasdaq_100 [INDICES]: last 30470.18, z20 2.33, zc -0.60, resid-z 1.67 [unexplained], 1d -0.84%, |z20|=2.33; 1y-pct=97
- dyn_nvda [EQUITIES]: last 225.51, z20 0.79, zc -0.60, resid-z 0.10 [quiet], 1d -1.47%, 1y-pct=96
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.925 vs nasdaq_100, historically leads by 2d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.91 vs nasdaq_100
- Watch next: vix (inverse) — not yet - watch; rho -0.653 vs nasdaq_100, historically leads by 2d
- Watch next: dyn_dell (co-move) — not yet - watch; rho 0.561 vs nasdaq_100
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.503 vs nasdaq_100
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US 10-year Treasury yield tops 5% for first time since 2007; Nasdaq slumps over 1% — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/url-dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-war-hormuz-deal-brent-crude-oil-fed-warsh-trump-xi-meet-un-jpmorgan-chase-uber-airbnb-meta-apple-amazon-chip-stock-price-news-23th-september-2026/liveblog/134437316.cms
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks slide as oil, strong data drive bond yields higher — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/url-dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-war-hormuz-deal-brent-crude-oil-fed-warsh-trump-xi-meet-un-jpmorgan-chase-uber-airbnb-meta-apple-amazon-chip-stock-price-news-23th-september-2026/liveblog/134437316.cms
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks end down as oil prices, Treasury yields rise — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/url-dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-war-hormuz-deal-brent-crude-oil-fed-warsh-trump-xi-meet-un-jpmorgan-chase-uber-airbnb-meta-apple-amazon-chip-stock-price-news-23th-september-2026/liveblog/134437316.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-04 (d=0.11), 2025-08-28 (d=0.2)

### [AMBER 5.12] wti ↓
- wti [COMMODITIES]: last 94.03, z20 -0.12, zc 0.71, resid-z -1.19 [quiet], 1d 2.03%, 1-session move +2.03% ≥ 1.5%
- **Mechanism**: wti ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.902 vs wti
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.623 vs wti
- Watch next: sp500 (inverse) — not yet - watch; rho -0.591 vs wti
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.51 vs wti
- Source: Sensex slides 813 points, financial stocks tumble as crude oil and bond yields pressure markets — BusinessLine Mkts, 2026-09-24. https://www.thehindubusinessline.com/markets/sensex-slides-813-points-financial-stocks-tumble-as-crude-oil-and-bond-yields-pressure-markets/article71503302.ece
- Source: Oil India is beating ONGC. Can its production edge last? — Mint Markets, 2026-09-24. https://www.livemint.com/market/mark-to-market/ongc-oil-india-share-price-production-growth-crude-oil-11790228253135.html
- Source: Gulf nations have found ways to keep oil flowing through the Iran war, but the costs are mounting — BusinessLine Mkts, 2026-09-24. https://www.thehindubusinessline.com/markets/commodities/gulf-nations-have-found-ways-to-keep-oil-flowing-through-the-iran-war-but-the-costs-are-mounting/article71502877.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

### [AMBER 4.28] dyn_bac ↓
- dyn_bac [EQUITIES]: last 56.01, z20 -2.28, zc -0.20, resid-z -2.46 [unexplained], 1d -0.34%, |z20|=2.28
- **Mechanism**: dyn_bac ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Nuclear Safety Brings America Into Russia's Uzbek Energy Project — OilPrice, 2026-09-22. https://oilprice.com/Energy/Energy-General/Nuclear-Safety-Brings-America-Into-Russias-Uzbek-Energy-Project.html
- Source: Oil could top $150 a barrel if supplies tighten further, Bank of America warns — MarketWatch Top, 2026-09-22. https://www.marketwatch.com/story/oil-could-top-150-a-barrel-if-supplies-further-tighten-bank-of-america-warns-2fcd5bd3?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

## Watchlist (below surfacing floor)
dyn_chkp ↑ (4.13), dyn_meta ↑ (4.13), dyn_4417_t ↑ (4.06), dyn_stylebaaza_ns ↓ (4.0), comex_gold ↓ (3.91), dyn_tech ↑ (3.68), nifty_50 ↓ (3.62), gold_silver_ratio ↓ (3.58), dyn_voltas_ns ↓ (3.49), dyn_jiofin_bo ↓ (3.44), comex_copper ↑ (3.36), dyn_indusindbk_bo ↓ (3.14)

## India macro
- nifty_50: 23101.5000 (1d -1.47%, z20 -1.62, flag amber)
- nifty_midcap_100: 61097.8008 (1d -2.07%, z20 -1.63, flag amber)
- usd_inr: 95.9275 (1d 0.25%, z20 1.14, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6448 (1d -0.61%, z20 -0.38, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 86.1 — "NSE set for trading debut as India’s biggest stock exchange, modest gains seen"
- INOXINDIA.NS (INOX INDIA LIMITED) score 84.6 — "NSE set for trading debut as India’s biggest stock exchange, modest gains seen"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 83.9 — "NSE set for trading debut as India’s biggest stock exchange, modest gains seen"
- INDIANB.NS (INDIAN BANK) score 63.1 — "Indian copper producers seek GST cut to 5% as record prices lock up working capital"
- COIN (Coinbase Global, Inc.) score 52.2 — "Global Market: Chinese yuan dips as dollar gains on Fed hike bets; Trump-Xi talks eyed"
- HDB (HDFC Bank Limited) score 49.6 — "Explained: Why PB Fintech, Turtlemint, SBI Life, HDFC Life and other insurance stocks tank"
- BAC (Bank of America Corporation) score 47.6 — "HDFC Bank share price down 25% in 2026 - Opportunity for bottom fishing ahead of new CEO a"
- OHI (Omega Healthcare Investors, In) score 45.5 — "Moneyview mobilises ₹327.5 crore from anchor investors ahead of IPO"
- IDBI.NS (IDBI BANK LIMITED) score 41.5 — "HDFC Bank share price down 25% in 2026 - Opportunity for bottom fishing ahead of new CEO a"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 41.5 — "HDFC Bank share price down 25% in 2026 - Opportunity for bottom fishing ahead of new CEO a"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 41.5 — "HDFC Bank share price down 25% in 2026 - Opportunity for bottom fishing ahead of new CEO a"
- CHKP (Check Point Software Technolog) score 40.9 — "NSE IPO listing time today: Check share listing price prediction ahead of BSE debut - Will"
- TECHM.NS (TECH MAHINDRA LIMITED) score 35.6 — "Explained: Why PB Fintech, Turtlemint, SBI Life, HDFC Life and other insurance stocks tank"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 35.6 — "Explained: Why PB Fintech, Turtlemint, SBI Life, HDFC Life and other insurance stocks tank"
- TECH (Bio-Techne Corp) score 35.6 — "Explained: Why PB Fintech, Turtlemint, SBI Life, HDFC Life and other insurance stocks tank"
- BOND (PIMCO Active Bond Exchange-Tra) score 33.9 — "Indian bonds set for selloff as US yields, oil prices fuel rate hike bets"
- LTH (Life Time Group Holdings, Inc.) score 32.0 — "NSE IPO listing time today: Check share listing price prediction ahead of BSE debut - Will"
- SEPN (Septerna, Inc.) score 29.1 — "Raja Venkatraman recommends three stocks for 24 September"
- 301077.SZ (CHINASTARS) score 23.9 — "China, Hong Kong stocks decline as Trump-Xi talks face investor scepticism"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 21.0 — "Tata Motors PV Share Price Live Updates: Tata Motors PV's Price Decline Continues"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 21.0 — "Tata Motors PV Share Price Live Updates: Tata Motors PV's Price Decline Continues"
- JIOFIN.BO (Jio Financial Services Limited) score 20.7 — "Jio Financial Services Share Price Live Updates: Jio Financial Services experiences a down"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 19.8 — "Dividend, stock split record date alert: Last chance to buy today - Noble Polymers, Naturi"
- BZ=F (Brent Crude Oil Last Day Finan) score 15.5 — "Dividend, stock split record date alert: Last chance to buy today - Noble Polymers, Naturi"
- META (Meta) score 12.8 — "Global Market: Japan's Nikkei rises as CPU stocks surge on Meta gadget launch"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.8 — "IPO reality check! Is GMP a useful signal or just market noise? Here’s what experts think"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 10.5 — "World heads into food crises 'blind' as U.S. aid cuts squeeze UN food agency, experts warn"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 9.0 — "3 cheers: SS Retail, Hero Motors, Jindal Supreme end sharply higher on listing day"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.0 — "Five Adani firms pay ₹1.51 crore to settle SEBI proceedings"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 8.2 — "Bank, financial stocks tumble as IRDAI flags high insurance payouts; Axis Bank, IDFC First"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.5 — "IRDAI paper impact: Insurance stocks crash - PB Fintech, HDFC Life, ICICI Prudential, Turt"
- MS (Morgan Stanley) score 7.3 — "Morgan Stanley employee accidentally leaks bank’s Asia investment pipeline details"
- VT (Vanguard Total World Stock Ind) score 6.8 — "World heads into food crises 'blind' as U.S. aid cuts squeeze UN food agency, experts warn"
- POLICYBZR.NS (PB FINTECH LIMITED) score 6.0 — "PB Fintech among 4 F&O stocks with a sharp rise in futures open interest"
- PINELABS.NS (PINE LABS LIMITED) score 5.4 — "Pine Labs shares: Over 25% up in a month; Motilal Oswal sees 30% more upside | Buy rating "
- GS (Goldman Sachs Group, Inc. (The) score 4.2 — "Goldman Sees China Oil Imports Staying Subdued in Fourth Quarter"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.6 — "ADIA sells 2.01% stake in Lenskart Solutions for ₹2,390 crore"
- NVDA (NVIDIA Corporation) score 3.2 — "Why Apple could soon join Nvidia in the exclusive $5 trillion club"
- VOLTAS.NS (VOLTAS LTD) score 2.0 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 0.1 — "Why Dell and HPE were the S&P 500’s top-performing stocks today"

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