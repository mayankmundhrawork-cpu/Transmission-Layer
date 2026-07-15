# Transmission Layer — board brief · 2026-07-15 10:32Z

data as of **2026-07-15** · 98 series · 12 red / 35 amber · 8 events surfaced (31 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.378, 7d in regime; vol-pct 0.589, breadth-off 0.167, Markov P(high-vol) 0.017)
- [INVERTED] **safe_haven_gold** — corr20 -0.09, corr60 -0.45, contra nifty_50 corr20=0.37, last shift 2026-05-28. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.93, corr60 0.83, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [VALID] **metal_copper_channel** — corr20 0.43, corr60 0.35, last shift 2026-05-14. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.17, corr60 0.01, last shift 2026-03-11. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.93, corr60 -0.78, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.0, corr60 -0.05, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.24, corr60 -0.26, last shift 2026-05-13. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.35, corr60 0.26, last shift 2026-04-21. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 87** scanned series survive multiplicity control (effective p ≤ 6.334248366623996e-05)
- **SETUP** dyn_ms → asx_200: leads 1d (ccf 0.508, β 0.2125, p 0.0); driver zc 1.78 → expected 0.669%. Type hit-rate 0.818 (n=2411).
- **SETUP** dyn_gs → asx_200: leads 1d (ccf 0.5, β 0.2009, p 0.0); driver zc 5.08 → expected 1.84%. Type hit-rate 0.818 (n=2411).
- **SETUP** dyn_gs → nikkei_225: leads 1d (ccf 0.391, β 0.3394, p 0.0); driver zc 5.08 → expected 3.107%. Type hit-rate 0.818 (n=2411).
- **SETUP** dyn_gs → usd_mxn: leads 1d (ccf -0.309, β -0.1042, p 2e-05); driver zc 5.08 → expected -0.954%. Type hit-rate 0.818 (n=2411).
- Track record · residual_reversion: hit-rate **0.482** (n=1147) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=2411) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.632** (n=19) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 18.84] dyn_patanjali_ns ↓
- dyn_patanjali_ns [EQUITIES]: last 347.00, z20 -16.84, zc -11.24, resid-z -12.24 [unexplained], 1d -14.86%, |z20|=16.84; 1y-pct=0
- **Mechanism**: The sharp decline in Patanjali Foods shares is attributed to heavy selling, with technical analysts warning of further downside. The stock's 20% plunge is not fully explained by factor exposures, as indicated by a resid_z of -12.24. This unexplained move may propagate through the metal_copper_channel, given the VALID status of this channel. However, the primary driver of the move appears to be idiosyncratic to Patanjali Foods, with no clear link to broader market or macro factors.
- **Gap**: No gap: the 20% decline in Patanjali Foods shares is largely priced in, given the stock's significant decline over the past year and the lack of clear catalysts for a reversal
- **India take**: The Indian instrument that expresses this move is dyn_tataelxsi_ns, which has already reacted with a decline. Further downside in Patanjali Foods may lead to additional selling pressure in related stocks, although the lack of a clear event-to-price gap suggests that the market has already digested the news.
- Watch next: dyn_tataelxsi_ns (down) — already moved; rho=0.418 with dyn_patanjali_ns
- **India receivers**: dyn_tataelxsi_ns (rho 0.418, z -1.67)
- Source: Patanjali Foods shares crash 20%, stock nearly halves in value in one year. What's ahead? — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/stocks/news/patanjali-foods-shares-crash-20-stock-nearly-halves-in-value-in-one-year-whats-ahead/articleshow/132410105.cms
- Source: Patanjali Foods share price crashes 20%, extending losses for third straight session; what should investors do? — Mint Markets, 2026-07-15. https://www.livemint.com/market/stock-market-news/patanjali-foods-share-price-crashes-20-extends-its-losses-for-third-session-what-should-investors-do-11784098857317.html
- Historical analogues: 2025-01-27 (d=0.01), 2026-05-28 (d=0.05), 2025-06-30 (d=0.06)

