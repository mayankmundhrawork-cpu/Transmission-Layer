# Transmission Layer — board brief · 2026-09-15 22:53Z

data as of **2026-09-15** · 97 series · 22 red / 37 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.749, 4d in regime; vol-pct 0.616, breadth-off 0.882, Markov P(high-vol) 0.017)
- [INVERTED] **safe_haven_gold** — corr20 -0.56, corr60 -0.3, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.78, corr60 0.87, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.13, corr60 0.31, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.19, corr60 0.14, last shift 2026-06-05. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.89, corr60 -0.84, last shift 2026-07-22. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.12, corr60 -0.03, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.08, last shift 2026-07-23. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.19, corr60 0.14, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 0.003076390423476072)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.495** (n=1111) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.819** (n=2069) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 11.01] cross-asset · 18 series ↓
- tips_10y_real [RATES]: last 2.60, z20 2.73, zc 0.00, resid-z -0.81 [quiet], 1d 0.00%, |z20|=2.73; 1y-pct=99
- dyn_vt [EQUITIES]: last 158.02, z20 -2.66, zc -0.55, resid-z -0.67 [quiet], 1d -0.45%, |z20|=2.66
- ust_2y [RATES]: last 4.65, z20 2.64, zc 0.33, resid-z -0.45 [quiet], 1d 0.43%, |z20|=2.64; 1y-pct=100
- dyn_ms [EQUITIES]: last 206.23, z20 -2.60, zc -0.09, resid-z -1.98 [unexplained], 1d -0.17%, |z20|=2.60
- ust_10y [RATES]: last 4.97, z20 2.55, zc 0.20, resid-z -0.34 [quiet], 1d 0.20%, |z20|=2.55; 1y-pct=100
- wti [COMMODITIES]: last 105.40, z20 2.54, zc 1.34, resid-z 1.07 [quiet], 1d 3.96%, 1-session move +3.96% ≥ 1.5%; |z20|=2.54; 1y-pct=96
- stoxx_50 [INDICES]: last 6237.52, z20 -2.52, zc -0.38, resid-z -0.17 [quiet], 1d -0.37%, |z20|=2.52
- brent [COMMODITIES]: last 108.32, z20 2.33, zc 0.85, resid-z 0.51 [quiet], 1d 2.50%, 1-session move +2.50% ≥ 1.5%; |z20|=2.33; co-occur[inr_oil] suppressed: channel WEAK
- sp500 [INDICES]: last 7585.51, z20 -2.24, zc -0.59, resid-z 0.30 [quiet], 1d -0.45%, |z20|=2.24
- dyn_bond [EQUITIES]: last 88.65, z20 -2.23, zc -0.33, resid-z -0.01 [quiet], 1d -0.11%, |z20|=2.23; 1y-pct=0
- russell_2000 [INDICES]: last 2869.79, z20 -2.20, zc -0.66, resid-z -0.53 [quiet], 1d -0.78%, |z20|=2.20
- dow_jones [INDICES]: last 52092.45, z20 -2.19, zc -0.78, resid-z -0.37 [quiet], 1d -0.63%, |z20|=2.19
- cac_40 [INDICES]: last 8098.38, z20 -1.93, zc -0.27, resid-z 0.00 [quiet], 1d -0.24%, |z20|=1.93
- dax [INDICES]: last 25420.42, z20 -1.91, zc -0.09, resid-z 0.27 [quiet], 1d -0.08%, |z20|=1.91
- vix [INDICES]: last 17.21, z20 1.87, zc 0.07, resid-z n/a [quiet], 1d 0.64%, |z20|=1.87
- nasdaq_100 [INDICES]: last 28937.75, z20 -1.87, zc -0.62, resid-z 0.09 [quiet], 1d -0.65%, |z20|=1.87
- ust_30y [RATES]: last 5.34, z20 1.73, zc -0.24, resid-z -0.58 [quiet], 1d -0.19%, |z20|=1.73; 1y-pct=99
- ftse_100 [INDICES]: last 10654.36, z20 -1.59, zc -0.65, resid-z -0.54 [quiet], 1d -0.40%, |z20|=1.59
- **Mechanism**: cross-asset · 18 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.516 via ftse_100, z -1.12, reacted); nifty_midcap_100 (rho 0.477 via dax, z -4.2, reacted); dyn_techm_ns (rho 0.419 via ftse_100, z -0.31, quiet); midcap_largecap_ratio (rho -0.402 via ust_2y, z -0.81, quiet); nifty_50 (rho 0.385 via ftse_100, z -3.0, reacted)
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.559 vs sp500, historically leads by 1d
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.505 vs cac_40, historically leads by 5d
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.611 vs dyn_vt
- **India receivers**: nifty_it (rho 0.516, z -1.12); nifty_midcap_100 (rho 0.477, z -4.2); dyn_techm_ns (rho 0.419, z -0.31); midcap_largecap_ratio (rho -0.402, z -0.81)
- Source: Hormuz Risk Opens $40-Plus Price Gap Between Crude Grades — OilPrice, 2026-09-15. https://oilprice.com/Energy/Crude-Oil/Hormuz-Risk-Opens-40-Plus-Price-Gap-Between-Crude-Grades.html
- Source: It Costs a Record $44.8 Million to Ship US Crude Oil to Asia — Mint Markets, 2026-09-15. https://www.livemint.com/market/it-costs-a-record-44-8-million-to-ship-us-crude-oil-to-asia-11789507070739.html
- Source: U.S. Oil Inventories Jump as Cushing Stocks Keep Falling — OilPrice, 2026-09-15. https://oilprice.com/Latest-Energy-News/World-News/US-Oil-Inventories-Jump-as-Cushing-Stocks-Keep-Falling.html

