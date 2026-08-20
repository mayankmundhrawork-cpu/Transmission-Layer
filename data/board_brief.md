# Transmission Layer — board brief · 2026-08-20 14:52Z

data as of **2026-08-20** · 98 series · 14 red / 26 amber · 8 events surfaced (21 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.239, 2d in regime; vol-pct 0.184, breadth-off 0.294, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.4, last shift 2026-06-05. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.88, corr60 0.88, last shift 2026-02-05. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.21, corr60 0.4, last shift 2026-07-02. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.16, corr60 -0.12, last shift 2026-06-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.67, corr60 -0.82, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.01, corr60 -0.11, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.13, corr60 -0.16, last shift 2026-06-24. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.2, corr60 0.24, last shift 2026-04-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 6.607329525865069e-05)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.491** (n=1116) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.826** (n=2466) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.92] dyn_mrna ↑
- dyn_mrna [EQUITIES]: last 140.64, z20 7.92, zc 5.98, resid-z -0.64 [moved], 1d 38.05%, |z20|=7.92; 1y-pct=100
- **Mechanism**: dyn_mrna ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Moderna’s Cancer Vaccine Breakthrough: What It Means for the Stock — ET Markets, 2026-08-20. https://economictimes.indiatimes.com/markets/us-stocks/news/modernas-cancer-vaccine-breakthrough-what-it-means-for-the-stock/slideshow/133367426.cms
- Source: Moderna’s 177% Surge Burns Shorts in ‘Painful’ $5.5 Billion Loss — Mint Markets, 2026-08-19. https://www.livemint.com/market/modernas-177-surge-burns-shorts-in-painful-5-5-billion-loss-11787175519880.html
- Source: Moderna’s cancer-vaccine breakthrough drives broad biopharma stock rally — MarketWatch Top, 2026-08-19. https://www.marketwatch.com/story/modernas-cancer-vaccine-breakthrough-drives-broad-biopharma-stock-rally-ff2816aa?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-16 (d=0.01), 2025-08-20 (d=0.01)

### [RED 8.98] cross-asset · 3 series ↑
- btc_usd [CRYPTO]: last 71652.22, z20 5.66, zc 1.04, resid-z 1.92 [unexplained], 1d 3.44%, |z20|=5.66
- eth_usd [CRYPTO]: last 2276.29, z20 4.50, zc 0.18, resid-z 0.64 [quiet], 1d 1.10%, |z20|=4.50
- dyn_coin [EQUITIES]: last 170.10, z20 2.28, zc 1.22, resid-z -0.31 [quiet], 1d 6.18%, |z20|=2.28
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 1.52).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: vix (inverse) — not yet - watch; rho -0.585 vs eth_usd
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.511 vs eth_usd
- Source: Crypto comeback? Bitcoin, ethereum are headed for their best day in months as investors flock to hard assets — MarketWatch Top, 2026-08-20. https://www.marketwatch.com/story/crypto-comeback-bitcoin-ethereum-are-headed-for-their-best-day-in-months-as-investors-flock-to-hard-assets-1573b803?mod=mw_rss_topstories
- Source: Bitcoin rallies past $70,000 as falling US yields, Trump's crypto meeting boost optimism — Mint Markets, 2026-08-20. https://www.livemint.com/market/cryptocurrency/bitcoin-rallies-past-70-000-as-falling-us-yields-trumps-crypto-meeting-boost-optimism-11787226673971.html
- Source: Is Bitcoin finally nearing a bottom? Bitwise CIO Matt Hougan answers — ET Markets, 2026-08-20. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/is-bitcoin-finally-nearing-a-bottom-bitwise-cio-matt-hougan-answers/articleshow/133374496.cms
- Historical analogues: 2025-08-13 (d=1.52), 2025-05-09 (d=2.52), 2024-11-13 (d=2.74)

