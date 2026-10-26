# Transmission Layer — board brief · 2026-10-26 10:04Z

data as of **2026-10-26** · 97 series · 13 red / 42 amber · 8 events surfaced (30 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.844, 16d in regime; vol-pct 0.78, breadth-off 0.909, Markov P(high-vol) 0.03)
- [INVERTED] **safe_haven_gold** — corr20 -0.35, corr60 -0.37, contra nifty_50 corr20=0.42, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.83, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.08, corr60 0.16, last shift 2026-09-03. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.23, corr60 0.06, last shift 2026-09-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.9, corr60 -0.77, last shift 2026-09-09. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.15, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.04, corr60 -0.14, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.54, corr60 0.24, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **4 of 89** scanned series survive multiplicity control (effective p ≤ 0.003389620038554586)
- **SETUP** dow_jones → asx_200: leads 1d (ccf 0.59, β 0.4873, p 0.0); driver zc -1.63 → expected -0.607%. Type hit-rate 0.823 (n=1843).
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.464, β 0.242, p 0.0); driver zc -3.33 → expected -0.802%. Type hit-rate 0.823 (n=1843).
- **SETUP** dow_jones → usd_brl: leads 1d (ccf -0.405, β -0.338, p 0.0); driver zc -1.63 → expected 0.421%. Type hit-rate 0.823 (n=1843).
- **SETUP** dow_jones → aud_usd: leads 1d (ccf 0.394, β 0.2532, p 2e-05); driver zc -1.63 → expected -0.316%. Type hit-rate 0.823 (n=1843).
- **SETUP** dow_jones → usd_mxn: leads 1d (ccf -0.378, β -0.2329, p 0.0); driver zc -1.63 → expected 0.29%. Type hit-rate 0.823 (n=1843).
- Track record · residual_reversion: hit-rate **0.504** (n=1118) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.823** (n=1843) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.26] cross-asset · 5 series ↓
- ust_10y [RATES]: last 4.96, z20 -3.60, zc -3.33, resid-z -3.95 [unexplained], 1d -3.31%, |z20|=3.60
- ust_2y [RATES]: last 4.65, z20 -3.44, zc -2.66, resid-z -2.93 [unexplained], 1d -3.33%, |z20|=3.44
- tips_10y_real [RATES]: last 2.64, z20 -3.33, zc -2.43, resid-z -2.52 [unexplained], 1d -4.35%, 1d move -12.0bps ≥ 5bps; |z20|=3.33
- ust_30y [RATES]: last 5.29, z20 -2.82, zc -3.30, resid-z -3.38 [unexplained], 1d -2.40%, |z20|=2.82
- dyn_bond [EQUITIES]: last 88.51, z20 2.22, zc -0.52, resid-z 0.08 [quiet], 1d -0.20%, |z20|=2.22
- **Mechanism**: cross-asset · 5 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dxy (inverse) — not yet - watch; rho -0.56 vs dyn_bond
- Source: French bond selloff eases as country spared ratings downgrade — ET Markets, 2026-10-26. https://economictimes.indiatimes.com/markets/bonds/french-bond-selloff-eases-as-country-spared-ratings-downgrade/articleshow/135206922.cms
- Source: Global Market: Japan bond yields edge higher ahead of key central bank meetings — ET Markets, 2026-10-26. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japan-bond-yields-edge-higher-ahead-of-key-central-bank-meetings/articleshow/135204344.cms
- Source: Nifty's PEG ratio near 10-year low but why don't stocks look cheap yet? Valuation paradox explained — ET Markets, 2026-10-26. https://economictimes.indiatimes.com/markets/stocks/news/niftys-peg-ratio-near-10-year-low-but-why-dont-stocks-look-cheap-yet-valuation-paradox-explained/articleshow/135202215.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 8.01] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4031.20, z20 -2.62, zc 0.42, resid-z -2.09 [unexplained], 1d 0.58%, |z20|=2.62; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 54.11, z20 -2.06, zc 0.28, resid-z -0.01 [quiet], 1d 0.74%, |z20|=2.06; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 74.50, z20 1.69, zc n/a, resid-z n/a [quiet], 1d -0.16%, GSR<75 (extreme low); |z20|=1.69
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.507 vs comex_silver, historically leads by 1d
- Watch next: dxy (inverse) — not yet - watch; rho -0.523 vs comex_gold
- Source: Why is gold price under pressure ahead of Dhanteras, Diwali? What should interested buyers do? Experts's views, target — Mint Markets, 2026-10-26. https://www.livemint.com/market/commodities/why-is-gold-price-under-pressure-ahead-of-dhanteras-diwali-what-should-interested-buyers-do-expertss-views-target-11793002314682.html
- Source: Silver prices at 2026 lowest;  ₹2,23,500 away from record high! Right time to buy for good returns? Target price per kg — Mint Markets, 2026-10-26. https://www.livemint.com/market/commodities/silver-prices-at-2026-lowest-rs-2-23-500-away-from-record-high-right-time-to-buy-for-good-returns-target-price-per-kg-11792992915881.html
- Source: Silver prices are tarnished but not forgotten. Why HSBC thinks gains in white metal may be limited? — ET Markets, 2026-10-26. https://economictimes.indiatimes.com/markets/commodities/news/silver-prices-are-tarnished-but-not-forgotten-why-hsbc-thinks-gains-in-white-metal-may-be-limited/articleshow/135207313.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [AMBER 7.15] commodities · 2 series ↑
- wti [COMMODITIES]: last 101.11, z20 1.31, zc -0.71, resid-z 0.90 [quiet], 1d -2.09%, 1-session move -2.09% ≥ 1.5%
- brent [COMMODITIES]: last 109.80, z20 0.93, zc -2.37, resid-z 0.54 [priced], 1d -5.93%, 1-session move -5.93% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.387 via wti, z -2.12, reacted)
- **India receivers**: nifty_midcap_100 (rho -0.387, z -2.12)
- Source: Indian shares on track for muted open as oil concerns persist, Fed in focus — Mint Markets, 2026-10-26. https://www.livemint.com/market/stock-market-news/indian-shares-on-track-for-muted-open-as-oil-concerns-persist-fed-in-focus-11792981672692.html
- Source: Markets claw back from morning lows; Dr. Reddy’s surges 7%, crude eases — BusinessLine Mkts, 2026-10-26. https://www.thehindubusinessline.com/markets/stock-markets/markets-claw-back-from-morning-lows-dr-reddys-surges-7-crude-eases/article71626242.ece
- Source: India's Stock Market Feels the Heat From High Oil Prices — OilPrice, 2026-10-26. https://oilprice.com/Latest-Energy-News/World-News/Indias-Stock-Market-Feels-the-Heat-From-High-Oil-Prices.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 6.75] cross-asset · 6 series ↓
- india_vix [INDICES]: last 17.13, z20 2.60, zc 0.27, resid-z n/a [quiet], 1d 1.62%, |z20|=2.60
- dyn_bajfinance_ns [EQUITIES]: last 920.00, z20 -2.36, zc -0.54, resid-z -0.66 [quiet], 1d -0.96%, |z20|=2.36
- dyn_swiggy_ns [EQUITIES]: last 185.75, z20 -2.16, zc 0.65, resid-z 0.85 [quiet], 1d 5.54%, |z20|=2.16; 1y-pct=0
- nifty_midcap_100 [INDICES]: last 56466.80, z20 -2.12, zc 0.96, resid-z 1.45 [quiet], 1d 1.20%, |z20|=2.12
- dyn_jiofin_bo [EQUITIES]: last 205.15, z20 -2.05, zc 0.05, resid-z -0.23 [quiet], 1d 0.07%, |z20|=2.05; 1y-pct=0
- dyn_policybzr_ns [EQUITIES]: last 1020.60, z20 -0.49, zc 0.18, resid-z -0.43 [quiet], 1d 0.55%, 1y-pct=3
- **Mechanism**: cross-asset · 6 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.79).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho -0.733 via india_vix, z 0.16, quiet); nifty_metal (rho 0.692 via nifty_midcap_100, z -1.24, reacted); nifty_fmcg (rho 0.603 via nifty_midcap_100, z -2.14, reacted); midcap_largecap_ratio (rho 0.597 via nifty_midcap_100, z -2.45, reacted); dyn_indusindbk_bo (rho -0.563 via india_vix, z -1.75, reacted)
- Watch next: nifty_50 (inverse) — not yet - watch; rho -0.733 vs india_vix, historically leads by 1d
- Watch next: dyn_indianb_ns (co-move) — not yet - watch; rho 0.554 vs nifty_midcap_100, historically leads by 1d
- **India receivers**: nifty_50 (rho -0.733, z 0.16); nifty_metal (rho 0.692, z -1.24); nifty_fmcg (rho 0.603, z -2.14); midcap_largecap_ratio (rho 0.597, z -2.45)
- Source: Swiggy shares rise 6% after 4-session down episode; is this a relief rally or worst is over? Experts decode | Target, SL — Mint Markets, 2026-10-26. https://www.livemint.com/market/stock-market-news/swiggy-shares-rise-6-after-4-session-down-episode-is-this-a-relief-rally-or-worst-is-over-experts-decode-target-sl-11792998360954.html
- Source: Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bullish despite target price cuts — ET Markets, 2026-10-26. https://economictimes.indiatimes.com/markets/stocks/news/swiggy-shares-jump-5-a-day-after-q2-results-sparked-a-17-crash-why-brokerages-remain-bullish-despite-target-price-cuts/articleshow/135205591.cms
- Source: Mcap of eight of the top-10 firms erodes by ₹1.55 lakh cr; HDFC Bank, Bajaj Fin biggest laggards — BusinessLine Mkts, 2026-10-25. https://www.thehindubusinessline.com/markets/mcap-of-eight-of-the-top-10-firms-erodes-by-155-lakh-cr-hdfc-bank-bajaj-fin-biggest-laggards/article71622878.ece
- Historical analogues: 2025-07-21 (d=0.79), 2025-05-30 (d=0.88), 2025-07-10 (d=0.91)

