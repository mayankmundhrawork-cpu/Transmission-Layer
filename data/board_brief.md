# Transmission Layer — board brief · 2026-08-21 14:51Z

data as of **2026-08-21** · 98 series · 13 red / 28 amber · 8 events surfaced (24 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.256, 2d in regime; vol-pct 0.217, breadth-off 0.294, Markov P(high-vol) 0.015)
- [INVERTED] **safe_haven_gold** — corr20 -0.41, corr60 -0.4, contra nifty_50 corr20=0.04, last shift 2026-06-08. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.83, corr60 0.86, last shift 2026-01-29. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.23, corr60 0.37, last shift 2026-07-03. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.15, corr60 -0.13, last shift 2026-06-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.7, corr60 -0.83, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.02, corr60 -0.13, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.21, last shift 2026-06-25. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.26, corr60 0.19, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.00034359420749185965)
- **SETUP** bovespa → usd_brl: leads 1d (ccf -0.574, β -0.4391, p 0.0); driver zc 1.75 → expected -0.806%. Type hit-rate 0.819 (n=2302).
- **SETUP** tips_10y_real → usd_jpy: leads 1d (ccf 0.409, β 0.1225, p 0.0); driver zc -1.66 → expected -0.305%. Type hit-rate 0.819 (n=2302).
- **SETUP** bovespa → usd_mxn: leads 1d (ccf -0.368, β -0.2179, p 0.0); driver zc 1.75 → expected -0.4%. Type hit-rate 0.819 (n=2302).
- **SETUP** btc_usd → asx_200: leads 1d (ccf 0.309, β 0.0866, p 0.0); driver zc 1.6 → expected 0.517%. Type hit-rate 0.819 (n=2302).
- Track record · residual_reversion: hit-rate **0.491** (n=1106) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.819** (n=2302) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.12] cross-asset · 4 series ↑
- btc_usd [CRYPTO]: last 77388.07, z20 5.45, zc 1.60, resid-z 2.73 [unexplained], 1d 5.96%, |z20|=5.45
- dyn_mrna [EQUITIES]: last 151.55, z20 4.75, zc 1.02, resid-z 11.29 [unexplained], 1d 13.68%, |z20|=4.75; 1y-pct=100
- dyn_coin [EQUITIES]: last 189.83, z20 4.40, zc 1.94, resid-z 2.13 [unexplained], 1d 10.14%, |z20|=4.40
- eth_usd [CRYPTO]: last 2391.16, z20 3.77, zc 0.55, resid-z 0.74 [quiet], 1d 2.78%, |z20|=3.77
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 1.17).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.384 via btc_usd, z 0.91, quiet)
- Watch next: vix (inverse) — not yet - watch; rho -0.584 vs eth_usd
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.512 vs eth_usd
- **India receivers**: nifty_metal (rho 0.384, z 0.91)
- Source: Carlsberg India posts strong volume growth in H1, IPO process underway: Global CEO — BusinessLine Mkts, 2026-08-21. https://www.thehindubusinessline.com/companies/carlsberg-india-posts-strong-volume-growth-in-h1-ipo-process-underway-global-ceo/article71372631.ece
- Source: Bitcoin on track for best week in more than two years. Can this mean the next crypto bull market has arrived? — MarketWatch Top, 2026-08-21. https://www.marketwatch.com/story/bitcoin-on-track-for-best-week-in-more-than-two-years-has-the-next-crypto-bull-market-arrived-0181180c?mod=mw_rss_topstories
- Source: Global Market: European shares little changed as bond yields rise and gulf tensions lift oil — ET Markets, 2026-08-21. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-european-shares-little-changed-as-bond-yields-rise-and-gulf-tensions-lift-oil/articleshow/133399383.cms
- Historical analogues: 2025-08-13 (d=1.17), 2025-05-09 (d=2.11), 2024-11-21 (d=2.35)

