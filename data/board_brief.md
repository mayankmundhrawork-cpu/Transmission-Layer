# Transmission Layer — board brief · 2026-09-14 09:49Z

data as of **2026-09-14** · 98 series · 16 red / 34 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.702, 1d in regime; vol-pct 0.604, breadth-off 0.8, Markov P(high-vol) 0.022)
- [INVERTED] **safe_haven_gold** — corr20 -0.43, corr60 -0.33, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.82, corr60 0.88, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.13, corr60 0.31, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.15, corr60 0.12, last shift 2026-06-05. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.86, corr60 -0.85, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.12, corr60 -0.03, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.36, corr60 -0.17, last shift 2026-06-26. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.25, corr60 0.11, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** vix → asx_200: leads 1d (ccf -0.503, β -0.0454, p 0.0); driver zc 1.5 → expected -0.624%. Type hit-rate 0.818 (n=2009).
- **SETUP** vix → nikkei_225: leads 1d (ccf -0.489, β -0.0886, p 0.0); driver zc 1.5 → expected -1.219%. Type hit-rate 0.818 (n=2009).
- **SETUP** dyn_jef → asx_200: leads 1d (ccf 0.449, β 0.1292, p 0.0); driver zc -1.66 → expected -0.477%. Type hit-rate 0.818 (n=2009).
- **SETUP** vix → taiwan_weighted: leads 1d (ccf -0.438, β -0.0808, p 0.0); driver zc 1.5 → expected -1.111%. Type hit-rate 0.818 (n=2009).
- **SETUP** dyn_dell → taiwan_weighted: leads 1d (ccf 0.36, β 0.1434, p 1e-05); driver zc 2.28 → expected 1.712%. Type hit-rate 0.818 (n=2009).
- **SETUP** ust_10y → gbp_usd: leads 1d (ccf -0.271, β -0.1092, p 0.0); driver zc 2.66 → expected -0.271%. Type hit-rate 0.818 (n=2009).
- Track record · residual_reversion: hit-rate **0.496** (n=1125) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=2009) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.57] cross-asset · 5 series ↑
- ust_10y [RATES]: last 4.95, z20 4.00, zc 2.66, resid-z 2.36 [unexplained], 1d 2.48%, |z20|=4.00; 1y-pct=100
- tips_10y_real [RATES]: last 2.55, z20 3.64, zc 2.28, resid-z 1.99 [unexplained], 1d 3.66%, 1d move +9.0bps ≥ 5bps; |z20|=3.64; 1y-pct=100
- ust_30y [RATES]: last 5.37, z20 3.62, zc 2.26, resid-z 2.02 [unexplained], 1d 1.70%, |z20|=3.62; 1y-pct=100
- ust_2y [RATES]: last 4.56, z20 3.18, zc 2.33, resid-z 1.94 [unexplained], 1d 2.93%, |z20|=3.18; 1y-pct=100
- dyn_bond [EQUITIES]: last 88.85, z20 -2.91, zc -0.31, resid-z -0.71 [quiet], 1d -0.11%, |z20|=2.91; 1y-pct=0
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.514 vs dyn_bond, historically leads by 3d
- Source: MSE facilitates its first tokenised corporate bond under SEBI’s Demat 2.0 pilot — BusinessLine Mkts, 2026-09-14. https://www.thehindubusinessline.com/markets/mse-facilitates-indias-first-tokenised-corporate-bond-under-sebis-demat-20-pilot/article71456088.ece
- Source: FIIs sell Indian shares worth Rs 14,475 crore in Sept; analyst warns soaring bond yields may deepen selloff — ET Markets, 2026-09-14. https://economictimes.indiatimes.com/markets/stocks/news/fiis-sell-indian-shares-worth-rs-14475-crore-in-sept-analyst-warns-soaring-bond-yields-may-deepen-selloff/articleshow/134233848.cms
- Source: Tata Sons listing to improve SP Group bond outlook; yields seen tightening — ET Markets, 2026-09-14. https://economictimes.indiatimes.com/markets/bonds/sp-group-bond-yields-set-to-tighten-as-tata-sons-listing-improves-repayment-visibility/articleshow/134229864.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 8.73] cross-asset · 4 series ↓
- comex_silver [COMMODITIES]: last 62.98, z20 -2.21, zc -0.90, resid-z -0.68 [quiet], 1d -2.44%, |z20|=2.21; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 68.66, z20 2.07, zc n/a, resid-z n/a [quiet], 1d 1.51%, GSR<75 (extreme low); |z20|=2.07
- comex_copper [COMMODITIES]: last 6.41, z20 -1.76, zc -0.40, resid-z -0.54 [quiet], 1d -0.87%, |z20|=1.76
- comex_gold [COMMODITIES]: last 4324.20, z20 -1.51, zc -0.73, resid-z -0.37 [quiet], 1d -0.96%, |z20|=1.51; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eth_usd (co-move) — not yet - watch; rho 0.629 vs comex_gold, historically leads by 5d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.598 vs comex_copper, historically leads by 1d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.595 vs comex_copper, historically leads by 5d
- Watch next: btc_usd (co-move) — not yet - watch; rho 0.579 vs comex_silver, historically leads by 5d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.526 vs comex_silver, historically leads by 5d
- Source: EVs, home appliances likely to become pricier as copper price soars — BusinessLine Mkts, 2026-09-14. https://www.thehindubusinessline.com/markets/commodities/evs-home-appliances-likely-to-become-pricier-as-copper-price-soars/article71462841.ece
- Source: The US Federal Reserve's policy meeting due on Wednesday, September 16; how will it impact stocks, gold, and rupee? — Mint Markets, 2026-09-14. https://www.livemint.com/market/stock-market-news/the-us-federal-reserves-policy-meeting-due-on-wednesday-september-16-how-will-it-impact-your-stocks-gold-and-rupee-11789368302533.html
- Source: Gold slips as oil rally fans rate hike bets ahead of Fed meeting — BusinessLine Mkts, 2026-09-14. https://www.thehindubusinessline.com/markets/gold/gold-slips-as-oil-rally-fans-rate-hike-bets-ahead-of-fed-meeting/article71465512.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.34)

