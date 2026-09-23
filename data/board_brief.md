# Transmission Layer — board brief · 2026-09-23 22:56Z

data as of **2026-09-23** · 97 series · 8 red / 38 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.378, 4d in regime; vol-pct 0.131, breadth-off 0.625, Markov P(high-vol) 0.027)
- [INVERTED] **safe_haven_gold** — corr20 -0.52, corr60 -0.37, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.83, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.11, corr60 0.3, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.19, corr60 0.12, last shift 2026-08-10. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.78, corr60 -0.8, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.06, corr60 -0.06, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.08, corr60 -0.04, last shift 2026-07-31. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.39, corr60 0.24, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.0018708734390282533)
- **SETUP** dyn_tna → asx_200: leads 1d (ccf 0.57, β 0.1126, p 0.0); driver zc -1.65 → expected -0.612%. Type hit-rate 0.821 (n=2374).
- **SETUP** russell_2000 → asx_200: leads 1d (ccf 0.569, β 0.3334, p 0.0); driver zc -1.61 → expected -0.6%. Type hit-rate 0.821 (n=2374).
- **SETUP** dyn_tna → nikkei_225: leads 1d (ccf 0.502, β 0.2051, p 0.0); driver zc -1.65 → expected -1.114%. Type hit-rate 0.821 (n=2374).
- **SETUP** russell_2000 → nikkei_225: leads 1d (ccf 0.499, β 0.6048, p 0.0); driver zc -1.61 → expected -1.087%. Type hit-rate 0.821 (n=2374).
- **SETUP** dyn_tna → taiwan_weighted: leads 1d (ccf 0.466, β 0.1855, p 0.0); driver zc -1.65 → expected -1.008%. Type hit-rate 0.821 (n=2374).
- **SETUP** russell_2000 → taiwan_weighted: leads 1d (ccf 0.462, β 0.5454, p 0.0); driver zc -1.61 → expected -0.981%. Type hit-rate 0.821 (n=2374).
- **SETUP** dyn_tna → kospi: leads 1d (ccf 0.354, β 0.2129, p 0.0); driver zc -1.65 → expected -1.156%. Type hit-rate 0.821 (n=2374).
- **SETUP** russell_2000 → kospi: leads 1d (ccf 0.353, β 0.6291, p 0.0); driver zc -1.61 → expected -1.131%. Type hit-rate 0.821 (n=2374).
- **SETUP** dyn_tna → nifty_metal: leads 1d (ccf 0.271, β 0.1012, p 0.00123); driver zc -1.65 → expected -0.549%. Type hit-rate 0.821 (n=2374).
- **SETUP** russell_2000 → nifty_metal: leads 1d (ccf 0.269, β 0.2981, p 0.00123); driver zc -1.61 → expected -0.536%. Type hit-rate 0.821 (n=2374).
- **SETUP** dyn_tna → nifty_midcap_100: leads 1d (ccf 0.259, β 0.0751, p 1e-05); driver zc -1.65 → expected -0.408%. Type hit-rate 0.821 (n=2374).
- **SETUP** russell_2000 → nifty_midcap_100: leads 1d (ccf 0.257, β 0.2213, p 1e-05); driver zc -1.61 → expected -0.398%. Type hit-rate 0.821 (n=2374).
- Track record · residual_reversion: hit-rate **0.495** (n=1098) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.821** (n=2374) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.75] natgas ↑
- natgas [COMMODITIES]: last 3.17, z20 5.75, zc 2.17, resid-z 3.11 [unexplained], 1d 6.98%, 1-session move +6.98% ≥ 5.0%; |z20|=5.75
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.112 vs natgas, historically leads by 4d
- Source: Hormuz Supply Crisis to Change LNG Market Forever — OilPrice, 2026-09-23. https://oilprice.com/Energy/Natural-Gas/Hormuz-Supply-Crisis-to-Change-LNG-Market-Forever.html
- Source: TotalEnergies to Develop Offshore Gas Field to Boost Nigeria LNG Supply — OilPrice, 2026-09-23. https://oilprice.com/Latest-Energy-News/World-News/TotalEnergies-to-Develop-Offshore-Gas-Field-to-Boost-Nigeria-LNG-Supply.html
- Source: Washington Needs This LNG Deal More Than Beijing Does — OilPrice, 2026-09-23. https://oilprice.com/Energy/Natural-Gas/Washington-Needs-This-LNG-Deal-More-Than-Beijing-Does.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [RED 8.09] fx · 4 series ↓
- usd_mxn [FX]: last 17.53, z20 4.42, zc 4.29, resid-z 4.22 [unexplained], 1d 1.82%, |z20|=4.42
- gbp_usd [FX]: last 1.32, z20 -3.45, zc -2.66, resid-z -2.52 [unexplained], 1d -0.96%, |z20|=3.45
- aud_usd [FX]: last 0.70, z20 -3.20, zc -2.49, resid-z -2.50 [unexplained], 1d -1.08%, |z20|=3.20
- eur_usd [FX]: last 1.14, z20 -3.04, zc -2.18, resid-z -1.69 [unexplained], 1d -0.67%, |z20|=3.04; 1y-pct=4
- **Mechanism**: fx · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_icicigi_bo (rho -0.418 via gbp_usd, z -0.18, quiet); dyn_muthootfin_ns (rho 0.402 via aud_usd, z -0.31, quiet); dyn_inoxindia_ns (rho 0.352 via aud_usd, z 0.3, quiet)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.55 vs aud_usd, historically leads by 3d
- **India receivers**: dyn_icicigi_bo (rho -0.418, z -0.18); dyn_muthootfin_ns (rho 0.402, z -0.31); dyn_inoxindia_ns (rho 0.352, z 0.3)
- Source: Philip R. Lane: The Outlook for the Euro Area Economy — ECB press, 2026-09-23. https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260923_1~ac21bf46e3.en.pdf
- Source: Almost ten million people took part in ECB survey on new euro banknotes — ECB press, 2026-09-23. https://www.ecb.europa.eu//press/pr/date/2026/html/ecb.pr260923~6ebddaf01e.en.html
- Source: Sterling and Wilson Renewable Energy shares rally 8% after securing Rs 985 crore domestic and global orders — ET Markets, 2026-09-22. https://economictimes.indiatimes.com/markets/stocks/news/sterling-and-wilson-renewable-energy-shares-rally-8-after-securing-rs-985-crore-domestic-and-global-orders/articleshow/134402652.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [AMBER 6.76] cross-asset · 8 series ↑
- dyn_ms [EQUITIES]: last 198.43, z20 -2.27, zc -0.47, resid-z -1.67 [unexplained], 1d -0.89%, |z20|=2.27
- dyn_bond [EQUITIES]: last 88.13, z20 -1.85, zc -3.06, resid-z 0.59 [priced], 1d -1.03%, 1y-pct=0
- russell_2000 [INDICES]: last 2838.83, z20 -1.77, zc -1.61, resid-z -1.87 [unexplained], 1d -1.80%, |z20|=1.77
- dow_jones [INDICES]: last 51523.30, z20 -1.61, zc -0.85, resid-z -0.47 [quiet], 1d -0.66%, |z20|=1.61
- ust_2y [RATES]: last 4.71, z20 1.27, zc -0.80, resid-z -1.41 [quiet], 1d -1.05%, 1y-pct=98
- tips_10y_real [RATES]: last 2.63, z20 1.22, zc 0.20, resid-z -0.25 [quiet], 1d 0.38%, 1y-pct=99
- ust_10y [RATES]: last 4.96, z20 1.00, zc 0.00, resid-z -0.34 [quiet], 1d 0.00%, 1y-pct=97
- ust_30y [RATES]: last 5.29, z20 0.26, zc 0.00, resid-z -0.16 [quiet], 1d 0.00%, 1y-pct=96
- **Mechanism**: cross-asset · 8 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.38 via ust_2y, z 0.98, quiet)
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.747 vs dyn_ms, historically leads by 4d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.728 vs dyn_ms, historically leads by 4d
- Watch next: dyn_dell (co-move) — not yet - watch; rho 0.615 vs dyn_ms, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.591 vs dyn_ms, historically leads by 4d
- Watch next: brent (inverse) — not yet - watch; rho -0.556 vs dyn_bond, historically leads by 3d
- **India receivers**: midcap_largecap_ratio (rho -0.38, z 0.98)
- Source: Here's what happens to the economy when Treasury yields soar like they are now — CNBC Economy, 2026-09-23. https://www.cnbc.com/2026/09/23/what-happens-to-the-economy-when-treasury-yields-soar.html
- Source: US stocks fall as 10-year Treasury yield hits highest since 2007 — Mint Markets, 2026-09-23. https://www.livemint.com/market/us-stocks-fall-as-10-year-treasury-yield-hits-highest-since-2007-11790195978698.html
- Source: US stocks: US market ends down as oil prices, Treasury yields rise — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-us-market-ends-down-as-oil-prices-treasury-yields-rise/articleshow/134445625.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-14 (d=0.59), 2025-05-12 (d=0.67)

