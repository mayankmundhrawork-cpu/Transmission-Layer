# Transmission Layer — board brief · 2026-08-19 10:45Z

data as of **2026-08-19** · 98 series · 7 red / 37 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.325, 3d in regime; vol-pct 0.233, breadth-off 0.417, Markov P(high-vol) 0.02)
- [INVERTED] **safe_haven_gold** — corr20 -0.4, corr60 -0.4, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.87, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.27, corr60 0.39, last shift 2026-07-01. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.18, corr60 -0.11, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.72, corr60 -0.82, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.11, corr60 -0.11, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.19, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.03, corr60 0.23, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- No live setups: drivers quiet or targets already repriced.
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
- Watch next: brent (co-move) — not yet - watch; rho 0.578 vs ust_30y, historically leads by 3d
- Watch next: wti (co-move) — not yet - watch; rho 0.559 vs ust_30y, historically leads by 3d
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.541 vs ust_30y, historically leads by 1d
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.522 vs tips_10y_real, historically leads by 4d
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.517 vs ust_30y, historically leads by 1d
- Source: IDFC First Bank raises $500 million via maiden international bond issuance — BusinessLine Mkts, 2026-08-19. https://www.thehindubusinessline.com/markets/idfc-first-bank-raises-500-million-via-maiden-international-bond-issuance/article71364245.ece
- Source: Global Market: Eurozone bond rout loses steam, but rising oil prices keep investors wary — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-eurozone-bond-rout-loses-steam-but-rising-oil-prices-keep-investors-wary/articleshow/133344103.cms
- Source: BlackRock, Capital Group anchor IDFC FIRST Bank’s maiden $500 million global bond — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/stocks/news/blackrock-capital-group-anchor-idfc-first-banks-maiden-500-million-global-bond/articleshow/133342921.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-03-30 (d=0.28), 2026-05-07 (d=0.32)