### [RED 9.6] dyn_nuvoco_ns ↑
- dyn_nuvoco_ns [EQUITIES]: last 376.30, z20 7.60, zc 3.42, resid-z 4.00 [unexplained], 1d 10.22%, |z20|=7.60
- **Mechanism**: The strong Q1 results of Nuvoco Vistas, with a 20% year-on-year increase in net profit and its highest-ever first-quarter EBITDA, have led to a rally in the stock price. This move is unexplained by factor exposures, with a resid_z of 4.0, indicating that the market is pricing in the company's improved profitability and growth prospects. The metal_copper_channel and gold_silver_comove channels are valid and may be contributing to the move.
- **Gap**: No gap: The stock price has already reacted to the strong Q1 results, with a 12% rally, and the resid_z of 4.0 indicates that the move is largely priced in.
- **India take**: The Indian transmission candidates, such as dyn_justdial_bo, nifty_midcap_100, and dyn_pcjeweller_ns, have already reacted to the move in Nuvoco Vistas, with correlations ranging from 0.403 to 0.469. The Nifty Midcap 100 index has also reacted, indicating a broader impact on the Indian market.
- Watch next: dyn_nuvoco_ns (up) — already moved; Strong Q1 results
- **India receivers**: dyn_justdial_bo (rho 0.469, z 3.7); nifty_midcap_100 (rho 0.451, z 1.74); dyn_pcjeweller_ns (rho 0.403, z 2.49)
- Source: Nuvoco Vistas share price rallies 12% on strong Q1 results FY27. Should you buy or sell? — Mint Markets, 2026-07-15. https://www.livemint.com/market/stock-market-news/nuvoco-vistas-share-price-rallies-12-on-strong-q1-results-fy27-should-you-buy-or-sell-11784091753229.html
- Source: Nuvoco Vistas shares soar 10% after strong Q1. Why Nomura, Choice see up to 47% upside? — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/stocks/news/nuvoco-vistas-shares-soar-10-after-strong-q1-why-nomura-choice-see-up-to-47-upside/articleshow/132406082.cms
- Source: Nuvoco Vistas shares rocket 14% after Q1 net profit jumps 20%; firm reports strongest EBITDA ever — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/stocks/news/nuvoco-vistas-shares-rocket-14-after-q1-net-profit-jumps-20-firm-reports-strongest-ebitda-ever/articleshow/132381134.cms
- Historical analogues: 2025-08-12 (d=0.03), 2025-08-05 (d=0.05), 2025-07-29 (d=0.05)

