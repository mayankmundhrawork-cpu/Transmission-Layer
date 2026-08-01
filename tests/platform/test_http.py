"""Polite-session tests (§5).

The behaviour worth defending: a *block* must not be retried. Backing off and
trying again after a 403 is how a soft rate-limit becomes a multi-day ban, and
it is the failure that costs the most to recover from.
"""
from __future__ import annotations

import pytest
import requests

from src.archive.http import (
    FetchError, NotFound, PoliteSession, RateLimiter, SourceBlocked,
)
from tests.platform.fixtures import HTML_BLOCK_PAGE


class FakeResponse:
    def __init__(self, status_code=200, content=b"ok", headers=None):
        self.status_code = status_code
        self.content = content
        self.headers = headers or {}
        self.text = content.decode("utf-8", "replace")


class FakeSession:
    """Scripted responses; records every URL requested."""

    def __init__(self, responses):
        self._responses = list(responses)
        self.calls = []
        self.headers = {}

    def get(self, url, **kwargs):
        self.calls.append(url)
        if not self._responses:
            raise AssertionError(f"unexpected extra request to {url}")
        item = self._responses.pop(0)
        if isinstance(item, Exception):
            raise item
        return item

    def close(self):
        pass


@pytest.fixture
def slept():
    """Collect sleep durations instead of actually waiting."""
    return []


def make_session(responses, slept, **kw):
    fake = FakeSession(responses)
    return PoliteSession(session=fake, sleep=slept.append, min_interval_s=0.0, **kw)


# --- blocking ---------------------------------------------------------------

@pytest.mark.parametrize("status", [401, 403])
def test_block_status_raises_immediately_without_retry(status, slept):
    sess = make_session([FakeResponse(status_code=status)], slept, max_retries=4)
    with pytest.raises(SourceBlocked):
        sess.get("https://www.nseindia.com/api/x")
    assert len(sess.session.calls) == 1, "a block must not be retried"
    assert slept == [], "a block must not trigger backoff"


def test_block_page_with_200_status_is_still_a_block(slept):
    """NSE serves its refusal as a 200 with an HTML body. Status alone is not
    enough to tell success from denial."""
    sess = make_session([FakeResponse(200, HTML_BLOCK_PAGE)], slept)
    with pytest.raises(SourceBlocked):
        sess.get("https://www.nseindia.com/api/x")


def test_block_message_explains_not_retrying(slept):
    sess = make_session([FakeResponse(403)], slept)
    with pytest.raises(SourceBlocked) as exc:
        sess.get("https://www.nseindia.com/api/x")
    assert "Not retrying" in str(exc.value)
    assert "archive keeps everything already fetched" in str(exc.value)


# --- retries ----------------------------------------------------------------

def test_transient_5xx_retries_then_succeeds(slept):
    sess = make_session(
        [FakeResponse(503), FakeResponse(502), FakeResponse(200, b"data")], slept
    )
    assert sess.get("https://x.test/a").content == b"data"
    assert len(sess.session.calls) == 3
    assert len(slept) == 2


def test_backoff_is_exponential(slept):
    sess = make_session(
        [FakeResponse(503), FakeResponse(503), FakeResponse(503), FakeResponse(200)],
        slept, max_retries=4,
    )
    sess.get("https://x.test/a")
    # 2s, 4s, 8s with up to +25% jitter
    assert 2.0 <= slept[0] < 2.5
    assert 4.0 <= slept[1] < 5.0
    assert 8.0 <= slept[2] < 10.0
    assert slept[0] < slept[1] < slept[2]


def test_retries_are_bounded(slept):
    sess = make_session([FakeResponse(503)] * 3, slept, max_retries=2)
    with pytest.raises(FetchError, match="503"):
        sess.get("https://x.test/a")
    assert len(sess.session.calls) == 3  # initial + 2 retries


def test_network_error_retries_then_raises(slept):
    err = requests.ConnectionError("dns")
    sess = make_session([err, err], slept, max_retries=1)
    with pytest.raises(FetchError, match="network error"):
        sess.get("https://x.test/a")


def test_404_is_not_found_not_an_error_to_retry(slept):
    sess = make_session([FakeResponse(404)], slept)
    with pytest.raises(NotFound):
        sess.get("https://x.test/a")
    assert slept == []


# --- priming ----------------------------------------------------------------

def test_prime_is_called_once_per_host(slept):
    sess = make_session(
        [FakeResponse(200, b"<html>home</html>"), FakeResponse(200, b"a"),
         FakeResponse(200, b"b")],
        slept,
    )
    sess.get("https://www.nseindia.com/api/1", prime_url="https://www.nseindia.com")
    sess.get("https://www.nseindia.com/api/2", prime_url="https://www.nseindia.com")
    assert sess.session.calls[0] == "https://www.nseindia.com"
    assert sess.session.calls.count("https://www.nseindia.com") == 1


def test_failed_prime_does_not_abort_the_request(slept):
    sess = make_session(
        [requests.ConnectionError("prime failed"), FakeResponse(200, b"data")], slept
    )
    assert sess.get("https://x.test/a", prime_url="https://x.test").content == b"data"


# --- rate limiting ----------------------------------------------------------

def test_rate_limiter_spaces_requests_per_host():
    slept, clock = [], iter([0.0, 0.0, 0.5, 0.5, 3.0, 3.0])
    limiter = RateLimiter(min_interval_s=2.0, sleep=slept.append, clock=lambda: next(clock))
    limiter.wait("a.test")            # first call: no wait
    assert limiter.wait("a.test") == pytest.approx(1.5)  # only 0.5s elapsed
    assert slept == [pytest.approx(1.5)]


def test_rate_limiter_tracks_hosts_independently():
    slept, ticks = [], iter([0.0, 0.0, 0.1, 0.1])
    limiter = RateLimiter(min_interval_s=2.0, sleep=slept.append, clock=lambda: next(ticks))
    limiter.wait("a.test")
    limiter.wait("b.test")
    assert slept == [], "a different host does not inherit the other's cooldown"
