import os
import json
import pandas as pd 
from googleapiclient.discovery import build
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

CHANNNEL_ID = "UCX6OQ3DkcsbYNE6H8uQQuVA"

def fetch_youtube_videos(channel_id, max_results=50):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey = API_KEY)

    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults= max_results,
        order="date",
        type="video"
    )
    response = request.execute()

    videos = []
    for item in response.get("items", []):
        video_id = item['id']["videoId"]
        title = item["snippet"]["title"]
        published_at = item["snippet"]["publishedAt"]
        description = item["snippet"]["description"]
        videos.append({
            "video_id": video_id,
            "title" : title,
            "description" : description,
            "published_at" : published_at
        })

    return videos

if __name__ == "__main__":
    print("Fetching video metadata.....")
    video_data = fetch_youtube_videos(CHANNNEL_ID)

    os.makedirs("data/raw", exist_ok=True)
    with open("data/raw/youtube_data.json", "w") as f:
        json.dump(video_data, f, indent=2)

    df = pd.DataFrame(video_data)
    df.to_csv("data/raw/youtube_data.csv", index=False)

    print(f"Fetched {len(video_data)} videos and saved")