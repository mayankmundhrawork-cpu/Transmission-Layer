# Transmission Layer — board brief · 2026-08-28 16:36Z

data as of **2026-08-28** · 98 series · 8 red / 36 amber · 8 events surfaced (32 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.214, 2d in regime; vol-pct 0.135, breadth-off 0.294, Markov P(high-vol) 0.013)
- [WEAK] **safe_haven_gold** — corr20 -0.21, corr60 -0.39, last shift 2026-06-08. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.81, corr60 0.86, last shift 2026-01-29. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.21, corr60 0.33, last shift 2026-07-10. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.19, corr60 0.03, last shift 2026-07-14. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.35, corr60 -0.84, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.23, corr60 -0.15, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.11, corr60 -0.08, last shift 2026-06-25. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.26, corr60 0.2, last shift 2026-07-10. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 90** scanned series survive multiplicity control (effective p ≤ 0.0005605865536324472)
- **SETUP** dxy → aud_usd: leads 1d (ccf -0.569, β -0.8489, p 0.0); driver zc 1.55 → expected -0.439%. Type hit-rate 0.812 (n=2272).
- Track record · residual_reversion: hit-rate **0.497** (n=1121) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.812** (n=2272) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.36] commodities · 3 series ↑
- wheat [COMMODITIES]: last 787.00, z20 4.04, zc 2.76, resid-z 2.90 [unexplained], 1d 5.96%, |z20|=4.04; 1y-pct=100
- corn [COMMODITIES]: last 539.50, z20 3.06, zc 4.49, resid-z 3.45 [unexplained], 1d 5.73%, |z20|=3.06; 1y-pct=100
- soybeans [COMMODITIES]: last 1286.00, z20 2.77, zc 2.30, resid-z 2.13 [unexplained], 1d 2.35%, |z20|=2.77; 1y-pct=100
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: UBS SEES COMMODITY OPPORTUNITIES BEYOND OIL UBS sees opportunities across copper, agriculture and gold, arguing commodities offer both returns and inflation protection. Copper should benefit from AI infrastructure and electrification. Wheat and corn are gaining as a — DeItaone, 2026-08-27. https://t.me/walter_bloomberg/35133
- Source: Wheat Hits Three-Year High as Russia Prepares to Escalate War — Mint Markets, 2026-08-27. https://www.livemint.com/market/wheat-hits-three-year-high-as-russia-prepares-to-escalate-war-11787802575795.html
- Source: Wheat soars to daily limit on Black Sea export worries, corn at lifetime highs — Mint Markets, 2026-08-26. https://www.livemint.com/market/wheat-soars-to-daily-limit-on-black-sea-export-worries-corn-at-lifetime-highs-11787773711563.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [RED 5.58] dyn_chkp ↑
- dyn_chkp [EQUITIES]: last 139.63, z20 3.58, zc 1.76, resid-z -0.10 [moved], 1d 4.80%, |z20|=3.58
- **Mechanism**: dyn_chkp ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_karurvysya_ns (rho -0.363 via dyn_chkp, z 1.25, reacted)
- **India receivers**: dyn_karurvysya_ns (rho -0.363, z 1.25)
- Source: The bull market for stocks is defying everything, but Bank of America warns that an autumn reality check is coming — MarketWatch Top, 2026-08-28. https://www.marketwatch.com/story/the-bull-market-for-stocks-is-defying-everything-but-bank-of-america-warns-that-an-autumn-reality-check-is-coming-8cdf831f?mod=mw_rss_topstories
- Source: Over 45% returns in one month, now double delight of bonus share and dividend | Check record date, ratio — Mint Markets, 2026-08-28. https://www.livemint.com/market/stock-market-news/over-45-returns-in-one-month-now-double-delight-of-bonus-share-and-dividend-check-record-date-ratio-11787906215782.html
- Source: Elara initiates coverage on Alkem, Eris, IPCA and Mankind. Check ratings and targets — ET Markets, 2026-08-28. https://economictimes.indiatimes.com/markets/stocks/news/elara-initiates-coverage-on-alkem-eris-ipca-and-mankind-check-ratings-and-targets/articleshow/133586795.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2024-10-18 (d=0.02)

