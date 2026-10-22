# Transmission Layer — board brief · 2026-10-22 15:13Z

data as of **2026-10-22** · 97 series · 19 red / 38 amber · 8 events surfaced (39 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.803, 14d in regime; vol-pct 0.782, breadth-off 0.824, Markov P(high-vol) 0.081)
- [INVERTED] **safe_haven_gold** — corr20 -0.37, corr60 -0.4, contra nifty_50 corr20=0.41, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.84, corr60 0.83, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.24, corr60 0.21, last shift 2026-08-27. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.02, corr60 0.11, last shift 2026-09-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.78, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.07, corr60 -0.01, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.27, corr60 -0.24, last shift 2026-08-07. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.52, corr60 0.25, last shift 2026-07-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.001632704625657233)
- **SETUP** dyn_vt → aud_usd: leads 1d (ccf 0.557, β 0.343, p 0.0); driver zc -1.94 → expected -0.506%. Type hit-rate 0.822 (n=1842).
- **SETUP** dyn_vt → usd_brl: leads 1d (ccf -0.512, β -0.4068, p 0.0); driver zc -1.94 → expected 0.6%. Type hit-rate 0.822 (n=1842).
- **SETUP** sp500 → aud_usd: leads 1d (ccf 0.465, β 0.2773, p 0.0); driver zc -1.84 → expected -0.385%. Type hit-rate 0.822 (n=1842).
- **SETUP** nasdaq_100 → aud_usd: leads 1d (ccf 0.441, β 0.1925, p 0.0); driver zc -2.03 → expected -0.499%. Type hit-rate 0.822 (n=1842).
- **SETUP** vix → aud_usd: leads 1d (ccf -0.432, β -0.0295, p 0.0); driver zc 1.93 → expected -0.47%. Type hit-rate 0.822 (n=1842).
- **SETUP** vix → usd_brl: leads 1d (ccf 0.426, β 0.0377, p 0.0); driver zc 1.93 → expected 0.601%. Type hit-rate 0.822 (n=1842).
- **SETUP** nasdaq_100 → usd_brl: leads 1d (ccf -0.421, β -0.2375, p 0.0); driver zc -2.03 → expected 0.616%. Type hit-rate 0.822 (n=1842).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.368, β -2.4319, p 0.00818); driver zc -1.94 → expected 3.588%. Type hit-rate 0.822 (n=1842).
- **SETUP** dyn_nvda → aud_usd: leads 1d (ccf 0.344, β 0.077, p 0.0); driver zc -1.81 → expected -0.305%. Type hit-rate 0.822 (n=1842).
- **SETUP** vix → india_vix: leads 1d (ccf 0.343, β 0.2279, p 0.01301); driver zc 1.93 → expected 3.634%. Type hit-rate 0.822 (n=1842).
- **SETUP** sp500 → india_vix: leads 1d (ccf -0.335, β -2.1617, p 0.01751); driver zc -1.84 → expected 3.005%. Type hit-rate 0.822 (n=1842).
- **SETUP** dyn_vt → gbp_usd: leads 1d (ccf 0.329, β 0.1448, p 1e-05); driver zc -1.94 → expected -0.214%. Type hit-rate 0.822 (n=1842).
- **SETUP** btc_usd → aud_usd: leads 1d (ccf 0.287, β 0.063, p 0.0); driver zc -1.66 → expected -0.198%. Type hit-rate 0.822 (n=1842).
- **SETUP** dyn_bond → eur_usd: leads 1d (ccf 0.255, β 0.3599, p 3e-05); driver zc 2.09 → expected 0.256%. Type hit-rate 0.822 (n=1842).
- Track record · residual_reversion: hit-rate **0.494** (n=1119) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.822** (n=1842) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.21] cross-asset · 4 series ↓
- vix [INDICES]: last 19.34, z20 2.54, zc 1.93, resid-z n/a [moved], 1d 15.95%, 1-session move +15.95% ≥ 15.0%; |z20|=2.54
- dyn_vt [EQUITIES]: last 156.25, z20 -2.44, zc -1.94, resid-z 0.37 [priced], 1d -1.48%, |z20|=2.44
- nasdaq_100 [INDICES]: last 29048.86, z20 -2.39, zc -2.03, resid-z -0.79 [priced], 1d -2.59%, |z20|=2.39
- sp500 [INDICES]: last 7649.33, z20 -1.59, zc -1.84, resid-z -0.79 [priced], 1d -1.39%, |z20|=1.59
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-23 (z-distance 0.16).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.695 vs vix, historically leads by 1d
- Watch next: dyn_gs (inverse) — not yet - watch; rho -0.615 vs vix
- Watch next: dax (co-move) — not yet - watch; rho 0.613 vs dyn_vt
- Source: US stocks today: US stocks slide as AI spending jitters hit Nasdaq, oil prices rebound — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-us-stocks-open-lower-as-ai-jitters-return-oil-rises/articleshow/135120582.cms
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: Nasdaq crashes 2% as AI, oil risks drive flight to bonds — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-earnings-forecast-ai-stocks-nvidia-tesla-meta-stock-price-news-22nd-october-2026/liveblog/135118971.cms
- Source: US stocks today: Nasdaq leads Wall Street higher as SpaceX, Super Micro lift AI sentiment — ET Markets, 2026-10-21. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-nasdaq-leads-wall-street-higher-as-spacex-super-micro-lift-ai-sentiment/articleshow/135100483.cms
- Historical analogues: 2025-10-23 (d=0.16), 2026-05-20 (d=0.17), 2025-05-06 (d=0.18)

