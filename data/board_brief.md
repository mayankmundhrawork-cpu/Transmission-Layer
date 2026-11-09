# Transmission Layer — board brief · 2026-11-09 23:26Z

data as of **2026-11-09** · 97 series · 13 red / 37 amber · 8 events surfaced (32 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.614, 3d in regime; vol-pct 0.815, breadth-off 0.412, Markov P(high-vol) 0.555)
- [INVERTED] **safe_haven_gold** — corr20 -0.15, corr60 -0.22, contra nifty_50 corr20=0.29, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.91, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.12, corr60 0.12, last shift 2026-09-10. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.08, corr60 0.05, last shift 2026-09-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.91, last shift 2026-09-16. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.28, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.1, corr60 -0.1, last shift 2026-08-12. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.33, corr60 0.29, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **9 of 89** scanned series survive multiplicity control (effective p ≤ 0.009054222265934664)
- **SETUP** dxy → eur_usd: leads 1d (ccf -0.829, β -0.8883, p 0.0); driver zc 2.49 → expected -0.656%. Type hit-rate 0.818 (n=2176).
- **SETUP** dxy → gbp_usd: leads 1d (ccf -0.733, β -0.7782, p 0.0); driver zc 2.49 → expected -0.575%. Type hit-rate 0.818 (n=2176).
- **SETUP** dxy → usd_jpy: leads 1d (ccf 0.636, β 0.8913, p 0.0); driver zc 2.49 → expected 0.658%. Type hit-rate 0.818 (n=2176).
- **SETUP** dxy → aud_usd: leads 1d (ccf -0.559, β -0.8293, p 0.0); driver zc 2.49 → expected -0.612%. Type hit-rate 0.818 (n=2176).
- Track record · residual_reversion: hit-rate **0.509** (n=1124) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.818** (n=2176) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.562** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.39] commodities · 2 series ↓
- brent [COMMODITIES]: last 92.13, z20 -2.56, zc 0.01, resid-z 0.08 [quiet], 1d -6.30%, 1-session move -6.30% ≥ 1.5%; |z20|=2.56; co-occur[inr_oil] suppressed: channel WEAK
- wti [COMMODITIES]: last 86.19, z20 -2.53, zc 0.10, resid-z 0.27 [quiet], 1d -5.11%, 1-session move -5.11% ≥ 1.5%; |z20|=2.53
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.481 via wti, z 2.64, reacted)
- Watch next: vix (co-move) — not yet - watch; rho 0.545 vs brent, historically leads by 1d
- Watch next: dyn_demz (inverse) — not yet - watch; rho -0.681 vs brent
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.652 vs brent
- Watch next: sp500 (inverse) — not yet - watch; rho -0.613 vs brent
- Watch next: dow_jones (inverse) — not yet - watch; rho -0.597 vs brent
- **India receivers**: dyn_muthootfin_ns (rho -0.481, z 2.64)
- Source: Scientists Develop Cheap Filter That Could Slash Oil Refining Energy Use by 32% — OilPrice, 2026-11-09. https://oilprice.com/Energy/Energy-General/Scientists-Develop-Cheap-Filter-That-Could-Slash-Oil-Refining-Energy-Use-by-32.html
- Source: Brent Crashes 7% on Iran Peace Hopes Despite Fresh Saudi Pipeline Attack — OilPrice, 2026-11-09. https://oilprice.com/Latest-Energy-News/World-News/Brent-Crashes-7-on-Iran-Peace-Hopes-Despite-Fresh-Saudi-Pipeline-Attack.html
- Source: Oil down more than $7 a barrel in post settlement trade as Trump signals restraint on Iran — Mint Markets, 2026-11-09. https://www.livemint.com/market/oil-down-more-than-7-a-barrel-in-post-settlement-trade-as-trump-signals-restraint-on-iran-11794254623929.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-29 (d=0.06), 2025-08-14 (d=0.06)

