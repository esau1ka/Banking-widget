def decorator(func):
    def wapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wapper


@decorator
def get_sq(width, height):
    s = width * height
    return s


w = 5
h = 6
print(f"Площадь прямоугольника {get_sq(w, h)}")

t = {
    "ё": "yo",
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "y",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "h",
    "ц": "c",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ъ": "",
    "ы": "y",
    "ь": "",
    "э": "e",
    "ю": "yu",
    "я": "ya",
}


def decorator(chars="!?"):
    def func_decor(func):
        def wrapper(*args, **kwargs):
            stroka = []
            result = func(*args, **kwargs)
            for i in result:
                if i in t:
                    stroka.append(t[i])
                elif i in chars:
                    if not stroka or stroka[-1] != "-":
                        stroka.append("-")
            return "".join(stroka)

        return wrapper

    return func_decor


@decorator(chars="?!:;,. ")
def str_lower(x):
    x_lower = x.lower()
    return x_lower


s = input()

itog = str_lower(s)
print(itog)


str_1 = input()


def get_list(x):
    spisok = x.split()
    spisok_num = []
    for i in spisok:
        spisok_num.append(int(i))
    return spisok_num


print(get_list(str_1))
