from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, to_timestamp
import os

RAW_PATH = "data/raw/youtube_data.csv"
PROCESSED_PATH = "data/processed/youtube_data_cleaned_spark.csv"
os.makedirs("data/processed", exist_ok=True)

def clean_youtube_data():
    spark = SparkSession.builder.appName("CleanYoutubeData").getOrCreate()

    print("Reading CSV......")
    df = spark.read.option("header", True).csv(RAW_PATH)

    print("Cleaning.......")
    df_cleaned= (
        df.dropna(subset=["video_id", "title"])
        .withColumn("published_at", to_timestamp(col("published_at")))
        .filter(col("published_at").isNotNull())
        .withColumn("title", trim(col("title")))
        .withColumn("description", trim(col("description")))
    )

    print("Saving cleaned data....")
    df_cleaned.write.mode("overwrite").option("header", True).csv(PROCESSED_PATH)
    print(f"Saved to {PROCESSED_PATH}")

    spark.stop()

if __name__ == '__main__':
    clean_youtube_data()