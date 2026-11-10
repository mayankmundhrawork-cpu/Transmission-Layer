# Transmission Layer — board brief · 2026-11-10 12:34Z

data as of **2026-11-10** · 97 series · 13 red / 33 amber · 8 events surfaced (25 suppressed)

## Regime & assumption health (measured at generation)
- **Regime: RISK_OFF** (score 0.61, 4d in regime; vol-pct 0.82, breadth-off 0.4, Markov P(high-vol) 0.555)
- [INVERTED] **safe_haven_gold** — corr20 -0.15, corr60 -0.22, contra nifty_50 corr20=0.29, last shift 2026-06-02. Channel: risk-off safe-haven bid: vol up -> gold bid
- [VALID] **gold_silver_comove** — corr20 0.91, corr60 0.85, last shift 2026-01-30. Channel: monetary metals co-move; ratio extremes are rotations
- [WEAK] **metal_copper_channel** — corr20 0.12, corr60 0.12, last shift 2026-09-10. Channel: global copper leads Indian metal equities
- [WEAK] **inr_oil_channel** — corr20 -0.19, corr60 0.05, last shift 2026-09-08. Channel: oil up -> import bill -> INR weakens (usd_inr up)
- [INSUFFICIENT_DATA] **goi_ust_comove** — corr20 None, corr60 None. Channel: global duration transmits to GoI yields
- [VALID] **vix_equity_inverse** — corr20 -0.96, corr60 -0.91, last shift 2026-09-16. Channel: vol spike -> equity drawdown
- [WEAK] **dxy_inr_channel** — corr20 0.33, corr60 -0.01, last shift 2026-01-16. Channel: broad dollar strength -> EM FX weakness incl INR
- [WEAK] **real_rates_gold_inverse** — corr20 0.1, corr60 -0.1, last shift 2026-08-12. Channel: real yields up -> non-yielding gold down
- [VALID] **gsr_stress_gauge** — corr20 0.34, corr60 0.3, last shift 2026-07-14. Channel: gold/silver ratio rises under monetary stress

## Scan control & verified transmission setups
- FDR (BH q=0.1): **6 of 89** scanned series survive multiplicity control (effective p ≤ 0.005605629265529988)
- No live setups: drivers quiet or targets already repriced.
- Track record · residual_reversion: hit-rate **0.508** (n=1127) — |resid_z|>=2.0 -> fwd 5d return opposes residual
- Track record · transmission_follow: hit-rate **0.82** (n=2092) — first-half-significant lead pairs; driver |zc|>=1.5 on 2nd half -> target next-k cum ret matches beta-implied sign
- Track record · spread_reversion: hit-rate **0.562** (n=16) — |dev| >= 2sigma vs PIT 252d -> |dev| shrinks >=25% within max(half-life,10) sessions

## Events (ranked)

