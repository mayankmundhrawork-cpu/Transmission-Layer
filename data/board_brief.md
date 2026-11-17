# Transmission Layer — board brief · 2026-11-17 04:03Z

data as of **2026-11-17** · 97 series · 9 red / 38 amber · 8 events surfaced (22 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.626, 2d in regime; vol-pct 0.628, breadth-off 0.625, Markov P(high-vol) 0.034)
- [INVERTED] **safe_haven_gold** — corr20 -0.09, corr60 -0.21, contra nifty_50 corr20=0.32, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.88, corr60 0.84, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.15, corr60 0.1, last shift 2026-09-17. Channel: global copper leads Indian metal equities
- [INVERTED] **inr_oil_channel** — corr20 -0.31, corr60 0.04, last shift 2026-09-01. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.91, last shift 2026-09-23. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.27, corr60 0.0, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.05, corr60 -0.17, last shift 2026-08-11. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.37, corr60 0.32, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 0.0006738585313537104)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.515** (n=1159) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.815** (n=2130) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.62] rates · 4 series ↑
- tips_10y_real [RATES]: last 2.91, z20 2.95, zc 0.88, resid-z 0.62 [quiet], 1d 1.75%, 1d move +5.0bps ≥ 5bps; |z20|=2.95; 1y-pct=97
- ust_2y [RATES]: last 4.88, z20 2.05, zc 0.30, resid-z -0.11 [quiet], 1d 0.41%, |z20|=2.05; 1y-pct=98
- ust_30y [RATES]: last 5.47, z20 1.88, zc 0.83, resid-z 0.51 [quiet], 1d 0.74%, |z20|=1.88
- ust_10y [RATES]: last 5.15, z20 1.66, zc 0.88, resid-z 0.55 [quiet], 1d 0.98%, |z20|=1.66
- **Mechanism**: rates · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_tgt (inverse) — not yet - watch; rho -0.581 vs ust_30y
- Watch next: dyn_schd (inverse) — not yet - watch; rho -0.521 vs tips_10y_real
- Source: Rupee likely to open flat as dollar strength, US bond yields weigh on sentiment — BusinessLine Mkts, 2026-11-16. https://www.thehindubusinessline.com/markets/forex/rupee-likely-to-open-flat-as-dollar-strength-us-bond-yields-weigh-on-sentiment/article71706648.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.26), 2026-05-14 (d=0.57)

### [AMBER 8.73] cross-asset · 8 series ↓
- dyn_nvda [EQUITIES]: last 156.16, z20 -2.20, zc -0.49, resid-z -0.50 [quiet], 1d -4.11%, |z20|=2.20; 1y-pct=0
- btc_usd [CRYPTO]: last 64985.54, z20 -2.17, zc -0.09, resid-z -1.19 [quiet], 1d -0.29%, |z20|=2.17
- dyn_coin [EQUITIES]: last 119.83, z20 -1.98, zc -0.49, resid-z -0.11 [quiet], 1d -6.13%, 1y-pct=0
- eth_usd [CRYPTO]: last 1831.96, z20 -1.94, zc 0.11, resid-z -0.81 [quiet], 1d 0.48%, |z20|=1.94
- sp500 [INDICES]: last 7420.19, z20 -1.78, zc -0.30, resid-z -0.25 [quiet], 1d -1.87%, |z20|=1.78
- russell_2000 [INDICES]: last 2743.39, z20 -1.55, zc -0.21, resid-z 0.30 [quiet], 1d -1.69%, |z20|=1.55
- nasdaq_100 [INDICES]: last 27204.77, z20 -1.55, zc -0.57, resid-z -1.47 [quiet], 1d -2.64%, |z20|=1.55
- vix [INDICES]: last 22.88, z20 1.23, zc 0.34, resid-z n/a [quiet], 1d 18.55%, 1-session move +18.55% ≥ 15.0%
- **Mechanism**: cross-asset · 8 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.5).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho -0.426 via dyn_nvda, z 1.62, reacted)
- Watch next: dyn_rs (co-move) — not yet - watch; rho 0.606 vs russell_2000, historically leads by 4d
- Watch next: dyn_bac (co-move) — not yet - watch; rho 0.543 vs russell_2000, historically leads by 2d
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.685 vs dyn_nvda
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.519 vs dyn_nvda
- **India receivers**: dyn_bajfinance_ns (rho -0.426, z 1.62)
- Source: Sensex today | Stock Market Live Updates: Sensex, Nifty likely to open flat after 10% November rally; global tech sell-off weighs — BusinessLine Mkts, 2026-11-17. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-17th-november-2026/article71708442.ece
- Source: Nvidia slides 4.1% as US tech stocks plunge; Nasdaq falls 2.5% — BusinessLine Mkts, 2026-11-17. https://www.thehindubusinessline.com/markets/stock-markets/nvidia-slides-41-as-us-tech-stocks-plunge-nasdaq-falls-25/article71710260.ece
- Source: Stock market outlook today,17 Nov:Sensex, Nifty prediction-DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-17. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-17-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-cue-11794875550779.html
- Historical analogues: 2026-05-22 (d=0.5), 2025-10-23 (d=0.66), 2025-08-19 (d=0.99)

