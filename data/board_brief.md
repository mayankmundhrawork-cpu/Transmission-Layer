# Transmission Layer — board brief · 2026-11-24 14:48Z

data as of **2026-11-24** · 97 series · 10 red / 37 amber · 8 events surfaced (30 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.958, 7d in regime; vol-pct 0.983, breadth-off 0.933, Markov P(high-vol) 0.567)
- [WEAK] **safe_haven_gold** — corr20 -0.18, corr60 -0.28, contra nifty_50 corr20=0.2, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.93, corr60 0.87, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.35, corr60 0.21, last shift 2026-09-22. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.22, corr60 0.04, last shift 2026-09-01. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.92, corr60 -0.9, last shift 2026-09-23. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.01, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.19, corr60 -0.01, last shift 2026-08-11. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.36, corr60 0.37, last shift 2026-10-07. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **10 of 89** scanned series survive multiplicity control (effective p ≤ 0.009880031515541177)
- **SETUP** dxy → eur_usd: leads 1d (ccf -0.836, β -0.894, p 0.0); driver zc -1.56 → expected 0.473%. Type hit-rate 0.82 (n=2093).
- **SETUP** dxy → gbp_usd: leads 1d (ccf -0.742, β -0.7864, p 0.0); driver zc -1.56 → expected 0.416%. Type hit-rate 0.82 (n=2093).
- **SETUP** dxy → usd_jpy: leads 1d (ccf 0.645, β 0.8996, p 0.0); driver zc -1.56 → expected -0.476%. Type hit-rate 0.82 (n=2093).
- **SETUP** dxy → aud_usd: leads 1d (ccf -0.571, β -0.8454, p 0.0); driver zc -1.56 → expected 0.447%. Type hit-rate 0.82 (n=2093).
- **SETUP** ust_2y → usd_jpy: leads 1d (ccf 0.483, β 0.2082, p 0.0); driver zc -2.02 → expected -0.569%. Type hit-rate 0.82 (n=2093).
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.458, β 0.2397, p 0.0); driver zc -2.21 → expected -0.571%. Type hit-rate 0.82 (n=2093).
- **SETUP** dxy → usd_mxn: leads 1d (ccf 0.437, β 0.6373, p 0.0); driver zc -1.56 → expected -0.337%. Type hit-rate 0.82 (n=2093).
- Track record · residual_reversion: hit-rate **0.507** (n=1152) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.82** (n=2093) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.57] cross-asset · 3 series ↓
- gold_silver_ratio [DERIVED]: last 85.97, z20 2.25, zc n/a, resid-z n/a [quiet], 1d 1.58%, GSR>85 (extreme high); |z20|=2.25; 1y-pct=100
- comex_silver [COMMODITIES]: last 42.12, z20 -2.03, zc -0.61, resid-z -0.56 [quiet], 1d -2.38%, |z20|=2.03; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- comex_gold [COMMODITIES]: last 3620.90, z20 -1.85, zc -0.30, resid-z -3.12 [unexplained], 1d -0.84%, |z20|=1.85; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.588 via comex_gold, z -0.51, quiet); dyn_karurvysya_ns (rho 0.509 via comex_gold, z 1.03, reacted)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.546 vs comex_silver, historically leads by 4d
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.521 vs comex_silver, historically leads by 5d
- **India receivers**: dyn_muthootfin_ns (rho 0.588, z -0.51); dyn_karurvysya_ns (rho 0.509, z 1.03)
- Source: Explained: Why Gold prices gained and extended a rebound from a 14-month low - 3 reasons — Mint Markets, 2026-11-24. https://www.livemint.com/market/stock-market-news/explained-why-gold-prices-gained-and-extended-a-rebound-from-a-14-month-low-3-reasons-11795514651749.html
- Source: How will the AI boom impact gold prices? 4 key factors investors should watch, explains World Gold Council strategist — Mint Markets, 2026-11-24. https://www.livemint.com/market/how-will-the-ai-boom-impact-gold-prices-4-key-factors-investors-should-watch-explains-world-gold-council-strategist-11795519705028.html
- Source: Silver price crash: Rates today in India down  ₹1 lakh in 3 months! Recovery or more fall ahead for MCX silver futures? — Mint Markets, 2026-11-24. https://www.livemint.com/market/commodities/silver-price-crash-rates-today-in-india-down-rs-1-lakh-in-3-months-recovery-or-more-fall-ahead-for-mcx-silver-futures-11795511561513.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 7.76] natgas ↑
- natgas [COMMODITIES]: last 3.65, z20 2.76, zc 3.73, resid-z 4.98 [unexplained], 1d 14.70%, 1-session move +14.70% ≥ 5.0%; |z20|=2.76
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: PNGRB proposes 14% assured returns to attract investment in natural gas pipelines — BusinessLine Mkts, 2026-11-24. https://www.thehindubusinessline.com/markets/commodities/pngrb-proposes-14-assured-returns-to-attract-investment-in-natural-gas-pipelines/article71738560.ece
- Source: Japan Poised to Ramp Up LNG Buying as Power Prices Surge — OilPrice, 2026-11-24. https://oilprice.com/Latest-Energy-News/World-News/Japan-Poised-to-Ramp-Up-LNG-Buying-as-Power-Prices-Surge.html
- Source: South Korea Asks Qatar for Priority LNG Once Hormuz Reopens — OilPrice, 2026-11-23. https://oilprice.com/Latest-Energy-News/World-News/South-Korea-Asks-Qatar-for-Priority-LNG-Once-Hormuz-Reopens.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [RED 6.84] rates · 2 series ↑
- hy_oas [RATES]: last 3.76, z20 4.01, zc 3.00, resid-z 0.45 [priced], 1d 6.82%, |z20|=4.01; 1y-pct=100
- ig_oas [RATES]: last 0.98, z20 3.23, zc 2.78, resid-z 0.71 [priced], 1d 4.26%, |z20|=3.23; 1y-pct=100
- **Mechanism**: rates · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.46 via ig_oas, z -1.13, reacted); nifty_it (rho 0.385 via ig_oas, z -0.3, quiet)
- Watch next: dyn_nvda (inverse) — not yet - watch; rho -0.51 vs hy_oas, historically leads by 2d
- Watch next: cac_40 (inverse) — not yet - watch; rho -0.501 vs hy_oas, historically leads by 3d
- Watch next: ust_2y (inverse) — not yet - watch; rho -0.537 vs hy_oas
- **India receivers**: midcap_largecap_ratio (rho -0.46, z -1.13); nifty_it (rho 0.385, z -0.3)
- Source: Dividend vs fixed deposits: 5 high yield stocks generating better income than FDs - CyberTech, Majestic Auto, to Premco — Mint Markets, 2026-11-24. https://www.livemint.com/market/stock-market-news/dividend-vs-fixed-deposits-5-high-yield-stocks-generating-better-income-than-fds-cybertech-majestic-auto-to-premco-11795463444218.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-01 (d=0.48), 2026-07-01 (d=0.59)

