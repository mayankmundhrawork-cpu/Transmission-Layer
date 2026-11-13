# Transmission Layer — board brief · 2026-11-13 12:08Z

data as of **2026-11-13** · 97 series · 11 red / 25 amber · 8 events surfaced (22 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.536, 1d in regime; vol-pct 0.656, breadth-off 0.417, Markov P(high-vol) 0.074)
- [WEAK] **safe_haven_gold** — corr20 -0.1, corr60 -0.21, contra nifty_50 corr20=0.24, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.9, corr60 0.85, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.15, corr60 0.11, last shift 2026-09-16. Channel: global copper leads Indian metal equities
- [INVERTED] **inr_oil_channel** — corr20 -0.32, corr60 0.04, last shift 2026-09-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.91, last shift 2026-09-25. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.23, corr60 -0.01, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.08, corr60 -0.17, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.39, corr60 0.32, last shift 2026-07-16. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** ust_2y → usd_jpy: leads 1d (ccf 0.477, β 0.2051, p 0.0); driver zc 2.86 → expected 0.765%. Type hit-rate 0.816 (n=2212).
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.447, β 0.2336, p 0.0); driver zc 1.9 → expected 0.479%. Type hit-rate 0.816 (n=2212).
- **SETUP** dyn_bond → usd_jpy: leads 1d (ccf -0.396, β -0.6991, p 0.0); driver zc -2.04 → expected 0.534%. Type hit-rate 0.816 (n=2212).
- Track record · residual_reversion: hit-rate **0.511** (n=1154) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.816** (n=2212) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.23] dyn_301077_sz ↑
- dyn_301077_sz [EQUITIES]: last 22.11, z20 6.23, zc 3.90, resid-z 0.60 [moved], 1d 10.38%, |z20|=6.23
- **Mechanism**: dyn_301077_sz ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.513 vs dyn_301077_sz, historically leads by 1d
- Source: Nvidia shares recover 4.5% after steep sell-off; China spy probe and November 17 earnings to test investor confidence — Mint Markets, 2026-11-11. https://www.livemint.com/market/stock-market-news/nvidia-shares-recover-4-5-after-steep-sell-off-china-spy-probe-and-november-17-earnings-to-test-investor-confidence-11794413606492.html
- Historical analogues: 2026-06-18 (d=0.0), 2026-03-30 (d=0.02), 2026-06-03 (d=0.03)

### [RED 6.41] fx · 2 series ↓
- eur_usd [FX]: last 1.11, z20 -3.58, zc -0.97, resid-z -0.93 [quiet], 1d -0.37%, |z20|=3.58; 1y-pct=0
- gbp_usd [FX]: last 1.32, z20 -2.51, zc -0.88, resid-z -0.87 [quiet], 1d -0.34%, |z20|=2.51
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.054 vs eur_usd, historically leads by 1d
- Source: Sterling drops against firmer dollar as markets price in a hawkish Fed — ET Markets, 2026-11-11. https://economictimes.indiatimes.com/markets/forex/forex-news/sterling-drops-against-firmer-dollar-as-markets-price-in-a-hawkish-fed/articleshow/135738659.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [RED 5.96] cross-asset · 3 series ↓
- btc_usd [CRYPTO]: last 69360.03, z20 -2.64, zc -1.10, resid-z -1.42 [quiet], 1d -2.78%, |z20|=2.64
- eth_usd [CRYPTO]: last 1961.14, z20 -2.42, zc -0.73, resid-z -0.25 [quiet], 1d -2.76%, |z20|=2.42
- dyn_coin [EQUITIES]: last 130.62, z20 -1.56, zc -0.88, resid-z 0.21 [quiet], 1d -4.15%, 1y-pct=0
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.53).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.73 vs btc_usd
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.727 vs btc_usd
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.71 vs btc_usd
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.625 vs btc_usd
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.546 vs btc_usd
- Source: Global Market Today: Asian stocks gain after Nvidia shakeup, oil steady — ET Markets, 2026-11-13. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-today-asian-stocks-gain-after-nvidia-shakeup-oil-steady/articleshow/135785602.cms
- Source: CHINA PLANS $15 BILLION SHIPPING INSURANCE RIVAL TO LLOYD'S OF LONDON Beijing is exploring a $15 billion maritime insurance and reinsurance hub by 2029, challenging Western dominance of global shipping coverage. The proposed system would protect Chinese shipping from Western sanctions and disruption — DeItaone, 2026-11-12. https://t.me/walter_bloomberg/38481
- Source: UK Vows Global Climate Leadership as PM Doubles Down on Net Zero — OilPrice, 2026-11-12. https://oilprice.com/Latest-Energy-News/World-News/UK-Vows-Global-Climate-Leadership-as-PM-Doubles-Down-on-Net-Zero.html
- Historical analogues: 2026-05-22 (d=0.53), 2025-04-10 (d=0.78), 2025-10-16 (d=0.84)

