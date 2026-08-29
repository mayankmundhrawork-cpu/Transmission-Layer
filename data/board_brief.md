# Transmission Layer — board brief · 2026-08-29 03:14Z

data as of **2026-08-29** · 98 series · 8 red / 37 amber · 8 events surfaced (32 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.214, 1d in regime; vol-pct 0.135, breadth-off 0.294, Markov P(high-vol) 0.014)
- [WEAK] **safe_haven_gold** — corr20 -0.18, corr60 -0.39, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.82, corr60 0.86, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.21, corr60 0.33, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.19, corr60 0.03, last shift 2026-07-15. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.34, corr60 -0.83, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.23, corr60 -0.15, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.11, corr60 -0.08, last shift 2026-06-26. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.28, corr60 0.2, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 90** scanned series survive multiplicity control (effective p ≤ 0.0005204583648548144)
- **SETUP** dxy → aud_usd: leads 1d (ccf -0.57, β -0.8502, p 0.0); driver zc 1.56 → expected -0.443%. Type hit-rate 0.822 (n=2047).
- Track record · residual_reversion: hit-rate **0.496** (n=1117) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.822** (n=2047) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.24] commodities · 3 series ↑
- wheat [COMMODITIES]: last 783.50, z20 3.92, zc 2.55, resid-z 2.62 [unexplained], 1d 5.49%, |z20|=3.92; 1y-pct=100
- corn [COMMODITIES]: last 536.25, z20 2.93, zc 3.99, resid-z 2.89 [unexplained], 1d 5.10%, |z20|=2.93; 1y-pct=100
- soybeans [COMMODITIES]: last 1287.75, z20 2.82, zc 2.44, resid-z 2.17 [unexplained], 1d 2.49%, |z20|=2.82; 1y-pct=100
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: UBS SEES COMMODITY OPPORTUNITIES BEYOND OIL UBS sees opportunities across copper, agriculture and gold, arguing commodities offer both returns and inflation protection. Copper should benefit from AI infrastructure and electrification. Wheat and corn are gaining as a — DeItaone, 2026-08-27. https://t.me/walter_bloomberg/35133
- Source: Wheat Hits Three-Year High as Russia Prepares to Escalate War — Mint Markets, 2026-08-27. https://www.livemint.com/market/wheat-hits-three-year-high-as-russia-prepares-to-escalate-war-11787802575795.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [AMBER 5.9] cross-asset · 2 series ↑
- brent [COMMODITIES]: last 88.29, z20 0.07, zc -0.67, resid-z -0.49 [quiet], 1d -1.57%, 1-session move -1.57% ≥ 1.5%
- dow_jones [INDICES]: last 53546.79, z20 -0.06, zc -0.06, resid-z 0.03 [quiet], 1d -0.04%, 1y-pct=95
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: wti (co-move) — not yet - watch; rho 0.979 vs brent, historically leads by 5d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.749 vs dow_jones, historically leads by 5d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.676 vs dow_jones, historically leads by 1d
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.618 vs brent, historically leads by 5d
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.586 vs dow_jones, historically leads by 5d
- Source: US-Venezuela oil deal: Trump announces agreement over 65 billion barrels of reserves — BusinessLine Mkts, 2026-08-29. https://www.thehindubusinessline.com/news/world/us-venezuela-oil-deal-trump-announces-agreement-over-65-billion-barrels-of-reserves/article71403319.ece
- Source: TRUMP: US ENTERS AGREEMENT WITH VENEZUELA ON BIGGEST OIL DEAL IN WORLD HISTORY US SECURES MAJORITY CONTROL OF MORE THAN 65 BILLION BARRELS OF VENEZUELA OIL RESERVES DEAL SAID TO INCREASE OIL SUPPLY AND LOWER GASOLINE PRICES — DeItaone, 2026-08-28. https://t.me/walter_bloomberg/35187
- Source: IRAN SOLD ABOUT 90 MILLION BARRELS OF OIL DURING THE IMPLEMENTATION OF INTERIM DEAL- PEZESHKIAN — DeItaone, 2026-08-28. https://t.me/walter_bloomberg/35186
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-17 (d=0.39), 2024-11-08 (d=0.53)

