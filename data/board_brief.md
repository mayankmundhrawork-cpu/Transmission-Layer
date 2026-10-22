# Transmission Layer — board brief · 2026-10-22 20:03Z

data as of **2026-10-22** · 97 series · 23 red / 35 amber · 8 events surfaced (41 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.816, 14d in regime; vol-pct 0.808, breadth-off 0.824, Markov P(high-vol) 0.053)
- [INVERTED] **safe_haven_gold** — corr20 -0.45, corr60 -0.42, contra nifty_50 corr20=0.4, last shift 2026-06-03. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.84, last shift 2026-02-03. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.24, corr60 0.21, last shift 2026-08-27. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.01, corr60 0.11, last shift 2026-09-02. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.78, last shift 2026-05-04. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.06, corr60 -0.02, last shift 2026-01-21. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.27, corr60 -0.24, last shift 2026-08-07. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.54, corr60 0.26, last shift 2026-07-23. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **2 of 89** scanned series survive multiplicity control (effective p ≤ 0.0005605865536324472)
- **SETUP** dyn_vt → aud_usd: leads 1d (ccf 0.557, β 0.3431, p 0.0); driver zc -1.7 → expected -0.446%. Type hit-rate 0.823 (n=1848).
- **SETUP** dyn_vt → usd_brl: leads 1d (ccf -0.512, β -0.4068, p 0.0); driver zc -1.7 → expected 0.528%. Type hit-rate 0.823 (n=1848).
- **SETUP** vix → asx_200: leads 1d (ccf -0.496, β -0.0448, p 0.0); driver zc 2.28 → expected -0.846%. Type hit-rate 0.823 (n=1848).
- **SETUP** sp500 → aud_usd: leads 1d (ccf 0.465, β 0.2774, p 0.0); driver zc -1.6 → expected -0.335%. Type hit-rate 0.823 (n=1848).
- **SETUP** nasdaq_100 → aud_usd: leads 1d (ccf 0.441, β 0.1926, p 0.0); driver zc -2.26 → expected -0.555%. Type hit-rate 0.823 (n=1848).
- **SETUP** vix → aud_usd: leads 1d (ccf -0.432, β -0.0295, p 0.0); driver zc 2.28 → expected -0.557%. Type hit-rate 0.823 (n=1848).
- **SETUP** vix → usd_brl: leads 1d (ccf 0.426, β 0.0377, p 0.0); driver zc 2.28 → expected 0.712%. Type hit-rate 0.823 (n=1848).
- **SETUP** nasdaq_100 → usd_brl: leads 1d (ccf -0.421, β -0.2375, p 0.0); driver zc -2.26 → expected 0.685%. Type hit-rate 0.823 (n=1848).
- **SETUP** dyn_vt → india_vix: leads 1d (ccf -0.368, β -2.4319, p 0.00818); driver zc -1.7 → expected 3.159%. Type hit-rate 0.823 (n=1848).
- **SETUP** dyn_nvda → aud_usd: leads 1d (ccf 0.345, β 0.0771, p 0.0); driver zc -1.99 → expected -0.336%. Type hit-rate 0.823 (n=1848).
- **SETUP** vix → india_vix: leads 1d (ccf 0.343, β 0.2279, p 0.01301); driver zc 2.28 → expected 4.303%. Type hit-rate 0.823 (n=1848).
- **SETUP** sp500 → india_vix: leads 1d (ccf -0.335, β -2.1617, p 0.01751); driver zc -1.6 → expected 2.612%. Type hit-rate 0.823 (n=1848).
- **SETUP** dyn_vt → gbp_usd: leads 1d (ccf 0.329, β 0.145, p 1e-05); driver zc -1.7 → expected -0.188%. Type hit-rate 0.823 (n=1848).
- **SETUP** btc_usd → aud_usd: leads 1d (ccf 0.287, β 0.063, p 0.0); driver zc -1.67 → expected -0.199%. Type hit-rate 0.823 (n=1848).
- **SETUP** dyn_bond → eur_usd: leads 1d (ccf 0.256, β 0.3599, p 3e-05); driver zc 2.89 → expected 0.355%. Type hit-rate 0.823 (n=1848).
- Track record · residual_reversion: hit-rate **0.494** (n=1119) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.823** (n=1848) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.625** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 9.6] cross-asset · 4 series ↓
- vix [INDICES]: last 19.83, z20 2.93, zc 2.28, resid-z n/a [moved], 1d 18.88%, 1-session move +18.88% ≥ 15.0%; |z20|=2.93
- nasdaq_100 [INDICES]: last 28962.86, z20 -2.55, zc -2.26, resid-z -0.79 [priced], 1d -2.88%, |z20|=2.55
- dyn_vt [EQUITIES]: last 156.53, z20 -2.17, zc -1.70, resid-z 0.37 [priced], 1d -1.30%, |z20|=2.17
- dyn_nvda [EQUITIES]: last 212.28, z20 -2.03, zc -1.99, resid-z -0.62 [priced], 1d -4.36%, |z20|=2.03
- **Mechanism**: cross-asset · 4 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-04 (z-distance 0.21).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: russell_2000 (inverse) — not yet - watch; rho -0.665 vs vix, historically leads by 1d
- Watch next: dax (co-move) — not yet - watch; rho 0.617 vs dyn_vt
- Watch next: dyn_gs (inverse) — not yet - watch; rho -0.592 vs vix
- Source: US stocks today: US stocks slide as AI spending jitters hit Nasdaq, oil prices rebound — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/us-stocks-today-us-stocks-open-lower-as-ai-jitters-return-oil-rises/articleshow/135120582.cms
- Source: U.S. STOCKS EXTEND FALL, NASDAQ DOWN 1.55% — DeItaone, 2026-10-22. https://t.me/walter_bloomberg/37431
- Source: Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: Nasdaq crashes 2% as AI, oil risks drive flight to bonds — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/dow-jones-stock-market-live-updates-nasdaq-sp-500-us-iran-israel-war-hormuz-deal-brent-crude-oil-earnings-forecast-ai-stocks-nvidia-tesla-meta-stock-price-news-22nd-october-2026/liveblog/135118971.cms
- Historical analogues: 2026-05-04 (d=0.21), 2025-04-28 (d=0.28), 2025-08-28 (d=0.3)

