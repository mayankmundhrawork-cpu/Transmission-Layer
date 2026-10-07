# Transmission Layer — board brief · 2026-10-07 00:52Z

data as of **2026-10-07** · 97 series · 5 red / 34 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_ON** (score 0.333, 1d in regime; vol-pct None, breadth-off 0.333, Markov P(high-vol) 0.015)
- [INVERTED] **safe_haven_gold** — corr20 -0.4, corr60 -0.42, contra nifty_50 corr20=0.03, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.82, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.13, corr60 0.2, last shift 2026-07-09. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.04, corr60 0.12, last shift 2026-08-24. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.77, corr60 -0.77, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.23, corr60 -0.09, last shift 2026-08-17. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.3, corr60 -0.24, last shift 2026-08-17. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.43, corr60 0.19, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 1.1604051053382136e-12)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.497** (n=1132) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.82** (n=2236) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 6.35] usd_inr ↑
- usd_inr [FX]: last 96.36, z20 1.35, zc 0.03, resid-z -0.22 [quiet], 1d 0.02%, 20d range extreme; 1y-pct=96
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.405 via usd_inr, z 2.35, reacted); dyn_karurvysya_ns (rho -0.388 via usd_inr, z -0.52, quiet)
- **India receivers**: dyn_idbi_ns (rho -0.405, z 2.35); dyn_karurvysya_ns (rho -0.388, z -0.52)
- Source: Rupee loses 13 paise to close at 96.42 per US dollar — ET Markets, 2026-10-06. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-loses-13-paise-to-close-at-96-42-per-us-dollar/articleshow/134744262.cms
- Source: Rupee slips to over two-month low ahead of RBI policy decision — BusinessLine Mkts, 2026-10-06. https://www.thehindubusinessline.com/markets/forex/rupee-slips-to-over-two-month-low-ahead-of-rbi-policy-decision/article71551180.ece
- Source: Bulls hold for second day, but rupee bleeds near record low — BusinessLine Mkts, 2026-10-06. https://www.thehindubusinessline.com/markets/bulls-hold-for-second-day-but-rupee-bleeds-near-record-low/article71551341.ece
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2025-09-16 (d=0.01)

### [AMBER 5.87] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.66, z20 1.94, zc 0.44, resid-z 0.65 [quiet], 1d 0.53%, |z20|=1.94; 1y-pct=100
- ust_10y [RATES]: last 5.31, z20 1.66, zc 0.72, resid-z 1.07 [quiet], 1d 0.57%, |z20|=1.66; 1y-pct=100
- tips_10y_real [RATES]: last 2.95, z20 1.57, zc 0.69, resid-z 1.03 [quiet], 1d 1.03%, |z20|=1.57; 1y-pct=100
- dyn_bond [EQUITIES]: last 86.65, z20 -1.46, zc 0.81, resid-z -0.41 [quiet], 1d 0.30%, 1y-pct=1
- ust_2y [RATES]: last 4.84, z20 0.82, zc 0.78, resid-z 1.10 [quiet], 1d 0.21%, 1y-pct=98
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.542 vs ust_10y, historically leads by 4d
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.556 vs ust_30y
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.542 vs ust_30y
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.509 vs dyn_bond
- Source: Jefferies favours Indian largecap stocks amid rising bond yields — ET Markets, 2026-10-07. https://economictimes.indiatimes.com/markets/stocks/news/jefferies-favours-indian-largecap-stocks-amid-rising-bond-yields/articleshow/134752755.cms
- Source: BNP WARNS AXING 20-YEAR TREASURY COULD BACKFIRE BNP Paribas warns eliminating the 20-year Treasury bond could push yields higher, signaling panic and encouraging bond vigilantes rather than lowering borrowing costs. The bank maintains its 30-year Treasury short, targeting a yield of 5.8% versus 5.64 — DeItaone, 2026-10-06. https://t.me/walter_bloomberg/36717
- Source: U.S. 10-Year Treasury Yield at 5.25% Is Attractive for Buyers, American Century Investments Says *Competition From AI-Related Credit Boom Is Major Factor Behind Spike in Government-Bond Yields: American Century Investments *Projected Multi-Trillion AI Spending Boom Is Unrealistic, Could Result in 'B — DeItaone, 2026-10-06. https://t.me/walter_bloomberg/36694
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.7] dyn_sepn ↓
- dyn_sepn [EQUITIES]: last 35.71, z20 -3.70, zc -1.40, resid-z -0.08 [quiet], 1d -5.72%, |z20|=3.70
- **Mechanism**: dyn_sepn ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: IEX logs 10.4% growth in electricity trade volume to 12.2 billion units in Sept — BusinessLine Mkts, 2026-10-06. https://www.thehindubusinessline.com/economy/iex-logs-104-growth-in-electricity-trade-volume-to-122-billion-units-in-sept/article71550216.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-13 (d=0.0), 2025-05-01 (d=0.01)

