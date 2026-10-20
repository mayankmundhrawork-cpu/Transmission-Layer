# Transmission Layer — board brief · 2026-10-20 09:24Z

data as of **2026-10-20** · 97 series · 9 red / 34 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.87, 12d in regime; vol-pct 0.739, breadth-off 1.0, Markov P(high-vol) 0.022)
- [INVERTED] **safe_haven_gold** — corr20 -0.26, corr60 -0.39, contra nifty_50 corr20=0.41, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.83, corr60 0.83, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.26, corr60 0.21, last shift 2026-08-26. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.08, corr60 0.1, last shift 2026-09-01. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.78, corr60 -0.78, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.11, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.18, corr60 -0.26, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.44, corr60 0.22, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** dyn_hdb → usd_inr: leads 1d (ccf -0.362, β -0.0913, p 0.0); driver zc -1.87 → expected 0.295%. Type hit-rate 0.814 (n=1944).
- Track record · residual_reversion: hit-rate **0.501** (n=1121) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.814** (n=1944) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.41] commodities · 2 series ↑
- brent [COMMODITIES]: last 111.50, z20 2.58, zc 0.85, resid-z 0.18 [quiet], 1d 1.78%, 1-session move +1.78% ≥ 1.5%; |z20|=2.58; 1y-pct=96
- wti [COMMODITIES]: last 100.50, z20 1.87, zc -1.22, resid-z 1.20 [quiet], 1d -3.05%, 1-session move -3.05% ≥ 1.5%; |z20|=1.87
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.603 vs brent, historically leads by 5d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.59 vs brent
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.567 vs brent
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.562 vs brent
- Source: Asian refiners in dispute with Saudis over 2027 oil contracts — BusinessLine Mkts, 2026-10-20. https://www.thehindubusinessline.com/markets/commodities/asian-refiners-in-dispute-with-saudis-over-2027-oil-contracts/article71603833.ece
- Source: Brent Tops $110 as Tanker Attacks Threaten Persian Gulf Supply — OilPrice, 2026-10-20. https://oilprice.com/Latest-Energy-News/World-News/Brent-Tops-110-as-Tanker-Attacks-Threaten-Persian-Gulf-Supply.html
- Source: Brent crude holds near five-month high on Middle East tension — BusinessLine Mkts, 2026-10-20. https://www.thehindubusinessline.com/markets/commodities/brent-crude-holds-near-five-month-high-on-middle-east-tension/article71603236.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 6.8] cross-asset · 3 series ↑
- dyn_techm_ns [EQUITIES]: last 1779.10, z20 3.49, zc -0.20, resid-z 0.71 [quiet], 1d -0.61%, |z20|=3.49; 1y-pct=99
- nifty_it [INDICES]: last 31516.30, z20 2.58, zc -0.63, resid-z 0.27 [quiet], 1d -1.28%, |z20|=2.58
- dyn_tataelxsi_ns [EQUITIES]: last 3790.00, z20 2.43, zc -0.61, resid-z 0.38 [quiet], 1d -1.56%, |z20|=2.43
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 0.78).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.521 via dyn_tataelxsi_ns, z 0.13, quiet); dyn_justdial_bo (rho 0.513 via nifty_it, z 3.68, reacted); nifty_fmcg (rho 0.489 via dyn_tataelxsi_ns, z -1.54, reacted); midcap_largecap_ratio (rho -0.439 via dyn_techm_ns, z -2.66, reacted); dyn_tatatech_ns (rho 0.404 via nifty_it, z -0.6, quiet)
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.514 vs nifty_it
- **India receivers**: nifty_50 (rho 0.521, z 0.13); dyn_justdial_bo (rho 0.513, z 3.68); nifty_fmcg (rho 0.489, z -1.54); midcap_largecap_ratio (rho -0.439, z -2.66)
- Source: What to do with IT stocks? TCS, HCL Tech, Wipro, Infosys, Tech Mahindra — Why experts are bullish after Accenture news — Mint Markets, 2026-10-19. https://www.livemint.com/market/stock-market-news/tcs-hcl-tech-wipro-infosys-to-tech-mahindra-experts-bullish-on-it-shares-after-accentures-shift-from-ai-investment-11792390800742.html
- Source: How to trade Tech Mahindra shares after 22% rally in 4 days? Technical expert weighs in — ET Markets, 2026-10-19. https://economictimes.indiatimes.com/markets/stocks/news/how-to-trade-tech-mahindra-shares-after-22-rally-in-4-days-technical-expert-weighs-in/articleshow/135041900.cms
- Source: Veteran SIP investors not deterred by stagnant market: Kotak Mahindra's's Harsha Upadhyaya — Mint Markets, 2026-10-19. https://www.livemint.com/market/veteran-sip-investors-not-deterred-by-stagnant-market-kotak-mahindrass-harsha-upadhyaya-11792308340457.html
- Historical analogues: 2025-08-13 (d=0.78), 2025-01-23 (d=0.84), 2025-12-30 (d=0.85)

