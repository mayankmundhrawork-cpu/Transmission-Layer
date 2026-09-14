# Transmission Layer — board brief · 2026-09-14 21:47Z

data as of **2026-09-14** · 97 series · 13 red / 43 amber · 8 events surfaced (30 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.598, 1d in regime; vol-pct 0.462, breadth-off 0.733, Markov P(high-vol) 0.019)
- [INVERTED] **safe_haven_gold** — corr20 -0.51, corr60 -0.35, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.81, corr60 0.88, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.13, corr60 0.31, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.16, corr60 0.13, last shift 2026-06-05. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.87, corr60 -0.83, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.11, corr60 -0.03, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.31, corr60 -0.16, last shift 2026-06-26. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.1, corr60 0.07, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 3.956591173648327e-05)
- **SETUP** dyn_ms → asx_200: leads 1d (ccf 0.489, β 0.1971, p 0.0); driver zc -2.14 → expected -0.715%. Type hit-rate 0.818 (n=2011).
- **SETUP** dyn_bac → asx_200: leads 1d (ccf 0.473, β 0.2342, p 0.0); driver zc -3.69 → expected -1.203%. Type hit-rate 0.818 (n=2011).
- **SETUP** dyn_ms → nikkei_225: leads 1d (ccf 0.416, β 0.3448, p 0.0); driver zc -2.14 → expected -1.251%. Type hit-rate 0.818 (n=2011).
- **SETUP** dyn_ms → taiwan_weighted: leads 1d (ccf 0.39, β 0.3212, p 0.0); driver zc -2.14 → expected -1.166%. Type hit-rate 0.818 (n=2011).
- **SETUP** dyn_coin → aud_usd: leads 1d (ccf 0.263, β 0.0321, p 0.00024); driver zc 1.88 → expected 0.296%. Type hit-rate 0.818 (n=2011).
- Track record · residual_reversion: hit-rate **0.495** (n=1111) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=2011) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.62] cross-asset · 5 series ↑
- tips_10y_real [RATES]: last 2.60, z20 3.69, zc 1.10, resid-z 1.46 [quiet], 1d 1.96%, 1d move +5.0bps ≥ 5bps; |z20|=3.69; 1y-pct=100
- ust_2y [RATES]: last 4.63, z20 3.12, zc 1.16, resid-z 1.39 [quiet], 1d 1.54%, |z20|=3.12; 1y-pct=100
- ust_10y [RATES]: last 4.96, z20 3.00, zc 0.20, resid-z 0.38 [quiet], 1d 0.20%, |z20|=3.00; 1y-pct=100
- dyn_bond [EQUITIES]: last 88.75, z20 -2.50, zc -0.27, resid-z -0.80 [quiet], 1d -0.10%, |z20|=2.50; 1y-pct=0
- ust_30y [RATES]: last 5.35, z20 2.27, zc -0.47, resid-z -0.34 [quiet], 1d -0.37%, |z20|=2.27; 1y-pct=99
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dxy (co-move) — not yet - watch; rho 0.52 vs tips_10y_real
- Source: 10-year Treasury yield hits 5% as oil prices jump and Fed meeting looms — MarketWatch Top, 2026-09-14. https://www.marketwatch.com/story/10-year-treasury-yield-tops-5-for-the-first-time-since-2007-as-bond-market-selloff-deepens-14c81f75?mod=mw_rss_topstories
- Source: 10-year Treasury yield hits highest level since 2023 as US Federal Reserve decision looms — Mint Markets, 2026-09-14. https://www.livemint.com/market/stock-market-news/10year-treasury-yield-hits-highest-level-since-2023-as-us-federal-reserve-decision-looms-11789400968499.html
- Source: 10-year Treasury yield briefly tops 5%, hitting its highest level since 2007 as bond-market selloff deepens — MarketWatch Top, 2026-09-14. https://www.marketwatch.com/story/10-year-treasury-yield-tops-5-for-the-first-time-since-2007-as-bond-market-selloff-deepens-14c81f75?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 10.06] cross-asset · 10 series ↓
- dyn_ms [EQUITIES]: last 206.60, z20 -3.15, zc -2.14, resid-z -0.11 [priced], 1d -3.63%, |z20|=3.15
- stoxx_50 [INDICES]: last 6254.56, z20 -2.56, zc -1.21, resid-z -1.15 [quiet], 1d -1.12%, |z20|=2.56
- wti [COMMODITIES]: last 101.89, z20 2.29, zc 0.58, resid-z 0.46 [quiet], 1d 1.84%, 1-session move +1.84% ≥ 1.5%; |z20|=2.29
- brent [COMMODITIES]: last 106.15, z20 2.26, zc 0.45, resid-z 0.30 [quiet], 1d 1.47%, |z20|=2.26
- dax [INDICES]: last 25415.49, z20 -2.22, zc -0.63, resid-z -0.28 [quiet], 1d -0.60%, |z20|=2.22
- dyn_vt [EQUITIES]: last 158.72, z20 -2.12, zc -0.93, resid-z 0.03 [quiet], 1d -0.76%, |z20|=2.12
- vix [INDICES]: last 17.10, z20 2.02, zc 0.86, resid-z n/a [quiet], 1d 7.95%, |z20|=2.02
- cac_40 [INDICES]: last 8112.78, z20 -1.99, zc -0.89, resid-z -0.64 [quiet], 1d -0.82%, |z20|=1.99
- russell_2000 [INDICES]: last 2892.41, z20 -1.88, zc -0.33, resid-z 0.29 [quiet], 1d -0.40%, |z20|=1.88
- dow_jones [INDICES]: last 52421.57, z20 -1.65, zc -0.34, resid-z 0.31 [quiet], 1d -0.29%, |z20|=1.65
- **Mechanism**: cross-asset · 10 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-10-21 (z-distance 0.83).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.48 via dax, z -2.39, reacted)
- Watch next: dyn_hdb (co-move) — not yet - watch; rho 0.502 vs cac_40, historically leads by 5d
- **India receivers**: nifty_midcap_100 (rho 0.48, z -2.39)
- Source: The oil market is sending an increasingly loud warning about gas prices at the pump — MarketWatch Top, 2026-09-14. https://www.marketwatch.com/story/the-oil-market-is-sending-an-increasingly-loud-warning-about-gas-prices-at-the-pump-18177588?mod=mw_rss_topstories
- Source: Emerging-Market Assets Fall as Oil Surge, AI Jitters Dent Mood — Mint Markets, 2026-09-14. https://www.livemint.com/market/emergingmarket-assets-fall-as-oil-surge-ai-jitters-dent-mood-11789418890064.html
- Source: 10-year Treasury yield hits 5% as oil prices jump and Fed meeting looms — MarketWatch Top, 2026-09-14. https://www.marketwatch.com/story/10-year-treasury-yield-tops-5-for-the-first-time-since-2007-as-bond-market-selloff-deepens-14c81f75?mod=mw_rss_topstories
- Historical analogues: 2024-10-21 (d=0.83), 2024-11-11 (d=0.85), 2024-11-25 (d=0.9)

