
from dotenv import load_dotenv
import requests
import os
load_dotenv(".env")
API_KEY = os.getenv("API_KEY")
  # Используй свой ключ
url = f"https://api.apilayer.com/exchangerates_data/latest?apikey={API_KEY}"

# Получаем данные о курсах
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Получаем курс USD относительно RUB
    usd_to_rub = data['rates']['USD']
    print(f"Курс USD к RUB: {usd_to_rub}")

    # Конвертируем 150 рублей в доллары
    rub_amount = 150
    usd_amount = rub_amount / usd_to_rub
    print(f"{rub_amount} рублей = {usd_amount:.2f} долларов")
else:
    print("Ошибка при получении данных:", response.status_code, response.json())


API_KEY = os.getenv("API_KEY")
if API_KEY is None:
    print("Ошибка: API_KEY не найден в .env файле.")
else:
    print("API_KEY успешно загружен.")

from dotenv import load_dotenv
import os

load_dotenv("/полный/путь/к/.env")  # Укажи полный путь к файлу .env

API_KEY = os.getenv("API_KEY")
print("API_KEY:", API_KEY)





