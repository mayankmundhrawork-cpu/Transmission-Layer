# Transmission Layer — board brief · 2026-08-20 04:51Z

data as of **2026-08-20** · 98 series · 14 red / 33 amber · 8 events surfaced (30 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.333, 2d in regime; vol-pct 0.165, breadth-off 0.5, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.43, corr60 -0.41, last shift 2026-06-05. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.88, corr60 0.88, last shift 2026-02-05. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.22, corr60 0.4, last shift 2026-07-02. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.18, corr60 -0.12, last shift 2026-06-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.68, corr60 -0.82, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.02, corr60 -0.11, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.13, corr60 -0.16, last shift 2026-06-24. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.05, corr60 0.23, last shift 2026-04-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.0006496287948376533)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.498** (n=1115) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.827** (n=2397) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 36.35] cross-asset · 3 series ↑
- dyn_mrna [EQUITIES]: last 174.16, z20 33.03, zc 43.51, resid-z -0.64 [moved], 1d 176.63%, |z20|=33.03; 1y-pct=100
- eth_usd [CRYPTO]: last 2252.95, z20 3.77, zc -0.28, resid-z 6.31 [unexplained], 1d -1.83%, |z20|=3.77
- btc_usd [CRYPTO]: last 69413.55, z20 3.56, zc -0.22, resid-z 3.41 [unexplained], 1d -0.82%, |z20|=3.56
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.27).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_coin (co-move) — not yet - watch; rho 0.808 vs eth_usd, historically leads by 5d
- Watch next: vix (inverse) — not yet - watch; rho -0.574 vs eth_usd
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.509 vs btc_usd
- Source: Moderna’s 177% Surge Burns Shorts in ‘Painful’ $5.5 Billion Loss — Mint Markets, 2026-08-19. https://www.livemint.com/market/modernas-177-surge-burns-shorts-in-painful-5-5-billion-loss-11787175519880.html
- Source: Moderna’s cancer-vaccine breakthrough drives broad biopharma stock rally — MarketWatch Top, 2026-08-19. https://www.marketwatch.com/story/modernas-cancer-vaccine-breakthrough-drives-broad-biopharma-stock-rally-ff2816aa?mod=mw_rss_topstories
- Source: Moderna’s experimental vaccine prevents cancer recurrence, in ‘historic’ win for personalized medicine. Its stock soared. — MarketWatch Top, 2026-08-19. https://www.marketwatch.com/story/modernas-stock-doubles-on-promising-cancer-vaccine-results-896b1f2c?mod=mw_rss_topstories
- Historical analogues: 2025-08-13 (d=0.27), 2025-05-08 (d=1.01), 2024-11-07 (d=1.25)

