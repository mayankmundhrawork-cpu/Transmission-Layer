# Transmission Layer — board brief · 2026-08-17 14:42Z

data as of **2026-08-17** · 98 series · 10 red / 36 amber · 8 events surfaced (22 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.149, 2d in regime; vol-pct 0.235, breadth-off 0.062, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.34, corr60 -0.39, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.88, corr60 0.86, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.26, corr60 0.34, last shift 2026-07-01. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.2, corr60 -0.11, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.72, corr60 -0.82, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.1, corr60 -0.12, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.31, corr60 -0.2, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.02, corr60 0.23, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.0003306779614402622)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.49** (n=1117) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.829** (n=2423) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.27] cross-asset · 13 series ↑
- comex_gold [COMMODITIES]: last 4476.70, z20 2.11, zc 1.70, resid-z -0.69 [priced], 1d 2.20%, |z20|=2.11; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 66.22, z20 1.86, zc 0.85, resid-z -0.88 [quiet], 1d 1.90%, |z20|=1.86; co-occur[gold_silver] same-direction (channel VALID)
- dyn_nvda [EQUITIES]: last 226.85, z20 1.54, zc 0.32, resid-z -0.34 [quiet], 1d 0.75%, 1y-pct=99
- russell_2000 [INDICES]: last 3057.50, z20 1.50, zc -0.31, resid-z -0.14 [quiet], 1d -0.36%, 1y-pct=99
- nasdaq_100 [INDICES]: last 30102.72, z20 1.43, zc 0.15, resid-z 0.20 [quiet], 1d 0.19%, 1y-pct=96
- dyn_vt [EQUITIES]: last 162.35, z20 1.43, zc 0.08, resid-z -0.85 [quiet], 1d 0.06%, 1y-pct=99
- gold_silver_ratio [DERIVED]: last 67.60, z20 -1.19, zc n/a, resid-z n/a [quiet], 1d 0.29%, GSR<75 (extreme low)
- sp500 [INDICES]: last 7771.86, z20 1.18, zc -0.23, resid-z 0.78 [quiet], 1d -0.18%, 1y-pct=99
- dax [INDICES]: last 26404.85, z20 1.18, zc -0.18, resid-z -0.28 [quiet], 1d -0.13%, 1y-pct=99
- stoxx_50 [INDICES]: last 6539.19, z20 1.16, zc -0.01, resid-z -0.02 [quiet], 1d -0.01%, 1y-pct=98
- comex_copper [COMMODITIES]: last 6.62, z20 0.95, zc 0.13, resid-z 0.13 [quiet], 1d 0.29%, 1y-pct=98
- dow_jones [INDICES]: last 53518.48, z20 0.57, zc -0.56, resid-z -0.82 [quiet], 1d -0.40%, 1y-pct=96
- cac_40 [INDICES]: last 8592.76, z20 0.35, zc -0.71, resid-z -0.86 [quiet], 1d -0.51%, 1y-pct=95
- **Mechanism**: cross-asset · 13 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-11-26 (z-distance 0.92).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.517 via comex_silver, z 0.93, quiet); nifty_midcap_100 (rho 0.492 via dax, z 1.0, reacted); nifty_fmcg (rho -0.489 via dyn_nvda, z -2.91, reacted); nifty_50 (rho 0.489 via cac_40, z -0.13, quiet); dyn_stylebaaza_ns (rho -0.365 via gold_silver_ratio, z 2.57, reacted)
- Watch next: brent (inverse) — not yet - watch; rho -0.639 vs dow_jones, historically leads by 3d
- Watch next: vix (inverse) — not yet - watch; rho -0.637 vs dyn_nvda, historically leads by 3d
- Watch next: ust_10y (inverse) — not yet - watch; rho -0.63 vs russell_2000, historically leads by 1d
- Watch next: wti (inverse) — not yet - watch; rho -0.599 vs dow_jones, historically leads by 2d
- Watch next: tips_10y_real (inverse) — not yet - watch; rho -0.584 vs russell_2000, historically leads by 5d
- **India receivers**: nifty_metal (rho 0.517, z 0.93); nifty_midcap_100 (rho 0.492, z 1.0); nifty_fmcg (rho -0.489, z -2.91); nifty_50 (rho 0.489, z -0.13)
- Source: Positive inflows into gold ETFs continue for the 4th week in a row — BusinessLine Mkts, 2026-08-17. https://www.thehindubusinessline.com/markets/gold/positive-inflows-into-gold-etfs-continue-for-the-4th-week-in-a-row/article71356676.ece
- Source: US stocks: S&P 500 opens muted as Middle East tensions weigh — ET Markets, 2026-08-17. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-sp-500-opens-muted-as-middle-east-tensions-weigh/articleshow/133298963.cms
- Source: US stock market today: S&P 500, Dow futures steady after 3-week winning streak; oil rises on Hormuz risks — Mint Markets, 2026-08-17. https://www.livemint.com/market/stock-market-news/us-stock-market-today-s-p-500-dow-futures-steady-after-3-week-winning-streak-oil-rises-on-hormuz-risks-11786969512356.html
- Historical analogues: 2024-11-26 (d=0.92), 2025-10-31 (d=1.01), 2024-10-15 (d=1.11)

