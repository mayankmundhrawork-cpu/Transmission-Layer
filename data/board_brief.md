# Transmission Layer — board brief · 2026-08-21 16:50Z

data as of **2026-08-21** · 98 series · 14 red / 27 amber · 8 events surfaced (20 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.226, 2d in regime; vol-pct 0.217, breadth-off 0.235, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.41, corr60 -0.4, contra nifty_50 corr20=0.05, last shift 2026-06-08. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.83, corr60 0.86, last shift 2026-01-29. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.24, corr60 0.37, last shift 2026-07-03. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.15, corr60 -0.13, last shift 2026-06-04. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.7, corr60 -0.83, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.03, corr60 -0.13, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.21, last shift 2026-06-25. Channel: real yields up -> non-yielding gold down
- [INVERTED] **gsr_stress_gauge** — corr20 -0.26, corr60 0.19, last shift 2026-04-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.00024255046857080131)
- **SETUP** tips_10y_real → usd_jpy: leads 1d (ccf 0.409, β 0.1225, p 0.0); driver zc -1.66 → expected -0.305%. Type hit-rate 0.821 (n=2333).
- **SETUP** btc_usd → asx_200: leads 1d (ccf 0.309, β 0.0866, p 0.0); driver zc 1.64 → expected 0.527%. Type hit-rate 0.821 (n=2333).
- Track record · residual_reversion: hit-rate **0.491** (n=1106) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.821** (n=2333) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.667** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.15] cross-asset · 4 series ↑
- btc_usd [CRYPTO]: last 77474.41, z20 5.49, zc 1.64, resid-z 2.58 [unexplained], 1d 6.08%, |z20|=5.49
- dyn_mrna [EQUITIES]: last 150.91, z20 4.72, zc 0.98, resid-z 11.29 [unexplained], 1d 13.20%, |z20|=4.72; 1y-pct=100
- dyn_coin [EQUITIES]: last 187.59, z20 4.12, zc 1.69, resid-z 2.13 [unexplained], 1d 8.84%, |z20|=4.12
- eth_usd [CRYPTO]: last 2407.74, z20 3.91, zc 0.70, resid-z 0.74 [quiet], 1d 3.50%, |z20|=3.91
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 1.19).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: vix (inverse) — not yet - watch; rho -0.585 vs eth_usd
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.514 vs eth_usd
- Source: Carlsberg India posts strong volume growth in H1, IPO process underway: Global CEO — BusinessLine Mkts, 2026-08-21. https://www.thehindubusinessline.com/companies/carlsberg-india-posts-strong-volume-growth-in-h1-ipo-process-underway-global-ceo/article71372631.ece
- Source: U.S. S&P GLOBAL AUGUST FLASH COMPOSITE PMI AT 56.0 (VS 54.5 IN JULY) U.S. S&P GLOBAL AUGUST FLASH SERVICES PMI AT 56.8 (FORECAST 54.0) U.S. S&P GLOBAL AUGUST FLASH MANUFACTURING PMI AT 53.2 (FORECAST 53.9) — DeItaone, 2026-08-21. https://t.me/walter_bloomberg/34902
- Source: BITCOIN ETF INFLOWS TOP $1 BILLION IN TWO DAYS Bitcoin ETFs attracted more than $1 billion in net inflows over the past two days, including $606 million on Thursday. Four-day inflows have now reached $1.61 billion, signaling renewed investor appetite for crypto. The rebound — DeItaone, 2026-08-21. https://t.me/walter_bloomberg/34901
- Historical analogues: 2025-08-13 (d=1.19), 2025-05-09 (d=2.12), 2024-11-21 (d=2.39)

