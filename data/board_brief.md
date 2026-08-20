# Transmission Layer — board brief · 2026-08-20 08:54Z

data as of **2026-08-20** · 98 series · 14 red / 28 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.208, 2d in regime; vol-pct 0.165, breadth-off 0.25, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.4, corr60 -0.41, last shift 2026-06-05. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.88, corr60 0.88, last shift 2026-02-05. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.22, corr60 0.4, last shift 2026-07-02. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.16, corr60 -0.12, last shift 2026-06-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.68, corr60 -0.82, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.0, corr60 -0.1, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.13, corr60 -0.16, last shift 2026-06-24. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.15, corr60 0.25, last shift 2026-04-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **4 of 89** scanned series survive multiplicity control (effective p ≤ 0.0043719229098264645)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.491** (n=1116) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.826** (n=2466) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 36.35] cross-asset · 3 series ↑
- dyn_mrna [EQUITIES]: last 174.16, z20 33.03, zc 43.51, resid-z -0.64 [moved], 1d 176.63%, |z20|=33.03; 1y-pct=100
- btc_usd [CRYPTO]: last 71742.99, z20 5.73, zc 1.08, resid-z 2.85 [unexplained], 1d 3.58%, |z20|=5.73
- eth_usd [CRYPTO]: last 2278.55, z20 4.53, zc 0.20, resid-z 5.49 [unexplained], 1d 1.20%, |z20|=4.53
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 1.52).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_coin (co-move) — not yet - watch; rho 0.868 vs btc_usd, historically leads by 5d
- Watch next: vix (inverse) — not yet - watch; rho -0.589 vs eth_usd
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.51 vs btc_usd
- Source: Moderna’s Cancer Vaccine Breakthrough: What It Means for the Stock — ET Markets, 2026-08-20. https://economictimes.indiatimes.com/markets/us-stocks/news/modernas-cancer-vaccine-breakthrough-what-it-means-for-the-stock/slideshow/133367426.cms
- Source: Moderna’s 177% Surge Burns Shorts in ‘Painful’ $5.5 Billion Loss — Mint Markets, 2026-08-19. https://www.livemint.com/market/modernas-177-surge-burns-shorts-in-painful-5-5-billion-loss-11787175519880.html
- Source: Moderna’s cancer-vaccine breakthrough drives broad biopharma stock rally — MarketWatch Top, 2026-08-19. https://www.marketwatch.com/story/modernas-cancer-vaccine-breakthrough-drives-broad-biopharma-stock-rally-ff2816aa?mod=mw_rss_topstories
- Historical analogues: 2025-08-13 (d=1.52), 2025-05-08 (d=2.1), 2024-11-12 (d=2.14)