### [RED 6.5] fx · 4 series ↑
- aud_usd [FX]: last 0.71, z20 2.83, zc 1.83, resid-z 1.71 [unexplained], 1d 0.80%, |z20|=2.83
- gbp_usd [FX]: last 1.36, z20 1.87, zc 1.20, resid-z 1.06 [quiet], 1d 0.50%, |z20|=1.87
- usd_mxn [FX]: last 17.03, z20 -1.82, zc -0.05, resid-z -0.05 [quiet], 1d -0.02%, |z20|=1.82; 1y-pct=0
- eur_usd [FX]: last 1.16, z20 1.66, zc 1.47, resid-z 1.32 [quiet], 1d 0.49%, |z20|=1.66
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.548 via usd_mxn, z -0.87, quiet); eur_inr (rho 0.481 via gbp_usd, z 3.28, reacted); dyn_icicigi_bo (rho -0.419 via gbp_usd, z -0.43, quiet); nifty_midcap_100 (rho -0.355 via usd_mxn, z 1.0, reacted)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.508 vs aud_usd, historically leads by 5d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.511 vs eur_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.548, z -0.87); eur_inr (rho 0.481, z 3.28); dyn_icicigi_bo (rho -0.419, z -0.43); nifty_midcap_100 (rho -0.355, z 1.0)
- Source: Global Market: Euro zone bond yields hover near 15-year highs as Middle East war fuels inflation fears — ET Markets, 2026-08-17. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-bond-yields-hover-near-15-year-highs-as-middle-east-war-fuels-inflation-fears/articleshow/133293555.cms
- Source: Philip R. Lane: The rise in defence spending and the euro area economy — ECB press, 2026-08-17. https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260817~1f9f7149c9.en.pdf
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 5.12] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.63, z20 2.12, zc n/a, resid-z n/a [quiet], 1d 0.37%, 52-wk extreme (pct=99); |z20|=2.12; 1y-pct=99
- **Mechanism**: The midcap_largecap_ratio has reached a 52-week extreme, with a z20 level of 1.77, indicating a significant move. However, the resid_z is None, suggesting that this move is largely priced in by factor exposures. The RISK_ON regime and VALID vix_equity_inverse channel suggest that the market is positioned for a potential drawdown, but the midcap_largecap_ratio's move may not be an anomaly.
- **Gap**: No gap: the midcap_largecap_ratio's move is largely priced in by factor exposures, as indicated by the None resid_z value
- **India take**: The Nifty Midcap 100 index, which has a correlation of 0.531 with the midcap_largecap_ratio, has not yet reacted and is a potential responder. Other Indian transmission candidates like Dyn Bharatcoal NS and Dyn Fincables NS have already reacted.
- Watch next: nifty_midcap_100 (down) — not yet - watch; historically leads by 2d
- **India receivers**: nifty_midcap_100 (rho 0.533, z 1.0); dyn_bharatcoal_ns (rho 0.42, z -1.1); dyn_fincables_ns (rho 0.408, z 2.68); dyn_pcjeweller_ns (rho 0.374, z 0.66)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 4.81] commodities · 2 series ↑
- corn [COMMODITIES]: last 485.25, z20 3.98, zc 4.47, resid-z 3.59 [unexplained], 1d 5.72%, |z20|=3.98; 1y-pct=100
- wheat [COMMODITIES]: last 689.00, z20 1.49, zc 1.09, resid-z 0.78 [quiet], 1d 2.11%, 1y-pct=99
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_lenskart_ns (rho 0.388 via wheat, z 2.27, reacted)
- Watch next: soybeans (co-move) — not yet - watch; rho 0.74 vs corn
- **India receivers**: dyn_lenskart_ns (rho 0.388, z 2.27)
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [RED 4.57] dyn_stylebaaza_ns ↑
- dyn_stylebaaza_ns [EQUITIES]: last 383.50, z20 2.57, zc 1.37, resid-z 1.69 [unexplained], 1d 5.00%, |z20|=2.57
- **Mechanism**: dyn_stylebaaza_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_pcjeweller_ns (rho 0.439 via dyn_stylebaaza_ns, z 0.66, quiet); dyn_bharatcoal_ns (rho 0.402 via dyn_stylebaaza_ns, z -1.1, reacted); dyn_adanient_bo (rho 0.392 via dyn_stylebaaza_ns, z -0.53, quiet); dyn_fincables_ns (rho 0.376 via dyn_stylebaaza_ns, z 2.68, reacted); nifty_midcap_100 (rho 0.362 via dyn_stylebaaza_ns, z 1.0, reacted)
- **India receivers**: dyn_pcjeweller_ns (rho 0.439, z 0.66); dyn_bharatcoal_ns (rho 0.402, z -1.1); dyn_adanient_bo (rho 0.392, z -0.53); dyn_fincables_ns (rho 0.376, z 2.68)
- Source: FCNR(B) inflows stabilise rupee but fail to trigger 2013-style rally — BusinessLine Mkts, 2026-08-17. https://www.thehindubusinessline.com/markets/forex/fcnrb-inflows-stabilise-rupee-but-fail-to-trigger-2013-style-rally/article71356433.ece
- Source: Halwasiya buys 45 lakh shares of Baazar Style Retail for ₹163 crore in block deal — BusinessLine Mkts, 2026-08-17. https://www.thehindubusinessline.com/markets/stock-markets/halwasiya-buys-45-lakh-shares-of-baazar-style-retail-for-163-crore-in-block-deal/article71355344.ece
- Source: Baazar Style Retail shares hit 5% upper circuit on reports of Aditya Halwasia buying company shares worth  ₹163 crore — Mint Markets, 2026-08-17. https://www.livemint.com/market/stock-market-news/baazar-style-retail-shares-hit-5-upper-circuit-on-reports-of-aditya-halwasia-buying-company-shares-worth-163-crore-11786948034095.html
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-04 (d=0.01), 2025-02-20 (d=0.02)

