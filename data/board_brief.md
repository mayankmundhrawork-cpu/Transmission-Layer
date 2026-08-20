# Transmission Layer — board brief · 2026-08-20 10:46Z

data as of **2026-08-20** · 98 series · 14 red / 28 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.254, 2d in regime; vol-pct 0.174, breadth-off 0.333, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.4, corr60 -0.41, last shift 2026-06-05. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.88, corr60 0.88, last shift 2026-02-05. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.21, corr60 0.4, last shift 2026-07-02. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.16, corr60 -0.12, last shift 2026-06-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.68, corr60 -0.82, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.01, corr60 -0.1, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.13, corr60 -0.16, last shift 2026-06-24. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.16, corr60 0.25, last shift 2026-04-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **4 of 89** scanned series survive multiplicity control (effective p ≤ 0.0043719229098264645)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.491** (n=1116) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.826** (n=2466) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 36.35] cross-asset · 3 series ↑
- dyn_mrna [EQUITIES]: last 174.16, z20 33.03, zc 43.51, resid-z -0.64 [moved], 1d 176.63%, |z20|=33.03; 1y-pct=100
- btc_usd [CRYPTO]: last 71800.00, z20 5.77, zc 1.11, resid-z 2.85 [unexplained], 1d 3.66%, |z20|=5.77
- eth_usd [CRYPTO]: last 2281.84, z20 4.57, zc 0.22, resid-z 5.49 [unexplained], 1d 1.35%, |z20|=4.57
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 1.55).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_coin (co-move) — not yet - watch; rho 0.867 vs btc_usd, historically leads by 5d
- Watch next: vix (inverse) — not yet - watch; rho -0.589 vs eth_usd
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.51 vs btc_usd
- Source: Bitcoin jumps 11% to $71K, hits 2-month high; $190 billion added to crypto market cap after Trump’s crypto push — ET Markets, 2026-08-20. https://economictimes.indiatimes.com/markets/cryptocurrency/bitcoin-jumps-11-to-71k-hits-2-month-high-190-billion-added-to-crypto-market-cap-after-trumps-crypto-push/articleshow/133373099.cms
- Source: Moderna’s Cancer Vaccine Breakthrough: What It Means for the Stock — ET Markets, 2026-08-20. https://economictimes.indiatimes.com/markets/us-stocks/news/modernas-cancer-vaccine-breakthrough-what-it-means-for-the-stock/slideshow/133367426.cms
- Source: Moderna’s 177% Surge Burns Shorts in ‘Painful’ $5.5 Billion Loss — Mint Markets, 2026-08-19. https://www.livemint.com/market/modernas-177-surge-burns-shorts-in-painful-5-5-billion-loss-11787175519880.html
- Historical analogues: 2025-08-13 (d=1.55), 2025-05-08 (d=2.12), 2024-11-12 (d=2.17)

