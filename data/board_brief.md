# Transmission Layer — board brief · 2026-11-09 12:48Z

data as of **2026-11-09** · 97 series · 14 red / 37 amber · 8 events surfaced (22 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.613, 3d in regime; vol-pct 0.893, breadth-off 0.333, Markov P(high-vol) 0.553)
- [INVERTED] **safe_haven_gold** — corr20 -0.15, corr60 -0.22, contra nifty_50 corr20=0.29, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.91, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.12, corr60 0.12, last shift 2026-09-10. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.08, corr60 0.05, last shift 2026-09-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.91, last shift 2026-09-16. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.28, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.12, corr60 -0.11, last shift 2026-08-12. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.33, corr60 0.29, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **19 of 89** scanned series survive multiplicity control (effective p ≤ 0.019283739890716634)
- **SETUP** dxy → eur_usd: leads 1d (ccf -0.829, β -0.8883, p 0.0); driver zc 2.49 → expected -0.656%. Type hit-rate 0.819 (n=2126).
- **SETUP** dxy → gbp_usd: leads 1d (ccf -0.733, β -0.7782, p 0.0); driver zc 2.49 → expected -0.575%. Type hit-rate 0.819 (n=2126).
- **SETUP** dxy → usd_jpy: leads 1d (ccf 0.636, β 0.8913, p 0.0); driver zc 2.49 → expected 0.658%. Type hit-rate 0.819 (n=2126).
- **SETUP** dxy → aud_usd: leads 1d (ccf -0.559, β -0.8293, p 0.0); driver zc 2.49 → expected -0.612%. Type hit-rate 0.819 (n=2126).
- Track record · residual_reversion: hit-rate **0.509** (n=1124) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.819** (n=2126) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.562** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.95] commodities · 2 series ↓
- brent [COMMODITIES]: last 94.93, z20 -2.12, zc 0.01, resid-z 0.06 [quiet], 1d -3.45%, 1-session move -3.45% ≥ 1.5%; |z20|=2.12; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 88.25, z20 -2.09, zc 0.10, resid-z 0.25 [quiet], 1d -2.84%, 1-session move -2.84% ≥ 1.5%; |z20|=2.09
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.481 via wti, z 2.64, reacted)
- **India receivers**: dyn_muthootfin_ns (rho -0.481, z 2.64)
- Source: Iraq's Oil Sales to America Fall to Lowest Since the 2003 War — OilPrice, 2026-11-09. https://oilprice.com/Latest-Energy-News/World-News/Iraqs-Oil-Sales-to-America-Fall-to-Lowest-Since-the-2003-War.html
- Source: Sensex today | Stock Market Highlights: Stock markets end higher amid easing crude oil prices, buying in banks — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-9-november-2026/article71681002.ece
- Source: Iraq Strikes U.S. Deal to Boost Oil Exports Through Hormuz — OilPrice, 2026-11-09. https://oilprice.com/Latest-Energy-News/World-News/Iraq-Strikes-US-Deal-to-Boost-Oil-Exports-Through-Hormuz.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 7.77] cross-asset · 11 series ↓
- sp500 [INDICES]: last 7374.85, z20 -2.90, zc 0.15, resid-z 2.06 [unexplained], 1d 0.29%, |z20|=2.90
- dyn_vt [EQUITIES]: last 151.73, z20 -2.83, zc 0.12, resid-z 1.66 [unexplained], 1d 0.23%, |z20|=2.83
- eth_usd [CRYPTO]: last 2122.20, z20 -2.61, zc -1.33, resid-z 0.52 [quiet], 1d -5.10%, |z20|=2.61
- dyn_nvda [EQUITIES]: last 186.68, z20 -2.52, zc 0.60, resid-z -0.12 [quiet], 1d 2.80%, |z20|=2.52
- nasdaq_100 [INDICES]: last 26977.31, z20 -2.34, zc 0.46, resid-z 0.37 [quiet], 1d 1.30%, |z20|=2.34
- dyn_demz [EQUITIES]: last 46.82, z20 -2.08, zc 0.35, resid-z 1.56 [unexplained], 1d 0.62%, |z20|=2.08
- dyn_coin [EQUITIES]: last 134.71, z20 -2.06, zc -0.31, resid-z 0.44 [quiet], 1d -1.54%, |z20|=2.06; 1y-pct=0
- hy_oas [RATES]: last 3.48, z20 2.00, zc 1.63, resid-z -3.82 [unexplained], 1d 4.82%, |z20|=2.00; 1y-pct=100
- btc_usd [CRYPTO]: last 74732.81, z20 -1.92, zc -0.52, resid-z 0.04 [quiet], 1d -1.34%, |z20|=1.92
- dow_jones [INDICES]: last 51271.58, z20 -1.91, zc -0.27, resid-z -0.39 [quiet], 1d -0.49%, |z20|=1.91
- ig_oas [RATES]: last 0.93, z20 1.47, zc 0.82, resid-z -2.86 [unexplained], 1d 2.20%, 1y-pct=97
- **Mechanism**: cross-asset · 11 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-21 (z-distance 0.93).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.492 via ig_oas, z -1.5, reacted); nifty_it (rho 0.395 via ig_oas, z 0.71, quiet); nifty_midcap_100 (rho -0.386 via ig_oas, z 2.09, reacted); dyn_policybzr_ns (rho -0.357 via ig_oas, z -1.36, reacted)
- Watch next: dyn_jef (co-move) — not yet - watch; rho 0.673 vs dow_jones, historically leads by 5d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.82 vs sp500
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.5 vs eth_usd, historically leads by 1d
- Watch next: dyn_schd (co-move) — not yet - watch; rho 0.623 vs dow_jones
- **India receivers**: midcap_largecap_ratio (rho -0.492, z -1.5); nifty_it (rho 0.395, z 0.71); nifty_midcap_100 (rho -0.386, z 2.09); dyn_policybzr_ns (rho -0.357, z -1.36)
- Source: A new setback for the AI trade: Nvidia’s board is probing CEO Huang’s relationship with an alleged spy — MarketWatch Top, 2026-11-09. https://www.marketwatch.com/story/nvidias-board-will-probe-ceo-jensen-huangs-relationship-with-an-alleged-spy-heres-what-to-know-86656cd9?mod=mw_rss_topstories
- Source: Can the AI trade catch a break? Nvidia, Anthropic and CoreWeave may have a say. — MarketWatch Top, 2026-11-09. https://www.marketwatch.com/story/can-the-ai-trade-catch-a-break-nvidia-anthropic-and-coreweave-may-have-a-say-d00c9ab3?mod=mw_rss_topstories
- Source: Nvidia shares drop nearly 6% in pre-market as alleged China spy links put Jensen Huang under board scrutiny — Mint Markets, 2026-11-09. https://www.livemint.com/market/stock-market-news/nvidia-shares-drop-nearly-6-in-pre-market-as-alleged-china-spy-links-put-jensen-huang-under-board-scrutiny-11794222872171.html
- Historical analogues: 2025-10-21 (d=0.93), 2026-05-22 (d=1.22), 2025-10-31 (d=1.34)

