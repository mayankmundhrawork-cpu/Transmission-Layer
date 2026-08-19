# Transmission Layer — board brief · 2026-08-19 13:08Z

data as of **2026-08-19** · 98 series · 8 red / 38 amber · 8 events surfaced (30 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.325, 3d in regime; vol-pct 0.233, breadth-off 0.417, Markov P(high-vol) 0.02)
- [INVERTED] **safe_haven_gold** — corr20 -0.4, corr60 -0.4, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.87, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.27, corr60 0.39, last shift 2026-07-01. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.18, corr60 -0.11, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.72, corr60 -0.82, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.09, corr60 -0.11, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.19, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.06, corr60 0.23, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** dxy → aud_usd: leads 1d (ccf -0.573, β -0.8514, p 0.0); driver zc -1.79 → expected 0.484%. Type hit-rate 0.83 (n=2360).
- Track record · residual_reversion: hit-rate **0.493** (n=1116) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.83** (n=2360) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 6.07] cross-asset · 4 series ↑
- ust_30y [RATES]: last 5.31, z20 2.40, zc 1.46, resid-z 1.25 [quiet], 1d 1.14%, |z20|=2.40; 1y-pct=100
- ust_10y [RATES]: last 4.72, z20 1.35, zc 0.85, resid-z 0.60 [quiet], 1d 0.85%, 1y-pct=99
- tips_10y_real [RATES]: last 2.44, z20 1.06, zc 0.83, resid-z 0.48 [quiet], 1d 1.24%, 1y-pct=99
- dyn_bond [EQUITIES]: last 90.51, z20 -0.76, zc 0.33, resid-z 0.14 [quiet], 1d 0.10%, 1y-pct=2
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.579 vs ust_30y, historically leads by 3d
- Watch next: wti (co-move) — not yet - watch; rho 0.558 vs ust_30y, historically leads by 3d
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.541 vs ust_30y, historically leads by 1d
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.522 vs tips_10y_real, historically leads by 4d
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.517 vs ust_30y, historically leads by 1d
- Source: The bond selloff is rattling investors, but here’s why they shouldn’t expect a deeper stock downturn — MarketWatch Top, 2026-08-19. https://www.marketwatch.com/story/the-bond-selloff-is-rattling-investors-but-heres-why-they-shouldnt-expect-a-deeper-stock-downturn-43139350?mod=mw_rss_topstories
- Source: Why rising Treasury yields are becoming a growing risk for the US economy — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/why-rising-treasury-yields-are-becoming-a-growing-risk-for-the-us-economy/articleshow/133344713.cms
- Source: IDFC First Bank raises $500 million via maiden international bond issuance — BusinessLine Mkts, 2026-08-19. https://www.thehindubusinessline.com/markets/idfc-first-bank-raises-500-million-via-maiden-international-bond-issuance/article71364245.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

