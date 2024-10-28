import json
book_info = {
    "title": "Sherlok",
    "author": "Artur",
    "year": "1887",
    "ganres":["detective", "komedy"]
}
json_str = json.dumps(book_info)

str_dumps = json.loads(json_str)
print(type(str_dumps))



def sum_transaction():
    empty_list = []
    try:
        with open("/data/operations.json") as file:
            data = json.load(file)
            print(data)
            if len(data) == 0 or  data != list(data):
                return empty_list
    except FileNotFoundError:
        return empty_list


result = sum_transaction()
print("Результат:", result)
