# Transmission Layer — board brief · 2026-08-28 05:31Z

data as of **2026-08-28** · 98 series · 10 red / 35 amber · 8 events surfaced (30 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.264, 2d in regime; vol-pct 0.152, breadth-off 0.375, Markov P(high-vol) 0.015)
- [INVERTED] **safe_haven_gold** — corr20 -0.25, corr60 -0.4, last shift 2026-06-08. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.78, corr60 0.86, last shift 2026-01-29. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.19, corr60 0.33, last shift 2026-07-10. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.18, corr60 0.02, last shift 2026-07-14. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.55, corr60 -0.83, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.24, corr60 -0.15, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.11, corr60 -0.08, last shift 2026-06-25. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.24, corr60 0.2, last shift 2026-07-10. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 90** scanned series survive multiplicity control (effective p ≤ 0.00017683457040162942)
- **SETUP** dyn_nvda → taiwan_weighted: leads 1d (ccf 0.403, β 0.2398, p 0.0); driver zc 3.94 → expected 2.103%. Type hit-rate 0.811 (n=2308).
- **SETUP** dyn_nvda → nikkei_225: leads 1d (ccf 0.395, β 0.2246, p 0.0); driver zc 3.94 → expected 1.97%. Type hit-rate 0.811 (n=2308).
- **SETUP** dyn_nvda → usd_mxn: leads 1d (ccf -0.341, β -0.0729, p 0.0); driver zc 3.94 → expected -0.639%. Type hit-rate 0.811 (n=2308).
- **SETUP** dyn_nvda → aud_usd: leads 1d (ccf 0.324, β 0.0714, p 0.0); driver zc 3.94 → expected 0.626%. Type hit-rate 0.811 (n=2308).
- **SETUP** dyn_nvda → kospi: leads 1d (ccf 0.261, β 0.2332, p 0.0); driver zc 3.94 → expected 2.046%. Type hit-rate 0.811 (n=2308).
- Track record · residual_reversion: hit-rate **0.497** (n=1121) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.811** (n=2308) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.52] commodities · 3 series ↑
- wheat [COMMODITIES]: last 761.75, z20 3.20, zc 1.19, resid-z 0.73 [quiet], 1d 2.56%, |z20|=3.20; 1y-pct=100
- corn [COMMODITIES]: last 535.50, z20 2.90, zc 3.87, resid-z -0.49 [moved], 1d 4.95%, |z20|=2.90; 1y-pct=100
- soybeans [COMMODITIES]: last 1272.50, z20 2.38, zc 1.25, resid-z 0.22 [quiet], 1d 1.27%, |z20|=2.38; 1y-pct=100
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: UBS SEES COMMODITY OPPORTUNITIES BEYOND OIL UBS sees opportunities across copper, agriculture and gold, arguing commodities offer both returns and inflation protection. Copper should benefit from AI infrastructure and electrification. Wheat and corn are gaining as a — DeItaone, 2026-08-27. https://t.me/walter_bloomberg/35133
- Source: Wheat Hits Three-Year High as Russia Prepares to Escalate War — Mint Markets, 2026-08-27. https://www.livemint.com/market/wheat-hits-three-year-high-as-russia-prepares-to-escalate-war-11787802575795.html
- Source: Wheat soars to daily limit on Black Sea export worries, corn at lifetime highs — Mint Markets, 2026-08-26. https://www.livemint.com/market/wheat-soars-to-daily-limit-on-black-sea-export-worries-corn-at-lifetime-highs-11787773711563.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [AMBER 5.59] cross-asset · 3 series ↑
- dyn_coin [EQUITIES]: last 190.75, z20 2.27, zc 0.97, resid-z -0.42 [quiet], 1d 4.93%, |z20|=2.27
- btc_usd [CRYPTO]: last 79758.55, z20 1.73, zc -0.27, resid-z 0.61 [quiet], 1d -0.82%, |z20|=1.73
- eth_usd [CRYPTO]: last 2491.34, z20 1.54, zc -0.33, resid-z 0.01 [quiet], 1d -1.31%, |z20|=1.54
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-11 (z-distance 0.82).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.436 via btc_usd, z 1.72, reacted)
- Watch next: dxy (inverse) — not yet - watch; rho -0.562 vs eth_usd, historically leads by 1d
- **India receivers**: nifty_metal (rho 0.436, z 1.72)
- Source: Global Market: South Korean shares fall as AI trade loses steam, investors eye Jackson Hole — ET Markets, 2026-08-28. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-south-korean-shares-fall-as-ai-trade-loses-steam-investors-eye-jackson-hole/articleshow/133582603.cms
- Source: Global Market Today: Asian shares slip as US stock futures dip ahead of Warsh’s Jackson Hole speech — ET Markets, 2026-08-28. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-today-asian-shares-slip-as-us-stock-futures-dip-ahead-of-warshs-jackson-hole-speech/articleshow/133580806.cms
- Source: BITCOIN ETF INFLOWS HIT 10-MONTH HIGH Investors poured $2.5B into spot Bitcoin ETFs over the past seven trading days — the strongest inflow since October. Bitcoin and gold are benefiting from the return of the “debasement trade.” Investors are seeking alternatives to the — DeItaone, 2026-08-27. https://t.me/walter_bloomberg/35152
- Historical analogues: 2025-08-11 (d=0.82), 2024-10-31 (d=1.09), 2025-08-22 (d=1.23)