### [RED 8.63] commodities · 2 series ↑
- brent [COMMODITIES]: last 113.07, z20 2.80, zc 2.13, resid-z -0.30 [priced], 1d 3.91%, 1-session move +3.91% ≥ 1.5%; |z20|=2.80; 1y-pct=98
- wti [COMMODITIES]: last 99.29, z20 1.24, zc 0.78, resid-z -0.78 [quiet], 1d 2.20%, 1-session move +2.20% ≥ 1.5%
- **Mechanism**: commodities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: ust_10y (co-move) — not yet - watch; rho 0.546 vs brent, historically leads by 5d
- Watch next: ust_30y (co-move) — not yet - watch; rho 0.518 vs brent
- Source: Strathcona Pitches 250,000-Bpd Oil Export Route to Asia — OilPrice, 2026-10-22. https://oilprice.com/Energy/Crude-Oil/Strathcona-Pitches-250000-Bpd-Oil-Export-Route-to-Asia.html
- Source: Yen jumps as oil, AI and France worries rattle markets — Mint Markets, 2026-10-22. https://www.livemint.com/market/yen-jumps-as-oil-ai-and-france-worries-rattle-markets-11792694662480.html
- Source: EU’s Proposed Shipping Subsidies Could Make BioLNG Cheaper Than Fuel Oil — OilPrice, 2026-10-22. https://oilprice.com/Energy/Energy-General/EUs-Proposed-Shipping-Subsidies-Could-Make-BioLNG-Cheaper-Than-Fuel-Oil.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 8.17] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4043.00, z20 -2.89, zc -2.57, resid-z -1.25 [moved], 1d -2.58%, |z20|=2.89; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 54.70, z20 -2.28, zc -2.11, resid-z -0.59 [priced], 1d -4.74%, |z20|=2.28; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 73.91, z20 1.85, zc n/a, resid-z n/a [quiet], 1d 2.27%, GSR<75 (extreme low); |z20|=1.85
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dxy (inverse) — not yet - watch; rho -0.504 vs comex_gold
- Source: Silver crashes  ₹8,590/kg to a 7-month low; gold hits 2-month low. What’s driving the selloff in precious metals — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/silver-crashes-rs-8-590-per-kilo-to-7-month-low-gold-hits-2-month-low-what-s-driving-the-selloff-in-precious-metals-11792676479559.html
- Source: BSE, MMTC-PAMP partner to boost India’s electronic gold receipts market — BusinessLine Mkts, 2026-10-22. https://www.thehindubusinessline.com/markets/bse-mmtc-pamp-partner-to-boost-indias-electronic-gold-receipts-market/article71611647.ece
- Source: GOLD FALLS 1.3% AS RISING OIL PRICES COMPLICATE FED RATE OUTLOOK Gold slipped 1.3% to $4,083, pressured by concerns that higher oil prices could fuel inflation and delay Federal Reserve rate cuts. Capital. com's Monte Safieddine warns that gold faces a "difficult cocktail" of sticky inflation, eleva — DeItaone, 2026-10-22. https://t.me/walter_bloomberg/37427
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 6.12] dyn_chkp ↑
- dyn_chkp [EQUITIES]: last 152.00, z20 4.12, zc 2.64, resid-z 0.47 [moved], 1d 5.98%, |z20|=4.12
- **Mechanism**: dyn_chkp ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_indusindbk_bo (rho 0.407 via dyn_chkp, z -1.32, reacted)
- **India receivers**: dyn_indusindbk_bo (rho 0.407, z -1.32)
- Source: Reliance Jio IPO subscription status day 1, day 2: Check QIB, NII, Retail, Employee, RIL Shareholders wise data details — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/reliance-jio-ipo-subscription-status-day-1-day-2-check-qib-nii-retail-employee-ril-shareholders-wise-data-details-11792681049708.html
- Source: Coal India Q2 results 2026 date, dividend announcement news: Check Maharatna PSU's earnings schedule, preview, yield — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/coal-india-q2-results-2026-date-dividend-announcement-news-check-maharatna-psus-earnings-schedule-preview-yield-11792676595483.html
- Source: 163% return in 3 years! This AMC declares  ₹9.50 dividend despite 6% profit dip- Do you own? Check record date — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/163-return-in-3-years-this-amc-declares-rs-9-50-dividend-despite-6-profit-dip-do-you-own-check-record-date-11792672553645.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-07 (d=0.01), 2025-05-20 (d=0.04)

