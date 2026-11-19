# Transmission Layer — board brief · 2026-11-19 22:08Z

data as of **2026-11-19** · 97 series · 24 red / 32 amber · 8 events surfaced (33 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.905, 4d in regime; vol-pct 0.987, breadth-off 0.824, Markov P(high-vol) 0.473)
- [INVERTED] **safe_haven_gold** — corr20 -0.11, corr60 -0.22, contra nifty_50 corr20=0.29, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.91, corr60 0.86, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.33, corr60 0.2, last shift 2026-09-18. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.15, corr60 0.05, last shift 2026-09-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.95, corr60 -0.91, last shift 2026-09-24. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.13, corr60 -0.01, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.13, corr60 -0.14, last shift 2026-08-12. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.35, corr60 0.32, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **8 of 89** scanned series survive multiplicity control (effective p ≤ 0.008290602722071938)
- **SETUP** sp500 → nikkei_225: leads 1d (ccf 0.546, β 0.8569, p 0.0); driver zc -1.81 → expected -1.709%. Type hit-rate 0.821 (n=2012).
- **SETUP** russell_2000 → nikkei_225: leads 1d (ccf 0.525, β 0.6531, p 0.0); driver zc -1.6 → expected -1.397%. Type hit-rate 0.821 (n=2012).
- **SETUP** vix → nikkei_225: leads 1d (ccf -0.494, β -0.0849, p 0.0); driver zc 1.9 → expected -1.352%. Type hit-rate 0.821 (n=2012).
- **SETUP** dow_jones → nikkei_225: leads 1d (ccf 0.464, β 0.7839, p 0.0); driver zc -2.0 → expected -1.695%. Type hit-rate 0.821 (n=2012).
- **SETUP** dyn_gs → nikkei_225: leads 1d (ccf 0.456, β 0.3694, p 0.0); driver zc -1.51 → expected -1.085%. Type hit-rate 0.821 (n=2012).
- **SETUP** russell_2000 → kospi: leads 1d (ccf 0.375, β 0.7084, p 0.0); driver zc -1.6 → expected -1.515%. Type hit-rate 0.821 (n=2012).
- **SETUP** sp500 → kospi: leads 1d (ccf 0.362, β 0.8659, p 0.0); driver zc -1.81 → expected -1.727%. Type hit-rate 0.821 (n=2012).
- **SETUP** vix → india_vix: leads 1d (ccf 0.359, β 0.2237, p 0.00523); driver zc 1.9 → expected 3.561%. Type hit-rate 0.821 (n=2012).
- **SETUP** sp500 → india_vix: leads 1d (ccf -0.355, β -2.2554, p 0.00899); driver zc -1.81 → expected 4.498%. Type hit-rate 0.821 (n=2012).
- **SETUP** vix → kospi: leads 1d (ccf -0.351, β -0.0921, p 0.0); driver zc 1.9 → expected -1.466%. Type hit-rate 0.821 (n=2012).
- **SETUP** dyn_gs → kospi: leads 1d (ccf 0.346, β 0.4333, p 0.0); driver zc -1.51 → expected -1.273%. Type hit-rate 0.821 (n=2012).
- **SETUP** russell_2000 → nifty_metal: leads 1d (ccf 0.321, β 0.358, p 2e-05); driver zc -1.6 → expected -0.766%. Type hit-rate 0.821 (n=2012).
- **SETUP** russell_2000 → nifty_midcap_100: leads 1d (ccf 0.293, β 0.253, p 0.0); driver zc -1.6 → expected -0.541%. Type hit-rate 0.821 (n=2012).
- **SETUP** sp500 → nifty_midcap_100: leads 1d (ccf 0.281, β 0.3259, p 0.0); driver zc -1.81 → expected -0.65%. Type hit-rate 0.821 (n=2012).
- **SETUP** aud_usd → usd_cny: leads 1d (ccf -0.269, β -0.0803, p 0.0); driver zc -2.33 → expected 0.091%. Type hit-rate 0.821 (n=2012).
- **SETUP** vix → nifty_midcap_100: leads 1d (ccf -0.263, β -0.0298, p 0.00023); driver zc 1.9 → expected -0.474%. Type hit-rate 0.821 (n=2012).
- Track record · residual_reversion: hit-rate **0.51** (n=1159) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.821** (n=2012) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.28] cross-asset · 10 series ↓
- dow_jones [INDICES]: last 49112.63, z20 -4.20, zc -2.00, resid-z -1.62 [unexplained], 1d -2.16%, |z20|=4.20
- dyn_schd [EQUITIES]: last 34.19, z20 -3.55, zc -1.40, resid-z -2.73 [unexplained], 1d -1.47%, |z20|=3.55
- dyn_ms [EQUITIES]: last 174.98, z20 -3.50, zc -1.84, resid-z -0.43 [priced], 1d -3.42%, |z20|=3.50
- russell_2000 [INDICES]: last 2656.24, z20 -3.07, zc -1.60, resid-z -0.79 [priced], 1d -2.14%, |z20|=3.07
- sp500 [INDICES]: last 7177.56, z20 -2.93, zc -1.81, resid-z -1.20 [moved], 1d -1.99%, |z20|=2.93
- dyn_gs [EQUITIES]: last 847.52, z20 -2.63, zc -1.51, resid-z 0.28 [priced], 1d -2.94%, |z20|=2.63
- dyn_bac [EQUITIES]: last 48.56, z20 -2.60, zc -0.49, resid-z -0.25 [quiet], 1d -0.72%, |z20|=2.60
- vix [INDICES]: last 28.47, z20 2.52, zc 1.90, resid-z n/a [moved], 1d 15.92%, 1-session move +15.92% ≥ 15.0%; |z20|=2.52; 1y-pct=98
- dyn_nvda [EQUITIES]: last 146.00, z20 -1.89, zc -1.02, resid-z -1.04 [quiet], 1d -3.29%, 1y-pct=0
- nasdaq_100 [INDICES]: last 26523.44, z20 -1.86, zc -1.28, resid-z 1.89 [unexplained], 1d -2.19%, |z20|=1.86
- **Mechanism**: cross-asset · 10 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.38).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: usd_inr (rho 0.423 via dyn_bac, z -2.22, reacted); dyn_kaynes_ns (rho 0.377 via dyn_bac, z -2.05, reacted)
- **India receivers**: usd_inr (rho 0.423, z -2.22); dyn_kaynes_ns (rho 0.377, z -2.05)
- Source: Nvidia’s stock falls further. It has lost $669 billion in six trading days. — MarketWatch Top, 2026-11-19. https://www.marketwatch.com/story/nvidias-stock-falls-further-it-has-lost-611-billion-in-six-trading-days-434af231?mod=mw_rss_topstories
- Source: ‘I felt so seen’: Why families across America are laughing — and crying — over SNL’s ‘Sister’ sketch — MarketWatch Top, 2026-11-19. https://www.marketwatch.com/story/so-sad-and-so-true-has-your-family-talked-about-snls-sister-sketch-yet-19bf9d67?mod=mw_rss_topstories
- Source: Latin America Currencies Sink on Rate Worries; Brazil Intervenes — Mint Markets, 2026-11-19. https://www.livemint.com/market/latin-america-currencies-sink-on-rate-worries-brazil-intervenes-11795119814041.html
- Historical analogues: 2026-05-22 (d=0.38), 2025-08-22 (d=1.1), 2025-08-14 (d=1.11)

