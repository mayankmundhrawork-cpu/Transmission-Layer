# Transmission Layer — board brief · 2026-09-22 09:17Z

data as of **2026-09-22** · 97 series · 14 red / 31 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.434, 3d in regime; vol-pct 0.14, breadth-off 0.727, Markov P(high-vol) 0.066)
- [INVERTED] **safe_haven_gold** — corr20 -0.5, corr60 -0.28, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.83, corr60 0.86, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.12, corr60 0.29, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.18, corr60 0.09, last shift 2026-08-10. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.8, corr60 -0.8, last shift 2026-07-22. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.06, corr60 -0.05, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.3, corr60 -0.08, last shift 2026-07-31. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.39, corr60 0.16, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** sp500 → asx_200: leads 1d (ccf 0.573, β 0.4407, p 0.0); driver zc 1.91 → expected 0.655%. Type hit-rate 0.818 (n=2097).
- **SETUP** dyn_vt → asx_200: leads 1d (ccf 0.57, β 0.4531, p 0.0); driver zc 1.83 → expected 0.672%. Type hit-rate 0.818 (n=2097).
- **SETUP** dyn_vt → aud_usd: leads 1d (ccf 0.558, β 0.3468, p 0.0); driver zc 1.83 → expected 0.514%. Type hit-rate 0.818 (n=2097).
- **SETUP** nasdaq_100 → taiwan_weighted: leads 1d (ccf 0.554, β 0.6392, p 0.0); driver zc 2.55 → expected 1.798%. Type hit-rate 0.818 (n=2097).
- **SETUP** dyn_vt → taiwan_weighted: leads 1d (ccf 0.542, β 0.8871, p 0.0); driver zc 1.83 → expected 1.315%. Type hit-rate 0.818 (n=2097).
- **SETUP** sp500 → taiwan_weighted: leads 1d (ccf 0.523, β 0.8341, p 0.0); driver zc 1.91 → expected 1.24%. Type hit-rate 0.818 (n=2097).
- **SETUP** dyn_vt → usd_mxn: leads 1d (ccf -0.514, β -0.3028, p 0.0); driver zc 1.83 → expected -0.449%. Type hit-rate 0.818 (n=2097).
- **SETUP** sp500 → aud_usd: leads 1d (ccf 0.461, β 0.2776, p 0.0); driver zc 1.91 → expected 0.413%. Type hit-rate 0.818 (n=2097).
- **SETUP** nasdaq_100 → aud_usd: leads 1d (ccf 0.442, β 0.1961, p 0.0); driver zc 2.55 → expected 0.551%. Type hit-rate 0.818 (n=2097).
- **SETUP** sp500 → usd_mxn: leads 1d (ccf -0.432, β -0.2464, p 0.0); driver zc 1.91 → expected -0.366%. Type hit-rate 0.818 (n=2097).
- **SETUP** nasdaq_100 → usd_mxn: leads 1d (ccf -0.415, β -0.1743, p 0.0); driver zc 2.55 → expected -0.49%. Type hit-rate 0.818 (n=2097).
- **SETUP** dyn_vt → kospi: leads 1d (ccf 0.413, β 0.9914, p 0.0); driver zc 1.83 → expected 1.469%. Type hit-rate 0.818 (n=2097).
- **SETUP** nasdaq_100 → kospi: leads 1d (ccf 0.408, β 0.7016, p 0.0); driver zc 2.55 → expected 1.973%. Type hit-rate 0.818 (n=2097).
- **SETUP** sp500 → kospi: leads 1d (ccf 0.36, β 0.8358, p 0.0); driver zc 1.91 → expected 1.242%. Type hit-rate 0.818 (n=2097).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.359, β -2.3293, p 0.01223); driver zc 1.83 → expected -3.452%. Type hit-rate 0.818 (n=2097).
- **SETUP** dyn_vt → gbp_usd: leads 1d (ccf 0.333, β 0.1484, p 1e-05); driver zc 1.83 → expected 0.22%. Type hit-rate 0.818 (n=2097).
- **SETUP** dyn_vt → nifty_metal: leads 1d (ccf 0.326, β 0.5126, p 4e-05); driver zc 1.83 → expected 0.76%. Type hit-rate 0.818 (n=2097).
- **SETUP** sp500 → nifty_metal: leads 1d (ccf 0.294, β 0.4512, p 0.00096); driver zc 1.91 → expected 0.671%. Type hit-rate 0.818 (n=2097).
- **SETUP** dyn_vt → nifty_midcap_100: leads 1d (ccf 0.274, β 0.3356, p 0.0); driver zc 1.83 → expected 0.497%. Type hit-rate 0.818 (n=2097).
- Track record · residual_reversion: hit-rate **0.5** (n=1093) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=2097) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.99] cross-asset · 5 series ↑
- tips_10y_real [RATES]: last 2.68, z20 2.06, zc 1.47, resid-z 1.75 [unexplained], 1d 2.68%, 1d move +7.0bps ≥ 5bps; |z20|=2.06; 1y-pct=99
- ust_2y [RATES]: last 4.76, z20 1.96, zc 1.47, resid-z 1.50 [unexplained], 1d 1.93%, |z20|=1.96; 1y-pct=100
- ust_10y [RATES]: last 5.01, z20 1.71, zc 1.46, resid-z 1.48 [quiet], 1d 1.42%, |z20|=1.71; 1y-pct=99
- ust_30y [RATES]: last 5.34, z20 1.23, zc 1.23, resid-z 1.24 [quiet], 1d 0.95%, 1y-pct=98
- dyn_bond [EQUITIES]: last 88.98, z20 -0.99, zc 0.86, resid-z -0.08 [quiet], 1d 0.30%, 1y-pct=2
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.378 via ust_2y, z 0.35, quiet)
- Watch next: brent (co-move) — not yet - watch; rho 0.613 vs ust_10y
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.574 vs dyn_bond
- Watch next: wti (co-move) — not yet - watch; rho 0.56 vs ust_10y
- **India receivers**: midcap_largecap_ratio (rho -0.378, z 0.35)
- Source: Global Market: Eurozone bond yields rise as oil prices rebound above $100 — ET Markets, 2026-09-22. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-eurozone-bond-yields-rise-as-oil-prices-rebound-above-100/articleshow/134407409.cms
- Source: South Korean pension fund seeks India government bond investment licence — BusinessLine Mkts, 2026-09-22. https://www.thehindubusinessline.com/markets/south-korean-pension-fund-seeks-india-government-bond-investment-licence/article71494318.ece
- Source: South Korean pension fund seeks India government bond investment licence: Report — ET Markets, 2026-09-22. https://economictimes.indiatimes.com/markets/bonds/south-korean-pension-fund-seeks-india-government-bond-investment-licence-report/articleshow/134404611.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 8.24] indices · 2 series ↑
- nasdaq_100 [INDICES]: last 30477.86, z20 5.41, zc 2.55, resid-z 0.72 [priced], 1d 2.81%, |z20|=5.41; 1y-pct=98
- sp500 [INDICES]: last 7764.22, z20 2.20, zc 1.91, resid-z -0.11 [priced], 1d 1.49%, |z20|=2.20; 1y-pct=99
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.928 vs nasdaq_100
- Watch next: vix (inverse) — not yet - watch; rho -0.653 vs nasdaq_100, historically leads by 2d
- Watch next: brent (inverse) — not yet - watch; rho -0.646 vs sp500, historically leads by 2d
- Watch next: wti (inverse) — not yet - watch; rho -0.624 vs sp500, historically leads by 2d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.565 vs nasdaq_100
- Source: US stock market rally explained: Why did Nasdaq climb 2% to close at a fresh record high? — ET Markets, 2026-09-22. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stock-market-rally-explained-why-did-nasdaq-climb-2-to-close-at-a-fresh-record-high/articleshow/134406348.cms
- Source: As the S&P 500 nears a new record high, there are signs of weakness below the surface — MarketWatch Top, 2026-09-21. https://www.marketwatch.com/story/as-the-s-p-500-nears-a-new-record-high-there-are-cracks-below-the-surface-6df3e90d?mod=mw_rss_topstories
- Source: Wall Street ends sharply higher as AI optimism reignites and Treasury yields retreat — Mint Markets, 2026-09-21. https://www.livemint.com/market/wall-street-ends-sharply-higher-as-ai-optimism-reignites-and-treasury-yields-retreat-11790020951511.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-07 (d=0.06), 2026-05-15 (d=0.07)

