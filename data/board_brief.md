# Transmission Layer — board brief · 2026-10-28 00:37Z

data as of **2026-10-28** · 97 series · 10 red / 39 amber · 8 events surfaced (33 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.667, 18d in regime; vol-pct None, breadth-off 0.667, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.39, corr60 -0.39, contra nifty_50 corr20=0.43, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.83, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.1, corr60 0.15, last shift 2026-09-03. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.19, corr60 0.03, last shift 2026-09-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.77, last shift 2026-09-09. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.2, corr60 -0.0, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.1, corr60 -0.15, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.53, corr60 0.25, last shift 2026-07-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 7.384981515201616e-12)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.503** (n=1121) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.828** (n=1724) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.529** (n=17) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.19] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1674.00, z20 5.19, zc 1.93, resid-z 1.40 [moved], 1d 6.29%, |z20|=5.19; 1y-pct=98
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.423 via dyn_atherenerg_ns, z -1.42, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.423, z -1.42)
- Source: Ather Energy shares: 125% YTD returns! Experts give 'portfolio stock' tag after Q2 results 2026 | Target, stop-loss — Mint Markets, 2026-10-27. https://www.livemint.com/market/stock-market-news/ather-energy-shares-125-ytd-returns-experts-give-portfolio-stock-tag-after-q2-results-2026-target-stoploss-11793080902497.html
- Source: Ather achieves profitability milestone, supply ramp-up to pave the road ahead — Mint Markets, 2026-10-27. https://www.livemint.com/market/mark-to-market/ather-energy-q2-results-net-profit-revenue-growth-11793081766549.html
- Source: Ather Energy shares jump 5%, extend rally to 20% in two days after Q2 results. Can the run continue? — ET Markets, 2026-10-27. https://economictimes.indiatimes.com/markets/stocks/news/ather-energy-shares-jump-5-extend-rally-to-20-in-two-days-after-q2-results-can-the-run-continue/articleshow/135225009.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [RED 6.22] cross-asset · 4 series ↓
- dyn_bajfinance_ns [EQUITIES]: last 912.00, z20 -2.55, zc -0.42, resid-z 0.00 [quiet], 1d -0.73%, |z20|=2.55
- dyn_jiofin_bo [EQUITIES]: last 207.25, z20 -1.55, zc 0.58, resid-z 0.95 [quiet], 1d 0.90%, 1y-pct=1
- india_vix [INDICES]: last 16.36, z20 1.54, zc -0.79, resid-z n/a [quiet], 1d -4.66%, |z20|=1.54
- dyn_policybzr_ns [EQUITIES]: last 1008.40, z20 -0.71, zc -0.61, resid-z -0.35 [quiet], 1d -1.43%, 1y-pct=2
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-11 (z-distance 0.48).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.776 via dyn_jiofin_bo, z -1.42, reacted); nifty_50 (rho -0.73 via india_vix, z 0.23, quiet); nifty_metal (rho -0.58 via india_vix, z -0.97, quiet); nifty_fmcg (rho 0.579 via dyn_jiofin_bo, z -1.51, reacted); dyn_indusindbk_bo (rho -0.553 via india_vix, z -1.99, reacted)
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.591 vs dyn_bajfinance_ns, historically leads by 4d
- Watch next: dyn_indianb_ns (co-move) — not yet - watch; rho 0.537 vs dyn_jiofin_bo, historically leads by 1d
- Watch next: nifty_metal (co-move) — not yet - watch; rho 0.575 vs dyn_jiofin_bo
- **India receivers**: nifty_midcap_100 (rho 0.776, z -1.42); nifty_50 (rho -0.73, z 0.23); nifty_metal (rho -0.58, z -0.97); nifty_fmcg (rho 0.579, z -1.51)
- Source: MDR uncertainty, choppy markets cloud ₹33,600-crore fintech IPO pipeline — BusinessLine Mkts, 2026-10-27. https://www.thehindubusinessline.com/money-and-banking/mdr-uncertainty-choppy-markets-cloud-33600-crore-fintech-ipo-pipeline/article71632456.ece
- Source: Q2 Results Today Highlgihts: Bajaj Auto Q2 PAT up 35%, Maruti Suzuki & Cipla profit down, ACC, Mazagon Dock PAT tumbles, Honeywell Automation PAT up, L&T, Vedanta Iron, Waaree Energies, SAIL, SBI Life, Tata Capital, Star Health, ABDL to announce Q2 results — BusinessLine Mkts, 2026-10-27. https://www.thehindubusinessline.com/markets/q2-results-today-highlights-lampt-maruti-suzuki-bajaj-auto-tata-steel-vedanta-iron-waaree-acc-sail-sbi-star-health-mazagon-dock-cipla-united-breweries-ather-paytm-tata-consumer-results-27-october-20/article71626455.ece
- Source: Q2 Results Today Live: Bajaj Auto Q2 PAT up 35%, Maruti Suzuki & Cipla profit down, ACC, Mazagon Dock PAT tumbles, Honeywell Automation PAT up, L&T, Vedanta Iron, Waaree Energies, SAIL, SBI Life, Tata Capital, Star Health, ABDL to announce Q2 results — BusinessLine Mkts, 2026-10-27. https://www.thehindubusinessline.com/markets/q2-results-today-live-updates-lampt-maruti-suzuki-bajaj-auto-tata-steel-vedanta-iron-waaree-acc-sail-sbi-star-health-mazagon-dock-cipla-united-breweries-ather-paytm-tata-consumer-results-27-october-20/article71626455.ece
- Historical analogues: 2025-07-11 (d=0.48), 2025-07-21 (d=0.62), 2025-07-04 (d=0.99)

