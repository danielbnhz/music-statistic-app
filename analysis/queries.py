import duckdb
import pandas as pd


def load_top_tracks(csv_path):
    query = "SELECT * FROM read_csv_auto(?)"
    return duckdb.execute(query, [csv_path]).fetchdf()


def top_streamed(df, limit=20):
    df = df.copy()

    print("Raw streams sample:")
    print(df["streams"].head(20))

    df["streams"] = (
        df["streams"]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.strip()
    )

    df["streams"] = pd.to_numeric(df["streams"], errors="coerce")

    print("Null streams after conversion:", df["streams"].isna().sum())

    df = df.dropna(subset=["streams"])

    return (
        df.sort_values("streams", ascending=False)
        .head(limit)[["title", "artist", "streams"]]
    )