### [AMBER 5.28] indices · 2 series ↑
- sp500 [INDICES]: last 7819.83, z20 2.45, zc 0.81, resid-z 0.67 [quiet], 1d 0.59%, |z20|=2.45; 1y-pct=100
- nasdaq_100 [INDICES]: last 31231.04, z20 1.84, zc 0.47, resid-z -0.27 [quiet], 1d 0.50%, |z20|=1.84; 1y-pct=100
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: vix (inverse) — not yet - watch; rho -0.742 vs sp500, historically leads by 4d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.867 vs sp500
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.785 vs sp500
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.639 vs sp500
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.571 vs nasdaq_100
- Source: The S&P 500 is back in record territory as the ‘Magnificent Seven’ ride to the rescue — MarketWatch Top, 2026-10-06. https://www.marketwatch.com/story/the-s-p-500-is-back-in-record-territory-as-the-magnificent-seven-ride-to-the-rescue-e062724d?mod=mw_rss_topstories
- Source: Marvell just impressed Wall Street with ‘good numbers plus a better story’ — MarketWatch Top, 2026-10-06. https://www.marketwatch.com/story/marvell-just-impressed-wall-street-with-good-numbers-plus-a-better-story-57fbbf23?mod=mw_rss_topstories
- Source: US stocks: S&P 500, Nasdaq reach record closing highs as focus pivots to earnings — ET Markets, 2026-10-06. https://economictimes.indiatimes.com/markets/us-stocks/news/us-stocks-sp-500-nasdaq-reach-record-closing-highs-as-focus-pivots-to-earnings/articleshow/134749835.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-07 (d=0.06), 2026-05-15 (d=0.07)

### [AMBER 5.24] indices · 2 series ↑
- taiwan_weighted [INDICES]: last 49754.07, z20 2.41, zc 0.08, resid-z -0.18 [quiet], 1d 0.08%, |z20|=2.41; 1y-pct=100
- nikkei_225 [INDICES]: last 70707.52, z20 2.36, zc 0.02, resid-z 0.40 [quiet], 1d 0.03%, |z20|=2.36; 1y-pct=98
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.7).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_bajfinance_ns (rho 0.548 via taiwan_weighted, z -1.3, reacted); nifty_it (rho -0.376 via taiwan_weighted, z -0.88, quiet)
- Watch next: kospi (co-move) — not yet - watch; rho 0.94 vs taiwan_weighted
- **India receivers**: dyn_bajfinance_ns (rho 0.548, z -1.3); nifty_it (rho -0.376, z -0.88)
- Source: Stock market outlook today, 6 Oct: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Nikkei, Taiwan cues — Mint Markets, 2026-10-06. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-6-oct-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-nikkei-taiwan-cues-11791247193944.html
- Source: Global Market: Japan’s Nikkei jumps 2.5% to 3-month high as AI stocks rally — ET Markets, 2026-10-05. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-jumps-2-5-to-3-month-high-as-ai-stocks-rally/articleshow/134685851.cms
- Historical analogues: 2025-12-30 (d=0.7), 2025-07-11 (d=0.77), 2026-06-09 (d=1.0)