### [RED 6.97] usd_inr ↓
- usd_inr [FX]: last 93.64, z20 -1.97, zc -1.47, resid-z 0.74 [quiet], 1d -0.64%, 20d range extreme; |z20|=1.97
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_havells_ns (rho -0.502 via usd_inr, z 1.72, reacted); dyn_indianb_ns (rho -0.458 via usd_inr, z 1.73, reacted); nifty_it (rho -0.422 via usd_inr, z -0.83, quiet); dyn_bajfinance_ns (rho -0.379 via usd_inr, z 1.62, reacted); dyn_tataelxsi_ns (rho -0.379 via usd_inr, z -0.62, quiet)
- **India receivers**: dyn_havells_ns (rho -0.502, z 1.72); dyn_indianb_ns (rho -0.458, z 1.73); nifty_it (rho -0.422, z -0.83); dyn_bajfinance_ns (rho -0.379, z 1.62)
- Source: Rupee rises 27 paise to close at 93.92 against US dollar — BusinessLine Mkts, 2026-11-16. https://www.thehindubusinessline.com/markets/forex/rupee-rises-27-paise-to-close-at-9392-against-us-dollar/article71707584.ece
- Source: Rupee rises, volatility ebbs as equity inflows blunt global headwinds — ET Markets, 2026-11-16. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-rises-volatility-ebbs-as-equity-inflows-blunt-global-headwinds/articleshow/135883543.cms
- Source: Rupee rises 6 paise to 94.13 against US dollar in early trade — BusinessLine Mkts, 2026-11-16. https://www.thehindubusinessline.com/markets/forex/rupee-rises-6-paise-to-9413-against-us-dollar-in-early-trade/article71706773.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 5.86] cross-asset · 4 series ↓
- comex_copper [COMMODITIES]: last 5.98, z20 -2.20, zc 0.00, resid-z -0.94 [quiet], 1d 0.01%, |z20|=2.20
- comex_silver [COMMODITIES]: last 47.35, z20 -1.89, zc -0.01, resid-z -1.40 [quiet], 1d -0.02%, |z20|=1.89; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 81.82, z20 1.88, zc n/a, resid-z n/a [quiet], 1d 0.02%, |z20|=1.88; 1y-pct=100
- comex_gold [COMMODITIES]: last 3874.30, z20 -1.73, zc 0.00, resid-z 0.30 [quiet], 1d 0.00%, |z20|=1.73; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.45 via comex_gold, z 0.81, quiet); dyn_karurvysya_ns (rho 0.428 via comex_gold, z 2.3, reacted)
- **India receivers**: dyn_muthootfin_ns (rho 0.45, z 0.81); dyn_karurvysya_ns (rho 0.428, z 2.3)
- Source: Gold prices near 1-year low, silver slides as dollar hits 19-month high: Should you buy before wedding season or wait? — Mint Markets, 2026-11-17. https://www.livemint.com/market/stock-market-news/gold-prices-near-1-year-low-silver-slides-as-dollar-hits-19-month-high-should-you-buy-before-wedding-season-or-wait-11794882191547.html
- Source: Top stocks to watch today: Senco Gold, Adani Enterprises, BSE, Cipla shares in focus on Tuesday, 17 November | Full list — Mint Markets, 2026-11-17. https://www.livemint.com/market/stock-market-news/top-stocks-to-watch-today-senco-gold-adani-enterprises-bse-cipla-shares-in-focus-on-tuesday-17-november-full-list-11794879685406.html
- Source: Gold hovers near over one-year low as firm dollar, Fed-hike bets weigh — ET Markets, 2026-11-17. https://economictimes.indiatimes.com/markets/commodities/news/gold-hovers-near-over-one-year-low-as-firm-dollar-fed-hike-bets-weigh/articleshow/135907217.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.34)

