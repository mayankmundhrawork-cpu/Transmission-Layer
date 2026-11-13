# Transmission Layer — board brief · 2026-11-13 02:00Z

data as of **2026-11-13** · 97 series · 12 red / 28 amber · 8 events surfaced (20 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.833, 3d in regime; vol-pct None, breadth-off 0.833, Markov P(high-vol) 0.074)
- [INVERTED] **safe_haven_gold** — corr20 -0.11, corr60 -0.21, contra nifty_50 corr20=0.29, last shift 2026-06-04. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.9, corr60 0.84, last shift 2026-02-04. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.11, corr60 0.12, last shift 2026-09-16. Channel: global copper leads Indian metal equities
- [INVERTED] **inr_oil_channel** — corr20 -0.35, corr60 0.04, last shift 2026-09-03. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.91, last shift 2026-09-25. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.23, corr60 -0.01, last shift 2026-01-22. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.08, corr60 -0.17, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.36, corr60 0.32, last shift 2026-07-16. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **0 of 89** scanned series survive multiplicity control (effective p ≤ None)
- **SETUP** ust_2y → usd_jpy: leads 1d (ccf 0.477, β 0.2051, p 0.0); driver zc 2.86 → expected 0.765%. Type hit-rate 0.818 (n=2091).
- **SETUP** ust_10y → usd_jpy: leads 1d (ccf 0.447, β 0.2336, p 0.0); driver zc 1.9 → expected 0.479%. Type hit-rate 0.818 (n=2091).
- **SETUP** dyn_bond → usd_jpy: leads 1d (ccf -0.396, β -0.6982, p 0.0); driver zc -2.04 → expected 0.533%. Type hit-rate 0.818 (n=2091).
- Track record · residual_reversion: hit-rate **0.508** (n=1146) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=2091) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 6.83] cross-asset · 6 series ↑
- dyn_indusindbk_bo [EQUITIES]: last 930.00, z20 2.68, zc 0.94, resid-z 1.76 [unexplained], 1d 2.99%, |z20|=2.68
- dyn_bajfinance_ns [EQUITIES]: last 1115.00, z20 2.55, zc 1.59, resid-z 1.38 [moved], 1d 3.36%, |z20|=2.55; 1y-pct=98
- nifty_midcap_100 [INDICES]: last 62037.10, z20 2.22, zc 0.72, resid-z 1.18 [quiet], 1d 0.85%, |z20|=2.22
- nifty_50 [INDICES]: last 25299.35, z20 2.19, zc 0.14, resid-z 0.03 [quiet], 1d 0.18%, |z20|=2.19
- dyn_muthootfin_ns [EQUITIES]: last 2932.90, z20 2.02, zc 0.36, resid-z 0.59 [quiet], 1d 1.13%, |z20|=2.02
- nifty_metal [INDICES]: last 12771.65, z20 1.89, zc -0.08, resid-z -0.25 [quiet], 1d -0.11%, |z20|=1.89
- **Mechanism**: cross-asset · 6 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-18 (z-distance 1.27).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_jiofin_bo (rho 0.823 via nifty_midcap_100, z 1.79, reacted); dyn_adanient_bo (rho 0.747 via nifty_metal, z 1.24, reacted); nifty_fmcg (rho 0.644 via nifty_midcap_100, z 1.56, reacted); dyn_indianb_ns (rho 0.619 via nifty_midcap_100, z 2.82, reacted); dyn_policybzr_ns (rho 0.548 via dyn_bajfinance_ns, z 1.02, reacted)
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.518 vs nifty_50, historically leads by 5d
- Watch next: india_vix (inverse) — not yet - watch; rho -0.517 vs dyn_bajfinance_ns, historically leads by 1d
- Watch next: dyn_tatatech_ns (co-move) — not yet - watch; rho 0.533 vs dyn_indusindbk_bo
- Watch next: midcap_largecap_ratio (co-move) — not yet - watch; rho 0.527 vs nifty_midcap_100
- **India receivers**: dyn_jiofin_bo (rho 0.823, z 1.79); dyn_adanient_bo (rho 0.747, z 1.24); nifty_fmcg (rho 0.644, z 1.56); dyn_indianb_ns (rho 0.619, z 2.82)
- Source: Sensex today | Stock Market Live Updates: Stock to buy today: SBI Life Insurance (₹1,820) — BusinessLine Mkts, 2026-11-13. https://www.thehindubusinessline.com/markets/sensex-nifty50-today-stock-market-live-updates-13-november-2026/article71693403.ece
- Source: Stock market outlook today, 13 Nov: Sensex, Nifty prediction - DJIA, S&P, NASDAQ, GIFT Nifty, Kospi, Nikkei, Taiwan cues — Mint Markets, 2026-11-13. https://www.livemint.com/market/stock-market-news/stock-market-outlook-today-13-nov-sensex-nifty-prediction-djia-s-p-nasdaq-gift-nifty-kospi-nikkei-taiwan-11794532585928.html
- Source: Muthoot FinCorp diversifies funding to trim borrowing cost — BusinessLine Mkts, 2026-11-12. https://www.thehindubusinessline.com/markets/muthoot-fincorp-diversifies-funding-to-trim-borrowing-cost/article71695055.ece
- Historical analogues: 2025-07-18 (d=1.27), 2025-05-30 (d=1.4), 2025-12-19 (d=1.41)