### [RED 5.92] dxy ↑
- dxy [FX]: last 103.22, z20 2.92, zc 0.13, resid-z 0.95 [quiet], 1d 0.05%, 20d range extreme; |z20|=2.92; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_jef (inverse) — not yet - watch; rho -0.509 vs dxy, historically leads by 5d
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-10 (d=0.03), 2025-05-14 (d=0.06)

### [AMBER 5.47] cross-asset · 3 series ↑
- dyn_bajfinance_ns [EQUITIES]: last 1117.00, z20 2.15, zc 0.08, resid-z 0.79 [quiet], 1d 0.18%, |z20|=2.15; 1y-pct=98
- nifty_midcap_100 [INDICES]: last 61881.90, z20 1.84, zc -0.22, resid-z 0.43 [quiet], 1d -0.25%, |z20|=1.84
- nifty_50 [INDICES]: last 25144.30, z20 1.71, zc -0.53, resid-z 0.08 [quiet], 1d -0.61%, |z20|=1.71
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.59).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.814 via nifty_midcap_100, z 1.16, reacted); nifty_metal (rho 0.717 via nifty_midcap_100, z 1.34, reacted); dyn_muthootfin_ns (rho 0.713 via nifty_midcap_100, z 1.28, reacted); dyn_indusindbk_bo (rho 0.667 via nifty_midcap_100, z 1.83, reacted); nifty_fmcg (rho 0.644 via nifty_midcap_100, z 1.41, reacted)
- Watch next: dyn_adanient_bo (co-move) — not yet - watch; rho 0.536 vs nifty_midcap_100, historically leads by 5d
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.522 vs nifty_50, historically leads by 5d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.507 vs dyn_bajfinance_ns, historically leads by 1d
- Watch next: midcap_largecap_ratio (co-move) — not yet - watch; rho 0.52 vs nifty_midcap_100
- Watch next: taiwan_weighted (inverse) — not yet - watch; rho -0.514 vs nifty_50
- **India receivers**: dyn_jiofin_bo (rho 0.814, z 1.16); nifty_metal (rho 0.717, z 1.34); dyn_muthootfin_ns (rho 0.713, z 1.28); dyn_indusindbk_bo (rho 0.667, z 1.83)
- Source: Diwali gains often last. Will this year’s Sensex rally hold? — Mint Markets, 2026-11-13. https://www.livemint.com/market/stock-market-news/diwali-gains-this-year-sensex-rally-muhurat-11794459314013.html
- Source: Sensex today | Stock Market Highlights: Markets snap 3-day rally; Sensex drops 318 points, Nifty slips below 25,150 — BusinessLine Mkts, 2026-11-13. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-13-november-2026/article71693403.ece
- Source: Nifty PSU Bank logs biggest weekly surge in 7 months; PNB, Bank of India, Bank of Baroda among top performers — Mint Markets, 2026-11-13. https://www.livemint.com/market/stock-market-news/nifty-psu-bank-logs-biggest-weekly-surge-in-two-years-pnb-bank-of-india-bank-of-baroda-among-top-performers-11794563569958.html
- Historical analogues: 2025-07-21 (d=0.59), 2025-09-25 (d=1.13), 2025-07-11 (d=1.19)

