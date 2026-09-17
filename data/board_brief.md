# Transmission Layer — board brief · 2026-09-17 09:25Z

data as of **2026-09-17** · 97 series · 11 red / 33 amber · 8 events surfaced (24 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.65, 6d in regime; vol-pct 0.467, breadth-off 0.833, Markov P(high-vol) 0.016)
- [INVERTED] **safe_haven_gold** — corr20 -0.38, corr60 -0.26, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.78, corr60 0.87, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.21, corr60 0.32, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.18, corr60 0.08, last shift 2026-06-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.9, corr60 -0.84, last shift 2026-07-23. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.08, corr60 -0.03, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.33, corr60 -0.08, last shift 2026-07-24. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.2, corr60 0.13, last shift 2026-07-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** dyn_bac → asx_200: leads 1d (ccf 0.472, β 0.2304, p 0.0); driver zc -1.52 → expected -0.631%. Type hit-rate 0.822 (n=2069).
- Track record · residual_reversion: hit-rate **0.497** (n=1111) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.822** (n=2069) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.48] cross-asset · 6 series ↓
- dyn_ms [EQUITIES]: last 202.46, z20 -3.33, zc -0.99, resid-z 0.41 [quiet], 1d -1.85%, |z20|=3.33
- dow_jones [INDICES]: last 51477.73, z20 -3.08, zc -1.48, resid-z -2.76 [unexplained], 1d -1.18%, |z20|=3.08
- dyn_vt [EQUITIES]: last 157.43, z20 -2.84, zc -0.48, resid-z 0.26 [quiet], 1d -0.38%, |z20|=2.84
- sp500 [INDICES]: last 7553.33, z20 -2.73, zc -0.57, resid-z -0.73 [quiet], 1d -0.43%, |z20|=2.73
- russell_2000 [INDICES]: last 2859.05, z20 -2.18, zc -0.34, resid-z -0.20 [quiet], 1d -0.39%, |z20|=2.18
- nasdaq_100 [INDICES]: last 28953.02, z20 -1.84, zc 0.05, resid-z 0.37 [quiet], 1d 0.05%, |z20|=1.84
- **Mechanism**: cross-asset · 6 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.581 vs dyn_ms, historically leads by 4d
- Watch next: vix (inverse) — not yet - watch; rho -0.651 vs dyn_ms
- Watch next: dyn_nvda (co-move) — not yet - watch; rho 0.559 vs sp500
- Watch next: dax (co-move) — not yet - watch; rho 0.545 vs dow_jones
- Source: Why the S&P 500 could still advance after a Fed hike, according to a Wall Street strategist — MarketWatch Top, 2026-09-17. https://www.marketwatch.com/story/why-the-s-p-500-could-still-advance-after-a-fed-hike-according-to-a-wall-street-strategist-d357b4f2?mod=mw_rss_topstories
- Source: $46 billion IPO: NSE is the world’s most expensive stock exchange. Can it also become the most valuable? — ET Markets, 2026-09-17. https://economictimes.indiatimes.com/markets/ipos/fpos/46-billion-ipo-nse-is-the-worlds-most-expensive-stock-exchange-can-it-also-become-the-most-valuable/articleshow/134302520.cms
- Source: Why optical stocks Lumentum and Coherent were the day’s biggest S&P 500 gainers — MarketWatch Top, 2026-09-16. https://www.marketwatch.com/story/why-optical-stocks-lumentum-and-coherent-were-the-days-biggest-gainers-051af440?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-17 (d=0.52), 2026-05-14 (d=0.68)

