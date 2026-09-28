# Transmission Layer — board brief · 2026-09-28 10:51Z

data as of **2026-09-28** · 97 series · 13 red / 31 amber · 8 events surfaced (23 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.734, 1d in regime; vol-pct 0.651, breadth-off 0.818, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.54, corr60 -0.41, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.84, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 -0.02, corr60 0.24, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.02, corr60 0.11, last shift 2026-08-10. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.78, corr60 -0.78, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.05, corr60 -0.1, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.26, corr60 -0.11, last shift 2026-08-10. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.42, corr60 0.21, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.495** (n=1106) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.828** (n=2328) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.65] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.47, z20 3.04, zc 1.60, resid-z 1.52 [unexplained], 1d 1.30%, |z20|=3.04; 1y-pct=100
- tips_10y_real [RATES]: last 2.85, z20 2.72, zc 1.50, resid-z 1.81 [unexplained], 1d 3.26%, 1d move +9.0bps ≥ 5bps; |z20|=2.72; 1y-pct=100
- ust_10y [RATES]: last 5.18, z20 2.46, zc 1.29, resid-z 1.20 [quiet], 1d 1.37%, |z20|=2.46; 1y-pct=100
- dyn_bond [EQUITIES]: last 87.70, z20 -1.94, zc 0.36, resid-z -1.69 [unexplained], 1d 0.15%, 1y-pct=0
- ust_2y [RATES]: last 4.87, z20 1.78, zc 0.30, resid-z -0.10 [quiet], 1d 0.41%, |z20|=1.78; 1y-pct=100
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.673 vs ust_30y, historically leads by 3d
- Watch next: wti (co-move) — not yet - watch; rho 0.524 vs ust_30y, historically leads by 3d
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.503 vs ust_10y, historically leads by 4d
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.538 vs ust_10y
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.507 vs ust_30y
- Source: Global Market: Eurozone bond yields rise as oil climbs, inflation data eyed — ET Markets, 2026-09-28. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-eurozone-bond-yields-rise-as-oil-climbs-inflation-data-eyed/articleshow/134538460.cms
- Source: India 10-year yield hits over two-year high as supply angst adds to global woes — ET Markets, 2026-09-28. https://economictimes.indiatimes.com/markets/bonds/india-10-year-yield-hits-over-two-year-high-as-supply-angst-adds-to-global-woes/articleshow/134535660.cms
- Source: Global Market: Hong Kong sets pricing guidance for four-year digital green bond — ET Markets, 2026-09-28. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-hong-kong-sets-pricing-guidance-for-four-year-digital-green-bond/articleshow/134534365.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 6.87] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4190.00, z20 -3.56, zc 0.51, resid-z -0.40 [quiet], 1d -3.04%, |z20|=3.56; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 61.73, z20 -2.75, zc 0.60, resid-z 0.50 [quiet], 1d -3.91%, |z20|=2.75; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 67.88, z20 0.49, zc n/a, resid-z n/a [quiet], 1d 0.91%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.6 vs comex_silver, historically leads by 1d
- Watch next: eth_usd (co-move) — not yet - watch; rho 0.59 vs comex_gold
- Watch next: btc_usd (co-move) — not yet - watch; rho 0.586 vs comex_gold
- Source: Why Gold, silver ETFs tumbled over 4% today | What's behind the fall and what should investors do? — Mint Markets, 2026-09-28. https://www.livemint.com/market/commodities/why-gold-silver-etfs-tumbled-over-4-today-whats-behind-the-fall-and-what-should-investors-do-11790580238197.html
- Source: Gold drops more than 2% on US rate-hike bets — BusinessLine Mkts, 2026-09-28. https://www.thehindubusinessline.com/markets/gold/gold-drops-more-than-2-on-us-rate-hike-bets/article71518649.ece
- Source: Gold prices dip Rs 3,200/10 gram; silver falls Rs 6,700/kg as high oil prices raise rate hike bets. Time to sell? — ET Markets, 2026-09-28. https://economictimes.indiatimes.com/markets/commodities/news/gold-prices-dip-rs-3200/10-gram-silver-falls-rs-6700/kg-as-high-oil-prices-raise-rate-hike-bets-time-to-sell/articleshow/134532168.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.78] cross-asset · 4 series ↓
- dyn_policybzr_ns [EQUITIES]: last 1151.30, z20 -3.12, zc -0.11, resid-z -1.03 [quiet], 1d -1.26%, |z20|=3.12; 1y-pct=0
- india_vix [INDICES]: last 13.74, z20 2.62, zc -0.55, resid-z n/a [quiet], 1d 13.03%, |z20|=2.62
- nifty_midcap_100 [INDICES]: last 59913.20, z20 -2.51, zc -0.14, resid-z -1.03 [quiet], 1d -1.62%, |z20|=2.51
- nifty_50 [INDICES]: last 22780.25, z20 -2.29, zc 0.48, resid-z 0.35 [quiet], 1d -1.56%, |z20|=2.29; 1y-pct=2
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.49).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.586 via nifty_midcap_100, z -1.36, reacted); dyn_jiofin_bo (rho 0.582 via nifty_50, z -2.84, reacted); nifty_fmcg (rho 0.558 via nifty_50, z -1.07, reacted); nifty_metal (rho 0.51 via nifty_midcap_100, z -1.26, reacted); dyn_techm_ns (rho 0.495 via nifty_50, z -0.69, quiet)
- **India receivers**: midcap_largecap_ratio (rho 0.586, z -1.36); dyn_jiofin_bo (rho 0.582, z -2.84); nifty_fmcg (rho 0.558, z -1.07); nifty_metal (rho 0.51, z -1.26)
- Source: Sensex today | Stock Market Live: Sensex, Nifty tumble over 1.5% as broad-based selling grips markets — BusinessLine Mkts, 2026-09-28. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-28-septmeber-2026/article71515691.ece
- Source: Stock market prediction for tomorrow: Sensex, Nifty outlook for Tuesday | Kospi, Taiwan cues to watch | 29 Sept 2026 — Mint Markets, 2026-09-28. https://www.livemint.com/market/stock-market-news/stock-market-prediction-for-tomorrow-sensex-nifty-outlook-for-tuesday-kospi-taiwan-cues-to-watch-29-sept-2026-11790589056945.html
- Source: Nifty 50 Down 12% From Sept 2024 Peak: Motilal Oswal — BusinessLine Mkts, 2026-09-28. https://www.thehindubusinessline.com/markets/nifty-50-down-12-from-september-2024-peak-motilal-oswal/article71518801.ece
- Historical analogues: 2025-07-21 (d=0.49), 2025-07-14 (d=0.72), 2025-12-30 (d=0.96)

