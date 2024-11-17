import csv

import pandas as pd



def opening_a_file_csv(csv_file):
    """создание списка транзакций из csv"""
    data = []
    with open(csv_file) as file:
        read = csv.DictReader(file, delimiter=";")
        for row in read:
            data.append(row)
    return data


csv_result = opening_a_file_csv("/Users/a0000/MY_PROJEKT/bank_widget/data/transactions.csv")
print(csv_result)


def opening_a_file_excel(excel_file):
    """создание списка транзакций из excel"""
    read_excel = pd.read_excel(excel_file)
    return read_excel.to_dict(orient="records")


excel_result = opening_a_file_excel("/Users/a0000/MY_PROJEKT/bank_widget/data/transactions_excel.xlsx")
print(excel_result)
