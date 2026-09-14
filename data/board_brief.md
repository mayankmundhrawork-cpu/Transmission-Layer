# Transmission Layer — board brief · 2026-09-14 16:23Z

data as of **2026-09-14** · 98 series · 11 red / 43 amber · 8 events surfaced (36 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.537, 2d in regime; vol-pct 0.407, breadth-off 0.667, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.42, corr60 -0.33, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.82, corr60 0.88, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.13, corr60 0.31, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.15, corr60 0.13, last shift 2026-06-05. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.86, corr60 -0.83, last shift 2026-05-08. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.11, corr60 -0.03, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.36, corr60 -0.17, last shift 2026-06-26. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.19, corr60 0.09, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 90** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.478, β 0.2579, p 0.0); driver zc 2.66 → expected 0.641%. Type hit-rate 0.818 (n=2011).
- **SETUP** ust_10y → gbp_usd: leads 1d (ccf -0.271, β -0.1092, p 0.0); driver zc 2.66 → expected -0.271%. Type hit-rate 0.818 (n=2011).
- **SETUP** dyn_coin → aud_usd: leads 1d (ccf 0.263, β 0.0321, p 0.00024); driver zc 1.85 → expected 0.291%. Type hit-rate 0.818 (n=2011).
- Track record · residual_reversion: hit-rate **0.496** (n=1125) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=2011) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.57] cross-asset · 5 series ↑
- ust_10y [RATES]: last 4.95, z20 4.00, zc 2.66, resid-z 2.36 [unexplained], 1d 2.48%, |z20|=4.00; 1y-pct=100
- tips_10y_real [RATES]: last 2.55, z20 3.64, zc 2.28, resid-z 1.99 [unexplained], 1d 3.66%, 1d move +9.0bps ≥ 5bps; |z20|=3.64; 1y-pct=100
- ust_30y [RATES]: last 5.37, z20 3.62, zc 2.26, resid-z 2.02 [unexplained], 1d 1.70%, |z20|=3.62; 1y-pct=100
- ust_2y [RATES]: last 4.56, z20 3.18, zc 2.33, resid-z 1.94 [unexplained], 1d 2.93%, |z20|=3.18; 1y-pct=100
- dyn_bond [EQUITIES]: last 88.93, z20 -2.22, zc 0.27, resid-z -0.71 [quiet], 1d 0.10%, |z20|=2.22; 1y-pct=0
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dxy (co-move) — not yet - watch; rho 0.527 vs tips_10y_real
- Source: 10-year Treasury yield briefly tops 5%, hitting its highest level since 2007 as bond-market selloff deepens — MarketWatch Top, 2026-09-14. https://www.marketwatch.com/story/10-year-treasury-yield-tops-5-for-the-first-time-since-2007-as-bond-market-selloff-deepens-14c81f75?mod=mw_rss_topstories
- Source: Bond market shock: 10-year US Treasury yield tops 5% as oil spike puts Federal Reserve on rate-hike path — ET Markets, 2026-09-14. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/bond-market-shock-10-year-us-yield-tops-5-as-oil-at-108-puts-fed-on-rate-hike-path/articleshow/134242764.cms
- Source: WHAT TO WATCH TODAY — U.S. MARKETS A light U.S. data calendar puts the focus on oil, geopolitics, Treasury yields and Fed positioning. 8:30 AM ET — 🇨🇦 Canada CPI 11:00 AM ET — 🇺🇸 13-Week & 26-Week Treasury Bill Auctions After Close — 🫀 Kestra Medical Earnings After Close — 🎮 Dave & Buster’s Earnings — DeItaone, 2026-09-14. https://t.me/walter_bloomberg/35728
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 8.23] commodities · 2 series ↑
- brent [COMMODITIES]: last 106.84, z20 2.39, zc 0.65, resid-z 0.60 [quiet], 1d 2.13%, 1-session move +2.13% ≥ 1.5%; |z20|=2.39
- wti [COMMODITIES]: last 102.32, z20 2.37, zc 0.72, resid-z 0.67 [quiet], 1d 2.27%, 1-session move +2.27% ≥ 1.5%; |z20|=2.37; 1y-pct=95
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Gold, silver prices retreat as oil prices surge, inflation and rate-hike concerns mount — ET Markets, 2026-09-14. https://economictimes.indiatimes.com/markets/commodities/news/gold-silver-prices-retreat-as-oil-prices-surge-inflation-and-rate-hike-concerns-mount/articleshow/134243425.cms
- Source: Record Freight Costs Squeeze Russia's Black Sea Crude Exports — OilPrice, 2026-09-14. https://oilprice.com/Geopolitics/International/Record-Freight-Costs-Squeeze-Russias-Black-Sea-Crude-Exports.html
- Source: Bond market shock: 10-year US Treasury yield tops 5% as oil spike puts Federal Reserve on rate-hike path — ET Markets, 2026-09-14. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/bond-market-shock-10-year-us-yield-tops-5-as-oil-at-108-puts-fed-on-rate-hike-path/articleshow/134242764.cms
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-18 (d=0.03), 2024-10-31 (d=0.05)