### [AMBER 5.77] fx · 4 series ↑
- eur_usd [FX]: last 1.16, z20 2.10, zc 1.61, resid-z 1.21 [moved], 1d 0.53%, |z20|=2.10
- gbp_usd [FX]: last 1.36, z20 2.06, zc 0.89, resid-z 0.65 [quiet], 1d 0.38%, |z20|=2.06
- aud_usd [FX]: last 0.71, z20 1.97, zc 0.08, resid-z 0.27 [quiet], 1d 0.04%, |z20|=1.97
- usd_mxn [FX]: last 16.97, z20 -1.83, zc -1.06, resid-z -0.88 [quiet], 1d -0.38%, |z20|=1.83; 1y-pct=0
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.532 via usd_mxn, z -1.13, reacted); dyn_icicigi_bo (rho -0.428 via gbp_usd, z -1.09, reacted); nifty_midcap_100 (rho 0.396 via aud_usd, z 0.33, quiet)
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.6 vs eur_usd, historically leads by 4d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.539 vs eur_usd
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.531 vs aud_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.532, z -1.13); dyn_icicigi_bo (rho -0.428, z -1.09); nifty_midcap_100 (rho 0.396, z 0.33)
- Source: Selloff in euro zone bonds pauses but oil prices keep up pressure — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/bonds/selloff-in-euro-zone-bonds-pauses-but-oil-prices-keep-up-pressure/articleshow/133341510.cms
- Source: ECB'S LANE: EURO ZONE INFLATION ONE PERCENTAGE POINT ABOVE ECB'S 2% TARGET IS A LOT — DeItaone, 2026-08-18. https://t.me/walter_bloomberg/34837
- Source: Euro zone bonds join global selloff, long-end yields at multi-year highs — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bonds-join-global-selloff-long-end-yields-at-multi-year-highs/articleshow/133321858.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 5.34] dyn_voltas_ns ↓
- dyn_voltas_ns [EQUITIES]: last 1223.00, z20 -3.34, zc -1.24, resid-z -1.16 [quiet], 1d -2.39%, |z20|=3.34; 1y-pct=0
- **Mechanism**: dyn_voltas_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bharatcoal_ns (rho 0.568 via dyn_voltas_ns, z -2.35, reacted); nifty_midcap_100 (rho 0.516 via dyn_voltas_ns, z 0.33, quiet); nifty_50 (rho 0.395 via dyn_voltas_ns, z -0.89, quiet); dyn_havells_ns (rho 0.377 via dyn_voltas_ns, z 0.74, quiet); dyn_cupid_ns (rho 0.35 via dyn_voltas_ns, z 1.21, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.516 vs dyn_voltas_ns, historically leads by 5d
- **India receivers**: dyn_bharatcoal_ns (rho 0.568, z -2.35); nifty_midcap_100 (rho 0.516, z 0.33); nifty_50 (rho 0.395, z -0.89); dyn_havells_ns (rho 0.377, z 0.74)
- Source: Voltas reported strong growth in June quarter, but failed to impress — Mint Markets, 2026-08-18. https://www.livemint.com/market/mark-to-market/voltas-strong-growth-fails-to-impress-operating-revenue-acs-home-appliances-other-businesses-engineering-products-11787031152020.html
- Source: Voltas among 4 F&O stocks with a sharp rise in futures open interest — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/stocks/news/voltas-among-4-fampo-stocks-with-a-sharp-rise-in-futures-open-interest/slideshow/133310686.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-24 (d=0.0), 2024-11-14 (d=0.01)

### [RED 5.28] commodities · 3 series ↑
- corn [COMMODITIES]: last 490.50, z20 3.96, zc 4.60, resid-z -0.40 [moved], 1d 5.88%, |z20|=3.96; 1y-pct=100
- soybeans [COMMODITIES]: last 1226.25, z20 1.43, zc 2.10, resid-z -0.18 [moved], 1d 2.12%, 1y-pct=98
- wheat [COMMODITIES]: last 681.75, z20 1.19, zc 1.45, resid-z -0.87 [quiet], 1d 2.60%, 1y-pct=98
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_lenskart_ns (rho 0.361 via wheat, z 3.09, reacted)
- **India receivers**: dyn_lenskart_ns (rho 0.361, z 3.09)
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [RED 5.09] dyn_lenskart_ns ↑
- dyn_lenskart_ns [EQUITIES]: last 639.60, z20 3.09, zc 1.11, resid-z 0.98 [quiet], 1d 1.78%, |z20|=3.09; 1y-pct=99
- **Mechanism**: dyn_lenskart_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/stocks/news/lenskart-solutions-among-4-stocks-to-hit-52-week-highs-amp-surge-up-to-25-in-a-month/slideshow/133348316.cms
- Source: Lenskart shares gain over 5% to record high after incorporating new step-down subsidiary in China — Mint Markets, 2026-08-18. https://www.livemint.com/market/stock-market-news/lenskart-shares-gain-over-5-to-record-high-after-incorporating-new-step-down-subsidiary-in-china-11787043990119.html
- Source: Stocks to Watch, Aug 18: Paytm, Airtel, GMR Airports, Netweb Tech, SPR Auto, Lenskart, Manipal Health — BusinessLine Mkts, 2026-08-18. https://www.thehindubusinessline.com/markets/stock-markets/stocks-in-focus-paytm-airtel-gmr-airports-netweb-tech-spr-auto-lenskart-manipal-health-and-more/article71358731.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

### [RED 4.92] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.63, z20 1.92, zc n/a, resid-z n/a [quiet], 1d 0.12%, 52-wk extreme (pct=100); |z20|=1.92; 1y-pct=100
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.504 via midcap_largecap_ratio, z 0.33, quiet); dyn_bharatcoal_ns (rho 0.385 via midcap_largecap_ratio, z -2.35, reacted); dyn_fincables_ns (rho 0.361 via midcap_largecap_ratio, z 1.82, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.504 vs midcap_largecap_ratio, historically leads by 2d
- **India receivers**: nifty_midcap_100 (rho 0.504, z 0.33); dyn_bharatcoal_ns (rho 0.385, z -2.35); dyn_fincables_ns (rho 0.361, z 1.82)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 4.69] dxy ↓
- dxy [FX]: last 99.08, z20 -1.69, zc -1.79, resid-z -0.61 [moved], 1d -0.57%, 20d range extreme; |z20|=1.69
- **Mechanism**: dxy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [RED 4.65] dyn_stylebaaza_ns ↑
- dyn_stylebaaza_ns [EQUITIES]: last 422.75, z20 2.65, zc 1.32, resid-z 1.55 [unexplained], 1d 4.99%, |z20|=2.65; 1y-pct=100
- **Mechanism**: dyn_stylebaaza_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_pcjeweller_ns (rho 0.389 via dyn_stylebaaza_ns, z 0.25, quiet); dyn_adanient_bo (rho 0.356 via dyn_stylebaaza_ns, z -1.16, reacted)
- **India receivers**: dyn_pcjeweller_ns (rho 0.389, z 0.25); dyn_adanient_bo (rho 0.356, z -1.16)
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: US futures steady after tech rout; Iran tensions, retail earnings in focus — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-war-hormuz-deal-crude-oil-fed-warsh-rate-hike-moderna-nvidia-micron-sandisk-chip-stock-price-news-19th-august-2026/liveblog/133348429.cms
- Source: South Korea’s SK Hynix announces buyback after stock crashes 50% in two months, wipes off massive retail wealth — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/south-koreas-sk-hynix-announces-buyback-after-stock-crashes-50-in-two-months-wipes-off-massive-retail-wealth/articleshow/133344672.cms
- Source: Sunshine Pictures IPO sees strong retail demand on Day 1 — BusinessLine Mkts, 2026-08-18. https://www.thehindubusinessline.com/markets/sunshine-pictures-ipo-sees-strong-retail-demand-on-day-1/article71360474.ece
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-04 (d=0.01), 2025-02-20 (d=0.02)

