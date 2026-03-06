from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

input_csv = os.getenv("RAW_CSV_PATH")

df = pd.read_csv(input_csv, nrows=5)

print(df.columns)