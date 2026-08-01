"""Dashboard tests (§16).

The invariant worth defending is read-only. The dashboard is the part of any
system most likely to grow a convenient "just fix this row" button, and the
`mode=ro` connection makes that an error rather than a temptation.
"""
from __future__ import annotations

import sqlite3

import pytest
from fastapi.testclient import TestClient

from src.dashboard.app import Dashboard, create_app, open_readonly
from src.store.schema import connect
from tests.platform.world import build_fundamentals, build_world


@pytest.fixture(scope="module")
def seeded(tmp_path_factory):
    root = tmp_path_factory.mktemp("dash")
    (root / "db").mkdir()
    (root / "archive").mkdir()
    (root / "reports").mkdir()
    conn = connect(root / "db" / "platform.sqlite")
    world = build_world(conn)
    build_fundamentals(conn, world.isins)
    conn.close()
    return root


@pytest.fixture
def client(seeded, monkeypatch):
    """Data comes from the seeded temp dir; prereg/ comes from the real repo.

    That split mirrors production: the archive and store are machine-local
    state, while pre-registrations are committed source.
    """
    monkeypatch.setenv("DATA_DIR", str(seeded))
    from pathlib import Path

    from src.config import load_config

    config = load_config(repo_root=Path(__file__).resolve().parents[2])
    return TestClient(create_app(config)), config


# --- read-only --------------------------------------------------------------

def test_store_is_opened_read_only(seeded):
    """§16: read-only with respect to the store, enforced not intended."""
    conn = open_readonly(seeded / "db" / "platform.sqlite")
    with pytest.raises(sqlite3.OperationalError, match="readonly"):
        conn.execute("DELETE FROM price_daily")
    with pytest.raises(sqlite3.OperationalError):
        conn.execute("UPDATE security SET isin='x'")
    conn.close()


def test_dashboard_connection_cannot_write(seeded, tmp_path, monkeypatch):
    monkeypatch.setenv("DATA_DIR", str(seeded))
    from src.config import load_config

    dashboard = Dashboard(load_config(repo_root=tmp_path))
    with pytest.raises(sqlite3.OperationalError):
        dashboard.conn.execute("DROP TABLE price_daily")


# --- endpoints --------------------------------------------------------------

def test_index_serves_the_page(client):
    api, _ = client
    response = api.get("/")
    assert response.status_code == 200
    assert "Point-in-Time Factor Research Platform" in response.text
    assert "cdn" not in response.text.lower(), "the page must be self-contained"


def test_status_reports_config_and_rate_verification(client):
    api, _ = client
    body = api.get("/api/status").json()
    assert body["store_present"] is True
    assert body["config"]["live_enabled"] is False
    assert body["rates"]["all_verified"] is False, (
        "unverified rates must be surfaced to the user, not buried"
    )
    assert body["store"]["securities"] > 40


def test_universe_endpoint_is_point_in_time(client):
    """The delisted name is present before its delisting and gone after."""
    api, _ = client
    from tests.platform.world import SPECIALS

    before = api.get("/api/universe?date=2021-01-15&tier=nifty500").json()
    after = api.get("/api/universe?date=2021-12-15&tier=nifty500").json()
    delisted = SPECIALS["DELISTED"][0]
    assert delisted in [m["isin"] for m in before["members"]]
    assert delisted not in [m["isin"] for m in after["members"]]


def test_universe_reports_exclusion_counts(client):
    api, _ = client
    body = api.get("/api/universe?date=2022-06-30&tier=nifty500").json()
    assert "illiquid" in body["excluded"]
    assert body["screens"]["min_listing_sessions"] == 250


def test_factor_catalogue_lists_every_factor(client):
    api, _ = client
    from src.factors.base import all_factors

    body = api.get("/api/factors").json()
    assert len(body["factors"]) == len(all_factors())


def test_exposures_endpoint(client):
    api, _ = client
    body = api.get("/api/exposures?date=2022-06-30&tier=nifty500"
                   "&names=earnings_yield,roe").json()
    assert body["factors"] == ["earnings_yield", "roe"]
    assert len(body["rows"]) > 20
    assert "earnings_yield" in body["rows"][0]


def test_unknown_factor_is_rejected(client):
    api, _ = client
    assert api.get("/api/exposures?date=2022-06-30&names=not_a_factor"
                   ).status_code == 400


