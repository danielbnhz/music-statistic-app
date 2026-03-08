import duckdb
import pandas as pd


def load_top_tracks(csv_path):
    query = "SELECT * FROM read_csv_auto(?)"
    return duckdb.execute(query, [csv_path]).fetchdf()


def top_streamed(df, limit=20):
    df = df.copy()

    df["streams"] = (
        df["streams"]
        .astype(str)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    return (
        df.sort_values("streams", ascending=False)
        .head(limit)[["title", "artist", "streams"]]
    )