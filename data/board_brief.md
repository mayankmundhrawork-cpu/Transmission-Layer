# Transmission Layer — board brief · 2026-10-01 23:53Z

data as of **2026-10-01** · 97 series · 18 red / 36 amber · 8 events surfaced (30 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.68, 6d in regime; vol-pct 0.694, breadth-off 0.667, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.49, corr60 -0.43, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.79, corr60 0.85, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.02, corr60 0.15, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.05, corr60 0.12, last shift 2026-08-18. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.78, corr60 -0.76, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.02, corr60 -0.11, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [VALID] **real_rates_gold_inverse** — corr20 -0.29, corr60 -0.25, last shift 2026-08-11. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.44, corr60 0.21, last shift 2026-07-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.0018708734390282533)
- **SETUP** dxy → usd_jpy: leads 1d (ccf 0.655, β 0.9339, p 0.0); driver zc 1.7 → expected 0.521%. Type hit-rate 0.826 (n=2310).
- **SETUP** dyn_hdb → usd_inr: leads 1d (ccf -0.358, β -0.0891, p 0.0); driver zc 1.62 → expected -0.241%. Type hit-rate 0.826 (n=2310).
- Track record · residual_reversion: hit-rate **0.5** (n=1129) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.826** (n=2310) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.25] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4207.40, z20 -1.63, zc 0.54, resid-z 0.22 [quiet], 1d 0.49%, |z20|=1.63; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 61.40, z20 -1.53, zc 1.16, resid-z 1.00 [quiet], 1d 2.17%, |z20|=1.53; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 68.52, z20 0.93, zc n/a, resid-z n/a [quiet], 1d -1.64%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.589 vs comex_silver, historically leads by 1d
- Watch next: dyn_coin (co-move) — not yet - watch; rho 0.5 vs comex_silver, historically leads by 5d
- Source: The hidden silver lining of high interest rates: safer, cheaper retirement income — MarketWatch Top, 2026-10-01. https://www.marketwatch.com/story/the-hidden-silver-lining-of-high-interest-rates-safer-cheaper-retirement-income-36e2e077?mod=mw_rss_topstories
- Source: Gold futures rise to ₹1.50 lakh/10 gm on firm spot demand — BusinessLine Mkts, 2026-10-01. https://www.thehindubusinessline.com/markets/gold/gold-futures-rise-to-150-lakh10-gm-on-firm-spot-demand/article71532369.ece
- Source: Today’s Gold Rate in India October 1: Gold prices down in Delhi, Mumbai, Kolkata, Chennai, Bengaluru — BusinessLine Mkts, 2026-10-01. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-delhi-mumbai-kolkata-chennai-bengaluru-hyderabad-pune-gold-rates-metro-cities-october-1-2026/article71531990.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.81] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.64, z20 2.88, zc 1.10, resid-z 0.74 [quiet], 1d 0.89%, |z20|=2.88; 1y-pct=100
- ust_10y [RATES]: last 5.29, z20 2.09, zc 0.55, resid-z 0.14 [quiet], 1d 0.57%, |z20|=2.09; 1y-pct=100
- dyn_bond [EQUITIES]: last 86.74, z20 -2.04, zc -0.75, resid-z 1.10 [quiet], 1d -0.29%, |z20|=2.04; 1y-pct=0
- tips_10y_real [RATES]: last 2.93, z20 1.96, zc 0.33, resid-z 0.02 [quiet], 1d 0.69%, |z20|=1.96; 1y-pct=100
- ust_2y [RATES]: last 4.88, z20 1.27, zc -0.15, resid-z -0.64 [quiet], 1d -0.20%, 1y-pct=99
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.648 vs ust_30y, historically leads by 3d
- Watch next: wti (co-move) — not yet - watch; rho 0.507 vs ust_10y, historically leads by 3d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.537 vs dyn_bond
- Source: Bond yields suddenly retreat from recent highs as buyers step back into the Treasury market — MarketWatch Top, 2026-10-01. https://www.marketwatch.com/story/bond-yields-suddenly-retreat-from-recent-highs-as-buyers-step-back-into-the-treasury-market-e3840e3d?mod=mw_rss_topstories
- Source: US stocks: US market rebounds to close higher as surging Treasury yields recede — ET Markets, 2026-10-01. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-us-market-rebounds-to-close-higher-as-surging-treasury-yields-recede/articleshow/134626994.cms
- Source: Equities turn higher as Treasury yields drop from highs — Mint Markets, 2026-10-01. https://www.livemint.com/market/equities-turn-higher-as-treasury-yields-drop-from-highs-11790880604226.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 6.73] indices · 2 series ↑
- nikkei_225 [INDICES]: last 68986.97, z20 3.89, zc 2.33, resid-z 1.32 [moved], 1d 3.35%, |z20|=3.89
- taiwan_weighted [INDICES]: last 48281.21, z20 1.69, zc 0.67, resid-z -0.10 [quiet], 1d 0.71%, |z20|=1.69; 1y-pct=100
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.7).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho -0.423 via taiwan_weighted, z -0.79, quiet); dyn_techm_ns (rho -0.415 via taiwan_weighted, z -0.73, quiet)
- Watch next: kospi (co-move) — not yet - watch; rho 0.815 vs nikkei_225
- **India receivers**: nifty_it (rho -0.423, z -0.79); dyn_techm_ns (rho -0.415, z -0.73)
- Source: Global Market: Japan’s Nikkei hits six-week high as chip stocks rally on AI optimism — ET Markets, 2026-10-01. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-hits-six-week-high-as-chip-stocks-rally-on-ai-optimism/articleshow/134609469.cms
- Source: Global Market: Japan’s Nikkei rises as AI stocks track US chip gains — ET Markets, 2026-09-30. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-rises-as-ai-stocks-track-us-chip-gains/articleshow/134581624.cms
- Historical analogues: 2025-12-30 (d=0.7), 2025-07-11 (d=0.77), 2026-06-09 (d=1.0)

