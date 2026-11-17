# Transmission Layer — board brief · 2026-11-17 22:17Z

data as of **2026-11-17** · 97 series · 12 red / 31 amber · 8 events surfaced (19 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.825, 2d in regime; vol-pct 0.944, breadth-off 0.706, Markov P(high-vol) 0.054)
- [INVERTED] **safe_haven_gold** — corr20 -0.07, corr60 -0.2, contra nifty_50 corr20=0.33, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.88, corr60 0.84, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.15, corr60 0.1, last shift 2026-09-17. Channel: global copper leads Indian metal equities
- [INVERTED] **inr_oil_channel** — corr20 -0.31, corr60 0.03, last shift 2026-09-01. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.91, last shift 2026-09-23. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.27, corr60 0.0, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.05, corr60 -0.17, last shift 2026-08-11. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.33, corr60 0.3, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.000966848284767563)
- **SETUP** dow_jones → usd_mxn: leads 1d (ccf -0.422, β -0.2559, p 0.0); driver zc -1.69 → expected 0.421%. Type hit-rate 0.818 (n=2073).
- Track record · residual_reversion: hit-rate **0.51** (n=1158) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=2073) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.75] cross-asset · 9 series ↓
- dow_jones [INDICES]: last 50759.13, z20 -3.12, zc -1.69, resid-z -2.05 [unexplained], 1d -1.65%, |z20|=3.12
- russell_2000 [INDICES]: last 2703.29, z20 -2.76, zc -1.03, resid-z -0.74 [quiet], 1d -1.45%, |z20|=2.76
- btc_usd [CRYPTO]: last 64358.19, z20 -2.28, zc -0.24, resid-z -0.34 [quiet], 1d -0.77%, |z20|=2.28
- sp500 [INDICES]: last 7340.63, z20 -2.25, zc -0.82, resid-z -0.25 [quiet], 1d -1.02%, |z20|=2.25
- eth_usd [CRYPTO]: last 1803.17, z20 -2.10, zc -0.21, resid-z -0.16 [quiet], 1d -0.89%, |z20|=2.10
- dyn_coin [EQUITIES]: last 115.04, z20 -2.03, zc -0.86, resid-z -0.11 [quiet], 1d -4.00%, |z20|=2.03; 1y-pct=0
- vix [INDICES]: last 25.45, z20 1.99, zc 1.38, resid-z n/a [quiet], 1d 11.09%, |z20|=1.99
- dyn_nvda [EQUITIES]: last 155.47, z20 -1.92, zc -0.12, resid-z -0.50 [quiet], 1d -0.43%, 1y-pct=0
- nasdaq_100 [INDICES]: last 26996.90, z20 -1.61, zc -0.37, resid-z -1.47 [quiet], 1d -0.74%, |z20|=1.61
- **Mechanism**: cross-asset · 9 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.47).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho -0.419 via dyn_nvda, z 1.69, reacted)
- Watch next: dyn_rs (co-move) — not yet - watch; rho 0.6 vs russell_2000, historically leads by 4d
- Watch next: dyn_schd (co-move) — not yet - watch; rho 0.657 vs dow_jones
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.609 vs sp500
- Watch next: dax (co-move) — not yet - watch; rho 0.584 vs dow_jones
- **India receivers**: dyn_bajfinance_ns (rho -0.419, z 1.69)
- Source: US yields ease as equities drop before Nvidia results — Mint Markets, 2026-11-17. https://www.livemint.com/market/us-yields-ease-as-equities-drop-before-nvidia-results-11794948835861.html
- Source: Wall Street falters ahead of Nvidia earnings, Anthropic debut — Mint Markets, 2026-11-17. https://www.livemint.com/market/wall-street-falters-ahead-of-nvidia-earnings-anthropic-debut-11794943844807.html
- Source: Signature Global-led consortium buys 194 acre land via auction for Rs 194 cr — ET Markets, 2026-11-17. https://economictimes.indiatimes.com/markets/digital-real-estate/realty-news/signature-global-led-consortium-buys-194-acre-land-via-auction-for-rs-194-cr/articleshow/135929748.cms
- Historical analogues: 2026-05-22 (d=0.47), 2025-10-21 (d=0.73), 2025-08-19 (d=1.14)

