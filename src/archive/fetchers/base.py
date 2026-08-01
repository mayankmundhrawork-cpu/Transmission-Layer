"""Fetcher base class: the only sanctioned bridge between network and archive.

A fetcher declares *what* documents exist and *where* they live. This class
handles the parts that must be identical everywhere: cache-before-network,
ledger-every-attempt, and stop-the-run-on-block.

The cache rule is the load-bearing one. `fetch()` never touches the network for
a document already in the archive unless explicitly forced, so re-running a
three-year backfill is a few hundred SQLite lookups rather than a few hundred
requests into a rate limiter (§17 CP2: "re-fetch is a cache hit").
"""
from __future__ import annotations

import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Iterable, Mapping, Sequence

from src.archive.http import FetchError, NotFound, PoliteSession, SourceBlocked
from src.archive.store import Archive, ArchiveEntry


class SkipDocument(FetchError):
    """This document is legitimately absent (trading holiday, pre-listing).

    Logged as `skipped`, which keeps holidays out of the failure count.
    """


@dataclass
class FetchSummary:
    """Outcome tally for a batch fetch, for CP2 reporting and the dashboard."""

    source: str
    ok: int = 0
    cache_hits: int = 0
    skipped: int = 0
    failed: int = 0
    blocked: bool = False
    errors: list[tuple[str, str]] = field(default_factory=list)

    @property
    def attempted(self) -> int:
        return self.ok + self.cache_hits + self.skipped + self.failed

    def __str__(self) -> str:
        base = (
            f"{self.source}: {self.ok} fetched, {self.cache_hits} cached, "
            f"{self.skipped} skipped, {self.failed} failed"
        )
        return base + " [BLOCKED — run halted]" if self.blocked else base


class ArchiveFetcher(ABC):
    """Fetch documents into the archive, politely and idempotently."""

    #: Archive namespace, e.g. ``"nse.bhavcopy"``. Documents are keyed
    #: ``(source, doc_key)``.
    source: str = ""
    #: Homepage hit once per session to acquire cookies. None to skip priming.
    home_url: str | None = None

    def __init__(
        self,
        archive: Archive,
        session: PoliteSession | None = None,
        *,
        min_interval_s: float = 2.0,
        max_retries: int = 4,
    ) -> None:
        if not self.source:
            raise ValueError(f"{type(self).__name__} must declare a source name")
        self.archive = archive
        self.session = session or PoliteSession(
            min_interval_s=min_interval_s, max_retries=max_retries
        )

    # -- subclass contract -------------------------------------------------

    @abstractmethod
    def urls_for(self, doc_key: str) -> Sequence[str]:
        """Candidate URLs for a document, in preference order.

        A sequence rather than a single URL because NSE has changed its archive
        layout several times; a 2012 bhavcopy and a 2025 one live at different
        paths under different filename conventions, and the fetcher should try
        the plausible ones rather than make the caller know which era it is in.
        """

    def headers_for(self, doc_key: str) -> Mapping[str, str]:
        return {}

    def validate(self, content: bytes, doc_key: str) -> None:
        """Reject bytes that are technically a 200 but not the document.

        Sources return HTML error pages with 200 status more often than is
        polite. Subclasses should assert the shape they expect; a bad document
        archived as good poisons everything downstream.
        """
        if not content:
            raise SkipDocument(f"{self.source} {doc_key}: empty response")

    def meta_for(self, doc_key: str, url: str) -> dict[str, Any]:
        """Extra provenance stored alongside the entry."""
        return {}

    # -- fetching ----------------------------------------------------------

    def is_cached(self, doc_key: str) -> bool:
        return self.archive.has(self.source, doc_key)

    def cached_bytes(self, doc_key: str) -> bytes | None:
        entry = self.archive.latest_entry(self.source, doc_key)
        return self.archive.read_entry(entry) if entry else None

    def fetch(self, doc_key: str, *, force: bool = False) -> ArchiveEntry | None:
        """Archive one document. Returns None if it could not be obtained.

        Raises :class:`SourceBlocked` — and only that — to signal the caller
        should stop entirely rather than continue into a ban.
        """
        if not force and self.is_cached(doc_key):
            self.archive.log_attempt(
                source=self.source, doc_key=doc_key, outcome="cache_hit"
            )
            return self.archive.latest_entry(self.source, doc_key)

        urls = list(self.urls_for(doc_key))
        if not urls:
            self.archive.log_attempt(
                source=self.source, doc_key=doc_key, outcome="skipped",
                error="no candidate URLs",
            )
            return None

        last_error: Exception | None = None
        for url in urls:
            started = time.monotonic()
            try:
                resp = self.session.get(
                    url,
                    headers=self.headers_for(doc_key),
                    prime_url=self.home_url,
                )
                content = resp.content
                self.validate(content, doc_key)
            except SourceBlocked as exc:
                self.archive.log_attempt(
                    source=self.source, doc_key=doc_key, url=url, outcome="blocked",
                    error=str(exc), duration_ms=_ms(started),
                )
                raise
            except (NotFound, SkipDocument) as exc:
                # Try the next candidate URL — a 404 on the modern path is the
                # normal signal that this date belongs to an older layout.
                last_error = exc
                continue
            except FetchError as exc:
                last_error = exc
                self.archive.log_attempt(
                    source=self.source, doc_key=doc_key, url=url,
                    outcome="network_error", error=str(exc), duration_ms=_ms(started),
                )
                continue

            entry = self.archive.put(
                source=self.source,
                doc_key=doc_key,
                url=url,
                content=content,
                headers={k: v for k, v in resp.headers.items()},
                http_status=resp.status_code,
                meta=self.meta_for(doc_key, url),
            )
            self.archive.log_attempt(
                source=self.source, doc_key=doc_key, url=url, outcome="ok",
                http_status=resp.status_code, entry_id=entry.entry_id,
                duration_ms=_ms(started),
            )
            return entry

        outcome = "skipped" if isinstance(last_error, (NotFound, SkipDocument)) else "http_error"
        self.archive.log_attempt(
            source=self.source, doc_key=doc_key, url=urls[-1], outcome=outcome,
            error=str(last_error) if last_error else "all candidate URLs failed",
        )
        return None

    def fetch_many(
        self, doc_keys: Iterable[str], *, force: bool = False,
        on_progress: Any = None,
    ) -> FetchSummary:
        """Fetch a batch, halting immediately on a block."""
        summary = FetchSummary(source=self.source)
        for key in doc_keys:
            was_cached = not force and self.is_cached(key)
            try:
                entry = self.fetch(key, force=force)
            except SourceBlocked as exc:
                summary.blocked = True
                summary.errors.append((key, str(exc)))
                break
            if entry is None:
                # Distinguish "nothing there" from "we failed" via the ledger.
                last = self.archive.attempts(source=self.source)
                outcome = last[-1]["outcome"] if last else "http_error"
                if outcome == "skipped":
                    summary.skipped += 1
                else:
                    summary.failed += 1
                    summary.errors.append((key, str(last[-1]["error"]) if last else ""))
            elif was_cached:
                summary.cache_hits += 1
            else:
                summary.ok += 1
            if on_progress is not None:
                on_progress(key, summary)
        return summary


def _ms(started: float) -> int:
    return int((time.monotonic() - started) * 1000)