### [RED 7.22] usd_inr ↓
- usd_inr [FX]: last 93.28, z20 -2.22, zc -0.48, resid-z 0.18 [quiet], 1d -0.21%, 20d range extreme; |z20|=2.22; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_havells_ns (rho -0.446 via usd_inr, z 1.79, reacted); dyn_indianb_ns (rho -0.439 via usd_inr, z 1.51, reacted); nifty_it (rho -0.413 via usd_inr, z -3.05, reacted); dyn_tataelxsi_ns (rho -0.377 via usd_inr, z -0.93, quiet); dyn_bajfinance_ns (rho -0.35 via usd_inr, z 1.03, reacted)
- **India receivers**: dyn_havells_ns (rho -0.446, z 1.79); dyn_indianb_ns (rho -0.439, z 1.51); nifty_it (rho -0.413, z -3.05); dyn_tataelxsi_ns (rho -0.377, z -0.93)
- Source: Rupee extends rally to close 5 paise higher at 93.36 against US dollar — BusinessLine Mkts, 2026-11-19. https://www.thehindubusinessline.com/markets/forex/rupee-extends-rally-to-close-5-paise-higher-at-9336-against-us-dollar/article71719784.ece
- Source: Stock rally keeps rupee upbeat, traders eye exporters for fresh fuel — ET Markets, 2026-11-19. https://economictimes.indiatimes.com/markets/forex/forex-news/india-rupee-stock-rally-keeps-rupee-upbeat-traders-eye-exporters-for-fresh-fuel/articleshow/135986825.cms
- Source: Rupee slides 8 paise to 93.49 against US dollar in early trade — BusinessLine Mkts, 2026-11-19. https://www.thehindubusinessline.com/markets/forex/rupee-slides-8-paise-to-9349-against-us-dollar-in-early-trade/article71718647.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 6.94] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 3627.00, z20 -3.63, zc -1.50, resid-z -1.97 [unexplained], 1d -3.07%, |z20|=3.63; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 42.86, z20 -3.18, zc -1.54, resid-z 0.39 [priced], 1d -4.75%, |z20|=3.18; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 84.62, z20 2.66, zc n/a, resid-z n/a [quiet], 1d 1.77%, |z20|=2.66; 1y-pct=100
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.52 via comex_gold, z -0.06, quiet); dyn_karurvysya_ns (rho 0.47 via comex_gold, z 1.19, reacted); nifty_metal (rho 0.37 via comex_gold, z 0.22, quiet)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.52 vs comex_gold, historically leads by 4d
- **India receivers**: dyn_muthootfin_ns (rho 0.52, z -0.06); dyn_karurvysya_ns (rho 0.47, z 1.19); nifty_metal (rho 0.37, z 0.22)
- Source: 15% fall in gold prices could trigger panic, warn lenders — BusinessLine Mkts, 2026-11-19. https://www.thehindubusinessline.com/markets/gold/15-fall-in-gold-prices-could-trigger-panic-warn-lenders/article71719017.ece
- Source: Today’s Gold Rate in India, November 19: Gold prices down in Delhi, Mumbai, Kolkata, Chennai, Bengaluru — BusinessLine Mkts, 2026-11-19. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-delhi-mumbai-kolkata-chennai-bengaluru-hyderabad-pune-gold-rates-metro-cities-november-19-2026/article71719289.ece
- Source: Today’s Gold Rate in India November 19: Gold prices down in Coimbatore, Nagpur, Visakhapatnam, Surat, Jaipur — BusinessLine Mkts, 2026-11-19. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-coimbatore-nagpur-visakhapatnam-surat-jaipur-lucknow-chandigarh-gold-rates-other-cities-november-19-2026/article71719290.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [AMBER 6.27] brent ↓
- brent [COMMODITIES]: last 90.05, z20 -1.27, zc -0.85, resid-z -2.14 [unexplained], 1d -2.07%, 1-session move -2.07% ≥ 1.5%; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: brent ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Mercosur’s Tax Break Is Fueling Brazil’s Oil Push Into Europe — OilPrice, 2026-11-19. https://oilprice.com/Energy/Crude-Oil/Mercosurs-Tax-Break-Is-Fueling-Brazils-Oil-Push-Into-Europe.html
- Source: US Sour Crude’s War Premium Vanishes as Supply Surges — Mint Markets, 2026-11-19. https://www.livemint.com/market/us-sour-crude-s-war-premium-vanishes-as-supply-surges-11795121544365.html
- Source: EU Moves to Overhaul Emergency Oil Stockpiles — OilPrice, 2026-11-19. https://oilprice.com/Latest-Energy-News/World-News/EU-Moves-to-Overhaul-Emergency-Oil-Stockpiles.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-14 (d=0.02), 2025-04-16 (d=0.04)

