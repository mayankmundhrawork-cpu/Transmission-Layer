# Transmission Layer — board brief · 2026-08-17 20:41Z

data as of **2026-08-17** · 98 series · 8 red / 40 amber · 8 events surfaced (21 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.149, 1d in regime; vol-pct 0.235, breadth-off 0.062, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.33, corr60 -0.38, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.87, corr60 0.86, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.26, corr60 0.34, last shift 2026-07-01. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.23, corr60 -0.11, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.72, corr60 -0.82, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.12, corr60 -0.11, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.19, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.04, corr60 0.23, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.0011952969958688442)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.49** (n=1117) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.829** (n=2423) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.97] cross-asset · 12 series ↑
- comex_gold [COMMODITIES]: last 4471.50, z20 2.07, zc 1.61, resid-z -0.31 [priced], 1d 2.08%, |z20|=2.07; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 65.93, z20 1.76, zc 0.64, resid-z -1.01 [quiet], 1d 1.44%, |z20|=1.76; co-occur[gold_silver] same-direction (channel VALID)
- russell_2000 [INDICES]: last 3057.58, z20 1.50, zc -0.30, resid-z 0.45 [quiet], 1d -0.35%, 1y-pct=99
- dyn_nvda [EQUITIES]: last 225.05, z20 1.37, zc -0.02, resid-z 0.09 [quiet], 1d -0.05%, 1y-pct=98
- dyn_vt [EQUITIES]: last 161.83, z20 1.26, zc -0.34, resid-z 0.26 [quiet], 1d -0.26%, 1y-pct=99
- stoxx_50 [INDICES]: last 6538.73, z20 1.16, zc -0.02, resid-z 0.45 [quiet], 1d -0.01%, 1y-pct=98
- dax [INDICES]: last 26370.39, z20 1.12, zc -0.36, resid-z -0.04 [quiet], 1d -0.26%, 1y-pct=99
- sp500 [INDICES]: last 7746.14, z20 1.02, zc -0.66, resid-z -0.50 [quiet], 1d -0.51%, 1y-pct=98
- gold_silver_ratio [DERIVED]: last 67.83, z20 -0.99, zc n/a, resid-z n/a [quiet], 1d 0.63%, GSR<75 (extreme low)
- comex_copper [COMMODITIES]: last 6.61, z20 0.89, zc 0.07, resid-z 0.40 [quiet], 1d 0.17%, 1y-pct=97
- dow_jones [INDICES]: last 53466.68, z20 0.51, zc -0.70, resid-z -0.08 [quiet], 1d -0.49%, 1y-pct=96
- cac_40 [INDICES]: last 8585.62, z20 0.30, zc -0.82, resid-z -0.40 [quiet], 1d -0.59%, 1y-pct=95
- **Mechanism**: cross-asset · 12 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-11-26 (z-distance 0.94).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.514 via comex_silver, z 0.93, quiet); nifty_midcap_100 (rho 0.491 via dax, z 1.0, reacted); nifty_50 (rho 0.489 via cac_40, z -0.13, quiet); dyn_stylebaaza_ns (rho -0.359 via gold_silver_ratio, z 2.57, reacted)
- Watch next: brent (inverse) — not yet - watch; rho -0.644 vs dow_jones, historically leads by 3d
- Watch next: wti (inverse) — not yet - watch; rho -0.607 vs dow_jones, historically leads by 2d
- Watch next: ust_10y (inverse) — not yet - watch; rho -0.606 vs russell_2000, historically leads by 1d
- Watch next: tips_10y_real (inverse) — not yet - watch; rho -0.573 vs russell_2000, historically leads by 5d
- Watch next: btc_usd (co-move) — not yet - watch; rho 0.554 vs comex_gold, historically leads by 5d
- **India receivers**: nifty_metal (rho 0.514, z 0.93); nifty_midcap_100 (rho 0.491, z 1.0); nifty_50 (rho 0.489, z -0.13); dyn_stylebaaza_ns (rho -0.359, z 2.57)
- Source: SpaceX’s stock is rising, and that’s a good sign for Nvidia and Google — MarketWatch Top, 2026-08-17. https://www.marketwatch.com/story/spacexs-stock-is-rising-and-thats-a-good-sign-for-nvidia-and-google-913ce9de?mod=mw_rss_topstories
- Source: Gold appears set for a rebound as it regains safe-haven appeal after US-Iran war selloff — ET Markets, 2026-08-17. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/gold-appears-set-for-a-rebound-as-it-regains-safe-haven-appeal-after-us-iran-war-selloff/articleshow/133305922.cms
- Source: Wall Street indexes slip with Iran, retail results in focus — Mint Markets, 2026-08-17. https://www.livemint.com/market/wall-street-indexes-slip-with-iran-retail-results-in-focus-11786993198786.html
- Historical analogues: 2024-11-26 (d=0.94), 2025-10-31 (d=1.04), 2024-10-15 (d=1.15)

