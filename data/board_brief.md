# Transmission Layer — board brief · 2026-10-02 10:29Z

data as of **2026-10-02** · 97 series · 11 red / 42 amber · 8 events surfaced (35 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.476, 1d in regime; vol-pct 0.285, breadth-off 0.667, Markov P(high-vol) 0.011)
- [INVERTED] **safe_haven_gold** — corr20 -0.47, corr60 -0.44, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.77, corr60 0.85, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.1, corr60 0.19, last shift 2026-07-07. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.01, corr60 0.11, last shift 2026-08-19. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.78, corr60 -0.76, last shift 2026-05-05. Channel: vol spike -> equity drawdown
- [INVERTED] **dxy_inr_channel** — corr20 -0.26, corr60 -0.09, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [VALID] **real_rates_gold_inverse** — corr20 -0.29, corr60 -0.25, last shift 2026-08-12. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.45, corr60 0.19, last shift 2026-07-24. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** dyn_hdb → usd_inr: leads 1d (ccf -0.352, β -0.0875, p 0.0); driver zc 1.62 → expected -0.237%. Type hit-rate 0.825 (n=2349).
- Track record · residual_reversion: hit-rate **0.501** (n=1130) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.825** (n=2349) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [AMBER 7.23] commodities · 2 series ↓
- wti [COMMODITIES]: last 89.49, z20 -1.40, zc -1.35, resid-z 1.59 [unexplained], 1d -3.64%, 1-session move -3.64% ≥ 1.5%
- brent [COMMODITIES]: last 99.91, z20 -0.94, zc -1.01, resid-z -0.11 [quiet], 1d -2.35%, 1-session move -2.35% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (inverse) — not yet - watch; rho -0.57 vs wti
- Source: Brent Holds Above $102 as Gulf Export Rebound Offsets U.S. Military Moves — OilPrice, 2026-10-02. https://oilprice.com/Latest-Energy-News/World-News/Brent-Holds-Above-102-as-Gulf-Export-Rebound-Offsets-US-Military-Moves.html
- Source: Market crash wipes out Rs 26 lakh cr in 8 weeks! Why soaring bond yields may hurt Sensex, Nifty more than elevated oil prices — ET Markets, 2026-10-02. https://economictimes.indiatimes.com/markets/stocks/news/market-crash-wipes-out-rs-26-lakh-cr-in-8-weeks-why-soaring-bond-yields-may-hurt-sensex-nifty-more-than-elevated-oil-prices/articleshow/134632014.cms
- Source: Buy ONGC, Sell Oil India| Kotak raises FY27 oil price assumption to $90 — Mint Markets, 2026-10-02. https://www.livemint.com/market/stock-market-news/buy-ongc-sell-oil-india-kotak-raises-fy27-oil-price-assumption-to-90-11790915589820.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-31 (d=0.05), 2025-04-29 (d=0.06)