### [RED 5.04] dyn_ohi ↓
- dyn_ohi [EQUITIES]: last 44.77, z20 -3.04, zc -0.97, resid-z 1.04 [quiet], 1d -1.30%, |z20|=3.04
- **Mechanism**: dyn_ohi ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Retail investors chased small-caps. Now they’re nursing losses — Mint Markets, 2026-10-07. https://www.livemint.com/market/stock-market-news/retail-investors-chased-small-caps-now-they-re-nursing-losses-11791263994165.html
- Source: Oct. 9 has loomed large in stock-market history. Why investors still shouldn’t buy into an October jinx. — MarketWatch Top, 2026-10-06. https://www.marketwatch.com/story/oct-9-has-loomed-large-in-stock-market-history-why-investors-still-shouldnt-buy-into-an-october-jinx-81d7149b?mod=mw_rss_topstories
- Source: AMERICAN CENTURY: TREASURY SELLOFF LOOKS OVERDONE American Century’s Charles Tan says the recent Treasury selloff may have gone too far, calling a 5.25% 10-year yield an attractive entry point for long-term investors. He argues the surge was driven largely by forced selling and intense competition f — DeItaone, 2026-10-06. https://t.me/walter_bloomberg/36693
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2025-04-02 (d=0.09)

### [AMBER 4.24] dyn_techm_ns ↓
- dyn_techm_ns [EQUITIES]: last 1504.50, z20 -2.24, zc -1.37, resid-z -2.03 [unexplained], 1d -2.04%, |z20|=2.24
- **Mechanism**: dyn_techm_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.838 via dyn_techm_ns, z -0.88, quiet); dyn_tataelxsi_ns (rho 0.468 via dyn_techm_ns, z -1.41, reacted); dyn_justdial_bo (rho 0.454 via dyn_techm_ns, z -0.98, quiet); dyn_tatatech_ns (rho 0.396 via dyn_techm_ns, z -0.9, quiet)
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.838 vs dyn_techm_ns
- **India receivers**: nifty_it (rho 0.838, z -0.88); dyn_tataelxsi_ns (rho 0.468, z -1.41); dyn_justdial_bo (rho 0.454, z -0.98); dyn_tatatech_ns (rho 0.396, z -0.9)
- Source: Market wrap: Trent, BSE, Coal India, Tech Mahindra top gainers and losers on Nifty and Sensex on Tuesday — ET Markets, 2026-10-06. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-trent-bse-coal-india-tech-mahindra-top-gainers-and-losers-on-nifty-and-sensex-on-tuesday/articleshow/134739696.cms
- Source: Why Kotak Mahindra Bank shares are outperforming Nifty 50 and Bank Nifty in the last two months? Experts explain — Mint Markets, 2026-10-06. https://www.livemint.com/market/stock-market-news/why-kotak-mahindra-bank-shares-are-outperforming-nifty-50-and-bank-nifty-in-the-last-two-months-experts-explain-11791281103828.html
- Source: Reliance, Kotak Mahindra Bank, Welspun shares: Build model stock portfolio! Why Jefferies India is bullish on large-caps — Mint Markets, 2026-10-06. https://www.livemint.com/market/stock-market-news/reliance-kotak-mahindra-bank-welspun-shares-build-model-stock-portfolio-why-jefferies-india-is-bullish-on-largecaps-11791268837224.html
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-11 (d=0.03), 2025-02-10 (d=0.09)