### [RED 6.65] cross-asset · 5 series ↑
- ust_10y [RATES]: last 4.62, z20 2.72, zc 0.44, resid-z 0.56 [quiet], 1d 1.32%, |z20|=2.72; 1y-pct=99
- ust_30y [RATES]: last 5.10, z20 2.28, zc 0.27, resid-z 0.32 [quiet], 1d 0.79%, |z20|=2.28; 1y-pct=98
- tips_10y_real [RATES]: last 2.36, z20 2.27, zc 0.24, resid-z 0.27 [quiet], 1d 1.72%, |z20|=2.27; 1y-pct=100
- ust_2y [RATES]: last 4.26, z20 2.15, zc 0.93, resid-z 1.21 [quiet], 1d 1.19%, |z20|=2.15; 1y-pct=100
- dyn_bond [EQUITIES]: last 91.18, z20 -1.51, zc 0.93, resid-z 0.14 [quiet], 1d 0.29%, 1y-pct=4
- **Mechanism**: The recent rise in Euro zone bond yields, driven by increasing oil prices and central bank rate expectations, is likely to propagate to the Indian market through the global copper channel, which leads Indian metal equities. The valid gold_silver_comove channel also suggests a potential rotation in monetary metals, which could influence the Indian market.
- **Gap**: No gap: The big raw move in US bond yields is largely priced, with resid_z values ranging from 0.27 to 1.21, indicating that the move is mostly explained by factor exposures.
- **India take**: The Indian 10-year bond yield may trade in the range of 6.60-6.90% over the next month, according to PGIM India MF's Puneet Pal, and the metal_copper_channel may lead to a reaction in Indian metal equities.
- Watch next: nifty_50 (down) — not yet - watch; Risk-off sentiment and potential safe-haven bid in gold may lead to a decline in Indian equities
- Source: 10-year bond yield may trade in 6.60-6.90% range over the next month: PGIM India MF's Puneet Pal — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/bonds/10-year-bond-yield-may-trade-in-6-60-6-90-range-over-the-next-month-pgim-india-mfs-puneet-pal/articleshow/132409495.cms
- Source: Japan PM Takaichi says draft economic blueprint not cause of bond market rout — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/bonds/japan-pm-takaichi-says-draft-economic-blueprint-not-cause-of-bond-market-rout/articleshow/132409488.cms
- Source: Euro zone bond yields tick higher along with oil prices after big swings — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/bonds/euro-zone-bond-yields-tick-higher-along-with-oil-prices-after-big-swings/articleshow/132409354.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 6.5] cross-asset · 4 series ↑
- dyn_gs [EQUITIES]: last 1141.67, z20 2.83, zc 5.08, resid-z -0.28 [priced], 1d 9.16%, |z20|=2.83; 1y-pct=100
- dyn_ms [EQUITIES]: last 228.05, z20 1.76, zc 1.78, resid-z -0.20 [priced], 1d 3.15%, 1y-pct=100
- sp500 [INDICES]: last 7544.29, z20 1.12, zc 0.49, resid-z 0.02 [quiet], 1d 0.39%, 1y-pct=96
- dow_jones [INDICES]: last 52526.74, z20 0.78, zc 0.07, resid-z -0.53 [quiet], 1d 0.05%, 1y-pct=98
- **Mechanism**: The recent surge in Goldman Sachs shares, driven by stronger-than-expected Q2 earnings, has propagated to other equities such as dyn_ms, with the S&P 500 and Dow Jones indices also experiencing upward momentum. This move is largely priced, with resid_z values indicating that the unexplained component is relatively small. The valid channels, including the gold_silver_comove and metal_copper_channel, do not suggest any inversion or weakness that would imply a contrarian move.
- **Gap**: No gap: the recent move in dyn_gs and dyn_ms is largely priced, with resid_z values close to zero, indicating that the move is largely explained by factor exposures
- **India take**: The Indian instrument dyn_justdial_bo, which has a correlation of 0.49 with dyn_gs, has already reacted to the move. Further upside in dyn_gs and dyn_ms could lead to additional gains in dyn_justdial_bo.
- Watch next: dyn_ms (up) — already moved; historical analogue suggests further upside
- Watch next: sp500 (up) — not yet - watch; historical analogue suggests further upside
- **India receivers**: dyn_justdial_bo (rho 0.49, z 3.7)
- Source: Earnings Boost: Why Goldman Sachs shares jumped to record highs — ET Markets, 2026-07-15. https://economictimes.indiatimes.com/markets/us-stocks/news/earnings-boost-why-goldman-sachs-shares-jumped-to-record-highs/slideshow/132407452.cms
- Source: This overlooked index is a better investment than the S&P 500 — MarketWatch Top, 2026-07-14. https://www.marketwatch.com/story/this-overlooked-index-is-a-better-investment-than-the-s-p-500-74c7e698?mod=mw_rss_topstories
- Source: Wall Street has set a sky-high bar for companies to clear this earnings season. They just might pull it off. — MarketWatch Top, 2026-07-14. https://www.marketwatch.com/story/wall-street-has-set-a-sky-high-bar-for-companies-to-clear-this-earnings-season-they-just-might-pull-it-off-45731862?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-17 (d=0.32), 2024-11-11 (d=0.55)

### [RED 5.7] dyn_justdial_bo ↑
- dyn_justdial_bo [EQUITIES]: last 786.00, z20 3.70, zc -0.05, resid-z -0.43 [quiet], 1d -0.55%, |z20|=3.70
- **Mechanism**: dyn_justdial_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.19).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_biocon_bo (rho 0.507 via dyn_justdial_bo, z 2.07, reacted); dyn_nuvoco_ns (rho 0.469 via dyn_justdial_bo, z 7.6, reacted); dyn_patanjali_ns (rho 0.106 via dyn_justdial_bo, leads 1d, z -16.84, reacted)
- **India receivers**: dyn_biocon_bo (rho 0.507, z 2.07); dyn_nuvoco_ns (rho 0.469, z 7.6); dyn_patanjali_ns (rho 0.106, z -16.84)
- Source: Just Dial shares rocket 36% in two days! Why Citi, Kotak, others think Reliance-backed stock can rally up to 62%? — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/stocks/news/just-dial-shares-rocket-36-in-two-days-why-citi-kotak-others-think-reliance-backed-stock-can-rally-up-to-62/articleshow/132382158.cms
- Historical analogues: 2026-06-18 (d=0.19), 2025-06-30 (d=0.52), 2026-01-07 (d=0.52)