### [RED 7.4] cross-asset · 3 series ↑
- comex_gold [COMMODITIES]: last 4641.20, z20 2.35, zc 1.77, resid-z 0.72 [priced], 1d 2.77%, |z20|=2.35; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 69.10, z20 2.04, zc 0.60, resid-z -1.64 [unexplained], 1d 1.57%, |z20|=2.04; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 67.17, z20 -1.09, zc n/a, resid-z n/a [quiet], 1d 1.18%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.531 via comex_silver, z 0.91, quiet); dyn_stylebaaza_ns (rho -0.401 via gold_silver_ratio, z 1.7, reacted)
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.664 vs comex_gold, historically leads by 1d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.568 vs comex_silver, historically leads by 4d
- Watch next: dax (co-move) — not yet - watch; rho 0.541 vs comex_gold, historically leads by 4d
- Watch next: nifty_metal (co-move) — not yet - watch; rho 0.531 vs comex_silver, historically leads by 4d
- **India receivers**: nifty_metal (rho 0.531, z 0.91); dyn_stylebaaza_ns (rho -0.401, z 1.7)
- Source: Tata Mutual Fund lifts curbs on investment in gold ETFs — BusinessLine Mkts, 2026-08-21. https://www.thehindubusinessline.com/markets/tata-mf-lifts-curbs-on-investment-in-gold-etfs/article71372919.ece
- Source: Gold prices rally further on weak dollar — BusinessLine Mkts, 2026-08-21. https://www.thehindubusinessline.com/markets/gold/gold-prices-rally-further-on-weak-dollar/article71373772.ece
- Source: Shanti Gold among 7 consumer discretionary stocks that hit 52-week highs and surged up to 37% in a month — ET Markets, 2026-08-21. https://economictimes.indiatimes.com/markets/stocks/news/shanti-gold-among-7-consumer-discretionary-stocks-that-hit-52-week-highs-and-surged-up-to-37-in-a-month/slideshow/133404296.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.69] tips_10y_real ↓
- tips_10y_real [RATES]: last 2.35, z20 -3.69, zc -1.66, resid-z -1.10 [moved], 1d -2.49%, 1d move -6.0bps ≥ 5bps; |z20|=3.69
- **Mechanism**: tips_10y_real ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.87 vs tips_10y_real, historically leads by 1d
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.866 vs tips_10y_real, historically leads by 1d
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.759 vs tips_10y_real, historically leads by 1d
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.725 vs tips_10y_real
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.522 vs tips_10y_real
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-10 (d=0.0), 2025-05-22 (d=0.07)

### [AMBER 6.13] wti ↑
- wti [COMMODITIES]: last 86.43, z20 1.13, zc -0.67, resid-z -0.30 [quiet], 1d -1.59%, 1-session move -1.59% ≥ 1.5%
- **Mechanism**: wti ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.352 via wti, z 0.66, quiet); dyn_voltas_ns (rho -0.351 via wti, z -1.73, reacted)
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.627 vs wti
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.504 vs wti
- **India receivers**: nifty_midcap_100 (rho -0.352, z 0.66); dyn_voltas_ns (rho -0.351, z -1.73)
- Source: Saudi Oil Exports from Mediterranean Soar with Shuttles North to Avoid Houthis — OilPrice, 2026-08-21. https://oilprice.com/Latest-Energy-News/World-News/Saudi-Oil-Exports-from-Mediterranean-Soar-with-Shuttles-North-to-Avoid-Houthis.html
- Source: Oil Bulls Take Control as Iran Deal Collapses and Hormuz Stays Restricted — OilPrice, 2026-08-21. https://oilprice.com/Energy/Energy-General/Oil-Bulls-Take-Control-as-Iran-Deal-Collapses-and-Hormuz-Stays-Restricted.html
- Source: Nifty posts second straight gain but ends week lower; crude, bond yields cap rally — BusinessLine Mkts, 2026-08-21. https://www.thehindubusinessline.com/markets/nifty-posts-second-straight-gain-but-ends-week-lower-crude-bond-yields-cap-rally/article71373428.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-22 (d=0.01), 2025-04-29 (d=0.01)

### [RED 5.61] dyn_cartrade_ns ↑
- dyn_cartrade_ns [EQUITIES]: last 3072.90, z20 3.61, zc 1.79, resid-z 1.83 [unexplained], 1d 6.14%, |z20|=3.61
- **Mechanism**: dyn_cartrade_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Top Gainers & Losers on 21 Aug: Welspun Corp, Jindal Saw, Urban Company, Vedanta, CarTrade Tech among top gainers — Mint Markets, 2026-08-21. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-21-aug-welspun-corp-jindal-saw-urban-company-vedanta-cartrade-tech-among-top-gainers-11787305625058.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-13 (d=0.0), 2025-07-18 (d=0.01)