### [RED 8.35] commodities · 2 series ↑
- brent [COMMODITIES]: last 107.49, z20 2.52, zc 0.84, resid-z -0.61 [quiet], 1d 2.75%, 1-session move +2.75% ≥ 1.5%; |z20|=2.52
- wti [COMMODITIES]: last 102.82, z20 2.46, zc 0.88, resid-z -0.45 [quiet], 1d 2.77%, 1-session move +2.77% ≥ 1.5%; |z20|=2.46; 1y-pct=96
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.525 vs brent, historically leads by 4d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.656 vs brent
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.589 vs brent
- Source: Middle East Oil Routes Under Pressure as Hormuz Traffic Tumbles — OilPrice, 2026-09-14. https://oilprice.com/Latest-Energy-News/World-News/Middle-East-Oil-Routes-Under-Pressure-as-Hormuz-Traffic-Tumbles.html
- Source: Global Market: European shares subdued as tech stocks slide, oil prices surge — ET Markets, 2026-09-14. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-european-shares-subdued-as-tech-stocks-slide-oil-prices-surge/articleshow/134236833.cms
- Source: Soaring Oil Prices Put Fed on Track for September Rate Hike — OilPrice, 2026-09-14. https://oilprice.com/Latest-Energy-News/World-News/Soaring-Oil-Prices-Put-Fed-on-Track-for-September-Rate-Hike.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 6.68] cross-asset · 4 series ↓
- india_vix [INDICES]: last 12.29, z20 3.01, zc 0.74, resid-z n/a [quiet], 1d 4.15%, |z20|=3.01
- nifty_midcap_100 [INDICES]: last 62197.20, z20 -2.39, zc -0.40, resid-z -0.44 [quiet], 1d -0.26%, |z20|=2.39
- nifty_50 [INDICES]: last 23398.10, z20 -2.37, zc -0.61, resid-z -0.81 [quiet], 1d -0.34%, |z20|=2.37
- dyn_jiofin_bo [EQUITIES]: last 230.00, z20 -1.89, zc -0.35, resid-z 0.41 [quiet], 1d -0.50%, 1y-pct=2
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-17 (z-distance 0.67).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.624 via nifty_50, z -1.77, reacted); dyn_indianb_ns (rho 0.553 via nifty_midcap_100, z -2.13, reacted); nifty_it (rho 0.51 via nifty_50, z -2.31, reacted); dyn_techm_ns (rho 0.466 via nifty_50, z -1.48, reacted); dyn_indusindbk_bo (rho 0.457 via nifty_50, z -1.86, reacted)
- **India receivers**: nifty_fmcg (rho 0.624, z -1.77); dyn_indianb_ns (rho 0.553, z -2.13); nifty_it (rho 0.51, z -2.31); dyn_techm_ns (rho 0.466, z -1.48)
- Source: BofA turns bullish on Nifty after 2 years, cautious on small, midcaps. Here's what it expects now — ET Markets, 2026-09-14. https://economictimes.indiatimes.com/markets/stocks/news/bofa-turns-bullish-on-nifty-after-2-years-cautious-on-small-midcaps-heres-what-it-expects-now/articleshow/134237764.cms
- Source: From US Fed rate decision to crude oil - 3 factors that may dictate Sensex, Nifty 50 this week — Mint Markets, 2026-09-14. https://www.livemint.com/market/stock-market-news/from-us-fed-rate-decision-to-crude-oil-3-factors-that-may-dictate-sensex-nifty-50-this-week-11789356774067.html
- Source: Nifty oversold, IT poised for pullback: Anand James on what traders should do next — ET Markets, 2026-09-14. https://economictimes.indiatimes.com/markets/expert-view/nifty-oversold-it-poised-for-pullback-anand-james-on-what-traders-should-do-next/articleshow/134230830.cms
- Historical analogues: 2025-07-17 (d=0.67), 2025-12-19 (d=1.13), 2024-11-07 (d=1.15)

