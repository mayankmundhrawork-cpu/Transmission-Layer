# Transmission Layer — board brief · 2026-10-06 18:20Z

data as of **2026-10-06** · 97 series · 6 red / 34 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.619, 2d in regime; vol-pct 0.612, breadth-off 0.625, Markov P(high-vol) 0.017)
- [INVERTED] **safe_haven_gold** — corr20 -0.4, corr60 -0.42, contra nifty_50 corr20=0.04, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.79, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.13, corr60 0.2, last shift 2026-07-09. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.04, corr60 0.12, last shift 2026-08-17. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.77, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.23, corr60 -0.09, last shift 2026-08-17. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.3, corr60 -0.24, last shift 2026-08-17. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.43, corr60 0.19, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 3.9968028886505635e-15)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.497** (n=1130) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.824** (n=2279) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 6.43] usd_inr ↑
- usd_inr [FX]: last 96.41, z20 1.43, zc 0.17, resid-z -0.03 [quiet], 1d 0.09%, 20d range extreme; 1y-pct=96
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.392 via usd_inr, z 2.35, reacted)
- **India receivers**: dyn_idbi_ns (rho -0.392, z 2.35)
- Source: Rupee loses 13 paise to close at 96.42 per US dollar — ET Markets, 2026-10-06. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-loses-13-paise-to-close-at-96-42-per-us-dollar/articleshow/134744262.cms
- Source: Rupee slips to over two-month low ahead of RBI policy decision — BusinessLine Mkts, 2026-10-06. https://www.thehindubusinessline.com/markets/forex/rupee-slips-to-over-two-month-low-ahead-of-rbi-policy-decision/article71551180.ece
- Source: Bulls hold for second day, but rupee bleeds near record low — BusinessLine Mkts, 2026-10-06. https://www.thehindubusinessline.com/markets/bulls-hold-for-second-day-but-rupee-bleeds-near-record-low/article71551341.ece
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2025-09-16 (d=0.01)

### [AMBER 5.88] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.63, z20 1.95, zc 0.44, resid-z 0.65 [quiet], 1d 0.36%, |z20|=1.95; 1y-pct=99
- ust_10y [RATES]: last 5.28, z20 1.61, zc 0.72, resid-z 1.07 [quiet], 1d 0.76%, |z20|=1.61; 1y-pct=99
- tips_10y_real [RATES]: last 2.92, z20 1.52, zc 0.69, resid-z 1.03 [quiet], 1d 1.39%, |z20|=1.52; 1y-pct=99
- dyn_bond [EQUITIES]: last 86.70, z20 -1.42, zc 0.95, resid-z -0.41 [quiet], 1d 0.35%, 1y-pct=1
- ust_2y [RATES]: last 4.83, z20 0.82, zc 0.78, resid-z 1.10 [quiet], 1d 1.05%, 1y-pct=98
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.534 vs ust_10y, historically leads by 4d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.531 vs ust_30y
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.525 vs ust_30y
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: S&P 500, Nasdaq hit record highs as Treasury yields stall, crude slips — ET Markets, 2026-10-06. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-us-stock-market-live-updates-nasdaq-sp-500-iran-war-hormuz-deal-brent-crude-oil-fed-rate-treasury-yields-meta-tesla-amazon-amd-option-care-health-ai-chip-stock-price-news-6th-october-2026/liveblog/134740613.cms
- Source: U.S. YIELDS RETREAT FROM 24-YEAR HIGHS Treasury yields pulled back as oil fell below $100 and Scott Bessent pledged that stronger growth and spending restraint would begin improving the U.S. debt trajectory. The 10-year yield fell to 5.27% and the 30-year to 5.63%, easing from levels last seen in 20 — DeItaone, 2026-10-06. https://t.me/walter_bloomberg/36662
- Source: JULIUS BAER SEES FINAL FED HIKE IN DECEMBER Julius Baer expects the Fed to deliver one final 25bp rate hike in December, followed by an extended pause. The bank points to a cooling U.S. labor market and sharply tighter financial conditions, driven more by rising long-term Treasury yields and a stron — DeItaone, 2026-10-06. https://t.me/walter_bloomberg/36656
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.81] indices · 2 series ↑
- nikkei_225 [INDICES]: last 70773.80, z20 2.98, zc 0.66, resid-z 0.60 [quiet], 1d 1.18%, |z20|=2.98; 1y-pct=98
- taiwan_weighted [INDICES]: last 49754.07, z20 2.41, zc 0.08, resid-z 0.05 [quiet], 1d 0.08%, |z20|=2.41; 1y-pct=100
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.7).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho 0.538 via taiwan_weighted, z -1.3, reacted); nifty_it (rho -0.372 via taiwan_weighted, z -0.88, quiet)
- Watch next: kospi (co-move) — not yet - watch; rho 0.848 vs nikkei_225
- **India receivers**: dyn_bajfinance_ns (rho 0.538, z -1.3); nifty_it (rho -0.372, z -0.88)
- Source: Stock market outlook today, 6 Oct: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Nikkei, Taiwan cues — Mint Markets, 2026-10-06. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-6-oct-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-nikkei-taiwan-cues-11791247193944.html
- Source: Global Market: Japan’s Nikkei jumps 2.5% to 3-month high as AI stocks rally — ET Markets, 2026-10-05. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-jumps-2-5-to-3-month-high-as-ai-stocks-rally/articleshow/134685851.cms
- Historical analogues: 2025-12-30 (d=0.7), 2025-07-11 (d=0.77), 2026-06-09 (d=1.0)

