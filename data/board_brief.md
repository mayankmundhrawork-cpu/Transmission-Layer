# Transmission Layer — board brief · 2026-08-25 21:51Z

data as of **2026-08-25** · 98 series · 11 red / 32 amber · 8 events surfaced (24 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.241, 1d in regime; vol-pct 0.187, breadth-off 0.294, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.3, corr60 -0.4, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.78, corr60 0.86, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.14, corr60 0.35, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.29, corr60 -0.07, last shift 2026-07-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.65, corr60 -0.83, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.16, corr60 -0.12, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.08, corr60 -0.1, last shift 2026-06-30. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.34, corr60 0.2, last shift 2026-07-08. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 90** scanned series survive multiplicity control (effective p ≤ 1.5602920076185356e-05)
- **SETUP** dyn_bond → gbp_usd: leads 1d (ccf 0.301, β 0.4356, p 0.0); driver zc 1.69 → expected 0.223%. Type hit-rate 0.816 (n=2394).
- **SETUP** dyn_bond → eur_usd: leads 1d (ccf 0.251, β 0.3664, p 5e-05); driver zc 1.69 → expected 0.188%. Type hit-rate 0.816 (n=2394).
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

### [AMBER 7.13] cross-asset · 4 series ↑
- dyn_vt [EQUITIES]: last 160.99, z20 0.57, zc 0.75, resid-z -0.42 [quiet], 1d 0.56%, 1y-pct=98
- brent [COMMODITIES]: last 85.86, z20 -0.47, zc -3.20, resid-z -2.01 [unexplained], 1d -6.85%, 1-session move -6.85% ≥ 1.5%
- wti [COMMODITIES]: last 81.11, z20 -0.34, zc -2.00, resid-z -1.19 [moved], 1d -4.59%, 1-session move -4.59% ≥ 1.5%
- dow_jones [INDICES]: last 53572.91, z20 0.30, zc 0.35, resid-z -1.40 [quiet], 1d 0.29%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.959 vs dyn_vt, historically leads by 5d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.942 vs dyn_vt, historically leads by 5d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.832 vs dyn_vt
- Watch next: vix (inverse) — not yet - watch; rho -0.802 vs dyn_vt
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.598 vs dyn_vt, historically leads by 5d
- Source: Oil Falls on Fresh Iran War Diplomacy, Talks on Hormuz — Mint Markets, 2026-08-25. https://www.livemint.com/market/oil-falls-on-fresh-iran-war-diplomacy-talks-on-hormuz-11787692674565.html
- Source: SPR Sinks Toward Operational Minimum as U.S. Crude Inventories Build — OilPrice, 2026-08-25. https://oilprice.com/Latest-Energy-News/World-News/SPR-Sinks-Toward-Operational-Minimum-as-US-Crude-Inventories-Build.html
- Source: U.S. Refiners Face New Crude Squeeze as Canada Cuts Oil Sands Output — OilPrice, 2026-08-25. https://oilprice.com/Energy/Crude-Oil/US-Refiners-Face-New-Crude-Squeeze-as-Canada-Cuts-Oil-Sands-Output.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-16 (d=0.36), 2025-10-21 (d=0.5)

### [RED 6.59] cross-asset · 4 series ↑
- dyn_mrna [EQUITIES]: last 158.87, z20 2.93, zc 1.12, resid-z -0.68 [quiet], 1d 14.39%, |z20|=2.93; 1y-pct=100
- dyn_coin [EQUITIES]: last 187.19, z20 2.66, zc 0.81, resid-z -0.65 [quiet], 1d 4.30%, |z20|=2.66
- btc_usd [CRYPTO]: last 78594.16, z20 2.61, zc -0.12, resid-z -0.38 [quiet], 1d -0.47%, |z20|=2.61
- eth_usd [CRYPTO]: last 2440.83, z20 2.16, zc -0.37, resid-z -0.76 [quiet], 1d -1.65%, |z20|=2.16
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.94).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.425 via btc_usd, z 1.59, reacted)
- **India receivers**: nifty_metal (rho 0.425, z 1.59)
- Source: IMF WARNS OIL, DEBT RISKS STILL THREATEN OUTLOOK IMF chief Kristalina Georgieva says the global economy has weathered the Iran energy shock better than feared, helped by AI investment and increased non-Gulf energy supply. However, renewed oil price gains could fuel inflation — DeItaone, 2026-08-25. https://t.me/walter_bloomberg/35049
- Source: Japanese bond funds see record inflows as rising yields attract global investors — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/japanese-bond-funds-see-record-inflows-as-rising-yields-attract-global-investors/articleshow/133518488.cms
- Source: COVERAGE • $WMS: Coverage initiated at Buy by D.A. Davidson; PT $190 • $AMRZ: Coverage initiated at Neutral by D.A. Davidson; PT $50 • $APMD: Coverage initiated at Buy by BofA Global Research; PT $41 • $AWI: Coverage initiated at Buy by D.A. Davidson; PT $215 • $CSL: — DeItaone, 2026-08-25. https://t.me/walter_bloomberg/35021
- Historical analogues: 2025-08-13 (d=0.94), 2026-05-05 (d=1.25), 2024-11-21 (d=1.26)

