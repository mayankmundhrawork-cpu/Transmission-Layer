# Transmission Layer — board brief · 2026-10-06 11:14Z

data as of **2026-10-06** · 97 series · 6 red / 35 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.67, 2d in regime; vol-pct 0.612, breadth-off 0.727, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.42, contra nifty_50 corr20=0.02, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.78, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.12, corr60 0.2, last shift 2026-07-09. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.04, corr60 0.12, last shift 2026-08-17. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.77, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.24, corr60 -0.09, last shift 2026-08-17. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.3, corr60 -0.24, last shift 2026-08-17. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.42, corr60 0.19, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 4.04121180963557e-14)
- **SETUP** bovespa → aud_usd: leads 1d (ccf 0.384, β 0.2222, p 0.0); driver zc 2.61 → expected 0.584%. Type hit-rate 0.823 (n=2310).
- **SETUP** dyn_hdb → usd_inr: leads 1d (ccf -0.356, β -0.0892, p 0.0); driver zc -1.54 → expected 0.237%. Type hit-rate 0.823 (n=2310).
- Track record · residual_reversion: hit-rate **0.497** (n=1130) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.823** (n=2310) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.81] bovespa ↑
- bovespa [INDICES]: last 207190.44, z20 10.81, zc 2.61, resid-z 2.06 [unexplained], 1d 7.85%, |z20|=10.81; 1y-pct=100
- **Mechanism**: bovespa ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_stylebaaza_ns (rho -0.432 via bovespa, z -0.62, quiet)
- **India receivers**: dyn_stylebaaza_ns (rho -0.432, z -0.62)
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-12 (d=1.03), 2025-01-30 (d=1.08)

### [RED 7.73] commodities · 2 series ↓
- brent [COMMODITIES]: last 98.31, z20 -1.90, zc -0.94, resid-z 0.37 [quiet], 1d -2.00%, 1-session move -2.00% ≥ 1.5%; |z20|=1.90
- wti [COMMODITIES]: last 87.72, z20 -1.67, zc -0.73, resid-z -0.36 [quiet], 1d -1.91%, 1-session move -1.91% ≥ 1.5%; |z20|=1.67
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dax (inverse) — not yet - watch; rho -0.509 vs brent, historically leads by 5d
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.504 vs brent, historically leads by 5d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.664 vs brent
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.577 vs brent
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.511 vs brent
- Source: China Accelerates Ultra-Deep Drilling to Boost Domestic Oil Supply — OilPrice, 2026-10-06. https://oilprice.com/Latest-Energy-News/World-News/China-Accelerates-Ultra-Deep-Drilling-to-Boost-Domestic-Oil-Supply.html
- Source: World Bank flags oil, El Niño and global market risks to growth — ET Markets, 2026-10-06. https://economictimes.indiatimes.com/markets/us-stocks/news/world-bank-flags-oil-el-nio-and-global-market-risks-to-growth/articleshow/134736490.cms
- Source: Global Market:  Gulf oil flows rebound to 81% of pre-war levels in September — ET Markets, 2026-10-06. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/global-market-gulf-oil-flows-rebound-to-81-of-pre-war-levels-in-september/articleshow/134730619.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [AMBER 6.45] usd_inr ↑
- usd_inr [FX]: last 96.42, z20 1.45, zc 0.18, resid-z 0.23 [quiet], 1d 0.10%, 20d range extreme; 1y-pct=96
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.391 via usd_inr, z 2.35, reacted)
- **India receivers**: dyn_idbi_ns (rho -0.391, z 2.35)
- Source: Rupee hits two-month low on outflows, investors await RBI outcome with hike priced in — ET Markets, 2026-10-06. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-hits-two-month-low-on-outflows-investors-await-rbi-outcome-with-hike-priced-in/articleshow/134737972.cms
- Source: Rupee slips to over 2-month low on portfolio outflows, RBI likely steps in — ET Markets, 2026-10-06. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-slips-to-over-2-month-low-on-portfolio-outflows-rbi-likely-steps-in/articleshow/134725847.cms
- Source: RBI likely steps in to defend rupee and drain excess cash, traders say — BusinessLine Mkts, 2026-10-06. https://www.thehindubusinessline.com/markets/forex/rbi-likely-steps-in-to-defend-rupee-and-drain-excess-cash-traders-say/article71550119.ece
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2025-09-16 (d=0.01)

