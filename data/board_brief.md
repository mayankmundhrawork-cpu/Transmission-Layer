# Transmission Layer — board brief · 2026-10-27 00:39Z

data as of **2026-10-27** · 97 series · 13 red / 39 amber · 8 events surfaced (31 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 1.0, 17d in regime; vol-pct None, breadth-off 1.0, Markov P(high-vol) 0.021)
- [INVERTED] **safe_haven_gold** — corr20 -0.36, corr60 -0.37, contra nifty_50 corr20=0.42, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.85, corr60 0.82, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.1, corr60 0.17, last shift 2026-09-03. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.15, corr60 0.08, last shift 2026-09-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.91, corr60 -0.78, last shift 2026-09-09. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.18, corr60 -0.0, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 -0.1, corr60 -0.14, last shift 2026-08-13. Channel: real yields up -> non-yielding gold down
- [WEAK] **gsr_stress_gauge** — corr20 0.54, corr60 0.25, last shift 2026-07-30. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **3 of 89** scanned series survive multiplicity control (effective p ≤ 3.956591173648327e-05)
- **SETUP** bovespa → usd_brl: leads 1d (ccf -0.589, β -0.4317, p 0.0); driver zc -12.78 → expected 5.798%. Type hit-rate 0.825 (n=1845).
- Track record · residual_reversion: hit-rate **0.504** (n=1116) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.825** (n=1845) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.5** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 7.83] cross-asset · 3 series ↓
- comex_gold [COMMODITIES]: last 4026.60, z20 -2.22, zc 0.00, resid-z -0.90 [quiet], 1d 0.00%, |z20|=2.22; co-occur[gold_silver] same-direction (channel VALID)
- comex_silver [COMMODITIES]: last 54.06, z20 -1.81, zc 0.00, resid-z -0.00 [quiet], 1d 0.00%, |z20|=1.81; co-occur[gold_silver] same-direction (channel VALID)
- gold_silver_ratio [DERIVED]: last 74.48, z20 1.51, zc n/a, resid-z n/a [quiet], 1d 0.00%, GSR<75 (extreme low); |z20|=1.51
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: comex_copper (co-move) — not yet - watch; rho 0.565 vs comex_silver, historically leads by 1d
- Source: GEOPOLITICAL TENSIONS COMPLICATE GOLD'S BULL CASE Middle East tensions are creating mixed signals for gold, according to American Hartford Gold president Max Baecker. While geopolitical uncertainty supports safe-haven demand, rising energy prices could fuel inflation, strengthen the dollar, and pres — DeItaone, 2026-10-26. https://t.me/walter_bloomberg/37567
- Source: Inflows into gold ETFs turned negative after 13 weeks as the yellow metal fell 4% last week — BusinessLine Mkts, 2026-10-26. https://www.thehindubusinessline.com/markets/gold/inflows-into-gold-etfs-turned-negative-after-13-weeks-as-the-yellow-metal-fell-4-last-week/article71627333.ece
- Source: Gold gains as oil slide cools some inflation concerns — BusinessLine Mkts, 2026-10-26. https://www.thehindubusinessline.com/markets/gold/gold-gains-as-oil-slide-cools-some-inflation-concerns/article71626429.ece
- Historical analogues: 2026-05-22 (d=0.0), 2026-05-15 (d=0.21), 2025-07-30 (d=0.29)

### [RED 7.45] dyn_lth ↑
- dyn_lth [EQUITIES]: last 43.86, z20 5.45, zc 2.15, resid-z -0.11 [moved], 1d 4.60%, |z20|=5.45
- **Mechanism**: dyn_lth ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Anthropic IPO: It’s official now! Artificial intelligence giant files papers to sell shares to public for first time — Mint Markets, 2026-10-26. https://www.livemint.com/market/stock-market-news/anthropic-ipo-it-s-official-now-artificial-intelligence-giant-files-papers-to-sell-shares-to-public-for-first-time-11793019537204.html
- Source: Kotak Mahindra Bank shares rise 2% as top Nifty gainer | Is it right time to book profits or wait? Target, stop loss — Mint Markets, 2026-10-26. https://www.livemint.com/market/stock-market-news/kotak-mahindra-bank-shares-rise-2-as-top-nifty-gainer-is-it-right-time-to-book-profits-or-wait-target-stop-loss-11792995247655.html
- Source: Silver prices at 2026 lowest;  ₹2,23,500 away from record high! Right time to buy for good returns? Target price per kg — Mint Markets, 2026-10-26. https://www.livemint.com/market/commodities/silver-prices-at-2026-lowest-rs-2-23-500-away-from-record-high-right-time-to-buy-for-good-returns-target-price-per-kg-11792992915881.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-17 (d=0.02), 2025-12-31 (d=0.02)