### [RED 8.39] cross-asset · 6 series ↑
- comex_gold [COMMODITIES]: last 4676.60, z20 2.56, zc 2.27, resid-z 0.72 [priced], 1d 3.55%, |z20|=2.56; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 69.82, z20 2.25, zc 1.00, resid-z -1.78 [unexplained], 1d 2.63%, |z20|=2.25; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 66.99, z20 -1.24, zc n/a, resid-z n/a [quiet], 1d 0.90%, GSR<75 (extreme low)
- comex_copper [COMMODITIES]: last 6.58, z20 0.55, zc 0.84, resid-z 0.94 [quiet], 1d 1.86%, 1y-pct=95
- dax [INDICES]: last 26128.43, z20 0.36, zc 0.74, resid-z 0.36 [quiet], 1d 0.56%, 1y-pct=96
- stoxx_50 [INDICES]: last 6459.04, z20 0.19, zc 0.73, resid-z 0.29 [quiet], 1d 0.58%, 1y-pct=95
- **Mechanism**: cross-asset · 6 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-30 (z-distance 0.59).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.535 via comex_silver, z 0.91, quiet); nifty_midcap_100 (rho 0.476 via dax, z 0.66, quiet); dyn_stylebaaza_ns (rho -0.396 via gold_silver_ratio, z 1.7, reacted)
- Watch next: cac_40 (co-move) — not yet - watch; rho 0.813 vs dax, historically leads by 3d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.614 vs comex_copper, historically leads by 1d
- Watch next: ftse_100 (co-move) — not yet - watch; rho 0.596 vs dax, historically leads by 4d
- Watch next: vix (inverse) — not yet - watch; rho -0.583 vs comex_copper, historically leads by 3d
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.577 vs comex_copper, historically leads by 1d
- **India receivers**: nifty_metal (rho 0.535, z 0.91); nifty_midcap_100 (rho 0.476, z 0.66); dyn_stylebaaza_ns (rho -0.396, z 1.7)
- Source: Gold could top Goldman’s $4,900 forecast as options demand fuels rally — ET Markets, 2026-08-21. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/gold-could-top-goldmans-4900-forecast-as-options-demand-fuels-rally/articleshow/133408548.cms
- Source: Gold rallies to 3-month high on weaker dollar, bullish technicals — ET Markets, 2026-08-21. https://economictimes.indiatimes.com/markets/commodities/gold-rallies-to-3-month-high-on-weaker-dollar-bullish-technicals/articleshow/133407758.cms
- Source: Tata Mutual Fund lifts curbs on investment in gold ETFs — BusinessLine Mkts, 2026-08-21. https://www.thehindubusinessline.com/markets/tata-mf-lifts-curbs-on-investment-in-gold-etfs/article71372919.ece
- Historical analogues: 2025-07-30 (d=0.59), 2026-04-02 (d=0.67), 2024-11-07 (d=0.8)

### [RED 7.87] commodities · 3 series ↑
- corn [COMMODITIES]: last 507.50, z20 4.55, zc 4.68, resid-z 3.67 [unexplained], 1d 6.01%, |z20|=4.55; 1y-pct=100
- wheat [COMMODITIES]: last 697.50, z20 2.55, zc 1.24, resid-z 0.94 [quiet], 1d 2.16%, |z20|=2.55; 1y-pct=99
- soybeans [COMMODITIES]: last 1238.00, z20 2.02, zc 1.38, resid-z 1.33 [quiet], 1d 1.41%, |z20|=2.02; 1y-pct=99
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_atherenerg_ns (rho -0.377 via soybeans, z 0.55, quiet)
- **India receivers**: dyn_atherenerg_ns (rho -0.377, z 0.55)
- Source: Soybean oil imports likely to see a sharp jump during festive season: SEA President — BusinessLine Mkts, 2026-08-21. https://www.thehindubusinessline.com/economy/agri-business/soybean-oil-imports-likely-to-see-a-sharp-jump-during-festive-season-sea-president/article71372629.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [RED 6.69] tips_10y_real ↓
- tips_10y_real [RATES]: last 2.35, z20 -3.69, zc -1.66, resid-z -1.10 [moved], 1d -2.49%, 1d move -6.0bps ≥ 5bps; |z20|=3.69
- **Mechanism**: tips_10y_real ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.87 vs tips_10y_real, historically leads by 1d
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.866 vs tips_10y_real, historically leads by 1d
- Watch next: ust_2y (co-move) — not yet - watch; rho 0.759 vs tips_10y_real, historically leads by 1d
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.725 vs tips_10y_real
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.521 vs tips_10y_real
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-10 (d=0.0), 2025-05-22 (d=0.07)

### [RED 5.61] dyn_cartrade_ns ↑
- dyn_cartrade_ns [EQUITIES]: last 3072.90, z20 3.61, zc 1.79, resid-z 1.88 [unexplained], 1d 6.14%, |z20|=3.61
- **Mechanism**: dyn_cartrade_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Top Gainers & Losers on 21 Aug: Welspun Corp, Jindal Saw, Urban Company, Vedanta, CarTrade Tech among top gainers — Mint Markets, 2026-08-21. https://www.livemint.com/market/stock-market-news/top-gainers-losers-on-21-aug-welspun-corp-jindal-saw-urban-company-vedanta-cartrade-tech-among-top-gainers-11787305625058.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-13 (d=0.0), 2025-07-18 (d=0.01)

