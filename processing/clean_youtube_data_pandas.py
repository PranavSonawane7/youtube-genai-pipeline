import pandas as pd
import os

RAW_PATH = "data/raw/youtube_data.csv"
PROCESSED_PATH = "data/processed/youtube_data_cleaned_pandas.csv"
os.makedirs("data/processed", exist_ok=True)

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):

    df.dropna(subset=["video_id", "title"], inplace=True)

    df["published_at"] = pd.to_datetime(df["published_at"], errors="coerce")

    df = df[df["published_at"].notnull()]

    df["title"] = df["title"].str.strip()
    df["description"] = df["description"].fillna("").str.strip()

    return df

def save_data(df, path):
    df.to_csv(path, index=False)

if __name__ == "__main__":
    print("Loading raw data.....")
    df = load_data(RAW_PATH)
    print(f"Loaded {len(df)} records...")

    print("Cleaning data....")
    df_cleaned = clean_data(df)
    print(f"cleaned {len(df_cleaned)} records remaining...")

    print("Saving cleaned data...")
    save_data(df_cleaned, PROCESSED_PATH)
    print(f"saved to {PROCESSED_PATH}")

