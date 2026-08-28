# Transmission Layer — board brief · 2026-08-28 00:53Z

data as of **2026-08-28** · 98 series · 12 red / 32 amber · 8 events surfaced (29 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.667, 1d in regime; vol-pct None, breadth-off 0.667, Markov P(high-vol) 0.015)
- [INVERTED] **safe_haven_gold** — corr20 -0.27, corr60 -0.4, contra nifty_50 corr20=0.01, last shift 2026-06-08. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.79, corr60 0.86, last shift 2026-01-29. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.07, corr60 0.31, last shift 2026-07-10. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.1, corr60 -0.01, last shift 2026-07-14. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.55, corr60 -0.83, last shift 2026-05-07. Channel: vol spike -> equity drawdown
- [INVERTED] **dxy_inr_channel** — corr20 -0.27, corr60 -0.16, last shift 2026-01-15. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.11, corr60 -0.08, last shift 2026-06-25. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 -0.24, corr60 0.2, last shift 2026-07-10. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **4 of 90** scanned series survive multiplicity control (effective p ≤ 0.003976751709788617)
- **SETUP** dyn_nvda → taiwan_weighted: leads 1d (ccf 0.405, β 0.2443, p 0.0); driver zc 3.94 → expected 2.143%. Type hit-rate 0.814 (n=2283).
- **SETUP** dyn_nvda → nikkei_225: leads 1d (ccf 0.395, β 0.2247, p 0.0); driver zc 3.94 → expected 1.971%. Type hit-rate 0.814 (n=2283).
- **SETUP** dyn_nvda → usd_mxn: leads 1d (ccf -0.342, β -0.0732, p 0.0); driver zc 3.94 → expected -0.642%. Type hit-rate 0.814 (n=2283).
- **SETUP** dyn_nvda → aud_usd: leads 1d (ccf 0.325, β 0.0715, p 0.0); driver zc 3.94 → expected 0.627%. Type hit-rate 0.814 (n=2283).
- **SETUP** dyn_nvda → kospi: leads 1d (ccf 0.267, β 0.2378, p 0.0); driver zc 3.94 → expected 2.086%. Type hit-rate 0.814 (n=2283).
- Track record · residual_reversion: hit-rate **0.497** (n=1120) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.814** (n=2283) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.533** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 10.43] dyn_inoxindia_ns ↑
- dyn_inoxindia_ns [EQUITIES]: last 2160.30, z20 10.43, zc 7.37, resid-z 3.42 [unexplained], 1d 12.12%, |z20|=10.43; 1y-pct=100
- **Mechanism**: dyn_inoxindia_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.363 via dyn_inoxindia_ns, z 1.92, reacted)
- **India receivers**: midcap_largecap_ratio (rho 0.363, z 1.92)
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-14 (d=0.02), 2026-06-18 (d=0.04)

### [RED 7.77] dyn_indusindbk_bo ↓
- dyn_indusindbk_bo [EQUITIES]: last 970.00, z20 -5.77, zc -1.89, resid-z -2.88 [unexplained], 1d -3.19%, |z20|=5.77
- **Mechanism**: dyn_indusindbk_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.508 via dyn_indusindbk_bo, z -1.67, reacted); nifty_midcap_100 (rho 0.477 via dyn_indusindbk_bo, z 1.03, reacted); nifty_fmcg (rho 0.449 via dyn_indusindbk_bo, z -1.83, reacted); dyn_adanient_bo (rho 0.389 via dyn_indusindbk_bo, z 3.24, reacted); dyn_karurvysya_ns (rho 0.378 via dyn_indusindbk_bo, z 1.35, reacted)
- **India receivers**: nifty_50 (rho 0.508, z -1.67); nifty_midcap_100 (rho 0.477, z 1.03); nifty_fmcg (rho 0.449, z -1.83); dyn_adanient_bo (rho 0.389, z 3.24)
- Source: IndusInd Bank Share Price Live Updates: IndusInd Bank Moves Past 20-Day SMA — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/indusind-bank-share-price-live-26-aug-2026/liveblog/133528142.cms
- Source: IndusInd Bank Share Price Live Updates: IndusInd Bank's Current Price and Market Performance — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/stocks/stock-liveblog/indusind-bank-share-price-live-26-aug-2026/liveblog/133528142.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-15 (d=0.01), 2026-06-19 (d=0.02)