### [RED 7.02] natgas ↑
- natgas [COMMODITIES]: last 3.00, z20 2.02, zc 2.12, resid-z -0.39 [moved], 1d 5.71%, 1-session move +5.71% ≥ 5.0%; |z20|=2.02
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_lenskart_ns (rho 0.356 via natgas, z 1.08, reacted)
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.044 vs natgas, historically leads by 4d
- **India receivers**: dyn_lenskart_ns (rho 0.356, z 1.08)
- Source: Qatar’s LNG Loss Revives Projects From Argentina to Timor-Leste — OilPrice, 2026-09-22. https://oilprice.com/Energy/Natural-Gas/Qatars-LNG-Loss-Revives-Projects-From-Argentina-to-Timor-Leste.html
- Source: Hormuz Blockage Puts Qatar's $83 Billion LNG Bet at Risk — OilPrice, 2026-09-21. https://oilprice.com/Latest-Energy-News/World-News/Hormuz-Blockage-Puts-Qatars-83-Billion-LNG-Bet-at-Risk.html
- Source: Pakistan Secures Second Qatari LNG Cargo Through Hormuz After Iran Deal — OilPrice, 2026-09-21. https://oilprice.com/Latest-Energy-News/World-News/Pakistan-Secures-Second-Qatari-LNG-Cargo-Through-Hormuz-After-Iran-Deal.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [RED 6.39] cross-asset · 3 series ↑
- btc_usd [CRYPTO]: last 85879.92, z20 3.07, zc -0.21, resid-z 3.01 [unexplained], 1d -0.83%, |z20|=3.07
- eth_usd [CRYPTO]: last 2738.21, z20 3.04, zc -0.31, resid-z 2.21 [unexplained], 1d -1.38%, |z20|=3.04
- dyn_coin [EQUITIES]: last 200.95, z20 2.52, zc 0.75, resid-z 2.88 [unexplained], 1d 3.45%, |z20|=2.52
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.58).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cartrade_ns (rho 0.401 via eth_usd, z -1.39, reacted); midcap_largecap_ratio (rho 0.393 via dyn_coin, z 0.35, quiet)
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.541 vs btc_usd, historically leads by 1d
- **India receivers**: dyn_cartrade_ns (rho 0.401, z -1.39); midcap_largecap_ratio (rho 0.393, z 0.35)
- Source: Global Market: Eurozone bond yields rise as oil prices rebound above $100 — ET Markets, 2026-09-22. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-eurozone-bond-yields-rise-as-oil-prices-rebound-above-100/articleshow/134407409.cms
- Source: Sensex today | Stock Market Live Updates: Sensex falls 300 points, Nifty below 23,350 despite positive global cues — BusinessLine Mkts, 2026-09-22. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-22nd-september-2026/article71492546.ece
- Source: Iris Global Services files IPO papers with SEBI; eyes ₹200 crore via fresh issue — BusinessLine Mkts, 2026-09-22. https://www.thehindubusinessline.com/markets/iris-global-services-files-ipo-papers-with-sebi-eyes-200-crore-via-fresh-issue/article71494661.ece
- Historical analogues: 2025-08-13 (d=0.58), 2025-05-09 (d=1.48), 2024-11-21 (d=1.67)

