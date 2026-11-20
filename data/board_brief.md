# Transmission Layer — board brief · 2026-11-20 21:48Z

data as of **2026-11-20** · 97 series · 30 red / 34 amber · 8 events surfaced (36 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.938, 5d in regime; vol-pct 1.0, breadth-off 0.875, Markov P(high-vol) 1.0)
- [WEAK] **safe_haven_gold** — corr20 -0.18, corr60 -0.26, contra nifty_50 corr20=0.21, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.93, corr60 0.87, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.34, corr60 0.2, last shift 2026-09-25. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.03, corr60 0.07, last shift 2026-09-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.93, corr60 -0.91, last shift 2026-09-25. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.18, corr60 0.01, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.06, corr60 -0.14, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.37, corr60 0.34, last shift 2026-07-16. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.0003182171803151057)
- **SETUP** russell_2000 → nifty_metal: leads 1d (ccf 0.32, β 0.3562, p 2e-05); driver zc -1.92 → expected -0.975%. Type hit-rate 0.82 (n=2109).
- **SETUP** russell_2000 → nifty_midcap_100: leads 1d (ccf 0.289, β 0.249, p 0.0); driver zc -1.92 → expected -0.682%. Type hit-rate 0.82 (n=2109).
- **SETUP** sp500 → nifty_midcap_100: leads 1d (ccf 0.276, β 0.3187, p 0.0); driver zc -2.81 → expected -1.143%. Type hit-rate 0.82 (n=2109).
- **SETUP** aud_usd → usd_cny: leads 1d (ccf -0.27, β -0.0805, p 0.0); driver zc -2.73 → expected 0.113%. Type hit-rate 0.82 (n=2109).
- **SETUP** nasdaq_100 → nifty_midcap_100: leads 1d (ccf 0.262, β 0.2158, p 1e-05); driver zc -3.07 → expected -1.181%. Type hit-rate 0.82 (n=2109).
- **SETUP** vix → nifty_midcap_100: leads 1d (ccf -0.26, β -0.0294, p 0.00024); driver zc 2.11 → expected -0.769%. Type hit-rate 0.82 (n=2109).
- Track record · residual_reversion: hit-rate **0.512** (n=1157) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.82** (n=2109) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.438** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 12.54] cross-asset · 17 series ↓
- dyn_ms [EQUITIES]: last 165.66, z20 -4.82, zc -2.52, resid-z 0.06 [priced], 1d -5.33%, |z20|=4.82
- dyn_gs [EQUITIES]: last 790.74, z20 -4.68, zc -3.22, resid-z 0.48 [priced], 1d -6.70%, |z20|=4.68; 1y-pct=4
- vix [INDICES]: last 35.89, z20 4.14, zc 2.11, resid-z n/a [moved], 1d 26.20%, 1-session move +26.20% ≥ 15.0%; |z20|=4.14; 1y-pct=100
- dyn_bac [EQUITIES]: last 47.07, z20 -4.13, zc -2.14, resid-z 0.75 [priced], 1d -3.09%, |z20|=4.13; 1y-pct=2
- sp500 [INDICES]: last 6918.45, z20 -4.05, zc -2.81, resid-z -2.40 [unexplained], 1d -3.59%, |z20|=4.05
- dow_jones [INDICES]: last 48184.69, z20 -3.98, zc -1.43, resid-z 1.50 [unexplained], 1d -1.86%, |z20|=3.98
- russell_2000 [INDICES]: last 2582.42, z20 -3.79, zc -1.92, resid-z 0.35 [priced], 1d -2.74%, |z20|=3.79
- ftse_100 [INDICES]: last 10360.94, z20 -3.51, zc -0.91, resid-z 0.20 [quiet], 1d -0.88%, |z20|=3.51
- dyn_schd [EQUITIES]: last 33.96, z20 -3.17, zc -0.66, resid-z -2.00 [unexplained], 1d -0.70%, |z20|=3.17
- nasdaq_100 [INDICES]: last 25065.40, z20 -3.14, zc -3.07, resid-z 1.83 [unexplained], 1d -5.47%, |z20|=3.14
- dyn_rs [EQUITIES]: last 398.49, z20 -2.89, zc -2.42, resid-z -0.26 [moved], 1d -3.93%, |z20|=2.89
- stoxx_50 [INDICES]: last 5951.97, z20 -2.73, zc -2.58, resid-z -1.23 [moved], 1d -2.65%, |z20|=2.73
- dax [INDICES]: last 24839.47, z20 -2.64, zc -2.12, resid-z -0.83 [priced], 1d -2.45%, |z20|=2.64
- dyn_nvda [EQUITIES]: last 125.79, z20 -2.50, zc -4.31, resid-z 0.73 [priced], 1d -13.83%, |z20|=2.50; 1y-pct=0
- btc_usd [CRYPTO]: last 59015.11, z20 -2.33, zc -1.79, resid-z 0.35 [priced], 1d -4.66%, |z20|=2.33; 1y-pct=0
- eth_usd [CRYPTO]: last 1620.20, z20 -2.27, zc -2.04, resid-z -0.61 [priced], 1d -7.69%, |z20|=2.27; 1y-pct=3
- dyn_coin [EQUITIES]: last 101.95, z20 -2.17, zc -1.38, resid-z 1.49 [quiet], 1d -6.36%, |z20|=2.17; 1y-pct=0
- **Mechanism**: cross-asset · 17 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-24 (z-distance 1.6).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.494 via dax, z -0.43, quiet); dyn_bajfinance_ns (rho -0.494 via dyn_rs, z 1.3, reacted); dyn_indusindbk_bo (rho -0.488 via dyn_rs, z 3.52, reacted); usd_inr (rho 0.468 via dyn_bac, z -3.07, reacted); dyn_kaynes_ns (rho 0.412 via ftse_100, z -1.68, reacted)
- Watch next: cac_40 (co-move) — not yet - watch; rho 0.828 vs ftse_100
- **India receivers**: dyn_muthootfin_ns (rho 0.494, z -0.43); dyn_bajfinance_ns (rho -0.494, z 1.3); dyn_indusindbk_bo (rho -0.488, z 3.52); usd_inr (rho 0.468, z -3.07)
- Source: Wall Street banks set for banner year as Anthropic, SpaceX IPOs generate $1 billion in fees — Mint Markets, 2026-11-20. https://www.livemint.com/market/wall-street-banks-set-for-banner-year-as-anthropic-spacex-ipos-generate-1-billion-in-fees-11795201100809.html
- Source: Smallcap dividend stars: 5 stocks under  ₹100 with high dividend yield - Jagran Prakashan, Radiant Cash, and more — Mint Markets, 2026-11-20. https://www.livemint.com/market/stock-market-news/smallcap-dividend-stars-5-stocks-under-rs-100-with-high-dividend-yield-jagran-prakashan-radiant-cash-and-more-11795193828075.html
- Source: Pulse of the Street: Dalal Street extends winning run as global markets slide — Mint Markets, 2026-11-20. https://www.livemint.com/market/pulse-of-the-street-dalal-street-extends-winning-run-as-global-markets-slide-11795181421343.html
- Historical analogues: 2025-10-24 (d=1.6), 2026-04-02 (d=1.64), 2025-04-02 (d=1.69)

