from datetime import datetime
import datetime
import requests
from urllib3 import request

from SRC2.config import API_KEY, BASE_URL

def get_news(query: str, exclude_words: list, api_key: str=API_KEY) -> list:
    today = datetime.datetime.today()
    params = {
        "q": "query",
        "from": today.strftime("%y-%m-%d"),
        "sortBy": "publisher",
        "apikey": api_key,

    }
    response = requests.get(
        url=BASE_URL,
        params=params
    )


    json_response = response.json()
    print(json_response)
    return (json_response.get("articles"))