### [RED 4.99] usd_jpy ↑
- usd_jpy [FX]: last 159.96, z20 2.99, zc 0.25, resid-z 0.25 [quiet], 1d 0.14%, |z20|=2.99
- **Mechanism**: usd_jpy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho 0.409 via usd_jpy, z -0.07, quiet)
- **India receivers**: dyn_idbi_ns (rho 0.409, z -0.07)
- Source: Yen Falls to Cusp of 160 Level, Fanning Intervention Risk — Mint Markets, 2026-11-12. https://www.livemint.com/market/yen-falls-to-cusp-of-160-level-fanning-intervention-risk-11794521542082.html
- Source: The Yen Is Becoming Too Hard for Some Investors to Trade — Mint Markets, 2026-11-12. https://www.livemint.com/market/the-yen-is-becoming-too-hard-for-some-investors-to-trade-11794520064240.html
- Source: Dollar near one-month high as yen edges toward 160 — ET Markets, 2026-11-12. https://economictimes.indiatimes.com/markets/forex/forex-news/dollar-near-one-month-high-as-yen-edges-toward-160/articleshow/135751707.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2025-07-30 (d=0.01)

### [RED 4.7] commodities · 2 series ↓
- comex_gold [COMMODITIES]: last 3898.80, z20 -1.86, zc 0.17, resid-z -1.00 [quiet], 1d 0.35%, |z20|=1.86; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 49.99, z20 -1.23, zc 0.02, resid-z -0.31 [quiet], 1d 0.05%, 1y-pct=2; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.461 via comex_gold, z 1.28, reacted); dyn_karurvysya_ns (rho 0.424 via comex_gold, z 1.91, reacted)
- Watch next: gold_silver_ratio (inverse) — not yet - watch; rho -0.505 vs comex_gold
- **India receivers**: dyn_muthootfin_ns (rho 0.461, z 1.28); dyn_karurvysya_ns (rho 0.424, z 1.91)
- Source: Gem, jewellery exports up 34% on growing demand, rise in gold prices — BusinessLine Mkts, 2026-11-13. https://www.thehindubusinessline.com/markets/gold/gem-jewellery-exports-up-34-on-growing-demand-rise-in-gold-prices/article71697017.ece
- Source: India’s gold imports plunge 62.57% to $5.51 billion in October as prices fall below $4,000/oz — BusinessLine Mkts, 2026-11-13. https://www.thehindubusinessline.com/markets/gold/indias-gold-imports-plunge-6257-to-551-billion-in-october-as-prices-fall-below-4000oz/article71697565.ece
- Source: Gold demand stays firm as lower prices draw festive buying — BusinessLine Mkts, 2026-11-13. https://www.thehindubusinessline.com/markets/gold/gold-demand-stays-firm-as-lower-prices-draw-festive-buying/article71696958.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-15 (d=0.09), 2026-05-15 (d=0.16)

