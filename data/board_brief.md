# Transmission Layer — board brief · 2026-10-09 11:18Z

data as of **2026-10-09** · 97 series · 2 red / 38 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.788, 5d in regime; vol-pct 0.675, breadth-off 0.9, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.39, corr60 -0.4, contra nifty_50 corr20=0.23, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.8, corr60 0.84, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.23, corr60 0.22, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.08, corr60 0.13, last shift 2026-08-26. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.76, corr60 -0.77, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [INVERTED] **dxy_inr_channel** — corr20 -0.26, corr60 -0.11, last shift 2026-08-12. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.23, corr60 -0.27, last shift 2026-08-12. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.65, corr60 0.16, last shift 2026-07-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 4.026689709668574e-06)
- **SETUP** dyn_nvda → aud_usd: leads 1d (ccf 0.339, β 0.0756, p 0.0); driver zc -1.53 → expected -0.22%. Type hit-rate 0.826 (n=2228).
- Track record · residual_reversion: hit-rate **0.496** (n=1141) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.826** (n=2228) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 5.56] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.67, z20 1.63, zc 0.68, resid-z 0.09 [quiet], 1d 0.53%, |z20|=1.63; 1y-pct=100
- ust_10y [RATES]: last 5.28, z20 1.23, zc 0.18, resid-z -0.68 [quiet], 1d 0.19%, 1y-pct=98
- tips_10y_real [RATES]: last 2.92, z20 1.16, zc 0.18, resid-z -0.79 [quiet], 1d 0.34%, 1y-pct=98
- dyn_bond [EQUITIES]: last 86.90, z20 -0.98, zc 1.06, resid-z 0.48 [quiet], 1d 0.38%, 1y-pct=2
- ust_2y [RATES]: last 4.77, z20 0.15, zc -0.31, resid-z -1.30 [quiet], 1d -0.42%, 1y-pct=96
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.713 vs ust_30y, historically leads by 3d
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.53 vs ust_10y, historically leads by 4d
- Watch next: wti (co-move) — not yet - watch; rho 0.514 vs ust_30y, historically leads by 3d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.556 vs ust_30y
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.54 vs ust_30y
- Source: US 10-year Treasury yield could hit 6% as oil prices, debt worries mount: Pimco CIO — ET Markets, 2026-10-09. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-10-year-treasury-yield-could-hit-6-as-oil-prices-debt-worries-mount-pimco-cio/articleshow/134825801.cms
- Source: US bank earnings in focus as Treasury yields surge, raising concerns over lending and dealmaking — ET Markets, 2026-10-09. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-bank-earnings-in-focus-as-treasury-yields-surge-raising-concerns-over-lending-and-dealmaking/articleshow/134806882.cms
- Source: Punjab National Bank eyes debut dollar bond issue, bankers say — BusinessLine Mkts, 2026-10-09. https://www.thehindubusinessline.com/money-and-banking/punjab-national-bank-eyes-debut-dollar-bond-issue-bankers-say/article71562500.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.37] usd_cny ↓
- usd_cny [FX]: last 6.68, z20 -5.37, zc -3.17, resid-z -4.61 [unexplained], 1d -0.34%, |z20|=5.37; 1y-pct=0
- **Mechanism**: usd_cny ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-09-25 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indianb_ns (rho -0.393 via usd_cny, z 0.25, quiet); nifty_50 (rho -0.38 via usd_cny, z -1.3, reacted); dyn_muthootfin_ns (rho -0.369 via usd_cny, z -1.77, reacted); nifty_midcap_100 (rho -0.358 via usd_cny, z -1.38, reacted); dyn_cartrade_ns (rho -0.353 via usd_cny, z 0.18, quiet)
- **India receivers**: dyn_indianb_ns (rho -0.393, z 0.25); nifty_50 (rho -0.38, z -1.3); dyn_muthootfin_ns (rho -0.369, z -1.77); nifty_midcap_100 (rho -0.358, z -1.38)
- Historical analogues: 2026-09-25 (d=0.0), 2025-08-22 (d=0.01), 2026-05-05 (d=0.01)