### [RED 9.35] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 3525.90, z20 -3.77, zc -2.23, resid-z -0.94 [priced], 1d -4.33%, |z20|=3.77; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 40.93, z20 -3.40, zc -2.60, resid-z -0.33 [priced], 1d -7.64%, |z20|=3.40; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 86.14, z20 3.03, zc n/a, resid-z n/a [quiet], 1d 3.59%, GSR>85 (extreme high); |z20|=3.03; 1y-pct=100
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.549 via comex_gold, z -0.43, quiet); dyn_karurvysya_ns (rho 0.491 via comex_gold, z 0.72, quiet)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.549 vs comex_gold, historically leads by 4d
- **India receivers**: dyn_muthootfin_ns (rho 0.549, z -0.43); dyn_karurvysya_ns (rho 0.491, z 0.72)
- Source: Forex reserves decline by $14 billion to $705 billion amid valuation effects, gold price decline — BusinessLine Mkts, 2026-11-20. https://www.thehindubusinessline.com/money-and-banking/forex-reserves-decline-by-14-billion-to-705-billion-amid-valuation-effects-gold-price-decline/article71725300.ece
- Source: Indian jewellery body alerts BIS over suspected gold adulteration, urges jewellers to tighten quality checks — BusinessLine Mkts, 2026-11-20. https://www.thehindubusinessline.com/companies/gjc-alerts-bis-over-suspected-gold-adulteration-urges-jewellers-to-tighten-quality-checks/article71723585.ece
- Source: GOLD PLUNGES 8% THIS WEEK AS MARKETS PRICE IN ANOTHER FED RATE HIKE Gold extended its selloff for a fifth consecutive session, heading for its worst weekly decline in eight months. 🔸 Spot gold: $3,585.92 (-1.0%) 🔸 Session low: $3,513.54 — lowest since September 2025 🔸 Weekly performance: Approximate — DeItaone, 2026-11-20. https://t.me/walter_bloomberg/38860
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 8.07] usd_inr ↓
- usd_inr [FX]: last 92.66, z20 -3.07, zc -2.02, resid-z -0.75 [moved], 1d -0.86%, 20d range extreme; |z20|=3.07; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho -0.44 via usd_inr, z -1.59, reacted); dyn_havells_ns (rho -0.426 via usd_inr, z 1.73, reacted); dyn_tataelxsi_ns (rho -0.417 via usd_inr, z 0.94, quiet); dyn_indianb_ns (rho -0.416 via usd_inr, z 1.42, reacted); dyn_indusindbk_bo (rho -0.413 via usd_inr, z 3.52, reacted)
- **India receivers**: nifty_it (rho -0.44, z -1.59); dyn_havells_ns (rho -0.426, z 1.73); dyn_tataelxsi_ns (rho -0.417, z 0.94); dyn_indianb_ns (rho -0.416, z 1.42)
- Source: Nifty hit 9-month high as Rupee logs best weekly rally in 5 weeks; Bond yields ease — BusinessLine Mkts, 2026-11-20. https://www.thehindubusinessline.com/markets/nifty-hit-9-month-high-as-rupee-logs-best-weekly-rally-in-5-weeks-bond-yields-ease/article71725535.ece
- Source: Rupee soars to 7-month high against the dollar, strengthens below 93 level — BusinessLine Mkts, 2026-11-20. https://www.thehindubusinessline.com/money-and-banking/rupee-soars-to-7-month-high-against-the-dollar-strengthens-below-93-level/article71724707.ece
- Source: Rupee climbs past 93/USD as investors seek shelter in Indian stocks, shorts unwind — ET Markets, 2026-11-20. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-climbs-past-93/usd-as-investors-seek-shelter-in-indian-stocks-shorts-unwind/articleshow/136023536.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 6.78] dyn_meta ↓
- dyn_meta [EQUITIES]: last 561.46, z20 -4.78, zc -2.36, resid-z 0.30 [priced], 1d -5.83%, |z20|=4.78
- **Mechanism**: dyn_meta ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho -0.358 via dyn_meta, z 1.3, reacted)
- **India receivers**: dyn_bajfinance_ns (rho -0.358, z 1.3)
- Source: Apple seems to be building its own AI agent. This could be bad news for Meta’s Muse. — MarketWatch Top, 2026-11-20. https://www.marketwatch.com/story/apple-seems-to-be-building-its-own-ai-agent-this-could-be-bad-news-for-metas-muse-8d9be2a7?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2025-10-09 (d=0.12)

