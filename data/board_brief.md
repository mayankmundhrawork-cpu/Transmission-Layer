# Transmission Layer — board brief · 2026-09-21 16:29Z

data as of **2026-09-21** · 97 series · 12 red / 31 amber · 8 events surfaced (26 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: NEUTRAL** (score 0.398, 2d in regime; vol-pct 0.17, breadth-off 0.625, Markov P(high-vol) 0.044)
- [INVERTED] **safe_haven_gold** — corr20 -0.47, corr60 -0.26, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.79, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.09, corr60 0.28, last shift 2026-07-06. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 0.16, corr60 0.08, last shift 2026-06-05. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.81, corr60 -0.8, last shift 2026-07-22. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 -0.07, corr60 -0.04, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.28, corr60 -0.07, last shift 2026-07-31. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.41, corr60 0.14, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **1 of 89** scanned series survive multiplicity control (effective p ≤ 9.870090125208009e-06)
- **SETUP** sp500 → asx_200: leads 1d (ccf 0.573, β 0.4418, p 0.0); driver zc 1.68 → expected 0.577%. Type hit-rate 0.818 (n=2048).
- **SETUP** dyn_vt → asx_200: leads 1d (ccf 0.57, β 0.4543, p 0.0); driver zc 1.65 → expected 0.605%. Type hit-rate 0.818 (n=2048).
- **SETUP** dyn_vt → aud_usd: leads 1d (ccf 0.559, β 0.3487, p 0.0); driver zc 1.65 → expected 0.464%. Type hit-rate 0.818 (n=2048).
- **SETUP** dyn_vt → usd_mxn: leads 1d (ccf -0.516, β -0.3046, p 0.0); driver zc 1.65 → expected -0.405%. Type hit-rate 0.818 (n=2048).
- **SETUP** dyn_vt → usd_brl: leads 1d (ccf -0.514, β -0.4108, p 0.0); driver zc 1.65 → expected -0.547%. Type hit-rate 0.818 (n=2048).
- **SETUP** sp500 → aud_usd: leads 1d (ccf 0.463, β 0.2792, p 0.0); driver zc 1.68 → expected 0.364%. Type hit-rate 0.818 (n=2048).
- **SETUP** nasdaq_100 → aud_usd: leads 1d (ccf 0.445, β 0.1982, p 0.0); driver zc 2.26 → expected 0.494%. Type hit-rate 0.818 (n=2048).
- **SETUP** sp500 → usd_mxn: leads 1d (ccf -0.434, β -0.2479, p 0.0); driver zc 1.68 → expected -0.324%. Type hit-rate 0.818 (n=2048).
- **SETUP** nasdaq_100 → usd_brl: leads 1d (ccf -0.421, β -0.2401, p 0.0); driver zc 2.26 → expected -0.599%. Type hit-rate 0.818 (n=2048).
- **SETUP** nasdaq_100 → usd_mxn: leads 1d (ccf -0.418, β -0.1763, p 0.0); driver zc 2.26 → expected -0.44%. Type hit-rate 0.818 (n=2048).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.359, β -2.3385, p 0.0123); driver zc 1.65 → expected -3.112%. Type hit-rate 0.818 (n=2048).
- **SETUP** dyn_vt → nifty_metal: leads 1d (ccf 0.327, β 0.5155, p 4e-05); driver zc 1.65 → expected 0.686%. Type hit-rate 0.818 (n=2048).
- **SETUP** btc_usd → asx_200: leads 1d (ccf 0.304, β 0.0862, p 0.0); driver zc 2.01 → expected 0.536%. Type hit-rate 0.818 (n=2048).
- **SETUP** sp500 → nifty_metal: leads 1d (ccf 0.294, β 0.4535, p 0.00094); driver zc 1.68 → expected 0.592%. Type hit-rate 0.818 (n=2048).
- **SETUP** btc_usd → aud_usd: leads 1d (ccf 0.288, β 0.0637, p 0.0); driver zc 2.01 → expected 0.396%. Type hit-rate 0.818 (n=2048).
- **SETUP** dyn_vt → nifty_midcap_100: leads 1d (ccf 0.275, β 0.3382, p 0.0); driver zc 1.65 → expected 0.45%. Type hit-rate 0.818 (n=2048).
- **SETUP** btc_usd → usd_mxn: leads 1d (ccf -0.26, β -0.0573, p 1e-05); driver zc 2.01 → expected -0.356%. Type hit-rate 0.818 (n=2048).
- Track record · residual_reversion: hit-rate **0.5** (n=1091) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=2048) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.6** (n=15) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.31] cross-asset · 3 series ↑
- eth_usd [CRYPTO]: last 2766.42, z20 5.99, zc 1.39, resid-z 2.02 [unexplained], 1d 5.94%, |z20|=5.99
- btc_usd [CRYPTO]: last 85932.00, z20 5.16, zc 2.01, resid-z 2.58 [unexplained], 1d 6.22%, |z20|=5.16
- dyn_coin [EQUITIES]: last 203.41, z20 2.83, zc 1.03, resid-z 0.69 [quiet], 1d 4.72%, |z20|=2.83
- **Mechanism**: cross-asset · 3 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-08-13 (z-distance 1.76).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cartrade_ns (rho 0.407 via btc_usd, z -1.47, reacted)
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.592 vs btc_usd, historically leads by 1d
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.575 vs eth_usd, historically leads by 1d
- **India receivers**: dyn_cartrade_ns (rho 0.407, z -1.47)
- Source: US Fed, Bank of Japan and others impact on Indian stock markets: Global rate hike cycle begins - Sensex, Nifty outlook — Mint Markets, 2026-09-21. https://www.livemint.com/market/stock-market-news/us-fed-bank-of-japan-and-others-impact-on-indian-stock-markets-global-rate-hike-cycle-begins-sensex-nifty-outlook-11789995507694.html
- Source: ET Alpha Wealth Summit 2.0: Mapping global capital flows to identify the next big opportunity — ET Markets, 2026-09-21. https://economictimes.indiatimes.com/markets/stocks/news/et-alpha-summit-2-0-mapping-global-capital-flows-to-identify-the-next-big-opportunity/articleshow/134389341.cms
- Source: Bitcoin price today at record high since January, briefly crosses $85,000 amid optimistic sentiment — All we know — Mint Markets, 2026-09-21. https://www.livemint.com/market/cryptocurrency/bitcoin-price-today-85000-cryptocurrency-market-optimistic-rally-clarity-fed-september-eight-month-record-high-since-jan-11789989588018.html
- Historical analogues: 2025-08-13 (d=1.76), 2025-05-08 (d=2.48), 2024-11-13 (d=3.14)