### [AMBER 4.36] dxy ↓
- dxy [FX]: last 99.45, z20 -1.36, zc -0.68, resid-z 0.10 [quiet], 1d -0.22%, 20d range extreme
- **Mechanism**: The recent decline in the US Dollar Index (DXY) may propagate through the metal_copper_channel, a VALID channel, potentially leading to a move in Indian metal equities. The DXY decline, although priced with a small resid_z of 0.1, could still influence global copper prices, which in turn affect Indian metal equities. The VALID gold_silver_comove channel also suggests that monetary metals may co-move, potentially impacting the Indian market.
- **Gap**: No gap: The DXY move is priced with a small resid_z of 0.1, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is likely to be the Indian metal equities, such as Hindalco or Tata Steel, which may react to the potential move in global copper prices. However, the reaction has not occurred yet.
- Watch next: comex_gold (down) — not yet - watch; Historical analogues show a median decline of 1.82% in comex_gold 20 days after a similar DXY decline
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [AMBER 4.16] dyn_tech ↑
- dyn_tech [EQUITIES]: last 72.49, z20 2.16, zc 0.05, resid-z -0.38 [quiet], 1d 0.12%, |z20|=2.16; 1y-pct=100
- **Mechanism**: dyn_tech ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_inoxindia_ns (rho -0.387 via dyn_tech, z -0.16, quiet)
- **India receivers**: dyn_inoxindia_ns (rho -0.387, z -0.16)
- Source: Stanley Druckenmiller ditched these chip plays before the selloff. Here’s how he’s playing the tech sector now. — MarketWatch Top, 2026-08-17. https://www.marketwatch.com/story/stanley-druckenmiller-ditched-these-chip-plays-before-the-selloff-heres-how-hes-playing-the-tech-sector-now-9115c06f?mod=mw_rss_topstories
- Source: US stocks mixed as Iran tensions weigh, Anthropic outlook lifts tech stocks — Mint Markets, 2026-08-17. https://www.livemint.com/market/stock-market-news/us-stocks-mixed-as-iran-tensions-weigh-anthropic-outlook-lifts-tech-stocks-11786974172565.html
- Source: Broker’s Call: Endurance Tech (Buy) — BusinessLine Mkts, 2026-08-17. https://www.thehindubusinessline.com/markets/brokers-call-endurance-tech-buy/article71355597.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.0), 2025-05-19 (d=0.0)