### [AMBER 4.47] dyn_adanient_bo ↓
- dyn_adanient_bo [EQUITIES]: last 2633.10, z20 -2.47, zc 0.43, resid-z -0.25 [quiet], 1d 1.47%, |z20|=2.47
- **Mechanism**: dyn_adanient_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.552 via dyn_adanient_bo, z -2.34, reacted); nifty_50 (rho 0.378 via dyn_adanient_bo, z -1.3, reacted); nifty_midcap_100 (rho 0.373 via dyn_adanient_bo, z -1.38, reacted)
- **India receivers**: nifty_metal (rho 0.552, z -2.34); nifty_50 (rho 0.378, z -1.3); nifty_midcap_100 (rho 0.373, z -1.38)
- Source: Adani Power shares rise despite US-based FPI GQG Partners trimming stake in Gautam Adani-led company — Mint Markets, 2026-10-09. https://www.livemint.com/market/stock-market-news/adani-power-shares-rise-despite-us-based-fpi-gqg-partners-trimming-stake-in-gautam-adani-led-company-11791542076904.html
- Source: Adani Ent Share Price Live Updates: Adani Enterprises  Trading Update — ET Markets, 2026-10-09. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/adani-ent-share-price-today-live-09-oct-2026/liveblog/134807276.cms
- Source: Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Trading Insights — ET Markets, 2026-10-09. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/adani-ports-sez-stock-price-livestock-price-today-live-updates-09-oct-2026/liveblog/134805240.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [AMBER 4.41] dyn_ohi ↓
- dyn_ohi [EQUITIES]: last 44.13, z20 -2.41, zc 0.61, resid-z -1.66 [unexplained], 1d 0.87%, |z20|=2.41
- **Mechanism**: dyn_ohi ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Global Market: Foreign investors pull $23.5 billion from Asian equities in September as US yields surge — ET Markets, 2026-10-09. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-foreign-investors-pull-23-5-billion-from-asian-equities-in-september-as-us-yields-surge/articleshow/134829780.cms
- Source: Fortis Healthcare, Apollo Hospitals, Max, Medanta shares rise: Should investors buy after 30% cancer drug price cap? — Mint Markets, 2026-10-09. https://www.livemint.com/market/stock-market-news/fortis-healthcare-apollo-hospitals-max-medanta-shares-rise-should-investors-buy-after-30-cancer-drug-price-cap-11791528628172.html
- Source: Vivriti Asset Management returns over Rs 3,400 crore to investors across two fund vintages — ET Markets, 2026-10-09. https://economictimes.indiatimes.com/markets/stocks/news/vivriti-asset-management-returns-over-rs-3400-crore-to-investors-across-two-fund-vintages/articleshow/134815238.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2025-04-02 (d=0.09)

### [AMBER 4.39] cross-asset · 3 series ↑
- sp500 [INDICES]: last 7765.70, z20 1.07, zc -0.65, resid-z -0.62 [quiet], 1d -0.46%, 1y-pct=98
- nasdaq_100 [INDICES]: last 30728.97, z20 0.77, zc -1.41, resid-z 0.41 [quiet], 1d -1.38%, 1y-pct=98
- dyn_nvda [EQUITIES]: last 230.57, z20 0.61, zc -1.53, resid-z -0.34 [priced], 1d -2.91%, 1y-pct=97
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.951 vs sp500
- Watch next: vix (inverse) — not yet - watch; rho -0.729 vs sp500, historically leads by 4d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.855 vs sp500
- Watch next: brent (inverse) — not yet - watch; rho -0.616 vs sp500, historically leads by 2d
- Source: Why one Wall Street firm sees parallels to the late 1970s and recommends shorting U.S. stocks — MarketWatch Top, 2026-10-09. https://www.marketwatch.com/story/why-one-wall-street-firm-sees-parallels-to-the-late-1970s-and-recommends-shorting-u-s-stocks-bbd0ebd2?mod=mw_rss_topstories
- Source: Global Market: Maas Group shares plunge 11% after Nvidia-backed Firmus scraps $5 billion IPO — ET Markets, 2026-10-09. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-maas-group-shares-plunge-11-after-nvidia-backed-firmus-scraps-5-billion-ipo/articleshow/134814805.cms
- Source: Global Market: Wall Street in focus as US jobless claims ease amid Fed rate uncertainty — ET Markets, 2026-10-09. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-wall-street-in-focus-as-us-jobless-claims-ease-amid-fed-rate-uncertainty/articleshow/134806455.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-04 (d=0.18), 2025-08-28 (d=0.22)