### [AMBER 5.35] wti ↓
- wti [COMMODITIES]: last 91.10, z20 -0.35, zc -1.59, resid-z -0.91 [moved], 1d -4.89%, 1-session move -4.89% ≥ 1.5%
- **Mechanism**: wti ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.959 vs wti
- Watch next: dax (inverse) — not yet - watch; rho -0.531 vs wti, historically leads by 1d
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.63 vs wti
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.568 vs wti
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.565 vs wti
- Source: India’s Oil Import Bill Jumps 48% as Crude Prices Soar — OilPrice, 2026-09-22. https://oilprice.com/Latest-Energy-News/World-News/Indias-Oil-Import-Bill-Jumps-48-as-Crude-Prices-Soar.html
- Source: Global Market: Eurozone bond yields rise as oil prices rebound above $100 — ET Markets, 2026-09-22. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-eurozone-bond-yields-rise-as-oil-prices-rebound-above-100/articleshow/134407409.cms
- Source: Soaring Oil and Gas Prices Push Europe’s Inflation Fight Into 2027 — OilPrice, 2026-09-22. https://oilprice.com/Latest-Energy-News/World-News/Soaring-Oil-and-Gas-Prices-Push-Europes-Inflation-Fight-Into-2027.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

### [RED 5.1] dxy ↑
- dxy [FX]: last 100.49, z20 2.10, zc 0.19, resid-z -0.11 [quiet], 1d 0.06%, 20d range extreme; |z20|=2.10
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [AMBER 5.07] fx · 2 series ↓
- eur_usd [FX]: last 1.15, z20 -2.24, zc -0.59, resid-z -0.47 [quiet], 1d -0.18%, |z20|=2.24
- gbp_usd [FX]: last 1.34, z20 -2.15, zc -0.54, resid-z -0.59 [quiet], 1d -0.22%, |z20|=2.15
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_icicigi_bo (rho -0.408 via gbp_usd, z -0.5, quiet); nifty_50 (rho 0.357 via eur_usd, z -0.98, quiet)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.559 vs eur_usd, historically leads by 3d
- **India receivers**: dyn_icicigi_bo (rho -0.408, z -0.5); nifty_50 (rho 0.357, z -0.98)
- Source: Sterling and Wilson Renewable Energy shares rally 8% after securing Rs 985 crore domestic and global orders — ET Markets, 2026-09-22. https://economictimes.indiatimes.com/markets/stocks/news/sterling-and-wilson-renewable-energy-shares-rally-8-after-securing-rs-985-crore-domestic-and-global-orders/articleshow/134402652.cms
- Source: Global Market: Euro area bond yields fall as oil prices ease — ET Markets, 2026-09-21. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-area-bond-yields-fall-as-oil-prices-ease/articleshow/134386398.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [RED 4.92] dyn_meta ↑
- dyn_meta [EQUITIES]: last 741.13, z20 2.92, zc 4.73, resid-z -0.98 [moved], 1d 11.32%, |z20|=2.92; 1y-pct=96
- **Mechanism**: dyn_meta ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_havells_ns (rho -0.463 via dyn_meta, z -1.17, reacted)
- **India receivers**: dyn_havells_ns (rho -0.463, z -1.17)
- Source: Global AI trade roars back as Meta’s personal agent fuels optimism — ET Markets, 2026-09-22. https://economictimes.indiatimes.com/markets/us-stocks/news/global-ai-trade-roars-back-as-metas-personal-agent-fuels-optimism/articleshow/134401713.cms
- Source: AI trade roars back as Meta’s personal agent fuels optimism — BusinessLine Mkts, 2026-09-22. https://www.thehindubusinessline.com/markets/ai-trade-roars-back-as-metas-personal-agent-fuels-optimism/article71494034.ece
- Source: Meta’s stock is enjoying its best month in 13 years thanks to the company’s hot new AI assistant — MarketWatch Top, 2026-09-21. https://www.marketwatch.com/story/metas-stock-is-enjoying-its-best-month-in-more-than-two-years-thanks-to-the-companys-hot-new-ai-assistant-bf106291?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2024-10-21 (d=0.07)