### [AMBER 7.51] cross-asset · 3 series ↓
- comex_copper [COMMODITIES]: last 6.40, z20 -1.93, zc -0.51, resid-z -0.02 [quiet], 1d -1.11%, |z20|=1.93
- comex_silver [COMMODITIES]: last 63.76, z20 -1.75, zc -0.46, resid-z 0.75 [quiet], 1d -1.24%, |z20|=1.75
- gold_silver_ratio [DERIVED]: last 68.07, z20 1.20, zc n/a, resid-z n/a [quiet], 1d -0.33%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.358 via gold_silver_ratio, z -2.39, reacted); dyn_adanient_bo (rho -0.351 via gold_silver_ratio, z 0.56, quiet)
- Watch next: btc_usd (co-move) — not yet - watch; rho 0.577 vs comex_silver, historically leads by 5d
- **India receivers**: nifty_midcap_100 (rho -0.358, z -2.39); dyn_adanient_bo (rho -0.351, z 0.56)
- Source: Copper price hits three-week low as inventories rise and dollar strengthens — ET Markets, 2026-09-14. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/copper-hits-three-week-low-as-inventories-rise-and-dollar-strengthens/articleshow/134245729.cms
- Source: Gold, silver prices retreat as oil prices surge, inflation and rate-hike concerns mount — ET Markets, 2026-09-14. https://economictimes.indiatimes.com/markets/commodities/news/gold-silver-prices-retreat-as-oil-prices-surge-inflation-and-rate-hike-concerns-mount/articleshow/134243425.cms
- Source: Gold and silver prices crash up to 2% on MCX- What is driving precious metals down? — Mint Markets, 2026-09-14. https://www.livemint.com/market/commodities/gold-and-silver-prices-crash-up-to-2-on-mcx-what-is-driving-precious-metals-down-11789385809322.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.22), 2025-10-31 (d=0.34)

