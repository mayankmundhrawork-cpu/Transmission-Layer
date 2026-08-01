"""Desktop launcher — runs the dashboard in a native window.

    python -m src.desktop.main

Starts the FastAPI app on a free localhost port in a background thread, then
opens a native webview window pointed at it. Falls back to the default browser
if pywebview is unavailable, so the same entry point works on a headless box
and in a frozen build.

Binds to 127.0.0.1 only. This process can read a research database and, with
LIVE_ENABLED, reach a broker; it has no business being reachable from the
network, and binding to localhost is the difference between a desktop app and
an unauthenticated internal service.
"""
from __future__ import annotations

import argparse
import contextlib
import socket
import sys
import threading
import time
from typing import Any

HOST = "127.0.0.1"
TITLE = "PIT Factor Research Platform"


def ensure_streams() -> "str | None":
    """Give the process real stdout/stderr before anything tries to write.

    A PyInstaller build with ``console=False`` — which is what makes this a
    desktop app rather than a terminal program — starts with
    ``sys.stdout is None`` and ``sys.stderr is None`` on Windows. Every
    ``print(..., file=sys.stderr)`` then raises
    ``AttributeError: 'NoneType' object has no attribute 'write'``, and uvicorn's
    logging does the same. The app dies before serving anything, and because it
    has no console there is nowhere for the traceback to appear: it fails
    silently and looks like it simply did not launch.

    So: point both streams at a log file next to the user's data, and fall back
    to devnull if even that cannot be opened. Returns the log path, which is
    worth telling the user about — it is the only diagnostic a windowed build
    has.
    """
    if sys.stdout is not None and sys.stderr is not None:
        return None

    import os
    from pathlib import Path

    log_path = None
    stream = None
    try:
        from src.config import _default_data_dir, REPO_ROOT

        directory = _default_data_dir(REPO_ROOT)
        directory.mkdir(parents=True, exist_ok=True)
        log_path = str(directory / "desktop.log")
        stream = open(log_path, "a", encoding="utf-8", buffering=1)
    except Exception:
        try:
            stream = open(os.devnull, "w", encoding="utf-8")
            log_path = None
        except Exception:
            return None

    if sys.stdout is None:
        sys.stdout = stream
    if sys.stderr is None:
        sys.stderr = stream
    return log_path


# Run before anything else can print. Import-time rather than inside main(),
# because argparse writes to stderr on a bad argument too.
_LOG_PATH = ensure_streams()


def free_port() -> int:
    with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind((HOST, 0))
        return int(s.getsockname()[1])


def wait_until_up(port: int, timeout: float = 45.0) -> bool:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
            s.settimeout(0.4)
            if s.connect_ex((HOST, port)) == 0:
                return True
        time.sleep(0.15)
    return False


#: Set by the server thread if it dies, so the main thread can report *why*
#: rather than only that the port never opened.
_SERVER_ERROR: list[BaseException] = []


def serve(port: int) -> threading.Thread:
    import uvicorn

    from src.dashboard.app import create_app

    config = uvicorn.Config(create_app(), host=HOST, port=port, log_level="warning")
    server = uvicorn.Server(config)

    def run() -> None:
        try:
            server.run()
        except BaseException as exc:  # noqa: BLE001 - the whole point is to see it
            _SERVER_ERROR.append(exc)
            import traceback

            traceback.print_exc(file=sys.stderr)

    thread = threading.Thread(target=run, daemon=True, name="dashboard")
    thread.start()
    return thread


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m src.desktop.main",
                                     description=TITLE)
    parser.add_argument("--port", type=int, default=0, help="0 picks a free port")
    parser.add_argument("--browser", action="store_true",
                        help="open in the default browser instead of a native window")
    parser.add_argument("--no-window", action="store_true",
                        help="serve only; do not open any UI")
    args = parser.parse_args(argv)

    # Ensure the data directories exist before the UI asks about them, so a
    # first run shows "no store yet" rather than a stack trace.
    try:
        from src.config import get_config

        get_config().ensure_dirs()
    except Exception as exc:
        print(f"configuration error: {exc}", file=sys.stderr)
        return 2

    port = args.port or free_port()
    serve(port)
    url = f"http://{HOST}:{port}/"

    if not wait_until_up(port):
        if _SERVER_ERROR:
            print(f"the dashboard failed to start: {_SERVER_ERROR[0]!r}",
                  file=sys.stderr)
        else:
            print("the dashboard did not start in time", file=sys.stderr)
        return 1
    print(f"{TITLE} running at {url}", file=sys.stderr)
    if _LOG_PATH:
        print(f"log: {_LOG_PATH}", file=sys.stderr)

    if args.no_window:
        try:
            while True:
                time.sleep(3600)
        except KeyboardInterrupt:
            return 0

    if not args.browser:
        try:
            import webview  # pywebview

            webview.create_window(TITLE, url, width=1360, height=900,
                                  min_size=(900, 600))
            webview.start()
            return 0
        except Exception as exc:
            print(f"native window unavailable ({exc}); falling back to the browser",
                  file=sys.stderr)

    import webbrowser

    webbrowser.open(url)
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
