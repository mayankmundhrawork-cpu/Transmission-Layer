# Transmission Layer — board brief · 2026-10-07 11:02Z

data as of **2026-10-07** · 97 series · 11 red / 36 amber · 8 events surfaced (33 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.69, 3d in regime; vol-pct 0.654, breadth-off 0.727, Markov P(high-vol) 0.015)
- [INVERTED] **safe_haven_gold** — corr20 -0.42, corr60 -0.43, contra nifty_50 corr20=0.1, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.81, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.07, corr60 0.15, last shift 2026-07-09. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.06, corr60 0.12, last shift 2026-08-24. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.77, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.16, corr60 -0.07, last shift 2026-08-17. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.3, corr60 -0.24, last shift 2026-08-17. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.51, corr60 0.19, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** stoxx_50 → asx_200: leads 1d (ccf 0.258, β 0.1965, p 0.00873); driver zc -1.71 → expected -0.311%. Type hit-rate 0.82 (n=2205).
- **SETUP** dax → asx_200: leads 1d (ccf 0.255, β 0.1858, p 0.00565); driver zc -1.5 → expected -0.262%. Type hit-rate 0.82 (n=2205).
- **SETUP** dax → usd_mxn: leads 1d (ccf -0.251, β -0.1389, p 0.0022); driver zc -1.5 → expected 0.196%. Type hit-rate 0.82 (n=2205).
- **SETUP** stoxx_50 → usd_mxn: leads 1d (ccf -0.251, β -0.1462, p 0.00318); driver zc -1.71 → expected 0.232%. Type hit-rate 0.82 (n=2205).
- Track record · residual_reversion: hit-rate **0.496** (n=1133) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.82** (n=2205) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.38] usd_inr ↑
- usd_inr [FX]: last 96.78, z20 2.38, zc 0.85, resid-z 0.95 [quiet], 1d 0.45%, 20d range extreme; |z20|=2.38; 1y-pct=99
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.407 via usd_inr, z 1.21, reacted); dyn_karurvysya_ns (rho -0.355 via usd_inr, z 0.42, quiet)
- **India receivers**: dyn_idbi_ns (rho -0.407, z 1.21); dyn_karurvysya_ns (rho -0.355, z 0.42)
- Source: Rupee nears record low despite RBI hike, governor says markets can be irrational — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-nears-record-low-despite-rbi-hike-governor-says-markets-can-be-irrational/articleshow/134763067.cms
- Source: Markets can be irrational in the short run: What RBI Governor Sanjay Malhotra said as rupee nears lifetime low — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/forex/forex-news/markets-can-be-irrational-in-the-short-run-what-rbi-guv-sanjay-malhotra-said-as-rupee-nears-lifetime-low/articleshow/134762634.cms
- Source: Rupee undervalued, RBI governor says, even as he promises stability against dollar — Mint Markets, 2026-10-07. https://www.livemint.com/market/commodities/rbi-governor-on-rupee-vs-dollar-exchange-rate-11791362751173.html
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2025-09-16 (d=0.01)

### [AMBER 5.87] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.66, z20 1.94, zc 0.44, resid-z 0.65 [quiet], 1d 0.53%, |z20|=1.94; 1y-pct=100
- ust_10y [RATES]: last 5.31, z20 1.66, zc 0.72, resid-z 1.07 [quiet], 1d 0.57%, |z20|=1.66; 1y-pct=100
- tips_10y_real [RATES]: last 2.95, z20 1.57, zc 0.69, resid-z 1.03 [quiet], 1d 1.03%, |z20|=1.57; 1y-pct=100
- dyn_bond [EQUITIES]: last 86.65, z20 -1.46, zc 0.81, resid-z -0.41 [quiet], 1d 0.30%, 1y-pct=1
- ust_2y [RATES]: last 4.84, z20 0.82, zc 0.78, resid-z 1.10 [quiet], 1d 0.21%, 1y-pct=98
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.706 vs ust_30y, historically leads by 3d
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.556 vs ust_30y
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.542 vs ust_30y
- Source: US 30-year bond yield hits fresh 24-year high — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/bonds/us-30-year-bond-yield-hits-fresh-24-year-high/articleshow/134763100.cms
- Source: Global Market: UK Gilt yields rise as oil, US Treasury yields weigh on bonds — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-uk-gilt-yields-rise-as-oil-us-treasury-yields-weigh-on-bonds/articleshow/134762712.cms
- Source: RBI policy verdict, guidance to drive nervous bond market traders — BusinessLine Mkts, 2026-10-07. https://www.thehindubusinessline.com/markets/rbi-policy-verdict-guidance-to-drive-nervous-bond-market-traders/article71554186.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.7] dyn_sepn ↓
- dyn_sepn [EQUITIES]: last 35.71, z20 -3.70, zc -1.40, resid-z -0.08 [quiet], 1d -5.72%, |z20|=3.70
- **Mechanism**: dyn_sepn ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: India's forex reserves fall for fourth week, down $50 bn from Sept peak at $734 bn — BusinessLine Mkts, 2026-10-07. https://www.thehindubusinessline.com/markets/forex/indias-forex-reserves-fall-for-fourth-week-down-50-bn-from-sep-peak-to-734-bn/article71554797.ece
- Source: IEX logs 10.4% growth in electricity trade volume to 12.2 billion units in Sept — BusinessLine Mkts, 2026-10-06. https://www.thehindubusinessline.com/economy/iex-logs-104-growth-in-electricity-trade-volume-to-122-billion-units-in-sept/article71550216.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-13 (d=0.0), 2025-05-01 (d=0.01)