### [RED 6.75] cross-asset · 6 series ↓
- india_vix [INDICES]: last 17.13, z20 2.60, zc 0.27, resid-z n/a [quiet], 1d 1.62%, |z20|=2.60
- dyn_bajfinance_ns [EQUITIES]: last 918.70, z20 -2.44, zc -0.62, resid-z -0.85 [quiet], 1d -1.10%, |z20|=2.44
- dyn_swiggy_ns [EQUITIES]: last 185.75, z20 -2.16, zc 0.65, resid-z 0.92 [quiet], 1d 5.54%, |z20|=2.16; 1y-pct=0
- nifty_midcap_100 [INDICES]: last 56466.80, z20 -2.12, zc 0.96, resid-z 1.18 [quiet], 1d 1.20%, |z20|=2.12
- dyn_jiofin_bo [EQUITIES]: last 205.40, z20 -2.00, zc 0.12, resid-z -0.25 [quiet], 1d 0.20%, |z20|=2.00; 1y-pct=0
- dyn_policybzr_ns [EQUITIES]: last 1023.00, z20 -0.44, zc 0.26, resid-z -0.40 [quiet], 1d 0.79%, 1y-pct=3
- **Mechanism**: cross-asset · 6 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 0.79).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho -0.733 via india_vix, z 0.16, quiet); nifty_metal (rho 0.691 via nifty_midcap_100, z -1.24, reacted); nifty_fmcg (rho 0.602 via nifty_midcap_100, z -2.14, reacted); midcap_largecap_ratio (rho 0.595 via nifty_midcap_100, z -2.45, reacted); dyn_indusindbk_bo (rho -0.572 via india_vix, z -1.6, reacted)
- Watch next: nifty_50 (inverse) — not yet - watch; rho -0.733 vs india_vix, historically leads by 1d
- Watch next: dyn_indianb_ns (co-move) — not yet - watch; rho 0.558 vs nifty_midcap_100, historically leads by 1d
- **India receivers**: nifty_50 (rho -0.733, z 0.16); nifty_metal (rho 0.691, z -1.24); nifty_fmcg (rho 0.602, z -2.14); midcap_largecap_ratio (rho 0.595, z -2.45)
- Source: Swiggy shares rise 6% after 4-session down episode; is this a relief rally or worst is over? Experts decode | Target, SL — Mint Markets, 2026-10-26. https://www.livemint.com/market/stock-market-news/swiggy-shares-rise-6-after-4-session-down-episode-is-this-a-relief-rally-or-worst-is-over-experts-decode-target-sl-11792998360954.html
- Source: Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bullish despite target price cuts — ET Markets, 2026-10-26. https://economictimes.indiatimes.com/markets/stocks/news/swiggy-shares-jump-5-a-day-after-q2-results-sparked-a-17-crash-why-brokerages-remain-bullish-despite-target-price-cuts/articleshow/135205591.cms
- Source: Mcap of eight of the top-10 firms erodes by ₹1.55 lakh cr; HDFC Bank, Bajaj Fin biggest laggards — BusinessLine Mkts, 2026-10-25. https://www.thehindubusinessline.com/markets/mcap-of-eight-of-the-top-10-firms-erodes-by-155-lakh-cr-hdfc-bank-bajaj-fin-biggest-laggards/article71622878.ece
- Historical analogues: 2025-07-21 (d=0.79), 2025-05-30 (d=0.88), 2025-07-10 (d=0.91)

