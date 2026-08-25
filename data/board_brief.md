# Transmission Layer — board brief · 2026-08-25 20:44Z

data as of **2026-08-25** · 98 series · 12 red / 32 amber · 8 events surfaced (23 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.241, 1d in regime; vol-pct 0.187, breadth-off 0.294, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.3, corr60 -0.4, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.78, corr60 0.86, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.14, corr60 0.35, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.29, corr60 -0.07, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.65, corr60 -0.83, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.16, corr60 -0.12, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.08, corr60 -0.1, last shift 2026-06-30. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.34, corr60 0.2, last shift 2026-07-08. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 90** scanned series survive multiplicity control (effective p ≤ 1.5602920076185356e-05)
- **SETUP** dyn_bond → gbp_usd: leads 1d (ccf 0.301, β 0.4356, p 0.0); driver zc 1.69 → expected 0.223%. Type hit-rate 0.816 (n=2394).
- **SETUP** dyn_bond → eur_usd: leads 1d (ccf 0.251, β 0.3665, p 5e-05); driver zc 1.69 → expected 0.188%. Type hit-rate 0.816 (n=2394).
- Track record · residual_reversion: hit-rate **0.496** (n=1114) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.816** (n=2394) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.6] commodities · 3 series ↑
- corn [COMMODITIES]: last 524.25, z20 4.28, zc 5.23, resid-z 4.32 [unexplained], 1d 6.66%, |z20|=4.28; 1y-pct=100
- wheat [COMMODITIES]: last 704.50, z20 2.71, zc 2.10, resid-z 1.65 [unexplained], 1d 3.34%, |z20|=2.71; 1y-pct=99
- soybeans [COMMODITIES]: last 1238.75, z20 2.23, zc 1.85, resid-z 1.90 [unexplained], 1d 1.87%, |z20|=2.23; 1y-pct=99
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_atherenerg_ns (rho -0.389 via soybeans, z 0.2, quiet); dyn_adanient_bo (rho 0.351 via corn, z 3.6, reacted)
- **India receivers**: dyn_atherenerg_ns (rho -0.389, z 0.2); dyn_adanient_bo (rho 0.351, z 3.6)
- Source: Govt lifts wheat export ban with immediate effect — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/economy/agri-business/govt-lifts-wheat-export-ban-with-immediate-effect/article71384020.ece
- Source: Corn rockets to 3-year high as traders eye lower U.S. production — Mint Markets, 2026-08-24. https://www.livemint.com/market/corn-rockets-to-3-year-high-as-traders-eye-lower-u-s-production-11787533218087.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [AMBER 7.19] cross-asset · 4 series ↑
- dyn_vt [EQUITIES]: last 160.99, z20 0.57, zc 0.75, resid-z -0.42 [quiet], 1d 0.56%, 1y-pct=98
- brent [COMMODITIES]: last 85.63, z20 -0.52, zc -3.32, resid-z -2.09 [unexplained], 1d -7.10%, 1-session move -7.10% ≥ 1.5%
- wti [COMMODITIES]: last 80.77, z20 -0.44, zc -2.18, resid-z -1.31 [moved], 1d -4.99%, 1-session move -4.99% ≥ 1.5%
- dow_jones [INDICES]: last 53572.91, z20 0.30, zc 0.35, resid-z -1.45 [quiet], 1d 0.29%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.959 vs dyn_vt, historically leads by 5d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.942 vs dyn_vt, historically leads by 5d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.832 vs dyn_vt
- Watch next: vix (inverse) — not yet - watch; rho -0.802 vs dyn_vt
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.598 vs dyn_vt, historically leads by 5d
- Source: Satellite Images Show Seven Tankers Loading Iraqi Crude at Once — OilPrice, 2026-08-25. https://oilprice.com/Latest-Energy-News/World-News/Satellite-Images-Show-Seven-Tankers-Loading-Iraqi-Crude-at-Once.html
- Source: U.S. CRUDE OIL FUTURES SETTLE AT $82.36/BBL, DOWN $2.65, 3.12 PCT — DeItaone, 2026-08-25. https://t.me/walter_bloomberg/35052
- Source: IMF WARNS OIL, DEBT RISKS STILL THREATEN OUTLOOK IMF chief Kristalina Georgieva says the global economy has weathered the Iran energy shock better than feared, helped by AI investment and increased non-Gulf energy supply. However, renewed oil price gains could fuel inflation — DeItaone, 2026-08-25. https://t.me/walter_bloomberg/35049
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-16 (d=0.36), 2025-10-21 (d=0.5)

