# Transmission Layer — board brief · 2026-09-11 08:54Z

data as of **2026-09-11** · 98 series · 12 red / 41 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.676, 2d in regime; vol-pct 0.519, breadth-off 0.833, Markov P(high-vol) 0.02)
- [INVERTED] **safe_haven_gold** — corr20 -0.48, corr60 -0.34, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.81, corr60 0.88, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.04, corr60 0.28, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.17, corr60 0.12, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.83, corr60 -0.85, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.11, corr60 -0.03, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.29, corr60 -0.17, last shift 2026-06-30. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.17, corr60 0.1, last shift 2026-07-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.499** (n=1123) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.82** (n=2067) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.17] cross-asset · 11 series ↓
- dow_jones [INDICES]: last 52067.02, z20 -3.30, zc -0.72, resid-z 0.91 [quiet], 1d -0.60%, |z20|=3.30
- dyn_vt [EQUITIES]: last 158.54, z20 -2.85, zc -1.12, resid-z -0.59 [quiet], 1d -0.84%, |z20|=2.85
- russell_2000 [INDICES]: last 2890.85, z20 -2.52, zc -0.85, resid-z -0.41 [quiet], 1d -1.04%, |z20|=2.52
- vix [INDICES]: last 17.44, z20 2.43, zc -0.27, resid-z n/a [quiet], 1d -2.24%, |z20|=2.43
- sp500 [INDICES]: last 7592.30, z20 -2.31, zc -0.77, resid-z -0.13 [quiet], 1d -0.58%, |z20|=2.31
- brent [COMMODITIES]: last 104.60, z20 2.29, zc -0.82, resid-z 1.88 [unexplained], 1d -2.82%, 1-session move -2.82% ≥ 1.5%; |z20|=2.29
- wti [COMMODITIES]: last 99.98, z20 2.28, zc -0.75, resid-z 1.97 [unexplained], 1d -2.44%, 1-session move -2.44% ≥ 1.5%; |z20|=2.28
- dax [INDICES]: last 25470.54, z20 -2.26, zc 0.44, resid-z -0.15 [quiet], 1d 0.43%, |z20|=2.26
- ftse_100 [INDICES]: last 10645.77, z20 -2.03, zc 0.46, resid-z -0.07 [quiet], 1d 0.35%, |z20|=2.03
- stoxx_50 [INDICES]: last 6304.73, z20 -1.85, zc 0.62, resid-z 0.09 [quiet], 1d 0.57%, |z20|=1.85
- cac_40 [INDICES]: last 8161.13, z20 -1.69, zc 0.57, resid-z 0.69 [quiet], 1d 0.55%, |z20|=1.69
- **Mechanism**: cross-asset · 11 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-10-21 (z-distance 0.76).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.497 via ftse_100, z -2.16, reacted); nifty_midcap_100 (rho 0.487 via dax, z -2.53, reacted); dyn_techm_ns (rho 0.404 via ftse_100, z -1.46, reacted); nifty_50 (rho 0.385 via ftse_100, z -2.32, reacted)
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.703 vs dow_jones, historically leads by 5d
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.575 vs sp500, historically leads by 1d
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.62 vs dyn_vt
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.574 vs dyn_vt
- Watch next: dyn_dell (co-move) — not yet - watch; rho 0.558 vs dyn_vt
- **India receivers**: nifty_it (rho 0.497, z -2.16); nifty_midcap_100 (rho 0.487, z -2.53); dyn_techm_ns (rho 0.404, z -1.46); nifty_50 (rho 0.385, z -2.32)
- Source: Sensex today | Stock Market Live: Sensex, Nifty stay under pressure as Brent crude hits $108 — BusinessLine Mkts, 2026-09-11. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-11th-september-2026/article71453005.ece
- Source: Oil Prices Could Top $120 as Middle East Conflict Escalates — OilPrice, 2026-09-11. https://oilprice.com/Latest-Energy-News/World-News/Oil-Prices-Could-Top-120-as-Middle-East-Conflict-Escalates.html
- Source: Stock Market Bloodbath! Sensex, Nifty fall 1% as crude hits $108: Should investors buy the dip or stay away? — Mint Markets, 2026-09-11. https://www.livemint.com/market/stock-market-news/stock-market-bloodbath-sensex-nifty-fall-1-as-crude-hits-108-should-investors-buy-the-dip-or-stay-away-11789109234662.html
- Historical analogues: 2024-10-21 (d=0.76), 2024-11-26 (d=0.77), 2024-11-14 (d=0.84)

