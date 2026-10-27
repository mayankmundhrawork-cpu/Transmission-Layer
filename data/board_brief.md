# Transmission Layer — board brief · 2026-10-27 15:52Z

data as of **2026-10-27** · 97 series · 9 red / 46 amber · 8 events surfaced (37 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.752, 17d in regime; vol-pct 0.74, breadth-off 0.765, Markov P(high-vol) 0.017)
- [INVERTED] **safe_haven_gold** — corr20 -0.39, corr60 -0.39, contra nifty_50 corr20=0.43, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.86, corr60 0.82, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.09, corr60 0.15, last shift 2026-09-03. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.17, corr60 0.03, last shift 2026-09-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.77, last shift 2026-09-09. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.19, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.1, corr60 -0.14, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.54, corr60 0.25, last shift 2026-07-22. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 1.1738575289577113e-06)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.503** (n=1119) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.828** (n=1749) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.42] cross-asset · 2 series ↑
- comex_silver [COMMODITIES]: last 54.59, z20 -1.59, zc 0.36, resid-z -0.32 [quiet], 1d 0.89%, |z20|=1.59
- gold_silver_ratio [DERIVED]: last 74.67, z20 1.58, zc n/a, resid-z n/a [quiet], 1d 0.05%, GSR<75 (extreme low); |z20|=1.58
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.557 vs comex_silver
- Source: Can silver price hit  ₹2.84 lakh/kg as rates in free fall ahead of 2026 Dhanteras, Diwali? Levels, target, stop loss — Mint Markets, 2026-10-27. https://www.livemint.com/market/commodities/can-silver-price-hit-rs-2-84-lakh-kg-as-rates-in-free-fall-ahead-of-2026-dhanteras-diwali-levels-target-stop-loss-11793088097843.html
- Source: Silver futures decline to ₹1.92 lakh/kg — BusinessLine Mkts, 2026-10-27. https://www.thehindubusinessline.com/markets/commodities/silver-futures-decline-to-192-lakhkg/article71630370.ece
- Source: Gold steadies near $4,000 as Fed policy meet begins; silver near 11-month low — BusinessLine Mkts, 2026-10-27. https://www.thehindubusinessline.com/markets/commodities/gold-steadies-near-4000-as-fed-policy-meet-begins-silver-near-11-month-low/article71630140.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-29 (d=0.06), 2025-08-12 (d=0.14)