### [RED 5.25] dyn_icicigi_bo ↓
- dyn_icicigi_bo [EQUITIES]: last 1567.10, z20 -3.25, zc -1.04, resid-z 0.23 [quiet], 1d -1.65%, |z20|=3.25; 1y-pct=0
- **Mechanism**: dyn_icicigi_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: ICICI Bank Share Price Live Updates: ICICI Bank's Current Trading Price — ET Markets, 2026-08-28. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/icici-bank-share-price-live-updates-28-aug-2026/liveblog/133581796.cms
- Source: ICICI Pru AMC shares slide 3.8% as Prudential offloads 2% stake — BusinessLine Mkts, 2026-08-27. https://www.thehindubusinessline.com/markets/prudential-offloads-2-stake-in-icici-prudential-amc-stock-slides-38-in-bulk-deal/article71395770.ece
- Source: BIG DEAL | ICICI Prudential raises stake in SBI Cards and Payment Services to 7.30% — Mint Markets, 2026-08-27. https://www.livemint.com/market/stock-market-news/big-deal-icici-prudential-raises-stake-in-sbi-cards-and-payment-services-to-730-11787818758122.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.0), 2025-05-30 (d=0.03)

### [RED 5.2] dyn_hdb ↓
- dyn_hdb [EQUITIES]: last 22.46, z20 -3.20, zc -2.37, resid-z -1.16 [moved], 1d -3.06%, |z20|=3.20; 1y-pct=0
- **Mechanism**: dyn_hdb ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.67 via dyn_hdb, z -1.19, reacted); nifty_midcap_100 (rho 0.535 via dyn_hdb, z 1.51, reacted); dyn_jiofin_bo (rho 0.47 via dyn_hdb, z -1.62, reacted); nifty_fmcg (rho 0.434 via dyn_hdb, z -1.69, reacted); nifty_it (rho 0.418 via dyn_hdb, z 0.36, quiet)
- **India receivers**: nifty_50 (rho 0.67, z -1.19); nifty_midcap_100 (rho 0.535, z 1.51); dyn_jiofin_bo (rho 0.47, z -1.62); nifty_fmcg (rho 0.434, z -1.69)
- Source: HDFC Bank shares hit fresh 52-week low. Should investors be worried? — BusinessLine Mkts, 2026-08-28. https://www.thehindubusinessline.com/markets/hdfc-bank-shares-hit-fresh-52-week-low-should-investors-be-worried/article71399135.ece
- Source: HDFC Bank's CEO call gains urgency as Sashidhar Jagdishan's term nears end — ET Markets, 2026-08-27. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-banks-ceo-call-gains-urgency-as-sashidhar-jagdishans-term-nears-end/articleshow/133580693.cms
- Source: Market wrap: Adani Enterprises, Kotak Mahindra Bank, HDFC Bank, M&M top gainers and losers on Nifty and Sensex on Thursday — ET Markets, 2026-08-27. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-adani-enterprises-kotak-mahindra-bank-hdfc-bank-mm-top-gainers-and-losers-on-nifty-and-sensex-on-thursday/articleshow/133566380.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [AMBER 5.08] cross-asset · 4 series ↑
- vix [INDICES]: last 14.51, z20 -1.41, zc -0.61, resid-z n/a [quiet], 1d -4.60%, 1y-pct=4
- dyn_vt [EQUITIES]: last 161.58, z20 0.76, zc 0.62, resid-z 0.06 [quiet], 1d 0.44%, 1y-pct=98
- sp500 [INDICES]: last 7730.11, z20 0.49, zc 1.02, resid-z -0.23 [quiet], 1d 0.71%, 1y-pct=97
- dow_jones [INDICES]: last 53562.07, z20 0.11, zc 0.25, resid-z -0.19 [quiet], 1d 0.18%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-10-17 (z-distance 0.46).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: wti (inverse) — not yet - watch; rho -0.704 vs dow_jones, historically leads by 2d
- Watch next: brent (inverse) — not yet - watch; rho -0.704 vs dow_jones, historically leads by 3d
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.667 vs vix, historically leads by 5d
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.649 vs vix, historically leads by 1d
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.558 vs dyn_vt, historically leads by 5d
- Source: Marvell boosts its forecasts, but the stock slides as Wall Street wonders if there’s more to the story — MarketWatch Top, 2026-08-28. https://www.marketwatch.com/story/marvell-is-boosting-its-forecasts-but-thats-not-enough-to-lift-its-stock-c769556a?mod=mw_rss_topstories
- Source: CrowdStrike’s stock jumps after record-breaking earnings. Wall Street is lapping it up. — MarketWatch Top, 2026-08-27. https://www.marketwatch.com/story/crowdstrikes-stock-has-jumped-after-record-breaking-earnings-wall-street-is-lapping-it-up-dbdaca83?mod=mw_rss_topstories
- Source: The options market is signaling further gains for the S&P 500, but one indicator is flashing a warning — MarketWatch Top, 2026-08-27. https://www.marketwatch.com/story/the-s-p-500-is-nearing-an-especially-positive-price-and-the-options-market-suggests-a-surge-is-likely-a54d866d?mod=mw_rss_topstories
- Historical analogues: 2024-10-17 (d=0.46), 2025-10-21 (d=0.48), 2025-08-27 (d=0.53)