### [RED 8.22] commodities · 2 series ↑
- brent [COMMODITIES]: last 111.86, z20 2.39, zc 1.52, resid-z -0.76 [priced], 1d 2.79%, 1-session move +2.79% ≥ 1.5%; |z20|=2.39; 1y-pct=96
- wti [COMMODITIES]: last 98.82, z20 1.13, zc 0.61, resid-z -0.97 [quiet], 1d 1.72%, 1-session move +1.72% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.552 vs brent, historically leads by 5d
- Watch next: brent_wti_spread (inverse) — not yet - watch; rho -0.388 vs wti, historically leads by 4d
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.524 vs brent
- Source: Rupee snaps eight-day run, crude tops $112 as Nifty falls for third straight day — BusinessLine Mkts, 2026-10-22. https://www.thehindubusinessline.com/markets/rupee-snaps-eight-day-run-crude-tops-112-as-nifty-falls-for-third-straight-day/article71611785.ece
- Source: US stocks today: US stocks slide as AI spending jitters hit Nasdaq, oil prices rebound — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-us-stocks-open-lower-as-ai-jitters-return-oil-rises/articleshow/135120582.cms
- Source: Indian bonds tumble on oil surge, RBI rate hike fears — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/bonds/indian-bonds-tumble-on-oil-surge-rbi-rate-hike-fears/articleshow/135118875.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 8.07] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4076.10, z20 -2.21, zc -1.77, resid-z -1.25 [moved], 1d -1.78%, |z20|=2.21; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 55.30, z20 -2.00, zc -1.64, resid-z -0.66 [priced], 1d -3.70%, |z20|=2.00; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 73.71, z20 1.75, zc n/a, resid-z n/a [quiet], 1d 1.99%, GSR<75 (extreme low); |z20|=1.75
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dxy (inverse) — not yet - watch; rho -0.544 vs comex_gold
- Source: Silver crashes  ₹8,590/kg to a 7-month low; gold hits 2-month low. What’s driving the selloff in precious metals — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/silver-crashes-rs-8-590-per-kilo-to-7-month-low-gold-hits-2-month-low-what-s-driving-the-selloff-in-precious-metals-11792676479559.html
- Source: BSE, MMTC-PAMP partner to boost India’s electronic gold receipts market — BusinessLine Mkts, 2026-10-22. https://www.thehindubusinessline.com/markets/bse-mmtc-pamp-partner-to-boost-indias-electronic-gold-receipts-market/article71611647.ece
- Source: Stocks, gold, or cryptocurrency: Here's how they have performed in 5 years - Which one should you buy? — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/stocks-gold-or-cryptocurrency-heres-how-they-have-performed-in-5-years-which-one-should-you-buy-11792655530044.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 5.68] dyn_meta ↓
- dyn_meta [EQUITIES]: last 654.77, z20 -3.68, zc -2.53, resid-z -0.40 [moved], 1d -6.13%, |z20|=3.68
- **Mechanism**: dyn_meta ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Meta falls as investors balance Muse growth with rising AI costs — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/us-stocks/news/meta-falls-as-investors-balance-muse-growth-with-rising-ai-costs/articleshow/135119388.cms
- Source: Meta Q3 Earnings: AI spending, revenue beat & new stock class — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/meta-q3-earnings-ai-spending-revenue-beat-amp-new-stock-class/slideshow/135112550.cms
- Source: Meta Q3 revenue rises 26% to $64.6 billion, net income jumps 264% — BusinessLine Mkts, 2026-10-22. https://www.thehindubusinessline.com/info-tech/meta-q3-revenue-rises-26-to-646-billion-net-income-jumps-264/article71610031.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2025-10-09 (d=0.12)

