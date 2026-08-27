# Transmission Layer — board brief · 2026-08-27 15:13Z

data as of **2026-08-27** · 98 series · 13 red / 33 amber · 8 events surfaced (32 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.213, 2d in regime; vol-pct 0.191, breadth-off 0.235, Markov P(high-vol) 0.014)
- [INVERTED] **safe_haven_gold** — corr20 -0.27, corr60 -0.4, contra nifty_50 corr20=0.0, last shift 2026-06-05. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.8, corr60 0.87, last shift 2026-02-05. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.07, corr60 0.31, last shift 2026-07-09. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.01, corr60 -0.04, last shift 2026-07-10. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.55, corr60 -0.84, last shift 2026-05-06. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.23, corr60 -0.15, last shift 2026-01-23. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.02, corr60 -0.08, last shift 2026-07-01. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.26, corr60 0.2, last shift 2026-07-09. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **5 of 90** scanned series survive multiplicity control (effective p ≤ 0.0023657814862088067)
- **SETUP** dyn_nvda → taiwan_weighted: leads 1d (ccf 0.406, β 0.2447, p 0.0); driver zc 3.3 → expected 1.799%. Type hit-rate 0.817 (n=2224).
- **SETUP** dyn_nvda → nikkei_225: leads 1d (ccf 0.397, β 0.2283, p 0.0); driver zc 3.3 → expected 1.679%. Type hit-rate 0.817 (n=2224).
- **SETUP** dyn_nvda → usd_mxn: leads 1d (ccf -0.345, β -0.0745, p 0.0); driver zc 3.3 → expected -0.548%. Type hit-rate 0.817 (n=2224).
- **SETUP** dyn_nvda → kospi: leads 1d (ccf 0.272, β 0.245, p 0.0); driver zc 3.3 → expected 1.802%. Type hit-rate 0.817 (n=2224).
- Track record · residual_reversion: hit-rate **0.498** (n=1121) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.817** (n=2224) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.43] dyn_inoxindia_ns ↑
- dyn_inoxindia_ns [EQUITIES]: last 2160.30, z20 10.43, zc 7.38, resid-z 3.36 [unexplained], 1d 12.12%, |z20|=10.43; 1y-pct=100
- **Mechanism**: dyn_inoxindia_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.377 via dyn_inoxindia_ns, z 1.92, reacted)
- **India receivers**: midcap_largecap_ratio (rho 0.377, z 1.92)
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-14 (d=0.02), 2026-06-18 (d=0.04)

### [RED 7.77] dyn_indusindbk_bo ↓
- dyn_indusindbk_bo [EQUITIES]: last 970.00, z20 -5.77, zc -1.89, resid-z -3.04 [unexplained], 1d -3.19%, |z20|=5.77
- **Mechanism**: dyn_indusindbk_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.504 via dyn_indusindbk_bo, z -1.67, reacted); nifty_midcap_100 (rho 0.459 via dyn_indusindbk_bo, z 1.03, reacted); nifty_fmcg (rho 0.438 via dyn_indusindbk_bo, z -1.83, reacted); dyn_adanient_bo (rho 0.384 via dyn_indusindbk_bo, z 3.24, reacted); dyn_karurvysya_ns (rho 0.379 via dyn_indusindbk_bo, z 1.35, reacted)
- **India receivers**: nifty_50 (rho 0.504, z -1.67); nifty_midcap_100 (rho 0.459, z 1.03); nifty_fmcg (rho 0.438, z -1.83); dyn_adanient_bo (rho 0.384, z 3.24)
- Source: IndusInd Bank Share Price Live Updates: IndusInd Bank Moves Past 20-Day SMA — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/indusind-bank-share-price-live-26-aug-2026/liveblog/133528142.cms
- Source: IndusInd Bank Share Price Live Updates: IndusInd Bank's Current Price and Market Performance — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/indusind-bank-share-price-live-26-aug-2026/liveblog/133528142.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-15 (d=0.01), 2026-06-19 (d=0.02)