### [RED 7.59] cross-asset · 5 series ↑
- dyn_bond [EQUITIES]: last 88.95, z20 -3.66, zc -2.69, resid-z -1.11 [moved], 1d -0.86%, |z20|=3.66; 1y-pct=0
- ust_10y [RATES]: last 4.83, z20 2.24, zc 0.66, resid-z 0.45 [quiet], 1d 0.63%, |z20|=2.24; 1y-pct=100
- ust_2y [RATES]: last 4.43, z20 2.06, zc 0.72, resid-z 0.72 [quiet], 1d 0.91%, |z20|=2.06; 1y-pct=100
- tips_10y_real [RATES]: last 2.46, z20 1.52, zc 0.76, resid-z 0.72 [quiet], 1d 1.23%, |z20|=1.52; 1y-pct=99
- ust_30y [RATES]: last 5.28, z20 1.23, zc 0.75, resid-z 0.53 [quiet], 1d 0.57%, 1y-pct=99
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dxy (inverse) — not yet - watch; rho -0.537 vs dyn_bond
- Watch next: eur_usd (co-move) — not yet - watch; rho 0.321 vs ust_2y, historically leads by 1d
- Source: Global bond yields surge as oil spike fuels inflation fears — ET Markets, 2026-09-11. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-bond-yields-surge-as-oil-spike-fuels-inflation-fears/articleshow/134047045.cms
- Source: US Market: Rising US debt, inflation keep pressure on long-term Treasury yields — ET Markets, 2026-09-11. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-market-rising-us-debt-inflation-keep-pressure-on-long-term-treasury-yields/articleshow/134045805.cms
- Source: India's 10-year bond yield surpasses 7% on rising oil, Treasury yields — ET Markets, 2026-09-11. https://economictimes.indiatimes.com/markets/bonds/indias-10-year-bond-yield-surpasses-7-on-rising-oil-treasury-yields/articleshow/134044172.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 6.7] cross-asset · 4 series ↓
- india_vix [INDICES]: last 12.30, z20 3.04, zc 0.76, resid-z n/a [quiet], 1d 4.24%, |z20|=3.04
- nifty_midcap_100 [INDICES]: last 62123.10, z20 -2.53, zc -0.57, resid-z -0.47 [quiet], 1d -0.38%, |z20|=2.53
- nifty_50 [INDICES]: last 23409.85, z20 -2.32, zc -0.52, resid-z 0.92 [quiet], 1d -0.29%, |z20|=2.32
- dyn_jiofin_bo [EQUITIES]: last 229.55, z20 -1.98, zc -0.49, resid-z 0.00 [quiet], 1d -0.69%, 1y-pct=2
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-17 (z-distance 0.67).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.62 via nifty_50, z -1.61, reacted); dyn_indianb_ns (rho 0.547 via nifty_midcap_100, z -1.73, reacted); nifty_it (rho 0.508 via nifty_50, z -2.16, reacted); dyn_techm_ns (rho 0.471 via nifty_50, z -1.46, reacted); dyn_indusindbk_bo (rho 0.459 via nifty_50, z -2.19, reacted)
- **India receivers**: nifty_fmcg (rho 0.62, z -1.61); dyn_indianb_ns (rho 0.547, z -1.73); nifty_it (rho 0.508, z -2.16); dyn_techm_ns (rho 0.471, z -1.46)
- Source: Sensex today | Stock Market Live: Sensex, Nifty stay under pressure as Brent crude hits $108 — BusinessLine Mkts, 2026-09-11. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-11th-september-2026/article71453005.ece
- Source: Market is down but this 1925 company stock is soaring; surges 20% amid fall of Sensex, Nifty 50 — Mint Markets, 2026-09-11. https://www.livemint.com/market/stock-market-news/market-is-down-but-this-1925-company-stock-is-soaring-surges-15-amid-fall-of-sensex-nifty-50-11789108704583.html
- Source: Stock Market Bloodbath! Sensex, Nifty fall 1% as crude hits $108: Should investors buy the dip or stay away? — Mint Markets, 2026-09-11. https://www.livemint.com/market/stock-market-news/stock-market-bloodbath-sensex-nifty-fall-1-as-crude-hits-108-should-investors-buy-the-dip-or-stay-away-11789109234662.html
- Historical analogues: 2025-07-17 (d=0.67), 2025-12-19 (d=1.13), 2024-11-07 (d=1.15)