### [RED 5.34] commodities · 2 series ↑
- brent [COMMODITIES]: last 85.50, z20 2.51, zc 0.38, resid-z 0.90 [quiet], 1d 0.91%, |z20|=2.51; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 80.11, z20 2.28, zc 0.41, resid-z 0.80 [quiet], 1d 0.97%, |z20|=2.28
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.505 via wti, z 1.74, reacted)
- Watch next: cac_40 (inverse) — not yet - watch; rho -0.576 vs brent, historically leads by 5d
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.5 vs brent, historically leads by 5d
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.542 vs brent
- **India receivers**: nifty_midcap_100 (rho -0.505, z 1.74)
- Source: Brent Futures Flip to Backwardation as Middle East Supply Risks Return — OilPrice, 2026-07-15. https://oilprice.com/Latest-Energy-News/World-News/Brent-Futures-Flip-to-Backwardation-as-Middle-East-Supply-Risks-Return.html
- Source: US-Iran war: Crude oil prices extend gains amid rising tensions in the Middle East. Can it hit $100 per barrel? — Mint Markets, 2026-07-15. https://www.livemint.com/market/commodities/usiran-war-crude-oil-prices-extend-gains-amid-rising-tensions-in-the-middle-east-can-it-hit-100-per-barrel-11784096474117.html
- Source: U.S. Backs Iraq-Syria Oil Pipeline to Bypass the Strait of Hormuz — OilPrice, 2026-07-15. https://oilprice.com/Latest-Energy-News/World-News/US-Backs-Iraq-Syria-Oil-Pipeline-to-Bypass-the-Strait-of-Hormuz.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [RED 5.03] dyn_kalyankjil_ns ↑
- dyn_kalyankjil_ns [EQUITIES]: last 544.60, z20 3.03, zc 0.36, resid-z 0.57 [quiet], 1d 2.80%, |z20|=3.03
- **Mechanism**: dyn_kalyankjil_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-01-07 (z-distance 1.76).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.561 via dyn_kalyankjil_ns, z 1.74, reacted); dyn_indianb_ns (rho 0.483 via dyn_kalyankjil_ns, z 0.02, quiet); dyn_pcjeweller_ns (rho 0.442 via dyn_kalyankjil_ns, z 2.49, reacted); nifty_50 (rho 0.398 via dyn_kalyankjil_ns, z -0.06, quiet); midcap_largecap_ratio (rho 0.391 via dyn_kalyankjil_ns, z 1.93, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.561, z 1.74); dyn_indianb_ns (rho 0.483, z 0.02); dyn_pcjeweller_ns (rho 0.442, z 2.49); nifty_50 (rho 0.398, z -0.06)
- Source: Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. Time to buy or book profits? — ET Markets, 2026-07-14. https://economictimes.indiatimes.com/markets/stocks/news/kalyan-jewellers-shares-skyrocket-50-in-5-days-market-value-swells-by-rs-18200-crore-time-to-buy-or-book-profits/articleshow/132382065.cms
- Historical analogues: 2026-01-07 (d=1.76), 2026-06-15 (d=1.78), 2025-07-02 (d=2.84)