### [RED 6.99] cross-asset · 3 series ↑
- comex_gold [COMMODITIES]: last 4549.40, z20 2.01, zc 0.78, resid-z -0.53 [quiet], 1d 1.34%, |z20|=2.01; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 67.01, z20 1.65, zc 0.79, resid-z 0.10 [quiet], 1d 1.94%, |z20|=1.65; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 67.89, z20 -0.67, zc n/a, resid-z n/a [quiet], 1d -0.59%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.524 via comex_silver, z 0.57, quiet); dyn_stylebaaza_ns (rho -0.378 via gold_silver_ratio, z 2.54, reacted)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.648 vs comex_gold, historically leads by 1d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.574 vs comex_silver, historically leads by 4d
- Watch next: dax (co-move) — not yet - watch; rho 0.53 vs comex_gold, historically leads by 4d
- Watch next: nifty_metal (co-move) — not yet - watch; rho 0.524 vs comex_silver, historically leads by 4d
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.508 vs comex_gold
- **India receivers**: nifty_metal (rho 0.524, z 0.57); dyn_stylebaaza_ns (rho -0.378, z 2.54)
- Source: Why Bessent’s Treasury operations have breathed life back into the gold trade — MarketWatch Top, 2026-08-20. https://www.marketwatch.com/story/why-bessents-treasury-operations-have-breathed-life-back-into-the-gold-trade-d0a8419e?mod=mw_rss_topstories
- Source: Kerala gold jewellery trade bets big on Onam sales — BusinessLine Mkts, 2026-08-20. https://www.thehindubusinessline.com/markets/commodities/kerala-gold-jewellery-trade-bets-big-on-onam-sales/article71368561.ece
- Source: Gold rate today: Gold price retraces from 2-month high. Is it the right time to buy gold? — Mint Markets, 2026-08-20. https://www.livemint.com/market/commodities/gold-rate-today-gold-price-retraces-from-2-month-high-is-it-the-right-time-to-buy-gold-11787211652041.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.53] fx · 4 series ↑
- eur_usd [FX]: last 1.17, z20 2.87, zc 3.39, resid-z 3.23 [unexplained], 1d 1.09%, |z20|=2.87
- gbp_usd [FX]: last 1.36, z20 2.49, zc 1.97, resid-z 1.89 [unexplained], 1d 0.82%, |z20|=2.49; 1y-pct=96
- aud_usd [FX]: last 0.71, z20 2.29, zc 1.33, resid-z 1.47 [quiet], 1d 0.69%, |z20|=2.29
- usd_mxn [FX]: last 16.97, z20 -1.70, zc -1.57, resid-z -1.24 [moved], 1d -0.55%, |z20|=1.70; 1y-pct=0
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.582 via usd_mxn, z 0.49, quiet); dyn_hdbfs_bo (rho 0.414 via aud_usd, z 1.16, reacted); dyn_icicigi_bo (rho -0.384 via gbp_usd, z -0.67, quiet); nifty_midcap_100 (rho -0.37 via usd_mxn, z 0.63, quiet)
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.605 vs eur_usd, historically leads by 4d
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.548 vs eur_usd, historically leads by 5d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.565 vs eur_usd
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.528 vs aud_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.582, z 0.49); dyn_hdbfs_bo (rho 0.414, z 1.16); dyn_icicigi_bo (rho -0.384, z -0.67); nifty_midcap_100 (rho -0.37, z 0.63)
- Source: Selloff in euro zone bonds pauses but oil prices keep up pressure — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/bonds/selloff-in-euro-zone-bonds-pauses-but-oil-prices-keep-up-pressure/articleshow/133341510.cms
- Source: ECB'S LANE: EURO ZONE INFLATION ONE PERCENTAGE POINT ABOVE ECB'S 2% TARGET IS A LOT — DeItaone, 2026-08-18. https://t.me/walter_bloomberg/34837
- Source: Euro zone bonds join global selloff, long-end yields at multi-year highs — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bonds-join-global-selloff-long-end-yields-at-multi-year-highs/articleshow/133321858.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [AMBER 6.12] brent ↑
- brent [COMMODITIES]: last 93.83, z20 1.12, zc 1.12, resid-z -0.01 [quiet], 1d 2.41%, 1-session move +2.41% ≥ 1.5%
- **Mechanism**: brent ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_voltas_ns (rho -0.392 via brent, z -2.68, reacted)
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.56 vs brent, historically leads by 5d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.657 vs brent
- Watch next: cac_40 (inverse) — not yet - watch; rho -0.508 vs brent
- **India receivers**: dyn_voltas_ns (rho -0.392, z -2.68)
- Source: Crude oil price jumps over 1% as US issues fresh threats to Iran — BusinessLine Mkts, 2026-08-20. https://www.thehindubusinessline.com/markets/commodities/crude-oil-price-jumps-over-1-as-fresh-us-economic-warfare-on-iran-revives-supply-concerns/article71368559.ece
- Source: Global Market: European shares flat as oil prices offset bond market relief — ET Markets, 2026-08-20. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-european-shares-flat-as-oil-prices-offset-bond-market-relief/articleshow/133372637.cms
- Source: Has Iranian Crude Become Irrelevant to Global Oil Supply? — OilPrice, 2026-08-20. https://oilprice.com/Latest-Energy-News/World-News/Has-Iranian-Crude-Become-Irrelevant-to-Global-Oil-Supply.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.0), 2024-10-18 (d=0.02)

