import pandas as pd

def load_catalog(path):
    return pd.read_csv(path)

def compress_catalog(df, keep_cols):
    df = df[keep_cols]
    return df.to_csv(index=False)

def truncate(text, max_chars=5000):
    return text[:max_chars]

#this solves token limit problem