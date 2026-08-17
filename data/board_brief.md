# Transmission Layer — board brief · 2026-08-17 16:43Z

data as of **2026-08-17** · 98 series · 10 red / 36 amber · 8 events surfaced (21 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.149, 2d in regime; vol-pct 0.235, breadth-off 0.062, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.34, corr60 -0.39, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.88, corr60 0.86, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.26, corr60 0.34, last shift 2026-07-01. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.2, corr60 -0.11, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.72, corr60 -0.82, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.11, corr60 -0.11, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.31, corr60 -0.2, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.01, corr60 0.23, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.0017480630312631806)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.49** (n=1117) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.829** (n=2423) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.42] cross-asset · 13 series ↑
- comex_gold [COMMODITIES]: last 4480.30, z20 2.13, zc 1.76, resid-z -0.69 [priced], 1d 2.28%, |z20|=2.13; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 66.46, z20 1.93, zc 1.01, resid-z -0.76 [quiet], 1d 2.26%, |z20|=1.93; co-occur[gold_silver] same-direction (channel VALID)
- russell_2000 [INDICES]: last 3060.44, z20 1.56, zc -0.22, resid-z 0.02 [quiet], 1d -0.26%, |z20|=1.56; 1y-pct=99
- dyn_nvda [EQUITIES]: last 226.78, z20 1.54, zc 0.30, resid-z -0.34 [quiet], 1d 0.72%, 1y-pct=99
- nasdaq_100 [INDICES]: last 30102.18, z20 1.43, zc 0.15, resid-z 0.20 [quiet], 1d 0.19%, 1y-pct=96
- dyn_vt [EQUITIES]: last 162.33, z20 1.42, zc 0.06, resid-z -0.85 [quiet], 1d 0.05%, 1y-pct=99
- gold_silver_ratio [DERIVED]: last 67.42, z20 -1.35, zc n/a, resid-z n/a [quiet], 1d 0.02%, GSR<75 (extreme low)
- sp500 [INDICES]: last 7770.89, z20 1.17, zc -0.25, resid-z 0.78 [quiet], 1d -0.19%, 1y-pct=99
- stoxx_50 [INDICES]: last 6538.73, z20 1.16, zc -0.02, resid-z 0.00 [quiet], 1d -0.01%, 1y-pct=98
- dax [INDICES]: last 26370.39, z20 1.12, zc -0.36, resid-z -0.39 [quiet], 1d -0.26%, 1y-pct=99
- comex_copper [COMMODITIES]: last 6.61, z20 0.91, zc 0.09, resid-z 0.12 [quiet], 1d 0.20%, 1y-pct=98
- dow_jones [INDICES]: last 53567.53, z20 0.62, zc -0.43, resid-z -0.58 [quiet], 1d -0.31%, 1y-pct=96
- cac_40 [INDICES]: last 8585.62, z20 0.30, zc -0.82, resid-z -0.93 [quiet], 1d -0.59%, 1y-pct=95
- **Mechanism**: cross-asset · 13 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-11-26 (z-distance 0.92).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.519 via comex_silver, z 0.93, quiet); nifty_midcap_100 (rho 0.491 via dax, z 1.0, reacted); nifty_fmcg (rho -0.489 via dyn_nvda, z -2.91, reacted); nifty_50 (rho 0.489 via cac_40, z -0.13, quiet); dyn_stylebaaza_ns (rho 0.455 via comex_silver, z 2.57, reacted)
- Watch next: brent (inverse) — not yet - watch; rho -0.639 vs dow_jones, historically leads by 3d
- Watch next: ust_10y (inverse) — not yet - watch; rho -0.63 vs russell_2000, historically leads by 1d
- Watch next: wti (inverse) — not yet - watch; rho -0.601 vs dow_jones, historically leads by 2d
- Watch next: tips_10y_real (inverse) — not yet - watch; rho -0.585 vs russell_2000, historically leads by 5d
- Watch next: btc_usd (co-move) — not yet - watch; rho 0.552 vs comex_gold, historically leads by 5d
- **India receivers**: nifty_metal (rho 0.519, z 0.93); nifty_midcap_100 (rho 0.491, z 1.0); nifty_fmcg (rho -0.489, z -2.91); nifty_50 (rho 0.489, z -0.13)
- Source: Apple’s stock could rise 30% if it strikes an Nvidia deal for AI, this analyst says — MarketWatch Top, 2026-08-17. https://www.marketwatch.com/story/apples-stock-could-rise-30-if-it-strikes-an-nvidia-deal-for-ai-this-analyst-says-f5f5c861?mod=mw_rss_topstories
- Source: Market Trading Guide: Hindustan Copper among 2 stock recommendations for Tuesday — ET Markets, 2026-08-17. https://economictimes.indiatimes.com/markets/stocks/news/market-trading-guide-hindustan-copper-among-2-stock-recommendations-for-tuesday/articleshow/133300251.cms
- Source: SPOT GOLD RISES 1% TO $4,419.79/OZ — DeItaone, 2026-08-17. https://t.me/walter_bloomberg/34798
- Historical analogues: 2024-11-26 (d=0.92), 2025-10-31 (d=1.01), 2024-10-15 (d=1.11)