### [RED 5.47] dyn_icicigi_bo ↓
- dyn_icicigi_bo [EQUITIES]: last 1563.00, z20 -3.47, zc -1.20, resid-z -0.98 [quiet], 1d -1.91%, |z20|=3.47; 1y-pct=0
- **Mechanism**: dyn_icicigi_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Lenskart Rs 1,857-crore block deal: Goldman Sachs, Morgan Stanley, ICICI Prudential, SBI MF among buyers as Alpha Wave exits — ET Markets, 2026-08-28. https://economictimes.indiatimes.com/markets/stocks/news/lenskart-rs-1857-crore-block-deal-goldman-sachs-morgan-stanley-icici-prudential-sbi-mf-among-buyers-as-alpha-wave-exits/articleshow/133594276.cms
- Source: Market wrap: TCS, Tech Mahindra, ICICI Bank, ITC top gainers and losers on Nifty and Sensex on Friday — ET Markets, 2026-08-28. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-tcs-tech-mahindra-icici-bank-itc-top-gainers-and-losers-on-nifty-and-sensex-on-friday/articleshow/133589753.cms
- Source: ICICI Bank shares slide 1.32% amid $1 billion bond issuance and employee stock allotment — BusinessLine Mkts, 2026-08-28. https://www.thehindubusinessline.com/markets/icici-bank-shares-slide-132-amid-1-billion-bond-issuance-and-employee-stock-allotment/article71399396.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.0), 2025-05-30 (d=0.03)

### [AMBER 5.0] brent ↓
- brent [COMMODITIES]: last 87.99, z20 -0.00, zc -0.82, resid-z -0.52 [quiet], 1d -1.91%, 1-session move -1.91% ≥ 1.5%
- **Mechanism**: brent ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: wti (co-move) — not yet - watch; rho 0.98 vs brent, historically leads by 5d
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.593 vs brent, historically leads by 5d
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.532 vs brent, historically leads by 5d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.693 vs brent
- Source: Oil Shrugs Off Trump’s ‘Toughest Sanctions in History’ — OilPrice, 2026-08-28. https://oilprice.com/Energy/Crude-Oil/Oil-Shrugs-Off-Trumps-Toughest-Sanctions-in-History.html
- Source: Oil Selloff Outruns Reality in Hormuz — OilPrice, 2026-08-28. https://oilprice.com/Energy/Energy-General/Oil-Selloff-Outruns-Reality-in-Hormuz.html
- Source: Gulf Oil Exports Rebound Despite Iran War — OilPrice, 2026-08-28. https://oilprice.com/Latest-Energy-News/World-News/Gulf-Oil-Exports-Rebound-Despite-Iran-War.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.0), 2024-10-18 (d=0.02)

### [RED 4.77] dyn_adanient_bo ↑
- dyn_adanient_bo [EQUITIES]: last 3166.00, z20 2.77, zc 0.17, resid-z -0.20 [quiet], 1d 0.35%, |z20|=2.77; 1y-pct=97
- **Mechanism**: dyn_adanient_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.465 via dyn_adanient_bo, z -1.08, reacted); nifty_midcap_100 (rho 0.431 via dyn_adanient_bo, z 1.15, reacted); dyn_indusindbk_bo (rho 0.386 via dyn_adanient_bo, z -1.54, reacted); nifty_fmcg (rho 0.358 via dyn_adanient_bo, z -1.87, reacted)
- **India receivers**: nifty_50 (rho 0.465, z -1.08); nifty_midcap_100 (rho 0.431, z 1.15); dyn_indusindbk_bo (rho 0.386, z -1.54); nifty_fmcg (rho 0.358, z -1.87)
- Source: Market wrap: Adani Enterprises, Kotak Mahindra Bank, HDFC Bank, M&M top gainers and losers on Nifty and Sensex on Thursday — ET Markets, 2026-08-27. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-adani-enterprises-kotak-mahindra-bank-hdfc-bank-mm-top-gainers-and-losers-on-nifty-and-sensex-on-thursday/articleshow/133566380.cms
- Source: Motilal Oswal initiates coverage on Adani Enterprises with Buy, sees 25% upside. Here’s why — ET Markets, 2026-08-27. https://economictimes.indiatimes.com/markets/stocks/news/motilal-oswal-initiates-coverage-on-adani-enterprises-with-buy-sees-25-upside-heres-why/articleshow/133558689.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [AMBER 4.49] cross-asset · 3 series ↑
- vix [INDICES]: last 14.64, z20 -1.17, zc 0.12, resid-z n/a [quiet], 1d 0.90%, 1y-pct=5
- dyn_vt [EQUITIES]: last 160.97, z20 0.32, zc -0.53, resid-z 0.06 [quiet], 1d -0.37%, 1y-pct=96
- sp500 [INDICES]: last 7718.93, z20 0.26, zc -0.22, resid-z -0.23 [quiet], 1d -0.16%, 1y-pct=96
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-27 (z-distance 0.14).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.667 vs vix, historically leads by 5d
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.554 vs dyn_vt, historically leads by 5d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.645 vs vix
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.56 vs dyn_vt
- Watch next: dyn_nvda (inverse) — not yet - watch; rho -0.555 vs vix
- Source: Park Medi World targets 5,740-bed network by FY28 under expansion roadmap — Mint Markets, 2026-08-28. https://www.livemint.com/market/stock-market-news/park-medi-world-targets-5-740-bed-network-by-fy28-under-expansion-roadmap-11787926171520.html
- Source: US stock market today: Wall Street futures edge lower as investors await Kevin Warsh's Jackson Hole speech — Mint Markets, 2026-08-28. https://www.livemint.com/market/us-stock-market-today-wall-street-futures-edge-lower-as-investors-await-kevin-warshs-jackson-hole-speech-11787914922667.html
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: US markets turn green after Fed chief Warsh's speech at Jackson Hole — ET Markets, 2026-08-28. https://economictimes.indiatimes.com/markets/us-stocks/news/dow-jones-us-stock-market-live-updates-nasdaq-sp-500-iran-israel-war-hormuz-deal-brent-crude-oil-earnings-forecast-jackson-hole-fed-kevin-warsh-speech-rate-hike-outlook-hints-nvidia-salesforce-paypal-gap-marvell-micron-chip-stock-price-news-28th-august-2026/liveblog/133591066.cms
- Historical analogues: 2025-08-27 (d=0.14), 2025-10-23 (d=0.17), 2025-10-31 (d=0.17)