### [AMBER 6.42] cross-asset · 5 series ↑
- tips_10y_real [RATES]: last 2.62, z20 2.48, zc 0.44, resid-z -0.10 [quiet], 1d 0.77%, |z20|=2.48; 1y-pct=100
- ust_10y [RATES]: last 5.00, z20 2.43, zc 0.62, resid-z 0.14 [quiet], 1d 0.60%, |z20|=2.43; 1y-pct=100
- ust_2y [RATES]: last 4.67, z20 2.32, zc 0.33, resid-z -0.22 [quiet], 1d 0.43%, |z20|=2.32; 1y-pct=100
- dyn_bond [EQUITIES]: last 88.53, z20 -2.06, zc -0.44, resid-z 0.95 [quiet], 1d -0.15%, |z20|=2.06; 1y-pct=0
- ust_30y [RATES]: last 5.36, z20 1.91, zc 0.48, resid-z 0.14 [quiet], 1d 0.37%, |z20|=1.91; 1y-pct=99
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.417 via ust_2y, z -0.42, quiet)
- **India receivers**: midcap_largecap_ratio (rho -0.417, z -0.42)
- Source: Global Market: Eurozone bond yields edge higher after Fed rate hike — ET Markets, 2026-09-17. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-eurozone-bond-yields-edge-higher-after-fed-rate-hike/articleshow/134306233.cms
- Source: Shorter-dated US Treasury yields surge in anticipation of another Fed rate hike — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/us-stocks/news/shorter-dated-us-treasury-yields-surge-in-anticipation-of-another-fed-rate-hike/articleshow/134296264.cms
- Source: Morgan Stanley shifts $10 billion in municipal bond mutual funds to ETFs — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/us-stocks/news/morgan-stanley-shifts-10-billion-in-municipal-bond-mutual-funds-to-etfs/articleshow/134291061.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 5.97] dyn_bac ↓
- dyn_bac [EQUITIES]: last 57.89, z20 -3.97, zc -1.52, resid-z -0.02 [moved], 1d -2.74%, |z20|=3.97
- **Mechanism**: dyn_bac ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: eur_inr (rho 0.359 via dyn_bac, z -0.27, quiet)
- **India receivers**: eur_inr (rho 0.359, z -0.27)
- Source: TRUMP: LOWER INTEREST RATES FOR UNITED STATES OF AMERICA, AND FAST — DeItaone, 2026-09-16. https://t.me/walter_bloomberg/35874
- Source: TRUMP DEMANDS U.S. INTEREST RATES AT 1% OR LOWER President Trump is calling for U.S. interest rates to be cut to 1% or below, arguing America’s credit strength and booming investment justify dramatically cheaper borrowing. He also criticized U.S. trade deficits, claiming the country is effectively “ — DeItaone, 2026-09-16. https://t.me/walter_bloomberg/35872
- Source: 5% Treasury yields mean America’s debt bill just got a lot bigger — MarketWatch Top, 2026-09-16. https://www.marketwatch.com/story/5-treasury-yields-mean-americas-debt-bill-just-got-a-lot-bigger-8a5702b0?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2024-11-01 (d=0.01), 2025-04-23 (d=0.03)

### [RED 5.44] dyn_jef ↓
- dyn_jef [EQUITIES]: last 47.33, z20 -3.44, zc -1.12, resid-z -0.71 [quiet], 1d -3.07%, |z20|=3.44
- **Mechanism**: dyn_jef ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Solar Industries’ defence share may fall to 22-25% by FY30 after Omnia deal: Jefferies — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/stocks/news/solar-industries-defence-share-may-fall-to-22-25-by-fy30-after-omnia-deal-jefferies/articleshow/134280191.cms
- Source: Solar Industries shares plunge 17% in 2 days. Why Jefferies, Nuvama still see up to 46% upside — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/stocks/news/solar-industries-shares-plunge-17-in-2-days-why-jefferies-nuvama-still-see-up-to-46-upside/articleshow/134279133.cms
- Source: Paytm shares jump 7% as Jefferies, other brokerages raise target prices and earnings estimates after new UPI charges — ET Markets, 2026-09-16. https://economictimes.indiatimes.com/markets/stocks/news/paytm-shares-jump-7-as-jefferies-other-brokerages-raise-target-prices-and-earnings-estimates-after-new-upi-charges/articleshow/134278132.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-01 (d=0.04), 2025-08-19 (d=0.07)

