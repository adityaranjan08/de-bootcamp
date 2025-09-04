import os, io, requests, pandas as pd
from datetime import datetime

URL = os.getenv("SOURCE_URL",)
OUT = os.getenv("OUT_PATH",)


def main():
    os.makedirs(OUT, exist_ok=True)
    r = requests.get(URL,timeout=30)
    r.raise_for_status()
    df = pd.read_csv(io.StringIO(r.text))

    # Basic cleaning
    for c in df.columns:
        if df[c].dtype == "object":
            df[c] = df[c].str.strip()