### [RED 6.81] cross-asset · 5 series ↑
- ust_30y [RATES]: last 5.64, z20 2.88, zc 1.10, resid-z 0.74 [quiet], 1d 0.89%, |z20|=2.88; 1y-pct=100
- ust_10y [RATES]: last 5.29, z20 2.09, zc 0.55, resid-z 0.14 [quiet], 1d 0.57%, |z20|=2.09; 1y-pct=100
- dyn_bond [EQUITIES]: last 86.74, z20 -2.04, zc -0.75, resid-z 1.10 [quiet], 1d -0.29%, |z20|=2.04; 1y-pct=0
- tips_10y_real [RATES]: last 2.93, z20 1.96, zc 0.33, resid-z 0.02 [quiet], 1d 0.69%, |z20|=1.96; 1y-pct=100
- ust_2y [RATES]: last 4.88, z20 1.27, zc -0.15, resid-z -0.64 [quiet], 1d -0.20%, 1y-pct=99
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: brent (co-move) — not yet - watch; rho 0.65 vs ust_30y, historically leads by 3d
- Watch next: brent_wti_spread (co-move) — not yet - watch; rho 0.502 vs ust_10y, historically leads by 4d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.544 vs dyn_bond
- Source: Here’s the bond-market alternative as U.S. and other developed markets debt deteriorate — MarketWatch Top, 2026-10-02. https://www.marketwatch.com/story/heres-the-bond-market-alternative-as-u-s-and-other-developed-markets-debt-deteriorate-e3d57b02?mod=mw_rss_topstories
- Source: US bond yields: Trump may disappoint stocks, gold investors with these 2 steps to resolve debt crisis | Experts' view — Mint Markets, 2026-10-02. https://www.livemint.com/market/stock-market-news/us-bond-yields-trump-may-disappoint-stocks-gold-investors-with-these-2-steps-to-resolve-debt-crisis-experts-view-11790910214887.html
- Source: Market crash wipes out Rs 26 lakh cr in 8 weeks! Why soaring bond yields may hurt Sensex, Nifty more than elevated oil prices — ET Markets, 2026-10-02. https://economictimes.indiatimes.com/markets/stocks/news/market-crash-wipes-out-rs-26-lakh-cr-in-8-weeks-why-soaring-bond-yields-may-hurt-sensex-nifty-more-than-elevated-oil-prices/articleshow/134632014.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [AMBER 6.33] usd_inr ↑
- usd_inr [FX]: last 96.30, z20 1.33, zc 0.73, resid-z 0.79 [quiet], 1d 0.39%, 20d range extreme; 1y-pct=96
- **Mechanism**: usd_inr ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.39 via usd_inr, z 0.81, quiet)
- **India receivers**: dyn_idbi_ns (rho -0.39, z 0.81)
- Source: ETMarkets Smart Talk: Rupee under pressure, inflation sticky: Will RBI be forced to rethink rates? Ankita Pathak, Ionic Asset — ET Markets, 2026-10-02. https://economictimes.indiatimes.com/markets/expert-view/etmarkets-smart-talk-rupee-under-pressure-inflation-sticky-will-rbi-be-forced-to-rethink-rates-ankita-pathak-ionic-asset/articleshow/134634188.cms
- Source: FCNR inflows cushion rupee, BoP; FII flows crucial for sustained external stability: Report — BusinessLine Mkts, 2026-10-02. https://www.thehindubusinessline.com/markets/fcnr-inflows-cushion-rupee-bop-fii-flows-crucial-for-sustained-external-stability-report/article71535966.ece
- Source: Rupee sinks to 96.31, logs biggest fall in over 2 months — ET Markets, 2026-10-02. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-sinks-to-96-31-logs-biggest-fall-in-over-2-months/articleshow/134630728.cms
- Historical analogues: 2026-07-10 (d=0.0), 2024-11-06 (d=0.01), 2025-09-16 (d=0.01)

### [RED 6.3] dyn_ohi ↓
- dyn_ohi [EQUITIES]: last 45.23, z20 -4.30, zc -1.83, resid-z -0.48 [moved], 1d -2.33%, |z20|=4.30
- **Mechanism**: dyn_ohi ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Investors worried over bloodbath as Nifty 50 sees longest weekly losing streak in 25 yrs - Outlook for H2 from experts — Mint Markets, 2026-10-02. https://www.livemint.com/market/stock-market-news/investors-worried-over-bloodbath-as-nifty-50-sees-longest-weekly-losing-streak-in-25-yrs-outlook-for-h2-from-experts-11790922247662.html
- Source: Global Markets | Japan's Nikkei retreats from 6-week high as investors lock in gains — ET Markets, 2026-10-02. https://economictimes.indiatimes.com/markets/us-stocks/news/global-markets-japans-nikkei-retreats-from-6-week-high-as-investors-lock-in-gains/articleshow/134633243.cms
- Source: US bond yields: Trump may disappoint stocks, gold investors with these 2 steps to resolve debt crisis | Experts' view — Mint Markets, 2026-10-02. https://www.livemint.com/market/stock-market-news/us-bond-yields-trump-may-disappoint-stocks-gold-investors-with-these-2-steps-to-resolve-debt-crisis-experts-view-11790910214887.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-14 (d=0.06), 2025-04-02 (d=0.09)