### [RED 8.49] cross-asset · 5 series ↑
- ust_2y [RATES]: last 4.67, z20 1.64, zc -1.13, resid-z -1.31 [quiet], 1d -1.48%, |z20|=1.64; 1y-pct=99
- tips_10y_real [RATES]: last 2.61, z20 1.56, zc -1.48, resid-z -1.82 [unexplained], 1d -2.61%, 1d move -7.0bps ≥ 5bps; |z20|=1.56; 1y-pct=99
- ust_10y [RATES]: last 4.94, z20 1.23, zc -1.46, resid-z -1.30 [quiet], 1d -1.40%, 1y-pct=98
- dyn_bond [EQUITIES]: last 88.98, z20 -0.99, zc 0.84, resid-z 1.01 [quiet], 1d 0.29%, 1y-pct=2
- ust_30y [RATES]: last 5.29, z20 0.45, zc -1.49, resid-z -1.16 [quiet], 1d -1.12%, 1y-pct=97
- **Mechanism**: cross-asset · 5 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: midcap_largecap_ratio (rho -0.445 via ust_2y, z 0.15, quiet)
- Watch next: wti (co-move) — not yet - watch; rho 0.577 vs ust_10y, historically leads by 3d
- Watch next: brent (co-move) — not yet - watch; rho 0.605 vs ust_10y
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.588 vs dyn_bond
- **India receivers**: midcap_largecap_ratio (rho -0.445, z 0.15)
- Source: Global Market: Euro area bond yields fall as oil prices ease — ET Markets, 2026-09-21. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-area-bond-yields-fall-as-oil-prices-ease/articleshow/134386398.cms
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-07 (d=0.32), 2026-03-30 (d=0.54)