### [RED 7.15] cross-asset · 7 series ↑
- nifty_50 [INDICES]: last 25044.65, z20 2.81, zc 1.80, resid-z 2.78 [unexplained], 1d 0.06%, |z20|=2.81
- dyn_muthootfin_ns [EQUITIES]: last 2917.60, z20 2.64, zc 0.28, resid-z -0.76 [quiet], 1d 1.69%, |z20|=2.64
- dyn_bajfinance_ns [EQUITIES]: last 1064.85, z20 2.28, zc 0.74, resid-z -0.69 [quiet], 1d -2.11%, |z20|=2.28
- nifty_metal [INDICES]: last 12664.75, z20 2.22, zc 0.45, resid-z -1.15 [quiet], 1d -0.11%, |z20|=2.22
- dyn_jiofin_bo [EQUITIES]: last 229.95, z20 2.18, zc 0.25, resid-z -1.10 [quiet], 1d -0.28%, |z20|=2.18
- nifty_midcap_100 [INDICES]: last 61018.65, z20 2.09, zc 0.00, resid-z -2.77 [unexplained], 1d 0.66%, |z20|=2.09
- nifty_fmcg [INDICES]: last 46660.10, z20 1.91, zc 0.49, resid-z -1.60 [unexplained], 1d -0.27%, |z20|=1.91
- **Mechanism**: cross-asset · 7 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 1.08).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_adanient_bo (rho 0.701 via nifty_metal, z 1.06, reacted); dyn_indusindbk_bo (rho 0.628 via nifty_midcap_100, z 1.32, reacted); dyn_indianb_ns (rho 0.609 via nifty_midcap_100, z 4.09, reacted); dyn_policybzr_ns (rho 0.528 via nifty_midcap_100, z -1.36, reacted); nifty_it (rho 0.515 via nifty_50, z 0.71, quiet)
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.515 vs nifty_50, historically leads by 4d
- Watch next: dyn_tatatech_ns (co-move) — not yet - watch; rho 0.505 vs dyn_jiofin_bo
- **India receivers**: dyn_adanient_bo (rho 0.701, z 1.06); dyn_indusindbk_bo (rho 0.628, z 1.32); dyn_indianb_ns (rho 0.609, z 4.09); dyn_policybzr_ns (rho 0.528, z -1.36)
- Source: Nifty holds 25,000 after volatile session; PSU Banks surge 3.7%, IT drags — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/nifty-holds-25000-after-volatile-session-psu-banks-surge-37-it-drags/article71682374.ece
- Source: Sensex today | Stock Market Highlights: Stock markets end higher amid easing crude oil prices, buying in banks — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-9-november-2026/article71681002.ece
- Source: Nifty slips to 24,882 at midday; IT, Steel, Cement drag as Rupee hits 2026 high — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/nifty-slips-to-24882-at-midday-it-steel-cement-drag-as-rupee-hits-2026-high/article71681848.ece
- Historical analogues: 2025-07-21 (d=1.08), 2025-07-11 (d=1.35), 2025-12-23 (d=1.37)