### [AMBER 4.22] dyn_coalindia_ns ↓
- dyn_coalindia_ns [EQUITIES]: last 411.65, z20 -2.22, zc -2.43, resid-z -2.32 [unexplained], 1d -3.16%, |z20|=2.22
- **Mechanism**: dyn_coalindia_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Market wrap: Trent, BSE, Coal India, Tech Mahindra top gainers and losers on Nifty and Sensex on Tuesday — ET Markets, 2026-10-06. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-trent-bse-coal-india-tech-mahindra-top-gainers-and-losers-on-nifty-and-sensex-on-tuesday/articleshow/134739696.cms
- Source: RBI MPC meeting Oct 2026: Why TCS, HDFC Bank, ICICI Lombard, Coal India shares may gain if 25 bps rate hike is announced — Mint Markets, 2026-10-06. https://www.livemint.com/market/stock-market-news/rbi-mpc-meeting-october-2026-why-hdfc-bank-icici-lombard-coal-india-tcs-likely-to-gain-if-bank-announces-rate-hike-11791268517566.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-24 (d=0.03), 2024-11-07 (d=0.04)

## Watchlist (below surfacing floor)
dyn_nvda ↑ (4.16), indices · 2 series ↓ (3.91), bovespa ↑ (3.78), hy_oas ↑ (3.65), eur_usd ↓ (3.49), dyn_4417_t ↑ (3.49), dyn_policybzr_ns ↓ (3.32), dyn_jiofin_bo ↓ (3.28), usd_cny ↓ (3.1), gold_silver_ratio ↓ (3.01), usd_brl ↓ (2.94), dyn_meta ↑ (2.84)