### [RED 6.23] commodities · 3 series ↑
- wheat [COMMODITIES]: last 761.75, z20 2.91, zc 0.00, resid-z 1.96 [unexplained], 1d 0.00%, |z20|=2.91; 1y-pct=99
- corn [COMMODITIES]: last 535.25, z20 2.55, zc -0.03, resid-z 2.67 [unexplained], 1d -0.05%, |z20|=2.55; 1y-pct=99
- soybeans [COMMODITIES]: last 1278.25, z20 2.36, zc 0.00, resid-z 1.89 [unexplained], 1d 0.00%, |z20|=2.36; 1y-pct=99
- **Mechanism**: commodities · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_coalindia_ns (rho -0.387 via corn, z -1.9, reacted); dyn_atherenerg_ns (rho -0.351 via soybeans, z 0.58, quiet)
- **India receivers**: dyn_coalindia_ns (rho -0.387, z -1.9); dyn_atherenerg_ns (rho -0.351, z 0.58)
- Source: UBS SEES COMMODITY OPPORTUNITIES BEYOND OIL UBS sees opportunities across copper, agriculture and gold, arguing commodities offer both returns and inflation protection. Copper should benefit from AI infrastructure and electrification. Wheat and corn are gaining as a — DeItaone, 2026-08-27. https://t.me/walter_bloomberg/35133
- Source: Wheat Hits Three-Year High as Russia Prepares to Escalate War — Mint Markets, 2026-08-27. https://www.livemint.com/market/wheat-hits-three-year-high-as-russia-prepares-to-escalate-war-11787802575795.html
- Source: Wheat soars to daily limit on Black Sea export worries, corn at lifetime highs — Mint Markets, 2026-08-26. https://www.livemint.com/market/wheat-soars-to-daily-limit-on-black-sea-export-worries-corn-at-lifetime-highs-11787773711563.html
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-06 (d=0.32), 2025-10-03 (d=0.4)

### [AMBER 5.59] cross-asset · 3 series ↑
- dyn_coin [EQUITIES]: last 190.75, z20 2.27, zc 0.97, resid-z -0.42 [quiet], 1d 4.93%, |z20|=2.27
- btc_usd [CRYPTO]: last 80384.78, z20 1.82, zc -0.01, resid-z 0.55 [quiet], 1d -0.04%, |z20|=1.82
- eth_usd [CRYPTO]: last 2513.71, z20 1.62, zc -0.11, resid-z -0.06 [quiet], 1d -0.42%, |z20|=1.62
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-11 (z-distance 0.82).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_metal (rho 0.445 via btc_usd, z 1.62, reacted)
- Watch next: dxy (inverse) — not yet - watch; rho -0.561 vs eth_usd, historically leads by 1d
- **India receivers**: nifty_metal (rho 0.445, z 1.62)
- Source: Global Market Today: Asian shares slip as US stock futures dip ahead of Warsh’s Jackson Hole speech — ET Markets, 2026-08-28. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-today-asian-shares-slip-as-us-stock-futures-dip-ahead-of-warshs-jackson-hole-speech/articleshow/133580806.cms
- Source: Bitcoin’s ‘Uptober’ test: Will August’s rebound turn into a lasting rally? — ET Markets, 2026-08-27. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/bitcoins-uptober-test-will-augusts-rebound-turn-into-a-lasting-rally/articleshow/133572814.cms
- Source: S&P Global Ratings affirms India’s ‘BBB/A-2’ rating, retains stable outlook — Mint Markets, 2026-08-27. https://www.livemint.com/market/stock-market-news/sp-global-ratings-affirms-india-s-bbb-a-2-rating-retains-stable-outlook-11787835565723.html
- Historical analogues: 2025-08-11 (d=0.82), 2024-10-31 (d=1.15), 2025-08-22 (d=1.26)