### [RED 6.19] cross-asset · 4 series ↓
- nifty_50 [INDICES]: last 22421.95, z20 -2.53, zc -1.36, resid-z -1.33 [quiet], 1d -0.88%, |z20|=2.53; 1y-pct=0
- nifty_midcap_100 [INDICES]: last 58732.00, z20 -2.52, zc -1.06, resid-z -0.70 [quiet], 1d -0.99%, |z20|=2.52
- india_vix [INDICES]: last 14.46, z20 2.49, zc 1.22, resid-z n/a [quiet], 1d 7.19%, |z20|=2.49
- dyn_policybzr_ns [EQUITIES]: last 980.00, z20 -2.24, zc -1.16, resid-z -0.96 [quiet], 1d -7.89%, |z20|=2.24; 1y-pct=0
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.49).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho 0.601 via nifty_midcap_100, z -1.56, reacted); dyn_jiofin_bo (rho 0.589 via nifty_50, z -2.93, reacted); nifty_fmcg (rho 0.588 via nifty_50, z -3.7, reacted); nifty_metal (rho 0.523 via nifty_midcap_100, z -2.96, reacted); dyn_indusindbk_bo (rho 0.492 via nifty_midcap_100, z -2.15, reacted)
- **India receivers**: midcap_largecap_ratio (rho 0.601, z -1.56); dyn_jiofin_bo (rho 0.589, z -2.93); nifty_fmcg (rho 0.588, z -3.7); nifty_metal (rho 0.523, z -2.96)
- Source: Investors worried over bloodbath as Nifty 50 sees longest weekly losing streak in 25 yrs - Outlook for H2 from experts — Mint Markets, 2026-10-02. https://www.livemint.com/market/stock-market-news/investors-worried-over-bloodbath-as-nifty-50-sees-longest-weekly-losing-streak-in-25-yrs-outlook-for-h2-from-experts-11790922247662.html
- Source: Nifty 500 stocks fall up to 70% from 52-week highs; why broad market recovery may remain elusive in short term — Mint Markets, 2026-10-02. https://www.livemint.com/market/stock-market-news/nifty-500-stocks-fall-up-to-70-from-52-week-highs-why-broad-market-recovery-may-remain-elusive-in-short-term-11790910378791.html
- Source: Experts' views: Can new HDFC Bank CEO-MD Anup Bagchi's appointment change fortunes of Sensex, Nifty, Bank Nifty indices? — Mint Markets, 2026-10-02. https://www.livemint.com/market/stock-market-news/experts-views-can-new-hdfc-bank-ceo-md-anup-bagchis-appointment-change-fortunes-of-sensex-nifty-bank-nifty-indices-11790919995601.html
- Historical analogues: 2025-07-21 (d=0.49), 2025-07-14 (d=0.72), 2025-12-30 (d=0.96)

### [AMBER 5.26] fx · 2 series ↓
- eur_usd [FX]: last 1.12, z20 -2.43, zc -2.45, resid-z -2.67 [unexplained], 1d -0.78%, |z20|=2.43; 1y-pct=0
- gbp_usd [FX]: last 1.32, z20 -1.55, zc -1.14, resid-z -1.22 [quiet], 1d -0.42%, |z20|=1.55
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.365 via gbp_usd, z -2.12, reacted); nifty_50 (rho 0.353 via eur_usd, z -2.53, reacted)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.544 vs eur_usd, historically leads by 3d
- **India receivers**: dyn_muthootfin_ns (rho 0.365, z -2.12); nifty_50 (rho 0.353, z -2.53)
- Source: EURO EXTENDS LOSES AGAINST US DOLLAR, LAST DOWN 1% AT $1.12165 — DeItaone, 2026-10-01. https://t.me/walter_bloomberg/36495
- Source: UK pound falls to three-month lows as investors fret over rates, oil — ET Markets, 2026-10-01. https://economictimes.indiatimes.com/markets/us-stocks/news/uk-pound-falls-to-three-month-lows-as-investors-fret-over-rates-oil/articleshow/134621868.cms
- Source: EURO SLIDE CONTINUES; LAST DOWN 0.55% AT $1.127 — DeItaone, 2026-10-01. https://t.me/walter_bloomberg/36444
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [AMBER 5.13] indices · 2 series ↑
- nikkei_225 [INDICES]: last 68190.14, z20 2.30, zc -0.56, resid-z 1.26 [quiet], 1d -1.11%, |z20|=2.30
- taiwan_weighted [INDICES]: last 48483.91, z20 1.73, zc 0.25, resid-z -0.09 [quiet], 1d 0.27%, |z20|=1.73; 1y-pct=100
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.7).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_it (rho -0.425 via taiwan_weighted, z -0.79, quiet); dyn_techm_ns (rho -0.419 via taiwan_weighted, z -0.73, quiet)
- Watch next: kospi (co-move) — not yet - watch; rho 0.797 vs nikkei_225
- **India receivers**: nifty_it (rho -0.425, z -0.79); dyn_techm_ns (rho -0.419, z -0.73)
- Source: Global Markets | Japan's Nikkei retreats from 6-week high as investors lock in gains — ET Markets, 2026-10-02. https://economictimes.indiatimes.com/markets/us-stocks/news/global-markets-japans-nikkei-retreats-from-6-week-high-as-investors-lock-in-gains/articleshow/134633243.cms
- Source: Global Market: Japan’s Nikkei hits six-week high as chip stocks rally on AI optimism — ET Markets, 2026-10-01. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-hits-six-week-high-as-chip-stocks-rally-on-ai-optimism/articleshow/134609469.cms
- Historical analogues: 2025-12-30 (d=0.7), 2025-07-11 (d=0.77), 2026-06-09 (d=1.0)

