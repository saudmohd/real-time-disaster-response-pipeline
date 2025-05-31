import requests
from datetime import datetime, timedelta

def fetch_earthquake_data_monthly(start_date, end_date, min_magnitude=4.5):
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    all_features = []
    
    # Convert to datetime objects if strings
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

    current_start = start_date

    while current_start < end_date:
        # Calculate the start of next month
        next_month = (current_start + timedelta(days=31)).replace(day=1)
        current_end = min(next_month - timedelta(days=1), end_date)

        params = {
            "format": "geojson",
            "minmagnitude": min_magnitude,
            "starttime": current_start.strftime("%Y-%m-%d"),
            "endtime": current_end.strftime("%Y-%m-%d")
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            features = data.get('features', [])
            all_features.extend(features)
            print(f"Fetched {len(features)} events from {params['starttime']} to {params['endtime']}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {params['starttime']} to {params['endtime']}: {e}")

        current_start = next_month

    return all_features
