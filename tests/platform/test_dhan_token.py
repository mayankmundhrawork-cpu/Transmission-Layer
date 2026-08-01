"""Dhan token daemon tests (§5).

Two things are being defended here: the token never appears in anything
printable, and a broken auth flow degrades to a usable fallback instead of
taking the platform down with it.
"""
from __future__ import annotations

import datetime as dt
import json

import pytest
import requests

from src.auth.dhan_token import (
    DhanAuthError, DhanTokenManager, TokenRecord, TokenStore, main, redact,
)

UTC = dt.timezone.utc
TOKEN = "eyJhbGciOiJIUzI1NiJ9.super-secret-token-body.signature"


class FakeResponse:
    def __init__(self, status_code=200, payload=None):
        self.status_code = status_code
        self._payload = payload if payload is not None else {}

    def json(self):
        return self._payload


class FakeSession:
    """Routes by URL suffix so tests declare intent, not call order."""

    def __init__(self, *, profile=None, consent=None, consume=None):
        self.profile = profile if profile is not None else FakeResponse(200, {"dhanClientId": "X"})
        self.consent = consent if consent is not None else FakeResponse(200, {"consentId": "c-1"})
        self.consume = consume if consume is not None else FakeResponse(200, {"accessToken": TOKEN})
        self.calls: list[str] = []

    def get(self, url, **kw):
        self.calls.append(url)
        if url.endswith("/profile"):
            if isinstance(self.profile, Exception):
                raise self.profile
            return self.profile
        if "generate-consent" in url:
            return self.consent
        raise AssertionError(f"unexpected GET {url}")

    def post(self, url, **kw):
        self.calls.append(url)
        if "consume-consent" in url:
            return self.consume
        raise AssertionError(f"unexpected POST {url}")


@pytest.fixture
def manager(cfg, monkeypatch):
    monkeypatch.setenv("DHAN_API_KEY", "app-id")
    monkeypatch.setenv("DHAN_API_SECRET", "app-secret")
    monkeypatch.setenv("DHAN_TOTP_SEED", "JBSWY3DPEHPK3PXP")  # RFC 4226 test seed

    def build(session=None):
        return DhanTokenManager(cfg, session=session or FakeSession())

    return build


def record(expires_in_hours: float, token: str = TOKEN, source="generated") -> TokenRecord:
    now = dt.datetime.now(tz=UTC)
    return TokenRecord(
        access_token=token,
        expires_at=now + dt.timedelta(hours=expires_in_hours),
        obtained_at=now,
        source=source,
    )


# --- redaction --------------------------------------------------------------

def test_redact_never_shows_the_body():
    out = redact(TOKEN)
    assert TOKEN not in out
    assert "super-secret-token-body" not in out
    assert out.endswith("(len %d)" % len(TOKEN)) or "redacted" in out


def test_redact_handles_short_and_missing_tokens():
    assert redact(None) == "<none>"
    assert redact("") == "<none>"
    assert "redacted" in redact("abc")


def test_token_record_repr_redacts():
    rec = record(12)
    assert TOKEN not in repr(rec)
    assert TOKEN not in str(rec)
    assert TOKEN not in f"{rec}"


def test_status_does_not_leak_the_token(manager):
    mgr = manager()
    mgr.store.save(record(10))
    status = mgr.status()
    assert TOKEN not in json.dumps(status)
    assert status["present"] is True
    assert status["expires_in_hours"] == pytest.approx(10, abs=0.1)


# --- store ------------------------------------------------------------------

def test_token_store_round_trip(tmp_path):
    store = TokenStore(tmp_path / "tok.json")
    rec = record(5)
    store.save(rec)
    loaded = store.load()
    assert loaded.access_token == TOKEN
    assert loaded.source == "generated"
    assert abs((loaded.expires_at - rec.expires_at).total_seconds()) < 1


def test_token_file_is_not_world_readable(tmp_path):
    store = TokenStore(tmp_path / "tok.json")
    store.save(record(5))
    mode = store.path.stat().st_mode
    assert not mode & 0o077, "token file must be owner-only"


def test_corrupt_token_file_is_treated_as_absent(tmp_path):
    store = TokenStore(tmp_path / "tok.json")
    store.path.write_text("{not json", encoding="utf-8")
    assert store.load() is None


def test_missing_token_file_is_none(tmp_path):
    assert TokenStore(tmp_path / "nope.json").load() is None


# --- refresh policy ---------------------------------------------------------

def test_valid_cached_token_is_reused_without_network(manager):
    session = FakeSession()
    mgr = manager(session)
    mgr.store.save(record(10))
    assert mgr.get_token().access_token == TOKEN
    assert session.calls == [], "a fresh token must not trigger any request"


def test_token_near_expiry_is_refreshed(manager):
    session = FakeSession()
    mgr = manager(session)
    mgr.store.save(record(0.5))  # inside the 2h threshold
    mgr.get_token()
    assert any("generate-consent" in c for c in session.calls)


def test_expired_token_is_regenerated(manager):
    session = FakeSession()
    mgr = manager(session)
    mgr.store.save(record(-1))
    assert mgr.get_token().access_token == TOKEN
    assert any("consume-consent" in c for c in session.calls)


