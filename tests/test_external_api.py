from unittest.mock import patch
from src.external_api import currency_conversion


@patch("requests.get")
def test_currency_conversion_success(mock_get):
    # Мокаем успешный ответ от API
    mock_get.return_value.json.return_value = {"result": 1000.0}

    # Пример транзакции
    transaction = {"operationAmount": {"amount": "1000.50", "currency": {"code": "USD"}}}

    # Проверяем, что конвертированная сумма равна ожидаемому значению
    result = currency_conversion(transaction)
    assert result == 1000.0

    # Проверяем, что запрос был отправлен на правильный URL
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1000.5",
        headers={"apikey": "l1OZ0X2W7lddgQwR1zz0xrpCEtPjTHlZ"},
    )