### [RED 6.8] cross-asset · 3 series ↑
- comex_gold [COMMODITIES]: last 4548.10, z20 2.01, zc 0.76, resid-z -0.53 [quiet], 1d 1.31%, |z20|=2.01; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 66.77, z20 1.58, zc 0.64, resid-z -0.07 [quiet], 1d 1.58%, |z20|=1.58; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 68.12, z20 -0.48, zc n/a, resid-z n/a [quiet], 1d -0.26%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.523 via comex_silver, z 0.52, quiet); dyn_stylebaaza_ns (rho -0.374 via gold_silver_ratio, z 2.57, reacted)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.65 vs comex_gold, historically leads by 1d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.579 vs comex_silver, historically leads by 4d
- Watch next: dax (co-move) — not yet - watch; rho 0.529 vs comex_gold, historically leads by 4d
- Watch next: nifty_metal (co-move) — not yet - watch; rho 0.523 vs comex_silver, historically leads by 4d
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.509 vs comex_gold
- **India receivers**: nifty_metal (rho 0.523, z 0.52); dyn_stylebaaza_ns (rho -0.374, z 2.57)
- Source: MCX shares jump 4% as gold, silver futures rise. What lies ahead after a 900% rally in 3 years? — ET Markets, 2026-08-20. https://economictimes.indiatimes.com/markets/stocks/news/mcx-shares-jump-4-as-gold-silver-futures-rise-what-lies-ahead-after-a-900-rally-in-3-years/articleshow/133370940.cms
- Source: Gold Rate Today, Aug 20: Gold prices up in Delhi, Mumbai, Kolkata, Bengaluru, Ahmedabad — BusinessLine Mkts, 2026-08-20. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-mumbai-chennai-ahmedabad-delhi-hyderabad-bengaluru-kolkata-gold-rates-august-20-2026/article71368051.ece
- Source: Aditya Birla Capital to enter gold loan market, targets 200-300 branches by March 2027 — BusinessLine Mkts, 2026-08-20. https://www.thehindubusinessline.com/markets/gold/aditya-birla-capital-to-enter-gold-loan-market-targets-1000-branches/article71367805.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.49] fx · 4 series ↑
- eur_usd [FX]: last 1.17, z20 2.83, zc 3.31, resid-z 3.23 [unexplained], 1d 1.06%, |z20|=2.83
- gbp_usd [FX]: last 1.36, z20 2.36, zc 1.78, resid-z 1.74 [unexplained], 1d 0.74%, |z20|=2.36
- aud_usd [FX]: last 0.71, z20 2.24, zc 1.27, resid-z 1.39 [quiet], 1d 0.66%, |z20|=2.24
- usd_mxn [FX]: last 16.96, z20 -1.76, zc -1.73, resid-z -1.33 [moved], 1d -0.61%, |z20|=1.76; 1y-pct=0
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.584 via usd_mxn, z 0.43, quiet); dyn_hdbfs_bo (rho 0.429 via aud_usd, z 2.45, reacted); nifty_midcap_100 (rho -0.376 via usd_mxn, z 0.79, quiet); dyn_icicigi_bo (rho -0.374 via gbp_usd, z -0.07, quiet)
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.591 vs eur_usd, historically leads by 4d
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.544 vs eur_usd, historically leads by 5d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.556 vs eur_usd
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.529 vs aud_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.584, z 0.43); dyn_hdbfs_bo (rho 0.429, z 2.45); nifty_midcap_100 (rho -0.376, z 0.79); dyn_icicigi_bo (rho -0.374, z -0.07)
- Source: Selloff in euro zone bonds pauses but oil prices keep up pressure — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/bonds/selloff-in-euro-zone-bonds-pauses-but-oil-prices-keep-up-pressure/articleshow/133341510.cms
- Source: ECB'S LANE: EURO ZONE INFLATION ONE PERCENTAGE POINT ABOVE ECB'S 2% TARGET IS A LOT — DeItaone, 2026-08-18. https://t.me/walter_bloomberg/34837
- Source: Euro zone bonds join global selloff, long-end yields at multi-year highs — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bonds-join-global-selloff-long-end-yields-at-multi-year-highs/articleshow/133321858.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [AMBER 6.08] brent ↑
- brent [COMMODITIES]: last 93.65, z20 1.08, zc 1.02, resid-z -0.01 [quiet], 1d 2.22%, 1-session move +2.22% ≥ 1.5%
- **Mechanism**: brent ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_voltas_ns (rho -0.384 via brent, z -2.31, reacted)
- Watch next: wti (co-move) — not yet - watch; rho 0.982 vs brent, historically leads by 5d
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.561 vs brent, historically leads by 5d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.658 vs brent
- Watch next: cac_40 (inverse) — not yet - watch; rho -0.503 vs brent
- **India receivers**: dyn_voltas_ns (rho -0.384, z -2.31)
- Source: Middle East Oil Crisis Sends Supertanker Prices to Record Highs — OilPrice, 2026-08-20. https://oilprice.com/Latest-Energy-News/World-News/Middle-East-Oil-Crisis-Sends-Supertanker-Prices-to-Record-Highs.html
- Source: Elevated Oil Prices Push Japan’s Imports to an All-Time High — OilPrice, 2026-08-20. https://oilprice.com/Latest-Energy-News/World-News/Elevated-Oil-Prices-Push-Japans-Imports-to-an-All-Time-High.html
- Source: US opens secret oil shipping corridor, exporting about 10 million barrels a day amid Iran stalemate: Report — BusinessLine Mkts, 2026-08-20. https://www.thehindubusinessline.com/news/world/us-opens-secret-oil-shipping-corridor-exporting-about-10-million-barrels-a-day-amid-iran-stalemate-report/article71368005.ece
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.0), 2024-10-18 (d=0.02)

