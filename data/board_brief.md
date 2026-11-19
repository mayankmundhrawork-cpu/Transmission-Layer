# Transmission Layer — board brief · 2026-11-19 02:42Z

data as of **2026-11-19** · 97 series · 12 red / 35 amber · 8 events surfaced (30 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 1.0, 4d in regime; vol-pct None, breadth-off 1.0, Markov P(high-vol) 0.024)
- [INVERTED] **safe_haven_gold** — corr20 -0.06, corr60 -0.18, contra nifty_50 corr20=0.36, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.89, corr60 0.85, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.35, corr60 0.2, last shift 2026-09-18. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.08, corr60 0.06, last shift 2026-09-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.95, corr60 -0.91, last shift 2026-09-24. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.12, corr60 -0.01, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.11, corr60 -0.15, last shift 2026-08-12. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.35, corr60 0.31, last shift 2026-07-15. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 0.00011811782483794886)
- **SETUP** aud_usd → usd_cny: leads 1d (ccf -0.269, β -0.0803, p 0.0); driver zc -2.02 → expected 0.079%. Type hit-rate 0.822 (n=2010).
- Track record · residual_reversion: hit-rate **0.51** (n=1158) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.822** (n=2010) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.438** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.36] cross-asset · 5 series ↓
- dow_jones [INDICES]: last 50193.03, z20 -3.43, zc -1.01, resid-z -1.95 [unexplained], 1d -1.12%, |z20|=3.43
- dyn_schd [EQUITIES]: last 34.69, z20 -2.22, zc -1.86, resid-z -2.35 [unexplained], 1d -1.76%, |z20|=2.22
- sp500 [INDICES]: last 7322.28, z20 -2.07, zc -0.21, resid-z -0.77 [quiet], 1d -0.25%, |z20|=2.07
- russell_2000 [INDICES]: last 2714.66, z20 -2.01, zc 0.34, resid-z 1.13 [quiet], 1d 0.47%, |z20|=2.01
- dyn_nvda [EQUITIES]: last 150.87, z20 -1.89, zc -0.89, resid-z 1.01 [quiet], 1d -2.95%, 1y-pct=0
- **Mechanism**: cross-asset · 5 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_rs (co-move) — not yet - watch; rho 0.593 vs russell_2000, historically leads by 4d
- Watch next: dax (co-move) — not yet - watch; rho 0.602 vs dow_jones
- Watch next: dyn_ohi (co-move) — not yet - watch; rho 0.555 vs dyn_schd
- Source: ‘Nvidia’s turmoil has me spooked’: Should I sell my stocks and buy real estate — or ride out the storm? — MarketWatch Top, 2026-11-19. https://www.marketwatch.com/story/nvidia-spooked-me-should-i-sell-my-stocks-or-ride-out-the-market-turmoil-560583c6?mod=mw_rss_topstories
- Source: Nvidia’s booming demand is ‘hard to ignore,’ but these four questions loom over the stock — MarketWatch Top, 2026-11-18. https://www.marketwatch.com/story/what-wall-street-analysts-are-now-saying-after-nvidias-beat-and-raise-quarter-9311c85d?mod=mw_rss_topstories
- Source: What’s next for the AI trade after Nvidia’s blowout results are met with a shrug — MarketWatch Top, 2026-11-18. https://www.marketwatch.com/story/whats-next-for-the-ai-trade-after-nvidias-blowout-results-are-met-with-a-shrug-853c7abe?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-22 (d=0.91), 2025-05-16 (d=1.21)

