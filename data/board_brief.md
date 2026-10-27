# Transmission Layer — board brief · 2026-10-27 09:47Z

data as of **2026-10-27** · 97 series · 13 red / 44 amber · 8 events surfaced (35 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.828, 17d in regime; vol-pct 0.74, breadth-off 0.917, Markov P(high-vol) 0.021)
- [INVERTED] **safe_haven_gold** — corr20 -0.36, corr60 -0.38, contra nifty_50 corr20=0.44, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.83, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.07, corr60 0.15, last shift 2026-09-03. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.17, corr60 0.04, last shift 2026-09-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.78, last shift 2026-09-09. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.19, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.1, corr60 -0.14, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.53, corr60 0.25, last shift 2026-07-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 1.935929592189467e-06)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.504** (n=1117) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.824** (n=1870) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.45] dyn_lth ↑
- dyn_lth [EQUITIES]: last 43.86, z20 5.45, zc 2.15, resid-z -0.11 [moved], 1d 4.60%, |z20|=5.45
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Gold price in India to touch  ₹2 lakh per 10 gm by end of 2027? Is it the right time to buy before Dhanteras, Diwali? — Mint Markets, 2026-10-27. https://www.livemint.com/market/commodities/gold-price-in-india-to-touch-rs-2-lakh-per-10-gm-by-end-of-2027-is-it-the-right-time-to-buy-before-dhanteras-diwali-11793082888965.html
- Source: ITC Hotels share price jumps 6% after Q2 results - Is it the right time to buy the stock? Experts decode — Mint Markets, 2026-10-27. https://www.livemint.com/market/stock-market-news/itc-hotels-share-price-jumps-6-after-q2-results-is-it-the-right-time-to-buy-the-stock-experts-decode-11793073302905.html
- Source: Jio Platforms IPO listing date and time, share price prediction, expected gains, latest GMP; all eyes on NSE, BSE debut — Mint Markets, 2026-10-27. https://www.livemint.com/market/ipo/jio-platforms-ipo-listing-date-and-time-share-price-prediction-expected-gains-latest-gmp-all-eyes-on-nse-bse-debut-11793071293037.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-17 (d=0.02), 2025-12-31 (d=0.02)