### [RED 6.59] cross-asset · 4 series ↑
- dyn_mrna [EQUITIES]: last 158.87, z20 2.93, zc 1.12, resid-z -0.68 [quiet], 1d 14.39%, |z20|=2.93; 1y-pct=100
- dyn_coin [EQUITIES]: last 187.19, z20 2.66, zc 0.81, resid-z -0.65 [quiet], 1d 4.30%, |z20|=2.66
- btc_usd [CRYPTO]: last 78503.15, z20 2.59, zc -0.15, resid-z -0.44 [quiet], 1d -0.58%, |z20|=2.59
- eth_usd [CRYPTO]: last 2447.29, z20 2.19, zc -0.31, resid-z -0.70 [quiet], 1d -1.39%, |z20|=2.19
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.93).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.425 via btc_usd, z 1.59, reacted)
- **India receivers**: nifty_metal (rho 0.425, z 1.59)
- Source: IMF WARNS OIL, DEBT RISKS STILL THREATEN OUTLOOK IMF chief Kristalina Georgieva says the global economy has weathered the Iran energy shock better than feared, helped by AI investment and increased non-Gulf energy supply. However, renewed oil price gains could fuel inflation — DeItaone, 2026-08-25. https://t.me/walter_bloomberg/35049
- Source: Japanese bond funds see record inflows as rising yields attract global investors — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/japanese-bond-funds-see-record-inflows-as-rising-yields-attract-global-investors/articleshow/133518488.cms
- Source: COVERAGE • $WMS: Coverage initiated at Buy by D.A. Davidson; PT $190 • $AMRZ: Coverage initiated at Neutral by D.A. Davidson; PT $50 • $APMD: Coverage initiated at Buy by BofA Global Research; PT $41 • $AWI: Coverage initiated at Buy by D.A. Davidson; PT $215 • $CSL: — DeItaone, 2026-08-25. https://t.me/walter_bloomberg/35021
- Historical analogues: 2025-08-13 (d=0.93), 2026-05-05 (d=1.26), 2024-11-21 (d=1.26)

### [AMBER 5.83] fx · 4 series ↑
- aud_usd [FX]: last 0.72, z20 2.17, zc -0.08, resid-z 0.10 [quiet], 1d -0.06%, |z20|=2.17
- gbp_usd [FX]: last 1.36, z20 1.74, zc -0.07, resid-z -0.07 [quiet], 1d -0.03%, |z20|=1.74; 1y-pct=95
- eur_usd [FX]: last 1.17, z20 1.69, zc -0.08, resid-z 0.01 [quiet], 1d -0.03%, |z20|=1.69
- usd_mxn [FX]: last 16.94, z20 -1.35, zc 0.40, resid-z 0.27 [quiet], 1d 0.15%, 1y-pct=0
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.513 via aud_usd, z 2.77, reacted); dyn_icicigi_bo (rho -0.446 via gbp_usd, z -1.7, reacted)
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.595 vs aud_usd, historically leads by 1d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.566 vs eur_usd
- **India receivers**: dyn_muthootfin_ns (rho 0.513, z 2.77); dyn_icicigi_bo (rho -0.446, z -1.7)
- Source: Euro zone yields dip from multi-year highs as oil falls on Iran sanctions — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/us-stocks/news/euro-zone-yields-dip-from-multi-year-highs-as-oil-falls-on-iran-sanctions/articleshow/133512503.cms
- Source: Sterling hovers near six-month high underpinned by BoE rate hike expectations — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/us-stocks/news/sterling-hovers-near-six-month-high-underpinned-by-boe-rate-hike-expectations/articleshow/133512463.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 5.6] dyn_adanient_bo ↑
- dyn_adanient_bo [EQUITIES]: last 3106.50, z20 3.60, zc 2.78, resid-z 1.74 [unexplained], 1d 4.24%, |z20|=3.60
- **Mechanism**: dyn_adanient_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.489 via dyn_adanient_bo, z -0.23, quiet); nifty_midcap_100 (rho 0.453 via dyn_adanient_bo, z 1.48, reacted); dyn_indusindbk_bo (rho 0.439 via dyn_adanient_bo, z 0.09, quiet)
- **India receivers**: nifty_50 (rho 0.489, z -0.23); nifty_midcap_100 (rho 0.453, z 1.48); dyn_indusindbk_bo (rho 0.439, z 0.09)
- Source: Market Trading Guide: Adani Enterprises, Dixon Tech among 4 stock recommendations for Wednesday — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/stocks/news/market-trading-guide-adani-enterprises-dixontechamong-4-stock-recommendations-for-wednesday/slideshow/133515517.cms
- Source: Market wrap: Adani Enterprise, InterGlobe, HDFC Life, HCL Tech, top gainers and losers on Nifty and Sensex on Tuesday — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-adani-enterprise-interglobe-hdfc-life-hcl-tech-top-gainers-and-losers-on-nifty-and-sensex-on-tuesday/articleshow/133509563.cms
- Source: Adani Ent Share Price Live Updates: Adani Enterprises  Market Performance Snapshot — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/adani-ent-share-price-today-live-25-aug-2026/liveblog/133487865.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [RED 5.5] commodities · 3 series ↑
- comex_gold [COMMODITIES]: last 4720.30, z20 2.18, zc 1.07, resid-z 0.94 [quiet], 1d 1.71%, |z20|=2.18; co-occur[gold_silver] same-direction (channel VALID)
- comex_copper [COMMODITIES]: last 6.71, z20 1.60, zc 0.77, resid-z 1.00 [quiet], 1d 1.70%, |z20|=1.60; 1y-pct=100; co-occur[metal_copper] suppressed: channel WEAK
- comex_silver [COMMODITIES]: last 68.89, z20 1.52, zc 0.20, resid-z -1.24 [quiet], 1d 0.50%, |z20|=1.52; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.484 via comex_silver, z 1.59, reacted)
- Watch next: gold_silver_ratio (inverse) — not yet - watch; rho -0.59 vs comex_copper, historically leads by 1d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.539 vs comex_copper, historically leads by 1d
- Watch next: dax (co-move) — not yet - watch; rho 0.537 vs comex_gold, historically leads by 4d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.698 vs comex_copper
- **India receivers**: nifty_metal (rho 0.484, z 1.59)
- Source: Government signals more PSU stake sales after Hindustan Copper OFS: Report — Mint Markets, 2026-08-25. https://www.livemint.com/market/stock-market-news/government-signals-more-psu-stake-sales-after-hindustan-copper-ofs-report-11787677668931.html
- Source: SPOT GOLD FALLS NEARLY 1% TO $4,605.68/OZ — DeItaone, 2026-08-25. https://t.me/walter_bloomberg/35026
- Source: Hindustan Copper OFS subscribed over 3 times; govt to exercise greenshoe option — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/stocks/news/hindustan-copper-ofs-subscribed-over-3-times-govt-to-exercise-greenshoe-option/articleshow/133509483.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.17), 2025-07-30 (d=0.3)