### [RED 6.11] dyn_lth ↑
- dyn_lth [EQUITIES]: last 41.99, z20 4.11, zc 1.37, resid-z 0.66 [quiet], 1d 3.02%, |z20|=4.11
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: FRENCH 5-YEAR CDS RISE ABOVE 100 BPS, FIRST TIME SINCE OCTOBER 2012, LAST AT 97.75 BPS, LSEG DATA SHOWS — DeItaone, 2026-10-22. https://t.me/walter_bloomberg/37440
- Source: META - META PLATFORM'S 5-YEAR CREDIT DEFAULT SWAPS HITS ALL-TIME HIGH, LAST AT 114.5 BPS - MARKIT DATA — DeItaone, 2026-10-22. https://t.me/walter_bloomberg/37429
- Source: Trump's approval rating on economy hits all-time low as midterm looms: CNBC survey — CNBC Economy, 2026-10-22. https://www.cnbc.com/2026/10/22/trump-economic-approval-rating-midterms-poll.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-17 (d=0.02), 2025-12-31 (d=0.02)

### [RED 5.97] dyn_meta ↓
- dyn_meta [EQUITIES]: last 648.91, z20 -3.97, zc -2.87, resid-z -0.40 [moved], 1d -6.97%, |z20|=3.97
- **Mechanism**: dyn_meta ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Meta share price: Stock slumps 7.5% despite upbeat Q3 results; why is Facebook parent falling? — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/meta-share-price-stock-slumps-7-5-despite-upbeat-q3-results-why-is-facebook-parent-falling-11792689825393.html
- Source: Zuckerberg’s California tax move is a win for Meta — and for him — MarketWatch Top, 2026-10-22. https://www.marketwatch.com/story/zuckerbergs-california-tax-move-is-a-win-for-meta-and-for-him-aa049c94?mod=mw_rss_topstories
- Source: META - META PLATFORM'S 5-YEAR CREDIT DEFAULT SWAPS HITS ALL-TIME HIGH, LAST AT 114.5 BPS - MARKIT DATA — DeItaone, 2026-10-22. https://t.me/walter_bloomberg/37429
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2025-10-09 (d=0.12)