### [RED 6.12] fx · 2 series ↓
- eur_usd [FX]: last 1.11, z20 -3.29, zc -0.71, resid-z -2.11 [unexplained], 1d -0.27%, |z20|=3.29; 1y-pct=0
- gbp_usd [FX]: last 1.32, z20 -2.39, zc -0.75, resid-z -1.69 [unexplained], 1d -0.29%, |z20|=2.39
- **Mechanism**: fx · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: usd_cny (inverse) — not yet - watch; rho -0.044 vs eur_usd, historically leads by 1d
- Source: Sterling drops against firmer dollar as markets price in a hawkish Fed — ET Markets, 2026-11-11. https://economictimes.indiatimes.com/markets/forex/forex-news/sterling-drops-against-firmer-dollar-as-markets-price-in-a-hawkish-fed/articleshow/135738659.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-05-06 (d=0.12), 2025-08-15 (d=0.3)

### [AMBER 5.52] cross-asset · 3 series ↓
- btc_usd [CRYPTO]: last 70860.53, z20 -2.20, zc -0.39, resid-z -1.34 [quiet], 1d -0.96%, |z20|=2.20
- eth_usd [CRYPTO]: last 2009.50, z20 -2.05, zc -0.12, resid-z -0.27 [quiet], 1d -0.46%, |z20|=2.05
- dyn_coin [EQUITIES]: last 130.62, z20 -1.56, zc -0.88, resid-z 0.21 [quiet], 1d -4.15%, 1y-pct=0
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.4).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.74 vs btc_usd
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.738 vs btc_usd
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.72 vs btc_usd
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.633 vs btc_usd
- Watch next: vix (inverse) — not yet - watch; rho -0.564 vs btc_usd
- Source: Global Market Today: Asian stocks gain after Nvidia shakeup, oil steady — ET Markets, 2026-11-13. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-today-asian-stocks-gain-after-nvidia-shakeup-oil-steady/articleshow/135785602.cms
- Source: CHINA PLANS $15 BILLION SHIPPING INSURANCE RIVAL TO LLOYD'S OF LONDON Beijing is exploring a $15 billion maritime insurance and reinsurance hub by 2029, challenging Western dominance of global shipping coverage. The proposed system would protect Chinese shipping from Western sanctions and disruption — DeItaone, 2026-11-12. https://t.me/walter_bloomberg/38481
- Source: UK Vows Global Climate Leadership as PM Doubles Down on Net Zero — OilPrice, 2026-11-12. https://oilprice.com/Latest-Energy-News/World-News/UK-Vows-Global-Climate-Leadership-as-PM-Doubles-Down-on-Net-Zero.html
- Historical analogues: 2026-05-22 (d=0.4), 2025-10-16 (d=0.58), 2025-04-10 (d=0.59)