### [RED 8.86] cross-asset · 4 series ↓
- india_vix [INDICES]: last 13.47, z20 5.20, zc 0.74, resid-z n/a [quiet], 1d 9.56%, |z20|=5.20
- nifty_midcap_100 [INDICES]: last 60876.10, z20 -4.20, zc -0.40, resid-z -0.44 [quiet], 1d -2.12%, |z20|=4.20
- nifty_50 [INDICES]: last 23118.60, z20 -3.00, zc -0.61, resid-z -0.80 [quiet], 1d -1.19%, |z20|=3.00; 1y-pct=4
- dyn_jiofin_bo [EQUITIES]: last 226.00, z20 -2.50, zc -0.35, resid-z 0.41 [quiet], 1d -1.74%, |z20|=2.50; 1y-pct=0
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-17 (z-distance 0.67).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.622 via nifty_50, z -1.86, reacted); dyn_indianb_ns (rho 0.554 via nifty_midcap_100, z -3.34, reacted); nifty_it (rho 0.51 via nifty_50, z -1.12, reacted); dyn_indusindbk_bo (rho 0.464 via nifty_50, z -3.42, reacted); dyn_techm_ns (rho 0.463 via nifty_50, z -0.31, quiet)
- **India receivers**: nifty_fmcg (rho 0.622, z -1.86); dyn_indianb_ns (rho 0.554, z -3.34); nifty_it (rho 0.51, z -1.12); dyn_indusindbk_bo (rho 0.464, z -3.42)
- Source: Crude shock, bond jitters send Sensex, Nifty into a rout — BusinessLine Mkts, 2026-09-15. https://www.thehindubusinessline.com/markets/crude-shock-bond-jitters-send-sensex-nifty-into-a-rout/article71468059.ece
- Source: Expert View: Don’t wait for Nifty to stabilise, buy the dip, says Shweta Rajani of Anand Rathi Wealth — Mint Markets, 2026-09-15. https://www.livemint.com/market/stock-market-news/expert-view-don-t-wait-for-nifty-to-stabilise-buy-the-dip-says-shweta-rajani-of-anand-rathi-wealth-11789471660373.html
- Source: CAS crash: Nifty plunges 462 points in less than 30 seconds. Will Sebi’s review break trend? — ET Markets, 2026-09-15. https://economictimes.indiatimes.com/markets/stocks/news/cas-crash-nifty-plunges-462-points-in-less-than-30-seconds-will-sebis-review-break-trend/articleshow/134260167.cms
- Historical analogues: 2025-07-17 (d=0.67), 2025-12-19 (d=1.13), 2024-11-07 (d=1.15)