### [AMBER 5.74] fx · 4 series ↑
- aud_usd [FX]: last 0.72, z20 2.08, zc -0.18, resid-z -0.03 [quiet], 1d -0.12%, |z20|=2.08
- gbp_usd [FX]: last 1.36, z20 1.73, zc -0.07, resid-z -0.08 [quiet], 1d -0.03%, |z20|=1.73; 1y-pct=95
- eur_usd [FX]: last 1.17, z20 1.65, zc -0.14, resid-z -0.06 [quiet], 1d -0.05%, |z20|=1.65
- usd_mxn [FX]: last 16.94, z20 -1.36, zc 0.38, resid-z 0.26 [quiet], 1d 0.14%, 1y-pct=0
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.514 via aud_usd, z 2.77, reacted); dyn_icicigi_bo (rho -0.446 via gbp_usd, z -1.7, reacted)
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.595 vs aud_usd, historically leads by 1d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.567 vs eur_usd
- **India receivers**: dyn_muthootfin_ns (rho 0.514, z 2.77); dyn_icicigi_bo (rho -0.446, z -1.7)
- Source: Euro zone yields dip from multi-year highs as oil falls on Iran sanctions — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/us-stocks/news/euro-zone-yields-dip-from-multi-year-highs-as-oil-falls-on-iran-sanctions/articleshow/133512503.cms
- Source: Sterling hovers near six-month high underpinned by BoE rate hike expectations — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/us-stocks/news/sterling-hovers-near-six-month-high-underpinned-by-boe-rate-hike-expectations/articleshow/133512463.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 5.6] dyn_adanient_bo ↑
- dyn_adanient_bo [EQUITIES]: last 3106.50, z20 3.60, zc 2.78, resid-z 1.75 [unexplained], 1d 4.24%, |z20|=3.60
- **Mechanism**: dyn_adanient_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.489 via dyn_adanient_bo, z -0.23, quiet); nifty_midcap_100 (rho 0.453 via dyn_adanient_bo, z 1.48, reacted); dyn_indusindbk_bo (rho 0.439 via dyn_adanient_bo, z 0.09, quiet)
- **India receivers**: nifty_50 (rho 0.489, z -0.23); nifty_midcap_100 (rho 0.453, z 1.48); dyn_indusindbk_bo (rho 0.439, z 0.09)
- Source: Market Trading Guide: Adani Enterprises, Dixon Tech among 4 stock recommendations for Wednesday — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/stocks/news/market-trading-guide-adani-enterprises-dixontechamong-4-stock-recommendations-for-wednesday/slideshow/133515517.cms
- Source: Market wrap: Adani Enterprise, InterGlobe, HDFC Life, HCL Tech, top gainers and losers on Nifty and Sensex on Tuesday — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-adani-enterprise-interglobe-hdfc-life-hcl-tech-top-gainers-and-losers-on-nifty-and-sensex-on-tuesday/articleshow/133509563.cms
- Source: Adani Ent Share Price Live Updates: Adani Enterprises  Market Performance Snapshot — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/adani-ent-share-price-today-live-25-aug-2026/liveblog/133487865.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [RED 4.77] dyn_muthootfin_ns ↑
- dyn_muthootfin_ns [EQUITIES]: last 3201.00, z20 2.77, zc -0.07, resid-z -0.58 [quiet], 1d -0.25%, |z20|=2.77
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

### [AMBER 4.33] dyn_bond ↑
- dyn_bond [EQUITIES]: last 91.12, z20 2.33, zc 1.69, resid-z -0.49 [priced], 1d 0.51%, |z20|=2.33
- **Mechanism**: dyn_bond ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (inverse) — not yet - watch; rho -0.928 vs dyn_bond, historically leads by 1d
- Watch next: ust_2y (inverse) — not yet - watch; rho -0.737 vs dyn_bond, historically leads by 1d
- Watch next: ust_30y (inverse) — not yet - watch; rho -0.853 vs dyn_bond
- Watch next: wti (inverse) — not yet - watch; rho -0.587 vs dyn_bond, historically leads by 3d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.517 vs dyn_bond, historically leads by 3d
- Source: JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock and bond settlements using blockchain technology, according to Nikkei. The FSA, Finance Ministry, Bank of Japan and financial institutions will launch a study group this summer. A — DeItaone, 2026-08-25. https://t.me/walter_bloomberg/35047
- Source: Japanese bond funds see record inflows as rising yields attract global investors — ET Markets, 2026-08-25. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/japanese-bond-funds-see-record-inflows-as-rising-yields-attract-global-investors/articleshow/133518488.cms
- Source: Stanley Druckenmiller leads doubters who think Bessent's bond ploys will fail — CNBC Economy, 2026-08-25. https://www.cnbc.com/2026/08/25/stanley-druckenmiller-leads-doubters-who-think-bessents-bond-ploys-will-fail.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-11 (d=0.01), 2026-05-06 (d=0.01)