### [RED 5.68] dyn_justdial_bo ↑
- dyn_justdial_bo [EQUITIES]: last 732.55, z20 3.68, zc 0.82, resid-z 1.21 [quiet], 1d 2.82%, |z20|=3.68
- **Mechanism**: dyn_justdial_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.513 via dyn_justdial_bo, z 2.58, reacted); dyn_techm_ns (rho 0.505 via dyn_justdial_bo, z 3.49, reacted); nifty_50 (rho 0.454 via dyn_justdial_bo, z 0.13, quiet); dyn_tataelxsi_ns (rho 0.396 via dyn_justdial_bo, z 2.43, reacted); nifty_midcap_100 (rho 0.351 via dyn_justdial_bo, z -1.12, reacted)
- **India receivers**: nifty_it (rho 0.513, z 2.58); dyn_techm_ns (rho 0.505, z 3.49); nifty_50 (rho 0.454, z 0.13); dyn_tataelxsi_ns (rho 0.396, z 2.43)
- Source: Top stocks to buy for short term: Just Dial, BSE, Orient Hotels - Target price, stop-loss by Anand Rathi's expert — Mint Markets, 2026-10-20. https://www.livemint.com/market/stock-market-news/top-stocks-to-buy-for-short-term-just-dial-bse-orient-hotels-target-price-stop-loss-by-anand-rathis-expert-11792400725179.html
- Source: Just Dial shares skyrocket 13% as volume soars massively 115 times - More returns ahead or something else? Experts view — Mint Markets, 2026-10-19. https://www.livemint.com/market/stock-market-news/just-dial-shares-skyrocket-13-as-volume-soars-massively-115-times-more-returns-ahead-or-something-else-experts-view-11792394067468.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-18 (d=0.19), 2025-06-30 (d=0.52)

### [AMBER 5.33] cross-asset · 3 series ↓
- dyn_coin [EQUITIES]: last 168.45, z20 -2.01, zc -0.59, resid-z -1.10 [quiet], 1d -2.72%, |z20|=2.01
- eth_usd [CRYPTO]: last 2381.61, z20 -1.67, zc -0.25, resid-z -0.44 [quiet], 1d -0.96%, |z20|=1.67
- btc_usd [CRYPTO]: last 81360.66, z20 -1.51, zc -0.32, resid-z -0.12 [quiet], 1d -0.60%, |z20|=1.51
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-22 (z-distance 0.26).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.353 via btc_usd, z -1.48, reacted)
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.574 vs eth_usd, historically leads by 1d
- Watch next: dxy (inverse) — not yet - watch; rho -0.505 vs eth_usd, historically leads by 2d
- **India receivers**: dyn_muthootfin_ns (rho 0.353, z -1.48)
- Source: China flags APEC's role as key for a challenged global economy — ET Markets, 2026-10-20. https://economictimes.indiatimes.com/markets/us-stocks/news/update-1-china-flags-apecs-role-as-key-for-a-challenged-global-economy/articleshow/135065449.cms
- Source: Global Market: China and Hong Kong shares weaken as stable growth eases stimulus bets — ET Markets, 2026-10-20. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-china-and-hong-kong-shares-weaken-as-stable-growth-eases-stimulus-bets/articleshow/135061983.cms
- Source: Global Market: South Korea's Elice shares plunge 28% in market debut as data centre stocks shunned — ET Markets, 2026-10-20. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-south-koreas-elice-shares-plunge-28-in-market-debut-as-data-centre-stocks-shunned/articleshow/135060541.cms
- Historical analogues: 2025-10-22 (d=0.26), 2025-03-31 (d=0.32), 2025-10-30 (d=0.43)

