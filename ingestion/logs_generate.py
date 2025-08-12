import json
import random
import pandas as pd
from faker import Faker

fake = Faker()
Faker.seed(42)


yt_df = pd.read_csv("data/processed/youtube_data_with_summary.csv")
video_ids = yt_df["video_id"].dropna().tolist()


user_ids = [f"u{str(i).zfill(3)}" for i in range(1, 101)]  # 100 users

logs = []
for _ in range(1000):  
    log = {
        "user_id": random.choice(user_ids),
        "video_id": random.choice(video_ids),  
        "watch_time_sec": random.randint(30, 600),
        "watched_at": fake.date_time_between(start_date='-30d', end_date='now').isoformat()
    }
    logs.append(log)

with open("data/logs/viewer_logs.json", "w") as f:
    json.dump(logs, f, indent=2)

print(f"viewer_logs.json generated with {len(logs)} records using real video IDs.")