### [RED 5.88] cross-asset · 2 series ↓
- nifty_it [INDICES]: last 30919.45, z20 -3.05, zc -0.74, resid-z -1.68 [unexplained], 1d -1.10%, |z20|=3.05
- dyn_techm_ns [EQUITIES]: last 1723.00, z20 -2.91, zc -0.98, resid-z -1.59 [unexplained], 1d -1.54%, |z20|=2.91
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.52).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tataelxsi_ns (rho 0.674 via nifty_it, z -0.93, quiet); nifty_50 (rho 0.494 via nifty_it, z 1.38, reacted); dyn_justdial_bo (rho 0.444 via dyn_techm_ns, z -0.91, quiet); dyn_indianb_ns (rho 0.443 via nifty_it, z 1.51, reacted); usd_inr (rho -0.413 via nifty_it, z -2.22, reacted)
- Watch next: dyn_tataelxsi_ns (co-move) — not yet - watch; rho 0.674 vs nifty_it, historically leads by 1d
- **India receivers**: dyn_tataelxsi_ns (rho 0.674, z -0.93); nifty_50 (rho 0.494, z 1.38); dyn_justdial_bo (rho 0.444, z -0.91); dyn_indianb_ns (rho 0.443, z 1.51)
- Source: SML Mahindra offers shares at 37% discount as M&M steps up CV expansion — BusinessLine Mkts, 2026-11-18. https://www.thehindubusinessline.com/markets/sml-mahindra-offers-shares-at-36-discount-as-mm-steps-up-cv-expansion/article71714724.ece
- Source: SML Mahindra offers shares at 36% discount as M&M steps up CV expansion — BusinessLine Mkts, 2026-11-18. https://www.thehindubusinessline.com/markets/sml-mahindra-offers-shares-at-36-discount-as-mm-steps-up-cv-expansion/article71714724.ece
- Historical analogues: 2025-12-30 (d=0.52), 2025-08-13 (d=0.76), 2026-01-06 (d=0.77)