### [RED 4.66] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.66, z20 1.66, zc n/a, resid-z n/a [quiet], 1d -0.03%, 52-wk extreme (pct=99); |z20|=1.66; 1y-pct=99
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho -0.373 via midcap_largecap_ratio, z -1.69, reacted); dyn_techm_ns (rho -0.365 via midcap_largecap_ratio, z 0.68, quiet); dyn_inoxindia_ns (rho 0.361 via midcap_largecap_ratio, z 3.69, reacted); nifty_50 (rho -0.356 via midcap_largecap_ratio, z -1.19, reacted)
- **India receivers**: nifty_fmcg (rho -0.373, z -1.69); dyn_techm_ns (rho -0.365, z 0.68); dyn_inoxindia_ns (rho 0.361, z 3.69); nifty_50 (rho -0.356, z -1.19)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 4.64] natgas ↑
- natgas [COMMODITIES]: last 2.92, z20 2.64, zc 0.15, resid-z 0.89 [quiet], 1d 0.48%, |z20|=2.64
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Egypt’s LNG Comeback Is Set to Start in Cyprus — OilPrice, 2026-08-28. https://oilprice.com/Energy/Natural-Gas/Egypts-LNG-Comeback-Is-Set-to-Start-in-Cyprus.html
- Source: TotalEnergies Exits Russia’s Sanctioned Arctic LNG 2 Project — OilPrice, 2026-08-27. https://oilprice.com/Latest-Energy-News/World-News/TotalEnergies-Exits-Russias-Sanctioned-Arctic-LNG-2-Project.html
- Source: Thailand Accelerates Clean Energy Push to Cut LNG Dependence — OilPrice, 2026-08-27. https://oilprice.com/Latest-Energy-News/World-News/Thailand-Accelerates-Clean-Energy-Push-to-Cut-LNG-Dependence.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [RED 4.56] dyn_dks ↓
- dyn_dks [EQUITIES]: last 131.80, z20 -2.56, zc 0.14, resid-z 1.01 [quiet], 1d 1.65%, |z20|=2.56; 1y-pct=1
- **Mechanism**: dyn_dks ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: PRICE TARGET CUT • $APP: PT cut to $475 from $500 by Needham • $CHWY: PT cut to $37 from $42 by Morgan Stanley • $CPRT: PT cut to $25 from $26 by Barclays • $DKS: PT cut to $150 from $280 by Barclays; PT cut to $180 from $300 by BTIG; PT cut to $205 from $260 by D.A. — DeItaone, 2026-08-26. https://t.me/walter_bloomberg/35087
- Source: Dick’s Sporting Goods slumps after earnings miss: What’s next? — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/us-stocks/news/dicks-sporting-goods-slumps-after-earnings-miss-whats-next/slideshow/133532630.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-01 (d=0.0), 2025-08-15 (d=0.12)