### [AMBER 6.41] commodities · 2 series ↑
- wti [COMMODITIES]: last 84.88, z20 0.58, zc 1.10, resid-z 0.68 [quiet], 1d 3.01%, 1-session move +3.01% ≥ 1.5%
- brent [COMMODITIES]: last 91.01, z20 0.55, zc 1.07, resid-z 0.60 [quiet], 1d 2.81%, 1-session move +2.81% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.415 via wti, z 1.0, reacted); dyn_bharatcoal_ns (rho -0.371 via wti, z -1.1, reacted)
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.607 vs wti
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.517 vs wti
- Watch next: cac_40 (inverse) — not yet - watch; rho -0.51 vs brent
- **India receivers**: nifty_midcap_100 (rho -0.415, z 1.0); dyn_bharatcoal_ns (rho -0.371, z -1.1)
- Source: US stocks: US market slips as oil prices rise, retail results awaited — ET Markets, 2026-08-17. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-us-market-slips-as-oil-prices-rise-retail-results-awaited/articleshow/133306298.cms
- Source: Trump: We're taking out millions of barrels of oil a week from the strait of Hormuz, it is open — DeItaone, 2026-08-17. https://t.me/walter_bloomberg/34817
- Source: Chevron Strikes Oil and Gas Offshore Angola in Major Discovery — OilPrice, 2026-08-17. https://oilprice.com/Latest-Energy-News/World-News/Chevron-Strikes-Oil-and-Gas-Offshore-Angola-in-Major-Discovery.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [AMBER 6.1] fx · 4 series ↑
- aud_usd [FX]: last 0.71, z20 2.44, zc 1.37, resid-z 1.26 [quiet], 1d 0.60%, |z20|=2.44
- usd_mxn [FX]: last 17.03, z20 -1.80, zc 0.02, resid-z 0.04 [quiet], 1d 0.01%, |z20|=1.80; 1y-pct=0
- gbp_usd [FX]: last 1.35, z20 1.67, zc 0.94, resid-z 0.87 [quiet], 1d 0.39%, |z20|=1.67
- eur_usd [FX]: last 1.16, z20 1.51, zc 1.19, resid-z 1.12 [quiet], 1d 0.39%, |z20|=1.51
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.547 via usd_mxn, z -0.87, quiet); eur_inr (rho 0.477 via gbp_usd, z 2.98, reacted); dyn_icicigi_bo (rho -0.423 via gbp_usd, z -0.43, quiet); nifty_midcap_100 (rho -0.355 via usd_mxn, z 1.0, reacted)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.508 vs aud_usd, historically leads by 5d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.504 vs eur_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.547, z -0.87); eur_inr (rho 0.477, z 2.98); dyn_icicigi_bo (rho -0.423, z -0.43); nifty_midcap_100 (rho -0.355, z 1.0)
- Source: Global Market: Euro zone bond yields hover near 15-year highs as Middle East war fuels inflation fears — ET Markets, 2026-08-17. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-bond-yields-hover-near-15-year-highs-as-middle-east-war-fuels-inflation-fears/articleshow/133293555.cms
- Source: Philip R. Lane: The rise in defence spending and the euro area economy — ECB press, 2026-08-17. https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260817~1f9f7149c9.en.pdf
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 5.71] commodities · 3 series ↑
- corn [COMMODITIES]: last 489.00, z20 4.39, zc 5.10, resid-z 3.98 [unexplained], 1d 6.54%, |z20|=4.39; 1y-pct=100
- wheat [COMMODITIES]: last 689.25, z20 1.50, zc 1.11, resid-z 0.82 [quiet], 1d 2.15%, |z20|=1.50; 1y-pct=99
- soybeans [COMMODITIES]: last 1216.00, z20 0.95, zc 3.55, resid-z 3.24 [unexplained], 1d 3.60%, 1y-pct=98
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_lenskart_ns (rho 0.387 via wheat, z 2.27, reacted)
- **India receivers**: dyn_lenskart_ns (rho 0.387, z 2.27)
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [RED 5.12] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.63, z20 2.12, zc n/a, resid-z n/a [quiet], 1d 0.37%, 52-wk extreme (pct=99); |z20|=2.12; 1y-pct=99
- **Mechanism**: The midcap_largecap_ratio has reached a 52-week extreme, with a z20 level of 1.77, indicating a significant move. However, the resid_z is None, suggesting that this move is largely priced in by factor exposures. The RISK_ON regime and VALID vix_equity_inverse channel suggest that the market is positioned for a potential drawdown, but the midcap_largecap_ratio's move may not be an anomaly.
- **Gap**: No gap: the midcap_largecap_ratio's move is largely priced in by factor exposures, as indicated by the None resid_z value
- **India take**: The Nifty Midcap 100 index, which has a correlation of 0.531 with the midcap_largecap_ratio, has not yet reacted and is a potential responder. Other Indian transmission candidates like Dyn Bharatcoal NS and Dyn Fincables NS have already reacted.
- Watch next: nifty_midcap_100 (down) — not yet - watch; historically leads by 2d
- **India receivers**: nifty_midcap_100 (rho 0.533, z 1.0); dyn_bharatcoal_ns (rho 0.42, z -1.1); dyn_fincables_ns (rho 0.408, z 2.68); dyn_pcjeweller_ns (rho 0.374, z 0.66)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [AMBER 4.58] cross-asset · 3 series ↑
- ust_30y [RATES]: last 5.25, z20 1.26, zc 0.98, resid-z 0.73 [quiet], 1d 0.77%, 1y-pct=99
- dyn_bond [EQUITIES]: last 90.43, z20 -1.26, zc -0.71, resid-z -0.48 [quiet], 1d -0.22%, 1y-pct=1
- ust_10y [RATES]: last 4.68, z20 0.39, zc 1.08, resid-z 1.15 [quiet], 1d 1.08%, 1y-pct=96
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: tips_10y_real (co-move) — not yet - watch; rho 0.689 vs ust_30y, historically leads by 1d
- Watch next: brent (co-move) — not yet - watch; rho 0.543 vs ust_30y, historically leads by 3d
- Watch next: wti (co-move) — not yet - watch; rho 0.501 vs ust_30y, historically leads by 3d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.532 vs ust_30y
- Source: US 30-YEAR YIELD HITS 2007 HIGH The 30-year Treasury yield climbed to 5.29%, its highest since 2007, as investors worry about rising U.S. debt, heavy bond issuance and persistent inflation. AI-related corporate borrowing and weaker demand for long-term bonds are adding — DeItaone, 2026-08-17. https://t.me/walter_bloomberg/34813
- Source: Yes Bank eyes dollar bond market after six-year hiatus, arrangers appointed: Why now? — Mint Markets, 2026-08-17. https://www.livemint.com/market/stock-market-news/yes-bank-eyes-dollar-bond-market-after-six-year-hiatus-arrangers-appointed-why-now-11786981933063.html
- Source: CITADEL: FED POLICY KEEPING TREASURY YIELDS HIGH Citadel Securities says the Fed’s policy approach is helping keep long-term Treasury yields near multi-decade highs, creating broader market risks. The 30-year yield topped 5.28%, its highest in 19 years, despite softer inflation — DeItaone, 2026-08-17. https://t.me/walter_bloomberg/34808
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.12), 2025-04-23 (d=0.18)