### [RED 6.68] cross-asset · 4 series ↓
- india_vix [INDICES]: last 12.29, z20 3.01, zc 0.74, resid-z n/a [quiet], 1d 4.15%, |z20|=3.01
- nifty_midcap_100 [INDICES]: last 62197.20, z20 -2.39, zc -0.40, resid-z -0.44 [quiet], 1d -0.26%, |z20|=2.39
- nifty_50 [INDICES]: last 23398.10, z20 -2.37, zc -0.61, resid-z -0.80 [quiet], 1d -0.34%, |z20|=2.37
- dyn_jiofin_bo [EQUITIES]: last 230.00, z20 -1.89, zc -0.35, resid-z 0.41 [quiet], 1d -0.50%, 1y-pct=2
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-17 (z-distance 0.67).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho 0.624 via nifty_50, z -1.77, reacted); dyn_indianb_ns (rho 0.553 via nifty_midcap_100, z -2.13, reacted); nifty_it (rho 0.51 via nifty_50, z -2.31, reacted); dyn_techm_ns (rho 0.466 via nifty_50, z -1.48, reacted); dyn_indusindbk_bo (rho 0.457 via nifty_50, z -1.86, reacted)
- **India receivers**: nifty_fmcg (rho 0.624, z -1.77); dyn_indianb_ns (rho 0.553, z -2.13); nifty_it (rho 0.51, z -2.31); dyn_techm_ns (rho 0.466, z -1.48)
- Source: Stock Market prediction tomorrow: Sensex, Nifty outlook for Tue | Kospi, Taiwan Index, Nikkei cues to watch | 15 Sept — Mint Markets, 2026-09-14. https://www.livemint.com/market/stock-market-news/stock-market-prediction-tomorrow-sensex-nifty-outlook-for-tue-kospi-taiwan-index-nikkei-cues-to-watch-15-sept-11789387045689.html
- Source: Stock Market prediction today: Sensex, Nifty outlook for Tue | Kospi, Taiwan Index, Nikkei cues to watch | 15 Sept — Mint Markets, 2026-09-14. https://www.livemint.com/market/stock-market-news/stock-market-prediction-tomorrow-sensex-nifty-outlook-for-tue-kospi-taiwan-index-nikkei-cues-to-watch-15-sept-11789387045689.html
- Source: Nifty 50 crashes over 10% YTD | Will it continue to bleed or green will be seen? Decoded — Mint Markets, 2026-09-14. https://www.livemint.com/market/stock-market-news/nifty-50-crashes-over-10-ytd-will-it-continue-to-bleed-or-green-will-be-seen-decoded-11789380725124.html
- Historical analogues: 2025-07-17 (d=0.67), 2025-12-19 (d=1.13), 2024-11-07 (d=1.15)

### [RED 5.9] dyn_bac ↓
- dyn_bac [EQUITIES]: last 59.47, z20 -3.90, zc -3.69, resid-z -0.35 [moved], 1d -5.14%, |z20|=3.90
- **Mechanism**: dyn_bac ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: The 10 most overvalued housing markets in America — MarketWatch Top, 2026-09-14. https://www.marketwatch.com/story/the-10-most-overvalued-housing-markets-in-america-6d28efdf?mod=mw_rss_topstories
- Source: TRUMP: “DON’T KILL THE GOLDEN GOOSE” President Trump says America’s AI and data center boom is happening because the U.S. holds a commanding global lead. He urged against measures that could slow the industry’s expansion, warning policymakers: “Don’t kill the Golden Goose!” — DeItaone, 2026-09-14. https://t.me/walter_bloomberg/35759
- Source: BOFA TURNS MORE BULLISH ON S&P 500 Bank of America raised its S&P 500 year-end target to 7,400 from 7,100, signaling increased confidence in the equity rally. BofA also introduced a 12-month target of 7,800, pointing to further upside for U.S. stocks beyond year-end. — DeItaone, 2026-09-14. https://t.me/walter_bloomberg/35746
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

### [RED 4.71] dyn_jef ↓
- dyn_jef [EQUITIES]: last 50.10, z20 -2.71, zc -1.40, resid-z -1.87 [unexplained], 1d -3.58%, |z20|=2.71
- **Mechanism**: dyn_jef ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Jefferies says Sebi's proposed CAS changes will remove uncertainty, but still remains negative on BSE. Here’s why — ET Markets, 2026-09-14. https://economictimes.indiatimes.com/markets/stocks/news/jefferies-says-sebis-proposed-cas-changes-will-remove-uncertainty-but-still-remains-negative-on-bse-heres-why/articleshow/134233906.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-01 (d=0.04), 2025-08-19 (d=0.07)

