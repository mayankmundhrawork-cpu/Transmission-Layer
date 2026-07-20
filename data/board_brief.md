# Transmission Layer — board brief · 2026-07-20 20:11Z

data as of **2026-07-20** · 98 series · 10 red / 40 amber · 8 events surfaced (31 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.524, 10d in regime; vol-pct 0.672, breadth-off 0.375, Markov P(high-vol) 0.058)
- [WEAK] **safe_haven_gold** — corr20 -0.0, corr60 -0.42, contra nifty_50 corr20=0.24, last shift 2026-05-28. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.92, corr60 0.82, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.43, corr60 0.38, last shift 2026-05-19. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.09, corr60 -0.04, last shift 2026-06-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.8, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.06, corr60 -0.06, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.17, corr60 -0.27, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.21, corr60 0.23, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.0015243893761345273)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.497** (n=1159) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.819** (n=2999) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.722** (n=18) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.45] dyn_qessf ↓
- dyn_qessf [EQUITIES]: last 0.19, z20 -5.45, zc 0.60, resid-z -0.56 [quiet], 1d -23.72%, |z20|=5.45
- **Mechanism**: The recent decline in dyn_qessf, a defence-related equity, can be attributed to the escalation in the US-Iran war, which has led to a setback in defence stocks. The valid metal_copper_channel and vix_equity_inverse channels suggest that global risk-off sentiment and vol spike may have contributed to the decline. However, the move is largely priced, given the small resid_z of -0.56, indicating that the decline is largely explained by factor exposures.
- **Gap**: No gap: the decline in dyn_qessf is largely priced, with a small resid_z of -0.56, indicating that the move is explained by factor exposures
- **India take**: The Indian defence stocks, such as HAL, BEL, and Bharat Dynamics, have already reacted to the escalation in the US-Iran war, with declines in their share prices. The dyn_atherenerg_ns, which has a rho of -0.358 with dyn_qessf, has also reacted to the decline.
- Watch next: dyn_atherenerg_ns (down) — already moved; reacted to dyn_qessf decline
- **India receivers**: dyn_atherenerg_ns (rho -0.358, z 1.61)
- Source: West Asia conflict fuels defence stocks. Now comes the harder test — Mint Markets, 2026-07-20. https://www.livemint.com/market/stock-market-news/india-defence-stocks-rally-west-asia-conflict-next-leg-orders-or-execution-indigenization-procurement-11784518899336.html
- Source: HAL, BEL to Bharat Dynamics: Defence stocks dip after escalation in the US-Iran war — Mint Markets, 2026-07-20. https://www.livemint.com/market/stock-market-news/hal-bel-to-bharat-dynamics-defence-stocks-dip-after-escalation-in-the-us-iran-war-11784521448590.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-15 (d=0.32), 2024-11-14 (d=0.52)

### [AMBER 6.24] cross-asset · 6 series ↑
- russell_2000 [INDICES]: last 2945.50, z20 -2.09, zc -0.35, resid-z 1.55 [unexplained], 1d -0.56%, |z20|=2.09
- nasdaq_100 [INDICES]: last 28607.75, z20 -2.06, zc -1.09, resid-z -1.07 [quiet], 1d 0.05%, |z20|=2.06
- tips_10y_real [RATES]: last 2.35, z20 1.56, zc 0.74, resid-z 0.05 [quiet], 1d 1.29%, |z20|=1.56; 1y-pct=99
- ust_30y [RATES]: last 5.09, z20 1.47, zc 0.31, resid-z -0.18 [quiet], 1d 0.20%, 1y-pct=97
- dyn_bond [EQUITIES]: last 91.12, z20 -1.31, zc 0.18, resid-z 1.04 [quiet], 1d -0.37%, 1y-pct=2
- ust_10y [RATES]: last 4.57, z20 1.18, zc 0.45, resid-z -0.21 [quiet], 1d 0.44%, 1y-pct=97
- **Mechanism**: The recent move in the Russell 2000 and Nasdaq 100 indices is driven by a rebound in semiconductor stocks, which has led to a recovery in the broader market. The tips_10y_real and ust_30y rates have also moved in response to the shift in market sentiment. However, the resid_z values for these series are relatively small, indicating that the moves are largely priced in and not anomalous. The valid channels, such as the vix_equity_inverse and metal_copper_channel, are not currently driving the move.
- **Gap**: No gap: the recent moves in the Russell 2000 and Nasdaq 100 indices are largely priced in, with small resid_z values indicating no anomaly
- **India take**: The Indian instrument that expresses this move is the Nifty 50, which has not yet reacted significantly to the rebound in semiconductor stocks. The metal_copper_channel, which is a valid channel, may lead to a move in Indian metal equities.
- Watch next: russell_2000 (up) — already moved; rebound in semiconductor stocks
- Source: Lotus Petal opens first SSE bond issue since CSR rule change — BusinessLine Mkts, 2026-07-20. https://www.thehindubusinessline.com/markets/stock-markets/lotus-petal-opens-first-sse-bond-issue-since-csr-rule-change/article71245959.ece
- Source: Wall Street: S&P 500, Nasdaq rebound as chipmakers recover, investors brace for big tech earnings — Mint Markets, 2026-07-20. https://www.livemint.com/market/stock-market-news/us-stocks-rebound-as-chipmakers-recover-investors-brace-for-big-tech-earnings-11784555512184.html
- Source: The Titans of Nasdaq 100: Top companies ranked by market cap — ET Markets, 2026-07-20. https://economictimes.indiatimes.com/markets/us-stocks/news/the-titans-of-nasdaq-100-top-companies-ranked-by-market-cap/slideshow/132516440.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.4), 2025-05-20 (d=0.5)