### [RED 6.07] commodities · 3 series ↑
- corn [COMMODITIES]: last 503.25, z20 4.75, zc 4.99, resid-z 0.91 [moved], 1d 6.40%, |z20|=4.75; 1y-pct=100
- wheat [COMMODITIES]: last 702.25, z20 2.59, zc 1.77, resid-z 0.37 [moved], 1d 3.23%, |z20|=2.59; 1y-pct=99
- soybeans [COMMODITIES]: last 1244.00, z20 2.10, zc 1.75, resid-z 1.24 [moved], 1d 1.78%, |z20|=2.10; 1y-pct=99
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [RED 4.99] dxy ↓
- dxy [FX]: last 98.69, z20 -1.99, zc -0.39, resid-z -0.15 [quiet], 1d -0.14%, 20d range extreme; |z20|=1.99
- **Mechanism**: dxy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [RED 4.74] dyn_lenskart_ns ↑
- dyn_lenskart_ns [EQUITIES]: last 646.80, z20 2.74, zc 0.69, resid-z 0.45 [quiet], 1d 1.13%, |z20|=2.74; 1y-pct=99
- **Mechanism**: dyn_lenskart_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/stocks/news/lenskart-solutions-among-4-stocks-to-hit-52-week-highs-amp-surge-up-to-25-in-a-month/slideshow/133348316.cms
- Source: Lenskart shares gain over 5% to record high after incorporating new step-down subsidiary in China — Mint Markets, 2026-08-18. https://www.livemint.com/market/stock-market-news/lenskart-shares-gain-over-5-to-record-high-after-incorporating-new-step-down-subsidiary-in-china-11787043990119.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

### [RED 4.61] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.63, z20 1.61, zc n/a, resid-z n/a [quiet], 1d -0.06%, 52-wk extreme (pct=99); |z20|=1.61; 1y-pct=99
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.498 via midcap_largecap_ratio, z 0.79, quiet); dyn_bharatcoal_ns (rho 0.382 via midcap_largecap_ratio, z -1.24, reacted); dyn_fincables_ns (rho 0.36 via midcap_largecap_ratio, z 1.5, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.498, z 0.79); dyn_bharatcoal_ns (rho 0.382, z -1.24); dyn_fincables_ns (rho 0.36, z 1.5)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

## Watchlist (below surfacing floor)
dyn_stylebaaza_ns ↑ (4.57), cross-asset · 4 series ↑ (4.46), rates · 2 series ↑ (4.35), dyn_meta ↓ (4.0), dyn_tech ↑ (3.99), eur_inr ↑ (3.0), dyn_hdb ↓ (2.95), indices · 2 series ↑ (2.94), usd_cny ↓ (2.85), dyn_tatatech_ns ↑ (2.63), ig_oas ↑ (2.47), dyn_hdbfs_bo ↑ (2.45)

