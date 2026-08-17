# Transmission Layer — board brief · 2026-08-17 04:56Z

data as of **2026-08-17** · 98 series · 7 red / 39 amber · 8 events surfaced (20 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.139, 2d in regime; vol-pct 0.278, breadth-off 0.0, Markov P(high-vol) 0.012)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.41, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.88, corr60 0.86, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.26, corr60 0.34, last shift 2026-07-01. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.2, corr60 -0.11, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.72, corr60 -0.81, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.11, corr60 -0.11, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.31, corr60 -0.2, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.06, corr60 0.17, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 4.761345828718788e-08)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.491** (n=1115) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.823** (n=2451) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.24] cross-asset · 14 series ↑
- russell_2000 [INDICES]: last 3068.24, z20 1.99, zc 0.43, resid-z 1.16 [quiet], 1d 0.50%, |z20|=1.99; 1y-pct=100
- comex_gold [COMMODITIES]: last 4452.60, z20 1.94, zc 1.27, resid-z -0.69 [quiet], 1d 1.65%, |z20|=1.94; co-occur[gold_silver] same-direction (channel VALID)
- comex_copper [COMMODITIES]: last 6.72, z20 1.71, zc 0.83, resid-z 0.00 [quiet], 1d 1.86%, |z20|=1.71; 1y-pct=100
- comex_silver [COMMODITIES]: last 65.74, z20 1.70, zc 0.52, resid-z -0.19 [quiet], 1d 1.16%, |z20|=1.70; co-occur[gold_silver] same-direction (channel VALID)
- dyn_vt [EQUITIES]: last 162.24, z20 1.56, zc -0.11, resid-z -0.85 [quiet], 1d -0.09%, 1y-pct=99
- dyn_nvda [EQUITIES]: last 225.16, z20 1.55, zc -0.03, resid-z -0.34 [quiet], 1d -0.06%, 1y-pct=98
- vix [INDICES]: last 14.25, z20 -1.54, zc -0.34, resid-z n/a [quiet], 1d -2.60%, |z20|=1.54; 1y-pct=2
- nasdaq_100 [INDICES]: last 30050.44, z20 1.53, zc -0.09, resid-z 0.20 [quiet], 1d -0.11%, |z20|=1.53; 1y-pct=95
- sp500 [INDICES]: last 7786.01, z20 1.42, zc -0.21, resid-z 0.78 [quiet], 1d -0.17%, 1y-pct=99
- dax [INDICES]: last 26431.94, z20 1.35, zc 0.70, resid-z 0.61 [quiet], 1d 0.50%, 1y-pct=100
- stoxx_50 [INDICES]: last 6540.53, z20 1.29, zc -0.10, resid-z -0.07 [quiet], 1d -0.08%, 1y-pct=99
- gold_silver_ratio [DERIVED]: last 67.73, z20 -1.07, zc n/a, resid-z n/a [quiet], 1d 0.49%, GSR<75 (extreme low)
- dow_jones [INDICES]: last 53733.51, z20 0.88, zc -0.27, resid-z -0.15 [quiet], 1d -0.20%, 1y-pct=96
- cac_40 [INDICES]: last 8640.11, z20 0.76, zc -0.17, resid-z -0.23 [quiet], 1d -0.12%, 1y-pct=96
- **Mechanism**: The recent rise in gold and silver prices, coupled with a decline in the US dollar, has led to a surge in commodity prices. This move is propagated through the VALID gold_silver_comove channel, where monetary metals co-move, and the metal_copper_channel, where global copper leads Indian metal equities. The RISK_ON regime, with a low probability of high volatility, also supports this move.
- **Gap**: No gap: The big raw move in gold and silver prices is largely priced, with resid_z values of -0.69 and -0.19, respectively, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instruments that express this move are nifty_metal and nifty_midcap_100, which have not yet reacted. However, nifty_fmcg has already reacted, with a z20 value of -2.31.
- Watch next: nifty_metal (up) — not yet - watch; rho=0.509 via comex_silver
- Watch next: nifty_midcap_100 (up) — not yet - watch; rho=0.498 via dax
- **India receivers**: nifty_metal (rho 0.509, z 0.39); nifty_midcap_100 (rho 0.498, z 0.69); nifty_fmcg (rho -0.495, z -2.31); nifty_50 (rho 0.487, z -0.26)
- Source: Gold and silver prices rise on MCX on a weaker dollar; US-Iran stalled talks cap gains — Mint Markets, 2026-08-17. https://www.livemint.com/market/commodities/gold-and-silver-prices-rise-on-mcx-on-a-weaker-dollar-us-iran-stalled-talks-cap-gains-11786938089811.html
- Source: Gold Rises to Near $4,400 as Weak Retail Data Weighs on Dollar — Mint Markets, 2026-08-17. https://www.livemint.com/market/gold-rises-to-near-4-400-as-weak-retail-data-weighs-on-dollar-11786937454532.html
- Source: Stocks to buy in 2026 for long term: Senco Gold, Arvind among 5 stocks that could give 10-60% return — ET Markets, 2026-08-17. https://economictimes.indiatimes.com/markets/stocks/news/stocks-to-buy-in-2026-for-long-term-senco-gold-arvind-among-5-stocks-that-could-give-10-60-return/slideshow/133285138.cms
- Historical analogues: 2024-11-26 (d=0.9), 2025-10-31 (d=0.97), 2025-10-24 (d=1.11)