### [RED 5.83] dyn_hdb ↓
- dyn_hdb [EQUITIES]: last 23.59, z20 -3.83, zc 0.17, resid-z 0.73 [quiet], 1d -10.56%, |z20|=3.83; 1y-pct=2
- **Mechanism**: The decline in dyn_hdb is attributed to margin-related concerns and a flare-up in US-Iran tensions, which has led to a risk-off sentiment in the market. This sentiment is further reinforced by the weakness in bank stocks, particularly HDFC Bank and Axis Bank. The valid vix_equity_inverse channel suggests that the vol spike will lead to an equity drawdown, which is consistent with the current market movement.
- **Gap**: No gap: The big raw move in dyn_hdb with a relatively small resid_z of 0.73 suggests that the move is largely priced in, leaving no significant event-to-price gap.
- **India take**: The Indian instrument that expresses this move is the nifty_50, which has not yet reacted to the decline in dyn_hdb. Other Indian transmission candidates such as nifty_midcap_100 and dyn_indusindbk_bo have already reacted to the news.
- Watch next: nifty_50 (down) — not yet - watch; historically leads dyn_hdb by 1d
- **India receivers**: nifty_50 (rho 0.646, z 0.86); nifty_midcap_100 (rho 0.5, z 1.08); dyn_indusindbk_bo (rho 0.487, z 1.43)
- Source: What investors need to glean from HDFC Bank’s Q1 FY27 results — BusinessLine Mkts, 2026-07-20. https://www.thehindubusinessline.com/portfolio/stock-fundamental-analysis-india/what-investors-need-to-glean-from-hdfc-banks-q1-fy27-results/article71246090.ece
- Source: Sensex today | Stock Market Highlights: Sensex drops 442 pts to end at 77,708, Nifty closes below 24,240; Axis Bank, HDFC Bank fall most — BusinessLine Mkts, 2026-07-20. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-highlights-20th-july-2026/article71241122.ece
- Source: ICICI Bank gains while HDFC Bank, Axis Bank, Kotak Mahindra, Yes Bank decline after Q1 results — BusinessLine Mkts, 2026-07-20. https://www.thehindubusinessline.com/markets/stock-markets/bank-stocks-underperform-icici-bank-gains-while-hdfc-bank-axis-bank-kotak-mahindra-yes-bank-decline/article71243829.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [RED 5.61] cross-asset · 2 series ↑
- dyn_techm_ns [EQUITIES]: last 1575.40, z20 2.77, zc 2.21, resid-z 1.21 [moved], 1d 0.16%, |z20|=2.77
- nifty_it [INDICES]: last 29159.35, z20 1.77, zc 0.99, resid-z 0.43 [quiet], 1d -0.23%, |z20|=1.77
- **Mechanism**: The recent Q1 results of various Indian companies, including UltraTech Cement and Indian Overseas Bank, have led to a surge in their stock prices, which in turn has driven the Nifty IT index. However, the resid_z values indicate that the move in dyn_techm_ns is largely priced, with a resid_z of 1.21, suggesting that the big raw move is not an anomaly. The valid metal_copper_channel and vix_equity_inverse channels may also be contributing to the move.
- **Gap**: No gap: the move in dyn_techm_ns is largely priced, with a resid_z of 1.21, indicating that the big raw move is not an anomaly
- **India take**: The Indian instrument that expresses this move is dyn_tataelxsi_ns, which has already reacted with a rho of 0.704 via nifty_it, and a z20 of -1.19. The Nifty IT index has also been driven by the Q1 results, but its resid_z value is relatively low, indicating a quiet move.
- Watch next: dyn_techm_ns (up) — already moved; Q1 results driven surge
- **India receivers**: dyn_tataelxsi_ns (rho 0.704, z -1.19)
- Source: Q1 Results Today Highlights: UltraTech profit rises; IOB, KVB and Sobha post strong Q1 growth; Mahindra Logistics, Dynamic Cables, Jaiprakash Power, Shyam Metalics surge — BusinessLine Mkts, 2026-07-20. https://www.thehindubusinessline.com/markets/q1-results-today-highlights-cement-paytm-iob-karur-vysya-bank-shyam-metalics-sobha-jp-power-bluestone-hdfc-bank-kotak-icici-yes-bank-axis-bank-ril-results-20-july-2026/article71241085.ece
- Source: Q1 Results Today Live: UltraTech PAT up, IOB, KVB Q1 PAT climb, Mahindra Logistics, Dynamic Cables & Shyam Metalics zoom, Paytm, Sobha, JP Power, Bluestone to announce Q1 results — BusinessLine Mkts, 2026-07-20. https://www.thehindubusinessline.com/markets/q1-results-today-live-updates-ultratech-cement-paytm-iob-karur-vysya-bank-shyam-metalics-sobha-jp-power-bluestone-hdfc-bank-kotak-icici-yes-bank-axis-bank-ril-results-20-july-2026/article71241085.ece
- Source: ICICI Bank gains while HDFC Bank, Axis Bank, Kotak Mahindra, Yes Bank decline after Q1 results — BusinessLine Mkts, 2026-07-20. https://www.thehindubusinessline.com/markets/stock-markets/bank-stocks-underperform-icici-bank-gains-while-hdfc-bank-axis-bank-kotak-mahindra-yes-bank-decline/article71243829.ece
- Historical analogues: 2025-12-30 (d=0.52), 2025-08-13 (d=0.76), 2026-01-06 (d=0.77)