### [RED 7.09] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1669.80, z20 5.09, zc 1.85, resid-z 1.33 [moved], 1d 6.02%, |z20|=5.09; 1y-pct=98
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.406 via dyn_atherenerg_ns, z -1.51, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.406, z -1.51)
- Source: Ather Energy shares: 125% YTD returns! Experts give 'portfolio stock' tag after Q2 results 2026 | Target, stop-loss — Mint Markets, 2026-10-27. https://www.livemint.com/market/stock-market-news/ather-energy-shares-125-ytd-returns-experts-give-portfolio-stock-tag-after-q2-results-2026-target-stoploss-11793080902497.html
- Source: Ather achieves profitability milestone, supply ramp-up to pave the road ahead — Mint Markets, 2026-10-27. https://www.livemint.com/market/mark-to-market/ather-energy-q2-results-net-profit-revenue-growth-11793081766549.html
- Source: Ather Energy shares jump 5%, extend rally to 20% in two days after Q2 results. Can the run continue? — ET Markets, 2026-10-27. https://economictimes.indiatimes.com/markets/stocks/news/ather-energy-shares-jump-5-extend-rally-to-20-in-two-days-after-q2-results-can-the-run-continue/articleshow/135225009.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [RED 6.71] cross-asset · 6 series ↓
- dyn_bajfinance_ns [EQUITIES]: last 911.80, z20 -2.56, zc -0.43, resid-z -0.07 [quiet], 1d -0.75%, |z20|=2.56
- dyn_swiggy_ns [EQUITIES]: last 190.20, z20 -1.75, zc 0.34, resid-z 0.36 [quiet], 1d 2.40%, 1y-pct=1
- india_vix [INDICES]: last 16.41, z20 1.58, zc -0.74, resid-z n/a [quiet], 1d -4.37%, |z20|=1.58
- nifty_midcap_100 [INDICES]: last 56930.60, z20 -1.51, zc 0.66, resid-z 1.51 [unexplained], 1d 0.82%, |z20|=1.51
- dyn_jiofin_bo [EQUITIES]: last 207.80, z20 -1.44, zc 0.75, resid-z 1.08 [quiet], 1d 1.17%, 1y-pct=1
- dyn_policybzr_ns [EQUITIES]: last 1004.30, z20 -0.81, zc -0.79, resid-z -0.44 [quiet], 1d -1.83%, 1y-pct=2
- **Mechanism**: cross-asset · 6 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.79).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho -0.73 via india_vix, z 0.28, quiet); nifty_metal (rho 0.69 via nifty_midcap_100, z -1.01, reacted); midcap_largecap_ratio (rho 0.608 via nifty_midcap_100, z -1.68, reacted); nifty_fmcg (rho 0.599 via nifty_midcap_100, z -1.89, reacted); dyn_indusindbk_bo (rho -0.571 via india_vix, z -1.47, reacted)
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.58 vs dyn_bajfinance_ns, historically leads by 4d
- Watch next: dyn_indianb_ns (co-move) — not yet - watch; rho 0.568 vs nifty_midcap_100, historically leads by 1d
- **India receivers**: nifty_50 (rho -0.73, z 0.28); nifty_metal (rho 0.69, z -1.01); midcap_largecap_ratio (rho 0.608, z -1.68); nifty_fmcg (rho 0.599, z -1.89)
- Source: Q2 Results Today Live: Bharat Bijlee & Bharat Seats rally after Q2, Cipla profit declines 35%, L&T, Maruti Suzuki, Bajaj Auto, Vedanta Iron, Waaree Energies, Mazagon Dock, ACC, SAIL, SBI Life, Tata Capital, Star Health, Honeywell Automation, ABDL to announce Q2 results — BusinessLine Mkts, 2026-10-27. https://www.thehindubusinessline.com/markets/q2-results-today-live-updates-lampt-maruti-suzuki-bajaj-auto-tata-steel-vedanta-iron-waaree-acc-sail-sbi-star-health-mazagon-dock-cipla-united-breweries-ather-paytm-tata-consumer-results-27-october-20/article71626455.ece
- Source: Jio Financial Services share price decoded: Reliance stock performance amid Jio Platforms IPO buzz; target, outlook — Mint Markets, 2026-10-27. https://www.livemint.com/market/stock-market-news/jio-financial-services-share-price-decoded-reliance-stock-performance-amid-jio-platforms-ipo-buzz-target-outlook-11793079481962.html
- Source: Maruti Suzuki vs Bajaj Auto: Which auto stock to buy ahead of Q2 results 2026? Experts decode — Mint Markets, 2026-10-27. https://www.livemint.com/market/stock-market-news/maruti-suzuki-vs-bajaj-auto-which-auto-stock-to-buy-ahead-of-q2-results-2026-experts-decode-11793080790074.html
- Historical analogues: 2025-07-21 (d=0.79), 2025-05-30 (d=0.88), 2025-07-10 (d=0.91)

### [AMBER 6.59] cross-asset · 6 series ↓
- tips_10y_real [RATES]: last 2.66, z20 -2.44, zc 0.37, resid-z -0.05 [quiet], 1d 0.76%, |z20|=2.44
- ust_10y [RATES]: last 5.00, z20 -2.34, zc 0.73, resid-z 0.24 [quiet], 1d 0.81%, |z20|=2.34
- dyn_bond [EQUITIES]: last 88.59, z20 2.08, zc 0.27, resid-z 0.61 [quiet], 1d 0.10%, |z20|=2.08
- ust_30y [RATES]: last 5.33, z20 -2.05, zc 0.85, resid-z 0.47 [quiet], 1d 0.76%, |z20|=2.05
- ust_2y [RATES]: last 4.69, z20 -1.94, zc 0.65, resid-z 0.19 [quiet], 1d 0.86%, |z20|=1.94
- dyn_schd [EQUITIES]: last 35.27, z20 1.89, zc -0.01, resid-z -0.31 [quiet], 1d -0.01%, 1y-pct=99
- **Mechanism**: cross-asset · 6 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dxy (inverse) — not yet - watch; rho -0.545 vs dyn_bond
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.044 vs ust_2y, historically leads by 1d
- Source: Top dividend stocks to buy: PTC India, CESC, Vedanta, Coal India, HPCL offer up to 24% yield. Check full list here — Mint Markets, 2026-10-27. https://www.livemint.com/market/stock-market-news/top-dividend-stocks-to-buy-ptc-india-cesc-vedanta-coal-india-hpcl-offer-up-to-24-yield-check-full-list-here-11793085342244.html
- Source: Dividend stocks are having an excellent October as tech sector struggles — MarketWatch Top, 2026-10-26. https://www.marketwatch.com/story/dividend-stocks-are-having-an-excellent-october-as-tech-sector-struggles-5ae40b02?mod=mw_rss_topstories
- Source: Analysis: Why a $2 trillion deficit and 5% Treasury yields are becoming America's biggest economic challenge — CNBC Economy, 2026-10-26. https://www.cnbc.com/2026/10/15/treasury-yields-deficit-national-debt-ai.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-12 (d=0.58), 2025-05-19 (d=0.98)

