# Transmission Layer — board brief · 2026-08-19 18:52Z

data as of **2026-08-19** · 98 series · 14 red / 31 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.293, 3d in regime; vol-pct 0.233, breadth-off 0.353, Markov P(high-vol) 0.014)
- [INVERTED] **safe_haven_gold** — corr20 -0.42, corr60 -0.41, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.87, last shift 2026-05-13. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.27, corr60 0.39, last shift 2026-07-01. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.18, corr60 -0.11, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.69, corr60 -0.82, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.08, corr60 -0.11, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.19, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.07, corr60 0.23, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.0009329597122151867)
- **SETUP** dxy → aud_usd: leads 1d (ccf -0.573, β -0.8513, p 0.0); driver zc -2.56 → expected 0.693%. Type hit-rate 0.83 (n=2330).
- **SETUP** btc_usd → asx_200: leads 1d (ccf 0.311, β 0.0882, p 0.0); driver zc 3.19 → expected 0.501%. Type hit-rate 0.83 (n=2330).
- Track record · residual_reversion: hit-rate **0.496** (n=1115) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.83** (n=2330) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 29.79] dyn_mrna ↑
- dyn_mrna [EQUITIES]: last 155.77, z20 27.79, zc 36.33, resid-z 0.65 [moved], 1d 147.41%, |z20|=27.79; 1y-pct=100
- **Mechanism**: dyn_mrna ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Wall St rises as yields ease, Moderna lifts healthcare stocks — Mint Markets, 2026-08-19. https://www.livemint.com/market/wall-st-rises-as-yields-ease-moderna-lifts-healthcare-stocks-11787165297698.html
- Source: Moderna shares soar 135% in a day after cancer vaccine succeeds in late-stage trial — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/moderna-shares-soar-135-in-a-day-after-cancer-vaccine-succeeds-in-late-stage-trial/articleshow/133351080.cms
- Source: Moderna shares soar 159% in a day after cancer vaccine succeeds in late-stage trial — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/moderna-shares-soar-135-in-a-day-after-cancer-vaccine-succeeds-in-late-stage-trial/articleshow/133351080.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-16 (d=0.01), 2025-08-20 (d=0.01)

### [RED 11.67] crypto · 2 series ↑
- eth_usd [CRYPTO]: last 2088.60, z20 8.83, zc 2.39, resid-z 2.43 [unexplained], 1d 8.98%, |z20|=8.83
- btc_usd [CRYPTO]: last 68354.57, z20 7.22, zc 3.19, resid-z 2.16 [unexplained], 1d 5.68%, |z20|=7.22
- **Mechanism**: crypto · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-11-11 (z-distance 2.44).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_coin (co-move) — not yet - watch; rho 0.829 vs eth_usd, historically leads by 5d
- Watch next: vix (inverse) — not yet - watch; rho -0.653 vs eth_usd
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.592 vs eth_usd
- Watch next: sp500 (co-move) — not yet - watch; rho 0.56 vs eth_usd
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.521 vs eth_usd
- Source: Bitcoin near $64,350 as weak liquidity and subdued on-chain activity signal caution — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-near-64350-as-weak-liquidity-and-subdued-on-chain-activity-signal-caution/articleshow/133344028.cms
- Source: Bitcoin climbs towards $64,000 as cooling inflation and falling treasury yields aid recovery — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/cryptocurrency/crypto-news/bitcoin-climbs-towards-64000-as-cooling-inflation-and-falling-treasury-yields-aid-recovery/articleshow/133318408.cms
- Historical analogues: 2024-11-11 (d=2.44), 2025-07-10 (d=3.38), 2026-03-16 (d=4.01)

