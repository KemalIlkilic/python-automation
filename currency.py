import requests

KEY = 'fca_live_ZwLEjAAj0XO8KiH3LmrCAYnQOx3HbvMDQU9pRmTy'

BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={KEY}"

"""aud
It is project for currencies
How it works? 
BASE URL + KEY + QUERY
"""
CURRENCIES = ["EUR", "USD", "TRY", "PLN", "JPY", "AUD", "CAD"]

def convert_currency (base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data['data']
    except:
        print("Invalid currency")
        return None
while True:
    base = input("Enter the base currency (q for quit): ").upper()
    if base == "Q":
        break
    data = convert_currency(base)
    if not data:
        continue
    if base in data:
        del data[base]
    for key, value in data.items():
        print(f'{key} : {value}')