### [RED 6.0] commodities · 3 series ↑
- corn [COMMODITIES]: last 502.50, z20 4.69, zc 4.86, resid-z 0.91 [moved], 1d 6.24%, |z20|=4.69; 1y-pct=100
- wheat [COMMODITIES]: last 703.25, z20 2.65, zc 1.86, resid-z 0.37 [moved], 1d 3.38%, |z20|=2.65; 1y-pct=99
- soybeans [COMMODITIES]: last 1241.50, z20 2.01, zc 1.54, resid-z 1.24 [moved], 1d 1.57%, |z20|=2.01; 1y-pct=99
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_lenskart_ns (rho 0.368 via wheat, z 3.15, reacted)
- **India receivers**: dyn_lenskart_ns (rho 0.368, z 3.15)
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [RED 5.15] dyn_lenskart_ns ↑
- dyn_lenskart_ns [EQUITIES]: last 656.65, z20 3.15, zc 1.65, resid-z 1.46 [moved], 1d 2.67%, |z20|=3.15; 1y-pct=99
- **Mechanism**: dyn_lenskart_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/stocks/news/lenskart-solutions-among-4-stocks-to-hit-52-week-highs-amp-surge-up-to-25-in-a-month/slideshow/133348316.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

### [RED 5.13] dxy ↓
- dxy [FX]: last 98.58, z20 -2.13, zc -0.68, resid-z -0.15 [quiet], 1d -0.25%, 20d range extreme; |z20|=2.13
- **Mechanism**: dxy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [RED 4.54] dyn_stylebaaza_ns ↑
- dyn_stylebaaza_ns [EQUITIES]: last 440.55, z20 2.54, zc 1.09, resid-z 0.97 [quiet], 1d 4.21%, |z20|=2.54; 1y-pct=100
- **Mechanism**: dyn_stylebaaza_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_pcjeweller_ns (rho 0.385 via dyn_stylebaaza_ns, z 0.18, quiet); dyn_adanient_bo (rho 0.36 via dyn_stylebaaza_ns, z -0.9, quiet)
- **India receivers**: dyn_pcjeweller_ns (rho 0.385, z 0.18); dyn_adanient_bo (rho 0.36, z -0.9)
- Source: Young investors drive retail market participation as 18-30 age group accounts for 53% of new additions: Axis Direct — BusinessLine Mkts, 2026-08-20. https://www.thehindubusinessline.com/markets/young-investors-drive-retail-market-participation-as-18-30-age-group-accounts-for-53-of-new-additions-axis-direct/article71368203.ece
- Source: Mutual funds turn to large-caps as FPIs retreat, retail shifts bets — Mint Markets, 2026-08-20. https://www.livemint.com/market/stock-market-news/small-cap-stocks-mutual-funds-fpi-retail-investors-q1fy27-11787195441939.html
- Source: Korean investors dump home stocks for US ones, buy same names at a premium | Is KOSPI-style crash coming to Wall Street? — Mint Markets, 2026-08-19. https://www.livemint.com/market/stock-market-news/korean-investors-dump-home-stocks-for-us-buying-same-names-at-a-premium-is-wall-street-headed-for-kospi-style-crash-11787150873908.html
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-04 (d=0.01), 2025-02-20 (d=0.02)

## Watchlist (below surfacing floor)
cross-asset · 4 series ↑ (4.46), midcap_largecap_ratio ↑ (4.39), rates · 2 series ↑ (4.35), dyn_meta ↓ (4.0), dyn_tech ↑ (3.99), eur_inr ↑ (3.15), dyn_hdb ↓ (2.95), usd_cny ↓ (2.92), indices · 2 series ↑ (2.68), dyn_voltas_ns ↓ (2.68), dyn_icicigi_bo ↓ (2.67), dyn_tatatech_ns ↑ (2.51)