### [RED 7.1] cross-asset · 3 series ↑
- comex_gold [COMMODITIES]: last 4546.10, z20 1.99, zc 0.74, resid-z -0.53 [quiet], 1d 1.26%, |z20|=1.99; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 67.09, z20 1.68, zc 0.84, resid-z -1.10 [quiet], 1d 2.06%, |z20|=1.68; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 67.76, z20 -0.78, zc n/a, resid-z n/a [quiet], 1d -0.78%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.525 via comex_silver, z 0.62, quiet); dyn_stylebaaza_ns (rho -0.373 via gold_silver_ratio, z 2.3, reacted)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.653 vs comex_gold, historically leads by 1d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.594 vs comex_silver, historically leads by 4d
- Watch next: dax (co-move) — not yet - watch; rho 0.553 vs comex_gold, historically leads by 4d
- Watch next: nifty_metal (co-move) — not yet - watch; rho 0.525 vs comex_silver, historically leads by 4d
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.509 vs comex_gold
- **India receivers**: nifty_metal (rho 0.525, z 0.62); dyn_stylebaaza_ns (rho -0.373, z 2.3)
- Source: Gold retreats after scaling over 2-month peak on US Treasury move — BusinessLine Mkts, 2026-08-20. https://www.thehindubusinessline.com/markets/gold/gold-retreats-after-scaling-over-2-month-peak-on-us-treasury-move/article71367729.ece
- Source: Gold and silver prices rise on MCX amid a softer dollar, decline in the US bond yields — Mint Markets, 2026-08-20. https://www.livemint.com/market/commodities/gold-and-silver-prices-rise-on-mcx-amid-a-softer-dollar-decline-in-the-us-bond-yields-11787197068727.html
- Source: Gold hovers near early-June high on lower bond yields — ET Markets, 2026-08-20. https://economictimes.indiatimes.com/markets/commodities/news/gold-hovers-near-early-june-high-on-lower-bond-yields/articleshow/133361826.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.17] fx · 4 series ↑
- eur_usd [FX]: last 1.17, z20 2.50, zc 2.69, resid-z -0.66 [moved], 1d 0.86%, |z20|=2.50
- gbp_usd [FX]: last 1.36, z20 2.04, zc 1.32, resid-z -0.54 [quiet], 1d 0.55%, |z20|=2.04
- aud_usd [FX]: last 0.71, z20 2.00, zc 1.00, resid-z -0.49 [quiet], 1d 0.51%, |z20|=2.00
- usd_mxn [FX]: last 16.95, z20 -1.78, zc -1.80, resid-z 0.28 [moved], 1d -0.63%, |z20|=1.78; 1y-pct=0
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.586 via usd_mxn, z 0.46, quiet); dyn_hdbfs_bo (rho 0.426 via aud_usd, z 2.85, reacted); dyn_icicigi_bo (rho -0.406 via gbp_usd, z -0.97, quiet); nifty_midcap_100 (rho -0.375 via usd_mxn, z 0.76, quiet)
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.601 vs eur_usd, historically leads by 4d
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.543 vs eur_usd, historically leads by 5d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.552 vs eur_usd
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.53 vs aud_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.586, z 0.46); dyn_hdbfs_bo (rho 0.426, z 2.85); dyn_icicigi_bo (rho -0.406, z -0.97); nifty_midcap_100 (rho -0.375, z 0.76)
- Source: Selloff in euro zone bonds pauses but oil prices keep up pressure — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/bonds/selloff-in-euro-zone-bonds-pauses-but-oil-prices-keep-up-pressure/articleshow/133341510.cms
- Source: ECB'S LANE: EURO ZONE INFLATION ONE PERCENTAGE POINT ABOVE ECB'S 2% TARGET IS A LOT — DeItaone, 2026-08-18. https://t.me/walter_bloomberg/34837
- Source: Euro zone bonds join global selloff, long-end yields at multi-year highs — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bonds-join-global-selloff-long-end-yields-at-multi-year-highs/articleshow/133321858.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 5.91] commodities · 3 series ↑
- corn [COMMODITIES]: last 501.50, z20 4.59, zc 4.70, resid-z 0.91 [moved], 1d 6.03%, |z20|=4.59; 1y-pct=100
- wheat [COMMODITIES]: last 698.00, z20 2.35, zc 1.43, resid-z 0.37 [quiet], 1d 2.61%, |z20|=2.35; 1y-pct=99
- soybeans [COMMODITIES]: last 1238.50, z20 1.91, zc 1.30, resid-z 1.24 [quiet], 1d 1.33%, |z20|=1.91; 1y-pct=99
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [AMBER 5.49] wti ↑
- wti [COMMODITIES]: last 84.54, z20 0.49, zc -0.63, resid-z 0.16 [quiet], 1d -1.50%, 1-session move -1.50% ≥ 1.5%
- **Mechanism**: wti ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.375 via wti, z 0.76, quiet); dyn_voltas_ns (rho -0.371 via wti, z -2.73, reacted); dyn_adanient_bo (rho -0.36 via wti, z -0.49, quiet)
- Watch next: brent (co-move) — not yet - watch; rho 0.982 vs wti
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.634 vs wti
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.536 vs wti
- **India receivers**: nifty_midcap_100 (rho -0.375, z 0.76); dyn_voltas_ns (rho -0.371, z -2.73); dyn_adanient_bo (rho -0.36, z -0.49)
- Source: Crude oil price: Futures rise as UAE suspends economic ties with Iran — BusinessLine Mkts, 2026-08-20. https://www.thehindubusinessline.com/markets/commodities/crude-oil-price-futures-rise-as-uae-suspends-economic-ties-with-iran/article71367727.ece
- Source: Oil Price Today (August 19): Crude oil nears $92/barrel as Trump claims US is in no talks with Iran. What lies ahead? — ET Markets, 2026-08-20. https://economictimes.indiatimes.com/markets/commodities/news/oil-price-today-august-19-crude-oil-nears-92/barrel-as-trump-claims-us-is-in-no-talks-with-iran-what-lies-ahead/articleshow/133363931.cms
- Source: Stocks to watch: HDFC Bank, BSE, Oil India among shares in focus today; check list here — Mint Markets, 2026-08-20. https://www.livemint.com/market/stock-market-news/stocks-to-watch-hdfc-bank-bse-oil-india-among-shares-in-focus-today-check-list-here-11787192672692.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

