# Transmission Layer — board brief · 2026-10-23 09:19Z

data as of **2026-10-23** · 97 series · 24 red / 32 amber · 8 events surfaced (36 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.888, 15d in regime; vol-pct 0.775, breadth-off 1.0, Markov P(high-vol) 0.054)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.37, contra nifty_50 corr20=0.41, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.82, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.03, corr60 0.15, last shift 2026-08-28. Channel: global copper leads Indian metal equities
- [INVERTED] **inr_oil_channel** — corr20 -0.29, corr60 0.04, last shift 2026-09-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.9, corr60 -0.78, last shift 2026-09-02. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.15, corr60 -0.0, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.26, corr60 -0.25, last shift 2026-08-10. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.54, corr60 0.24, last shift 2026-07-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.0008081156037280657)
- **SETUP** sp500 → asx_200: leads 1d (ccf 0.566, β 0.4358, p 0.0); driver zc -1.59 → expected -0.527%. Type hit-rate 0.826 (n=1900).
- **SETUP** dyn_vt → asx_200: leads 1d (ccf 0.564, β 0.4479, p 0.0); driver zc -1.7 → expected -0.582%. Type hit-rate 0.826 (n=1900).
- **SETUP** dyn_vt → aud_usd: leads 1d (ccf 0.556, β 0.3415, p 0.0); driver zc -1.7 → expected -0.444%. Type hit-rate 0.826 (n=1900).
- **SETUP** nasdaq_100 → nikkei_225: leads 1d (ccf 0.544, β 0.6267, p 0.0); driver zc -2.25 → expected -1.806%. Type hit-rate 0.826 (n=1900).
- **SETUP** dyn_vt → nikkei_225: leads 1d (ccf 0.544, β 0.8883, p 0.0); driver zc -1.7 → expected -1.154%. Type hit-rate 0.826 (n=1900).
- **SETUP** sp500 → nikkei_225: leads 1d (ccf 0.538, β 0.8448, p 0.0); driver zc -1.59 → expected -1.021%. Type hit-rate 0.826 (n=1900).
- **SETUP** dyn_vt → usd_brl: leads 1d (ccf -0.512, β -0.407, p 0.0); driver zc -1.7 → expected 0.529%. Type hit-rate 0.826 (n=1900).
- **SETUP** sp500 → aud_usd: leads 1d (ccf 0.464, β 0.2761, p 0.0); driver zc -1.59 → expected -0.334%. Type hit-rate 0.826 (n=1900).
- **SETUP** sp500 → usd_brl: leads 1d (ccf -0.446, β -0.3434, p 0.0); driver zc -1.59 → expected 0.415%. Type hit-rate 0.826 (n=1900).
- **SETUP** nasdaq_100 → aud_usd: leads 1d (ccf 0.438, β 0.1906, p 0.0); driver zc -2.25 → expected -0.55%. Type hit-rate 0.826 (n=1900).
- **SETUP** nasdaq_100 → usd_brl: leads 1d (ccf -0.422, β -0.2371, p 0.0); driver zc -2.25 → expected 0.683%. Type hit-rate 0.826 (n=1900).
- **SETUP** dyn_vt → kospi: leads 1d (ccf 0.412, β 1.0108, p 0.0); driver zc -1.7 → expected -1.313%. Type hit-rate 0.826 (n=1900).
- **SETUP** nasdaq_100 → kospi: leads 1d (ccf 0.397, β 0.6889, p 0.0); driver zc -2.25 → expected -1.986%. Type hit-rate 0.826 (n=1900).
- **SETUP** sp500 → kospi: leads 1d (ccf 0.354, β 0.8369, p 0.0); driver zc -1.59 → expected -1.011%. Type hit-rate 0.826 (n=1900).
- **SETUP** dyn_nvda → aud_usd: leads 1d (ccf 0.343, β 0.0765, p 0.0); driver zc -1.98 → expected -0.334%. Type hit-rate 0.826 (n=1900).
- **SETUP** dyn_vt → hang_seng: leads 1d (ccf 0.265, β 0.3422, p 0.0); driver zc -1.7 → expected -0.445%. Type hit-rate 0.826 (n=1900).
- **SETUP** dyn_vt → shanghai_comp: leads 1d (ccf 0.251, β 0.2165, p 1e-05); driver zc -1.7 → expected -0.281%. Type hit-rate 0.826 (n=1900).
- Track record · residual_reversion: hit-rate **0.5** (n=1121) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.826** (n=1900) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.31] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4041.80, z20 -2.70, zc -0.33, resid-z -0.07 [quiet], 1d -0.46%, |z20|=2.70; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 54.12, z20 -2.28, zc -0.44, resid-z -0.29 [quiet], 1d -1.19%, |z20|=2.28; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 74.69, z20 1.99, zc n/a, resid-z n/a [quiet], 1d 0.74%, GSR<75 (extreme low); |z20|=1.99
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dxy (inverse) — not yet - watch; rho -0.518 vs comex_gold
- Source: Silver prices slide below Rs 2 lakh/kg, down nearly 55% from Jan peak. What’s behind the rapid selloff? — ET Markets, 2026-10-23. https://economictimes.indiatimes.com/markets/commodities/news/silver-prices-slide-below-rs-2-lakh/kg-down-nearly-55-from-jan-peak-whats-behind-the-rapid-selloff/articleshow/135139949.cms
- Source: Today’s Gold Rate in India October 23: Gold prices down in Coimbatore, Nagpur, Visakhapatnam, Surat, Jaipur — BusinessLine Mkts, 2026-10-23. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-coimbatore-nagpur-visakhapatnam-surat-jaipur-lucknow-chandigarh-gold-rates-other-cities-october-23-2026/article71615200.ece
- Source: Today’s Gold Rate in India October 23: Gold prices down in Delhi, Mumbai, Kolkata, Chennai, Bengaluru — BusinessLine Mkts, 2026-10-23. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-delhi-mumbai-kolkata-chennai-bengaluru-hyderabad-pune-gold-rates-metro-cities-october-23-2026/article71615199.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 7.71] cross-asset · 8 series ↓
- nifty_midcap_100 [INDICES]: last 55536.05, z20 -3.21, zc -2.58, resid-z -3.45 [unexplained], 1d -2.67%, |z20|=3.21
- dyn_swiggy_ns [EQUITIES]: last 179.20, z20 -2.96, zc -6.49, resid-z -6.01 [unexplained], 1d -15.23%, |z20|=2.96; 1y-pct=0
- nifty_fmcg [INDICES]: last 42419.95, z20 -2.95, zc -1.44, resid-z -1.19 [quiet], 1d -1.59%, |z20|=2.95; 1y-pct=0
- india_vix [INDICES]: last 17.08, z20 2.48, zc 1.42, resid-z n/a [quiet], 1d 8.41%, |z20|=2.48
- dyn_jiofin_bo [EQUITIES]: last 205.30, z20 -2.11, zc -1.83, resid-z -0.86 [priced], 1d -2.70%, |z20|=2.11; 1y-pct=0
- nifty_metal [INDICES]: last 11463.15, z20 -1.99, zc -2.05, resid-z -1.73 [unexplained], 1d -2.84%, |z20|=1.99
- nifty_50 [INDICES]: last 22494.85, z20 -0.91, zc -0.88, resid-z -0.92 [quiet], 1d -0.85%, 1y-pct=2
- dyn_policybzr_ns [EQUITIES]: last 1014.60, z20 -0.66, zc -0.67, resid-z 0.15 [quiet], 1d -2.24%, 1y-pct=2
- **Mechanism**: cross-asset · 8 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 1.06).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho -0.632 via india_vix, z -2.74, reacted); midcap_largecap_ratio (rho 0.603 via nifty_midcap_100, z -3.54, reacted); dyn_adanient_bo (rho 0.588 via nifty_metal, z -1.94, reacted); dyn_indianb_ns (rho 0.57 via nifty_midcap_100, z 0.42, quiet); dyn_indusindbk_bo (rho -0.568 via india_vix, z -1.81, reacted)
- Watch next: dyn_indianb_ns (co-move) — not yet - watch; rho 0.57 vs nifty_midcap_100, historically leads by 1d
- Watch next: ftse_100 (co-move) — not yet - watch; rho 0.529 vs nifty_50, historically leads by 2d
- Watch next: dax (co-move) — not yet - watch; rho 0.502 vs nifty_50, historically leads by 2d
- **India receivers**: dyn_bajfinance_ns (rho -0.632, z -2.74); midcap_largecap_ratio (rho 0.603, z -3.54); dyn_adanient_bo (rho 0.588, z -1.94); dyn_indianb_ns (rho 0.57, z 0.42)
- Source: Sensex today | Stock Market Live: Sensex recovers from day's low, down 253 pts; Nifty holds 22,500 — BusinessLine Mkts, 2026-10-23. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-23rd-october-2026/article71611889.ece
- Source: Why are mid, small-caps bleeding? Indices crash up to 4% - Swiggy, Meesho, Vedanta Aluminium, MCX lose big — Mint Markets, 2026-10-23. https://www.livemint.com/market/stock-market-news/why-are-mid-small-caps-bleeding-indices-crash-up-to-4-swiggy-meesho-vedanta-aluminium-mcx-lose-big-11792737065942.html
- Source: Nifty sinks below 22,400, breadth collapses as metal, finance stocks lead rout — BusinessLine Mkts, 2026-10-23. https://www.thehindubusinessline.com/markets/nifty-sinks-below-22400-breadth-collapses-as-metal-finance-stocks-lead-rout/article71615099.ece
- Historical analogues: 2025-07-21 (d=1.06), 2025-07-14 (d=1.23), 2025-12-19 (d=1.4)