### [RED 7.59] cross-asset · 3 series ↑
- comex_gold [COMMODITIES]: last 4550.50, z20 2.02, zc 0.79, resid-z -0.53 [quiet], 1d 1.36%, |z20|=2.02; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 67.71, z20 1.87, zc 1.22, resid-z 0.83 [quiet], 1d 3.01%, |z20|=1.87; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 67.20, z20 -1.27, zc n/a, resid-z n/a [quiet], 1d -1.60%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.524 via comex_silver, z 0.57, quiet); dyn_stylebaaza_ns (rho -0.387 via gold_silver_ratio, z 2.54, reacted)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.647 vs comex_gold, historically leads by 1d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.567 vs comex_silver, historically leads by 4d
- Watch next: dax (co-move) — not yet - watch; rho 0.53 vs comex_gold, historically leads by 4d
- Watch next: nifty_metal (co-move) — not yet - watch; rho 0.524 vs comex_silver, historically leads by 4d
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.503 vs comex_silver
- **India receivers**: nifty_metal (rho 0.524, z 0.57); dyn_stylebaaza_ns (rho -0.387, z 2.54)
- Source: Keralam gold jewellery trade bets big on Onam sales — BusinessLine Mkts, 2026-08-20. https://www.thehindubusinessline.com/markets/gold/kerala-gold-jewellery-trade-bets-big-on-onam-sales/article71368561.ece
- Source: Gold rises ₹264 to ₹1.58 lakh/10g on weak US dollar — BusinessLine Mkts, 2026-08-20. https://www.thehindubusinessline.com/markets/gold/gold-rises-264-to-158-lakh10g-on-weak-us-dollar/article71368617.ece
- Source: Silver futures jump nearly 1% to ₹2.38 lakh/kg as US Treasury move boosts precious metals — BusinessLine Mkts, 2026-08-20. https://www.thehindubusinessline.com/markets/silver-futures-jump-nearly-1-to-238-lakhkg-as-us-treasury-move-boosts-precious-metals/article71368614.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.26] fx · 4 series ↑
- eur_usd [FX]: last 1.17, z20 2.60, zc 2.87, resid-z 2.86 [unexplained], 1d 0.92%, |z20|=2.60
- gbp_usd [FX]: last 1.36, z20 2.30, zc 1.70, resid-z 1.66 [unexplained], 1d 0.71%, |z20|=2.30
- aud_usd [FX]: last 0.71, z20 2.16, zc 1.18, resid-z 1.26 [quiet], 1d 0.61%, |z20|=2.16
- usd_mxn [FX]: last 16.95, z20 -1.77, zc -1.76, resid-z -1.34 [moved], 1d -0.62%, |z20|=1.77; 1y-pct=0
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.585 via usd_mxn, z 0.49, quiet); dyn_hdbfs_bo (rho 0.413 via aud_usd, z 1.16, reacted); dyn_icicigi_bo (rho -0.391 via gbp_usd, z -0.67, quiet); nifty_midcap_100 (rho -0.37 via usd_mxn, z 0.63, quiet)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.546 vs eur_usd, historically leads by 5d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.539 vs eur_usd
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.53 vs aud_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.585, z 0.49); dyn_hdbfs_bo (rho 0.413, z 1.16); dyn_icicigi_bo (rho -0.391, z -0.67); nifty_midcap_100 (rho -0.37, z 0.63)
- Source: Selloff in euro zone bonds pauses but oil prices keep up pressure — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/bonds/selloff-in-euro-zone-bonds-pauses-but-oil-prices-keep-up-pressure/articleshow/133341510.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 6.07] commodities · 3 series ↑
- corn [COMMODITIES]: last 503.25, z20 4.75, zc 4.99, resid-z 3.99 [unexplained], 1d 6.40%, |z20|=4.75; 1y-pct=100
- wheat [COMMODITIES]: last 701.75, z20 2.56, zc 1.73, resid-z 1.52 [unexplained], 1d 3.16%, |z20|=2.56; 1y-pct=99
- soybeans [COMMODITIES]: last 1238.25, z20 1.90, zc 1.28, resid-z 1.19 [quiet], 1d 1.31%, |z20|=1.90; 1y-pct=99
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_lenskart_ns (rho 0.365 via wheat, z 3.15, reacted)
- **India receivers**: dyn_lenskart_ns (rho 0.365, z 3.15)
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [AMBER 6.03] brent ↑
- brent [COMMODITIES]: last 93.38, z20 1.03, zc 0.89, resid-z 0.50 [quiet], 1d 1.92%, 1-session move +1.92% ≥ 1.5%
- **Mechanism**: brent ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_voltas_ns (rho -0.393 via brent, z -2.68, reacted)
- Watch next: wti (co-move) — not yet - watch; rho 0.983 vs brent, historically leads by 5d
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.561 vs brent, historically leads by 5d
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.527 vs brent, historically leads by 5d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.657 vs brent
- Watch next: cac_40 (inverse) — not yet - watch; rho -0.508 vs brent
- **India receivers**: dyn_voltas_ns (rho -0.393, z -2.68)
- Source: Oil rises to 3-week high as Iran war impasse fuels Middle East supply concerns — ET Markets, 2026-08-20. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/oil-rises-to-3-week-high-as-iran-war-impasse-fuels-middle-east-supply-concerns/articleshow/133380064.cms
- Source: US stock market today: Wall Street futures remain flat amid concerns over rising bond yields, oil jitters — Mint Markets, 2026-08-20. https://www.livemint.com/market/stock-market-news/us-stock-market-today-wall-street-futures-remain-flat-amid-oil-yield-concerns-11787225819415.html
- Source: ADNOC Issues Ninth Spot Crude Tender Since June as UAE Boosts Exports — OilPrice, 2026-08-20. https://oilprice.com/Latest-Energy-News/World-News/ADNOC-Issues-Ninth-Spot-Crude-Tender-Since-June-as-UAE-Boosts-Exports.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.0), 2024-10-18 (d=0.02)

