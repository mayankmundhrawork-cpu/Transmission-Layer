# Transmission Layer — board brief · 2026-09-30 22:13Z

data as of **2026-09-30** · 97 series · 11 red / 35 amber · 8 events surfaced (24 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.659, 5d in regime; vol-pct 0.611, breadth-off 0.706, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.5, corr60 -0.41, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.8, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 -0.03, corr60 0.1, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.08, corr60 0.12, last shift 2026-08-17. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.77, last shift 2026-08-14. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.09, corr60 -0.11, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.3, corr60 -0.15, last shift 2026-08-10. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.43, corr60 0.21, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** bovespa → aud_usd: leads 1d (ccf 0.386, β 0.2242, p 0.0); driver zc 1.59 → expected 0.357%. Type hit-rate 0.827 (n=2371).
- **SETUP** bovespa → usd_mxn: leads 1d (ccf -0.374, β -0.2084, p 0.0); driver zc 1.59 → expected -0.332%. Type hit-rate 0.827 (n=2371).
- Track record · residual_reversion: hit-rate **0.501** (n=1117) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.827** (n=2371) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.89] cross-asset · 3 series ↓
- comex_silver [COMMODITIES]: last 60.79, z20 -2.23, zc 0.11, resid-z -0.08 [quiet], 1d 0.21%, |z20|=2.23; co-occur[gold_silver] same-direction (channel VALID)
- comex_gold [COMMODITIES]: last 4189.70, z20 -2.11, zc 0.25, resid-z 0.43 [quiet], 1d 0.24%, |z20|=2.11; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 68.92, z20 1.57, zc n/a, resid-z n/a [quiet], 1d 0.03%, GSR<75 (extreme low); |z20|=1.57
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.589 vs comex_silver, historically leads by 1d
- Watch next: eth_usd (co-move) — not yet - watch; rho 0.57 vs comex_gold
- Watch next: btc_usd (co-move) — not yet - watch; rho 0.535 vs comex_silver
- Source: Gold is supposed to be a safe haven when inflation surges. So why isn’t it working that way now? — MarketWatch Top, 2026-09-30. https://www.marketwatch.com/story/gold-is-supposed-to-be-a-safe-haven-when-inflation-surges-so-why-isnt-it-working-that-way-now-45cbb07b?mod=mw_rss_topstories
- Source: Today’s Gold Rate in India September 30: Gold prices up in Coimbatore, Nagpur, Visakhapatnam, Surat and other cities — BusinessLine Mkts, 2026-09-30. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-coimbatore-nagpur-visakhapatnam-surat-jaipur-lucknow-chandigarh-gold-rates-other-cities-september-30-2026/article71527482.ece
- Source: Today’s Gold Rate in India September 30: Gold prices up in Delhi, Mumbai, Kolkata, Chennai, Bengaluru — BusinessLine Mkts, 2026-09-30. https://www.thehindubusinessline.com/markets/gold/gold-price-today-in-delhi-mumbai-kolkata-chennai-bengaluru-hyderabad-pune-gold-rates-metro-cities-september-30-2026/article71527481.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.89] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.59, z20 2.96, zc 0.66, resid-z 0.33 [quiet], 1d 0.54%, |z20|=2.96; 1y-pct=100
- ust_10y [RATES]: last 5.26, z20 2.17, zc 0.36, resid-z -0.10 [quiet], 1d 0.38%, |z20|=2.17; 1y-pct=100
- tips_10y_real [RATES]: last 2.91, z20 2.11, zc 0.16, resid-z -0.39 [quiet], 1d 0.34%, |z20|=2.11; 1y-pct=100
- dyn_bond [EQUITIES]: last 86.99, z20 -2.05, zc -0.21, resid-z -0.95 [quiet], 1d -0.08%, |z20|=2.05; 1y-pct=0
- ust_2y [RATES]: last 4.89, z20 1.46, zc -0.46, resid-z -1.09 [quiet], 1d -0.61%, 1y-pct=99
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.546 vs dyn_bond
- Source: U.S. bond yields post biggest jump in a generation as global rout rattles investors — MarketWatch Top, 2026-09-30. https://www.marketwatch.com/story/u-s-bond-yields-head-for-biggest-jump-in-a-generation-as-global-rout-rattles-investors-7dede2f2?mod=mw_rss_topstories
- Source: Paramount’s mega debt sale reveals how higher bond yields are squeezing corporate America — MarketWatch Top, 2026-09-30. https://www.marketwatch.com/story/paramounts-mega-debt-sale-reveals-how-higher-bond-yields-are-squeezing-corporate-america-e9694ec3?mod=mw_rss_topstories
- Source: France’s 10-year bond yield heads for biggest quarterly surge since 1987 — ET Markets, 2026-09-30. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/frances-10-year-bond-yield-heads-for-biggest-quarterly-surge-since-1987/articleshow/134601116.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 6.12] fx · 3 series ↓
- usd_mxn [FX]: last 18.07, z20 2.80, zc 0.63, resid-z 0.78 [quiet], 1d 0.52%, |z20|=2.80
- aud_usd [FX]: last 0.69, z20 -2.64, zc -1.94, resid-z -2.49 [unexplained], 1d -0.96%, |z20|=2.64
- eur_usd [FX]: last 1.13, z20 -1.99, zc -1.03, resid-z -0.95 [quiet], 1d -0.33%, |z20|=1.99; 1y-pct=0
- **Mechanism**: fx · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.499 via usd_mxn, z -2.31, reacted); dyn_muthootfin_ns (rho 0.425 via aud_usd, z -1.55, reacted); dyn_inoxindia_ns (rho 0.408 via aud_usd, z -1.05, reacted); nifty_midcap_100 (rho -0.381 via usd_mxn, z -2.37, reacted); nifty_50 (rho 0.375 via eur_usd, z -2.23, reacted)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.52 vs aud_usd, historically leads by 3d
- **India receivers**: dyn_policybzr_ns (rho -0.499, z -2.31); dyn_muthootfin_ns (rho 0.425, z -1.55); dyn_inoxindia_ns (rho 0.408, z -1.05); nifty_midcap_100 (rho -0.381, z -2.37)
- Source: Global Market: Euro under pressure from energy shock and political risks — ET Markets, 2026-09-30. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-euro-under-pressure-from-energy-shock-and-political-risks/articleshow/134587000.cms
- Source: EURO HITS 16-MONTH LOW AGAINST US DOLLAR, LAST DOWN 0.26% AT $1.13415 — DeItaone, 2026-09-29. https://t.me/walter_bloomberg/36336
- Source: Euro Falls to 16-Month Low as Hawkish Fed Bets Boost Dollar — Mint Markets, 2026-09-29. https://www.livemint.com/market/euro-falls-to-16-month-low-as-hawkish-fed-bets-boost-dollar-11790707107261.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-02 (d=0.26), 2025-08-15 (d=0.26)