### [RED 4.97] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 5560.00, z20 2.97, zc 0.75, resid-z 1.60 [unexplained], 1d 2.77%, |z20|=2.97; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Apollo Micro Systems share price jumps 3.5% after recent fall | technical experts flag key levels — Mint Markets, 2026-09-17. https://www.livemint.com/market/stock-market-news/apollo-micro-systems-share-price-jumps-3-5-after-recent-fall-technical-experts-flag-key-levels-11789626185762.html
- Source: NSE IPO buzz lifts New India Assurance, IFCI up to 9% | What do technical experts say? — Mint Markets, 2026-09-17. https://www.livemint.com/market/stock-market-news/nse-ipo-buzz-lifts-new-india-assurance-ifci-up-to-9-what-do-technical-experts-say-11789623090580.html
- Source: Sensex, Nifty soar despite Fed rate hike — Is it NSE IPO impact and 6 listings today? Experts decode stock market rise — Mint Markets, 2026-09-17. https://www.livemint.com/market/stock-market-news/sensex-nifty-soar-despite-fed-rate-hike-is-it-nse-ipo-impact-and-6-listings-today-experts-decode-stock-market-rise-11789621059076.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

### [AMBER 4.43] cross-asset · 2 series ↓
- nifty_50 [INDICES]: last 23296.65, z20 -1.59, zc 0.63, resid-z 0.38 [quiet], 1d 0.34%, |z20|=1.59
- dyn_jiofin_bo [EQUITIES]: last 229.10, z20 -1.35, zc 1.34, resid-z 0.98 [quiet], 1d 1.82%, 1y-pct=2
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-06 (z-distance 0.09).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.622 via nifty_50, z -1.74, reacted); nifty_fmcg (rho 0.611 via nifty_50, z -0.7, quiet); nifty_it (rho 0.502 via nifty_50, z -1.32, reacted); dyn_techm_ns (rho 0.477 via nifty_50, z -0.87, quiet); dyn_indianb_ns (rho 0.467 via dyn_jiofin_bo, z -1.75, reacted)
- Watch next: nifty_fmcg (co-move) — not yet - watch; rho 0.611 vs nifty_50, historically leads by 3d
- **India receivers**: nifty_midcap_100 (rho 0.622, z -1.74); nifty_fmcg (rho 0.611, z -0.7); nifty_it (rho 0.502, z -1.32); dyn_techm_ns (rho 0.477, z -0.87)
- Source: Sensex today | Stock Market Live: Sensex, Nifty hold firm; IT stocks under pressure, NSE IPO in focus — BusinessLine Mkts, 2026-09-17. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-17th-september-2026/article71472777.ece
- Source: Happy Forgings share price target: 'Industrials, PVs to drive next leg of growth' - Buy from Motilal Oswal Fin Services — Mint Markets, 2026-09-17. https://www.livemint.com/market/stock-market-news/happy-forgings-share-price-target-industrials-pvs-to-drive-next-leg-of-growth-buy-rating-from-motilal-oswal-financ-11789628364291.html
- Source: Nifty Bank fails to hold ground after US Fed rate hike; HDFC, Yes Bank, ICICI among top laggards; Will they turn tide? — Mint Markets, 2026-09-17. https://www.livemint.com/market/stock-market-news/nifty-bank-fails-to-hold-ground-after-us-fed-rate-hike-hdfc-yes-bank-icici-among-top-laggards-will-they-turn-tide-11789623594191.html
- Historical analogues: 2025-08-06 (d=0.09), 2025-07-29 (d=0.53), 2025-07-18 (d=0.65)