### [AMBER 3.95] dyn_bac ↑
- dyn_bac [EQUITIES]: last 64.94, z20 1.95, zc 0.49, resid-z -1.09 [quiet], 1d 0.71%, 1y-pct=100
- **Mechanism**: dyn_bac ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.632 vs dyn_bac, historically leads by 2d
- Watch next: cac_40 (co-move) — not yet - watch; rho 0.53 vs dyn_bac, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.572 vs dyn_bac
- Source: BOFA: THE TRADE IS LONG GOLD Bank of America strategist Michael Hartnett says gold remains the best hedge against dollar weakness, bond losses and asset inflation. Gold funds attracted $6.3B last week, the largest inflow since January 2026. Hartnett’s “Anything But Dollar” — DeItaone, 2026-08-17. https://t.me/walter_bloomberg/34770
- Source: CLAUDE TOPS AI RANKINGS AS COSTS FALL Bank of America launched its Frontier AI Tracker, monitoring model intelligence, usage, token prices and hardware costs. Anthropic’s Claude Opus 5 ranks #1 for intelligence, followed by Claude Fable 5 and OpenAI’s GPT-5.6 Sol. DeepSeek — DeItaone, 2026-08-17. https://t.me/walter_bloomberg/34757
- Source: Just 7% of America’s Nuclear Fuel Comes From Home — OilPrice, 2026-08-15. https://oilprice.com/Alternative-Energy/Nuclear-Power/Just-7-of-Americas-Nuclear-Fuel-Comes-From-Home.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

## Watchlist (below surfacing floor)
cross-asset · 2 series ↑ (3.45), eur_inr ↑ (3.28), dyn_lth ↑ (3.27), dyn_tatatech_ns ↑ (3.01), indices · 2 series ↑ (2.95), nifty_fmcg ↓ (2.91), dyn_coin ↓ (2.8), usd_cny ↓ (2.69), dyn_fincables_ns ↑ (2.68), dyn_icicigi_bo ↓ (2.43), indices · 2 series ↑ (2.37), dyn_lenskart_ns ↑ (2.27)

