import json
book_info = {
    "title": "Sherlok",
    "author": "Artur",
    "year": "1887",
    "ganres":["detective", "komedy"]
}
json_str = json.dumps(book_info)

str_dumps = json.loads(json_str)
print(type(str_dumps))



def sum_transaction():
    empty_list = []
    try:
        with open("/data/operations.json") as file:
            data = json.load(file)
            print(data)
            if len(data) == 0 or  data != list(data):
                return empty_list
    except FileNotFoundError:
        return empty_list


result = sum_transaction()
print("Результат:", result)


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