### [RED 4.77] dyn_muthootfin_ns ↑
- dyn_muthootfin_ns [EQUITIES]: last 3201.00, z20 2.77, zc -0.07, resid-z -0.59 [quiet], 1d -0.25%, |z20|=2.77
- **Mechanism**: dyn_muthootfin_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.645 via dyn_muthootfin_ns, z 1.59, reacted); nifty_midcap_100 (rho 0.563 via dyn_muthootfin_ns, z 1.48, reacted); nifty_50 (rho 0.491 via dyn_muthootfin_ns, z -0.23, quiet); dyn_karurvysya_ns (rho 0.472 via dyn_muthootfin_ns, z 2.09, reacted); dyn_idbi_ns (rho 0.398 via dyn_muthootfin_ns, z 3.01, reacted)
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.51 vs dyn_muthootfin_ns
- **India receivers**: nifty_metal (rho 0.645, z 1.59); nifty_midcap_100 (rho 0.563, z 1.48); nifty_50 (rho 0.491, z -0.23); dyn_karurvysya_ns (rho 0.472, z 2.09)
- Source: Muthoot Finance at crucial support zone; breakout could trigger fresh rally: Kkunal V. Parar — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/stocks/muthoot-finance-at-crucial-support-zone-breakout-could-trigger-fresh-rally-kkunal-v-parar/videoshow/133507377.cms
- Source: Muthoot Finance among 6 stocks flashing bullish signals, hinting at a possible uptrend — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/stocks/news/muthoot-finance-among-6-stocks-flashing-bullish-signals-hinting-at-a-possible-uptrend/slideshow/133489659.cms
- Source: Muthoot Finance, Manappuram Finance shares rally up to 11% in 4 days as gold crosses Rs 1.63 lakh — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/stocks/news/muthoot-finance-manappuram-finance-shares-rally-up-to-11-in-4-days-as-gold-crosses-rs-1-63-lakh/articleshow/133455929.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-22 (d=0.01), 2025-12-04 (d=0.01)

### [AMBER 4.4] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.64, z20 1.40, zc n/a, resid-z n/a [quiet], 1d 0.07%, 52-wk extreme (pct=100); 1y-pct=100
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.483 via midcap_largecap_ratio, z 1.48, reacted); dyn_fincables_ns (rho 0.355 via midcap_largecap_ratio, z 0.84, quiet)
- **India receivers**: nifty_midcap_100 (rho 0.483, z 1.48); dyn_fincables_ns (rho 0.355, z 0.84)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

