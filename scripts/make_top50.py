import duckdb

duckdb.execute("""
COPY (
    SELECT
        title,
        rank,
        date,
        artist,
        url,
        region,
        chart,
        trend,
        streams
    FROM read_csv_auto('data/raw/charts.csv', HEADER=TRUE)
    WHERE rank <= 50
      AND region = 'Global'
) TO 'data/processed/top50_global.csv' (HEADER, DELIMITER ',', OVERWRITE 1);
""")

print("Done.")