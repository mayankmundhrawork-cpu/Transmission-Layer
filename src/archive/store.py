"""Immutable, content-addressed document archive (BUILD_SPEC §3.4, §5).

The archive is the bottom of the stack. Everything above it — the bitemporal
store, factors, evaluation — derives from these bytes, so a result is
reproducible from a git commit plus an archive snapshot and nothing else.

Two properties carry the weight:

**Append-only.** A fetcher may add entries; nothing may modify or remove one.
This is enforced by SQLite triggers that ABORT on UPDATE and DELETE, not by
convention. Re-fetching a document on a later date creates a *new* entry with
its own `fetched_at`, even when the bytes are identical — the archive records
what we saw and when we saw it, and that history is the audit trail.

**Content-addressed.** Blobs live at `blobs/<aa>/<sha256>` and are written
once, then chmod'd read-only. Identical bytes fetched twice occupy one blob
and two entries, which is exactly the intended relationship between content
and observation.

The `fetch_ledger` records *every* attempt including failures, blocks, and
cache hits. A gap in the bhavcopy series should be explainable from the ledger
without re-running anything.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import sqlite3
import stat
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Iterator, Mapping

UTC = dt.timezone.utc

# Outcomes recorded in the fetch ledger. Closed set: an unrecognised outcome is
# a programming error, not a new category to be invented at a call site.
OUTCOMES = frozenset({
    "ok",             # fetched and archived
    "cache_hit",      # already archived, no request made
    "http_error",     # server returned a non-2xx we understand
    "blocked",        # source actively refused us (NSE anti-bot). Do NOT retry.
    "network_error",  # DNS/TLS/timeout
    "empty",          # 2xx but zero-length or a known "no data" sentinel
    "parse_error",    # bytes archived but unusable
    "skipped",        # deliberately not attempted (holiday, out of range)
})


class ArchiveError(RuntimeError):
    """Raised on archive misuse — including any attempt to mutate it."""


@dataclass(frozen=True)
class ArchiveEntry:
    """One observation of one document at one instant."""

    entry_id: int
    source: str
    doc_key: str
    url: str
    content_hash: str
    content_bytes: int
    fetched_at: dt.datetime
    http_status: int | None
    headers: dict[str, str]
    meta: dict[str, Any]


_SCHEMA = """
PRAGMA journal_mode=WAL;

CREATE TABLE IF NOT EXISTS archive_entry (
    entry_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    source        TEXT    NOT NULL,
    doc_key       TEXT    NOT NULL,
    url           TEXT    NOT NULL,
    content_hash  TEXT    NOT NULL,
    content_bytes INTEGER NOT NULL,
    fetched_at    TEXT    NOT NULL,
    http_status   INTEGER,
    headers_json  TEXT    NOT NULL DEFAULT '{}',
    meta_json     TEXT    NOT NULL DEFAULT '{}'
);
CREATE INDEX IF NOT EXISTS ix_entry_source_key ON archive_entry(source, doc_key);
CREATE INDEX IF NOT EXISTS ix_entry_hash       ON archive_entry(content_hash);
CREATE INDEX IF NOT EXISTS ix_entry_fetched    ON archive_entry(fetched_at);

CREATE TABLE IF NOT EXISTS fetch_ledger (
    attempt_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    source       TEXT    NOT NULL,
    doc_key      TEXT    NOT NULL,
    url          TEXT    NOT NULL DEFAULT '',
    attempted_at TEXT    NOT NULL,
    outcome      TEXT    NOT NULL,
    http_status  INTEGER,
    entry_id     INTEGER,
    error        TEXT,
    duration_ms  INTEGER
);
CREATE INDEX IF NOT EXISTS ix_ledger_source_key ON fetch_ledger(source, doc_key);
CREATE INDEX IF NOT EXISTS ix_ledger_outcome    ON fetch_ledger(outcome);

-- §3.4 enforcement. Convention is not enforcement; a trigger is.
CREATE TRIGGER IF NOT EXISTS archive_entry_no_update
    BEFORE UPDATE ON archive_entry
BEGIN SELECT RAISE(ABORT, 'archive is append-only: archive_entry cannot be updated'); END;

CREATE TRIGGER IF NOT EXISTS archive_entry_no_delete
    BEFORE DELETE ON archive_entry
BEGIN SELECT RAISE(ABORT, 'archive is append-only: archive_entry cannot be deleted'); END;

CREATE TRIGGER IF NOT EXISTS fetch_ledger_no_update
    BEFORE UPDATE ON fetch_ledger
BEGIN SELECT RAISE(ABORT, 'fetch ledger is append-only'); END;

CREATE TRIGGER IF NOT EXISTS fetch_ledger_no_delete
    BEFORE DELETE ON fetch_ledger