### [RED 5.28] dyn_hdb ↓
- dyn_hdb [EQUITIES]: last 21.83, z20 -3.28, zc -0.79, resid-z -0.99 [quiet], 1d -1.13%, |z20|=3.28; 1y-pct=0
- **Mechanism**: dyn_hdb ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.608 via dyn_hdb, z -2.32, reacted); nifty_it (rho 0.535 via dyn_hdb, z -2.16, reacted); dyn_techm_ns (rho 0.453 via dyn_hdb, z -1.46, reacted); dyn_jiofin_bo (rho 0.4 via dyn_hdb, z -1.98, reacted); dyn_bharatcoal_ns (rho 0.384 via dyn_hdb, z -1.65, reacted)
- **India receivers**: nifty_50 (rho 0.608, z -2.32); nifty_it (rho 0.535, z -2.16); dyn_techm_ns (rho 0.453, z -1.46); dyn_jiofin_bo (rho 0.4, z -1.98)
- Source: Should you buy HDFC Bank shares? Stock slips 2% to hit a 52-week low- Experts suggest what investors should do — Mint Markets, 2026-09-11. https://www.livemint.com/market/stock-market-news/should-you-buy-hdfc-bank-shares-stock-slips-2-to-hit-a-52-week-low-experts-suggest-what-investors-should-do-11789111399447.html
- Source: HDFC Bank shares under pressure, hits fresh 52-week low — BusinessLine Mkts, 2026-09-11. https://www.thehindubusinessline.com/markets/stock-markets/hdfc-bank-shares-hit-fresh-52-week-low-amid-market-weakness/article71455169.ece
- Source: HDFC Bank shares fall 2% to fresh 52-week low despite victory in Credit Suisse AT1 bonds cases in Bahrain — ET Markets, 2026-09-11. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-bank-shares-fall-2-to-fresh-52-week-low-despite-victory-in-credit-suisse-at1-bonds-cases-in-bahrain/articleshow/134048892.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [RED 4.89] hang_seng ↓
- hang_seng [INDICES]: last 24805.63, z20 -2.89, zc -0.57, resid-z -1.30 [quiet], 1d -0.60%, |z20|=2.89
- **Mechanism**: hang_seng ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-04-02 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Hang Seng, Taiwan Taiex slip as Middle East tensions push oil above $100. What investors need to watch next? — Mint Markets, 2026-09-09. https://www.livemint.com/market/stock-market-news/hang-seng-taiwan-taiex-slip-as-middle-east-tensions-push-oil-above-100-what-investors-need-to-watch-next-11788951492880.html
- Historical analogues: 2026-04-02 (d=0.0), 2024-11-11 (d=0.06), 2025-12-04 (d=0.09)

### [RED 4.58] dyn_tech ↓
- dyn_tech [EQUITIES]: last 72.10, z20 -2.58, zc -0.11, resid-z -0.03 [quiet], 1d -0.21%, |z20|=2.58
- **Mechanism**: dyn_tech ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Orient Tech share surges 17% after this business update | All details here — Mint Markets, 2026-09-11. https://www.livemint.com/market/stock-market-news/orient-tech-share-surges-17-after-this-business-update-all-details-here-11789107926218.html
- Source: Sterlite Tech shares in focus as firm secures US certification for AI data centre fibre assemblies — ET Markets, 2026-09-11. https://economictimes.indiatimes.com/markets/stocks/news/sterlite-tech-shares-in-focus-as-firm-secures-us-certification-for-ai-data-centre-fibre-assemblies/articleshow/134044579.cms
- Source: PENTAGON REJECTS AI “DOOMSDAY” WARNINGS Pentagon tech chief Emil Michael pushed back on warnings that AI could destroy humanity, calling fears of mass job losses and runaway AI part of a growing “doom loop.” Meanwhile, the Pentagon has already shifted 90% of its classified AI workload away from Anth — DeItaone, 2026-09-10. https://t.me/walter_bloomberg/35603
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.0), 2025-05-19 (d=0.0)