### [RED 6.92] usd_inr ↓
- usd_inr [FX]: last 93.44, z20 -1.92, zc -0.09, resid-z -0.73 [quiet], 1d -0.04%, 20d range extreme; |z20|=1.92
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_havells_ns (rho -0.451 via usd_inr, z 0.87, quiet); dyn_indianb_ns (rho -0.439 via usd_inr, z 1.41, reacted); nifty_it (rho -0.431 via usd_inr, z -2.4, reacted); dyn_tataelxsi_ns (rho -0.375 via usd_inr, z -1.96, reacted); dyn_bajfinance_ns (rho -0.357 via usd_inr, z 1.15, reacted)
- **India receivers**: dyn_havells_ns (rho -0.451, z 0.87); dyn_indianb_ns (rho -0.439, z 1.41); nifty_it (rho -0.431, z -2.4); dyn_tataelxsi_ns (rho -0.375, z -1.96)
- Source: Rupee rises 7 paise to close at 93.44 against US dollar — BusinessLine Mkts, 2026-11-18. https://www.thehindubusinessline.com/markets/forex/rupee-rises-7-paise-to-close-at-9344-against-us-dollar/article71715511.ece
- Source: Rupee ends flat after hitting seven-month high as firmer dollar offsets inflows — ET Markets, 2026-11-18. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-ends-flat-after-hitting-seven-month-high-as-firmer-dollar-offsets-inflows/articleshow/135959732.cms
- Source: Rupee appreciates for third consecutive day as oil dips — BusinessLine Mkts, 2026-11-18. https://www.thehindubusinessline.com/markets/forex/rupee-appreciates-for-third-consecutive-day-as-oil-dips/article71714723.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [RED 5.77] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 3742.90, z20 -2.45, zc 0.01, resid-z 0.21 [quiet], 1d 0.03%, |z20|=2.45; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 45.17, z20 -2.30, zc 0.02, resid-z 0.16 [quiet], 1d 0.07%, |z20|=2.30; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 82.87, z20 1.97, zc n/a, resid-z n/a [quiet], 1d -0.04%, |z20|=1.97; 1y-pct=99
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.537 via comex_gold, z 0.07, quiet); dyn_karurvysya_ns (rho 0.473 via comex_gold, z 1.46, reacted); nifty_metal (rho 0.436 via comex_silver, z 0.05, quiet); dyn_jiofin_bo (rho 0.416 via comex_gold, z 0.61, quiet); nifty_midcap_100 (rho 0.397 via comex_gold, z 0.93, quiet)
- Watch next: dyn_muthootfin_ns (co-move) — not yet - watch; rho 0.537 vs comex_gold, historically leads by 4d
- **India receivers**: dyn_muthootfin_ns (rho 0.537, z 0.07); dyn_karurvysya_ns (rho 0.473, z 1.46); nifty_metal (rho 0.436, z 0.05); dyn_jiofin_bo (rho 0.416, z 0.61)
- Source: Top stocks to watch today: Coal India, Jio Financial, NALCO, Bharat Forge, Sky Gold, Dalmia Bharat and 7 others in focus — Mint Markets, 2026-11-19. https://www.livemint.com/market/stock-market-news/top-stocks-to-watch-today-coal-india-jio-financial-nalco-bharat-forge-sky-gold-dalmia-bharat-and-7-others-in-focus-11795052380903.html
- Source: Gold recovers from one-year low as markets assess Fed rate outlook — ET Markets, 2026-11-19. https://economictimes.indiatimes.com/markets/commodities/news/gold-recovers-from-one-year-low-as-markets-assess-fed-rate-outlook/articleshow/135975129.cms
- Source: Gold Slumps 3% to Lowest in Over a Year on Hawkish Fed Signals — Mint Markets, 2026-11-18. https://www.livemint.com/market/gold-slumps-3-to-lowest-in-over-a-year-on-hawkish-fed-signals-11795036212650.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 5.44] dyn_blln ↓
- dyn_blln [EQUITIES]: last 91.61, z20 -3.44, zc -1.80, resid-z 0.27 [moved], 1d -6.04%, |z20|=3.44
- **Mechanism**: dyn_blln ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Anthropic IPO set to raise $90.4 billion, could become biggest stock market debut ever — Mint Markets, 2026-11-18. https://www.livemint.com/market/anthropic-ipo-set-to-raise-90-4-billion-could-become-biggest-stock-market-debut-ever-11795025331762.html
- Source: SITUATIONAL AWARENESS PLANS COMEBACK AFTER $20 BILLION AI HEDGE FUND NEARLY COLLAPSED Leopold Aschenbrenner, the 25-year-old founder of Situational Awareness, is reportedly planning a comeback just four months after leveraged AI-stock bets nearly destroyed his hedge fund. Dubbed “Situational Awarene — DeItaone, 2026-11-18. https://t.me/walter_bloomberg/38780
- Source: U.S. 20-YEAR TREASURY AUCTION CLEARS AT 5.459% WITH SOLID DEMAND The U.S. Treasury sold $16 billion in 20-year bonds, with the auction clearing at a 5.459% yield, slightly below the previous auction's 5.469%. The sale recorded a 2.63 bid-to-cover ratio, indicating demand of $2.63 for every $1 offere — DeItaone, 2026-11-18. https://t.me/walter_bloomberg/38777