### [AMBER 6.59] cross-asset · 6 series ↓
- tips_10y_real [RATES]: last 2.66, z20 -2.44, zc 0.37, resid-z -0.05 [quiet], 1d 0.76%, |z20|=2.44
- ust_10y [RATES]: last 5.00, z20 -2.34, zc 0.73, resid-z 0.24 [quiet], 1d 0.81%, |z20|=2.34
- dyn_bond [EQUITIES]: last 88.59, z20 2.08, zc 0.27, resid-z 0.61 [quiet], 1d 0.10%, |z20|=2.08
- ust_30y [RATES]: last 5.33, z20 -2.05, zc 0.85, resid-z 0.47 [quiet], 1d 0.76%, |z20|=2.05
- ust_2y [RATES]: last 4.69, z20 -1.94, zc 0.65, resid-z 0.19 [quiet], 1d 0.86%, |z20|=1.94
- dyn_schd [EQUITIES]: last 35.27, z20 1.89, zc -0.01, resid-z -0.31 [quiet], 1d -0.01%, 1y-pct=99
- **Mechanism**: cross-asset · 6 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: kospi (inverse) — not yet - watch; rho -0.549 vs dyn_schd
- Watch next: dxy (inverse) — not yet - watch; rho -0.546 vs dyn_bond
- Watch next: usd_jpy (inverse) — not yet - watch; rho -0.044 vs ust_2y, historically leads by 1d
- Source: Dividend stocks are having an excellent October as tech sector struggles — MarketWatch Top, 2026-10-26. https://www.marketwatch.com/story/dividend-stocks-are-having-an-excellent-october-as-tech-sector-struggles-5ae40b02?mod=mw_rss_topstories
- Source: Analysis: Why a $2 trillion deficit and 5% Treasury yields are becoming America's biggest economic challenge — CNBC Economy, 2026-10-26. https://www.cnbc.com/2026/10/15/treasury-yields-deficit-national-debt-ai.html
- Source: Nippon Life AMC shares: Last chance to buy for  ₹9.50 interim dividend; record date, dividend yield — Mint Markets, 2026-10-26. https://www.livemint.com/market/stock-market-news/nippon-life-amc-shares-last-chance-to-buy-for-rs-9-50-interim-dividend-record-date-dividend-yield-11793035793393.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-12 (d=0.58), 2025-05-19 (d=0.98)

### [RED 5.79] dyn_atherenerg_ns ↑
- dyn_atherenerg_ns [EQUITIES]: last 1575.00, z20 3.79, zc 4.51, resid-z 4.11 [unexplained], 1d 14.13%, |z20|=3.79
- **Mechanism**: dyn_atherenerg_ns ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.381 via dyn_atherenerg_ns, z -2.12, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.381, z -2.12)
- Source: Q2 Results Today Highlights: Tata Consumer Q2 profit declines, Aequs, Dalmia Bharat PAT declines q-o-q, Ather Energy & ITC Hotels jump after Q2 results, BoM, TMB, IOB, Mankind Pharma, APL Apollo Q2 PAT rise, Paytm, KFin Tech, Nazara to announce Q2 results — BusinessLine Mkts, 2026-10-26. https://www.thehindubusinessline.com/markets/q2-results-today-highlights-paytm-tata-consumer-mankind-pharma-rec-itc-hotels-iob-ather-aegis-logistics-supreme-ind-aequs-nazara-sona-blw-tmb-bom-infosys-kotak-idfc-results-26-october-2026/article71625561.ece
- Source: Ather Energy shares skyrocket 19% after EV maker swings to Rs 1.26 crore profit in Q2 — ET Markets, 2026-10-26. https://economictimes.indiatimes.com/markets/stocks/news/ather-energy-shares-skyrocket-19-after-ev-maker-swings-to-rs-1-26-crore-profit-in-q2/articleshow/135209355.cms
- Source: Q2 Results Today Live: Ather Energy logs profit in Q2, ITC Hotels surge after Q2 results, TMB, IOB, APL Apollo, Supreme Industries Q2 PAT rise, Paytm, Tata Consumer, Dalmia Bharat, KFin Tech, Mankind Pharma, BOM, Sona BLW, Nazara, Aequs to announce Q2 results — BusinessLine Mkts, 2026-10-26. https://www.thehindubusinessline.com/markets/q2-results-today-live-updates-paytm-tata-consumer-mankind-pharma-rec-itc-hotels-iob-ather-aegis-logistics-supreme-ind-aequs-nazara-sona-blw-tmb-bom-infosys-kotak-idfc-results-26-october-2026/article71625561.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-31 (d=0.03), 2025-07-15 (d=0.03)