### [RED 4.37] fx · 2 series ↓
- eur_usd [FX]: last 1.15, z20 -3.54, zc -1.70, resid-z -1.69 [unexplained], 1d -0.51%, |z20|=3.54
- gbp_usd [FX]: last 1.34, z20 -2.99, zc -1.65, resid-z -1.60 [unexplained], 1d -0.58%, |z20|=2.99
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_icicigi_bo (rho -0.381 via gbp_usd, z -0.87, quiet); nifty_50 (rho 0.375 via eur_usd, z -1.59, reacted)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.559 vs eur_usd, historically leads by 3d
- **India receivers**: dyn_icicigi_bo (rho -0.381, z -0.87); nifty_50 (rho 0.375, z -1.59)
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [RED 4.37] fx · 2 series ↑
- usd_mxn [FX]: last 17.20, z20 3.54, zc 0.77, resid-z 0.88 [quiet], 1d 0.32%, |z20|=3.54
- aud_usd [FX]: last 0.71, z20 -1.72, zc -0.30, resid-z -0.28 [quiet], 1d -0.13%, |z20|=1.72
- **Mechanism**: fx · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.479 via aud_usd, z -1.21, reacted); dyn_karurvysya_ns (rho -0.358 via usd_mxn, z -1.21, reacted)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.536 vs aud_usd, historically leads by 3d
- **India receivers**: dyn_muthootfin_ns (rho 0.479, z -1.21); dyn_karurvysya_ns (rho -0.358, z -1.21)
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-25 (d=0.08), 2025-01-31 (d=0.11)

## Watchlist (below surfacing floor)
hy_oas ↑ (4.05), soybeans ↑ (3.46), midcap_largecap_ratio ↓ (3.42), usd_cny ↓ (3.24), dyn_hdb ↓ (3.23), gold_silver_ratio ↑ (3.03), dyn_icicigi_bo ↓ (2.87), commodities · 2 series ↑ (2.51), dxy ↑ (2.44), dyn_tech ↑ (2.16), hang_seng ↓ (2.07), brent_wti_spread ↓ (1.91)