### [RED 8.23] commodities · 2 series ↓
- wti [COMMODITIES]: last 85.21, z20 -2.40, zc -0.57, resid-z 0.27 [quiet], 1d -1.89%, 1-session move -1.89% ≥ 1.5%; |z20|=2.40
- brent [COMMODITIES]: last 90.53, z20 -2.38, zc -0.63, resid-z 0.08 [quiet], 1d -2.20%, 1-session move -2.20% ≥ 1.5%; |z20|=2.38; co-occur[inr_oil] suppressed: channel WEAK
- **Mechanism**: commodities · 2 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho -0.492 via wti, z 2.64, reacted)
- Watch next: vix (co-move) — not yet - watch; rho 0.546 vs brent, historically leads by 1d
- Watch next: sp500 (inverse) — not yet - watch; rho -0.618 vs brent
- Watch next: dyn_gs (inverse) — not yet - watch; rho -0.549 vs brent
- Watch next: dyn_demz (inverse) — not yet - watch; rho -0.548 vs wti
- Watch next: dyn_vt (inverse) — not yet - watch; rho -0.506 vs wti
- **India receivers**: dyn_muthootfin_ns (rho -0.492, z 2.64)
- Source: China Is Buying Oil Again After Months of Living Off Its Stockpiles — OilPrice, 2026-11-10. https://oilprice.com/Latest-Energy-News/World-News/China-Is-Buying-Oil-Again-After-Months-of-Living-Off-Its-Stockpiles.html
- Source: U.S. Military Coordinates With Saudi Oil Tankers on Risky Hormuz Crossings — OilPrice, 2026-11-10. https://oilprice.com/Latest-Energy-News/World-News/US-Military-Coordinates-With-Saudi-Oil-Tankers-on-Risky-Hormuz-Crossings.html
- Source: Brent Crude Falls Below $90 for First Time Since August — OilPrice, 2026-11-10. https://oilprice.com/Latest-Energy-News/World-News/Brent-Crude-Falls-Below-90-for-First-Time-Since-August.html
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
- **India take**: dyn_adanient_bo (rho 0.733 via nifty_metal, z 1.06, reacted); dyn_indusindbk_bo (rho 0.632 via nifty_midcap_100, z 1.32, reacted); dyn_indianb_ns (rho 0.607 via nifty_midcap_100, z 4.09, reacted); dyn_policybzr_ns (rho 0.527 via nifty_midcap_100, z -1.36, reacted); nifty_it (rho 0.514 via nifty_50, z 0.71, quiet)
- Watch next: nifty_it (co-move) — not yet - watch; rho 0.514 vs nifty_50, historically leads by 5d
- Watch next: dyn_tatatech_ns (co-move) — not yet - watch; rho 0.505 vs dyn_jiofin_bo
- Watch next: comex_gold (co-move) — not yet - watch; rho 0.501 vs dyn_muthootfin_ns
- **India receivers**: dyn_adanient_bo (rho 0.733, z 1.06); dyn_indusindbk_bo (rho 0.632, z 1.32); dyn_indianb_ns (rho 0.607, z 4.09); dyn_policybzr_ns (rho 0.527, z -1.36)
- Source: Bajaj Finance issues 5.74 crore warrants to promoter for Rs 5,799 crore — ET Markets, 2026-11-10. https://economictimes.indiatimes.com/markets/stocks/news/bajaj-finance-issues-5-74-crore-warrants-to-promoter-for-rs-5799-crore/articleshow/135708439.cms
- Source: Mutual funds' Nifty 50 allocation falls to 21-year low — BusinessLine Mkts, 2026-11-10. https://www.thehindubusinessline.com/markets/mutual-funds-nifty-50-allocation-falls-to-21-year-low/article71685515.ece
- Source: Sensex, Nifty 50 rise over 6% in past 5 sessions: More rally from tomorrow or profit booking will dent returns hopes? — Mint Markets, 2026-11-10. https://www.livemint.com/market/stock-market-news/sensex-nifty-50-rise-over-6-in-past-5-sessions-more-rally-from-tomorrow-or-profit-booking-will-dent-returns-hopes-11794292057445.html
- Historical analogues: 2025-07-21 (d=1.08), 2025-07-11 (d=1.35), 2025-12-23 (d=1.37)

### [RED 5.88] cross-asset · 3 series ↓
- eth_usd [CRYPTO]: last 2087.88, z20 -2.56, zc -0.51, resid-z 0.51 [quiet], 1d -2.05%, |z20|=2.56
- btc_usd [CRYPTO]: last 74114.12, z20 -1.94, zc -0.61, resid-z 0.02 [quiet], 1d -1.47%, |z20|=1.94
- dyn_coin [EQUITIES]: last 136.07, z20 -1.71, zc -0.30, resid-z 0.35 [quiet], 1d 0.97%, 1y-pct=0
- **Mechanism**: cross-asset · 3 series ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.12).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.756 vs eth_usd
- Watch next: sp500 (co-move) — not yet - watch; rho 0.739 vs eth_usd
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.73 vs eth_usd
- Watch next: comex_silver (co-move) — not yet - watch; rho 0.504 vs eth_usd, historically leads by 1d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.655 vs eth_usd
- Source: FIIs may return to Indian equities as global headwinds ease and domestic fundamentals remain strong: Report — BusinessLine Mkts, 2026-11-10. https://www.thehindubusinessline.com/markets/fiis-may-return-to-indian-equities-as-global-headwinds-ease-and-domestic-fundamentals-remain-strong-report/article71685694.ece
- Source: Global stocks build on tech-fuelled rally as oil retreats: Markets Wrap — Mint Markets, 2026-11-10. https://www.livemint.com/market/stock-market-news/asian-stocks-ride-tech-rally-higher-as-oil-falls-11794291620755.html
- Source: Global equities to rely on earnings growth as investor risk appetite weakens: Goldman Sachs — BusinessLine Mkts, 2026-11-10. https://www.thehindubusinessline.com/markets/global-equities-to-rely-on-earnings-growth-as-investor-risk-appetite-weakens-goldman-sachs/article71685164.ece
- Historical analogues: 2026-05-22 (d=0.12), 2025-04-10 (d=0.52), 2025-10-16 (d=0.72)