### [RED 4.77] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.62, z20 1.77, zc n/a, resid-z n/a [quiet], 1d 0.16%, 52-wk extreme (pct=99); |z20|=1.77; 1y-pct=99
- **Mechanism**: The midcap_largecap_ratio has reached a 52-week extreme, with a z20 level of 1.77, indicating a significant move. However, the resid_z is None, suggesting that this move is largely priced in by factor exposures. The RISK_ON regime and VALID vix_equity_inverse channel suggest that the market is positioned for a potential drawdown, but the midcap_largecap_ratio's move may not be an anomaly.
- **Gap**: No gap: the midcap_largecap_ratio's move is largely priced in by factor exposures, as indicated by the None resid_z value
- **India take**: The Nifty Midcap 100 index, which has a correlation of 0.531 with the midcap_largecap_ratio, has not yet reacted and is a potential responder. Other Indian transmission candidates like Dyn Bharatcoal NS and Dyn Fincables NS have already reacted.
- Watch next: nifty_midcap_100 (down) — not yet - watch; historically leads by 2d
- **India receivers**: nifty_midcap_100 (rho 0.531, z 0.69); dyn_bharatcoal_ns (rho 0.424, z -1.05); dyn_fincables_ns (rho 0.399, z 2.46); dyn_pcjeweller_ns (rho 0.369, z 0.07)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 4.76] commodities · 2 series ↑
- corn [COMMODITIES]: last 484.75, z20 3.92, zc 4.38, resid-z 1.25 [moved], 1d 5.61%, |z20|=3.92; 1y-pct=100
- wheat [COMMODITIES]: last 689.75, z20 1.53, zc 1.15, resid-z 1.20 [quiet], 1d 2.22%, |z20|=1.53; 1y-pct=99
- **Mechanism**: The recent surge in commodities, particularly corn and wheat, is driven by their own momentum, with corn's z20 level at 3.9249982985024037 and wheat's at 1.5256880801758035. This move is priced, given the relatively small resid_z values of 1.25 for corn and 1.2 for wheat, indicating that the current price levels are largely explained by factor exposures. The VALID metal_copper_channel and VALID gold_silver_comove channels suggest that the momentum in commodities may continue, potentially influencing Indian metal equities and monetary metals.
- **Gap**: No gap: the current price levels of corn and wheat are largely explained by their factor exposures, with small resid_z values indicating that the move is priced.
- **India take**: The Indian instrument dyn_lenskart_ns has already reacted, with a rho of 0.397 via wheat, and the VALID metal_copper_channel suggests that Indian metal equities may follow the momentum in commodities.
- Watch next: soybeans (up) — not yet - watch; high correlation with corn
- **India receivers**: dyn_lenskart_ns (rho 0.397, z 2.46)
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [AMBER 4.3] dxy ↓
- dxy [FX]: last 99.49, z20 -1.30, zc -0.55, resid-z 0.10 [quiet], 1d -0.18%, 20d range extreme
- **Mechanism**: The recent decline in the US Dollar Index (DXY) may propagate through the metal_copper_channel, a VALID channel, potentially leading to a move in Indian metal equities. The DXY decline, although priced with a small resid_z of 0.1, could still influence global copper prices, which in turn affect Indian metal equities. The VALID gold_silver_comove channel also suggests that monetary metals may co-move, potentially impacting the Indian market.
- **Gap**: No gap: The DXY move is priced with a small resid_z of 0.1, indicating that the move is largely explained by factor exposures.
- **India take**: The Indian instrument that expresses this move is likely to be the Indian metal equities, such as Hindalco or Tata Steel, which may react to the potential move in global copper prices. However, the reaction has not occurred yet.
- Watch next: comex_gold (down) — not yet - watch; Historical analogues show a median decline of 1.82% in comex_gold 20 days after a similar DXY decline
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [AMBER 4.07] dyn_tech ↑
- dyn_tech [EQUITIES]: last 72.42, z20 2.07, zc 0.15, resid-z -0.38 [quiet], 1d 0.35%, |z20|=2.07; 1y-pct=100
- **Mechanism**: dyn_tech ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_inoxindia_ns (rho -0.392 via dyn_tech, z 0.23, quiet)
- **India receivers**: dyn_inoxindia_ns (rho -0.392, z 0.23)
- Source: Why Goldman Sachs thinks there may be an ‘earnings bubble’ in tech? — BusinessLine Mkts, 2026-08-16. https://www.thehindubusinessline.com/markets/why-goldman-sachs-thinks-there-may-be-an-earnings-bubble-in-tech/article71352404.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.0), 2025-05-19 (d=0.0)

