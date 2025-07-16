from pyspark.sql import SparkSession
from ydata_profiling import ProfileReport

# Step 1: Start SparkSession
spark = SparkSession.builder.appName("ProfilingWithPySpark").getOrCreate()

# Step 2: Load CSV into Spark DataFrame
spark_df = spark.read.csv("data/processed/youtube_data_cleaned_pandas.csv", header=True, inferSchema=True)

# Step 3: Convert to Pandas DataFrame
pandas_df = spark_df.toPandas()

# Step 4: Generate Profile Report
profile = ProfileReport(pandas_df, title="Youtube Data Profiling using spark", explorative=True)

# Step 5: Save report to HTML
profile.to_file("reports/youtube_data_quality_report_spark.html")

print("✅ Profile report saved as youtube_data_quality_report_spark.html")