### [AMBER 4.25] gold_silver_ratio ↑
- gold_silver_ratio [DERIVED]: last 69.54, z20 1.25, zc n/a, resid-z n/a [quiet], 1d -1.19%, GSR<75 (extreme low)
- **Mechanism**: gold_silver_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.373 via gold_silver_ratio, z -1.46, reacted)
- **India receivers**: midcap_largecap_ratio (rho -0.373, z -1.46)
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

### [AMBER 4.16] usd_inr ↑
- usd_inr [FX]: last 96.73, z20 2.16, zc -0.05, resid-z -0.01 [quiet], 1d -0.03%, |z20|=2.16; 1y-pct=99
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.41 via usd_inr, z -0.57, quiet); dyn_karurvysya_ns (rho -0.359 via usd_inr, z 2.87, reacted)
- **India receivers**: dyn_idbi_ns (rho -0.41, z -0.57); dyn_karurvysya_ns (rho -0.359, z 2.87)
- Source: Rupee rises 16 paise to close at 96.72 against US dollar — BusinessLine Mkts, 2026-10-09. https://www.thehindubusinessline.com/markets/forex/rupee-rises-16-paise-to-close-at-9672-against-us-dollar/article71563647.ece
- Source: Rupee posts weekly fall despite rate hike amid adverse flows, weak sentiment — ET Markets, 2026-10-09. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-posts-weekly-fall-despite-rate-hike-amid-adverse-flows-weak-sentiment/articleshow/134831035.cms
- Source: RBI steps in to keep rupee from slipping to record low, traders say — BusinessLine Mkts, 2026-10-09. https://www.thehindubusinessline.com/markets/forex/rbi-steps-in-to-keep-rupee-from-slipping-to-record-low-traders-say/article71562522.ece
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2025-09-16 (d=0.01)

### [AMBER 4.13] indices · 2 series ↓
- nifty_50 [INDICES]: last 22520.45, z20 -1.30, zc 1.54, resid-z -2.37 [unexplained], 1d 1.30%, 1y-pct=2
- nifty_fmcg [INDICES]: last 44864.80, z20 -0.48, zc 2.25, resid-z 1.52 [unexplained], 1d 2.20%, 1y-pct=3
- **Mechanism**: indices · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-18 (z-distance 0.29).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.778 via nifty_50, z -1.38, reacted); dyn_jiofin_bo (rho 0.6 via nifty_50, z -1.25, reacted); nifty_metal (rho 0.585 via nifty_50, z -2.34, reacted); dyn_policybzr_ns (rho 0.515 via nifty_50, z -1.02, reacted); dyn_justdial_bo (rho 0.512 via nifty_50, z -1.42, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.778, z -1.38); dyn_jiofin_bo (rho 0.6, z -1.25); nifty_metal (rho 0.585, z -2.34); dyn_policybzr_ns (rho 0.515, z -1.02)
- Source: Sensex today | Stock Market Highlights: Sensex gained over 879.09 points, Nifty topped 22,520.45 as all sectoral indices turned green — BusinessLine Mkts, 2026-10-09. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-9th-october-2026/article71560336.ece
- Source: Friday heavy lifting saves Nifty from record nine weeks of losses. Can bulls take charge now? — ET Markets, 2026-10-09. https://economictimes.indiatimes.com/markets/stocks/news/friday-heavy-lifting-saves-nifty-from-record-nine-weeks-of-losses-can-bulls-take-charge-now/articleshow/134830751.cms
- Source: Nifty rebounds past 22,490 as IT, Consumption stocks lead rally — BusinessLine Mkts, 2026-10-09. https://www.thehindubusinessline.com/markets/markets-stage-sharp-rebound-it-and-consumption-stocks-lead-nifty-past-22490/article71563154.ece
- Historical analogues: 2025-07-18 (d=0.29), 2025-08-01 (d=0.88), 2025-07-11 (d=1.11)