## India macro
- nifty_50: 22776.0996 (1d 0.98%, z20 -1.08, flag amber)
- nifty_midcap_100: 59761.7500 (1d 1.07%, z20 -1.14, flag none)
- usd_inr: 96.3600 (1d 0.02%, z20 1.35, flag amber)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6239 (1d 0.09%, z20 -1.05, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI MPC decision T-0d · AMFI SIP / MF flows T-1d · RBI Weekly Statistical Supplement T-2d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 82.5 — "BNP WARNS AXING 20-YEAR TREASURY COULD BACKFIRE BNP Paribas warns eliminating the 20-year "
- INOXINDIA.NS (INOX INDIA LIMITED) score 80.5 — "Jefferies favours Indian largecap stocks amid rising bond yields"
- COALINDIA.NS (COAL INDIA LTD) score 79.5 — "Jefferies favours Indian largecap stocks amid rising bond yields"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 77.7 — "Jefferies favours Indian largecap stocks amid rising bond yields"
- BAC (Bank of America Corporation) score 69.9 — "BNP WARNS AXING 20-YEAR TREASURY COULD BACKFIRE BNP Paribas warns eliminating the 20-year "
- HDB (HDFC Bank Limited) score 63.6 — "BNP WARNS AXING 20-YEAR TREASURY COULD BACKFIRE BNP Paribas warns eliminating the 20-year "
- IDBI.NS (IDBI BANK LIMITED) score 61.6 — "BNP WARNS AXING 20-YEAR TREASURY COULD BACKFIRE BNP Paribas warns eliminating the 20-year "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 61.6 — "BNP WARNS AXING 20-YEAR TREASURY COULD BACKFIRE BNP Paribas warns eliminating the 20-year "
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 61.6 — "BNP WARNS AXING 20-YEAR TREASURY COULD BACKFIRE BNP Paribas warns eliminating the 20-year "
- COIN (Coinbase Global, Inc.) score 46.9 — "Taiwan Dethrones Korea Atop Global Markets as AI Trade Widens"
- BOND (PIMCO Active Bond Exchange-Tra) score 46.1 — "BNP WARNS AXING 20-YEAR TREASURY COULD BACKFIRE BNP Paribas warns eliminating the 20-year "
- OHI (Omega Healthcare Investors, In) score 44.7 — "Retail investors chased small-caps. Now they’re nursing losses"
- TECHM.NS (TECH MAHINDRA LIMITED) score 43.3 — "Top stocks in focus today: Investors must watch Titan, Utkarsh SFB, HCL Tech shares on Wed"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 36.4 — "Top stocks in focus today: Investors must watch Titan, Utkarsh SFB, HCL Tech shares on Wed"
- TECH (Bio-Techne Corp) score 36.4 — "Top stocks in focus today: Investors must watch Titan, Utkarsh SFB, HCL Tech shares on Wed"
- TGT (Target Corporation) score 35.4 — "BNP WARNS AXING 20-YEAR TREASURY COULD BACKFIRE BNP Paribas warns eliminating the 20-year "
- CHKP (Check Point Software Technolog) score 32.2 — "TajGVK Hotels shares: Stock down 26% in 1 year, but Monarch sees 49% upside - Here's why |"
- LTH (Life Time Group Holdings, Inc.) score 29.8 — "S&P 500 REGISTERS RECORD CLOSING HIGH FOR FIRST TIME SINCE AUG 13"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 25.4 — "BNP WARNS AXING 20-YEAR TREASURY COULD BACKFIRE BNP Paribas warns eliminating the 20-year "
- SEPN (Septerna, Inc.) score 22.2 — "September demat account addition falls to 2.89 million amid market selloff"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 17.6 — "Mutual Funds', FPI favourite Tata Group stock hits upper circuit after Q2 update - Can it "
- BZ=F (Brent Crude Oil Last Day Finan) score 16.3 — "S&P 500 BRIEFLY HITS INTRADAY RECORD HIGH, LAST UP 0.5%"
- 301077.SZ (CHINASTARS) score 16.0 — "US AND CHINA DISCUSSING RECIPROCAL NUCLEAR SITE VISITS AMID CONCERNS ABOUT A NEW ARMS RACE"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.0 — "Marvell just impressed Wall Street with ‘good numbers plus a better story’"
- JIOFIN.BO (Jio Financial Services Limited) score 9.8 — "JULIUS BAER SEES FINAL FED HIKE IN DECEMBER Julius Baer expects the Fed to deliver one fin"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 9.3 — "FRANCE READY TO BYPASS PARLIAMENT FOR €43 BILLION IN CUTS French Finance Minister Roland L"
- JEF (Jefferies Financial Group Inc.) score 9.3 — "Jefferies favours Indian largecap stocks amid rising bond yields"
- VT (Vanguard Total World Stock Ind) score 9.2 — "UKRAINE'S ZELENSKIY SAYS UPDATED INTELLIGENCE SHOWS RUSSIA IS PREPARING A 'MASSIVE ATTACK'"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 7.2 — "Mutual Funds', FPI favourite Tata Group stock hits upper circuit after Q2 update - Can it "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 7.2 — "Mutual Funds', FPI favourite Tata Group stock hits upper circuit after Q2 update - Can it "
- NVDA (NVIDIA Corporation) score 7.1 — "SPCX - SPACEX LOOKS TO RAISE $40BN TO BUY NVIDIA CHIPS IN FINANCING LED BY APOLLO - FT"
- META (Meta) score 6.7 — "Bitcoin vs gold: Why Cathie Wood feels cryptocurrency's 'turn is in' against the precious "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.3 — "Adani Power gains 2% after signing pact for 770-MW hydropower project in Bhutan"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 6.1 — "Retail investors chased small-caps. Now they’re nursing losses"
- GS (Goldman Sachs Group, Inc. (The) score 6.1 — "TSLA - GOLDMAN: TESLA’S AI STORY MATTERS MORE THAN Q3 EARNINGS Goldman Sachs reiterated it"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 5.5 — "FRANCE READY TO BYPASS PARLIAMENT FOR €43 BILLION IN CUTS French Finance Minister Roland L"
- POLICYBZR.NS (PB FINTECH LIMITED) score 5.1 — "PB Fintech extends losing streak to 7 sessions, stock hits 32-month low"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.7 — "RBI MPC meeting Oct 2026: Why TCS, HDFC Bank, ICICI Lombard, Coal India shares may gain if"
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