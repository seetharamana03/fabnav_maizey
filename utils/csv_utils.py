import pandas as pd

def load_dataset(path):
    return pd.read_csv(path)

def validate_columns(df):
    # Normalize column names to lowercase so callers can safely use
    # `row["input"]` and `row["output"]` regardless of CSV header casing.
    df.columns = [c.lower() for c in df.columns]
    if "input" not in df.columns or "output" not in df.columns:
        raise ValueError("Dataset must contain 'input' and 'output' columns.")
    return df
    
#Keeps dataset handling separate from evaluation logic