### [AMBER 5.33] cross-asset · 2 series ↓
- dyn_coin [EQUITIES]: last 159.68, z20 -2.50, zc -0.62, resid-z -0.11 [quiet], 1d -2.90%, |z20|=2.50
- btc_usd [CRYPTO]: last 80239.09, z20 -1.64, zc 0.26, resid-z -0.98 [quiet], 1d 0.55%, |z20|=1.64
- **Mechanism**: cross-asset · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.06).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.382 via btc_usd, z -2.1, reacted)
- **India receivers**: dyn_muthootfin_ns (rho 0.382, z -2.1)
- Source: COINBASE GLOBAL INC: SOME USERS MAY CURRENTLY BE UNABLE TO CONVERT BRL TO BUY/SELL CRYPTO ON COINBASE — DeItaone, 2026-10-26. https://t.me/walter_bloomberg/37558
- Source: India’s crude steel output rises 5.6% in Jan-Sept even as global production dips — BusinessLine Mkts, 2026-10-26. https://www.thehindubusinessline.com/markets/commodities/indias-crude-steel-output-rises-56-in-jan-sept-even-as-global-production-dips/article71620869.ece
- Source: ANTHROPIC: WE HAVE APPLIED TO LIST OUR CLASS A COMMON STOCK ON NASDAQ GLOBAL SELECT MARKET UNDER THE SYMBOL $ANT — DeItaone, 2026-10-26. https://t.me/walter_bloomberg/37547
- Historical analogues: 2026-05-22 (d=0.06), 2026-04-02 (d=0.18), 2025-10-22 (d=0.33)

### [RED 5.06] dyn_tgt ↓
- dyn_tgt [EQUITIES]: last 148.50, z20 -3.06, zc -1.47, resid-z -1.89 [unexplained], 1d -2.79%, |z20|=3.06
- **Mechanism**: dyn_tgt ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_adanient_bo (rho -0.359 via dyn_tgt, z -1.67, reacted)
- **India receivers**: dyn_adanient_bo (rho -0.359, z -1.67)
- Source: Goldman Sachs Kospi target cut: Why South Korea market experts lowered target to 9,000 from 12,000 - Explained — Mint Markets, 2026-10-26. https://www.livemint.com/market/stock-market-news/goldman-sachs-kospi-target-cut-why-south-korea-market-experts-lowered-target-to-9-000-from-12-000-explained-11793031984804.html
- Source: ANT - ANTHROPIC IPO COULD TARGET $2 TRILLION VALUATION Anthropic has publicly filed for its IPO, with trading potentially beginning before Thanksgiving. Market speculation points to a massive $100B offering at a $2T valuation, although the company has not disclosed its fundraising target. That would — DeItaone, 2026-10-26. https://t.me/walter_bloomberg/37553
- Source: Top 3 stocks to buy tomorrow: Laurus Labs, MCX, Coforge by market expert; check stop-loss, target price for Tue, 27 Oct — Mint Markets, 2026-10-26. https://www.livemint.com/market/stock-market-news/top-3-stocks-to-buy-tomorrow-laurus-labs-mcx-coforge-by-market-expert-check-stop-loss-target-price-for-tue-27-oct-11793014330701.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.01), 2025-09-30 (d=0.01)