### [RED 5.27] indices · 4 series ↑
- stoxx_50 [INDICES]: last 6364.00, z20 3.61, zc 1.14, resid-z -1.21 [quiet], 1d 1.17%, |z20|=3.61
- cac_40 [INDICES]: last 8328.33, z20 2.77, zc 1.25, resid-z -0.59 [quiet], 1d 1.15%, |z20|=2.77
- dax [INDICES]: last 26583.03, z20 2.43, zc 0.94, resid-z -2.23 [unexplained], 1d 1.20%, |z20|=2.43; 1y-pct=100
- ftse_100 [INDICES]: last 10836.08, z20 1.54, zc 0.55, resid-z -0.86 [quiet], 1d 0.49%, |z20|=1.54
- **Mechanism**: indices · 4 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: dyn_muthootfin_ns (rho 0.529 via cac_40, z 2.64, reacted); nifty_midcap_100 (rho 0.489 via dax, z 2.09, reacted); nifty_fmcg (rho 0.476 via cac_40, z 1.91, reacted); dyn_jiofin_bo (rho 0.455 via cac_40, z 2.18, reacted); dyn_tataelxsi_ns (rho 0.446 via ftse_100, z 0.96, quiet)
- Watch next: dyn_gs (co-move) — not yet - watch; rho 0.592 vs stoxx_50, historically leads by 5d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.541 vs stoxx_50, historically leads by 5d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.507 vs stoxx_50, historically leads by 5d
- **India receivers**: dyn_muthootfin_ns (rho 0.529, z 2.64); nifty_midcap_100 (rho 0.489, z 2.09); nifty_fmcg (rho 0.476, z 1.91); dyn_jiofin_bo (rho 0.455, z 2.18)
- Historical analogues: 2026-07-10 (d=0.0), 2025-04-16 (d=0.34), 2026-03-31 (d=0.71)

### [RED 5.18] dyn_tgt ↑
- dyn_tgt [EQUITIES]: last 165.90, z20 3.18, zc 0.14, resid-z 0.20 [quiet], 1d 4.73%, |z20|=3.18; 1y-pct=99
- **Mechanism**: dyn_tgt ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: dyn_schd (co-move) — not yet - watch; rho 0.646 vs dyn_tgt, historically leads by 4d
- Watch next: dow_jones (co-move) — not yet - watch; rho 0.506 vs dyn_tgt
- Source: Balrampur Chini Mills shares: Over 50% returns in 1 year, sugar stock in focus with new  ₹3100 cr plant - check target — Mint Markets, 2026-11-10. https://www.livemint.com/market/stock-market-news/balrampur-chini-mills-shares-over-50-returns-in-1-year-sugar-stock-in-focus-with-new-rs-3100-cr-plant-check-target-11794306339768.html
- Source: Data Patterns shares surge 55% in 2026: Should you buy stock after Q2 results? What brokerages say: check target price — Mint Markets, 2026-11-10. https://www.livemint.com/market/stock-market-news/data-patterns-shares-surge-55-in-2026-should-you-buy-stock-after-q2-results-what-brokerages-say-check-target-price-11794290061612.html
- Source: TCPL Packaging shares: High-conviction stock! 60% returns in 6 months, InCred sees 18% more gain | Check target price — Mint Markets, 2026-11-10. https://www.livemint.com/market/stock-market-news/tcpl-packaging-shares-incred-equities-recommends-this-high-conviction-stock-with-18-upside-check-target-returns-11794287696958.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.01), 2025-09-30 (d=0.01)