### [AMBER 6.36] cross-asset · 7 series ↓
- dyn_gs [EQUITIES]: last 817.48, z20 -2.02, zc -0.26, resid-z -0.65 [quiet], 1d -0.75%, |z20|=2.02
- dax [INDICES]: last 25100.44, z20 -1.83, zc -0.63, resid-z -1.97 [unexplained], 1d -0.93%, |z20|=1.83
- ftse_100 [INDICES]: last 10453.56, z20 -1.72, zc -0.28, resid-z -1.03 [quiet], 1d -0.26%, |z20|=1.72
- stoxx_50 [INDICES]: last 6025.89, z20 -1.65, zc -0.56, resid-z -1.22 [quiet], 1d -0.80%, |z20|=1.65
- russell_2000 [INDICES]: last 2657.99, z20 -1.54, zc -0.28, resid-z -0.10 [quiet], 1d -0.44%, |z20|=1.54
- vix [INDICES]: last 29.34, z20 1.47, zc 0.54, resid-z n/a [quiet], 1d 10.22%, 1y-pct=98
- dyn_nvda [EQUITIES]: last 155.80, z20 -0.90, zc -0.87, resid-z -2.60 [unexplained], 1d -5.60%, 1y-pct=2
- **Mechanism**: cross-asset · 7 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-04-02 (z-distance 0.69).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.477 via dax, z -0.51, quiet); dyn_kaynes_ns (rho 0.43 via ftse_100, z -2.03, reacted)
- Watch next: cac_40 (co-move) — not yet - watch; rho 0.913 vs dax
- **India receivers**: dyn_muthootfin_ns (rho 0.477, z -0.51); dyn_kaynes_ns (rho 0.43, z -2.03)
- Source: Nasdaq futures drop as AI stocks cool after Nvidia-fueled rally: US Stock Market Live Updates — ET Markets, 2026-11-24. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/stock-market-live-updates-dow-jones-nasdaq-sp-500-nvidia-anthropic-iphone-google-meta-tesla-earnings-treasury-yield-news-24-nov-2026/liveblog/136131363.cms
- Source: Jensen Huang’s return was worth nearly $950 billion to Nvidia. How much of the stock market should ride on one man? — MarketWatch Top, 2026-11-24. https://www.marketwatch.com/story/jensen-huangs-return-was-worth-nearly-950-billion-to-nvidia-how-much-of-the-stock-market-should-ride-on-one-man-c7129e95?mod=mw_rss_topstories
- Source: Nvidia's 37% rally wipes out gains for bearish investors; leveraged short ETFs plunge up to 92% — Mint Markets, 2026-11-24. https://www.livemint.com/market/nvidias-37-rally-wipes-out-gains-for-bearish-investors-leveraged-short-etfs-plunge-up-to-92-11795515861134.html
- Historical analogues: 2026-04-02 (d=0.69), 2025-04-02 (d=1.33), 2025-10-31 (d=1.47)

