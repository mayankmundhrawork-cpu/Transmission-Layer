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


def serve(port: int) -> threading.Thread:
    import uvicorn

    from src.dashboard.app import create_app

    config = uvicorn.Config(create_app(), host=HOST, port=port, log_level="warning")
    server = uvicorn.Server(config)
    thread = threading.Thread(target=server.run, daemon=True, name="dashboard")
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
        print("the dashboard did not start in time", file=sys.stderr)
        return 1
    print(f"{TITLE} running at {url}", file=sys.stderr)

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
