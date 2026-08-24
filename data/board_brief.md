# Transmission Layer — board brief · 2026-08-24 07:18Z

data as of **2026-08-24** · 98 series · 14 red / 30 amber · 8 events surfaced (24 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.345, 2d in regime; vol-pct 0.274, breadth-off 0.417, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.42, corr60 -0.4, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.76, corr60 0.86, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.15, corr60 0.4, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.08, corr60 -0.11, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.7, corr60 -0.83, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.1, corr60 -0.13, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.3, corr60 -0.21, last shift 2026-06-30. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.26, corr60 0.2, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.0018708734390282533)
- **SETUP** dyn_ms → nikkei_225: leads 1d (ccf 0.413, β 0.3414, p 0.0); driver zc 1.75 → expected 1.112%. Type hit-rate 0.816 (n=2478).
- **SETUP** dyn_ms → taiwan_weighted: leads 1d (ccf 0.386, β 0.317, p 0.0); driver zc 1.75 → expected 1.032%. Type hit-rate 0.816 (n=2478).
- **SETUP** bovespa → usd_mxn: leads 1d (ccf -0.37, β -0.2162, p 0.0); driver zc 1.75 → expected -0.398%. Type hit-rate 0.816 (n=2478).
- Track record · residual_reversion: hit-rate **0.493** (n=1101) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.816** (n=2478) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.06] cross-asset · 4 series ↑
- dyn_mrna [EQUITIES]: last 145.04, z20 4.40, zc 0.66, resid-z 4.54 [unexplained], 1d 8.79%, |z20|=4.40; 1y-pct=100
- dyn_coin [EQUITIES]: last 186.57, z20 4.00, zc 1.58, resid-z 2.63 [unexplained], 1d 8.25%, |z20|=4.00
- btc_usd [CRYPTO]: last 77634.17, z20 3.25, zc -0.20, resid-z 3.11 [unexplained], 1d -0.89%, |z20|=3.25
- eth_usd [CRYPTO]: last 2464.14, z20 2.86, zc -0.41, resid-z 2.06 [unexplained], 1d -2.03%, |z20|=2.86
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.59).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Sensex today | Stock Market Live: Sensex, Nifty fall as high crude prices, weak global cues weigh — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-24-august-2026/article71380598.ece
- Source: 5 key themes set to drive global markets this week — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/us-stocks/news/5-key-themes-set-to-drive-global-markets-this-week/slideshow/133452590.cms
- Source: Global Market: Alibaba rout drags China, Hong Kong markets lower amid AI spending concerns — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-alibaba-rout-drags-china-hong-kong-markets-lower-amid-ai-spending-concerns/articleshow/133452201.cms
- Historical analogues: 2025-08-13 (d=0.59), 2025-05-09 (d=1.41), 2024-11-21 (d=1.48)