### [RED 5.47] dyn_icicigi_bo ↓
- dyn_icicigi_bo [EQUITIES]: last 1563.00, z20 -3.47, zc -1.28, resid-z -0.97 [quiet], 1d -1.91%, |z20|=3.47; 1y-pct=0
- **Mechanism**: dyn_icicigi_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Lenskart Rs 1,857-crore block deal: Goldman Sachs, Morgan Stanley, ICICI Prudential, SBI MF among buyers as Alpha Wave exits — ET Markets, 2026-08-28. https://economictimes.indiatimes.com/markets/stocks/news/lenskart-rs-1857-crore-block-deal-goldman-sachs-morgan-stanley-icici-prudential-sbi-mf-among-buyers-as-alpha-wave-exits/articleshow/133594276.cms
- Source: Market wrap: TCS, Tech Mahindra, ICICI Bank, ITC top gainers and losers on Nifty and Sensex on Friday — ET Markets, 2026-08-28. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-tcs-tech-mahindra-icici-bank-itc-top-gainers-and-losers-on-nifty-and-sensex-on-friday/articleshow/133589753.cms
- Source: ICICI Bank shares slide 1.32% amid $1 billion bond issuance and employee stock allotment — BusinessLine Mkts, 2026-08-28. https://www.thehindubusinessline.com/markets/icici-bank-shares-slide-132-amid-1-billion-bond-issuance-and-employee-stock-allotment/article71399396.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.0), 2025-05-30 (d=0.03)

### [RED 5.16] dyn_chkp ↑
- dyn_chkp [EQUITIES]: last 138.38, z20 3.16, zc 1.40, resid-z 1.32 [quiet], 1d 3.87%, |z20|=3.16
- **Mechanism**: dyn_chkp ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_karurvysya_ns (rho -0.386 via dyn_chkp, z 1.25, reacted)
- **India receivers**: dyn_karurvysya_ns (rho -0.386, z 1.25)
- Source: Gold prices down 1% following Fed's Kevin Warsh hints at rate hike, trading at  ₹1,56,780/10 gm — Check details — Mint Markets, 2026-08-28. https://www.livemint.com/market/commodities/gold-prices-down-1-pc-us-fed-chair-kevin-warsh-hints-interest-rate-hike-trade-rs-156780-10-gm-spot-rate-inflation-labour-11787931055296.html
- Source: The bull market for stocks is defying everything, but Bank of America warns that an autumn reality check is coming — MarketWatch Top, 2026-08-28. https://www.marketwatch.com/story/the-bull-market-for-stocks-is-defying-everything-but-bank-of-america-warns-that-an-autumn-reality-check-is-coming-8cdf831f?mod=mw_rss_topstories
- Source: Over 45% returns in one month, now double delight of bonus share and dividend | Check record date, ratio — Mint Markets, 2026-08-28. https://www.livemint.com/market/stock-market-news/over-45-returns-in-one-month-now-double-delight-of-bonus-share-and-dividend-check-record-date-ratio-11787906215782.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2024-10-18 (d=0.02)

### [AMBER 4.87] cross-asset · 3 series ↑
- vix [INDICES]: last 14.42, z20 -1.55, zc -0.08, resid-z n/a [quiet], 1d -0.62%, |z20|=1.55; 1y-pct=3
- dyn_vt [EQUITIES]: last 161.00, z20 0.34, zc -0.50, resid-z -1.23 [quiet], 1d -0.35%, 1y-pct=97
- sp500 [INDICES]: last 7709.90, z20 0.12, zc -0.38, resid-z 0.79 [quiet], 1d -0.27%, 1y-pct=95
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-27 (z-distance 0.14).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.667 vs vix, historically leads by 1d
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.554 vs dyn_vt, historically leads by 5d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.637 vs vix
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.564 vs dyn_vt
- Watch next: dyn_nvda (inverse) — not yet - watch; rho -0.55 vs vix
- Source: TRUMP: US ENTERS AGREEMENT WITH VENEZUELA ON BIGGEST OIL DEAL IN WORLD HISTORY US SECURES MAJORITY CONTROL OF MORE THAN 65 BILLION BARRELS OF VENEZUELA OIL RESERVES DEAL SAID TO INCREASE OIL SUPPLY AND LOWER GASOLINE PRICES — DeItaone, 2026-08-28. https://t.me/walter_bloomberg/35187
- Source: Nvidia’s revenue forecast is so huge that Wall Street wonders if SpaceX is the reason — MarketWatch Top, 2026-08-28. https://www.marketwatch.com/story/nvidias-revenue-forecast-is-so-huge-that-wall-street-wonders-if-spacex-is-the-reason-1ee7a8a9?mod=mw_rss_topstories
- Source: Wall Street Piles On Rate-Hike Bets as Warsh Renews Hawkish Tone — Mint Markets, 2026-08-28. https://www.livemint.com/market/wall-street-piles-on-rate-hike-bets-as-warsh-renews-hawkish-tone-11787949474200.html
- Historical analogues: 2025-08-27 (d=0.14), 2025-10-23 (d=0.17), 2025-10-31 (d=0.17)