### [RED 7.81] indices · 2 series ↑
- nasdaq_100 [INDICES]: last 30383.38, z20 4.97, zc 2.26, resid-z 0.22 [priced], 1d 2.49%, |z20|=4.97; 1y-pct=97
- sp500 [INDICES]: last 7750.34, z20 1.91, zc 1.68, resid-z -0.46 [priced], 1d 1.31%, |z20|=1.91; 1y-pct=98
- **Mechanism**: indices · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.93 vs nasdaq_100
- Watch next: brent (inverse) — not yet - watch; rho -0.657 vs sp500, historically leads by 2d
- Watch next: vix (inverse) — not yet - watch; rho -0.651 vs nasdaq_100, historically leads by 2d
- Watch next: wti (inverse) — not yet - watch; rho -0.535 vs nasdaq_100, historically leads by 2d
- Watch next: stoxx_50 (co-move) — not yet - watch; rho 0.578 vs nasdaq_100
- Source: Wall Street rises as AI stocks shine, oil drops; Dow, S&P, Nasdaq up — BusinessLine Mkts, 2026-09-21. https://www.thehindubusinessline.com/markets/wall-street-rises-as-ai-stocks-shine-oil-drops-dow-sp-nasdaq-up/article71492647.ece
- Source: Dow Jones| Nasdaq | US Stock Market Today | Live: Nasdaq, S&P 500 climb 1% as oil prices slide, Trump-Xi meeting nears — ET Markets, 2026-09-21. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-war-hormuz-deal-brent-crude-oil-fed-warsh-bitcoin-warner-bros-meta-marvell-accenture-chip-stock-price-news-21st-september-2026/liveblog/134389611.cms
- Source: US stock market today: S&P 500, Nasdaq futures rise up to 1% as oil falls; Trump-Xi summit in focus — Mint Markets, 2026-09-21. https://www.livemint.com/market/stock-market-news/us-stock-market-today-s-p-500-nasdaq-futures-rise-up-to-1-as-oil-falls-trump-xi-summit-in-focus-11789987134756.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-07 (d=0.06), 2026-05-15 (d=0.07)

### [AMBER 6.23] commodities · 2 series ↓
- brent [COMMODITIES]: last 95.16, z20 -0.40, zc -3.46, resid-z -2.35 [unexplained], 1d -8.39%, 1-session move -8.39% ≥ 1.5%
- wti [COMMODITIES]: last 91.33, z20 -0.24, zc -3.20, resid-z -2.53 [unexplained], 1d -8.94%, 1-session move -8.94% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: stoxx_50 (inverse) — not yet - watch; rho -0.61 vs brent, historically leads by 5d
- Watch next: dax (inverse) — not yet - watch; rho -0.567 vs brent, historically leads by 5d
- Watch next: cac_40 (inverse) — not yet - watch; rho -0.551 vs brent, historically leads by 5d
- Watch next: dyn_bond (inverse) — not yet - watch; rho -0.648 vs brent
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.616 vs brent
- Source: Rupee gains for third day as crude eases, but volatility persists — ET Markets, 2026-09-21. https://economictimes.indiatimes.com/markets/forex/forex-news/rupee-gains-for-third-day-as-crude-eases-but-volatility-persists/articleshow/134393258.cms
- Source: Wall Street rises as AI stocks shine, oil drops; Dow, S&P, Nasdaq up — BusinessLine Mkts, 2026-09-21. https://www.thehindubusinessline.com/markets/wall-street-rises-as-ai-stocks-shine-oil-drops-dow-sp-nasdaq-up/article71492647.ece
- Source: Hungary Asks U.S. to Waive Tariffs Over Russian Oil Purchases — OilPrice, 2026-09-21. https://oilprice.com/Latest-Energy-News/World-News/Hungary-Asks-US-to-Waive-Tariffs-Over-Russian-Oil-Purchases.html
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-31 (d=0.05), 2025-04-29 (d=0.06)

### [RED 5.36] gold_silver_ratio ↓
- gold_silver_ratio [DERIVED]: last 65.73, z20 -2.36, zc n/a, resid-z n/a [quiet], 1d -1.14%, GSR<75 (extreme low); |z20|=2.36
- **Mechanism**: gold_silver_ratio ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho -0.373 via gold_silver_ratio, z -0.88, quiet)
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.86 vs gold_silver_ratio
- **India receivers**: nifty_midcap_100 (rho -0.373, z -0.88)
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-12 (d=0.01), 2025-10-29 (d=0.08)

### [RED 5.19] dxy ↑
- dxy [FX]: last 100.37, z20 2.19, zc 0.45, resid-z 0.52 [quiet], 1d 0.15%, 20d range extreme; |z20|=2.19
- **Mechanism**: dxy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Historical analogues: 2026-05-22 (d=0.0), 2024-10-23 (d=0.02), 2024-11-21 (d=0.02)