def test_refresh_failure_falls_back_to_the_still_valid_token(manager):
    """Inside the refresh window the old token still works. A failed renewal
    must not throw away a credential that would have completed the fetch."""
    session = FakeSession(consent=FakeResponse(500))
    mgr = manager(session)
    mgr.store.save(record(1.0, token="still-good"))
    assert mgr.get_token().access_token == "still-good"


def test_generation_disabled_raises_when_no_cached_token(manager):
    mgr = manager()
    with pytest.raises(DhanAuthError, match="generation is disabled"):
        mgr.get_token(allow_generate=False)


# --- validation -------------------------------------------------------------

def test_validate_rejects_401(manager):
    mgr = manager(FakeSession(profile=FakeResponse(401)))
    with pytest.raises(DhanAuthError, match="rejected"):
        mgr.validate(TOKEN)


def test_validate_error_message_does_not_contain_the_token(manager):
    mgr = manager(FakeSession(profile=FakeResponse(403)))
    with pytest.raises(DhanAuthError) as exc:
        mgr.validate(TOKEN)
    assert TOKEN not in str(exc.value)


def test_validate_surfaces_network_failure(manager):
    mgr = manager(FakeSession(profile=requests.ConnectionError("down")))
    with pytest.raises(DhanAuthError, match="could not reach Dhan"):
        mgr.validate(TOKEN)


def test_broker_supplied_validity_wins_over_the_24h_assumption(manager):
    mgr = manager(FakeSession(
        profile=FakeResponse(200, {"tokenValidity": "02/01/2030 06:00"})
    ))
    rec = mgr.set_manual_token(TOKEN)
    assert rec.expires_at == dt.datetime(2030, 1, 2, 6, 0, tzinfo=UTC)


def test_unparseable_validity_falls_back_to_24h_cap(manager):
    mgr = manager(FakeSession(profile=FakeResponse(200, {"tokenValidity": "whenever"})))
    rec = mgr.set_manual_token(TOKEN)
    assert 23.5 < (rec.expires_at - rec.obtained_at).total_seconds() / 3600 <= 24.0


# --- manual fallback --------------------------------------------------------

def test_manual_token_is_validated_before_being_stored(manager):
    mgr = manager(FakeSession(profile=FakeResponse(401)))
    with pytest.raises(DhanAuthError):
        mgr.set_manual_token(TOKEN)
    assert mgr.store.load() is None, "a rejected token must not be cached"


def test_manual_token_is_stored_with_manual_provenance(manager):
    mgr = manager()
    rec = mgr.set_manual_token(f"  {TOKEN}  \n")
    assert rec.access_token == TOKEN, "whitespace from a paste is stripped"
    assert rec.source == "manual"
    assert mgr.store.load().source == "manual"


def test_empty_manual_token_rejected(manager):
    with pytest.raises(DhanAuthError, match="empty token"):
        manager().set_manual_token("   \n")


# --- seed handling ----------------------------------------------------------

def test_missing_totp_seed_points_at_the_fallback(cfg, monkeypatch):
    monkeypatch.setenv("DHAN_API_KEY", "app-id")
    monkeypatch.setenv("DHAN_API_SECRET", "app-secret")
    monkeypatch.delenv("DHAN_TOTP_SEED", raising=False)
    mgr = DhanTokenManager(cfg, session=FakeSession())
    with pytest.raises(DhanAuthError, match="--token-from-stdin"):
        mgr.generate()


def test_missing_api_credentials_point_at_the_fallback(cfg, monkeypatch):
    monkeypatch.delenv("DHAN_API_KEY", raising=False)
    mgr = DhanTokenManager(cfg, session=FakeSession())
    with pytest.raises(DhanAuthError, match="--token-from-stdin"):
        mgr.generate()


def test_totp_seed_is_not_retained_on_the_manager(manager):
    mgr = manager()
    mgr.generate()
    blob = json.dumps({k: str(v) for k, v in vars(mgr).items()})
    assert "JBSWY3DPEHPK3PXP" not in blob, "the seed must not outlive the call"


def test_partner_flow_failure_names_the_manual_path(manager):
    mgr = manager(FakeSession(consent=FakeResponse(403)))
    with pytest.raises(DhanAuthError, match="--token-from-stdin"):
        mgr.generate()


# --- CLI --------------------------------------------------------------------

def test_status_cli_needs_no_network(cfg, monkeypatch, capsys):
    monkeypatch.setattr("src.auth.dhan_token.get_config", lambda: cfg)
    assert main(["--status"]) == 0
    assert json.loads(capsys.readouterr().out)["present"] is False


def test_cli_failure_says_research_still_runs(cfg, monkeypatch, capsys):
    """§5: token failure blocks new fetches only. The message must say so —
    otherwise the operator assumes the platform is down."""
    monkeypatch.setattr("src.auth.dhan_token.get_config", lambda: cfg)
    monkeypatch.setattr(
        "src.auth.dhan_token.DhanTokenManager.get_token",
        lambda self, **kw: (_ for _ in ()).throw(DhanAuthError("nope")),
    )
    assert main([]) == 1
    assert "research pipeline still runs" in capsys.readouterr().err
