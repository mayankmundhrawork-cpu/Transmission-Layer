# Transmission Layer — board brief · 2026-10-15 23:44Z

data as of **2026-10-15** · 97 series · 11 red / 28 amber · 8 events surfaced (28 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.673, 9d in regime; vol-pct 0.64, breadth-off 0.706, Markov P(high-vol) 0.021)
- [INVERTED] **safe_haven_gold** — corr20 -0.42, corr60 -0.43, contra nifty_50 corr20=0.37, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.87, corr60 0.84, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.22, corr60 0.21, last shift 2026-07-10. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.19, corr60 0.14, last shift 2026-08-25. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.78, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.1, corr60 -0.03, last shift 2026-08-11. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.05, corr60 -0.24, last shift 2026-08-14. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.76, corr60 0.23, last shift 2026-07-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.001577691388751301)
- **SETUP** dyn_hdb → usd_inr: leads 1d (ccf -0.357, β -0.0898, p 0.0); driver zc 2.49 → expected -0.353%. Type hit-rate 0.821 (n=2177).
- **SETUP** dyn_bond → eur_usd: leads 1d (ccf 0.261, β 0.3684, p 2e-05); driver zc 1.98 → expected 0.249%. Type hit-rate 0.821 (n=2177).
- Track record · residual_reversion: hit-rate **0.496** (n=1143) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.821** (n=2177) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.28] cross-asset · 2 series ↑
- gold_silver_ratio [DERIVED]: last 72.96, z20 2.44, zc n/a, resid-z n/a [quiet], 1d -1.34%, GSR<75 (extreme low); |z20|=2.44
- comex_silver [COMMODITIES]: last 57.33, z20 -1.58, zc 1.10, resid-z 0.59 [quiet], 1d 3.20%, |z20|=1.58
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.825 vs comex_silver, historically leads by 4d
- Watch next: dyn_coin (co-move) — not yet - watch; rho 0.564 vs comex_silver, historically leads by 5d
- Watch next: comex_copper (inverse) — not yet - watch; rho -0.51 vs gold_silver_ratio, historically leads by 3d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.507 vs comex_silver
- Source: Silver futures rise to ₹2.08 lakh per kg — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/markets/gold/silver-futures-rise-to-208-lakh-per-kg/article71586939.ece
- Source: Silver futures plunge 4% on MCX ahead of US CPI; rising oil adds pressure — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/commodities/silver-futures-plunge-4-on-mcx-ahead-of-us-cpi-rising-oil-adds-pressure/articleshow/134946048.cms
- Source: SPOT SILVER FALLS NEARLY 3% TO $57.58/OZ — DeItaone, 2026-10-14. https://t.me/walter_bloomberg/37071
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-29 (d=0.06), 2025-08-12 (d=0.14)

### [RED 7.9] cross-asset · 3 series ↑
- dyn_techm_ns [EQUITIES]: last 1650.00, z20 4.59, zc 2.75, resid-z 1.91 [unexplained], 1d 4.75%, |z20|=4.59
- dyn_tataelxsi_ns [EQUITIES]: last 3700.00, z20 3.51, zc 0.85, resid-z 0.11 [quiet], 1d 2.12%, |z20|=3.51
- nifty_it [INDICES]: last 30719.80, z20 3.38, zc 1.08, resid-z -0.05 [quiet], 1d 1.82%, |z20|=3.38
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.78).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_justdial_bo (rho 0.502 via nifty_it, z 1.06, reacted); nifty_fmcg (rho 0.5 via dyn_tataelxsi_ns, z -0.45, quiet); nifty_50 (rho 0.491 via dyn_techm_ns, z 0.37, quiet); dyn_tatatech_ns (rho 0.479 via nifty_it, z 1.53, reacted); midcap_largecap_ratio (rho -0.418 via dyn_techm_ns, z -3.43, reacted)
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.5 vs dyn_tataelxsi_ns
- **India receivers**: dyn_justdial_bo (rho 0.502, z 1.06); nifty_fmcg (rho 0.5, z -0.45); nifty_50 (rho 0.491, z 0.37); dyn_tatatech_ns (rho 0.479, z 1.53)
- Source: Kotak Mahindra Bank shares rise 2% as HSBC upgrades stock to buy — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/markets/kotak-mahindra-bank-shares-rise-2-as-hsbc-upgrades-stock-to-buy/article71554661.ece
- Source: Q2 Results Highlights, 15 Oct: Wipro PAT rises 9% year-on-year; Tech Mahindra profit jumps 32.7%; Nestlé shares tank after Q2 results; IIFL Finance, IRFC, Polycab, KVB and HDFC AMC report higher PAT; Heritage Foods posts decline — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/markets/q2-results-highlights-wipro-nestle-india-tech-mahindra-jio-financial-persistent-systems-irfc-polycab-hdfc-amc-tata-communication-results-groww-tata-tech-leela-emmvee-15-october-2026/article71586591.ece
- Source: Q2 results: Tech Mahindra dividend, bonus shares - Double delight for 7 lakh investors | Payout, ratio, record date — Mint Markets, 2026-10-15. https://www.livemint.com/market/stock-market-news/q2-results-tech-mahindra-dividend-bonus-shares-double-delight-for-7-lakh-investors-payout-ratio-record-date-11792060760425.html
- Historical analogues: 2025-08-13 (d=0.78), 2025-01-23 (d=0.84), 2025-12-30 (d=0.85)