### [AMBER 5.12] wti ↑
- wti [COMMODITIES]: last 96.41, z20 0.12, zc -0.82, resid-z -0.87 [quiet], 1d 4.33%, 1-session move +4.33% ≥ 1.5%
- **Mechanism**: wti ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.931 vs wti
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.63 vs wti
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.544 vs wti
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.513 vs wti
- Source: TotalEnergies Targets 3% Annual Oil and Gas Growth Through 2030 — OilPrice, 2026-09-28. https://oilprice.com/Latest-Energy-News/World-News/TotalEnergies-Targets-3-Annual-Oil-and-Gas-Growth-Through-2030.html
- Source: Oil woes push rupee to over one-week low, RBI caps fall near 96/USD — ET Markets, 2026-09-28. https://economictimes.indiatimes.com/markets/forex/forex-news/oil-woes-push-rupee-to-over-one-week-low-rbi-caps-fall-near-96/usd/articleshow/134539275.cms
- Source: Global Market: Eurozone bond yields rise as oil climbs, inflation data eyed — ET Markets, 2026-09-28. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-eurozone-bond-yields-rise-as-oil-climbs-inflation-data-eyed/articleshow/134538460.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

### [AMBER 5.01] brent ↓
- brent [COMMODITIES]: last 101.16, z20 -0.01, zc -0.75, resid-z -0.78 [quiet], 1d -3.03%, 1-session move -3.03% ≥ 1.5%
- **Mechanism**: brent ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: wti (co-move) — not yet - watch; rho 0.931 vs brent, historically leads by 5d
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.568 vs brent, historically leads by 5d
- Watch next: dax (inverse) — not yet - watch; rho -0.536 vs brent, historically leads by 5d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.691 vs brent
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.585 vs brent
- Source: TotalEnergies Targets 3% Annual Oil and Gas Growth Through 2030 — OilPrice, 2026-09-28. https://oilprice.com/Latest-Energy-News/World-News/TotalEnergies-Targets-3-Annual-Oil-and-Gas-Growth-Through-2030.html
- Source: Oil woes push rupee to over one-week low, RBI caps fall near 96/USD — ET Markets, 2026-09-28. https://economictimes.indiatimes.com/markets/forex/forex-news/oil-woes-push-rupee-to-over-one-week-low-rbi-caps-fall-near-96/usd/articleshow/134539275.cms
- Source: Global Market: Eurozone bond yields rise as oil climbs, inflation data eyed — ET Markets, 2026-09-28. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-eurozone-bond-yields-rise-as-oil-climbs-inflation-data-eyed/articleshow/134538460.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.0), 2025-08-14 (d=0.02)