### [RED 7.59] commodities · 2 series ↑
- corn [COMMODITIES]: last 518.75, z20 4.76, zc 5.68, resid-z 0.49 [moved], 1d 7.24%, |z20|=4.76; 1y-pct=100
- wheat [COMMODITIES]: last 708.75, z20 3.18, zc 2.41, resid-z -0.26 [moved], 1d 4.00%, |z20|=3.18; 1y-pct=100
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Corn rockets to 3-year high as traders eye lower U.S. production — Mint Markets, 2026-08-24. https://www.livemint.com/market/corn-rockets-to-3-year-high-as-traders-eye-lower-u-s-production-11787533218087.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [AMBER 7.03] commodities · 2 series ↑
- brent [COMMODITIES]: last 92.69, z20 1.19, zc -0.88, resid-z 0.33 [quiet], 1d -1.80%, 1-session move -1.80% ≥ 1.5%
- wti [COMMODITIES]: last 85.09, z20 0.84, zc -1.00, resid-z -0.12 [quiet], 1d -2.26%, 1-session move -2.26% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.598 vs brent, historically leads by 5d
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.58 vs brent, historically leads by 5d
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.55 vs brent, historically leads by 5d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.693 vs brent
- Source: Sensex today | Stock Market Live: Sensex, Nifty fall as high crude prices, weak global cues weigh — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-24-august-2026/article71380598.ece
- Source: Rain Industries share price: Petrochemical stock jumps 4% amid soaring crude oil prices on US-Iran war — Mint Markets, 2026-08-24. https://www.livemint.com/market/stock-market-news/rain-industries-share-price-petrochemical-stock-jumps-4-amid-soaring-crude-oil-prices-on-us-iran-war-11787549018567.html
- Source: India 10-year bond yield clings to 6.85%; traders eye oil moves amid sanctions threat — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/markets/india-bonds-could-open-weaker-as-us-threatens-more-iran-sanctions/article71383094.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 6.54] cross-asset · 3 series ↑
- comex_gold [COMMODITIES]: last 4704.50, z20 2.38, zc 0.98, resid-z 0.88 [quiet], 1d 1.74%, |z20|=2.38; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 69.11, z20 1.75, zc -0.20, resid-z -0.90 [quiet], 1d -0.51%, |z20|=1.75; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 68.07, z20 -0.22, zc n/a, resid-z n/a [quiet], 1d 2.26%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.491 via comex_silver, z 1.55, reacted); dyn_stylebaaza_ns (rho -0.404 via gold_silver_ratio, z 1.41, reacted)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.624 vs comex_gold, historically leads by 1d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.56 vs comex_silver, historically leads by 4d
- Watch next: dax (co-move) — not yet - watch; rho 0.519 vs comex_gold, historically leads by 4d
- **India receivers**: nifty_metal (rho 0.491, z 1.55); dyn_stylebaaza_ns (rho -0.404, z 1.41)
- Source: Gold prices rise Rs 8,200/10g in 4 days; silver falls Rs 1,800/kg ahead of US inflation data. Buy, sell or hold? — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/commodities/news/gold-prices-rise-rs-8200/10g-in-4-days-silver-falls-rs-1800/kg-ahead-of-us-inflation-data-buy-sell-or-hold/articleshow/133450787.cms
- Source: Gold hits over 3-month high ahead of US inflation data, Fed chair speech — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/markets/gold/gold-hits-over-3-month-high-ahead-of-us-inflation-data-fed-chair-speech/article71383095.ece
- Source: Gold prices rise, silver drops on profit booking as focus shifts to US inflation data, US Fed Chair Kevin Warsh's speech — Mint Markets, 2026-08-24. https://www.livemint.com/market/commodities/gold-prices-rise-silver-drops-on-profit-booking-as-focus-shifts-to-us-inflation-data-us-fed-chair-kevin-warshs-speech-11787542262849.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 4.55] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.64, z20 1.55, zc n/a, resid-z n/a [quiet], 1d 0.33%, 52-wk extreme (pct=100); |z20|=1.55; 1y-pct=100
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.489 via midcap_largecap_ratio, z 0.66, quiet); dyn_fincables_ns (rho 0.368 via midcap_largecap_ratio, z 1.09, reacted); dyn_bharatcoal_ns (rho 0.357 via midcap_largecap_ratio, z 1.73, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.489, z 0.66); dyn_fincables_ns (rho 0.368, z 1.09); dyn_bharatcoal_ns (rho 0.357, z 1.73)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 4.32] fx · 4 series ↑
- aud_usd [FX]: last 0.72, z20 2.66, zc 1.41, resid-z -0.03 [quiet], 1d 0.69%, |z20|=2.66
- gbp_usd [FX]: last 1.36, z20 1.91, zc -0.01, resid-z 0.77 [quiet], 1d -0.00%, |z20|=1.91
- eur_usd [FX]: last 1.17, z20 1.84, zc -0.28, resid-z 0.38 [quiet], 1d -0.11%, |z20|=1.84
- usd_mxn [FX]: last 16.93, z20 -1.60, zc -0.31, resid-z -0.06 [quiet], 1d -0.12%, |z20|=1.60; 1y-pct=0
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.585 via aud_usd, z 3.43, reacted); nifty_midcap_100 (rho 0.422 via aud_usd, z 0.66, quiet); dyn_icicigi_bo (rho -0.411 via gbp_usd, z -1.17, reacted)
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.665 vs aud_usd, historically leads by 1d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.554 vs eur_usd
- **India receivers**: dyn_muthootfin_ns (rho 0.585, z 3.43); nifty_midcap_100 (rho 0.422, z 0.66); dyn_icicigi_bo (rho -0.411, z -1.17)
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [AMBER 4.16] dyn_lenskart_ns ↑
- dyn_lenskart_ns [EQUITIES]: last 659.70, z20 2.16, zc -0.16, resid-z 0.24 [quiet], 1d -0.26%, |z20|=2.16; 1y-pct=99
- **Mechanism**: dyn_lenskart_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_adanient_bo (rho 0.359 via dyn_lenskart_ns, z -1.2, reacted)
- **India receivers**: dyn_adanient_bo (rho 0.359, z -1.2)
- Source: 20 stocks to watch: Lenskart, Natco Pharma, Power Grid, GHCL, Sigachi — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/markets/20-stocks-to-watch-on-monday-lenskart-natco-pharma-power-grid-ghcl-sigachi-and-others/article71383021.ece
- Source: Lenskart Large Trade: 2.6% equity traded in a $300 million block deal; Softbank Vision likely seller — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/stocks/news/lenskart-solutions-shares-in-focus-after-300-million-block-deal-softbank-vision-fund-likely-seller/articleshow/133450319.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

