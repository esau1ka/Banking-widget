from unittest.mock import patch
from src.reading_from_excel_scv import opening_a_file_excel, opening_a_file_csv
import pandas as pd
from io import StringIO


def test_opening_a_file_csv():
    def test_opening_a_file_csv():
        # Мокаем open, чтобы он возвращал предсказанные данные
        with patch(
            "builtins.open",
            new_callable=patch.mock_open,
            read_data="id;state;date;amount;currency_name;currency_code;from;to;description\n650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации\n3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту",
        ) as mock_file:
            # Ожидаемый результат
            expected_result = [
                {
                    "id": "650703",
                    "state": "EXECUTED",
                    "date": "2023-09-05T11:30:32Z",
                    "amount": "16210",
                    "currency_name": "Sol",
                    "currency_code": "PEN",
                    "from": "Счет 58803664561298323391",
                    "to": "Счет 39745660563456619397",
                    "description": "Перевод организации",
                },
                {
                    "id": "3598919",
                    "state": "EXECUTED",
                    "date": "2020-12-06T23:00:58Z",
                    "amount": "29740",
                    "currency_name": "Peso",
                    "currency_code": "COP",
                    "from": "Discover 3172601889670065",
                    "to": "Discover 0720428384694643",
                    "description": "Перевод с карты на карту",
                },
            ]

            # Вызов функции с мокированным файлом
            result = opening_a_file_csv("fakefile.csv")

            # Проверка, что результат соответствует ожидаемому
            assert result == expected_result, f"Ожидался результат {expected_result}, но получен {result}"

            # Проверка, что open был вызван с правильным аргументом
            mock_file.assert_called_once_with("fakefile.csv")
