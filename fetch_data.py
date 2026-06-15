import requests
import json
from datetime import datetime

def fetch_php_rates():
    url = "https://open.er-api.com/v6/latest/USD"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        rates = data.get("rates",{})
        
        php_rate = round(rates.get("PHP"), 4)
        eur_rate = round(rates.get("EUR"),4)
        jpy_rate = round(rates.get("JPY"), 4)
        
        raw_time = data.get("time_last_update_utc")
        
        clean_time_str = raw_time.split (" +")[0]
        parsed_time = datetime.strptime(clean_time_str, "%a, %d %b %Y %H:%M:%S")
        db_timestamp = parsed_time.strftime("%Y-%m-%d %H:%M:%S")
        
        
        transformed_data = {
            "base_currency": "USD",
            "php_exchange_rate": php_rate,
            "eur_to_usd": eur_rate,
            "jpy_to_usd": jpy_rate,
            "extracted_at": db_timestamp
        }
        
        return transformed_data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    
if __name__=="__main__":
    cleaned_data = fetch_php_rates()
    print("Transformed Data ready for DB load:")
    print(json.dumps(cleaned_data, indent = 4))
    