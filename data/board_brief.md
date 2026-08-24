# Transmission Layer — board brief · 2026-08-24 13:11Z

data as of **2026-08-24** · 98 series · 16 red / 29 amber · 8 events surfaced (27 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.304, 2d in regime; vol-pct 0.274, breadth-off 0.333, Markov P(high-vol) 0.016)
- [WEAK] **safe_haven_gold** — corr20 -0.23, corr60 -0.39, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.75, corr60 0.86, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.18, corr60 0.4, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.08, corr60 -0.11, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.7, corr60 -0.83, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.1, corr60 -0.13, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.3, corr60 -0.21, last shift 2026-06-30. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.29, corr60 0.2, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **4 of 90** scanned series survive multiplicity control (effective p ≤ 0.0018708734390282533)
- **SETUP** dyn_ms → nikkei_225: leads 1d (ccf 0.413, β 0.3414, p 0.0); driver zc 1.75 → expected 1.112%. Type hit-rate 0.816 (n=2478).
- **SETUP** dyn_ms → taiwan_weighted: leads 1d (ccf 0.386, β 0.317, p 0.0); driver zc 1.75 → expected 1.032%. Type hit-rate 0.816 (n=2478).
- **SETUP** bovespa → usd_mxn: leads 1d (ccf -0.37, β -0.216, p 0.0); driver zc 1.76 → expected -0.399%. Type hit-rate 0.816 (n=2478).
- Track record · residual_reversion: hit-rate **0.496** (n=1113) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.816** (n=2478) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.06] cross-asset · 4 series ↑
- dyn_mrna [EQUITIES]: last 145.04, z20 4.40, zc 0.66, resid-z 4.54 [unexplained], 1d 8.79%, |z20|=4.40; 1y-pct=100
- dyn_coin [EQUITIES]: last 186.57, z20 4.00, zc 1.58, resid-z 2.63 [unexplained], 1d 8.25%, |z20|=4.00
- btc_usd [CRYPTO]: last 79231.89, z20 3.67, zc 0.25, resid-z 3.11 [unexplained], 1d 1.14%, |z20|=3.67
- eth_usd [CRYPTO]: last 2512.15, z20 3.13, zc -0.03, resid-z 2.06 [unexplained], 1d -0.12%, |z20|=3.13
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.54).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Global Markets: Fast-fashion giant Shein shrinks value to up to $27 billion in Hong Kong IPO — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/us-stocks/news/global-markets-fast-fashion-giant-shein-shrinks-value-to-up-to-27-billion-in-hong-kong-ipo/articleshow/133466240.cms
- Source: Global Markets | Japan's Nikkei weighed down by AI stocks ahead of Nvidia earnings — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/us-stocks/news/global-markets-japans-nikkei-weighed-down-by-ai-stocks-ahead-of-nvidia-earnings/articleshow/133461403.cms
- Source: Bitcoin surges 22% in a week, climbs to nearly $78K as US Treasury bond-buying plan boosts sentiment — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-surges-22-in-a-week-climbs-to-nearly-78k-as-us-treasury-bond-buying-plan-boosts-sentiment/articleshow/133460825.cms
- Historical analogues: 2025-08-13 (d=0.54), 2025-05-09 (d=1.48), 2024-11-21 (d=1.63)