### [AMBER 4.06] fx · 4 series ↑
- aud_usd [FX]: last 0.71, z20 2.40, zc 1.32, resid-z 0.17 [quiet], 1d 0.58%, |z20|=2.40
- usd_mxn [FX]: last 17.00, z20 -1.99, zc -0.45, resid-z -0.39 [quiet], 1d -0.17%, |z20|=1.99; 1y-pct=0
- gbp_usd [FX]: last 1.36, z20 1.70, zc 0.30, resid-z 0.62 [quiet], 1d 0.13%, |z20|=1.70
- eur_usd [FX]: last 1.16, z20 1.55, zc 0.40, resid-z 1.01 [quiet], 1d 0.14%, |z20|=1.55
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.554 via usd_mxn, z -1.05, reacted); eur_inr (rho 0.471 via gbp_usd, z 3.1, reacted); dyn_icicigi_bo (rho -0.423 via gbp_usd, z -0.52, quiet)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.506 vs eur_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.554, z -1.05); eur_inr (rho 0.471, z 3.1); dyn_icicigi_bo (rho -0.423, z -0.52)
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [AMBER 3.78] dyn_bac ↑
- dyn_bac [EQUITIES]: last 64.49, z20 1.78, zc 0.43, resid-z -1.09 [quiet], 1d 0.62%, 1y-pct=99
- **Mechanism**: dyn_bac ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cupid_ns (rho 0.372 via dyn_bac, z 1.54, reacted)
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.632 vs dyn_bac, historically leads by 2d
- Watch next: cac_40 (co-move) — not yet - watch; rho 0.539 vs dyn_bac, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.577 vs dyn_bac
- **India receivers**: dyn_cupid_ns (rho 0.372, z 1.54)
- Source: Just 7% of America’s Nuclear Fuel Comes From Home — OilPrice, 2026-08-15. https://oilprice.com/Alternative-Energy/Nuclear-Power/Just-7-of-Americas-Nuclear-Fuel-Comes-From-Home.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

### [AMBER 3.45] cross-asset · 2 series ↑
- ust_30y [RATES]: last 5.21, z20 0.62, zc -0.73, resid-z -0.48 [quiet], 1d -0.57%, 1y-pct=97
- dyn_bond [EQUITIES]: last 90.64, z20 -0.39, zc -1.00, resid-z 0.82 [quiet], 1d -0.30%, 1y-pct=3
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.901 vs ust_30y, historically leads by 1d
- Watch next: tips_10y_real (co-move) — not yet - watch; rho 0.688 vs ust_30y, historically leads by 1d
- Watch next: brent (co-move) — not yet - watch; rho 0.548 vs ust_30y, historically leads by 3d
- Watch next: wti (co-move) — not yet - watch; rho 0.506 vs ust_30y, historically leads by 3d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.533 vs ust_30y
- Source: ETMarkets Smart Talk | Dhawal Dalal’s fixed-income playbook: Stagger bond bets, favour AAA debt — ET Markets, 2026-08-17. https://economictimes.indiatimes.com/markets/bonds/etmarkets-smart-talk-dhawal-dalals-fixed-income-playbook-stagger-bond-bets-favour-aaa-debt/articleshow/133284956.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-04-01 (d=0.06), 2025-04-16 (d=0.08)

## Watchlist (below surfacing floor)
indices · 3 series ↑ (3.16), dyn_tatatech_ns ↑ (3.16), eur_inr ↑ (3.1), dyn_coin ↓ (2.95), dyn_idbi_ns ↓ (2.52), usd_brl ↑ (2.51), dyn_fincables_ns ↑ (2.46), dyn_lenskart_ns ↑ (2.46), nifty_fmcg ↓ (2.31), bovespa ↓ (2.17), ust_2y ↓ (1.72), usd_cny ↓ (1.57)