### [RED 5.87] fx · 2 series ↓
- gbp_usd [FX]: last 1.31, z20 -3.04, zc -2.30, resid-z -3.32 [unexplained], 1d -0.86%, |z20|=3.04; 1y-pct=0
- eur_usd [FX]: last 1.10, z20 -2.36, zc -0.58, resid-z -1.14 [quiet], 1d -0.21%, |z20|=2.36; 1y-pct=0
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.052 vs eur_usd, historically leads by 1d
- Source: GOLD, SILVER AND COPPER PLUNGE AS METALS SELLOFF ACCELERATES Precious and industrial metals extended losses, with futures falling to fresh lows for the year amid a stronger dollar and expectations of persistently high interest rates. Copper plunged 6.1% to $5.62 per pound, pressured by concerns over — DeItaone, 2026-11-18. https://t.me/walter_bloomberg/38776
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [AMBER 5.48] cross-asset · 3 series ↓
- btc_usd [CRYPTO]: last 61660.40, z20 -2.16, zc -0.75, resid-z -0.09 [quiet], 1d -2.11%, |z20|=2.16; 1y-pct=4
- dyn_coin [EQUITIES]: last 108.87, z20 -1.97, zc -0.32, resid-z -0.14 [quiet], 1d -1.48%, 1y-pct=0
- eth_usd [CRYPTO]: last 1742.07, z20 -1.90, zc -0.48, resid-z 0.19 [quiet], 1d -1.84%, |z20|=1.90
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.46).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: How Energy Security Is Reshaping Global Investment Decisions — OilPrice, 2026-11-19. https://oilprice.com/Energy/Energy-General/How-Energy-Security-Is-Reshaping-Global-Investment-Decisions.html
- Source: Signature Global acquires 10-acre land parcels in Gurugram to build realty projects — ET Markets, 2026-11-19. https://economictimes.indiatimes.com/markets/digital-real-estate/realty-news/signature-global-acquires-10-acre-land-parcels-in-gurugram-to-build-realty-projects/articleshow/135997924.cms
- Source: Global Cooling Demand Overtakes Heating for the First Time — OilPrice, 2026-11-19. https://oilprice.com/Latest-Energy-News/World-News/Global-Cooling-Demand-Overtakes-Heating-for-the-First-Time.html
- Historical analogues: 2026-05-22 (d=0.46), 2025-10-16 (d=0.54), 2025-04-10 (d=0.6)