### [RED 6.65] fx · 4 series ↓
- usd_mxn [FX]: last 18.32, z20 2.99, zc 1.94, resid-z 3.13 [unexplained], 1d 1.51%, |z20|=2.99
- eur_usd [FX]: last 1.12, z20 -2.59, zc -2.51, resid-z -2.56 [unexplained], 1d -0.80%, |z20|=2.59; 1y-pct=0
- aud_usd [FX]: last 0.69, z20 -2.56, zc -1.63, resid-z -2.29 [unexplained], 1d -0.84%, |z20|=2.56
- gbp_usd [FX]: last 1.32, z20 -1.77, zc -0.74, resid-z -0.72 [quiet], 1d -0.28%, |z20|=1.77
- **Mechanism**: fx · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.516 via usd_mxn, z -2.24, reacted); dyn_icicigi_bo (rho -0.504 via gbp_usd, z 1.68, reacted); dyn_muthootfin_ns (rho 0.478 via aud_usd, z -2.12, reacted); nifty_metal (rho 0.444 via aud_usd, z -2.95, reacted); nifty_midcap_100 (rho -0.423 via usd_mxn, z -2.52, reacted)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.556 vs eur_usd, historically leads by 3d
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.343 vs eur_usd, historically leads by 1d
- **India receivers**: dyn_policybzr_ns (rho -0.516, z -2.24); dyn_icicigi_bo (rho -0.504, z 1.68); dyn_muthootfin_ns (rho 0.478, z -2.12); nifty_metal (rho 0.444, z -2.95)
- Source: EURO EXTENDS LOSES AGAINST US DOLLAR, LAST DOWN 1% AT $1.12165 — DeItaone, 2026-10-01. https://t.me/walter_bloomberg/36495
- Source: UK pound falls to three-month lows as investors fret over rates, oil — ET Markets, 2026-10-01. https://economictimes.indiatimes.com/markets/us-stocks/news/uk-pound-falls-to-three-month-lows-as-investors-fret-over-rates-oil/articleshow/134621868.cms
- Source: EURO SLIDE CONTINUES; LAST DOWN 0.55% AT $1.127 — DeItaone, 2026-10-01. https://t.me/walter_bloomberg/36444
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 6.3] dyn_ohi ↓
- dyn_ohi [EQUITIES]: last 45.23, z20 -4.30, zc -1.83, resid-z -0.48 [moved], 1d -2.33%, |z20|=4.30
- **Mechanism**: dyn_ohi ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Hong Kong Investors Buying US Treasuries Is a No-Brainer — Mint Markets, 2026-10-01. https://www.livemint.com/market/hong-kong-investors-buying-us-treasuries-is-anobrainer-11790879988010.html
- Source: 50% of Nifty stocks slip into bear territory, down up to 40% - What should investors do now? Experts view — Mint Markets, 2026-10-01. https://www.livemint.com/market/stock-market-news/50-of-nifty-stocks-slip-into-bear-territory-down-up-to-40-what-should-investors-do-now-experts-view-11790873814742.html
- Source: ANTHROPIC TARGETS IPO BEFORE THANKSGIVING Anthropic is reportedly seeking to go public as soon as mid-November, with formal IPO marketing potentially starting the week of Nov. 9. Prospective investors see a potential valuation of roughly $1.8 trillion to $2 trillion. The Claude developer is still ex — DeItaone, 2026-10-01. https://t.me/walter_bloomberg/36501
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2025-04-02 (d=0.09)

