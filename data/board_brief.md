# Transmission Layer — board brief · 2026-10-01 10:55Z

data as of **2026-10-01** · 97 series · 15 red / 40 amber · 8 events surfaced (32 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.697, 6d in regime; vol-pct 0.694, breadth-off 0.7, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.49, corr60 -0.43, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.79, corr60 0.85, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.02, corr60 0.15, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.01, corr60 0.1, last shift 2026-08-18. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.77, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.09, corr60 -0.1, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.3, corr60 -0.15, last shift 2026-08-11. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.45, corr60 0.21, last shift 2026-07-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** bovespa → aud_usd: leads 1d (ccf 0.384, β 0.2225, p 0.0); driver zc 1.59 → expected 0.354%. Type hit-rate 0.823 (n=2375).
- **SETUP** bovespa → usd_mxn: leads 1d (ccf -0.368, β -0.2051, p 0.0); driver zc 1.59 → expected -0.326%. Type hit-rate 0.823 (n=2375).
- Track record · residual_reversion: hit-rate **0.503** (n=1126) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.823** (n=2375) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.36] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4201.50, z20 -1.69, zc 0.39, resid-z 0.43 [quiet], 1d 0.35%, |z20|=1.69; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 61.21, z20 -1.62, zc 0.99, resid-z 0.99 [quiet], 1d 1.85%, |z20|=1.62; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 68.64, z20 1.05, zc n/a, resid-z n/a [quiet], 1d -1.47%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.59 vs comex_silver, historically leads by 1d
- Watch next: dyn_coin (co-move) — not yet - watch; rho 0.501 vs comex_silver, historically leads by 5d
- Watch next: btc_usd (co-move) — not yet - watch; rho 0.572 vs comex_gold
- Source: Gold futures rise to ₹1.50 lakh/10 gm on firm spot demand — BusinessLine Mkts, 2026-10-01. https://www.thehindubusinessline.com/markets/gold/gold-futures-rise-to-150-lakh10-gm-on-firm-spot-demand/article71532369.ece
- Source: Today’s Gold Rate in India October 1: Gold prices down in Delhi, Mumbai, Kolkata, Chennai, Bengaluru — BusinessLine Mkts, 2026-10-01. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-delhi-mumbai-kolkata-chennai-bengaluru-hyderabad-pune-gold-rates-metro-cities-october-1-2026/article71531990.ece
- Source: Today’s Gold Rate in India October 1: Gold prices down in Coimbatore, Nagpur, Visakhapatnam, Surat, Jaipur — BusinessLine Mkts, 2026-10-01. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-coimbatore-nagpur-visakhapatnam-surat-jaipur-lucknow-chandigarh-gold-rates-other-cities-october-1-2026/article71531991.ece
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
- Watch next: brent (co-move) — not yet - watch; rho 0.648 vs ust_30y, historically leads by 3d
- Watch next: wti (co-move) — not yet - watch; rho 0.506 vs ust_30y, historically leads by 3d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.543 vs dyn_bond
- Source: Rupee drops to two-month low as global bond rout deepens, oil jumps — ET Markets, 2026-10-01. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-drops-to-two-month-low-as-global-bond-rout-deepens-oil-jumps/articleshow/134615636.cms
- Source: Rupee drops to two-month low of 96.31/$ as global bond rout deepens, oil jumps — BusinessLine Mkts, 2026-10-01. https://www.thehindubusinessline.com/markets/forex/rupee-drops-to-two-month-low-of-9631-as-global-bond-rout-deepens-oil-jumps/article71532379.ece
- Source: France’s bond market is stumbling. Should Americans care? — MarketWatch Top, 2026-10-01. https://www.marketwatch.com/story/frances-bond-market-is-stumbling-should-americans-care-202ea2af?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 6.73] indices · 2 series ↑
- nikkei_225 [INDICES]: last 68986.97, z20 3.89, zc 2.33, resid-z 1.12 [moved], 1d 3.35%, |z20|=3.89
- taiwan_weighted [INDICES]: last 48281.21, z20 1.69, zc 0.67, resid-z 0.42 [quiet], 1d 0.71%, |z20|=1.69; 1y-pct=100
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.7).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho -0.423 via taiwan_weighted, z -0.79, quiet); dyn_techm_ns (rho -0.415 via taiwan_weighted, z -0.73, quiet)
- Watch next: kospi (co-move) — not yet - watch; rho 0.815 vs nikkei_225
- **India receivers**: nifty_it (rho -0.423, z -0.79); dyn_techm_ns (rho -0.415, z -0.73)
- Source: Global Market: Japan’s Nikkei hits six-week high as chip stocks rally on AI optimism — ET Markets, 2026-10-01. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-hits-six-week-high-as-chip-stocks-rally-on-ai-optimism/articleshow/134609469.cms
- Source: Global Market: Japan’s Nikkei rises as AI stocks track US chip gains — ET Markets, 2026-09-30. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-rises-as-ai-stocks-track-us-chip-gains/articleshow/134581624.cms
- Historical analogues: 2025-12-30 (d=0.7), 2025-07-11 (d=0.77), 2026-06-09 (d=1.0)

