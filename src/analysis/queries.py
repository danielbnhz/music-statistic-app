import duckdb
import pandas as pd


def load_top_tracks(csv_path):
    """
    Load dataset using DuckDB.
    """
    query = """
        SELECT *
        FROM read_csv_auto(?)
    """

    df = duckdb.query(query, [csv_path]).to_df()
    return df


def top_streamed(df, limit=20):
    """
    Return most streamed tracks.
    """
    return (
        df.sort_values("streams", ascending=False)
        .head(limit)
        [["title", "artist", "streams"]]
    )