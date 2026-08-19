# Transmission Layer — board brief · 2026-08-19 20:43Z

data as of **2026-08-19** · 98 series · 16 red / 29 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.293, 1d in regime; vol-pct 0.233, breadth-off 0.353, Markov P(high-vol) 0.013)
- [INVERTED] **safe_haven_gold** — corr20 -0.43, corr60 -0.41, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.87, corr60 0.87, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.27, corr60 0.39, last shift 2026-07-01. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.18, corr60 -0.11, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.68, corr60 -0.82, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.08, corr60 -0.11, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.13, corr60 -0.16, last shift 2026-06-30. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.06, corr60 0.23, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 3.0459963896056763e-05)
- **SETUP** dxy → aud_usd: leads 1d (ccf -0.573, β -0.8513, p 0.0); driver zc -2.65 → expected 0.717%. Type hit-rate 0.83 (n=2330).
- **SETUP** btc_usd → asx_200: leads 1d (ccf 0.311, β 0.0882, p 0.0); driver zc 3.47 → expected 0.544%. Type hit-rate 0.83 (n=2330).
- Track record · residual_reversion: hit-rate **0.496** (n=1115) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.83** (n=2330) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 35.03] dyn_mrna ↑
- dyn_mrna [EQUITIES]: last 174.16, z20 33.03, zc 43.53, resid-z -0.64 [moved], 1d 176.63%, |z20|=33.03; 1y-pct=100
- **Mechanism**: dyn_mrna ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Moderna’s cancer-vaccine breakthrough drives broad biopharma stock rally — MarketWatch Top, 2026-08-19. https://www.marketwatch.com/story/modernas-cancer-vaccine-breakthrough-drives-broad-biopharma-stock-rally-ff2816aa?mod=mw_rss_topstories
- Source: Moderna’s experimental vaccine prevents cancer recurrence, in ‘historic’ win for personalized medicine. Its stock soared. — MarketWatch Top, 2026-08-19. https://www.marketwatch.com/story/modernas-stock-doubles-on-promising-cancer-vaccine-results-896b1f2c?mod=mw_rss_topstories
- Source: US stocks: US market rises as yields ease, Moderna lifts healthcare stocks — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-us-market-rises-as-yields-ease-moderna-lifts-healthcare-stocks/articleshow/133358680.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-16 (d=0.01), 2025-08-20 (d=0.01)

### [RED 13.18] crypto · 2 series ↑
- eth_usd [CRYPTO]: last 2123.08, z20 10.35, zc 2.86, resid-z 3.02 [unexplained], 1d 10.78%, |z20|=10.35
- btc_usd [CRYPTO]: last 68669.84, z20 7.73, zc 3.47, resid-z 2.37 [unexplained], 1d 6.17%, |z20|=7.73
- **Mechanism**: crypto · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-11-11 (z-distance 3.57).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_coin (co-move) — not yet - watch; rho 0.833 vs eth_usd, historically leads by 5d
- Watch next: vix (inverse) — not yet - watch; rho -0.647 vs eth_usd
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.579 vs eth_usd
- Watch next: sp500 (co-move) — not yet - watch; rho 0.539 vs eth_usd
- Source: Bitcoin near $64,350 as weak liquidity and subdued on-chain activity signal caution — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-near-64350-as-weak-liquidity-and-subdued-on-chain-activity-signal-caution/articleshow/133344028.cms
- Source: Bitcoin climbs towards $64,000 as cooling inflation and falling treasury yields aid recovery — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-climbs-towards-64000-as-cooling-inflation-and-falling-treasury-yields-aid-recovery/articleshow/133318408.cms
- Historical analogues: 2024-11-11 (d=3.57), 2025-07-10 (d=4.49), 2026-03-16 (d=5.03)