### [RED 7.15] cross-asset · 7 series ↑
- nifty_50 [INDICES]: last 25044.65, z20 2.81, zc 1.80, resid-z 2.78 [unexplained], 1d 0.06%, |z20|=2.81
- dyn_muthootfin_ns [EQUITIES]: last 2917.60, z20 2.64, zc 0.28, resid-z -0.76 [quiet], 1d 1.69%, |z20|=2.64
- dyn_bajfinance_ns [EQUITIES]: last 1064.85, z20 2.28, zc 0.74, resid-z -0.69 [quiet], 1d -2.11%, |z20|=2.28
- nifty_metal [INDICES]: last 12664.75, z20 2.22, zc 0.45, resid-z -1.15 [quiet], 1d -0.11%, |z20|=2.22
- dyn_jiofin_bo [EQUITIES]: last 229.95, z20 2.18, zc 0.25, resid-z -1.10 [quiet], 1d -0.28%, |z20|=2.18
- nifty_midcap_100 [INDICES]: last 61018.65, z20 2.09, zc 0.00, resid-z -2.77 [unexplained], 1d 0.66%, |z20|=2.09
- nifty_fmcg [INDICES]: last 46660.10, z20 1.91, zc 0.49, resid-z -1.60 [unexplained], 1d -0.27%, |z20|=1.91
- **Mechanism**: cross-asset · 7 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2025-07-21 (z-distance 1.08).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_adanient_bo (rho 0.701 via nifty_metal, z 1.06, reacted); dyn_indusindbk_bo (rho 0.628 via nifty_midcap_100, z 1.32, reacted); dyn_indianb_ns (rho 0.609 via nifty_midcap_100, z 4.09, reacted); dyn_policybzr_ns (rho 0.528 via nifty_midcap_100, z -1.36, reacted); nifty_it (rho 0.515 via nifty_50, z 0.71, quiet)
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.515 vs nifty_50, historically leads by 4d
- Watch next: dyn_tatatech_ns (co-move) — not yet - watch; rho 0.505 vs dyn_jiofin_bo
- **India receivers**: dyn_adanient_bo (rho 0.701, z 1.06); dyn_indusindbk_bo (rho 0.628, z 1.32); dyn_indianb_ns (rho 0.609, z 4.09); dyn_policybzr_ns (rho 0.528, z -1.36)
- Source: Promoter holding in Nifty 50 firms falls to 40% — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/promoter-holding-in-nifty-50-firms-falls-to-40/article71683186.ece
- Source: Eternal shares rebound over 70% from March lows, emerge as top Nifty 50 recovery stock; what drove the rally? — Mint Markets, 2026-11-09. https://www.livemint.com/market/eternal-shares-rebound-over-70-from-march-lows-emerge-as-top-nifty-50-recovery-stock-what-drove-the-rally-11794234112702.html
- Source: Nifty holds 25,000 after volatile session; PSU Banks surge 3.7%, IT drags — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/nifty-holds-25000-after-volatile-session-psu-banks-surge-37-it-drags/article71682374.ece
- Historical analogues: 2025-07-21 (d=1.08), 2025-07-11 (d=1.35), 2025-12-23 (d=1.37)

### [RED 7.08] usd_inr ↓
- usd_inr [FX]: last 93.92, z20 -2.08, zc -0.13, resid-z -0.39 [quiet], 1d -0.57%, 20d range extreme; |z20|=2.08; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: usd_inr ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_idbi_ns (rho -0.381 via usd_inr, z -0.26, quiet)
- **India receivers**: dyn_idbi_ns (rho -0.381, z -0.26)
- Source: Rupee’s 5-day winning streak ends with the currency closing at ₹93.93 — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/forex/rupees-5-day-winning-streak-ends-with-the-currency-closing-at-9393/article71683133.ece
- Source: FPI investments in FAR G-Secs rise nearly ₹8,000 cr as rupee gains, bond yields ease — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/fpi-investments-in-far-g-secs-rise-nearly-8000-cr-as-rupee-gains-bond-yields-ease/article71682301.ece
- Source: Rupee breaks six-day winning streak on state banks' dollar bids — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/forex/indian-rupee-breaks-six-day-winning-streak-on-state-banks-dollar-bids/article71682202.ece
- Historical analogues: 2026-07-10 (d=0.0), 2025-09-16 (d=0.01), 2026-05-29 (d=0.02)