BEGIN SELECT RAISE(ABORT, 'fetch ledger is append-only'); END;
"""


def utc_now() -> dt.datetime:
    return dt.datetime.now(tz=UTC)


def iso(ts: dt.datetime) -> str:
    """UTC ISO-8601 with a trailing Z. Naive datetimes are rejected rather than
    assumed local — a silently-localised fetch timestamp is a look-ahead bug
    waiting for a timezone change."""
    if ts.tzinfo is None:
        raise ArchiveError("timestamps must be timezone-aware (UTC)")
    return ts.astimezone(UTC).isoformat(timespec="microseconds").replace("+00:00", "Z")


def parse_iso(text: str) -> dt.datetime:
    return dt.datetime.fromisoformat(text.replace("Z", "+00:00")).astimezone(UTC)


def content_hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class Archive:
    """Append-only document store rooted at a directory."""

    def __init__(self, root: Path) -> None:
        self.root = Path(root)
        self.blob_dir = self.root / "blobs"
        self.db_path = self.root / "archive.sqlite"
        self.blob_dir.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(self.db_path, isolation_level=None)
        self._conn.row_factory = sqlite3.Row
        self._conn.executescript(_SCHEMA)

    # -- lifecycle ---------------------------------------------------------

    def close(self) -> None:
        self._conn.close()

    def __enter__(self) -> "Archive":
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    # -- blob layer --------------------------------------------------------

    def blob_path(self, hash_: str) -> Path:
        return self.blob_dir / hash_[:2] / hash_

    def _write_blob(self, data: bytes) -> str:
        """Write bytes at their content address. Idempotent by construction:
        if the file exists, the bytes are already identical."""
        h = content_hash(data)
        path = self.blob_path(h)
        if path.exists():
            return h
        path.parent.mkdir(parents=True, exist_ok=True)
        # Write to a temp name then rename, so a crash mid-write cannot leave a
        # truncated blob sitting at a valid content address.
        tmp = path.with_suffix(".tmp")
        tmp.write_bytes(data)
        os.replace(tmp, path)
        # Read-only: makes accidental mutation an OSError rather than a silent
        # corruption of everything derived from this document.
        try:
            path.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
        except OSError:
            pass  # some filesystems (and Windows under some ACLs) refuse; not fatal
        return h

    def read(self, hash_: str) -> bytes:
        path = self.blob_path(hash_)
        if not path.exists():
            raise ArchiveError(f"blob {hash_} missing from archive at {self.root}")
        data = path.read_bytes()
        actual = content_hash(data)
        if actual != hash_:
            raise ArchiveError(
                f"archive corruption: blob at {path} hashes to {actual}, expected {hash_}"
            )
        return data

    def read_entry(self, entry: ArchiveEntry) -> bytes:
        return self.read(entry.content_hash)

    # -- writes ------------------------------------------------------------

    def put(
        self,
        *,
        source: str,
        doc_key: str,
        url: str,
        content: bytes,
        headers: Mapping[str, str] | None = None,
        http_status: int | None = None,
        meta: Mapping[str, Any] | None = None,
        fetched_at: dt.datetime | None = None,
    ) -> ArchiveEntry:
        """Archive one observation. Always creates a new entry (§3.4)."""
        if not source or not doc_key:
            raise ArchiveError("source and doc_key are required")
        ts = fetched_at or utc_now()
        h = self._write_blob(content)
        cur = self._conn.execute(
            "INSERT INTO archive_entry"
            " (source, doc_key, url, content_hash, content_bytes, fetched_at,"
            "  http_status, headers_json, meta_json)"
            " VALUES (?,?,?,?,?,?,?,?,?)",
            (
                source, doc_key, url, h, len(content), iso(ts), http_status,
                json.dumps(dict(headers or {}), sort_keys=True),
                json.dumps(dict(meta or {}), sort_keys=True, default=str),
            ),
        )
        return self._entry(int(cur.lastrowid))

    def log_attempt(
        self,
        *,
        source: str,
        doc_key: str,
        outcome: str,
        url: str = "",
        http_status: int | None = None,
        entry_id: int | None = None,
        error: str | None = None,
        duration_ms: int | None = None,
        attempted_at: dt.datetime | None = None,
    ) -> int:
        """Record a fetch attempt — including the ones that failed. A gap in the
        data should always be explainable from this table."""
        if outcome not in OUTCOMES:
            raise ArchiveError(f"unknown outcome {outcome!r}; expected one of {sorted(OUTCOMES)}")
        cur = self._conn.execute(
            "INSERT INTO fetch_ledger"
            " (source, doc_key, url, attempted_at, outcome, http_status, entry_id, error, duration_ms)"
            " VALUES (?,?,?,?,?,?,?,?,?)",
            (
                source, doc_key, url, iso(attempted_at or utc_now()), outcome,
                http_status, entry_id, error, duration_ms,
            ),
        )
        return int(cur.lastrowid)

    # -- reads -------------------------------------------------------------

    def _entry(self, entry_id: int) -> ArchiveEntry:
        row = self._conn.execute(
            "SELECT * FROM archive_entry WHERE entry_id = ?", (entry_id,)
        ).fetchone()
        if row is None:
            raise ArchiveError(f"no archive entry {entry_id}")
        return _row_to_entry(row)

    def has(self, source: str, doc_key: str) -> bool:
        row = self._conn.execute(
            "SELECT 1 FROM archive_entry WHERE source = ? AND doc_key = ? LIMIT 1",
            (source, doc_key),
        ).fetchone()
        return row is not None

    def latest_entry(self, source: str, doc_key: str) -> ArchiveEntry | None:
        """The most recent observation of a document. `fetched_at` first, then
        `entry_id` — two fetches in the same microsecond still order."""
        row = self._conn.execute(
            "SELECT * FROM archive_entry WHERE source = ? AND doc_key = ?"
            " ORDER BY fetched_at DESC, entry_id DESC LIMIT 1",
            (source, doc_key),
        ).fetchone()
        return _row_to_entry(row) if row else None

    def entries(
        self,
        source: str | None = None,
        doc_key: str | None = None,
        since: dt.datetime | None = None,
    ) -> list[ArchiveEntry]:
        sql = "SELECT * FROM archive_entry WHERE 1=1"
        args: list[Any] = []
        if source is not None:
            sql += " AND source = ?"
            args.append(source)
        if doc_key is not None:
            sql += " AND doc_key = ?"
            args.append(doc_key)
        if since is not None:
            sql += " AND fetched_at >= ?"
            args.append(iso(since))
        sql += " ORDER BY entry_id"
        return [_row_to_entry(r) for r in self._conn.execute(sql, args)]

    def doc_keys(self, source: str) -> list[str]:
        return [
            r["doc_key"]
            for r in self._conn.execute(
                "SELECT DISTINCT doc_key FROM archive_entry WHERE source = ? ORDER BY doc_key",
                (source,),
            )
        ]

    def iter_documents(self, source: str) -> Iterator[tuple[ArchiveEntry, bytes]]:
        """Latest observation of every document from a source, key order."""
        for key in self.doc_keys(source):
            entry = self.latest_entry(source, key)
            if entry is not None:
                yield entry, self.read_entry(entry)

    def attempts(
        self, source: str | None = None, outcome: str | None = None
    ) -> list[sqlite3.Row]:
        sql = "SELECT * FROM fetch_ledger WHERE 1=1"
        args: list[Any] = []
        if source is not None:
            sql += " AND source = ?"
            args.append(source)
        if outcome is not None:
            sql += " AND outcome = ?"
            args.append(outcome)
        sql += " ORDER BY attempt_id"
        return list(self._conn.execute(sql, args))

    def stats(self) -> dict[str, Any]:
        """Archive summary for the dashboard and for CP2 verification."""
        by_source = {
            r["source"]: {"entries": r["n"], "documents": r["docs"], "bytes": r["b"]}
            for r in self._conn.execute(
                "SELECT source, COUNT(*) n, COUNT(DISTINCT doc_key) docs,"
                " COALESCE(SUM(content_bytes),0) b FROM archive_entry GROUP BY source"
            )
        }
        outcomes = {
            r["outcome"]: r["n"]
            for r in self._conn.execute(
                "SELECT outcome, COUNT(*) n FROM fetch_ledger GROUP BY outcome"
            )
        }
        totals = self._conn.execute(
            "SELECT COUNT(*) n, COUNT(DISTINCT content_hash) blobs,"
            " COALESCE(SUM(content_bytes),0) b FROM archive_entry"
        ).fetchone()
        return {
            "root": str(self.root),
            "entries": totals["n"],
            "distinct_blobs": totals["blobs"],
            "bytes": totals["b"],
            "by_source": by_source,
            "ledger_outcomes": outcomes,
        }

    def verify(self, limit: int | None = None) -> list[str]:
        """Re-hash stored blobs and report any that no longer match. Empty list
        means the archive is intact."""
        problems: list[str] = []
        rows = self._conn.execute(
            "SELECT DISTINCT content_hash FROM archive_entry ORDER BY content_hash"
            + (f" LIMIT {int(limit)}" if limit else "")
        )
        for row in rows:
            h = row["content_hash"]
            try:
                self.read(h)
            except ArchiveError as exc:
                problems.append(str(exc))
        return problems


def _row_to_entry(row: sqlite3.Row) -> ArchiveEntry:
    return ArchiveEntry(
        entry_id=row["entry_id"],
        source=row["source"],
        doc_key=row["doc_key"],
        url=row["url"],
        content_hash=row["content_hash"],
        content_bytes=row["content_bytes"],
        fetched_at=parse_iso(row["fetched_at"]),
        http_status=row["http_status"],
        headers=json.loads(row["headers_json"]),
        meta=json.loads(row["meta_json"]),
    )


def open_archive(root: Path | None = None) -> Archive:
    """Open the configured archive."""
    if root is None:
        from src.config import get_config

        root = get_config().archive_dir
    return Archive(root)