def test_portfolio_endpoint_reports_cost_and_liquidation(client):
    """§16: target portfolio with cost estimates and days-to-liquidate per position."""
    api, _ = client
    body = api.get("/api/portfolio?date=2022-06-30&tier=nifty500"
                   "&factor=earnings_yield").json()
    assert body["summary"]["n_positions"] >= 25
    assert body["summary"]["max_position_weight"] <= 0.04 + 1e-9
    position = body["positions"][0]
    for key in ("entry_cost_inr", "entry_cost_bps", "days_to_liquidate",
                "notional_inr", "weight_pct"):
        assert key in position
    assert position["entry_cost_inr"] > 0, "§18.6: no costless position"


def test_symbols_are_point_in_time_in_the_portfolio(client):
    """The renamed security must show the symbol it carried on the as-of date."""
    api, _ = client
    from tests.platform.world import SPECIALS

    old = api.get("/api/portfolio?date=2019-06-28&tier=nifty500"
                  "&factor=log_free_float_mcap").json()
    new = api.get("/api/portfolio?date=2023-06-30&tier=nifty500"
                  "&factor=log_free_float_mcap").json()
    renamed = SPECIALS["RENAMED"][0]
    for body, expected in ((old, "OLDNAME"), (new, "NEWNAME")):
        row = next((p for p in body.get("positions", []) if p["isin"] == renamed), None)
        if row is not None:
            assert row["symbol"] == expected


def test_studies_endpoint_exposes_ledger_and_trials(client):
    api, _ = client
    body = api.get("/api/studies").json()
    assert any(s["study_id"] == "PREREG-000-noise-control" for s in body["specs"])
    assert "Study ledger" in body["ledger"]
    assert "trials" in body


def test_report_path_traversal_is_rejected(client):
    api, _ = client
    for name in ("../../.env", "..%2F..%2Fetc%2Fpasswd", "a/b.md"):
        assert api.get(f"/api/report/{name}").status_code in (400, 404)


def test_missing_report_is_404(client):
    api, _ = client
    assert api.get("/api/report/nope.md").status_code == 404


def test_missing_store_gives_actionable_guidance(tmp_path, monkeypatch):
    monkeypatch.setenv("DATA_DIR", str(tmp_path / "empty"))
    from src.config import load_config

    api = TestClient(create_app(load_config(repo_root=tmp_path)))
    response = api.get("/api/universe?date=2022-06-30")
    assert response.status_code == 503
    assert "backfill" in response.json()["detail"]


def test_status_works_without_a_store(tmp_path, monkeypatch):
    """The overview must open on a fresh install rather than erroring."""
    monkeypatch.setenv("DATA_DIR", str(tmp_path / "empty"))
    from src.config import load_config

    api = TestClient(create_app(load_config(repo_root=tmp_path)))
    body = api.get("/api/status").json()
    assert body["store_present"] is False


# --- desktop launcher -------------------------------------------------------

def test_launcher_binds_localhost_only():
    """This process can reach a broker; it has no business being on the network."""
    from src.desktop import main as launcher

    assert launcher.HOST == "127.0.0.1"


def test_free_port_is_usable():
    from src.desktop.main import free_port

    assert 1024 < free_port() < 65536


# --- packaging --------------------------------------------------------------

def test_desktop_spec_bundles_every_runtime_data_file():
    """The frozen build reads these from disk at runtime.

    A spec that stops bundling one of them produces an app that starts and then
    fails on the page that needs it — which is exactly the failure a user hits
    and a developer never does.
    """
    import ast
    from pathlib import Path

    repo = Path(__file__).resolve().parents[2]
    spec = (repo / "desktop.spec").read_text(encoding="utf-8")

    for required in ("src/dashboard/static", "src/costs/rates.yaml", "prereg"):
        assert f'"{required}"' in spec, f"desktop.spec no longer bundles {required}"
        assert (repo / required).exists(), f"{required} is bundled but missing"


def test_desktop_spec_does_not_exclude_distutils():
    """Excluding distutils prunes part of numpy's module graph and the frozen
    app dies with 'Importing the numpy C-extensions failed'. Learned the hard
    way; keep it learned."""
    from pathlib import Path

    spec = (Path(__file__).resolve().parents[2] / "desktop.spec").read_text()
    excludes = spec.split("excludes=[")[1].split("]")[0]
    assert '"distutils"' not in excludes


def test_installer_script_preserves_user_data_on_uninstall():
    """An uninstall must not destroy a multi-hour archive backfill."""
    from pathlib import Path

    iss = (Path(__file__).resolve().parents[2] / "installer" / "setup.iss").read_text()
    assert "{app}" in iss
    for user_data in ("{localappdata}", "%LOCALAPPDATA%"):
        assert f"Type: filesandordirs; Name: \"{user_data}" not in iss