### [RED 5.15] dyn_lenskart_ns ↑
- dyn_lenskart_ns [EQUITIES]: last 656.65, z20 3.15, zc 1.65, resid-z 1.56 [unexplained], 1d 2.67%, |z20|=3.15; 1y-pct=99
- **Mechanism**: dyn_lenskart_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/stocks/news/lenskart-solutions-among-4-stocks-to-hit-52-week-highs-amp-surge-up-to-25-in-a-month/slideshow/133348316.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

### [AMBER 4.83] cross-asset · 3 series ↑
- ust_30y [RATES]: last 5.28, z20 1.51, zc -0.71, resid-z -1.41 [quiet], 1d -0.56%, |z20|=1.51; 1y-pct=99
- ust_10y [RATES]: last 4.71, z20 0.98, zc -0.21, resid-z -0.85 [quiet], 1d -0.21%, 1y-pct=98
- dyn_bond [EQUITIES]: last 90.64, z20 -0.05, zc -1.16, resid-z 0.22 [quiet], 1d -0.36%, 1y-pct=5
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: tips_10y_real (co-move) — not yet - watch; rho 0.699 vs ust_30y, historically leads by 1d
- Watch next: wti (co-move) — not yet - watch; rho 0.547 vs ust_30y, historically leads by 3d
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.534 vs ust_30y, historically leads by 1d
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.581 vs ust_10y
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.529 vs ust_30y
- Source: Conditions are ripe for a market ‘accident,’ but surging bond yields alone won’t cause it, concedes pessimistic strategist — MarketWatch Top, 2026-08-20. https://www.marketwatch.com/story/conditions-are-ripe-for-a-market-accident-but-surging-bond-yields-alone-wont-cause-it-concedes-pessimistic-strategist-222cfc57?mod=mw_rss_topstories
- Source: Wall Street stocks edge lower as bond yields rebound, Walmart sinks 8% — Mint Markets, 2026-08-20. https://www.livemint.com/market/stock-market-news/wall-street-stocks-edge-lower-as-bond-yields-rebound-11787233341461.html
- Source: SEBI, RBI working on bond tokenisation project; pilot to test faster settlement — BusinessLine Mkts, 2026-08-20. https://www.thehindubusinessline.com/markets/sebi-rbi-working-on-bond-tokenisation-project-pilot-to-test-faster-settlement/article71369111.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.12), 2025-04-23 (d=0.18)