### [AMBER 5.33] indices · 3 series ↓
- taiwan_weighted [INDICES]: last 46099.28, z20 -2.01, zc -1.18, resid-z 0.20 [quiet], 1d -1.68%, |z20|=2.01
- nikkei_225 [INDICES]: last 63139.59, z20 -1.87, zc -1.34, resid-z -0.65 [quiet], 1d -2.29%, |z20|=1.87
- kospi [INDICES]: last 5531.37, z20 -1.70, zc -1.01, resid-z -0.29 [quiet], 1d -3.56%, |z20|=1.70
- **Mechanism**: indices · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). 
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_cartrade_ns (rho 0.455 via kospi, z -1.25, reacted); dyn_idbi_ns (rho 0.403 via nikkei_225, z -2.03, reacted); midcap_largecap_ratio (rho 0.362 via kospi, z -2.85, reacted)
- **India receivers**: dyn_cartrade_ns (rho 0.455, z -1.25); dyn_idbi_ns (rho 0.403, z -2.03); midcap_largecap_ratio (rho 0.362, z -2.85)
- Source: Global Market: Japan’s Nikkei falls as chip stocks retreat on AI spending concerns — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-japans-nikkei-falls-as-chip-stocks-retreat-on-ai-spending-concerns/articleshow/135106795.cms
- Source: Japan’s Nikkei jumps over 1% as AI optimism lifts chip stocks; exports rise 16.7% — ET Markets, 2026-10-21. https://economictimes.indiatimes.com/markets/us-stocks/news/japans-nikkei-jumps-over-1-as-ai-optimism-lifts-chip-stocks-exports-rise-16-7/articleshow/135081946.cms

### [AMBER 5.33] cross-asset · 2 series ↑
- dyn_techm_ns [EQUITIES]: last 1829.10, z20 2.49, zc -0.11, resid-z -0.79 [quiet], 1d -0.31%, |z20|=2.49; 1y-pct=99
- nifty_it [INDICES]: last 32081.25, z20 2.08, zc -0.66, resid-z -0.94 [quiet], 1d -1.05%, |z20|=2.08
- **Mechanism**: cross-asset · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-12-30 (z-distance 0.52).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_tataelxsi_ns (rho 0.76 via nifty_it, z 1.93, reacted); nifty_50 (rho 0.515 via nifty_it, z -0.32, quiet); dyn_justdial_bo (rho 0.511 via nifty_it, z 2.85, reacted); midcap_largecap_ratio (rho -0.434 via dyn_techm_ns, z -2.85, reacted); dyn_tatatech_ns (rho 0.404 via nifty_it, z -1.28, reacted)
- Watch next: nifty_50 (co-move) — not yet - watch; rho 0.515 vs nifty_it
- **India receivers**: dyn_tataelxsi_ns (rho 0.76, z 1.93); nifty_50 (rho 0.515, z -0.32); dyn_justdial_bo (rho 0.511, z 2.85); midcap_largecap_ratio (rho -0.434, z -2.85)
- Source: IT stocks rebound sharply in October: TCS gains 22%, Wipro and Tech Mahindra gain 20% — 3 key reasons behind the jump — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/it-stocks-rebound-sharply-in-october-tcs-gains-22-wipro-and-tech-mahindra-gain-20-3-key-reasons-behind-the-jump-11792671461699.html
- Source: Mahindra Lifespace Q2 profit down 66 pc to Rs 16 cr — ET Markets, 2026-10-22. https://economictimes.indiatimes.com/markets/stocks/earnings/mahindra-lifespace-q2-profit-down-66-pc-to-rs-16-cr/articleshow/135118930.cms
- Source: SML Isuzu shares: SML Mahindra shares tank for 3rd session in row after 33% gain in 6 months | Buy, sell or hold? — Mint Markets, 2026-10-22. https://www.livemint.com/market/stock-market-news/sml-isuzu-shares-sml-mahindra-shares-tank-for-3rd-session-in-row-after-33-gain-in-6-months-buy-sell-or-hold-11792645465680.html
- Historical analogues: 2025-12-30 (d=0.52), 2025-08-13 (d=0.76), 2026-01-06 (d=0.77)

