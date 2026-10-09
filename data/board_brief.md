# Transmission Layer — board brief · 2026-10-09 18:21Z

data as of **2026-10-09** · 97 series · 4 red / 39 amber · 8 events surfaced (28 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.704, 5d in regime; vol-pct 0.675, breadth-off 0.733, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.41, corr60 -0.41, contra nifty_50 corr20=0.29, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.83, corr60 0.84, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.24, corr60 0.22, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.07, corr60 0.13, last shift 2026-08-26. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.75, corr60 -0.77, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [INVERTED] **dxy_inr_channel** — corr20 -0.27, corr60 -0.11, last shift 2026-08-12. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.23, corr60 -0.27, last shift 2026-08-12. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.65, corr60 0.17, last shift 2026-07-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 6.795346249477419e-06)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.496** (n=1142) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.826** (n=2228) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.25] usd_inr ↑
- usd_inr [FX]: last 96.76, z20 2.25, zc 0.01, resid-z -0.15 [quiet], 1d 0.00%, 20d range extreme; |z20|=2.25; 1y-pct=99
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.41 via usd_inr, z -0.57, quiet); dyn_karurvysya_ns (rho -0.356 via usd_inr, z 2.87, reacted)
- **India receivers**: dyn_idbi_ns (rho -0.41, z -0.57); dyn_karurvysya_ns (rho -0.356, z 2.87)
- Source: Rupee recovers to 96.73 vs US dollar after RBI intervention, but dollar demand persists — ET Markets, 2026-10-09. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-recovers-to-96-73-vs-us-dollar-after-rbi-intervention-but-dollar-demand-persists/articleshow/134838115.cms
- Source: Rupee rises 16 paise to close at 96.72 against US dollar — BusinessLine Mkts, 2026-10-09. https://www.thehindubusinessline.com/markets/forex/rupee-rises-16-paise-to-close-at-9672-against-us-dollar/article71563647.ece
- Source: Rupee posts weekly fall despite rate hike amid adverse flows, weak sentiment — ET Markets, 2026-10-09. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-posts-weekly-fall-despite-rate-hike-amid-adverse-flows-weak-sentiment/articleshow/134831035.cms
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2025-09-16 (d=0.01)

### [AMBER 5.56] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.67, z20 1.63, zc 0.68, resid-z 0.09 [quiet], 1d 0.53%, |z20|=1.63; 1y-pct=100
- ust_10y [RATES]: last 5.28, z20 1.23, zc 0.18, resid-z -0.68 [quiet], 1d 0.19%, 1y-pct=98
- tips_10y_real [RATES]: last 2.92, z20 1.16, zc 0.18, resid-z -0.79 [quiet], 1d 0.34%, 1y-pct=98
- dyn_bond [EQUITIES]: last 86.89, z20 -0.89, zc -0.08, resid-z 0.48 [quiet], 1d -0.03%, 1y-pct=2
- ust_2y [RATES]: last 4.77, z20 0.15, zc -0.31, resid-z -1.30 [quiet], 1d -0.42%, 1y-pct=96
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.716 vs ust_30y, historically leads by 3d
- Watch next: wti (co-move) — not yet - watch; rho 0.515 vs ust_30y, historically leads by 3d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.553 vs ust_30y
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.547 vs ust_30y
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.541 vs ust_30y
- Source: RBI OMO sale fears spur bond sell-off; 10-year G-Sec hits three year high — BusinessLine Mkts, 2026-10-09. https://www.thehindubusinessline.com/markets/rbi-omo-sale-fears-spur-bond-sell-off-10-year-g-sec-hits-three-year-high/article71564483.ece
- Source: US 10-year Treasury yield could hit 6% as oil prices, debt worries mount: Pimco CIO — ET Markets, 2026-10-09. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-10-year-treasury-yield-could-hit-6-as-oil-prices-debt-worries-mount-pimco-cio/articleshow/134825801.cms
- Source: US bank earnings in focus as Treasury yields surge, raising concerns over lending and dealmaking — ET Markets, 2026-10-09. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-bank-earnings-in-focus-as-treasury-yields-surge-raising-concerns-over-lending-and-dealmaking/articleshow/134806882.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.28] usd_cny ↓
- usd_cny [FX]: last 6.68, z20 -5.28, zc -3.12, resid-z -4.50 [unexplained], 1d -0.34%, |z20|=5.28; 1y-pct=0
- **Mechanism**: usd_cny ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-09-25 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indianb_ns (rho -0.392 via usd_cny, z 0.25, quiet); nifty_50 (rho -0.378 via usd_cny, z -1.3, reacted); dyn_muthootfin_ns (rho -0.369 via usd_cny, z -1.77, reacted); nifty_midcap_100 (rho -0.356 via usd_cny, z -1.38, reacted); dyn_cartrade_ns (rho -0.353 via usd_cny, z 0.18, quiet)
- **India receivers**: dyn_indianb_ns (rho -0.392, z 0.25); nifty_50 (rho -0.378, z -1.3); dyn_muthootfin_ns (rho -0.369, z -1.77); nifty_midcap_100 (rho -0.356, z -1.38)
- Historical analogues: 2026-09-25 (d=0.0), 2025-08-22 (d=0.01), 2026-05-05 (d=0.01)