### [AMBER 6.41] natgas ↑
- natgas [COMMODITIES]: last 3.21, z20 1.41, zc 0.50, resid-z 0.34 [quiet], 1d 7.00%, 1-session move +7.00% ≥ 5.0%
- **Mechanism**: natgas ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: gold_silver_ratio (co-move) — not yet - watch; rho 0.05 vs natgas, historically leads by 4d
- Watch next: comex_silver (inverse) — not yet - watch; rho -0.026 vs natgas, historically leads by 4d
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.016 vs natgas, historically leads by 4d
- Source: Global LNG Markets Face a Winter of Extreme Uncertainty — OilPrice, 2026-11-09. https://oilprice.com/Energy/Energy-General/Global-LNG-Markets-Face-a-Winter-of-Extreme-Uncertainty.html
- Source: China Cuts LNG Imports as Cheap Domestic Gas Undercuts Global Prices — OilPrice, 2026-11-09. https://oilprice.com/Latest-Energy-News/World-News/China-Cuts-LNG-Imports-as-Cheap-Domestic-Gas-Undercuts-Global-Prices.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-10-23 (d=0.01), 2025-05-14 (d=0.02)

### [RED 5.83] cross-asset · 3 series ↓
- eth_usd [CRYPTO]: last 2130.64, z20 -2.51, zc -1.23, resid-z 0.51 [quiet], 1d -4.73%, |z20|=2.51
- btc_usd [CRYPTO]: last 75154.45, z20 -1.76, zc -0.30, resid-z 0.02 [quiet], 1d -0.78%, |z20|=1.76
- dyn_coin [EQUITIES]: last 136.07, z20 -1.71, zc -0.30, resid-z 0.35 [quiet], 1d 0.97%, 1y-pct=0
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.03).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.741 vs eth_usd
- Watch next: sp500 (co-move) — not yet - watch; rho 0.727 vs eth_usd
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.712 vs eth_usd
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.502 vs eth_usd, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.644 vs eth_usd
- Source: Global LNG Markets Face a Winter of Extreme Uncertainty — OilPrice, 2026-11-09. https://oilprice.com/Energy/Energy-General/Global-LNG-Markets-Face-a-Winter-of-Extreme-Uncertainty.html
- Source: Indian IT stocks strengthen buoyed by weakness in the global AI trade and attractive valuations — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/indian-it-stocks-strengthen-buoyed-by-weakness-in-the-global-ai-trade-and-attractive-valuations/article71683017.ece
- Source: Broker’s Call: Healthcare Global Enterprises (Buy) — BusinessLine Mkts, 2026-11-09. https://www.thehindubusinessline.com/markets/brokers-call-healthcare-global-enterprises-buy/article71682158.ece
- Historical analogues: 2026-05-22 (d=0.03), 2025-04-10 (d=0.47), 2025-03-31 (d=0.67)

