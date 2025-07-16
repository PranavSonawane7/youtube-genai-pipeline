import pandas as pd 
from ydata_profiling import ProfileReport
import os


PROCESSED_PATH = "data/processed/youtube_data_cleaned_pandas.csv"
REPORT_PATH = "reports/youtube_data_quaility_report.html"
os.makedirs("reports", exist_ok=True)

def generate_report():
    print("Loading Cleaned data.....")
    df = pd.read_csv(PROCESSED_PATH)

    print("Geneartig Profile Report...")
    profile = ProfileReport(df, title= "Youtube Data Quality Report", explorative=True)


    print("Saving Report.....")
    profile.to_file(REPORT_PATH)
    print(f"Report Saved to {REPORT_PATH}")



if __name__ == '__main__':
    generate_report()