### [RED 6.41] fx · 4 series ↑
- aud_usd [FX]: last 0.71, z20 2.75, zc 1.73, resid-z 1.62 [unexplained], 1d 0.76%, |z20|=2.75
- gbp_usd [FX]: last 1.36, z20 1.96, zc 1.31, resid-z 1.18 [quiet], 1d 0.55%, |z20|=1.96
- usd_mxn [FX]: last 17.02, z20 -1.90, zc -0.22, resid-z -0.18 [quiet], 1d -0.08%, |z20|=1.90; 1y-pct=0
- eur_usd [FX]: last 1.16, z20 1.70, zc 1.54, resid-z 1.43 [moved], 1d 0.51%, |z20|=1.70
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.55 via usd_mxn, z -0.87, quiet); eur_inr (rho 0.482 via gbp_usd, z 3.38, reacted); dyn_icicigi_bo (rho -0.417 via gbp_usd, z -0.43, quiet); nifty_midcap_100 (rho -0.355 via usd_mxn, z 1.0, reacted)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.508 vs aud_usd, historically leads by 5d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.505 vs eur_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.55, z -0.87); eur_inr (rho 0.482, z 3.38); dyn_icicigi_bo (rho -0.417, z -0.43); nifty_midcap_100 (rho -0.355, z 1.0)
- Source: Global Market: Euro zone bond yields hover near 15-year highs as Middle East war fuels inflation fears — ET Markets, 2026-08-17. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-bond-yields-hover-near-15-year-highs-as-middle-east-war-fuels-inflation-fears/articleshow/133293555.cms
- Source: Philip R. Lane: The rise in defence spending and the euro area economy — ECB press, 2026-08-17. https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260817~1f9f7149c9.en.pdf
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 5.79] commodities · 3 series ↑
- corn [COMMODITIES]: last 489.75, z20 4.48, zc 5.23, resid-z 4.19 [unexplained], 1d 6.70%, |z20|=4.48; 1y-pct=100
- wheat [COMMODITIES]: last 688.75, z20 1.48, zc 1.07, resid-z 0.79 [quiet], 1d 2.07%, 1y-pct=99
- soybeans [COMMODITIES]: last 1213.50, z20 0.87, zc 3.34, resid-z 3.13 [unexplained], 1d 3.39%, 1y-pct=97
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_lenskart_ns (rho 0.388 via wheat, z 2.27, reacted)
- **India receivers**: dyn_lenskart_ns (rho 0.388, z 2.27)
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [RED 5.12] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.63, z20 2.12, zc n/a, resid-z n/a [quiet], 1d 0.37%, 52-wk extreme (pct=99); |z20|=2.12; 1y-pct=99
- **Mechanism**: The midcap_largecap_ratio has reached a 52-week extreme, with a z20 level of 1.77, indicating a significant move. However, the resid_z is None, suggesting that this move is largely priced in by factor exposures. The RISK_ON regime and VALID vix_equity_inverse channel suggest that the market is positioned for a potential drawdown, but the midcap_largecap_ratio's move may not be an anomaly.
- **Gap**: No gap: the midcap_largecap_ratio's move is largely priced in by factor exposures, as indicated by the None resid_z value
- **India take**: The Nifty Midcap 100 index, which has a correlation of 0.531 with the midcap_largecap_ratio, has not yet reacted and is a potential responder. Other Indian transmission candidates like Dyn Bharatcoal NS and Dyn Fincables NS have already reacted.
- Watch next: nifty_midcap_100 (down) — not yet - watch; historically leads by 2d
- **India receivers**: nifty_midcap_100 (rho 0.533, z 1.0); dyn_bharatcoal_ns (rho 0.42, z -1.1); dyn_fincables_ns (rho 0.408, z 2.68); dyn_pcjeweller_ns (rho 0.374, z 0.66)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

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