### [AMBER 4.31] dyn_tatatech_ns ↓
- dyn_tatatech_ns [EQUITIES]: last 762.15, z20 -2.31, zc -1.03, resid-z -0.77 [quiet], 1d -2.17%, |z20|=2.31
- **Mechanism**: dyn_tatatech_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.585 via dyn_tatatech_ns, z -2.31, reacted); dyn_tataelxsi_ns (rho 0.507 via dyn_tatatech_ns, z -2.28, reacted); dyn_techm_ns (rho 0.48 via dyn_tatatech_ns, z -1.48, reacted)
- **India receivers**: nifty_it (rho 0.585, z -2.31); dyn_tataelxsi_ns (rho 0.507, z -2.28); dyn_techm_ns (rho 0.48, z -1.48)
- Source: Tata Sons IPO news | Why is it getting difficult for Tata Group's holding company to stay private? — Mint Markets, 2026-09-14. https://www.livemint.com/market/ipo/tata-sons-ipo-news-why-is-it-getting-difficult-for-tata-groups-holding-company-to-stay-private-11789349656909.html
- Source: Tata group stocks may pop after RBI decision on listing — Mint Markets, 2026-09-14. https://www.livemint.com/market/stock-market-news/tata-sons-ipo-listing-impact-on-tata-group-stocks-11789296081226.html
- Source: Tata Sons listing to improve SP Group bond outlook; yields seen tightening — ET Markets, 2026-09-14. https://economictimes.indiatimes.com/markets/bonds/sp-group-bond-yields-set-to-tighten-as-tata-sons-listing-improves-repayment-visibility/articleshow/134229864.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