### [RED 4.77] dyn_adanient_bo ↑
- dyn_adanient_bo [EQUITIES]: last 3166.00, z20 2.77, zc 0.17, resid-z -0.18 [quiet], 1d 0.35%, |z20|=2.77; 1y-pct=97
- **Mechanism**: dyn_adanient_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.501 via dyn_adanient_bo, z -1.08, reacted); nifty_midcap_100 (rho 0.487 via dyn_adanient_bo, z 1.15, reacted); dyn_indusindbk_bo (rho 0.391 via dyn_adanient_bo, z -1.54, reacted); nifty_fmcg (rho 0.358 via dyn_adanient_bo, z -1.87, reacted)
- **India receivers**: nifty_50 (rho 0.501, z -1.08); nifty_midcap_100 (rho 0.487, z 1.15); dyn_indusindbk_bo (rho 0.391, z -1.54); nifty_fmcg (rho 0.358, z -1.87)
- Source: Market wrap: Adani Enterprises, Kotak Mahindra Bank, HDFC Bank, M&M top gainers and losers on Nifty and Sensex on Thursday — ET Markets, 2026-08-27. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-adani-enterprises-kotak-mahindra-bank-hdfc-bank-mm-top-gainers-and-losers-on-nifty-and-sensex-on-thursday/articleshow/133566380.cms
- Source: Motilal Oswal initiates coverage on Adani Enterprises with Buy, sees 25% upside. Here’s why — ET Markets, 2026-08-27. https://economictimes.indiatimes.com/markets/stocks/news/motilal-oswal-initiates-coverage-on-adani-enterprises-with-buy-sees-25-upside-heres-why/articleshow/133558689.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [AMBER 4.4] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.65, z20 1.40, zc n/a, resid-z n/a [quiet], 1d -0.29%, 52-wk extreme (pct=99); 1y-pct=99
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho -0.453 via midcap_largecap_ratio, z -1.08, reacted); dyn_inoxindia_ns (rho 0.387 via midcap_largecap_ratio, z 3.16, reacted); nifty_fmcg (rho -0.385 via midcap_largecap_ratio, z -1.87, reacted); dyn_techm_ns (rho -0.369 via midcap_largecap_ratio, z 0.86, quiet); nifty_it (rho -0.362 via midcap_largecap_ratio, z 0.53, quiet)
- **India receivers**: nifty_50 (rho -0.453, z -1.08); dyn_inoxindia_ns (rho 0.387, z 3.16); nifty_fmcg (rho -0.385, z -1.87); dyn_techm_ns (rho -0.369, z 0.86)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

### [AMBER 4.2] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1616.30, z20 2.20, zc 2.53, resid-z 2.35 [unexplained], 1d 8.09%, |z20|=2.20; 1y-pct=100
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Hero MotoCorp buys Rs 1,758 crore Ather Energy stake in block deal — ET Markets, 2026-08-28. https://economictimes.indiatimes.com/markets/stocks/news/hero-motocorp-buys-rs-1758-crore-ather-energy-stake-in-block-deal/articleshow/133594919.cms
- Source: Ather Energy share price jumps 10% | here's why — Mint Markets, 2026-08-28. https://www.livemint.com/market/stock-market-news/ather-energy-share-price-jumps-10-heres-why-11787894092380.html
- Source: Ather Energy shares rally 4% as Hero MotoCorp plans Rs 1,758 crore investment — ET Markets, 2026-08-28. https://economictimes.indiatimes.com/markets/stocks/news/ather-energy-shares-rally-4-as-hero-motocorp-plans-rs-1758-crore-investment/articleshow/133583523.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

## Watchlist (below surfacing floor)
natgas ↑ (4.0), gold_silver_ratio ↓ (3.67), usd_jpy ↑ (3.64), dyn_havells_ns ↓ (3.64), dyn_inoxindia_ns ↑ (3.16), dyn_stylebaaza_ns ↑ (3.01), indices · 2 series ↑ (2.96), dyn_hdb ↓ (2.95), indices · 2 series ↑ (2.86), comex_copper ↑ (2.81), dyn_lenskart_ns ↑ (2.78), dyn_tech ↑ (2.7)