## Watchlist (below surfacing floor)
dyn_adanient_bo ↑ (4.5), gold_silver_ratio ↓ (4.16), dyn_bac ↓ (4.01), dyn_atherenerg_ns ↑ (3.98), dyn_inoxindia_ns ↑ (3.69), dyn_tech ↑ (3.65), dyn_mrna ↑ (3.61), comex_copper ↑ (3.59), dyn_nvda ↑ (3.55), fx · 2 series ↑ (3.04), dyn_lenskart_ns ↑ (2.94), dyn_stylebaaza_ns ↑ (2.94)

## India macro
- nifty_50: 24154.7500 (1d 0.27%, z20 -1.19, flag none)
- nifty_midcap_100: 64181.1016 (1d 0.23%, z20 1.51, flag amber)
- usd_inr: 95.5575 (1d 0.13%, z20 0.42, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6571 (1d -0.03%, z20 1.66, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 82.3 — "From Gift Nifty to Fed chair speech, crude oil prices: 7 key things that changed for India"
- COALINDIA.NS (COAL INDIA LTD) score 82.2 — "CANADA ADDS 50% TARIFFS TO US COPPER WIRE, WOOD CHARCOAL"
- INOXINDIA.NS (INOX INDIA LIMITED) score 81.3 — "Morgan Advanced Materials exits Foseco India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 79.6 — "Morgan Advanced Materials exits Foseco India"
- BAC (Bank of America Corporation) score 70.2 — "TRUMP SAYS TO RENAME LAKE ONTARIO TO LAKE AMERICA"
- HDB (HDFC Bank Limited) score 64.6 — "Kotak Bank Share Price Live Updates: Kotak Bank's Price and EMA3 Overview"
- IDBI.NS (IDBI BANK LIMITED) score 60.9 — "Kotak Bank Share Price Live Updates: Kotak Bank's Price and EMA3 Overview"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 60.9 — "Kotak Bank Share Price Live Updates: Kotak Bank's Price and EMA3 Overview"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 60.9 — "Kotak Bank Share Price Live Updates: Kotak Bank's Price and EMA3 Overview"
- TECHM.NS (TECH MAHINDRA LIMITED) score 55.0 — "HCL Tech Share Price Live Updates: HCL Tech Sees a -2.76% Drop in Weekly Returns"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 53.5 — "HCL Tech Share Price Live Updates: HCL Tech Sees a -2.76% Drop in Weekly Returns"
- TECH (Bio-Techne Corp) score 53.5 — "HCL Tech Share Price Live Updates: HCL Tech Sees a -2.76% Drop in Weekly Returns"
- COIN (Coinbase Global, Inc.) score 50.4 — "Global Market: South Korean shares fall as AI trade loses steam, investors eye Jackson Hol"
- OHI (Omega Healthcare Investors, In) score 49.8 — "BITCOIN ETF INFLOWS HIT 10-MONTH HIGH Investors poured $2.5B into spot Bitcoin ETFs over t"
- BOND (PIMCO Active Bond Exchange-Tra) score 48.9 — "U.S. TREASURY OFFICIAL: BOND YIELDS WILL FALL AS INFLATION COOLS OVER TIME, TRUMP ADMINIST"
- NVDA (NVIDIA Corporation) score 40.8 — "NVIDIA TO START EMPLOYEE-FUNDED U.S. POLITICAL ACTION COMMITTEE CALLED NVPAC - SOURCE FAMI"
- LTH (Life Time Group Holdings, Inc.) score 35.8 — "U.S. TREASURY OFFICIAL: BOND YIELDS WILL FALL AS INFLATION COOLS OVER TIME, TRUMP ADMINIST"
- CHKP (Check Point Software Technolog) score 32.8 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 2"
- 301077.SZ (CHINASTARS) score 27.2 — "China-Nepal floods: debris lake the size of 1,000 Olympic pools in breach danger"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.8 — "TRUMP MET WITH ENERGY, EPA AND AGRI SECRETARIES ON WEDNESDAY AND DISCUSSED PENDING APPLICA"
- JIOFIN.BO (Jio Financial Services Limited) score 19.3 — "All eyes on Skyways Air Services IPO allotment status, listing date as GMP jumps at  ₹44/s"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 18.6 — "US Stock Market: Build-A-Bear shares plunge after retailer cuts revenue outlook, fires gro"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 15.8 — "Tata Motors PV Share Price Live Updates: Tata Motors PV Current Price and Change"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 15.6 — "Tata Motors PV Share Price Live Updates: Tata Motors PV Current Price and Change"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 15.4 — "Bajaj Finance Share Price Live Updates: Bajaj Finance's Market Position Update"
- MS (Morgan Stanley) score 14.8 — "Morgan Advanced Materials exits Foseco India"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 11.8 — "Copper’s record run is sending three clear messages about the state of financial markets t"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 11.7 — "CANADA ADDS 50% TARIFFS TO US COPPER WIRE, WOOD CHARCOAL"
- META (Meta) score 11.5 — "Gold rate today: Precious metal rises 12% this month. Is it the right time to buy gold?"
- PCJEWELLER.NS (PC JEWELLER LTD) score 11.1 — "Deepa Jewellers IPO: ₹460-cr issue to open on September 1, price band fixed at ₹168-177"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 11.0 — "Motilal Oswal initiates coverage on Adani Enterprises with Buy, sees 25% upside. Here’s wh"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 8.5 — "ICICI Bank Share Price Live Updates: ICICI Bank's Current Trading Price"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 6.7 — "Lenskart shares fall 1.5% after Rs 1,856 crore stake change hands in block deal, Alpha Wav"
- VT (Vanguard Total World Stock Ind) score 5.9 — "Bill Gates lists 3 big risks to AI shift. Is the world heading towards turbulent times?"
- JUSTDIAL.BO (JUST DIAL LTD.) score 5.6 — "I just had my first baby and don’t want to go back to work. Is quitting for a year a bad i"
- DKS (Dick's Sporting Goods Inc) score 3.5 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- MRNA (Moderna, Inc.) score 2.7 — "Can Wolfe’s upgrade push Moderna stock higher?"
- VOLTAS.NS (VOLTAS LTD) score 0.4 — "Voltas reported strong growth in June quarter, but failed to impress"
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