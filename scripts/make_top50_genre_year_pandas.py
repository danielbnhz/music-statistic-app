import duckdb

input_csv = "data/spotify_charts.csv"
output_csv = "data/top50_global.csv"

duckdb.execute("""
COPY (
    SELECT
        title,
        artist,
        rank,
        date,
        region,
        streams
    FROM read_csv_auto(?)
    WHERE rank <= 50
    AND region = 'Global'
) TO ? (HEADER, DELIMITER ',');
""", [input_csv, output_csv])