## India macro
- nifty_50: 23296.6504 (1d 0.34%, z20 -1.59, flag amber)
- nifty_midcap_100: 61463.6016 (1d 0.96%, z20 -1.74, flag amber)
- usd_inr: 95.9200 (1d -0.08%, z20 1.27, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6383 (1d 0.62%, z20 -0.42, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 70.9 — "NSE Subscription for India IPO Starts With Valuation in Focus"
- COALINDIA.NS (COAL INDIA LTD) score 69.7 — "NSE Subscription for India IPO Starts With Valuation in Focus"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 69.0 — "NSE Subscription for India IPO Starts With Valuation in Focus"
- INDIANB.NS (INDIAN BANK) score 66.3 — "Top 5 breakout stocks to buy today by Sumeet Bagadia: Heritage Foods, HDFC Bank, JK Paper;"
- COIN (Coinbase Global, Inc.) score 55.8 — "Global Market: Nikkei gains as investors snap up gaming, pharma stocks"
- BAC (Bank of America Corporation) score 54.9 — "Top 5 breakout stocks to buy today by Sumeet Bagadia: Heritage Foods, HDFC Bank, JK Paper;"
- HDB (HDFC Bank Limited) score 48.7 — "Top 5 breakout stocks to buy today by Sumeet Bagadia: Heritage Foods, HDFC Bank, JK Paper;"
- OHI (Omega Healthcare Investors, In) score 48.5 — "NSE IPO goes live: Key things investors need to know"
- IDBI.NS (IDBI BANK LIMITED) score 44.5 — "Top 5 breakout stocks to buy today by Sumeet Bagadia: Heritage Foods, HDFC Bank, JK Paper;"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 44.5 — "Top 5 breakout stocks to buy today by Sumeet Bagadia: Heritage Foods, HDFC Bank, JK Paper;"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 44.5 — "Top 5 breakout stocks to buy today by Sumeet Bagadia: Heritage Foods, HDFC Bank, JK Paper;"
- BOND (PIMCO Active Bond Exchange-Tra) score 43.2 — "Govt bonds dip as US Fed move seen as final straw pushing RBI toward hikes"
- CHKP (Check Point Software Technolog) score 40.5 — "Top 5 breakout stocks to buy today by Sumeet Bagadia: Heritage Foods, HDFC Bank, JK Paper;"
- TECHM.NS (TECH MAHINDRA LIMITED) score 33.5 — "Manika Plastech IPO allotment likely today: GMP signals 5% listing gain. Here’s how to che"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 33.5 — "Manika Plastech IPO allotment likely today: GMP signals 5% listing gain. Here’s how to che"
- TECH (Bio-Techne Corp) score 33.5 — "Manika Plastech IPO allotment likely today: GMP signals 5% listing gain. Here’s how to che"
- SEPN (Septerna, Inc.) score 26.8 — "Buzzing stocks for Sept 17: Reliance, Infosys, Krsnaa, Mazagon Dock, Motilal Oswal, Granul"
- LTH (Life Time Group Holdings, Inc.) score 26.3 — "Gold prices fall Rs 2,000/10 gram, silver dips Rs 4,600/kg as US Fed hikes rate after 3 ye"
- 301077.SZ (CHINASTARS) score 24.4 — "Global Market: China, Hong Kong markets slip as Fed signals more rate hikes"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.7 — "MARKETS MAY BE PRICING TOO MANY RATE HIKES Markets now expect four 25bp Fed hikes over the"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 14.0 — "SS Retail IPO Day 2; GMP at 19%, subscribed 1.44 times; Check key details"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.1 — "Tata Sons Listing: 1st board meeting after RBI directive — Only 3 options, one is IPO, che"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.1 — "Tata Sons Listing: 1st board meeting after RBI directive — Only 3 options, one is IPO, che"
- BZ=F (Brent Crude Oil Last Day Finan) score 12.4 — "Dividend stocks alert, record date: Last chance to buy Cochin Shipyard, Anupam Rasayan, Ba"
- JIOFIN.BO (Jio Financial Services Limited) score 10.3 — "GMR Airports shares gain 2% after JM Financial retains Buy rating; sees up to 24% upside"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 9.7 — "Tata Sons Listing: 1st board meeting after RBI directive — Only 3 options, one is IPO, che"
- JUSTDIAL.BO (JUST DIAL LTD.) score 8.8 — "TRUMP DEMANDS U.S. INTEREST RATES AT 1% OR LOWER President Trump is calling for U.S. inter"
- VT (Vanguard Total World Stock Ind) score 8.2 — "$46 billion IPO: NSE is the world’s most expensive stock exchange. Can it also become the "
- PCJEWELLER.NS (PC JEWELLER LTD) score 8.2 — "PC Jeweller share price extend losses for fifth session, falls 9% in a week | Should you b"
- MS (Morgan Stanley) score 7.9 — "LIC, Morgan Stanley, Goldman Sachs among anchor investors as NSE raises Rs 6,746 crore ahe"
- NVDA (NVIDIA Corporation) score 7.4 — "BESSENT: TRUMP COMPLETELY ALIGNED WITH NVIDIA'S JENSEN HUANG"
- JEF (Jefferies Financial Group Inc.) score 6.5 — "Paytm shares jump 7% as Jefferies, other brokerages raise target prices and earnings estim"
- META (Meta) score 6.2 — "US Fed rate hike impact on gold: FOMC outcome on yellow metal decoded"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 5.3 — "Indonesia's new finance minister faces an uphill battle on fiscal credibility"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 5.2 — "HDFC Bank is winning the mutual fund vote over ICICI Bank. Can the shift last?"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 4.9 — "Suzlon Energy, Adani Power share prices fall: Check 1-week, 1-year and 5-year returns"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 0.9 — "Stocks to watch, Sept 15: HDFC Bank, BSE, broking firms, HCL Tech, Deccan Gold Mines, CESC"
- DELL (Dell Technologies Inc.) score 0.5 — "Why Dell and HPE were the S&P 500’s top-performing stocks today"
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