### [AMBER 5.28] indices · 2 series ↑
- sp500 [INDICES]: last 7819.83, z20 2.45, zc 0.81, resid-z 0.67 [quiet], 1d 0.59%, |z20|=2.45; 1y-pct=100
- nasdaq_100 [INDICES]: last 31231.04, z20 1.84, zc 0.47, resid-z -0.27 [quiet], 1d 0.50%, |z20|=1.84; 1y-pct=100
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: vix (inverse) — not yet - watch; rho -0.746 vs sp500, historically leads by 4d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.867 vs sp500
- Watch next: brent (inverse) — not yet - watch; rho -0.65 vs sp500, historically leads by 2d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.785 vs sp500
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.568 vs nasdaq_100
- Source: The S&P 500 is back in record territory as the ‘Magnificent Seven’ ride to the rescue — MarketWatch Top, 2026-10-06. https://www.marketwatch.com/story/the-s-p-500-is-back-in-record-territory-as-the-magnificent-seven-ride-to-the-rescue-e062724d?mod=mw_rss_topstories
- Source: Marvell just impressed Wall Street with ‘good numbers plus a better story’ — MarketWatch Top, 2026-10-06. https://www.marketwatch.com/story/marvell-just-impressed-wall-street-with-good-numbers-plus-a-better-story-57fbbf23?mod=mw_rss_topstories
- Source: US stocks: S&P 500, Nasdaq reach record closing highs as focus pivots to earnings — ET Markets, 2026-10-06. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-sp-500-nasdaq-reach-record-closing-highs-as-focus-pivots-to-earnings/articleshow/134749835.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-07 (d=0.06), 2026-05-15 (d=0.07)

### [RED 5.04] dyn_ohi ↓
- dyn_ohi [EQUITIES]: last 44.77, z20 -3.04, zc -0.97, resid-z 1.04 [quiet], 1d -1.30%, |z20|=3.04
- **Mechanism**: dyn_ohi ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Global Market: Nomura Asset Management targets global investors as Japan markets regain appeal — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-nomura-asset-management-targets-global-investors-as-japan-markets-regain-appeal/articleshow/134762175.cms
- Source: Jio Platforms IPO: What does it mean for Reliance Industries share price? What should RIL investors do? — Mint Markets, 2026-10-07. https://www.livemint.com/market/stock-market-news/jio-platforms-ipo-what-does-it-mean-for-reliance-industries-share-price-what-should-ril-investors-do-11791361785458.html
- Source: RBI MPC 25 bps rate hike impact on stock market: Sensex, Nifty crash - Experts reveal what investors should do now — Mint Markets, 2026-10-07. https://www.livemint.com/market/stock-market-news/rbi-mpc-25-bps-rate-hike-impact-on-stock-market-sensex-nifty-fall-experts-reveal-what-investors-should-do-now-11791341499851.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2025-04-02 (d=0.09)

### [AMBER 4.92] indices · 2 series ↑
- nikkei_225 [INDICES]: last 70163.27, z20 2.09, zc -0.44, resid-z 0.55 [quiet], 1d -0.74%, |z20|=2.09; 1y-pct=97
- taiwan_weighted [INDICES]: last 49710.92, z20 1.97, zc -0.23, resid-z 0.11 [quiet], 1d -0.22%, |z20|=1.97; 1y-pct=99
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.7).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho 0.546 via taiwan_weighted, z -1.16, reacted); nifty_it (rho -0.367 via taiwan_weighted, z -1.45, reacted)
- Watch next: kospi (co-move) — not yet - watch; rho 0.844 vs nikkei_225
- **India receivers**: dyn_bajfinance_ns (rho 0.546, z -1.16); nifty_it (rho -0.367, z -1.45)
- Source: Stock market outlook today, 6 Oct: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Nikkei, Taiwan cues — Mint Markets, 2026-10-06. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-6-oct-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-nikkei-taiwan-cues-11791247193944.html
- Historical analogues: 2025-12-30 (d=0.7), 2025-07-11 (d=0.77), 2026-06-09 (d=1.0)