### [AMBER 6.23] brent ↓
- brent [COMMODITIES]: last 87.99, z20 -1.23, zc -0.73, resid-z -0.99 [quiet], 1d -1.54%, 1-session move -1.54% ≥ 1.5%; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: brent ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: South Korea Says Its Crude Supply Is Stable Through the Winter — OilPrice, 2026-11-24. https://oilprice.com/Latest-Energy-News/World-News/South-Korea-Says-Its-Crude-Supply-Is-Stable-Through-the-Winter.html
- Source: Oil Prices Hold Near Three-Month Lows Despite Hormuz Mine Claims — OilPrice, 2026-11-24. https://oilprice.com/Latest-Energy-News/World-News/Oil-Prices-Hold-Near-Three-Month-Lows-Despite-Hormuz-Mine-Claims.html
- Source: Crude oil prices near three-month lows as rising supply offsets Hormuz threat — BusinessLine Mkts, 2026-11-24. https://www.thehindubusinessline.com/markets/commodities/crude-oil-prices-near-three-month-lows-as-rising-supply-offsets-hormuz-threat/article71737296.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-14 (d=0.02), 2025-04-16 (d=0.04)

### [RED 4.55] dyn_chkp ↑
- dyn_chkp [EQUITIES]: last 163.33, z20 2.55, zc 0.94, resid-z -1.04 [quiet], 1d 2.56%, |z20|=2.55
- **Mechanism**: dyn_chkp ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Top defence stocks to buy: Apollo Micro Systems, BEL, Data Patterns, GRSE, Zen Technologies - check Choice's top picks — Mint Markets, 2026-11-24. https://www.livemint.com/market/stock-market-news/top-defence-stocks-to-buy-apollo-micro-systems-bel-data-patterns-grse-zen-technologies-check-choices-top-picks-11795507257890.html
- Source: Mahanadi Coalfields IPO: Allotment date, status check online by PAN number on BSE, NSE, Kfin Tech websites; listing date — Mint Markets, 2026-11-24. https://www.livemint.com/market/ipo/coal-indias-mahanadi-coalfields-ipo-allotment-likely-nov-25-heres-how-to-check-status-online-on-bse-nse-kfin-tech-11795494163132.html
- Source: Persistent Systems, Ather Energy shares: Top 2 stocks to buy on 25 Nov; check expected returns, stop loss, target price — Mint Markets, 2026-11-24. https://www.livemint.com/market/stock-market-news/persistent-systems-ather-energy-shares-top-2-stocks-to-buy-on-25-nov-check-expected-returns-stop-loss-target-price-11795486721247.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2025-05-20 (d=0.04)