### [AMBER 6.09] brent ↓
- brent [COMMODITIES]: last 97.93, z20 -1.09, zc -1.68, resid-z -2.09 [unexplained], 1d -4.54%, 1-session move -4.54% ≥ 1.5%
- **Mechanism**: brent ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.513 vs brent, historically leads by 5d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.595 vs brent
- Source: Venezuela’s Oil Revival Accelerates as Foreign Companies Return — OilPrice, 2026-09-30. https://oilprice.com/Energy/Energy-General/Venezuelas-Oil-Revival-Accelerates-as-Foreign-Companies-Return.html
- Source: Guyana’s Oil Riches Are Transforming Its Economy at Breakneck Speed — OilPrice, 2026-09-30. https://oilprice.com/Energy/Energy-General/Guyanas-Oil-Riches-Are-Transforming-Its-Economy-at-Breakneck-Speed.html
- Source: Indian rupee rebounds to 95.83 vs US dollar as crude prices ease — ET Markets, 2026-09-30. https://economictimes.indiatimes.com/markets/forex/forex-news/indian-rupee-rebounds-to-95-83-vs-us-dollar-as-crude-prices-ease/articleshow/134600948.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.0), 2025-08-14 (d=0.02)

### [AMBER 6.03] cross-asset · 4 series ↓
- nifty_midcap_100 [INDICES]: last 59321.50, z20 -2.37, zc 0.00, resid-z 0.70 [quiet], 1d 0.00%, |z20|=2.37
- dyn_policybzr_ns [EQUITIES]: last 1063.90, z20 -2.31, zc -0.14, resid-z -0.09 [quiet], 1d -1.58%, |z20|=2.31; 1y-pct=0
- nifty_50 [INDICES]: last 22620.45, z20 -2.23, zc -0.64, resid-z -0.97 [quiet], 1d -0.42%, |z20|=2.23; 1y-pct=1
- india_vix [INDICES]: last 13.46, z20 1.67, zc 0.06, resid-z n/a [quiet], 1d 0.39%, |z20|=1.67
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.49).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.611 via nifty_midcap_100, z -1.45, reacted); dyn_jiofin_bo (rho 0.57 via nifty_50, z -2.59, reacted); nifty_fmcg (rho 0.557 via nifty_50, z -2.49, reacted); dyn_indusindbk_bo (rho 0.476 via nifty_midcap_100, z -1.9, reacted); dyn_techm_ns (rho 0.47 via nifty_50, z -1.13, reacted)
- **India receivers**: midcap_largecap_ratio (rho 0.611, z -1.45); dyn_jiofin_bo (rho 0.57, z -2.59); nifty_fmcg (rho 0.557, z -2.49); dyn_indusindbk_bo (rho 0.476, z -1.9)
- Source: Nifty 50 prediction today: Oversold zone raises counter-trend rally hopes | Support, resistance — Mint Markets, 2026-09-30. https://www.livemint.com/market/stock-market-news/nifty-50-prediction-today-oversold-zone-raises-counter-trend-rally-hopes-support-resistance-11790790026650.html
- Source: 10 Nifty 50 stocks, including Infosys and TCS, posted double-digit losses in September as market sell-off deepens — Mint Markets, 2026-09-30. https://www.livemint.com/market/stock-market-news/10-nifty-50-stocks-including-infosys-and-tcs-posted-double-digit-losses-in-september-as-market-sell-off-deepens-11790786786742.html
- Source: September rout makes history: Nifty posts worst monthly fall in 8 years, worst series drop since 2001 — BusinessLine Mkts, 2026-09-30. https://www.thehindubusinessline.com/markets/september-rout-makes-history-nifty-posts-worst-monthly-fall-in-8-years-worst-series-drop-since-2001/article71528719.ece
- Historical analogues: 2025-07-21 (d=0.49), 2025-07-14 (d=0.72), 2025-12-30 (d=0.96)