### [RED 5.34] dyn_voltas_ns ↓
- dyn_voltas_ns [EQUITIES]: last 1223.00, z20 -3.34, zc -1.24, resid-z -1.06 [quiet], 1d -2.39%, |z20|=3.34; 1y-pct=0
- **Mechanism**: dyn_voltas_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bharatcoal_ns (rho 0.568 via dyn_voltas_ns, z -2.35, reacted); nifty_midcap_100 (rho 0.516 via dyn_voltas_ns, z 0.33, quiet); nifty_50 (rho 0.395 via dyn_voltas_ns, z -0.89, quiet); dyn_havells_ns (rho 0.377 via dyn_voltas_ns, z 0.74, quiet); dyn_cupid_ns (rho 0.35 via dyn_voltas_ns, z 1.21, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.516 vs dyn_voltas_ns, historically leads by 5d
- **India receivers**: dyn_bharatcoal_ns (rho 0.568, z -2.35); nifty_midcap_100 (rho 0.516, z 0.33); nifty_50 (rho 0.395, z -0.89); dyn_havells_ns (rho 0.377, z 0.74)
- Source: Voltas reported strong growth in June quarter, but failed to impress — Mint Markets, 2026-08-18. https://www.livemint.com/market/mark-to-market/voltas-strong-growth-fails-to-impress-operating-revenue-acs-home-appliances-other-businesses-engineering-products-11787031152020.html
- Source: Voltas among 4 F&O stocks with a sharp rise in futures open interest — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/stocks/news/voltas-among-4-fampo-stocks-with-a-sharp-rise-in-futures-open-interest/slideshow/133310686.cms
- Source: Voltas shares fall 4% as brokerages differ after Q1 results — BusinessLine Mkts, 2026-08-17. https://www.thehindubusinessline.com/markets/voltas-shares-fall-over-6-from-intraday-high-as-brokerages-differ-after-q1-results/article71355298.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-24 (d=0.0), 2024-11-14 (d=0.01)

### [RED 5.2] commodities · 3 series ↑
- corn [COMMODITIES]: last 489.75, z20 3.88, zc 4.47, resid-z -0.40 [moved], 1d 5.72%, |z20|=3.88; 1y-pct=100
- soybeans [COMMODITIES]: last 1227.75, z20 1.48, zc 2.19, resid-z -0.18 [moved], 1d 2.25%, 1y-pct=98
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
- Source: Lenskart shares gain over 5% to record high after incorporating new step-down subsidiary in China — Mint Markets, 2026-08-18. https://www.livemint.com/market/stock-market-news/lenskart-shares-gain-over-5-to-record-high-after-incorporating-new-step-down-subsidiary-in-china-11787043990119.html
- Source: Stocks to Watch, Aug 18: Paytm, Airtel, GMR Airports, Netweb Tech, SPR Auto, Lenskart, Manipal Health — BusinessLine Mkts, 2026-08-18. https://www.thehindubusinessline.com/markets/stock-markets/stocks-in-focus-paytm-airtel-gmr-airports-netweb-tech-spr-auto-lenskart-manipal-health-and-more/article71358731.ece
- Source: Stocks in focus: Paytm, Airtel, GMR Airports, Netweb Tech, SPR Auto, Lenskart, Manipal Health and more — BusinessLine Mkts, 2026-08-18. https://www.thehindubusinessline.com/markets/stock-markets/stocks-in-focus-paytm-airtel-gmr-airports-netweb-tech-spr-auto-lenskart-manipal-health-and-more/article71358731.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

### [AMBER 5.01] fx · 3 series ↑
- eur_usd [FX]: last 1.16, z20 1.69, zc 0.83, resid-z 0.65 [quiet], 1d 0.27%, |z20|=1.69
- gbp_usd [FX]: last 1.36, z20 1.59, zc 0.24, resid-z 0.13 [quiet], 1d 0.10%, |z20|=1.59
- usd_mxn [FX]: last 17.02, z20 -1.47, zc -0.10, resid-z -0.10 [quiet], 1d -0.04%, 1y-pct=0
- **Mechanism**: fx · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.545 via usd_mxn, z -1.13, reacted); dyn_icicigi_bo (rho -0.426 via gbp_usd, z -1.09, reacted); nifty_midcap_100 (rho -0.35 via usd_mxn, z 0.33, quiet)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.517 vs eur_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.545, z -1.13); dyn_icicigi_bo (rho -0.426, z -1.09); nifty_midcap_100 (rho -0.35, z 0.33)
- Source: Selloff in euro zone bonds pauses but oil prices keep up pressure — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/bonds/selloff-in-euro-zone-bonds-pauses-but-oil-prices-keep-up-pressure/articleshow/133341510.cms
- Source: ECB'S LANE: EURO ZONE INFLATION ONE PERCENTAGE POINT ABOVE ECB'S 2% TARGET IS A LOT — DeItaone, 2026-08-18. https://t.me/walter_bloomberg/34837
- Source: Euro zone bonds join global selloff, long-end yields at multi-year highs — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bonds-join-global-selloff-long-end-yields-at-multi-year-highs/articleshow/133321858.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.25), 2026-05-05 (d=0.45)