### [RED 5.64] fx · 2 series ↓
- eur_usd [FX]: last 1.10, z20 -2.81, zc -0.40, resid-z -1.27 [quiet], 1d -0.15%, |z20|=2.81; 1y-pct=0
- gbp_usd [FX]: last 1.32, z20 -2.48, zc -0.46, resid-z -1.13 [quiet], 1d -0.17%, |z20|=2.48; 1y-pct=2
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.052 vs eur_usd, historically leads by 1d
- Source: Boris Vujčić: Risks and resilience in the euro area financial system — ECB press, 2026-11-16. https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp261116~db374b56ab.en.html
- Source: Yen steady against euro and dollar after soft Japanese GDP data — Mint Markets, 2026-11-16. https://www.livemint.com/market/yen-steady-against-euro-and-dollar-after-soft-japanese-gdp-data-11794791270301.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [RED 5.47] dyn_blln ↓
- dyn_blln [EQUITIES]: last 96.10, z20 -3.47, zc -1.53, resid-z -0.57 [moved], 1d -8.61%, |z20|=3.47
- **Mechanism**: dyn_blln ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Why Iraq Just Fast-Tracked Chevron’s Takeover Of A 14-Billion-Barrel Supergiant — OilPrice, 2026-11-17. https://oilprice.com/Energy/Energy-General/Why-Iraq-Just-Fast-Tracked-Chevrons-Takeover-Of-A-14-Billion-Barrel-Supergiant.html
- Source: NVDA - JENSEN HUANG TRANSFERRED OVER $10 BILLION IN NVIDIA STOCK TO FAMILY TRUST BEFORE DOWNFALL Former Nvidia CEO Jensen Huang and his wife transferred nearly 60 million shares, worth over $10.5 billion, into an irrevocable family trust in March, according to SEC filings reviewed by Barron's. The t — DeItaone, 2026-11-16. https://t.me/walter_bloomberg/38619
- Source: MACQUARIE WARNS OF DATA CENTER EXUBERANCE AMID TRILLION-DOLLAR AI BUILDOUT Macquarie Asset Management, overseeing $503 billion, warns that soaring data center valuations are increasing investment risks despite strong structural AI demand. CEO Ben Way says investors are paying excessive prices for ex — DeItaone, 2026-11-16. https://t.me/walter_bloomberg/38618

### [AMBER 5.34] cross-asset · 4 series ↑
- nifty_fmcg [INDICES]: last 47778.10, z20 1.67, zc 0.12, resid-z 0.79 [quiet], 1d 0.15%, |z20|=1.67
- dyn_bajfinance_ns [EQUITIES]: last 1116.25, z20 1.62, zc 0.28, resid-z 0.62 [quiet], 1d 0.56%, 1y-pct=97
- nifty_midcap_100 [INDICES]: last 61937.85, z20 1.53, zc 0.55, resid-z 0.48 [quiet], 1d 0.59%, |z20|=1.53
- nifty_50 [INDICES]: last 25325.60, z20 1.50, zc 0.12, resid-z -0.92 [quiet], 1d 0.14%, |z20|=1.50
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-18 (z-distance 0.56).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.81 via nifty_midcap_100, z 0.96, quiet); nifty_metal (rho 0.734 via nifty_midcap_100, z 0.76, quiet); dyn_muthootfin_ns (rho 0.699 via nifty_midcap_100, z 0.81, quiet); dyn_indusindbk_bo (rho 0.671 via nifty_midcap_100, z 1.24, reacted); dyn_indianb_ns (rho 0.601 via nifty_midcap_100, z 1.73, reacted)
- Watch next: nifty_metal (co-move) — not yet - watch; rho 0.734 vs nifty_midcap_100, historically leads by 5d
- Watch next: dyn_jiofin_bo (co-move) — not yet - watch; rho 0.585 vs nifty_fmcg, historically leads by 2d
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.555 vs nifty_fmcg, historically leads by 2d
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.528 vs nifty_50, historically leads by 5d
- Watch next: dyn_adanient_bo (co-move) — not yet - watch; rho 0.525 vs nifty_midcap_100, historically leads by 5d
- **India receivers**: dyn_jiofin_bo (rho 0.81, z 0.96); nifty_metal (rho 0.734, z 0.76); dyn_muthootfin_ns (rho 0.699, z 0.81); dyn_indusindbk_bo (rho 0.671, z 1.24)
- Source: Sensex today | Stock Market Live Updates: Sensex, Nifty likely to open flat after 10% November rally; global tech sell-off weighs — BusinessLine Mkts, 2026-11-17. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-17th-november-2026/article71708442.ece
- Source: Stock Market Live Updates | Opening Bell: Sensex gains over 200 pts, Nifty above 25,300; Indigo, Adani Ports rise up to 2% — ET Markets, 2026-11-17. https://economictimes.indiatimes.com/markets/stocks/live-blog/bse-sensex-today-nifty50-stock-market-live-updates-gift-nifty-adani-enterprises-bse-share-price-17-november-2026/liveblog/135907345.cms
- Source: Stock market outlook today,17 Nov:Sensex, Nifty prediction-DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-17. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-17-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-cue-11794875550779.html
- Historical analogues: 2025-07-18 (d=0.56), 2025-07-11 (d=1.04), 2025-12-29 (d=1.63)