### [AMBER 4.11] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.66, z20 1.11, zc n/a, resid-z n/a [quiet], 1d 0.08%, 52-wk extreme (pct=98); 1y-pct=98
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho -0.436 via midcap_largecap_ratio, z -2.37, reacted); nifty_midcap_100 (rho 0.431 via midcap_largecap_ratio, z -2.39, reacted); nifty_fmcg (rho -0.398 via midcap_largecap_ratio, z -1.77, reacted)
- **India receivers**: nifty_50 (rho -0.436, z -2.37); nifty_midcap_100 (rho 0.431, z -2.39); nifty_fmcg (rho -0.398, z -1.77)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [AMBER 3.93] nikkei_225 ↓
- nikkei_225 [INDICES]: last 63633.57, z20 -1.93, zc -0.39, resid-z -1.10 [quiet], 1d -0.59%, |z20|=1.93
- **Mechanism**: nikkei_225 ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_techm_ns (rho -0.37 via nikkei_225, z -1.48, reacted)
- Watch next: kospi (co-move) — not yet - watch; rho 0.835 vs nikkei_225
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.776 vs nikkei_225
- **India receivers**: dyn_techm_ns (rho -0.37, z -1.48)
- Source: Some up, some down! What's happening in Nikkei, Kospi, Taiwan? Oil on boil, rude crude impacting gold - Latest update — Mint Markets, 2026-09-14. https://www.livemint.com/market/stock-market-news/some-up-some-down-whats-happening-in-nikkei-kospi-taiwan-oil-on-boil-rude-crude-impacting-gold-latest-update-11789360541093.html
- Source: Global Market: Japan stocks fall as AI concerns hit tech shares; Nikkei down 1.6% — ET Markets, 2026-09-14. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japan-stocks-fall-as-ai-concerns-hit-tech-shares-nikkei-down-1-6/articleshow/134232052.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-21 (d=0.23), 2026-06-11 (d=0.6)

### [RED 3.84] indices · 3 series ↓
- stoxx_50 [INDICES]: last 6256.62, z20 -2.52, zc -1.17, resid-z 0.23 [quiet], 1d -1.08%, |z20|=2.52
- dax [INDICES]: last 25394.96, z20 -2.29, zc -0.71, resid-z 0.37 [quiet], 1d -0.68%, |z20|=2.29
- cac_40 [INDICES]: last 8115.39, z20 -1.97, zc -0.85, resid-z 0.25 [quiet], 1d -0.79%, |z20|=1.97
- **Mechanism**: indices · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.48 via dax, z -2.39, reacted)
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.682 vs stoxx_50, historically leads by 5d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.647 vs stoxx_50, historically leads by 5d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.528 vs stoxx_50, historically leads by 5d
- Watch next: ftse_100 (co-move) — not yet - watch; rho 0.549 vs stoxx_50
- **India receivers**: nifty_midcap_100 (rho 0.48, z -2.39)
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-14 (d=0.36), 2025-04-16 (d=0.39)

## Watchlist (below surfacing floor)
vix ↑ (3.15), cross-asset · 2 series ↓ (3.14), fx · 2 series ↓ (3.1), dyn_qcom ↑ (3.01), dyn_dell ↑ (2.7), asx_200 ↓ (2.68), commodities · 2 series ↑ (2.33), dyn_4417_t ↑ (2.3), usd_mxn ↑ (2.28), dyn_indianb_ns ↓ (2.13), dyn_meta ↑ (2.12), hang_seng ↓ (2.04)

