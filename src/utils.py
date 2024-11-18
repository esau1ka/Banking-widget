import json
import os
import logging

log_folder = "logs_1"
log_file = os.path.join(log_folder, "utils.log")
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

# from external_api import currency_conversion


def to_get_json(local):
    empty_list = []
    try:
        with open(local) as file:
            data = json.load(file)

            if len(data) == 0 or data != list(data):
                return empty_list
            logger.info(f"Успешно загружены данные из {local}")
        return data
    except FileNotFoundError:
        logger.error(f"не найден {local}")
        return empty_list
    except json.JSONDecodeError as e:
        return f"Ошибка при обработке файла JSON:: {e}"


file_json = os.path.join("/Users/a0000/MY_PROJEKT/bank_widget/", "data/operations.json")
result = to_get_json(file_json)


def sum_transaction(money):
    from external_api import currency_conversion

    if money["operationAmount"]["currency"]["code"] == "RUB":
        result = money["operationAmount"]["amount"]
        logger.info(f"Транзакция в RUB: {result}")
        return float(result)
    else:
        logger.info(f"Конвертируем валюту: {money}")
        return currency_conversion(money)


for transaction in result:
    rub_amount = round(sum_transaction(transaction), 2)
    if rub_amount is not None:
        print(f"Транзакция ID {transaction.get('id', 'неизвестный ID')}: Сумма в RUB = {rub_amount}")
    else:
        print(f"Транзакция ID {transaction.get('id', 'неизвестный ID')} не в RUB или данные некорректны.")


# /Users/a0000/MY_PROJEKT/bank_widget/data/operations.json