### [AMBER 4.96] cross-asset · 3 series ↑
- sp500 [INDICES]: last 7812.33, z20 1.64, zc 0.86, resid-z -0.62 [quiet], 1d 0.60%, |z20|=1.64; 1y-pct=99
- nasdaq_100 [INDICES]: last 30882.25, z20 0.91, zc 0.47, resid-z 0.41 [quiet], 1d 0.51%, 1y-pct=98
- dyn_nvda [EQUITIES]: last 229.63, z20 0.43, zc -0.17, resid-z -0.34 [quiet], 1d -0.37%, 1y-pct=96
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.952 vs sp500
- Watch next: vix (inverse) — not yet - watch; rho -0.723 vs sp500, historically leads by 4d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.856 vs sp500
- Watch next: brent (inverse) — not yet - watch; rho -0.609 vs sp500, historically leads by 2d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.782 vs sp500
- Source: As AT&T, Verizon and T-Mobile shares fall, Wall Street assesses the growing SpaceX threat — MarketWatch Top, 2026-10-09. https://www.marketwatch.com/story/as-at-t-verizon-and-t-mobile-shares-fall-wall-street-assesses-the-growing-spacex-threat-e869ef9e?mod=mw_rss_topstories
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks inch toward close of a record-breaking week — ET Markets, 2026-10-09. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-us-stock-market-live-updates-nasdaq-sp-500-iran-war-hormuz-deal-brent-crude-oil-fed-rate-yield-spacex-nvidia-tesla-apple-delta-ai-chip-stock-price-news-9th-october-2026/liveblog/134833667.cms
- Source: Why one Wall Street firm sees parallels to the late 1970s and recommends shorting U.S. stocks — MarketWatch Top, 2026-10-09. https://www.marketwatch.com/story/why-one-wall-street-firm-sees-parallels-to-the-late-1970s-and-recommends-shorting-u-s-stocks-bbd0ebd2?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-04 (d=0.18), 2025-08-28 (d=0.22)

