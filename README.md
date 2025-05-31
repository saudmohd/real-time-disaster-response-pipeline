# 🌍 Real-Time Disaster Response Data Pipeline

This project implements a **real-time data pipeline** that ingests, processes, and visualizes earthquake data from the [USGS Earthquake API](https://earthquake.usgs.gov/fdsnws/event/1/), enabling timely insights for disaster response and monitoring.

## 🚀 Features

- 📡 **Data Ingestion** using Kafka (Producer/Consumer model)
- 🧹 **Data Transformation** into clean, structured format
- 🗄️ **PostgreSQL Database** integration for persistent storage
- 📊 **Streamlit Dashboard** for interactive visualization
- ✅ Modular Python scripts for Producer, Consumer, Transform, Load, and Fetch operations

  ---

## 🧱 Tech Stack

| Layer            | Tools/Libraries                         |
|------------------|------------------------------------------|
| Data Source      | [USGS Earthquake API](https://earthquake.usgs.gov/) |
| Messaging Queue  | Apache Kafka                            |
| Backend Scripts  | Python (requests, json, pandas)         |
| Storage          | PostgreSQL                              |
| Visualization    | Streamlit                               |
| Orchestration    | CLI Scripts                             |

---
## 🧠 ETL Pipeline Overview

This project follows a real-time ETL (Extract, Transform, Load) pipeline:

- **Extract**:  
  - `fetch.py` retrieves real-time earthquake data from the [USGS Earthquake API](https://earthquake.usgs.gov/fdsnws/event/1/).
  - `producer.py` sends this data to an Apache Kafka topic (`earthquakes`).

- **Transform**:  
  - `consumer.py` reads data from Kafka.
  - `transform.py` parses and cleans the data (e.g., extracting magnitude, location, time, coordinates).

- **Load**:  
  - `load.py` inserts the transformed data into a PostgreSQL database with proper schema handling and deduplication (via `ON CONFLICT`).

- **Visualize**:  
  - `streamlit_app.py` provides a real-time interactive dashboard to explore earthquake data visually.

---


## 🗂️ Project Structure

```
rt_disasterResponseDP/
├── producer.py          # Sends earthquake data to Kafka
├── consumer.py          # Consumes messages and loads into PostgreSQL
├── transform.py         # Cleans/transforms raw data
├── load.py              # Inserts data into PostgreSQL
├── fetch.py             # Fetches data from USGS API
├── streamlit_app.py     # Dashboard visualization
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ How It Works

1. **Producer** fetches earthquake data from the USGS API and publishes it to Kafka.
2. **Consumer** listens to the Kafka topic, transforms the data, and loads it into PostgreSQL.
3. **Streamlit App** visualizes real-time earthquake reports with maps, filters, and charts.

---

## 🧪 Run Locally

### 1. Clone the Repo

git clone https://github.com/saudmohd/real-time-disaster-response-pipeline.git
cd real-time-disaster-response-pipeline

### 2. Set up PostgreSQL
Create a database and a table using this SQL:
CREATE TABLE earthquakes (
    id TEXT PRIMARY KEY,
    magnitude REAL,
    place TEXT,
    time TIMESTAMP,
    longitude REAL,
    latitude REAL,
    depth_km REAL
);
### 3. Start Kafka
Ensure Kafka and Zookeeper are running locally.

### 4. Run Components
# Start Producer
python producer.py // or uv run consumer.py

# Start Consumer
python consumer.py // or uv run producer.py

# Launch Dashboard
streamlit run streamlit_app.py
___

#📸 Sample Dashboard
___
Screenshots
![Screenshot 2025-05-31 134606](https://github.com/user-attachments/assets/4575fede-8f49-4827-86f9-e1cb8705d884)
![Screenshot 2025-05-31 134631](https://github.com/user-attachments/assets/d9b40eb0-4151-4b4b-937e-568adab397eb)
![Screenshot 2025-05-31 134649](https://github.com/user-attachments/assets/80ccd1d1-828d-43e3-a3bb-439925597d45)


___
🙌 Acknowledgments
*USGS Earthquake API
*Kafka
*Streamlit
*PostgreSQL
___
📬 Contact
Saud Muhammad
📧 saudmuhammad.zbi786@gmail.com
___
🔗 www.linkedin.com/in/saud-muhammad-8bbb98368
___
🔗 www.github.com/saudmohd
___