### [RED 4.94] dyn_hdb ↑
- dyn_hdb [EQUITIES]: last 25.81, z20 2.94, zc 0.92, resid-z 1.20 [quiet], 1d 2.67%, |z20|=2.94
- **Mechanism**: dyn_hdb ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_50 (rho 0.38 via dyn_hdb, z 2.81, reacted); dyn_muthootfin_ns (rho 0.36 via dyn_hdb, z 2.64, reacted)
- **India receivers**: nifty_50 (rho 0.38, z 2.81); dyn_muthootfin_ns (rho 0.36, z 2.64)
- Source: Retail investors shed stocks, but crowd into Reliance, HDFC Bank — Mint Markets, 2026-11-10. https://www.livemint.com/market/stock-market-news/retail-investors-reliance-hdfc-bank-fpis-stock-markets-india-11794288650697.html
- Historical analogues: 2026-05-22 (d=0.0), 2025-05-14 (d=0.04), 2025-08-21 (d=0.05)

### [RED 4.92] equities · 2 series ↑
- dyn_indianb_ns [EQUITIES]: last 933.70, z20 4.09, zc 0.51, resid-z -0.16 [quiet], 1d 3.51%, |z20|=4.09
- dyn_karurvysya_ns [EQUITIES]: last 370.00, z20 2.01, zc 1.01, resid-z 0.92 [quiet], 1d -0.01%, |z20|=2.01; 1y-pct=99
- **Mechanism**: equities · 2 series ↑: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-07-10 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: nifty_midcap_100 (rho 0.607 via dyn_indianb_ns, z 2.09, reacted); dyn_jiofin_bo (rho 0.578 via dyn_indianb_ns, z 2.18, reacted); dyn_bajfinance_ns (rho 0.519 via dyn_indianb_ns, z 2.28, reacted); nifty_50 (rho 0.496 via dyn_indianb_ns, z 2.81, reacted); dyn_muthootfin_ns (rho 0.491 via dyn_indianb_ns, z 2.64, reacted)
- **India receivers**: nifty_midcap_100 (rho 0.607, z 2.09); dyn_jiofin_bo (rho 0.578, z 2.18); dyn_bajfinance_ns (rho 0.519, z 2.28); nifty_50 (rho 0.496, z 2.81)
- Historical analogues: 2026-07-10 (d=0.0), 2025-07-04 (d=0.46), 2025-02-01 (d=0.51)

### [RED 4.84] dyn_nvda ↓
- dyn_nvda [EQUITIES]: last 178.60, z20 -2.84, zc 0.60, resid-z 0.97 [quiet], 1d -4.31%, |z20|=2.84
- **Mechanism**: dyn_nvda ↓: correlated cluster flagged by the engine. Mechanism narrative unassessed (LLM off). Nearest historical analogue: 2026-05-22 (z-distance 0.0).
- **Gap**: Unassessed (LLM off) — laggard list above is the live math.
- **India take**: No exposed Indian receivers above the correlation floor.
- Watch next: sp500 (co-move) — not yet - watch; rho 0.699 vs dyn_nvda, historically leads by 4d
- Watch next: dyn_vt (co-move) — not yet - watch; rho 0.662 vs dyn_nvda, historically leads by 4d
- Watch next: vix (inverse) — not yet - watch; rho -0.655 vs dyn_nvda, historically leads by 4d
- Watch next: dyn_demz (co-move) — not yet - watch; rho 0.653 vs dyn_nvda, historically leads by 4d
- Source: Nvidia in Crisis! China Spy Allegations, FBI Probe, shares crash, more: Key things investors should know - Still a buy? — Mint Markets, 2026-11-10. https://www.livemint.com/market/stock-market-news/nvidia-in-crisis-china-spy-allegations-fbi-probe-shares-crash-more-key-things-investors-should-know-still-a-buy-11794309541206.html
- Source: Jensen Huang scandal: Nvidia shares rebound in premarket after sharp sell-off, $1.57 trillion in market value wiped out — Mint Markets, 2026-11-10. https://www.livemint.com/market/stock-market-news/huangs-affair-nvidia-shares-rebound-in-premarket-trade-after-sharp-sell-off-1-57-trillion-in-market-value-wiped-out-11794304912609.html
- Source: The short seller who saw signs of Nvidia’s China scandal months ago claims Megaspeed isn’t the only company helping China access chips — MarketWatch Top, 2026-11-10. https://www.marketwatch.com/story/the-short-seller-who-saw-signs-of-nvidias-china-scandal-months-ago-claims-megaspeed-isnt-the-ony-company-helping-china-access-chips-9877f544?mod=mw_rss_topstories
- Historical analogues: 2026-05-22 (d=0.0), 2025-04-24 (d=0.03), 2026-05-04 (d=0.03)