## India macro
- nifty_50: 24251.6992 (1d -0.47%, z20 -0.26, flag none)
- nifty_midcap_100: 63583.3984 (1d -0.31%, z20 0.69, flag amber)
- usd_inr: 95.5900 (1d 0.20%, z20 -0.28, flag none)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6218 (1d 0.16%, z20 1.77, flag red)
- Next India prints: NSDL FPI flows T-0d · India trade / CAD data T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 76.2 — "Can gold recycling become India’s next circular economy success story?"
- INOXINDIA.NS (INOX INDIA LIMITED) score 75.7 — "Can gold recycling become India’s next circular economy success story?"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 75.5 — "Can gold recycling become India’s next circular economy success story?"
- INDIANB.NS (INDIAN BANK) score 50.7 — "FPIs pour ₹16,621 crore into Indian equities in first half of August"
- BAC (Bank of America Corporation) score 36.3 — "Just 7% of America’s Nuclear Fuel Comes From Home"
- TECHM.NS (TECH MAHINDRA LIMITED) score 34.7 — "Why Goldman Sachs thinks there may be an ‘earnings bubble’ in tech?"
- CHKP (Check Point Software Technolog) score 34.3 — "Crude Check: Set to consolidate"
- OHI (Omega Healthcare Investors, In) score 34.2 — "U.S. stock futures little changed as investors ponder the Fed’s next move"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 33.1 — "Why Goldman Sachs thinks there may be an ‘earnings bubble’ in tech?"
- COIN (Coinbase Global, Inc.) score 32.8 — "Global Market: Japan stocks edge lower after GDP growth misses forecasts"
- TECH (Bio-Techne Corp) score 32.7 — "Why Goldman Sachs thinks there may be an ‘earnings bubble’ in tech?"
- HDB (HDFC Bank Limited) score 30.3 — "Thai Baht Rally May Fade on Dovish Central Bank, Analysts Say"
- IDBI.NS (IDBI BANK LIMITED) score 27.9 — "Thai Baht Rally May Fade on Dovish Central Bank, Analysts Say"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 27.9 — "Thai Baht Rally May Fade on Dovish Central Bank, Analysts Say"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 27.8 — "Thai Baht Rally May Fade on Dovish Central Bank, Analysts Say"
- LTH (Life Time Group Holdings, Inc.) score 22.8 — "Molbio Diagnostics IPO listing: Shares debut at a 21% premium, defying weak stock market s"
- 301077.SZ (CHINASTARS) score 20.6 — "Zhu Rongji’s death a reminder of what US-China relations have lost"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 19.1 — "Tata Motors PV Share Price Live Updates: Tata Motors PV's stock shows negative movement"
- BOND (PIMCO Active Bond Exchange-Tra) score 18.9 — "ETMarkets Smart Talk | Dhawal Dalal’s fixed-income playbook: Stagger bond bets, favour AAA"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 16.9 — "Tata Motors PV Share Price Live Updates: Tata Motors PV's stock shows negative movement"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 16.4 — "Adani Energy Solution shares end 2% higher after acquiring Vizag Power Transmission"
- JIOFIN.BO (Jio Financial Services Limited) score 13.2 — "Jio Financial Services Share Price Live Updates: Jio Financial Services Experiences Declin"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 10.6 — "India's Coal Demand Set to Hit 1.6 Billion Tons by 2030"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 9.9 — "Jio Financial Services Share Price Live Updates: Jio Financial Services Experiences Declin"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 9.9 — "Bajaj Finance Share Price Live Updates: Bajaj Finance slips below its 20-day EMA"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.8 — "Just 7% of America’s Nuclear Fuel Comes From Home"
- PCJEWELLER.NS (PC JEWELLER LTD) score 7.8 — "Lalithaa Jewellery Mart's Rs 1,700-cr IPO opens: GMP signals 15% premium. Should you subsc"
- MS (Morgan Stanley) score 7.1 — "Tata Motors PV shares fall 5% after weak Q1 results. What are Morgan Stanley, Nomura, othe"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 7.0 — "Cement makers face a forgettable H1FY27 as prices weaken and costs rise"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.3 — "Adani Ent Share Price Live Updates: Adani Ent. Stock Details"
- META (Meta) score 5.2 — "Pulse of the Street: Tata jitters, metal rout weigh on Indian equities"
- NVDA (NVIDIA Corporation) score 5.1 — "Nvidia’s $500 billion plan envelops Wall Street in its AI frenzy"
- RDDT (Reddit, Inc.) score 3.2 — "Reddit shares surge 14% on S&P 500 inclusion, replacing AvalonBay"
- AAPL (Apple Inc.) score 3.1 — "Nvidia, Apple, Google fuel record $185 billion gain for Norway’s wealth fund, but CEO say,"
- VT (Vanguard Total World Stock Ind) score 3.0 — "China’s next economic ambition: workshop for the Muslim world"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 2.5 — "Lenskart shares soar after strong Q1 results and MSCI inclusion buzz"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 1.3 — "ICICI Bank Share Price Live Updates: ICICI Bank Stock Details"
- CRWV (CoreWeave, Inc.) score 1.0 — "US stocks: S&P 500 ends higher as CoreWeave results fuel AI optimism"
- FINCABLES.NS (FINOLEX CABLES LTD) score 1.0 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.9 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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