### [AMBER 4.4] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.65, z20 1.40, zc n/a, resid-z n/a [quiet], 1d -0.29%, 52-wk extreme (pct=99); 1y-pct=99
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_techm_ns (rho -0.384 via midcap_largecap_ratio, z 0.86, quiet); dyn_inoxindia_ns (rho 0.368 via midcap_largecap_ratio, z 3.16, reacted); nifty_fmcg (rho -0.363 via midcap_largecap_ratio, z -1.87, reacted); nifty_it (rho -0.361 via midcap_largecap_ratio, z 0.53, quiet); nifty_50 (rho -0.359 via midcap_largecap_ratio, z -1.08, reacted)
- **India receivers**: dyn_techm_ns (rho -0.384, z 0.86); dyn_inoxindia_ns (rho 0.368, z 3.16); nifty_fmcg (rho -0.363, z -1.87); nifty_it (rho -0.361, z 0.53)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [AMBER 4.2] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1616.30, z20 2.20, zc 2.53, resid-z 2.30 [unexplained], 1d 8.09%, |z20|=2.20; 1y-pct=100
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Hero MotoCorp buys Rs 1,758 crore Ather Energy stake in block deal — ET Markets, 2026-08-28. https://economictimes.indiatimes.com/markets/stocks/news/hero-motocorp-buys-rs-1758-crore-ather-energy-stake-in-block-deal/articleshow/133594919.cms
- Source: Ather Energy share price jumps 10% | here's why — Mint Markets, 2026-08-28. https://www.livemint.com/market/stock-market-news/ather-energy-share-price-jumps-10-heres-why-11787894092380.html
- Source: Ather Energy shares rally 4% as Hero MotoCorp plans Rs 1,758 crore investment — ET Markets, 2026-08-28. https://economictimes.indiatimes.com/markets/stocks/news/ather-energy-shares-rally-4-as-hero-motocorp-plans-rs-1758-crore-investment/articleshow/133583523.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

## Watchlist (below surfacing floor)
usd_jpy ↑ (3.77), gold_silver_ratio ↓ (3.74), dyn_havells_ns ↓ (3.64), natgas ↑ (3.59), dyn_hdb ↓ (3.45), dyn_inoxindia_ns ↑ (3.16), dyn_stylebaaza_ns ↑ (3.01), indices · 2 series ↑ (2.96), comex_copper ↑ (2.87), indices · 2 series ↑ (2.86), dyn_tech ↑ (2.8), dyn_lenskart_ns ↑ (2.78)