### [AMBER 5.58] cross-asset · 3 series ↓
- dyn_ms [EQUITIES]: last 188.11, z20 -2.26, zc -1.41, resid-z 0.14 [quiet], 1d -2.41%, |z20|=2.26
- dow_jones [INDICES]: last 50924.10, z20 -1.87, zc -1.07, resid-z -2.47 [unexplained], 1d -0.83%, |z20|=1.87
- russell_2000 [INDICES]: last 2797.20, z20 -1.86, zc -0.34, resid-z -0.36 [quiet], 1d -0.38%, |z20|=1.86
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.725 vs dyn_ms, historically leads by 4d
- Watch next: dyn_dell (co-move) — not yet - watch; rho 0.594 vs dyn_ms, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.584 vs dyn_ms, historically leads by 4d
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.512 vs dyn_ms
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.506 vs dyn_ms
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US market edges higher as inflation, consumer spending data boost stocks — ET Markets, 2026-09-30. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-iran-war-hormuz-deal-brent-crude-oil-fed-warsh-treasury-bond-meta-openai-boeing-northrop-grumman-ai-chip-stock-price-news-30th-september-2026/liveblog/134594254.cms
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: Dow, S&P 500 dip while Nasdaq rises on modest inflation increase — ET Markets, 2026-09-30. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-iran-war-hormuz-deal-brent-crude-oil-fed-warsh-treasury-bond-meta-openai-boeing-northrop-grumman-ai-chip-stock-price-news-30th-september-2026/liveblog/134594254.cms
- Source: JP Morgan, Goldman Diverge on Hormuz Oil Flow Estimates — OilPrice, 2026-09-30. https://oilprice.com/Latest-Energy-News/World-News/JP-Morgan-Goldman-Diverge-on-Hormuz-Oil-Flow-Estimates.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-27 (d=0.32), 2026-05-14 (d=0.54)