### [RED 4.92] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.63, z20 1.92, zc n/a, resid-z n/a [quiet], 1d 0.12%, 52-wk extreme (pct=100); |z20|=1.92; 1y-pct=100
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.504 via midcap_largecap_ratio, z 0.33, quiet); dyn_bharatcoal_ns (rho 0.385 via midcap_largecap_ratio, z -2.35, reacted); dyn_fincables_ns (rho 0.361 via midcap_largecap_ratio, z 1.82, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.504 vs midcap_largecap_ratio, historically leads by 2d
- **India receivers**: nifty_midcap_100 (rho 0.504, z 0.33); dyn_bharatcoal_ns (rho 0.385, z -2.35); dyn_fincables_ns (rho 0.361, z 1.82)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [RED 4.65] dyn_stylebaaza_ns ↑
- dyn_stylebaaza_ns [EQUITIES]: last 422.75, z20 2.65, zc 1.32, resid-z 1.56 [unexplained], 1d 4.99%, |z20|=2.65; 1y-pct=100
- **Mechanism**: dyn_stylebaaza_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_pcjeweller_ns (rho 0.389 via dyn_stylebaaza_ns, z 0.25, quiet); dyn_adanient_bo (rho 0.356 via dyn_stylebaaza_ns, z -1.16, reacted)
- **India receivers**: dyn_pcjeweller_ns (rho 0.389, z 0.25); dyn_adanient_bo (rho 0.356, z -1.16)
- Source: South Korea’s SK Hynix announces buyback after stock crashes 50% in two months, wipes off massive retail wealth — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/south-koreas-sk-hynix-announces-buyback-after-stock-crashes-50-in-two-months-wipes-off-massive-retail-wealth/articleshow/133344672.cms
- Source: Sunshine Pictures IPO sees strong retail demand on Day 1 — BusinessLine Mkts, 2026-08-18. https://www.thehindubusinessline.com/markets/sunshine-pictures-ipo-sees-strong-retail-demand-on-day-1/article71360474.ece
- Source: Klarna trims full-year revenue, volume outlook as German retail weakens — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/us-stocks/news/klarna-trims-full-year-revenue-volume-outlook-as-german-retail-weakens/articleshow/133323113.cms
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-04 (d=0.01), 2025-02-20 (d=0.02)

### [AMBER 4.35] dyn_bharatcoal_ns ↓
- dyn_bharatcoal_ns [EQUITIES]: last 32.95, z20 -2.35, zc -0.48, resid-z -0.07 [quiet], 1d -0.87%, |z20|=2.35
- **Mechanism**: dyn_bharatcoal_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.643 via dyn_bharatcoal_ns, z 0.33, quiet); dyn_voltas_ns (rho 0.568 via dyn_bharatcoal_ns, z -3.34, reacted); dyn_jiofin_bo (rho 0.463 via dyn_bharatcoal_ns, z -0.74, quiet); dyn_coalindia_ns (rho 0.46 via dyn_bharatcoal_ns, z -2.25, reacted); dyn_indianb_ns (rho 0.44 via dyn_bharatcoal_ns, z 0.57, quiet)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.643 vs dyn_bharatcoal_ns
- **India receivers**: nifty_midcap_100 (rho 0.643, z 0.33); dyn_voltas_ns (rho 0.568, z -3.34); dyn_jiofin_bo (rho 0.463, z -0.74); dyn_coalindia_ns (rho 0.46, z -2.25)
- Source: Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata Chemicals among top losers — Mint Markets, 2026-08-19. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-19-aug-netweb-tech-bata-reliance-power-bharat-dynamics-tata-chemicals-among-top-losers-11787134391057.html
- Source: Indian steel mills face margin squeeze as global coking coal prices rise — BusinessLine Mkts, 2026-08-19. https://www.thehindubusinessline.com/markets/commodities/indian-steel-mills-face-margin-squeeze-as-global-coking-coal-prices-rise/article71363850.ece
- Source: Bharat Value Fund bets ₹300 crore for undisclosed stake in Big Mishra Pedha — BusinessLine Mkts, 2026-08-19. https://www.thehindubusinessline.com/markets/bharat-value-fund-bets-300-crore-for-undisclosed-stake-in-big-mishra-pedha/article71363394.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-11 (d=0.3), 2026-07-03 (d=0.75)

