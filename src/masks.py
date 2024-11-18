from typing import Union
import logging
import os


log_folder = "logs_1"
log_file = os.path.join(log_folder, "masks.log")
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)


def get_mask_card_number(cards: Union[str]) -> str:
    """Функция шифрует 6 цифр карты, начиная с 6 по 12"""
    if len(cards) == 16:
        cods_number = cards[:6] + "******" + cards[12:]
        hidden_number = cods_number[:4] + " " + cods_number[4:8] + " " + cods_number[8:12] + " " + cods_number[12:16]
        logger.debug(f" шифровка номера карты {hidden_number}")
        return hidden_number
    logger.error(f"Ошибка: некорректный номер карты: {cards}")
    return "Ошибка: введен некорректный номер карты"


def get_mask_account(check: Union[str]) -> str:
    """Функция добавляет две ** и  отображает последние 4 числа"""
    if len(check) > 5:
        if check.isdigit():
            check_number = "**" + check[-4:]
            return check_number
    logger.error(f"Ошибка: некорректный номер карты: {check}")
    return "Ошибка: введен некорректный номер счета"