## India macro
- nifty_50: 24287.6504 (1d -0.32%, z20 -0.13, flag none)
- nifty_midcap_100: 63814.1484 (1d 0.05%, z20 1.00, flag amber)
- usd_inr: 95.5920 (1d 0.20%, z20 -0.28, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6274 (1d 0.37%, z20 2.12, flag red)
- Next India prints: NSDL FPI flows T-0d · India trade / CAD data T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 87.5 — "Wealth creation expands beyond metros: Julius Baer India"
- INOXINDIA.NS (INOX INDIA LIMITED) score 87.0 — "Wealth creation expands beyond metros: Julius Baer India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 86.8 — "Wealth creation expands beyond metros: Julius Baer India"
- INDIANB.NS (INDIAN BANK) score 56.6 — "BOFA: THE TRADE IS LONG GOLD Bank of America strategist Michael Hartnett says gold remains"
- TECHM.NS (TECH MAHINDRA LIMITED) score 43.2 — "US stocks mixed as Iran tensions weigh, Anthropic outlook lifts tech stocks"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 41.7 — "US stocks mixed as Iran tensions weigh, Anthropic outlook lifts tech stocks"
- TECH (Bio-Techne Corp) score 41.4 — "US stocks mixed as Iran tensions weigh, Anthropic outlook lifts tech stocks"
- BAC (Bank of America Corporation) score 40.7 — "BOFA: THE TRADE IS LONG GOLD Bank of America strategist Michael Hartnett says gold remains"
- COIN (Coinbase Global, Inc.) score 39.3 — "Global Market: European shares climb despite geopolitical risks; miners lead gains"
- OHI (Omega Healthcare Investors, In) score 36.8 — "Quote of the day by Robert Shiller: "The problem with the markets is that they are just li"
- CHKP (Check Point Software Technolog) score 35.0 — "Horizon Industrial Parks’ Rs 2,600 crore IPO opens. Check GMP, price band and other key de"
- HDB (HDFC Bank Limited) score 34.3 — "BOFA: THE TRADE IS LONG GOLD Bank of America strategist Michael Hartnett says gold remains"
- IDBI.NS (IDBI BANK LIMITED) score 32.1 — "BOFA: THE TRADE IS LONG GOLD Bank of America strategist Michael Hartnett says gold remains"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 32.1 — "BOFA: THE TRADE IS LONG GOLD Bank of America strategist Michael Hartnett says gold remains"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 32.0 — "BOFA: THE TRADE IS LONG GOLD Bank of America strategist Michael Hartnett says gold remains"
- LTH (Life Time Group Holdings, Inc.) score 27.6 — "TRUMP’S MONDAY SCHEDULE President Trump’s schedule for Monday, August 17: 🔸 8:00 AM — Exec"
- BOND (PIMCO Active Bond Exchange-Tra) score 24.9 — "BOFA: THE TRADE IS LONG GOLD Bank of America strategist Michael Hartnett says gold remains"
- 301077.SZ (CHINASTARS) score 23.6 — "Rice exporters seek Goyal’s intervention on China’s allegation of GMO presence in shipment"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 21.1 — "Top Gainers & Losers on 17 August: NMDC Steel, LG Electronics, BSE, Tata Tech, Infosys, Vo"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 19.2 — "Top Gainers & Losers on 17 August: NMDC Steel, LG Electronics, BSE, Tata Tech, Infosys, Vo"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 17.8 — "UK Inflation Set to Rebound as Energy Bills Surge"
- JIOFIN.BO (Jio Financial Services Limited) score 15.9 — "Getting diagnosed with dementia isn’t the end. It’s a time to take financial action."
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 11.5 — "Coal India Share Price Live Updates: Coal India  Price and Volume Overview"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 11.0 — "Getting diagnosed with dementia isn’t the end. It’s a time to take financial action."
- PCJEWELLER.NS (PC JEWELLER LTD) score 10.0 — "Lalithaa Jewellery IPO Day 1: Subscribed 0.69x so far"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 10.0 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Trading Update"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.9 — "Quote of the day by Robert Shiller: "The problem with the markets is that they are just li"
- MS (Morgan Stanley) score 9.4 — "PRICE TARGET CUT • $AEP: PT cut to $139 from $146 by Truist Securities • $AMTM: PT cut to "
- BHARATFORG.BO (BHARAT FORGE LTD.) score 6.4 — "Cement makers face a forgettable H1FY27 as prices weaken and costs rise"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.7 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ News"
- NVDA (NVIDIA Corporation) score 5.6 — "NVDA - NVIDIA EYES $3 BILLION SB ENERGY INVESTMENT Nvidia is reportedly in talks to invest"
- META (Meta) score 4.7 — "Pulse of the Street: Tata jitters, metal rout weigh on Indian equities"
- AAPL (Apple Inc.) score 3.8 — "AAPL - APPLE UPGRADED TO BUY — $400 TARGET Rothschild Redburn upgraded Apple from Neutral "
- VT (Vanguard Total World Stock Ind) score 3.7 — "Neighbors in rural Texas county are not happy about Elon Musk’s plan to erect world’s larg"
- RDDT (Reddit, Inc.) score 2.9 — "Reddit shares surge 14% on S&P 500 inclusion, replacing AvalonBay"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 2.9 — "FCNR(B) inflows stabilise rupee but fail to trigger 2013-style rally"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 2.3 — "Lenskart shares soar after strong Q1 results and MSCI inclusion buzz"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 2.1 — "ICICI Bank Share Price Live Updates: ICICI Bank's Market Movement Today"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.9 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
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