## Watchlist (below surfacing floor)
dyn_bond ↑ (4.33), natgas ↑ (4.05), dyn_lenskart_ns ↑ (3.74), dyn_icicigi_bo ↓ (3.7), rates · 2 series ↑ (3.39), gold_silver_ratio ↑ (3.23), dyn_idbi_ns ↑ (3.01), dyn_tech ↑ (2.99), dyn_cartrade_ns ↑ (2.93), ftse_100 ↑ (2.89), dyn_pcjeweller_ns ↑ (2.78), usd_cny ↓ (2.15)

## India macro
- nifty_50: 24334.5508 (1d 0.48%, z20 -0.23, flag none)
- nifty_midcap_100: 64163.3516 (1d 0.54%, z20 1.48, flag amber)
- usd_inr: 95.4020 (1d -0.31%, z20 -0.37, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6367 (1d 0.07%, z20 1.40, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 80.6 — "Broker’s Call: Cummins India (Buy)"
- COALINDIA.NS (COAL INDIA LTD) score 79.3 — "Broker’s Call: Cummins India (Buy)"
- INDIANB.NS (INDIAN BANK) score 78.7 — "JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 77.7 — "Broker’s Call: Cummins India (Buy)"
- BAC (Bank of America Corporation) score 73.8 — "JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock"
- BOND (PIMCO Active Bond Exchange-Tra) score 68.2 — "JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock"
- HDB (HDFC Bank Limited) score 66.0 — "JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock"
- IDBI.NS (IDBI BANK LIMITED) score 61.8 — "JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 61.8 — "JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 61.8 — "JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock"
- TECHM.NS (TECH MAHINDRA LIMITED) score 53.4 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Highlights: US stocks rebound on tech"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 52.2 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Highlights: US stocks rebound on tech"
- TECH (Bio-Techne Corp) score 52.2 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Highlights: US stocks rebound on tech"
- COIN (Coinbase Global, Inc.) score 50.4 — "IMF WARNS OIL, DEBT RISKS STILL THREATEN OUTLOOK IMF chief Kristalina Georgieva says the g"
- OHI (Omega Healthcare Investors, In) score 44.1 — "This chart shows exactly why investors should worry about rising yields — even if they don"
- LTH (Life Time Group Holdings, Inc.) score 35.3 — "JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock"
- CHKP (Check Point Software Technolog) score 32.0 — "Stock market open or closed tomorrow on Eid Milad-un-Nabi 2026? Check NSE, BSE trading off"
- 301077.SZ (CHINASTARS) score 26.0 — "China Defies U.S. Economic D-Day against Iran"
- NVDA (NVIDIA Corporation) score 21.3 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Highlights: US stocks rebound on tech"
- JIOFIN.BO (Jio Financial Services Limited) score 21.1 — "JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock"
- MS (Morgan Stanley) score 18.5 — "Stanley Druckenmiller leads doubters who think Bessent's bond ploys will fail"
- PCJEWELLER.NS (PC JEWELLER LTD) score 17.7 — "Shankesh Jewellers, Sunshine Pictures make a decent debut with 2% listing gains"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.2 — "JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 16.0 — "IMF WARNS OIL, DEBT RISKS STILL THREATEN OUTLOOK IMF chief Kristalina Georgieva says the g"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 15.3 — "JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 12.9 — "Persisting retail F&O losses spur call for tighter eligibility filters"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.1 — "Stocks to buy in 2026 for long term: Welspun Corp, Tata Consumer among 5 stocks which coul"
- META (Meta) score 8.9 — "CANADA HITS BACK WITH 50% U.S. TARIFFS Canada plans 15%-50% tariffs on roughly $20 billion"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 8.8 — "Stocks to buy in 2026 for long term: Welspun Corp, Tata Consumer among 5 stocks which coul"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.2 — "Market Trading Guide: Adani Enterprises, Dixon Tech among 4 stock recommendations for Wedn"
- VT (Vanguard Total World Stock Ind) score 7.5 — "BESSENT: TRUMP IS MAKING PHONE CALLS TO WORLD LEADERS TO CUT ECONOMIC TIES WITH IRAN"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.2 — "U.S. HOME PRICES BEAT EXPECTATIONS IN JUNE U.S. 20-city home prices rose 0.2% month-over-m"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.7 — "ICICI raises $1 billion, Union Bank $600 million through dollar bonds"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 6.4 — "Coal India Share Price Live Updates: Coal India Ltd's Price Breakout Signals Strength"
- JEF (Jefferies Financial Group Inc.) score 5.1 — "Jefferies picks 4 NBFCs with up to 20% upside that may continue outperforming Nifty, bank "
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.9 — "From IPO mockery to Rs 1 lakh crore m-cap: Why investors are still betting on Lenskart’s v"
- MRNA (Moderna, Inc.) score 3.5 — "Moderna’s personalized mRNA shot could reshape the fight against skin cancer — but it may "
- VOLTAS.NS (VOLTAS LTD) score 0.8 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.1 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.1 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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