### [AMBER 5.98] cross-asset · 5 series ↓
- tips_10y_real [RATES]: last 2.66, z20 -2.05, zc 0.00, resid-z -0.36 [quiet], 1d 0.00%, |z20|=2.05
- ust_30y [RATES]: last 5.31, z20 -2.00, zc -0.43, resid-z -0.44 [quiet], 1d -0.38%, |z20|=2.00
- ust_10y [RATES]: last 5.00, z20 -1.99, zc 0.00, resid-z -0.15 [quiet], 1d 0.00%, |z20|=1.99
- ust_2y [RATES]: last 4.68, z20 -1.86, zc -0.16, resid-z -0.52 [quiet], 1d -0.21%, |z20|=1.86
- dyn_schd [EQUITIES]: last 35.12, z20 1.50, zc -0.56, resid-z 0.09 [quiet], 1d -0.50%, 1y-pct=98
- **Mechanism**: cross-asset · 5 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cartrade_ns (rho 0.386 via ust_10y, z -1.02, reacted)
- Watch next: kospi (inverse) — not yet - watch; rho -0.576 vs dyn_schd
- Watch next: nikkei_225 (inverse) — not yet - watch; rho -0.557 vs dyn_schd
- **India receivers**: dyn_cartrade_ns (rho 0.386, z -1.02)
- Source: Mazagon Dock Shipbuilders shares crash 10% after Q2 net profit tumbles 54%; firm declares Rs 5/share dividend — ET Markets, 2026-10-27. https://economictimes.indiatimes.com/markets/stocks/news/mazagon-dock-shipbuilders-shares-crash-10-after-q2-net-profit-tumbles-54-firm-declares-rs-5/share-dividend/articleshow/135232098.cms
- Source: Top dividend stocks to buy: PTC India, CESC, Vedanta, Coal India, HPCL offer up to 24% yield. Check full list here — Mint Markets, 2026-10-27. https://www.livemint.com/market/stock-market-news/top-dividend-stocks-to-buy-ptc-india-cesc-vedanta-coal-india-hpcl-offer-up-to-24-yield-check-full-list-here-11793085342244.html
- Source: Dividend stocks are having an excellent October as tech sector struggles — MarketWatch Top, 2026-10-26. https://www.marketwatch.com/story/dividend-stocks-are-having-an-excellent-october-as-tech-sector-struggles-5ae40b02?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-12 (d=0.63), 2025-05-19 (d=1.06)