### [RED 4.53] dyn_tgt ↑
- dyn_tgt [EQUITIES]: last 174.25, z20 2.53, zc 1.77, resid-z -2.28 [unexplained], 1d 3.60%, |z20|=2.53; 1y-pct=100
- **Mechanism**: dyn_tgt ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_30y (inverse) — not yet - watch; rho -0.533 vs dyn_tgt, historically leads by 4d
- Watch next: dyn_bond (co-move) — not yet - watch; rho 0.508 vs dyn_tgt, historically leads by 5d
- Watch next: ust_10y (inverse) — not yet - watch; rho -0.5 vs dyn_tgt, historically leads by 1d
- Watch next: dyn_ohi (co-move) — not yet - watch; rho 0.5 vs dyn_tgt, historically leads by 3d
- Source: Poonawalla Fincorp share price: After 25% jump in 1 month, JM Financial sees 21% further upside, raises target — Mint Markets, 2026-11-24. https://www.livemint.com/market/stock-market-news/poonawalla-fincorp-share-price-after-25-jump-in-1-month-jm-financial-sees-21-further-upside-raises-target-11795515723611.html
- Source: Penny stock under  ₹10 with high book value, strong fundamentals — Can it become a multibagger? Experts' views, target — Mint Markets, 2026-11-24. https://www.livemint.com/market/stock-market-news/penny-stock-under-rs-10-with-high-book-value-strong-fundamentals-can-it-become-a-multibagger-experts-views-target-11795505964712.html
- Source: Jensen Huang is back $1 trn m-cap; Nvidia's  ₹92.84 lakh cr comeback - 70% losses recovered; Baird is bullish; target — Mint Markets, 2026-11-24. https://www.livemint.com/market/stock-market-news/jensen-huang-is-back-1-trn-m-cap-nvidias-rs-92-84-lakh-cr-comeback-70-losses-recovered-baird-is-bullish-target-11795500713599.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.01), 2025-09-30 (d=0.01)

### [RED 4.5] dyn_coalindia_ns ↓
- dyn_coalindia_ns [EQUITIES]: last 382.00, z20 -2.50, zc -0.29, resid-z -0.11 [quiet], 1d -2.05%, |z20|=2.50
- **Mechanism**: dyn_coalindia_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Coal India unit Mahanadi's IPO fully subscribed on final day, led by institutional investors — BusinessLine Mkts, 2026-11-23. https://www.thehindubusinessline.com/markets/stock-markets/coal-india-unit-mahanadis-ipo-fully-subscribed-on-final-day-led-by-institutional-investors/article71734460.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.03), 2025-07-04 (d=0.04)

## Watchlist (below surfacing floor)
cross-asset · 2 series ↓ (4.33), dyn_tatatech_ns ↑ (4.15), usd_inr ↓ (3.9), comex_copper ↓ (3.89), tips_10y_real ↑ (3.42), dyn_atherenerg_ns ↑ (3.28), usd_mxn ↑ (3.22), dyn_301077_sz ↓ (3.11), dyn_crwv ↓ (3.05), dyn_lth ↑ (2.87), dyn_4417_t ↑ (2.58), dyn_tech ↑ (2.56)