### [AMBER 6.0] brent ↑
- brent [COMMODITIES]: last 111.13, z20 1.00, zc -1.74, resid-z 0.30 [priced], 1d -4.04%, 1-session move -4.04% ≥ 1.5%
- **Mechanism**: brent ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (inverse) — not yet - watch; rho -0.562 vs brent
- Source: Trump Moves to Ease Methane Regulations for U.S. Oil Producers — OilPrice, 2026-10-27. https://oilprice.com/Latest-Energy-News/World-News/Trump-Moves-to-Ease-Methane-Regulations-for-US-Oil-Producers.html
- Source: India’s Oil Buyers Squeezed by $123 Crude and Weak Rupee — OilPrice, 2026-10-27. https://oilprice.com/Latest-Energy-News/World-News/Indias-Oil-Buyers-Squeezed-by-123-Crude-and-Weak-Rupee.html
- Source: Oil Prices Drop Despite Threat of New U.S. Strikes on Iran — OilPrice, 2026-10-27. https://oilprice.com/Latest-Energy-News/World-News/Oil-Prices-Drop-Despite-Threat-of-New-US-Strikes-on-Iran.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-14 (d=0.02), 2025-04-16 (d=0.04)

### [RED 5.92] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4009.30, z20 -2.60, zc -0.56, resid-z -0.90 [quiet], 1d -0.72%, |z20|=2.60; 1y-pct=5; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 53.22, z20 -2.17, zc -0.66, resid-z -0.34 [quiet], 1d -1.64%, |z20|=2.17; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 75.33, z20 1.89, zc n/a, resid-z n/a [quiet], 1d 0.94%, |z20|=1.89
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.543 vs comex_silver, historically leads by 1d
- Source: Amundi Says ‘Worst Is Behind Us’ as Gold Flirts With $4,000 — Mint Markets, 2026-10-27. https://www.livemint.com/market/amundi-says-worst-is-behind-us-as-gold-flirts-with-4000-11793092640404.html
- Source: Can silver price hit  ₹2.84 lakh/kg as rates in free fall ahead of 2026 Dhanteras, Diwali? Levels, target, stop loss — Mint Markets, 2026-10-27. https://www.livemint.com/market/commodities/can-silver-price-hit-rs-2-84-lakh-kg-as-rates-in-free-fall-ahead-of-2026-dhanteras-diwali-levels-target-stop-loss-11793088097843.html
- Source: Today’s Gold Rate in India October 27: Gold prices up in Coimbatore, Nagpur, Visakhapatnam, Surat, Jaipur — BusinessLine Mkts, 2026-10-27. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-coimbatore-nagpur-visakhapatnam-surat-jaipur-lucknow-chandigarh-gold-rates-other-cities-october-27-2026/article71630368.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [AMBER 5.82] cross-asset · 3 series ↓
- dyn_coin [EQUITIES]: last 159.68, z20 -2.50, zc -0.62, resid-z -0.11 [quiet], 1d -2.90%, |z20|=2.50
- btc_usd [CRYPTO]: last 79559.05, z20 -2.10, zc -0.27, resid-z -0.92 [quiet], 1d -0.56%, |z20|=2.10
- eth_usd [CRYPTO]: last 2305.24, z20 -1.69, zc -0.17, resid-z -1.02 [quiet], 1d -0.65%, |z20|=1.69
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-16 (z-distance 0.5).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.377 via btc_usd, z -1.82, reacted)
- **India receivers**: dyn_muthootfin_ns (rho 0.377, z -1.82)
- Source: Global Market: Japan life insurers eye domestic bonds as foreign debt selling grows — ET Markets, 2026-10-27. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-japan-life-insurers-eye-domestic-bonds-as-foreign-debt-selling-grows/articleshow/135228458.cms
- Source: IEA Warns of Dangerous Concentration in Global Clean Energy Supply Chains — OilPrice, 2026-10-27. https://oilprice.com/Latest-Energy-News/World-News/IEA-Warns-of-Dangerous-Concentration-in-Global-Clean-Energy-Supply-Chains.html
- Source: Global Market: JGB yields climb as investors await BOJ, Fed policy decisions — ET Markets, 2026-10-27. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-jgb-yields-climb-as-investors-await-boj-fed-policy-decisions/articleshow/135228326.cms
- Historical analogues: 2025-10-16 (d=0.5), 2026-05-22 (d=0.55), 2025-04-10 (d=0.63)