### [AMBER 5.15] commodities · 2 series ↑
- brent [COMMODITIES]: last 88.86, z20 2.32, zc 2.22, resid-z 1.14 [moved], 1d 0.86%, |z20|=2.32; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 82.38, z20 2.19, zc 2.13, resid-z 1.00 [moved], 1d -0.13%, |z20|=2.19
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.602 via wti, z 1.08, reacted)
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.505 vs brent, historically leads by 5d
- Watch next: cac_40 (inverse) — not yet - watch; rho -0.578 vs brent
- Watch next: india_vix (co-move) — not yet - watch; rho 0.531 vs brent
- **India receivers**: nifty_midcap_100 (rho -0.602, z 1.08)
- Source: New Zealand Oil Explorers Rush to Secure Offshore Permits Before Election — OilPrice, 2026-07-20. https://oilprice.com/Latest-Energy-News/World-News/New-Zealand-Oil-Explorers-Rush-to-Secure-Offshore-Permits-Before-Election.html
- Source: Nigeria Targets Record 3 Million Bpd Oil Output by 2030 — OilPrice, 2026-07-20. https://oilprice.com/Energy/Crude-Oil/Nigeria-Targets-Record-3-Million-Bpd-Oil-Output-by-2030.html
- Source: New UK Prime Minister Set to Back North Sea Oil and Gas Projects — OilPrice, 2026-07-20. https://oilprice.com/Energy/Energy-General/New-UK-Prime-Minister-Set-to-Back-North-Sea-Oil-and-Gas-Projects.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [AMBER 5.13] fx · 3 series ↑
- usd_brl [FX]: last 5.09, z20 -1.81, zc 0.57, resid-z 0.64 [quiet], 1d -0.44%, |z20|=1.81
- aud_usd [FX]: last 0.70, z20 1.61, zc -0.21, resid-z -0.20 [quiet], 1d 0.01%, |z20|=1.61
- eur_usd [FX]: last 1.14, z20 0.10, zc -0.62, resid-z -0.67 [quiet], 1d -0.24%, 1y-pct=4
- **Mechanism**: fx · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-07 (z-distance 0.08).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_ceatltd_ns (rho 0.364 via aud_usd, z -1.56, reacted)
- Watch next: usd_mxn (co-move) — not yet - watch; rho 0.664 vs usd_brl
- Watch next: asx_200 (co-move) — not yet - watch; rho 0.588 vs aud_usd
- **India receivers**: dyn_ceatltd_ns (rho 0.364, z -1.56)
- Source: Global Market: Euro Zone firms see slower price and wage growth, ECB survey shows — ET Markets, 2026-07-20. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-zone-firms-see-slower-price-and-wage-growth-ecb-survey-shows/articleshow/132510738.cms
- Historical analogues: 2026-07-07 (d=0.08), 2025-09-30 (d=0.17), 2025-08-26 (d=0.27)