## Watchlist (below surfacing floor)
dxy ↓ (4.28), cross-asset · 4 series ↑ (4.26), dyn_coalindia_ns ↓ (4.25), dyn_meta ↓ (4.22), gold_silver_ratio ↑ (3.9), dyn_bac ↑ (3.32), dyn_lth ↑ (3.19), dyn_icicigi_bo ↓ (3.09), dyn_coin ↓ (3.08), dyn_hdb ↓ (3.06), nifty_fmcg ↓ (2.97), dyn_tech ↑ (2.88)

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
- COALINDIA.NS (COAL INDIA LTD) score 97.2 — "Indian Bank raises $400 million for four years"
- INOXINDIA.NS (INOX INDIA LIMITED) score 96.8 — "Indian Bank raises $400 million for four years"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 95.9 — "Indian Bank raises $400 million for four years"
- INDIANB.NS (INDIAN BANK) score 85.3 — "IDFC First Bank raises $500 million through maiden overseas bond issue"
- BAC (Bank of America Corporation) score 67.3 — "IDFC First Bank raises $500 million through maiden overseas bond issue"
- HDB (HDFC Bank Limited) score 60.5 — "IDFC First Bank raises $500 million through maiden overseas bond issue"
- IDBI.NS (IDBI BANK LIMITED) score 55.9 — "IDFC First Bank raises $500 million through maiden overseas bond issue"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 55.9 — "IDFC First Bank raises $500 million through maiden overseas bond issue"
- COIN (Coinbase Global, Inc.) score 55.9 — "BlackRock, Capital Group anchor IDFC FIRST Bank’s maiden $500 million global bond"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 55.9 — "IDFC First Bank raises $500 million through maiden overseas bond issue"
- TECHM.NS (TECH MAHINDRA LIMITED) score 49.7 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 47.9 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- TECH (Bio-Techne Corp) score 47.7 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- BOND (PIMCO Active Bond Exchange-Tra) score 47.3 — "IDFC First Bank raises $500 million through maiden overseas bond issue"
- OHI (Omega Healthcare Investors, In) score 43.8 — "Global Market: Eurozone bond rout loses steam, but rising oil prices keep investors wary"
- CHKP (Check Point Software Technolog) score 36.7 — "Mopshop Distribution IPO Day 1: Issue booked 29% so far. Check GMP, issue details"
- LTH (Life Time Group Holdings, Inc.) score 30.6 — "Markets fall for seventh straight session; banks, metals drag as crude weighs on sentiment"
- 301077.SZ (CHINASTARS) score 20.7 — "China’s Solar Exports Fell 21.4% in July"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 19.8 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 19.6 — "The U.S. Is Quietly Building a New Energy Foothold in Iraq"
- JIOFIN.BO (Jio Financial Services Limited) score 19.4 — "Cipla Share Price Live Updates: Cipla's Current Financial Snapshot"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 18.6 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- PCJEWELLER.NS (PC JEWELLER LTD) score 16.5 — "Lalithaa Jewellery Mart IPO Day 3: Subscribed 28.89x so far; GMP signals 20% premium. Shou"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 15.7 — "Indian steel mills face margin squeeze as global coking coal prices rise"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 12.5 — "Cipla Share Price Live Updates: Cipla's Current Financial Snapshot"
- MS (Morgan Stanley) score 10.7 — "ANTHROPIC LINES UP $10B+ CREDIT AHEAD OF IPO Anthropic’s revolving credit facility is set "
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.3 — "Ashok Leyland just had a record June quarter. So why did the margin fall a full point?"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 10.2 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Sees Minor Drop in Price"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.3 — "IGL, MGL to Adani Total Gas: City gas distributor stocks rise up to 4%; here's why"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 7.9 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- META (Meta) score 7.6 — "Markets fall for seventh straight session; banks, metals drag as crude weighs on sentiment"
- VT (Vanguard Total World Stock Ind) score 7.4 — "Christine Lagarde: Panel remarks about the European economy during a discussion on the glo"
- NVDA (NVIDIA Corporation) score 7.4 — "NVDA - BOFA: NVIDIA COULD BE UP TO 50% UNDERVALUED Bank of America says Nvidia may trade a"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 7.4 — "South Korea’s SK Hynix announces buyback after stock crashes 50% in two months, wipes off "
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.0 — "ICICI Bank shares slip 0.52% in early trade, despite yearly gains"
- AAPL (Apple Inc.) score 4.0 — "AAPL - APPLE OVERHAULS EU APP STORE FEES Apple is revamping its EU App Store terms from Oc"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.8 — "Lenskart shares gain over 5% to record high after incorporating new step-down subsidiary i"
- VOLTAS.NS (VOLTAS LTD) score 3.4 — "Voltas reported strong growth in June quarter, but failed to impress"
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