import pandas as pd

def transform_data(earthquake_data):
    earthquake = []
    for event in earthquake_data:
        properties = event["properties"]
        geometry = event["geometry"]
        earthquake.append({
            "id": event.get("id", "unknown"),
            "magnitude": properties["mag"],
            "place": properties["place"],
            "time": pd.to_datetime(properties["time"], unit="ms"),
            "longitude": geometry["coordinates"][0],
            "latitude": geometry["coordinates"][1],
            "depth_km": geometry["coordinates"][2]
        })
    return pd.DataFrame(earthquake)

def clean_data(df):
    df = df.drop_duplicates(subset="id")
    df = df.dropna(subset=["magnitude", "longitude", "latitude"])
    return df