### [AMBER 4.52] indices · 2 series ↓
- nikkei_225 [INDICES]: last 64006.42, z20 -1.69, zc -1.45, resid-z -0.07 [quiet], 1d -1.94%, |z20|=1.69
- shanghai_comp [INDICES]: last 3886.80, z20 -1.58, zc -1.72, resid-z -0.76 [moved], 1d -1.21%, |z20|=1.58
- **Mechanism**: indices · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-16 (z-distance 0.84).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_techm_ns (rho -0.538 via shanghai_comp, z -1.46, reacted); nifty_it (rho -0.471 via shanghai_comp, z -2.16, reacted); midcap_largecap_ratio (rho 0.392 via shanghai_comp, z 0.8, quiet)
- Watch next: kospi (co-move) — not yet - watch; rho 0.835 vs nikkei_225
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.776 vs nikkei_225
- Watch next: usd_mxn (inverse) — not yet - watch; rho -0.514 vs nikkei_225, historically leads by 3d
- **India receivers**: dyn_techm_ns (rho -0.538, z -1.46); nifty_it (rho -0.471, z -2.16); midcap_largecap_ratio (rho 0.392, z 0.8)
- Source: Global Market: Japan's Nikkei falls 3% as oil surge, US rate hike fears weigh — ET Markets, 2026-09-11. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-falls-3-as-oil-surge-us-rate-hike-fears-weigh/articleshow/134045193.cms
- Source: How Asian markets, crude will impact Sensex, Nifty 50: What GIFT Nifty, Nikkei, Kospi, Taiwan index signals for India — Mint Markets, 2026-09-11. https://www.livemint.com/market/stock-market-news/how-asian-markets-crude-will-impact-sensex-nifty-50-what-gift-nifty-nikkei-kospi-taiwan-index-signals-for-india-11789089499149.html
- Source: Stock Market prediction tomorrow: Sensex, Nifty outlook for Friday | Kospi, Taiwan Index, Nikkei cues to watch | 11 Sept — Mint Markets, 2026-09-10. https://www.livemint.com/market/stock-market-news/stock-market-prediction-tomorrow-sensex-nifty-outlook-for-friday-kospi-taiwan-index-nikkei-cues-to-watch-11-sept-11789033761629.html
- Historical analogues: 2025-07-16 (d=0.84), 2025-12-23 (d=1.2), 2026-06-12 (d=1.31)

### [AMBER 4.36] dyn_meta ↑
- dyn_meta [EQUITIES]: last 644.37, z20 2.36, zc -0.54, resid-z 2.62 [unexplained], 1d -1.43%, |z20|=2.36
- **Mechanism**: dyn_meta ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.372 via dyn_meta, z -2.53, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.372, z -2.53)
- Source: META - JPMORGAN TURNS BULLISH ON META’S AI POTENTIAL JPMorgan upgraded Meta to Overweight and raised its price target to $820 from $640, implying roughly 24% upside. The bank sees significant new revenue opportunities from AI agents, subscriptions and enterprise AI services beyond advertising. — DeItaone, 2026-09-10. https://t.me/walter_bloomberg/35569
- Source: US stocks fall as oil surges past $100 on deepening Middle East tensions, Meta jumps 5.5%, AMD gains 3.49% — Mint Markets, 2026-09-09. https://www.livemint.com/market/us-stocks-fall-as-oil-surges-past-100-on-deepening-middle-east-tensions-11788961419384.html
- Source: Meta’s stock jumps as new personal AI agent Muse addresses a major investor concern — MarketWatch Top, 2026-09-09. https://www.marketwatch.com/story/meta-stock-jumps-as-new-personal-ai-agent-muse-addresses-a-major-investor-concern-5ad0a373?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2024-10-21 (d=0.07)

## Watchlist (below surfacing floor)
commodities · 2 series ↑ (4.24), dyn_icicigi_bo ↓ (4.22), gold_silver_ratio ↑ (4.13), dyn_tatatech_ns ↓ (4.12), dyn_lth ↓ (4.05), usd_jpy ↓ (3.86), dyn_pcjeweller_ns ↑ (3.82), midcap_largecap_ratio ↑ (3.8), asx_200 ↓ (3.73), dyn_atherenerg_ns ↑ (3.09), cross-asset · 2 series ↓ (2.99), dyn_qcom ↑ (2.47)

