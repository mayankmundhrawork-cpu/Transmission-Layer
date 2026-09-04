# Transmission Layer — board brief · 2026-09-04 22:21Z

data as of **2026-09-04** · 98 series · 7 red / 37 amber · 8 events surfaced (30 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.213, 1d in regime; vol-pct 0.131, breadth-off 0.294, Markov P(high-vol) 0.018)
- [INVERTED] **safe_haven_gold** — corr20 -0.46, corr60 -0.41, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.88, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.07, corr60 0.35, last shift 2026-07-08. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.17, corr60 0.05, last shift 2026-06-09. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.79, corr60 -0.84, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.16, corr60 -0.08, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.34, corr60 -0.16, last shift 2026-06-30. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.02, corr60 0.22, last shift 2026-07-16. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 90** scanned series survive multiplicity control (effective p ≤ 0.0018085103996448026)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.502** (n=1127) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.828** (n=1985) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.48] usd_jpy ↓
- usd_jpy [FX]: last 156.22, z20 -5.48, zc -3.13, resid-z -4.54 [unexplained], 1d -1.70%, |z20|=5.48
- **Mechanism**: usd_jpy ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: eur_usd (inverse) — not yet - watch; rho -0.547 vs usd_jpy
- Watch next: kospi (inverse) — not yet - watch; rho -0.509 vs usd_jpy
- Source: Dollar Posts Weekly Loss as Yen Jumps Amid Shifting Rate Bets — Mint Markets, 2026-09-04. https://www.livemint.com/market/dollar-posts-weekly-loss-as-yen-jumps-amid-shifting-rate-bets-11788559180077.html
- Source: Global Market: JGB yields extend fall as stronger yen, hawkish BOJ outlook lift sentiment — ET Markets, 2026-09-04. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-jgb-yields-extend-fall-as-stronger-yen-hawkish-boj-outlook-lift-sentiment/articleshow/133753277.cms
- Source: Yen Rallies as Intervention, BOJ Rate Risk Weigh on Traders — Mint Markets, 2026-09-03. https://www.livemint.com/market/yen-rallies-as-intervention-boj-rate-risk-weigh-on-traders-11788476981657.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2024-11-08 (d=0.01)

### [AMBER 5.26] cross-asset · 4 series ↑
- ust_10y [RATES]: last 4.77, z20 1.59, zc -0.43, resid-z 0.29 [quiet], 1d -0.42%, |z20|=1.59; 1y-pct=99
- dyn_bond [EQUITIES]: last 90.04, z20 -1.49, zc -0.03, resid-z -0.38 [quiet], 1d -0.01%, 1y-pct=1
- ust_2y [RATES]: last 4.34, z20 1.48, zc -0.89, resid-z -0.06 [quiet], 1d -1.14%, 1y-pct=98
- ust_30y [RATES]: last 5.25, z20 0.47, zc -0.48, resid-z -0.10 [quiet], 1d -0.38%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: tips_10y_real (co-move) — not yet - watch; rho 0.858 vs ust_10y
- Watch next: eur_usd (co-move) — not yet - watch; rho 0.527 vs ust_10y, historically leads by 1d
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.524 vs dyn_bond, historically leads by 3d
- Watch next: ust_2s10s (inverse) — not yet - watch; rho -0.506 vs ust_2y, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.506 vs dyn_bond
- Source: INFLATION TAKES CENTER STAGE AFTER STRONG JOBS REPORT BlackRock’s Jeff Rosenberg says strong August jobs data shifts attention to next week’s CPI report and the Fed’s September rate decision. Payrolls rose 162,000, beating forecasts and pushing Treasury yields higher. Rosenberg expects the Fed to ho — DeItaone, 2026-09-04. https://t.me/walter_bloomberg/35476
- Source: Pulse of the Street: US bond yields, interest rate jitters drag Indian equities lower this week — Mint Markets, 2026-09-04. https://www.livemint.com/market/stock-market-news/indian-stock-markets-us-bond-yields-interest-rate-crude-oil-price-11788527556882.html
- Source: Is the stock market open on Labor Day? What about bond trading? Will the post office deliver mail? — MarketWatch Top, 2026-09-04. https://www.marketwatch.com/story/is-the-stock-market-open-on-labor-day-does-the-post-office-deliver-mail-6d58fd77?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-11 (d=0.3), 2025-05-08 (d=0.36)

### [RED 4.99] dyn_pcjeweller_ns ↑
- dyn_pcjeweller_ns [EQUITIES]: last 11.99, z20 2.99, zc 4.07, resid-z 4.50 [unexplained], 1d 13.97%, |z20|=2.99
- **Mechanism**: dyn_pcjeweller_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: PC Jeweller clears debt to one more bank, nears debt-free status — BusinessLine Mkts, 2026-09-03. https://www.thehindubusinessline.com/markets/gold/pc-jeweller-clears-debt-to-one-more-bank-nears-debt-free-status/article71423219.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-01-07 (d=0.32), 2025-02-06 (d=0.36)

