import csv

import pandas as pd


def opening_a_file_csv(csv_file):
    with open(csv_file) as file:
        read = csv.DictReader(file, delimiter=";")
        for row in read:
            print(row)
            #(row["from"], row["to"], row["description"])


opening_a_file_csv("/Users/a0000/MY_PROJEKT/bank_widget/data/transactions.csv")


def opening_a_file_excel(excel_file):
    read_excel = pd.read_excel(excel_file)
    return read_excel


result = opening_a_file_excel("/Users/a0000/MY_PROJEKT/bank_widget/data/transactions_excel.xlsx")
print(result)