### [RED 6.21] cross-asset · 4 series ↓
- nasdaq_100 [INDICES]: last 28962.86, z20 -2.55, zc -2.25, resid-z 0.40 [priced], 1d -2.88%, |z20|=2.55
- dyn_vt [EQUITIES]: last 156.53, z20 -2.17, zc -1.70, resid-z -0.15 [priced], 1d -1.30%, |z20|=2.17
- dyn_nvda [EQUITIES]: last 212.28, z20 -2.03, zc -1.98, resid-z 0.74 [priced], 1d -4.36%, |z20|=2.03
- vix [INDICES]: last 19.10, z20 1.99, zc 0.04, resid-z n/a [quiet], 1d 0.37%, |z20|=1.99
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-04 (z-distance 0.21).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: usd_inr (rho 0.412 via dyn_nvda, z -1.08, reacted)
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.598 vs nasdaq_100, historically leads by 2d
- Watch next: dax (co-move) — not yet - watch; rho 0.619 vs dyn_vt
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.597 vs nasdaq_100
- **India receivers**: usd_inr (rho 0.412, z -1.08)
- Source: Nasdaq CEO flags IPO slowdown amid market volatility — ET Markets, 2026-10-23. https://economictimes.indiatimes.com/markets/us-stocks/news/nasdaq-ceo-flags-ipo-slowdown-amid-market-volatility/articleshow/135139313.cms
- Source: Christopher Wood swapped Nvidia for a Greek infrastructure stock. The bet is paying off — ET Markets, 2026-10-23. https://economictimes.indiatimes.com/markets/stocks/news/christopher-wood-swapped-nvidia-for-a-greek-infrastructure-stock-the-bet-is-paying-off/articleshow/135136490.cms
- Source: Stock market outlook today, 23 Oct: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-10-23. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-23-oct-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-11792716174246.html
- Historical analogues: 2026-05-04 (d=0.21), 2025-04-28 (d=0.28), 2025-08-28 (d=0.3)