### [RED 7.72] commodities · 2 series ↑
- corn [COMMODITIES]: last 520.50, z20 4.88, zc 5.97, resid-z 0.49 [moved], 1d 7.60%, |z20|=4.88; 1y-pct=100
- wheat [COMMODITIES]: last 709.00, z20 3.19, zc 2.43, resid-z -0.26 [moved], 1d 4.04%, |z20|=3.19; 1y-pct=100
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Govt lifts wheat export ban with immediate effect — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/economy/agri-business/govt-lifts-wheat-export-ban-with-immediate-effect/article71384020.ece
- Source: Corn rockets to 3-year high as traders eye lower U.S. production — Mint Markets, 2026-08-24. https://www.livemint.com/market/corn-rockets-to-3-year-high-as-traders-eye-lower-u-s-production-11787533218087.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [RED 6.86] cross-asset · 4 series ↑
- comex_gold [COMMODITIES]: last 4720.60, z20 2.47, zc 1.17, resid-z 0.88 [quiet], 1d 2.09%, |z20|=2.47; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 69.32, z20 1.81, zc -0.08, resid-z -2.19 [unexplained], 1d -0.20%, |z20|=1.81; co-occur[gold_silver] same-direction (channel VALID)
- comex_copper [COMMODITIES]: last 6.61, z20 0.71, zc 0.20, resid-z 1.01 [quiet], 1d 0.43%, 1y-pct=97; co-occur[metal_copper] suppressed: channel WEAK
- gold_silver_ratio [DERIVED]: last 68.09, z20 -0.20, zc n/a, resid-z n/a [quiet], 1d 2.29%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.489 via comex_silver, z 1.73, reacted); dyn_stylebaaza_ns (rho -0.422 via gold_silver_ratio, z 1.14, reacted)
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.559 vs comex_silver, historically leads by 4d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.547 vs comex_copper, historically leads by 1d
- Watch next: dax (co-move) — not yet - watch; rho 0.52 vs comex_gold, historically leads by 4d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.511 vs comex_copper, historically leads by 1d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.505 vs comex_copper
- **India receivers**: nifty_metal (rho 0.489, z 1.73); dyn_stylebaaza_ns (rho -0.422, z 1.14)
- Source: Gold, Bitcoin or Stocks: Who’s winning the 2026 race for returns? — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/stocks/news/gold-bitcoin-or-stocks-whos-winning-the-2026-race-for-returns/articleshow/133460698.cms
- Source: IPO: GMP over  ₹380 per share - Company specialises in gold, silver refining | What grey market signals at listing gain — Mint Markets, 2026-08-24. https://www.livemint.com/market/ipo/ipo-gmp-over-rs-380-per-share-company-specialises-in-gold-silver-refining-what-grey-market-signals-at-listing-gain-11787560873073.html
- Source: Domestic silver futures rise to ₹2.46 lakh per kg — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/markets/gold/domestic-silver-futures-rise-to-246-lakh-per-kg/article71383712.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.34)

### [AMBER 5.98] wti ↑
- wti [COMMODITIES]: last 85.58, z20 0.98, zc -0.75, resid-z -0.12 [quiet], 1d -1.70%, 1-session move -1.70% ≥ 1.5%
- **Mechanism**: wti ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.688 vs wti
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.577 vs wti
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.564 vs wti
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.525 vs wti
- Source: Sensex today | Stock Market Highlights: Stock markets end lower amid simmering geopolitical tensions, elevated crude oil prices — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-24-august-2026/article71380598.ece
- Source: Norway Vows to Keep Drilling for Oil and Gas in the Arctic — OilPrice, 2026-08-24. https://oilprice.com/Latest-Energy-News/World-News/Norway-Vows-to-Keep-Drilling-for-Oil-and-Gas-in-the-Arctic.html
- Source: Sensex today | Stock Market Live: Sensex falls 300 pts, Nifty near 24,150 as crude prices, West Asia tensions weigh — BusinessLine Mkts, 2026-08-24. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-24-august-2026/article71380598.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

### [RED 5.75] dyn_muthootfin_ns ↑
- dyn_muthootfin_ns [EQUITIES]: last 3209.00, z20 3.75, zc 2.81, resid-z 3.53 [unexplained], 1d 6.19%, |z20|=3.75
- **Mechanism**: dyn_muthootfin_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.687 via dyn_muthootfin_ns, z 1.73, reacted); nifty_midcap_100 (rho 0.614 via dyn_muthootfin_ns, z 0.77, quiet); nifty_50 (rho 0.537 via dyn_muthootfin_ns, z -0.7, quiet); dyn_karurvysya_ns (rho 0.429 via dyn_muthootfin_ns, z 0.13, quiet); dyn_bharatcoal_ns (rho 0.425 via dyn_muthootfin_ns, z 1.67, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.614 vs dyn_muthootfin_ns, historically leads by 3d
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.537 vs dyn_muthootfin_ns, historically leads by 3d
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.579 vs dyn_muthootfin_ns
- **India receivers**: nifty_metal (rho 0.687, z 1.73); nifty_midcap_100 (rho 0.614, z 0.77); nifty_50 (rho 0.537, z -0.7); dyn_karurvysya_ns (rho 0.429, z 0.13)
- Source: Muthoot Finance, Manappuram Finance shares rally up to 11% in 4 days as gold crosses Rs 1.63 lakh — ET Markets, 2026-08-24. https://economictimes.indiatimes.com/markets/stocks/news/muthoot-finance-manappuram-finance-shares-rally-up-to-11-in-4-days-as-gold-crosses-rs-1-63-lakh/articleshow/133455929.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-22 (d=0.01), 2025-12-04 (d=0.01)

### [RED 5.09] dyn_pcjeweller_ns ↑
- dyn_pcjeweller_ns [EQUITIES]: last 11.05, z20 5.09, zc 2.35, resid-z 3.13 [unexplained], 1d 8.12%, |z20|=5.09
- **Mechanism**: dyn_pcjeweller_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.401 via dyn_pcjeweller_ns, z 3.75, reacted)
- **India receivers**: dyn_muthootfin_ns (rho 0.401, z 3.75)
- Historical analogues: 2026-07-10 (d=0.0), 2024-10-01 (d=0.19), 2026-01-07 (d=0.32)