### [AMBER 6.39] usd_inr ↑
- usd_inr [FX]: last 96.32, z20 1.39, zc 0.51, resid-z 0.78 [quiet], 1d 0.28%, 20d range extreme; 1y-pct=96
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.354 via usd_inr, z 0.81, quiet)
- **India receivers**: dyn_idbi_ns (rho -0.354, z 0.81)
- Source: Rupee drops to two-month low as global bond rout deepens, oil jumps — ET Markets, 2026-10-01. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-drops-to-two-month-low-as-global-bond-rout-deepens-oil-jumps/articleshow/134615636.cms
- Source: Rupee drops to two-month low of 96.31/$ as global bond rout deepens, oil jumps — BusinessLine Mkts, 2026-10-01. https://www.thehindubusinessline.com/markets/forex/rupee-drops-to-two-month-low-of-9631-as-global-bond-rout-deepens-oil-jumps/article71532379.ece
- Source: US 10-year yield at 24-year high rattles Nifty, rupee and bond markets. Why is India hit hard? — ET Markets, 2026-10-01. https://economictimes.indiatimes.com/markets/bonds/us-10-year-yield-at-24-year-high-rattles-nifty-rupee-and-bond-markets-why-is-india-hit-hard/articleshow/134614052.cms
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2025-09-16 (d=0.01)