## India macro
- nifty_50: 23409.8496 (1d -0.29%, z20 -2.32, flag amber)
- nifty_midcap_100: 62123.1016 (1d -0.38%, z20 -2.53, flag red)
- usd_inr: 95.6350 (1d 0.55%, z20 0.85, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6537 (1d -0.09%, z20 0.80, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · India CPI T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 88.3 — "Stock recommendations for 11 September from MarketSmith India"
- COALINDIA.NS (COAL INDIA LTD) score 84.9 — "Stock recommendations for 11 September from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 84.2 — "Stock recommendations for 11 September from MarketSmith India"
- INDIANB.NS (INDIAN BANK) score 60.7 — "Elevated food inflation means upside risks loom for FY27 inflation projections: IDFC First"
- COIN (Coinbase Global, Inc.) score 59.5 — "Global Market: Japan's Nikkei falls 3% as oil surge, US rate hike fears weigh"
- BAC (Bank of America Corporation) score 56.0 — "Elevated food inflation means upside risks loom for FY27 inflation projections: IDFC First"
- OHI (Omega Healthcare Investors, In) score 52.0 — "Midcap rally hides a deeper split: Every second stock down but index up 11% in 1 year. Are"
- HDB (HDFC Bank Limited) score 49.0 — "Elevated food inflation means upside risks loom for FY27 inflation projections: IDFC First"
- IDBI.NS (IDBI BANK LIMITED) score 44.8 — "Elevated food inflation means upside risks loom for FY27 inflation projections: IDFC First"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 44.8 — "Elevated food inflation means upside risks loom for FY27 inflation projections: IDFC First"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 44.8 — "Elevated food inflation means upside risks loom for FY27 inflation projections: IDFC First"
- CHKP (Check Point Software Technolog) score 44.1 — "NSE IPO: Price band set at  ₹1,700-1,785 per share; check key dates, issue details"
- BOND (PIMCO Active Bond Exchange-Tra) score 43.0 — "BESSENT DISMISSES TREASURY MARKET CONCERNS Treasury Secretary Scott Bessent says the bond "
- TECHM.NS (TECH MAHINDRA LIMITED) score 37.1 — "Sterlite Tech shares in focus as firm secures US certification for AI data centre fibre as"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 37.0 — "Sterlite Tech shares in focus as firm secures US certification for AI data centre fibre as"
- TECH (Bio-Techne Corp) score 37.0 — "Sterlite Tech shares in focus as firm secures US certification for AI data centre fibre as"
- LTH (Life Time Group Holdings, Inc.) score 29.4 — "Rentomojo IPO Day 3: GMP at 33%, subscription reaches 4.71 times. Should you subscribe?"
- 301077.SZ (CHINASTARS) score 27.7 — "Global Market: China state insurers, banks to raise up to $54 billion to bolster capital"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.8 — "US, IRAN PREPARE FOR PROTRACTED WAR Iran and the U.S. are reportedly preparing for a poten"
- JUSTDIAL.BO (JUST DIAL LTD.) score 14.3 — "Molbio Diagnostics shares surge over 50% in just 3 days! What is driving the rally?"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 14.0 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Current Price Update"
- SEPN (Septerna, Inc.) score 13.6 — "Raja Venkatraman recommends three stocks for 11 September"
- MS (Morgan Stanley) score 11.5 — "MUNI YIELDS SURGE TO HIGHEST SINCE APRIL 2025 U.S. 10-year municipal bond yields jumped to"
- PCJEWELLER.NS (PC JEWELLER LTD) score 11.3 — "Dividend stocks alert! Last chance to qualify- Kalyan Jewellers, Aarti Industries, Blue Je"
- JIOFIN.BO (Jio Financial Services Limited) score 11.2 — "Global Market: Hong Kong draws professionals back as IPO boom revives financial hub"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 10.8 — "Retail algo trading gets a makeover: how APIs, AI and regulation are opening the door for "
- META (Meta) score 9.4 — "Vedanta Aluminium Metal shares dip over 3% | Here's why Anil Agarwal-owned stock is nosedi"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 8.6 — "Tata Motors PV Share Price Live Updates: Tata Motors PV experiences a modest increase"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 8.6 — "Tata Motors PV Share Price Live Updates: Tata Motors PV experiences a modest increase"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.3 — "ICICI Bank Share Price Live Updates: Rs 1.09 crore remittance sent home by an Indian worki"
- NVDA (NVIDIA Corporation) score 7.0 — "NVDA - NVIDIA’S HUANG SEES CYBERSECURITY AS AI’S NEXT BIG MARKET Nvidia CEO Jensen Huang s"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 6.5 — "Running the numbers on Trump’s $5,000 dividend proposal, from its cost to the impact on av"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 6.0 — "IEA: Global Coal Demand Set to Hit Record High as Iran War Chokes LNG Supply"
- VT (Vanguard Total World Stock Ind) score 5.3 — "How China Became the World's First Electrostate"
- JEF (Jefferies Financial Group Inc.) score 4.0 — "Vodafone Idea shares price in focus as Jefferies initiates coverage with Buy rating. Why a"
- QCOM (QUALCOMM Incorporated) score 2.3 — "Qualcomm-Amazon AI deal: Why the chipmaker’s stock surged"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 1.0 — "Lenskart Solutions among 4 stocks to hit 52-week highs & rallied up to 22% in a month"
- DELL (Dell Technologies Inc.) score 0.8 — "Dell’s AI Boom: $95 billion backlog reshapes growth outlook"
- DKS (Dick's Sporting Goods Inc) score 0.1 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- VOLTAS.NS (VOLTAS LTD) score 0.0 — "Voltas reported strong growth in June quarter, but failed to impress"

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