### [RED 6.53] dyn_tatatech_ns ↑
- dyn_tatatech_ns [EQUITIES]: last 728.50, z20 4.53, zc 1.36, resid-z 0.99 [quiet], 1d 3.52%, |z20|=4.53
- **Mechanism**: dyn_tatatech_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.562 via dyn_tatatech_ns, z 3.52, reacted); dyn_jiofin_bo (rho 0.505 via dyn_tatatech_ns, z 0.59, quiet); nifty_midcap_100 (rho 0.497 via dyn_tatatech_ns, z 1.24, reacted); dyn_tataelxsi_ns (rho 0.496 via dyn_tatatech_ns, z 0.94, quiet); dyn_indianb_ns (rho 0.442 via dyn_tatatech_ns, z 1.42, reacted)
- Watch next: dyn_jiofin_bo (co-move) — not yet - watch; rho 0.505 vs dyn_tatatech_ns, historically leads by 1d
- **India receivers**: dyn_indusindbk_bo (rho 0.562, z 3.52); dyn_jiofin_bo (rho 0.505, z 0.59); nifty_midcap_100 (rho 0.497, z 1.24); dyn_tataelxsi_ns (rho 0.496, z 0.94)
- Source: Tata Steel shares slide nearly 2% as EU anti-dumping duty and bearish technicals weigh — BusinessLine Mkts, 2026-11-20. https://www.thehindubusinessline.com/markets/stock-markets/tata-steel-shares-slide-nearly-2-as-eu-anti-dumping-duty-and-bearish-technicals-weigh/article71723418.ece
- Source: Hindustan Zinc vs Tata Steel vs JSW Steel: Which metal stock to buy amid big fall in the metal stocks | Targets — Mint Markets, 2026-11-20. https://www.livemint.com/market/stock-market-news/hindustan-zinc-vs-tata-steel-vs-jsw-steel-which-metal-stock-to-buy-amid-big-fall-in-the-metal-stocks-targets-11795153441565.html
- Source: Tata Motors PV Share Price Live Updates: Tata Motors PV Stock Price History — ET Markets, 2026-11-20. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/tata-motors-pv-share-price-today-live-20-nov-2026/liveblog/136013458.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