### [AMBER 4.29] dxy ↓
- dxy [FX]: last 99.49, z20 -1.29, zc -0.54, resid-z 0.10 [quiet], 1d -0.18%, 20d range extreme
- **Mechanism**: The recent decline in the US Dollar Index (DXY) may propagate through the metal_copper_channel, a VALID channel, potentially leading to a move in Indian metal equities. The DXY decline, although priced with a small resid_z of 0.1, could still influence global copper prices, which in turn affect Indian metal equities. The VALID gold_silver_comove channel also suggests that monetary metals may co-move, potentially impacting the Indian market.
- **Gap**: No gap: The DXY move is priced with a small resid_z of 0.1, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is likely to be the Indian metal equities, such as Hindalco or Tata Steel, which may react to the potential move in global copper prices. However, the reaction has not occurred yet.
- Watch next: comex_gold (down) — not yet - watch; Historical analogues show a median decline of 1.82% in comex_gold 20 days after a similar DXY decline
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [AMBER 3.84] dyn_bac ↑
- dyn_bac [EQUITIES]: last 64.81, z20 1.84, zc 0.34, resid-z -1.09 [quiet], 1d 0.50%, 1y-pct=100
- **Mechanism**: dyn_bac ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: cac_40 (co-move) — not yet - watch; rho 0.533 vs dyn_bac, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.575 vs dyn_bac
- Source: BOFA: THE TRADE IS LONG GOLD Bank of America strategist Michael Hartnett says gold remains the best hedge against dollar weakness, bond losses and asset inflation. Gold funds attracted $6.3B last week, the largest inflow since January 2026. Hartnett’s “Anything But Dollar” — DeItaone, 2026-08-17. https://t.me/walter_bloomberg/34770
- Source: CLAUDE TOPS AI RANKINGS AS COSTS FALL Bank of America launched its Frontier AI Tracker, monitoring model intelligence, usage, token prices and hardware costs. Anthropic’s Claude Opus 5 ranks #1 for intelligence, followed by Claude Fable 5 and OpenAI’s GPT-5.6 Sol. DeepSeek — DeItaone, 2026-08-17. https://t.me/walter_bloomberg/34757
- Source: Just 7% of America’s Nuclear Fuel Comes From Home — OilPrice, 2026-08-15. https://oilprice.com/Alternative-Energy/Nuclear-Power/Just-7-of-Americas-Nuclear-Fuel-Comes-From-Home.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

### [AMBER 3.79] dyn_tech ↑
- dyn_tech [EQUITIES]: last 72.40, z20 1.79, zc 0.00, resid-z -0.38 [quiet], 1d 0.01%, 1y-pct=100
- **Mechanism**: dyn_tech ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_inoxindia_ns (rho -0.387 via dyn_tech, z -0.16, quiet)
- **India receivers**: dyn_inoxindia_ns (rho -0.387, z -0.16)
- Source: Stanley Druckenmiller ditched these chip plays before the selloff. Here’s how he’s playing the tech sector now. — MarketWatch Top, 2026-08-17. https://www.marketwatch.com/story/stanley-druckenmiller-ditched-these-chip-plays-before-the-selloff-heres-how-hes-playing-the-tech-sector-now-9115c06f?mod=mw_rss_topstories
- Source: ECB WARNS AI BOOM COULD END IN CORRECTION ECB economists warn stock-market valuations may be heading for a correction as enthusiasm around AI pushes tech valuations toward dot-com bubble levels. Unlike the early 2000s, policymakers have less room to cut rates or deploy fiscal — DeItaone, 2026-08-17. https://t.me/walter_bloomberg/34797
- Source: US stocks mixed as Iran tensions weigh, Anthropic outlook lifts tech stocks — Mint Markets, 2026-08-17. https://www.livemint.com/market/stock-market-news/us-stocks-mixed-as-iran-tensions-weigh-anthropic-outlook-lifts-tech-stocks-11786974172565.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.0), 2025-05-19 (d=0.0)