### [RED 7.19] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1674.00, z20 5.19, zc 1.93, resid-z 1.37 [moved], 1d 6.29%, |z20|=5.19; 1y-pct=98
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.412 via dyn_atherenerg_ns, z -1.42, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.412, z -1.42)
- Source: Ather Energy shares: 125% YTD returns! Experts give 'portfolio stock' tag after Q2 results 2026 | Target, stop-loss — Mint Markets, 2026-10-27. https://www.livemint.com/market/stock-market-news/ather-energy-shares-125-ytd-returns-experts-give-portfolio-stock-tag-after-q2-results-2026-target-stoploss-11793080902497.html
- Source: Ather achieves profitability milestone, supply ramp-up to pave the road ahead — Mint Markets, 2026-10-27. https://www.livemint.com/market/mark-to-market/ather-energy-q2-results-net-profit-revenue-growth-11793081766549.html
- Source: Ather Energy shares jump 5%, extend rally to 20% in two days after Q2 results. Can the run continue? — ET Markets, 2026-10-27. https://economictimes.indiatimes.com/markets/stocks/news/ather-energy-shares-jump-5-extend-rally-to-20-in-two-days-after-q2-results-can-the-run-continue/articleshow/135225009.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [AMBER 6.78] commodities · 2 series ↑
- wti [COMMODITIES]: last 100.00, z20 0.95, zc -0.62, resid-z 0.02 [quiet], 1d -1.73%, 1-session move -1.73% ≥ 1.5%
- brent [COMMODITIES]: last 109.31, z20 0.62, zc -2.42, resid-z -1.64 [unexplained], 1d -5.61%, 1-session move -5.61% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.398 via wti, z -1.42, reacted)
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.59 vs brent
- Watch next: vix (co-move) — not yet - watch; rho 0.541 vs brent
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.525 vs wti
- Watch next: sp500 (inverse) — not yet - watch; rho -0.504 vs wti
- **India receivers**: nifty_midcap_100 (rho -0.398, z -1.42)
- Source: OPEC+ Set to Keep Oil Quotas Unchanged — OilPrice, 2026-10-27. https://oilprice.com/Latest-Energy-News/World-News/OPEC-Set-to-Keep-Oil-Quotas-Unchanged.html
- Source: US stocks today: S&P 500, Nasdaq advance as oil eases ahead of Fed decision — ET Markets, 2026-10-27. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-sp-500-nasdaq-open-higher-as-oil-pulls-back-ahead-of-fed-decision/articleshow/135236366.cms
- Source: US Stock Market Live Updates: S&P 500, Nasdaq advance as oil eases ahead of Fed decision — ET Markets, 2026-10-27. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/stock-market-live-updates-dow-jones-nasdaq-sp-500-coca-cola-paypal-tesla-meta-earnings-federal-reserve-fed-rate-decision-us-stocks-oil-crude-oil-treasury-yields-ai-stocks-anthropic-ipo-27th-october-2026/liveblog/135233966.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [AMBER 6.37] cross-asset · 5 series ↓
- tips_10y_real [RATES]: last 2.66, z20 -2.44, zc 0.37, resid-z -0.05 [quiet], 1d 0.76%, |z20|=2.44
- ust_10y [RATES]: last 5.00, z20 -2.34, zc 0.73, resid-z 0.24 [quiet], 1d 0.81%, |z20|=2.34
- ust_30y [RATES]: last 5.33, z20 -2.05, zc 0.85, resid-z 0.47 [quiet], 1d 0.76%, |z20|=2.05
- ust_2y [RATES]: last 4.69, z20 -1.94, zc 0.65, resid-z 0.19 [quiet], 1d 0.86%, |z20|=1.94
- dyn_schd [EQUITIES]: last 35.13, z20 1.51, zc -0.54, resid-z -0.31 [quiet], 1d -0.48%, 1y-pct=98
- **Mechanism**: cross-asset · 5 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.043 vs ust_2y, historically leads by 1d
- Source: Mazagon Dock Shipbuilders shares crash 10% after Q2 net profit tumbles 54%; firm declares Rs 5/share dividend — ET Markets, 2026-10-27. https://economictimes.indiatimes.com/markets/stocks/news/mazagon-dock-shipbuilders-shares-crash-10-after-q2-net-profit-tumbles-54-firm-declares-rs-5/share-dividend/articleshow/135232098.cms
- Source: Top dividend stocks to buy: PTC India, CESC, Vedanta, Coal India, HPCL offer up to 24% yield. Check full list here — Mint Markets, 2026-10-27. https://www.livemint.com/market/stock-market-news/top-dividend-stocks-to-buy-ptc-india-cesc-vedanta-coal-india-hpcl-offer-up-to-24-yield-check-full-list-here-11793085342244.html
- Source: Dividend stocks are having an excellent October as tech sector struggles — MarketWatch Top, 2026-10-26. https://www.marketwatch.com/story/dividend-stocks-are-having-an-excellent-october-as-tech-sector-struggles-5ae40b02?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-12 (d=0.63), 2025-05-19 (d=1.06)