### [RED 5.37] dyn_chkp ↑
- dyn_chkp [EQUITIES]: last 148.70, z20 3.37, zc 1.62, resid-z 0.47 [moved], 1d 3.67%, |z20|=3.37
- **Mechanism**: dyn_chkp ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.418 via dyn_chkp, z -1.32, reacted)
- **India receivers**: dyn_indusindbk_bo (rho 0.418, z -1.32)
- Source: Reliance Jio IPO subscription status day 1, day 2: Check QIB, NII, Retail, Employee, RIL Shareholders wise data details — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/reliance-jio-ipo-subscription-status-day-1-day-2-check-qib-nii-retail-employee-ril-shareholders-wise-data-details-11792681049708.html
- Source: Coal India Q2 results 2026 date, dividend announcement news: Check Maharatna PSU's earnings schedule, preview, yield — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/coal-india-q2-results-2026-date-dividend-announcement-news-check-maharatna-psus-earnings-schedule-preview-yield-11792676595483.html
- Source: 163% return in 3 years! This AMC declares  ₹9.50 dividend despite 6% profit dip- Do you own? Check record date — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/163-return-in-3-years-this-amc-declares-rs-9-50-dividend-despite-6-profit-dip-do-you-own-check-record-date-11792672553645.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2025-05-20 (d=0.04)

### [AMBER 5.33] indices · 3 series ↓
- taiwan_weighted [INDICES]: last 46099.28, z20 -2.01, zc -1.18, resid-z 0.09 [quiet], 1d -1.68%, |z20|=2.01
- nikkei_225 [INDICES]: last 63139.59, z20 -1.87, zc -1.34, resid-z -0.60 [quiet], 1d -2.29%, |z20|=1.87
- kospi [INDICES]: last 5531.37, z20 -1.70, zc -1.01, resid-z -0.18 [quiet], 1d -3.56%, |z20|=1.70
- **Mechanism**: indices · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cartrade_ns (rho 0.455 via kospi, z -1.25, reacted); dyn_idbi_ns (rho 0.403 via nikkei_225, z -2.03, reacted); midcap_largecap_ratio (rho 0.362 via kospi, z -2.85, reacted)
- **India receivers**: dyn_cartrade_ns (rho 0.455, z -1.25); dyn_idbi_ns (rho 0.403, z -2.03); midcap_largecap_ratio (rho 0.362, z -2.85)
- Source: Global Market: Japan’s Nikkei falls as chip stocks retreat on AI spending concerns — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-falls-as-chip-stocks-retreat-on-ai-spending-concerns/articleshow/135106795.cms
- Source: Japan’s Nikkei jumps over 1% as AI optimism lifts chip stocks; exports rise 16.7% — ET Markets, 2026-10-21. https://economictimes.indiatimes.com/markets/us-stocks/news/japans-nikkei-jumps-over-1-as-ai-optimism-lifts-chip-stocks-exports-rise-16-7/articleshow/135081946.cms