### [RED 6.22] fx · 4 series ↑
- eur_usd [FX]: last 1.17, z20 2.56, zc 2.47, resid-z 1.87 [unexplained], 1d 0.81%, |z20|=2.56
- aud_usd [FX]: last 0.71, z20 2.29, zc 0.45, resid-z 0.66 [quiet], 1d 0.22%, |z20|=2.29
- gbp_usd [FX]: last 1.36, z20 2.15, zc 1.02, resid-z 0.69 [quiet], 1d 0.43%, |z20|=2.15
- usd_mxn [FX]: last 16.94, z20 -1.96, zc -1.40, resid-z -1.18 [quiet], 1d -0.50%, |z20|=1.96; 1y-pct=0
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.526 via usd_mxn, z -1.13, reacted); dyn_icicigi_bo (rho -0.427 via gbp_usd, z -1.09, reacted); nifty_midcap_100 (rho 0.392 via aud_usd, z 0.33, quiet)
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.594 vs eur_usd, historically leads by 4d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.554 vs eur_usd
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.524 vs aud_usd
- Watch next: dyn_lth (inverse) — not yet - watch; rho -0.501 vs eur_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.526, z -1.13); dyn_icicigi_bo (rho -0.427, z -1.09); nifty_midcap_100 (rho 0.392, z 0.33)
- Source: Selloff in euro zone bonds pauses but oil prices keep up pressure — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/bonds/selloff-in-euro-zone-bonds-pauses-but-oil-prices-keep-up-pressure/articleshow/133341510.cms
- Source: ECB'S LANE: EURO ZONE INFLATION ONE PERCENTAGE POINT ABOVE ECB'S 2% TARGET IS A LOT — DeItaone, 2026-08-18. https://t.me/walter_bloomberg/34837
- Source: Euro zone bonds join global selloff, long-end yields at multi-year highs — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bonds-join-global-selloff-long-end-yields-at-multi-year-highs/articleshow/133321858.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [RED 6.04] commodities · 3 series ↑
- corn [COMMODITIES]: last 498.25, z20 4.72, zc 5.91, resid-z 4.31 [unexplained], 1d 7.56%, |z20|=4.72; 1y-pct=100
- wheat [COMMODITIES]: last 696.50, z20 1.93, zc 2.70, resid-z 1.60 [unexplained], 1d 4.82%, |z20|=1.93; 1y-pct=99
- soybeans [COMMODITIES]: last 1236.00, z20 1.76, zc 2.86, resid-z 2.32 [unexplained], 1d 2.94%, |z20|=1.76; 1y-pct=99
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_lenskart_ns (rho 0.374 via wheat, z 3.09, reacted)
- **India receivers**: dyn_lenskart_ns (rho 0.374, z 3.09)
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [AMBER 5.72] rates · 3 series ↑
- ust_30y [RATES]: last 5.31, z20 2.40, zc 1.46, resid-z 1.25 [quiet], 1d 1.14%, |z20|=2.40; 1y-pct=100
- ust_10y [RATES]: last 4.72, z20 1.35, zc 0.85, resid-z 0.60 [quiet], 1d 0.85%, 1y-pct=99
- tips_10y_real [RATES]: last 2.44, z20 1.06, zc 0.83, resid-z 0.48 [quiet], 1d 1.24%, 1y-pct=99
- **Mechanism**: rates · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.579 vs ust_30y, historically leads by 3d
- Watch next: wti (co-move) — not yet - watch; rho 0.559 vs ust_30y, historically leads by 3d
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.541 vs ust_30y, historically leads by 1d
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.526 vs tips_10y_real, historically leads by 4d
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.522 vs ust_30y, historically leads by 1d
- Source: US stocks bounce back as bond yields retreat — Mint Markets, 2026-08-19. https://www.livemint.com/market/stock-market-news/us-stocks-bounce-back-as-bond-yields-retreat-11787146991392.html
- Source: US stocks bounce back as bond yields retreat, Moderna rallies over 150%, Merck jumps 9.6% — Mint Markets, 2026-08-19. https://www.livemint.com/market/stock-market-news/us-stocks-bounce-back-as-bond-yields-retreat-11787146991392.html
- Source: US stocks: US market regains ground as bond yields ease; healthcare stocks rally — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-us-market-opens-up-after-tech-led-slump-as-yields-ease-earnings-watched/articleshow/133350322.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.25), 2026-03-30 (d=0.31)

