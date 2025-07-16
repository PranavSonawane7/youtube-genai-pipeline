import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_absolute_error
import joblib

# Load merged data
yt_df = pd.read_csv("data/processed/youtube_data_with_summary.csv")
logs_df = pd.read_json("data/logs/viewer_logs.json")
merged_df = logs_df.merge(yt_df, on="video_id", how="inner")

# Features: title + description + gpt_summary_tags
merged_df["text_features"] = merged_df["title"].fillna("") + " " + merged_df["description"].fillna("") + " " + merged_df["gpt_summary_tags"].fillna("")

X = merged_df["text_features"]
y = merged_df["watch_time_sec"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pipeline: TF-IDF + RandomForest
model = make_pipeline(TfidfVectorizer(max_features=5000), RandomForestRegressor(n_estimators=100, random_state=42))
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
mae = mean_absolute_error(y_test, preds)
print(f"✅ MAE: {mae:.2f} seconds")

# Save model
joblib.dump(model, "ml/models/watch_time_predictor.pkl")
print("✅ Model saved at ml/models/watch_time_predictor.pkl")