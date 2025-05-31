# producer.py

from kafka import KafkaProducer
import json
import time
from datetime import datetime, timedelta
import fetch 

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def get_last_10_minutes_window():
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(minutes=10)
    return start_time, end_time

test_message = {
    "type": "Feature",
    "id": "abc123",
    "properties": {
        "mag": 5.2,
        "place": "100 km SE of City, Country",
        "time": 1717142400000
    },
    "geometry": {
        "type": "Point",
        "coordinates": [138.5, 35.6, 10.0]
    }
}
producer.send('earthquakes', test_message)
producer.flush()
print("Test message sent.")



def produce_earthquake_events():
    start_time, end_time = get_last_10_minutes_window()
    data = fetch.fetch_earthquake_data_monthly(
    start_time,
    end_time,
    min_magnitude=4.5
)

    if data:
        for event in data:
            print("Producing event:", event)
            producer.send('earthquakes', event)
        producer.flush()
        print(f"Produced {len(data)} events to Kafka.")
    else:
        print("No data fetched.")

if __name__ == "__main__":
    while True:
        produce_earthquake_events()
        time.sleep(600)  # Wait 10 minutes