### [RED 6.14] dyn_chkp ↑
- dyn_chkp [EQUITIES]: last 159.03, z20 4.14, zc 2.05, resid-z 0.79 [moved], 1d 4.64%, |z20|=4.14
- **Mechanism**: dyn_chkp ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.357 via dyn_chkp, z -1.75, reacted)
- **India receivers**: dyn_indusindbk_bo (rho 0.357, z -1.75)
- Source: Apollo Micro Systems share price jumps 10% after Q2 results; stock up 44% in 2026 — check resistance, support levels — Mint Markets, 2026-10-26. https://www.livemint.com/market/stock-market-news/apollo-micro-systems-share-price-jumps-10-after-q2-results-stock-up-44-in-2026-check-resistance-support-levels-11792987859346.html
- Source: Reliance's Jio Platforms IPO allotment today, 26 Oct: Check status online, latest GMP price, share listing prediction — Mint Markets, 2026-10-26. https://www.livemint.com/market/ipo/reliances-jio-platforms-ipo-allotment-today-26-oct-check-status-online-latest-gmp-price-share-listing-prediction-11792980669475.html
- Source: Paras Healthcare allotment likely today: Check GMP, key details and how to check status — ET Markets, 2026-10-26. https://economictimes.indiatimes.com/markets/stocks/news/paras-healthcare-allotment-likely-today-check-gmp-key-details-and-how-to-check-status/articleshow/135202716.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2025-05-20 (d=0.04)