## Watchlist (below surfacing floor)
rates · 2 series ↓ (4.7), dyn_tech ↑ (4.38), usd_inr ↓ (4.36), dyn_ohi ↑ (4.08), natgas ↑ (3.75), dyn_atherenerg_ns ↑ (3.74), dyn_lth ↑ (3.54), dyn_4417_t ↑ (3.12), asx_200 ↑ (3.04), dyn_schd ↑ (2.89), cross-asset · 2 series ↑ (2.84), dyn_havells_ns ↑ (2.52)

## India macro
- nifty_50: 25044.6504 (1d 0.06%, z20 2.81, flag red)
- nifty_midcap_100: 61018.6484 (1d 0.66%, z20 2.09, flag amber)
- usd_inr: 93.9180 (1d 0.02%, z20 -2.36, flag amber)
- goi_10y: 7.0600 (1d 3.22%, z20 1.84, flag none)
- india_cpi_yoy: 2.9518 (1d 14.13%, z20 n/a, flag none)
- goi_ust_spread: 2.2700 (1d -1.30%, z20 n/a, flag none)
- midcap_largecap_ratio: 2.4364 (1d 0.60%, z20 -1.50, flag none)
- Next India prints: NSDL FPI flows T-0d · India CPI T-2d · RBI Weekly Statistical Supplement T-3d · Kharif sowing data T-3d