### [AMBER 4.79] commodities · 2 series ↑
- wti [COMMODITIES]: last 91.22, z20 1.96, zc -0.04, resid-z -0.21 [quiet], 1d -0.09%, |z20|=1.96
- brent [COMMODITIES]: last 95.83, z20 1.73, zc 0.14, resid-z -0.13 [quiet], 1d 0.32%, |z20|=1.73
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.664 vs wti
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.517 vs wti
- Source: BLM Moves to Fast-Track Oil Permits in Alaska Petroleum Reserve — OilPrice, 2026-09-04. https://oilprice.com/Latest-Energy-News/World-News/BLM-Moves-to-Fast-Track-Oil-Permits-in-Alaska-Petroleum-Reserve.html
- Source: Bessent Sees Oil as Low as $40 Post-Iran War, Taking Yields Down — Mint Markets, 2026-09-04. https://www.livemint.com/market/bessent-sees-oil-as-low-as-40-post-iran-war-taking-yields-down-11788548753614.html
- Source: Citadel Eyes U.S. Shale as Oil Trading Moves Closer to the Wellhead — OilPrice, 2026-09-04. https://oilprice.com/Latest-Energy-News/World-News/Citadel-Eyes-US-Shale-as-Oil-Trading-Moves-Closer-to-the-Wellhead.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 4.61] dyn_icicigi_bo ↓
- dyn_icicigi_bo [EQUITIES]: last 1510.00, z20 -2.61, zc -0.18, resid-z -0.02 [quiet], 1d -0.26%, |z20|=2.61; 1y-pct=0
- **Mechanism**: dyn_icicigi_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Eternal, ICICI Bank, 5 other largecap stocks with upside potential of up to 40%. Do you own any? — ET Markets, 2026-09-04. https://economictimes.indiatimes.com/markets/stocks/news/eternal-icici-bank-5-other-largecap-stocks-with-upside-potential-of-up-to-40-do-you-own-any/slideshow/133751438.cms
- Source: Explained: What $127 billion FCNR(B) inflows mean for ICICI Bank, HDFC Bank, other bank stocks — ET Markets, 2026-09-03. https://economictimes.indiatimes.com/markets/stocks/news/explained-what-127-billion-fcnrb-inflows-mean-for-icici-bank-hdfc-bank-other-bank-stocks/articleshow/133725930.cms
- Source: HDFC Bank is losing ground as Nifty’s top stock while ICICI Bank gains — BusinessLine Mkts, 2026-09-03. https://www.thehindubusinessline.com/markets/hdfc-bank-is-losing-ground-as-niftys-top-stock-while-icici-bank-gains/article71422302.ece
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.0), 2025-05-30 (d=0.03)

### [RED 4.58] dyn_dell ↑
- dyn_dell [EQUITIES]: last 523.99, z20 2.58, zc 0.19, resid-z 0.25 [quiet], 1d 1.47%, |z20|=2.58; 1y-pct=100
- **Mechanism**: dyn_dell ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_coalindia_ns (rho 0.461 via dyn_dell, z 1.41, reacted); nifty_it (rho -0.44 via dyn_dell, z -0.58, quiet)
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.542 vs dyn_dell, historically leads by 5d
- **India receivers**: dyn_coalindia_ns (rho 0.461, z 1.41); nifty_it (rho -0.44, z -0.58)
- Source: Dell’s AI Boom: $95 billion backlog reshapes growth outlook — ET Markets, 2026-09-03. https://economictimes.indiatimes.com/markets/us-stocks/news/dells-ai-boom-95-billion-backlog-reshapes-growth-outlook/slideshow/133726366.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-08 (d=0.18), 2025-10-01 (d=0.3)