### [RED 5.96] dxy ↑
- dxy [FX]: last 101.11, z20 2.96, zc 1.74, resid-z 0.54 [moved], 1d 0.57%, 20d range extreme; |z20|=2.96
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [AMBER 5.26] wti ↓
- wti [COMMODITIES]: last 92.45, z20 -0.26, zc -0.78, resid-z -1.08 [quiet], 1d -2.26%, 1-session move -2.26% ≥ 1.5%
- **Mechanism**: wti ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.977 vs wti
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.621 vs wti
- Watch next: sp500 (inverse) — not yet - watch; rho -0.598 vs wti
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.542 vs wti
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.519 vs wti
- Source: US stocks: US market ends down as oil prices, Treasury yields rise — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-us-market-ends-down-as-oil-prices-treasury-yields-rise/articleshow/134445625.cms
- Source: Hormuz Workarounds Keep Gulf Oil Flowing—at a Steep Cost — OilPrice, 2026-09-23. https://oilprice.com/Energy/Crude-Oil/Hormuz-Workarounds-Keep-Gulf-Oil-Flowingat-a-Steep-Cost.html
- Source: Wall Street falls as oil prices, Treasury yields rise — Mint Markets, 2026-09-23. https://www.livemint.com/market/wall-street-falls-as-oil-prices-treasury-yields-rise-11790188753276.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