### [AMBER 5.88] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.63, z20 1.95, zc 0.44, resid-z 0.65 [quiet], 1d 0.36%, |z20|=1.95; 1y-pct=99
- dyn_bond [EQUITIES]: last 86.38, z20 -1.91, zc -0.58, resid-z -0.41 [quiet], 1d -0.18%, 1y-pct=0
- ust_10y [RATES]: last 5.28, z20 1.61, zc 0.72, resid-z 1.07 [quiet], 1d 0.76%, |z20|=1.61; 1y-pct=99
- tips_10y_real [RATES]: last 2.92, z20 1.52, zc 0.69, resid-z 1.03 [quiet], 1d 1.39%, |z20|=1.52; 1y-pct=99
- ust_2y [RATES]: last 4.83, z20 0.82, zc 0.78, resid-z 1.10 [quiet], 1d 1.05%, 1y-pct=98
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.534 vs ust_10y, historically leads by 4d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.528 vs ust_30y
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.521 vs ust_30y
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.507 vs ust_30y
- Source: Should I put my nest egg in a 30-year Treasury bond? — MarketWatch Top, 2026-10-06. https://www.marketwatch.com/story/should-i-put-my-nest-egg-in-a-30-year-treasury-bond-89db6e09?mod=mw_rss_topstories
- Source: How Jefferies is reshuffling its portfolio as soaring bond yields give Nifty bulls sleepless nights — ET Markets, 2026-10-06. https://economictimes.indiatimes.com/markets/stocks/news/how-jefferies-is-reshuffling-its-portfolio-as-soaring-bond-yields-give-nifty-bulls-sleepless-nights/articleshow/134724801.cms
- Source: Global Market: Japan 30-year bond yield hits record high ahead of 10-year auction — ET Markets, 2026-10-06. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japan-30-year-bond-yield-hits-record-high-ahead-of-10-year-auction/articleshow/134722888.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.81] indices · 2 series ↑
- nikkei_225 [INDICES]: last 70773.80, z20 2.98, zc 0.66, resid-z -0.82 [quiet], 1d 1.18%, |z20|=2.98; 1y-pct=98
- taiwan_weighted [INDICES]: last 49754.07, z20 2.41, zc 0.08, resid-z -0.28 [quiet], 1d 0.08%, |z20|=2.41; 1y-pct=100
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.7).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho 0.538 via taiwan_weighted, z -1.3, reacted); nifty_it (rho -0.372 via taiwan_weighted, z -0.88, quiet)
- Watch next: kospi (co-move) — not yet - watch; rho 0.848 vs nikkei_225
- **India receivers**: dyn_bajfinance_ns (rho 0.538, z -1.3); nifty_it (rho -0.372, z -0.88)
- Source: Stock market outlook today, 6 Oct: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Nikkei, Taiwan cues — Mint Markets, 2026-10-06. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-6-oct-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-nikkei-taiwan-cues-11791247193944.html
- Source: Global Market: Japan’s Nikkei jumps 2.5% to 3-month high as AI stocks rally — ET Markets, 2026-10-05. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-jumps-2-5-to-3-month-high-as-ai-stocks-rally/articleshow/134685851.cms
- Historical analogues: 2025-12-30 (d=0.7), 2025-07-11 (d=0.77), 2026-06-09 (d=1.0)

### [AMBER 4.73] rates · 2 series ↑
- ig_oas [RATES]: last 0.85, z20 1.89, zc -0.69, resid-z -0.96 [quiet], 1d -1.16%, |z20|=1.89
- hy_oas [RATES]: last 3.10, z20 1.75, zc -1.61, resid-z -2.96 [unexplained], 1d -4.32%, |z20|=1.75
- **Mechanism**: rates · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_policybzr_ns (rho -0.476 via ig_oas, z -1.32, reacted); nifty_midcap_100 (rho -0.452 via ig_oas, z -1.14, reacted)
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.522 vs hy_oas
- Watch next: dax (inverse) — not yet - watch; rho -0.507 vs hy_oas
- **India receivers**: dyn_policybzr_ns (rho -0.476, z -1.32); nifty_midcap_100 (rho -0.452, z -1.14)
- Source: Why junk bonds deliver equity-like returns but with far inferior volatility, explains Saurabh Mukherjea — ET Markets, 2026-10-06. https://economictimes.indiatimes.com/markets/bonds/why-junk-bonds-deliver-equity-like-returns-but-with-far-inferior-volatility-explains-saurabh-mukherjea/articleshow/134727904.cms
- Source: HIGH YIELDS FORCE MUNI BORROWERS TO DELAY REFINANCINGS Roughly $6 billion of municipal bond refinancing deals are on hold or delayed as elevated yields erase potential savings for borrowers. Benchmark 30-year muni yields recently hit 5.26%, the highest since at least 2011. New Jersey postponed a pla — DeItaone, 2026-10-05. https://t.me/walter_bloomberg/36647
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-01 (d=0.48), 2024-11-04 (d=0.56)