### [RED 7.06] usd_inr ↓
- usd_inr [FX]: last 93.93, z20 -2.06, zc -0.13, resid-z -0.39 [quiet], 1d -0.56%, 20d range extreme; |z20|=2.06; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.381 via usd_inr, z -0.26, quiet)
- **India receivers**: dyn_idbi_ns (rho -0.381, z -0.26)
- Source: FPI investments in FAR G-Secs rise nearly ₹8,000 cr as rupee gains, bond yields ease — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/fpi-investments-in-far-g-secs-rise-nearly-8000-cr-as-rupee-gains-bond-yields-ease/article71682301.ece
- Source: Rupee breaks six-day winning streak on state banks' dollar bids — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/forex/indian-rupee-breaks-six-day-winning-streak-on-state-banks-dollar-bids/article71682202.ece
- Source: Indian rupee breaks six-day winning streak on state banks' dollar bids — ET Markets, 2026-11-09. https://economictimes.indiatimes.com/markets/forex/indian-rupee-breaks-six-day-winning-streak-on-state-banks-dollar-bids/articleshow/135678769.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 5.83] rates · 2 series ↓
- ust_2y [RATES]: last 4.46, z20 -3.00, zc -2.07, resid-z -0.57 [priced], 1d -2.62%, |z20|=3.00
- ust_10y [RATES]: last 4.84, z20 -2.00, zc -1.12, resid-z 0.28 [quiet], 1d -1.22%, |z20|=2.00
- **Mechanism**: rates · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_schd (inverse) — not yet - watch; rho -0.574 vs ust_10y, historically leads by 2d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.017 vs ust_2y, historically leads by 1d
- Source: FPI investments in FAR G-Secs rise nearly ₹8,000 cr as rupee gains, bond yields ease — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/fpi-investments-in-far-g-secs-rise-nearly-8000-cr-as-rupee-gains-bond-yields-ease/article71682301.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-11 (d=0.18), 2025-05-15 (d=0.36)

### [RED 4.92] equities · 2 series ↑
- dyn_indianb_ns [EQUITIES]: last 933.70, z20 4.09, zc 0.51, resid-z -0.16 [quiet], 1d 3.51%, |z20|=4.09
- dyn_karurvysya_ns [EQUITIES]: last 370.00, z20 2.01, zc 1.01, resid-z 0.92 [quiet], 1d -0.01%, |z20|=2.01; 1y-pct=99
- **Mechanism**: equities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.609 via dyn_indianb_ns, z 2.09, reacted); dyn_jiofin_bo (rho 0.577 via dyn_indianb_ns, z 2.18, reacted); dyn_bajfinance_ns (rho 0.521 via dyn_indianb_ns, z 2.28, reacted); nifty_50 (rho 0.498 via dyn_indianb_ns, z 2.81, reacted); dyn_muthootfin_ns (rho 0.489 via dyn_indianb_ns, z 2.64, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.609, z 2.09); dyn_jiofin_bo (rho 0.577, z 2.18); dyn_bajfinance_ns (rho 0.521, z 2.28); nifty_50 (rho 0.498, z 2.81)
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-04 (d=0.46), 2025-02-01 (d=0.51)