### [AMBER 5.01] indices · 2 series ↓
- nasdaq_100 [INDICES]: last 29536.02, z20 -2.18, zc 0.84, resid-z -1.80 [unexplained], 1d 1.19%, |z20|=2.18
- russell_2000 [INDICES]: last 2727.92, z20 -2.03, zc 0.16, resid-z -0.02 [quiet], 1d 0.24%, |z20|=2.03
- **Mechanism**: indices · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.916 vs nasdaq_100, historically leads by 2d
- Watch next: dyn_bond (co-move) — not yet - watch; rho 0.53 vs russell_2000, historically leads by 1d
- Watch next: ust_10y (inverse) — not yet - watch; rho -0.507 vs russell_2000, historically leads by 1d
- Source: Global markets today: GIFT Nifty up, Nikkei 225, Kospi slide on Tuesday, 20 Oct | Nasdaq, S&P, DJIA rise up to 1% — Mint Markets, 2026-10-20. https://www.livemint.com/market/stock-market-news/global-markets-today-gift-nifty-nikkei-225-kospi-t-slide-on-tuesday-20-october-nasdaq-s-p-djia-rise-up-to-1-11792458344691.html
- Source: US stocks today: Nasdaq leads Wall Street gains as chip, AI stocks rebound — ET Markets, 2026-10-19. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-nasdaq-leads-wall-street-gains-as-chip-ai-stocks-rebound/articleshow/135056194.cms
- Source: HEDGE FUNDS DUMP TECH STOCKS AT FASTEST PACE IN A DECADE Goldman Sachs reports that hedge funds cut technology exposure at the fastest pace since at least 2016 during the five sessions ending October 15. The Nasdaq 100 plunged 5.5% last week, while semiconductor stocks suffered the largest dollar se — DeItaone, 2026-10-19. https://t.me/walter_bloomberg/37318
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-18 (d=0.06), 2025-05-07 (d=0.12)

### [AMBER 4.36] dyn_bac ↓
- dyn_bac [EQUITIES]: last 50.39, z20 -2.36, zc -0.97, resid-z 0.59 [quiet], 1d -1.64%, |z20|=2.36
- **Mechanism**: dyn_bac ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Why Invading Iran Could Become America's Biggest Military Mistake — OilPrice, 2026-10-19. https://oilprice.com/Energy/Energy-General/Why-Invading-Iran-Could-Become-Americas-Biggest-Military-Mistake.html
- Source: Colombia’s Critical Minerals Could Be a Game Changer for America — OilPrice, 2026-10-19. https://oilprice.com/Energy/Energy-General/Colombias-Critical-Minerals-Could-Be-a-Game-Changer-for-America.html
- Source: Elon Musk pledges a share of SpaceX company to 'every kid in America' — ET Markets, 2026-10-19. https://economictimes.indiatimes.com/markets/us-stocks/news/elon-musk-pledges-a-share-of-spacex-company-to-every-kid-in-america/articleshow/135048478.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-23 (d=0.03), 2025-03-31 (d=0.12)

### [AMBER 4.26] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 7510.00, z20 2.26, zc 0.10, resid-z 2.82 [unexplained], 1d 0.54%, |z20|=2.26; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Hindustan Zinc shares: Experts bullish on Anil Agarwal-led metal stock after robust Q2 results 2026 | Target, stop-loss — Mint Markets, 2026-10-20. https://www.livemint.com/market/stock-market-news/hindustan-zinc-shares-experts-bullish-on-anil-agarwal-led-metal-stock-after-robust-q2-results-2026-target-stoploss-11792474520524.html
- Source: Why should you buy Vedanta shares despite strong Hindustan Zinc Q2 results 2026? Experts' views, target price — Mint Markets, 2026-10-20. https://www.livemint.com/market/stock-market-news/why-should-you-buy-vedanta-shares-despite-strong-hindustan-zinc-q2-results-2026-experts-views-target-price-stoploss-11792469059843.html
- Source: Oil Price Today (October 20): Crude oil nears $110 again as fresh attacks outweigh easing Russian sanctions. What are experts saying? — ET Markets, 2026-10-20. https://economictimes.indiatimes.com/markets/commodities/news/oil-price-today-october-20-crude-oil-nears-110-again-as-fresh-attacks-outweigh-easing-russian-sanctions-what-are-experts-saying/articleshow/135059918.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

