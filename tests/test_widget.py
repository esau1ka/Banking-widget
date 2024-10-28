import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize(
    "name_number_card, result_mask",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(name_number_card, result_mask):
    assert mask_account_card(name_number_card) == result_mask