### [AMBER 6.21] usd_inr ↑
- usd_inr [FX]: last 95.85, z20 1.21, zc 1.48, resid-z 1.49 [quiet], 1d 0.86%, 20d range extreme; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Rupee slumps 38 paise to close at 95.92 against US dollar — ET Markets, 2026-09-15. https://economictimes.indiatimes.com/markets/forex/rupee-slumps-38-paise-to-close-at-95-92-against-us-dollar/articleshow/134259296.cms
- Source: Rupee drops with stocks, bonds as oil, inflation and Fed worries mount — BusinessLine Mkts, 2026-09-15. https://www.thehindubusinessline.com/markets/forex/rupee-drops-with-stocks-bonds-as-oil-inflation-and-fed-worries-mount/article71467588.ece
- Source: RBI likely intervened to shield rupee as oil prices climb, traders say — BusinessLine Mkts, 2026-09-15. https://www.thehindubusinessline.com/markets/forex/rbi-likely-intervened-to-shield-rupee-as-oil-prices-climb-traders-say/article71466683.ece
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2024-10-24 (d=0.01)

### [RED 6.08] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 5360.00, z20 4.08, zc 1.56, resid-z 3.20 [unexplained], 1d 8.83%, |z20|=4.08; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: From VBL, Power Grid to Paytm - 6 stocks experts recommend buying for the short term; do you own any? — Mint Markets, 2026-09-15. https://www.livemint.com/market/stock-market-news/from-vbl-power-grid-to-paytm-6-stocks-experts-recommend-buying-for-the-short-term-do-you-own-any-11789451473678.html
- Source: HDFC Bank share price jumps over 6% in 3 days | Experts see 15% more upside, check target price — Mint Markets, 2026-09-15. https://www.livemint.com/market/stock-market-news/hdfc-bank-share-price-jumps-over-6-in-3-days-experts-see-15-more-upside-check-target-price-11789444548891.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

### [AMBER 5.28] fx · 2 series ↓
- eur_usd [FX]: last 1.15, z20 -2.45, zc -1.48, resid-z -1.47 [quiet], 1d -0.44%, |z20|=2.45
- gbp_usd [FX]: last 1.35, z20 -1.77, zc -0.94, resid-z -1.04 [quiet], 1d -0.37%, |z20|=1.77
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.395 via gbp_usd, z -1.93, reacted); nifty_50 (rho 0.367 via eur_usd, z -3.0, reacted)
- Watch next: aud_usd (co-move) — not yet - watch; rho 0.629 vs eur_usd, historically leads by 5d
- **India receivers**: dyn_muthootfin_ns (rho 0.395, z -1.93); nifty_50 (rho 0.367, z -3.0)
- Source: Piero Cipollone: The future of euro cash: trusted today, designed for tomorrow — ECB press, 2026-09-14. https://www.ecb.europa.eu//press/key/date/2026/html/ecb.sp260914_1~91d3436449.en.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [RED 5.18] dyn_jef ↓
- dyn_jef [EQUITIES]: last 48.86, z20 -3.18, zc -0.90, resid-z -1.05 [quiet], 1d -2.48%, |z20|=3.18
- **Mechanism**: dyn_jef ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Even Nikhil Kamath is a YouTuber! Jefferies calls Zerodha co-founder a ‘renowned YouTube Podcaster’ - Why this matters? — Mint Markets, 2026-09-15. https://www.livemint.com/market/stock-market-news/even-nikhil-kamath-is-a-youtuber-jefferies-calls-zerodha-co-founder-a-renowned-youtube-podcaster-why-this-matters-11789460259445.html
- Source: Coforge shares fall over 3%. What are Jefferies, Emkay saying after Chairman, independent director exit? — ET Markets, 2026-09-15. https://economictimes.indiatimes.com/markets/stocks/news/coforge-shares-fall-over-3-what-are-jefferies-emkay-saying-after-chairman-independent-director-exit/articleshow/134256354.cms
- Source: HDFC Bank share price target: What are Jefferies, 3 other foreign brokerages saying as CEO hunt intensifies? — ET Markets, 2026-09-15. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-bank-share-price-target-what-are-jefferies-3-other-foreign-brokerages-saying-as-ceo-hunt-intensifies/articleshow/134253758.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-01 (d=0.04), 2025-08-19 (d=0.07)