### [AMBER 5.1] fx · 2 series ↓
- eur_usd [FX]: last 1.15, z20 -2.26, zc -0.04, resid-z 0.46 [quiet], 1d -0.01%, |z20|=2.26
- gbp_usd [FX]: last 1.34, z20 -2.16, zc 0.29, resid-z 0.47 [quiet], 1d 0.12%, |z20|=2.16
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_icicigi_bo (rho -0.403 via gbp_usd, z -0.4, quiet)
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.554 vs eur_usd, historically leads by 3d
- **India receivers**: dyn_icicigi_bo (rho -0.403, z -0.4)
- Source: Global Market: Euro area bond yields fall as oil prices ease — ET Markets, 2026-09-21. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-euro-area-bond-yields-fall-as-oil-prices-ease/articleshow/134386398.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [RED 4.87] dyn_4417_t ↑
- dyn_4417_t [EQUITIES]: last 5760.00, z20 2.87, zc 0.85, resid-z 0.48 [quiet], 1d 3.04%, |z20|=2.87; 1y-pct=100
- **Mechanism**: dyn_4417_t ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Knowledge Marine shares jump 5% then drop 2% despite this work order update - What next? Tech experts decode — Mint Markets, 2026-09-21. https://www.livemint.com/market/stock-market-news/knowledge-marine-shares-jump-5-then-drop-2-despite-this-work-order-update-what-next-tech-experts-decode-11789968774263.html
- Source: NSE IPO: Will there be a negative listing? But, should you still apply — if yes, then why | What experts suggest — Mint Markets, 2026-09-21. https://www.livemint.com/market/ipo/nse-ipo-will-there-be-a-negative-listing-but-should-you-still-apply-if-yes-then-why-what-experts-suggest-11789965511769.html
- Source: Xi Jinping US visit: Trump to weigh on rare-earth magnet | Experts bet high on Vedanta, GMDC, Ather Energy, other stocks — Mint Markets, 2026-09-21. https://www.livemint.com/market/stock-market-news/xi-jinping-us-visit-trump-to-weigh-on-rare-earth-magnet-experts-bet-high-on-vedanta-gmdc-ather-energy-other-stocks-11789959864197.html
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-26 (d=0.02), 2025-09-09 (d=0.26)

## Watchlist (below surfacing floor)
usd_cny ↓ (4.69), dyn_meta ↑ (4.6), dyn_tatatech_ns ↓ (4.27), sofr ↑ (4.12), comex_copper ↑ (3.77), dyn_tech ↑ (3.77), commodities · 3 series ↑ (3.59), ig_oas ↓ (3.27), midcap_largecap_ratio ↑ (3.15), dyn_jiofin_bo ↓ (2.96), dyn_lenskart_ns ↑ (2.51), dyn_icicigi_bo ↓ (2.4)