### [RED 6.22] cross-asset · 4 series ↓
- dyn_bajfinance_ns [EQUITIES]: last 912.00, z20 -2.55, zc -0.42, resid-z 0.02 [quiet], 1d -0.73%, |z20|=2.55
- dyn_jiofin_bo [EQUITIES]: last 207.25, z20 -1.55, zc 0.58, resid-z 0.95 [quiet], 1d 0.90%, 1y-pct=1
- india_vix [INDICES]: last 16.36, z20 1.54, zc -0.79, resid-z n/a [quiet], 1d -4.66%, |z20|=1.54
- dyn_policybzr_ns [EQUITIES]: last 1008.40, z20 -0.71, zc -0.61, resid-z -0.37 [quiet], 1d -1.43%, 1y-pct=2
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-11 (z-distance 0.48).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.744 via dyn_jiofin_bo, z -1.42, reacted); nifty_50 (rho -0.728 via india_vix, z 0.23, quiet); nifty_metal (rho -0.579 via india_vix, z -0.97, quiet); nifty_fmcg (rho 0.572 via dyn_jiofin_bo, z -1.51, reacted); dyn_indusindbk_bo (rho -0.553 via india_vix, z -1.99, reacted)
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.581 vs dyn_bajfinance_ns, historically leads by 4d
- Watch next: dyn_indianb_ns (co-move) — not yet - watch; rho 0.54 vs dyn_jiofin_bo, historically leads by 1d
- Watch next: nifty_metal (co-move) — not yet - watch; rho 0.564 vs dyn_jiofin_bo
- **India receivers**: nifty_midcap_100 (rho 0.744, z -1.42); nifty_50 (rho -0.728, z 0.23); nifty_metal (rho -0.579, z -0.97); nifty_fmcg (rho 0.572, z -1.51)
- Source: Q2 Results Today Live: Bajaj Auto Q2 PAT up 35%, Maruti Suzuki & Cipla profit down, ACC, Mazagon Dock PAT tumbles, Honeywell Automation PAT up, L&T, Vedanta Iron, Waaree Energies, SAIL, SBI Life, Tata Capital, Star Health, ABDL to announce Q2 results — BusinessLine Mkts, 2026-10-27. https://www.thehindubusinessline.com/markets/q2-results-today-live-updates-lampt-maruti-suzuki-bajaj-auto-tata-steel-vedanta-iron-waaree-acc-sail-sbi-star-health-mazagon-dock-cipla-united-breweries-ather-paytm-tata-consumer-results-27-october-20/article71626455.ece
- Source: Bajaj Auto Q2 Results: Profit jumps 35% YoY to Rs 3,354 crore; revenue up 34% — ET Markets, 2026-10-27. https://economictimes.indiatimes.com/markets/stocks/earnings/bajaj-auto-q2-results-profit-jumps-35-yoy-to-rs-3354-crore-revenue-up-34/articleshow/135230311.cms
- Source: Q2 Results Today Live: Bharat Bijlee & Bharat Seats rally after Q2, Cipla profit declines 35%, L&T, Maruti Suzuki, Bajaj Auto, Vedanta Iron, Waaree Energies, Mazagon Dock, ACC, SAIL, SBI Life, Tata Capital, Star Health, Honeywell Automation, ABDL to announce Q2 results — BusinessLine Mkts, 2026-10-27. https://www.thehindubusinessline.com/markets/q2-results-today-live-updates-lampt-maruti-suzuki-bajaj-auto-tata-steel-vedanta-iron-waaree-acc-sail-sbi-star-health-mazagon-dock-cipla-united-breweries-ather-paytm-tata-consumer-results-27-october-20/article71626455.ece
- Historical analogues: 2025-07-11 (d=0.48), 2025-07-21 (d=0.62), 2025-07-04 (d=0.99)

### [RED 6.1] dyn_lth ↑
- dyn_lth [EQUITIES]: last 44.50, z20 4.10, zc 0.50, resid-z -0.11 [quiet], 1d 1.46%, |z20|=4.10
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Gold price in India to touch  ₹2 lakh per 10 gm by end of 2027? Is it the right time to buy before Dhanteras, Diwali? — Mint Markets, 2026-10-27. https://www.livemint.com/market/commodities/gold-price-in-india-to-touch-rs-2-lakh-per-10-gm-by-end-of-2027-is-it-the-right-time-to-buy-before-dhanteras-diwali-11793082888965.html
- Source: ITC Hotels share price jumps 6% after Q2 results - Is it the right time to buy the stock? Experts decode — Mint Markets, 2026-10-27. https://www.livemint.com/market/stock-market-news/itc-hotels-share-price-jumps-6-after-q2-results-is-it-the-right-time-to-buy-the-stock-experts-decode-11793073302905.html
- Source: Jio Platforms IPO listing date and time, share price prediction, expected gains, latest GMP; all eyes on NSE, BSE debut — Mint Markets, 2026-10-27. https://www.livemint.com/market/ipo/jio-platforms-ipo-listing-date-and-time-share-price-prediction-expected-gains-latest-gmp-all-eyes-on-nse-bse-debut-11793071293037.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-17 (d=0.02), 2025-12-31 (d=0.02)