### [RED 5.24] dyn_adanient_bo ↑
- dyn_adanient_bo [EQUITIES]: last 3155.00, z20 3.24, zc 0.43, resid-z 0.75 [quiet], 1d 0.96%, |z20|=3.24; 1y-pct=96
- **Mechanism**: dyn_adanient_bo ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.465 via dyn_adanient_bo, z -1.67, reacted); nifty_midcap_100 (rho 0.432 via dyn_adanient_bo, z 1.03, reacted); dyn_indusindbk_bo (rho 0.389 via dyn_adanient_bo, z -5.77, reacted); nifty_fmcg (rho 0.36 via dyn_adanient_bo, z -1.83, reacted)
- **India receivers**: nifty_50 (rho 0.465, z -1.67); nifty_midcap_100 (rho 0.432, z 1.03); dyn_indusindbk_bo (rho 0.389, z -5.77); nifty_fmcg (rho 0.36, z -1.83)
- Source: Market wrap: Adani Enterprises, Kotak Mahindra Bank, HDFC Bank, M&M top gainers and losers on Nifty and Sensex on Thursday — ET Markets, 2026-08-27. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-adani-enterprises-kotak-mahindra-bank-hdfc-bank-mm-top-gainers-and-losers-on-nifty-and-sensex-on-thursday/articleshow/133566380.cms
- Source: Motilal Oswal initiates coverage on Adani Enterprises with Buy, sees 25% upside. Here’s why — ET Markets, 2026-08-27. https://economictimes.indiatimes.com/markets/stocks/news/motilal-oswal-initiates-coverage-on-adani-enterprises-with-buy-sees-25-upside-heres-why/articleshow/133558689.cms
- Source: Adani’s Cemindia is said to near up to $524 million share sale — ET Markets, 2026-08-26. https://economictimes.indiatimes.com/markets/stocks/news/adanis-cemindia-is-said-to-near-up-to-524-million-share-sale/articleshow/133536591.cms
- Historical analogues: 2026-07-10 (d=0.0), 2025-10-01 (d=0.0), 2026-06-04 (d=0.0)

### [RED 5.2] dyn_hdb ↓
- dyn_hdb [EQUITIES]: last 22.46, z20 -3.20, zc -2.37, resid-z -1.16 [moved], 1d -3.06%, |z20|=3.20; 1y-pct=0
- **Mechanism**: dyn_hdb ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.664 via dyn_hdb, z -1.67, reacted); nifty_midcap_100 (rho 0.529 via dyn_hdb, z 1.03, reacted); dyn_jiofin_bo (rho 0.465 via dyn_hdb, z -1.77, reacted); nifty_fmcg (rho 0.43 via dyn_hdb, z -1.83, reacted); nifty_it (rho 0.429 via dyn_hdb, z -1.71, reacted)
- Watch next: india_vix (inverse) — not yet - watch; rho -0.606 vs dyn_hdb, historically leads by 1d
- **India receivers**: nifty_50 (rho 0.664, z -1.67); nifty_midcap_100 (rho 0.529, z 1.03); dyn_jiofin_bo (rho 0.465, z -1.77); nifty_fmcg (rho 0.43, z -1.83)
- Source: HDFC Bank's CEO call gains urgency as Sashidhar Jagdishan's term nears end — ET Markets, 2026-08-27. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-banks-ceo-call-gains-urgency-as-sashidhar-jagdishans-term-nears-end/articleshow/133580693.cms
- Source: Market wrap: Adani Enterprises, Kotak Mahindra Bank, HDFC Bank, M&M top gainers and losers on Nifty and Sensex on Thursday — ET Markets, 2026-08-27. https://economictimes.indiatimes.com/markets/stocks/news/market-wrap-adani-enterprises-kotak-mahindra-bank-hdfc-bank-mm-top-gainers-and-losers-on-nifty-and-sensex-on-thursday/articleshow/133566380.cms
- Source: HDFC Bank shares fall 2% to fresh 52-week low, tumble 30% in 10 months. What lies ahead? — ET Markets, 2026-08-27. https://economictimes.indiatimes.com/markets/stocks/news/hdfc-bank-shares-fall-2-to-fresh-52-week-low-tumble-30-in-10-months-what-lies-ahead/articleshow/133563941.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [AMBER 5.08] cross-asset · 4 series ↑
- vix [INDICES]: last 14.51, z20 -1.41, zc -0.61, resid-z n/a [quiet], 1d -4.60%, 1y-pct=4
- dyn_vt [EQUITIES]: last 161.58, z20 0.76, zc 0.62, resid-z 0.06 [quiet], 1d 0.44%, 1y-pct=98
- sp500 [INDICES]: last 7730.11, z20 0.49, zc 1.02, resid-z -0.23 [quiet], 1d 0.71%, 1y-pct=97
- dow_jones [INDICES]: last 53562.07, z20 0.11, zc 0.25, resid-z -0.51 [quiet], 1d 0.18%, 1y-pct=96
- **Mechanism**: cross-asset · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2024-10-17 (z-distance 0.46).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (inverse) — not yet - watch; rho -0.71 vs dow_jones, historically leads by 3d
- Watch next: wti (inverse) — not yet - watch; rho -0.704 vs dow_jones, historically leads by 2d
- Watch next: nasdaq_100 (inverse) — not yet - watch; rho -0.667 vs vix, historically leads by 5d
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.649 vs vix, historically leads by 1d
- Watch next: dyn_ms (co-move) — not yet - watch; rho 0.558 vs dyn_vt, historically leads by 5d
- Source: Marvell boosts its forecasts, but the stock slides as Wall Street wonders if there’s more to the story — MarketWatch Top, 2026-08-28. https://www.marketwatch.com/story/marvell-is-boosting-its-forecasts-but-thats-not-enough-to-lift-its-stock-c769556a?mod=mw_rss_topstories
- Source: CrowdStrike’s stock jumps after record-breaking earnings. Wall Street is lapping it up. — MarketWatch Top, 2026-08-27. https://www.marketwatch.com/story/crowdstrikes-stock-has-jumped-after-record-breaking-earnings-wall-street-is-lapping-it-up-dbdaca83?mod=mw_rss_topstories
- Source: The options market is signaling further gains for the S&P 500, but one indicator is flashing a warning — MarketWatch Top, 2026-08-27. https://www.marketwatch.com/story/the-s-p-500-is-nearing-an-especially-positive-price-and-the-options-market-suggests-a-surge-is-likely-a54d866d?mod=mw_rss_topstories
- Historical analogues: 2024-10-17 (d=0.46), 2025-10-21 (d=0.48), 2025-08-27 (d=0.53)

