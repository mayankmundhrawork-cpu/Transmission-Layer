"""Polite HTTP session for sources that do not want to be scraped (§5).

NSE fingerprints clients and will blackhole an IP that hammers it. The rules
encoded here:

* **Prime before you ask.** NSE's data endpoints 401 without the cookies its
  homepage sets. We hit the homepage once per session and reuse the jar.
* **Hard rate limit.** One request per `min_interval_s` (default 2s), enforced
  per host across the whole process, not per call site.
* **Back off on transient failure, stop dead on a block.** 5xx and network
  errors retry with exponential backoff. A 401/403/careful-worded HTML block
  page raises :class:`SourceBlocked` immediately — retrying a block converts a
  soft rate-limit into a long ban, which is the one failure that costs days.

Nothing here writes to the archive; the fetchers do that. This layer only
concerns itself with getting bytes politely or failing clearly.
"""
from __future__ import annotations

import random
import time
from dataclasses import dataclass, field
from typing import Any, Callable, Mapping

import requests

# A real browser UA. Not deception for its own sake: NSE serves a different,
# broken response to obvious scripts, so a plausible UA is what makes the
# document we archive the same document a human would see.
DEFAULT_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

BROWSER_HEADERS: dict[str, str] = {
    "User-Agent": DEFAULT_UA,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}

# Substrings that mean "you are blocked", not "this document is missing".
BLOCK_MARKERS = (
    b"Access Denied",
    b"Request Rejected",
    b"You don't have permission to access",
    b"<title>Attention Required",  # Cloudflare
    b"unusual traffic",
)

RETRYABLE_STATUS = frozenset({408, 425, 429, 500, 502, 503, 504})
BLOCKED_STATUS = frozenset({401, 403})


class FetchError(RuntimeError):
    """A fetch failed in a way the caller should record and move past."""


class SourceBlocked(FetchError):
    """The source refused us. Do not retry — back off for hours, not seconds."""


class NotFound(FetchError):
    """The document does not exist at the source (404, or a 'no data' sentinel).

    Distinct from a block: a missing bhavcopy for a trading holiday is normal
    and should be logged as `skipped`/`empty`, not treated as an outage.
    """


@dataclass
class RateLimiter:
    """Per-host minimum spacing between requests."""

    min_interval_s: float = 2.0
    sleep: Callable[[float], None] = time.sleep
    clock: Callable[[], float] = time.monotonic
    _last: dict[str, float] = field(default_factory=dict, repr=False)

    def wait(self, host: str) -> float:
        """Block until this host may be called again. Returns seconds slept."""
        now = self.clock()
        last = self._last.get(host)
        slept = 0.0
        if last is not None:
            gap = self.min_interval_s - (now - last)
            if gap > 0:
                self.sleep(gap)
                slept = gap
        self._last[host] = self.clock()
        return slept


@dataclass
class PoliteSession:
    """A `requests.Session` with priming, spacing, backoff, and block detection."""

    min_interval_s: float = 2.0
    max_retries: int = 4
    timeout_s: float = 30.0
    headers: Mapping[str, str] = field(default_factory=lambda: dict(BROWSER_HEADERS))
    sleep: Callable[[float], None] = time.sleep
    session: requests.Session | None = None
    limiter: RateLimiter | None = None
    _primed: set[str] = field(default_factory=set, repr=False)

    def __post_init__(self) -> None:
        if self.session is None:
            self.session = requests.Session()
        self.session.headers.update(self.headers)
        if self.limiter is None:
            self.limiter = RateLimiter(self.min_interval_s, sleep=self.sleep)

    # -- priming -----------------------------------------------------------

    def prime(self, home_url: str, force: bool = False) -> None:
        """Acquire cookies from a source's homepage. Idempotent per session."""
        host = _host(home_url)
        if host in self._primed and not force:
            return
        try:
            self.limiter.wait(host)  # type: ignore[union-attr]
            resp = self.session.get(home_url, timeout=self.timeout_s)  # type: ignore[union-attr]
            # A failed prime is not fatal on its own — the real request will
            # tell us whether we actually needed the cookies.
            if resp.status_code < 400:
                self._primed.add(host)
        except requests.RequestException:
            pass

    # -- fetching ----------------------------------------------------------

    def get(
        self,
        url: str,
        *,
        headers: Mapping[str, str] | None = None,
        params: Mapping[str, Any] | None = None,
        prime_url: str | None = None,
    ) -> requests.Response:
        """GET with the full politeness stack. Raises on failure, never returns
        a non-2xx response."""
        if prime_url:
            self.prime(prime_url)
        host = _host(url)
        last_exc: Exception | None = None

        for attempt in range(self.max_retries + 1):
            self.limiter.wait(host)  # type: ignore[union-attr]
            try:
                resp = self.session.get(  # type: ignore[union-attr]
                    url, headers=dict(headers or {}), params=dict(params or {}),
                    timeout=self.timeout_s,
                )
            except requests.RequestException as exc:
                last_exc = exc
                if attempt >= self.max_retries:
                    raise FetchError(f"network error fetching {url}: {exc}") from exc
                self._backoff(attempt)
                continue

            status = resp.status_code
            if status in BLOCKED_STATUS or _looks_blocked(resp.content):
                raise SourceBlocked(
                    f"{host} refused the request (HTTP {status}). Not retrying: "
                    "repeated attempts after a block extend the ban. Wait, then "
                    "re-run — the archive keeps everything already fetched."
                )
            if status == 404:
                raise NotFound(f"{url} returned 404")
            if status in RETRYABLE_STATUS:
                last_exc = FetchError(f"HTTP {status} from {url}")
                if attempt >= self.max_retries:
                    raise last_exc
                self._backoff(attempt)
                continue
            if status >= 400:
                raise FetchError(f"HTTP {status} from {url}")
            return resp

        raise FetchError(f"exhausted retries for {url}") from last_exc

    def _backoff(self, attempt: int) -> None:
        """2s, 4s, 8s, 16s, with jitter so parallel runs don't resonate."""
        delay = (2.0 ** (attempt + 1)) * (1.0 + random.random() * 0.25)
        self.sleep(delay)

    def close(self) -> None:
        if self.session is not None:
            self.session.close()

    def __enter__(self) -> "PoliteSession":
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()


def _host(url: str) -> str:
    from urllib.parse import urlparse

    return urlparse(url).netloc.lower()


def _looks_blocked(content: bytes) -> bool:
    head = content[:4096]
    return any(marker in head for marker in BLOCK_MARKERS)