## News-tracked universe (why each is watched)
- COALINDIA.NS (COAL INDIA LTD) score 74.0 — "US ETFs to Buy for Samvat 2083: Samco recommends 2 ETFs  with potential upside of up to 60"
- INOXINDIA.NS (INOX INDIA LIMITED) score 72.7 — "US ETFs to Buy for Samvat 2083: Samco recommends 2 ETFs  with potential upside of up to 60"
- HAVELLS.NS (HAVELLS INDIA LIMITED) score 72.5 — "US ETFs to Buy for Samvat 2083: Samco recommends 2 ETFs  with potential upside of up to 60"
- INDIANB.NS (INDIAN BANK) score 50.9 — "Anthropic retracts details of $69 billion IPO filing sent to bankers. Why analysts are rai"
- TECHM.NS (TECH MAHINDRA LIMITED) score 40.0 — "NSE deploys liquid cooling technology for AI infrastructure, targets 224-GPU capacity"
- CARTRADE.NS (CARTRADE TECH LIMITED) score 39.3 — "NSE deploys liquid cooling technology for AI infrastructure, targets 224-GPU capacity"
- TECH (Bio-Techne Corp) score 39.3 — "NSE deploys liquid cooling technology for AI infrastructure, targets 224-GPU capacity"
- 301077.SZ (CHINASTARS) score 37.7 — "India launches probe into dumping of aluminium products from China, Malaysia, Vietnam"
- BAC (Bank of America Corporation) score 35.1 — "Anthropic retracts details of $69 billion IPO filing sent to bankers. Why analysts are rai"
- TGT (Target Corporation) score 35.1 — "ANTHROPIC TARGETS RECORD-BREAKING $69.3 BILLION IPO Anthropic is seeking to raise up to $6"
- OHI (Omega Healthcare Investors, In) score 31.7 — "US ETFs to Buy for Samvat 2083: Samco recommends 2 ETFs  with potential upside of up to 60"
- HDB (HDFC Bank Limited) score 31.4 — "Anthropic retracts details of $69 billion IPO filing sent to bankers. Why analysts are rai"
- INDUSINDBK.BO (INDUSIND BANK LTD.) score 29.8 — "Anthropic retracts details of $69 billion IPO filing sent to bankers. Why analysts are rai"
- IDBI.NS (IDBI BANK LIMITED) score 29.7 — "Anthropic retracts details of $69 billion IPO filing sent to bankers. Why analysts are rai"
- KARURVYSYA.NS (KARUR VYSYA BANK LTD) score 29.7 — "Anthropic retracts details of $69 billion IPO filing sent to bankers. Why analysts are rai"
- COIN (Coinbase Global, Inc.) score 29.1 — "Global equities to rely on earnings growth as investor risk appetite weakens: Goldman Sach"
- CHKP (Check Point Software Technolog) score 24.5 — "HUL dividend 2026: Tomorrow is the last day to buy | Check payout amount, record date, his"
- NVDA (NVIDIA Corporation) score 24.5 — "Jensen Huang scandal: Nvidia shares rebound in premarket after sharp sell-off, $1.57 trill"
- ATHERENERG.NS (ATHER ENERGY LIMITED) score 22.9 — "ADNOC Gas Posts Stunning Profit Recovery as Energy Exports Rebound"
- BOND (PIMCO Active Bond Exchange-Tra) score 19.7 — "Easing oil, bond yields to support bank margins, RBI rate hikes likely in Dec: Jefferies"
- LTH (Life Time Group Holdings, Inc.) score 16.5 — "Asian stocks gain as Wall Street tech rally lifts investor sentiment"
- BAJFINANCE.NS (BAJAJ FINANCE LIMITED) score 15.4 — "Upcoming IPOs: SEBI clears 8 issues, including Mahanadi Coalfields, Veritas Finance and Sa"
- 4417.T (GLOBAL SECURITY EXPERTS INC) score 14.2 — "Gold rates today 10 Nov Tuesday: Can price rise to  ₹1.48 lakh per 10 gm? What experts say"
- SCHD (Schwab US Dividend Equity ETF) score 13.2 — "HUL dividend 2026: Tomorrow is the last day to buy | Check payout amount, record date, his"
- MUTHOOTFIN.NS (MUTHOOT FINANCE LIMITED) score 11.8 — "Upcoming IPOs: SEBI clears 8 issues, including Mahanadi Coalfields, Veritas Finance and Sa"
- TATAELXSI.NS (TATA ELXSI LIMITED) score 10.7 — "Tata Steel’s domestic business shines in Q2; Netherlands uncertainty poses risk"
- TATATECH.NS (TATA TECHNOLOGIES LIMITED) score 10.7 — "Tata Steel’s domestic business shines in Q2; Netherlands uncertainty poses risk"
- JIOFIN.BO (Jio Financial Services Limited) score 10.6 — "NVDA - NVIDIA DOWNGRADED TO HOLD AS $165 BILLION AI FINANCING EXPOSURE RAISES CONCERNS Ale"
- BZ=F (Brent Crude Oil Last Day Finan) score 9.9 — "HUL dividend 2026: Tomorrow is the last day to buy | Check payout amount, record date, his"
- RS (Reliance, Inc.) score 8.7 — "AMFI Rejig: Reliance's Jio Platforms, NSE, Lenskart, LG among 7 stocks set for large cap u"
- META (Meta) score 8.6 — "Gold vs silver vs copper vs platinum: Which metal could deliver the biggest returns in Sam"
- ADANIENT.BO (ADANI ENTERPRISES LTD.) score 6.9 — "Stocks in focus: SBI, L&T, Alkem Lab, Adani Enterprises, BEL, GRSE, BHEL, Waaree Renewable"
- DEMZ (Democratic Large Cap Core ETF) score 5.9 — "Democratic Win Set to Reshuffle U.S. Energy Policy"
- JEF (Jefferies Financial Group Inc.) score 5.8 — "Easing oil, bond yields to support bank margins, RBI rate hikes likely in Dec: Jefferies"
- GS (Goldman Sachs Group, Inc. (The) score 5.4 — "Global equities to rely on earnings growth as investor risk appetite weakens: Goldman Sach"
- SEPN (Septerna, Inc.) score 4.7 — "Promoter shareholding in listed companies hits three-year high at 41.93% in September quar"
- JUSTDIAL.BO (JUST DIAL LTD.) score 4.4 — "Actor Justin Baldoni quietly sold his L.A. home for $2.1 million after moving to Nashville"
- VT (Vanguard Total World Stock Ind) score 3.3 — "JENSEN HUANG IS SCHEDULED TO ATTEND SEMAFOR’S SILICON VALLEY & THE WORLD, SOURCE SAYS"
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