### [RED 4.92] midcap_largecap_ratio ↑
- midcap_largecap_ratio [DERIVED]: last 2.66, z20 1.92, zc n/a, resid-z n/a [quiet], 1d 0.38%, 52-wk extreme (pct=100); |z20|=1.92; 1y-pct=100
- **Mechanism**: midcap_largecap_ratio ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-31 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_fmcg (rho -0.373 via midcap_largecap_ratio, z -1.83, reacted); dyn_techm_ns (rho -0.37 via midcap_largecap_ratio, z -1.32, reacted); dyn_inoxindia_ns (rho 0.363 via midcap_largecap_ratio, z 10.43, reacted); nifty_50 (rho -0.355 via midcap_largecap_ratio, z -1.67, reacted)
- **India receivers**: nifty_fmcg (rho -0.373, z -1.83); dyn_techm_ns (rho -0.37, z -1.32); dyn_inoxindia_ns (rho 0.363, z 10.43); nifty_50 (rho -0.355, z -1.67)
- Historical analogues: 2025-12-31 (d=0.0), 2024-11-06 (d=0.1), 2025-07-03 (d=0.11)

## Watchlist (below surfacing floor)
dyn_dks ↓ (4.56), natgas ↑ (4.5), gold_silver_ratio ↓ (4.38), dyn_icicigi_bo ↓ (4.17), dyn_bac ↓ (4.01), nifty_50 ↓ (3.67), dyn_tech ↑ (3.65), dyn_mrna ↑ (3.61), dyn_nvda ↑ (3.55), comex_copper ↑ (3.21), fx · 2 series ↑ (3.08), dyn_lenskart_ns ↑ (3.03)