### [AMBER 4.36] cross-asset · 3 series ↑
- vix [INDICES]: last 14.52, z20 -1.04, zc 0.17, resid-z n/a [quiet], 1d 1.40%, 1y-pct=5
- dyn_vt [EQUITIES]: last 161.71, z20 0.99, zc -0.04, resid-z -0.82 [quiet], 1d -0.03%, 1y-pct=98
- sp500 [INDICES]: last 7717.81, z20 0.15, zc -0.49, resid-z 1.12 [quiet], 1d -0.39%, 1y-pct=95
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-27 (z-distance 0.14).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.646 vs vix, historically leads by 5d
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.612 vs vix, historically leads by 1d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.654 vs vix
- Watch next: dax (co-move) — not yet - watch; rho 0.526 vs dyn_vt
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.505 vs dyn_vt
- Source: Bloom Energy was just named to the S&P 500. These other stocks are joining the index as well. — MarketWatch Top, 2026-09-04. https://www.marketwatch.com/story/s-p-500-changes-are-coming-soon-these-stocks-could-be-named-to-the-index-today-2d0d7c14?mod=mw_rss_topstories
- Source: TRUMP CALLS FOR LOWER RATES AFTER JOBS BEAT President Trump hailed the addition of 162,000 U.S. jobs in August, saying the figure smashed expectations. He urged the Federal Reserve to cut interest rates, arguing America’s stronger economy deserves the world’s lowest rates. Trump also threatened to h — DeItaone, 2026-09-04. https://t.me/walter_bloomberg/35477
- Source: Wall Street mixed after stronger-than-expected jobs data — Mint Markets, 2026-09-04. https://www.livemint.com/market/wall-street-mixed-after-stronger-than-expected-jobs-data-11788529451652.html
- Historical analogues: 2025-08-27 (d=0.14), 2025-10-23 (d=0.17), 2025-10-31 (d=0.17)

### [AMBER 3.9] dyn_nvda ↑
- dyn_nvda [EQUITIES]: last 230.35, z20 1.90, zc 0.26, resid-z -0.32 [quiet], 1d 0.83%, 1y-pct=99
- **Mechanism**: dyn_nvda ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_inoxindia_ns (rho 0.381 via dyn_nvda, z 2.51, reacted); midcap_largecap_ratio (rho 0.361 via dyn_nvda, z 0.47, quiet)
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.628 vs dyn_nvda, historically leads by 4d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.596 vs dyn_nvda, historically leads by 4d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.591 vs dyn_nvda, historically leads by 1d
- **India receivers**: dyn_inoxindia_ns (rho 0.381, z 2.51); midcap_largecap_ratio (rho 0.361, z 0.47)
- Source: Think of Nvidia’s $13 billion deal for Hugging Face as a form of ‘health insurance’ — MarketWatch Top, 2026-09-04. https://www.marketwatch.com/story/think-of-nvidias-13-billion-deal-for-hugging-face-as-a-form-of-health-insurance-04c37535?mod=mw_rss_topstories
- Source: NVDA - NVIDIA: NEEDHAM STAYS BULLISH AFTER $12.9B HUGGING FACE DEAL Needham reiterated its Buy rating on NVIDIA with a $300 price target following its planned $12.93B acquisition of Hugging Face. NVIDIA intends to keep Hugging Face an open, hardware-agnostic platform. The deal includes roughly $11.9 — DeItaone, 2026-09-04. https://t.me/walter_bloomberg/35461
- Source: Nvidia takes back control of the AI trade as Big Tech nears record highs — MarketWatch Top, 2026-09-03. https://www.marketwatch.com/story/nvidia-takes-back-control-of-the-ai-trade-as-big-tech-nears-record-highs-c0dfed9d?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-24 (d=0.03), 2026-05-04 (d=0.03)

## Watchlist (below surfacing floor)
nifty_50 ↓ (3.78), usd_inr ↓ (3.64), natgas ↑ (3.59), gold_silver_ratio ↓ (3.53), dyn_havells_ns ↓ (3.49), midcap_largecap_ratio ↑ (3.47), dyn_tech ↑ (3.1), usd_cny ↓ (2.78), fx · 2 series ↑ (2.56), dyn_atherenerg_ns ↑ (2.56), dyn_inoxindia_ns ↑ (2.51), dyn_heromotoco_ns ↓ (2.22)

