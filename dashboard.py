import streamlit as st
import psycopg2
import pandas as pd
import pydeck as pdk

# --- DB Config ---
db_config = {
    'host': 'localhost',
    'port': 5432,
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'saud'
}

# --- Fetch data from PostgreSQL ---
def fetch_data():
    try:
        conn = psycopg2.connect(**db_config)
        query = "SELECT * FROM earthquakes ORDER BY time DESC;"
        df = pd.read_sql(query, conn)
        conn.close()
        df['time'] = pd.to_datetime(df['time'])
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

# --- Streamlit Config ---
st.set_page_config(page_title="🌍 Earthquake Dashboard", layout="wide")
st.title("🌍 Real-Time Earthquake Monitoring Dashboard")

# --- Load Data ---
df = fetch_data()

if not df.empty:
    st.sidebar.header("🔍 Filters")

    # --- Magnitude Filter ---
    min_mag = float(df["magnitude"].min())
    max_mag = float(df["magnitude"].max())
    mag_filter = st.sidebar.slider("Minimum Magnitude", min_mag, max_mag, min_mag)

    # --- Date Range Filter ---
    min_date = df["time"].min().date()
    max_date = df["time"].max().date()
    date_range = st.sidebar.date_input("Date Range", [min_date, max_date])

    # --- Apply Filters ---
    filtered_df = df[df["magnitude"] >= mag_filter]
    if len(date_range) == 2:
        start_date, end_date = pd.to_datetime(date_range)
        filtered_df = filtered_df[(filtered_df["time"] >= start_date) & (filtered_df["time"] <= end_date)]

    # --- Dashboard KPIs ---
    st.subheader("📊 Earthquake Statistics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Earthquakes", len(filtered_df))
    col2.metric("Max Magnitude", round(filtered_df["magnitude"].max(), 2))
    col3.metric("Avg Magnitude", round(filtered_df["magnitude"].mean(), 2))

    # --- 3D Map ---
    st.subheader("🗺️ Earthquake Map")
    st.pydeck_chart(pdk.Deck(
        initial_view_state=pdk.ViewState(
            latitude=filtered_df["latitude"].mean(),
            longitude=filtered_df["longitude"].mean(),
            zoom=2,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "ColumnLayer",
                data=filtered_df,
                get_position='[longitude, latitude]',
                get_elevation='magnitude * 100000',
                elevation_scale=0.5,
                radius=40000,
                get_fill_color='[255, 50, 30, 200]',
                pickable=True,
                auto_highlight=True,
            )
        ],
    ))

    # --- Histogram ---
    st.subheader("📈 Magnitude Distribution")
    st.bar_chart(filtered_df["magnitude"].value_counts().sort_index())

    # --- Data Table ---
    with st.expander("📄 View Raw Data Table"):
        st.dataframe(filtered_df)
else:
    st.warning("⚠️ No data available or failed to fetch.")
