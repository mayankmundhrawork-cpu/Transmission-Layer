# Transmission Layer — board brief · 2026-09-21 21:58Z

data as of **2026-09-21** · 97 series · 12 red / 31 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.398, 2d in regime; vol-pct 0.17, breadth-off 0.625, Markov P(high-vol) 0.066)
- [INVERTED] **safe_haven_gold** — corr20 -0.46, corr60 -0.25, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.79, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.08, corr60 0.28, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.16, corr60 0.08, last shift 2026-06-05. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.8, corr60 -0.8, last shift 2026-07-22. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.07, corr60 -0.04, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.3, corr60 -0.08, last shift 2026-07-31. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.41, corr60 0.14, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** sp500 → asx_200: leads 1d (ccf 0.573, β 0.4418, p 0.0); driver zc 1.91 → expected 0.657%. Type hit-rate 0.815 (n=2191).
- **SETUP** dyn_vt → asx_200: leads 1d (ccf 0.57, β 0.4543, p 0.0); driver zc 1.83 → expected 0.673%. Type hit-rate 0.815 (n=2191).
- **SETUP** dyn_vt → aud_usd: leads 1d (ccf 0.56, β 0.3488, p 0.0); driver zc 1.83 → expected 0.517%. Type hit-rate 0.815 (n=2191).
- **SETUP** dyn_vt → usd_mxn: leads 1d (ccf -0.516, β -0.3045, p 0.0); driver zc 1.83 → expected -0.451%. Type hit-rate 0.815 (n=2191).
- **SETUP** dyn_vt → usd_brl: leads 1d (ccf -0.514, β -0.4109, p 0.0); driver zc 1.83 → expected -0.609%. Type hit-rate 0.815 (n=2191).
- **SETUP** sp500 → aud_usd: leads 1d (ccf 0.463, β 0.2792, p 0.0); driver zc 1.91 → expected 0.415%. Type hit-rate 0.815 (n=2191).
- **SETUP** nasdaq_100 → aud_usd: leads 1d (ccf 0.445, β 0.1981, p 0.0); driver zc 2.55 → expected 0.557%. Type hit-rate 0.815 (n=2191).
- **SETUP** sp500 → usd_brl: leads 1d (ccf -0.442, β -0.3422, p 0.0); driver zc 1.91 → expected -0.509%. Type hit-rate 0.815 (n=2191).
- **SETUP** sp500 → usd_mxn: leads 1d (ccf -0.434, β -0.2479, p 0.0); driver zc 1.91 → expected -0.369%. Type hit-rate 0.815 (n=2191).
- **SETUP** nasdaq_100 → usd_brl: leads 1d (ccf -0.421, β -0.24, p 0.0); driver zc 2.55 → expected -0.675%. Type hit-rate 0.815 (n=2191).
- **SETUP** nasdaq_100 → usd_mxn: leads 1d (ccf -0.419, β -0.1763, p 0.0); driver zc 2.55 → expected -0.496%. Type hit-rate 0.815 (n=2191).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.359, β -2.3385, p 0.0123); driver zc 1.83 → expected -3.466%. Type hit-rate 0.815 (n=2191).
- **SETUP** dyn_vt → gbp_usd: leads 1d (ccf 0.336, β 0.1499, p 1e-05); driver zc 1.83 → expected 0.222%. Type hit-rate 0.815 (n=2191).
- **SETUP** dyn_vt → nifty_metal: leads 1d (ccf 0.327, β 0.5155, p 4e-05); driver zc 1.83 → expected 0.764%. Type hit-rate 0.815 (n=2191).
- **SETUP** btc_usd → asx_200: leads 1d (ccf 0.304, β 0.0862, p 0.0); driver zc 2.28 → expected 0.607%. Type hit-rate 0.815 (n=2191).
- **SETUP** sp500 → nifty_metal: leads 1d (ccf 0.294, β 0.4535, p 0.00094); driver zc 1.91 → expected 0.674%. Type hit-rate 0.815 (n=2191).
- **SETUP** btc_usd → aud_usd: leads 1d (ccf 0.288, β 0.0636, p 0.0); driver zc 2.28 → expected 0.448%. Type hit-rate 0.815 (n=2191).
- **SETUP** dyn_vt → nifty_midcap_100: leads 1d (ccf 0.275, β 0.3382, p 0.0); driver zc 1.83 → expected 0.501%. Type hit-rate 0.815 (n=2191).
- **SETUP** btc_usd → usd_mxn: leads 1d (ccf -0.261, β -0.0575, p 1e-05); driver zc 2.28 → expected -0.405%. Type hit-rate 0.815 (n=2191).
- Track record · residual_reversion: hit-rate **0.5** (n=1091) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.815** (n=2191) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.41] cross-asset · 3 series ↑
- eth_usd [CRYPTO]: last 2771.45, z20 6.09, zc 1.44, resid-z 2.10 [unexplained], 1d 6.13%, |z20|=6.09
- btc_usd [CRYPTO]: last 86599.04, z20 5.61, zc 2.28, resid-z 2.96 [unexplained], 1d 7.04%, |z20|=5.61
- dyn_coin [EQUITIES]: last 200.95, z20 2.52, zc 0.75, resid-z 2.88 [unexplained], 1d 3.45%, |z20|=2.52
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 1.97).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cartrade_ns (rho 0.405 via eth_usd, z -1.47, reacted); midcap_largecap_ratio (rho 0.389 via dyn_coin, z 0.15, quiet)
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.573 vs btc_usd, historically leads by 1d
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.565 vs eth_usd
- **India receivers**: dyn_cartrade_ns (rho 0.405, z -1.47); midcap_largecap_ratio (rho 0.389, z 0.15)
- Source: Bitcoin hits an 8-month high — and sends a clear message about risk appetite right now — MarketWatch Top, 2026-09-21. https://www.marketwatch.com/story/bitcoin-hits-an-8-month-high-and-sends-a-clear-message-about-risk-appetite-right-now-edc7b9a5?mod=mw_rss_topstories
- Source: Bitcoin Tops $85,000 For First Time Since Late January — OilPrice, 2026-09-21. https://oilprice.com/Finance/the-Economy/Bitcoin-Tops-85000-For-First-Time-Since-Late-January.html
- Source: US Fed, Bank of Japan and others impact on Indian stock markets: Global rate hike cycle begins - Sensex, Nifty outlook — Mint Markets, 2026-09-21. https://www.livemint.com/market/stock-market-news/us-fed-bank-of-japan-and-others-impact-on-indian-stock-markets-global-rate-hike-cycle-begins-sensex-nifty-outlook-11789995507694.html
- Historical analogues: 2025-08-13 (d=1.97), 2025-05-08 (d=2.68), 2024-11-13 (d=3.29)