## India macro
- nifty_50: 24090.8496 (1d -0.48%, z20 -1.67, flag amber)
- nifty_midcap_100: 64032.1992 (1d -0.10%, z20 1.03, flag amber)
- usd_inr: 95.5400 (1d 0.11%, z20 0.38, flag none)
- goi_10y: 6.8900 (1d -1.85%, z20 1.12, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.4200 (1d -7.98%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6579 (1d 0.38%, z20 1.92, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- INDIANB.NS (INDIAN BANK) score 77.7 — "Stock market holiday: Is the Indian stock market open or closed today for Raksha Bandhan?"
- INOXINDIA.NS (INOX INDIA LIMITED) score 77.7 — "Stock market holiday: Is the Indian stock market open or closed today for Raksha Bandhan?"
- COALINDIA.NS (COAL INDIA LTD) score 77.6 — "Stock market holiday: Is the Indian stock market open or closed today for Raksha Bandhan?"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 75.9 — "Stock market holiday: Is the Indian stock market open or closed today for Raksha Bandhan?"
- BAC (Bank of America Corporation) score 68.2 — "Sebi proposes merchant banker exemption for small-value private debt issues"
- HDB (HDFC Bank Limited) score 63.4 — "Sebi proposes merchant banker exemption for small-value private debt issues"
- IDBI.NS (IDBI BANK LIMITED) score 59.5 — "Sebi proposes merchant banker exemption for small-value private debt issues"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 59.5 — "Sebi proposes merchant banker exemption for small-value private debt issues"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 59.5 — "Sebi proposes merchant banker exemption for small-value private debt issues"
- COIN (Coinbase Global, Inc.) score 51.6 — "Global Market Today: Asian shares slip as US stock futures dip ahead of Warsh’s Jackson Ho"
- TECHM.NS (TECH MAHINDRA LIMITED) score 51.3 — "MUSK, ALTMAN AND HUANG HEADLINE G20 TECH TALKS Elon Musk, Sam Altman, Jensen Huang and Dav"
- BOND (PIMCO Active Bond Exchange-Tra) score 50.0 — "Irdai opens NDB's Maharajah INR bonds to insurers"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 49.7 — "MUSK, ALTMAN AND HUANG HEADLINE G20 TECH TALKS Elon Musk, Sam Altman, Jensen Huang and Dav"
- TECH (Bio-Techne Corp) score 49.7 — "MUSK, ALTMAN AND HUANG HEADLINE G20 TECH TALKS Elon Musk, Sam Altman, Jensen Huang and Dav"
- OHI (Omega Healthcare Investors, In) score 44.7 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Highlights: Nasdaq, S&P 500 lifted by"
- NVDA (NVIDIA Corporation) score 41.6 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Highlights: Nasdaq, S&P 500 lifted by"
- LTH (Life Time Group Holdings, Inc.) score 34.3 — "PRESIDENTIAL CALENDAR — THURSDAY, AUGUST 27 🔸 8:00 AM ET — Executive Time | White House 🔸 "
- CHKP (Check Point Software Technolog) score 30.1 — "Hy Tech IPO: Subscription hits massive 244x, eclipses Tempsens by a wide margin; check lat"
- 301077.SZ (CHINASTARS) score 27.4 — "China-Nepal flash flood: 392 dead and over 1,000 missing, including hundreds of foreigners"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 19.7 — "FED'S SCHMID: ENERGY SHOCK IS LEAKING INTO ECONOMY"
- JIOFIN.BO (Jio Financial Services Limited) score 19.2 — "MOSCOW HAS REASON TO BELIEVE THAT FRENCH AND UKRAINIAN SECURITY SERVICES WERE BEHIND RECEN"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 18.4 — "Good Good Golf ad fallout deepens as Callaway ends partnership, retailers pull gear and Go"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 15.0 — "Piramal Finance’s Rs 2,100-crore QIP sees 10x demand as BlackRock, Goldman lead institutio"
- MS (Morgan Stanley) score 14.4 — "JPMorgan, Apollo Urge Inflation Focus for Warsh’s Big Speech"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.3 — "Stocks in news: Wipro, Lenskart, Tata Motors PV, Ather Energy and Kotak Bank"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.2 — "Stocks in news: Wipro, Lenskart, Tata Motors PV, Ather Energy and Kotak Bank"
- HDBFS.BO (HDB FINANCIAL SERVICES LIMITED) score 12.3 — "Copper’s record run is sending three clear messages about the state of financial markets t"
- META (Meta) score 12.0 — "Gold rate today: Precious metal rises 12% this month. Is it the right time to buy gold?"
- PCJEWELLER.NS (PC JEWELLER LTD) score 11.6 — "Deepa Jewellers IPO: ₹460-cr issue to open on September 1, price band fixed at ₹168-177"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 11.5 — "Motilal Oswal initiates coverage on Adani Enterprises with Buy, sees 25% upside. Here’s wh"
- BHARATCOAL.NS (BHARAT COKING COAL LTD) score 10.1 — "45 Power Plants in India Running on Critically Low Levels of Coal Stocks"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 7.9 — "BIG DEAL | ICICI Prudential raises stake in SBI Cards and Payment Services to 7.30%"
- VT (Vanguard Total World Stock Ind) score 6.1 — "Bill Gates lists 3 big risks to AI shift. Is the world heading towards turbulent times?"
- JUSTDIAL.BO (JUST DIAL LTD.) score 5.8 — "I just had my first baby and don’t want to go back to work. Is quitting for a year a bad i"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 4.9 — "Lenskart shares block deal: Alpha Wave Ventures II likely to sell 1.2% stake worth Rs 1,31"
- DKS (Dick's Sporting Goods Inc) score 3.7 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"
- MRNA (Moderna, Inc.) score 2.8 — "Can Wolfe’s upgrade push Moderna stock higher?"
- VOLTAS.NS (VOLTAS LTD) score 0.5 — "Voltas reported strong growth in June quarter, but failed to impress"
- FINCABLES.NS (FINOLEX CABLES LTD) score 0.1 — "Finolex Cables ends 6% higher after Q1 results, Jefferies lift target to ₹1,410"
- CUPID.NS (CUPID LIMITED) score 0.1 — "Cupid shares jump nearly 9% in two days post Q1 earnings"

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