## Watchlist (below surfacing floor)
dyn_4417_t ↑ (4.87), gold_silver_ratio ↓ (4.54), brent_wti_spread ↑ (4.22), dyn_tatatech_ns ↓ (4.17), sofr ↑ (4.12), comex_copper ↑ (4.12), midcap_largecap_ratio ↑ (3.35), ig_oas ↓ (3.27), dyn_tech ↑ (3.21), dyn_lenskart_ns ↑ (3.08), indices · 2 series ↑ (3.0), commodities · 2 series ↑ (2.7)

## India macro
- nifty_50: 23376.0996 (1d -0.16%, z20 -0.98, flag none)
- nifty_midcap_100: 61992.9492 (1d -0.09%, z20 -0.85, flag none)
- usd_inr: 95.7070 (1d -0.32%, z20 0.77, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6520 (1d 0.07%, z20 0.35, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 62.1 — "Sonaselection India IPO allotment likely today: Grey Market Premium and steps to check sta"
- INOXINDIA.NS (INOX INDIA LIMITED) score 59.6 — "Sonaselection India IPO allotment likely today: Grey Market Premium and steps to check sta"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 58.6 — "Sonaselection India IPO allotment likely today: Grey Market Premium and steps to check sta"
- COIN (Coinbase Global, Inc.) score 53.8 — "Sensex, Nifty set for steady opening amid positive global cues"
- INDIANB.NS (INDIAN BANK) score 45.9 — "Global Market: Bank of Korea signals data-driven approach to further rate hikes"
- BAC (Bank of America Corporation) score 42.9 — "Global Market: Bank of Korea signals data-driven approach to further rate hikes"
- HDB (HDFC Bank Limited) score 39.3 — "Global Market: Bank of Korea signals data-driven approach to further rate hikes"
- CHKP (Check Point Software Technolog) score 37.3 — "NSE IPO allotment today: Check status online by PAN number, GMP, listing share price predi"
- IDBI.NS (IDBI BANK LIMITED) score 35.5 — "Global Market: Bank of Korea signals data-driven approach to further rate hikes"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 35.5 — "Global Market: Bank of Korea signals data-driven approach to further rate hikes"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 35.5 — "Global Market: Bank of Korea signals data-driven approach to further rate hikes"
- OHI (Omega Healthcare Investors, In) score 35.5 — "Pine Labs block deal: Why Mastercard Asia-Pacific is selling its entire stake for  ₹890 cr"
- BOND (PIMCO Active Bond Exchange-Tra) score 29.7 — "India's first blue bond set for launch next week, official says"
- LTH (Life Time Group Holdings, Inc.) score 26.8 — "Sensex rises 110 points, Nifty above 23,450 as oil prices, bond yields cool down. Time for"
- TECHM.NS (TECH MAHINDRA LIMITED) score 23.5 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Current Trading Price"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 23.5 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Current Trading Price"
- TECH (Bio-Techne Corp) score 23.5 — "Tech Mahindra Share Price Live Updates: Tech Mahindra's Current Trading Price"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 23.2 — "Tata Group stocks see sharp swings as boardroom battle intensifies, but analysts say avoid"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 23.2 — "Tata Group stocks see sharp swings as boardroom battle intensifies, but analysts say avoid"
- SEPN (Septerna, Inc.) score 23.0 — "Nifty Prediction Today – September 22, 2026: Nifty 50 Futures: Bullish. Go long"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 18.4 — "Sterling and Wilson Renewable Energy shares rally 8% after securing Rs 985 crore domestic "
- 301077.SZ (CHINASTARS) score 17.6 — "Global Market: China stocks climb on AI boost, US-China talks in focus"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.4 — "Dividend countdown begins! Last chance to buy today GMDC, Titagarh Rail, AGI Infra, others"
- JIOFIN.BO (Jio Financial Services Limited) score 11.8 — "Oracle Financial among 4 F&O stocks with a sharp rise in futures open interest"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 9.6 — "Transrail Lighting shares surge 13% |  Is the pullback set to continue? Experts weigh in"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 9.4 — "NSE’s $2.4 billion IPO gets subdued demand from retail crowd"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.2 — "This stock just beat AI star HFCL’s 230% rally to top Nifty 500 gainers in 2026. Can outpe"
- META (Meta) score 9.2 — "AI trade roars back as Meta’s personal agent fuels optimism"
- PINELABS.NS (PINE LABS LIMITED) score 7.3 — "Pine Labs block deal: Why Mastercard Asia-Pacific is selling its entire stake for  ₹890 cr"
- VT (Vanguard Total World Stock Ind) score 6.3 — "U.S. Threatens to Ground Iranian Airlines Worldwide"
- MS (Morgan Stanley) score 5.8 — "Coal India share price climbs 3% after Morgan Stanley upgrades, raises target price"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 5.7 — "ADIA sells 2.01% stake in Lenskart Solutions for ₹2,390 crore"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 4.8 — "Why Adani Total Gas lost 5%, Adani Ports fell 2% despite gains on Sensex, Nifty | Check ho"
- GS (Goldman Sachs Group, Inc. (The) score 4.1 — "Goldman Sachs raises target on a stock that has already surged over 140% this year. Do you"
- NVDA (NVIDIA Corporation) score 3.9 — "NVDA - NVIDIA’S HUANG REJECTS CALLS TO SLOW AI Nvidia CEO Jensen Huang says AI development"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 3.7 — "Eurosystem brings central bank money to tokenised finance"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.4 — "Defence stock rallies 100% in 6 months! ICICI Direct sees 25% upside in Apollo Micro Syste"
- VOLTAS.NS (VOLTAS LTD) score 0.3 — "Voltas among 7 stocks hitting 52-week low; slipped up to 10% in a month"
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