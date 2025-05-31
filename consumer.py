from kafka import KafkaConsumer
import json
import transform  
import load       

consumer = KafkaConsumer(
    'earthquakes',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='earthquake-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)


db_config = {
    'host': 'localhost',
    'port': 5432,
    'dbname': 'postgres',
    'user': 'postgres',    
    'password': 'saud'     
}


def consume_and_load():
    for message in consumer:
        event = message.value
        if "properties" not in event:
            print("Skipping invalid message (no 'properties' key).")
            continue
        
        try:
            df = transform.transform_data([event])
            df = transform.clean_data(df)
            load.load_to_postgres(df, db_config)  # Pass config dict here
            print("Consumed and loaded one event.")
        except Exception as e:
            print(f"Error processing message: {e}")


if __name__ == "__main__":
    consume_and_load()