### [AMBER 4.34] dyn_nvda ↓
- dyn_nvda [EQUITIES]: last 166.04, z20 -2.34, zc -1.08, resid-z -2.56 [unexplained], 1d -4.43%, |z20|=2.34; 1y-pct=0
- **Mechanism**: dyn_nvda ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.812 vs dyn_nvda, historically leads by 4d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.739 vs dyn_nvda, historically leads by 4d
- Watch next: vix (inverse) — not yet - watch; rho -0.702 vs dyn_nvda
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.674 vs dyn_nvda
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.623 vs dyn_nvda
- Source: Anthropic IPO oversubscribed nearly six times; can AI firm become new NVIDIA amid stock crash? Experts' views — Mint Markets, 2026-11-13. https://www.livemint.com/market/stock-market-news/anthropic-ipo-oversubscribed-nearly-six-times-can-ai-firm-become-new-nvidia-amid-stock-crash-experts-views-11794542852438.html
- Source: NVIDIA share price crash: Broadcom, AMD to Micron — Should you buy other AI stocks after Jensen Huang's resignation? — Mint Markets, 2026-11-13. https://www.livemint.com/market/stock-market-news/nvidia-share-price-crash-broadcom-amd-to-micron-should-you-buy-other-ai-stocks-after-jensen-huangs-resignation-11794540876728.html
- Source: Nvidia PE falls to 14-year low, but CEO exit and AI worries cloud the bargain — BusinessLine Mkts, 2026-11-13. https://www.thehindubusinessline.com/markets/stock-markets/nvidia-pe-falls-to-14-year-low-but-ceo-exit-and-ai-worries-cloud-the-bargain/article71696470.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-24 (d=0.03), 2026-05-04 (d=0.03)

## Watchlist (below surfacing floor)
tips_10y_real ↑ (4.06), comex_copper ↓ (3.87), dyn_tech ↑ (3.87), indices · 4 series ↑ (3.86), natgas ↑ (3.53), dyn_schd ↑ (3.09), ust_2s10s ↓ (2.92), dyn_4417_t ↑ (2.9), aud_usd ↓ (2.74), dyn_cochinship_ns ↓ (2.64), dyn_rs ↑ (2.64), dyn_lth ↑ (2.57)

