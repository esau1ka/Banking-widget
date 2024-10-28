from dotenv import load_dotenv
import requests
import os


load_dotenv(".env")
API_KEY = os.getenv("API_KEY")
def currency_conversion(transaction):
  from_convert = transaction["operationAmount"]["currency"]["code"]
  to_convert = "RUB"
  amount = transaction["operationAmount"]["amount"]
  url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_convert}&from={from_convert}&amount={amount}"
  headers = {
    "apikey": API_KEY
  }
  r = requests.get(url, headers=headers)
  result = r.json()
  return r


