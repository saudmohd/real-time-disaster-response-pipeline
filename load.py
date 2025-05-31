# load.py

import psycopg2

def load_to_postgres(df, db_config):
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        for _, row in df.iterrows():
            cur.execute("""
                INSERT INTO earthquakes (id, magnitude, place, time, longitude, latitude, depth_km)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
            """, (
                row["id"],
                row["magnitude"],
                row["place"],
                row["time"],
                row["longitude"],
                row["latitude"],
                row["depth_km"]
            ))

        conn.commit()
        print("✅ Data loaded to PostgreSQL successfully.")
    except Exception as e:
        print(f"❌ Error loading data: {e}")
  
  
        