### [RED 4.57] dyn_stylebaaza_ns ↑
- dyn_stylebaaza_ns [EQUITIES]: last 383.50, z20 2.57, zc 1.37, resid-z 1.73 [unexplained], 1d 5.00%, |z20|=2.57
- **Mechanism**: dyn_stylebaaza_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_pcjeweller_ns (rho 0.439 via dyn_stylebaaza_ns, z 0.66, quiet); dyn_bharatcoal_ns (rho 0.402 via dyn_stylebaaza_ns, z -1.1, reacted); dyn_adanient_bo (rho 0.392 via dyn_stylebaaza_ns, z -0.53, quiet); dyn_fincables_ns (rho 0.376 via dyn_stylebaaza_ns, z 2.68, reacted); nifty_midcap_100 (rho 0.362 via dyn_stylebaaza_ns, z 1.0, reacted)
- **India receivers**: dyn_pcjeweller_ns (rho 0.439, z 0.66); dyn_bharatcoal_ns (rho 0.402, z -1.1); dyn_adanient_bo (rho 0.392, z -0.53); dyn_fincables_ns (rho 0.376, z 2.68)
- Source: US stocks: US market slips as oil prices rise, retail results awaited — ET Markets, 2026-08-17. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-us-market-slips-as-oil-prices-rise-retail-results-awaited/articleshow/133306298.cms
- Source: Wall Street indexes slip with Iran, retail results in focus — Mint Markets, 2026-08-17. https://www.livemint.com/market/wall-street-indexes-slip-with-iran-retail-results-in-focus-11786993198786.html
- Source: FCNR(B) inflows stabilise rupee but fail to trigger 2013-style rally — BusinessLine Mkts, 2026-08-17. https://www.thehindubusinessline.com/markets/forex/fcnrb-inflows-stabilise-rupee-but-fail-to-trigger-2013-style-rally/article71356433.ece
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-04 (d=0.01), 2025-02-20 (d=0.02)