### [RED 4.86] usd_jpy ↑
- usd_jpy [FX]: last 159.88, z20 2.86, zc 0.16, resid-z 1.50 [unexplained], 1d 0.09%, |z20|=2.86
- **Mechanism**: usd_jpy ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho 0.416 via usd_jpy, z 0.1, quiet)
- **India receivers**: dyn_idbi_ns (rho 0.416, z 0.1)
- Source: Yen Falls to Cusp of 160 Level, Fanning Intervention Risk — Mint Markets, 2026-11-12. https://www.livemint.com/market/yen-falls-to-cusp-of-160-level-fanning-intervention-risk-11794521542082.html
- Source: The Yen Is Becoming Too Hard for Some Investors to Trade — Mint Markets, 2026-11-12. https://www.livemint.com/market/the-yen-is-becoming-too-hard-for-some-investors-to-trade-11794520064240.html
- Source: Dollar near one-month high as yen edges toward 160 — ET Markets, 2026-11-12. https://economictimes.indiatimes.com/markets/forex/forex-news/dollar-near-one-month-high-as-yen-edges-toward-160/articleshow/135751707.cms
- Historical analogues: 2026-07-10 (d=0.0), 2026-06-12 (d=0.0), 2025-07-30 (d=0.01)

### [RED 4.6] commodities · 2 series ↓
- comex_gold [COMMODITIES]: last 3912.30, z20 -1.77, zc -0.00, resid-z -1.00 [quiet], 1d -0.01%, |z20|=1.77; 1y-pct=0; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 50.62, z20 -1.01, zc 0.02, resid-z 0.95 [quiet], 1d 0.06%, 1y-pct=3; co-occur[gold_silver] same-direction (channel VALID)
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.511 via comex_gold, z 2.02, reacted); dyn_karurvysya_ns (rho 0.43 via comex_gold, z 2.15, reacted)
- Watch next: gold_silver_ratio (inverse) — not yet - watch; rho -0.501 vs comex_gold
- **India receivers**: dyn_muthootfin_ns (rho 0.511, z 2.02); dyn_karurvysya_ns (rho 0.43, z 2.15)
- Source: Gold inches higher but heads for weekly loss on Fed hike concerns — ET Markets, 2026-11-13. https://economictimes.indiatimes.com/markets/commodities/news/gold-inches-higher-but-heads-for-weekly-loss-on-fed-hike-concerns/articleshow/135785994.cms
- Source: Gold drops to over one-year low as fading Middle East peace hopes fan inflation fears — Mint Markets, 2026-11-12. https://www.livemint.com/market/gold-drops-to-over-one-year-low-as-fading-middle-east-peace-hopes-fan-inflation-fears-11794511222562.html
- Source: Today’s Gold Rate in India November 12: Gold prices down in Delhi, Mumbai, Kolkata, Chennai and Bengaluru — BusinessLine Mkts, 2026-11-12. https://www.thehindubusinessline.com/gold-rate-today/gold-price-today-in-delhi-mumbai-kolkata-chennai-bengaluru-hyderabad-pune-gold-rates-metro-cities-november-12-2026/article71692844.ece
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-15 (d=0.09), 2026-05-15 (d=0.16)