### [AMBER 4.78] indices · 2 series ↑
- nasdaq_100 [INDICES]: last 30601.51, z20 1.95, zc 0.32, resid-z -0.12 [quiet], 1d 0.40%, |z20|=1.95; 1y-pct=99
- sp500 [INDICES]: last 7742.32, z20 1.21, zc 0.61, resid-z 0.85 [quiet], 1d 0.50%, 1y-pct=96
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.923 vs nasdaq_100, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.653 vs nasdaq_100, historically leads by 2d
- Watch next: brent (inverse) — not yet - watch; rho -0.638 vs sp500, historically leads by 2d
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.609 vs nasdaq_100, historically leads by 3d
- Watch next: wti (inverse) — not yet - watch; rho -0.585 vs sp500, historically leads by 2d
- Source: Forget KOSPI, Nikkei, Nasdaq, even Pakistan's KSE surged over 100% in 2 years, leaving India's Nifty, Sensex far behind — Mint Markets, 2026-09-28. https://www.livemint.com/market/stock-market-news/forget-kospi-nikkei-nasdaq-even-pakistans-kse-surged-over-100-in-2-years-leaving-indias-nifty-sensex-far-behind-11790576868466.html
- Source: Global Market: Japan’s Nikkei slips after early gains as Nasdaq futures weaken — ET Markets, 2026-09-28. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-slips-after-early-gains-as-nasdaq-futures-weaken/articleshow/134532154.cms
- Source: US Market: Wall Street rally faces fresh test as jobs, inflation data loom — ET Markets, 2026-09-28. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-market-wall-street-rally-faces-fresh-test-as-jobs-inflation-data-loom/articleshow/134532058.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-07 (d=0.06), 2026-05-15 (d=0.07)