### [RED 4.71] dxy ↓
- dxy [FX]: last 98.79, z20 -1.71, zc -0.30, resid-z -2.52 [unexplained], 1d -0.11%, 20d range extreme; |z20|=1.71
- **Mechanism**: dxy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [RED 4.62] fx · 4 series ↑
- aud_usd [FX]: last 0.72, z20 2.95, zc 1.13, resid-z 1.44 [quiet], 1d 0.70%, |z20|=2.95
- eur_usd [FX]: last 1.17, z20 2.21, zc 0.25, resid-z 0.29 [quiet], 1d 0.10%, |z20|=2.21
- gbp_usd [FX]: last 1.36, z20 2.13, zc 0.70, resid-z 0.71 [quiet], 1d 0.30%, |z20|=2.13
- usd_mxn [FX]: last 16.89, z20 -1.94, zc -0.92, resid-z -0.77 [quiet], 1d -0.37%, |z20|=1.94; 1y-pct=0
- **Mechanism**: fx · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.589 via usd_mxn, z 1.26, reacted); nifty_midcap_100 (rho 0.425 via aud_usd, z 0.66, quiet); dyn_icicigi_bo (rho -0.409 via gbp_usd, z -1.23, reacted)
- Watch next: usd_brl (inverse) — not yet - watch; rho -0.653 vs aud_usd, historically leads by 4d
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.554 vs eur_usd
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.519 vs aud_usd
- **India receivers**: dyn_muthootfin_ns (rho -0.589, z 1.26); nifty_midcap_100 (rho 0.425, z 0.66); dyn_icicigi_bo (rho -0.409, z -1.23)
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-15 (d=0.23), 2025-03-31 (d=0.52)

### [AMBER 4.28] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.63, z20 1.28, zc n/a, resid-z n/a [quiet], 1d 0.02%, 52-wk extreme (pct=98); 1y-pct=98
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.492 via midcap_largecap_ratio, z 0.66, quiet); dyn_fincables_ns (rho 0.355 via midcap_largecap_ratio, z 1.05, reacted); dyn_bharatcoal_ns (rho 0.351 via midcap_largecap_ratio, z 1.7, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.492, z 0.66); dyn_fincables_ns (rho 0.355, z 1.05); dyn_bharatcoal_ns (rho 0.351, z 1.7)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

