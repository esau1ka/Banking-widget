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