### [RED 7.25] commodities · 3 series ↑
- wheat [COMMODITIES]: last 757.25, z20 3.93, zc 1.68, resid-z 1.66 [unexplained], 1d 3.66%, |z20|=3.93; 1y-pct=100
- corn [COMMODITIES]: last 531.50, z20 3.15, zc 2.66, resid-z 2.13 [unexplained], 1d 3.40%, |z20|=3.15; 1y-pct=100
- soybeans [COMMODITIES]: last 1262.50, z20 2.46, zc 0.64, resid-z 0.65 [quiet], 1d 0.66%, |z20|=2.46; 1y-pct=100
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Wheat Hits Three-Year High as Russia Prepares to Escalate War — Mint Markets, 2026-08-27. https://www.livemint.com/market/wheat-hits-three-year-high-as-russia-prepares-to-escalate-war-11787802575795.html
- Source: Wheat soars to daily limit on Black Sea export worries, corn at lifetime highs — Mint Markets, 2026-08-26. https://www.livemint.com/market/wheat-soars-to-daily-limit-on-black-sea-export-worries-corn-at-lifetime-highs-11787773711563.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [AMBER 6.85] cross-asset · 2 series ↑
- comex_copper [COMMODITIES]: last 6.67, z20 1.21, zc 0.52, resid-z 0.40 [quiet], 1d 1.14%, 1y-pct=98; co-occur[metal_copper] suppressed: channel WEAK
- gold_silver_ratio [DERIVED]: last 66.91, z20 -1.02, zc n/a, resid-z n/a [quiet], 1d -1.07%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho -0.495 via gold_silver_ratio, z 1.62, reacted); nifty_midcap_100 (rho -0.488 via gold_silver_ratio, z 1.03, reacted); dyn_stylebaaza_ns (rho -0.412 via gold_silver_ratio, z 0.93, quiet)
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.532 vs comex_copper, historically leads by 1d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.651 vs comex_copper
- Watch next: dax (co-move) — not yet - watch; rho 0.547 vs comex_copper
- **India receivers**: nifty_metal (rho -0.495, z 1.62); nifty_midcap_100 (rho -0.488, z 1.03); dyn_stylebaaza_ns (rho -0.412, z 0.93)
- Source: Copper’s record run is sending three clear messages about the state of financial markets today — MarketWatch Top, 2026-08-27. https://www.marketwatch.com/story/bond-jitters-ai-demand-and-tariff-threats-inside-the-new-darling-of-the-hard-asset-trade-copper-944fb585?mod=mw_rss_topstories
- Source: Stocks in news: Tata Power, Jio Financial Services, Bharat Electronics and Hindustan Copper — ET Markets, 2026-08-27. https://economictimes.indiatimes.com/markets/stocks/news/stocks-in-news-tata-power-jio-financial-services-bharat-electronics-and-hindustan-copper/articleshow/133550824.cms
- Source: Top Gainers & Losers on 26 Aug: SBFC Finance, Capri Global, Hindustan Copper, SAIL, OLA, Vedanta among top gainers — Mint Markets, 2026-08-26. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-26-aug-sbfc-finance-capri-global-hindustan-copper-sail-ola-vedanta-among-top-gainers-11787739634109.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.14), 2026-05-15 (d=0.24)

### [RED 6.25] tips_10y_real ↓
- tips_10y_real [RATES]: last 2.32, z20 -3.25, zc -1.58, resid-z -1.86 [unexplained], 1d -2.52%, 1d move -6.0bps ≥ 5bps; |z20|=3.25
- **Mechanism**: tips_10y_real ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-10 (d=0.0), 2025-05-22 (d=0.07)

### [AMBER 5.69] cross-asset · 3 series ↑
- dyn_coin [EQUITIES]: last 192.18, z20 2.37, zc 1.13, resid-z 0.82 [quiet], 1d 5.72%, |z20|=2.37
- btc_usd [CRYPTO]: last 80420.71, z20 2.13, zc 0.55, resid-z 0.60 [quiet], 1d 1.76%, |z20|=2.13
- eth_usd [CRYPTO]: last 2524.42, z20 1.90, zc 0.18, resid-z -0.03 [quiet], 1d 0.72%, |z20|=1.90
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-11 (z-distance 0.88).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.425 via btc_usd, z 1.62, reacted)
- Watch next: dxy (inverse) — not yet - watch; rho -0.561 vs eth_usd, historically leads by 1d
- **India receivers**: nifty_metal (rho 0.425, z 1.62)
- Source: S&P Global Ratings affirms India’s ‘BBB/A-2’ rating, retains stable outlook — Mint Markets, 2026-08-27. https://www.livemint.com/market/stock-market-news/sp-global-ratings-affirms-india-s-bbb-a-2-rating-retains-stable-outlook-11787835565723.html
- Source: Why these analysts say bitcoin will double by next year — and could reach $500,000 by the end of the decade — MarketWatch Top, 2026-08-27. https://www.marketwatch.com/story/why-these-analysts-say-bitcoin-will-double-by-next-year-and-could-reach-500-000-at-the-end-of-the-decade-23ec78f3?mod=mw_rss_topstories
- Source: Expert view: Expect Nifty at 29,000 by March 2027, says Seshadri Sen of Emkay Global — Mint Markets, 2026-08-27. https://www.livemint.com/market/stock-market-news/expert-view-expect-nifty-at-29-000-by-march-2027-says-seshadri-sen-of-emkay-global-11787829217981.html
- Historical analogues: 2025-08-11 (d=0.88), 2026-05-05 (d=1.32), 2024-11-21 (d=1.34)