### [RED 7.38] usd_inr ↓
- usd_inr [FX]: last 95.15, z20 -2.38, zc -0.27, resid-z -0.28 [quiet], 1d -0.14%, 20d range extreme; |z20|=2.38
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.369 via usd_inr, z -0.4, quiet); dyn_karurvysya_ns (rho -0.364 via usd_inr, z 2.27, reacted)
- **India receivers**: dyn_idbi_ns (rho -0.369, z -0.4); dyn_karurvysya_ns (rho -0.364, z 2.27)
- Source: Rupee falls 13 paise to close at 96.88 against US dollar — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/markets/forex/rupee-falls-13-paise-to-close-at-9688-against-us-dollar/article71559337.ece
- Source: Rupee rises 10 paise to 96.65 against US dollar in early trade — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/markets/forex/rupee-rises-10-paise-to-9665-against-us-dollar-in-early-trade/article71558347.ece
- Source: Rupee slides to a five-month low of 96.7/$, yields rise — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/markets/rupee-slides-to-a-five-month-low-of-967-yields-rise/article71556132.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 6.43] midcap_largecap_ratio ↓
- midcap_largecap_ratio [DERIVED]: last 2.57, z20 -3.43, zc n/a, resid-z n/a [quiet], 1d -1.97%, break below 100-DMA; |z20|=3.43
- **Mechanism**: midcap_largecap_ratio ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.523 via midcap_largecap_ratio, z -0.72, quiet); dyn_techm_ns (rho -0.418 via midcap_largecap_ratio, z 4.59, reacted); dyn_cartrade_ns (rho 0.375 via midcap_largecap_ratio, z -0.01, quiet)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.523 vs midcap_largecap_ratio, historically leads by 2d
- **India receivers**: nifty_midcap_100 (rho 0.523, z -0.72); dyn_techm_ns (rho -0.418, z 4.59); dyn_cartrade_ns (rho 0.375, z -0.01)
- Historical analogues: 2025-12-31 (d=0.0), 2025-07-03 (d=0.11), 2025-07-23 (d=0.2)

### [RED 5.08] dyn_301077_sz ↓
- dyn_301077_sz [EQUITIES]: last 19.80, z20 -3.08, zc -0.97, resid-z -1.01 [quiet], 1d -2.80%, |z20|=3.08; 1y-pct=5
- **Mechanism**: dyn_301077_sz ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: India poised to fill fuel export gap as China suspends October shipments — BusinessLine Mkts, 2026-10-15. https://www.thehindubusinessline.com/markets/commodities/india-poised-to-fill-fuel-export-gap-as-china-suspends-october-shipments/article71546098.ece
- Source: Global Market: China stocks fall as hot US inflation data revives rate hike fears — ET Markets, 2026-10-15. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-fall-as-hot-us-inflation-data-revives-rate-hike-fears/articleshow/134957483.cms
- Source: Global Market: China stocks slip as AI selloff deepens, mixed inflation data weighs — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-slip-as-ai-selloff-deepens-mixed-inflation-data-weighs/articleshow/134933453.cms
- Historical analogues: 2026-06-18 (d=0.0), 2026-03-30 (d=0.02), 2026-06-03 (d=0.03)