## India macro
- nifty_50: 25144.3008 (1d -0.61%, z20 1.71, flag amber)
- nifty_midcap_100: 61881.8984 (1d -0.25%, z20 1.84, flag amber)
- usd_inr: 94.2200 (1d 0.56%, z20 -0.91, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4611 (1d 0.36%, z20 -0.75, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · India WPI T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 89.9 — "Nestle India Share Price Live Updates: Nestle India Stock Insights"
- INOXINDIA.NS (INOX INDIA LIMITED) score 87.3 — "Nestle India Share Price Live Updates: Nestle India Stock Insights"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 87.1 — "Nestle India Share Price Live Updates: Nestle India Stock Insights"
- NVDA (NVIDIA Corporation) score 72.6 — "Nvidia PE falls to 14-year low, but CEO exit and AI worries cloud the bargain"
- INDIANB.NS (INDIAN BANK) score 61.2 — "Indian shares likely to open flat as oil surge counters strong foreign inflows"
- BAC (Bank of America Corporation) score 51.6 — "Axis Bank Share Price Live Updates: Axis Bank  Daily and Weekly Returns"
- HDB (HDFC Bank Limited) score 45.8 — "HDFC Life Share Price Live Updates: HDFC Life's Current Trading Price"
- TGT (Target Corporation) score 43.1 — "51% rally in 2026 so far! ICICI Direct sees 28% upside potential in this defence stock - D"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 41.9 — "Axis Bank Share Price Live Updates: Axis Bank  Daily and Weekly Returns"
- IDBI.NS (IDBI BANK LIMITED) score 41.9 — "Axis Bank Share Price Live Updates: Axis Bank  Daily and Weekly Returns"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 41.9 — "Axis Bank Share Price Live Updates: Axis Bank  Daily and Weekly Returns"
- CHKP (Check Point Software Technolog) score 38.4 — "51% rally in 2026 so far! ICICI Direct sees 28% upside potential in this defence stock - D"
- TECHM.NS (TECH MAHINDRA LIMITED) score 36.5 — "UltraTech Cem Share Price Live Updates: UltraTech Cement's Recent Performance Overview"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 34.5 — "UltraTech Cem Share Price Live Updates: UltraTech Cement's Recent Performance Overview"
- TECH (Bio-Techne Corp) score 34.5 — "UltraTech Cem Share Price Live Updates: UltraTech Cement's Recent Performance Overview"
- OHI (Omega Healthcare Investors, In) score 32.1 — "Anthropic IPO how to apply from India: Can Indian investors apply online? Check eligibilit"
- 301077.SZ (CHINASTARS) score 29.5 — "CHINA PLANS $15 BILLION SHIPPING INSURANCE RIVAL TO LLOYD'S OF LONDON Beijing is exploring"
- LTH (Life Time Group Holdings, Inc.) score 25.1 — "Anthropic IPO oversubscribed nearly six times; can AI firm become new NVIDIA amid stock cr"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 22.6 — "Bajaj Finserv Share Price Live Updates: Bajaj Finserv ends the day at Rs 1858.2"
- BOND (PIMCO Active Bond Exchange-Tra) score 22.4 — "India bond selloff may continue as Treasury rout, fresh debt sale hurt"
- COIN (Coinbase Global, Inc.) score 22.2 — "CHINA PLANS $15 BILLION SHIPPING INSURANCE RIVAL TO LLOYD'S OF LONDON Beijing is exploring"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 19.9 — "Up 94% from 52-week low, Hitachi Energy shares jump 9% today after Q2 results: Should you "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 18.2 — "Tata Steel Share Price Live Updates: Tata Steel's Price Movement Today"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 18.2 — "Tata Steel Share Price Live Updates: Tata Steel's Price Movement Today"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 17.6 — "Q2 Results Highlights Nov 12: HAL, Oil India, Manappuram Finance log gains, Ola Electric n"
- SCHD (Schwab US Dividend Equity ETF) score 17.4 — "Cochin Shipyard dividend 2026: Last day to buy today | Check record date, payout amount, h"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 15.7 — "Anthropic IPO oversubscribed nearly six times; can AI firm become new NVIDIA amid stock cr"
- BZ=F (Brent Crude Oil Last Day Finan) score 13.8 — "Last chance to buy today ahead of record date! BN Agrochem announces split, stock delivers"
- JUSTDIAL.BO (JUST DIAL LTD.) score 12.0 — "Titan Company Share Price Live Updates: Titan Company Sees Price Adjustment"
- JIOFIN.BO (Jio Financial Services Limited) score 11.9 — "Jio Financial Services Share Price Live Updates: Jio Financial Services wraps up trading a"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.2 — "Adani Ent Share Price Live Updates: Adani Enterprises Declines Below EMA Threshold"
- CRWV (CoreWeave, Inc.) score 7.6 — "COREWEAVE SHARES FOLLOW NVIDIA LOWER, DOWN 6%"
- RS (Reliance, Inc.) score 5.3 — "Q2 Results Highlights Nov 12: HAL, Oil India, Manappuram Finance log gains, Ola Electric n"
- META (Meta) score 5.2 — "India ETFs draw ₹35,120 crore in Q3 as large-cap, precious metals lead inflows"
- DEMZ (Democratic Large Cap Core ETF) score 5.0 — "DEMOCRATIC SENATOR REED SAYS CONGRESS NEEDS ASSESSMENT OF WHETHER NVIDIA IS "TOO BIG TO FA"
- JEF (Jefferies Financial Group Inc.) score 4.4 — "FIIs are back! Jefferies lists 11 stocks that can be the biggest beneficiaries"
- GS (Goldman Sachs Group, Inc. (The) score 4.3 — "Earnings growth is set to peter out — but not the bull market, says Goldman Sachs. Here’s "
- BLLN (BillionToOne, Inc.) score 3.5 — "India’s gold imports plunge 62.57% to $5.51 billion in October as prices fall below $4,000"
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 3.1 — "Cochin Shipyard dividend 2026: Last day to buy today | Check record date, payout amount, h"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 2.7 — "Can Ola Electric’s pivot to dealership model hedge revenue decline?"

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