### [RED 5.0] dyn_nflx ↓
- dyn_nflx [EQUITIES]: last 67.57, z20 -3.00, zc -4.00, resid-z 0.65 [moved], 1d -1.99%, |z20|=3.00; 1y-pct=0
- **Mechanism**: dyn_nflx ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: US stocks to buy for short term: From Nvidia to Netflix- Appreciate CEO suggests picking these 5 shares — Mint Markets, 2026-07-20. https://www.livemint.com/market/stock-market-news/us-stocks-to-buy-for-short-term-from-nvidia-to-netflix-appreciate-ceo-suggests-picking-these-5-shares-11784551408198.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-10 (d=0.03), 2025-04-01 (d=0.05)

### [RED 4.62] commodities · 3 series ↑
- corn [COMMODITIES]: last 472.50, z20 3.30, zc 0.58, resid-z 0.34 [quiet], 1d 6.24%, |z20|=3.30; 1y-pct=98
- wheat [COMMODITIES]: last 672.75, z20 1.88, zc 0.47, resid-z 0.33 [quiet], 1d -1.46%, |z20|=1.88; 1y-pct=98
- soybeans [COMMODITIES]: last 1225.00, z20 1.72, zc 0.78, resid-z 0.32 [quiet], 1d 1.70%, |z20|=1.72; 1y-pct=100
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_patanjali_ns (rho -0.501 via wheat, z -2.57, reacted); dyn_adanient_bo (rho -0.359 via soybeans, z 1.04, reacted)
- **India receivers**: dyn_patanjali_ns (rho -0.501, z -2.57); dyn_adanient_bo (rho -0.359, z 1.04)
- Historical analogues: 2026-05-22 (d=0.0), 2024-08-30 (d=0.27), 2026-05-06 (d=0.32)

## Watchlist (below surfacing floor)
indices · 3 series ↓ (4.6), dyn_icicigi_bo ↓ (4.54), shanghai_comp ↓ (4.48), gold_silver_ratio ↑ (4.29), natgas ↓ (3.8), usd_inr ↑ (3.52), dyn_ohi ↑ (3.04), dyn_bac ↑ (3.01), dyn_bhel_ns ↑ (2.97), brent_wti_spread ↑ (2.62), dyn_patanjali_ns ↓ (2.57), dyn_pypl ↑ (2.35)