### [RED 4.74] fx · 4 series ↓
- usd_mxn [FX]: last 17.78, z20 3.07, zc 1.72, resid-z 2.44 [unexplained], 1d 0.22%, |z20|=3.07
- aud_usd [FX]: last 0.70, z20 -2.30, zc -0.44, resid-z -0.69 [quiet], 1d 0.09%, |z20|=2.30
- eur_usd [FX]: last 1.14, z20 -2.03, zc -0.19, resid-z -0.19 [quiet], 1d 0.02%, |z20|=2.03; 1y-pct=2
- gbp_usd [FX]: last 1.33, z20 -1.90, zc -0.54, resid-z -0.67 [quiet], 1d 0.37%, |z20|=1.90
- **Mechanism**: fx · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.49 via usd_mxn, z -3.12, reacted); dyn_icicigi_bo (rho -0.485 via gbp_usd, z 0.91, quiet); dyn_muthootfin_ns (rho 0.459 via aud_usd, z -1.43, reacted); dyn_inoxindia_ns (rho 0.415 via aud_usd, z -1.1, reacted); nifty_50 (rho 0.374 via eur_usd, z -2.29, reacted)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.552 vs aud_usd, historically leads by 3d
- **India receivers**: dyn_policybzr_ns (rho -0.49, z -3.12); dyn_icicigi_bo (rho -0.485, z 0.91); dyn_muthootfin_ns (rho 0.459, z -1.43); dyn_inoxindia_ns (rho 0.415, z -1.1)
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [AMBER 4.03] dyn_tech ↑
- dyn_tech [EQUITIES]: last 72.62, z20 2.03, zc 0.62, resid-z 0.09 [quiet], 1d 0.07%, |z20|=2.03; 1y-pct=100
- **Mechanism**: dyn_tech ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Global Market: Chinese stocks slide as US-China optimism fades, tech shares tumble — ET Markets, 2026-09-28. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-chinese-stocks-slide-as-us-china-optimism-fades-tech-shares-tumble/articleshow/134495616.cms
- Source: Tech picks: Balrampur Chini Mills among 4 stocks to buy for up to 18% returns in short term — ET Markets, 2026-09-28. https://economictimes.indiatimes.com/markets/stocks/news/tech-picks-balrampur-chini-mills-among-4-stocks-to-buy-for-up-to-18-returns-in-short-term/slideshow/134534034.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.0), 2025-05-19 (d=0.0)

## Watchlist (below surfacing floor)
hy_oas ↑ (3.38), dyn_4417_t ↑ (3.17), shanghai_comp ↓ (3.13), dyn_jiofin_bo ↓ (2.84), dyn_indianb_ns ↓ (2.7), dyn_msft ↑ (2.64), dyn_indusindbk_bo ↓ (2.41), dyn_atherenerg_ns ↓ (2.2), sofr ↑ (1.94), taiwan_weighted ↑ (1.89), dxy ↑ (1.75), usd_brl ↑ (1.66)

