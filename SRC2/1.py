import os
from typing import Union


def get_mask_card_number(cards: Union[str]) -> str:
    """Функция шифрует 6 цифр карты, начиная с 6 по 12"""
    if len(cards) == 16:
        cods_number = cards[:6] + "******" + cards[12:]
        hidden_number = (
            cods_number[:4]
            + " "
            + cods_number[4:8]
            + " "
            + cods_number[8:12]
            + " "
            + cods_number[12:16]
        )
        return hidden_number
    return "Ошибка: введен некорректный номер карты"


user_cards = input()

print(get_mask_card_number(user_cards))


def get_mask_account(check: Union[str]) -> str:
    """Функция добавляет две ** и отображает последние 4 числа"""
    if len(check) > 5:
        check_number = "**" + check[-4:]
        return check_number
    return "Ошибка: введен некорректный номер счета"


you_check = input()
print(get_mask_account(you_check))
print(os.getcwd())


import random
import json


def generate_users(first_names: list[str], last_names: list[str], cities:list[str]) -> dict:
    """Генерирует пользователя."""

    while True:
        user = {
            'first_name': random.choice(first_names),
            'last_name': random.choice(last_names),
            'age': random.randint(18, 65),
            'city': random.choice(cities)
        }
        yield user


if __name__ == '__main__':
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
    first_names = ['John', 'Jane', 'Mark', 'Emily', 'Michael', 'Sarah']
    last_names = ['Doe', 'Smith', 'Johnson', 'Brown', 'Lee', 'Wilson']

    users = generate_users(first_names, last_names, cities)

    user_group1 = [next(users) for i in range(4)]
    user_group2 = [next(users) for i in range(6)]

    print('User group #1')
    print(json.dumps(user_group1, indent=4))
    print('User group #2')
    print(json.dumps(user_group2, indent=4))