### [RED 5.66] dyn_lth ↑
- dyn_lth [EQUITIES]: last 44.10, z20 3.66, zc 0.19, resid-z 2.40 [unexplained], 1d 0.55%, |z20|=3.66
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Gold price in India to touch  ₹2 lakh per 10 gm by end of 2027? Is it the right time to buy before Dhanteras, Diwali? — Mint Markets, 2026-10-27. https://www.livemint.com/market/commodities/gold-price-in-india-to-touch-rs-2-lakh-per-10-gm-by-end-of-2027-is-it-the-right-time-to-buy-before-dhanteras-diwali-11793082888965.html
- Source: ITC Hotels share price jumps 6% after Q2 results - Is it the right time to buy the stock? Experts decode — Mint Markets, 2026-10-27. https://www.livemint.com/market/stock-market-news/itc-hotels-share-price-jumps-6-after-q2-results-is-it-the-right-time-to-buy-the-stock-experts-decode-11793073302905.html
- Source: Jio Platforms IPO listing date and time, share price prediction, expected gains, latest GMP; all eyes on NSE, BSE debut — Mint Markets, 2026-10-27. https://www.livemint.com/market/ipo/jio-platforms-ipo-listing-date-and-time-share-price-prediction-expected-gains-latest-gmp-all-eyes-on-nse-bse-debut-11793071293037.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-17 (d=0.02), 2025-12-31 (d=0.02)

### [RED 5.47] dyn_sepn ↑
- dyn_sepn [EQUITIES]: last 44.09, z20 3.47, zc 1.66, resid-z 0.24 [moved], 1d 6.55%, |z20|=3.47; 1y-pct=98
- **Mechanism**: dyn_sepn ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: US OCT CONSUMER CONFIDENCE INDEX 91.7 (CONSENSUS 81.0) VS SEPT REVISED 84.2 (PREVIOUS 81.9) - CONFERENCE BOARD — DeItaone, 2026-10-27. https://t.me/walter_bloomberg/37609
- Source: India’s crude steel output rises 5.6% in Jan-Sept even as global production dips — BusinessLine Mkts, 2026-10-26. https://www.thehindubusinessline.com/markets/commodities/indias-crude-steel-output-rises-56-in-jan-sept-even-as-global-production-dips/article71620869.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-13 (d=0.0), 2025-05-01 (d=0.01)

### [RED 4.76] dyn_tgt ↓
- dyn_tgt [EQUITIES]: last 148.00, z20 -2.76, zc -0.19, resid-z -1.60 [unexplained], 1d -0.36%, |z20|=2.76
- **Mechanism**: dyn_tgt ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_adanient_bo (rho -0.356 via dyn_tgt, z -1.66, reacted)
- **India receivers**: dyn_adanient_bo (rho -0.356, z -1.66)
- Source: Sunteck Realty, Radico Khaitan, WeWork India, Supreme Industries, Kajaria: Jefferies sees up to 64% upside; target price — Mint Markets, 2026-10-28. https://www.livemint.com/market/stock-market-news/sunteck-realty-radico-khaitan-wework-india-supreme-industries-kajaria-jefferies-sees-up-to-64-upside-target-price-11793118823438.html
- Source: Boeing cuts delivery target, shares hit 18-month low as recovery takes longer — ET Markets, 2026-10-27. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/boeing-cuts-delivery-target-shares-hit-18-month-low-as-recovery-takes-longer/articleshow/135243808.cms
- Source: Newly listed stock has 27% upside potential! JM Financial issues buy call; Check target price and key triggers — Mint Markets, 2026-10-27. https://www.livemint.com/market/stock-market-news/newly-listed-stock-has-27-upside-potential-jm-financial-issues-buy-call-check-target-price-and-key-triggers-11793097853945.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.01), 2025-09-30 (d=0.01)