### [RED 6.19] cross-asset · 4 series ↓
- nifty_50 [INDICES]: last 22421.95, z20 -2.53, zc -1.36, resid-z -1.32 [quiet], 1d -0.88%, |z20|=2.53; 1y-pct=0
- nifty_midcap_100 [INDICES]: last 58731.25, z20 -2.52, zc -1.06, resid-z -0.70 [quiet], 1d -1.00%, |z20|=2.52
- india_vix [INDICES]: last 14.44, z20 2.46, zc 1.19, resid-z n/a [quiet], 1d 7.01%, |z20|=2.46
- dyn_policybzr_ns [EQUITIES]: last 980.00, z20 -2.24, zc -1.16, resid-z -0.96 [quiet], 1d -7.89%, |z20|=2.24; 1y-pct=0
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.49).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.603 via nifty_midcap_100, z -1.57, reacted); nifty_fmcg (rho 0.589 via nifty_50, z -3.71, reacted); dyn_jiofin_bo (rho 0.588 via nifty_50, z -2.93, reacted); nifty_metal (rho 0.525 via nifty_midcap_100, z -2.95, reacted); dyn_indusindbk_bo (rho 0.485 via nifty_midcap_100, z -2.15, reacted)
- **India receivers**: midcap_largecap_ratio (rho 0.603, z -1.57); nifty_fmcg (rho 0.589, z -3.71); dyn_jiofin_bo (rho 0.588, z -2.93); nifty_metal (rho 0.525, z -2.95)
- Source: 50% of Nifty stocks slip into bear territory, down up to 40% - What should investors do now? Experts view — Mint Markets, 2026-10-01. https://www.livemint.com/market/stock-market-news/50-of-nifty-stocks-slip-into-bear-territory-down-up-to-40-what-should-investors-do-now-experts-view-11790873814742.html
- Source: Nifty IT crashes 11% in September: TCS, Infosys, Wipro among top losers — Can Q2 earnings spark a rebound? — Mint Markets, 2026-10-01. https://www.livemint.com/market/stock-market-news/nifty-it-crashes-11-in-september-tcs-infosys-wipro-among-top-losers-can-q2-earnings-spark-a-rebound-11790851695743.html
- Source: Market wrap: Infosys, HDFC Bank, Bajaj Auto, Maruti Suzuki among top gainers and losers on Nifty and Sensex on Thursday — ET Markets, 2026-10-01. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-infosys-hdfc-bank-bajaj-auto-maruti-suzuki-among-top-gainers-and-losers-on-nifty-and-sensex-on-thursday/articleshow/134617786.cms
- Historical analogues: 2025-07-21 (d=0.49), 2025-07-14 (d=0.72), 2025-12-30 (d=0.96)

### [AMBER 5.64] wti ↓
- wti [COMMODITIES]: last 92.99, z20 -0.64, zc 1.05, resid-z 1.57 [unexplained], 1d 2.84%, 1-session move +2.84% ≥ 1.5%
- **Mechanism**: wti ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.914 vs wti
- Watch next: sp500 (inverse) — not yet - watch; rho -0.563 vs wti
- Source: Oil Extends Gains as US Weighs Sending Carrier to Middle East — Mint Markets, 2026-10-01. https://www.livemint.com/market/oil-extends-gains-as-us-weighs-sending-carrier-to-middle-east-11790897581331.html
- Source: Venezuela’s Oil Exports Drop 9% as Freight Costs Bite — OilPrice, 2026-10-01. https://oilprice.com/Energy/Crude-Oil/Venezuelas-Oil-Exports-Drop-9-as-Freight-Costs-Bite.html
- Source: Middle East Oil Exports Stage a Remarkable Comeback — OilPrice, 2026-10-01. https://oilprice.com/Energy/Energy-General/Middle-East-Oil-Exports-Stage-a-Remarkable-Comeback.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

