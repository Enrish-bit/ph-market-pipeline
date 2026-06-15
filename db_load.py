import os
import psycopg2
from dotenv import load_dotenv
from fetch_data import fetch_php_rates

load_dotenv()
DB_URL = os.getenv("DATABASE_URL")

def initialize_database():
    create_table_query = """ CREATE TABLE IF NOT EXISTS exchange_rates (
        id SERIAL PRIMARY KEY,
        base_currency VARCHAR(10) NOT NULL,
        php_exchange_rate NUMERIC(10, 4) NOT NULL,
        eur_to_usd NUMERIC(10, 4),
        jpy_to_usd NUMERIC(10, 4),
        extracted_at TIMESTAMP NOT NULL,
        inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    
    try:
        conn= psycopg2.connect(DB_URL)
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        conn.commit()
        print("Database initialized: 'exchange_rates' table is ready.")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error initializing database: {e}")
        
def load_data_to_db(data):
    if not data:
        print("No data received to insert.")
        return
    
    insert_query = """
    INSERT INTO exchange_rates (base_currency, php_exchange_rate, eur_to_usd, jpy_to_usd, extracted_at)
    VALUES (%s, %s, %s, %s, %s);
    """
    
    try:
        conn = psycopg2.connect(DB_URL)
        cursor = conn.cursor()
        
        cursor.execute(insert_query, (
            data['base_currency'],
            data['php_exchange_rate'],
            data['eur_to_usd'],
            data['jpy_to_usd'],
            data['extracted_at']
        ))
        
        conn.commit()
        print("Success! Live data successfully written to the Cloud Database.")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Database insertion error: {e}")
        
if __name__ == "__main__":
    print("Starting DB Initialization...")
    initialize_database()
    
    print("\nFetching fresh market data...")
    live_data = fetch_php_rates()
    
    print("\nLoading data into the cloud...")
    load_data_to_db(live_data)