## India macro
- nifty_50: 25366.4004 (1d -1.68%, z20 0.97, flag none)
- nifty_midcap_100: 61403.8516 (1d -1.00%, z20 0.83, flag none)
- usd_inr: 92.9000 (1d 0.24%, z20 -1.90, flag amber)
- goi_10y: 7.3800 (1d 4.53%, z20 3.03, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.1400 (1d -5.73%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4207 (1d 0.70%, z20 -1.13, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 66.0 — "Silver price crash: Rates today in India down  ₹1 lakh in 3 months! Recovery or more fall "
- NVDA (NVIDIA Corporation) score 63.7 — "Jensen Huang reinstated NVIDIA CEO! How may it impact Sensex, Nifty recovery as bets are h"
- INOXINDIA.NS (INOX INDIA LIMITED) score 61.2 — "Silver price crash: Rates today in India down  ₹1 lakh in 3 months! Recovery or more fall "
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 60.9 — "Silver price crash: Rates today in India down  ₹1 lakh in 3 months! Recovery or more fall "
- INDIANB.NS (INDIAN BANK) score 47.9 — "HDFC Bank, Reliance Industries among 10 stocks with highest DII holding in Q2. See full li"
- BAC (Bank of America Corporation) score 37.3 — "HDFC Bank, Reliance Industries among 10 stocks with highest DII holding in Q2. See full li"
- OHI (Omega Healthcare Investors, In) score 33.4 — "Investors mint Rs 34.61 lakh cr in November as markets rally nearly 11%"
- HDB (HDFC Bank Limited) score 32.9 — "HDFC Bank, Reliance Industries among 10 stocks with highest DII holding in Q2. See full li"
- TECHM.NS (TECH MAHINDRA LIMITED) score 32.5 — "Top defence stocks to buy: Apollo Micro Systems, BEL, Data Patterns, GRSE, Zen Technologie"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 31.5 — "HDFC Bank, Reliance Industries among 10 stocks with highest DII holding in Q2. See full li"
- IDBI.NS (IDBI BANK LIMITED) score 31.5 — "HDFC Bank, Reliance Industries among 10 stocks with highest DII holding in Q2. See full li"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 31.5 — "HDFC Bank, Reliance Industries among 10 stocks with highest DII holding in Q2. See full li"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 30.7 — "Top defence stocks to buy: Apollo Micro Systems, BEL, Data Patterns, GRSE, Zen Technologie"
- TECH (Bio-Techne Corp) score 30.7 — "Top defence stocks to buy: Apollo Micro Systems, BEL, Data Patterns, GRSE, Zen Technologie"
- TGT (Target Corporation) score 29.8 — "Jensen Huang is back $1 trn m-cap; Nvidia's  ₹92.84 lakh cr comeback - 70% losses recovere"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 25.5 — "How does EIA compare different types of energy?"
- BLLN (BillionToOne, Inc.) score 23.1 — "PE-VC ‘mega’ deals hit three year high in 2026 (YTD) at $31 billion"
- CHKP (Check Point Software Technolog) score 20.7 — "Top defence stocks to buy: Apollo Micro Systems, BEL, Data Patterns, GRSE, Zen Technologie"
- 2545.TW (HUANG HSIANG CONSTRUCTION) score 20.5 — "Nasdaq surges 6%, Dow soars 1,400 pts as markets rebound on Huang’s return: Stock Market H"
- 301077.SZ (CHINASTARS) score 18.3 — "TRUMP SAYS HE DID NOT ASK CHINA'S XI WHETHER WOMAN LINKED TO HUANG WAS A SPY"
- COIN (Coinbase Global, Inc.) score 17.6 — "Global crude oil prices may fall to $70 by end-2027 as supply surplus looms"
- LTH (Life Time Group Holdings, Inc.) score 16.4 — "Gold rate today, 24 November 2026: Gold price rebounds from 14-month low; is it the right "
- BOND (PIMCO Active Bond Exchange-Tra) score 12.9 — "Japanese bond yields fall as lower oil prices ease inflation concerns"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 12.6 — "Gold rate today, 24 November 2026: Gold price rebounds from 14-month low; is it the right "
- JIOFIN.BO (Jio Financial Services Limited) score 10.3 — "Poonawalla Fincorp share price: After 25% jump in 1 month, JM Financial sees 21% further u"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 10.0 — "Climate Finance Dispute Derails COP31 Negotiations"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.4 — "Stocks to watch, Nov 23: Tata Steel, APL Apollo Tubes, IndusInd Bank, NSE, Adani Energy, W"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.4 — "Stocks to watch, Nov 23: Tata Steel, APL Apollo Tubes, IndusInd Bank, NSE, Adani Energy, W"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 8.4 — "Climate Finance Dispute Derails COP31 Negotiations"
- BZ=F (Brent Crude Oil Last Day Finan) score 8.2 — "NVDA - NVIDIA SHARES EXTEND PREMARKET GAINS, LAST UP 27%"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.3 — "Amazon may have just found a ‘cheap’ way to get a lot more out of its chips"
- META (Meta) score 6.8 — "The Energy Transition Needs More Metals but Less Extraction"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.6 — "Stocks to watch, Nov 23: Tata Steel, APL Apollo Tubes, IndusInd Bank, NSE, Adani Energy, W"
- MS (Morgan Stanley) score 3.3 — "JPMORGAN SEES THREE MORE FED RATE HIKES AS U.S. GROWTH AND AI SPENDING MODERATE IN 2027 JP"
- GS (Goldman Sachs Group, Inc. (The) score 3.0 — "Rupee retreats, Goldman calls it a 'port of stability' in AI storm"
- CRWV (CoreWeave, Inc.) score 2.5 — "Oracle and CoreWeave stocks stage big gains as investors bet the AI cash will keep flowing"
- RS (Reliance, Inc.) score 2.2 — "HDFC Bank, Reliance Industries among 10 stocks with highest DII holding in Q2. See full li"
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 1.6 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "
- ETERNAL.NS (ETERNAL LIMITED) score 1.1 — "Goldman Sachs names 22 ‘high-growth’ stocks; Bharti Airtel, Eternal and HDFC Bank feature "
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 1.0 — "Tech Query: ICICI Bank, Gujarat Energy, Kaynes Technology Limited, Cochin Shipyard — What "

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