### [RED 5.16] dxy ↑
- dxy [FX]: last 103.95, z20 2.16, zc 0.24, resid-z 1.30 [quiet], 1d 0.08%, 20d range extreme; |z20|=2.16; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.537 vs dxy, historically leads by 1d
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-10 (d=0.03), 2025-05-14 (d=0.06)

## Watchlist (below surfacing floor)
dyn_tatatech_ns ↑ (5.14), comex_copper ↓ (4.99), dyn_blln ↓ (4.89), dyn_301077_sz ↑ (4.41), dyn_tgt ↑ (3.84), usd_mxn ↑ (3.68), dyn_crwv ↓ (3.56), hang_seng ↓ (3.43), ftse_100 ↓ (3.41), dyn_inoxindia_ns ↑ (3.36), dyn_eternal_ns ↑ (3.02), dyn_4417_t ↑ (2.73)

## India macro
- nifty_50: 25514.3008 (1d 1.14%, z20 1.38, flag none)
- nifty_midcap_100: 61618.8516 (1d 1.06%, z20 1.16, flag none)
- usd_inr: 93.2800 (1d -0.21%, z20 -2.22, flag red)
- goi_10y: 7.3800 (1d 4.53%, z20 3.03, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.1400 (1d -5.73%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4151 (1d -0.08%, z20 -1.63, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 94.6 — "Goldman Sachs turns bullish on India stock market, upgrades rating to Overweight; sets Nif"
- INOXINDIA.NS (INOX INDIA LIMITED) score 87.0 — "Goldman Sachs turns bullish on India stock market, upgrades rating to Overweight; sets Nif"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 86.0 — "Goldman Sachs turns bullish on India stock market, upgrades rating to Overweight; sets Nif"
- INDIANB.NS (INDIAN BANK) score 57.8 — "JPMORGAN SEES THREE MORE FED RATE HIKES AS U.S. GROWTH AND AI SPENDING MODERATE IN 2027 JP"
- NVDA (NVIDIA Corporation) score 54.2 — "Peterson: Nvidia’s leadership crisis tests the chipmaker’s role as the ‘central bank of AI"
- BAC (Bank of America Corporation) score 51.1 — "JPMORGAN SEES THREE MORE FED RATE HIKES AS U.S. GROWTH AND AI SPENDING MODERATE IN 2027 JP"
- HDB (HDFC Bank Limited) score 44.5 — "JPMORGAN SEES THREE MORE FED RATE HIKES AS U.S. GROWTH AND AI SPENDING MODERATE IN 2027 JP"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 41.5 — "JPMORGAN SEES THREE MORE FED RATE HIKES AS U.S. GROWTH AND AI SPENDING MODERATE IN 2027 JP"
- IDBI.NS (IDBI BANK LIMITED) score 41.5 — "JPMORGAN SEES THREE MORE FED RATE HIKES AS U.S. GROWTH AND AI SPENDING MODERATE IN 2027 JP"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 41.5 — "JPMORGAN SEES THREE MORE FED RATE HIKES AS U.S. GROWTH AND AI SPENDING MODERATE IN 2027 JP"
- TECHM.NS (TECH MAHINDRA LIMITED) score 38.4 — "Sterlite Technologies among 3 stocks showing White Marubozu pattern"
- TGT (Target Corporation) score 36.2 — "ANT - WALL STREET TURNS BULLISH ON ANTHROPIC WITH PRICE TARGETS UP TO $155 Four Wall Stree"
- OHI (Omega Healthcare Investors, In) score 35.7 — "Investors vs Economists: Should Govt Cut LTCG Tax?"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 35.5 — "Sterlite Technologies among 3 stocks showing White Marubozu pattern"
- TECH (Bio-Techne Corp) score 35.5 — "Sterlite Technologies among 3 stocks showing White Marubozu pattern"
- COIN (Coinbase Global, Inc.) score 27.7 — "Signature Global acquires 10-acre land parcels in Gurugram to build realty projects"
- 301077.SZ (CHINASTARS) score 25.5 — "RUSSIA'S PUTIN: TRILATERAL SUMMIT BETWEEN RUSSIA, CHINA AND THE USA – A CHAPTER IN THE HIS"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 23.1 — "Carlyle and Orlen Team Up to Hunt for Energy Deals Across Europe"
- BLLN (BillionToOne, Inc.) score 22.8 — "Japanese investors sought $9.4 billion of shares in Anthropic IPO, sources say"
- LTH (Life Time Group Holdings, Inc.) score 21.5 — "Nifty claws back 286 pts; Bank Nifty hits all-time high Auto, Banking rally"
- CHKP (Check Point Software Technolog) score 20.5 — "Gold Rates Live Updates: Gold prices fall marginally, silver gains on MCX. Check future es"
- BOND (PIMCO Active Bond Exchange-Tra) score 17.7 — "Amundi CIO says not bearish on France bonds, AI at the start of repricing"
- JIOFIN.BO (Jio Financial Services Limited) score 17.3 — "HACKERS ACCESSED FINANCIAL INFORMATION OF AS MANY AS 4,000 RETIRED NEW YORK CITY GOVT WORK"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 15.2 — "IIFL Finance shares drop over 3% after Fairfax pared over 13% stake"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 12.5 — "Tata Tech shares jump 10% as company targets $1.3 billion revenue by FY30, bets on aerospa"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 12.5 — "Tata Tech shares jump 10% as company targets $1.3 billion revenue by FY30, bets on aerospa"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 11.7 — "Why gold, silver prices are going down? What experts say about rate fall - More plunge ahe"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 11.4 — "IIFL Finance shares drop over 3% after Fairfax pared over 13% stake"
- MS (Morgan Stanley) score 9.7 — "JPMORGAN SEES THREE MORE FED RATE HIKES AS U.S. GROWTH AND AI SPENDING MODERATE IN 2027 JP"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.5 — "A CoreWeave co-founder just made an unconventional $30 million wager on its battered bonds"
- BZ=F (Brent Crude Oil Last Day Finan) score 6.8 — "Dividend record date, Nov 19: Last day to buy today to qualify- Oil India, Ashok Leyland, "
- GS (Goldman Sachs Group, Inc. (The) score 6.5 — "Goldman Sachs turns bullish on India stock market, upgrades rating to Overweight; sets Nif"
- META (Meta) score 5.8 — "GOLD, SILVER AND COPPER PLUNGE AS METALS SELLOFF ACCELERATES Precious and industrial metal"
- SCHD (Schwab US Dividend Equity ETF) score 5.3 — "Dividend record date, Nov 19: Last day to buy today to qualify- Oil India, Ashok Leyland, "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 4.9 — "Adani Ent Share Price Highlights: Adani Ent. Stock Price History"
- RS (Reliance, Inc.) score 3.6 — "Reliance Industries shares: After 13% surge in 1 month, JPMorgan sees another 23% upside i"
- CRWV (CoreWeave, Inc.) score 3.4 — "A CoreWeave co-founder just made an unconventional $30 million wager on its battered bonds"
- ETERNAL.NS (ETERNAL LIMITED) score 3.4 — "Goldman Sachs names 22 ‘high-growth’ stocks; Bharti Airtel, Eternal and HDFC Bank feature "
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 2.5 — "Kaynes Technology shares extend losses, fall another 4%; should investors worry about its "
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 0.7 — "Cochin Shipyard dividend 2026: Last day to buy today | Check record date, payout amount, h"

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