### [RED 8.99] cross-asset · 5 series ↑
- tips_10y_real [RATES]: last 2.68, z20 2.06, zc 1.47, resid-z 1.75 [unexplained], 1d 2.68%, 1d move +7.0bps ≥ 5bps; |z20|=2.06; 1y-pct=99
- ust_2y [RATES]: last 4.76, z20 1.96, zc 1.47, resid-z 1.50 [unexplained], 1d 1.93%, |z20|=1.96; 1y-pct=100
- ust_10y [RATES]: last 5.01, z20 1.71, zc 1.46, resid-z 1.48 [quiet], 1d 1.42%, |z20|=1.71; 1y-pct=99
- ust_30y [RATES]: last 5.34, z20 1.23, zc 1.23, resid-z 1.24 [quiet], 1d 0.95%, 1y-pct=98
- dyn_bond [EQUITIES]: last 88.98, z20 -0.99, zc 0.86, resid-z -0.08 [quiet], 1d 0.30%, 1y-pct=2
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.378 via ust_2y, z 0.15, quiet)
- Watch next: wti (co-move) — not yet - watch; rho 0.544 vs ust_10y, historically leads by 3d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.589 vs dyn_bond
- Watch next: brent (co-move) — not yet - watch; rho 0.579 vs ust_10y
- **India receivers**: midcap_largecap_ratio (rho -0.378, z 0.15)
- Source: US stocks: US market ends sharply higher as AI optimism reignites and Treasury yields retreat — ET Markets, 2026-09-21. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-us-market-ends-sharply-higher-as-ai-optimism-reignites-and-treasury-yields-retreat/articleshow/134397491.cms
- Source: Wall Street ends sharply higher as AI optimism reignites and Treasury yields retreat — Mint Markets, 2026-09-21. https://www.livemint.com/market/wall-street-ends-sharply-higher-as-ai-optimism-reignites-and-treasury-yields-retreat-11790020951511.html
- Source: Global Market: Euro area bond yields fall as oil prices ease — ET Markets, 2026-09-21. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-area-bond-yields-fall-as-oil-prices-ease/articleshow/134386398.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 8.24] indices · 2 series ↑
- nasdaq_100 [INDICES]: last 30477.86, z20 5.41, zc 2.55, resid-z 0.72 [priced], 1d 2.81%, |z20|=5.41; 1y-pct=98
- sp500 [INDICES]: last 7764.22, z20 2.20, zc 1.91, resid-z -0.11 [priced], 1d 1.49%, |z20|=2.20; 1y-pct=99
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.931 vs nasdaq_100
- Watch next: brent (inverse) — not yet - watch; rho -0.664 vs sp500, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.648 vs nasdaq_100, historically leads by 2d
- Watch next: wti (inverse) — not yet - watch; rho -0.543 vs nasdaq_100, historically leads by 2d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.581 vs nasdaq_100
- Source: As the S&P 500 nears a new record high, there are signs of weakness below the surface — MarketWatch Top, 2026-09-21. https://www.marketwatch.com/story/as-the-s-p-500-nears-a-new-record-high-there-are-cracks-below-the-surface-6df3e90d?mod=mw_rss_topstories
- Source: Wall Street ends sharply higher as AI optimism reignites and Treasury yields retreat — Mint Markets, 2026-09-21. https://www.livemint.com/market/wall-street-ends-sharply-higher-as-ai-optimism-reignites-and-treasury-yields-retreat-11790020951511.html
- Source: Wall Street rises as AI stocks shine, oil drops; Dow, S&P, Nasdaq up — BusinessLine Mkts, 2026-09-21. https://www.thehindubusinessline.com/markets/wall-street-rises-as-ai-stocks-shine-oil-drops-dow-sp-nasdaq-up/article71492647.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-07 (d=0.06), 2026-05-15 (d=0.07)