### [RED 4.93] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.62, z20 1.93, zc n/a, resid-z n/a [quiet], 1d 0.20%, 52-wk extreme (pct=99); |z20|=1.93; 1y-pct=99
- **Mechanism**: The midcap_largecap_ratio has reached a 52-week extreme, with a z20 level of 1.84, indicating a significant move. However, the resid_z is None, suggesting that this move is largely priced in by factor exposures. The valid channels, such as gold_silver_comove and metal_copper_channel, do not directly relate to this event, but the vix_equity_inverse channel may influence the broader market sentiment.
- **Gap**: No gap: the move is largely priced in, as indicated by the None resid_z value
- **India take**: The Indian instruments, such as nifty_midcap_100 and dyn_kalyankjil_ns, have already reacted to this move, while others like dyn_indianb_ns and dyn_swiggy_ns remain quiet. The reaction in the Indian market is likely to be limited, given the priced-in nature of the event.
- Watch next: nifty_midcap_100 (down) — already moved; high correlation with midcap_largecap_ratio
- **India receivers**: nifty_midcap_100 (rho 0.545, z 1.74); dyn_kalyankjil_ns (rho 0.391, z 3.03); dyn_indianb_ns (rho 0.364, z 0.02)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

## Watchlist (below surfacing floor)
commodities · 2 series ↑ (4.83), dyn_pcjeweller_ns ↑ (4.49), dyn_atherenerg_ns ↑ (4.26), usd_inr ↑ (4.16), dyn_bac ↑ (4.15), dyn_meta ↑ (4.12), dyn_biocon_bo ↑ (4.07), natgas ↓ (3.95), gold_silver_ratio ↑ (3.74), dyn_cupid_ns ↑ (3.7), dyn_tataelxsi_ns ↓ (3.67), shanghai_comp ↓ (3.6)