### [AMBER 7.41] cross-asset · 3 series ↓
- comex_copper [COMMODITIES]: last 6.38, z20 -2.11, zc -0.63, resid-z -0.32 [quiet], 1d -1.38%, |z20|=2.11
- comex_silver [COMMODITIES]: last 63.85, z20 -1.69, zc -0.40, resid-z -0.01 [quiet], 1d -1.09%, |z20|=1.69
- gold_silver_ratio [DERIVED]: last 67.92, z20 1.09, zc n/a, resid-z n/a [quiet], 1d 0.42%, GSR<75 (extreme low)
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.353 via gold_silver_ratio, z -2.39, reacted)
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.596 vs comex_copper, historically leads by 1d
- Watch next: btc_usd (co-move) — not yet - watch; rho 0.577 vs comex_silver, historically leads by 5d
- **India receivers**: nifty_midcap_100 (rho -0.353, z -2.39)
- Source: Gold, silver prices retreat as oil prices surge, inflation and rate-hike concerns mount — ET Markets, 2026-09-14. https://economictimes.indiatimes.com/markets/commodities/news/gold-silver-prices-retreat-as-oil-prices-surge-inflation-and-rate-hike-concerns-mount/articleshow/134243425.cms
- Source: Gold and silver prices crash up to 2% on MCX- What is driving precious metals down? — Mint Markets, 2026-09-14. https://www.livemint.com/market/commodities/gold-and-silver-prices-crash-up-to-2-on-mcx-what-is-driving-precious-metals-down-11789385809322.html
- Source: EVs, home appliances likely to become pricier as copper price soars — BusinessLine Mkts, 2026-09-14. https://www.thehindubusinessline.com/markets/commodities/evs-home-appliances-likely-to-become-pricier-as-copper-price-soars/article71462841.ece
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
- Source: Nifty 50 crashes over 10% YTD | Will it continue to bleed or green will be seen? Decoded — Mint Markets, 2026-09-14. https://www.livemint.com/market/stock-market-news/nifty-50-crashes-over-10-ytd-will-it-continue-to-bleed-or-green-will-be-seen-decoded-11789380725124.html
- Source: Nifty may reach 26,200 by December 2026 as earnings cuts, market risks ease: BofA Securities — BusinessLine Mkts, 2026-09-14. https://www.thehindubusinessline.com/markets/nifty-may-reach-26200-by-december-2026-as-earnings-cuts-market-risks-ease-bofa-securities/article71465945.ece
- Historical analogues: 2025-07-17 (d=0.67), 2025-12-19 (d=1.13), 2024-11-07 (d=1.15)

### [AMBER 4.44] dyn_jef ↓
- dyn_jef [EQUITIES]: last 50.44, z20 -2.44, zc -1.15, resid-z -0.75 [quiet], 1d -2.93%, |z20|=2.44
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

