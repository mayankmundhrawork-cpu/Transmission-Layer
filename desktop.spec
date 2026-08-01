# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller spec for the desktop build.

    pyinstaller desktop.spec --noconfirm

Produces `dist/PITFactorPlatform/` (onedir). Onedir rather than onefile: a
onefile build unpacks ~200MB of pandas/scipy/numpy to a temp directory on every
launch, which costs 10-20 seconds of cold start and confuses antivirus. The
Inno Setup installer packages the directory into a single .exe for
distribution, so the user still gets one file to download.
"""
import sys
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

datas = [
    ("src/dashboard/static", "src/dashboard/static"),
    ("src/costs/rates.yaml", "src/costs"),
    ("prereg", "prereg"),
    (".env.example", "."),
]
# scipy.stats and statsmodels reach for submodules dynamically; without these
# the deflated Sharpe and the Newey-West path fail only at runtime, in the
# frozen build, which is the worst place to find out.
hiddenimports = (
    collect_submodules("scipy.stats")
    + collect_submodules("scipy.special")
    # numpy 2.x imports several _core submodules dynamically (notably
    # numpy._core._exceptions), so the dependency graph misses them and the
    # frozen app dies with "Importing the numpy C-extensions failed" — a
    # message that sends you looking at your install rather than your spec.
    + collect_submodules("numpy._core")
    + ["uvicorn.logging", "uvicorn.loops.auto", "uvicorn.protocols.http.auto",
       "uvicorn.protocols.websockets.auto", "uvicorn.lifespan.on",
       "sqlite3", "pandas._libs.tslibs.base", "lxml._elementpath"]
)

a = Analysis(
    ["src/desktop/main.py"],
    pathex=["."],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    excludes=[
        # Nothing in this app draws with matplotlib or opens a Tk window; both
        # pull in tens of MB and slow the build.
        "matplotlib", "tkinter", "PyQt5", "PySide2", "notebook", "IPython",
        "pytest", "playwright",
        # Excluding setuptools is not size trimming. PyInstaller injects a
        # pkg_resources runtime hook whenever setuptools is importable, and on
        # modern setuptools that hook imports jaraco.context -> backports, which
        # is not bundled: the frozen app then dies at startup before running a
        # line of our code. Nothing here needs pkg_resources at runtime.
        "setuptools", "pkg_resources", "_distutils_hack",
        # NOTE: `distutils` is deliberately NOT excluded. Pruning it also
        # pruned parts of numpy's module graph and produced the same
        # C-extension import failure as above.
    ],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz, a.scripts, [],
    exclude_binaries=True,
    name="PITFactorPlatform",
    debug=False,
    strip=False,
    upx=False,           # UPX-packed binaries trip several AV engines
    console=False,       # native window, not a console app
    icon=None,
)
coll = COLLECT(
    exe, a.binaries, a.datas,
    strip=False, upx=False, name="PITFactorPlatform",
)