### [RED 5.52] indices · 4 series ↓
- ftse_100 [INDICES]: last 10432.33, z20 -3.86, zc -3.00, resid-z -2.70 [unexplained], 1d -1.64%, |z20|=3.86
- cac_40 [INDICES]: last 7847.96, z20 -3.26, zc -1.77, resid-z -2.17 [unexplained], 1d -1.46%, |z20|=3.26; 1y-pct=4
- stoxx_50 [INDICES]: last 6188.13, z20 -2.41, zc -1.56, resid-z -2.33 [unexplained], 1d -1.29%, |z20|=2.41
- dax [INDICES]: last 24981.34, z20 -2.25, zc -1.04, resid-z -1.23 [quiet], 1d -0.86%, |z20|=2.25
- **Mechanism**: indices · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.416 via ftse_100, z -2.15, reacted); nifty_fmcg (rho 0.369 via ftse_100, z -3.71, reacted)
- Watch next: sp500 (co-move) — not yet - watch; rho 0.642 vs stoxx_50, historically leads by 5d
- Watch next: vix (inverse) — not yet - watch; rho -0.555 vs stoxx_50, historically leads by 5d
- Watch next: wti (inverse) — not yet - watch; rho -0.553 vs stoxx_50, historically leads by 4d
- Watch next: brent (inverse) — not yet - watch; rho -0.528 vs stoxx_50
- **India receivers**: dyn_indusindbk_bo (rho 0.416, z -2.15); nifty_fmcg (rho 0.369, z -3.71)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-16 (d=0.34), 2024-11-21 (d=0.62)

## Watchlist (below surfacing floor)
commodities · 3 series ↓ (5.23), dxy ↑ (5.1), dyn_jiofin_bo ↓ (4.93), dyn_stylebaaza_ns ↓ (4.11), rates · 2 series ↑ (3.97), nifty_fmcg ↓ (3.71), dow_jones ↓ (3.61), nasdaq_100 ↑ (3.21), dyn_4417_t ↑ (3.1), nifty_metal ↓ (2.95), dyn_voltas_ns ↓ (2.95), dyn_tech ↑ (2.28)