### [RED 7.33] usd_inr ↓
- usd_inr [FX]: last 93.47, z20 -2.33, zc -1.88, resid-z -1.24 [moved], 1d -0.81%, 20d range extreme; |z20|=2.33
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_havells_ns (rho -0.48 via usd_inr, z 1.55, reacted); dyn_indianb_ns (rho -0.434 via usd_inr, z 1.56, reacted); nifty_it (rho -0.388 via usd_inr, z -1.48, reacted); dyn_bajfinance_ns (rho -0.383 via usd_inr, z 1.69, reacted); dyn_jiofin_bo (rho -0.358 via usd_inr, z 1.21, reacted)
- **India receivers**: dyn_havells_ns (rho -0.48, z 1.55); dyn_indianb_ns (rho -0.434, z 1.56); nifty_it (rho -0.388, z -1.48); dyn_bajfinance_ns (rho -0.383, z 1.69)
- Source: Rupee hits 7-month high on FPI inflows, softer oil prices — BusinessLine Mkts, 2026-11-17. https://www.thehindubusinessline.com/markets/forex/rupee-hits-7-month-high-on-fpi-inflows-softer-oil-prices/article71712359.ece
- Source: Rupee rises 43 paise to close at 93.51 (provisional) against US dollar — BusinessLine Mkts, 2026-11-17. https://www.thehindubusinessline.com/markets/forex/rupee-rises-43-paise-to-close-at-9351-provisional-against-us-dollar/article71711397.ece
- Source: Robust inflows, pullback in shorts lift rupee to seven-month peak — ET Markets, 2026-11-17. https://economictimes.indiatimes.com/markets/forex/forex-news/robust-inflows-pullback-in-shorts-lift-rupee-to-seven-month-peak/articleshow/135921416.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 5.81] cross-asset · 4 series ↓
- comex_copper [COMMODITIES]: last 5.99, z20 -2.15, zc -0.02, resid-z 0.74 [quiet], 1d -0.04%, |z20|=2.15
- comex_gold [COMMODITIES]: last 3851.80, z20 -1.94, zc -0.02, resid-z 0.30 [quiet], 1d -0.03%, |z20|=1.94; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 47.29, z20 -1.86, zc 0.38, resid-z 1.29 [quiet], 1d 1.08%, |z20|=1.86; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 81.45, z20 1.68, zc n/a, resid-z n/a [quiet], 1d -1.10%, |z20|=1.68; 1y-pct=99
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.448 via comex_gold, z 0.65, quiet); dyn_karurvysya_ns (rho 0.428 via comex_gold, z 2.14, reacted)
- **India receivers**: dyn_muthootfin_ns (rho 0.448, z 0.65); dyn_karurvysya_ns (rho 0.428, z 2.14)
- Source: Gold struggles to rebound from one-year low as US dollar, yields advance — Mint Markets, 2026-11-17. https://www.livemint.com/market/gold-struggles-to-rebound-from-one-year-low-as-us-dollar-yields-advance-11794942964000.html
- Source: Call for efforts to drive sustainable growth in gold-loan sector — BusinessLine Mkts, 2026-11-17. https://www.thehindubusinessline.com/markets/gold/call-for-efforts-to-drive-sustainable-growth-in-gold-loan-sector/article71712201.ece
- Source: Today’s Gold Rate in India November 17: Gold prices down in Coimbatore, Nagpur, Visakhapatnam, Surat, Jaipur — BusinessLine Mkts, 2026-11-17. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-coimbatore-nagpur-visakhapatnam-surat-jaipur-lucknow-chandigarh-gold-rates-other-cities-november-17-2026/article71710917.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.34)