### [AMBER 6.12] commodities · 2 series ↓
- brent [COMMODITIES]: last 95.96, z20 -0.28, zc -3.14, resid-z -1.96 [unexplained], 1d -7.62%, 1-session move -7.62% ≥ 1.5%
- wti [COMMODITIES]: last 91.97, z20 -0.15, zc -2.97, resid-z -2.20 [unexplained], 1d -8.31%, 1-session move -8.31% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.61 vs brent, historically leads by 5d
- Watch next: dax (inverse) — not yet - watch; rho -0.567 vs brent, historically leads by 5d
- Watch next: cac_40 (inverse) — not yet - watch; rho -0.551 vs brent, historically leads by 5d
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.652 vs brent
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.603 vs brent
- Source: Where Is OPEC+? Riyadh and Moscow’s Silence Is Becoming Deafening — OilPrice, 2026-09-21. https://oilprice.com/Energy/Crude-Oil/Where-Is-OPEC-Riyadh-and-Moscows-Silence-Is-Becoming-Deafening.html
- Source: Oil Drops Below $100 as Iran Diplomacy, Hormuz Flows Stunt Rally — Mint Markets, 2026-09-21. https://www.livemint.com/market/oil-drops-below-100-as-iran-diplomacy-hormuz-flows-stunt-rally-11790015876956.html
- Source: Investors upbeat on hawkish Fed fighting inflation but remain wary of crude oil prices and AI risks — ET Markets, 2026-09-21. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/investors-upbeat-on-hawkish-fed-fighting-inflation-but-remain-wary-of-crude-oil-prices-and-ai-risks/articleshow/134395926.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-31 (d=0.05), 2025-04-29 (d=0.06)

### [RED 5.25] dxy ↑
- dxy [FX]: last 100.40, z20 2.25, zc 0.52, resid-z -0.11 [quiet], 1d 0.18%, 20d range extreme; |z20|=2.25
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [RED 5.21] gold_silver_ratio ↓
- gold_silver_ratio [DERIVED]: last 65.85, z20 -2.21, zc n/a, resid-z n/a [quiet], 1d -0.95%, GSR<75 (extreme low); |z20|=2.21
- **Mechanism**: gold_silver_ratio ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.375 via gold_silver_ratio, z -0.88, quiet)
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.859 vs gold_silver_ratio
- **India receivers**: nifty_midcap_100 (rho -0.375, z -0.88)
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