### [AMBER 5.16] natgas ↓
- natgas [COMMODITIES]: last 3.00, z20 -0.16, zc 4.05, resid-z 5.93 [unexplained], 1d 15.41%, 1-session move +15.41% ≥ 5.0%
- **Mechanism**: natgas ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Alleged Russian Funding Prompts Executive Exodus at U.S. LNG Firm — OilPrice, 2026-10-26. https://oilprice.com/Energy/Natural-Gas/Alleged-Russian-Funding-Prompts-Executive-Exodus-at-US-LNG-Firm.html
- Source: The Iran War Just Added $39 Billion to the World's LNG Bill — OilPrice, 2026-10-26. https://oilprice.com/Energy/Natural-Gas/The-Iran-War-Just-Added-39-Billion-to-the-Worlds-LNG-Bill.html
- Source: Europe's Natural Gas Prices Soar to Four-Year High as Winter Looms — OilPrice, 2026-10-26. https://oilprice.com/Latest-Energy-News/World-News/Europes-Natural-Gas-Prices-Soar-to-Four-Year-High-as-Winter-Looms.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [AMBER 4.8] commodities · 2 series ↓
- wheat [COMMODITIES]: last 616.50, z20 -1.97, zc 0.05, resid-z 0.10 [quiet], 1d 0.08%, |z20|=1.97
- corn [COMMODITIES]: last 451.50, z20 -1.70, zc -0.57, resid-z -0.50 [quiet], 1d -0.77%, |z20|=1.70
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Corn drops on US harvest pressure, wheat near 3-1/2-month low — BusinessLine Mkts, 2026-10-27. https://www.thehindubusinessline.com/markets/commodities/corn-drops-on-us-harvest-pressure-wheat-near-3-12-month-low/article71629668.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-04-01 (d=0.35), 2025-08-28 (d=0.36)

## Watchlist (below surfacing floor)
dyn_sepn ↑ (4.68), dyn_meta ↓ (4.54), dyn_tech ↑ (4.49), dyn_chkp ↑ (4.45), dyn_tgt ↓ (4.22), dyn_hdb ↓ (4.21), dyn_coin ↓ (4.09), dyn_tatatech_ns ↓ (4.09), dyn_rs ↑ (4.02), dyn_coalindia_ns ↓ (4.01), dyn_gs ↑ (4.01), usd_cny ↓ (3.85)

