import json
import os

#from external_api import currency_conversion


def to_get_json(local):
    empty_list = []
    try:
        with open(local) as file:
            data = json.load(file)

            if len(data) == 0 or data != list(data):
                return empty_list
        return data
    except FileNotFoundError:
        return empty_list
    except json.JSONDecodeError as e:
        return (f"Ошибка при обработке файла JSON:: {e}")




file_json = os.path.join("/Users/a0000/MY_PROJEKT/bank_widget/", "data/operations.json")
result = to_get_json(file_json)


def sum_transaction(money):
    from external_api import currency_conversion
    if money["operationAmount"]["currency"]["code"] == "RUB":
        result = money["operationAmount"]["amount"]
        return float(result)
    else:
        return currency_conversion(money)


for transaction in result:
    rub_amount = round(sum_transaction(transaction), 2)
    if rub_amount is not None:
        print(f"Транзакция ID {transaction.get('id', 'неизвестный ID')}: Сумма в RUB = {rub_amount}")
    else:
        print(f"Транзакция ID {transaction.get('id', 'неизвестный ID')} не в RUB или данные некорректны.")


# /Users/a0000/MY_PROJEKT/bank_widget/data/operations.json