### [RED 4.8] dxy ↓
- dxy [FX]: last 98.83, z20 -1.80, zc -0.01, resid-z -0.15 [quiet], 1d -0.00%, 20d range extreme; |z20|=1.80
- **Mechanism**: dxy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [RED 4.73] dyn_voltas_ns ↓
- dyn_voltas_ns [EQUITIES]: last 1218.00, z20 -2.73, zc -0.21, resid-z -1.14 [quiet], 1d -0.41%, |z20|=2.73; 1y-pct=0
- **Mechanism**: dyn_voltas_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bharatcoal_ns (rho 0.564 via dyn_voltas_ns, z -1.35, reacted); nifty_midcap_100 (rho 0.51 via dyn_voltas_ns, z 0.76, quiet); nifty_50 (rho 0.388 via dyn_voltas_ns, z -0.42, quiet); dyn_havells_ns (rho 0.38 via dyn_voltas_ns, z 0.36, quiet)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.51 vs dyn_voltas_ns, historically leads by 5d
- **India receivers**: dyn_bharatcoal_ns (rho 0.564, z -1.35); nifty_midcap_100 (rho 0.51, z 0.76); nifty_50 (rho 0.388, z -0.42); dyn_havells_ns (rho 0.38, z 0.36)
- Source: Voltas reported strong growth in June quarter, but failed to impress — Mint Markets, 2026-08-18. https://www.livemint.com/market/mark-to-market/voltas-strong-growth-fails-to-impress-operating-revenue-acs-home-appliances-other-businesses-engineering-products-11787031152020.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-24 (d=0.0), 2024-11-14 (d=0.01)

