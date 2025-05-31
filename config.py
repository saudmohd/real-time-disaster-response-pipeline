from datetime import datetime, timedelta

start_date = datetime.utcnow() - timedelta(days=5*365)
end_date = datetime.utcnow()

min_magnitude = 4.5

db_config = {
    'host': 'localhost',
    'port': 5432,
    'dbname': 'postgres',
    'user': 'postgres',    
    'password': 'saud'     
}