## Watchlist (below surfacing floor)
dyn_4417_t ↑ (3.88), shanghai_comp ↓ (3.87), dyn_muthootfin_ns ↓ (3.77), eur_usd ↓ (3.54), dyn_hdb ↓ (3.47), dyn_jiofin_bo ↓ (3.25), comex_copper ↑ (3.08), dyn_policybzr_ns ↓ (3.02), dyn_karurvysya_ns ↑ (2.87), indices · 2 series ↓ (2.51), bovespa ↑ (2.39), dyn_tech ↑ (2.38)

## India macro
- nifty_50: 22520.4492 (1d 1.30%, z20 -1.30, flag amber)
- nifty_midcap_100: 58780.8984 (1d 1.56%, z20 -1.38, flag none)
- usd_inr: 96.7300 (1d -0.03%, z20 2.16, flag amber)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6101 (1d 0.25%, z20 -1.46, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · India CPI T-3d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 88.8 — "Kotak Bank Share Price Live Updates: Kotak Bank's Current Price and Performance"
- INOXINDIA.NS (INOX INDIA LIMITED) score 87.6 — "Kalyan Jewellers shares shine: 55% up in 3 months, Jefferies India sees further 46% upside"
- COALINDIA.NS (COAL INDIA LTD) score 86.6 — "Kalyan Jewellers shares shine: 55% up in 3 months, Jefferies India sees further 46% upside"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 85.0 — "Kalyan Jewellers shares shine: 55% up in 3 months, Jefferies India sees further 46% upside"
- BAC (Bank of America Corporation) score 75.5 — "Kotak Bank Share Price Live Updates: Kotak Bank's Current Price and Performance"
- HDB (HDFC Bank Limited) score 71.7 — "Kotak Bank Share Price Live Updates: Kotak Bank's Current Price and Performance"
- IDBI.NS (IDBI BANK LIMITED) score 69.0 — "Kotak Bank Share Price Live Updates: Kotak Bank's Current Price and Performance"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 69.0 — "Kotak Bank Share Price Live Updates: Kotak Bank's Current Price and Performance"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 69.0 — "Kotak Bank Share Price Live Updates: Kotak Bank's Current Price and Performance"
- COIN (Coinbase Global, Inc.) score 64.7 — "Global Market: Japan’s Nikkei falls as AI concerns, global bond market stress weigh"
- OHI (Omega Healthcare Investors, In) score 49.3 — "Steel Authority: SAIL shares rebound after falling for two sessions amid market rally | Ta"
- TECHM.NS (TECH MAHINDRA LIMITED) score 47.9 — "Nifty IT becomes rocket! 3% up; Check TCS, Infosys, Wipro, Mphasis, HCL, Oracle, Tech Mahi"
- BOND (PIMCO Active Bond Exchange-Tra) score 44.0 — "Global Market: Japan’s Nikkei falls as AI concerns, global bond market stress weigh"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 42.1 — "Nifty IT becomes rocket! 3% up; Check TCS, Infosys, Wipro, Mphasis, HCL, Oracle, Tech Mahi"
- TECH (Bio-Techne Corp) score 42.1 — "Nifty IT becomes rocket! 3% up; Check TCS, Infosys, Wipro, Mphasis, HCL, Oracle, Tech Mahi"
- TGT (Target Corporation) score 40.1 — "Kalyan Jewellers shares shine: 55% up in 3 months, Jefferies India sees further 46% upside"
- CHKP (Check Point Software Technolog) score 34.5 — "Nifty IT becomes rocket! 3% up; Check TCS, Infosys, Wipro, Mphasis, HCL, Oracle, Tech Mahi"
- LTH (Life Time Group Holdings, Inc.) score 30.1 — "Anand Rathi Wealth Q2 results 2026, dividend amount announcement today: Date, time, quarte"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 28.4 — "TCS Q2, US Green Card program, H1B visa: Big triggers for IT stocks today - TCS, Infosys, "
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 25.5 — "Inox Green Energy Services share price jumps 15% after this acquisition update — buy, sell"
- SEPN (Septerna, Inc.) score 25.2 — "D-St Exit Rush! Sectors that saw sharpest FII selloff in 2nd half of September"
- 301077.SZ (CHINASTARS) score 20.3 — "Copper Set for Weekly Gain on China’s Return and Supply Concerns"
- JIOFIN.BO (Jio Financial Services Limited) score 16.9 — "Inox Green Energy Services share price jumps 15% after this acquisition update — buy, sell"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 16.5 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Trading Insights"
- JUSTDIAL.BO (JUST DIAL LTD.) score 14.2 — "Madhusudan Kela-backed MV Electrosystems shares more than double from IPO price in just 2 "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.7 — "Tata Technologies stock jumps 30% in 6 months, up 6% today: Should you buy now? Check targ"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.7 — "Tata Technologies stock jumps 30% in 6 months, up 6% today: Should you buy now? Check targ"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.7 — "₹5 dividend vs  ₹34 last year: Why Vedanta's dividend payout story has fundamentally chang"
- JEF (Jefferies Financial Group Inc.) score 12.4 — "Kalyan Jewellers shares shine: 55% up in 3 months, Jefferies India sees further 46% upside"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 11.1 — "LAGARDE TOLD EURO FINANCE CHIEF: NO SENSE OF BROADENING PRICES *LAGARDE TO EURO FINANCE CH"
- NVDA (NVIDIA Corporation) score 8.8 — "Global Market: Maas Group shares plunge 11% after Nvidia-backed Firmus scraps $5 billion I"
- META (Meta) score 8.2 — "US President Donald Trump buys $1 million-plus stakes in Meta, Microsoft, McDonald’s; adds"
- VT (Vanguard Total World Stock Ind) score 8.1 — "World’s Top Crude Trader Isn’t Ruling Out $200 Oil Just Yet"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 8.1 — "LAGARDE TOLD EURO FINANCE CHIEF: NO SENSE OF BROADENING PRICES *LAGARDE TO EURO FINANCE CH"
- RS (Reliance, Inc.) score 7.2 — "Europe’s diesel shortage could lift Reliance’s O2C earnings 38% to ₹20,700 crore in Q2"
- GS (Goldman Sachs Group, Inc. (The) score 5.3 — "TCS shares jump 4% after Q2 results. What are Goldman Sachs, Nomura, others saying?"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 4.9 — "UK Retailers Push to Cut Green Levies as Power Bills Top £440 Million"
- POLICYBZR.NS (PB FINTECH LIMITED) score 4.5 — "Nomura becomes latest brokerage to cut PB Fintech share price target by 31%, lists 2 scena"
- DELL (Dell Technologies Inc.) score 0.8 — "Piero Cipollone: Interview with Corriere della Sera"
- VOLTAS.NS (VOLTAS LTD) score 0.1 — "Voltas’s market share is growing. Will margins follow?"

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