### [RED 5.43] indices · 2 series ↑
- sp500 [INDICES]: last 7828.74, z20 2.60, zc 0.96, resid-z 0.67 [quiet], 1d 0.70%, |z20|=2.60; 1y-pct=100
- nasdaq_100 [INDICES]: last 31293.09, z20 1.93, zc 0.66, resid-z -0.27 [quiet], 1d 0.70%, |z20|=1.93; 1y-pct=100
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: vix (inverse) — not yet - watch; rho -0.749 vs sp500, historically leads by 4d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.87 vs sp500
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.79 vs sp500
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.651 vs sp500
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.596 vs nasdaq_100
- Source: These 5 chip stocks are cheaper than the S&P 500 — and offer faster growth — MarketWatch Top, 2026-10-06. https://www.marketwatch.com/story/these-5-chip-stocks-are-cheaper-than-the-s-p-500-and-offer-faster-growth-f8ab4386?mod=mw_rss_topstories
- Source: Why US stocks are rising today: S&P 500, Nasdaq hit records as easing yields and oil fuel AI rally — ET Markets, 2026-10-06. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-sp-500-hits-intraday-record-high-as-ai-rally-continues/articleshow/134742430.cms
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: S&P 500, Nasdaq hit record highs as Treasury yields stall, crude slips — ET Markets, 2026-10-06. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-us-stock-market-live-updates-nasdaq-sp-500-iran-war-hormuz-deal-brent-crude-oil-fed-rate-treasury-yields-meta-tesla-amazon-amd-option-care-health-ai-chip-stock-price-news-6th-october-2026/liveblog/134740613.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-07 (d=0.06), 2026-05-15 (d=0.07)

### [RED 5.23] dyn_sepn ↓
- dyn_sepn [EQUITIES]: last 36.08, z20 -3.23, zc -1.16, resid-z -0.08 [quiet], 1d -4.74%, |z20|=3.23
- **Mechanism**: dyn_sepn ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: IEX logs 10.4% growth in electricity trade volume to 12.2 billion units in Sept — BusinessLine Mkts, 2026-10-06. https://www.thehindubusinessline.com/economy/iex-logs-104-growth-in-electricity-trade-volume-to-122-billion-units-in-sept/article71550216.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-13 (d=0.0), 2025-05-01 (d=0.01)

### [RED 5.2] dyn_ohi ↓
- dyn_ohi [EQUITIES]: last 44.68, z20 -3.20, zc -1.12, resid-z 1.04 [quiet], 1d -1.50%, |z20|=3.20
- **Mechanism**: dyn_ohi ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Top stocks in focus tomorrow: Investors must watch Titan, Utkarsh SFB, HCL Tech shares on Wed, 7 Oct | Triggers — Mint Markets, 2026-10-06. https://www.livemint.com/market/stock-market-news/top-stocks-in-focus-tomorrow-investors-must-watch-titan-utkarsh-sfb-hcl-tech-shares-on-wed-7-oct-triggers-11791294292454.html
- Source: SRIT India shares jump 19% on listing day, Shah Investors Home gain 4% — BusinessLine Mkts, 2026-10-06. https://www.thehindubusinessline.com/markets/srit-india-shah-investors-home-shares-make-positive-debut-stocks-hit-upper-circuit/article71550305.ece
- Source: Can IPO buzz boost CDSL and NSDL Q2 earnings? What the stocks investors need to know — Mint Markets, 2026-10-06. https://www.livemint.com/market/stock-market-news/can-ipo-buzz-boost-cdsl-and-nsdl-q2-earnings-what-the-stocks-investors-need-to-know-11791284891478.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2025-04-02 (d=0.09)

