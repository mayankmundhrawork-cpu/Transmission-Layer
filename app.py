"""Streamlit board — v1 continuous-tier view.

Renders the four-market metric grid and the anomaly panel described in
Step 8 items 1 and 2. Reads data/prices.csv and computes flags in-process.

Run: streamlit run app.py
"""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import streamlit as st

from config import MARKETS
from engine import build_snapshot
from release_calendar import build_calendar

DATA_DIR = Path(__file__).parent / "data"
FETCH_LOG = DATA_DIR / "fetch_log.json"

st.set_page_config(page_title="Transmission Layer", layout="wide")

FLAG_COLOR = {"red": "#c0392b", "amber": "#d68910", "none": "#2ecc71", "missing": "#7f8c8d"}
FLAG_ICON = {"red": "●", "amber": "●", "none": "○", "missing": "×"}


def _fmt(v, dp: int = 2, suffix: str = "") -> str:
    if v is None:
        return "—"
    try:
        return f"{v:.{dp}f}{suffix}"
    except (TypeError, ValueError):
        return "—"


def _flag_badge(level: str) -> str:
    color = FLAG_COLOR.get(level, "#95a5a6")
    icon = FLAG_ICON.get(level, "·")
    return f"<span style='color:{color};font-size:16px'>{icon}</span> <span style='color:{color}'>{level}</span>"


def _grid_row(r: dict) -> dict:
    return {
        "flag":      f"{FLAG_ICON.get(r['flag'],'·')} {r['flag']}",
        "id":        r["id"],
        "last":      _fmt(r["last"], 4),
        "1d %":      _fmt(r["d1_pct"], 2, "%"),
        "5d %":      _fmt(r["d5_pct"], 2, "%"),
        "20d z":     _fmt(r["z20"], 2),
        "60d z":     _fmt(r["z60"], 2),
        "1y %ile":   _fmt(r["pct_1y"], 0),
        "as of":     r["last_date"] or "—",
        "reasons":   "; ".join(r["reasons"]) if r["reasons"] else "",
    }


def _style_grid(df: pd.DataFrame) -> pd.io.formats.style.Styler:
    def _row_style(row: pd.Series):
        level = row["flag"].split(" ", 1)[-1]
        color = FLAG_COLOR.get(level, "")
        if level in ("red", "amber"):
            bg = "rgba(192,57,43,0.12)" if level == "red" else "rgba(214,137,16,0.12)"
            return [f"background-color:{bg};color:{color}"] * len(row)
        if level == "missing":
            return ["opacity:0.55"] * len(row)
        return [""] * len(row)
    return df.style.apply(_row_style, axis=1)


# ── header ─────────────────────────────────────────────────────────────
st.title("The Transmission Layer")
st.caption("Continuous tier · v1 · macro anomaly board")

snap = build_snapshot()

if "error" in snap:
    st.error(snap["error"])
    st.stop()

meta_cols = st.columns([2, 2, 2, 2])
meta_cols[0].metric("Data as of", snap.get("last_data_date") or "—")
meta_cols[1].metric("Series tracked", len(snap["series"]))
red = sum(1 for r in snap["series"] if r["flag"] == "red")
amber = sum(1 for r in snap["series"] if r["flag"] == "amber")
missing = sum(1 for r in snap["series"] if r["flag"] == "missing")
meta_cols[2].metric("Red flags", red)
meta_cols[3].metric("Amber flags", amber)

if FETCH_LOG.exists():
    try:
        log = json.loads(FETCH_LOG.read_text())
        st.caption(f"Last fetch: {log.get('fetched_at','?')} · {missing} series missing data")
    except Exception:
        pass

# ── anomaly panel ──────────────────────────────────────────────────────
st.subheader("Anomaly panel")
flags = snap["flags"]
if not flags:
    st.success("No flags — calm session.")
else:
    fdf = pd.DataFrame([{
        "score":   f"{f['score']:.2f}",
        "flag":    f["flag"],
        "type":    f["type"],
        "market":  f["market"],
        "id":      f["id"],
        "z20":     _fmt(f["z20"], 2),
        "last":    _fmt(f["last"], 4),
        "reasons": "; ".join(f["reasons"]),
    } for f in flags])
    st.dataframe(fdf, hide_index=True, use_container_width=True)

# ── release calendar ───────────────────────────────────────────────────
st.subheader("Release calendar")
cal = build_calendar()

recent = cal["recent"]
if recent:
    st.markdown("**Released in last 24h** — read the number in manually:")
    for r in recent:
        st.markdown(
            f"- **{r['name']}** ({r['market']}, {r['released_date']}) — "
            f"[open source]({r['url']}) · _{r['threshold']}_"
        )

upcoming = cal["upcoming"]
if not upcoming:
    st.info("No upcoming releases computed.")
else:
    cal_df = pd.DataFrame([{
        "days": r["days_until"],
        "date": r["next_date"],
        "release": r["name"],
        "market": r["market"],
        "threshold": r["threshold"],
        "link": r["url"],
        "_soon": r["soon"],
    } for r in upcoming])

    def _cal_style(row: pd.Series):
        if row["_soon"]:
            return ["background-color:rgba(214,137,16,0.15);color:#d68910"] * len(row)
        return [""] * len(row)

    styled = cal_df.style.apply(_cal_style, axis=1)
    st.dataframe(
        styled,
        hide_index=True,
        use_container_width=True,
        column_config={
            "days": st.column_config.NumberColumn("days", format="%dd"),
            "link": st.column_config.LinkColumn("link", display_text="open"),
            "_soon": None,  # hidden helper column
        },
    )
    st.caption("Amber row = due within 3 days. Dates for FOMC / RBI-MPC / "
               "US CPI·PPI·PCE / OPEC are hardcoded 2026 estimates — see V2_BUILD_NOTES.md.")

# ── four-market grid ───────────────────────────────────────────────────
st.subheader("Four-market metric grid")
by_market: dict[str, list] = {m: [] for m in MARKETS}
for r in snap["series"]:
    by_market.setdefault(r["market"], []).append(r)

tabs = st.tabs(MARKETS)
for tab, market in zip(tabs, MARKETS):
    with tab:
        rows = by_market.get(market, [])
        if not rows:
            st.info(f"No series in {market}")
            continue
        grid = pd.DataFrame([_grid_row(r) for r in rows])
        st.dataframe(_style_grid(grid), hide_index=True, use_container_width=True)

st.caption(
    "Flag levels: red |z|≥2.5 or framework+|z|≥1.5 · amber |z|≥1.5, pct≤5/≥95, "
    "or framework trigger · none otherwise. Co-occurrence in a linked group "
    "escalates all members to red."
)