### [AMBER 5.38] cross-asset · 3 series ↓
- dyn_coin [EQUITIES]: last 110.54, z20 -2.06, zc -0.84, resid-z -0.27 [quiet], 1d -3.90%, |z20|=2.06; 1y-pct=0
- btc_usd [CRYPTO]: last 62616.45, z20 -1.96, zc 0.20, resid-z -1.60 [unexplained], 1d 0.62%, |z20|=1.96
- eth_usd [CRYPTO]: last 1770.09, z20 -1.75, zc 0.12, resid-z -0.80 [quiet], 1d 0.48%, |z20|=1.75
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-10-22 (z-distance 0.46).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Global Market Today: Asian shares mixed as commodity prices tumble — ET Markets, 2026-11-19. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-today-asian-shares-mixed-as-commodity-prices-tumble/articleshow/135974671.cms
- Source: China Gas Upsizes Long-Term LNG Supply with U.S. Venture Global — OilPrice, 2026-11-18. https://oilprice.com/Latest-Energy-News/World-News/China-Gas-Upsizes-Long-Term-LNG-Supply-with-US-Venture-Global.html
- Source: SPCX $APO - SPACEX PLANS $40 BILLION OFF-BALANCE-SHEET AI CHIP FINANCING SpaceX is preparing a $40 billion financing deal arranged by Apollo Global Management to fund AI chips without adding the debt directly to its balance sheet. The financing will use a special-purpose vehicle (SPV), allowing Spac — DeItaone, 2026-11-18. https://t.me/walter_bloomberg/38740
- Historical analogues: 2025-10-22 (d=0.46), 2026-05-22 (d=0.49), 2025-04-10 (d=0.57)

### [AMBER 5.29] fx · 2 series ↓
- gbp_usd [FX]: last 1.31, z20 -2.46, zc -1.31, resid-z 0.19 [quiet], 1d -0.49%, |z20|=2.46; 1y-pct=0
- eur_usd [FX]: last 1.10, z20 -2.33, zc -0.52, resid-z -0.27 [quiet], 1d -0.19%, |z20|=2.33; 1y-pct=0
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.05 vs eur_usd, historically leads by 1d
- Source: GOLD, SILVER AND COPPER PLUNGE AS METALS SELLOFF ACCELERATES Precious and industrial metals extended losses, with futures falling to fresh lows for the year amid a stronger dollar and expectations of persistently high interest rates. Copper plunged 6.1% to $5.62 per pound, pressured by concerns over — DeItaone, 2026-11-18. https://t.me/walter_bloomberg/38776
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [RED 5.17] dyn_inoxindia_ns ↑
- dyn_inoxindia_ns [EQUITIES]: last 2145.00, z20 5.17, zc 2.97, resid-z 2.90 [unexplained], 1d 8.92%, |z20|=5.17
- **Mechanism**: dyn_inoxindia_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-18 (d=0.04), 2025-06-30 (d=0.07)

### [RED 5.05] dxy ↑
- dxy [FX]: last 103.87, z20 2.05, zc 0.00, resid-z -0.42 [quiet], 1d 0.00%, 20d range extreme; |z20|=2.05; 1y-pct=100
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.54 vs dxy, historically leads by 1d
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-10 (d=0.03), 2025-05-14 (d=0.06)

## Watchlist (below surfacing floor)
comex_copper ↓ (4.68), dyn_bac ↓ (4.53), dyn_kaynes_ns ↓ (4.52), dyn_coalindia_ns ↓ (4.02), dyn_tgt ↑ (3.75), natgas ↑ (3.63), wti ↓ (3.54), dyn_lth ↑ (3.41), dyn_eternal_ns ↑ (3.08), ftse_100 ↓ (2.84), dyn_4417_t ↑ (2.73), rates · 2 series ↑ (2.69)