### [RED 5.65] cross-asset · 2 series ↓
- dyn_hdb [EQUITIES]: last 22.58, z20 -2.82, zc -1.95, resid-z -0.16 [moved], 1d -2.52%, |z20|=2.82; 1y-pct=0
- nifty_50 [INDICES]: last 24090.85, z20 -1.67, zc -0.87, resid-z -0.94 [quiet], 1d -0.48%, |z20|=1.67
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.768 via nifty_50, z -1.77, reacted); nifty_midcap_100 (rho 0.757 via nifty_50, z 1.03, reacted); nifty_fmcg (rho 0.636 via nifty_50, z -1.83, reacted); dyn_indusindbk_bo (rho 0.504 via nifty_50, z -5.77, reacted); dyn_muthootfin_ns (rho 0.503 via nifty_50, z 1.02, reacted)
- Watch next: india_vix (inverse) — not yet - watch; rho -0.577 vs dyn_hdb, historically leads by 1d
- **India receivers**: dyn_jiofin_bo (rho 0.768, z -1.77); nifty_midcap_100 (rho 0.757, z 1.03); nifty_fmcg (rho 0.636, z -1.83); dyn_indusindbk_bo (rho 0.504, z -5.77)
- Source: Sebi chief Tuhin Kanta Pandey clarifies on CAS changes after big Sensex expiry-day swing — ET Markets, 2026-08-27. https://economictimes.indiatimes.com/markets/stocks/news/sebi-chief-tuhin-kanta-pandey-clarifies-on-cas-changes-after-big-sensex-expiry-day-swing/articleshow/133571371.cms
- Source: Monthly Expiry shock: Did CAS fail its biggest test after Sensex loses 2,000 points in 6 minutes? — ET Markets, 2026-08-27. https://economictimes.indiatimes.com/markets/stocks/news/monthly-expiry-shock-did-cas-fail-its-biggest-test-after-sensex-loses-2000-points-in-6-minutes/articleshow/133566940.cms
- Source: Expert view: Expect Nifty at 29,000 by March 2027, says Seshadri Sen of Emkay Global — Mint Markets, 2026-08-27. https://www.livemint.com/market/stock-market-news/expert-view-expect-nifty-at-29-000-by-march-2027-says-seshadri-sen-of-emkay-global-11787829217981.html

### [RED 5.55] natgas ↑
- natgas [COMMODITIES]: last 2.93, z20 3.55, zc 1.01, resid-z 1.17 [quiet], 1d 3.20%, |z20|=3.55
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: TotalEnergies Exits Russia’s Sanctioned Arctic LNG 2 Project — OilPrice, 2026-08-27. https://oilprice.com/Latest-Energy-News/World-News/TotalEnergies-Exits-Russias-Sanctioned-Arctic-LNG-2-Project.html
- Source: Thailand Accelerates Clean Energy Push to Cut LNG Dependence — OilPrice, 2026-08-27. https://oilprice.com/Latest-Energy-News/World-News/Thailand-Accelerates-Clean-Energy-Push-to-Cut-LNG-Dependence.html
- Source: GAIL opposes IGX platform for LNG terminal capacity booking — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/stocks/news/gail-opposes-igx-platform-for-lng-terminal-capacity-booking/articleshow/133553269.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

## Watchlist (below surfacing floor)
dyn_adanient_bo ↑ (5.24), cross-asset · 4 series ↑ (5.06), midcap_largecap_ratio ↑ (4.92), dyn_dks ↓ (4.5), dyn_icicigi_bo ↓ (4.17), dyn_chkp ↑ (4.11), dyn_tech ↑ (3.62), dyn_mrna ↑ (3.56), comex_gold ↑ (3.52), dyn_nvda ↑ (3.18), fx · 2 series ↑ (3.12), dyn_havells_ns ↓ (2.9)

