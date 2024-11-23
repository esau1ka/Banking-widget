# ##import re
# import os
# import src.utils
# from src.utils import to_get_json
#
# file_json = os.path.join("/Users/a0000/MY_PROJEKT/bank_widget/", "data/operations.json")
# result = to_get_json(file_json)
#
#
# def main():
#     print(
#         """Привет! Добро пожаловать в программу работы
# с банковскими транзакциями.
# Выберите необходимый пункт меню:
# 1. Получить информацию о транзакциях из JSON-файла
# 2. Получить информацию о транзакциях из CSV-файла
# 3. Получить информацию о транзакциях из XLSX-файла"""
#     )
#     user_input_file = input("Введите номер пункта ")
#     if user_input_file == 1:
#         transactions_from_file = to_get_json(file_json)
#         print(transactions_from_file)
#
#
# if __name__ == "__main__":
#     main()