### [RED 5.18] dyn_tgt ↑
- dyn_tgt [EQUITIES]: last 165.90, z20 3.18, zc 0.14, resid-z 0.20 [quiet], 1d 4.73%, |z20|=3.18; 1y-pct=99
- **Mechanism**: dyn_tgt ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_schd (co-move) — not yet - watch; rho 0.634 vs dyn_tgt, historically leads by 4d
- Source: Top 3 stocks to buy this week: Union Bank, Ather Energy, Laurus Labs by market expert; check stop-loss, target price — Mint Markets, 2026-11-09. https://www.livemint.com/market/stock-market-news/top-3-stocks-to-buy-this-week-union-bank-ather-energy-laurus-labs-by-market-expert-check-stop-loss-target-price-11794224157187.html
- Source: Top PSU stock to buy: Brokerage sees 50% upside! Gujarat Energy shares gain 2% as profit surges 26% - Check target price — Mint Markets, 2026-11-09. https://www.livemint.com/market/stock-market-news/top-psu-stock-to-buy-brokerage-sees-50-upside-gujarat-energy-shares-gain-2-as-profit-surges-26-check-target-price-11794218975640.html
- Source: GOLDMAN SACHS DEFENDS NVIDIA WITH $300 PRICE TARGET Goldman Sachs reiterates its Buy rating on Nvidia ($NVDA ) with a $300 price target, calling the stock's risk/reward attractive following the recent AI-sector selloff. Analyst James Schneider expects Nvidia's near-term fundamentals to exceed Wall S — DeItaone, 2026-11-09. https://t.me/walter_bloomberg/38215
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.01), 2025-09-30 (d=0.01)

### [RED 4.92] equities · 2 series ↑
- dyn_indianb_ns [EQUITIES]: last 933.70, z20 4.09, zc 0.51, resid-z -0.16 [quiet], 1d 3.51%, |z20|=4.09
- dyn_karurvysya_ns [EQUITIES]: last 370.00, z20 2.01, zc 1.01, resid-z 0.92 [quiet], 1d -0.01%, |z20|=2.01; 1y-pct=99
- **Mechanism**: equities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.609 via dyn_indianb_ns, z 2.09, reacted); dyn_jiofin_bo (rho 0.577 via dyn_indianb_ns, z 2.18, reacted); dyn_bajfinance_ns (rho 0.521 via dyn_indianb_ns, z 2.28, reacted); nifty_50 (rho 0.498 via dyn_indianb_ns, z 2.81, reacted); dyn_muthootfin_ns (rho 0.489 via dyn_indianb_ns, z 2.64, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.609, z 2.09); dyn_jiofin_bo (rho 0.577, z 2.18); dyn_bajfinance_ns (rho 0.521, z 2.28); nifty_50 (rho 0.498, z 2.81)
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-04 (d=0.46), 2025-02-01 (d=0.51)

### [RED 4.84] dyn_nvda ↓
- dyn_nvda [EQUITIES]: last 178.60, z20 -2.84, zc 0.60, resid-z 0.97 [quiet], 1d -4.31%, |z20|=2.84
- **Mechanism**: dyn_nvda ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.699 vs dyn_nvda, historically leads by 4d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.666 vs dyn_nvda, historically leads by 4d
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.656 vs dyn_nvda, historically leads by 4d
- Watch next: vix (inverse) — not yet - watch; rho -0.647 vs dyn_nvda, historically leads by 4d
- Source: As Nvidia’s stock falls, here’s what Wall Street has to say about the Jensen Huang scandal — MarketWatch Top, 2026-11-09. https://www.marketwatch.com/story/how-wall-street-is-reacting-to-the-news-of-nvidias-jensen-huang-investigation-into-spy-claims-d8c839ab?mod=mw_rss_topstories
- Source: Are AMD and Broadcom the real winners of the Nvidia spy scandal? — MarketWatch Top, 2026-11-09. https://www.marketwatch.com/story/are-amd-and-broadcom-the-real-winners-of-the-nvidia-spy-scandal-d2343072?mod=mw_rss_topstories
- Source: Wall Street bounces back from AI sell-off, Nasdaq rallies over 3%, but Nvidia plunges 9% on Jensen Huang controversy — Mint Markets, 2026-11-09. https://www.livemint.com/market/stock-market-news/wall-street-bounces-back-from-ai-sell-off-nasdaq-rallies-over-3-but-nvidia-plunges-9-on-jensen-huang-controversy-11794238373887.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-24 (d=0.03), 2026-05-04 (d=0.03)