## India macro
- nifty_50: 23429.0000 (1d 0.35%, z20 -0.94, flag none)
- nifty_midcap_100: 62047.9492 (1d -0.23%, z20 -0.88, flag none)
- usd_inr: 95.8050 (1d 0.01%, z20 0.97, flag none)
- goi_10y: 6.7800 (1d -1.60%, z20 0.56, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.3000 (1d -4.96%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.6483 (1d -0.58%, z20 0.15, flag amber)
- Next India prints: NSDL FPI flows T-0d · IMD weekly rainfall T-0d · RBI Weekly Statistical Supplement T-4d · Kharif sowing data T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 55.6 — "India becomes Asia’s 4th-largest REIT market, overtakes Hong Kong: Cushman & Wakefield"
- INOXINDIA.NS (INOX INDIA LIMITED) score 53.7 — "India becomes Asia’s 4th-largest REIT market, overtakes Hong Kong: Cushman & Wakefield"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 52.6 — "India becomes Asia’s 4th-largest REIT market, overtakes Hong Kong: Cushman & Wakefield"
- INDIANB.NS (INDIAN BANK) score 48.1 — "Eurosystem brings central bank money to tokenised finance"
- COIN (Coinbase Global, Inc.) score 45.7 — "Global Market: Euro area bond yields fall as oil prices ease"
- BAC (Bank of America Corporation) score 44.7 — "U.S., DENMARK AND GREENLAND REACH SECURITY DEAL The U.S., Denmark and Greenland have agree"
- HDB (HDFC Bank Limited) score 41.6 — "Eurosystem brings central bank money to tokenised finance"
- IDBI.NS (IDBI BANK LIMITED) score 37.1 — "Eurosystem brings central bank money to tokenised finance"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 37.1 — "Eurosystem brings central bank money to tokenised finance"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 37.1 — "Eurosystem brings central bank money to tokenised finance"
- OHI (Omega Healthcare Investors, In) score 36.2 — "Emami share price jumps 4% ahead of buyback: What should investors do? Check stop loss, ta"
- CHKP (Check Point Software Technolog) score 33.3 — "Emami share price jumps 4% ahead of buyback: What should investors do? Check stop loss, ta"
- BOND (PIMCO Active Bond Exchange-Tra) score 26.7 — "Global Market: Euro area bond yields fall as oil prices ease"
- LTH (Life Time Group Holdings, Inc.) score 26.0 — "Bitcoin trades above $84,000 after regulatory developments boost market sentiment"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 23.7 — "Tata Group stocks face fresh risk as Trusts-Sons row escalates: Which stock looks most att"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 23.7 — "Tata Group stocks face fresh risk as Trusts-Sons row escalates: Which stock looks most att"
- SEPN (Septerna, Inc.) score 21.5 — "Stock Market prediction tomorrow: Sensex, Nifty outlook for Tue | Kospi, Taiwan Index, Nik"
- TECHM.NS (TECH MAHINDRA LIMITED) score 20.9 — "Concord Biotech bonus issue sparks rally! Pharma stock jumps 6% on maiden share reward - T"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 20.9 — "Concord Biotech bonus issue sparks rally! Pharma stock jumps 6% on maiden share reward - T"
- TECH (Bio-Techne Corp) score 20.9 — "Concord Biotech bonus issue sparks rally! Pharma stock jumps 6% on maiden share reward - T"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 18.4 — "Rising Energy Costs Threaten UK Growth Despite 1.3% Expansion"
- 301077.SZ (CHINASTARS) score 17.4 — "U.S.-CHINA TALKS SET AHEAD OF TRUMP-XI SUMMIT Treasury Secretary Scott Bessent will meet C"
- BZ=F (Brent Crude Oil Last Day Finan) score 10.1 — "Latest GMP compared: NSE IPO vs Sonaselection India IPO - Last day to apply today | Share "
- STYLEBAAZA.NS (BAAZAR STYLE RETAIL LTD) score 9.9 — "SS Retail IPO allotment likely today: GMP signals 35% listing gain; here's how to check st"
- JIOFIN.BO (Jio Financial Services Limited) score 9.3 — "Apollo Hospital Share Price Live Updates: Apollo Hospital's Financial Snapshot"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 8.9 — "Xi Jinping US visit: Trump to weigh on rare-earth magnet | Experts bet high on Vedanta, GM"
- JUSTDIAL.BO (JUST DIAL LTD.) score 7.4 — "U.S.-CHINA TALKS SET AHEAD OF TRUMP-XI SUMMIT Treasury Secretary Scott Bessent will meet C"
- VT (Vanguard Total World Stock Ind) score 6.3 — "UN Warns World Must Prepare for Life Beyond 1.5°C"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 5.6 — "Why Adani Total Gas lost 5%, Adani Ports fell 2% despite gains on Sensex, Nifty | Check ho"
- MS (Morgan Stanley) score 5.6 — "JP MORGAN EXPECTS ECB TO DELIVER ANOTHER 25 BP INTEREST RATE HIKE IN MARCH 2027 AFTER A DE"
- META (Meta) score 5.2 — "Meta’s stock is enjoying its best month in more than two years thanks to the company’s hot"
- NVDA (NVIDIA Corporation) score 4.6 — "NVDA - NVIDIA’S HUANG REJECTS CALLS TO SLOW AI Nvidia CEO Jensen Huang says AI development"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 4.4 — "Eurosystem brings central bank money to tokenised finance"
- PINELABS.NS (PINE LABS LIMITED) score 4.0 — "Pine Labs share price target: MOFSL sees 72% upside in bull case - know bear case | Ration"
- GS (Goldman Sachs Group, Inc. (The) score 3.6 — "Consumer sentiment is in the dumps despite a solid economy. Goldman Sachs blames 'lower ha"
- LENSKART.NS (LENSKART SOLUTIONS LTD) score 3.2 — "Lenskart Solutions share price drops 3% due to a likely  ₹2,047 crore block deal | Details"
- ICICIGI.BO (ICICI Lombard General Insuranc) score 2.8 — "ICICI Bank Share Price Live Updates: ICICI Bank's Current Market Position"
- VOLTAS.NS (VOLTAS LTD) score 0.4 — "Voltas among 7 stocks hitting 52-week low; slipped up to 10% in a month"
- DELL (Dell Technologies Inc.) score 0.2 — "Why Dell and HPE were the S&P 500’s top-performing stocks today"
- DKS (Dick's Sporting Goods Inc) score 0.0 — "Dick’s Sporting Goods slumps after earnings miss: What’s next?"

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