### [AMBER 4.67] indices · 2 series ↑
- sp500 [INDICES]: last 7774.22, z20 1.84, zc 1.04, resid-z 0.67 [quiet], 1d 0.67%, |z20|=1.84; 1y-pct=99
- nasdaq_100 [INDICES]: last 31078.13, z20 1.84, zc 0.98, resid-z -0.27 [quiet], 1d 0.88%, |z20|=1.84; 1y-pct=100
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.956 vs sp500
- Watch next: vix (inverse) — not yet - watch; rho -0.756 vs sp500, historically leads by 4d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.869 vs sp500
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.805 vs sp500
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.648 vs sp500
- Source: The S&P 500 is facing rate chaos and narrow breadth. Why one Goldman Sachs insider is still bullish on stocks. — MarketWatch Top, 2026-10-06. https://www.marketwatch.com/story/the-s-p-500-is-facing-rate-chaos-and-narrow-breadth-why-one-goldman-sachs-insider-is-still-bullish-on-stocks-84a20206?mod=mw_rss_topstories
- Source: Stock market outlook today, 6 Oct: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Nikkei, Taiwan cues — Mint Markets, 2026-10-06. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-6-oct-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-nikkei-taiwan-cues-11791247193944.html
- Source: US stocks: Nasdaq gains 1% at close as investors focus on earnings — ET Markets, 2026-10-05. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-nasdaq-dow-close-1-higher-as-investors-focus-on-earnings/articleshow/134716734.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-07 (d=0.06), 2026-05-15 (d=0.07)

### [AMBER 4.45] dyn_nvda ↑
- dyn_nvda [EQUITIES]: last 239.11, z20 2.45, zc 0.66, resid-z -0.19 [quiet], 1d 2.21%, |z20|=2.45; 1y-pct=100
- **Mechanism**: dyn_nvda ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.603 vs dyn_nvda, historically leads by 4d
- Watch next: vix (inverse) — not yet - watch; rho -0.572 vs dyn_nvda, historically leads by 4d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.562 vs dyn_nvda, historically leads by 1d
- Watch next: dyn_dell (co-move) — not yet - watch; rho 0.522 vs dyn_nvda, historically leads by 1d
- Source: The case for Nvidia’s stock to march even higher after clinching its first record high in months — MarketWatch Top, 2026-10-05. https://www.marketwatch.com/story/the-case-for-nvidias-stock-to-march-even-higher-after-clinching-its-first-record-high-in-months-2bb5a937?mod=mw_rss_topstories
- Source: AI stock Nvidia stock gets target upgrade from BNP Paribas; 47% further upside seen by experts - check revised price — Mint Markets, 2026-10-05. https://www.livemint.com/market/stock-market-news/ai-stock-nvidia-stock-gets-target-upgrade-from-bnp-paribas-47-further-upside-seen-by-experts-check-revised-price-11791214034610.html
- Source: Nvidia still 'the one' for AI? BNP Paribas raises target to $345, sees up to 47% upside — ET Markets, 2026-10-05. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/nvidia-still-the-one-for-ai-bnp-paribas-raises-target-to-345-sees-up-to-47-upside/articleshow/134698952.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-24 (d=0.03), 2026-05-04 (d=0.03)

## Watchlist (below surfacing floor)
dyn_ohi ↓ (4.37), dyn_4417_t ↑ (4.27), dyn_techm_ns ↓ (4.24), dyn_coalindia_ns ↓ (4.22), eur_usd ↓ (3.72), usd_brl ↓ (3.69), dyn_tech ↑ (3.51), dyn_hdb ↓ (3.41), gold_silver_ratio ↑ (3.38), dyn_policybzr_ns ↓ (3.32), dyn_jiofin_bo ↓ (3.28), usd_cny ↓ (3.12)