### [AMBER 6.08] cross-asset · 4 series ↓
- dyn_vt [EQUITIES]: last 155.88, z20 -2.42, zc -0.46, resid-z -1.21 [quiet], 1d -0.41%, |z20|=2.42
- nasdaq_100 [INDICES]: last 28956.07, z20 -2.12, zc -0.01, resid-z -0.62 [quiet], 1d -0.01%, |z20|=2.12
- sp500 [INDICES]: last 7622.99, z20 -1.97, zc -0.63, resid-z -1.84 [unexplained], 1d -0.53%, |z20|=1.97
- vix [INDICES]: last 19.19, z20 1.75, zc -0.16, resid-z n/a [quiet], 1d -1.34%, |z20|=1.75
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-23 (z-distance 0.16).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.777 vs dyn_vt, historically leads by 1d
- Watch next: brent (inverse) — not yet - watch; rho -0.517 vs nasdaq_100, historically leads by 2d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.696 vs dyn_vt
- Watch next: dax (co-move) — not yet - watch; rho 0.617 vs dyn_vt
- Source: Stock market outlook today, 26 Oct: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei cues — Mint Markets, 2026-10-26. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-26-oct-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-cues-11792975256498.html
- Source: US Stock Markets this week: Wall Street gears up for Fed rate decision; Q3 earnings from Alphabet, Microsoft, Amazon — Mint Markets, 2026-10-26. https://www.livemint.com/market/us-stock-markets-this-week-wall-street-gears-up-for-fed-rate-decision-q3-earnings-from-alphabet-microsoft-amazon-11792944787786.html
- Source: Asia Is Building the World’s Next $15 Trillion Energy Market — OilPrice, 2026-10-25. https://oilprice.com/Energy/Energy-General/Asia-Is-Building-the-Worlds-Next-15-Trillion-Energy-Market.html
- Historical analogues: 2025-10-23 (d=0.16), 2026-05-20 (d=0.17), 2025-05-06 (d=0.18)