### [AMBER 5.16] cross-asset · 2 series ↑
- nasdaq_100 [INDICES]: last 30470.18, z20 2.33, zc -0.60, resid-z 1.67 [unexplained], 1d -0.84%, |z20|=2.33; 1y-pct=97
- dyn_nvda [EQUITIES]: last 225.51, z20 0.79, zc -0.60, resid-z 0.10 [quiet], 1d -1.47%, 1y-pct=96
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.926 vs nasdaq_100, historically leads by 2d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.912 vs nasdaq_100, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.66 vs nasdaq_100, historically leads by 2d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.607 vs nasdaq_100
- Watch next: dyn_dell (co-move) — not yet - watch; rho 0.567 vs nasdaq_100
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US 10-year Treasury yield tops 5% for first time since 2007; Nasdaq slumps over 1% — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/url-dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-war-hormuz-deal-brent-crude-oil-fed-warsh-trump-xi-meet-un-jpmorgan-chase-uber-airbnb-meta-apple-amazon-chip-stock-price-news-23th-september-2026/liveblog/134437316.cms
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks slide as oil, strong data drive bond yields higher — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/url-dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-war-hormuz-deal-brent-crude-oil-fed-warsh-trump-xi-meet-un-jpmorgan-chase-uber-airbnb-meta-apple-amazon-chip-stock-price-news-23th-september-2026/liveblog/134437316.cms
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks end down as oil prices, Treasury yields rise — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/url-dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-war-hormuz-deal-brent-crude-oil-fed-warsh-trump-xi-meet-un-jpmorgan-chase-uber-airbnb-meta-apple-amazon-chip-stock-price-news-23th-september-2026/liveblog/134437316.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-04 (d=0.11), 2025-08-28 (d=0.2)

### [RED 4.87] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 5760.00, z20 2.87, zc 0.85, resid-z 0.40 [quiet], 1d 3.04%, |z20|=2.87; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_justdial_bo (rho 0.366 via dyn_4417_t, z 0.69, quiet)
- **India receivers**: dyn_justdial_bo (rho 0.366, z 0.69)
- Source: Sebi board is set to grow. Experts say it's missing one safeguard it needs most — Mint Markets, 2026-09-23. https://www.livemint.com/market/stock-market-news/sebi-board-expansion-securities-markets-code-2025-appointmentprocess-11788844688106.html
- Source: How to invest amid heightened uncertainty? Look at multi-asset allocation funds, say experts — Mint Markets, 2026-09-22. https://www.livemint.com/market/stock-market-news/how-to-invest-amid-heightened-uncertainty-look-at-multi-asset-allocation-funds-say-experts-11790078842845.html
- Source: Vedanta Aluminium stock jumps 4% days after hitting 52-week low! Can it reclaim demerger level? Experts decode outlook — Mint Markets, 2026-09-22. https://www.livemint.com/market/stock-market-news/vedanta-aluminium-stock-jumps-4-days-after-hitting-52-week-low-can-it-reclaim-demerger-level-experts-decode-outlook-11790062916085.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