## India macro
- nifty_50: 23897.6992 (1d 0.10%, z20 -1.78, flag amber)
- nifty_midcap_100: 63081.2500 (1d -0.24%, z20 -2.06, flag amber)
- usd_inr: 94.4800 (1d -0.01%, z20 -1.64, flag amber)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6396 (1d -0.35%, z20 0.47, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 83.1 — "Skewed fertiliser use continues in India as farmers buy more urea"
- COALINDIA.NS (COAL INDIA LTD) score 81.8 — "Skewed fertiliser use continues in India as farmers buy more urea"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 80.5 — "Skewed fertiliser use continues in India as farmers buy more urea"
- INDIANB.NS (INDIAN BANK) score 77.5 — "MORGAN STANLEY: FED TO HOLD DESPITE WARSH’S HAWKISH TONE Morgan Stanley expects the Fed to"
- BAC (Bank of America Corporation) score 66.6 — "TRUMP CALLS FOR LOWER RATES AFTER JOBS BEAT President Trump hailed the addition of 162,000"
- HDB (HDFC Bank Limited) score 59.3 — "MORGAN STANLEY: FED TO HOLD DESPITE WARSH’S HAWKISH TONE Morgan Stanley expects the Fed to"
- COIN (Coinbase Global, Inc.) score 57.8 — "Global Market: European shares edge lower as investors await US jobs data"
- IDBI.NS (IDBI BANK LIMITED) score 56.8 — "MORGAN STANLEY: FED TO HOLD DESPITE WARSH’S HAWKISH TONE Morgan Stanley expects the Fed to"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 56.8 — "MORGAN STANLEY: FED TO HOLD DESPITE WARSH’S HAWKISH TONE Morgan Stanley expects the Fed to"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 56.8 — "MORGAN STANLEY: FED TO HOLD DESPITE WARSH’S HAWKISH TONE Morgan Stanley expects the Fed to"
- BOND (PIMCO Active Bond Exchange-Tra) score 55.6 — "Pulse of the Street: US bond yields, interest rate jitters drag Indian equities lower this"
- CHKP (Check Point Software Technolog) score 43.4 — "PTC India, Coal India to REC: Top 10 dividend stocks | One beats PPF interest rate — check"
- OHI (Omega Healthcare Investors, In) score 40.8 — "Micron is doubling down on AI memory chips. That could pay off big time for investors."
- TECHM.NS (TECH MAHINDRA LIMITED) score 38.2 — "Can Big Tech’s $1-trillion AI bet pay off? Jefferies explains why it remains bullish"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 38.0 — "Can Big Tech’s $1-trillion AI bet pay off? Jefferies explains why it remains bullish"
- TECH (Bio-Techne Corp) score 38.0 — "Can Big Tech’s $1-trillion AI bet pay off? Jefferies explains why it remains bullish"
- LTH (Life Time Group Holdings, Inc.) score 33.4 — "Micron is doubling down on AI memory chips. That could pay off big time for investors."
- 301077.SZ (CHINASTARS) score 26.1 — "How The U.S. Fell Behind China On Nuclear Power"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 23.7 — "Bloom Energy was just named to the S&P 500. These other stocks are joining the index as we"
- PCJEWELLER.NS (PC JEWELLER LTD) score 17.0 — "Priority Jewels IPO listing today: Will the jewellery maker deliver gains? Here's what GMP"
- NVDA (NVIDIA Corporation) score 15.8 — "NVDA - NVIDIA: NEEDHAM STAYS BULLISH AFTER $12.9B HUGGING FACE DEAL Needham reiterated its"
- JIOFIN.BO (Jio Financial Services Limited) score 15.5 — "US JOBS BLOW PAST EXPECTATIONS 🔸 August Nonfarm Payrolls: +162K vs +55K expected — a major"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 13.6 — "Retail investors raise stakes in 10 stocks for two straight quarters; shares rally up to 8"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.5 — "SEBI goes after Hindenburg, others in Adani case"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 10.3 — "PTC India, Coal India to REC: Top 10 dividend stocks | One beats PPF interest rate — check"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.1 — "Market wrap:  RIL,Tata Steel, Bharti Airtel, HCL Tech top gainers and losers on Nifty and "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 10.0 — "Market wrap:  RIL,Tata Steel, Bharti Airtel, HCL Tech top gainers and losers on Nifty and "
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.1 — "Bloom Energy was just named to the S&P 500. These other stocks are joining the index as we"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 8.5 — "Bajaj Finance Share Price Live Updates: Bajaj Finance Price Decline Report"
- VT (Vanguard Total World Stock Ind) score 8.2 — "TRUMP CALLS FOR LOWER RATES AFTER JOBS BEAT President Trump hailed the addition of 162,000"
- MS (Morgan Stanley) score 8.0 — "MORGAN STANLEY: FED TO HOLD DESPITE WARSH’S HAWKISH TONE Morgan Stanley expects the Fed to"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 7.2 — "JM Financial initiates coverage on OnEMI Technology with Buy call, sees 28% upside"
- META (Meta) score 5.7 — "Gold vs Silver: Which precious metal offers a better bet for investors after the recent co"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.4 — "Eternal, ICICI Bank, 5 other largecap stocks with upside potential of up to 40%. Do you ow"
- DELL (Dell Technologies Inc.) score 3.7 — "Dell’s AI Boom: $95 billion backlog reshapes growth outlook"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 2.0 — "Lenskart shares to rally 40%? Nomura initiates coverage with Buy, says its growth journey "
- HEROMOTOCO.NS (HERO MOTOCORP LIMITED) score 1.7 — "August sales: Hero MotoCorp’s weak show no reason to ring alarm bells on auto sector slowd"
- DKS (Dick's Sporting Goods Inc) score 0.6 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- MRNA (Moderna, Inc.) score 0.5 — "Can Wolfe’s upgrade push Moderna stock higher?"
- VOLTAS.NS (VOLTAS LTD) score 0.1 — "Voltas reported strong growth in June quarter, but failed to impress"

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