### [AMBER 4.48] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.63, z20 1.48, zc n/a, resid-z n/a [quiet], 1d 0.26%, 52-wk extreme (pct=100); 1y-pct=100
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.491 via midcap_largecap_ratio, z 0.77, quiet); dyn_fincables_ns (rho 0.37 via midcap_largecap_ratio, z 1.18, reacted); dyn_bharatcoal_ns (rho 0.356 via midcap_largecap_ratio, z 1.67, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.491, z 0.77); dyn_fincables_ns (rho 0.37, z 1.18); dyn_bharatcoal_ns (rho 0.356, z 1.67)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 4.29] fx · 4 series ↑
- aud_usd [FX]: last 0.72, z20 2.62, zc 1.36, resid-z 1.32 [quiet], 1d 0.67%, |z20|=2.62
- gbp_usd [FX]: last 1.36, z20 1.95, zc 0.06, resid-z -0.01 [quiet], 1d 0.03%, |z20|=1.95; 1y-pct=95
- eur_usd [FX]: last 1.17, z20 1.84, zc -0.28, resid-z -0.27 [quiet], 1d -0.11%, |z20|=1.84
- usd_mxn [FX]: last 16.93, z20 -1.55, zc -0.19, resid-z -0.08 [quiet], 1d -0.07%, |z20|=1.55; 1y-pct=0
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.584 via aud_usd, z 3.75, reacted); nifty_midcap_100 (rho 0.426 via aud_usd, z 0.77, quiet); dyn_icicigi_bo (rho -0.411 via gbp_usd, z -1.29, reacted)
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.659 vs aud_usd, historically leads by 1d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.554 vs eur_usd
- **India receivers**: dyn_muthootfin_ns (rho 0.584, z 3.75); nifty_midcap_100 (rho 0.426, z 0.77); dyn_icicigi_bo (rho -0.411, z -1.29)
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

## Watchlist (below surfacing floor)
cross-asset · 3 series ↑ (4.1), dyn_idbi_ns ↑ (4.09), dyn_lenskart_ns ↑ (4.01), dyn_cartrade_ns ↑ (3.69), cross-asset · 2 series ↑ (3.46), dyn_icicigi_bo ↓ (3.29), usd_cny ↓ (3.21), dyn_tech ↑ (3.02), natgas ↑ (2.98), tips_10y_real ↓ (2.88), dyn_lth ↑ (2.74), dyn_indusindbk_bo ↑ (2.52)