### [RED 4.66] dyn_techm_ns ↓
- dyn_techm_ns [EQUITIES]: last 1491.10, z20 -2.66, zc -0.58, resid-z -0.32 [quiet], 1d -0.89%, |z20|=2.66
- **Mechanism**: dyn_techm_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.838 via dyn_techm_ns, z -1.45, reacted); dyn_tataelxsi_ns (rho 0.467 via dyn_techm_ns, z -1.4, reacted); dyn_justdial_bo (rho 0.453 via dyn_techm_ns, z -1.05, reacted); dyn_tatatech_ns (rho 0.397 via dyn_techm_ns, z -1.01, reacted)
- **India receivers**: nifty_it (rho 0.838, z -1.45); dyn_tataelxsi_ns (rho 0.467, z -1.4); dyn_justdial_bo (rho 0.453, z -1.05); dyn_tatatech_ns (rho 0.397, z -1.01)
- Source: Kotak Mahindra Bank shares rise 2% as HSBC upgrades stock to buy — BusinessLine Mkts, 2026-10-07. https://www.thehindubusinessline.com/markets/kotak-mahindra-bank-shares-rise-2-as-hsbc-upgrades-stock-to-buy/article71554661.ece
- Source: PNB, Kotak Mahindra Bank, other bank stocks rise up to 2% after RBI’s rate hike, Nifty Bank above 55,500 — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/stocks/news/pnb-kotak-mahindra-bank-other-bank-stocks-rise-up-to-2-after-rbis-rate-hike-nifty-bank-above-55500/articleshow/134757463.cms
- Source: Market wrap: Trent, BSE, Coal India, Tech Mahindra top gainers and losers on Nifty and Sensex on Tuesday — ET Markets, 2026-10-06. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-trent-bse-coal-india-tech-mahindra-top-gainers-and-losers-on-nifty-and-sensex-on-tuesday/articleshow/134739696.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-11 (d=0.03), 2025-02-10 (d=0.09)

### [RED 4.64] dyn_adanient_bo ↓
- dyn_adanient_bo [EQUITIES]: last 2744.00, z20 -2.64, zc -1.67, resid-z -1.81 [unexplained], 1d -3.72%, |z20|=2.64
- **Mechanism**: dyn_adanient_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.452 via dyn_adanient_bo, z -2.49, reacted)
- **India receivers**: nifty_metal (rho 0.452, z -2.49)
- Source: Adani Power gains 2% after signing pact for 770-MW hydropower project in Bhutan — ET Markets, 2026-10-06. https://economictimes.indiatimes.com/markets/stocks/news/adani-power-gains-2-after-signing-pact-for-770-mw-hydropower-project-in-bhutan/articleshow/134723550.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

## Watchlist (below surfacing floor)
dxy ↑ (4.61), indices · 4 series ↓ (4.38), indices · 2 series ↓ (4.29), dyn_nvda ↑ (4.16), eur_usd ↓ (3.98), bovespa ↑ (3.78), hang_seng ↓ (3.71), gold_silver_ratio ↑ (3.7), hy_oas ↑ (3.65), comex_gold ↓ (3.61), dyn_rs ↑ (3.58), natgas ↑ (3.57)