### [AMBER 4.45] dyn_tech ↑
- dyn_tech [EQUITIES]: last 72.80, z20 2.45, zc 2.06, resid-z 0.17 [moved], 1d 0.19%, |z20|=2.45; 1y-pct=100
- **Mechanism**: dyn_tech ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: eur_inr (rho -0.444 via dyn_tech, z -2.84, reacted); dyn_coalindia_ns (rho 0.356 via dyn_tech, z -0.32, quiet)
- **India receivers**: eur_inr (rho -0.444, z -2.84); dyn_coalindia_ns (rho 0.356, z -0.32)
- Source: Until AI sentiment improves, Citi tells investors it’s better to sit out the global tech trade — MarketWatch Top, 2026-11-09. https://www.marketwatch.com/story/until-sentiment-in-the-ai-trade-improves-citi-tells-investors-its-better-to-sit-out-the-global-tech-trade-ed939f30?mod=mw_rss_topstories
- Source: US markets still reliant on tech stocks despite AI selloff and Democrat-win triggered political risks — ET Markets, 2026-11-09. https://economictimes.indiatimes.com/markets/us-stocks/news/us-markets-still-reliant-on-tech-stocks-despite-ai-selloff-and-democrat-win-triggered-political-risks/articleshow/135679992.cms
- Source: Tech Query: Alkem Laboratories, Intellect Design Arena, Trent, SRF — What is the outlook? Where are these stocks headed? — BusinessLine Mkts, 2026-11-07. https://www.thehindubusinessline.com/portfolio/technical-analysis/tech-query-alkem-laboratoriesintellect-design-arena-trent-srf-what-is-the-outlook-where-are-these-stocks-headed/article71674469.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.0), 2025-05-19 (d=0.0)

### [AMBER 3.79] indices · 3 series ↓
- kospi [INDICES]: last 5028.48, z20 -2.47, zc -1.60, resid-z -2.15 [unexplained], 1d -0.62%, |z20|=2.47
- nikkei_225 [INDICES]: last 58750.45, z20 -2.02, zc -3.56, resid-z -4.15 [unexplained], 1d 2.29%, |z20|=2.02
- taiwan_weighted [INDICES]: last 41680.11, z20 -1.74, zc -1.91, resid-z -3.45 [unexplained], 1d 4.98%, |z20|=1.74
- **Mechanism**: indices · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.563 via nikkei_225, z -1.5, reacted); nifty_50 (rho -0.541 via taiwan_weighted, z 2.81, reacted); nifty_it (rho -0.475 via kospi, z 0.71, quiet); dyn_idbi_ns (rho 0.45 via nikkei_225, z -0.26, quiet); dyn_inoxindia_ns (rho 0.367 via nikkei_225, z -0.47, quiet)
- Watch next: shanghai_comp (co-move) — not yet - watch; rho 0.502 vs kospi
- **India receivers**: midcap_largecap_ratio (rho 0.563, z -1.5); nifty_50 (rho -0.541, z 2.81); nifty_it (rho -0.475, z 0.71); dyn_idbi_ns (rho 0.45, z -0.26)

## Watchlist (below surfacing floor)
dyn_atherenerg_ns ↑ (3.74), dyn_4417_t ↑ (3.23), indices · 2 series ↑ (2.97), cross-asset · 2 series ↑ (2.84), eur_inr ↓ (2.84), dyn_hdb ↑ (2.82), dyn_havells_ns ↑ (2.52), dyn_schd ↑ (2.4), asx_200 ↑ (2.28), dyn_sepn ↑ (2.11), aud_usd ↓ (2.07), dyn_lth ↑ (1.85)