### [AMBER 5.33] cross-asset · 2 series ↑
- dyn_techm_ns [EQUITIES]: last 1829.10, z20 2.49, zc -0.11, resid-z -0.71 [quiet], 1d -0.31%, |z20|=2.49; 1y-pct=99
- nifty_it [INDICES]: last 32081.25, z20 2.08, zc -0.66, resid-z -0.85 [quiet], 1d -1.05%, |z20|=2.08
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.52).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tataelxsi_ns (rho 0.76 via nifty_it, z 1.93, reacted); nifty_50 (rho 0.515 via nifty_it, z -0.32, quiet); dyn_justdial_bo (rho 0.511 via nifty_it, z 2.85, reacted); midcap_largecap_ratio (rho -0.434 via dyn_techm_ns, z -2.85, reacted); dyn_tatatech_ns (rho 0.404 via nifty_it, z -1.28, reacted)
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.515 vs nifty_it
- **India receivers**: dyn_tataelxsi_ns (rho 0.76, z 1.93); nifty_50 (rho 0.515, z -0.32); dyn_justdial_bo (rho 0.511, z 2.85); midcap_largecap_ratio (rho -0.434, z -2.85)
- Source: IT stocks rebound sharply in October: TCS gains 22%, Wipro and Tech Mahindra gain 20% — 3 key reasons behind the jump — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/it-stocks-rebound-sharply-in-october-tcs-gains-22-wipro-and-tech-mahindra-gain-20-3-key-reasons-behind-the-jump-11792671461699.html
- Source: Mahindra Lifespace Q2 profit down 66 pc to Rs 16 cr — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/stocks/earnings/mahindra-lifespace-q2-profit-down-66-pc-to-rs-16-cr/articleshow/135118930.cms
- Source: SML Isuzu shares: SML Mahindra shares tank for 3rd session in row after 33% gain in 6 months | Buy, sell or hold? — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/sml-isuzu-shares-sml-mahindra-shares-tank-for-3rd-session-in-row-after-33-gain-in-6-months-buy-sell-or-hold-11792645465680.html
- Historical analogues: 2025-12-30 (d=0.52), 2025-08-13 (d=0.76), 2026-01-06 (d=0.77)

### [AMBER 4.91] indices · 2 series ↓
- nifty_midcap_100 [INDICES]: last 57062.15, z20 -2.08, zc -0.84, resid-z -0.02 [quiet], 1d -0.88%, |z20|=2.08
- nifty_50 [INDICES]: last 22687.65, z20 -0.32, zc -0.54, resid-z -0.70 [quiet], 1d -0.54%, 1y-pct=4
- **Mechanism**: indices · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.6).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.639 via nifty_50, z -2.44, reacted); nifty_metal (rho 0.633 via nifty_midcap_100, z -1.41, reacted); dyn_jiofin_bo (rho 0.633 via nifty_midcap_100, z -1.2, reacted); dyn_policybzr_ns (rho 0.571 via nifty_midcap_100, z -0.31, quiet); dyn_bajfinance_ns (rho 0.55 via nifty_50, z -1.16, reacted)
- Watch next: dyn_policybzr_ns (co-move) — not yet - watch; rho 0.571 vs nifty_midcap_100, historically leads by 5d
- Watch next: ftse_100 (co-move) — not yet - watch; rho 0.522 vs nifty_50, historically leads by 2d
- **India receivers**: nifty_fmcg (rho 0.639, z -2.44); nifty_metal (rho 0.633, z -1.41); dyn_jiofin_bo (rho 0.633, z -1.2); dyn_policybzr_ns (rho 0.571, z -0.31)
- Source: Rupee snaps eight-day run, crude tops $112 as Nifty falls for third straight day — BusinessLine Mkts, 2026-10-22. https://www.thehindubusinessline.com/markets/rupee-snaps-eight-day-run-crude-tops-112-as-nifty-falls-for-third-straight-day/article71611785.ece
- Source: Market wrap: Bajaj Finance, Cipla, Nestle India, Eternal top gainers and losers on Nifty and Sensex on Thursday — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-bajaj-finance-cipla-nestle-india-eternal-top-gainers-and-losers-on-nifty-and-sensex-on-thursday/articleshow/135117923.cms
- Source: Sensex today | Stock Market Highlights: Sensex sheds 460 pts, Nifty falls 123 pts for 3rd straight session — BusinessLine Mkts, 2026-10-22. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-22nd-october-2026/article71608127.ece
- Historical analogues: 2025-07-21 (d=0.6), 2025-07-14 (d=0.96), 2025-12-19 (d=1.23)