## India macro
- nifty_50: 24236.4004 (1d 0.66%, z20 -0.34, flag none)
- nifty_midcap_100: 63787.2500 (1d 0.60%, z20 0.79, flag amber)
- usd_inr: 95.6900 (1d -0.13%, z20 0.11, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6319 (1d -0.06%, z20 1.61, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 101.5 — "Titagarh Rail Systems shares gain 3% after Indian Railways' approval for traction motor su"
- INOXINDIA.NS (INOX INDIA LIMITED) score 99.3 — "Titagarh Rail Systems shares gain 3% after Indian Railways' approval for traction motor su"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 98.6 — "Titagarh Rail Systems shares gain 3% after Indian Railways' approval for traction motor su"
- INDIANB.NS (INDIAN BANK) score 90.1 — "ICICI Bank Share Price Live Updates: ICICI Bank Price Update"
- BAC (Bank of America Corporation) score 70.5 — "ICICI Bank Share Price Live Updates: ICICI Bank Price Update"
- HDB (HDFC Bank Limited) score 64.3 — "ICICI Bank Share Price Live Updates: ICICI Bank Price Update"
- BOND (PIMCO Active Bond Exchange-Tra) score 61.1 — "Nifty snaps 7-session losing streak; IT stocks lead as bond yields ease"
- IDBI.NS (IDBI BANK LIMITED) score 59.6 — "ICICI Bank Share Price Live Updates: ICICI Bank Price Update"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 59.6 — "ICICI Bank Share Price Live Updates: ICICI Bank Price Update"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 59.6 — "ICICI Bank Share Price Live Updates: ICICI Bank Price Update"
- COIN (Coinbase Global, Inc.) score 55.8 — "Global Market: China, Hong Kong stocks rebound as healthcare and tech shares rally"
- TECHM.NS (TECH MAHINDRA LIMITED) score 49.1 — "Global Market: China, Hong Kong stocks rebound as healthcare and tech shares rally"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 47.6 — "Global Market: China, Hong Kong stocks rebound as healthcare and tech shares rally"
- TECH (Bio-Techne Corp) score 47.5 — "Global Market: China, Hong Kong stocks rebound as healthcare and tech shares rally"
- OHI (Omega Healthcare Investors, In) score 42.9 — "Young investors drive retail market participation as 18-30 age group accounts for 53% of n"
- CHKP (Check Point Software Technolog) score 39.2 — "IPOs GMP comparison: Check grey market winner - Shankesh Jewellers vs Sunshine Pictures vs"
- LTH (Life Time Group Holdings, Inc.) score 36.6 — "Gaja Alternative Asset Management IPO Day 2 LIVE: Issue subscribed 1.53 times so far. Here"
- JIOFIN.BO (Jio Financial Services Limited) score 22.2 — "Nifty holds gap-up gains in tight range; financials lead, metals drag"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.3 — "A $420 camera for $10: China’s young consumers would rather rent than buy. Beijing has a p"
- PCJEWELLER.NS (PC JEWELLER LTD) score 20.0 — "IPOs GMP comparison: Check grey market winner - Shankesh Jewellers vs Sunshine Pictures vs"
- 301077.SZ (CHINASTARS) score 19.6 — "Global Market: China, Hong Kong stocks rebound as healthcare and tech shares rally"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 16.7 — "Nifty holds gap-up gains in tight range; financials lead, metals drag"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 16.0 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 15.6 — "Coal India Share Price Live Updates: Coal India Ltd Stock Details"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 15.0 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 14.8 — "Why Jefferies sees limited upside in Bajaj Housing Finance despite its fast-growing loan b"
- MS (Morgan Stanley) score 11.6 — "Explained: How a JP Morgan unit and a Mumbai-based stock broking firm allegedly manipulate"
- MRNA (Moderna, Inc.) score 11.4 — "Moderna’s Cancer Vaccine Breakthrough: What It Means for the Stock"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 10.5 — "Mutual funds turn to large-caps as FPIs retreat, retail shifts bets"
- META (Meta) score 9.8 — "Nifty holds gap-up gains in tight range; financials lead, metals drag"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.7 — "Adani Ent Share Price Live Updates: Adani Enterprises  Current Market Insights"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 9.6 — "ICICI Bank Share Price Live Updates: ICICI Bank Price Update"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.2 — "The national debt just hit $40 trillion. Here’s how it can hurt Americans."
- BHARATFORG.BO (BHARAT FORGE LTD.) score 8.4 — "Coforge shares jump 3% after IT major launches private equity unit"
- JEF (Jefferies Financial Group Inc.) score 7.8 — "Why Jefferies sees limited upside in Bajaj Housing Finance despite its fast-growing loan b"
- VT (Vanguard Total World Stock Ind) score 7.7 — "World's Largest Electric Plane Flies for 27 Minutes on $5 of Power"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.9 — "Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month"
- VOLTAS.NS (VOLTAS LTD) score 2.7 — "Voltas reported strong growth in June quarter, but failed to impress"
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