### [AMBER 4.47] dyn_adanient_bo ↓
- dyn_adanient_bo [EQUITIES]: last 2633.10, z20 -2.47, zc 0.43, resid-z -0.18 [quiet], 1d 1.47%, |z20|=2.47
- **Mechanism**: dyn_adanient_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.552 via dyn_adanient_bo, z -2.34, reacted); nifty_50 (rho 0.378 via dyn_adanient_bo, z -1.3, reacted); nifty_midcap_100 (rho 0.373 via dyn_adanient_bo, z -1.38, reacted)
- **India receivers**: nifty_metal (rho 0.552, z -2.34); nifty_50 (rho 0.378, z -1.3); nifty_midcap_100 (rho 0.373, z -1.38)
- Source: Broker’s call: Adani Power (Accumulate) — BusinessLine Mkts, 2026-10-09. https://www.thehindubusinessline.com/markets/brokers-call-adani-power-accumulate/article71564351.ece
- Source: Adani Power shares: GQG Partners-managed entities cut stake to 5.72% from 5.74% — ET Markets, 2026-10-09. https://economictimes.indiatimes.com/markets/stocks/news/adani-power-shares-gqg-partners-managed-entities-cut-stake-to-5-72-from-5-74/articleshow/134834452.cms
- Source: Adani Power shares rise despite US-based FPI GQG Partners trimming stake in Gautam Adani-led company — Mint Markets, 2026-10-09. https://www.livemint.com/market/stock-market-news/adani-power-shares-rise-despite-us-based-fpi-gqg-partners-trimming-stake-in-gautam-adani-led-company-11791542076904.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [AMBER 4.13] indices · 2 series ↓
- nifty_50 [INDICES]: last 22520.45, z20 -1.30, zc 1.54, resid-z 2.23 [unexplained], 1d 1.30%, 1y-pct=2
- nifty_fmcg [INDICES]: last 44864.80, z20 -0.48, zc 2.25, resid-z 1.60 [unexplained], 1d 2.20%, 1y-pct=3
- **Mechanism**: indices · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-18 (z-distance 0.29).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.778 via nifty_50, z -1.38, reacted); dyn_jiofin_bo (rho 0.6 via nifty_50, z -1.25, reacted); nifty_metal (rho 0.585 via nifty_50, z -2.34, reacted); dyn_policybzr_ns (rho 0.515 via nifty_50, z -1.02, reacted); dyn_justdial_bo (rho 0.512 via nifty_50, z -1.42, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.778, z -1.38); dyn_jiofin_bo (rho 0.6, z -1.25); nifty_metal (rho 0.585, z -2.34); dyn_policybzr_ns (rho 0.515, z -1.02)
- Source: TCS rally pulls Dalal Street out of its 8-week rut — BusinessLine Mkts, 2026-10-09. https://www.thehindubusinessline.com/markets/tcs-lifts-dalal-street-out-of-its-eight-week-rut/article71563965.ece
- Source: Relief rally in Indian stock market; biggest weekly losing streak in 25 years snapped: What's next for Sensex, Nifty? — Mint Markets, 2026-10-09. https://www.livemint.com/market/stock-market-news/relief-rally-in-indian-stock-market-biggest-weekly-losing-streak-in-25-years-snapped-whats-next-for-sensex-nifty-11791550093630.html
- Source: Navratri 2025 to Navratri 2026: Nifty's performance - Top gainers, losers, outlook — Mint Markets, 2026-10-09. https://www.livemint.com/market/stock-market-news/navratri-2025-to-navratri-2026-niftys-performance-top-gainers-losers-outlook-11791549174535.html
- Historical analogues: 2025-07-18 (d=0.29), 2025-08-01 (d=0.88), 2025-07-11 (d=1.11)

### [AMBER 3.94] dyn_rs ↑
- dyn_rs [EQUITIES]: last 405.42, z20 1.94, zc 1.39, resid-z -0.73 [quiet], 1d 2.14%, 1y-pct=97
- **Mechanism**: dyn_rs ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Reliance Jio IPO price band alert: Mukesh Ambani's telecom giant likely to set band at  ₹1,065–  ₹1,119, says report — Mint Markets, 2026-10-09. https://www.livemint.com/market/stock-market-news/reliance-jio-ipo-price-band-revealed-price-band-fixed-at-rs-1-065-rs-1-119-report-11791554628948.html
- Source: Reliance Jio IPO: Likely price band for India's biggest listing revealed. Check details — ET Markets, 2026-10-09. https://economictimes.indiatimes.com/markets/ipos/fpos/reliance-jio-ipo-likely-price-band-range-for-indias-biggest-listing-revealed-check-details/articleshow/134831025.cms
- Source: Europe’s diesel shortage could lift Reliance’s O2C earnings 38% to ₹20,700 crore in Q2 — BusinessLine Mkts, 2026-10-09. https://www.thehindubusinessline.com/companies/europes-diesel-shortage-could-lift-reliances-o2c-earnings-38-to-20700-crore-in-q2/article71559652.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-30 (d=0.02), 2026-03-31 (d=0.02)