### [RED 6.3] fx · 4 series ↓
- usd_mxn [FX]: last 18.19, z20 2.64, zc 1.04, resid-z 1.39 [quiet], 1d 0.81%, |z20|=2.64
- aud_usd [FX]: last 0.69, z20 -2.30, zc -1.09, resid-z -1.53 [unexplained], 1d -0.56%, |z20|=2.30
- eur_usd [FX]: last 1.13, z20 -2.08, zc -1.11, resid-z -0.94 [quiet], 1d -0.35%, |z20|=2.08; 1y-pct=0
- gbp_usd [FX]: last 1.32, z20 -1.55, zc -0.21, resid-z -0.16 [quiet], 1d -0.08%, |z20|=1.55
- **Mechanism**: fx · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.514 via usd_mxn, z -2.24, reacted); dyn_icicigi_bo (rho -0.51 via gbp_usd, z 1.68, reacted); dyn_muthootfin_ns (rho 0.477 via aud_usd, z -2.12, reacted); nifty_metal (rho 0.422 via aud_usd, z -2.95, reacted); nifty_midcap_100 (rho -0.406 via usd_mxn, z -2.52, reacted)
- **India receivers**: dyn_policybzr_ns (rho -0.514, z -2.24); dyn_icicigi_bo (rho -0.51, z 1.68); dyn_muthootfin_ns (rho 0.477, z -2.12); nifty_metal (rho 0.422, z -2.95)
- Source: FOREX-Euro slides to 17-month low, hit by rates and inflation cocktail — ET Markets, 2026-10-01. https://economictimes.indiatimes.com/markets/forex/forex-news/forex-euro-slides-to-17-month-low-hit-by-rates-and-inflation-cocktail/articleshow/134613639.cms
- Source: Global Market: Euro under pressure from energy shock and political risks — ET Markets, 2026-09-30. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-euro-under-pressure-from-energy-shock-and-political-risks/articleshow/134587000.cms
- Source: EURO HITS 16-MONTH LOW AGAINST US DOLLAR, LAST DOWN 0.26% AT $1.13415 — DeItaone, 2026-09-29. https://t.me/walter_bloomberg/36336
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 6.19] cross-asset · 4 series ↓
- nifty_50 [INDICES]: last 22421.95, z20 -2.53, zc -1.36, resid-z -0.60 [quiet], 1d -0.88%, |z20|=2.53; 1y-pct=0
- nifty_midcap_100 [INDICES]: last 58731.25, z20 -2.52, zc -1.06, resid-z -0.64 [quiet], 1d -1.00%, |z20|=2.52
- india_vix [INDICES]: last 14.44, z20 2.46, zc 1.19, resid-z n/a [quiet], 1d 7.01%, |z20|=2.46
- dyn_policybzr_ns [EQUITIES]: last 980.00, z20 -2.24, zc -1.16, resid-z -0.99 [quiet], 1d -7.89%, |z20|=2.24; 1y-pct=0
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.49).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.603 via nifty_midcap_100, z -1.57, reacted); nifty_fmcg (rho 0.589 via nifty_50, z -3.71, reacted); dyn_jiofin_bo (rho 0.588 via nifty_50, z -2.93, reacted); nifty_metal (rho 0.525 via nifty_midcap_100, z -2.95, reacted); dyn_indusindbk_bo (rho 0.485 via nifty_midcap_100, z -2.15, reacted)
- **India receivers**: midcap_largecap_ratio (rho 0.603, z -1.57); nifty_fmcg (rho 0.589, z -3.71); dyn_jiofin_bo (rho 0.588, z -2.93); nifty_metal (rho 0.525, z -2.95)
- Source: Sensex today | Stock Market Live: Sensex falls 650 points, Nifty slips 1%, dragged by auto stocks — BusinessLine Mkts, 2026-10-01. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-1-october-2026/article71528461.ece
- Source: Nifty FMCG falls 6% in six months. Can festive demand trigger a recovery? | Marico, HUL, Tata Consumer among top picks — Mint Markets, 2026-10-01. https://www.livemint.com/market/stock-market-news/nifty-fmcg-falls-6-in-six-months-can-festive-demand-trigger-a-recovery-marico-hul-tata-consumer-among-top-picks-11790847453775.html
- Source: RBI rate hike expected in October? What it means for Sensex, Nifty | Experts decode — Mint Markets, 2026-10-01. https://www.livemint.com/market/stock-market-news/rbi-rate-hike-expected-in-october-what-it-mean-for-sensex-nifty-experts-decode-11790847271851.html
- Historical analogues: 2025-07-21 (d=0.49), 2025-07-14 (d=0.72), 2025-12-30 (d=0.96)

### [AMBER 5.76] brent ↓
- brent [COMMODITIES]: last 99.88, z20 -0.76, zc -1.42, resid-z -0.12 [quiet], 1d -3.53%, 1-session move -3.53% ≥ 1.5%
- **Mechanism**: brent ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: wti (co-move) — not yet - watch; rho 0.908 vs brent, historically leads by 5d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.622 vs brent
- Source: Rupee drops to two-month low as global bond rout deepens, oil jumps — ET Markets, 2026-10-01. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-drops-to-two-month-low-as-global-bond-rout-deepens-oil-jumps/articleshow/134615636.cms
- Source: Rupee drops to two-month low of 96.31/$ as global bond rout deepens, oil jumps — BusinessLine Mkts, 2026-10-01. https://www.thehindubusinessline.com/markets/forex/rupee-drops-to-two-month-low-of-9631-as-global-bond-rout-deepens-oil-jumps/article71532379.ece
- Source: Russia steps up sunflower oil exports to China as war disrupts India trade — BusinessLine Mkts, 2026-10-01. https://www.thehindubusinessline.com/markets/commodities/russia-steps-up-sunflower-oil-exports-to-china-as-war-disrupts-india-trade/article71531478.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.0), 2025-08-14 (d=0.02)