### [AMBER 4.77] crypto · 2 series ↑
- btc_usd [CRYPTO]: last 84567.73, z20 1.94, zc -0.52, resid-z -0.18 [quiet], 1d -1.86%, |z20|=1.94
- eth_usd [CRYPTO]: last 2690.56, z20 1.90, zc -0.55, resid-z 0.17 [quiet], 1d -2.26%, |z20|=1.90
- **Mechanism**: crypto · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-04-16 (z-distance 0.06).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cartrade_ns (rho 0.367 via eth_usd, z -0.2, quiet)
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.536 vs btc_usd, historically leads by 1d
- **India receivers**: dyn_cartrade_ns (rho 0.367, z -0.2)
- Source: Bitcoin holds near $86,000 as spot Bitcoin ETF inflows hit 11-month high of $999 million — ET Markets, 2026-09-23. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-holds-near-86000-as-spot-bitcoin-etf-inflows-hit-11-month-high-of-999-million/articleshow/134432852.cms
- Source: $3 trillion crypto comeback: Can Bitcoin bulls reclaim $100K and push higher? — ET Markets, 2026-09-22. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/3-trillion-crypto-comeback-can-bitcoin-bulls-reclaim-100k-and-push-higher/articleshow/134412450.cms
- Source: Bitcoin jumps nearly 5% to cross $85,000 as strong ETF inflows and institutional buying boost crypto momentum — ET Markets, 2026-09-22. https://economictimes.indiatimes.com/markets/cryptocurrency/bitcoin-jumps-nearly-5-to-cross-85000-as-strong-etf-inflows-and-institutional-buying-boost-crypto-momentum/articleshow/134406404.cms
- Historical analogues: 2026-04-16 (d=0.06), 2026-01-06 (d=0.11), 2026-08-27 (d=0.12)

## Watchlist (below surfacing floor)
dyn_bac ↓ (4.28), dyn_chkp ↑ (4.13), dyn_meta ↑ (4.13), gold_silver_ratio ↓ (4.06), midcap_largecap_ratio ↑ (3.98), comex_copper ↑ (3.73), dyn_tech ↑ (3.68), comex_gold ↓ (3.62), dyn_voltas_ns ↓ (2.99), sofr ↑ (2.6), taiwan_weighted ↑ (2.31), dyn_hdb ↓ (2.19)