### [RED 5.72] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1572.60, z20 3.72, zc 4.45, resid-z 4.05 [unexplained], 1d 13.96%, |z20|=3.72
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.384 via dyn_atherenerg_ns, z -2.12, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.384, z -2.12)
- Source: Q2 Results Today Live: Ather Energy logs profit in Q2, ITC Hotels surge after Q2 results, TMB, IOB, APL Apollo, Supreme Industries Q2 PAT rise, Paytm, Tata Consumer, Dalmia Bharat, KFin Tech, Mankind Pharma, BOM, Sona BLW, Nazara, Aequs to announce Q2 results — BusinessLine Mkts, 2026-10-26. https://www.thehindubusinessline.com/markets/q2-results-today-live-updates-paytm-tata-consumer-mankind-pharma-rec-itc-hotels-iob-ather-aegis-logistics-supreme-ind-aequs-nazara-sona-blw-tmb-bom-infosys-kotak-idfc-results-26-october-2026/article71625561.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [AMBER 5.43] cross-asset · 3 series ↓
- dyn_coin [EQUITIES]: last 164.40, z20 -2.11, zc -0.59, resid-z -0.79 [quiet], 1d -2.77%, |z20|=2.11
- btc_usd [CRYPTO]: last 80355.35, z20 -1.87, zc -0.43, resid-z -0.17 [quiet], 1d -0.89%, |z20|=1.87
- eth_usd [CRYPTO]: last 2329.24, z20 -1.67, zc -0.60, resid-z 0.12 [quiet], 1d -2.30%, |z20|=1.67
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-22 (z-distance 0.4).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.386 via btc_usd, z -2.18, reacted)
- **India receivers**: dyn_muthootfin_ns (rho 0.386, z -2.18)
- Source: Global Market: BOJ nears historic inflation milestone, shifts focus to rate hikes — ET Markets, 2026-10-26. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-boj-nears-historic-inflation-milestone-shifts-focus-to-rate-hikes/articleshow/135206926.cms
- Source: Global equity funds attract $28.16 billion as easing yields boost sentiment — ET Markets, 2026-10-26. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-equity-funds-attract-28-16-billion-as-easing-yields-boost-sentiment/articleshow/135206114.cms
- Source: Global Market | SK Hynix weighs $12 billion special dividend ahead of Q3 Results: Reports — ET Markets, 2026-10-26. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-sk-hynix-weighs-12-billion-special-dividend-ahead-of-q3-results-reports/articleshow/135205842.cms
- Historical analogues: 2025-10-22 (d=0.4), 2026-05-22 (d=0.53), 2025-03-31 (d=0.53)

## Watchlist (below surfacing floor)
dyn_meta ↓ (5.35), natgas ↓ (5.22), indices · 2 series ↓ (4.9), dyn_lth ↑ (4.85), cross-asset · 2 series ↑ (4.53), dyn_4417_t ↑ (3.3), shanghai_comp ↓ (3.28), dyn_hdb ↓ (3.27), dyn_rs ↑ (3.25), dyn_tech ↑ (2.82), usd_cny ↓ (2.81), commodities · 2 series ↓ (2.7)