### [RED 4.7] dyn_meta ↓
- dyn_meta [EQUITIES]: last 620.12, z20 -2.70, zc -0.62, resid-z -1.06 [quiet], 1d -1.66%, |z20|=2.70
- **Mechanism**: dyn_meta ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: META AI DIRECTOR ROHIT PATEL LEAVES TO TAKE ON MICROSOFT OFFICE AND GOOGLE WORKSPACE - TECHCRUNCH — DeItaone, 2026-10-27. https://t.me/walter_bloomberg/37613
- Source: AMD $META - AMD AND META ADVANCE STRATEGIC PARTNERSHIP TO POWER META’S SUPERINTELLIGENCE INFRASTRUCTURE ADVANCED MICRO DEVICES - TO INVEST $1 BLN IN META'S EQUITY OFFERING — DeItaone, 2026-10-27. https://t.me/walter_bloomberg/37604
- Source: Nvidia, AMD and Broadcom could buy Meta shares as part of $35 billion stock offering — MarketWatch Top, 2026-10-26. https://www.marketwatch.com/story/nvidia-amd-and-broadcom-could-buy-meta-shares-as-part-of-35-billion-stock-offering-d816fec2?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2025-10-09 (d=0.12)

### [AMBER 4.67] commodities · 2 series ↓
- wheat [COMMODITIES]: last 612.75, z20 -1.84, zc 0.00, resid-z -0.26 [quiet], 1d 0.00%, |z20|=1.84
- corn [COMMODITIES]: last 450.75, z20 -1.63, zc 0.00, resid-z -0.64 [quiet], 1d 0.00%, |z20|=1.63
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Corn drops on US harvest pressure, wheat near 3-1/2-month low — BusinessLine Mkts, 2026-10-27. https://www.thehindubusinessline.com/markets/commodities/corn-drops-on-us-harvest-pressure-wheat-near-3-12-month-low/article71629668.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-04-01 (d=0.35), 2025-08-28 (d=0.36)

## Watchlist (below surfacing floor)
dyn_rs ↑ (4.61), gold_silver_ratio ↑ (4.48), dyn_chkp ↑ (4.41), dyn_hdb ↓ (4.41), eur_usd ↓ (4.26), dyn_tatatech_ns ↓ (4.09), dyn_gs ↑ (4.04), dyn_coalindia_ns ↓ (4.01), dyn_4417_t ↑ (3.83), dyn_swiggy_ns ↓ (3.79), dyn_301077_sz ↓ (3.77), shanghai_comp ↓ (3.64)