## India macro
- nifty_50: 24073.4492 (1d 0.16%, z20 -0.06, flag none)
- nifty_midcap_100: 63001.5508 (1d 0.36%, z20 1.74, flag amber)
- usd_inr: 96.2550 (1d -0.05%, z20 2.16, flag amber)
- goi_10y: 7.0200 (1d -0.43%, z20 1.89, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.6300 (1d -3.31%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6171 (1d 0.20%, z20 1.93, flag red)
- Next India prints: NSDL FPI flows T-0d · India trade / CAD data T-0d · RBI Weekly Statistical Supplement T-2d · Kharif sowing data T-2d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 50.7 — "Q1 results 2026: Groww to Union Bank among companies to declare Q1 results today; full lis"
- HDB (HDFC Bank Limited) score 46.7 — "Q1 results 2026: Groww to Union Bank among companies to declare Q1 results today; full lis"
- INOXINDIA.NS (INOX INDIA LIMITED) score 45.3 — "Revised US Russia sanctions bill lowers proposed tariffs on China, India"
- COIN (Coinbase Global, Inc.) score 44.1 — "Gift Nifty points to flat opening; earnings, global cues to drive markets today"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 43.2 — "Q1 results 2026: Groww to Union Bank among companies to declare Q1 results today; full lis"
- BOND (PIMCO Active Bond Exchange-Tra) score 20.9 — "China CITIC Bank International plans dollar, offshore yuan perpetual bonds"
- BAC (Bank of America Corporation) score 17.3 — "Q1 results 2026: Groww to Union Bank among companies to declare Q1 results today; full lis"
- CHKP (Check Point Software Technolog) score 17.0 — "Stocks to watch: Groww, Delhivery, NBCC among shares in focus today; check list here"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 16.4 — "L&T Technology Services’ healthy start to FY27 lifts investor spirits"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 15.8 — "Crude oil futures gain as Trump threatens strikes on Iran’s energy targets"
- SKHYV (SK hynix Inc. American Deposit) score 12.7 — "Global Market: SK Hynix jumps 13% as easing US inflation, AI memory optimism lift chip sto"
- VT (Vanguard Total World Stock Ind) score 12.5 — "Alpine Texworld IPO Day 2: Here's GMP, subscription status, other details. Apply or not?"
- JUSTDIAL.BO (JUST DIAL LTD.) score 11.6 — "101 equity mutual funds doubled money in 5 years; 4 did it in just 3 years. Should you inv"
- PCJEWELLER.NS (PC JEWELLER LTD) score 7.1 — "Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. T"
- META (Meta) score 6.8 — "Global Market: China Q2 growth slows to 4.3% yoy; Asia, metals stocks likely to remain vol"
- KALYANKJIL.NS (KALYAN JEWELLERS IND LTD) score 6.6 — "Kalyan Jewellers shares skyrocket 50% in 5 days, market value swells by Rs 18,200 crore. T"
- QESSF (AEGIS CRITICAL ENERGY DEFENCE ) score 5.5 — "PL Capital raises Nifty target to 27,019; favours banks, NBFCs, capital goods and defence"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.3 — "Adani ducks headwinds to record a huge jump in realty fortune; at cusp of being richest in"
- GS (Goldman Sachs Group, Inc. (The) score 5.1 — "Earnings Boost: Why Goldman Sachs shares jumped to record highs"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 4.6 — "Tata Elxsi shares hit 52-week low as margin miss weighs on sentiment"
- MS (Morgan Stanley) score 4.2 — "JPMorgan posts record profit on big gains from dealmaking, stock trading"
- BIOCON.BO (BIOCON LTD.) score 4.0 — "Mylan exits Biocon, sells entire 5.64% stake for ₹3,679 crore via block deals"
- SWIGGY.NS (SWIGGY LIMITED) score 3.5 — "Top Gainers & Losers on 14 July: HCL Tech, Ceat, Swiggy, Anant Raj, Newgen Software Tech a"
- MU (Micron Technology, Inc.) score 2.8 — "Micron and other chip stocks feel the pain of imported volatility — blame SK Hynix"
- CUPID.NS (CUPID LIMITED) score 2.7 — "Cupid shares jump 5%, multibagger stock turns Rs 1 lakh investment into Rs 87 lakh in just"
- OLAELEC.NS (OLA ELECTRIC MOBILITY LTD) score 2.7 — "CUBA'S NATIONAL ELECTRIC GRID COLLAPSES, SAYS CUBA'S STATE MEDIA"
- IDBI.NS (IDBI BANK LIMITED) score 2.6 — "IDBI Bank shares jump 3% as Fairfax set to make biggest foreign investment in Indian lende"
- BHARTIARTL.NS (BHARTI AIRTEL LIMITED) score 2.3 — "Mcap of 4 of top-10 most valued firms jumps ₹92,995 crore; HDFC Bank, Airtel top gainers"
- HEROMOTOCO.NS (HERO MOTOCORP LIMITED) score 2.0 — "Ather Energy shares rally 6% after Hero MotoCorp approves Rs 1,000 crore additional invest"
- NUVOCO.NS (NUVOCO VISTAS CORP LTD) score 2.0 — "Nuvoco Vistas shares soar 10% after strong Q1. Why Nomura, Choice see up to 47% upside?"
- PATANJALI.NS (PATANJALI FOODS LIMITED) score 2.0 — "Patanjali Foods share price crashes 20%, extending losses for third straight session; what"
- JEF (Jefferies Financial Group Inc.) score 1.8 — "Greed and Fear report: Christopher Wood sees 'AI fatigue' setting in. Why Jefferies is tur"
- LGDS (JPMorgan Fundamental Data Scie) score 1.7 — "JPMorgan posts record profit on big gains from dealmaking, stock trading"
- MCAP (MCAP Inc.) score 1.6 — "Mcap of 4 of top-10 most valued firms jumps ₹92,995 crore; HDFC Bank, Airtel top gainers"
- DRREDDY.NS (DR. REDDY S LABORATORIES) score 1.2 — "Broker’s call: Dr Reddy’s Lab (Accumulate)"
- BLK (BlackRock, Inc.) score 1.0 — "SBI Funds IPO anchor book 20 times subscribed; draws Capital Group, BlackRock, Goldman, AD"
- KNACK.BO (KNACK PACKAGING LIMITED) score 1.0 — "Knack Packaging shares list at 11% premium; expert sees further upside"
- AVGO (Broadcom Inc.) score 0.7 — "Is Broadcom stock a buy after Apple's massive chip pact?"
- HLIO (Helios Technologies, Inc.) score 0.6 — "Adani flagship is the next big India pick for Singapore’s Helios"
- WULF (TeraWulf Inc.) score 0.4 — "TeraWulf’s stock gains after a $19 billion deal with Anthropic"

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