### [AMBER 5.58] cross-asset · 3 series ↓
- dyn_ms [EQUITIES]: last 188.11, z20 -2.26, zc -1.42, resid-z 0.14 [quiet], 1d -2.41%, |z20|=2.26
- dow_jones [INDICES]: last 50924.10, z20 -1.87, zc -1.07, resid-z -1.56 [unexplained], 1d -0.83%, |z20|=1.87
- russell_2000 [INDICES]: last 2797.20, z20 -1.86, zc -0.34, resid-z -0.04 [quiet], 1d -0.38%, |z20|=1.86
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (inverse) — not yet - watch; rho -0.663 vs dow_jones, historically leads by 3d
- Watch next: dyn_dell (co-move) — not yet - watch; rho 0.636 vs dyn_ms, historically leads by 2d
- Watch next: wti (inverse) — not yet - watch; rho -0.613 vs dow_jones, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.588 vs dyn_ms, historically leads by 4d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.724 vs dyn_ms
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US market edges higher as inflation, consumer spending data boost stocks — ET Markets, 2026-09-30. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-iran-war-hormuz-deal-brent-crude-oil-fed-warsh-treasury-bond-meta-openai-boeing-northrop-grumman-ai-chip-stock-price-news-30th-september-2026/liveblog/134594254.cms
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: Dow, S&P 500 dip while Nasdaq rises on modest inflation increase — ET Markets, 2026-09-30. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-iran-war-hormuz-deal-brent-crude-oil-fed-warsh-treasury-bond-meta-openai-boeing-northrop-grumman-ai-chip-stock-price-news-30th-september-2026/liveblog/134594254.cms
- Source: JP Morgan, Goldman Diverge on Hormuz Oil Flow Estimates — OilPrice, 2026-09-30. https://oilprice.com/Latest-Energy-News/World-News/JP-Morgan-Goldman-Diverge-on-Hormuz-Oil-Flow-Estimates.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-27 (d=0.32), 2026-05-14 (d=0.54)

## Watchlist (below surfacing floor)
indices · 4 series ↓ (4.99), dyn_jiofin_bo ↓ (4.93), dxy ↑ (4.87), rates · 2 series ↑ (4.68), dyn_stylebaaza_ns ↓ (4.11), nifty_fmcg ↓ (3.71), nasdaq_100 ↑ (3.16), dyn_hdb ↓ (3.11), dyn_4417_t ↑ (3.1), dyn_nvda ↑ (3.0), nifty_metal ↓ (2.95), dyn_voltas_ns ↓ (2.95)