### [AMBER 5.16] fx · 2 series ↓
- eur_usd [FX]: last 1.15, z20 -2.33, zc -0.15, resid-z 0.35 [quiet], 1d -0.05%, |z20|=2.33
- gbp_usd [FX]: last 1.34, z20 -2.17, zc 0.27, resid-z 0.46 [quiet], 1d 0.11%, |z20|=2.17
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_icicigi_bo (rho -0.404 via gbp_usd, z -0.4, quiet)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.558 vs eur_usd, historically leads by 3d
- **India receivers**: dyn_icicigi_bo (rho -0.404, z -0.4)
- Source: Global Market: Euro area bond yields fall as oil prices ease — ET Markets, 2026-09-21. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-area-bond-yields-fall-as-oil-prices-ease/articleshow/134386398.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [RED 4.92] dyn_meta ↑
- dyn_meta [EQUITIES]: last 741.13, z20 2.92, zc 4.73, resid-z -0.98 [moved], 1d 11.32%, |z20|=2.92; 1y-pct=96
- **Mechanism**: dyn_meta ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_havells_ns (rho -0.377 via dyn_meta, z -1.08, reacted)
- **India receivers**: dyn_havells_ns (rho -0.377, z -1.08)
- Source: Meta’s stock is enjoying its best month in more than two years thanks to the company’s hot new AI assistant — MarketWatch Top, 2026-09-21. https://www.marketwatch.com/story/metas-stock-is-enjoying-its-best-month-in-more-than-two-years-thanks-to-the-companys-hot-new-ai-assistant-bf106291?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2024-10-21 (d=0.07)

## Watchlist (below surfacing floor)
dyn_4417_t ↑ (4.87), dyn_tatatech_ns ↓ (4.27), sofr ↑ (4.12), comex_copper ↑ (3.9), commodities · 3 series ↑ (3.65), ig_oas ↓ (3.27), dyn_tech ↑ (3.21), midcap_largecap_ratio ↑ (3.15), usd_cny ↓ (3.03), dyn_jiofin_bo ↓ (2.96), dyn_lenskart_ns ↑ (2.51), dyn_icicigi_bo ↓ (2.4)

