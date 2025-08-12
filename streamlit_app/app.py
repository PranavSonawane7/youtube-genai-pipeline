import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import joblib


MODEL_PATH = "ml/models/watch_time_predictor.pkl"
YOUTUBE_DATA_PATH = "data/processed/youtube_data_with_summary.csv"
VIEWER_LOGS_PATH = "data/logs/viewer_logs.json"


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


model = load_model()


@st.cache_data
def load_data():
    yt_df = pd.read_csv(YOUTUBE_DATA_PATH)
    logs_df = pd.read_json(VIEWER_LOGS_PATH)
    return yt_df, logs_df


def show_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)


def main():
    st.set_page_config(page_title="YouTube + Viewer Analytics Dashboard", layout="wide")
    st.title("📊 YouTube GenAI Dashboard with Viewer Analytics")


    yt_df, logs_df = load_data()


    st.subheader("🤖 Predict Watch Time for a Video")
    user_input_title = st.text_input("Enter video title:", key="video_title_input")
    user_input_desc = st.text_area("Enter video description:", key="video_desc_input")
    user_input_tags = st.text_input("Enter GPT tags (comma separated):", key="video_tags_input")

    if st.button("Predict", key="predict_button"):
        input_text = user_input_title + " " + user_input_desc + " " + user_input_tags
        predicted_time = model.predict([input_text])[0]
        st.success(f"Estimated Watch Time: {predicted_time:.2f} seconds")

   
    merged_df = logs_df.merge(yt_df, on="video_id", how="inner")

    
    st.sidebar.header("Filters")
    user_filter = st.sidebar.text_input("Filter by User ID:")
    if user_filter:
        merged_df = merged_df[merged_df["user_id"].str.contains(user_filter)]

    
    query = st.text_input("🔍 Search videos by keyword:", key="search_input")
    if query:
        merged_df = merged_df[
            merged_df["title"].str.contains(query, case=False, na=False) |
            merged_df["description"].str.contains(query, case=False, na=False)
        ]

    st.markdown(f"### Showing {len(merged_df)} records")

    
    st.subheader("Top 10 Most Viewed Videos")
    video_stats = merged_df.groupby("title").agg(
        total_views=("user_id", "count"),
        avg_watch_time=("watch_time_sec", "mean")
    ).sort_values("total_views", ascending=False).head(10)

    st.bar_chart(video_stats["total_views"])
    st.subheader("Average Watch Time (Top 10 Videos)")
    st.bar_chart(video_stats["avg_watch_time"])

    
    if st.checkbox("Show Word Cloud of GPT Tags"):
        all_tags = " ".join(yt_df["gpt_summary_tags"].dropna().astype(str))
        show_wordcloud(all_tags)

    if st.checkbox(" Show merged dataset"):
        st.dataframe(merged_df)

if __name__ == "__main__":
    main()
