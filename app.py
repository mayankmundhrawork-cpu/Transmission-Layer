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
import plotly.graph_objects as go
import streamlit as st

from config import LINKED_GROUPS, MARKETS
from digest import CHAT_PROMPT
# Threshold/window constants imported (read-only) so the chart's z-band and
# historical flag markers stay consistent with the engine. Engine logic itself
# is not touched.
from engine import AMBER_Z, RED_Z, Z_WIN_SHORT, build_snapshot
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

  /* anomaly panel — centrepiece cards */
  .anom {{ display: flex; align-items: center; gap: 14px; background: {PANEL};
           border: 1px solid {GRIDLN}; border-left: 3px solid {HEADLN};
           padding: 9px 15px; margin-bottom: 5px; }}
  .anom.red   {{ border-left-color: {RED};   background: rgba(229,72,77,0.07); }}
  .anom.amber {{ border-left-color: {AMBER}; background: rgba(224,168,59,0.06); }}
  .anom .score {{ font-family: {MONO}; font-variant-numeric: tabular-nums;
                  font-size: 21px; color: {TEXT}; min-width: 54px; text-align: right; }}
  .anom .body {{ flex: 1; min-width: 0; }}
  .anom .aid {{ font-size: 14px; color: {TEXT}; }}
  .anom .aid .mk {{ color: {MUT}; font-size: 11px; margin-left: 7px;
                    text-transform: uppercase; letter-spacing: .4px; }}
  .anom .reason {{ color: {MUT}; font-size: 11.5px; margin-top: 2px; }}
  .anom .metrics {{ font-family: {MONO}; font-variant-numeric: tabular-nums;
                    font-size: 11px; color: {MUT}; white-space: nowrap; text-align: right; }}
  .cooc-members {{ display: flex; gap: 22px; margin-top: 7px; flex-wrap: wrap; }}
  .member .mid {{ font-size: 11px; color: {TEXT}; }}
  .member .mz {{ font-family: {MONO}; font-variant-numeric: tabular-nums;
                 font-size: 10px; color: {MUT}; }}
  .calm-sub {{ font-size: 11px; color: {DIM}; margin-top: 7px; letter-spacing: .2px; }}
  .drill-cap {{ color: {MUT}; font-size: 11px; margin: 2px 0 6px; }}
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


# ── drill-down chart (Plotly) ──────────────────────────────────────────
CHART_WINDOW = 252   # sessions shown (zoomable); rolling stats warm up on full history
PLOT_FONT = "Consolas, Menlo, monospace"


def _z_series(s: pd.Series):
    """Rolling z-score matching engine semantics: today vs the PRIOR 20d window."""
    m = s.shift(1).rolling(Z_WIN_SHORT).mean()
    sd = s.shift(1).rolling(Z_WIN_SHORT).std(ddof=0)
    z = (s - m) / sd
    return z, m, sd


def _drilldown_fig(sid: str, cur_flag: str) -> go.Figure:
    s_full = prices[sid].dropna()
    z_full, mean_full, sd_full = _z_series(s_full)

    disp = s_full.tail(CHART_WINDOW)
    idx = disp.index
    price = disp
    mean = mean_full.reindex(idx)
    sd = sd_full.reindex(idx)
    z = z_full.reindex(idx)
    ma20 = s_full.rolling(Z_WIN_SHORT).mean().reindex(idx)
    ma50 = s_full.rolling(50).mean().reindex(idx)
    rng_hi = s_full.rolling(Z_WIN_SHORT).max().reindex(idx)
    rng_lo = s_full.rolling(Z_WIN_SHORT).min().reindex(idx)

    fig = go.Figure()

    # z-bands (amber = ±1.5σ, red = ±2.5σ) — amber/red only, they ARE the flag levels
    fig.add_trace(go.Scatter(x=idx, y=mean + RED_Z * sd, line=dict(width=0),
                             showlegend=False, hoverinfo="skip"))
    fig.add_trace(go.Scatter(x=idx, y=mean - RED_Z * sd, fill="tonexty",
                             fillcolor="rgba(229,72,77,0.05)", line=dict(width=0),
                             name="±2.5σ (red)", hoverinfo="skip"))
    fig.add_trace(go.Scatter(x=idx, y=mean + AMBER_Z * sd, line=dict(width=0),
                             showlegend=False, hoverinfo="skip"))
    fig.add_trace(go.Scatter(x=idx, y=mean - AMBER_Z * sd, fill="tonexty",
                             fillcolor="rgba(224,168,59,0.07)", line=dict(width=0),
                             name="±1.5σ (amber)", hoverinfo="skip"))

    # 20d range envelope + mean
    fig.add_trace(go.Scatter(x=idx, y=rng_hi, line=dict(color=ACCENT, width=0.7, dash="dot"),
                             name="20d high/low", hoverinfo="skip"))
    fig.add_trace(go.Scatter(x=idx, y=rng_lo, line=dict(color=ACCENT, width=0.7, dash="dot"),
                             showlegend=False, hoverinfo="skip"))
    fig.add_trace(go.Scatter(x=idx, y=mean, line=dict(color=MUT, width=1, dash="dash"),
                             name="20d mean", hoverinfo="skip"))

    # moving averages
    fig.add_trace(go.Scatter(x=idx, y=ma20, line=dict(color="#6aa0c8", width=1), name="MA20"))
    fig.add_trace(go.Scatter(x=idx, y=ma50, line=dict(color="#7d8590", width=1), name="MA50"))

    # price
    fig.add_trace(go.Scatter(
        x=idx, y=price, line=dict(color=TEXT, width=1.6), name=sid, customdata=z,
        hovertemplate="%{x|%Y-%m-%d}<br>" + sid + " %{y:.2f}<br>z=%{customdata:.2f}<extra></extra>",
    ))

    # historical flag markers (recomputed in presentation layer, engine thresholds)
    za = z.abs()
    amber_mask = (za >= AMBER_Z) & (za < RED_Z)
    red_mask = za >= RED_Z
    if amber_mask.any():
        fig.add_trace(go.Scatter(x=idx[amber_mask], y=price[amber_mask], mode="markers",
                                 marker=dict(color=AMBER, size=5), name="amber flag",
                                 hovertemplate="%{x|%Y-%m-%d} amber<extra></extra>"))
    if red_mask.any():
        fig.add_trace(go.Scatter(x=idx[red_mask], y=price[red_mask], mode="markers",
                                 marker=dict(color=RED, size=6), name="red flag",
                                 hovertemplate="%{x|%Y-%m-%d} red<extra></extra>"))

    # current break (latest point), ringed in the current flag colour
    last_color = {"red": RED, "amber": AMBER}.get(cur_flag, ACCENT)
    fig.add_trace(go.Scatter(
        x=[idx[-1]], y=[price.iloc[-1]], mode="markers",
        marker=dict(color="rgba(0,0,0,0)", size=13, symbol="circle",
                    line=dict(width=2, color=last_color)),
        name="latest", hovertemplate="latest %{y:.2f}<extra></extra>",
    ))

    fig.update_layout(
        template="plotly_dark", height=400,
        paper_bgcolor=BG, plot_bgcolor=BG,
        font=dict(family=PLOT_FONT, color=TEXT, size=11),
        margin=dict(l=44, r=12, t=28, b=28), hovermode="x unified",
        legend=dict(orientation="h", yanchor="bottom", y=1.0, x=0,
                    font=dict(size=9), bgcolor="rgba(0,0,0,0)"),
        xaxis=dict(gridcolor=GRIDLN, zeroline=False),
        yaxis=dict(gridcolor=GRIDLN, zeroline=False),
    )
    return fig


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