### [RED 4.93] dyn_jiofin_bo ↓
- dyn_jiofin_bo [EQUITIES]: last 212.00, z20 -2.93, zc -1.66, resid-z -0.41 [priced], 1d -2.12%, |z20|=2.93; 1y-pct=0
- **Mechanism**: dyn_jiofin_bo ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.589 via dyn_jiofin_bo, z -2.53, reacted); nifty_midcap_100 (rho 0.446 via dyn_jiofin_bo, z -2.52, reacted)
- **India receivers**: nifty_50 (rho 0.589, z -2.53); nifty_midcap_100 (rho 0.446, z -2.52)
- Source: Geojit Financial Services reshuffles top deck; Jones George to take over as MD — ET Markets, 2026-09-30. https://economictimes.indiatimes.com/markets/stocks/news/geojit-financial-services-reshuffles-top-deck-jones-george-to-take-over-as-md/articleshow/134596797.cms
- Source: Geojit Financial Services appoints Jones George as MD, founder C J George moves to Executive Chairman role — BusinessLine Mkts, 2026-09-30. https://www.thehindubusinessline.com/markets/geojit-financial-services-appoints-jones-george-as-md-founder-c-j-george-moves-to-executive-chairman-role/article71527951.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-08-14 (d=0.01), 2025-08-06 (d=0.03)

## Watchlist (below surfacing floor)
commodities · 2 series ↓ (4.72), indices · 4 series ↓ (4.64), rates · 2 series ↑ (3.97), gold_silver_ratio ↑ (3.83), dxy ↑ (3.8), nifty_fmcg ↓ (3.7), dow_jones ↓ (3.61), comex_gold ↓ (3.54), dyn_nvda ↑ (3.37), dyn_4417_t ↑ (3.22), nasdaq_100 ↑ (3.21), hang_seng ↓ (3.01)