### [RED 5.34] commodities · 2 series ↑
- corn [COMMODITIES]: last 507.00, z20 4.51, zc 4.60, resid-z 3.58 [unexplained], 1d 5.90%, |z20|=4.51; 1y-pct=100
- wheat [COMMODITIES]: last 699.00, z20 2.64, zc 1.37, resid-z 1.11 [quiet], 1d 2.38%, |z20|=2.64; 1y-pct=99
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-11 (d=0.33), 2026-04-01 (d=0.35)

### [RED 4.46] fx · 4 series ↑
- aud_usd [FX]: last 0.72, z20 2.80, zc 0.97, resid-z 1.23 [quiet], 1d 0.59%, |z20|=2.80
- eur_usd [FX]: last 1.17, z20 2.14, zc 0.13, resid-z 0.23 [quiet], 1d 0.05%, |z20|=2.14
- gbp_usd [FX]: last 1.36, z20 2.01, zc 0.52, resid-z 0.55 [quiet], 1d 0.22%, |z20|=2.01
- usd_mxn [FX]: last 16.91, z20 -1.81, zc -0.58, resid-z -0.46 [quiet], 1d -0.23%, |z20|=1.81; 1y-pct=0
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.586 via usd_mxn, z 1.26, reacted); nifty_midcap_100 (rho 0.427 via aud_usd, z 0.66, quiet); dyn_icicigi_bo (rho -0.409 via gbp_usd, z -1.23, reacted)
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.645 vs aud_usd, historically leads by 4d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.557 vs eur_usd
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.522 vs aud_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.586, z 1.26); nifty_midcap_100 (rho 0.427, z 0.66); dyn_icicigi_bo (rho -0.409, z -1.23)
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [AMBER 4.28] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.63, z20 1.28, zc n/a, resid-z n/a [quiet], 1d 0.02%, 52-wk extreme (pct=98); 1y-pct=98
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.492 via midcap_largecap_ratio, z 0.66, quiet); dyn_fincables_ns (rho 0.355 via midcap_largecap_ratio, z 1.05, reacted); dyn_bharatcoal_ns (rho 0.351 via midcap_largecap_ratio, z 1.7, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.492, z 0.66); dyn_fincables_ns (rho 0.355, z 1.05); dyn_bharatcoal_ns (rho 0.351, z 1.7)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

## Watchlist (below surfacing floor)
soybeans ↑ (3.89), dyn_stylebaaza_ns ↑ (3.7), usd_cny ↓ (3.59), dyn_icicigi_bo ↓ (3.23), dyn_tech ↑ (2.98), dyn_bond ↓ (2.74), dyn_lenskart_ns ↑ (2.66), dyn_lth ↑ (2.66), dyn_vt ↑ (2.59), dyn_pcjeweller_ns ↑ (2.49), eur_inr ↑ (2.36), dyn_tatatech_ns ↑ (2.32)