### [RED 5.02] dyn_bac ↓
- dyn_bac [EQUITIES]: last 59.49, z20 -3.02, zc 0.01, resid-z -4.20 [unexplained], 1d 0.03%, |z20|=3.02
- **Mechanism**: dyn_bac ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: WALL STREET OVERWHELMINGLY EXPECTS FED HIKE Nearly every major Wall Street bank now expects the Federal Reserve to raise rates in September, according to a WSJ survey. Most forecast 50 basis points of total tightening in 2026, while Bank of America, Deutsche Bank and RBC see 75bps. Market angle: exp — DeItaone, 2026-09-15. https://t.me/walter_bloomberg/35811
- Source: The 10 most overvalued housing markets in America — MarketWatch Top, 2026-09-14. https://www.marketwatch.com/story/the-10-most-overvalued-housing-markets-in-america-6d28efdf?mod=mw_rss_topstories
- Source: TRUMP: “DON’T KILL THE GOLDEN GOOSE” President Trump says America’s AI and data center boom is happening because the U.S. holds a commanding global lead. He urged against measures that could slow the industry’s expansion, warning policymakers: “Don’t kill the Golden Goose!” — DeItaone, 2026-09-14. https://t.me/walter_bloomberg/35759
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

### [AMBER 4.85] indices · 2 series ↓
- nikkei_225 [INDICES]: last 63611.84, z20 -2.02, zc 0.13, resid-z 0.25 [quiet], 1d 0.19%, |z20|=2.02
- shanghai_comp [INDICES]: last 3865.00, z20 -1.96, zc -0.72, resid-z -0.29 [quiet], 1d -0.52%, |z20|=1.96
- **Mechanism**: indices · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-16 (z-distance 0.84).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_techm_ns (rho -0.547 via shanghai_comp, z -0.31, quiet); nifty_it (rho -0.473 via shanghai_comp, z -1.12, reacted); midcap_largecap_ratio (rho 0.386 via shanghai_comp, z -0.81, quiet)
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.77 vs nikkei_225
- Watch next: aud_usd (co-move) — not yet - watch; rho 0.501 vs nikkei_225, historically leads by 3d
- Watch next: dyn_techm_ns (inverse) — not yet - watch; rho -0.547 vs shanghai_comp
- **India receivers**: dyn_techm_ns (rho -0.547, z -0.31); nifty_it (rho -0.473, z -1.12); midcap_largecap_ratio (rho 0.386, z -0.81)
- Source: Stock Market prediction tomorrow: Sensex, Nifty outlook for Wed | Kospi, Taiwan Index, Nikkei cues to watch | 16 Sept — Mint Markets, 2026-09-15. https://www.livemint.com/market/stock-market-prediction-tomorrow-sensex-nifty-outlook-for-wed-kospi-taiwan-index-nikkei-cues-to-watch-16-sept-11789465506120.html
- Source: Stock Market prediction today: Sensex, Nifty outlook for Wed | Kospi, Taiwan Index, Nikkei cues to watch | 16 Sept — Mint Markets, 2026-09-15. https://www.livemint.com/market/stock-market-prediction-tomorrow-sensex-nifty-outlook-for-wed-kospi-taiwan-index-nikkei-cues-to-watch-16-sept-11789465506120.html
- Source: Global Market: Japan’s Nikkei rises 1% as SoftBank rebounds from AI selloff — ET Markets, 2026-09-15. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-rises-1-as-softbank-rebounds-from-ai-selloff/articleshow/134252512.cms
- Historical analogues: 2025-07-16 (d=0.84), 2025-12-23 (d=1.2), 2026-06-12 (d=1.31)