### [AMBER 3.88] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 6580.00, z20 1.88, zc -0.07, resid-z -2.11 [unexplained], 1d -0.45%, 1y-pct=99
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: South India set to play a key role in India’s next phase of steel growth: Experts — BusinessLine Mkts, 2026-10-09. https://www.thehindubusinessline.com/markets/commodities/south-india-set-to-play-a-key-role-in-indias-next-phase-of-steel-growth-experts/article71563711.ece
- Source: Experts say it's time to look at mid-caps, suggest looking at mid-cap funds through the SIP route — Mint Markets, 2026-10-09. https://www.livemint.com/market/stock-market-news/experts-say-its-time-to-look-at-mid-caps-suggest-looking-at-mid-cap-funds-through-the-sip-route-11791544855519.html
- Source: BEL shares down 16% in 6 months - Is a trend reversal in this multibagger defence stock on the cards? Experts decode — Mint Markets, 2026-10-09. https://www.livemint.com/market/stock-market-news/bel-shares-down-16-in-6-months-is-a-trend-reversal-in-this-multibagger-defence-stock-on-the-cards-experts-decode-11791540651920.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

## Watchlist (below surfacing floor)
shanghai_comp ↓ (3.87), dyn_muthootfin_ns ↓ (3.77), gold_silver_ratio ↑ (3.74), natgas ↑ (3.68), eur_usd ↓ (3.62), commodities · 2 series ↓ (3.48), comex_copper ↑ (3.32), dyn_jiofin_bo ↓ (3.25), dyn_hdb ↓ (3.06), dyn_policybzr_ns ↓ (3.02), dyn_karurvysya_ns ↑ (2.87), indices · 2 series ↓ (2.46)