### [AMBER 4.13] dyn_chkp ↑
- dyn_chkp [EQUITIES]: last 139.55, z20 2.13, zc 2.29, resid-z -1.01 [moved], 1d 6.01%, |z20|=2.13
- **Mechanism**: dyn_chkp ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: GMM Pfaudler share price target: Buy rating, 39% upside - Check rationale behind recommendation by InCred Equities — Mint Markets, 2026-09-14. https://www.livemint.com/market/stock-market-news/gmm-pfaudler-share-price-target-buy-rating-39-upside-check-rationale-behind-recommendation-by-incred-equities-11789387758447.html
- Source: Finolex Cables share price target 2026: Buy - 'Unlocking growth' | Check rationale behind rating — Mint Markets, 2026-09-14. https://www.livemint.com/market/finolex-cables-share-price-target-2026-buy-unlocking-growth-check-rationale-behind-rating-11789382900920.html
- Source: EaseMyTrip co-founder Nishant Pitti pledges 34.51 cr shares to Motilal Oswal Fin Services; check penny stock performance — Mint Markets, 2026-09-14. https://www.livemint.com/market/stock-market-news/easemytrip-co-founder-nishant-pitti-pledges-34-51-crore-shares-to-motilal-oswal-check-travel-stocks-performance-11789377257232.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2024-10-18 (d=0.02)

### [AMBER 4.11] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.66, z20 1.11, zc n/a, resid-z n/a [quiet], 1d 0.08%, 52-wk extreme (pct=98); 1y-pct=98
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho -0.436 via midcap_largecap_ratio, z -2.37, reacted); nifty_midcap_100 (rho 0.431 via midcap_largecap_ratio, z -2.39, reacted); nifty_fmcg (rho -0.398 via midcap_largecap_ratio, z -1.77, reacted)
- **India receivers**: nifty_50 (rho -0.436, z -2.37); nifty_midcap_100 (rho 0.431, z -2.39); nifty_fmcg (rho -0.398, z -1.77)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