## India macro
- nifty_50: 22421.9492 (1d -0.88%, z20 -2.53, flag red)
- nifty_midcap_100: 58731.2500 (1d -1.00%, z20 -2.52, flag red)
- usd_inr: 96.3150 (1d 0.28%, z20 1.39, flag amber)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6194 (1d -0.12%, z20 -1.57, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 97.9 — "AI pressure, client caution cloud Indian IT earnings in September quarter"
- COALINDIA.NS (COAL INDIA LTD) score 94.4 — "AI pressure, client caution cloud Indian IT earnings in September quarter"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 92.6 — "AI pressure, client caution cloud Indian IT earnings in September quarter"
- INDIANB.NS (INDIAN BANK) score 66.8 — "Top stocks to buy for short term: Kotak Securities' expert suggests TCS, Axis Bank, Lodha "
- BOND (PIMCO Active Bond Exchange-Tra) score 57.3 — "Markets open lower as FII selling, high bond yields weigh on sentiment"
- COIN (Coinbase Global, Inc.) score 54.4 — "Global Market: Japanese bond yields rise as investors weigh inflation, rate-hike risks"
- TECHM.NS (TECH MAHINDRA LIMITED) score 51.4 — "Double delight Tech Mahindra shareholders: Bonus issue and dividend amount this Diwali sea"
- OHI (Omega Healthcare Investors, In) score 49.5 — "IPO investors strike gold with 7 multibagger stocks in 3 months. Did you miss the bus?"
- BAC (Bank of America Corporation) score 47.5 — "Cars have become unaffordable for many Americans. Here’s what the numbers show."
- CARTRADE.NS (CARTRADE TECH LIMITED) score 47.2 — "Double delight Tech Mahindra shareholders: Bonus issue and dividend amount this Diwali sea"
- TECH (Bio-Techne Corp) score 47.2 — "Double delight Tech Mahindra shareholders: Bonus issue and dividend amount this Diwali sea"
- HDB (HDFC Bank Limited) score 46.8 — "Top stocks to buy for short term: Kotak Securities' expert suggests TCS, Axis Bank, Lodha "
- CHKP (Check Point Software Technolog) score 42.6 — "Double delight Tech Mahindra shareholders: Bonus issue and dividend amount this Diwali sea"
- IDBI.NS (IDBI BANK LIMITED) score 42.1 — "Top stocks to buy for short term: Kotak Securities' expert suggests TCS, Axis Bank, Lodha "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 42.1 — "Top stocks to buy for short term: Kotak Securities' expert suggests TCS, Axis Bank, Lodha "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 42.1 — "Top stocks to buy for short term: Kotak Securities' expert suggests TCS, Axis Bank, Lodha "
- SEPN (Septerna, Inc.) score 37.3 — "AI pressure, client caution cloud Indian IT earnings in September quarter"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 36.2 — "40% return in 6 months! Adani Energy Solutions share price up 5%, outshines Adani Group st"
- LTH (Life Time Group Holdings, Inc.) score 33.4 — "Markets open lower as FII selling, high bond yields weigh on sentiment"
- TGT (Target Corporation) score 26.0 — "Top stocks to buy for short term: Kotak Securities' expert suggests TCS, Axis Bank, Lodha "
- 301077.SZ (CHINASTARS) score 24.6 — "Shows, tours and film as China marks 90 years since the end of the Long March"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 18.6 — "Kotak Mahindra Bank shares climb 4% after naming new MD, CEO - Can the stock rally further"
- BZ=F (Brent Crude Oil Last Day Finan) score 16.7 — "Usual October cheer could be missing after rout last month"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 16.6 — "Power stocks fall despite  ₹1.86 lakh crore PM-DHARA scheme: Tata Power, Adani Power, NTPC"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 16.6 — "Power stocks fall despite  ₹1.86 lakh crore PM-DHARA scheme: Tata Power, Adani Power, NTPC"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 14.8 — "Power stocks fall despite  ₹1.86 lakh crore PM-DHARA scheme: Tata Power, Adani Power, NTPC"
- JIOFIN.BO (Jio Financial Services Limited) score 13.9 — "Macquarie stock recommendations: ICICI Bank, SBI, PayTM to LIC — top 11 financial shares t"
- GS (Goldman Sachs Group, Inc. (The) score 10.2 — "Goldman Sachs pushes Fed rate hike forecast to December"
- POLICYBZR.NS (PB FINTECH LIMITED) score 9.6 — "PB Fintech shares crash 50% from peak, fall below 2021 IPO price. More downside coming?"
- META (Meta) score 9.2 — "Gold price future roadmap: What led to 6% yellow metal fall in Sept 2026? Will Diwali help"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.7 — "Google shows it’s not out of the AI race just yet"
- VT (Vanguard Total World Stock Ind) score 8.4 — "Mexican Peso Becomes World’s Worst as Carry Traders Flee"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 8.3 — "Macquarie stock recommendations: ICICI Bank, SBI, PayTM to LIC — top 11 financial shares t"
- JEF (Jefferies Financial Group Inc.) score 7.0 — "Jefferies is bearish TCS, Wipro, 6 other IT stocks ahead of Q2 results. How many do you ow"
- NVDA (NVIDIA Corporation) score 6.2 — "NVIDIA'S HUANG: WE'RE GOING TO ADVANCE THIS RESPONSIBLY AND SAFELY"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 5.7 — "Retail investors are aggressively piling into this bold contrarian bet through one ETF."
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 5.3 — "Jio Finance, Allianz Europe invest ₹320 cr each in JV Jio Allianz General Insurance"
- MS (Morgan Stanley) score 4.6 — "Morgan Stanley raises Lenskart target price to Rs 718; bull case implies 41% upside. Here’"
- VOLTAS.NS (VOLTAS LTD) score 0.4 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 0.2 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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