### [RED 4.58] dyn_301077_sz ↑
- dyn_301077_sz [EQUITIES]: last 20.77, z20 2.58, zc 1.39, resid-z 0.60 [quiet], 1d 3.69%, |z20|=2.58
- **Mechanism**: dyn_301077_sz ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-06-18 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: shanghai_comp (co-move) — not yet - watch; rho 0.603 vs dyn_301077_sz, historically leads by 4d
- Watch next: taiwan_weighted (co-move) — not yet - watch; rho 0.561 vs dyn_301077_sz, historically leads by 1d
- Source: Nvidia shares recover 4.5% after steep sell-off; China spy probe and November 17 earnings to test investor confidence — Mint Markets, 2026-11-11. https://www.livemint.com/market/stock-market-news/nvidia-shares-recover-4-5-after-steep-sell-off-china-spy-probe-and-november-17-earnings-to-test-investor-confidence-11794413606492.html
- Historical analogues: 2026-06-18 (d=0.0), 2026-03-30 (d=0.02), 2026-06-03 (d=0.03)

### [RED 4.46] indices · 4 series ↑
- stoxx_50 [INDICES]: last 6409.74, z20 2.80, zc 0.26, resid-z 0.72 [quiet], 1d 0.26%, |z20|=2.80
- dax [INDICES]: last 26816.59, z20 2.41, zc 0.51, resid-z 1.17 [quiet], 1d 0.58%, |z20|=2.41; 1y-pct=100
- cac_40 [INDICES]: last 8372.71, z20 2.26, zc 0.56, resid-z 1.03 [quiet], 1d 0.48%, |z20|=2.26
- ftse_100 [INDICES]: last 10867.29, z20 1.91, zc 0.40, resid-z 0.86 [quiet], 1d 0.29%, |z20|=1.91
- **Mechanism**: indices · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.511 via cac_40, z 2.02, reacted); nifty_fmcg (rho 0.508 via cac_40, z 1.56, reacted); nifty_midcap_100 (rho 0.506 via dax, z 2.22, reacted); dyn_jiofin_bo (rho 0.462 via cac_40, z 1.79, reacted); dyn_tataelxsi_ns (rho 0.442 via ftse_100, z 0.87, quiet)
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.598 vs stoxx_50, historically leads by 5d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.522 vs stoxx_50, historically leads by 5d
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.512 vs stoxx_50, historically leads by 5d
- Watch next: hy_oas (inverse) — not yet - watch; rho -0.505 vs stoxx_50, historically leads by 2d
- **India receivers**: dyn_muthootfin_ns (rho 0.511, z 2.02); nifty_fmcg (rho 0.508, z 1.56); nifty_midcap_100 (rho 0.506, z 2.22); dyn_jiofin_bo (rho 0.462, z 1.79)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-16 (d=0.34), 2026-03-31 (d=0.71)

### [AMBER 4.34] dyn_nvda ↓
- dyn_nvda [EQUITIES]: last 166.04, z20 -2.34, zc -1.08, resid-z -2.56 [unexplained], 1d -4.43%, |z20|=2.34; 1y-pct=0
- **Mechanism**: dyn_nvda ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: nasdaq_100 (co-move) — not yet - watch; rho 0.812 vs dyn_nvda, historically leads by 4d
- Watch next: sp500 (co-move) — not yet - watch; rho 0.739 vs dyn_nvda, historically leads by 4d
- Watch next: vix (inverse) — not yet - watch; rho -0.695 vs dyn_nvda
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.674 vs dyn_nvda
- Watch next: russell_2000 (co-move) — not yet - watch; rho 0.623 vs dyn_nvda
- Source: NVIDIA stock crash: Why did AMD, Broadcom shares rise up to 5% after Jensen Huang's exit? Experts' views — Mint Markets, 2026-11-13. https://www.livemint.com/market/stock-market-news/nvidia-stock-crash-why-did-amd-broadcom-shares-rise-up-to-5-after-jensen-huangs-exit-experts-views-11794530850114.html
- Source: Jensen Huang forfeits $108 million in unvested Nvidia equity — ET Markets, 2026-11-13. https://economictimes.indiatimes.com/markets/us-stocks/news/jensen-huang-forfeits-108-million-in-unvested-nvidia-equity/articleshow/135785775.cms
- Source: Global Market Today: Asian stocks gain after Nvidia shakeup, oil steady — ET Markets, 2026-11-13. https://economictimes.indiatimes.com/markets/us-stocks/news/global-market-today-asian-stocks-gain-after-nvidia-shakeup-oil-steady/articleshow/135785602.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-24 (d=0.03), 2026-05-04 (d=0.03)