## Watchlist (below surfacing floor)
comex_gold ↑ (4.16), natgas ↑ (4.15), dyn_lenskart_ns ↑ (3.74), dyn_icicigi_bo ↓ (3.7), comex_copper ↑ (3.59), rates · 2 series ↑ (3.39), gold_silver_ratio ↑ (3.38), dyn_idbi_ns ↑ (3.01), dyn_tech ↑ (2.99), dyn_cartrade_ns ↑ (2.93), usd_cny ↓ (2.9), ftse_100 ↑ (2.89)

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
- INOXINDIA.NS (INOX INDIA LIMITED) score 79.7 — "Broker’s Call: Cummins India (Buy)"
- COALINDIA.NS (COAL INDIA LTD) score 78.4 — "Broker’s Call: Cummins India (Buy)"
- INDIANB.NS (INDIAN BANK) score 77.9 — "JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 76.9 — "Broker’s Call: Cummins India (Buy)"
- BAC (Bank of America Corporation) score 73.0 — "JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock"
- BOND (PIMCO Active Bond Exchange-Tra) score 67.5 — "JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock"
- HDB (HDFC Bank Limited) score 65.3 — "JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock"
- IDBI.NS (IDBI BANK LIMITED) score 61.2 — "JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 61.2 — "JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 61.1 — "JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock"
- TECHM.NS (TECH MAHINDRA LIMITED) score 52.8 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Highlights: US stocks rebound on tech"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 51.7 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Highlights: US stocks rebound on tech"
- TECH (Bio-Techne Corp) score 51.6 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Highlights: US stocks rebound on tech"
- COIN (Coinbase Global, Inc.) score 49.8 — "IMF WARNS OIL, DEBT RISKS STILL THREATEN OUTLOOK IMF chief Kristalina Georgieva says the g"
- OHI (Omega Healthcare Investors, In) score 43.6 — "This chart shows exactly why investors should worry about rising yields — even if they don"
- LTH (Life Time Group Holdings, Inc.) score 35.0 — "JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock"
- CHKP (Check Point Software Technolog) score 31.6 — "Stock market open or closed tomorrow on Eid Milad-un-Nabi 2026? Check NSE, BSE trading off"
- 301077.SZ (CHINASTARS) score 25.7 — "China Defies U.S. Economic D-Day against Iran"
- NVDA (NVIDIA Corporation) score 21.1 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Highlights: US stocks rebound on tech"
- JIOFIN.BO (Jio Financial Services Limited) score 20.9 — "JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock"
- MS (Morgan Stanley) score 18.3 — "Stanley Druckenmiller leads doubters who think Bessent's bond ploys will fail"
- PCJEWELLER.NS (PC JEWELLER LTD) score 17.5 — "Shankesh Jewellers, Sunshine Pictures make a decent debut with 2% listing gains"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 16.9 — "ECB SET FOR SEPTEMBER RATE HIKE ECB policymakers are prepared to raise rates by 25 basis p"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.0 — "JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 15.1 — "JAPAN EYES BLOCKCHAIN FOR REAL-TIME MARKET SETTLEMENT Japan plans to trial real-time stock"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 12.8 — "Persisting retail F&O losses spur call for tighter eligibility filters"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.0 — "Stocks to buy in 2026 for long term: Welspun Corp, Tata Consumer among 5 stocks which coul"
- META (Meta) score 8.8 — "CANADA HITS BACK WITH 50% U.S. TARIFFS Canada plans 15%-50% tariffs on roughly $20 billion"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 8.7 — "Stocks to buy in 2026 for long term: Welspun Corp, Tata Consumer among 5 stocks which coul"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.1 — "Market Trading Guide: Adani Enterprises, Dixon Tech among 4 stock recommendations for Wedn"
- VT (Vanguard Total World Stock Ind) score 7.4 — "BESSENT: TRUMP IS MAKING PHONE CALLS TO WORLD LEADERS TO CUT ECONOMIC TIES WITH IRAN"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.1 — "U.S. HOME PRICES BEAT EXPECTATIONS IN JUNE U.S. 20-city home prices rose 0.2% month-over-m"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.6 — "ICICI raises $1 billion, Union Bank $600 million through dollar bonds"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 6.3 — "Coal India Share Price Live Updates: Coal India Ltd's Price Breakout Signals Strength"
- JEF (Jefferies Financial Group Inc.) score 5.1 — "Jefferies picks 4 NBFCs with up to 20% upside that may continue outperforming Nifty, bank "
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.8 — "From IPO mockery to Rs 1 lakh crore m-cap: Why investors are still betting on Lenskart’s v"
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