"""Streamlit board — terminal view (v3 visual pass, Block A).

Presentation only. Reads the proven data layer:
  - engine.build_snapshot()  → metric state + flags (over data/prices.csv)
  - release_calendar.build_calendar() → countdown
  - data/digest_latest.txt   → assembled morning digest
  - data/prices.csv          → trailing values for sparklines (read here, not via
                               the engine, to avoid touching engine.py)

Design: dense dark terminal. Red/amber are used ONLY for flags — nothing
decorative. Calm rows are monochrome so a flag is the loudest thing on screen.
All numeric values render in a monospace, tabular-figures font.

Run: streamlit run app.py
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import pandas as pd
import streamlit as st

from config import MARKETS
from digest import CHAT_PROMPT
from engine import build_snapshot
from release_calendar import build_calendar

DATA_DIR = Path(__file__).parent / "data"
FETCH_LOG = DATA_DIR / "fetch_log.json"
DIGEST_TXT = DATA_DIR / "digest_latest.txt"
PRICES_CSV = DATA_DIR / "prices.csv"

# ── palette ────────────────────────────────────────────────────────────
# Strong colours (RED, AMBER) are reserved exclusively for flags.
BG      = "#0b0d10"
PANEL   = "#14171c"
TEXT    = "#d8dde3"
MUT     = "#8b949e"   # secondary / labels
DIM     = "#5c636d"   # calm sparkline, calm dots
ACCENT  = "#5a7ea6"   # the one structural accent
GRIDLN  = "#1b1f26"
HEADLN  = "#2a2f37"
RED     = "#e5484d"
AMBER   = "#e0a83b"

MONO = "'JetBrains Mono','SF Mono','Menlo','Consolas',ui-monospace,monospace"

# Key cross-market series for the headline strip.
HEADLINE_IDS = [
    "nifty_50", "midcap_largecap_ratio", "usd_inr", "ust_10y",
    "dxy", "brent", "comex_gold", "gold_silver_ratio",
]
SPARK_WINDOW = 40  # sessions of trend (inside the 20–60d band)

st.set_page_config(page_title="Transmission Layer", layout="wide")

# ── global CSS: density + monospace numerics + terminal tables ─────────
st.markdown(f"""
<style>
  .block-container {{ padding-top: 1.4rem; padding-bottom: 2rem; max-width: 100%; }}
  [data-testid="stVerticalBlock"] {{ gap: 0.45rem; }}
  h1, h2, h3 {{ letter-spacing: .3px; }}
  .tl-title {{ font-size: 20px; font-weight: 700; color: {TEXT};
               border-bottom: 1px solid {HEADLN}; padding-bottom: 4px; margin-bottom: 2px; }}
  .tl-sub {{ color: {MUT}; font-size: 12px; margin-bottom: 10px; }}
  .sec {{ color: {ACCENT}; font-size: 11px; font-weight: 700; text-transform: uppercase;
          letter-spacing: 1px; margin: 14px 0 4px; border-bottom: 1px solid {GRIDLN};
          padding-bottom: 3px; }}
  .mono {{ font-family: {MONO}; font-variant-numeric: tabular-nums; }}

  /* headline strip */
  .strip {{ display: flex; flex-wrap: wrap; gap: 6px; margin: 2px 0 6px; }}
  .cell {{ background: {PANEL}; border: 1px solid {GRIDLN}; border-left: 2px solid {HEADLN};
           padding: 5px 11px; min-width: 104px; }}
  .cell .lbl {{ color: {MUT}; font-size: 10px; text-transform: uppercase; letter-spacing: .5px; }}
  .cell .val {{ font-family: {MONO}; font-variant-numeric: tabular-nums; font-size: 15px; color: {TEXT}; }}
  .cell .chg {{ font-family: {MONO}; font-variant-numeric: tabular-nums; font-size: 11px; color: {MUT}; }}
  .cell.red   {{ border-left-color: {RED}; }}
  .cell.amber {{ border-left-color: {AMBER}; }}

  /* terminal tables */
  table.tl {{ border-collapse: collapse; width: 100%; }}
  table.tl th {{ color: {MUT}; font-size: 10px; font-weight: 600; text-transform: uppercase;
                 letter-spacing: .5px; text-align: right; padding: 3px 9px;
                 border-bottom: 1px solid {HEADLN}; white-space: nowrap; }}
  table.tl td {{ font-size: 12.5px; padding: 2px 9px; border-bottom: 1px solid {GRIDLN};
                 text-align: right; white-space: nowrap; color: {TEXT}; }}
  table.tl td.l, table.tl th.l {{ text-align: left; }}
  table.tl td.c {{ text-align: center; padding: 0 6px; }}
  table.tl td.num {{ font-family: {MONO}; font-variant-numeric: tabular-nums; }}
  table.tl td.note {{ text-align: left; color: {MUT}; font-size: 11px; }}
  table.tl td.id {{ text-align: left; color: {TEXT}; }}
  table.tl a {{ color: {ACCENT}; text-decoration: none; }}
  table.tl a:hover {{ text-decoration: underline; }}
  .spark {{ display: block; }}

  .calm {{ color: {DIM}; border: 1px dashed {GRIDLN}; padding: 12px; text-align: center;
           font-size: 13px; letter-spacing: .3px; }}
  .recent {{ border-left: 2px solid {ACCENT}; background: {PANEL}; padding: 6px 12px;
             margin-bottom: 8px; font-size: 12px; }}
  .recent a {{ color: {ACCENT}; text-decoration: none; }}
  .metastrip {{ color: {MUT}; font-size: 11px; margin: 2px 0 4px; font-family: {MONO}; }}
  .metastrip b {{ color: {TEXT}; }}