### [RED 5.34] dyn_voltas_ns ↓
- dyn_voltas_ns [EQUITIES]: last 1223.00, z20 -3.34, zc -1.24, resid-z -1.12 [quiet], 1d -2.39%, |z20|=3.34; 1y-pct=0
- **Mechanism**: dyn_voltas_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bharatcoal_ns (rho 0.568 via dyn_voltas_ns, z -2.35, reacted); nifty_midcap_100 (rho 0.516 via dyn_voltas_ns, z 0.33, quiet); nifty_50 (rho 0.395 via dyn_voltas_ns, z -0.89, quiet); dyn_havells_ns (rho 0.377 via dyn_voltas_ns, z 0.74, quiet); dyn_cupid_ns (rho 0.35 via dyn_voltas_ns, z 1.21, reacted)
- Watch next: nifty_midcap_100 (co-move) — not yet - watch; rho 0.516 vs dyn_voltas_ns, historically leads by 5d
- **India receivers**: dyn_bharatcoal_ns (rho 0.568, z -2.35); nifty_midcap_100 (rho 0.516, z 0.33); nifty_50 (rho 0.395, z -0.89); dyn_havells_ns (rho 0.377, z 0.74)
- Source: Voltas reported strong growth in June quarter, but failed to impress — Mint Markets, 2026-08-18. https://www.livemint.com/market/mark-to-market/voltas-strong-growth-fails-to-impress-operating-revenue-acs-home-appliances-other-businesses-engineering-products-11787031152020.html
- Source: Voltas among 4 F&O stocks with a sharp rise in futures open interest — ET Markets, 2026-08-18. https://economictimes.indiatimes.com/markets/stocks/news/voltas-among-4-fampo-stocks-with-a-sharp-rise-in-futures-open-interest/slideshow/133310686.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-24 (d=0.0), 2024-11-14 (d=0.01)

### [RED 5.09] dyn_lenskart_ns ↑
- dyn_lenskart_ns [EQUITIES]: last 639.60, z20 3.09, zc 1.11, resid-z 0.93 [quiet], 1d 1.78%, |z20|=3.09; 1y-pct=99
- **Mechanism**: dyn_lenskart_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month — ET Markets, 2026-08-19. https://economictimes.indiatimes.com/markets/stocks/news/lenskart-solutions-among-4-stocks-to-hit-52-week-highs-amp-surge-up-to-25-in-a-month/slideshow/133348316.cms
- Source: Lenskart shares gain over 5% to record high after incorporating new step-down subsidiary in China — Mint Markets, 2026-08-18. https://www.livemint.com/market/stock-market-news/lenskart-shares-gain-over-5-to-record-high-after-incorporating-new-step-down-subsidiary-in-china-11787043990119.html
- Source: Stocks to Watch, Aug 18: Paytm, Airtel, GMR Airports, Netweb Tech, SPR Auto, Lenskart, Manipal Health — BusinessLine Mkts, 2026-08-18. https://www.thehindubusinessline.com/markets/stock-markets/stocks-in-focus-paytm-airtel-gmr-airports-netweb-tech-spr-auto-lenskart-manipal-health-and-more/article71358731.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-29 (d=0.13), 2025-12-24 (d=0.24)

### [RED 5.04] dxy ↓
- dxy [FX]: last 98.84, z20 -2.04, zc -2.56, resid-z -0.61 [moved], 1d -0.81%, 20d range extreme; |z20|=2.04
- **Mechanism**: dxy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

