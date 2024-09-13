


from src.masks import get_mask_card_number, get_mask_account
from datetime import datetime

def mask_account_card(info):
    slovo = ["Maestro", "MasterCard", "Visa Classic", "Visa Platinum", "Visa Gold"]
    account = "Счет"
    for i in slovo:
        if i.lower() in info.lower():
            no_word = info.replace(i, "")
            no_space = no_word.strip()
            return (f"{i} {get_mask_card_number(no_space)}")

        elif account.lower() in info.lower():
            no_word = info.replace(i, "")
            no_space = no_word.strip()
            return (f"{account} {get_mask_account(no_space)}")







