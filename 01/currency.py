import requests

API_KEY = 'fca_live_etuv5ypfcRpEcbQ8maOADq5XLG7B9M5O7WgORooE'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "EUR", "CAD", "INR", "AUD"]

def convert_currency(base):
    currencies = []
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print(e)
        return None

while True:
    print("The available currencies are:")
    print("USD\tEUR\tCAD\tINR\tAUD")
    base = input("Enter the currency you want to convert to(q to quit): ").upper()

    if base == 'Q':
        print("Thanks for using :D")
        break
    elif base not in CURRENCIES:
        print("No such currency found...")
        continue

    data = convert_currency(base)
    if not data:
        continue

    del data[base]
    for ticker, value in data.items():
        print(f"{ticker} : {value}")