# import json
# import random
# from faker import Faker
# from datetime import timedelta

# fake = Faker()
# Faker.seed(42)

# video_ids = [f"vid00{i}" for i in range(1, 11)]  # e.g., 10 video IDs
# user_ids = [f"u{str(i).zfill(3)}" for i in range(1, 101)]  # 100 users

# logs = []
# for _ in range(1000):
#     log = {
#         "user_id": random.choice(user_ids),
#         "video_id": random.choice(video_ids),
#         "watch_time_sec": random.randint(30, 600),
#         "watched_at": fake.date_time_between(start_date='-30d', end_date='now').isoformat()
#     }
#     logs.append(log)

# with open("data/logs/viewer_logs.json", "w") as f:
#     json.dump(logs, f, indent=2)

# print("✅ viewer_logs.json generated with 1000 records.")

import json
import random
import pandas as pd
from faker import Faker

fake = Faker()
Faker.seed(42)

# ✅ Load real video IDs
yt_df = pd.read_csv("data/processed/youtube_data_with_summary.csv")
video_ids = yt_df["video_id"].dropna().tolist()

# ✅ Simulate users
user_ids = [f"u{str(i).zfill(3)}" for i in range(1, 101)]  # 100 users

logs = []
for _ in range(1000):  # 1000 watch logs
    log = {
        "user_id": random.choice(user_ids),
        "video_id": random.choice(video_ids),  # ✅ Real YouTube video IDs
        "watch_time_sec": random.randint(30, 600),
        "watched_at": fake.date_time_between(start_date='-30d', end_date='now').isoformat()
    }
    logs.append(log)

with open("data/logs/viewer_logs.json", "w") as f:
    json.dump(logs, f, indent=2)

print(f"✅ viewer_logs.json generated with {len(logs)} records using real video IDs.")