## India macro
- nifty_50: 22749.7500 (1d -0.02%, z20 0.23, flag none)
- nifty_midcap_100: 57030.3008 (1d 1.00%, z20 -1.42, flag none)
- usd_inr: 95.1870 (1d 0.26%, z20 -0.58, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5069 (1d 1.01%, z20 -1.57, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d · IMD weekly rainfall T-5d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 85.6 — "India's growth momentum stays resilient despite global headwinds: RBI Deputy Governor Poon"
- INOXINDIA.NS (INOX INDIA LIMITED) score 83.7 — "India's growth momentum stays resilient despite global headwinds: RBI Deputy Governor Poon"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 83.0 — "India's growth momentum stays resilient despite global headwinds: RBI Deputy Governor Poon"
- INDIANB.NS (INDIAN BANK) score 64.3 — "Credit card additions hit second-highest monthly level in 2026 as banks gear up for festiv"
- BAC (Bank of America Corporation) score 61.3 — "Credit card additions hit second-highest monthly level in 2026 as banks gear up for festiv"
- HDB (HDFC Bank Limited) score 52.6 — "Credit card additions hit second-highest monthly level in 2026 as banks gear up for festiv"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 52.1 — "Credit card additions hit second-highest monthly level in 2026 as banks gear up for festiv"
- IDBI.NS (IDBI BANK LIMITED) score 51.7 — "Credit card additions hit second-highest monthly level in 2026 as banks gear up for festiv"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 51.7 — "Credit card additions hit second-highest monthly level in 2026 as banks gear up for festiv"
- TGT (Target Corporation) score 50.5 — "Sunteck Realty, Radico Khaitan, WeWork India, Supreme Industries, Kajaria: Jefferies sees "
- COIN (Coinbase Global, Inc.) score 47.5 — "India's growth momentum stays resilient despite global headwinds: RBI Deputy Governor Poon"
- TECHM.NS (TECH MAHINDRA LIMITED) score 45.2 — "The rest of the market is leaving Big Tech behind after a historic comeback"
- OHI (Omega Healthcare Investors, In) score 43.6 — "S&P DOW JONES INDICES AND KALSHI PARTNER TO CREATE NEW FINANCIAL INDICES S&P DJI will deve"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.9 — "The rest of the market is leaving Big Tech behind after a historic comeback"
- TECH (Bio-Techne Corp) score 39.9 — "The rest of the market is leaving Big Tech behind after a historic comeback"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 32.2 — "US ENERGY SEC WRIGHT SAYS IRAN WAR HAS 'COME AT A COST': FOX"
- CHKP (Check Point Software Technolog) score 31.6 — "Is that used EV worth the price? This checklist could save you thousands of dollars."
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 26.0 — "Netweb Technologies shares: Multibagger stock jumps 780% against IPO price in 3 years; exp"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 25.7 — "Stocks in news: Jio Platforms, RIL, Infosys, L&T, Tata Capital, Waaree Energies and Vedant"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 25.7 — "Stocks in news: Jio Platforms, RIL, Infosys, L&T, Tata Capital, Waaree Energies and Vedant"
- BOND (PIMCO Active Bond Exchange-Tra) score 24.1 — "Corporate bond market liquidity expands across US and Europe"
- LTH (Life Time Group Holdings, Inc.) score 22.8 — "When will Anthropic go public? Here’s what to know about the IPO timeline."
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 21.8 — "Q2 Results Today Highlgihts: Bajaj Auto Q2 PAT up 35%, Maruti Suzuki & Cipla profit down, "
- 301077.SZ (CHINASTARS) score 18.4 — "China Stock Premium Over Hong Kong Widens on State Intervention"
- JUSTDIAL.BO (JUST DIAL LTD.) score 16.6 — "Housing is flashing warning signs just as the Fed weighs more interest rate hikes"
- RS (Reliance, Inc.) score 16.0 — "Jio IPO GMP hints at 22% listing-day pop for a market cap second only to Reliance Industri"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 15.3 — "Shriram Finance shares falls 5% as analysts cut targets after Q2 results"
- JIOFIN.BO (Jio Financial Services Limited) score 14.9 — "S&P DOW JONES INDICES AND KALSHI PARTNER TO CREATE NEW FINANCIAL INDICES S&P DJI will deve"
- BZ=F (Brent Crude Oil Last Day Finan) score 13.1 — "COREWEAVE 5-YEAR CDS NARROWS TO LOWEST LEVEL IN OVER A WEEK, LAST AT 1041.4 BPS - MARKIT D"
- SEPN (Septerna, Inc.) score 13.1 — "US OCT CONSUMER CONFIDENCE INDEX 91.7 (CONSENSUS 81.0) VS SEPT REVISED 84.2 (PREVIOUS 81.9"
- META (Meta) score 12.5 — "AMD $META - AMD AND META ADVANCE STRATEGIC PARTNERSHIP TO POWER META’S SUPERINTELLIGENCE I"
- JEF (Jefferies Financial Group Inc.) score 12.0 — "Sunteck Realty, Radico Khaitan, WeWork India, Supreme Industries, Kajaria: Jefferies sees "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 8.8 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Daily Price Change"
- VT (Vanguard Total World Stock Ind) score 8.4 — "World Bank's Banga: Availability of capital 'not really an issue' as AI demand drives up b"
- INFY (Infosys Limited) score 8.3 — "Stocks in news: Jio Platforms, RIL, Infosys, L&T, Tata Capital, Waaree Energies and Vedant"
- GS (Goldman Sachs Group, Inc. (The) score 7.9 — "Paytm shares rise 2% after Q2 results. What are Jefferies, Goldman Sachs, and others sayin"
- SCHD (Schwab US Dividend Equity ETF) score 5.0 — "Mazagon Dock Shipbuilders shares crash 10% after Q2 net profit tumbles 54%; firm declares "
- SWIGGY.NS (SWIGGY LIMITED) score 3.7 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"
- POLICYBZR.NS (PB FINTECH LIMITED) score 1.1 — "MDR uncertainty, choppy markets cloud ₹33,600-crore fintech IPO pipeline"
- VOLTAS.NS (VOLTAS LTD) score 0.0 — "Voltas’s market share is growing. Will margins follow?"

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