## India macro
- nifty_50: 24175.6504 (1d 0.35%, z20 -1.08, flag none)
- nifty_midcap_100: 64070.1016 (1d 0.06%, z20 1.15, flag amber)
- usd_inr: 95.3600 (1d -0.07%, z20 -0.01, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6502 (1d -0.29%, z20 1.40, flag amber)
- Next India prints: NSDL FPI flows T-2d · IMD weekly rainfall T-2d · RBI Weekly Statistical Supplement T-6d · Kharif sowing data T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 81.3 — "Indian bank stocks see sharp NSE-BSE closing price gaps under new auction system"
- INOXINDIA.NS (INOX INDIA LIMITED) score 80.6 — "Indian bank stocks see sharp NSE-BSE closing price gaps under new auction system"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 79.2 — "Indian bank stocks see sharp NSE-BSE closing price gaps under new auction system"
- INDIANB.NS (INDIAN BANK) score 77.9 — "Indian bank stocks see sharp NSE-BSE closing price gaps under new auction system"
- BAC (Bank of America Corporation) score 68.3 — "US DEFENDS YEN SUPPORT TO PROTECT BORROWING COSTS Treasury Secretary Scott Bessent defende"
- HDB (HDFC Bank Limited) score 60.8 — "Indian bank stocks see sharp NSE-BSE closing price gaps under new auction system"
- IDBI.NS (IDBI BANK LIMITED) score 57.8 — "Indian bank stocks see sharp NSE-BSE closing price gaps under new auction system"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 57.8 — "Indian bank stocks see sharp NSE-BSE closing price gaps under new auction system"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 57.8 — "Indian bank stocks see sharp NSE-BSE closing price gaps under new auction system"
- OHI (Omega Healthcare Investors, In) score 48.5 — "Tempsens Instruments doubles IPO investors’ money as stock lists at 111% premium. Should y"
- TECHM.NS (TECH MAHINDRA LIMITED) score 48.3 — "IT stocks surge: Why Nifty IT is up today - Reason behind TCS, Infosys, Wipro, Tech Mahind"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 47.0 — "IT stocks surge: Why Nifty IT is up today - Reason behind TCS, Infosys, Wipro, Tech Mahind"
- TECH (Bio-Techne Corp) score 47.0 — "IT stocks surge: Why Nifty IT is up today - Reason behind TCS, Infosys, Wipro, Tech Mahind"
- COIN (Coinbase Global, Inc.) score 46.3 — "Global Market: China stocks steady as property shares offset Biotech, chip losses"
- BOND (PIMCO Active Bond Exchange-Tra) score 45.1 — "Kevin Warsh gets what every Fed chair hopes for: a bond market that trusts his word"
- NVDA (NVIDIA Corporation) score 35.1 — "Explained | How Nvidia's solid earnings sparked a rally in Taiwan Index and AI stocks"
- CHKP (Check Point Software Technolog) score 32.1 — "Gold prices down 1% following Fed's Kevin Warsh hints at rate hike, trading at  ₹1,56,780/"
- LTH (Life Time Group Holdings, Inc.) score 31.8 — "YEN WEAKENS TO 160 PER DOLLAR FOR FIRST TIME SINCE JULY 31"
- 301077.SZ (CHINASTARS) score 24.8 — "Global Market: China stocks steady as property shares offset Biotech, chip losses"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.7 — "HEGSETH EYES SECOND MASS MILITARY SUMMIT Defense Secretary Pete Hegseth is considering cal"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 19.6 — "Retail investors bet big on these 12 smallcap stocks that rallied up to 150%; 3 turned mul"
- JIOFIN.BO (Jio Financial Services Limited) score 18.5 — "US TREASURY IMPOSES LIMITS ON EGYPTIAN BANK FOR DOING BUSINESS WITH IRAN- FT US TREASURY D"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 14.6 — "Noel Tata, Shapoorji discuss share swap for Tata Sons stake sale"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 14.5 — "Noel Tata, Shapoorji discuss share swap for Tata Sons stake sale"
- MS (Morgan Stanley) score 13.8 — "Lenskart Rs 1,857-crore block deal: Goldman Sachs, Morgan Stanley, ICICI Prudential, SBI M"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 13.4 — "Welspun Corp, Piramal Finance, Divis Labs among 12 BSE 500 stocks that jumped to their rec"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 12.4 — "US TREASURY IMPOSES LIMITS ON EGYPTIAN BANK FOR DOING BUSINESS WITH IRAN- FT US TREASURY D"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 11.3 — "Sebi approves 7 IPOs including Jio Platforms, Paras Healthcare and Bharat PET"
- META (Meta) score 10.2 — "Hindustan Copper: Strong metal cycle aids earnings growth, but valuation is not cheap"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 9.6 — "ICICI Bank shares slide 1.32% amid $1 billion bond issuance and employee stock allotment"
- PCJEWELLER.NS (PC JEWELLER LTD) score 9.0 — "Deepa Jewellers IPO: ₹460-cr issue to open on September 1, price band fixed at ₹168-177"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.9 — "Motilal Oswal initiates coverage on Adani Enterprises with Buy, sees 25% upside. Here’s wh"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.2 — "Upper circuit as losing streak ends - Just Dial share price surges 10% | Can it rise furth"
- VT (Vanguard Total World Stock Ind) score 6.7 — "TRUMP: US ENTERS AGREEMENT WITH VENEZUELA ON BIGGEST OIL DEAL IN WORLD HISTORY US SECURES "
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 6.4 — "Lenskart Rs 1,857-crore block deal: Goldman Sachs, Morgan Stanley, ICICI Prudential, SBI M"
- DKS (Dick's Sporting Goods Inc) score 2.9 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- MRNA (Moderna, Inc.) score 2.2 — "Can Wolfe’s upgrade push Moderna stock higher?"
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