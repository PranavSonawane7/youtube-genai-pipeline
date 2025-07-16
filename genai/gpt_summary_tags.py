import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# openai.api_key = os.getenv("OPENAI_API_KEY")

INPUT_PATH = "data/processed/youtube_data_cleaned_pandas.csv"
OUTPUT_PATH = "data/processed/youtube_data_with_summary.csv"

def generate_summary_and_tags(title, description):
    prompt = f"""
    You are a Youtube content analyst.
    Given this video title and edscription, return:
    1. A short summary (1-2 lines):
    2. 5 relevant tags or keywords

    Title: {title}
    Description: {description}
    """

    try: 
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user", "content":prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
         

    except Exception as e:
        return f"Error: {e}"

def main():
    df = pd.read_csv(INPUT_PATH)
    print(f"Loaded {len(df)} videso for summarization.....")

    df["gpt_summary_tags"] = df.apply(
        lambda row: generate_summary_and_tags(row["title"], row["description"]), axis= 1
    )

    df.to_csv(OUTPUT_PATH, index=False)
    print(f"GPT-enriched data saved to : {OUTPUT_PATH}")

if __name__ == '__main__':
    main()