### [AMBER 4.22] dyn_rs ↑
- dyn_rs [EQUITIES]: last 415.67, z20 2.22, zc 0.68, resid-z 0.63 [quiet], 1d 1.09%, |z20|=2.22; 1y-pct=100
- **Mechanism**: dyn_rs ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Dussehra 2026 special: Top 3 stocks to buy; ICICI Bank, Adani Ports, Reliance Industries | Target price by Mahesh M Ojha — Mint Markets, 2026-10-20. https://www.livemint.com/market/stock-market-news/dussehra-2026-special-top-3-stocks-to-buy-icici-bank-adani-ports-reliance-industries-target-price-by-mahesh-m-ojha-11792481678492.html
- Source: Analysis ahead of Reliance Jio IPO: Bharti Airtel is better or Mukesh Ambani shares? Top value things before bid opens — Mint Markets, 2026-10-20. https://www.livemint.com/market/ipo/analysis-ahead-of-reliance-jio-ipo-bharti-airtel-is-better-or-mukesh-ambani-shares-top-value-things-before-bid-opens-11792481253599.html
- Source: Reliance Jio IPO review: Apply or not? Bid now or buy shares post NSE, BSE debut? Check GMP, listing price prediction — Mint Markets, 2026-10-20. https://www.livemint.com/market/ipo/reliance-jio-ipo-review-apply-or-not-bid-now-or-buy-shares-post-nse-bse-debut-check-gmp-listing-price-prediction-11792461309554.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-30 (d=0.02), 2026-03-31 (d=0.02)

## Watchlist (below surfacing floor)
gold_silver_ratio ↑ (4.18), gbp_usd ↑ (4.07), dyn_wit ↑ (4.04), dyn_karurvysya_ns ↑ (3.88), usd_inr ↓ (3.69), hy_oas ↑ (3.54), usd_cny ↓ (3.15), indices · 2 series ↓ (3.14), commodities · 3 series ↓ (3.11), indices · 2 series ↓ (3.01), eur_usd ↓ (2.73), dyn_dell ↓ (2.7)