### [AMBER 4.31] dyn_tatatech_ns ↓
- dyn_tatatech_ns [EQUITIES]: last 762.15, z20 -2.31, zc -1.03, resid-z -0.77 [quiet], 1d -2.17%, |z20|=2.31
- **Mechanism**: dyn_tatatech_ns ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho 0.585 via dyn_tatatech_ns, z -2.31, reacted); dyn_tataelxsi_ns (rho 0.507 via dyn_tatatech_ns, z -2.28, reacted); dyn_techm_ns (rho 0.48 via dyn_tatatech_ns, z -1.48, reacted)
- **India receivers**: nifty_it (rho 0.585, z -2.31); dyn_tataelxsi_ns (rho 0.507, z -2.28); dyn_techm_ns (rho 0.48, z -1.48)
- Source: Tata Sons IPO news | Why is it getting difficult for Tata Group's holding company to stay private? — Mint Markets, 2026-09-14. https://www.livemint.com/market/ipo/tata-sons-ipo-news-why-is-it-getting-difficult-for-tata-groups-holding-company-to-stay-private-11789349656909.html
- Source: Tata group stocks may pop after RBI decision on listing — Mint Markets, 2026-09-14. https://www.livemint.com/market/stock-market-news/tata-sons-ipo-listing-impact-on-tata-group-stocks-11789296081226.html
- Source: Tata Sons listing to improve SP Group bond outlook; yields seen tightening — ET Markets, 2026-09-14. https://economictimes.indiatimes.com/markets/bonds/sp-group-bond-yields-set-to-tighten-as-tata-sons-listing-improves-repayment-visibility/articleshow/134229864.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-12-26 (d=0.0), 2025-02-20 (d=0.02)

### [AMBER 4.11] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.66, z20 1.11, zc n/a, resid-z n/a [quiet], 1d 0.08%, 52-wk extreme (pct=98); 1y-pct=98
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho -0.436 via midcap_largecap_ratio, z -2.37, reacted); nifty_midcap_100 (rho 0.431 via midcap_largecap_ratio, z -2.39, reacted); nifty_fmcg (rho -0.398 via midcap_largecap_ratio, z -1.77, reacted)
- **India receivers**: nifty_50 (rho -0.436, z -2.37); nifty_midcap_100 (rho 0.431, z -2.39); nifty_fmcg (rho -0.398, z -1.77)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

## Watchlist (below surfacing floor)
eur_usd ↓ (4.08), nikkei_225 ↓ (3.93), usd_jpy ↓ (3.56), usd_mxn ↑ (3.25), cross-asset · 2 series ↓ (3.14), asx_200 ↓ (2.68), ust_2s10s ↓ (2.63), usd_cny ↓ (2.57), dyn_meta ↑ (2.37), dyn_hdb ↓ (2.31), dyn_4417_t ↑ (2.3), dyn_indianb_ns ↓ (2.13)

