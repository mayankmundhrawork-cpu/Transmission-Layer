"""Synthetic-but-faithful source documents for offline tests.

Each fixture reproduces the real file's quirks, because the quirks are what
break parsers: the legacy bhavcopy's trailing comma, the security-wise file's
space-padded headers and turnover-in-lakhs, UDiFF's all-segments rows that must
be filtered down to cash equities.
"""
from __future__ import annotations

import io
import zipfile

# --- NSE bhavcopy: legacy layout (to ~2020-07) ------------------------------
# Note the trailing comma on every line — the real file has it.
BHAVCOPY_LEGACY = (
    b"SYMBOL,SERIES,OPEN,HIGH,LOW,CLOSE,LAST,PREVCLOSE,TOTTRDQTY,TOTTRDVAL,"
    b"TIMESTAMP,TOTALTRADES,ISIN,\n"
    b"RELIANCE,EQ,1000.00,1020.00,995.00,1015.50,1015.00,998.00,1000000,1015500000.00,"
    b"15-JAN-2015,45000,INE002A01018,\n"
    b"TINYCO,BE,12.00,12.50,11.80,12.10,12.10,12.00,50000,605000.00,"
    b"15-JAN-2015,300,INE999Z01011,\n"
    b"SOMEBOND,N1,100.00,100.00,100.00,100.00,100.00,100.00,10,1000.00,"
    b"15-JAN-2015,1,INE888Y01012,\n"
    b"SUSPENDCO,EQ,0.00,0.00,0.00,0.00,0.00,5.00,0,0.00,"
    b"15-JAN-2015,0,INE777X01013,\n"
)

# --- NSE bhavcopy: security-wise full (2020→), turnover in ₹ lakhs ----------
BHAVCOPY_SECWISE = (
    b"SYMBOL, SERIES, DATE1, PREV_CLOSE, OPEN_PRICE, HIGH_PRICE, LOW_PRICE, "
    b"LAST_PRICE, CLOSE_PRICE, AVG_PRICE, TTL_TRD_QNTY, TURNOVER_LACS, "
    b"NO_OF_TRADES, DELIV_QTY, DELIV_PER\n"
    b"RELIANCE, EQ, 15-JAN-2021, 1998.00, 2000.00, 2020.00, 1995.00, 2015.00, "
    b"2015.50, 2010.00, 1000000, 20155.00, 45000, 400000, 40.00\n"
    b"TINYCO, BE, 15-JAN-2021, 12.00, 12.00, 12.50, 11.80, 12.10, 12.10, 12.05, "
    b"50000, 6.05, 300, 45000, 90.00\n"
)

# --- NSE bhavcopy: UDiFF (2024-07→), all segments in one file ---------------
_UDIFF_HEADER = (
    "TradDt,BizDt,Sgmt,Src,FinInstrmTp,FinInstrmId,ISIN,TckrSymb,SctySrs,XpryDt,"
    "FininstrmActlXpryDt,StrkPric,OptnTp,FinInstrmNm,OpnPric,HghPric,LwPric,"
    "ClsPric,LastPric,PrvsClsgPric,UndrlygPric,SttlmPric,OpnIntrst,"
    "ChngInOpnIntrst,TtlTradgVol,TtlTrfVal,TtlNbOfTxsExctd,SsnId,NewBrdLotQty,"
    "Rmks,Rsvd1,Rsvd2,Rsvd3,Rsvd4"
)
_UDIFF_ROWS = [
    # cash equity — should survive the filter
    "2024-07-05,2024-07-05,CM,NSE,STK,2885,INE002A01018,RELIANCE,EQ,,,,,RELIANCE,"
    "3100.00,3150.00,3090.00,3140.00,3139.00,3095.00,,3140.00,,,2000000,"
    "6280000000.00,90000,F1,1,,,,,",
    "2024-07-05,2024-07-05,CM,NSE,STK,9999,INE999Z01011,TINYCO,BE,,,,,TINYCO,"
    "20.00,21.00,19.50,20.50,20.50,20.00,,20.50,,,80000,1640000.00,500,F1,1,,,,,",
    # derivative in the same file — must be filtered OUT
    "2024-07-05,2024-07-05,FO,NSE,IDF,53001,,NIFTY,,2024-07-25,2024-07-25,0,XX,"
    "NIFTY24JUL,24000.00,24200.00,23900.00,24100.00,24100.00,23950.00,24100.00,"
    "24100.00,1000,50,500000,12000000000.00,20000,F1,25,,,,,",
]
BHAVCOPY_UDIFF = ("\n".join([_UDIFF_HEADER, *_UDIFF_ROWS]) + "\n").encode()


def zipped(content: bytes, name: str = "bhav.csv") -> bytes:
    """Wrap CSV bytes in a zip, the way NSE ships bhavcopies."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(name, content)
    return buf.getvalue()


HTML_BLOCK_PAGE = (
    b"<!DOCTYPE html><html><head><title>Access Denied</title></head>"
    b"<body>You don't have permission to access this resource.</body></html>"
)

HTML_ERROR_PAGE = b"<!DOCTYPE html><html><body>Resource not available</body></html>"