## India macro
- nifty_50: 24219.0508 (1d -0.14%, z20 -0.70, flag none)
- nifty_midcap_100: 63816.3984 (1d 0.13%, z20 0.77, flag amber)
- usd_inr: 95.7350 (1d -0.04%, z20 0.65, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6350 (1d 0.26%, z20 1.48, flag amber)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 77.2 — "Bajaj Finance, HDFC Life to Nippon Life India AMC: Mirae Asset Sharekhan recommends 11 BFS"
- INOXINDIA.NS (INOX INDIA LIMITED) score 75.4 — "Bajaj Finance, HDFC Life to Nippon Life India AMC: Mirae Asset Sharekhan recommends 11 BFS"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 75.1 — "Bajaj Finance, HDFC Life to Nippon Life India AMC: Mirae Asset Sharekhan recommends 11 BFS"
- INDIANB.NS (INDIAN BANK) score 73.6 — "Stock market prediction tomorrow, 25 August: What will happen to Sensex, Nifty Bank, Nifty"
- BOND (PIMCO Active Bond Exchange-Tra) score 62.7 — "India plans first tokenised bond issue in September: Report"
- BAC (Bank of America Corporation) score 61.6 — "Stock market prediction tomorrow, 25 August: What will happen to Sensex, Nifty Bank, Nifty"
- HDB (HDFC Bank Limited) score 58.3 — "Stock market prediction tomorrow, 25 August: What will happen to Sensex, Nifty Bank, Nifty"
- IDBI.NS (IDBI BANK LIMITED) score 55.0 — "Stock market prediction tomorrow, 25 August: What will happen to Sensex, Nifty Bank, Nifty"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 55.0 — "Stock market prediction tomorrow, 25 August: What will happen to Sensex, Nifty Bank, Nifty"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 55.0 — "Stock market prediction tomorrow, 25 August: What will happen to Sensex, Nifty Bank, Nifty"
- COIN (Coinbase Global, Inc.) score 47.8 — "Global Markets: Fast-fashion giant Shein shrinks value to up to $27 billion in Hong Kong I"
- TECHM.NS (TECH MAHINDRA LIMITED) score 44.7 — "Market wrap: Tata Steel, HCL Tech, Bajaj Finance, Adani Ports top gainers and losers on Ni"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 43.2 — "Market wrap: Tata Steel, HCL Tech, Bajaj Finance, Adani Ports top gainers and losers on Ni"
- TECH (Bio-Techne Corp) score 43.1 — "Market wrap: Tata Steel, HCL Tech, Bajaj Finance, Adani Ports top gainers and losers on Ni"
- OHI (Omega Healthcare Investors, In) score 33.8 — "Alibaba shares tumble as investors question whether AI spending splurge is justified"
- LTH (Life Time Group Holdings, Inc.) score 28.8 — "Nifty drops 7% in 2026, smallcaps gain 13%. Is it time to bet on broader markets?"
- CHKP (Check Point Software Technolog) score 26.6 — "IPO: Share price band  ₹300, GMP  ₹313 - Check last date to apply, allotment and listing d"
- PCJEWELLER.NS (PC JEWELLER LTD) score 19.2 — "Lalithaa Jewellery shares end with 24% listing gains, Horizon Ind ends below ₹60-IPO price"
- JIOFIN.BO (Jio Financial Services Limited) score 18.4 — "Skyways Air Services IPO opens with 0.90x subscription on day 1"
- 301077.SZ (CHINASTARS) score 17.5 — "Global Market: China’s property crisis deepens as Evergrande founder gets life sentence"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 12.7 — "My father-in-law passed away, leaving a house with tenants. Do I evict them?"
- MS (Morgan Stanley) score 11.6 — "This market shift resembles the post–World War II era — and bond yields could have room to"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 11.4 — "How retail F&O participation changed after Sebi tightened rules, in charts"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 10.8 — "Market wrap: Tata Steel, HCL Tech, Bajaj Finance, Adani Ports top gainers and losers on Ni"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 10.5 — "Stocks to buy in 2026 for long term: Jubilant FoodWorks, Max Financial among 5 stocks that"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.0 — "Market wrap: Tata Steel, HCL Tech, Bajaj Finance, Adani Ports top gainers and losers on Ni"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.6 — "Market wrap: Tata Steel, HCL Tech, Bajaj Finance, Adani Ports top gainers and losers on Ni"
- VT (Vanguard Total World Stock Ind) score 9.1 — "This market shift resembles the post–World War II era — and bond yields could have room to"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 8.6 — "Coal India Share Price Live Updates: Coal India Ltd's Price Breakout Signals Strength"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 8.0 — "India lenders' dollar debt sales top $10 billion since RBI window, ICICI Bank beats peer t"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.4 — "Market wrap: Tata Steel, HCL Tech, Bajaj Finance, Adani Ports top gainers and losers on Ni"
- META (Meta) score 7.0 — "Stock market today: Sensex falls 170 points, Nifty 50 ends below 24,219; metal stocks shin"
- JEF (Jefferies Financial Group Inc.) score 5.7 — "Why Jefferies’ Chris Wood sees gold as the second-best hedge amid Iran war and fiscal risk"
- JUSTDIAL.BO (JUST DIAL LTD.) score 4.9 — "Alibaba shares tumble as investors question whether AI spending splurge is justified"
- NVDA (NVIDIA Corporation) score 4.9 — "Here are two trades to make ahead of a critical week for markets as Nvidia results and Jac"
- MRNA (Moderna, Inc.) score 4.8 — "Moderna’s personalized mRNA shot could reshape the fight against skin cancer — but it may "
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.3 — "Lenskart Large Trade: 2.6% equity traded in a $300 million block deal; Softbank Vision lik"
- VOLTAS.NS (VOLTAS LTD) score 1.0 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.2 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.2 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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