### [AMBER 4.3] dyn_nvda ↑
- dyn_nvda [EQUITIES]: last 240.20, z20 2.30, zc 0.27, resid-z -0.19 [quiet], 1d 0.54%, |z20|=2.30; 1y-pct=100
- **Mechanism**: dyn_nvda ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: vix (inverse) — not yet - watch; rho -0.566 vs dyn_nvda, historically leads by 4d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.56 vs dyn_nvda, historically leads by 1d
- Source: The case for Nvidia’s stock to march even higher after clinching its first record high in months — MarketWatch Top, 2026-10-05. https://www.marketwatch.com/story/the-case-for-nvidias-stock-to-march-even-higher-after-clinching-its-first-record-high-in-months-2bb5a937?mod=mw_rss_topstories
- Source: AI stock Nvidia stock gets target upgrade from BNP Paribas; 47% further upside seen by experts - check revised price — Mint Markets, 2026-10-05. https://www.livemint.com/market/stock-market-news/ai-stock-nvidia-stock-gets-target-upgrade-from-bnp-paribas-47-further-upside-seen-by-experts-check-revised-price-11791214034610.html
- Source: Nvidia still 'the one' for AI? BNP Paribas raises target to $345, sees up to 47% upside — ET Markets, 2026-10-05. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/nvidia-still-the-one-for-ai-bnp-paribas-raises-target-to-345-sees-up-to-47-upside/articleshow/134698952.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-24 (d=0.03), 2026-05-04 (d=0.03)

### [AMBER 4.27] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 6420.00, z20 2.27, zc 2.11, resid-z 0.12 [moved], 1d 8.26%, |z20|=2.27; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tatatech_ns (rho 0.356 via dyn_4417_t, z -0.9, quiet)
- **India receivers**: dyn_tatatech_ns (rho 0.356, z -0.9)
- Source: Why Kotak Mahindra Bank shares are outperforming Nifty 50 and Bank Nifty in the last two months? Experts explain — Mint Markets, 2026-10-06. https://www.livemint.com/market/stock-market-news/why-kotak-mahindra-bank-shares-are-outperforming-nifty-50-and-bank-nifty-in-the-last-two-months-experts-explain-11791281103828.html
- Source: Gold-Silver ratio hits 68: What it means? Should investors switch from gold to silver? Here's what experts suggest — Mint Markets, 2026-10-06. https://www.livemint.com/market/commodities/goldsilver-ratio-hits-68-what-it-means-should-investors-switch-from-gold-to-silver-heres-what-experts-suggest-11791275528883.html
- Source: Q2 business updates: Experts tell best banking stocks to buy ahead of Q2 results FY27? — Mint Markets, 2026-10-06. https://www.livemint.com/market/stock-market-news/q2-business-updates-experts-tell-which-banking-stocks-to-buy-ahead-of-q2-results-fy27-11791272451622.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

## Watchlist (below surfacing floor)
dyn_techm_ns ↓ (4.24), dyn_coalindia_ns ↓ (4.22), usd_brl ↓ (3.99), bovespa ↑ (3.97), hy_oas ↑ (3.65), eur_usd ↓ (3.61), dyn_policybzr_ns ↓ (3.32), dyn_jiofin_bo ↓ (3.28), nifty_50 ↓ (3.08), gold_silver_ratio ↓ (3.06), dyn_meta ↑ (2.94), dyn_tech ↑ (2.41)