## Watchlist (below surfacing floor)
cross-asset · 2 series ↑ (3.5), eur_inr ↑ (3.38), dyn_lth ↑ (3.22), dyn_tatatech_ns ↑ (3.01), indices · 2 series ↑ (2.95), nifty_fmcg ↓ (2.91), dyn_fincables_ns ↑ (2.68), usd_cny ↓ (2.66), dyn_icicigi_bo ↓ (2.43), indices · 2 series ↑ (2.37), dyn_lenskart_ns ↑ (2.27), bovespa ↓ (1.88)

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
- COALINDIA.NS (COAL INDIA LTD) score 87.8 — "ICICI Bank raises $750 million as Indian banks tap dollar bond market"
- INOXINDIA.NS (INOX INDIA LIMITED) score 87.3 — "ICICI Bank raises $750 million as Indian banks tap dollar bond market"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 87.2 — "ICICI Bank raises $750 million as Indian banks tap dollar bond market"
- INDIANB.NS (INDIAN BANK) score 56.5 — "ICICI Bank raises $750 million as Indian banks tap dollar bond market"
- TECHM.NS (TECH MAHINDRA LIMITED) score 44.4 — "S&P 500 REVENUE GROWTH HITS 5-YEAR HIGH Goldman Sachs says S&P 500 revenues grew 6.4% YoY "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 42.9 — "S&P 500 REVENUE GROWTH HITS 5-YEAR HIGH Goldman Sachs says S&P 500 revenues grew 6.4% YoY "
- TECH (Bio-Techne Corp) score 42.6 — "S&P 500 REVENUE GROWTH HITS 5-YEAR HIGH Goldman Sachs says S&P 500 revenues grew 6.4% YoY "
- BAC (Bank of America Corporation) score 40.9 — "ICICI Bank raises $750 million as Indian banks tap dollar bond market"
- OHI (Omega Healthcare Investors, In) score 39.1 — "Sunshine Pictures raises  ₹85 crore from anchor investors ahead of IPO launch on Tuesday"
- COIN (Coinbase Global, Inc.) score 38.6 — "Global Market: European shares climb despite geopolitical risks; miners lead gains"
- HDB (HDFC Bank Limited) score 34.7 — "ICICI Bank raises $750 million as Indian banks tap dollar bond market"
- CHKP (Check Point Software Technolog) score 34.3 — "Horizon Industrial Parks’ Rs 2,600 crore IPO opens. Check GMP, price band and other key de"
- IDBI.NS (IDBI BANK LIMITED) score 32.5 — "ICICI Bank raises $750 million as Indian banks tap dollar bond market"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 32.5 — "ICICI Bank raises $750 million as Indian banks tap dollar bond market"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 32.4 — "ICICI Bank raises $750 million as Indian banks tap dollar bond market"
- LTH (Life Time Group Holdings, Inc.) score 27.0 — "TRUMP’S MONDAY SCHEDULE President Trump’s schedule for Monday, August 17: 🔸 8:00 AM — Exec"
- 301077.SZ (CHINASTARS) score 26.2 — "China’s Xi praises former president Jiang Zemin’s contribution in show of party unity"
- BOND (PIMCO Active Bond Exchange-Tra) score 25.5 — "ICICI Bank raises $750 million as Indian banks tap dollar bond market"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 20.7 — "Top Gainers & Losers on 17 August: NMDC Steel, LG Electronics, BSE, Tata Tech, Infosys, Vo"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 19.4 — "S&P 500 REVENUE GROWTH HITS 5-YEAR HIGH Goldman Sachs says S&P 500 revenues grew 6.4% YoY "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 18.8 — "Top Gainers & Losers on 17 August: NMDC Steel, LG Electronics, BSE, Tata Tech, Infosys, Vo"
- JIOFIN.BO (Jio Financial Services Limited) score 15.6 — "Getting diagnosed with dementia isn’t the end. It’s a time to take financial action."
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 11.3 — "Coal India Share Price Live Updates: Coal India  Price and Volume Overview"
- MS (Morgan Stanley) score 11.2 — "JP MORGAN RAISES 2026 YEAR-END TARGET FOR JAPAN'S TOPIX INDEX TO 4,600 FROM 4,400"
- PCJEWELLER.NS (PC JEWELLER LTD) score 10.8 — "Lalithaa Jewellery Mart IPO: Issue booked 69% so far. GMP hints 15% listing pop. Apply or "
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 10.8 — "Getting diagnosed with dementia isn’t the end. It’s a time to take financial action."
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.7 — "S&P 500 REVENUE GROWTH HITS 5-YEAR HIGH Goldman Sachs says S&P 500 revenues grew 6.4% YoY "
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 9.8 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Trading Update"
- NVDA (NVIDIA Corporation) score 7.4 — "NVDA - NVIDIA TO INVEST $100BN FOR OPENAI DATA CENTRE IN OHIO - FT"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 6.2 — "Cement makers face a forgettable H1FY27 as prices weaken and costs rise"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.6 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ News"
- AAPL (Apple Inc.) score 4.8 — "Apple’s stock could rise 30% if it strikes an Nvidia deal for AI, this analyst says"
- META (Meta) score 4.6 — "Pulse of the Street: Tata jitters, metal rout weigh on Indian equities"
- VT (Vanguard Total World Stock Ind) score 3.7 — "Neighbors in rural Texas county are not happy about Elon Musk’s plan to erect world’s larg"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.1 — "ICICI Bank raises $750 million as Indian banks tap dollar bond market"
- RDDT (Reddit, Inc.) score 2.9 — "Reddit shares surge 14% on S&P 500 inclusion, replacing AvalonBay"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 2.8 — "FCNR(B) inflows stabilise rupee but fail to trigger 2013-style rally"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 2.2 — "Lenskart shares soar after strong Q1 results and MSCI inclusion buzz"
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