### [RED 5.02] dyn_meta ↓
- dyn_meta [EQUITIES]: last 630.47, z20 -3.02, zc -0.70, resid-z -0.15 [quiet], 1d -1.89%, |z20|=3.02
- **Mechanism**: dyn_meta ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Source: Nvidia, AMD and Broadcom could buy Meta shares as part of $35 billion stock offering — MarketWatch Top, 2026-10-26. https://www.marketwatch.com/story/nvidia-amd-and-broadcom-could-buy-meta-shares-as-part-of-35-billion-stock-offering-d816fec2?mod=mw_rss_topstories
- Source: Meta plans to raise up to $95 billion to fund AI and data centre expansion — BusinessLine Mkts, 2026-10-26. https://www.thehindubusinessline.com/markets/meta-plans-to-raise-up-to-95-billion-to-fund-ai-and-data-centre-expansion/article71627458.ece
- Source: Meta to create non-voting shares to fund AI expansion, retain Zuckerberg’s control — ET Markets, 2026-10-26. https://economictimes.indiatimes.com/markets/us-stocks/wall-street-guide/meta-to-create-non-voting-shares-to-fund-ai-expansion-retain-zuckerbergs-control/articleshow/135206256.cms
- Historical analogues: 2026-05-22 (d=0.0), 2025-08-21 (d=0.05), 2025-10-09 (d=0.12)

## Watchlist (below surfacing floor)
dyn_chkp ↑ (5.0), dyn_tech ↑ (4.7), cross-asset · 2 series ↑ (4.53), dyn_ohi ↑ (4.1), dyn_sepn ↑ (4.1), dyn_hdb ↓ (3.92), dyn_rs ↑ (3.73), sofr ↑ (3.31), shanghai_comp ↓ (3.28), ig_oas ↑ (3.23), eur_usd ↓ (3.21), dyn_4417_t ↑ (3.15)