### [RED 6.4] cross-asset · 3 series ↑
- comex_gold [COMMODITIES]: last 4579.60, z20 2.48, zc 3.91, resid-z -0.53 [priced], 1d 4.89%, |z20|=2.48; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 66.75, z20 1.73, zc 1.83, resid-z -2.19 [unexplained], 1d 4.39%, |z20|=1.73; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 68.61, z20 -0.08, zc n/a, resid-z n/a [quiet], 1d 0.49%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.513 via comex_silver, z 0.5, quiet); dyn_stylebaaza_ns (rho -0.363 via gold_silver_ratio, z 2.65, reacted)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.636 vs comex_gold, historically leads by 1d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.586 vs comex_silver, historically leads by 4d
- Watch next: dax (co-move) — not yet - watch; rho 0.528 vs comex_gold, historically leads by 4d
- Watch next: nifty_metal (co-move) — not yet - watch; rho 0.513 vs comex_silver, historically leads by 4d
- Watch next: dyn_coin (co-move) — not yet - watch; rho 0.517 vs comex_gold
- **India receivers**: nifty_metal (rho 0.513, z 0.5); dyn_stylebaaza_ns (rho -0.363, z 2.65)
- Source: Gold surges over 3% as US Treasury announcement hurts yields, dollar — Mint Markets, 2026-08-19. https://www.livemint.com/market/gold-surges-over-3-as-us-treasury-announcement-hurts-yields-dollar-11787164505057.html
- Source: Stocks, bonds and gold rally after Treasury indicates it will buy more government bonds to stop yields from surging — MarketWatch Top, 2026-08-19. https://www.marketwatch.com/story/pressure-on-bonds-abates-as-treasury-announces-buybacks-what-may-come-next-af7d7c76?mod=mw_rss_topstories
- Source: Gold, silver prices drop in Delhi as rising crude oil rates, geopolitical worries weigh on bullion — BusinessLine Mkts, 2026-08-19. https://www.thehindubusinessline.com/markets/gold/gold-silver-prices-drop-in-delhi-as-rising-crude-oil-rates-geopolitical-worries-weigh-on-bullion/article71365539.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.3] fx · 4 series ↑
- eur_usd [FX]: last 1.17, z20 2.64, zc 2.61, resid-z 2.00 [unexplained], 1d 0.86%, |z20|=2.64
- aud_usd [FX]: last 0.71, z20 2.38, zc 0.55, resid-z 0.76 [quiet], 1d 0.27%, |z20|=2.38
- gbp_usd [FX]: last 1.36, z20 2.13, zc 1.00, resid-z 0.66 [quiet], 1d 0.42%, |z20|=2.13
- usd_mxn [FX]: last 16.95, z20 -1.94, zc -1.35, resid-z -1.14 [quiet], 1d -0.48%, |z20|=1.94; 1y-pct=0
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.527 via usd_mxn, z -1.13, reacted); dyn_icicigi_bo (rho -0.427 via gbp_usd, z -1.09, reacted); nifty_midcap_100 (rho 0.391 via aud_usd, z 0.33, quiet); dyn_stylebaaza_ns (rho 0.377 via aud_usd, z 2.65, reacted)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.563 vs eur_usd
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.522 vs aud_usd
- Watch next: dyn_lth (inverse) — not yet - watch; rho -0.502 vs eur_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.527, z -1.13); dyn_icicigi_bo (rho -0.427, z -1.09); nifty_midcap_100 (rho 0.391, z 0.33); dyn_stylebaaza_ns (rho 0.377, z 2.65)
- Source: Selloff in euro zone bonds pauses but oil prices keep up pressure — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/bonds/selloff-in-euro-zone-bonds-pauses-but-oil-prices-keep-up-pressure/articleshow/133341510.cms
- Source: ECB'S LANE: EURO ZONE INFLATION ONE PERCENTAGE POINT ABOVE ECB'S 2% TARGET IS A LOT — DeItaone, 2026-08-18. https://t.me/walter_bloomberg/34837
- Source: Euro zone bonds join global selloff, long-end yields at multi-year highs — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bonds-join-global-selloff-long-end-yields-at-multi-year-highs/articleshow/133321858.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 6.04] commodities · 3 series ↑
- corn [COMMODITIES]: last 498.25, z20 4.72, zc 5.91, resid-z 4.17 [unexplained], 1d 7.56%, |z20|=4.72; 1y-pct=100
- wheat [COMMODITIES]: last 696.50, z20 1.93, zc 2.70, resid-z 1.53 [unexplained], 1d 4.82%, |z20|=1.93; 1y-pct=99
- soybeans [COMMODITIES]: last 1236.00, z20 1.76, zc 2.86, resid-z 2.23 [unexplained], 1d 2.94%, |z20|=1.76; 1y-pct=99
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_lenskart_ns (rho 0.374 via wheat, z 3.09, reacted)
- **India receivers**: dyn_lenskart_ns (rho 0.374, z 3.09)
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [RED 5.34] dyn_voltas_ns ↓
- dyn_voltas_ns [EQUITIES]: last 1223.00, z20 -3.34, zc -1.24, resid-z -1.11 [quiet], 1d -2.39%, |z20|=3.34; 1y-pct=0
- **Mechanism**: dyn_voltas_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bharatcoal_ns (rho 0.568 via dyn_voltas_ns, z -2.35, reacted); nifty_midcap_100 (rho 0.516 via dyn_voltas_ns, z 0.33, quiet); nifty_50 (rho 0.395 via dyn_voltas_ns, z -0.89, quiet); dyn_havells_ns (rho 0.377 via dyn_voltas_ns, z 0.74, quiet); dyn_cupid_ns (rho 0.35 via dyn_voltas_ns, z 1.21, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.516 vs dyn_voltas_ns, historically leads by 5d
- **India receivers**: dyn_bharatcoal_ns (rho 0.568, z -2.35); nifty_midcap_100 (rho 0.516, z 0.33); nifty_50 (rho 0.395, z -0.89); dyn_havells_ns (rho 0.377, z 0.74)
- Source: Voltas reported strong growth in June quarter, but failed to impress — Mint Markets, 2026-08-18. https://www.livemint.com/market/mark-to-market/voltas-strong-growth-fails-to-impress-operating-revenue-acs-home-appliances-other-businesses-engineering-products-11787031152020.html
- Source: Voltas among 4 F&O stocks with a sharp rise in futures open interest — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/stocks/news/voltas-among-4-fampo-stocks-with-a-sharp-rise-in-futures-open-interest/slideshow/133310686.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-24 (d=0.0), 2024-11-14 (d=0.01)

### [RED 5.09] dyn_lenskart_ns ↑
- dyn_lenskart_ns [EQUITIES]: last 639.60, z20 3.09, zc 1.11, resid-z 0.91 [quiet], 1d 1.78%, |z20|=3.09; 1y-pct=99
- **Mechanism**: dyn_lenskart_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/stocks/news/lenskart-solutions-among-4-stocks-to-hit-52-week-highs-amp-surge-up-to-25-in-a-month/slideshow/133348316.cms
- Source: Lenskart shares gain over 5% to record high after incorporating new step-down subsidiary in China — Mint Markets, 2026-08-18. https://www.livemint.com/market/stock-market-news/lenskart-shares-gain-over-5-to-record-high-after-incorporating-new-step-down-subsidiary-in-china-11787043990119.html
- Source: Stocks to Watch, Aug 18: Paytm, Airtel, GMR Airports, Netweb Tech, SPR Auto, Lenskart, Manipal Health — BusinessLine Mkts, 2026-08-18. https://www.thehindubusinessline.com/markets/stock-markets/stocks-in-focus-paytm-airtel-gmr-airports-netweb-tech-spr-auto-lenskart-manipal-health-and-more/article71358731.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

### [RED 5.08] dxy ↓
- dxy [FX]: last 98.81, z20 -2.08, zc -2.65, resid-z -0.15 [moved], 1d -0.84%, 20d range extreme; |z20|=2.08
- **Mechanism**: dxy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

## Watchlist (below surfacing floor)
midcap_largecap_ratio ↑ (4.92), dyn_stylebaaza_ns ↑ (4.65), cross-asset · 4 series ↑ (4.46), rates · 2 series ↑ (4.35), dyn_bharatcoal_ns ↓ (4.35), dyn_coalindia_ns ↓ (4.25), dyn_meta ↓ (4.0), dyn_tech ↑ (3.99), usd_cny ↓ (3.16), dyn_icicigi_bo ↓ (3.09), eur_inr ↑ (3.02), nifty_fmcg ↓ (2.97)

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
- COALINDIA.NS (COAL INDIA LTD) score 96.7 — "BSE looks to launch MSCI-linked futures and options in India"
- INOXINDIA.NS (INOX INDIA LIMITED) score 96.4 — "BSE looks to launch MSCI-linked futures and options in India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 95.5 — "BSE looks to launch MSCI-linked futures and options in India"
- INDIANB.NS (INDIAN BANK) score 79.4 — "Indian stocks least preferred for Asia fund managers: BofA survey"
- BAC (Bank of America Corporation) score 64.0 — "The national debt just hit $40 trillion. Here’s how it can hurt Americans."
- HDB (HDFC Bank Limited) score 55.9 — "Nifty fall for seventh straight session; banks, metals drag as crude weighs on sentiment"
- BOND (PIMCO Active Bond Exchange-Tra) score 53.4 — "Treasury-market reprieve could be fleeting with deluge of corporate-bond issuance due in S"
- IDBI.NS (IDBI BANK LIMITED) score 51.7 — "Nifty fall for seventh straight session; banks, metals drag as crude weighs on sentiment"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 51.7 — "Nifty fall for seventh straight session; banks, metals drag as crude weighs on sentiment"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 51.7 — "Nifty fall for seventh straight session; banks, metals drag as crude weighs on sentiment"
- TECHM.NS (TECH MAHINDRA LIMITED) score 50.8 — "Apple’s stock could be the savviest buy within Big Tech, according to this analysis"
- COIN (Coinbase Global, Inc.) score 50.8 — "BlackRock, Capital Group anchor IDFC FIRST Bank’s maiden $500 million global bond"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 49.2 — "Apple’s stock could be the savviest buy within Big Tech, according to this analysis"
- TECH (Bio-Techne Corp) score 49.0 — "Apple’s stock could be the savviest buy within Big Tech, according to this analysis"
- OHI (Omega Healthcare Investors, In) score 41.7 — "Korean investors dump home stocks for US ones, buy same names at a premium | Is KOSPI-styl"
- CHKP (Check Point Software Technolog) score 34.3 — "Want to bet on the bond rally? Check out these overlooked funds."
- LTH (Life Time Group Holdings, Inc.) score 33.4 — "U.S. government debt passes $40 trillion mark for the first time"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.7 — "The Strongest El Niño on Record Lands on the Tightest Energy Market in Years"
- JIOFIN.BO (Jio Financial Services Limited) score 19.4 — "IRAN REPORTEDLY WEIGHS STRIKES ON U.S. TARGETS IN EUROPE Iran is considering expanding its"
- 301077.SZ (CHINASTARS) score 18.8 — "China’s Solar Exports Fell 21.4% in July"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 18.0 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 16.9 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- PCJEWELLER.NS (PC JEWELLER LTD) score 15.9 — "Lalithaa Jewellery IPO Day 3: Issue booked 63x, QIB category leads at 145x"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 14.3 — "Indian steel mills face margin squeeze as global coking coal prices rise"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 13.2 — "IRAN REPORTEDLY WEIGHS STRIKES ON U.S. TARGETS IN EUROPE Iran is considering expanding its"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 11.1 — "Market wrap:  HCL Tech, Sun Pharma, Power Grid, Bajaj Finance top gainers and losers on Ni"
- MRNA (Moderna, Inc.) score 10.7 — "US stocks: US market rises as yields ease, Moderna lifts healthcare stocks"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.3 — "The national debt just hit $40 trillion. Here’s how it can hurt Americans."
- MS (Morgan Stanley) score 9.7 — "ANTHROPIC LINES UP $10B+ CREDIT AHEAD OF IPO Anthropic’s revolving credit facility is set "
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 9.6 — "Korean investors dump home stocks for US ones, buy same names at a premium | Is KOSPI-styl"
- META (Meta) score 8.8 — "Metal stock to be in focus on Thursday after this Capex expansion update. Details here"
- VT (Vanguard Total World Stock Ind) score 8.6 — "World's Largest Electric Plane Flies for 27 Minutes on $5 of Power"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.6 — "IGL, MGL to Adani Total Gas: City gas distributor stocks rise up to 4%; here's why"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 7.2 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- NVDA (NVIDIA Corporation) score 6.7 — "NVDA - BOFA: NVIDIA COULD BE UP TO 50% UNDERVALUED Bank of America says Nvidia may trade a"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.3 — "ICICI Bank shares slip 0.52% in early trade, despite yearly gains"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.4 — "Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month"
- VOLTAS.NS (VOLTAS LTD) score 3.1 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.5 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
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