### [RED 6.25] indices · 3 series ↓
- taiwan_weighted [INDICES]: last 35877.63, z20 -2.93, zc -2.38, resid-z -1.60 [unexplained], 1d -6.63%, |z20|=2.93
- nikkei_225 [INDICES]: last 56576.41, z20 -2.44, zc -3.02, resid-z -2.01 [unexplained], 1d -4.82%, |z20|=2.44
- kospi [INDICES]: last 4853.85, z20 -1.83, zc -1.89, resid-z -0.62 [moved], 1d -5.53%, |z20|=1.83
- **Mechanism**: indices · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho -0.586 via taiwan_weighted, z 1.5, reacted); midcap_largecap_ratio (rho 0.55 via kospi, z -1.81, reacted); dyn_indusindbk_bo (rho -0.541 via taiwan_weighted, z 3.52, reacted); nifty_it (rho -0.514 via kospi, z -1.59, reacted); nifty_midcap_100 (rho 0.432 via nikkei_225, z 1.24, reacted)
- Watch next: dyn_301077_sz (co-move) — not yet - watch; rho 0.622 vs taiwan_weighted, historically leads by 3d
- **India receivers**: nifty_50 (rho -0.586, z 1.5); midcap_largecap_ratio (rho 0.55, z -1.81); dyn_indusindbk_bo (rho -0.541, z 3.52); nifty_it (rho -0.514, z -1.59)
- Source: ANT - JAPAN’S NIKKEI PLUNGES NEARLY 5% AS ANTHROPIC IPO FAILS TO REVIVE AI CONFIDENCE Japan’s Nikkei plunged as much as 4.85%, hitting a seven-month low, as technology stocks suffered heavy selling. 🔸 SoftBank Group: -14.4% 🔸 Kioxia: -11.62% 🔸 Advantest: -10.15% 🔸 Tokyo Electron: -6.07% Anthropic op — DeItaone, 2026-11-20. https://t.me/walter_bloomberg/38857
- Source: Stock market outlook today,20 Nov:Sensex, Nifty prediction-DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-20. https://www.livemint.com/market/stock-market-outlook-today-20-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-cues-11795135137736.html
- Source: Stock market outlook today,19 Nov:Sensex, Nifty prediction-DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-19. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-19-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-cues-11795048871272.html