## India macro
- nifty_50: 22753.1992 (1d 0.68%, z20 0.16, flag none)
- nifty_midcap_100: 56466.8008 (1d 1.20%, z20 -2.12, flag amber)
- usd_inr: 94.9380 (1d 0.24%, z20 -0.97, flag none)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4817 (1d 0.51%, z20 -2.45, flag amber)
- Next India prints: NSDL FPI flows T-0d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d · IMD weekly rainfall T-6d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 75.7 — "Indian markets rebound, but rising oil prices keep investors cautious"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 72.4 — "Indian markets rebound, but rising oil prices keep investors cautious"
- INOXINDIA.NS (INOX INDIA LIMITED) score 72.1 — "Indian markets rebound, but rising oil prices keep investors cautious"
- INDIANB.NS (INDIAN BANK) score 67.4 — "Indian markets rebound, but rising oil prices keep investors cautious"
- BAC (Bank of America Corporation) score 62.1 — "GEOPOLITICAL TENSIONS COMPLICATE GOLD'S BULL CASE Middle East tensions are creating mixed "
- HDB (HDFC Bank Limited) score 54.9 — "Jio IPO brings a smaller payday for bankers than other large offers"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 54.2 — "Jio IPO brings a smaller payday for bankers than other large offers"
- IDBI.NS (IDBI BANK LIMITED) score 53.8 — "Jio IPO brings a smaller payday for bankers than other large offers"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 53.8 — "Jio IPO brings a smaller payday for bankers than other large offers"
- TGT (Target Corporation) score 44.3 — "ANT - ANTHROPIC IPO COULD TARGET $2 TRILLION VALUATION Anthropic has publicly filed for it"
- COIN (Coinbase Global, Inc.) score 42.9 — "NTHROPIC: WE HAVE APPLIED TO LIST OUR CLASS A COMMON STOCK ON NASDAQ GLOBAL SELECT MARKET "
- TECHM.NS (TECH MAHINDRA LIMITED) score 42.1 — "AI-LINKED STOCKS CLIMB AFTER ANTHROPIC FILES FOR IPO NVIDIA UP 3.1% MICROSOFT UP 1.1% AMAZ"
- OHI (Omega Healthcare Investors, In) score 41.6 — "Retail investors return to equities with Rs 10,572 crore buying in September"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 35.4 — "AI-LINKED STOCKS CLIMB AFTER ANTHROPIC FILES FOR IPO NVIDIA UP 3.1% MICROSOFT UP 1.1% AMAZ"
- TECH (Bio-Techne Corp) score 35.4 — "AI-LINKED STOCKS CLIMB AFTER ANTHROPIC FILES FOR IPO NVIDIA UP 3.1% MICROSOFT UP 1.1% AMAZ"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 29.0 — "GEOPOLITICAL TENSIONS COMPLICATE GOLD'S BULL CASE Middle East tensions are creating mixed "
- CHKP (Check Point Software Technolog) score 28.5 — "Dividend stock down 4% today; declares  ₹12 per share dividend, record date fixed | Check "
- BOND (PIMCO Active Bond Exchange-Tra) score 24.7 — "FRANCE'S 10-YR BOND YIELD DOWN 5.3 BPS TO 4.9685% AFTER MOODY'S MAINTAINS SOVEREIGN RATING"
- LTH (Life Time Group Holdings, Inc.) score 21.9 — "Jio Platforms IPO listing on Oct 28: Time, expectations share price & key details"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 21.7 — "Shriram Finance shares falls 5% as analysts cut targets after Q2 results"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 21.6 — "Goldman Sachs Kospi target cut: Why South Korea market experts lowered target to 9,000 fro"
- 301077.SZ (CHINASTARS) score 19.7 — "China's central bank sets up non-bank financial institution bond market swap facility"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 19.2 — "Shriram Finance shares falls 5% as analysts cut targets after Q2 results"
- RS (Reliance, Inc.) score 15.7 — "Reliance's Jio Platforms IPO allotment today, 26 Oct: Check status online, latest GMP pric"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 15.3 — "Market wrap: Dr Reddys, JSW Steel, Shriram Finance, Tata Consumer top gainers and losers o"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 15.3 — "Market wrap: Dr Reddys, JSW Steel, Shriram Finance, Tata Consumer top gainers and losers o"
- JUSTDIAL.BO (JUST DIAL LTD.) score 14.9 — "US JUSTICE DEPARTMENT CHARGES FORMER FBI DIRECTOR JAMES COMEY WITH TRANSMITTING NATIONAL D"
- SEPN (Septerna, Inc.) score 14.0 — "OIL OPTIONS SIGNAL RISING MIDDLE EAST SUPPLY RISKS WTI crude oil options skew toward calls"
- META (Meta) score 13.4 — "Nvidia, AMD and Broadcom could buy Meta shares as part of $35 billion stock offering"
- BZ=F (Brent Crude Oil Last Day Finan) score 13.0 — "STOCKS OF CRUDE OIL IN THE US STRATEGIC PETROLEUM RESERVE FELL TO 282.6 MLN BARRELS LAST W"
- JIOFIN.BO (Jio Financial Services Limited) score 11.9 — "China's central bank sets up non-bank financial institution bond market swap facility"
- JEF (Jefferies Financial Group Inc.) score 10.5 — "IndusInd Bank shares rise 2% after Q2 results. Why Jefferies cut target price despite lend"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 10.0 — "Top stocks to buy: Adani Energy, AU Small Finance Bank, BPCL, IDFC First Bank — Jefferies "
- GS (Goldman Sachs Group, Inc. (The) score 8.9 — "ANTHROPIC FILES FOR NASDAQ IPO, REVEALS $80.7 BILLION LOSS Anthropic has filed for a Nasda"
- VT (Vanguard Total World Stock Ind) score 8.3 — "The Iran War Just Added $39 Billion to the World's LNG Bill"
- INFY (Infosys Limited) score 4.8 — "Infosys shares fall 4% after IT major lowers FY27 guidance. What are Goldman Sachs, Nomura"
- SWIGGY.NS (SWIGGY LIMITED) score 4.7 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"
- SCHD (Schwab US Dividend Equity ETF) score 4.0 — "Dividend stocks are having an excellent October as tech sector struggles"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.2 — "From crypto to fintech, consumer and AI: Ashish Singhal explains CoinSwitch Ventures’ Blac"
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