### [RED 4.7] dxy ↑
- dxy [FX]: last 101.46, z20 1.70, zc 0.28, resid-z 0.55 [quiet], 1d 0.09%, 20d range extreme; |z20|=1.70; 1y-pct=98
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-21 (d=0.02), 2025-10-10 (d=0.03)

### [RED 4.68] rates · 2 series ↑
- hy_oas [RATES]: last 3.08, z20 3.84, zc 0.79, resid-z 1.37 [quiet], 1d 1.99%, |z20|=3.84
- ig_oas [RATES]: last 0.84, z20 2.48, zc 0.70, resid-z 1.00 [quiet], 1d 1.20%, |z20|=2.48
- **Mechanism**: rates · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.424 via ig_oas, z -2.31, reacted); nifty_midcap_100 (rho -0.413 via ig_oas, z -2.37, reacted)
- **India receivers**: dyn_policybzr_ns (rho -0.424, z -2.31); nifty_midcap_100 (rho -0.413, z -2.37)
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-01 (d=0.48), 2024-11-04 (d=0.56)

## Watchlist (below surfacing floor)
indices · 2 series ↑ (4.66), dyn_jiofin_bo ↓ (4.59), dyn_icicigi_bo ↑ (4.16), cross-asset · 2 series ↑ (3.99), shanghai_comp ↓ (3.69), indices · 3 series ↓ (3.67), commodities · 2 series ↓ (3.29), dyn_hdb ↓ (3.11), dyn_4417_t ↑ (3.0), dyn_voltas_ns ↓ (2.94), dyn_tech ↑ (2.82), dyn_havells_ns ↓ (2.69)

