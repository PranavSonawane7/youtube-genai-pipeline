import os
import subprocess

# Define the steps of the pipeline
steps = [
    ("Fetch YouTube Data", "python ingestion/fetch_youtube_data.py"),
    ("Generate Viewer Logs", "python ingestion/logs_generate.py"),
    ("Clean Data with Pandas", "python processing/clean_youtube_data_pandas.py"),
    ("Clean Data with PySpark", "python processing/clean_youtube_data_pyspark.py"),
    ("Generate AI Tags", "python genai/gpt_summary_tags.py"),
    ("Train ML Model", "python ml/train_model.py")
]

def run_pipeline():
    for step_name, command in steps:
        print(f"\n🚀 Running Step: {step_name}")
        result = subprocess.run(command, shell=True)
        if result.returncode != 0:
            print(f"❌ Error in step: {step_name}. Exiting...")
            break
    print("\n✅ Pipeline Completed Successfully!")

if _name_ == "_main_":
    run_pipeline()