## India macro
- nifty_50: 25227.9492 (1d -0.63%, z20 1.25, flag none)
- nifty_midcap_100: 60974.4492 (1d -1.22%, z20 0.93, flag none)
- usd_inr: 93.4400 (1d -0.04%, z20 -1.92, flag red)
- goi_10y: 7.3800 (1d 4.53%, z20 3.03, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.1400 (1d -5.73%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4169 (1d -0.60%, z20 -1.66, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 81.7 — "China Burns Less Oil and Coal as the Iran War Reshapes Its Energy Mix"
- INOXINDIA.NS (INOX INDIA LIMITED) score 77.0 — "Stock recommendations for 19 November from MarketSmith India"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 75.7 — "Stock recommendations for 19 November from MarketSmith India"
- NVDA (NVIDIA Corporation) score 61.8 — "NVDA - ARM'S RENE APPROACHED BY NVIDIA BOARD IN CEO SEARCH"
- INDIANB.NS (INDIAN BANK) score 58.1 — "Indian shares set to open lower as hawkish Fed minutes weigh"
- BAC (Bank of America Corporation) score 49.9 — "FED'S BARR BACKS FURTHER RATE HIKES AS INFLATION REMAINS TOO HIGH Federal Reserve Governor"
- HDB (HDFC Bank Limited) score 44.4 — "HDFC Life Share Price Highlights: HDFC Life Stock Price History"
- TECHM.NS (TECH MAHINDRA LIMITED) score 43.0 — "The stock market is being rocked by the biggest shake-up in a generation as tech falls beh"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 40.9 — "U.S. MORTGAGE RATES SURGE TO 7.35% AS LOAN DEMAND FALLS The average U.S. 30-year mortgage "
- IDBI.NS (IDBI BANK LIMITED) score 40.9 — "U.S. MORTGAGE RATES SURGE TO 7.35% AS LOAN DEMAND FALLS The average U.S. 30-year mortgage "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 40.9 — "U.S. MORTGAGE RATES SURGE TO 7.35% AS LOAN DEMAND FALLS The average U.S. 30-year mortgage "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.4 — "The stock market is being rocked by the biggest shake-up in a generation as tech falls beh"
- TECH (Bio-Techne Corp) score 39.4 — "The stock market is being rocked by the biggest shake-up in a generation as tech falls beh"
- TGT (Target Corporation) score 34.6 — "Anthropic prices IPO at $83, beating target range in blockbuster AI listing"
- OHI (Omega Healthcare Investors, In) score 31.7 — "Should investors consider the stock of Apollo Micro Systems?"
- 301077.SZ (CHINASTARS) score 26.0 — "US OFFICIAL SAYS PRESIDENT TRUMP WILL HAVE A ONE-ON-ONE MEETING WITH RUSSIAN PRESIDENT PUT"
- COIN (Coinbase Global, Inc.) score 25.4 — "Global Market Today: Asian shares mixed as commodity prices tumble"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.1 — "China Burns Less Oil and Coal as the Iran War Reshapes Its Energy Mix"
- BLLN (BillionToOne, Inc.) score 21.7 — "U.S. 20-YEAR TREASURY AUCTION CLEARS AT 5.459% WITH SOLID DEMAND The U.S. Treasury sold $1"
- CHKP (Check Point Software Technolog) score 20.3 — "GMR Airports, IIFL Finance shares: Top 2 stocks to buy in near term; check target price, s"
- LTH (Life Time Group Holdings, Inc.) score 20.2 — "OPENAI CEO SAM ALTMAN REAFFIRMS IPO PLANS AS ANTHROPIC PREPARES TO GO PUBLIC OpenAI CEO Sa"
- JIOFIN.BO (Jio Financial Services Limited) score 18.5 — "PLAYSTATION: SOME SERVICES ARE EXPERIENCING ISSUES"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 17.2 — "GMR Airports, IIFL Finance shares: Top 2 stocks to buy in near term; check target price, s"
- BOND (PIMCO Active Bond Exchange-Tra) score 14.5 — "U.S. 20-YEAR TREASURY AUCTION CLEARS AT 5.459% WITH SOLID DEMAND The U.S. Treasury sold $1"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 14.0 — "Tata Motors among 5 stocks closing above 200-DMA"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 14.0 — "Tata Motors among 5 stocks closing above 200-DMA"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 12.7 — "GMR Airports, IIFL Finance shares: Top 2 stocks to buy in near term; check target price, s"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 11.9 — "Indoco Remedies share price jumps 13%; pharma stock up over 16% in 2 weeks: Can the rally "
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.1 — "GTA VI FEVER HITS THE US WORKFORCE A Zety survey finds 11% of US workers plan to take time"
- BZ=F (Brent Crude Oil Last Day Finan) score 7.1 — "NVIDIA SHARES EXTEND LOSSES; LAST DOWN 4.2%"
- MS (Morgan Stanley) score 7.1 — "JPMORGAN WARNS LEVERAGED-LOAN DEFAULTS COULD MORE THAN DOUBLE IN 2027 JPMorgan forecasts U"
- META (Meta) score 7.0 — "GOLD, SILVER AND COPPER PLUNGE AS METALS SELLOFF ACCELERATES Precious and industrial metal"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.9 — "Adani Ent Share Price Highlights: Adani Ent. Stock Price History"
- SCHD (Schwab US Dividend Equity ETF) score 5.3 — "Mahanadi Coalfields IPO: Dividend king in the making? What top official says about Coal In"
- GS (Goldman Sachs Group, Inc. (The) score 4.5 — "Goldman Sachs upgrades India to overweight, sets Nifty target of 28,500"
- RS (Reliance, Inc.) score 3.3 — "Reliance, UltraTech, Hyundai Motor shares: Top 3 stocks to buy; check ratings, target pric"
- KAYNES.NS (KAYNES TECHNOLOGY IND LTD) score 3.0 — "Kaynes Technology shares extend losses, fall another 4%; should investors worry about its "
- CRWV (CoreWeave, Inc.) score 2.9 — "CoreWeave’s stock pops — even as Nvidia talks up a ‘disciplined’ approach to financing"
- ETERNAL.NS (ETERNAL LIMITED) score 1.9 — "Eternal among 5 stocks hitting 52-week highs; stock rallies up to 15% in a month"
- COCHINSHIP.NS (COCHIN SHIPYARD LIMITED) score 0.9 — "Cochin Shipyard dividend 2026: Last day to buy today | Check record date, payout amount, h"

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