## India macro
- nifty_50: 22603.0508 (1d -0.76%, z20 -1.46, flag amber)
- nifty_midcap_100: 59376.8516 (1d -0.64%, z20 -1.33, flag none)
- usd_inr: 96.7750 (1d 0.45%, z20 2.38, flag red)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6269 (1d 0.12%, z20 -0.80, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI MPC decision T-0d · AMFI SIP / MF flows T-1d · RBI Weekly Statistical Supplement T-2d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 88.8 — "Indian stock markets likely to open flat despite positive global cues"
- COALINDIA.NS (COAL INDIA LTD) score 86.1 — "Indian stock markets likely to open flat despite positive global cues"
- INOXINDIA.NS (INOX INDIA LIMITED) score 86.0 — "Indian stock markets likely to open flat despite positive global cues"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 83.5 — "Indian stock markets likely to open flat despite positive global cues"
- BAC (Bank of America Corporation) score 75.4 — "IDFC First Bank share: 30% rally in 6 months! Experts see more upside after Q2FY27 busines"
- HDB (HDFC Bank Limited) score 69.7 — "IDFC First Bank share: 30% rally in 6 months! Experts see more upside after Q2FY27 busines"
- IDBI.NS (IDBI BANK LIMITED) score 67.9 — "IDFC First Bank share: 30% rally in 6 months! Experts see more upside after Q2FY27 busines"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 67.9 — "IDFC First Bank share: 30% rally in 6 months! Experts see more upside after Q2FY27 busines"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 67.9 — "IDFC First Bank share: 30% rally in 6 months! Experts see more upside after Q2FY27 busines"
- COIN (Coinbase Global, Inc.) score 55.5 — "Indian stock markets likely to open flat despite positive global cues"
- OHI (Omega Healthcare Investors, In) score 48.6 — "Korean Investors Suffer $1.7 Billion Losses From Leveraged ETFs"
- TECHM.NS (TECH MAHINDRA LIMITED) score 46.2 — "China’s DeepZang AI aims to transform Tibetan language tech, promote ethnic unity"
- BOND (PIMCO Active Bond Exchange-Tra) score 45.8 — "RBI policy verdict, guidance to drive nervous bond market traders"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 38.0 — "China’s DeepZang AI aims to transform Tibetan language tech, promote ethnic unity"
- TECH (Bio-Techne Corp) score 38.0 — "China’s DeepZang AI aims to transform Tibetan language tech, promote ethnic unity"
- TGT (Target Corporation) score 36.1 — "IDFC First Bank share: 30% rally in 6 months! Experts see more upside after Q2FY27 busines"
- CHKP (Check Point Software Technolog) score 33.2 — "Stock split, spin-off: Last chance to buy these stocks today - Check record date, share pe"
- LTH (Life Time Group Holdings, Inc.) score 31.0 — "India’s central bank hikes rates for the first time since 2023 as inflation risks build"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 25.1 — "Suzlon Energy share: 25% dip in YTD! Will there be a trend reversal? Experts weigh in | Su"
- SEPN (Septerna, Inc.) score 23.1 — "Results of the September 2026 survey on credit terms and conditions in euro-denominated se"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 20.9 — "IDFC First Bank share: 30% rally in 6 months! Experts see more upside after Q2FY27 busines"
- 301077.SZ (CHINASTARS) score 16.5 — "China’s DeepZang AI aims to transform Tibetan language tech, promote ethnic unity"
- BZ=F (Brent Crude Oil Last Day Finan) score 15.8 — "Stock split, spin-off: Last chance to buy these stocks today - Check record date, share pe"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.5 — "Tata Motors PV Share Price Live Updates: Tata Motors PV Decline Noted"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 11.5 — "Tata Motors PV Share Price Live Updates: Tata Motors PV Decline Noted"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 11.5 — "Utkarsh Small Finance Bank shares rally 7% after Q2 disbursements jump 55% YoY, deposits r"
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.0 — "10 BSE 500 stocks tumble up to 45% in just one month"
- JIOFIN.BO (Jio Financial Services Limited) score 10.9 — "How RBI MPC 25 bps outcome impacted rate-sensitive sectors, Nifty Bank, Financial Services"
- JEF (Jefferies Financial Group Inc.) score 10.4 — "Jefferies increases weight in Reliance, 2 others; trims weight in 3 stocks in latest model"
- VT (Vanguard Total World Stock Ind) score 9.3 — "Why AI is both the hope and the hazard for world leaders, according to IMF chief Georgieva"
- META (Meta) score 8.1 — "Meta’s stock sees a golden cross as shares thrive since Muse introduction"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 8.0 — "Utkarsh Small Finance Bank shares rally 7% after Q2 disbursements jump 55% YoY, deposits r"
- NVDA (NVIDIA Corporation) score 7.4 — "SpaceX reportedly is looking to raise as much money as the company generates in revenue to"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 6.5 — "Trent’s Rs 1.80 lakh crore rout from peak: Has Q2 just flipped the script for Tata group’s"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.7 — "Adani Power gains 2% after signing pact for 770-MW hydropower project in Bhutan"
- RS (Reliance, Inc.) score 5.6 — "Jefferies increases weight in Reliance, 2 others; trims weight in 3 stocks in latest model"
- POLICYBZR.NS (PB FINTECH LIMITED) score 5.6 — "Pine Labs, CAMS, Moneyview, other fintech stocks rally up to 11% after RBI MPC move. Here’"
- GS (Goldman Sachs Group, Inc. (The) score 5.5 — "TSLA - GOLDMAN: TESLA’S AI STORY MATTERS MORE THAN Q3 EARNINGS Goldman Sachs reiterated it"
- VOLTAS.NS (VOLTAS LTD) score 0.1 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 0.1 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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