### [AMBER 4.1] cross-asset · 3 series ↑
- dyn_bond [EQUITIES]: last 90.50, z20 -0.78, zc -0.41, resid-z -1.29 [quiet], 1d -0.13%, 1y-pct=3
- ust_30y [RATES]: last 5.23, z20 0.40, zc 0.90, resid-z 0.53 [quiet], 1d 0.77%, 1y-pct=96
- ust_10y [RATES]: last 4.69, z20 0.35, zc 0.86, resid-z 0.36 [quiet], 1d 0.86%, 1y-pct=96
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_2y (inverse) — not yet - watch; rho -0.752 vs dyn_bond, historically leads by 1d
- Watch next: wti (inverse) — not yet - watch; rho -0.562 vs dyn_bond, historically leads by 3d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.523 vs dyn_bond, historically leads by 3d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.531 vs dyn_bond
- Source: HDFC Bank shares rise as bond issue draw attention; Bank Nifty near resistance — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-rise-as-bond-issue-draw-attention-bank-nifty-near-resistance/article71383336.ece
- Source: India 10-year bond yield clings to 6.85%; traders eye oil moves amid sanctions threat — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/markets/india-bonds-could-open-weaker-as-us-threatens-more-iran-sanctions/article71383094.ece
- Source: ETMarkets Smart Talk | Have money in FDs? Why retail investors should consider 7-7.25% bond yields: Amit Somani — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/bonds/etmarkets-smart-talk-have-money-in-fds-why-retail-investors-should-consider-7-7-25-bond-yields-amit-somani/articleshow/133451013.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.12), 2025-04-23 (d=0.18)

## Watchlist (below surfacing floor)
cross-asset · 2 series ↑ (3.46), dyn_muthootfin_ns ↑ (3.43), dyn_stylebaaza_ns ↑ (3.41), dyn_pcjeweller_ns ↑ (3.3), dyn_icicigi_bo ↓ (3.17), dyn_cartrade_ns ↑ (3.15), dyn_tech ↑ (3.02), tips_10y_real ↓ (2.88), dyn_lth ↑ (2.74), brent_wti_spread ↑ (2.34), usd_cny ↓ (2.2), dyn_tatatech_ns ↑ (2.17)