### [RED 4.92] shanghai_comp ↓
- shanghai_comp [INDICES]: last 3706.48, z20 -2.92, zc -2.24, resid-z -1.24 [moved], 1d -1.61%, |z20|=2.92; 1y-pct=0
- **Mechanism**: shanghai_comp ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_inoxindia_ns (rho 0.391 via shanghai_comp, z -1.48, reacted)
- Watch next: nikkei_225 (co-move) — not yet - watch; rho 0.638 vs shanghai_comp, historically leads by 2d
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.509 vs shanghai_comp, historically leads by 1d
- **India receivers**: dyn_inoxindia_ns (rho 0.391, z -1.48)
- Source: Global Market: China stocks fall as hot US inflation data revives rate hike fears — ET Markets, 2026-10-15. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-fall-as-hot-us-inflation-data-revives-rate-hike-fears/articleshow/134957483.cms
- Source: Global Market: China stocks slip as AI selloff deepens, mixed inflation data weighs — ET Markets, 2026-10-14. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-stocks-slip-as-ai-selloff-deepens-mixed-inflation-data-weighs/articleshow/134933453.cms
- Historical analogues: 2026-06-18 (d=0.0), 2025-12-19 (d=0.02), 2025-09-25 (d=0.03)

### [RED 4.32] kospi ↓
- kospi [INDICES]: last 5484.38, z20 -4.32, zc -3.35, resid-z -1.65 [unexplained], 1d -8.73%, |z20|=4.32
- **Mechanism**: kospi ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho 0.486 via kospi, z -0.56, quiet); dyn_techm_ns (rho -0.407 via kospi, z 4.59, reacted); nifty_it (rho -0.383 via kospi, z 3.38, reacted)
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.928 vs kospi, historically leads by 2d
- Watch next: nikkei_225 (co-move) — not yet - watch; rho 0.832 vs kospi, historically leads by 2d
- **India receivers**: dyn_bajfinance_ns (rho 0.486, z -0.56); dyn_techm_ns (rho -0.407, z 4.59); nifty_it (rho -0.383, z 3.38)
- Historical analogues: 2026-07-10 (d=0.0), 2026-04-02 (d=0.01), 2025-04-01 (d=0.04)

### [RED 4.29] dyn_dell ↓
- dyn_dell [EQUITIES]: last 472.71, z20 -4.29, zc -1.19, resid-z -1.69 [unexplained], 1d -6.93%, |z20|=4.29
- **Mechanism**: dyn_dell ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.621 vs dyn_dell, historically leads by 5d
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.569 vs dyn_dell, historically leads by 5d
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-08 (d=0.18), 2025-10-01 (d=0.3)

## Watchlist (below surfacing floor)
dow_jones ↑ (4.21), dyn_nvda ↓ (4.16), soybeans ↓ (4.15), dyn_hdb ↑ (4.06), rates · 3 series ↑ (3.7), dyn_rs ↑ (3.49), usd_cny ↓ (3.45), dyn_muthootfin_ns ↓ (3.37), eur_usd ↓ (3.02), dyn_4417_t ↑ (3.01), dyn_tech ↑ (2.76), dxy ↑ (2.68)