# ── 2) anomaly panel — the centrepiece ─────────────────────────────────
st.markdown('<div class="sec">◈ Anomaly panel</div>', unsafe_allow_html=True)
flags = snap["flags"]


def _anom_card(f: dict) -> str:
    flag = f["flag"]
    dot = _flag_dot(flag)
    reasons = "; ".join(f.get("reasons", []))
    if f["type"] == "co-occurrence":
        members = []
        for mid in LINKED_GROUPS.get(f["id"], []):
            r = by_id.get(mid)
            if not r:
                continue
            sp = _spark(_trend(prices, mid), r["flag"], w=118, h=26)
            members.append(
                f'<div class="member"><div class="mid">{_flag_dot(r["flag"])} {mid}</div>'
                f'{sp}<div class="mz">z {_fmt(r["z20"], 2)} · {_fmt(r["last"], 2)}</div></div>'
            )
        return (
            f'<div class="anom {flag}"><div class="score">{f["score"]:.2f}</div>'
            f'<div class="body"><div class="aid">{dot} {f["id"]}'
            f'<span class="mk">cross · co-occurrence</span></div>'
            f'<div class="reason">{reasons}</div>'
            f'<div class="cooc-members">{"".join(members)}</div></div></div>'
        )
    sp = _spark(_trend(prices, f["id"]), flag, w=150, h=28)
    return (
        f'<div class="anom {flag}"><div class="score">{f["score"]:.2f}</div>'
        f'<div class="body"><div class="aid">{dot} {f["id"]}'
        f'<span class="mk">{f["market"]} · {f["type"]}</span></div>'
        f'<div class="reason">{reasons}</div></div>'
        f'<div>{sp}</div>'
        f'<div class="metrics">z {_fmt(f.get("z20"), 2)}<br>{_fmt(f.get("last"), 2)}</div></div>'
    )


if not flags:
    st.markdown(
        f'<div class="calm">◦ No flags — calm session.'
        f'<div class="calm-sub">{len(snap["series"])} series tracked · all within normal range · '
        f'an empty panel is the correct resting state</div></div>',
        unsafe_allow_html=True,
    )
else:
    st.markdown("".join(_anom_card(f) for f in flags), unsafe_allow_html=True)


# ── 2b) drill-down chart ───────────────────────────────────────────────
st.markdown('<div class="sec">Drill-down</div>', unsafe_allow_html=True)
chartable = [r["id"] for r in snap["series"] if r["id"] in prices.columns]
if not chartable:
    st.markdown('<div class="calm">No price history available to chart.</div>',
                unsafe_allow_html=True)
else:
    # default to the top-ranked flagged series that is chartable
    default_id = next((f["id"] for f in flags if f["id"] in chartable), chartable[0])
    sel = st.selectbox("series", chartable,
                       index=chartable.index(default_id),
                       label_visibility="collapsed")
    st.markdown('<div class="drill-cap">price · MA20/50 · 20d mean &amp; range · '
                'amber ±1.5σ / red ±2.5σ z-bands · markers where flags fired · '
                'ringed latest point. Zoom + hover enabled.</div>',
                unsafe_allow_html=True)
    st.plotly_chart(_drilldown_fig(sel, by_id[sel]["flag"]),
                    use_container_width=True,
                    config={"displayModeBar": True, "scrollZoom": True})


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