## India macro
- nifty_50: 24090.8496 (1d -0.48%, z20 -1.67, flag amber)
- nifty_midcap_100: 64032.1992 (1d -0.10%, z20 1.03, flag amber)
- usd_inr: 95.5300 (1d 2.12%, z20 0.32, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6579 (1d 0.38%, z20 1.92, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 81.9 — "India’s space economy may grow 5x to $45 billion by 2030. Who is leading the boom?"
- COALINDIA.NS (COAL INDIA LTD) score 81.9 — "India’s space economy may grow 5x to $45 billion by 2030. Who is leading the boom?"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 80.1 — "India’s space economy may grow 5x to $45 billion by 2030. Who is leading the boom?"
- INDIANB.NS (INDIAN BANK) score 79.8 — "Nvidia surge lifts sentiment, but Nifty stays range-bound; HDFC Bank drags"
- BAC (Bank of America Corporation) score 70.5 — "Nvidia surge lifts sentiment, but Nifty stays range-bound; HDFC Bank drags"
- HDB (HDFC Bank Limited) score 65.2 — "Nvidia surge lifts sentiment, but Nifty stays range-bound; HDFC Bank drags"
- IDBI.NS (IDBI BANK LIMITED) score 61.0 — "Nvidia surge lifts sentiment, but Nifty stays range-bound; HDFC Bank drags"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 61.0 — "Nvidia surge lifts sentiment, but Nifty stays range-bound; HDFC Bank drags"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 60.9 — "Nvidia surge lifts sentiment, but Nifty stays range-bound; HDFC Bank drags"
- COIN (Coinbase Global, Inc.) score 55.6 — "Global Market: China stocks rise as Nvidia outlook boosts AI and hardware shares"
- BOND (PIMCO Active Bond Exchange-Tra) score 53.8 — "India bonds decline as debt supply caution overpowers oil moves"
- TECHM.NS (TECH MAHINDRA LIMITED) score 51.9 — "Hy-Tech Engineers IPO Day 4: Issue subscribed 244x so far. GMP hints 83% listing pop. Appl"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 50.1 — "Hy-Tech Engineers IPO Day 4: Issue subscribed 244x so far. GMP hints 83% listing pop. Appl"
- TECH (Bio-Techne Corp) score 50.1 — "Hy-Tech Engineers IPO Day 4: Issue subscribed 244x so far. GMP hints 83% listing pop. Appl"
- OHI (Omega Healthcare Investors, In) score 44.7 — "Kwick Forensic Solutions IPO fully subscribed on Day 1; retail investors steal the show. G"
- NVDA (NVIDIA Corporation) score 38.0 — "Global Market: China stocks rise as Nvidia outlook boosts AI and hardware shares"
- LTH (Life Time Group Holdings, Inc.) score 36.5 — "Symbiotec Pharmalab IPO Day 4: Issue booked 16.98 times so far. Here's GMP, review, & othe"
- CHKP (Check Point Software Technolog) score 31.9 — "Augmont Enterprises IPO allotment date in focus | GMP, how to check allotment status"
- 301077.SZ (CHINASTARS) score 29.0 — "China-Nepal flash flood: 362 dead and over 1,000 missing, including hundreds of foreigners"
- JIOFIN.BO (Jio Financial Services Limited) score 19.9 — "BIG DEAL | ICICI Prudential raises stake in SBI Cards and Payment Services to 7.30%"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 19.1 — "Why brokers see little retail appetite for closing auction session"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 17.2 — "Hitachi Energy India, GE Vernova, other power capex stocks rise up to 5%. Two reasons behi"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.5 — "Piramal Finance’s Rs 2,100-crore QIP sees 10x demand as BlackRock, Goldman lead institutio"
- MS (Morgan Stanley) score 14.7 — "JPMORGAN CHASE RECENTLY EVALUATED PURSUING ITS OWN STABLECOIN: WSJ"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.5 — "Tata Power share price falls 4% after $490 million arbitration challenge. Do you own?"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 13.5 — "Copper’s record run is sending three clear messages about the state of financial markets t"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.3 — "Tata Power share price falls 4% after $490 million arbitration challenge. Do you own?"
- META (Meta) score 13.2 — "Gold rate today: Precious metal rises 12% this month. Is it the right time to buy gold?"
- PCJEWELLER.NS (PC JEWELLER LTD) score 12.7 — "Deepa Jewellers IPO: ₹460-cr issue to open on September 1, price band fixed at ₹168-177"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 12.6 — "Motilal Oswal initiates coverage on Adani Enterprises with Buy, sees 25% upside. Here’s wh"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 10.0 — "45 Indian power plants face critically low coal stocks amid monsoon disruption"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 8.6 — "BIG DEAL | ICICI Prudential raises stake in SBI Cards and Payment Services to 7.30%"
- VT (Vanguard Total World Stock Ind) score 6.7 — "Bill Gates lists 3 big risks to AI shift. Is the world heading towards turbulent times?"
- JUSTDIAL.BO (JUST DIAL LTD.) score 6.4 — "I just had my first baby and don’t want to go back to work. Is quitting for a year a bad i"
- DKS (Dick's Sporting Goods Inc) score 4.0 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.2 — "From IPO mockery to Rs 1 lakh crore m-cap: Why investors are still betting on Lenskart’s v"
- MRNA (Moderna, Inc.) score 3.1 — "Can Wolfe’s upgrade push Moderna stock higher?"
- VOLTAS.NS (VOLTAS LTD) score 0.5 — "Voltas reported strong growth in June quarter, but failed to impress"
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