### [RED 5.68] fx · 2 series ↓
- eur_usd [FX]: last 1.10, z20 -2.85, zc -0.45, resid-z -0.67 [quiet], 1d -0.17%, |z20|=2.85; 1y-pct=0
- gbp_usd [FX]: last 1.32, z20 -2.27, zc -0.17, resid-z -0.47 [quiet], 1d -0.07%, |z20|=2.27; 1y-pct=3
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Boris Vujčić: Risks and resilience in the euro area financial system — ECB press, 2026-11-16. https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp261116~db374b56ab.en.html
- Source: Yen steady against euro and dollar after soft Japanese GDP data — Mint Markets, 2026-11-16. https://www.livemint.com/market/yen-steady-against-euro-and-dollar-after-soft-japanese-gdp-data-11794791270301.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [RED 5.61] dyn_kaynes_ns ↓
- dyn_kaynes_ns [EQUITIES]: last 2858.00, z20 -3.61, zc -1.50, resid-z -1.65 [unexplained], 1d -4.09%, |z20|=3.61; 1y-pct=0
- **Mechanism**: dyn_kaynes_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-01-23 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.368 via dyn_kaynes_ns, z 1.58, reacted); nifty_metal (rho 0.359 via dyn_kaynes_ns, z 0.84, quiet); dyn_tatatech_ns (rho 0.358 via dyn_kaynes_ns, z -0.55, quiet); dyn_jiofin_bo (rho 0.35 via dyn_kaynes_ns, z 1.21, reacted)
- **India receivers**: nifty_fmcg (rho 0.368, z 1.58); nifty_metal (rho 0.359, z 0.84); dyn_tatatech_ns (rho 0.358, z -0.55); dyn_jiofin_bo (rho 0.35, z 1.21)
- Source: Kaynes Technology stock in pain as Street falls out of love — Mint Markets, 2026-11-17. https://www.livemint.com/market/mark-to-market/kaynes-technology-stock-q2-results-smart-meter-sales-crash-11794899402071.html
- Source: Kaynes Technology shares extend losses, fall another 4%; should investors worry about its Q2 performance? — Mint Markets, 2026-11-17. https://www.livemint.com/market/stock-market-news/kaynes-technology-shares-extend-losses-fall-another-4-should-investors-worry-about-its-q2-performance-11794900682488.html
- Source: Amber Enterprises shares resume losing run, tank over 8% after weak Q2 from peer Kaynes Technology. Is more fall ahead? — Mint Markets, 2026-11-16. https://www.livemint.com/market/stock-market-news/amber-enterprises-shares-resume-losing-run-tank-over-8-after-weak-q2-from-peer-kaynes-technology-is-more-fall-ahead-11794813833370.html
- Historical analogues: 2026-01-23 (d=0.0), 2025-01-23 (d=0.01), 2026-01-06 (d=0.02)

### [RED 5.3] dxy ↑
- dxy [FX]: last 103.55, z20 2.30, zc 0.01, resid-z 0.14 [quiet], 1d 0.00%, 20d range extreme; |z20|=2.30; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-10 (d=0.03), 2025-05-14 (d=0.06)

### [AMBER 5.29] indices · 3 series ↓
- kospi [INDICES]: last 4965.31, z20 -1.97, zc -0.78, resid-z -0.43 [quiet], 1d -2.65%, |z20|=1.97
- taiwan_weighted [INDICES]: last 40146.34, z20 -1.90, zc -0.90, resid-z -0.86 [quiet], 1d -2.18%, |z20|=1.90
- nikkei_225 [INDICES]: last 58965.48, z20 -1.59, zc -0.56, resid-z -0.37 [quiet], 1d -1.17%, |z20|=1.59
- **Mechanism**: indices · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.545 via kospi, z -1.35, reacted); nifty_50 (rho -0.514 via taiwan_weighted, z 1.56, reacted); nifty_it (rho -0.451 via kospi, z -1.48, reacted); nifty_midcap_100 (rho 0.45 via nikkei_225, z 1.43, reacted); dyn_idbi_ns (rho 0.437 via nikkei_225, z -0.23, quiet)
- **India receivers**: midcap_largecap_ratio (rho 0.545, z -1.35); nifty_50 (rho -0.514, z 1.56); nifty_it (rho -0.451, z -1.48); nifty_midcap_100 (rho 0.45, z 1.43)
- Source: Stock market outlook today,17 Nov:Sensex, Nifty prediction-DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-17. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-17-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-cue-11794875550779.html
- Source: Stock market outlook today,16 Nov: Sensex, Nifty prediction-DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-16. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-16-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-11794789061627.html
- Source: JAPAN'S NIKKEI AVERAGE FUTURES UP 0.75% IN EARLY TRADE — DeItaone, 2026-11-15. https://t.me/walter_bloomberg/38547

