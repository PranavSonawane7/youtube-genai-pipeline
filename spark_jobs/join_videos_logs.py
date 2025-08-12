from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count

spark = SparkSession.builder \
    .appName("JoinYouTubeWithViewerLogs") \
    .getOrCreate()


videos_df = spark.read.option("header", True).csv("data/processed/youtube_data_with_summary.csv")

logs_df = spark.read.option("multiline", "true").json("data/logs/viewer_logs.json")


videos_df = videos_df.withColumnRenamed("video_id", "vid_id")

# Join
joined_df = logs_df.join(videos_df, logs_df.video_id == videos_df.vid_id, "inner")

# Analytics
summary_df = joined_df.groupBy("title").agg(
    count("*").alias("total_views"),
    avg("watch_time_sec").alias("avg_watch_time")
).orderBy(col("total_views").desc())

summary_df.show(truncate=False)
