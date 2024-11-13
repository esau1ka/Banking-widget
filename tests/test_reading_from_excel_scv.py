from unittest.mock import patch
from src.reading_from_excel_scv import opening_a_file_excel, opening_a_file_csv
import pandas as pd
from io import StringIO



def test_opening_a_file_csv():
    # Подготовим тестовые данные, как строку (имитируем файл)
    test_data = """id;state;date;amount;currency_name;currency_code;from;to;description
650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации
3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту"""

    # Мокаем open, чтобы он возвращал объект StringIO с тестовыми данными
    with patch("builtins.open", return_value=StringIO(test_data)):
        # Запускаем функцию, которая будет читать данные из мока
        opening_a_file_csv("fakefile.csv")

# Запуск теста
if __name__ == "__main__":
    test_opening_a_file_csv()


# Тест для функции opening_a_file_excel
@patch("pandas.read_excel")
def test_opening_a_file_excel(mock_read_excel):
    # Создаем пример данных, которые должны быть возвращены из мока
    mock_data = pd.DataFrame({
        "from": ["12345", "54321"],
        "to": ["67890", "09876"],
        "description": ["Payment", "Refund"]
    })

    # Настроим mock так, чтобы он возвращал mock_data
    mock_read_excel.return_value = mock_data

    # Вызов функции с мокированным pandas.read_excel
    result = opening_a_file_excel("/path/to/fakefile.xlsx")

    # Проверяем, что результат соответствует ожидаемому
    assert result.equals(mock_data), f"Ожидалось: {mock_data}, но получено: {result}"

    # Проверяем, что read_excel был вызван с правильным аргументом
    mock_read_excel.assert_called_once_with("/path/to/fakefile.xlsx")


if __name__ == "__main__":
    unittest.main()