### [RED 6.25] natgas ↑
- natgas [COMMODITIES]: last 3.78, z20 3.25, zc 4.12, resid-z 5.18 [unexplained], 1d 15.61%, 1-session move +15.61% ≥ 5.0%; |z20|=3.25
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.425 via natgas, z 3.52, reacted); usd_inr (rho -0.363 via natgas, z -3.07, reacted)
- **India receivers**: dyn_indusindbk_bo (rho 0.425, z 3.52); usd_inr (rho -0.363, z -3.07)
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [AMBER 6.17] brent ↓
- brent [COMMODITIES]: last 89.99, z20 -1.17, zc -0.96, resid-z -2.72 [unexplained], 1d -2.16%, 1-session move -2.16% ≥ 1.5%; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: brent ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Saudi Arabia Expands Oil Storage in Japan as Tokyo Restocks — OilPrice, 2026-11-20. https://oilprice.com/Latest-Energy-News/World-News/Saudi-Arabia-Expands-Oil-Storage-in-Japan-as-Tokyo-Restocks.html
- Source: U.S. Oil Drillers Pick Up the Pace Just as Oil Prices Fall — OilPrice, 2026-11-20. https://oilprice.com/Energy/Energy-General/US-Oil-Drillers-Pick-Up-the-Pace-Just-as-Oil-Prices-Fall.html
- Source: Tankers Are Being Hit Daily. So Why Is Oil Falling? — OilPrice, 2026-11-20. https://oilprice.com/Energy/Crude-Oil/Tankers-Are-Being-Hit-Daily-So-Why-Is-Oil-Falling.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-14 (d=0.02), 2025-04-16 (d=0.04)

## Watchlist (below surfacing floor)
indices · 2 series ↓ (5.55), fx · 2 series ↓ (5.55), dyn_indusindbk_bo ↑ (5.52), comex_copper ↓ (4.85), cross-asset · 3 series ↑ (4.82), dxy ↑ (4.82), dyn_blln ↓ (4.36), dyn_crwv ↓ (4.36), usd_mxn ↑ (4.18), dyn_tgt ↑ (3.35), shanghai_comp ↓ (2.98), eur_inr ↓ (2.72)