## India macro
- nifty_50: 22753.1992 (1d 0.68%, z20 0.16, flag none)
- nifty_midcap_100: 56466.8008 (1d 1.20%, z20 -2.12, flag amber)
- usd_inr: 95.1850 (1d 0.50%, z20 -0.65, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4817 (1d 0.51%, z20 -2.45, flag amber)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 73.0 — "EAAA India Alternatives secures ₹360 crore from anchor investors ahead of IPO"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 70.2 — "EAAA India Alternatives secures ₹360 crore from anchor investors ahead of IPO"
- INOXINDIA.NS (INOX INDIA LIMITED) score 69.9 — "EAAA India Alternatives secures ₹360 crore from anchor investors ahead of IPO"
- INDIANB.NS (INDIAN BANK) score 63.5 — "NSE Chief warns of AI cyber threats, flags quantum risk as Indian markets hit ₹460 lakh cr"
- BAC (Bank of America Corporation) score 56.3 — "Q2 Results Highlights Oct 24: Kotak Mahindra Bank, AU Small Finance Bank, IDFC First Bank,"
- HDB (HDFC Bank Limited) score 51.4 — "Q2 Results Highlights Oct 24: Kotak Mahindra Bank, AU Small Finance Bank, IDFC First Bank,"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 50.6 — "Q2 Results Highlights Oct 24: Kotak Mahindra Bank, AU Small Finance Bank, IDFC First Bank,"
- IDBI.NS (IDBI BANK LIMITED) score 50.1 — "Q2 Results Highlights Oct 24: Kotak Mahindra Bank, AU Small Finance Bank, IDFC First Bank,"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 50.1 — "Q2 Results Highlights Oct 24: Kotak Mahindra Bank, AU Small Finance Bank, IDFC First Bank,"
- TGT (Target Corporation) score 45.5 — "Trump Targets $6.2 Billion Offshore Wind Project Nearing Completion"
- TECHM.NS (TECH MAHINDRA LIMITED) score 43.0 — "Q2 Results Highlights Oct 24: Kotak Mahindra Bank, AU Small Finance Bank, IDFC First Bank,"
- COIN (Coinbase Global, Inc.) score 41.7 — "Global Market: South Korean shares fall over 1% as AI trade concerns weigh; won strengthen"
- OHI (Omega Healthcare Investors, In) score 40.1 — "EAAA India Alternatives secures ₹360 crore from anchor investors ahead of IPO"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 35.3 — "Q2 Results Highlights Oct 24: Kotak Mahindra Bank, AU Small Finance Bank, IDFC First Bank,"
- TECH (Bio-Techne Corp) score 35.3 — "Q2 Results Highlights Oct 24: Kotak Mahindra Bank, AU Small Finance Bank, IDFC First Bank,"
- CHKP (Check Point Software Technolog) score 29.6 — "Crude Check: Uptrend stays strong"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 24.6 — "Syria's Energy Comeback Could Reshape Middle East Oil and Gas"
- LTH (Life Time Group Holdings, Inc.) score 23.1 — "Global equity funds attract $28.16 billion as easing yields boost sentiment"
- BOND (PIMCO Active Bond Exchange-Tra) score 23.0 — "Crude oil prices, US Fed policy decision to steer rupee, bonds this week"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 22.8 — "India's Finance Ministry pushes broking industry to shed family-firm model, build structur"
- 301077.SZ (CHINASTARS) score 21.6 — "Thousands evacuated and flights grounded as Typhoon Champi hits eastern China"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 20.0 — "India's Finance Ministry pushes broking industry to shed family-firm model, build structur"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 19.5 — "Infosys shares crash 4% - Should investors buy, sell, hold this IT stock after Q2 results?"
- RS (Reliance, Inc.) score 18.1 — "Reliance's Jio Platforms IPO allotment today, 26 Oct: Check status online, latest GMP pric"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 14.4 — "Q2 Results Today Live: Ather Energy logs profit in Q2, ITC Hotels surge after Q2 results, "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 14.4 — "Q2 Results Today Live: Ather Energy logs profit in Q2, ITC Hotels surge after Q2 results, "
- JUSTDIAL.BO (JUST DIAL LTD.) score 12.8 — "Can Undersea Volcanoes Power Cities? A Seattle Startup Just Took the First Step"
- META (Meta) score 12.1 — "Meta to create non-voting shares to fund AI expansion, retain Zuckerberg’s control"
- JEF (Jefferies Financial Group Inc.) score 12.1 — "IndusInd Bank shares rise 2% after Q2 results. Why Jefferies cut target price despite lend"
- JIOFIN.BO (Jio Financial Services Limited) score 11.6 — "U.S. S&P GLOBAL OCTOBER FLASH COMPOSITE PMI AT 57.6 (VS 58.4 IN SEPTEMBER) U.S. S&P GLOBAL"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 11.5 — "Top stocks to buy: Adani Energy, AU Small Finance Bank, BPCL, IDFC First Bank — Jefferies "
- SEPN (Septerna, Inc.) score 10.6 — "Brokerage profits grow in September quarter despite slowdown in market activity"
- BZ=F (Brent Crude Oil Last Day Finan) score 10.5 — "Investors piled a record sum into a leveraged semiconductor ETF last week. Things didn’t w"
- GS (Goldman Sachs Group, Inc. (The) score 6.9 — "Kotak Mahindra Bank shares climb 4% after Q2 results. What are Jefferies, Goldman Sachs sa"
- INFY (Infosys Limited) score 5.5 — "Infosys shares fall 4% after IT major lowers FY27 guidance. What are Goldman Sachs, Nomura"
- SWIGGY.NS (SWIGGY LIMITED) score 5.4 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"
- VT (Vanguard Total World Stock Ind) score 5.2 — "World Is on Track for Up to 2.8 Degrees of Warming Despite Clean Energy Boom"
- WIT (Wipro Limited) score 4.1 — "Top IT stocks to buy after Q2 results: TCS vs Infosys vs Wipro vs HCL vs Tech Mahindra - W"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.2 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
- VOLTAS.NS (VOLTAS LTD) score 0.0 — "Voltas’s market share is growing. Will margins follow?"

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