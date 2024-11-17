import os
from unittest.mock import patch

import requests
from dotenv import load_dotenv


load_dotenv()
github_token = os.getenv("API_KEY")


# API_KEY = "l1OZ0X2W7lddgQwR1zz0xrpCEtPjTHlZ"
def currency_conversion(transaction):
    from_convert = transaction["operationAmount"]["currency"]["code"]
    to_convert = "RUB"
    amount = float(transaction["operationAmount"]["amount"])
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_convert}&from={from_convert}&amount={amount}"
    headers = {"apikey": github_token}
    r = requests.get(url, headers=headers)
    result = r.json()
    return result["result"]