## India macro
- nifty_50: 24175.6504 (1d 0.35%, z20 -1.08, flag none)
- nifty_midcap_100: 64070.1016 (1d 0.06%, z20 1.15, flag amber)
- usd_inr: 95.3680 (1d -0.07%, z20 0.01, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6502 (1d -0.29%, z20 1.40, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 87.9 — "India 10-year yield at more than two-month peak on supply, Warsh speech"
- INOXINDIA.NS (INOX INDIA LIMITED) score 87.0 — "India 10-year yield at more than two-month peak on supply, Warsh speech"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 85.6 — "India 10-year yield at more than two-month peak on supply, Warsh speech"
- INDIANB.NS (INDIAN BANK) score 83.0 — "Indian government bonds: 10-yr yield at more than two-month peak on supply, Warsh speech"
- BAC (Bank of America Corporation) score 70.1 — "ICICI Bank shares slide 1.32% amid $1 billion bond issuance and employee stock allotment"
- HDB (HDFC Bank Limited) score 64.1 — "ICICI Bank shares slide 1.32% amid $1 billion bond issuance and employee stock allotment"
- IDBI.NS (IDBI BANK LIMITED) score 60.8 — "ICICI Bank shares slide 1.32% amid $1 billion bond issuance and employee stock allotment"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 60.8 — "ICICI Bank shares slide 1.32% amid $1 billion bond issuance and employee stock allotment"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 60.8 — "ICICI Bank shares slide 1.32% amid $1 billion bond issuance and employee stock allotment"
- OHI (Omega Healthcare Investors, In) score 53.7 — "Tempsens Instruments doubles IPO investors’ money as stock lists at 111% premium. Should y"
- TECHM.NS (TECH MAHINDRA LIMITED) score 53.5 — "IT stocks surge: Why Nifty IT is up today - Reason behind TCS, Infosys, Wipro, Tech Mahind"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 52.1 — "IT stocks surge: Why Nifty IT is up today - Reason behind TCS, Infosys, Wipro, Tech Mahind"
- TECH (Bio-Techne Corp) score 52.1 — "IT stocks surge: Why Nifty IT is up today - Reason behind TCS, Infosys, Wipro, Tech Mahind"
- COIN (Coinbase Global, Inc.) score 51.3 — "Global Market: China stocks steady as property shares offset Biotech, chip losses"
- BOND (PIMCO Active Bond Exchange-Tra) score 48.9 — "Indian government bonds: 10-yr yield at more than two-month peak on supply, Warsh speech"
- NVDA (NVIDIA Corporation) score 36.6 — "NVIDIA TO START EMPLOYEE-FUNDED U.S. POLITICAL ACTION COMMITTEE CALLED NVPAC - SOURCE FAMI"
- CHKP (Check Point Software Technolog) score 34.5 — "Symbiotec Pharmalab IPO allotment to be finalised today. Here's GMP, how to check status o"
- LTH (Life Time Group Holdings, Inc.) score 34.2 — "Lumino Industries IPO Day 2: Issue subscribed 2.63 times so far. Here's GMP, review & othe"
- 301077.SZ (CHINASTARS) score 27.4 — "Global Market: China stocks steady as property shares offset Biotech, chip losses"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 21.7 — "Retail investors bet big on these 12 smallcap stocks that rallied up to 150%; 3 turned mul"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.7 — "Ather Energy share price jumps 10% | here's why"
- JIOFIN.BO (Jio Financial Services Limited) score 19.4 — "JM Financial calls Metropolis Healthcare ‘best-value diagnostic stock’, sees up to   27%  "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 16.2 — "Noel Tata, Shapoorji discuss share swap for Tata Sons stake sale"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 16.0 — "Noel Tata, Shapoorji discuss share swap for Tata Sons stake sale"
- MS (Morgan Stanley) score 15.3 — "Lenskart Rs 1,857-crore block deal: Goldman Sachs, Morgan Stanley, ICICI Prudential, SBI M"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 14.8 — "Welspun Corp, Piramal Finance, Divis Labs among 12 BSE 500 stocks that jumped to their rec"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 12.6 — "JM Financial calls Metropolis Healthcare ‘best-value diagnostic stock’, sees up to   27%  "
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 12.5 — "Sebi approves 7 IPOs including Jio Platforms, Paras Healthcare and Bharat PET"
- META (Meta) score 11.3 — "Hindustan Copper: Strong metal cycle aids earnings growth, but valuation is not cheap"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 10.7 — "ICICI Bank shares slide 1.32% amid $1 billion bond issuance and employee stock allotment"
- PCJEWELLER.NS (PC JEWELLER LTD) score 10.0 — "Deepa Jewellers IPO: ₹460-cr issue to open on September 1, price band fixed at ₹168-177"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.9 — "Motilal Oswal initiates coverage on Adani Enterprises with Buy, sees 25% upside. Here’s wh"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.0 — "Upper circuit as losing streak ends - Just Dial share price surges 10% | Can it rise furth"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 7.0 — "Lenskart Rs 1,857-crore block deal: Goldman Sachs, Morgan Stanley, ICICI Prudential, SBI M"
- VT (Vanguard Total World Stock Ind) score 6.3 — "Park Medi World targets 5,740-bed network by FY28 under expansion roadmap"
- DKS (Dick's Sporting Goods Inc) score 3.2 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- MRNA (Moderna, Inc.) score 2.4 — "Can Wolfe’s upgrade push Moderna stock higher?"
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