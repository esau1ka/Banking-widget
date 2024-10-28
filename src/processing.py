from typing import Dict, List, Tuple, Union


def filter_by_state(
    dictionary_one: List[Dict[str, Union[str, int]]], state="EXECUTED"
) -> Tuple[List[Dict[str, Union[str, int]]], List[Dict[str, Union[str, int]]]]:
    """Функция сортирует словарь по значению 'EXECUTED' и создает два новых словаря"""
    dictionary_executed = []
    dictionary_canceled = []
    for i in dictionary_one:
        if i["state"] == state:
            dictionary_executed.append(i)
        elif i["state"] == "CANCELED":
            dictionary_canceled.append(i)
    return dictionary_executed, dictionary_canceled


dictionary = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

executed, canceled = filter_by_state(dictionary)
print(executed)
print(canceled)


def sort_by_date(
    dictionary_two: List[Dict[str, Union[str, int]]], descending: bool = True
) -> List[Dict[str, Union[str, int]]]:
    """Сортировка словаря по дате, со значением по умолчанию"""
    sorted_dictionary = sorted(dictionary_two, key=lambda k: k["date"], reverse=descending)
    return sorted_dictionary


print(sort_by_date(dictionary))
# Функция сортировки по двум критериям