### [AMBER 5.03] cross-asset · 3 series ↑
- dyn_eternal_ns [EQUITIES]: last 375.05, z20 1.71, zc 0.50, resid-z 0.56 [quiet], 1d 1.06%, 1y-pct=100
- dyn_bajfinance_ns [EQUITIES]: last 1121.10, z20 1.69, zc 0.50, resid-z -0.11 [quiet], 1d 1.00%, 1y-pct=98
- nifty_50 [INDICES]: last 25387.40, z20 1.56, zc 0.34, resid-z -0.11 [quiet], 1d 0.38%, |z20|=1.56
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-02-19 (z-distance 0.49).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.701 via nifty_50, z 1.43, reacted); dyn_jiofin_bo (rho 0.651 via nifty_50, z 1.21, reacted); nifty_fmcg (rho 0.643 via nifty_50, z 1.58, reacted); dyn_indusindbk_bo (rho 0.62 via dyn_bajfinance_ns, z 1.86, reacted); dyn_muthootfin_ns (rho 0.592 via nifty_50, z 0.65, quiet)
- Watch next: india_vix (inverse) — not yet - watch; rho -0.506 vs dyn_bajfinance_ns, historically leads by 1d
- Watch next: nifty_metal (co-move) — not yet - watch; rho 0.575 vs nifty_50
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.55 vs dyn_bajfinance_ns
- **India receivers**: nifty_midcap_100 (rho 0.701, z 1.43); dyn_jiofin_bo (rho 0.651, z 1.21); nifty_fmcg (rho 0.643, z 1.58); dyn_indusindbk_bo (rho 0.62, z 1.86)
- Source: FII inflows spark re-rating, lift Nifty Bank to record high — BusinessLine Mkts, 2026-11-17. https://www.thehindubusinessline.com/markets/fii-inflows-spark-re-rating-lift-nifty-bank-to-record-high/article71711942.ece
- Source: Nifty reclaims pre-war levels intraday as Indian stocks lead Asia with 10% monthly gain — Mint Markets, 2026-11-17. https://www.livemint.com/market/stock-market-news/nifty-reclaims-pre-war-levels-intraday-as-indian-stocks-lead-asia-with-10-monthly-gain-11794923846111.html
- Source: Bank Nifty breaks into uncharted territory as FII billions back India’s bull run — BusinessLine Mkts, 2026-11-17. https://www.thehindubusinessline.com/markets/bank-nifty-breaks-into-uncharted-territory-as-fii-billions-back-indias-bull-run/article71711651.ece
- Historical analogues: 2025-02-19 (d=0.49), 2025-07-21 (d=0.84), 2025-07-11 (d=1.03)

## Watchlist (below surfacing floor)
dyn_blln ↓ (4.65), rates · 3 series ↑ (3.9), dyn_atherenerg_ns ↑ (3.14), eur_inr ↓ (3.1), dyn_4417_t ↑ (2.87), dyn_lth ↑ (2.84), aud_usd ↓ (2.56), shanghai_comp ↓ (2.35), dyn_karurvysya_ns ↑ (2.14), usd_mxn ↓ (1.9), usd_cny ↓ (1.83), usd_brl ↑ (1.82)