## India macro
- nifty_50: 23398.0996 (1d -0.34%, z20 -2.37, flag amber)
- nifty_midcap_100: 62197.1992 (1d -0.26%, z20 -2.39, flag amber)
- usd_inr: 95.5400 (1d -0.16%, z20 0.65, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6582 (1d 0.08%, z20 1.11, flag amber)
- Next India prints: India CPI T-0d · India WPI T-0d · NSDL FPI flows T-0d · IMD weekly rainfall T-0d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 58.2 — "Infosys, Wipro ADRs surge up to 6%: What it means for Indian IT stocks on Tuesday"
- COALINDIA.NS (COAL INDIA LTD) score 57.6 — "Infosys, Wipro ADRs surge up to 6%: What it means for Indian IT stocks on Tuesday"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 56.3 — "Infosys, Wipro ADRs surge up to 6%: What it means for Indian IT stocks on Tuesday"
- INDIANB.NS (INDIAN BANK) score 50.2 — "BOFA TURNS MORE BULLISH ON S&P 500 Bank of America raised its S&P 500 year-end target to 7"
- COIN (Coinbase Global, Inc.) score 47.9 — "TRUMP: “DON’T KILL THE GOLDEN GOOSE” President Trump says America’s AI and data center boo"
- BAC (Bank of America Corporation) score 45.7 — "BOFA TURNS MORE BULLISH ON S&P 500 Bank of America raised its S&P 500 year-end target to 7"
- HDB (HDFC Bank Limited) score 37.8 — "BOFA TURNS MORE BULLISH ON S&P 500 Bank of America raised its S&P 500 year-end target to 7"
- OHI (Omega Healthcare Investors, In) score 36.8 — "Top stocks in focus today: Investors must watch HDFC Bank, HCL Tech, Sun Pharma shares on "
- IDBI.NS (IDBI BANK LIMITED) score 35.0 — "BOFA TURNS MORE BULLISH ON S&P 500 Bank of America raised its S&P 500 year-end target to 7"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 35.0 — "BOFA TURNS MORE BULLISH ON S&P 500 Bank of America raised its S&P 500 year-end target to 7"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 35.0 — "BOFA TURNS MORE BULLISH ON S&P 500 Bank of America raised its S&P 500 year-end target to 7"
- CHKP (Check Point Software Technolog) score 27.8 — "EaseMyTrip co-founder Nishant Pitti pledges 34.51 cr shares to Motilal Oswal Fin Services;"
- BOND (PIMCO Active Bond Exchange-Tra) score 27.4 — "U.S. 10-YEAR YIELD BREAKS 5% The 10-year Treasury yield climbed above 5%, its highest sinc"
- TECHM.NS (TECH MAHINDRA LIMITED) score 24.9 — "Top stocks in focus today: Investors must watch HDFC Bank, HCL Tech, Sun Pharma shares on "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 24.8 — "Top stocks in focus today: Investors must watch HDFC Bank, HCL Tech, Sun Pharma shares on "
- TECH (Bio-Techne Corp) score 24.8 — "Top stocks in focus today: Investors must watch HDFC Bank, HCL Tech, Sun Pharma shares on "
- 301077.SZ (CHINASTARS) score 24.7 — "China’s Growing Iran Trade Is Moving Overland Through Central Asia"
- LTH (Life Time Group Holdings, Inc.) score 20.6 — "US 10-YEAR TREASURY YIELD REACHES 5% FOR FIRST TIME SINCE 2023"
- SEPN (Septerna, Inc.) score 18.7 — "Stock Market prediction today: Sensex, Nifty outlook for Tue | Kospi, Taiwan Index, Nikkei"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 17.9 — "TRUMP: UKRAINE HAS AGREED NOT TO HIT RUSSIAN ENERGY TARGETS, RUSSIA HAS AGREED TO DO, LIKE"
- NVDA (NVIDIA Corporation) score 10.7 — "NVIDIA, Palantir and Booz Allen Hamilton will limit use of ANTHROPIC models"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.1 — "Saudi Arabia may be just days away from not being able to export much oil"
- JIOFIN.BO (Jio Financial Services Limited) score 9.1 — "EaseMyTrip co-founder Nishant Pitti pledges 34.51 cr shares to Motilal Oswal Fin Services;"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 8.7 — "Tata Sons may be valued up to Rs 12.5 lakh cr in IPO"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 8.7 — "Tata Sons may be valued up to Rs 12.5 lakh cr in IPO"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 8.4 — "Can SS Retail IPO deliver long-term growth for high-risk investors?"
- MS (Morgan Stanley) score 7.0 — "GOLDMAN, JPMORGAN NOW EXPECT FED TO HIKE THIS WEEK Goldman Sachs and JPMorgan have shifted"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.2 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Current Price Update"
- PCJEWELLER.NS (PC JEWELLER LTD) score 5.9 — "Gem, jewellery exports up 3% to $2.30 billion in Aug"
- VT (Vanguard Total World Stock Ind) score 5.1 — "TRUMP PUSHES FED FOR WORLD’S LOWEST INTEREST RATES President Donald Trump says the U.S. sh"
- META (Meta) score 5.1 — "Gold and silver prices crash up to 2% on MCX- What is driving precious metals down?"
- JEF (Jefferies Financial Group Inc.) score 4.0 — "Jefferies says Sebi's proposed CAS changes will remove uncertainty, but still remains nega"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 3.6 — "Cochin Shipyard shares crash nearly 9% - Is it opportunity to buy? Should you take fresh e"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 3.3 — "Joint finances, joint risks: A couple’s roadmap to starting up"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.2 — "ICICI Bank Share Price Live Updates: Rs 1.09 crore remittance sent home by an Indian worki"
- BZ=F (Brent Crude Oil Last Day Finan) score 2.8 — "The Next Oil Shock Is Never the Last"
- DELL (Dell Technologies Inc.) score 0.9 — "Why Dell and HPE were the S&P 500’s top-performing stocks today"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 0.4 — "Lenskart Solutions among 4 stocks to hit 52-week highs & rallied up to 22% in a month"
- DKS (Dick's Sporting Goods Inc) score 0.1 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
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