## India macro
- nifty_50: 24239.5000 (1d -0.39%, z20 0.86, flag none)
- nifty_midcap_100: 62818.7500 (1d 0.63%, z20 1.08, flag amber)
- usd_inr: 96.4350 (1d -0.22%, z20 1.52, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5916 (1d 1.02%, z20 0.29, flag none)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 61.6 — "Coca-Cola names JPMorgan, Citi as bankers for India bottling unit IPO"
- INOXINDIA.NS (INOX INDIA LIMITED) score 58.9 — "Broker’s call:  WeWork India (Buy)"
- HDB (HDFC Bank Limited) score 56.4 — "Coca-Cola names JPMorgan, Citi as bankers for India bottling unit IPO"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 51.0 — "Coca-Cola names JPMorgan, Citi as bankers for India bottling unit IPO"
- BAC (Bank of America Corporation) score 47.1 — "U.S. MAY HAVE HIDDEN IRAN ATTACK INJURIES The New York Times reports the U.S. military may"
- IDBI.NS (IDBI BANK LIMITED) score 39.4 — "Coca-Cola names JPMorgan, Citi as bankers for India bottling unit IPO"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 38.3 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Live: US Stocks edge unevenly as US-"
- COIN (Coinbase Global, Inc.) score 36.9 — "​5 global market themes investors will track this week"
- TECHM.NS (TECH MAHINDRA LIMITED) score 25.0 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today | Live: US Stocks edge unevenly as US-"
- BOND (PIMCO Active Bond Exchange-Tra) score 20.2 — "Lotus Petal opens first SSE bond issue since CSR rule change"
- CHKP (Check Point Software Technolog) score 18.2 — "Nifty 50, Sensex prediction today: Check how Indian stock market is expected to trade on 2"
- VT (Vanguard Total World Stock Ind) score 14.7 — "ENGLAND BEAT FRANCE 6-4 TO FINISH THIRD IN WORLD CUP"
- OHI (Omega Healthcare Investors, In) score 13.7 — "WALL STREET WEEK AHEAD: $GOOGL, $INTC IN FOCUS U.S. earnings season accelerates next week,"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 12.4 — "MORGAN STANLEY: DIESEL MARKET STAYS TIGHT Morgan Stanley says Europe’s record-high diesel "
- ICICIGI.BO (ICICI Lombard General Insuranc) score 11.6 — "Q1 Results Today Highlights: Kotak Mahindra, YES Bank drive Q1 with 23%, 34% profit jump; "
- JIOFIN.BO (Jio Financial Services Limited) score 9.8 — "Expert view: Overweight on diversified financials, automobiles, new age tech firms, says N"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 9.8 — "Expert view: Overweight on diversified financials, automobiles, new age tech firms, says N"
- META (Meta) score 9.1 — "Market Trading Guide: Lloyds Metals among 2 stock recommendations for Tuesday"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.2 — "MEN MORE LIKELY TO NEGOTIATE PAY RISES Men are more likely than women to use outside job o"
- MS (Morgan Stanley) score 6.1 — "MORGAN STANLEY: DIESEL MARKET STAYS TIGHT Morgan Stanley says Europe’s record-high diesel "
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 5.9 — "Broker’s call:  WeWork India (Buy)"
- NFLX (Netflix, Inc.) score 5.7 — "US stocks to buy for short term: From Nvidia to Netflix- Appreciate CEO suggests picking t"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 5.6 — "Tata Technologies Q1 Results: Profit rises 6% to Rs 180 crore"
- PCJEWELLER.NS (PC JEWELLER LTD) score 5.3 — "BlueStone Jewellery shares to be in focus on Tuesday as company turns profitable in Q1, re"
- SKHYV (SK hynix Inc. American Deposit) score 5.3 — "SKHY – SK HYNIX DOWN 0.7% IN PREMARKET SK Hynix shares are slipping 0.7% in premarket afte"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 5.2 — "BAHRAIN AIR DEFENCES INTERCEPT IRANIAN ATTACK - STATE TV"
- BHEL.NS (BHEL) score 5.0 — "BHEL share price: Brokerages see up to 23% upside after Maharatna PSU posts first Q1 profi"
- WIT (Wipro Limited) score 4.8 — "Stocks to watch: Reliance Industries, Wipro, CEAT among shares in focus today; check list "
- GS (Goldman Sachs Group, Inc. (The) score 4.6 — "Goldman Sachs initiates coverage on Sansera Engineering, 3 other auto ancillary stocks wit"
- NVDA (NVIDIA Corporation) score 4.5 — "US stocks to buy for short term: From Nvidia to Netflix- Appreciate CEO suggests picking t"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 3.0 — "Adani Ent Share Price Live Updates: Adani Enterprises  Current Price Update"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 3.0 — "New York imports more electricity from Canada after high-voltage transmission line opens"
- CEATLTD.NS (CEAT LIMITED) score 2.6 — "Top Gainers & Losers on 20 July: Axis Bank, HDFC Bank, Ceat, India Cements, OLA, HFCL amon"
- AAPL (Apple Inc.) score 2.5 — "APPLE CLOSES IN ON NVIDIA $AAPL is on the verge of reclaiming the title of the world’s mos"
- KO (Coca-Cola Company (The)) score 2.0 — "Coca-Cola names JPMorgan, Citi as bankers for India bottling unit IPO"
- KALYANKJIL.NS (KALYAN JEWELLERS IND LTD) score 1.9 — "Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. T"
- PYPL (PayPal Holdings, Inc.) score 1.2 — "US stocks today: US stocks rise with earnings in focus; PayPal jumps on takeover bid repor"
- BIOCON.BO (BIOCON LTD.) score 1.2 — "Mylan exits Biocon, sells entire 5.64% stake for ₹3,679 crore via block deals"
- CUPID.NS (CUPID LIMITED) score 0.8 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 0.6 — "Patanjali Foods share price crashes 20%, extending losses for third straight session; what"

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