## India macro
- nifty_50: 23398.0996 (1d -0.34%, z20 -2.37, flag amber)
- nifty_midcap_100: 62197.1992 (1d -0.26%, z20 -2.39, flag amber)
- usd_inr: 95.5400 (1d -0.16%, z20 0.65, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6582 (1d 0.08%, z20 1.11, flag amber)
- Next India prints: India CPI T-0d · India WPI T-0d · NSDL FPI flows T-0d · IMD weekly rainfall T-0d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 62.0 — "Making Indian commodity derivatives markets competitive"
- COALINDIA.NS (COAL INDIA LTD) score 61.3 — "Making Indian commodity derivatives markets competitive"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 60.0 — "Making Indian commodity derivatives markets competitive"
- INDIANB.NS (INDIAN BANK) score 49.8 — "Making Indian commodity derivatives markets competitive"
- COIN (Coinbase Global, Inc.) score 47.1 — "Why global funds are losing faith in Indian stocks?"
- BAC (Bank of America Corporation) score 43.6 — "Inflation is outpacing wage growth again, squeezing Americans’ paychecks"
- HDB (HDFC Bank Limited) score 38.0 — "All eyes on Warsh as rate-hike fever spreads across G7 central banks"
- OHI (Omega Healthcare Investors, In) score 35.9 — "Investors will move towards institutional products for F&O trades, says NSE executive"
- IDBI.NS (IDBI BANK LIMITED) score 34.9 — "All eyes on Warsh as rate-hike fever spreads across G7 central banks"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 34.9 — "All eyes on Warsh as rate-hike fever spreads across G7 central banks"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 34.9 — "All eyes on Warsh as rate-hike fever spreads across G7 central banks"
- CHKP (Check Point Software Technolog) score 28.0 — "Inflation is outpacing wage growth again, squeezing Americans’ paychecks"
- BOND (PIMCO Active Bond Exchange-Tra) score 27.5 — "Tata Sons listing to improve SP Group bond outlook; yields seen tightening"
- TECHM.NS (TECH MAHINDRA LIMITED) score 22.5 — "Global Market: Japan stocks fall as AI concerns hit tech shares; Nikkei down 1.6%"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 22.5 — "Global Market: Japan stocks fall as AI concerns hit tech shares; Nikkei down 1.6%"
- TECH (Bio-Techne Corp) score 22.5 — "Global Market: Japan stocks fall as AI concerns hit tech shares; Nikkei down 1.6%"
- 301077.SZ (CHINASTARS) score 22.3 — "China targets ‘toxic’ traffic as viral sensations upend daily life and public services"
- LTH (Life Time Group Holdings, Inc.) score 20.9 — "Global Market: Yen speculators turn net long for first time since February"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 17.9 — "The Race to Solve Nuclear Energy’s Biggest Problem"
- SEPN (Septerna, Inc.) score 14.4 — "Indian stock markets are closed today: NSE, BSE trading holiday on Ganesh Chaturthi 14 Sep"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.8 — "Tata Sons may be valued up to Rs 12.5 lakh cr in IPO"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.8 — "Tata Sons may be valued up to Rs 12.5 lakh cr in IPO"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 9.4 — "Can SS Retail IPO deliver long-term growth for high-risk investors?"
- JIOFIN.BO (Jio Financial Services Limited) score 9.1 — "China targets ‘toxic’ traffic as viral sensations upend daily life and public services"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.1 — "RBL Bank: Is investor frenzy over FCNR (B) deposits justified?"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.9 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Current Price Update"
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.6 — "Gem, jewellery exports up 3% to $2.30 billion in Aug"
- MS (Morgan Stanley) score 5.7 — "MUNI YIELDS SURGE TO HIGHEST SINCE APRIL 2025 U.S. 10-year municipal bond yields jumped to"
- VT (Vanguard Total World Stock Ind) score 4.7 — "Isabel Schnabel: Macroeconomic, fiscal and financial stability in a shock-prone world"
- META (Meta) score 4.7 — "Vedanta Aluminium Metal shares dip over 3% | Here's why Anil Agarwal-owned stock is nosedi"
- JEF (Jefferies Financial Group Inc.) score 4.5 — "Jefferies says Sebi's proposed CAS changes will remove uncertainty, but still remains nega"
- NVDA (NVIDIA Corporation) score 4.5 — "Nvidia in talks to invest in Anthropic’s mega IPO"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 4.0 — "Cochin Shipyard shares crash nearly 9% - Is it opportunity to buy? Should you take fresh e"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 3.7 — "Joint finances, joint risks: A couple’s roadmap to starting up"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.6 — "ICICI Bank Share Price Live Updates: Rs 1.09 crore remittance sent home by an Indian worki"
- QCOM (QUALCOMM Incorporated) score 1.1 — "Qualcomm-Amazon AI deal: Why the chipmaker’s stock surged"
- DELL (Dell Technologies Inc.) score 1.0 — "Why Dell and HPE were the S&P 500’s top-performing stocks today"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 0.5 — "Lenskart Solutions among 4 stocks to hit 52-week highs & rallied up to 22% in a month"
- DKS (Dick's Sporting Goods Inc) score 0.1 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- VOLTAS.NS (VOLTAS LTD) score 0.0 — "Voltas reported strong growth in June quarter, but failed to impress"

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