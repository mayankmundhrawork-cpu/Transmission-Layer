"""Dhan access-token daemon (§5).

Exchange/SEBI rules cap API access tokens at 24 hours, so a research platform
that fetches prices needs a token refreshed daily without a human in the loop.

Design constraints from the spec, each of which shows up as code below:

* **Validate before regenerating.** Hit the profile endpoint; only mint a new
  token when the current one is invalid or expiring inside the threshold.
  Regenerating on every run is how you get rate-limited off your own account.
* **The TOTP seed is read at use and never persisted or logged.** It comes from
  :class:`~src.config.Secret`, is passed straight into the OTP computation, and
  is not stored on this object. The generated *token* is persisted (it has to
  be, to survive across processes) in a 0600 file, and is redacted everywhere
  it is printed.
* **A manual fallback always exists.** ``--token-from-stdin`` accepts a token
  pasted from the Dhan web console. The automated consent flow is a partner-
  account feature and can be withdrawn or broken by the broker at any time;
  when that happens the platform must still be usable.
* **Token failure blocks new fetches only.** Nothing here is imported by the
  research pipeline. `src/eval` and `src/factors` read the archive, and the
  archive does not care whether today's token minted.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import stat
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import requests

from src.config import Config, MissingSecret, get_config

UTC = dt.timezone.utc

DHAN_API = "https://api.dhan.co/v2"
DHAN_AUTH = "https://auth.dhan.co"

#: Refresh when less than this remains. Two hours of slack means a scheduled
#: overnight run is never racing the expiry.
REFRESH_THRESHOLD = dt.timedelta(hours=2)
#: Exchange cap. Used as the assumed lifetime when the API does not say.
MAX_TOKEN_LIFETIME = dt.timedelta(hours=24)


class DhanAuthError(RuntimeError):
    """Token could not be obtained or validated."""


def redact(token: str | None) -> str:
    """Render a token safe to print. Used in every user-facing message."""
    if not token:
        return "<none>"
    return f"…{token[-4:]} (len {len(token)})" if len(token) > 8 else "<redacted>"


@dataclass(frozen=True)
class TokenRecord:
    access_token: str
    expires_at: dt.datetime
    obtained_at: dt.datetime
    source: str  # "generated" | "manual" | "env"

    @property
    def expires_in(self) -> dt.timedelta:
        return self.expires_at - dt.datetime.now(tz=UTC)

    @property
    def is_expired(self) -> bool:
        return self.expires_in <= dt.timedelta(0)

    @property
    def needs_refresh(self) -> bool:
        return self.expires_in <= REFRESH_THRESHOLD

    def __repr__(self) -> str:  # never leak the token through a repr
        return (
            f"TokenRecord(token={redact(self.access_token)}, "
            f"expires_at={self.expires_at.isoformat()}, source={self.source!r})"
        )

    __str__ = __repr__


class TokenStore:
    """Persists the current token to a 0600 file under the DB directory."""

    def __init__(self, path: Path) -> None:
        self.path = Path(path)

    def load(self) -> TokenRecord | None:
        if not self.path.exists():
            return None
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
            return TokenRecord(
                access_token=data["access_token"],
                expires_at=dt.datetime.fromisoformat(data["expires_at"]),
                obtained_at=dt.datetime.fromisoformat(data["obtained_at"]),
                source=data.get("source", "unknown"),
            )
        except (OSError, ValueError, KeyError):
            # A corrupt token file must not sink the run; treat as absent.
            return None

    def save(self, record: TokenRecord) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(
            json.dumps({
                "access_token": record.access_token,
                "expires_at": record.expires_at.isoformat(),
                "obtained_at": record.obtained_at.isoformat(),
                "source": record.source,
            }),
            encoding="utf-8",
        )
        # Restrict before publishing the name, so the token is never briefly
        # world-readable at its final path.
        try:
            tmp.chmod(stat.S_IRUSR | stat.S_IWUSR)
        except OSError:
            pass
        os.replace(tmp, self.path)

    def clear(self) -> None:
        self.path.unlink(missing_ok=True)


class DhanTokenManager:
    """Obtain, validate, cache, and refresh the Dhan access token."""

    def __init__(
        self,
        config: Config | None = None,
        *,
        session: requests.Session | None = None,
        store: TokenStore | None = None,
    ) -> None:
        self.config = config or get_config()
        self.session = session or requests.Session()
        self.store = store or TokenStore(self.config.db_dir / "dhan_token.json")

    # -- validation --------------------------------------------------------

    def validate(self, token: str) -> dict[str, Any]:
        """Check a token against the profile endpoint.

        Returns the profile payload. Raises :class:`DhanAuthError` if the token
        is rejected — never returns a falsy "probably fine".
        """
        try:
            resp = self.session.get(
                f"{DHAN_API}/profile",
                headers={"access-token": token, "Accept": "application/json"},
                timeout=20,
            )
        except requests.RequestException as exc:
            raise DhanAuthError(f"could not reach Dhan to validate token: {exc}") from exc

        if resp.status_code in (401, 403):
            raise DhanAuthError(f"Dhan rejected token {redact(token)} (HTTP {resp.status_code})")
        if resp.status_code >= 400:
            raise DhanAuthError(f"Dhan profile endpoint returned HTTP {resp.status_code}")
        try:
            return resp.json()
        except ValueError as exc:
            raise DhanAuthError("Dhan profile endpoint returned non-JSON") from exc

    def _record_from_profile(self, token: str, profile: dict[str, Any], source: str) -> TokenRecord:
        """Build a record, preferring the broker's own expiry over our assumption."""
        now = dt.datetime.now(tz=UTC)
        expires_at = now + MAX_TOKEN_LIFETIME
        raw = profile.get("tokenValidity") or profile.get("token_validity")
        if isinstance(raw, str):
            for fmt in ("%d/%m/%Y %H:%M", "%Y-%m-%d %H:%M:%S", "%d-%m-%Y %H:%M:%S"):
                try:
                    expires_at = dt.datetime.strptime(raw, fmt).replace(tzinfo=UTC)
                    break
                except ValueError:
                    continue
        return TokenRecord(
            access_token=token, expires_at=expires_at, obtained_at=now, source=source
        )

    # -- acquisition -------------------------------------------------------

    def _totp_now(self) -> str:
        """Current TOTP code. The seed lives in this frame and nowhere else."""
        try:
            import pyotp
        except ImportError as exc:  # pragma: no cover
            raise DhanAuthError("pyotp is required for the automated token flow") from exc
        try:
            seed = self.config.secret("DHAN_TOTP_SEED").reveal()
        except MissingSecret as exc:
            raise DhanAuthError(
                "DHAN_TOTP_SEED is not set. Either configure it, or use "
                "`python -m src.auth.dhan_token --token-from-stdin`."
            ) from exc
        try:
            return pyotp.TOTP(seed).now()
        finally:
            del seed  # do not let the seed outlive the call that needed it

    def generate(self) -> TokenRecord:
        """Run the API key + secret + TOTP consent flow.

        This is the partner-app flow. It is genuinely fragile — the broker can
        change or gate it — which is why every failure here points at the
        manual path rather than just raising.
        """
        try:
            app_id = self.config.secret("DHAN_API_KEY").reveal()
            app_secret = self.config.secret("DHAN_API_SECRET").reveal()
        except MissingSecret as exc:
            raise DhanAuthError(
                f"{exc} Automated token generation needs DHAN_API_KEY and "
                "DHAN_API_SECRET; otherwise use --token-from-stdin."
            ) from exc

        auth_headers = {"app_id": app_id, "app_secret": app_secret,
                        "Accept": "application/json"}
        try:
            consent = self.session.get(
                f"{DHAN_AUTH}/app/generate-consent", headers=auth_headers, timeout=20
            )
            if consent.status_code >= 400:
                raise DhanAuthError(
                    f"consent request failed (HTTP {consent.status_code}). "
                    "This flow requires a Dhan partner app; if you have a "
                    "standard account, paste a token with --token-from-stdin."
                )
            consent_id = (consent.json() or {}).get("consentId")
            if not consent_id:
                raise DhanAuthError("Dhan returned no consentId")

            resp = self.session.post(
                f"{DHAN_AUTH}/app/consume-consent",
                headers=auth_headers,
                json={"consentId": consent_id, "totp": self._totp_now()},
                timeout=20,
            )
            if resp.status_code >= 400:
                raise DhanAuthError(
                    f"consent consumption failed (HTTP {resp.status_code}). "
                    "If TOTP is not enabled on the app, use --token-from-stdin."
                )
            token = (resp.json() or {}).get("accessToken")
            if not token:
                raise DhanAuthError("Dhan returned no accessToken")
        except requests.RequestException as exc:
            raise DhanAuthError(f"network failure during token generation: {exc}") from exc
        finally:
            del app_id, app_secret

        record = self._record_from_profile(token, self.validate(token), "generated")
        self.store.save(record)
        return record

    def set_manual_token(self, token: str) -> TokenRecord:
        """Accept a token pasted from the Dhan web console, after validating it."""
        token = token.strip()
        if not token:
            raise DhanAuthError("empty token")
        record = self._record_from_profile(token, self.validate(token), "manual")
        self.store.save(record)
        return record

    # -- the entry point everything else uses ------------------------------

    def get_token(self, *, allow_generate: bool = True) -> TokenRecord:
        """Return a usable token, refreshing only if needed."""
        record = self.store.load()
        if record is not None and not record.needs_refresh:
            return record
        if record is not None and not record.is_expired:
            # Inside the refresh window but still alive: try to renew, and fall
            # back to the existing token rather than failing a fetch that could
            # have succeeded.
            if allow_generate:
                try:
                    return self.generate()
                except DhanAuthError:
                    return record
            return record
        if not allow_generate:
            raise DhanAuthError("no valid cached token and generation is disabled")
        return self.generate()

    def status(self) -> dict[str, Any]:
        """Non-secret status for the dashboard and the CLI."""
        record = self.store.load()
        if record is None:
            return {"present": False, "valid": False, "detail": "no token cached"}
        return {
            "present": True,
            "token": redact(record.access_token),
            "source": record.source,
            "expires_at": record.expires_at.isoformat(),
            "expires_in_hours": round(record.expires_in.total_seconds() / 3600, 2),
            "expired": record.is_expired,
            "needs_refresh": record.needs_refresh,
        }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m src.auth.dhan_token",
        description="Dhan access-token daemon. Validates the cached token and "
                    "regenerates only when it is invalid or near expiry.",
    )
    parser.add_argument("--token-from-stdin", action="store_true",
                        help="read a token from stdin instead of generating one "
                             "(fallback for when the automated flow is unavailable)")
    parser.add_argument("--status", action="store_true",
                        help="print token status and exit without touching the network")
    parser.add_argument("--force", action="store_true",
                        help="regenerate even if the cached token is still valid")
    args = parser.parse_args(argv)

    manager = DhanTokenManager()

    if args.status:
        print(json.dumps(manager.status(), indent=2))
        return 0

    try:
        if args.token_from_stdin:
            print("Paste the Dhan access token, then press Enter:", file=sys.stderr)
            record = manager.set_manual_token(sys.stdin.readline())
        elif args.force:
            record = manager.generate()
        else:
            record = manager.get_token()
    except DhanAuthError as exc:
        # Non-zero exit, but the message must make the fallback obvious.
        print(f"token unavailable: {exc}", file=sys.stderr)
        print(
            "The research pipeline still runs — it reads the archive, not the "
            "broker. Only new price fetches are blocked.",
            file=sys.stderr,
        )
        return 1

    print(f"token ok: {redact(record.access_token)}, "
          f"expires {record.expires_at.isoformat()} ({record.source})")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