## India macro
- nifty_50: 22749.7500 (1d -0.02%, z20 0.23, flag none)
- nifty_midcap_100: 57030.3008 (1d 1.00%, z20 -1.42, flag none)
- usd_inr: 95.1050 (1d 0.18%, z20 -0.68, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5069 (1d 1.01%, z20 -1.57, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 86.7 — "Indian lenders defer dollar debt sale plan as rates turn expensive"
- INOXINDIA.NS (INOX INDIA LIMITED) score 84.5 — "Indian lenders defer dollar debt sale plan as rates turn expensive"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 83.8 — "Indian lenders defer dollar debt sale plan as rates turn expensive"
- INDIANB.NS (INDIAN BANK) score 68.9 — "Indian lenders defer dollar debt sale plan as rates turn expensive"
- BAC (Bank of America Corporation) score 62.3 — "Sensex today | Stock Market Highlights: Stock markets end largely unchanged amid elevated "
- HDB (HDFC Bank Limited) score 56.1 — "Sensex today | Stock Market Highlights: Stock markets end largely unchanged amid elevated "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 55.5 — "Sensex today | Stock Market Highlights: Stock markets end largely unchanged amid elevated "
- IDBI.NS (IDBI BANK LIMITED) score 55.2 — "Sensex today | Stock Market Highlights: Stock markets end largely unchanged amid elevated "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 55.2 — "Sensex today | Stock Market Highlights: Stock markets end largely unchanged amid elevated "
- TGT (Target Corporation) score 52.8 — "Top Diwali 2026 Muhurat stocks to buy: Axis Securities lists 9 shares for Samvat 2083 | Ch"
- COIN (Coinbase Global, Inc.) score 49.5 — "Global Market: European shares fall as HSBC earnings drag banking stocks"
- OHI (Omega Healthcare Investors, In) score 46.4 — "Nifty FMCG down 22% in 2026; Diwali shopping opportunity for investors? Experts decode sup"
- TECHM.NS (TECH MAHINDRA LIMITED) score 46.0 — "KFin Technologies surges 6% after Q2 results"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 40.2 — "KFin Technologies surges 6% after Q2 results"
- TECH (Bio-Techne Corp) score 40.2 — "KFin Technologies surges 6% after Q2 results"
- CHKP (Check Point Software Technolog) score 33.3 — "Top Diwali 2026 Muhurat stocks to buy: Axis Securities lists 9 shares for Samvat 2083 | Ch"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 31.8 — "El Nino ramping up into a ‘very strong' weather event as index surges to 18-year high"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 28.3 — "Netweb Technologies shares: Multibagger stock jumps 780% against IPO price in 3 years; exp"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 25.8 — "This Tata Group stock jumps 7% today after Q2 results - Is it a stock to buy now? Experts "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 25.8 — "This Tata Group stock jumps 7% today after Q2 results - Is it a stock to buy now? Experts "
- BOND (PIMCO Active Bond Exchange-Tra) score 25.2 — "Global bond issuance set to grow at slowest pace in five years in 2027, S&P Global Ratings"
- LTH (Life Time Group Holdings, Inc.) score 22.7 — "Jio Platforms IPO listing date and time, share price prediction, expected gains, latest GM"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 22.6 — "Bajaj Auto Q2 Results: Profit jumps 35% YoY to Rs 3,354 crore; revenue up 34%"
- 301077.SZ (CHINASTARS) score 18.9 — "Global Market: Yuan holds near four-year high as China tempers appreciation pace"
- RS (Reliance, Inc.) score 17.4 — "Jio IPO GMP hints at 22% listing-day pop for a market cap second only to Reliance Industri"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.6 — "Shriram Finance shares falls 5% as analysts cut targets after Q2 results"
- JUSTDIAL.BO (JUST DIAL LTD.) score 15.9 — "10 microcap stocks rally up to 80% in just 3 months"
- JIOFIN.BO (Jio Financial Services Limited) score 15.2 — "Newly listed stock has 27% upside potential! JM Financial issues buy call; Check target pr"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.1 — "Cold Blasts to Pose Early Test for European and Asia Gas Markets"
- SEPN (Septerna, Inc.) score 12.1 — "OIL OPTIONS SIGNAL RISING MIDDLE EAST SUPPLY RISKS WTI crude oil options skew toward calls"
- JEF (Jefferies Financial Group Inc.) score 11.9 — "Paytm, Vodafone Idea, ITC Hotels, Sona BLW to Tata Consumer shares: Jefferies sees up to 4"
- META (Meta) score 11.6 — "Nvidia, AMD and Broadcom could buy Meta shares as part of $35 billion stock offering"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.5 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Daily Price Change"
- VT (Vanguard Total World Stock Ind) score 9.1 — "World Bank's Banga: Availability of capital 'not really an issue' as AI demand drives up b"
- GS (Goldman Sachs Group, Inc. (The) score 8.6 — "Paytm shares rise 2% after Q2 results. What are Jefferies, Goldman Sachs, and others sayin"
- INFY (Infosys Limited) score 8.0 — "Stock market ends flat as Infosys drags IT stocks, defence shares rally"
- SCHD (Schwab US Dividend Equity ETF) score 5.4 — "Mazagon Dock Shipbuilders shares crash 10% after Q2 net profit tumbles 54%; firm declares "
- SWIGGY.NS (SWIGGY LIMITED) score 4.0 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.1 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
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