## India macro
- nifty_50: 23429.0000 (1d 0.35%, z20 -0.94, flag none)
- nifty_midcap_100: 62047.9492 (1d -0.23%, z20 -0.88, flag none)
- usd_inr: 95.8050 (1d 0.01%, z20 0.97, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6483 (1d -0.58%, z20 0.15, flag amber)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 53.7 — "RUSSIA REROUTES GRAIN AS BLACK SEA EXPORTS STALL Russian firms are converting fertilizer a"
- INOXINDIA.NS (INOX INDIA LIMITED) score 51.0 — "India becomes Asia’s 4th-largest REIT market, overtakes Hong Kong: Cushman & Wakefield"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 49.9 — "India becomes Asia’s 4th-largest REIT market, overtakes Hong Kong: Cushman & Wakefield"
- INDIANB.NS (INDIAN BANK) score 45.6 — "Eurosystem brings central bank money to tokenised finance"
- BAC (Bank of America Corporation) score 43.4 — "America’s power grid is running out of juice — and these stocks stand to gain"
- COIN (Coinbase Global, Inc.) score 43.4 — "Global Market: Euro area bond yields fall as oil prices ease"
- HDB (HDFC Bank Limited) score 39.4 — "Eurosystem brings central bank money to tokenised finance"
- OHI (Omega Healthcare Investors, In) score 37.3 — "Top stocks in focus today: Investors must watch Pine Labs, Waaree Energies, GRSE shares on"
- IDBI.NS (IDBI BANK LIMITED) score 35.2 — "Eurosystem brings central bank money to tokenised finance"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 35.2 — "Eurosystem brings central bank money to tokenised finance"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 35.2 — "Eurosystem brings central bank money to tokenised finance"
- CHKP (Check Point Software Technolog) score 31.6 — "Emami share price jumps 4% ahead of buyback: What should investors do? Check stop loss, ta"
- LTH (Life Time Group Holdings, Inc.) score 27.6 — "SURGING FUEL PRICES COULD HIT U.S. INFLATION EXPECTATIONS U.S. diesel prices have surged t"
- BOND (PIMCO Active Bond Exchange-Tra) score 25.4 — "Global Market: Euro area bond yields fall as oil prices ease"
- SEPN (Septerna, Inc.) score 23.4 — "Stock Market prediction today: Sensex, Nifty outlook for Tue | Kospi, Taiwan Index, Nikkei"
- TECHM.NS (TECH MAHINDRA LIMITED) score 22.8 — "Top stocks to buy today: Eternal, NTPC Green, Kaynes Tech, Aavas, GESHIP by Sumeet Bagadia"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 22.8 — "Top stocks to buy today: Eternal, NTPC Green, Kaynes Tech, Aavas, GESHIP by Sumeet Bagadia"
- TECH (Bio-Techne Corp) score 22.8 — "Top stocks to buy today: Eternal, NTPC Green, Kaynes Tech, Aavas, GESHIP by Sumeet Bagadia"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 22.5 — "Tata Group stocks face fresh risk as Trusts-Sons row escalates: Which stock looks most att"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 22.5 — "Tata Group stocks face fresh risk as Trusts-Sons row escalates: Which stock looks most att"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 19.4 — "VENEZUELAN DELEGATION LED BY INTERIM PRESIDENT RODRIGUEZ TO DISCUSS ENERGY, DEBT AND MININ"
- 301077.SZ (CHINASTARS) score 18.5 — "US PROPOSED EXTENDING CHINA TRADE TRUCE BY SIX MONTHS: NYT *CHINA HAS PUSHED FOR A LONGER "
- BZ=F (Brent Crude Oil Last Day Finan) score 10.6 — "STOCKS OF CRUDE OIL IN US STRATEGIC PETROLEUM RESERVE FELL TO 284.6 MLN BARRELS LAST WEEK,"
- JIOFIN.BO (Jio Financial Services Limited) score 9.9 — "TSX gains powered by tech, financial stocks"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 9.4 — "SS Retail IPO allotment likely today: GMP signals 35% listing gain; here's how to check st"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 8.4 — "Xi Jinping US visit: Trump to weigh on rare-earth magnet | Experts bet high on Vedanta, GM"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.1 — "‘She says it’s just money’: My friend pays for everything. I should be grateful, but I can"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 6.4 — "ADIA sells 2.01% stake in Lenskart Solutions for ₹2,390 crore"
- VT (Vanguard Total World Stock Ind) score 6.0 — "UN Warns World Must Prepare for Life Beyond 1.5°C"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.3 — "Why Adani Total Gas lost 5%, Adani Ports fell 2% despite gains on Sensex, Nifty | Check ho"
- MS (Morgan Stanley) score 5.3 — "JP MORGAN EXPECTS ECB TO DELIVER ANOTHER 25 BP INTEREST RATE HIKE IN MARCH 2027 AFTER A DE"
- META (Meta) score 4.9 — "Meta’s stock is enjoying its best month in more than two years thanks to the company’s hot"
- PINELABS.NS (PINE LABS LIMITED) score 4.8 — "Top stocks in focus today: Investors must watch Pine Labs, Waaree Energies, GRSE shares on"
- NVDA (NVIDIA Corporation) score 4.4 — "NVDA - NVIDIA’S HUANG REJECTS CALLS TO SLOW AI Nvidia CEO Jensen Huang says AI development"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 4.1 — "Eurosystem brings central bank money to tokenised finance"
- GS (Goldman Sachs Group, Inc. (The) score 3.4 — "Consumer sentiment is in the dumps despite a solid economy. Goldman Sachs blames 'lower ha"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 2.7 — "ICICI Bank Share Price Live Updates: ICICI Bank's Current Market Position"
- VOLTAS.NS (VOLTAS LTD) score 0.4 — "Voltas among 7 stocks hitting 52-week low; slipped up to 10% in a month"
- DELL (Dell Technologies Inc.) score 0.2 — "Why Dell and HPE were the S&P 500’s top-performing stocks today"
- DKS (Dick's Sporting Goods Inc) score 0.0 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"

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