## India macro
- nifty_50: 22620.4492 (1d -0.42%, z20 -2.23, flag amber)
- nifty_midcap_100: 59321.5000 (1d 0.00%, z20 -2.37, flag amber)
- usd_inr: 95.8200 (1d -0.17%, z20 0.67, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6225 (1d 0.42%, z20 -1.45, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 91.8 — "Indian rupee rebounds to 95.83 vs US dollar as crude prices ease"
- COALINDIA.NS (COAL INDIA LTD) score 90.1 — "Indian rupee rebounds to 95.83 vs US dollar as crude prices ease"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 88.0 — "Indian rupee rebounds to 95.83 vs US dollar as crude prices ease"
- INDIANB.NS (INDIAN BANK) score 61.2 — "Indian rupee rebounds to 95.83 vs US dollar as crude prices ease"
- TECHM.NS (TECH MAHINDRA LIMITED) score 49.3 — "Up 410% in 5 yrs, why MOFSL sees another 52% upside in Time Technoplast- check target pric"
- COIN (Coinbase Global, Inc.) score 49.2 — "U.S. bond yields post biggest jump in a generation as global rout rattles investors"
- BOND (PIMCO Active Bond Exchange-Tra) score 47.9 — "U.S. 10-YEAR YIELD HITS 24-YEAR HIGH The 10-year Treasury yield surged to 5.304%, surpassi"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 46.8 — "Up 410% in 5 yrs, why MOFSL sees another 52% upside in Time Technoplast- check target pric"
- TECH (Bio-Techne Corp) score 46.8 — "Up 410% in 5 yrs, why MOFSL sees another 52% upside in Time Technoplast- check target pric"
- OHI (Omega Healthcare Investors, In) score 45.8 — "Top stocks in focus today: Investors must watch Jio Financial, Infosys, NCC shares on Thu,"
- BAC (Bank of America Corporation) score 39.4 — "TRUMP ON TRUTH SOCIAL: I AM PLEASED TO ANNOUNCE, THE LAST AMERICAN FORCES ARE LEAVING IRAQ"
- CHKP (Check Point Software Technolog) score 39.1 — "Up 410% in 5 yrs, why MOFSL sees another 52% upside in Time Technoplast- check target pric"
- HDB (HDFC Bank Limited) score 38.6 — "BANK OF ENGLAND WARNS OF SHARPER AI MARKET CORRECTION The Bank of England warns AI valuati"
- SEPN (Septerna, Inc.) score 36.5 — "A brutal September for bonds points to an even darker October"
- LTH (Life Time Group Holdings, Inc.) score 35.6 — "PRESIDENT TRUMP — WEDNESDAY, SEPTEMBER 30, 2026 🔸 8:00 AM — Executive Time — White House 🔸"
- IDBI.NS (IDBI BANK LIMITED) score 35.5 — "BANK OF ENGLAND WARNS OF SHARPER AI MARKET CORRECTION The Bank of England warns AI valuati"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 35.5 — "BANK OF ENGLAND WARNS OF SHARPER AI MARKET CORRECTION The Bank of England warns AI valuati"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 35.5 — "BANK OF ENGLAND WARNS OF SHARPER AI MARKET CORRECTION The Bank of England warns AI valuati"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 34.3 — "U.S. 10-YEAR YIELD HITS 24-YEAR HIGH The 10-year Treasury yield surged to 5.304%, surpassi"
- 301077.SZ (CHINASTARS) score 24.4 — "China’s Thermal Coal Prices Surge to Three-Year High"
- TGT (Target Corporation) score 21.6 — "SPCX - NEEDHAM REITERATES SPACEX BUY, $250 TARGET Needham maintains its Buy rating and $25"
- BZ=F (Brent Crude Oil Last Day Finan) score 17.9 — "TRUMP ON TRUTH SOCIAL: I AM PLEASED TO ANNOUNCE, THE LAST AMERICAN FORCES ARE LEAVING IRAQ"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 15.3 — "Tata Group stock! BofA turns bullish on Trent, initiates coverage with Buy, pegs 17% upsid"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 15.3 — "Tata Group stock! BofA turns bullish on Trent, initiates coverage with Buy, pegs 17% upsid"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 14.5 — "Power Mech Projects shares rise 4% after company secures Rs 549 crore order from Adani Gro"
- JIOFIN.BO (Jio Financial Services Limited) score 13.5 — "Top stocks in focus today: Investors must watch Jio Financial, Infosys, NCC shares on Thu,"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 13.1 — "RIL, Infosys, TCS, HUL, HDFC Bank at multi-year lows | Time to look beyond? Experts sugges"
- GS (Goldman Sachs Group, Inc. (The) score 10.3 — "GOLDMAN PUSHES NEXT FED HIKE TO DECEMBER Goldman Sachs now says an October Fed hike is unl"
- POLICYBZR.NS (PB FINTECH LIMITED) score 9.7 — "PB Fintech, Wipro among  8 stocks that hit 52-week low and slipped up to 45% in a month"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.8 — "Global Market: BoE's Taylor says energy prices alone do not justify rate hike"
- VT (Vanguard Total World Stock Ind) score 8.4 — "The World’s Diesel Problem Runs Deeper Than the Iran War"
- NVDA (NVIDIA Corporation) score 7.1 — "NVIDIA'S HUANG: WE'RE GOING TO ADVANCE THIS RESPONSIBLY AND SAFELY"
- META (Meta) score 7.0 — "Nifty Metal slips 5% in September post 29% 1 yr rally, October comeback ahead? Hindustan Z"
- JEF (Jefferies Financial Group Inc.) score 6.8 — "Molbio Diagnostics shares rally 9% as Jefferies initiates 'high conviction top pick' call "
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.1 — "Broker’s Call: ICICI Lombard GIC (Add)"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 6.0 — "Jio Finance, Allianz Europe invest ₹320 cr each in JV Jio Allianz General Insurance"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 5.4 — "US SEC proposes wider retail investor access to private assets amid risk concerns"
- MS (Morgan Stanley) score 5.2 — "Morgan Stanley raises Lenskart target price to Rs 718; bull case implies 41% upside. Here’"
- VOLTAS.NS (VOLTAS LTD) score 0.4 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 0.3 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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