## India macro
- nifty_50: 24231.8496 (1d 0.64%, z20 -0.35, flag none)
- nifty_midcap_100: 63668.2500 (1d 0.41%, z20 0.63, flag amber)
- usd_inr: 95.6950 (1d -0.13%, z20 0.12, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6275 (1d -0.22%, z20 1.39, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 103.7 — "India's REIT sector has substantial room to grow: CareEdge Ratings"
- INOXINDIA.NS (INOX INDIA LIMITED) score 101.6 — "India's REIT sector has substantial room to grow: CareEdge Ratings"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 100.8 — "India's REIT sector has substantial room to grow: CareEdge Ratings"
- INDIANB.NS (INDIAN BANK) score 89.5 — "Indian realty market remains divided amid affordability pressures and GCC-led commercial d"
- BAC (Bank of America Corporation) score 69.3 — "ICICI Bank Share Price Live Updates: ICICI Bank Price Update"
- HDB (HDFC Bank Limited) score 63.2 — "ICICI Bank Share Price Live Updates: ICICI Bank Price Update"
- BOND (PIMCO Active Bond Exchange-Tra) score 63.0 — "Global Market: Eurozone bond yields ease as US Treasury moves to support long-dated debt"
- COIN (Coinbase Global, Inc.) score 60.8 — "Global Market: European blue-chip earnings outlook improves as recovery broadens"
- IDBI.NS (IDBI BANK LIMITED) score 58.5 — "ICICI Bank Share Price Live Updates: ICICI Bank Price Update"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 58.5 — "ICICI Bank Share Price Live Updates: ICICI Bank Price Update"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 58.5 — "ICICI Bank Share Price Live Updates: ICICI Bank Price Update"
- TECHM.NS (TECH MAHINDRA LIMITED) score 49.2 — "Why Zerodha’s Nithin Kamath wants fintech founders to rethink trading in the age of AI"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 47.8 — "Why Zerodha’s Nithin Kamath wants fintech founders to rethink trading in the age of AI"
- TECH (Bio-Techne Corp) score 47.6 — "Why Zerodha’s Nithin Kamath wants fintech founders to rethink trading in the age of AI"
- OHI (Omega Healthcare Investors, In) score 43.1 — "Young crypto investors sell more, while older investors buy and diversify portfolios : Coi"
- CHKP (Check Point Software Technolog) score 38.5 — "IPOs GMP comparison: Check grey market winner - Shankesh Jewellers vs Sunshine Pictures vs"
- LTH (Life Time Group Holdings, Inc.) score 37.0 — "Gold rate today: Gold price retraces from 2-month high. Is it the right time to buy gold?"
- JIOFIN.BO (Jio Financial Services Limited) score 21.8 — "Nifty holds gap-up gains in tight range; financials lead, metals drag"
- PCJEWELLER.NS (PC JEWELLER LTD) score 20.6 — "Kerala gold jewellery trade bets big on Onam sales"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.0 — "A $420 camera for $10: China’s young consumers would rather rent than buy. Beijing has a p"
- 301077.SZ (CHINASTARS) score 19.3 — "Global Market: China, Hong Kong stocks rebound as healthcare and tech shares rally"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 16.4 — "Nifty holds gap-up gains in tight range; financials lead, metals drag"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 15.7 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 15.5 — "Top Gainers & Losers on 20 Aug: Balrampur Chini Mills, Meesho, MCX, Redington, Muthoot Fin"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 15.3 — "Coal India Share Price Live Updates: Coal India Ltd Stock Details"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 14.7 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- MS (Morgan Stanley) score 12.4 — "Quote of the day by Stanley Druckenmiller: "It’s liquidity that moves markets""
- MRNA (Moderna, Inc.) score 11.2 — "Moderna’s Cancer Vaccine Breakthrough: What It Means for the Stock"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 10.3 — "Mutual funds turn to large-caps as FPIs retreat, retail shifts bets"
- META (Meta) score 9.6 — "Nifty holds gap-up gains in tight range; financials lead, metals drag"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.5 — "Adani Ent Share Price Live Updates: Adani Enterprises  Current Market Insights"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 9.4 — "ICICI Bank Share Price Live Updates: ICICI Bank Price Update"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.0 — "The national debt just hit $40 trillion. Here’s how it can hurt Americans."
- BHARATFORG.BO (BHARAT FORGE LTD.) score 8.2 — "Coforge shares jump 3% after IT major launches private equity unit"
- JEF (Jefferies Financial Group Inc.) score 7.7 — "Why Jefferies sees limited upside in Bajaj Housing Finance despite its fast-growing loan b"
- VT (Vanguard Total World Stock Ind) score 7.5 — "World's Largest Electric Plane Flies for 27 Minutes on $5 of Power"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.8 — "Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month"
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