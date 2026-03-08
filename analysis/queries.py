import duckdb
import os


def load_top_tracks(csv_path):
    if not csv_path:
        raise ValueError("No CSV path was provided.")

    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    query = """
        SELECT *
        FROM read_csv_auto(?)
    """
    return duckdb.execute(query, [csv_path]).fetchdf()


def top_streamed(df, limit=20):
    required_cols = {"title", "artist", "streams"}
    missing = required_cols - set(df.columns)

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df["streams"] = df["streams"].astype(str).str.replace(",", "", regex=False)
    df["streams"] = df["streams"].astype(float)

    return (
        df.sort_values("streams", ascending=False)
        .head(limit)[["title", "artist", "streams"]]
    )