## Watchlist (below surfacing floor)
tips_10y_real ↑ (4.06), natgas ↑ (4.0), dyn_tech ↑ (3.87), dyn_schd ↑ (3.09), ust_2s10s ↓ (2.92), dyn_4417_t ↑ (2.9), dyn_indianb_ns ↑ (2.82), dxy ↑ (2.74), eur_inr ↓ (2.72), dyn_rs ↑ (2.64), dyn_lth ↑ (2.57), aud_usd ↓ (2.45)

## India macro
- nifty_50: 25299.3496 (1d 0.18%, z20 2.19, flag amber)
- nifty_midcap_100: 62037.1016 (1d 0.85%, z20 2.22, flag amber)
- usd_inr: 94.0330 (1d 0.36%, z20 -1.32, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4521 (1d 0.67%, z20 -0.99, flag none)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-0d · Kharif sowing data T-0d · India WPI T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 81.5 — "India bonds track Treasury weakness ahead of debt supply"
- INOXINDIA.NS (INOX INDIA LIMITED) score 78.6 — "India bonds track Treasury weakness ahead of debt supply"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 78.4 — "India bonds track Treasury weakness ahead of debt supply"
- NVDA (NVIDIA Corporation) score 76.7 — "US stocks close lower as Nvidia drop outweighs energy gains: Stock Market Highlights"
- INDIANB.NS (INDIAN BANK) score 57.5 — "DEMOCRATIC SENATOR REED SAYS CONGRESS NEEDS ASSESSMENT OF WHETHER NVIDIA IS "TOO BIG TO FA"
- BAC (Bank of America Corporation) score 51.4 — "DEMOCRATIC SENATOR REED SAYS CONGRESS NEEDS ASSESSMENT OF WHETHER NVIDIA IS "TOO BIG TO FA"
- HDB (HDFC Bank Limited) score 43.9 — "DEMOCRATIC SENATOR REED SAYS CONGRESS NEEDS ASSESSMENT OF WHETHER NVIDIA IS "TOO BIG TO FA"
- TGT (Target Corporation) score 42.0 — "ANTHROPIC IPO IS 6 TIMES OVERSUBSCRIBED AS VALUATION TARGETS $1.4 TRILLION Anthropic’s ($A"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 40.7 — "DEMOCRATIC SENATOR REED SAYS CONGRESS NEEDS ASSESSMENT OF WHETHER NVIDIA IS "TOO BIG TO FA"
- IDBI.NS (IDBI BANK LIMITED) score 40.7 — "DEMOCRATIC SENATOR REED SAYS CONGRESS NEEDS ASSESSMENT OF WHETHER NVIDIA IS "TOO BIG TO FA"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 40.7 — "DEMOCRATIC SENATOR REED SAYS CONGRESS NEEDS ASSESSMENT OF WHETHER NVIDIA IS "TOO BIG TO FA"
- TECHM.NS (TECH MAHINDRA LIMITED) score 37.0 — "UltraTech Cem Share Price Highlights: UltraTech Cem. Stock Price History"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 34.7 — "UltraTech Cem Share Price Highlights: UltraTech Cem. Stock Price History"
- TECH (Bio-Techne Corp) score 34.7 — "UltraTech Cem Share Price Highlights: UltraTech Cem. Stock Price History"
- 301077.SZ (CHINASTARS) score 32.6 — "CHINA PLANS $15 BILLION SHIPPING INSURANCE RIVAL TO LLOYD'S OF LONDON Beijing is exploring"
- CHKP (Check Point Software Technolog) score 30.2 — "Oil India dividend, Q2 results 2026: PSU giant announces interim payout as profit more tha"
- OHI (Omega Healthcare Investors, In) score 29.9 — "RETAIL INVESTORS POUR $111 MILLION INTO NVIDIA IN JUST 30 MINUTES Retail investors bought "
- COIN (Coinbase Global, Inc.) score 24.5 — "CHINA PLANS $15 BILLION SHIPPING INSURANCE RIVAL TO LLOYD'S OF LONDON Beijing is exploring"
- LTH (Life Time Group Holdings, Inc.) score 24.4 — "CHINA PLANS $15 BILLION SHIPPING INSURANCE RIVAL TO LLOYD'S OF LONDON Beijing is exploring"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 22.7 — "Q2 Results Highlights Nov 12: HAL, Oil India, Manappuram Finance log gains, Ola Electric n"
- BOND (PIMCO Active Bond Exchange-Tra) score 21.3 — "Bond yields just saw their biggest surge since 2022 as expectations grow for more Fed rate"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 20.8 — "US stocks close lower as Nvidia drop outweighs energy gains: Stock Market Highlights"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 19.4 — "Q2 Results Highlights Nov 12: HAL, Oil India, Manappuram Finance log gains, Ola Electric n"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 16.8 — "Tata Consumer Share Price Live Updates: Tata Consumer Market Movement"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 16.8 — "Tata Consumer Share Price Live Updates: Tata Consumer Market Movement"
- SCHD (Schwab US Dividend Equity ETF) score 13.7 — "Oil India dividend, Q2 results 2026: PSU giant announces interim payout as profit more tha"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 12.9 — "NVIDIA stock crash: Why did AMD, Broadcom shares rise up to 5% after Jensen Huang's exit? "
- JUSTDIAL.BO (JUST DIAL LTD.) score 12.2 — "RETAIL INVESTORS POUR $111 MILLION INTO NVIDIA IN JUST 30 MINUTES Retail investors bought "
- BZ=F (Brent Crude Oil Last Day Finan) score 11.9 — "US OCTOBER BUDGET DEFICIT HITS RECORD $404 BILLION The US federal budget deficit surged to"
- JIOFIN.BO (Jio Financial Services Limited) score 10.9 — "Federal Reserve Board announces pricing, effective January 1, 2027, for payment services t"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 9.0 — "Buzzing stocks: Bajaj Finance, Tata Power, Adani Enterprises, Sandur Manganese, Alivus Lif"
- CRWV (CoreWeave, Inc.) score 8.3 — "COREWEAVE SHARES FOLLOW NVIDIA LOWER, DOWN 6%"
- RS (Reliance, Inc.) score 5.8 — "Q2 Results Highlights Nov 12: HAL, Oil India, Manappuram Finance log gains, Ola Electric n"
- META (Meta) score 5.7 — "India ETFs draw ₹35,120 crore in Q3 as large-cap, precious metals lead inflows"
- DEMZ (Democratic Large Cap Core ETF) score 5.5 — "DEMOCRATIC SENATOR REED SAYS CONGRESS NEEDS ASSESSMENT OF WHETHER NVIDIA IS "TOO BIG TO FA"
- JEF (Jefferies Financial Group Inc.) score 4.8 — "FIIs are back! Jefferies lists 11 stocks that can be the biggest beneficiaries"
- GS (Goldman Sachs Group, Inc. (The) score 3.7 — "Why Goldman Sachs is now changing its Federal Reserve interest-rate forecast"
- BLLN (BillionToOne, Inc.) score 2.8 — "US OCTOBER BUDGET DEFICIT HITS RECORD $404 BILLION The US federal budget deficit surged to"
- SEPN (Septerna, Inc.) score 2.6 — "Promoter shareholding in listed companies hits three-year high at 41.93% in September quar"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.2 — "Broker’s call: PB Fintech (Buy)"

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