## Watchlist (below surfacing floor)
rates · 2 series ↓ (4.7), dyn_tech ↑ (4.38), dyn_ohi ↑ (4.08), indices · 3 series ↑ (3.98), indices · 3 series ↓ (3.79), dyn_atherenerg_ns ↑ (3.74), vix ↑ (3.34), dyn_4417_t ↑ (3.23), asx_200 ↑ (3.0), dyn_hdb ↑ (2.94), dyn_schd ↑ (2.89), cross-asset · 2 series ↑ (2.84)

## India macro
- nifty_50: 25044.6504 (1d 0.06%, z20 2.81, flag red)
- nifty_midcap_100: 61018.6484 (1d 0.66%, z20 2.09, flag amber)
- usd_inr: 93.9200 (1d -0.57%, z20 -2.08, flag red)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4364 (1d 0.60%, z20 -1.50, flag none)
- Next India prints: AMFI SIP / MF flows T-0d · NSDL FPI flows T-0d · IMD weekly rainfall T-0d · India CPI T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 71.6 — "HSBC upgrades India to Overweight, cuts China to Neutral; Citi, Jefferies also favour Indi"
- INOXINDIA.NS (INOX INDIA LIMITED) score 71.3 — "HSBC upgrades India to Overweight, cuts China to Neutral; Citi, Jefferies also favour Indi"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 71.0 — "HSBC upgrades India to Overweight, cuts China to Neutral; Citi, Jefferies also favour Indi"
- INDIANB.NS (INDIAN BANK) score 48.8 — "CITI DOWNGRADES US STOCKS AND TECH, TURNS BULLISH ON EUROPE Citi has downgraded US equitie"
- TECHM.NS (TECH MAHINDRA LIMITED) score 39.8 — "CITIGROUP CUTS US EQUITIES TO NEUTRAL FROM OVERWEIGHT CITIGROUP CUTS GLOBAL TECHNOLOGY TO "
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.0 — "CITIGROUP CUTS US EQUITIES TO NEUTRAL FROM OVERWEIGHT CITIGROUP CUTS GLOBAL TECHNOLOGY TO "
- TECH (Bio-Techne Corp) score 39.0 — "CITIGROUP CUTS US EQUITIES TO NEUTRAL FROM OVERWEIGHT CITIGROUP CUTS GLOBAL TECHNOLOGY TO "
- BAC (Bank of America Corporation) score 33.1 — "CITI DOWNGRADES US STOCKS AND TECH, TURNS BULLISH ON EUROPE Citi has downgraded US equitie"
- TGT (Target Corporation) score 31.9 — "NVDA - NVIDIA BOARD LAUNCHES ESPIONAGE PROBE INVOLVING CEO JENSEN HUANG Nvidia IS launchin"
- HDB (HDFC Bank Limited) score 30.0 — "CITI DOWNGRADES US STOCKS AND TECH, TURNS BULLISH ON EUROPE Citi has downgraded US equitie"
- 301077.SZ (CHINASTARS) score 29.7 — "CHINA DENIES ESPIONAGE ALLEGATIONS INVOLVING NVIDIA CEO China has rejected reports that it"
- COIN (Coinbase Global, Inc.) score 28.6 — "CITIGROUP CUTS US EQUITIES TO NEUTRAL FROM OVERWEIGHT CITIGROUP CUTS GLOBAL TECHNOLOGY TO "
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 28.2 — "CITI DOWNGRADES US STOCKS AND TECH, TURNS BULLISH ON EUROPE Citi has downgraded US equitie"
- IDBI.NS (IDBI BANK LIMITED) score 28.2 — "CITI DOWNGRADES US STOCKS AND TECH, TURNS BULLISH ON EUROPE Citi has downgraded US equitie"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 28.2 — "CITI DOWNGRADES US STOCKS AND TECH, TURNS BULLISH ON EUROPE Citi has downgraded US equitie"
- OHI (Omega Healthcare Investors, In) score 28.0 — "Upcoming IPO: Veritas Finance gets Sebi nod to launch public issue – Top things for invest"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 21.7 — "Chemplast Sanmar shares jump over 11% in biggest single-day gain in 10 months as Q2 rally "
- CHKP (Check Point Software Technolog) score 21.0 — "Crude Check: Bears make their move"
- NVDA (NVIDIA Corporation) score 20.3 — "NVIDIA SAYS JENSEN HUANG WILL REMAIN CEO AMID PROBE Nvidia ($NVDA ) says CEO Jensen Huang "
- BOND (PIMCO Active Bond Exchange-Tra) score 19.1 — "India bonds could rally some more as fundamentals favour bulls"
- LTH (Life Time Group Holdings, Inc.) score 15.4 — "CITI DOWNGRADES US STOCKS AND TECH, TURNS BULLISH ON EUROPE Citi has downgraded US equitie"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 15.2 — "Upcoming IPO: Veritas Finance gets Sebi nod to launch public issue – Top things for invest"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 15.0 — "Pearl Global shares hit 52-week high ahead of dividend record date; will the rally continu"
- JIOFIN.BO (Jio Financial Services Limited) score 12.0 — "NVDA - NVIDIA DOWNGRADED TO HOLD AS $165 BILLION AI FINANCING EXPOSURE RAISES CONCERNS Ale"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 11.1 — "Upcoming IPO: Veritas Finance gets Sebi nod to launch public issue – Top things for invest"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 11.0 — "Tata Consumer Share Price Highlights: Tata Consumer Stock Price History"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 11.0 — "Tata Consumer Share Price Highlights: Tata Consumer Stock Price History"
- META (Meta) score 9.7 — "Gold vs silver vs copper vs platinum: Which metal could deliver the biggest returns in Sam"
- SCHD (Schwab US Dividend Equity ETF) score 9.4 — "Pearl Global shares hit 52-week high ahead of dividend record date; will the rally continu"
- BZ=F (Brent Crude Oil Last Day Finan) score 9.1 — "Dow Jones| Nasdaq | US Stock Market Today | Highlights: Dow rockets 1,200 pts after last w"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 7.8 — "Stocks in focus: SBI, L&T, Alkem Lab, Adani Enterprises, BEL, GRSE, BHEL, Waaree Renewable"
- RS (Reliance, Inc.) score 7.7 — "US Midterm Election results impact on oil and IT shares: Reliance, Indian Oil, TCS, Infosy"
- DEMZ (Democratic Large Cap Core ETF) score 6.7 — "Democratic Win Set to Reshuffle U.S. Energy Policy"
- JEF (Jefferies Financial Group Inc.) score 4.4 — "HSBC upgrades India to Overweight, cuts China to Neutral; Citi, Jefferies also favour Indi"
- SEPN (Septerna, Inc.) score 4.2 — "DEMOCRATS SWEEP CONGRESS. FED HIKE BETS RETREAT. Following the midterm results, December F"
- GS (Goldman Sachs Group, Inc. (The) score 3.8 — "GOLDMAN SACHS DEFENDS NVIDIA WITH $300 PRICE TARGET Goldman Sachs reiterates its Buy ratin"
- JUSTDIAL.BO (JUST DIAL LTD.) score 3.8 — "₹13 to  ₹82: This multibagger small-cap stock turns  ₹1 lakh into 6.5 lakh in just 10 mont"
- VT (Vanguard Total World Stock Ind) score 2.7 — "Gold prices may be nearing bottom as World Gold Council sees recovery signals"
- POLICYBZR.NS (PB FINTECH LIMITED) score 0.4 — "Broker’s call: PB Fintech (Buy)"
- SWIGGY.NS (SWIGGY LIMITED) score 0.2 — "Swiggy shares jump 5% a day after Q2 results sparked a 17% crash. Why brokerages remain bu"

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