## India macro
- nifty_50: 22421.9492 (1d -0.88%, z20 -2.53, flag red)
- nifty_midcap_100: 58732.0000 (1d -0.99%, z20 -2.52, flag red)
- usd_inr: 96.3000 (1d 0.39%, z20 1.33, flag amber)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6194 (1d -0.12%, z20 -1.56, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · IMD weekly rainfall T-3d

## News-tracked universe (why each is watched)
- INOXINDIA.NS (INOX INDIA LIMITED) score 99.3 — "FPIs pull record Rs 3 lakh crore from Indian equities in 9 months. More pain ahead?"
- COALINDIA.NS (COAL INDIA LTD) score 93.8 — "FPIs pull record Rs 3 lakh crore from Indian equities in 9 months. More pain ahead?"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 92.4 — "FPIs pull record Rs 3 lakh crore from Indian equities in 9 months. More pain ahead?"
- INDIANB.NS (INDIAN BANK) score 71.8 — "HDFC Bank shares: Will stock finally reward its investors after Anup Bagchi as new MD-CEO?"
- BOND (PIMCO Active Bond Exchange-Tra) score 63.1 — "US dollar climbs to 17-month high as bond rout, French fiscal worries weigh on euro"
- COIN (Coinbase Global, Inc.) score 56.2 — "Japan government bond yields fall as global markets steady"
- OHI (Omega Healthcare Investors, In) score 51.4 — "HDFC Bank shares: Will stock finally reward its investors after Anup Bagchi as new MD-CEO?"
- BAC (Bank of America Corporation) score 49.9 — "HDFC Bank shares: Will stock finally reward its investors after Anup Bagchi as new MD-CEO?"
- HDB (HDFC Bank Limited) score 48.4 — "HDFC Bank shares: Will stock finally reward its investors after Anup Bagchi as new MD-CEO?"
- TECHM.NS (TECH MAHINDRA LIMITED) score 46.5 — "Kotak Mahindra Bank shares: How new MD-CEO Anup Saha's appointment can impact the stock - "
- IDBI.NS (IDBI BANK LIMITED) score 44.6 — "HDFC Bank shares: Will stock finally reward its investors after Anup Bagchi as new MD-CEO?"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 44.6 — "HDFC Bank shares: Will stock finally reward its investors after Anup Bagchi as new MD-CEO?"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 44.6 — "HDFC Bank shares: Will stock finally reward its investors after Anup Bagchi as new MD-CEO?"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 42.1 — "TCS, Wipro, Infosys, HCL Tech: Why experts see IT stocks' price jump on Monday — What's gi"
- TECH (Bio-Techne Corp) score 42.1 — "TCS, Wipro, Infosys, HCL Tech: Why experts see IT stocks' price jump on Monday — What's gi"
- CHKP (Check Point Software Technolog) score 41.7 — "Stock market holiday today: Are NSE, BSE closed for Gandhi Jayanti? Check 2026 holiday lis"
- SEPN (Septerna, Inc.) score 37.7 — "H1 digest: New capex proposals rise, but momentum plunges in September quarter"
- LTH (Life Time Group Holdings, Inc.) score 34.7 — "RBI MPC Meeting October 2026: Repo rate hike soon? Date, announcement time, members, monet"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 33.3 — "US ENERGY SECRETARY CHRIS WRIGHT:ABSOLUTELY WE WILL ASK EUROPE TO RELEASE STRATEGIC DIESEL"
- TGT (Target Corporation) score 30.0 — "Top 2 stocks to buy or sell for short-term: Laurus Labs, Canara Bank by Chandan Taparia - "
- 301077.SZ (CHINASTARS) score 25.9 — "Oil prices edge higher, hover around $102 as US-Iran tensions, China fuel curbs support pr"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 21.4 — "US bond yields: Trump may disappoint stocks, gold investors with these 2 steps to resolve "
- BZ=F (Brent Crude Oil Last Day Finan) score 19.5 — "EURO EXTENDS LOSES AGAINST US DOLLAR, LAST DOWN 1% AT $1.12165"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 13.7 — "Adani Group's most valuable company sets new record; shares major business update"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 13.2 — "Power stocks fall despite  ₹1.86 lakh crore PM-DHARA scheme: Tata Power, Adani Power, NTPC"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 13.2 — "Power stocks fall despite  ₹1.86 lakh crore PM-DHARA scheme: Tata Power, Adani Power, NTPC"
- JIOFIN.BO (Jio Financial Services Limited) score 12.0 — "Financial stocks are falling below a key chart level to warn the worst is yet to come"
- JUSTDIAL.BO (JUST DIAL LTD.) score 10.4 — "AUGUST JOBS STRENGTH MAY HAVE BEEN OVERSTATED August payroll growth of 162K was boosted by"
- POLICYBZR.NS (PB FINTECH LIMITED) score 10.2 — "Where could PB Fintech share price be in the next five years?"
- GS (Goldman Sachs Group, Inc. (The) score 9.9 — "U.S. Diesel Export Ban Would Hit Latin America Hardest: Goldman"
- VT (Vanguard Total World Stock Ind) score 8.4 — "Jio Platforms IPO in final stages after concluding worldwide roadshows"
- META (Meta) score 8.3 — "Gold price today: Precious metal slips ahead of US Jobs data; MCX closed for Gandhi Jayant"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 7.1 — "Down 10% in a month; Bajaj Finance approves  ₹11,700 cr QIP,  ₹5,800 cr warrants to Bajaj "
- JEF (Jefferies Financial Group Inc.) score 6.6 — "Jefferies is bullish on 6 healthcare stocks with upside potential of up to 46%. Own any?"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 6.6 — "Macquarie stock recommendations: ICICI Bank, SBI, PayTM to LIC — top 11 financial shares t"
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 6.4 — "ESDS, Lumino, Purple Style Labs: 18 IPO stocks facing anchor lock-in expiry in October - C"
- NVDA (NVIDIA Corporation) score 6.0 — "Amazon is hiking chip-rental prices and reportedly moving Nvidia processors off the balanc"
- MS (Morgan Stanley) score 3.7 — "Morgan Stanley raises Lenskart target price to Rs 718; bull case implies 41% upside. Here’"
- VOLTAS.NS (VOLTAS LTD) score 0.3 — "Voltas’s market share is growing. Will margins follow?"
- DELL (Dell Technologies Inc.) score 0.2 — "Global Market: BoE's Lombardelli says rates may need to rise if energy prices stay high"

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