### [AMBER 6.17] brent ↑
- brent [COMMODITIES]: last 109.23, z20 1.17, zc -1.48, resid-z -0.21 [quiet], 1d -3.48%, 1-session move -3.48% ≥ 1.5%
- **Mechanism**: brent ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.529 vs brent, historically leads by 5d
- Source: Oil India strikes gas in Krishna-Godavari Basin, records 200,000 SCMD peak flow — BusinessLine Mkts, 2026-10-23. https://www.thehindubusinessline.com/markets/commodities/oil-india-strikes-gas-in-krishna-godavari-basin-records-200000-scmd-peak-flow/article71614983.ece
- Source: Gold price falls Rs 1,500/10g; silver plunges Rs 7,000/kg as soaring oil fuels rate hike bets. Time to sell? — ET Markets, 2026-10-23. https://economictimes.indiatimes.com/markets/commodities/news/gold-price-falls-rs-1500/10g-silver-plunges-rs-7000/kg-as-soaring-oil-fuels-rate-hike-bets-time-to-sell/articleshow/135135987.cms
- Source: Brent Hits $114 as Houthi Attacks Threaten Saudi Energy Infrastructure — OilPrice, 2026-10-23. https://oilprice.com/Latest-Energy-News/World-News/Brent-Hits-114-as-Houthi-Attacks-Threaten-Saudi-Energy-Infrastructure.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-14 (d=0.02), 2025-04-16 (d=0.04)