## Watchlist (below surfacing floor)
midcap_largecap_ratio ↑ (4.92), dyn_stylebaaza_ns ↑ (4.65), cross-asset · 4 series ↑ (4.48), dyn_bharatcoal_ns ↓ (4.35), comex_gold ↑ (4.27), dyn_coalindia_ns ↓ (4.25), dyn_tech ↑ (3.87), dyn_meta ↓ (3.77), usd_cny ↓ (3.4), gold_silver_ratio ↑ (3.2), dyn_icicigi_bo ↓ (3.09), dyn_hdb ↓ (3.0)

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
- COALINDIA.NS (COAL INDIA LTD) score 98.4 — "BSE looks to launch MSCI-linked futures and options in India"
- INOXINDIA.NS (INOX INDIA LIMITED) score 98.1 — "BSE looks to launch MSCI-linked futures and options in India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 97.2 — "BSE looks to launch MSCI-linked futures and options in India"
- INDIANB.NS (INDIAN BANK) score 80.8 — "Indian stocks least preferred for Asia fund managers: BofA survey"
- BAC (Bank of America Corporation) score 64.1 — "POLL SHOWS 69% SEE TRUMP BUSINESS INFLUENCE A Reuters/Ipsos poll found 69% of Americans be"
- HDB (HDFC Bank Limited) score 56.9 — "Nifty fall for seventh straight session; banks, metals drag as crude weighs on sentiment"
- BOND (PIMCO Active Bond Exchange-Tra) score 54.4 — "Treasury-market reprieve could be fleeting with deluge of corporate-bond issuance due in S"
- IDBI.NS (IDBI BANK LIMITED) score 52.7 — "Nifty fall for seventh straight session; banks, metals drag as crude weighs on sentiment"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 52.7 — "Nifty fall for seventh straight session; banks, metals drag as crude weighs on sentiment"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 52.6 — "Nifty fall for seventh straight session; banks, metals drag as crude weighs on sentiment"
- TECHM.NS (TECH MAHINDRA LIMITED) score 51.8 — "Apple’s stock could be the savviest buy within Big Tech, according to this analysis"
- COIN (Coinbase Global, Inc.) score 51.7 — "BlackRock, Capital Group anchor IDFC FIRST Bank’s maiden $500 million global bond"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 50.0 — "Apple’s stock could be the savviest buy within Big Tech, according to this analysis"
- TECH (Bio-Techne Corp) score 49.9 — "Apple’s stock could be the savviest buy within Big Tech, according to this analysis"
- OHI (Omega Healthcare Investors, In) score 42.4 — "Korean investors dump home stocks for US ones, buy same names at a premium | Is KOSPI-styl"
- CHKP (Check Point Software Technolog) score 34.9 — "Want to bet on the bond rally? Check out these overlooked funds."
- LTH (Life Time Group Holdings, Inc.) score 33.0 — "Ukraine’s Ousted Defense Chief Calls for Wartime Elections"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.1 — "The Strongest El Niño on Record Lands on the Tightest Energy Market in Years"
- JIOFIN.BO (Jio Financial Services Limited) score 19.8 — "IRAN REPORTEDLY WEIGHS STRIKES ON U.S. TARGETS IN EUROPE Iran is considering expanding its"
- 301077.SZ (CHINASTARS) score 19.1 — "China’s Solar Exports Fell 21.4% in July"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 18.3 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 17.2 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- PCJEWELLER.NS (PC JEWELLER LTD) score 16.2 — "Lalithaa Jewellery IPO Day 3: Issue booked 63x, QIB category leads at 145x"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 14.5 — "Indian steel mills face margin squeeze as global coking coal prices rise"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 13.4 — "IRAN REPORTEDLY WEIGHS STRIKES ON U.S. TARGETS IN EUROPE Iran is considering expanding its"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 11.3 — "Market wrap:  HCL Tech, Sun Pharma, Power Grid, Bajaj Finance top gainers and losers on Ni"
- MS (Morgan Stanley) score 9.9 — "ANTHROPIC LINES UP $10B+ CREDIT AHEAD OF IPO Anthropic’s revolving credit facility is set "
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 9.8 — "Korean investors dump home stocks for US ones, buy same names at a premium | Is KOSPI-styl"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.5 — "Ashok Leyland just had a record June quarter. So why did the margin fall a full point?"
- META (Meta) score 8.9 — "Metal stock to be in focus on Thursday after this Capex expansion update. Details here"
- VT (Vanguard Total World Stock Ind) score 8.8 — "World's Largest Electric Plane Flies for 27 Minutes on $5 of Power"
- MRNA (Moderna, Inc.) score 7.8 — "Moderna shares climb over 150% as mRNA vaccine with Merck succeeds in large trial for skin"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.7 — "IGL, MGL to Adani Total Gas: City gas distributor stocks rise up to 4%; here's why"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 7.3 — "Top Gainers & Losers on 19 Aug: Netweb Tech, Bata, Reliance Power, Bharat Dynamics, Tata C"
- NVDA (NVIDIA Corporation) score 6.8 — "NVDA - BOFA: NVIDIA COULD BE UP TO 50% UNDERVALUED Bank of America says Nvidia may trade a"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.4 — "ICICI Bank shares slip 0.52% in early trade, despite yearly gains"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.5 — "Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month"
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