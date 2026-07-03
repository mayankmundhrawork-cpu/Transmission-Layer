"""Release calendar registry — Step 4 of the spec.

Each scheduled release is structured data the calendar engine turns into a
next-occurrence countdown. No fetching happens here; the schedule rule is pure
logic evaluated against today's date.

Rule types (see release_calendar.py for the evaluator):
  monthly_day     nth calendar day of every month, rolled to the next weekday
                  if it lands on a weekend.  {"type":"monthly_day","day":12}
  weekly          a fixed weekday every week.  {"type":"weekly","weekday":4}
                  weekday: Mon=0 … Sun=6
  daily_business  every Mon–Fri.  {"type":"daily_business"}
  fixed           an explicit list of ISO dates (published schedules).
                  {"type":"fixed","dates":["2026-01-28", ...]}

FIXED-DATE MAINTENANCE: every `fixed` rule below is hardcoded for 2026 and
MUST be refreshed annually against the official published calendar. FOMC dates
are high-confidence; RBI-MPC, US CPI/PCE/PPI and OPEC dates are best-estimates
and are flagged for verification in V2_BUILD_NOTES.md.
"""

# Weekday constants for readability
MON, TUE, WED, THU, FRI = 0, 1, 2, 3, 4

RELEASES = [
    # ── INDIA ────────────────────────────────────────────────────────────
    {
        "name": "India CPI",
        "market": "INDIA",
        "rule": {"type": "monthly_day", "day": 12},
        "url": "https://www.mospi.gov.in/press-release",
        "threshold": "surprise >0.2% vs consensus",
    },
    {
        "name": "India WPI",
        "market": "INDIA",
        "rule": {"type": "monthly_day", "day": 14},
        "url": "https://eaindustry.nic.in/",
        "threshold": "any; WPI leads MCX; watch fuel & mfg sub-indices",
    },
    {
        "name": "AMFI SIP / MF flows",
        "market": "INDIA",
        "rule": {"type": "monthly_day", "day": 8},
        "url": "https://www.amfiindia.com/mutual-fund",
        "threshold": "stoppage ratio >95%; category flow skew",
    },
    {
        "name": "NSDL FPI flows",
        "market": "INDIA",
        "rule": {"type": "daily_business"},
        "url": "https://www.fpi.nsdl.co.in/web/Reports/Latest.aspx",
        "threshold": "5-session outflow >$500M sustained",
    },
    {
        "name": "RBI MPC decision",
        "market": "INDIA",
        "rule": {"type": "fixed", "dates": [
            "2026-02-06", "2026-04-08", "2026-06-05",
            "2026-08-07", "2026-10-07", "2026-12-04",
        ]},
        "url": "https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx",
        "threshold": "any; RBI/Fed differential is standing thesis",
        "verify": "RBI-MPC 2026 dates are estimates — confirm on rbi.org.in",
    },
    {
        "name": "RBI Weekly Statistical Supplement",
        "market": "INDIA",
        "rule": {"type": "weekly", "weekday": FRI},
        "url": "https://www.rbi.org.in/Scripts/WSSView.aspx",
        "threshold": "forex reserves change; liquidity posture",
    },
    {
        "name": "India trade / CAD data",
        "market": "INDIA",
        "rule": {"type": "monthly_day", "day": 15},
        "url": "https://commerce.gov.in/trade-statistics/",
        "threshold": "any print >$2B vs consensus",
    },
    {
        "name": "IMD weekly rainfall",
        "market": "INDIA",
        "rule": {"type": "weekly", "weekday": MON},
        "url": "https://mausam.imd.gov.in/",
        "threshold": "cumulative deficit direction; >10% deviation (monsoon season)",
    },
    {
        "name": "Kharif sowing data",
        "market": "INDIA",
        "rule": {"type": "weekly", "weekday": FRI},
        "url": "https://agriwelfare.gov.in/",
        "threshold": "area vs year-ago >5% (in season, Jun–Sep)",
    },

    # ── USA ──────────────────────────────────────────────────────────────
    {
        "name": "FOMC decision",
        "market": "USA",
        "rule": {"type": "fixed", "dates": [
            "2026-01-28", "2026-03-18", "2026-04-29", "2026-06-17",
            "2026-07-29", "2026-09-16", "2026-10-28", "2026-12-09",
        ]},
        "url": "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm",
        "threshold": "any; repricing since last meeting",
    },
    {
        "name": "US CPI",
        "market": "USA",
        "rule": {"type": "fixed", "dates": [
            "2026-01-13", "2026-02-11", "2026-03-11", "2026-04-10",
            "2026-05-12", "2026-06-10", "2026-07-14", "2026-08-12",
            "2026-09-11", "2026-10-13", "2026-11-13", "2026-12-10",
        ]},
        "url": "https://www.bls.gov/schedule/news_release/cpi.htm",
        "threshold": "surprise >0.2% vs consensus",
        "verify": "US CPI 2026 dates are estimates — confirm on bls.gov schedule",
    },
    {
        "name": "US PPI",
        "market": "USA",
        "rule": {"type": "fixed", "dates": [
            "2026-01-14", "2026-02-12", "2026-03-12", "2026-04-14",
            "2026-05-13", "2026-06-11", "2026-07-15", "2026-08-13",
            "2026-09-14", "2026-10-14", "2026-11-16", "2026-12-11",
        ]},
        "url": "https://www.bls.gov/schedule/news_release/ppi.htm",
        "threshold": "surprise >0.2% vs consensus",
        "verify": "US PPI 2026 dates are estimates — confirm on bls.gov schedule",
    },
    {
        "name": "US PCE",
        "market": "USA",
        "rule": {"type": "fixed", "dates": [
            "2026-01-30", "2026-02-27", "2026-03-27", "2026-04-30",
            "2026-05-29", "2026-06-26", "2026-07-31", "2026-08-28",
            "2026-09-25", "2026-10-30", "2026-11-25", "2026-12-23",
        ]},
        "url": "https://www.bea.gov/data/personal-consumption-expenditures-price-index",
        "threshold": "surprise >0.2% vs consensus",
        "verify": "US PCE 2026 dates are estimates — confirm on bea.gov schedule",
    },
    {
        "name": "EIA Weekly Petroleum Status",
        "market": "COMMODITIES",
        "rule": {"type": "weekly", "weekday": WED},
        "url": "https://www.eia.gov/petroleum/supply/weekly/",
        "threshold": "Cushing move >3M bbl vs consensus",
    },
    {
        "name": "CFTC Commitments of Traders",
        "market": "COMMODITIES",
        "rule": {"type": "weekly", "weekday": FRI},
        "url": "https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm",
        "threshold": "Producer/Merchant vs Money Mgr divergence",
    },
    {
        "name": "OPEC+ ministerial",
        "market": "COMMODITIES",
        "rule": {"type": "fixed", "dates": [
            "2026-05-31", "2026-11-30",
        ]},
        "url": "https://www.opec.org/opec_web/en/press_room/28.htm",
        "threshold": "any; check Brent backwardation vs decision",
        "verify": "OPEC+ 2026 ministerial dates are placeholders — announced ad hoc, confirm on opec.org",
    },

    # ── CHINA ────────────────────────────────────────────────────────────
    {
        "name": "China TSF / credit",
        "market": "CHINA",
        "rule": {"type": "monthly_day", "day": 15},
        "url": "http://www.pbc.gov.cn/en/3688247/index.html",
        "threshold": "MoM deceleration >10% (release window ~10th–15th, irregular)",
    },
    {
        "name": "China Mfg PMI (NBS + Caixin)",
        "market": "CHINA",
        "rule": {"type": "monthly_day", "day": 1},
        "url": "https://www.stats.gov.cn/english/",
        "threshold": "crossing 50; NBS-Caixin divergence >1.5pt",
    },
]