### [RED 6.12] dyn_chkp ↑
- dyn_chkp [EQUITIES]: last 152.00, z20 4.12, zc 2.65, resid-z 0.74 [moved], 1d 5.98%, |z20|=4.12
- **Mechanism**: dyn_chkp ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.409 via dyn_chkp, z -1.81, reacted)
- **India receivers**: dyn_indusindbk_bo (rho 0.409, z -1.81)
- Source: Already jumped 55% in 2026, PL Capital sees more returns in Sai Lifesciences shares | Check target, upside — Mint Markets, 2026-10-23. https://www.livemint.com/market/stock-market-news/already-jumped-55-in-2026-pl-capital-sees-more-returns-in-sai-lifesciences-shares-check-target-upside-11792742770583.html
- Source: LTM dividend 2026 record date today | Check dividend payout details, history, yield and share performance — Mint Markets, 2026-10-23. https://www.livemint.com/market/stock-market-news/ltm-dividend-2026-record-date-today-check-dividend-payout-details-history-yield-and-share-performance-11792734155795.html
- Source: Jio IPO Day 3: GMP at 22%, issue subscribed over 5X; check brokerage views and key details — ET Markets, 2026-10-23. https://economictimes.indiatimes.com/markets/ipos/fpos/jio-ipo-day-3-gmp-at-22-issue-subscribed-over-5x-check-brokerage-views-and-key-details/articleshow/135134397.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2025-05-20 (d=0.04)

### [RED 6.09] dyn_lth ↑
- dyn_lth [EQUITIES]: last 41.98, z20 4.09, zc 1.36, resid-z -0.53 [quiet], 1d 2.99%, |z20|=4.09
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: This market signal just occurred for only the second time since 1999. Here’s what happened and what it means. — MarketWatch Top, 2026-10-23. https://www.marketwatch.com/story/this-market-signal-just-occurred-for-only-the-second-time-since-1999-heres-what-happened-and-what-it-means-a126cf31?mod=mw_rss_topstories
- Source: D-Street bleeds! Market value of all BSE-listed firms falls below Rs 450 lakh crore for first time since April. More pain ahead? — ET Markets, 2026-10-23. https://economictimes.indiatimes.com/markets/stocks/news/d-street-bleeds-market-value-of-all-bse-listed-firms-falls-below-rs-450-lakh-crore-for-first-time-since-april-more-pain-ahead/articleshow/135140291.cms
- Source: Gold price falls Rs 1,500/10g; silver plunges Rs 7,000/kg as soaring oil fuels rate hike bets. Time to sell? — ET Markets, 2026-10-23. https://economictimes.indiatimes.com/markets/commodities/news/gold-price-falls-rs-1500/10g-silver-plunges-rs-7000/kg-as-soaring-oil-fuels-rate-hike-bets-time-to-sell/articleshow/135135987.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-17 (d=0.02), 2025-12-31 (d=0.02)