## Watchlist (below surfacing floor)
dyn_bharatcoal_ns ↓ (4.35), cross-asset · 4 series ↑ (4.26), dyn_coalindia_ns ↓ (4.25), dyn_meta ↓ (4.22), comex_gold ↑ (3.9), gold_silver_ratio ↑ (3.39), dyn_bac ↑ (3.32), dyn_lth ↑ (3.19), dyn_icicigi_bo ↓ (3.09), dyn_coin ↓ (3.08), dyn_hdb ↓ (3.06), nifty_fmcg ↓ (2.97)

## India macro
- nifty_50: 24078.3008 (1d -0.32%, z20 -0.89, flag none)
- nifty_midcap_100: 63406.8008 (1d -0.20%, z20 0.33, flag amber)
- usd_inr: 95.7430 (1d 0.05%, z20 0.16, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6334 (1d 0.12%, z20 1.92, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 101.0 — "Oil India vs ONGC vs OMCs: What JM Financial’s $80 Brent call means for oil stocks"
- INOXINDIA.NS (INOX INDIA LIMITED) score 100.6 — "Oil India vs ONGC vs OMCs: What JM Financial’s $80 Brent call means for oil stocks"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 99.7 — "Oil India vs ONGC vs OMCs: What JM Financial’s $80 Brent call means for oil stocks"
- INDIANB.NS (INDIAN BANK) score 84.4 — "Nifty fall for seventh straight session; banks, metals drag as crude weighs on sentiment"
- BAC (Bank of America Corporation) score 66.8 — "Nifty fall for seventh straight session; banks, metals drag as crude weighs on sentiment"
- HDB (HDFC Bank Limited) score 60.2 — "Nifty fall for seventh straight session; banks, metals drag as crude weighs on sentiment"
- IDBI.NS (IDBI BANK LIMITED) score 55.7 — "Nifty fall for seventh straight session; banks, metals drag as crude weighs on sentiment"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 55.7 — "Nifty fall for seventh straight session; banks, metals drag as crude weighs on sentiment"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 55.6 — "Nifty fall for seventh straight session; banks, metals drag as crude weighs on sentiment"
- COIN (Coinbase Global, Inc.) score 54.6 — "BlackRock, Capital Group anchor IDFC FIRST Bank’s maiden $500 million global bond"
- TECHM.NS (TECH MAHINDRA LIMITED) score 51.6 — "Tech holds the crown, but defensive positioning grows: BofA survey"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 49.8 — "Tech holds the crown, but defensive positioning grows: BofA survey"
- TECH (Bio-Techne Corp) score 49.6 — "Tech holds the crown, but defensive positioning grows: BofA survey"
- BOND (PIMCO Active Bond Exchange-Tra) score 48.2 — "The bond selloff is rattling investors, but here’s why they shouldn’t expect a deeper stoc"
- OHI (Omega Healthcare Investors, In) score 43.8 — "The bond selloff is rattling investors, but here’s why they shouldn’t expect a deeper stoc"
- CHKP (Check Point Software Technolog) score 35.8 — "Mopshop Distribution IPO Day 1: Issue booked 29% so far. Check GMP, issue details"
- LTH (Life Time Group Holdings, Inc.) score 33.9 — "Sunshine Pictures IPO day 2: Issue subscribed over 18 times, GMP signals 21% listing pop. "
- JIOFIN.BO (Jio Financial Services Limited) score 20.9 — "IRAN REPORTEDLY WEIGHS STRIKES ON U.S. TARGETS IN EUROPE Iran is considering expanding its"
- 301077.SZ (CHINASTARS) score 20.2 — "China’s Solar Exports Fell 21.4% in July"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.2 — "Iran War Set to Drive UK Energy Bills to 3-Year High"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 19.4 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 18.1 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- PCJEWELLER.NS (PC JEWELLER LTD) score 17.1 — "Lalithaa Jewellery IPO Day 3: Issue booked 63x, QIB category leads at 145x"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 15.3 — "Indian steel mills face margin squeeze as global coking coal prices rise"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 14.2 — "IRAN REPORTEDLY WEIGHS STRIKES ON U.S. TARGETS IN EUROPE Iran is considering expanding its"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 12.0 — "Market wrap:  HCL Tech, Sun Pharma, Power Grid, Bajaj Finance top gainers and losers on Ni"
- MS (Morgan Stanley) score 10.5 — "ANTHROPIC LINES UP $10B+ CREDIT AHEAD OF IPO Anthropic’s revolving credit facility is set "
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.0 — "Ashok Leyland just had a record June quarter. So why did the margin fall a full point?"
- META (Meta) score 8.4 — "Nifty fall for seventh straight session; banks, metals drag as crude weighs on sentiment"
- VT (Vanguard Total World Stock Ind) score 8.2 — "India's gold demand recovery likely to strengthen ahead of festive season: World Gold Coun"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 8.2 — "Dow Jones| Nasdaq | US Stock Market Today | Live: US futures steady after tech rout; Iran "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.1 — "IGL, MGL to Adani Total Gas: City gas distributor stocks rise up to 4%; here's why"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 7.7 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- NVDA (NVIDIA Corporation) score 7.2 — "NVDA - BOFA: NVIDIA COULD BE UP TO 50% UNDERVALUED Bank of America says Nvidia may trade a"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.8 — "ICICI Bank shares slip 0.52% in early trade, despite yearly gains"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.7 — "Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month"
- AAPL (Apple Inc.) score 3.9 — "AAPL - APPLE OVERHAULS EU APP STORE FEES Apple is revamping its EU App Store terms from Oc"
- VOLTAS.NS (VOLTAS LTD) score 3.3 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.6 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.5 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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