## Watchlist (below surfacing floor)
dyn_ohi ↑ (4.09), eur_usd ↓ (4.01), nikkei_225 ↓ (3.93), indices · 3 series ↓ (3.88), usd_jpy ↓ (3.53), usd_mxn ↑ (3.18), cross-asset · 2 series ↓ (3.14), asx_200 ↓ (2.68), usd_cny ↓ (2.64), dyn_4417_t ↑ (2.3), dyn_meta ↑ (2.25), dyn_ms ↓ (2.17)

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
- INOXINDIA.NS (INOX INDIA LIMITED) score 60.2 — "Can Rs 6.6 lakh crore in potential PSU divestments bring FPIs back to Indian markets? Axis"
- COALINDIA.NS (COAL INDIA LTD) score 59.6 — "Can Rs 6.6 lakh crore in potential PSU divestments bring FPIs back to Indian markets? Axis"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 58.3 — "Can Rs 6.6 lakh crore in potential PSU divestments bring FPIs back to Indian markets? Axis"
- INDIANB.NS (INDIAN BANK) score 49.8 — "Can Rs 6.6 lakh crore in potential PSU divestments bring FPIs back to Indian markets? Axis"
- COIN (Coinbase Global, Inc.) score 47.3 — "CHINA SLAMS U.S. CALLS TO SLOW AI RACE China’s state-backed Global Times accused Anthropic"
- BAC (Bank of America Corporation) score 43.9 — "TRUMP PUSHES FED FOR WORLD’S LOWEST INTEREST RATES President Donald Trump says the U.S. sh"
- OHI (Omega Healthcare Investors, In) score 37.7 — "Japanese stocks: Nikkei 225 sell-off deepens as AI slowdown concerns hits chip stocks; sho"
- HDB (HDFC Bank Limited) score 37.7 — "AI slowdown trade hits Nvidia, SoftBank, SK Hynix as global tech stocks fall up to 10%"
- IDBI.NS (IDBI BANK LIMITED) score 34.8 — "AI slowdown trade hits Nvidia, SoftBank, SK Hynix as global tech stocks fall up to 10%"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 34.8 — "AI slowdown trade hits Nvidia, SoftBank, SK Hynix as global tech stocks fall up to 10%"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 34.8 — "AI slowdown trade hits Nvidia, SoftBank, SK Hynix as global tech stocks fall up to 10%"
- CHKP (Check Point Software Technolog) score 29.3 — "EaseMyTrip co-founder Nishant Pitti pledges 34.51 cr shares to Motilal Oswal Fin Services;"
- BOND (PIMCO Active Bond Exchange-Tra) score 27.8 — "Bond market shock: 10-year US Treasury yield tops 5% as oil spike puts Federal Reserve on "
- TECHM.NS (TECH MAHINDRA LIMITED) score 25.1 — "CHINA SLAMS U.S. CALLS TO SLOW AI RACE China’s state-backed Global Times accused Anthropic"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 25.1 — "CHINA SLAMS U.S. CALLS TO SLOW AI RACE China’s state-backed Global Times accused Anthropic"
- TECH (Bio-Techne Corp) score 25.1 — "CHINA SLAMS U.S. CALLS TO SLOW AI RACE China’s state-backed Global Times accused Anthropic"
- 301077.SZ (CHINASTARS) score 25.0 — "CHINA SLAMS U.S. CALLS TO SLOW AI RACE China’s state-backed Global Times accused Anthropic"
- LTH (Life Time Group Holdings, Inc.) score 20.6 — "CHINA SLAMS U.S. CALLS TO SLOW AI RACE China’s state-backed Global Times accused Anthropic"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 17.8 — "U.S. WARNS AGAINST HORMUZ DEAL OPTIMISM U.S. Energy Secretary Chris Wright warned traders "
- SEPN (Septerna, Inc.) score 17.5 — "GULF–IRAN HORMUZ TALKS POSTPONED A planned September 14 meeting in Oman between Iran and G"
- NVDA (NVIDIA Corporation) score 10.2 — "US market prediction today: S&P 500, Nasdaq futures fall up to 1.8% as AI fears hit Nvidia"
- JIOFIN.BO (Jio Financial Services Limited) score 9.6 — "EaseMyTrip co-founder Nishant Pitti pledges 34.51 cr shares to Motilal Oswal Fin Services;"
- JUSTDIAL.BO (JUST DIAL LTD.) score 9.5 — "TRUMP PUSHES FED FOR WORLD’S LOWEST INTEREST RATES President Donald Trump says the U.S. sh"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 9.2 — "Tata Sons may be valued up to Rs 12.5 lakh cr in IPO"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 9.2 — "Tata Sons may be valued up to Rs 12.5 lakh cr in IPO"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 8.8 — "Can SS Retail IPO deliver long-term growth for high-risk investors?"
- MS (Morgan Stanley) score 7.4 — "GOLDMAN, JPMORGAN NOW EXPECT FED TO HIKE THIS WEEK Goldman Sachs and JPMorgan have shifted"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.5 — "Adani Ports SEZ Share Price Live Updates: Adani Ports SEZ Current Price Update"
- PCJEWELLER.NS (PC JEWELLER LTD) score 6.2 — "Gem, jewellery exports up 3% to $2.30 billion in Aug"
- VT (Vanguard Total World Stock Ind) score 5.4 — "TRUMP PUSHES FED FOR WORLD’S LOWEST INTEREST RATES President Donald Trump says the U.S. sh"
- META (Meta) score 5.4 — "Gold and silver prices crash up to 2% on MCX- What is driving precious metals down?"
- JEF (Jefferies Financial Group Inc.) score 4.3 — "Jefferies says Sebi's proposed CAS changes will remove uncertainty, but still remains nega"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 3.7 — "Cochin Shipyard shares crash nearly 9% - Is it opportunity to buy? Should you take fresh e"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 3.5 — "Joint finances, joint risks: A couple’s roadmap to starting up"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 3.4 — "ICICI Bank Share Price Live Updates: Rs 1.09 crore remittance sent home by an Indian worki"
- QCOM (QUALCOMM Incorporated) score 1.1 — "Qualcomm-Amazon AI deal: Why the chipmaker’s stock surged"
- DELL (Dell Technologies Inc.) score 0.9 — "Why Dell and HPE were the S&P 500’s top-performing stocks today"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 0.5 — "Lenskart Solutions among 4 stocks to hit 52-week highs & rallied up to 22% in a month"
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