### [RED 5.97] dyn_meta ↓
- dyn_meta [EQUITIES]: last 648.91, z20 -3.97, zc -2.87, resid-z -0.12 [moved], 1d -6.97%, |z20|=3.97
- **Mechanism**: dyn_meta ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Meta share price: Stock slumps 7.5% despite upbeat Q3 results; why is Facebook parent falling? — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/meta-share-price-stock-slumps-7-5-despite-upbeat-q3-results-why-is-facebook-parent-falling-11792689825393.html
- Source: Zuckerberg’s California tax move is a win for Meta — and for him — MarketWatch Top, 2026-10-22. https://www.marketwatch.com/story/zuckerbergs-california-tax-move-is-a-win-for-meta-and-for-him-aa049c94?mod=mw_rss_topstories
- Source: META - META PLATFORM'S 5-YEAR CREDIT DEFAULT SWAPS HITS ALL-TIME HIGH, LAST AT 114.5 BPS - MARKIT DATA — DeItaone, 2026-10-22. https://t.me/walter_bloomberg/37429
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2025-10-09 (d=0.12)

### [RED 5.7] usd_jpy ↓
- usd_jpy [FX]: last 156.62, z20 -3.70, zc -2.09, resid-z -2.01 [unexplained], 1d -0.96%, |z20|=3.70
- **Mechanism**: usd_jpy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Yen jumps as oil, AI and France worries rattle markets — Mint Markets, 2026-10-22. https://www.livemint.com/market/yen-jumps-as-oil-ai-and-france-worries-rattle-markets-11792694662480.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2025-07-30 (d=0.01)

## Watchlist (below surfacing floor)
indices · 3 series ↓ (5.38), natgas ↑ (5.3), dyn_bond ↑ (5.17), dyn_tatatech_ns ↓ (4.92), dyn_wit ↑ (4.81), dyn_coalindia_ns ↓ (4.79), dyn_bajfinance_ns ↓ (4.74), cross-asset · 2 series ↑ (4.62), dow_jones ↑ (4.52), dyn_sepn ↑ (4.34), dyn_tech ↑ (3.79), dyn_4417_t ↑ (3.66)