### [RED 5.26] dxy ↑
- dxy [FX]: last 103.52, z20 2.26, zc 0.02, resid-z 0.14 [quiet], 1d 0.01%, 20d range extreme; |z20|=2.26; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-10 (d=0.03), 2025-05-14 (d=0.06)

## Watchlist (below surfacing floor)
indices · 3 series ↓ (4.98), dyn_kaynes_ns ↓ (4.92), indices · 3 series ↑ (3.47), dyn_atherenerg_ns ↑ (3.44), dyn_tech ↑ (3.24), eur_inr ↓ (2.9), dyn_4417_t ↑ (2.87), dyn_schd ↑ (2.82), dyn_lth ↑ (2.71), aud_usd ↓ (2.5), dyn_karurvysya_ns ↑ (2.3), dyn_inoxindia_ns ↑ (2.19)

## India macro
- nifty_50: 25325.5996 (1d 0.14%, z20 1.50, flag amber)
- nifty_midcap_100: 61937.8516 (1d 0.59%, z20 1.53, flag amber)
- usd_inr: 93.6375 (1d -0.64%, z20 -1.97, flag red)
- goi_10y: 7.3800 (1d 4.53%, z20 3.03, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.1400 (1d -5.73%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4457 (1d 0.45%, z20 -0.98, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 69.6 — "Stock recommendations for 17 November from MarketSmith India"
- INOXINDIA.NS (INOX INDIA LIMITED) score 66.6 — "Stock recommendations for 17 November from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 65.7 — "Stock recommendations for 17 November from MarketSmith India"
- NVDA (NVIDIA Corporation) score 60.4 — "OPENAI CEO SAM ALTMAN - AI REVOLUTION WITHOUT EX-NVIDIA CEO HUANG IS ‘HARD TO IMAGINE’ - S"
- INDIANB.NS (INDIAN BANK) score 45.8 — "JPM $BAC $WFC $USB $COF - MULTIPLE U.S. BANKS FACE SERVICE DISRUPTION REPORTS Several majo"
- BAC (Bank of America Corporation) score 43.2 — "JPM $BAC $WFC $USB $COF - MULTIPLE U.S. BANKS FACE SERVICE DISRUPTION REPORTS Several majo"
- TECHM.NS (TECH MAHINDRA LIMITED) score 42.2 — "FED CHAIR WARSH WARNS AI COULD TRIGGER MAJOR ECONOMIC DISRUPTION Fed Chair Kevin Warsh say"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.5 — "FED CHAIR WARSH WARNS AI COULD TRIGGER MAJOR ECONOMIC DISRUPTION Fed Chair Kevin Warsh say"
- TECH (Bio-Techne Corp) score 39.5 — "FED CHAIR WARSH WARNS AI COULD TRIGGER MAJOR ECONOMIC DISRUPTION Fed Chair Kevin Warsh say"
- HDB (HDFC Bank Limited) score 37.4 — "JPM $BAC $WFC $USB $COF - MULTIPLE U.S. BANKS FACE SERVICE DISRUPTION REPORTS Several majo"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 34.4 — "JPM $BAC $WFC $USB $COF - MULTIPLE U.S. BANKS FACE SERVICE DISRUPTION REPORTS Several majo"
- IDBI.NS (IDBI BANK LIMITED) score 34.4 — "JPM $BAC $WFC $USB $COF - MULTIPLE U.S. BANKS FACE SERVICE DISRUPTION REPORTS Several majo"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 34.4 — "JPM $BAC $WFC $USB $COF - MULTIPLE U.S. BANKS FACE SERVICE DISRUPTION REPORTS Several majo"
- TGT (Target Corporation) score 29.0 — "SPCX: CITIGROUP RAISES TARGET PRICE TO $280 FROM $240"
- OHI (Omega Healthcare Investors, In) score 24.5 — "MACQUARIE WARNS OF DATA CENTER EXUBERANCE AMID TRILLION-DOLLAR AI BUILDOUT Macquarie Asset"
- COIN (Coinbase Global, Inc.) score 24.5 — "MSFT - MICROSOFT REVEALS MONTHS-OLD BUG BEHIND GLOBAL OUTAGE Microsoft says a software bug"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.5 — "RISK OF NUCLEAR ACCIDENT IN UKRAINE INCREASING THIS WINTER, ATOMIC SAFETY REGULATORS REPRE"
- CHKP (Check Point Software Technolog) score 22.3 — "SML Mahindra Rights Issue Details:  ₹1,450 crore offer; check open date, price, record dat"
- 301077.SZ (CHINASTARS) score 21.4 — "China’s Buyback Push Struggles to Put a Floor Under Stocks"
- LTH (Life Time Group Holdings, Inc.) score 19.6 — "NO INDICATION AT THIS TIME THAT THERE IS A BUG AFFECTING MULTIPLE BANKS AT THE SAME TIME -"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 15.9 — "Tata Steel Share Price Live Updates: Tata Steel experiences a slight dip in weekly returns"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 15.9 — "Tata Steel Share Price Live Updates: Tata Steel experiences a slight dip in weekly returns"
- BLLN (BillionToOne, Inc.) score 14.2 — "MACQUARIE WARNS OF DATA CENTER EXUBERANCE AMID TRILLION-DOLLAR AI BUILDOUT Macquarie Asset"
- BOND (PIMCO Active Bond Exchange-Tra) score 14.0 — "Rupee likely to open flat as dollar strength, US bond yields weigh on sentiment"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 13.7 — "Bajaj Finserv Share Price Highlights: Bajaj Finserv Stock Price History"
- JIOFIN.BO (Jio Financial Services Limited) score 12.5 — "MSFT - MICROSOFT REVEALS MONTHS-OLD BUG BEHIND GLOBAL OUTAGE Microsoft says a software bug"
- BZ=F (Brent Crude Oil Last Day Finan) score 11.2 — "NVIDIA SHARES EXTEND LOSSES; LAST DOWN 4.2%"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.6 — "Why Iraq Just Fast-Tracked Chevron’s Takeover Of A 14-Billion-Barrel Supergiant"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 9.3 — "Nifty may open 75 points higher; experts flag consolidation amid global weakness"
- SCHD (Schwab US Dividend Equity ETF) score 8.3 — "Mahanadi Coalfields IPO: Dividend king in the making? What top official says about Coal In"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 8.0 — "Bajaj Finance Share Price Highlights: Bajaj Finance Stock Price History"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.8 — "Stock Market Live Updates | Opening Bell: Sensex gains over 200 pts, Nifty above 25,300; I"
- MS (Morgan Stanley) score 7.5 — "JPM $BAC $WFC $USB $COF - MULTIPLE U.S. BANKS FACE SERVICE DISRUPTION REPORTS Several majo"
- GS (Goldman Sachs Group, Inc. (The) score 5.5 — "GOLDMAN SACHS CUTS OIL PRICE FORECASTS FOR 2026 AND 2027 Goldman Sachs has lowered its Bre"
- CRWV (CoreWeave, Inc.) score 3.2 — "COREWEAVE SHARES FOLLOW NVIDIA LOWER, DOWN 6%"
- META (Meta) score 3.1 — "Nvidia Without Huang: What a Pause in AI Deals Means for Metals"
- RS (Reliance, Inc.) score 2.7 — "Reliance Industries shares rebound 15% in November, add  ₹2.38 lakh crore in market value;"
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 2.6 — "Kaynes Technology shares crash 12%, hit fresh 52-week low after weak Q2 results"
- DEMZ (Democratic Large Cap Core ETF) score 2.1 — "DEMOCRATIC SENATOR REED SAYS CONGRESS NEEDS ASSESSMENT OF WHETHER NVIDIA IS "TOO BIG TO FA"
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 1.3 — "Cochin Shipyard dividend 2026: Last day to buy today | Check record date, payout amount, h"

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