## India macro
- nifty_50: 22997.3496 (1d 1.66%, z20 0.37, flag none)
- nifty_midcap_100: 59192.0000 (1d -0.35%, z20 -0.72, flag none)
- usd_inr: 95.1513 (1d -0.14%, z20 -2.38, flag red)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5739 (1d -1.97%, z20 -3.43, flag red)
- Next India prints: NSDL FPI flows T-0d · India trade / CAD data T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 118.1 — "India’s Venezuelan oil imports set to hit highest level in nearly seven years"
- INOXINDIA.NS (INOX INDIA LIMITED) score 114.1 — "India’s Venezuelan oil imports set to hit highest level in nearly seven years"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 113.0 — "India’s Venezuelan oil imports set to hit highest level in nearly seven years"
- INDIANB.NS (INDIAN BANK) score 105.9 — "HDFC Bank shares in focus after RBI repo rate hike, loan growth at 16%"
- BAC (Bank of America Corporation) score 94.3 — "HDFC Bank shares in focus after RBI repo rate hike, loan growth at 16%"
- HDB (HDFC Bank Limited) score 87.7 — "HDFC Bank shares in focus after RBI repo rate hike, loan growth at 16%"
- IDBI.NS (IDBI BANK LIMITED) score 83.2 — "HDFC Bank shares in focus after RBI repo rate hike, loan growth at 16%"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 83.2 — "HDFC Bank shares in focus after RBI repo rate hike, loan growth at 16%"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 83.2 — "HDFC Bank shares in focus after RBI repo rate hike, loan growth at 16%"
- TECHM.NS (TECH MAHINDRA LIMITED) score 78.7 — "Kotak Mahindra Bank shares rise 2% as HSBC upgrades stock to buy"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 76.4 — "Goldman Sachs sees 26% return for Asian equities, bets big on tech earnings surge"
- TECH (Bio-Techne Corp) score 76.4 — "Goldman Sachs sees 26% return for Asian equities, bets big on tech earnings surge"
- COIN (Coinbase Global, Inc.) score 67.3 — "Indian stock markets set for weak opening as global cues turn negative"
- OHI (Omega Healthcare Investors, In) score 59.7 — "ANTHROPIC’S IPO VALUATION EXPECTATIONS DROP FROM $2 TRILLION TO $1.5 TRILLION Some investo"
- TGT (Target Corporation) score 42.3 — "ZELENSKYY: RUSSIA LAUNCHED NEARLY 1,000 DRONES AS UKRAINE SEEKS MORE AIR DEFENSE President"
- BOND (PIMCO Active Bond Exchange-Tra) score 39.2 — "JAPAN MOF OFFICIAL SAYS ALWAYS MONITORING MARKET MOVES CAREFULLY, WON'T COMMENT ON EACH ST"
- CHKP (Check Point Software Technolog) score 38.2 — "Newly listed stock has 30% upside potential! JM Financial issues buy call; Check target pr"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 32.3 — "IEA TO ACCELERATE OIL RESERVE RELEASES AS DIESEL SUPPLY TIGHTENS The International Energy "
- LTH (Life Time Group Holdings, Inc.) score 28.6 — "Nifty hits intra-day high on open for the sixth time in 2026"
- RS (Reliance, Inc.) score 27.4 — "Jio Platforms IPO: Uday Kotak draws interesting link between Reliance’s 1977 listing and J"
- SEPN (Septerna, Inc.) score 27.0 — "Pernod Ricard India sales grow 19% in Sept qtr; IPO plan awaits board approval"
- JIOFIN.BO (Jio Financial Services Limited) score 24.8 — "JM Financial, ICICI Securities top IPO deals in H1FY27"
- 301077.SZ (CHINASTARS) score 24.1 — "Central banks’ gold purchases net positive in August as China leads the way"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 23.8 — "Reliance Jio IPO to be listed soon: Why a 12% tariff hike may be coming in 3-4 months? Exp"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 20.7 — "Tata Power shares hits 52-week low; announced Ocean Sun deal buzz"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 20.7 — "Tata Power shares hits 52-week low; announced Ocean Sun deal buzz"
- BZ=F (Brent Crude Oil Last Day Finan) score 18.3 — "CRWV - COREWEAVE SHARES REVERSE DECLINES, LAST UP 2.7%"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 17.9 — "JAPAN SENIOR MINISTRY OF FINANCE OFFICIAL SAYS G7, G20 MEETINGS DID NOT SPECIFICALLY DEBAT"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.9 — "Muthoot Microfin AUM crosses ₹15,300 crore, cost of funds enters single digits"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 13.3 — "Nifty falls below 22,300 at noon as Adani Stocks, ITC, Metals slide"
- NVDA (NVIDIA Corporation) score 12.0 — "GERMANY PLANS MAJOR AI PARTNERSHIP WITH NVIDIA — HANDELSBLATT German Chancellor Friedrich "
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.6 — "Don’t ditch tech stocks just yet. Make these moves to take advantage of the latest AI rese"
- VT (Vanguard Total World Stock Ind) score 10.0 — "U.S. Wants World Bank to Drop Ban on Upstream Oil and Gas Funding"
- GS (Goldman Sachs Group, Inc. (The) score 8.9 — "FED’S HAMMACK WARNS MORE AGGRESSIVE ACTION MAY BE NEEDED TO FIGHT INFLATION Cleveland Fed "
- META (Meta) score 7.4 — "Nifty falls below 22,300 at noon as Adani Stocks, ITC, Metals slide"
- JEF (Jefferies Financial Group Inc.) score 5.9 — "Aditya Birla Capital shares: Up 30% in one year! Jefferies sees 25% more upside; should yo"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 4.2 — "Bajaj Broking rolls out algorithm trading platform for retail investors"
- POLICYBZR.NS (PB FINTECH LIMITED) score 2.2 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
- DELL (Dell Technologies Inc.) score 0.2 — "Piero Cipollone: Interview with Corriere della Sera"
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