## Watchlist (below surfacing floor)
dyn_tatatech_ns ↓ (4.39), dyn_icicigi_bo ↓ (4.18), usd_mxn ↑ (3.79), comex_gold ↓ (3.75), nifty_metal ↓ (3.5), dyn_indusindbk_bo ↓ (3.42), dyn_indianb_ns ↓ (3.34), gold_silver_ratio ↓ (3.13), dyn_lenskart_ns ↑ (3.01), dyn_hdb ↓ (2.92), asx_200 ↓ (2.86), brent_wti_spread ↓ (2.76)

## India macro
- nifty_50: 23118.5996 (1d -1.19%, z20 -3.00, flag red)
- nifty_midcap_100: 60876.1016 (1d -2.12%, z20 -4.20, flag red)
- usd_inr: 95.8490 (1d 0.86%, z20 1.21, flag amber)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6332 (1d -0.94%, z20 -0.81, flag none)
- Next India prints: NSDL FPI flows T-0d · India trade / CAD data T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 62.2 — "RUSSIAN OIL PREMIUMS SURGE AS MIDDLE EAST SUPPLY TIGHTENS Russian Urals crude premiums in "
- COALINDIA.NS (COAL INDIA LTD) score 61.8 — "RUSSIAN OIL PREMIUMS SURGE AS MIDDLE EAST SUPPLY TIGHTENS Russian Urals crude premiums in "
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 60.8 — "RUSSIAN OIL PREMIUMS SURGE AS MIDDLE EAST SUPPLY TIGHTENS Russian Urals crude premiums in "
- INDIANB.NS (INDIAN BANK) score 60.4 — "WALL STREET OVERWHELMINGLY EXPECTS FED HIKE Nearly every major Wall Street bank now expect"
- COIN (Coinbase Global, Inc.) score 53.1 — "SAUDI OIL PIPELINE COULD RESTART WITHIN DAYS Saudi Arabia’s critical East-West Pipeline co"
- BAC (Bank of America Corporation) score 50.4 — "WALL STREET OVERWHELMINGLY EXPECTS FED HIKE Nearly every major Wall Street bank now expect"
- HDB (HDFC Bank Limited) score 44.1 — "WALL STREET OVERWHELMINGLY EXPECTS FED HIKE Nearly every major Wall Street bank now expect"
- BOND (PIMCO Active Bond Exchange-Tra) score 42.1 — "BESSENT: TREASURY'S BOND BUYBACK INTERVENTION WAS SUCCESSFUL"
- IDBI.NS (IDBI BANK LIMITED) score 42.0 — "WALL STREET OVERWHELMINGLY EXPECTS FED HIKE Nearly every major Wall Street bank now expect"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 42.0 — "WALL STREET OVERWHELMINGLY EXPECTS FED HIKE Nearly every major Wall Street bank now expect"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 42.0 — "WALL STREET OVERWHELMINGLY EXPECTS FED HIKE Nearly every major Wall Street bank now expect"
- OHI (Omega Healthcare Investors, In) score 41.8 — "Top stocks in focus today: Investors must watch NBCC, BHEL, Bharat Forge shares on Wednesd"
- CHKP (Check Point Software Technolog) score 36.3 — "BESSENT: EXAMINING $5,000 CHECK PROPOSAL AT TREASURY"
- TECHM.NS (TECH MAHINDRA LIMITED) score 32.8 — "NHAI extends debarment to PNC Infratech; stock hits 52-week low"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 32.8 — "NHAI extends debarment to PNC Infratech; stock hits 52-week low"
- TECH (Bio-Techne Corp) score 32.8 — "NHAI extends debarment to PNC Infratech; stock hits 52-week low"
- 301077.SZ (CHINASTARS) score 27.9 — "JOHNSON SAYS AI MORATORIUM WILL LOSE COMPETITIVE EDGE TO CHINA"
- SEPN (Septerna, Inc.) score 25.9 — "WALL STREET OVERWHELMINGLY EXPECTS FED HIKE Nearly every major Wall Street bank now expect"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.3 — "SAUDI OIL PIPELINE COULD RESTART WITHIN DAYS Saudi Arabia’s critical East-West Pipeline co"
- LTH (Life Time Group Holdings, Inc.) score 20.7 — "U.S., GULF STATES EXPAND HORMUZ TANKER TRANSITS The U.S. military and Gulf countries have "
- TATAELXSI.NS (TATA ELXSI LIMITED) score 12.2 — "Afcons Infra stock surges on Tata Sons listing hopes. Is a re-rating on the cards?"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 12.2 — "Afcons Infra stock surges on Tata Sons listing hopes. Is a re-rating on the cards?"
- NVDA (NVIDIA Corporation) score 10.4 — "BESSENT: TRUMP COMPLETELY ALIGNED WITH NVIDIA'S JENSEN HUANG"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.8 — "TRUMP BLASTS SUPREME COURT OVER MAJOR RULINGS President Trump sharply criticized the U.S. "
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 8.5 — "Indian government allocates record sugar sales quota for September to rein in retail price"
- JIOFIN.BO (Jio Financial Services Limited) score 8.1 — "BESSENT: WE HAVE HAD GOOD PRIVATE DISCUSSIONS WITH CHINA ON IRANIAN FINANCIAL LINKS"
- MS (Morgan Stanley) score 7.4 — "MORGAN STANLEY'S DAN SIMKOWITZ SAYS WE ARE IN RELATIVELY EARLY TO MIDDLE INNINGS OF AI FIN"
- VT (Vanguard Total World Stock Ind) score 6.7 — "BESSENT SAYS U.S. BOND MARKET IS THE BEST-PERFORMING IN THE WORLD"
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.4 — "All that glitters... in jewellers’ IPO boom"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 6.2 — "BESSENT SAYS WE HAVE SEEN SOME FORWARD FACING STATEMENTS FROM UNITED ARAB EMIRATES TO CUT "
- JEF (Jefferies Financial Group Inc.) score 5.8 — "HDFC Bank share price target: What are Jefferies, 3 other foreign brokerages saying as CEO"
- BZ=F (Brent Crude Oil Last Day Finan) score 5.8 — "TRUMP BLASTS SUPREME COURT OVER MAJOR RULINGS President Trump sharply criticized the U.S. "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.7 — "Tech picks: Adani Ports, Data Patterns among 5 stocks that could give up to 23% returns in"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 4.5 — "HDFC Bank share price jumps over 6% in 3 days | Experts see 15% more upside, check target "
- ICICIGI.BO (ICICI Lombard General Insuranc) score 4.4 — "ICICI Prudential MF, Kotak MF top buyers in SS Retail's Rs 146 crore anchor round before I"
- META (Meta) score 4.0 — "Gold and silver prices crash up to 2% on MCX- What is driving precious metals down?"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 1.2 — "Stocks to watch, Sept 15: HDFC Bank, BSE, broking firms, HCL Tech, Deccan Gold Mines, CESC"
- DELL (Dell Technologies Inc.) score 0.7 — "Why Dell and HPE were the S&P 500’s top-performing stocks today"
- DKS (Dick's Sporting Goods Inc) score 0.0 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- VOLTAS.NS (VOLTAS LTD) score 0.0 — "Voltas reported strong growth in June quarter, but failed to impress"

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