## India macro
- nifty_50: 23446.8008 (1d 0.50%, z20 -0.69, flag none)
- nifty_midcap_100: 62391.4492 (1d 0.70%, z20 -0.38, flag none)
- usd_inr: 95.7300 (1d 0.02%, z20 0.81, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6610 (1d 0.20%, z20 0.98, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 67.5 — "NLC India raises ₹500 crore via issuance of commercial papers"
- INOXINDIA.NS (INOX INDIA LIMITED) score 65.8 — "NLC India raises ₹500 crore via issuance of commercial papers"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 65.1 — "NLC India raises ₹500 crore via issuance of commercial papers"
- INDIANB.NS (INDIAN BANK) score 52.0 — "SEBI plans to review merchant banking and IPO rules"
- COIN (Coinbase Global, Inc.) score 51.1 — "Global Market: European shares edge higher as lower oil prices lift sentiment"
- OHI (Omega Healthcare Investors, In) score 47.0 — "Top stocks in focus today: Investors must watch GHCL, Max Estates, Bharat Dynamics shares "
- BAC (Bank of America Corporation) score 44.9 — "SEBI plans to review merchant banking and IPO rules"
- HDB (HDFC Bank Limited) score 42.6 — "Sedemac Mechatronics block deal: A91, Xponentia, HDFC Life likely to offload 10% stake: Re"
- CHKP (Check Point Software Technolog) score 40.8 — "Nifty outlook, guide tomorrow: Why 23,600 matters; bullish candle formed, check resistance"
- IDBI.NS (IDBI BANK LIMITED) score 38.1 — "SEBI plans to review merchant banking and IPO rules"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 38.1 — "SEBI plans to review merchant banking and IPO rules"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 38.1 — "SEBI plans to review merchant banking and IPO rules"
- BOND (PIMCO Active Bond Exchange-Tra) score 30.8 — "Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks slide as oil, strong data driv"
- LTH (Life Time Group Holdings, Inc.) score 28.7 — "FIVE-YEAR TREASURY YIELD RISES TO 5% FOR FIRST TIME SINCE 2007"
- TECHM.NS (TECH MAHINDRA LIMITED) score 28.2 — "ANTHROPIC LEADERS BACK AI-ERA BIODEFENSE STARTUP Two Anthropic leaders invested in Pilgrim"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 28.2 — "ANTHROPIC LEADERS BACK AI-ERA BIODEFENSE STARTUP Two Anthropic leaders invested in Pilgrim"
- TECH (Bio-Techne Corp) score 28.2 — "ANTHROPIC LEADERS BACK AI-ERA BIODEFENSE STARTUP Two Anthropic leaders invested in Pilgrim"
- SEPN (Septerna, Inc.) score 27.7 — "Stock market prediction for today: Sensex, Nifty outlook for Thursday | Kospi, Taiwan cues"
- 301077.SZ (CHINASTARS) score 25.3 — "BESSENT AFTER MEETING WITH CHINA'S HE: WE'RE FINE WITH EITHER CONTINUING BUSAN ARRANGEMENT"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 22.1 — "Top breakout stocks to buy today: Aptus, KRBL, Tata Steel, Radico, GNFC by Sumeet Bagadia "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 22.1 — "Top breakout stocks to buy today: Aptus, KRBL, Tata Steel, Radico, GNFC by Sumeet Bagadia "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.8 — "IRAN'S PRESIDENT PEZESHKIAN: IRAN NEEDS NUCLEAR ENERGY NOT NUCLEAR BOMB"
- JIOFIN.BO (Jio Financial Services Limited) score 17.4 — "The ingredients for a financial reckoning are all in place"
- BZ=F (Brent Crude Oil Last Day Finan) score 14.9 — "U.S. TREASURY YIELD ON 10-YEAR TREASURY NOTE HITS 5.081%, HIGHEST SINCE JULY 17, 2007; LAS"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.8 — "MCDONALD’S CEO: HIGH INFLATION IS HERE TO STAY McDonald’s CEO Chris Kempczinski says weak "
- META (Meta) score 10.8 — "Why physical gold sales lost sheen on Ganesha Chaturthi? Will yellow metal regain its glit"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 10.0 — "3 cheers: SS Retail, Hero Motors, Jindal Supreme end sharply higher on listing day"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.9 — "Five Adani firms pay ₹1.51 crore to settle SEBI proceedings"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 8.3 — "Sebi board is set to grow. Experts say it's missing one safeguard it needs most"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 8.0 — "Social Security overpaid my 82-year-old mother by $20,000. What else is hiding in her fina"
- PINELABS.NS (PINE LABS LIMITED) score 6.0 — "Pine Labs shares: Over 25% up in a month; Motilal Oswal sees 30% more upside | Buy rating "
- VT (Vanguard Total World Stock Ind) score 5.3 — "‘Built for the World in India’: Nippon AMC’s Sikka sees manufacturing opportunity amid glo"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.0 — "Stylam Industries gets BUY from ICICI Direct; 21% upside seen — check price target"
- MS (Morgan Stanley) score 4.8 — "DIMON WARNS AGAINST PUNISHING INDIA OVER RUSSIAN OIL JPMorgan CEO Jamie Dimon says the U.S"
- GS (Goldman Sachs Group, Inc. (The) score 4.6 — "Goldman Sees China Oil Imports Staying Subdued in Fourth Quarter"
- TNA (Direxion Small Cap Bull 3X ETF) score 4.3 — "Small-cap stocks trade at nearly twice Nifty 50 valuation, says VK Vijayakumar"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.0 — "ADIA sells 2.01% stake in Lenskart Solutions for ₹2,390 crore"
- NVDA (NVIDIA Corporation) score 3.5 — "Why Apple could soon join Nvidia in the exclusive $5 trillion club"
- VOLTAS.NS (VOLTAS LTD) score 1.1 — "Voltas share price: Nuvama upgrades rating but Jefferies cuts target price after analyst m"
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