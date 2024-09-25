import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("dddd7000792289606361") == "Ошибка: введен некорректный номер карты"
    assert get_mask_card_number("") == "Ошибка: введен некорректный номер карты"


@pytest.fixture
def fixture_mask_card_number():
    return [
        ("73654108430135874305", "**4305"),
        ("123456", "**3456"),
        ("123456qwer", "Ошибка: введен некорректный номер счета"),
    ]


def test_get_mask_account(fixture_mask_card_number):
    for i, n in fixture_mask_card_number:
        assert get_mask_account(i) == n