## Watchlist (below surfacing floor)
dyn_stylebaaza_ns ↑ (3.7), usd_cny ↓ (3.62), dyn_icicigi_bo ↓ (3.23), dyn_tech ↑ (3.05), dyn_bond ↓ (2.83), dyn_lenskart_ns ↑ (2.66), dyn_vt ↑ (2.66), dyn_lth ↑ (2.58), dyn_pcjeweller_ns ↑ (2.49), eur_inr ↑ (2.33), dyn_tatatech_ns ↑ (2.32), nifty_fmcg ↓ (2.08)

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
- COALINDIA.NS (COAL INDIA LTD) score 110.0 — "Online Instruments India gets Sebi approval to float IPO"
- INOXINDIA.NS (INOX INDIA LIMITED) score 106.5 — "Online Instruments India gets Sebi approval to float IPO"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 106.0 — "Online Instruments India gets Sebi approval to float IPO"
- INDIANB.NS (INDIAN BANK) score 98.3 — "JPMORGAN WARNS OF AUTUMN SELLOFF AS AI ECHOES 2000 JPMorgan sees growing risks of a late-s"
- BOND (PIMCO Active Bond Exchange-Tra) score 88.0 — "US stocks surge as bond market volatility eases, crypto stocks rally"
- BAC (Bank of America Corporation) score 82.2 — "JPMORGAN WARNS OF AUTUMN SELLOFF AS AI ECHOES 2000 JPMorgan sees growing risks of a late-s"
- HDB (HDFC Bank Limited) score 73.9 — "JPMORGAN WARNS OF AUTUMN SELLOFF AS AI ECHOES 2000 JPMorgan sees growing risks of a late-s"
- IDBI.NS (IDBI BANK LIMITED) score 69.7 — "JPMORGAN WARNS OF AUTUMN SELLOFF AS AI ECHOES 2000 JPMorgan sees growing risks of a late-s"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 69.7 — "JPMORGAN WARNS OF AUTUMN SELLOFF AS AI ECHOES 2000 JPMorgan sees growing risks of a late-s"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 69.6 — "JPMORGAN WARNS OF AUTUMN SELLOFF AS AI ECHOES 2000 JPMorgan sees growing risks of a late-s"
- COIN (Coinbase Global, Inc.) score 59.4 — "U.S. S&P GLOBAL AUGUST FLASH COMPOSITE PMI AT 56.0 (VS 54.5 IN JULY) U.S. S&P GLOBAL AUGUS"
- TECHM.NS (TECH MAHINDRA LIMITED) score 55.1 — "PRIVATE EQUITY FIRM APOLLO CONFIRMS DATA BREACH AMID HACKING WAVE TARGETING FINANCIAL GIAN"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 52.1 — "PRIVATE EQUITY FIRM APOLLO CONFIRMS DATA BREACH AMID HACKING WAVE TARGETING FINANCIAL GIAN"
- TECH (Bio-Techne Corp) score 52.0 — "PRIVATE EQUITY FIRM APOLLO CONFIRMS DATA BREACH AMID HACKING WAVE TARGETING FINANCIAL GIAN"
- OHI (Omega Healthcare Investors, In) score 51.5 — "Symbiotec Pharmalab gets Rs 526 crore anchor backing ahead of IPO; Citi Group, Singularity"
- LTH (Life Time Group Holdings, Inc.) score 39.0 — "FRIDAY, AUGUST 21, 2026 — PRESIDENTIAL SCHEDULE 🔸 8:00 AM — Executive Time 📍 White House 🔸"
- CHKP (Check Point Software Technolog) score 38.8 — "American consumers are delivering a retail reality check as they laser in on bargains"
- 301077.SZ (CHINASTARS) score 29.1 — "China and US push Southeast Asia over their AI blocs. Will it test region’s non-alignment?"
- JIOFIN.BO (Jio Financial Services Limited) score 21.8 — "PRIVATE EQUITY FIRM APOLLO CONFIRMS DATA BREACH AMID HACKING WAVE TARGETING FINANCIAL GIAN"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.8 — "Saatvik Green Energy shares post biggest 1-day gain in over a month on  ₹190 crore order w"
- PCJEWELLER.NS (PC JEWELLER LTD) score 20.5 — "Lalithaa Jewellery IPO listing share price prediction: What latest GMP hints at"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 16.6 — "Retail F&O gets younger as trading outpaces equity wealth"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 15.7 — "PRIVATE EQUITY FIRM APOLLO CONFIRMS DATA BREACH AMID HACKING WAVE TARGETING FINANCIAL GIAN"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 15.5 — "Tata Mutual Fund lifts curbs on investment in gold ETFs"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 15.1 — "Muthoot, Manappuram Finance shares jump up to 7% in 2 days as gold crosses Rs 1.6 lakh/10 "
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 14.9 — "Bharat Coking Coal shares jump over 7%. What's behind the sharp surge?"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 14.8 — "Tata Mutual Fund lifts curbs on investment in gold ETFs"
- MS (Morgan Stanley) score 13.9 — "JPMORGAN WARNS OF AUTUMN SELLOFF AS AI ECHOES 2000 JPMorgan sees growing risks of a late-s"
- JEF (Jefferies Financial Group Inc.) score 11.0 — "Why Jefferies’ Chris Wood sees gold as the second-best hedge amid Iran war and fiscal risk"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.6 — "Tata Steel, Adani Ports among top 10 stocks downgraded by Motilal Oswal after Q1 results"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 9.8 — "ICICI Bank doubles borrowing from overseas markets to $5 billion"
- MRNA (Moderna, Inc.) score 9.2 — "Moderna’s personalized mRNA shot could reshape the fight against skin cancer — but it may "
- VT (Vanguard Total World Stock Ind) score 9.2 — "PRESIDENT PEZESHKIAN SAYS IRAN SHOULD END WAR NOW THAT IT IS IN A POSITION OF STRENGTH AND"
- META (Meta) score 8.0 — "Silver futures jump nearly 1% to ₹2.38 lakh/kg as US Treasury move boosts precious metals"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.7 — "Did Goodluck India shares really crash 66% in just one day? Here's how the bonus math work"
- BHARATFORG.BO (BHARAT FORGE LTD.) score 7.1 — "Bharat Coking Coal shares jump over 7%. What's behind the sharp surge?"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 2.9 — "Lenskart Solutions among 4 stocks to hit 52-week highs & surge up to 25% in a month"
- VOLTAS.NS (VOLTAS LTD) score 2.0 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.3 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
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