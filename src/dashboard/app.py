"""Local dashboard (§16).

Pages: universe explorer with a point-in-time date selector, factor exposure
viewer, study report viewer keyed by pre-registration hash, current target
portfolio with cost estimates and days-to-liquidate per position, and the study
ledger.

**Read-only with respect to the store**, enforced rather than intended: the
database is opened with SQLite's `mode=ro` URI, so a write from this process is
an `OperationalError` rather than a silent mutation of research data. The
dashboard is the part of a system most likely to grow a convenient "just fix
this row" button, and this makes that impossible instead of discouraged.

Chosen over Streamlit because it freezes cleanly under PyInstaller — the
desktop build in `src/desktop/` wraps this same app in a native window.
"""
from __future__ import annotations

import datetime as dt
import json
import sqlite3
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse, JSONResponse

from src.config import Config, get_config

STATIC_DIR = Path(__file__).parent / "static"


def open_readonly(db_path: Path) -> sqlite3.Connection:
    """Open the store read-only. A write raises instead of succeeding."""
    if not Path(db_path).exists():
        raise FileNotFoundError(db_path)
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True,
                           check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


class Dashboard:
    """Holds the read-only connection and answers the API's questions."""

    def __init__(self, config: Config | None = None) -> None:
        self.config = config or get_config()
        self.db_path = self.config.db_dir / "platform.sqlite"
        self._conn: sqlite3.Connection | None = None

    @property
    def conn(self) -> sqlite3.Connection:
        if self._conn is None:
            self._conn = open_readonly(self.db_path)
        return self._conn

    @property
    def available(self) -> bool:
        return self.db_path.exists()

    # -- status ------------------------------------------------------------

    def status(self) -> dict[str, Any]:
        from src.costs.model import rate_table_status

        out: dict[str, Any] = {
            "store_present": self.available,
            "db_path": str(self.db_path),
            "config": {
                "capital_inr": self.config.capital_inr,
                "universe_tier": self.config.universe_tier,
                "benchmark": self.config.benchmark,
                "rebalance_freq": self.config.rebalance_freq,
                "max_position_pct": self.config.max_position_pct,
                "max_sector_pct": self.config.max_sector_pct,
                "min_positions": self.config.min_positions,
                "live_enabled": self.config.live_enabled,
                "llm_mode": self.config.llm_mode,
            },
            "rates": rate_table_status(),
        }
        try:
            from src.archive.store import Archive

            archive_db = self.config.archive_dir / "archive.sqlite"
            if archive_db.exists():
                with Archive(self.config.archive_dir) as archive:
                    out["archive"] = archive.stats()
        except Exception as exc:  # the dashboard must open even if the archive is odd
            out["archive_error"] = str(exc)

        if self.available:
            out["store"] = {
                "securities": self._scalar("SELECT COUNT(*) c FROM security"),
                "price_rows": self._scalar("SELECT COUNT(*) c FROM price_daily"),
                "first_session": self._scalar("SELECT MIN(date) c FROM price_daily"),
                "last_session": self._scalar("SELECT MAX(date) c FROM price_daily"),
                "trials": self._scalar("SELECT COUNT(*) c FROM trial_registry"),
            }
        return out

    def _scalar(self, sql: str) -> Any:
        row = self.conn.execute(sql).fetchone()
        return row["c"] if row else None

    def sessions(self) -> list[str]:
        return [r["date"] for r in self.conn.execute(
            "SELECT DISTINCT date FROM price_daily ORDER BY date DESC LIMIT 4000")]

    # -- §16 universe explorer --------------------------------------------

    def universe(self, date: str, tier: str) -> dict[str, Any]:
        from src.master.universe import Universe

        result = Universe(self.conn).as_of(date, tier)
        members = result.members.replace({np.nan: None})
        return {
            "date": result.date,
            "tier": result.tier,
            "count": len(result),
            "excluded": result.excluded,
            "screens": result.screens.describe(),
            "members": members.to_dict("records"),
        }

    # -- §16 factor exposure viewer ---------------------------------------

    def exposures(self, date: str, tier: str, factor_names: list[str]) -> dict[str, Any]:
        from src.factors.base import FactorContext, all_factors
        from src.master.universe import Universe

        registry = all_factors()
        unknown = [n for n in factor_names if n not in registry]
        if unknown:
            raise HTTPException(400, f"unknown factors: {unknown}")

        result = Universe(self.conn).as_of(date, tier)
        if not len(result):
            return {"date": date, "tier": tier, "rows": [], "factors": factor_names}

        ctx = FactorContext(self.conn, date, result.isins)
        frame = pd.DataFrame({name: registry[name](ctx) for name in factor_names})
        frame.insert(0, "symbol", result.members.set_index("isin")["symbol"])
        frame.insert(1, "sector", result.members.set_index("isin")["sector"])
        frame = frame.reset_index().rename(columns={"index": "isin"})
        return {
            "date": date, "tier": tier, "factors": factor_names,
            "rows": json.loads(frame.replace({np.nan: None}).to_json(orient="records")),
        }

    def factor_catalogue(self) -> list[dict[str, Any]]:
        from src.factors.base import all_factors

        return [f.describe() for f in all_factors().values()]

    # -- §16 target portfolio ---------------------------------------------

    def portfolio(self, date: str, tier: str, factor_name: str) -> dict[str, Any]:
        from src.factors.base import FactorContext, all_factors
        from src.master.universe import Universe
        from src.portfolio.construct import Constraints, ConstructionError, construct

        registry = all_factors()
        if factor_name not in registry:
            raise HTTPException(400, f"unknown factor {factor_name}")
        factor = registry[factor_name]

        universe = Universe(self.conn)
        result = universe.as_of(date, tier)
        if not len(result):
            raise HTTPException(400, f"universe is empty on {date}")

        ctx = FactorContext(self.conn, date, result.isins)
        scores = factor(ctx)
        members = result.members.set_index("isin")

        try:
            target = construct(
                scores,
                constraints=Constraints(
                    capital_inr=self.config.capital_inr,
                    max_position_pct=self.config.max_position_pct,
                    max_sector_pct=self.config.max_sector_pct,
                    min_positions=self.config.min_positions,
                    max_participation_pct=self.config.max_participation_pct,
                ),
                sectors=members["sector"],
                median_turnover=members["median_turnover"],
                as_of_date=date,
                higher_is_better=factor.higher_is_better,
            )
        except ConstructionError as exc:
            raise HTTPException(400, str(exc)) from exc

        from src.costs.model import CostModel

        model = CostModel(warn_unverified=False)
        rows = []
        for isin, weight in target.weights.items():
            price = float(members.loc[isin, "close"])
            notional = float(target.notional[isin])
            quantity = int(notional // price) if price > 0 else 0
            cost = model.leg("buy", price=price, quantity=quantity, date=date)
            rows.append({
                "isin": isin,
                "symbol": members.loc[isin, "symbol"],
                "sector": members.loc[isin, "sector"],
                "weight_pct": round(float(weight) * 100, 3),
                "notional_inr": round(notional, 2),
                "price": round(price, 2),
                "quantity": quantity,
                "entry_cost_inr": round(cost.total, 2),
                "entry_cost_bps": round(cost.bps, 1),
                "days_to_liquidate": (round(float(target.days_to_liquidate[isin]), 2)
                                      if np.isfinite(target.days_to_liquidate[isin])
                                      else None),
                "score": (None if pd.isna(scores.get(isin))
                          else round(float(scores[isin]), 6)),
            })
        return {
            "summary": target.summary(),
            "factor": factor_name,
            "positions": rows,
            "sector_weights": {k: round(float(v) * 100, 2)
                               for k, v in target.sector_weights().items()},
        }

    # -- §16 studies -------------------------------------------------------

    def studies(self) -> dict[str, Any]:
        from src.prereg.registry import load_all

        specs = []
        for study_id, prereg in load_all(self.config.prereg_dir).items():
            specs.append({
                "study_id": study_id,
                "prereg_hash": prereg.spec_hash,
                "spec_fingerprint": prereg.spec_fingerprint(),
                "factor": prereg.factor_name,
                "tier": prereg.universe_tier,
                "window": list(prereg.window),
                "horizon_days": prereg.horizon_days,
                "hypothesis": prereg.hypothesis,
            })

        ledger_path = self.config.prereg_dir / "LEDGER.md"
        reports = []
        if self.config.reports_dir.exists():
            reports = sorted(p.name for p in self.config.reports_dir.glob("*.md"))

        trials = []
        if self.available:
            trials = [dict(r) for r in self.conn.execute(
                "SELECT * FROM trial_registry ORDER BY trial_id DESC LIMIT 200")]

        return {
            "specs": specs,
            "ledger": ledger_path.read_text(encoding="utf-8")
            if ledger_path.exists() else "",
            "reports": reports,
            "trials": trials,
            "trial_count": len(trials),
        }

    def report(self, name: str) -> str:
        """Study report by file name. Reports are keyed by prereg hash (§16)."""
        # Reject any path component: this is a file name, not a path.
        if "/" in name or "\\" in name or ".." in name:
            raise HTTPException(400, "invalid report name")
        path = self.config.reports_dir / name
        if not path.exists() or path.suffix != ".md":
            raise HTTPException(404, f"no report {name}")
        return path.read_text(encoding="utf-8")


def create_app(config: Config | None = None) -> FastAPI:
    dashboard = Dashboard(config)
    app = FastAPI(title="PIT Factor Research Platform", version="0.1.0",
                  docs_url="/api/docs")
    app.state.dashboard = dashboard

    @app.get("/", response_class=HTMLResponse)
    def index() -> str:
        return (STATIC_DIR / "index.html").read_text(encoding="utf-8")

    @app.get("/api/status")
    def status() -> Any:
        return dashboard.status()

    @app.get("/api/sessions")
    def sessions() -> Any:
        return {"sessions": dashboard.sessions()} if dashboard.available else {"sessions": []}

    @app.get("/api/universe")
    def universe(date: str = Query(...), tier: str = Query("smallcap_inclusive")) -> Any:
        _require_store(dashboard)
        return dashboard.universe(date, tier)

    @app.get("/api/factors")
    def factors() -> Any:
        return {"factors": dashboard.factor_catalogue()}

    @app.get("/api/exposures")
    def exposures(date: str = Query(...), tier: str = Query("smallcap_inclusive"),
                  names: str = Query(...)) -> Any:
        _require_store(dashboard)
        return dashboard.exposures(date, tier, [n for n in names.split(",") if n])

    @app.get("/api/portfolio")
    def portfolio(date: str = Query(...), tier: str = Query("smallcap_inclusive"),
                  factor: str = Query(...)) -> Any:
        _require_store(dashboard)
        return dashboard.portfolio(date, tier, factor)

    @app.get("/api/studies")
    def studies() -> Any:
        return dashboard.studies()

    @app.get("/api/report/{name}", response_class=JSONResponse)
    def report(name: str) -> Any:
        return {"name": name, "markdown": dashboard.report(name)}

    return app


def _require_store(dashboard: Dashboard) -> None:
    if not dashboard.available:
        raise HTTPException(
            503,
            "No derived store yet. Run `python -m src.archive.backfill` to fetch "
            "source documents, then `python -m src.store.build` to build the "
            "store from them.",
        )


app = None  # created lazily by the desktop launcher / uvicorn factory


def get_app() -> FastAPI:
    global app
    if app is None:
        app = create_app()
    return app
