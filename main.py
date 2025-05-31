from config import start_date, end_date, min_magnitude, db_config
from fetch import fetch_earthquake_data_monthly
from transform import transform_data, clean_data
from load import load_to_postgres

def main():
    raw_data = fetch_earthquake_data_monthly(start_date, end_date, min_magnitude)
    if raw_data:
        df = transform_data(raw_data)
        df = clean_data(df)
        df.to_csv("earthquakes_cleaned.csv", index=False)
        load_to_postgres(df, db_config)

if __name__ == "__main__":
    main()