### [RED 4.68] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.63, z20 1.68, zc n/a, resid-z n/a [quiet], 1d -0.00%, 52-wk extreme (pct=99); |z20|=1.68; 1y-pct=99
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.5 via midcap_largecap_ratio, z 0.76, quiet); dyn_bharatcoal_ns (rho 0.384 via midcap_largecap_ratio, z -1.35, reacted); dyn_fincables_ns (rho 0.36 via midcap_largecap_ratio, z 1.52, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.5 vs midcap_largecap_ratio, historically leads by 2d
- **India receivers**: nifty_midcap_100 (rho 0.5, z 0.76); dyn_bharatcoal_ns (rho 0.384, z -1.35); dyn_fincables_ns (rho 0.36, z 1.52)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

## Watchlist (below surfacing floor)
dyn_lenskart_ns ↑ (4.56), cross-asset · 4 series ↑ (4.46), rates · 2 series ↑ (4.35), dyn_stylebaaza_ns ↑ (4.3), dyn_meta ↓ (4.0), dyn_tech ↑ (3.99), dyn_icicigi_bo ↓ (2.97), dyn_hdb ↓ (2.95), dyn_hdbfs_bo ↑ (2.85), indices · 2 series ↑ (2.8), usd_cny ↓ (2.74), eur_inr ↑ (2.58)

## India macro
- nifty_50: 24213.7500 (1d 0.56%, z20 -0.42, flag none)
- nifty_midcap_100: 63762.3516 (1d 0.56%, z20 0.76, flag amber)
- usd_inr: 95.6175 (1d -0.21%, z20 -0.04, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6333 (1d -0.00%, z20 1.68, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 100.4 — "Coking coal market poised to be volatile in the short-term on China mine mishap, steel out"
- INOXINDIA.NS (INOX INDIA LIMITED) score 98.1 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 2"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 97.3 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 2"
- INDIANB.NS (INDIAN BANK) score 84.4 — "LIC gets RBI nod to raise HDFC Bank stake to 9.99%"
- BAC (Bank of America Corporation) score 68.2 — "LIC gets RBI nod to raise HDFC Bank stake to 9.99%"
- HDB (HDFC Bank Limited) score 60.7 — "LIC gets RBI nod to raise HDFC Bank stake to 9.99%"
- BOND (PIMCO Active Bond Exchange-Tra) score 58.4 — "Dollar hugs three-month lows as Treasury seeks to sooth the bond market"
- IDBI.NS (IDBI BANK LIMITED) score 56.8 — "LIC gets RBI nod to raise HDFC Bank stake to 9.99%"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 56.8 — "LIC gets RBI nod to raise HDFC Bank stake to 9.99%"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 56.8 — "LIC gets RBI nod to raise HDFC Bank stake to 9.99%"
- COIN (Coinbase Global, Inc.) score 54.9 — "Coal Remains The Undisputed King Of Global Power"
- TECHM.NS (TECH MAHINDRA LIMITED) score 49.0 — "18  stocks including  BSE, LIC, HDFC Bank, Aditya Infotech, Ramco Systems, Titagarh Rail, "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 47.5 — "18  stocks including  BSE, LIC, HDFC Bank, Aditya Infotech, Ramco Systems, Titagarh Rail, "
- TECH (Bio-Techne Corp) score 47.3 — "18  stocks including  BSE, LIC, HDFC Bank, Aditya Infotech, Ramco Systems, Titagarh Rail, "
- OHI (Omega Healthcare Investors, In) score 41.5 — "Can Tempsens IPO deliver long-term growth for high-risk investors?"
- CHKP (Check Point Software Technolog) score 37.7 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 2"
- LTH (Life Time Group Holdings, Inc.) score 32.9 — "IndusInd Bank Share Price Live Updates: IndusInd Bank's price action indicates bearish sen"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.1 — "A $420 camera for $10: China’s young consumers would rather rent than buy. Beijing has a p"
- JIOFIN.BO (Jio Financial Services Limited) score 20.0 — "Rupee falls to a 3-week low of 95.71, raising financial concerns"
- 301077.SZ (CHINASTARS) score 19.4 — "Coking coal market poised to be volatile in the short-term on China mine mishap, steel out"
- PCJEWELLER.NS (PC JEWELLER LTD) score 17.7 — "Lalithaa Jewellery Mart IPO allotment expected today; GMP at 27% — Here’s how to check sta"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 16.7 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 15.6 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 15.2 — "Coking coal market poised to be volatile in the short-term on China mine mishap, steel out"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 14.2 — "Rupee falls to a 3-week low of 95.71, raising financial concerns"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 12.3 — "Sensex Today | Nifty 50 | Stock Market LIVE Updates: Sensex rallies over 550 pts, Nifty ab"
- MRNA (Moderna, Inc.) score 10.8 — "Moderna’s 177% Surge Burns Shorts in ‘Painful’ $5.5 Billion Loss"
- MS (Morgan Stanley) score 10.0 — "India bars JPMorgan unit for alleged market manipulation"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.5 — "The national debt just hit $40 trillion. Here’s how it can hurt Americans."
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 8.9 — "Korean investors dump home stocks for US ones, buy same names at a premium | Is KOSPI-styl"
- META (Meta) score 8.1 — "Metal stock to be in focus on Thursday after this Capex expansion update. Details here"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.0 — "Adani Ent Share Price Live Updates: Adani Enterprises Achieves 0.15% Return in One Week"
- VT (Vanguard Total World Stock Ind) score 8.0 — "World's Largest Electric Plane Flies for 27 Minutes on $5 of Power"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.8 — "ICICI Prudential AMC among 4 stocks showing bullish RSI upswing"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 6.6 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- NVDA (NVIDIA Corporation) score 6.2 — "NVDA - BOFA: NVIDIA COULD BE UP TO 50% UNDERVALUED Bank of America says Nvidia may trade a"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.1 — "Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month"
- VOLTAS.NS (VOLTAS LTD) score 2.9 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.5 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.4 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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