## India macro
- nifty_50: 22888.9492 (1d -1.11%, z20 0.13, flag none)
- nifty_midcap_100: 58483.4492 (1d -1.09%, z20 -1.12, flag none)
- usd_inr: 94.9200 (1d -0.06%, z20 -1.69, flag amber)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5551 (1d 0.02%, z20 -2.66, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 86.4 — "OPENAI SEEKS $1.4 TRILLION VALUATION AHEAD OF ANTHROPIC IPO OpenAI is reportedly racing to"
- COALINDIA.NS (COAL INDIA LTD) score 86.2 — "Dussehra holiday: Indian financial markets to remain closed on Tuesday"
- INOXINDIA.NS (INOX INDIA LIMITED) score 81.2 — "Dussehra holiday: Indian financial markets to remain closed on Tuesday"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 80.8 — "Dussehra holiday: Indian financial markets to remain closed on Tuesday"
- BAC (Bank of America Corporation) score 79.3 — "OPENAI SEEKS $1.4 TRILLION VALUATION AHEAD OF ANTHROPIC IPO OpenAI is reportedly racing to"
- HDB (HDFC Bank Limited) score 73.4 — "OPENAI SEEKS $1.4 TRILLION VALUATION AHEAD OF ANTHROPIC IPO OpenAI is reportedly racing to"
- IDBI.NS (IDBI BANK LIMITED) score 70.1 — "OPENAI SEEKS $1.4 TRILLION VALUATION AHEAD OF ANTHROPIC IPO OpenAI is reportedly racing to"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 70.1 — "OPENAI SEEKS $1.4 TRILLION VALUATION AHEAD OF ANTHROPIC IPO OpenAI is reportedly racing to"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 70.1 — "OPENAI SEEKS $1.4 TRILLION VALUATION AHEAD OF ANTHROPIC IPO OpenAI is reportedly racing to"
- TECHM.NS (TECH MAHINDRA LIMITED) score 57.8 — "UltraTech Cement Q2 net profit up 21% in September quarter"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 55.7 — "UltraTech Cement Q2 net profit up 21% in September quarter"
- TECH (Bio-Techne Corp) score 55.7 — "UltraTech Cement Q2 net profit up 21% in September quarter"
- COIN (Coinbase Global, Inc.) score 52.1 — "Global Market Today: Asian stocks decline in break from US chip rally"
- OHI (Omega Healthcare Investors, In) score 50.2 — "OPENAI SEEKS $1.4 TRILLION VALUATION AHEAD OF ANTHROPIC IPO OpenAI is reportedly racing to"
- CHKP (Check Point Software Technolog) score 39.8 — "Stock Market Holiday 2026: Is stock market closed today for Dussehra? Check remaining holi"
- BOND (PIMCO Active Bond Exchange-Tra) score 34.9 — "Maharajah Bonds gain investor appeal with TDS exemption"
- TGT (Target Corporation) score 34.3 — "Top stocks to buy for short term: Just Dial, BSE, Orient Hotels - Target price, stop-loss "
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 22.2 — "Oil Price Today (October 20): Crude oil nears $110 again as fresh attacks outweigh easing "
- RS (Reliance, Inc.) score 22.1 — "Reliance Jio IPO review: Apply or not? Bid now or buy shares post NSE, BSE debut? Check GM"
- 301077.SZ (CHINASTARS) score 20.3 — "Robot Wars – How China Has the Robotics Industry in Its Grip"
- LTH (Life Time Group Holdings, Inc.) score 19.6 — "TRUMP ON ZELENSKYY'S COMMENTS: TIME FOR SOMEONE ELSE TO NEGOTIATE ON BEHALF OF UKRAINE"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 18.3 — "Gold Holds Decline as Energy-Led Inflation Weighs on Rate Path"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 16.0 — "Q2 Results Today Highlights: UltraTech Q2 profit declines q-o-q, Hindustan Zinc, Union Ban"
- SEPN (Septerna, Inc.) score 14.2 — "UltraTech Cement Q2 net profit up 21% in September quarter"
- JIOFIN.BO (Jio Financial Services Limited) score 13.4 — "Dussehra holiday: Indian financial markets to remain closed on Tuesday"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 13.3 — "Q2 Results Today Highlights: UltraTech Q2 profit declines q-o-q, Hindustan Zinc, Union Ban"
- BZ=F (Brent Crude Oil Last Day Finan) score 11.5 — "HEDGE FUNDS DUMP TECH STOCKS AT FASTEST PACE IN A DECADE Goldman Sachs reports that hedge "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.6 — "Tata Group stock to buy on Dussehra 2026 for money gains - Check target, stop loss by Choi"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 10.6 — "Tata Group stock to buy on Dussehra 2026 for money gains - Check target, stop loss by Choi"
- META (Meta) score 10.1 — "Gold price outlook: Yellow metal prices cool 26% from record high: What are Indians buying"
- GS (Goldman Sachs Group, Inc. (The) score 9.8 — "It’s a rough housing market, and Goldman Sachs expects it to get worse"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.2 — "Top stocks to buy for short term: Just Dial, BSE, Orient Hotels - Target price, stop-loss "
- VT (Vanguard Total World Stock Ind) score 7.1 — "Already a hit? Reliance's Jio Platforms gets  ₹8,110 cr from anchor investors; LIC, New Wo"
- NVDA (NVIDIA Corporation) score 6.1 — "DEEPSEEK AND HUAWEI ARE COLLABORATING ON NEW AI CHIP DESIGNS TO CHALLENGE NVIDIA - THE IN "
- JEF (Jefferies Financial Group Inc.) score 5.8 — "ICICI Bank share price target after Q2 results: What are Jefferies, other analysts saying?"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.8 — "Dussehra 2026 special: Top 3 stocks to buy; ICICI Bank, Adani Ports, Reliance Industries |"
- WIT (Wipro Limited) score 3.5 — "What to do with IT stocks? TCS, HCL Tech, Wipro, Infosys, Tech Mahindra — Why experts are "
- DELL (Dell Technologies Inc.) score 1.0 — "Michael Dell Says in Interview That Just-in-Time Manufacturing Provides a Cushion if AI Bo"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.8 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
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