## India macro
- nifty_50: 25387.4004 (1d 0.38%, z20 1.56, flag amber)
- nifty_midcap_100: 61728.4492 (1d 0.25%, z20 1.43, flag none)
- usd_inr: 93.4700 (1d -0.81%, z20 -2.33, flag red)
- goi_10y: 7.3800 (1d 4.53%, z20 3.03, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.1400 (1d -5.73%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4315 (1d -0.13%, z20 -1.35, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 79.8 — "Bank Nifty breaks into uncharted territory as FII billions back India’s bull run"
- INOXINDIA.NS (INOX INDIA LIMITED) score 77.3 — "Bank Nifty breaks into uncharted territory as FII billions back India’s bull run"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 75.6 — "Bank Nifty breaks into uncharted territory as FII billions back India’s bull run"
- INDIANB.NS (INDIAN BANK) score 58.4 — "BANK OF AMERICA SURVEY SHOWS BIGGEST TECH STOCK SELLING SINCE 2006 Investors slashed techn"
- NVDA (NVIDIA Corporation) score 56.4 — "Dow plunges over 850 points as Nvidia turmoil deepens selloff in AI stocks: Stock Market H"
- BAC (Bank of America Corporation) score 53.5 — "BANK OF AMERICA SURVEY SHOWS BIGGEST TECH STOCK SELLING SINCE 2006 Investors slashed techn"
- HDB (HDFC Bank Limited) score 47.6 — "BANK OF AMERICA SURVEY SHOWS BIGGEST TECH STOCK SELLING SINCE 2006 Investors slashed techn"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 44.2 — "BANK OF AMERICA SURVEY SHOWS BIGGEST TECH STOCK SELLING SINCE 2006 Investors slashed techn"
- IDBI.NS (IDBI BANK LIMITED) score 44.2 — "BANK OF AMERICA SURVEY SHOWS BIGGEST TECH STOCK SELLING SINCE 2006 Investors slashed techn"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 44.2 — "BANK OF AMERICA SURVEY SHOWS BIGGEST TECH STOCK SELLING SINCE 2006 Investors slashed techn"
- TECHM.NS (TECH MAHINDRA LIMITED) score 43.8 — "BANK OF AMERICA SURVEY SHOWS BIGGEST TECH STOCK SELLING SINCE 2006 Investors slashed techn"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 41.5 — "BANK OF AMERICA SURVEY SHOWS BIGGEST TECH STOCK SELLING SINCE 2006 Investors slashed techn"
- TECH (Bio-Techne Corp) score 41.5 — "BANK OF AMERICA SURVEY SHOWS BIGGEST TECH STOCK SELLING SINCE 2006 Investors slashed techn"
- TGT (Target Corporation) score 34.6 — "ANT - NEW STREET INITIATES ANTHROPIC AT BUY WITH $105 PRICE TARGET New Street Research ana"
- OHI (Omega Healthcare Investors, In) score 31.1 — "BANK OF AMERICA SURVEY SHOWS BIGGEST TECH STOCK SELLING SINCE 2006 Investors slashed techn"
- COIN (Coinbase Global, Inc.) score 26.3 — "AI BUBBLE TOPS GLOBAL MARKET RISKS, BANK OF AMERICA SURVEY FINDS Bank of America's Novembe"
- 301077.SZ (CHINASTARS) score 21.9 — "CHINA, CANADA AGREE TO EXTEND TARIFF RELIEF FOR TWO YEARS"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.8 — "How does EIA account for small differences between energy supply and demand data?"
- BLLN (BillionToOne, Inc.) score 19.9 — "CITI WARNS 95% OF S&P 500 LONG POSITIONS ARE UNDERWATER Citi warns that $45.9 billion in S"
- CHKP (Check Point Software Technolog) score 19.7 — "HDFC Bank vs Axis Bank: Both shares recover after Q2 sell-off; which banking stock offers "
- LTH (Life Time Group Holdings, Inc.) score 18.4 — "Urban Company's  ₹2,500-crore QIP oversubscribed 6 times, attracts  ₹15,300 crore in bids:"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 16.1 — "Tata Chemicals share price jumps 9%: Volume surge, Tata Sons listing buzz behind the Tata "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 16.1 — "Tata Chemicals share price jumps 9%: Volume surge, Tata Sons listing buzz behind the Tata "
- BOND (PIMCO Active Bond Exchange-Tra) score 15.5 — "BP launches offer to buy back up to $6 billion of bonds"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 13.3 — "Why Silver rates crashed from record high of  ₹4 lakh per kg price to below  ₹1.75 lakh? E"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 12.4 — "After IDBI Bank stake buy, now Fairfax set to sell 13.25% stake in IIFL Finance via  ₹3,45"
- JIOFIN.BO (Jio Financial Services Limited) score 12.4 — "TD - NEARLY 80% OF YOUNG CANADIANS FEEL FINANCIALLY INSECURE, TD SURVEY FINDS A TD Bank su"
- BZ=F (Brent Crude Oil Last Day Finan) score 9.4 — "NVIDIA SHARES EXTEND LOSSES; LAST DOWN 4.2%"
- MS (Morgan Stanley) score 8.3 — "TRUMP DOWNPLAYS MAJOR U.S. SYSTEM OUTAGES, SAYS AMERICANS ARE SAFE President Donald Trump "
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.0 — "Why Iraq Just Fast-Tracked Chevron’s Takeover Of A 14-Billion-Barrel Supergiant"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.6 — "After IDBI Bank stake buy, now Fairfax set to sell 13.25% stake in IIFL Finance via  ₹3,45"
- SCHD (Schwab US Dividend Equity ETF) score 7.0 — "Mahanadi Coalfields IPO: Dividend king in the making? What top official says about Coal In"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.5 — "Stock Market Live Updates | Opening Bell: Sensex gains over 200 pts, Nifty above 25,300; I"
- GS (Goldman Sachs Group, Inc. (The) score 4.6 — "GOLDMAN SACHS CUTS OIL PRICE FORECASTS FOR 2026 AND 2027 Goldman Sachs has lowered its Bre"
- META (Meta) score 4.4 — "Metal stock jumps 17%, inches close to 52-week high after this CAPEX update; will the rall"
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 4.0 — "Kaynes Technology shares extend losses, fall another 4%; should investors worry about its "
- RS (Reliance, Inc.) score 3.3 — "Reliance Bets $1.6 Billion on India's Biogas Boom"
- CRWV (CoreWeave, Inc.) score 2.7 — "COREWEAVE SHARES FOLLOW NVIDIA LOWER, DOWN 6%"
- ETERNAL.NS (ETERNAL LIMITED) score 2.4 — "Eternal among 5 stocks hitting 52-week highs; stock rallies up to 15% in a month"
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 1.1 — "Cochin Shipyard dividend 2026: Last day to buy today | Check record date, payout amount, h"

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