## India macro
- nifty_50: 25800.5996 (1d 1.12%, z20 1.50, flag amber)
- nifty_midcap_100: 62021.6016 (1d 0.65%, z20 1.24, flag none)
- usd_inr: 92.6600 (1d -0.86%, z20 -3.07, flag red)
- goi_10y: 7.3800 (1d 4.53%, z20 3.03, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.1400 (1d -5.73%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4039 (1d -0.46%, z20 -1.81, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 102.7 — "Coal India Share Price Highlights: Coal India Ltd Stock Price History"
- INOXINDIA.NS (INOX INDIA LIMITED) score 95.7 — "Coal India Share Price Highlights: Coal India Ltd Stock Price History"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 94.9 — "Coal India Share Price Highlights: Coal India Ltd Stock Price History"
- INDIANB.NS (INDIAN BANK) score 70.4 — "ANT - JAPAN’S NIKKEI PLUNGES NEARLY 5% AS ANTHROPIC IPO FAILS TO REVIVE AI CONFIDENCE Japa"
- BAC (Bank of America Corporation) score 56.6 — "ANT - JAPAN’S NIKKEI PLUNGES NEARLY 5% AS ANTHROPIC IPO FAILS TO REVIVE AI CONFIDENCE Japa"
- HDB (HDFC Bank Limited) score 50.4 — "ANT - JAPAN’S NIKKEI PLUNGES NEARLY 5% AS ANTHROPIC IPO FAILS TO REVIVE AI CONFIDENCE Japa"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 47.2 — "ANT - JAPAN’S NIKKEI PLUNGES NEARLY 5% AS ANTHROPIC IPO FAILS TO REVIVE AI CONFIDENCE Japa"
- IDBI.NS (IDBI BANK LIMITED) score 47.2 — "ANT - JAPAN’S NIKKEI PLUNGES NEARLY 5% AS ANTHROPIC IPO FAILS TO REVIVE AI CONFIDENCE Japa"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 47.2 — "ANT - JAPAN’S NIKKEI PLUNGES NEARLY 5% AS ANTHROPIC IPO FAILS TO REVIVE AI CONFIDENCE Japa"
- NVDA (NVIDIA Corporation) score 44.8 — "TRUMP DID NOT TALK TOO MUCH ABOUT NVIDIA OR THE CHINESE SPY WITH CHINESE PRESIDENT XI -FOX"
- TECHM.NS (TECH MAHINDRA LIMITED) score 42.9 — "ANT - JAPAN’S NIKKEI PLUNGES NEARLY 5% AS ANTHROPIC IPO FAILS TO REVIVE AI CONFIDENCE Japa"
- OHI (Omega Healthcare Investors, In) score 41.7 — "PE investors seek easier take-private rules, leverage for acquisitions"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 40.6 — "ANT - JAPAN’S NIKKEI PLUNGES NEARLY 5% AS ANTHROPIC IPO FAILS TO REVIVE AI CONFIDENCE Japa"
- TECH (Bio-Techne Corp) score 40.6 — "ANT - JAPAN’S NIKKEI PLUNGES NEARLY 5% AS ANTHROPIC IPO FAILS TO REVIVE AI CONFIDENCE Japa"
- TGT (Target Corporation) score 39.7 — "StockGro expert explains: WeWork India share price target - should investors buy, sell or "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 28.4 — "India's growth story intact at 7%, but energy costs and twin deficits cloud the outlook: R"
- COIN (Coinbase Global, Inc.) score 26.6 — "Pulse of the Street: Dalal Street extends winning run as global markets slide"
- 301077.SZ (CHINASTARS) score 24.8 — "China’s Oil Imports from Persian Gulf Jump to Wartime High"
- BLLN (BillionToOne, Inc.) score 24.8 — "C - CITIGROUP UNDERSTATED RISK-WEIGHTED ASSETS BY $35 BILLION, FORCING CAPITAL INJECTION C"
- CHKP (Check Point Software Technolog) score 22.8 — "Indian jewellery body alerts BIS over suspected gold adulteration, urges jewellers to tigh"
- LTH (Life Time Group Holdings, Inc.) score 22.7 — "China’s Oil Imports from Persian Gulf Jump to Wartime High"
- BOND (PIMCO Active Bond Exchange-Tra) score 17.8 — "Nifty hit 9-month high as Rupee logs best weekly rally in 5 weeks; Bond yields ease"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 17.8 — "Bajaj Finance Share Price Highlights: Bajaj Finance Stock Price History"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 16.5 — "Tata Steel Share Price Highlights: Tata Steel Stock Price History"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 16.5 — "Tata Steel Share Price Highlights: Tata Steel Stock Price History"
- JIOFIN.BO (Jio Financial Services Limited) score 15.7 — "Federal Reserve Board releases results from survey of senior financial officers at banks a"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 13.9 — "Bajaj Finance Share Price Highlights: Bajaj Finance Stock Price History"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 11.1 — "Why Tips Films' shares jump 15% after the announcement of voluntary delisting? Experts's v"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.4 — "U.S. Oil Drillers Pick Up the Pace Just as Oil Prices Fall"
- BZ=F (Brent Crude Oil Last Day Finan) score 8.1 — "SPOT GOLD EXTENDS LOSSES, LAST DOWN NEARLY 2% AT $3,551.75/OZ"
- MS (Morgan Stanley) score 7.7 — "JPMORGAN SEES THREE MORE FED RATE HIKES AS U.S. GROWTH AND AI SPENDING MODERATE IN 2027 JP"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.7 — "Adani Ports SEZ Share Price Highlights: Adani Ports SEZ Stock Price History"
- META (Meta) score 7.4 — "Hindustan Zinc vs Tata Steel vs JSW Steel: Which metal stock to buy amid big fall in the m"
- SCHD (Schwab US Dividend Equity ETF) score 6.2 — "Smallcap dividend stars: 5 stocks under  ₹100 with high dividend yield - Jagran Prakashan,"
- GS (Goldman Sachs Group, Inc. (The) score 5.2 — "Goldman Sachs turns bullish on India stock market, upgrades rating to Overweight; sets Nif"
- CRWV (CoreWeave, Inc.) score 3.7 — "TECH STOCKS SLIDE AS AI SELL-OFF ACCELERATES Technology and AI-linked stocks face broad se"
- RS (Reliance, Inc.) score 2.9 — "Reliance Industries shares: After 13% surge in 1 month, JPMorgan sees another 23% upside i"
- ETERNAL.NS (ETERNAL LIMITED) score 2.7 — "Goldman Sachs names 22 ‘high-growth’ stocks; Bharti Airtel, Eternal and HDFC Bank feature "
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 2.0 — "Kaynes Technology shares extend losses, fall another 4%; should investors worry about its "
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 0.6 — "Cochin Shipyard dividend 2026: Last day to buy today | Check record date, payout amount, h"

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