### [AMBER 4.15] dxy ↓
- dxy [FX]: last 99.59, z20 -1.15, zc -0.23, resid-z -1.32 [quiet], 1d -0.08%, 20d range extreme
- **Mechanism**: dxy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eth_usd (inverse) — not yet - watch; rho -0.503 vs dxy
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

## Watchlist (below surfacing floor)
dyn_tech ↑ (3.73), dyn_lth ↑ (3.24), dyn_bac ↑ (3.09), dyn_tatatech_ns ↑ (3.01), eur_inr ↑ (2.98), indices · 2 series ↑ (2.95), nifty_fmcg ↓ (2.91), dyn_fincables_ns ↑ (2.68), dyn_icicigi_bo ↓ (2.43), indices · 2 series ↑ (2.37), dyn_lenskart_ns ↑ (2.27), usd_brl ↑ (2.22)

## India macro
- nifty_50: 24287.6504 (1d -0.32%, z20 -0.13, flag none)
- nifty_midcap_100: 63814.1484 (1d 0.05%, z20 1.00, flag amber)
- usd_inr: 95.5920 (1d 0.20%, z20 -0.28, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6274 (1d 0.37%, z20 2.12, flag red)
- Next India prints: NSDL FPI flows T-0d · India trade / CAD data T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 85.5 — "Russia Receives First Gasoline Cargo From India as Fuel Shortages Spread"
- INOXINDIA.NS (INOX INDIA LIMITED) score 85.0 — "Russia Receives First Gasoline Cargo From India as Fuel Shortages Spread"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 84.9 — "Russia Receives First Gasoline Cargo From India as Fuel Shortages Spread"
- INDIANB.NS (INDIAN BANK) score 55.4 — "Yes Bank eyes dollar bond market after six-year hiatus, arrangers appointed: Why now?"
- TECHM.NS (TECH MAHINDRA LIMITED) score 42.7 — "S&P 500 REVENUE GROWTH HITS 5-YEAR HIGH Goldman Sachs says S&P 500 revenues grew 6.4% YoY "
- BAC (Bank of America Corporation) score 41.4 — "TRUMP APPROVAL FALLS TO PRESIDENCY LOW President Trump’s approval rating fell to 33%, the "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 41.3 — "S&P 500 REVENUE GROWTH HITS 5-YEAR HIGH Goldman Sachs says S&P 500 revenues grew 6.4% YoY "
- TECH (Bio-Techne Corp) score 41.0 — "S&P 500 REVENUE GROWTH HITS 5-YEAR HIGH Goldman Sachs says S&P 500 revenues grew 6.4% YoY "
- OHI (Omega Healthcare Investors, In) score 39.6 — "US 30-YEAR YIELD HITS 2007 HIGH The 30-year Treasury yield climbed to 5.29%, its highest s"
- COIN (Coinbase Global, Inc.) score 38.1 — "GLOBAL DEBT ISSUANCE DROPS 16% Global debt issuance fell 16% YoY last week, according to G"
- HDB (HDFC Bank Limited) score 34.3 — "Yes Bank eyes dollar bond market after six-year hiatus, arrangers appointed: Why now?"
- CHKP (Check Point Software Technolog) score 33.0 — "Horizon Industrial Parks’ Rs 2,600 crore IPO opens. Check GMP, price band and other key de"
- IDBI.NS (IDBI BANK LIMITED) score 32.2 — "Yes Bank eyes dollar bond market after six-year hiatus, arrangers appointed: Why now?"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 32.2 — "Yes Bank eyes dollar bond market after six-year hiatus, arrangers appointed: Why now?"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 32.2 — "Yes Bank eyes dollar bond market after six-year hiatus, arrangers appointed: Why now?"
- LTH (Life Time Group Holdings, Inc.) score 28.0 — "NKE - NIKE SINKS TO 12-YEAR LOW Nike fell 3.2% to $39.42, putting shares on track for thei"
- BOND (PIMCO Active Bond Exchange-Tra) score 26.5 — "US 30-YEAR YIELD HITS 2007 HIGH The 30-year Treasury yield climbed to 5.29%, its highest s"
- 301077.SZ (CHINASTARS) score 25.2 — "China’s Xi praises former president Jiang Zemin’s contribution in show of party unity"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.7 — "TRUMP ON UK PM: HE HAS IMMIGRATION, ENERGY PROBLEMS"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 20.0 — "Top Gainers & Losers on 17 August: NMDC Steel, LG Electronics, BSE, Tata Tech, Infosys, Vo"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 18.1 — "Top Gainers & Losers on 17 August: NMDC Steel, LG Electronics, BSE, Tata Tech, Infosys, Vo"
- JIOFIN.BO (Jio Financial Services Limited) score 15.0 — "Getting diagnosed with dementia isn’t the end. It’s a time to take financial action."
- MS (Morgan Stanley) score 11.8 — "Here’s how Amazon’s stock could nearly double by the end of next year, according to Morgan"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 10.9 — "Coal India Share Price Live Updates: Coal India  Price and Volume Overview"
- PCJEWELLER.NS (PC JEWELLER LTD) score 10.4 — "Lalithaa Jewellery Mart IPO: Issue booked 69% so far. GMP hints 15% listing pop. Apply or "
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 10.4 — "Getting diagnosed with dementia isn’t the end. It’s a time to take financial action."
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.3 — "S&P 500 REVENUE GROWTH HITS 5-YEAR HIGH Goldman Sachs says S&P 500 revenues grew 6.4% YoY "
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 9.4 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Trading Update"
- NVDA (NVIDIA Corporation) score 8.2 — "SpaceX’s stock is rising, and that’s a good sign for Nvidia and Google"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 6.0 — "Cement makers face a forgettable H1FY27 as prices weaken and costs rise"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 5.7 — "Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks slip as oil prices rise; retai"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.4 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ News"
- AAPL (Apple Inc.) score 4.6 — "Apple’s stock could rise 30% if it strikes an Nvidia deal for AI, this analyst says"
- VT (Vanguard Total World Stock Ind) score 4.5 — "War and Drought Are Choking the World’s Most Vital Trade Routes"
- META (Meta) score 4.5 — "Pulse of the Street: Tata jitters, metal rout weigh on Indian equities"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.0 — "ICICI Bank raises $750 million as Indian banks tap dollar bond market"
- RDDT (Reddit, Inc.) score 2.8 — "Reddit shares surge 14% on S&P 500 inclusion, replacing AvalonBay"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 2.1 — "Lenskart shares soar after strong Q1 results and MSCI inclusion buzz"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.8 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.8 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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