## India macro
- nifty_50: 22776.0996 (1d 0.98%, z20 -1.08, flag amber)
- nifty_midcap_100: 59761.7500 (1d 1.07%, z20 -1.14, flag none)
- usd_inr: 96.4200 (1d 0.10%, z20 1.45, flag amber)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6239 (1d 0.09%, z20 -1.05, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI MPC decision T-1d · AMFI SIP / MF flows T-2d · RBI Weekly Statistical Supplement T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 81.9 — "India bonds seen boxed in narrow range, all eyes on RBI verdict"
- COALINDIA.NS (COAL INDIA LTD) score 80.8 — "SAUDI-LED COALITION SAYS DESTROYED SANAA MISSILE LAUNCHER: SPA"
- INDIANB.NS (INDIAN BANK) score 78.9 — "World Bank warns of AI concentration risks as it lifts East Asia and Pacific growth outloo"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 78.8 — "India bonds seen boxed in narrow range, all eyes on RBI verdict"
- BAC (Bank of America Corporation) score 62.3 — "World Bank warns of AI concentration risks as it lifts East Asia and Pacific growth outloo"
- HDB (HDFC Bank Limited) score 59.5 — "World Bank warns of AI concentration risks as it lifts East Asia and Pacific growth outloo"
- IDBI.NS (IDBI BANK LIMITED) score 57.2 — "World Bank warns of AI concentration risks as it lifts East Asia and Pacific growth outloo"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 57.2 — "World Bank warns of AI concentration risks as it lifts East Asia and Pacific growth outloo"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 57.2 — "World Bank warns of AI concentration risks as it lifts East Asia and Pacific growth outloo"
- COIN (Coinbase Global, Inc.) score 50.2 — "Global Market: Japan 30-year bond yield hits record high ahead of 10-year auction"
- BOND (PIMCO Active Bond Exchange-Tra) score 48.1 — "India bonds seen boxed in narrow range, all eyes on RBI verdict"
- OHI (Omega Healthcare Investors, In) score 43.3 — "What actually makes a stock 'cheap'? With markets under pressure, analysts share how inves"
- TECHM.NS (TECH MAHINDRA LIMITED) score 40.6 — "Why are Kotak Mahindra Bank shares up 3.7%? Strong Q2 loan, deposit data"
- TGT (Target Corporation) score 34.9 — "Vedanta vs Vedanta Iron and Steel vs Vedanta Aluminium Metal vs Hindustan Zinc: Which stoc"
- CHKP (Check Point Software Technolog) score 34.6 — "Acme Universal Safezone 9 debuts 42% premium on BSE SME; Pind Hospitality opens at 20% dis"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 32.8 — "AI OPTIMISM OVERRIDES RISING BOND YIELDS Tech stocks are rallying even as bond yields clim"
- TECH (Bio-Techne Corp) score 32.8 — "AI OPTIMISM OVERRIDES RISING BOND YIELDS Tech stocks are rallying even as bond yields clim"
- LTH (Life Time Group Holdings, Inc.) score 27.4 — "China tried 3 times to talk crime families out of scam business in Myanmar: state media"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 24.5 — "World Bank Warns Asia Is Running Out of Money to Fight Energy Shock"
- SEPN (Septerna, Inc.) score 23.0 — "IEX logs 10.4% growth in electricity trade volume to 12.2 billion units in Sept"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 20.0 — "Mutual Funds', FPI favourite Tata Group stock hits upper circuit after Q2 update - Can it "
- 301077.SZ (CHINASTARS) score 16.1 — "TRUMP: CHINA WILL BE DOUBLING UP WHAT THEY’RE BUYING"
- BZ=F (Brent Crude Oil Last Day Finan) score 15.4 — "Why Kotak Mahindra Bank shares are outperforming Nifty 50 and Bank Nifty in the last two m"
- JIOFIN.BO (Jio Financial Services Limited) score 10.1 — "TREASURY YIELDS SURGE TO FRESH 24-YEAR HIGHS Treasuries sold off sharply, pushing the 10-y"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.1 — "BOFA: ACTIVE FUNDS STRUGGLE AS MEGACAPS DOMINATE Just 44% of large-cap active funds beat t"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 8.4 — "Piramal Finance directors okay ₹1,750-cr preferential allotment of warrants to promoter gr"
- JEF (Jefferies Financial Group Inc.) score 8.4 — "Jefferies, Nomura and  Macquarie initiate coverage on 5 stocks with up to 30% upside poten"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 8.2 — "Mutual Funds', FPI favourite Tata Group stock hits upper circuit after Q2 update - Can it "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 8.2 — "Mutual Funds', FPI favourite Tata Group stock hits upper circuit after Q2 update - Can it "
- VT (Vanguard Total World Stock Ind) score 7.2 — "World Bank warns of AI concentration risks as it lifts East Asia and Pacific growth outloo"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.2 — "Adani Power gains 2% after signing pact for 770-MW hydropower project in Bhutan"
- META (Meta) score 6.6 — "Vedanta vs Vedanta Iron and Steel vs Vedanta Aluminium Metal vs Hindustan Zinc: Which stoc"
- GS (Goldman Sachs Group, Inc. (The) score 5.8 — "The S&P 500 is facing rate chaos and narrow breadth. Why one Goldman Sachs insider is stil"
- POLICYBZR.NS (PB FINTECH LIMITED) score 5.8 — "PB Fintech extends losing streak to 7 sessions, stock hits 32-month low"
- NVDA (NVIDIA Corporation) score 5.8 — "The case for Nvidia’s stock to march even higher after clinching its first record high in "
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 5.8 — "Value retail stocks slide on cautious consumer spending"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.4 — "RBI MPC meeting Oct 2026: Why TCS, HDFC Bank, ICICI Lombard, Coal India shares may gain if"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 4.0 — "Piramal Finance directors okay ₹1,750-cr preferential allotment of warrants to promoter gr"
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