### [AMBER 5.07] natgas ↑
- natgas [COMMODITIES]: last 3.05, z20 0.07, zc 4.48, resid-z -0.52 [moved], 1d 17.06%, 1-session move +17.06% ≥ 5.0%
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Alleged Russian Funding Prompts Executive Exodus at U.S. LNG Firm — OilPrice, 2026-10-26. https://oilprice.com/Energy/Natural-Gas/Alleged-Russian-Funding-Prompts-Executive-Exodus-at-US-LNG-Firm.html
- Source: The Iran War Just Added $39 Billion to the World's LNG Bill — OilPrice, 2026-10-26. https://oilprice.com/Energy/Natural-Gas/The-Iran-War-Just-Added-39-Billion-to-the-Worlds-LNG-Bill.html
- Source: Europe's Natural Gas Prices Soar to Four-Year High as Winter Looms — OilPrice, 2026-10-26. https://oilprice.com/Latest-Energy-News/World-News/Europes-Natural-Gas-Prices-Soar-to-Four-Year-High-as-Winter-Looms.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

## Watchlist (below surfacing floor)
dyn_tgt ↓ (5.06), dyn_meta ↓ (5.02), dyn_chkp ↑ (5.0), commodities · 2 series ↓ (4.83), dyn_tech ↑ (4.7), dyn_tatatech_ns ↓ (4.23), dyn_ohi ↑ (4.1), dyn_sepn ↑ (4.1), dyn_hdb ↓ (3.92), eur_usd ↓ (3.9), usd_brl ↑ (3.89), dyn_301077_sz ↓ (3.77)