## India macro
- nifty_50: 24252.0000 (1d 0.08%, z20 -0.37, flag none)
- nifty_midcap_100: 63735.6016 (1d 0.11%, z20 0.66, flag amber)
- usd_inr: 95.6850 (1d 0.20%, z20 0.24, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6281 (1d 0.02%, z20 1.28, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 109.0 — "India bonds log worst week in FY27 on RBI surprise U-turns"
- INOXINDIA.NS (INOX INDIA LIMITED) score 105.5 — "India bonds log worst week in FY27 on RBI surprise U-turns"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 105.0 — "India bonds log worst week in FY27 on RBI surprise U-turns"
- INDIANB.NS (INDIAN BANK) score 98.2 — "TRUMP’S IRAN CRACKDOWN RISKS CHINA BACKLASH Washington is preparing tougher measures to is"
- BOND (PIMCO Active Bond Exchange-Tra) score 86.6 — "India bonds log worst week in FY27 on RBI surprise U-turns"
- BAC (Bank of America Corporation) score 81.8 — "TRUMP’S IRAN CRACKDOWN RISKS CHINA BACKLASH Washington is preparing tougher measures to is"
- HDB (HDFC Bank Limited) score 74.3 — "TRUMP’S IRAN CRACKDOWN RISKS CHINA BACKLASH Washington is preparing tougher measures to is"
- IDBI.NS (IDBI BANK LIMITED) score 70.0 — "TRUMP’S IRAN CRACKDOWN RISKS CHINA BACKLASH Washington is preparing tougher measures to is"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 70.0 — "TRUMP’S IRAN CRACKDOWN RISKS CHINA BACKLASH Washington is preparing tougher measures to is"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 69.9 — "TRUMP’S IRAN CRACKDOWN RISKS CHINA BACKLASH Washington is preparing tougher measures to is"
- COIN (Coinbase Global, Inc.) score 59.5 — "Carlsberg India posts strong volume growth in H1, IPO process underway: Global CEO"
- TECHM.NS (TECH MAHINDRA LIMITED) score 54.1 — "UBS SEES S&P 500 BULL RUN EXTENDING UBS raised its S&P 500 targets to 8,100 for December 2"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 51.1 — "UBS SEES S&P 500 BULL RUN EXTENDING UBS raised its S&P 500 targets to 8,100 for December 2"
- TECH (Bio-Techne Corp) score 50.9 — "UBS SEES S&P 500 BULL RUN EXTENDING UBS raised its S&P 500 targets to 8,100 for December 2"
- OHI (Omega Healthcare Investors, In) score 50.5 — "WARSH COULD OFFER MARKETS SOME RELIEF AT JACKSON HOLE Fed Chair Kevin Warsh could provide "
- LTH (Life Time Group Holdings, Inc.) score 39.8 — "FRIDAY, AUGUST 21, 2026 — PRESIDENTIAL SCHEDULE 🔸 8:00 AM — Executive Time 📍 White House 🔸"
- CHKP (Check Point Software Technolog) score 39.5 — "American consumers are delivering a retail reality check as they laser in on bargains"
- 301077.SZ (CHINASTARS) score 27.6 — "TSLA - TESLA RECALLS NEARLY 3 MILLION VEHICLES IN CHINA Tesla is recalling up to 2.98 mill"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.2 — "Saatvik Green Energy shares post biggest 1-day gain in over a month on  ₹190 crore order w"
- PCJEWELLER.NS (PC JEWELLER LTD) score 20.9 — "Lalithaa Jewellery IPO listing share price prediction: What latest GMP hints at"
- JIOFIN.BO (Jio Financial Services Limited) score 19.1 — "FIIs pour Rs 6,535 crore into Indian financial stocks. What else are they buying this mont"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 15.8 — "Tata Mutual Fund lifts curbs on investment in gold ETFs"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 15.4 — "Muthoot, Manappuram Finance shares jump up to 7% in 2 days as gold crosses Rs 1.6 lakh/10 "
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 15.1 — "Bharat Coking Coal shares jump over 7%. What's behind the sharp surge?"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 15.0 — "Tata Mutual Fund lifts curbs on investment in gold ETFs"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 15.0 — "FIIs pour Rs 6,535 crore into Indian financial stocks. What else are they buying this mont"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 14.8 — "Sebi proposes bond distributor network, tighter ad rules to deepen retail participation"
- MS (Morgan Stanley) score 12.1 — "PRICE TARGET RAISED • $ABT: PT raised to $135 from $115 by TD Cowen • $ADSK: PT raised to "
- JEF (Jefferies Financial Group Inc.) score 11.2 — "Why Jefferies’ Chris Wood sees gold as the second-best hedge amid Iran war and fiscal risk"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.8 — "Tata Steel, Adani Ports among top 10 stocks downgraded by Motilal Oswal after Q1 results"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 10.0 — "ICICI Bank doubles borrowing from overseas markets to $5 billion"
- MRNA (Moderna, Inc.) score 9.4 — "Moderna’s personalized mRNA shot could reshape the fight against skin cancer — but it may "
- VT (Vanguard Total World Stock Ind) score 9.3 — "PRESIDENT PEZESHKIAN SAYS IRAN SHOULD END WAR NOW THAT IT IS IN A POSITION OF STRENGTH AND"
- META (Meta) score 8.1 — "Silver futures jump nearly 1% to ₹2.38 lakh/kg as US Treasury move boosts precious metals"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.8 — "Did Goodluck India shares really crash 66% in just one day? Here's how the bonus math work"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 7.2 — "Bharat Coking Coal shares jump over 7%. What's behind the sharp surge?"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 2.9 — "Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month"
- VOLTAS.NS (VOLTAS LTD) score 2.1 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.4 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.3 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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