# 🎥 YouTube Data Engineering Project with GenAI & ML

## 📌 Overview
This project demonstrates a *real-world data engineering pipeline* using *YouTube API, Generative AI (OpenAI), and Machine Learning*.  
The pipeline:
- Extracts YouTube channel data using API
- Generates simulated viewer logs
- Cleans & transforms data using *Pandas* and *PySpark*
- Enriches data with *AI-generated tags & summaries*
- Trains an ML model to predict watch time
- Visualizes analytics via an *interactive Streamlit Dashboard*

---

## 🛠 Tech Stack
- *Python 3.12*
- *Pandas* & *PySpark* for data processing
- *OpenAI GPT* for GenAI-based summaries & tags
- *Scikit-learn* for ML modeling
- *Streamlit* for dashboard
- *YData-Profiling* for data quality report

---

## 📂 Project Structure
youtube-genai-data-engineering/
├── ingestion/                       # ETL scripts
│   ├── fetch_youtube_data.py      # Extract from YouTube API
│   ├── generate_viewer_logs.py    # Simulate viewer logs
│   ├── clean_data_pandas.py       # Clean data using Pandas
│   ├── clean_data_pyspark.py      # Clean data using PySpark
│   ├── genai_video_tags.py        # Add AI tags & summaries              
│   └── data_quality_report.py     # Generate quality report
├── ml/
│   ├── train_model.py             # Train ML model
│   └── models/watch_time_predictor.pkl
├── streamlit_app/app.py           # Streamlit dashboard
├── data/                          # Raw & processed data (ignored in Git)
├── requirements.txt
├── create_pipeline.py  
├── README.md
└── .gitignore

## 🚀 Features
✔ *Data Extraction* – YouTube API integration  
✔ *Data Simulation* – Viewer log generation  
✔ *Data Cleaning* – Pandas & PySpark workflows  
✔ *Generative AI* – Auto-generated tags & summaries  
✔ *ML Model* – Predict watch time based on views, likes, comments  
✔ *Interactive Dashboard* – KPIs, charts, word clouds  
✔ *Data Quality Report* – YData profiling for insights  

---

## ▶️ How to Run the Project

### 1️⃣ Clone Repository
```bash
git clone https://github.com/<your-username>/youtube-genai-data-engineering.git
cd youtube-genai-data-engineering
2️⃣ Set up Virtual Environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
3️⃣ Add YouTube API Key
	•	Get your API Key from Google Developer Console
	•	Add it to scripts/fetch_youtube_data.py:
API_KEY = "your_api_key"
CHANNEL_ID = "your_channel_id"
4️⃣ Run Full Pipeline
python create_pipeline.py
5️⃣ Start Dashboard
streamlit run streamlit_app/app.py
📊 Dashboard Preview

<img width="1920" height="1080" alt="Screenshot (7)" src="https://github.com/user-attachments/assets/e6f5de23-4f2f-40da-814d-2640b1f94b65" />

⸻

🔮 Future Enhancements
	•	Deploy Streamlit on Streamlit Cloud
	•	Add Apache Airflow for orchestration
	•	Store data in PostgreSQL/Snowflake
	•	Deploy ML model as API with FastAPI

⸻

✅ Architecture

YouTube API → ETL → AI → ML → Dashboard