## India macro
- nifty_50: 22780.2500 (1d -1.56%, z20 -2.29, flag amber)
- nifty_midcap_100: 59913.1992 (1d -1.62%, z20 -2.51, flag red)
- usd_inr: 95.9800 (1d -0.19%, z20 1.07, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6301 (1d -0.07%, z20 -1.36, flag none)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 64.4 — "Green copper needs a definition and India can be the first"
- INOXINDIA.NS (INOX INDIA LIMITED) score 63.8 — "Green copper needs a definition and India can be the first"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 63.6 — "Green copper needs a definition and India can be the first"
- INDIANB.NS (INDIAN BANK) score 44.9 — "Gold may rise to $5,000/oz in H1 2027 after near-term consolidation: ICICI Bank"
- COIN (Coinbase Global, Inc.) score 43.5 — "Global Gas Squeeze Could Last Through Next Summer"
- OHI (Omega Healthcare Investors, In) score 36.2 — "PB Fintech: the risk was known. Investors chased the stock anyway"
- CHKP (Check Point Software Technolog) score 35.0 — "Today’s Gold Rate, September 26: Check Gold Rates in Delhi, Mumbai, Chennai"
- HDB (HDFC Bank Limited) score 34.1 — "Gold may rise to $5,000/oz in H1 2027 after near-term consolidation: ICICI Bank"
- BAC (Bank of America Corporation) score 31.9 — "Gold may rise to $5,000/oz in H1 2027 after near-term consolidation: ICICI Bank"
- TECHM.NS (TECH MAHINDRA LIMITED) score 31.3 — "J Infratech files IPO papers; eyes ₹600 cr via fresh issue"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 31.3 — "J Infratech files IPO papers; eyes ₹600 cr via fresh issue"
- TECH (Bio-Techne Corp) score 31.3 — "J Infratech files IPO papers; eyes ₹600 cr via fresh issue"
- IDBI.NS (IDBI BANK LIMITED) score 28.6 — "Gold may rise to $5,000/oz in H1 2027 after near-term consolidation: ICICI Bank"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 28.6 — "Gold may rise to $5,000/oz in H1 2027 after near-term consolidation: ICICI Bank"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 28.6 — "Gold may rise to $5,000/oz in H1 2027 after near-term consolidation: ICICI Bank"
- 301077.SZ (CHINASTARS) score 28.1 — "China’s consumer stocks trapped in a lost decade as AI boom dominates"
- BOND (PIMCO Active Bond Exchange-Tra) score 26.8 — "Rupee, bonds vulnerable to oil pangs on waning Iran diplomacy hopes"
- LTH (Life Time Group Holdings, Inc.) score 25.1 — "Gold prices dip Rs 3,200/10 gram; silver falls Rs 6,700/kg as high oil prices raise rate h"
- SEPN (Septerna, Inc.) score 23.3 — "Today’s Gold Rate, September 26: Check Gold Rates in Delhi, Mumbai, Chennai"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 18.3 — "Deon Energy files draft papers with SEBI to raise funds via IPO"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 12.7 — "Stock selection key as earnings and valuation gaps widen: Tata MF’s Chandraprakash Padiyar"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 12.7 — "Stock selection key as earnings and valuation gaps widen: Tata MF’s Chandraprakash Padiyar"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.1 — "Global Gas Squeeze Could Last Through Next Summer"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 12.0 — "Two dozen stocks, including NMDC, Adani Power, NTPC Green, Sedemac, Aditya Infotech, TVS M"
- POLICYBZR.NS (PB FINTECH LIMITED) score 10.4 — "PB Fintech: the risk was known. Investors chased the stock anyway"
- JIOFIN.BO (Jio Financial Services Limited) score 10.4 — "Jefferies names Max Financial as its top insurance pick, sees 41% upside despite target cu"
- META (Meta) score 8.9 — "H1 digest: Small caps overtake precious metals as H1 FY27’s best performer"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.1 — "The Next Global Energy Crisis Won’t Come From Just One Direction"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.3 — "Gold may rise to $5,000/oz in H1 2027 after near-term consolidation: ICICI Bank"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 6.1 — "JAPANESE, US FINANCE CHIEFS DISCUSS YEN DEPRECIATION: KYODO"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 6.0 — "ETMarkets Smart Talk| F&O STT, UPI charges and trading costs: Sandeep Neema on the hidden "
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 5.1 — "SBI Life, HDFC Life, ICICI Prudential: Should you invest in insurance stocks amid IRDAI ne"
- MS (Morgan Stanley) score 4.8 — "‘We were wrong.’ Why Morgan Stanley changed its tune on the U.S. dollar — and what it expe"
- GS (Goldman Sachs Group, Inc. (The) score 4.5 — "Goldman Warns Diesel Export Ban Would Send Gasoline Prices Higher"
- VT (Vanguard Total World Stock Ind) score 4.1 — "Beyond high-profile wars, a worldwide battle for critical minerals"
- PINELABS.NS (PINE LABS LIMITED) score 2.1 — "Pine Labs shares: Over 25% up in a month; Motilal Oswal sees 30% more upside | Buy rating "
- MOTILALOFS.BO (MOTILAL OSWAL FINANCIAL SERVIC) score 2.0 — "Up over 20% YTD despite weak market sentiment; Motilal Oswal says buy this hospital stock "
- MSFT (Microsoft Corporation) score 1.7 — "Wall Street ends higher as investors buy AI stocks; Microsoft rallies"
- VOLTAS.NS (VOLTAS LTD) score 0.8 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 0.5 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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