## India macro
- nifty_50: 25044.6504 (1d 0.06%, z20 2.81, flag red)
- nifty_midcap_100: 61018.6484 (1d 0.66%, z20 2.09, flag amber)
- usd_inr: 93.9275 (1d -0.56%, z20 -2.06, flag red)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4364 (1d 0.60%, z20 -1.50, flag none)
- Next India prints: AMFI SIP / MF flows T-0d · NSDL FPI flows T-0d · IMD weekly rainfall T-0d · India CPI T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 74.9 — "Edelweiss urges India to scrap foreign capital gains tax to revive markets"
- INOXINDIA.NS (INOX INDIA LIMITED) score 74.6 — "Edelweiss urges India to scrap foreign capital gains tax to revive markets"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 74.2 — "Edelweiss urges India to scrap foreign capital gains tax to revive markets"
- INDIANB.NS (INDIAN BANK) score 48.5 — "Coca-Cola’s Indian bottling arm HCCH files IPO papers; entire issue to be OFS"
- TECHM.NS (TECH MAHINDRA LIMITED) score 38.6 — "Tech Query: Alkem Laboratories, Intellect Design Arena, Trent, SRF — What is the outlook? "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 37.6 — "Tech Query: Alkem Laboratories, Intellect Design Arena, Trent, SRF — What is the outlook? "
- TECH (Bio-Techne Corp) score 37.6 — "Tech Query: Alkem Laboratories, Intellect Design Arena, Trent, SRF — What is the outlook? "
- BAC (Bank of America Corporation) score 34.5 — "Axis Bank Share Price Highlights: Axis Bank Stock Price History"
- HDB (HDFC Bank Limited) score 32.1 — "Axis Bank Share Price Highlights: Axis Bank Stock Price History"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 30.1 — "Axis Bank Share Price Highlights: Axis Bank Stock Price History"
- IDBI.NS (IDBI BANK LIMITED) score 30.1 — "Axis Bank Share Price Highlights: Axis Bank Stock Price History"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 30.1 — "Axis Bank Share Price Highlights: Axis Bank Stock Price History"
- OHI (Omega Healthcare Investors, In) score 29.9 — "Bosch shares falls 3% after stock split, bonus issue, Q2 results announcement | What shoul"
- 301077.SZ (CHINASTARS) score 28.5 — "China buys gold for 24th straight month, reserves rise to 78.3 million ounces"
- TGT (Target Corporation) score 26.5 — "Stock to buy: Elara Capital recommends this oil share amid volatility in crude oil prices "
- COIN (Coinbase Global, Inc.) score 26.2 — "Global gas supplies to tighten this winter due to Strait of Hormuz LNG shock, warns IEA"
- CHKP (Check Point Software Technolog) score 23.3 — "Crude Check: Bears make their move"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.8 — "How New York Plans to Turn Waste Heat Into Clean Energy"
- BOND (PIMCO Active Bond Exchange-Tra) score 21.1 — "India bonds could rally some more as fundamentals favour bulls"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 16.6 — "Pearl Global shares hit 52-week high ahead of dividend record date; will the rally continu"
- LTH (Life Time Group Holdings, Inc.) score 15.9 — "Why Sun Pharma Advanced Research shares surge 11% despite weak sentiments on D-Street; wha"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 14.6 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Daily Price Change"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 12.2 — "Tata Consumer Share Price Highlights: Tata Consumer Stock Price History"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 12.2 — "Tata Consumer Share Price Highlights: Tata Consumer Stock Price History"
- JIOFIN.BO (Jio Financial Services Limited) score 11.1 — "Jio Financial Services Share Price Highlights: Jio Financial Services Stock Price History"
- SCHD (Schwab US Dividend Equity ETF) score 10.5 — "Pearl Global shares hit 52-week high ahead of dividend record date; will the rally continu"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 10.1 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Daily Price Change"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.6 — "Stocks in focus: SBI, L&T, Alkem Lab, Adani Enterprises, BEL, GRSE, BHEL, Waaree Renewable"
- META (Meta) score 8.6 — "Vedanta Aluminium Metal among 5 stocks showing bullish RSI upswing"
- RS (Reliance, Inc.) score 8.5 — "US Midterm Election results impact on oil and IT shares: Reliance, Indian Oil, TCS, Infosy"
- BZ=F (Brent Crude Oil Last Day Finan) score 7.9 — "Iran suggests blasts are not US attacks as both sides report ships hit"
- DEMZ (Democratic Large Cap Core ETF) score 7.4 — "Democratic Win Set to Reshuffle U.S. Energy Policy"
- NVDA (NVIDIA Corporation) score 7.0 — "Nvidia falls about 3% in after-hours and perpetual futures trade"
- SEPN (Septerna, Inc.) score 4.6 — "DEMOCRATS SWEEP CONGRESS. FED HIKE BETS RETREAT. Following the midterm results, December F"
- JUSTDIAL.BO (JUST DIAL LTD.) score 4.2 — "₹13 to  ₹82: This multibagger small-cap stock turns  ₹1 lakh into 6.5 lakh in just 10 mont"
- JEF (Jefferies Financial Group Inc.) score 3.7 — "Jefferies warns AI investment cycle may have peaked; raises India allocation to 14%"
- GS (Goldman Sachs Group, Inc. (The) score 3.1 — "US midterms could accelerate stock market rotation; Goldman Sachs sees healthcare as ‘next"
- VT (Vanguard Total World Stock Ind) score 3.0 — "Gold prices may be nearing bottom as World Gold Council sees recovery signals"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.5 — "Broker’s call: PB Fintech (Buy)"
- SWIGGY.NS (SWIGGY LIMITED) score 0.2 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"

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