## Watchlist (below surfacing floor)
dyn_lth ↑ (4.88), dyn_wit ↑ (4.7), dyn_sepn ↑ (4.68), dyn_bond ↑ (4.64), comex_copper ↓ (4.46), natgas ↓ (4.32), dyn_4417_t ↑ (4.31), dyn_coalindia_ns ↓ (4.21), dow_jones ↑ (4.09), dyn_rs ↑ (4.03), dyn_301077_sz ↓ (3.9), hang_seng ↓ (3.81)

## India macro
- nifty_50: 22687.6504 (1d -0.54%, z20 -0.32, flag amber)
- nifty_midcap_100: 57062.1484 (1d -0.88%, z20 -2.08, flag amber)
- usd_inr: 94.8080 (1d 0.10%, z20 -1.53, flag amber)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5151 (1d -0.34%, z20 -2.85, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 99.2 — "Jio leverage play pops up at SBI as India brokers lure IPO bets"
- INOXINDIA.NS (INOX INDIA LIMITED) score 96.5 — "Jio leverage play pops up at SBI as India brokers lure IPO bets"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 96.4 — "Jio leverage play pops up at SBI as India brokers lure IPO bets"
- INDIANB.NS (INDIAN BANK) score 82.6 — "Jammu & Kashmir Bank Q2 Results: Net profit rises over 10% YoY to Rs 546 crore, NII jumps "
- BAC (Bank of America Corporation) score 70.0 — "Jammu & Kashmir Bank Q2 Results: Net profit rises over 10% YoY to Rs 546 crore, NII jumps "
- HDB (HDFC Bank Limited) score 64.1 — "Jammu & Kashmir Bank Q2 Results: Net profit rises over 10% YoY to Rs 546 crore, NII jumps "
- IDBI.NS (IDBI BANK LIMITED) score 62.1 — "Jammu & Kashmir Bank Q2 Results: Net profit rises over 10% YoY to Rs 546 crore, NII jumps "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 62.1 — "Jammu & Kashmir Bank Q2 Results: Net profit rises over 10% YoY to Rs 546 crore, NII jumps "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 62.1 — "Jammu & Kashmir Bank Q2 Results: Net profit rises over 10% YoY to Rs 546 crore, NII jumps "
- COIN (Coinbase Global, Inc.) score 56.7 — "Global Market: China's Lingjun Investment attracts $300 million from overseas investors"
- OHI (Omega Healthcare Investors, In) score 53.7 — "Ola Electric rights issue opens today: Who are the investors applying for 2.39 crore entit"
- TECHM.NS (TECH MAHINDRA LIMITED) score 53.1 — "Mahindra Lifespace Q2 profit down 66 pc to Rs 16 cr"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 49.2 — "IT stocks rebound sharply in October: TCS gains 22%, Wipro and Tech Mahindra gain 20% — 3 "
- TECH (Bio-Techne Corp) score 49.2 — "IT stocks rebound sharply in October: TCS gains 22%, Wipro and Tech Mahindra gain 20% — 3 "
- TGT (Target Corporation) score 48.1 — "Lost 30% in 6 months! Motilal Oswal sees 39% upside in Vishal Mega Mart stock - Check targ"
- CHKP (Check Point Software Technolog) score 47.8 — "Ola Electric rights issue opens today: Who are the investors applying for 2.39 crore entit"
- BOND (PIMCO Active Bond Exchange-Tra) score 35.1 — "Yes Bank shares tumble over 20% in two weeks amid AT-1 bond shock: Is more downside ahead?"
- RS (Reliance, Inc.) score 31.3 — "Reliance Industries shares: Monarch sees 20% upside in 3–4 months - Reveals buy range, tar"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 30.5 — "Adani Energy Q2 Results: Profit zooms 148% YoY to Rs 1,323 crore; revenue jumps 53%"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 29.8 — "Shoppers Stop shares deliver almost no returns in 10 years; Experts decode the road ahead "
- LTH (Life Time Group Holdings, Inc.) score 25.2 — "Jio Platforms IPO Day 2 Highlights: Issue subscribed 5.19 times, QIB demand crosses 12x"
- 301077.SZ (CHINASTARS) score 24.3 — "Ahead of Communist Party plenum, Xi Jinping warns that China faces a ‘new Long March’"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 20.8 — "Market wrap: Bajaj Finance, Cipla, Nestle India, Eternal top gainers and losers on Nifty a"
- JIOFIN.BO (Jio Financial Services Limited) score 17.9 — "Tata Teleservices narrows Q2 loss to ₹59 crore, revenue up 8%; stock surges 9% on results "
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 17.7 — "Market wrap: Bajaj Finance, Cipla, Nestle India, Eternal top gainers and losers on Nifty a"
- META (Meta) score 16.1 — "Meta falls as investors balance Muse growth with rising AI costs"
- JUSTDIAL.BO (JUST DIAL LTD.) score 16.0 — "Lumpy Jio IPO inflows push rupee into ‘overbought’ zone just as oil renews rise"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 14.1 — "Adani Energy Q2 Results: Profit zooms 148% YoY to Rs 1,323 crore; revenue jumps 53%"
- BZ=F (Brent Crude Oil Last Day Finan) score 13.6 — "YIELD ON 20-YR U.S. TREASURY BOND PARES DECLINE AFTER $13 BLN AUCTION, LAST DOWN 1.25 BASI"
- SEPN (Septerna, Inc.) score 13.5 — "India's Middle East Oil Imports Jumped 32% in September"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 12.6 — "Tata Teleservices narrows Q2 loss to ₹59 crore, revenue up 8%; stock surges 9% on results "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 12.6 — "Tata Teleservices narrows Q2 loss to ₹59 crore, revenue up 8%; stock surges 9% on results "
- JEF (Jefferies Financial Group Inc.) score 11.0 — "KEI Industries shares: Down 15% in one month! Jefferies India sees 45% upside after Q2 res"
- GS (Goldman Sachs Group, Inc. (The) score 9.5 — "Goldman Sachs Warns of New Oil Price Shock as Tanker Rates Soar"
- VT (Vanguard Total World Stock Ind) score 6.6 — "CHINESE PREMIER SAYS CHINA, RUSSIA SERVE AS "VALUABLE FORCE FOR STABILITY IN TURBULENT WOR"
- WIT (Wipro Limited) score 6.3 — "IT stocks rebound sharply in October: TCS gains 22%, Wipro and Tech Mahindra gain 20% — 3 "
- NVDA (NVIDIA Corporation) score 6.1 — "NVIDIA MAY ALSO BE A BIDDER FOR AMBARELLA ( $AMBA ) - BETAVILLE"
- ETERNAL.NS (ETERNAL LIMITED) score 6.0 — "Market wrap: Bajaj Finance, Cipla, Nestle India, Eternal top gainers and losers on Nifty a"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.5 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
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