</style>
""", unsafe_allow_html=True)


# ── formatting helpers ─────────────────────────────────────────────────
def _fmt(v, dp: int = 2, suffix: str = "") -> str:
    if v is None:
        return "·"
    try:
        if isinstance(v, float) and math.isnan(v):
            return "·"
        return f"{v:.{dp}f}{suffix}"
    except (TypeError, ValueError):
        return "·"


def _flag_color(flag: str) -> str:
    return {"red": RED, "amber": AMBER}.get(flag, DIM)


def _flag_dot(flag: str) -> str:
    glyph = {"red": "●", "amber": "●", "none": "·", "missing": "×"}.get(flag, "·")
    return f'<span style="color:{_flag_color(flag)}">{glyph}</span>'


def _row_bg(flag: str) -> str:
    if flag == "red":
        return "background:rgba(229,72,77,0.10);"
    if flag == "amber":
        return "background:rgba(224,168,59,0.08);"
    return ""


def _spark(vals: list[float], flag: str, w: int = 96, h: int = 20) -> str:
    """Tiny SVG sparkline; stroke tinted by flag (calm = muted grey)."""
    clean = [v for v in vals if v is not None and not (isinstance(v, float) and math.isnan(v))]
    color = _flag_color(flag)
    if len(clean) < 2:
        return f'<svg class="spark" width="{w}" height="{h}"></svg>'
    lo, hi = min(clean), max(clean)
    rng = (hi - lo) or 1.0
    n = len(clean)
    pad = 2
    pts = []
    for i, v in enumerate(clean):
        x = pad + (w - 2 * pad) * i / (n - 1)
        y = pad + (h - 2 * pad) * (1 - (v - lo) / rng)
        pts.append(f"{x:.1f},{y:.1f}")
    last_x, last_y = pts[-1].split(",")
    return (
        f'<svg class="spark" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'preserveAspectRatio="none">'
        f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" '
        f'stroke-width="1.3" stroke-linejoin="round"/>'
        f'<circle cx="{last_x}" cy="{last_y}" r="1.6" fill="{color}"/>'
        f'</svg>'
    )


@st.cache_data(show_spinner=False)
def _load_prices() -> pd.DataFrame:
    if not PRICES_CSV.exists():
        return pd.DataFrame()
    return pd.read_csv(PRICES_CSV, index_col=0, parse_dates=True).sort_index()


def _trend(prices: pd.DataFrame, sid: str) -> list[float]:
    if prices.empty or sid not in prices.columns:
        return []
    return prices[sid].dropna().tail(SPARK_WINDOW).tolist()


# ── load data ──────────────────────────────────────────────────────────
snap = build_snapshot()
prices = _load_prices()

st.markdown('<div class="tl-title">THE TRANSMISSION LAYER</div>', unsafe_allow_html=True)
st.markdown('<div class="tl-sub">continuous tier · macro anomaly board</div>', unsafe_allow_html=True)

if "error" in snap:
    st.error(snap["error"])
    st.stop()

by_id = {r["id"]: r for r in snap["series"]}
red_n = sum(1 for r in snap["series"] if r["flag"] == "red")
amber_n = sum(1 for r in snap["series"] if r["flag"] == "amber")
missing_n = sum(1 for r in snap["series"] if r["flag"] == "missing")

fetched_at = ""
if FETCH_LOG.exists():
    try:
        fetched_at = json.loads(FETCH_LOG.read_text()).get("fetched_at", "")
    except Exception:
        fetched_at = ""

st.markdown(
    f'<div class="metastrip">as of <b>{snap.get("last_data_date") or "·"}</b> · '
    f'series <b>{len(snap["series"])}</b> · '
    f'<span style="color:{RED}">red {red_n}</span> · '
    f'<span style="color:{AMBER}">amber {amber_n}</span> · '
    f'missing {missing_n} · fetch {fetched_at or "·"}</div>',
    unsafe_allow_html=True,
)


# ── 1) headline metric strip ───────────────────────────────────────────
st.markdown('<div class="sec">Headline · cross-market</div>', unsafe_allow_html=True)
cells = []
for sid in HEADLINE_IDS:
    r = by_id.get(sid)
    if not r:
        continue
    flag = r["flag"]
    cls = "cell " + (flag if flag in ("red", "amber") else "")
    dot = f' {_flag_dot(flag)}' if flag in ("red", "amber") else ""
    cells.append(
        f'<div class="{cls.strip()}">'
        f'<div class="lbl">{sid}{dot}</div>'
        f'<div class="val">{_fmt(r["last"], 2)}</div>'
        f'<div class="chg">{_fmt(r["d1_pct"], 2, "%")} · 5d {_fmt(r["d5_pct"], 2, "%")}</div>'
        f'</div>'
    )
st.markdown(f'<div class="strip">{"".join(cells)}</div>', unsafe_allow_html=True)


# ── 2) anomaly panel (prominent, high) ─────────────────────────────────
st.markdown('<div class="sec">Anomaly panel</div>', unsafe_allow_html=True)
flags = snap["flags"]
if not flags:
    st.markdown('<div class="calm">◦ No flags — calm session.</div>', unsafe_allow_html=True)
else:
    head = ('<tr><th>score</th><th>lvl</th><th class="l">type</th><th class="l">market</th>'
            '<th class="l">id</th><th>z20</th><th>last</th><th class="l">reason</th></tr>')
    body = []
    for f in flags:
        flag = f["flag"]
        body.append(
            f'<tr style="{_row_bg(flag)}">'
            f'<td class="num">{f["score"]:.2f}</td>'
            f'<td class="c">{_flag_dot(flag)}</td>'
            f'<td class="l">{f["type"]}</td>'
            f'<td class="l">{f["market"]}</td>'
            f'<td class="id">{f["id"]}</td>'
            f'<td class="num">{_fmt(f.get("z20"), 2)}</td>'
            f'<td class="num">{_fmt(f.get("last"), 2)}</td>'
            f'<td class="note">{"; ".join(f.get("reasons", []))}</td>'
            f'</tr>'
        )
    st.markdown(f'<table class="tl">{head}{"".join(body)}</table>', unsafe_allow_html=True)


# ── 3) release calendar ────────────────────────────────────────────────
st.markdown('<div class="sec">Release calendar</div>', unsafe_allow_html=True)
cal = build_calendar()

if cal["recent"]:
    links = " · ".join(
        f'<a href="{r["url"]}" target="_blank">{r["name"]}</a> ({r["released_date"]})'
        for r in cal["recent"]
    )
    st.markdown(f'<div class="recent"><b>Released &lt;24h:</b> {links}</div>', unsafe_allow_html=True)

if not cal["upcoming"]:
    st.markdown('<div class="calm">No upcoming releases computed.</div>', unsafe_allow_html=True)
else:
    head = ('<tr><th>days</th><th class="l">date</th><th class="l">release</th>'
            '<th class="l">market</th><th class="l">threshold</th><th class="l">link</th></tr>')
    body = []
    for r in cal["upcoming"]:
        soon = r["soon"]
        # "soon" uses the structural accent, NOT amber — amber is flags only.
        edge = f"border-left:2px solid {ACCENT};" if soon else "border-left:2px solid transparent;"
        dcol = ACCENT if soon else TEXT
        body.append(
            f'<tr style="{edge}">'
            f'<td class="num" style="color:{dcol}">T-{r["days_until"]}d</td>'
            f'<td class="l num">{r["next_date"]}</td>'
            f'<td class="l">{r["name"]}</td>'
            f'<td class="l" style="color:{MUT}">{r["market"]}</td>'
            f'<td class="note">{r["threshold"]}</td>'
            f'<td class="l"><a href="{r["url"]}" target="_blank">open</a></td>'
            f'</tr>'
        )
    st.markdown(f'<table class="tl">{head}{"".join(body)}</table>', unsafe_allow_html=True)
    st.markdown(f'<div class="tl-sub">Accent edge = due ≤3 days. Fixed 2026 dates '
                f'(FOMC/RBI-MPC/US CPI·PPI·PCE/OPEC) are estimates — see V2_BUILD_NOTES.md.</div>',
                unsafe_allow_html=True)


# ── 4) morning digest ──────────────────────────────────────────────────
st.markdown('<div class="sec">Morning digest</div>', unsafe_allow_html=True)
if not DIGEST_TXT.exists():
    st.markdown('<div class="calm">No digest yet — the scheduled workflow '
                'regenerates it. The app only reads the assembled file.</div>',
                unsafe_allow_html=True)
else:
    digest_text = DIGEST_TXT.read_text(encoding="utf-8")
    header = digest_text.splitlines()[0] if digest_text else ""
    st.markdown(f'<div class="tl-sub">{header.strip("= ")} · copy via the icon top-right</div>',
                unsafe_allow_html=True)
    st.code(digest_text, language="text")
    with st.expander("Chat prompt to paste with the digest"):
        st.code(CHAT_PROMPT, language="text")


# ── 5) four-market grid ────────────────────────────────────────────────
st.markdown('<div class="sec">Four-market grid</div>', unsafe_allow_html=True)
by_market: dict[str, list] = {m: [] for m in MARKETS}
for r in snap["series"]:
    by_market.setdefault(r["market"], []).append(r)


def _metric_table(rows: list[dict]) -> str:
    head = ('<tr><th class="c"></th><th class="l">series</th><th class="l">trend</th>'
            '<th>last</th><th>1d%</th><th>5d%</th><th>z20</th><th>z60</th>'
            '<th>1y%</th><th class="l">note</th></tr>')
    out = []
    for r in rows:
        flag = r["flag"]
        spark = _spark(_trend(prices, r["id"]), flag)
        out.append(
            f'<tr style="{_row_bg(flag)}">'
            f'<td class="c">{_flag_dot(flag)}</td>'
            f'<td class="id">{r["id"]}</td>'
            f'<td class="l">{spark}</td>'
            f'<td class="num">{_fmt(r["last"], 2)}</td>'
            f'<td class="num">{_fmt(r["d1_pct"], 2, "%")}</td>'
            f'<td class="num">{_fmt(r["d5_pct"], 2, "%")}</td>'
            f'<td class="num">{_fmt(r["z20"], 2)}</td>'
            f'<td class="num">{_fmt(r["z60"], 2)}</td>'
            f'<td class="num">{_fmt(r["pct_1y"], 0)}</td>'
            f'<td class="note">{"; ".join(r["reasons"]) if r["reasons"] else ""}</td>'
            f'</tr>'
        )
    return f'<table class="tl">{head}{"".join(out)}</table>'


tabs = st.tabs(MARKETS)
for tab, market in zip(tabs, MARKETS):
    with tab:
        rows = by_market.get(market, [])
        if not rows:
            st.markdown(f'<div class="calm">No series in {market}</div>', unsafe_allow_html=True)
            continue
        st.markdown(_metric_table(rows), unsafe_allow_html=True)

st.markdown(
    f'<div class="tl-sub">Flags: red |z|≥2.5 or framework+|z|≥1.5 · amber |z|≥1.5, '
    f'pct≤5/≥95, or framework · co-occurrence escalates a linked group to red. '
    f'Red/amber mark flags only; calm series are monochrome.</div>',
    unsafe_allow_html=True,
)