## India macro
- nifty_50: 22520.4492 (1d 1.30%, z20 -1.30, flag amber)
- nifty_midcap_100: 58780.8984 (1d 1.56%, z20 -1.38, flag none)
- usd_inr: 96.7600 (1d 0.00%, z20 2.25, flag red)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6101 (1d 0.25%, z20 -1.46, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · India CPI T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 89.8 — "De Beers to open 100 Forevermark stores in India by 2030"
- COALINDIA.NS (COAL INDIA LTD) score 88.9 — "De Beers to open 100 Forevermark stores in India by 2030"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 87.4 — "De Beers to open 100 Forevermark stores in India by 2030"
- INDIANB.NS (INDIAN BANK) score 85.0 — "Micro, trading MSMEs need targeted support: Equitas Small Finance Bank MD"
- BAC (Bank of America Corporation) score 74.6 — "Micro, trading MSMEs need targeted support: Equitas Small Finance Bank MD"
- HDB (HDFC Bank Limited) score 68.0 — "Micro, trading MSMEs need targeted support: Equitas Small Finance Bank MD"
- IDBI.NS (IDBI BANK LIMITED) score 65.5 — "Micro, trading MSMEs need targeted support: Equitas Small Finance Bank MD"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 65.5 — "Micro, trading MSMEs need targeted support: Equitas Small Finance Bank MD"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 65.5 — "Micro, trading MSMEs need targeted support: Equitas Small Finance Bank MD"
- COIN (Coinbase Global, Inc.) score 61.4 — "Global refining shock lifts India’s diesel exports to a 12-month high in September"
- OHI (Omega Healthcare Investors, In) score 48.1 — "Share price down 29% in 2026, retail investors’ favourite wind energy stock under pressure"
- TECHM.NS (TECH MAHINDRA LIMITED) score 45.8 — "Anthem Biosciences block deal: Portsmouth Technologies sells 30 lakh shares worth Rs 250 c"
- BOND (PIMCO Active Bond Exchange-Tra) score 44.1 — "Reissued bonds account for nearly 66% of state borrowings in H1 FY27: Report"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 40.4 — "Anthem Biosciences block deal: Portsmouth Technologies sells 30 lakh shares worth Rs 250 c"
- TECH (Bio-Techne Corp) score 40.4 — "Anthem Biosciences block deal: Portsmouth Technologies sells 30 lakh shares worth Rs 250 c"
- TGT (Target Corporation) score 39.5 — "Sun TV share price: Why IPL team value is the new trigger; Elara sees 45% upside - Check t"
- CHKP (Check Point Software Technolog) score 36.3 — "Sun TV share price: Why IPL team value is the new trigger; Elara sees 45% upside - Check t"
- LTH (Life Time Group Holdings, Inc.) score 31.1 — "After TCS  ₹12 dividend, all eyes on Infosys Q2 results, dividend; date, time, earnings sc"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 28.5 — "Experts say it's time to look at mid-caps, suggest looking at mid-cap funds through the SI"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 25.8 — "Crude Oil is Underpriced, Energy Aspects Says"
- SEPN (Septerna, Inc.) score 24.5 — "Global refining shock lifts India’s diesel exports to a 12-month high in September"
- 301077.SZ (CHINASTARS) score 19.0 — "Copper Set for Weekly Gain on China’s Return and Supply Concerns"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 17.4 — "Adani Power shares: GQG Partners-managed entities cut stake to 5.72% from 5.74%"
- JIOFIN.BO (Jio Financial Services Limited) score 16.8 — "Anand Rathi Wealth Q2 results 2026: Dividend declared; check amount, record date, net prof"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.8 — "ET Alpha Wealth Summit 2.0 | SIFs, passive funds and GIFT City: How India's wealth portfol"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.8 — "ET Alpha Wealth Summit 2.0 | SIFs, passive funds and GIFT City: How India's wealth portfol"
- JUSTDIAL.BO (JUST DIAL LTD.) score 13.2 — "Madhusudan Kela-backed MV Electrosystems shares more than double from IPO price in just 2 "
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 12.4 — "Micro, trading MSMEs need targeted support: Equitas Small Finance Bank MD"
- BZ=F (Brent Crude Oil Last Day Finan) score 11.9 — "₹5 dividend vs  ₹34 last year: Why Vedanta's dividend payout story has fundamentally chang"
- JEF (Jefferies Financial Group Inc.) score 11.6 — "Kalyan Jewellers shares shine: 55% up in 3 months, Jefferies India sees further 46% upside"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 9.6 — "Micro, trading MSMEs need targeted support: Equitas Small Finance Bank MD"
- META (Meta) score 8.6 — "Monetary tightening likely to keep industrial metal prices on leash"
- NVDA (NVIDIA Corporation) score 8.3 — "Global Market: Maas Group shares plunge 11% after Nvidia-backed Firmus scraps $5 billion I"
- RS (Reliance, Inc.) score 7.7 — "Reliance Jio IPO price band alert: Mukesh Ambani's telecom giant likely to set band at  ₹1"
- VT (Vanguard Total World Stock Ind) score 7.6 — "World’s Top Crude Trader Isn’t Ruling Out $200 Oil Just Yet"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 5.6 — "Share price down 29% in 2026, retail investors’ favourite wind energy stock under pressure"
- GS (Goldman Sachs Group, Inc. (The) score 5.0 — "TCS shares jump 4% after Q2 results. What are Goldman Sachs, Nomura, others saying?"
- POLICYBZR.NS (PB FINTECH LIMITED) score 4.2 — "Nomura becomes latest brokerage to cut PB Fintech share price target by 31%, lists 2 scena"
- DELL (Dell Technologies Inc.) score 0.8 — "Piero Cipollone: Interview with Corriere della Sera"
- VOLTAS.NS (VOLTAS LTD) score 0.1 — "Voltas’s market share is growing. Will margins follow?"

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