## India macro
- nifty_50: 22494.8496 (1d -0.85%, z20 -0.91, flag amber)
- nifty_midcap_100: 55536.0508 (1d -2.67%, z20 -3.21, flag red)
- usd_inr: 94.9525 (1d 0.68%, z20 -1.08, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4688 (1d -1.84%, z20 -3.54, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 101.2 — "Stock recommendations for 23 October from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 99.7 — "Stock recommendations for 23 October from MarketSmith India"
- INOXINDIA.NS (INOX INDIA LIMITED) score 99.0 — "Stock recommendations for 23 October from MarketSmith India"
- INDIANB.NS (INDIAN BANK) score 82.0 — "Indian shares subdued as rising crude prices eclipse IT gains"
- BAC (Bank of America Corporation) score 70.1 — "Kotak Mahindra Bank Q2 results preview: PAT may rise up to 32% YoY; margins, loan growth i"
- HDB (HDFC Bank Limited) score 63.5 — "HDFC Life Share Price Live Updates: HDFC Life's Price Update"
- OHI (Omega Healthcare Investors, In) score 62.2 — "Reliance Jio IPO oversubscribed | Should investors apply or avoid or buy shares after list"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 61.8 — "Kotak Mahindra Bank Q2 results preview: PAT may rise up to 32% YoY; margins, loan growth i"
- IDBI.NS (IDBI BANK LIMITED) score 60.8 — "Kotak Mahindra Bank Q2 results preview: PAT may rise up to 32% YoY; margins, loan growth i"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 60.8 — "Kotak Mahindra Bank Q2 results preview: PAT may rise up to 32% YoY; margins, loan growth i"
- COIN (Coinbase Global, Inc.) score 59.5 — "'AI-trade' bust will aid India only partially; don’t tweak LTCG, says Madhavi Arora of Emk"
- TECHM.NS (TECH MAHINDRA LIMITED) score 55.2 — "AI Tech Fears Push Global Credit Spreads to 17-Month High"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 50.9 — "AI Tech Fears Push Global Credit Spreads to 17-Month High"
- TECH (Bio-Techne Corp) score 50.9 — "AI Tech Fears Push Global Credit Spreads to 17-Month High"
- TGT (Target Corporation) score 46.0 — "Jindal Stainless shares: Down 17% in YTD! Jefferies India sees 32% upside after Q2 results"
- CHKP (Check Point Software Technolog) score 44.2 — "Paras Healthcare IPO Day 3: Check GMP, subscription status and key details"
- BOND (PIMCO Active Bond Exchange-Tra) score 34.1 — "Indian bonds flattish as oil spike offset by falling Treasury yields"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 33.2 — "Brent Hits $114 as Houthi Attacks Threaten Saudi Energy Infrastructure"
- LTH (Life Time Group Holdings, Inc.) score 32.8 — "Bitcoin Falls Below $83,000 as AI Jitters Weigh on Sentiment"
- RS (Reliance, Inc.) score 30.3 — "IPO GMP comparison: Reliance Jio Platforms IPO vs Paras Healthcare - Last day to apply tod"
- 301077.SZ (CHINASTARS) score 28.1 — "China AI Model Stocks’ $150 Billion Drop Shows No Sign of Easing"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 26.0 — "Reliance Jio IPO oversubscribed | Should investors apply or avoid or buy shares after list"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 19.5 — "Nifty sinks below 22,400, breadth collapses as metal, finance stocks lead rout"
- JIOFIN.BO (Jio Financial Services Limited) score 17.9 — "Jio Financial Services Share Price Live Updates: Jio Financial Services Trading Under Pres"
- BZ=F (Brent Crude Oil Last Day Finan) score 17.8 — "IPO GMP comparison: Reliance Jio Platforms IPO vs Paras Healthcare - Last day to apply tod"
- META (Meta) score 17.2 — "Nifty sinks below 22,400, breadth collapses as metal, finance stocks lead rout"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.8 — "Nifty sinks below 22,400, breadth collapses as metal, finance stocks lead rout"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 16.5 — "Top stocks to watch today: Infosys, Tata Motors, Swiggy, Cyient shares in focus on Friday,"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 16.5 — "Top stocks to watch today: Infosys, Tata Motors, Swiggy, Cyient shares in focus on Friday,"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 15.7 — "Adani Ent Share Price Live Updates: Adani Enterprises Reports Significant Monthly Loss"
- JUSTDIAL.BO (JUST DIAL LTD.) score 15.4 — "International Gemological Institute shares rally 16% in 2 days: Stock just 3.5% below 52-w"
- SEPN (Septerna, Inc.) score 15.0 — "ECB Consumer Expectations Survey results – September 2026"
- JEF (Jefferies Financial Group Inc.) score 11.3 — "Jindal Stainless shares: Down 17% in YTD! Jefferies India sees 32% upside after Q2 results"
- GS (Goldman Sachs Group, Inc. (The) score 9.9 — "Ola Electric shares dip 5% after Goldman Sachs downgrades stock to Sell. Here’s why"
- VT (Vanguard Total World Stock Ind) score 6.5 — "Reliance Jio IPO Global Record: Another feather in cap! History created - 1st IPO worldwid"
- WIT (Wipro Limited) score 6.3 — "Top stocks to buy: IT stocks soar! TCS, Infosys, HCL Tech, Wipro - Nifty IT up over 3% tod"
- NVDA (NVIDIA Corporation) score 6.2 — "Christopher Wood swapped Nvidia for a Greek infrastructure stock. The bet is paying off"
- SWIGGY.NS (SWIGGY LIMITED) score 5.7 — "Swiggy shares crash 14%, hit 52-week low after Q2 results. Here’s why Jefferies, Nomura, B"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.4 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
- VOLTAS.NS (VOLTAS LTD) score 0.0 — "Voltas’s market share is growing. Will margins follow?"

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