## India macro
- nifty_50: 22421.9492 (1d -0.88%, z20 -2.53, flag red)
- nifty_midcap_100: 58731.2500 (1d -1.00%, z20 -2.52, flag red)
- usd_inr: 95.9271 (1d -0.13%, z20 0.75, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6194 (1d -0.12%, z20 -1.57, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 97.8 — "Small-cap dividend gems: 9 stocks with up to 16% yield - Premco, PTC India, Honda Power to"
- COALINDIA.NS (COAL INDIA LTD) score 92.8 — "Small-cap dividend gems: 9 stocks with up to 16% yield - Premco, PTC India, Honda Power to"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 91.2 — "Small-cap dividend gems: 9 stocks with up to 16% yield - Premco, PTC India, Honda Power to"
- INDIANB.NS (INDIAN BANK) score 69.5 — "FED'S JEFFERSON SAYS US CENTRAL BANK 'MAY TAKE MORE TIME' TO DECIDE NEXT RATE MOVE"
- BOND (PIMCO Active Bond Exchange-Tra) score 61.0 — "Bond yields suddenly retreat from recent highs as buyers step back into the Treasury marke"
- COIN (Coinbase Global, Inc.) score 55.6 — "China Halts October Fuel Exports as Global Diesel Crunch Deepens"
- OHI (Omega Healthcare Investors, In) score 51.4 — "ANTHROPIC TARGETS IPO BEFORE THANKSGIVING Anthropic is reportedly seeking to go public as "
- BAC (Bank of America Corporation) score 48.7 — "FED'S JEFFERSON SAYS US CENTRAL BANK 'MAY TAKE MORE TIME' TO DECIDE NEXT RATE MOVE"
- TECHM.NS (TECH MAHINDRA LIMITED) score 48.2 — "U.S. LAYOFF PLANS FALL SHARPLY IN SEPTEMBER U.S. employers announced 43,281 job cuts in Se"
- HDB (HDFC Bank Limited) score 48.0 — "FED'S JEFFERSON SAYS US CENTRAL BANK 'MAY TAKE MORE TIME' TO DECIDE NEXT RATE MOVE"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 44.5 — "U.S. LAYOFF PLANS FALL SHARPLY IN SEPTEMBER U.S. employers announced 43,281 job cuts in Se"
- TECH (Bio-Techne Corp) score 44.5 — "U.S. LAYOFF PLANS FALL SHARPLY IN SEPTEMBER U.S. employers announced 43,281 job cuts in Se"
- IDBI.NS (IDBI BANK LIMITED) score 43.9 — "FED'S JEFFERSON SAYS US CENTRAL BANK 'MAY TAKE MORE TIME' TO DECIDE NEXT RATE MOVE"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 43.9 — "FED'S JEFFERSON SAYS US CENTRAL BANK 'MAY TAKE MORE TIME' TO DECIDE NEXT RATE MOVE"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 43.9 — "FED'S JEFFERSON SAYS US CENTRAL BANK 'MAY TAKE MORE TIME' TO DECIDE NEXT RATE MOVE"
- SEPN (Septerna, Inc.) score 40.7 — "TWO-YEAR U.S. TREASURY YIELDS BRIEFLY HIT LOWEST LEVEL SINCE SEPTEMBER 22, LAST DOWN 12.68"
- CHKP (Check Point Software Technolog) score 39.5 — "Small-cap dividend gems: 9 stocks with up to 16% yield - Premco, PTC India, Honda Power to"
- LTH (Life Time Group Holdings, Inc.) score 37.3 — "FED’S JEFFERSON SIGNALS PATIENCE ON NEXT RATE MOVE Fed Vice Chair Jefferson says the Fed “"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 34.8 — "JEFFERSON SAYS FED MAY NEED ‘MORE TIME’ TO DECIDE ON NEXT MOVE *JEFFERSON: INFLATION RISKS"
- TGT (Target Corporation) score 28.8 — "ANTHROPIC SAID TO TARGET MEGA-IPO BEFORE THANKSGIVING HOLIDAY"
- 301077.SZ (CHINASTARS) score 27.5 — "OIL FUTURES EXTEND GAINS , BRENT LAST UP 4.6%, WTI UP 2.8% AFTER CHINA SUSPENDS OIL EXPORT"
- BZ=F (Brent Crude Oil Last Day Finan) score 21.6 — "EURO EXTENDS LOSES AGAINST US DOLLAR, LAST DOWN 1% AT $1.12165"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 19.3 — "Azad Engineering share price: Up 86% in 6 months! Is more steam left in this defence stock"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 14.6 — "Power stocks fall despite  ₹1.86 lakh crore PM-DHARA scheme: Tata Power, Adani Power, NTPC"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 14.6 — "Power stocks fall despite  ₹1.86 lakh crore PM-DHARA scheme: Tata Power, Adani Power, NTPC"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 14.0 — "Adani Group has Rs 2.6 lakh crore projects completed or under execution in Maharashtra: Pr"
- JIOFIN.BO (Jio Financial Services Limited) score 13.3 — "Financial stocks are falling below a key chart level to warn the worst is yet to come"
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.6 — "AUGUST JOBS STRENGTH MAY HAVE BEEN OVERSTATED August payroll growth of 162K was boosted by"
- POLICYBZR.NS (PB FINTECH LIMITED) score 10.3 — "PB Fintech shares crash 48% in 6 sessions; stock back to IPO price - Should investors chan"
- GS (Goldman Sachs Group, Inc. (The) score 9.9 — "GOLDMAN REFRESHES TOP U.S. STOCK PICKS Goldman Sachs added Amazon ($AMZN), Burlington Stor"
- VT (Vanguard Total World Stock Ind) score 9.3 — "Jio Platforms IPO in final stages after concluding worldwide roadshows"
- META (Meta) score 8.1 — "Gold price future roadmap: What led to 6% yellow metal fall in Sept 2026? Will Diwali help"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.3 — "Macquarie stock recommendations: ICICI Bank, SBI, PayTM to LIC — top 11 financial shares t"
- JEF (Jefferies Financial Group Inc.) score 6.2 — "Jefferies is bearish TCS, Wipro, 6 other IT stocks ahead of Q2 results. How many do you ow"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 6.0 — "FPIs pull out  ₹36,000 cr from Indian equities in Sept as high oil, bond yields weigh — sh"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 5.6 — "HSBC: INVESTORS ROTATING OUT OF FRANCE INTO UK HSBC says European equity funds are shiftin"
- NVDA (NVIDIA Corporation) score 5.5 — "NVIDIA'S HUANG: WE'RE GOING TO ADVANCE THIS RESPONSIBLY AND SAFELY"
- MS (Morgan Stanley) score 4.1 — "Morgan Stanley raises Lenskart target price to Rs 718; bull case implies 41% upside. Here’"
- VOLTAS.NS (VOLTAS LTD) score 0.3 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 0.2 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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