## Watchlist (below surfacing floor)
dyn_bond ↑ (5.14), usd_jpy ↓ (5.03), indices · 2 series ↓ (4.91), dyn_wit ↑ (4.77), comex_copper ↓ (4.67), natgas ↓ (4.55), dow_jones ↑ (4.52), dyn_sepn ↑ (4.34), dyn_4417_t ↑ (4.31), dyn_coalindia_ns ↓ (4.21), dyn_301077_sz ↓ (3.9), hang_seng ↓ (3.81)

## India macro
- nifty_50: 22687.6504 (1d -0.54%, z20 -0.32, flag amber)
- nifty_midcap_100: 57062.1484 (1d -0.88%, z20 -2.08, flag amber)
- usd_inr: 94.8080 (1d 0.10%, z20 -1.53, flag amber)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.5151 (1d -0.34%, z20 -2.85, flag red)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-1d · Kharif sowing data T-1d · IMD weekly rainfall T-4d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 95.6 — "Indian Food Ministry asks States to ensure no sugar is diverted for ethanol"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 94.0 — "Indian Food Ministry asks States to ensure no sugar is diverted for ethanol"
- INOXINDIA.NS (INOX INDIA LIMITED) score 93.1 — "Indian Food Ministry asks States to ensure no sugar is diverted for ethanol"
- INDIANB.NS (INDIAN BANK) score 81.9 — "MAJOR U.S. BANKS DETECT UNAUTHORIZED AI AGENTS ACCESSING CUSTOMER ACCOUNTS — AXIOS Major b"
- BAC (Bank of America Corporation) score 70.8 — "Analysis: Why a $2 trillion deficit and 5% Treasury yields are becoming America's biggest "
- HDB (HDFC Bank Limited) score 63.2 — "MAJOR U.S. BANKS DETECT UNAUTHORIZED AI AGENTS ACCESSING CUSTOMER ACCOUNTS — AXIOS Major b"
- IDBI.NS (IDBI BANK LIMITED) score 61.3 — "MAJOR U.S. BANKS DETECT UNAUTHORIZED AI AGENTS ACCESSING CUSTOMER ACCOUNTS — AXIOS Major b"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 61.3 — "MAJOR U.S. BANKS DETECT UNAUTHORIZED AI AGENTS ACCESSING CUSTOMER ACCOUNTS — AXIOS Major b"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 61.3 — "MAJOR U.S. BANKS DETECT UNAUTHORIZED AI AGENTS ACCESSING CUSTOMER ACCOUNTS — AXIOS Major b"
- OHI (Omega Healthcare Investors, In) score 57.3 — "Investors’ recent money moves show a preference for lowering risks over boosting rewards"
- COIN (Coinbase Global, Inc.) score 55.1 — "EBAY SHARES UP 1.6% PREMARKET AFTER CO SAYS WILL REDUCE GLOBAL WORKFORCE BY ABOUT 9%"
- TECHM.NS (TECH MAHINDRA LIMITED) score 51.7 — "GOLDMAN SACHS: AI COULD TEMPORARILY DISPLACE 9% OF WORKERS Goldman Sachs estimates that a "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 47.9 — "GOLDMAN SACHS: AI COULD TEMPORARILY DISPLACE 9% OF WORKERS Goldman Sachs estimates that a "
- TECH (Bio-Techne Corp) score 47.9 — "GOLDMAN SACHS: AI COULD TEMPORARILY DISPLACE 9% OF WORKERS Goldman Sachs estimates that a "
- TGT (Target Corporation) score 47.9 — "BOFA RAISES SPACEX ($SPCX) PRICE TARGET TO $275 FROM $235 BofA Securities analyst Ronald E"
- CHKP (Check Point Software Technolog) score 45.6 — "Ola Electric rights issue opens today: Who are the investors applying for 2.39 crore entit"
- BOND (PIMCO Active Bond Exchange-Tra) score 36.5 — "Dow Jones| Nasdaq | S&P 500 | US Stock Market Today |Live Updates: Nasdaq crashes 3% as AI"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 32.1 — "Q2 Results Today Highlights: Q2 Results Live: Adani Energy PAT surges 145%, CPCL profit tr"
- RS (Reliance, Inc.) score 29.9 — "Reliance Industries shares: Monarch sees 20% upside in 3–4 months - Reveals buy range, tar"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 28.4 — "Shoppers Stop shares deliver almost no returns in 10 years; Experts decode the road ahead "
- LTH (Life Time Group Holdings, Inc.) score 26.1 — "META - META PLATFORM'S 5-YEAR CREDIT DEFAULT SWAPS HITS ALL-TIME HIGH, LAST AT 114.5 BPS -"
- 301077.SZ (CHINASTARS) score 24.1 — "EARTHQUAKE OF MAGNITUDE AROUND 6.7 STRIKES CHINA'S TIBET - XINHUA"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 19.9 — "Market wrap: Bajaj Finance, Cipla, Nestle India, Eternal top gainers and losers on Nifty a"
- META (Meta) score 18.4 — "META - META PLATFORM'S 5-YEAR CREDIT DEFAULT SWAPS HITS ALL-TIME HIGH, LAST AT 114.5 BPS -"
- JIOFIN.BO (Jio Financial Services Limited) score 18.1 — "Young Americans are giving up their cars. It’s a path to financial freedom, for some."
- BZ=F (Brent Crude Oil Last Day Finan) score 17.0 — "META - META PLATFORM'S 5-YEAR CREDIT DEFAULT SWAPS HITS ALL-TIME HIGH, LAST AT 114.5 BPS -"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 16.9 — "Market wrap: Bajaj Finance, Cipla, Nestle India, Eternal top gainers and losers on Nifty a"
- JUSTDIAL.BO (JUST DIAL LTD.) score 15.3 — "Lumpy Jio IPO inflows push rupee into ‘overbought’ zone just as oil renews rise"
- SEPN (Septerna, Inc.) score 14.9 — "FIVE-YEAR U.S. TREASURY YIELD FALLS TO 4.825% LOWEST SINCE SEPT 23, LAST DOWN 14.33 BASIS "
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 14.5 — "Q2 Results Today Highlights: Q2 Results Live: Adani Energy PAT surges 145%, CPCL profit tr"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 12.0 — "Tata Teleservices narrows Q2 loss to ₹59 crore, revenue up 8%; stock surges 9% on results "
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 12.0 — "Tata Teleservices narrows Q2 loss to ₹59 crore, revenue up 8%; stock surges 9% on results "
- JEF (Jefferies Financial Group Inc.) score 10.5 — "KEI Industries shares: Down 15% in one month! Jefferies India sees 45% upside after Q2 res"
- GS (Goldman Sachs Group, Inc. (The) score 10.1 — "GOLDMAN SACHS: AI COULD TEMPORARILY DISPLACE 9% OF WORKERS Goldman Sachs estimates that a "
- VT (Vanguard Total World Stock Ind) score 6.3 — "CHINESE PREMIER SAYS CHINA, RUSSIA SERVE AS "VALUABLE FORCE FOR STABILITY IN TURBULENT WOR"
- WIT (Wipro Limited) score 6.0 — "IT stocks rebound sharply in October: TCS gains 22%, Wipro and Tech Mahindra gain 20% — 3 "
- NVDA (NVIDIA Corporation) score 5.9 — "NVIDIA MAY ALSO BE A BIDDER FOR AMBARELLA ( $AMBA ) - BETAVILLE"
- ETERNAL.NS (ETERNAL LIMITED) score 5.7 — "Market wrap: Bajaj Finance, Cipla, Nestle India, Eternal top gainers and losers on Nifty a"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.5 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
- VOLTAS.NS (VOLTAS LTD) score 0.0 — "Voltas’s market share is growing. Will margins follow?"

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