## India macro
- nifty_50: 22760.7500 (1d 0.03%, z20 0.28, flag none)
- nifty_midcap_100: 56930.6016 (1d 0.82%, z20 -1.51, flag amber)
- usd_inr: 95.1300 (1d 0.20%, z20 -0.65, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5013 (1d 0.79%, z20 -1.68, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 82.3 — "Will Rs 5 lakh crore bet on Jio open floodgates for India's mega IPOs?"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 79.3 — "Will Rs 5 lakh crore bet on Jio open floodgates for India's mega IPOs?"
- INOXINDIA.NS (INOX INDIA LIMITED) score 79.0 — "Will Rs 5 lakh crore bet on Jio open floodgates for India's mega IPOs?"
- INDIANB.NS (INDIAN BANK) score 67.7 — "October 2026 euro area bank lending survey"
- BAC (Bank of America Corporation) score 61.9 — "October 2026 euro area bank lending survey"
- HDB (HDFC Bank Limited) score 55.3 — "October 2026 euro area bank lending survey"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 54.6 — "October 2026 euro area bank lending survey"
- IDBI.NS (IDBI BANK LIMITED) score 54.3 — "October 2026 euro area bank lending survey"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 54.3 — "October 2026 euro area bank lending survey"
- COIN (Coinbase Global, Inc.) score 49.3 — "Global Market: South Korean shares jump over 4% as AI chip rally lifts Samsung, SK Hynix"
- TGT (Target Corporation) score 48.5 — "Paytm, Vodafone Idea, ITC Hotels, Sona BLW to Tata Consumer shares: Jefferies sees up to 4"
- OHI (Omega Healthcare Investors, In) score 47.1 — "SFC Environmental Tech raises ₹200 crore from anchor investors"
- TECHM.NS (TECH MAHINDRA LIMITED) score 45.6 — "VVDN Technologies said to consider up to $300 million IPO"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.4 — "VVDN Technologies said to consider up to $300 million IPO"
- TECH (Bio-Techne Corp) score 39.4 — "VVDN Technologies said to consider up to $300 million IPO"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 31.6 — "Ather Energy shares already up 126% in 2026 and jump 5% to extend post Q2 rally today - Sh"
- CHKP (Check Point Software Technolog) score 31.1 — "BLS Polymers IPO opens today; GMP signals 27% listing gain. Check key details"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 26.8 — "ITC Hotels share price jumps 6% after Q2 results - Is it the right time to buy the stock? "
- BOND (PIMCO Active Bond Exchange-Tra) score 24.6 — "Indian bonds tick up on calm oil before Fed verdict"
- LTH (Life Time Group Holdings, Inc.) score 24.1 — "Jio Platforms IPO listing date and time, share price prediction, expected gains, latest GM"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 21.9 — "Maruti Suzuki vs Bajaj Auto: Which auto stock to buy ahead of Q2 results 2026? Experts dec"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 21.0 — "Paytm, Vodafone Idea, ITC Hotels, Sona BLW to Tata Consumer shares: Jefferies sees up to 4"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 21.0 — "Paytm, Vodafone Idea, ITC Hotels, Sona BLW to Tata Consumer shares: Jefferies sees up to 4"
- 301077.SZ (CHINASTARS) score 20.1 — "Global Market: Yuan holds near four-year high as China tempers appreciation pace"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 17.6 — "Shriram Finance shares falls 5% as analysts cut targets after Q2 results"
- RS (Reliance, Inc.) score 17.4 — "Reliance shares performance decoded: From Jio Platforms IPO opening to allotment finalisat"
- JUSTDIAL.BO (JUST DIAL LTD.) score 13.7 — "US JUSTICE DEPARTMENT CHARGES FORMER FBI DIRECTOR JAMES COMEY WITH TRANSMITTING NATIONAL D"
- JIOFIN.BO (Jio Financial Services Limited) score 12.9 — "HUL Share Price Live Updates: HUL's Financial Performance Review"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.9 — "Cold Blasts to Pose Early Test for European and Asia Gas Markets"
- SEPN (Septerna, Inc.) score 12.8 — "OIL OPTIONS SIGNAL RISING MIDDLE EAST SUPPLY RISKS WTI crude oil options skew toward calls"
- JEF (Jefferies Financial Group Inc.) score 12.6 — "Paytm, Vodafone Idea, ITC Hotels, Sona BLW to Tata Consumer shares: Jefferies sees up to 4"
- META (Meta) score 12.3 — "Nvidia, AMD and Broadcom could buy Meta shares as part of $35 billion stock offering"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.1 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Daily Price Change"
- GS (Goldman Sachs Group, Inc. (The) score 9.1 — "Paytm shares rise 2% after Q2 results. What are Jefferies, Goldman Sachs, and others sayin"
- VT (Vanguard Total World Stock Ind) score 8.6 — "Anthropic's potential mega IPO joins ranks of world's biggest listings"
- INFY (Infosys Limited) score 7.4 — "Infosys Share Price Live Updates: Infosys Price Movement Analysis"
- SCHD (Schwab US Dividend Equity ETF) score 4.7 — "Top dividend stocks to buy: PTC India, CESC, Vedanta, Coal India, HPCL offer up to 24% yie"
- SWIGGY.NS (SWIGGY LIMITED) score 4.3 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.2 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
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