## Watchlist (below surfacing floor)
dxy ↓ (4.81), dyn_stylebaaza_ns ↑ (4.54), midcap_largecap_ratio ↑ (4.39), dyn_meta ↓ (3.88), usd_cny ↓ (3.7), dyn_tech ↑ (3.34), dyn_hdb ↓ (2.84), eur_inr ↑ (2.73), indices · 2 series ↑ (2.68), dyn_voltas_ns ↓ (2.68), dyn_icicigi_bo ↓ (2.67), dyn_vt ↑ (2.58)

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
- COALINDIA.NS (COAL INDIA LTD) score 104.7 — "Coking Coal Prices Surge 25%, Squeezing India's Steelmakers"
- INOXINDIA.NS (INOX INDIA LIMITED) score 102.6 — "Coking Coal Prices Surge 25%, Squeezing India's Steelmakers"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 101.9 — "Coking Coal Prices Surge 25%, Squeezing India's Steelmakers"
- INDIANB.NS (INDIAN BANK) score 89.0 — "HDFC Bank shares post mild gains as RBI clears LIC stake increase"
- BOND (PIMCO Active Bond Exchange-Tra) score 72.5 — "Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks edge  lower as rising bond yie"
- BAC (Bank of America Corporation) score 69.5 — "HDFC Bank shares post mild gains as RBI clears LIC stake increase"
- HDB (HDFC Bank Limited) score 63.7 — "HDFC Bank shares post mild gains as RBI clears LIC stake increase"
- IDBI.NS (IDBI BANK LIMITED) score 59.2 — "HDFC Bank shares post mild gains as RBI clears LIC stake increase"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 59.2 — "HDFC Bank shares post mild gains as RBI clears LIC stake increase"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 59.2 — "HDFC Bank shares post mild gains as RBI clears LIC stake increase"
- COIN (Coinbase Global, Inc.) score 58.5 — "Global Market: European blue-chip earnings outlook improves as recovery broadens"
- TECHM.NS (TECH MAHINDRA LIMITED) score 49.3 — "smallcase Technologies expands under CASE Platforms; Zerodha CASE to be new name for mutua"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 47.9 — "smallcase Technologies expands under CASE Platforms; Zerodha CASE to be new name for mutua"
- TECH (Bio-Techne Corp) score 47.8 — "smallcase Technologies expands under CASE Platforms; Zerodha CASE to be new name for mutua"
- OHI (Omega Healthcare Investors, In) score 45.4 — "SEBI allows digitally signed Power of Attorney for foreign portfolio investors"
- LTH (Life Time Group Holdings, Inc.) score 38.5 — "Dow Jones| Nasdaq | US Stock Market Today | Live: US stocks edge  lower as rising bond yie"
- CHKP (Check Point Software Technolog) score 37.0 — "IPOs GMP comparison: Check grey market winner - Shankesh Jewellers vs Sunshine Pictures vs"
- JIOFIN.BO (Jio Financial Services Limited) score 22.9 — "Tourism Finance Corporation among 6 financial services stocks to hit 52-week highs & surge"
- PCJEWELLER.NS (PC JEWELLER LTD) score 22.8 — "Keralam gold jewellery trade bets big on Onam sales"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.2 — "Saatvik Green Energy arm bags  ₹190 crore solar PV module order"
- 301077.SZ (CHINASTARS) score 19.5 — "A $420 camera for $10: China’s young consumers would rather rent than buy. It’s a problem "
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 17.7 — "Tourism Finance Corporation among 6 financial services stocks to hit 52-week highs & surge"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 16.7 — "Coking Coal Prices Surge 25%, Squeezing India's Steelmakers"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 15.9 — "Tourism Finance Corporation among 6 financial services stocks to hit 52-week highs & surge"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 15.1 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 14.2 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- MS (Morgan Stanley) score 12.9 — "Treasury’s buyback blitz may end up driving bond yields higher, warns JPMorgan. Here’s its"
- MRNA (Moderna, Inc.) score 10.7 — "Moderna’s Cancer Vaccine Breakthrough: What It Means for the Stock"
- META (Meta) score 10.2 — "Silver futures jump nearly 1% to ₹2.38 lakh/kg as US Treasury move boosts precious metals"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.1 — "Gautam Adani’s big comeback: Adani Enterprises eyes Nifty crown"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 9.9 — "Mutual funds turn to large-caps as FPIs retreat, retail shifts bets"
- JEF (Jefferies Financial Group Inc.) score 9.4 — "Turtlemint shares soar 4% as Jefferies initiates buy call, sets ₹190 target"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 9.0 — "ICICI Bank Share Price Live Updates: ICICI Bank Price Update"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.7 — "The national debt just hit $40 trillion. Here’s how it can hurt Americans."
- VT (Vanguard Total World Stock Ind) score 8.2 — "World shares are mixed after US Treasury expands debt buybacks, while Brent crude gains 2."
- BHARATFORG.BO (BHARAT FORGE LTD.) score 7.9 — "Coforge shares jump 3% after IT major launches private equity unit"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.7 — "Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month"
- VOLTAS.NS (VOLTAS LTD) score 2.6 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.4 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
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