## India macro
- nifty_50: 24182.5000 (1d -0.29%, z20 -0.87, flag none)
- nifty_midcap_100: 63761.8984 (1d 0.04%, z20 0.66, flag amber)
- usd_inr: 95.7200 (1d -0.05%, z20 0.60, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6367 (1d 0.33%, z20 1.55, flag red)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 77.5 — "LIC, Indian Overseas Bank among 10 stocks with maximum GoI holding in Q1: See full list"
- INOXINDIA.NS (INOX INDIA LIMITED) score 75.6 — "LIC, Indian Overseas Bank among 10 stocks with maximum GoI holding in Q1: See full list"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 75.3 — "LIC, Indian Overseas Bank among 10 stocks with maximum GoI holding in Q1: See full list"
- INDIANB.NS (INDIAN BANK) score 70.6 — "Kotak Bank Share Price Live Updates: Kotak Bank's Price Movement Today"
- BOND (PIMCO Active Bond Exchange-Tra) score 57.9 — "TRUMP SAYS BESSENT ACTED ALONE ON TREASURY BUYBACKS President Trump says he did not direct"
- BAC (Bank of America Corporation) score 57.9 — "Kotak Bank Share Price Live Updates: Kotak Bank's Price Movement Today"
- HDB (HDFC Bank Limited) score 53.4 — "Kotak Bank Share Price Live Updates: Kotak Bank's Price Movement Today"
- IDBI.NS (IDBI BANK LIMITED) score 51.0 — "Kotak Bank Share Price Live Updates: Kotak Bank's Price Movement Today"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 51.0 — "Kotak Bank Share Price Live Updates: Kotak Bank's Price Movement Today"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 51.0 — "Kotak Bank Share Price Live Updates: Kotak Bank's Price Movement Today"
- COIN (Coinbase Global, Inc.) score 43.5 — "Global Market: Alibaba shares slide after $10.2 billion share placement to fund AI expansi"
- TECHM.NS (TECH MAHINDRA LIMITED) score 40.1 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Performance Overview"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 38.4 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Performance Overview"
- TECH (Bio-Techne Corp) score 38.4 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Performance Overview"
- OHI (Omega Healthcare Investors, In) score 32.7 — "Balrampur Chini Mills share price up over 10% in 5 days - What's sweetening up stock inves"
- CHKP (Check Point Software Technolog) score 27.2 — "IPO GMP Today Live Updates: Symbiotec Pharmalab, Skyways Air Services IPO Day 1 bidding be"
- LTH (Life Time Group Holdings, Inc.) score 26.4 — "U.S. LABOR MARKET MAY BE WEAKER THAN HEADLINE DATA Nearly 25% of U.S. workers were “functi"
- JIOFIN.BO (Jio Financial Services Limited) score 18.4 — "IPO GMP Today Live Updates: Symbiotec Pharmalab, Skyways Air Services IPO Day 1 bidding be"
- 301077.SZ (CHINASTARS) score 17.5 — "Global Market: Alibaba rout drags China, Hong Kong markets lower amid AI spending concerns"
- PCJEWELLER.NS (PC JEWELLER LTD) score 16.2 — "Lalithaa Jewellery Mart shares surge 36% from IPO price after strong market debut. Should "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 11.4 — "Saatvik Green Energy shares post biggest 1-day gain in over a month on  ₹190 crore order w"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 11.1 — "Stocks to buy in 2026 for long term: Jubilant FoodWorks, Max Financial among 5 stocks that"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 11.0 — "India’s retail F&O losses mirror a global pattern"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.5 — "Tata Steel Share Price Live Updates: Tata Steel's Market Update: Today's Gains vs. Long-Te"
- MS (Morgan Stanley) score 9.2 — "Vishal Mega Mart shares soar 10% after CEO reappointment. Here's why Morgan Stanley sees 4"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 9.1 — "Coal India Share Price Live Updates: Coal India Ltd's Price Breakout Signals Strength"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.1 — "Tata Steel Share Price Live Updates: Tata Steel's Market Update: Today's Gains vs. Long-Te"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 8.3 — "Muthoot, Manappuram Finance shares jump up to 7% in 2 days as gold crosses Rs 1.6 lakh/10 "
- VT (Vanguard Total World Stock Ind) score 7.5 — "Super El Niño Threatens Food, Water and Trade Worldwide"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.8 — "SEBI rejects settlement bids by Adani-linked funds"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.4 — "ICICI Bank shares dip after AGM as selling pressure builds"
- JEF (Jefferies Financial Group Inc.) score 6.0 — "Why Jefferies’ Chris Wood sees gold as the second-best hedge amid Iran war and fiscal risk"
- META (Meta) score 5.4 — "Nifty edges higher at open; IT and Pharma drag, metals lead"
- MRNA (Moderna, Inc.) score 5.0 — "Moderna’s personalized mRNA shot could reshape the fight against skin cancer — but it may "
- JUSTDIAL.BO (JUST DIAL LTD.) score 4.2 — "Did Goodluck India shares really crash 66% in just one day? Here's how the bonus math work"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 3.9 — "Bharat Coking Coal shares jump over 7%. What's behind the sharp surge?"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.5 — "Lenskart Large Trade: 2.6% equity traded in a $300 million block deal; Softbank Vision lik"
- VOLTAS.NS (VOLTAS LTD) score 1.1 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.2 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.2 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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