## India macro
- nifty_50: 22776.0996 (1d 0.98%, z20 -1.08, flag amber)
- nifty_midcap_100: 59761.7500 (1d 1.07%, z20 -1.14, flag none)
- usd_inr: 96.4100 (1d 0.09%, z20 1.43, flag amber)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6239 (1d 0.09%, z20 -1.05, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI MPC decision T-1d · AMFI SIP / MF flows T-2d · RBI Weekly Statistical Supplement T-3d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 83.7 — "TSLA - GOLDMAN: TESLA’S AI STORY MATTERS MORE THAN Q3 EARNINGS Goldman Sachs reiterated it"
- INOXINDIA.NS (INOX INDIA LIMITED) score 82.5 — "Market wrap: Trent, BSE, Coal India, Tech Mahindra top gainers and losers on Nifty and Sen"
- COALINDIA.NS (COAL INDIA LTD) score 81.4 — "Market wrap: Trent, BSE, Coal India, Tech Mahindra top gainers and losers on Nifty and Sen"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 79.6 — "Market wrap: Trent, BSE, Coal India, Tech Mahindra top gainers and losers on Nifty and Sen"
- BAC (Bank of America Corporation) score 69.2 — "DALIO WARNS CHINA AND JAPAN COULD PULL BACK FROM TREASURIES Ray Dalio warns U.S. Treasurie"
- HDB (HDFC Bank Limited) score 64.6 — "TSLA - GOLDMAN: TESLA’S AI STORY MATTERS MORE THAN Q3 EARNINGS Goldman Sachs reiterated it"
- IDBI.NS (IDBI BANK LIMITED) score 62.4 — "TSLA - GOLDMAN: TESLA’S AI STORY MATTERS MORE THAN Q3 EARNINGS Goldman Sachs reiterated it"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 62.4 — "TSLA - GOLDMAN: TESLA’S AI STORY MATTERS MORE THAN Q3 EARNINGS Goldman Sachs reiterated it"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 62.4 — "TSLA - GOLDMAN: TESLA’S AI STORY MATTERS MORE THAN Q3 EARNINGS Goldman Sachs reiterated it"
- COIN (Coinbase Global, Inc.) score 47.9 — "ET Alpha Wealth Summit 2.0: Where is smart money moving amid global market churn?"
- BOND (PIMCO Active Bond Exchange-Tra) score 45.9 — "Indian bonds rangebound as traders await a hawkish RBI verdict"
- OHI (Omega Healthcare Investors, In) score 43.4 — "Can IPO buzz boost CDSL and NSDL Q2 earnings? What the stocks investors need to know"
- TECHM.NS (TECH MAHINDRA LIMITED) score 42.9 — "Broker’s call: Techno Electric & Engineering (Buy)"
- TGT (Target Corporation) score 36.6 — "TSLA - GOLDMAN: TESLA’S AI STORY MATTERS MORE THAN Q3 EARNINGS Goldman Sachs reiterated it"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 35.6 — "Broker’s call: Techno Electric & Engineering (Buy)"
- TECH (Bio-Techne Corp) score 35.6 — "Broker’s call: Techno Electric & Engineering (Buy)"
- CHKP (Check Point Software Technolog) score 34.3 — "TajGVK Hotels shares: Stock down 26% in 1 year, but Monarch sees 49% upside - Here's why |"
- LTH (Life Time Group Holdings, Inc.) score 28.6 — "PRESIDENT TRUMP — TUESDAY, OCTOBER 6, 2026 🔸 8:00 AM — Executive Time — White House 🔸 9:00"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 23.9 — "Energy Shock Wipes $264 Billion Off the World's Top Mining Stocks"
- SEPN (Septerna, Inc.) score 21.5 — "IEX logs 10.4% growth in electricity trade volume to 12.2 billion units in Sept"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 18.7 — "Mutual Funds', FPI favourite Tata Group stock hits upper circuit after Q2 update - Can it "
- 301077.SZ (CHINASTARS) score 17.1 — "US AND CHINA DISCUSSING RECIPROCAL NUCLEAR SITE VISITS AMID CONCERNS ABOUT A NEW ARMS RACE"
- BZ=F (Brent Crude Oil Last Day Finan) score 16.3 — "U.S. YIELDS RETREAT FROM 24-YEAR HIGHS Treasury yields pulled back as oil fell below $100 "
- JIOFIN.BO (Jio Financial Services Limited) score 10.4 — "JULIUS BAER SEES FINAL FED HIKE IN DECEMBER Julius Baer expects the Fed to deliver one fin"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.5 — "Trade deficit hits $105.6 billion, widest since just before Trump tariffs enacted last yea"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 8.9 — "Utkarsh Small Finance Bank Q2 disbursements jump 55% YoY to Rs 3,525 crore; loan portfolio"
- JEF (Jefferies Financial Group Inc.) score 8.9 — "Reliance Industries shares gain 3% as JIO IPO inches closer; Jefferies increases weight in"
- VT (Vanguard Total World Stock Ind) score 8.7 — "Energy Shock Wipes $264 Billion Off the World's Top Mining Stocks"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 7.7 — "Mutual Funds', FPI favourite Tata Group stock hits upper circuit after Q2 update - Can it "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 7.7 — "Mutual Funds', FPI favourite Tata Group stock hits upper circuit after Q2 update - Can it "
- META (Meta) score 7.1 — "Bitcoin vs gold: Why Cathie Wood feels cryptocurrency's 'turn is in' against the precious "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.7 — "Adani Power gains 2% after signing pact for 770-MW hydropower project in Bhutan"
- GS (Goldman Sachs Group, Inc. (The) score 6.4 — "TSLA - GOLDMAN: TESLA’S AI STORY MATTERS MORE THAN Q3 EARNINGS Goldman Sachs reiterated it"
- POLICYBZR.NS (PB FINTECH LIMITED) score 5.4 — "PB Fintech extends losing streak to 7 sessions, stock hits 32-month low"
- NVDA (NVIDIA Corporation) score 5.4 — "The case for Nvidia’s stock to march even higher after clinching its first record high in "
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 5.4 — "Value retail stocks slide on cautious consumer spending"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.0 — "RBI MPC meeting Oct 2026: Why TCS, HDFC Bank, ICICI Lombard, Coal India shares may gain if"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 4.8 — "Utkarsh Small Finance Bank Q2 disbursements jump 55% YoY to Rs 3,525 crore; loan portfolio"
- VOLTAS.NS (VOLTAS LTD) score 0.1 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 0.1 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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