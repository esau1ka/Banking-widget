import random
from itertools import chain

result = (x**3 for x in range(10) if x % 2 == 0)
print(list(result))

#Задача 2
#Напишите функцию, которая принимает список
#чисел и возвращает сумму квадратов положительных
#чисел в этом списке. Используйте для этого
#генераторное выражение.

def number(x):
    return sum(i**i for i in x if i > 0 )


q = [2,3,4,5,6]
print(number(q))


result = (x for x in "Hello" if x.lower() in "aoueiy")
print(list(result))


def suma(x):
    return sum(x)


def arifm(x):
    return sum(x)

q = (i for i in range(15) if i % 3 == 0 or i % 5 == 0)

print(arifm(q))

slovo = [1, 2, 3]
slovo1 = [3, 4, 5]

result1 = chain(slovo, slovo1)
print(list(result1))



number = [2, 3, 4, 5]

f = list(map(lambda x: x**2, number))
print(f)

people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 30},
    {"name": "Eve", "age": 25},
]

f = list(filter(lambda x: x["age"] == 30, people))
print(f)

def f(x):
    for y in x:
        print(y)

q = (i**2 for i in range(10))
f(q)


import random
def random_number(start, end):
    while True:
        yield random.randint(start, end)

gen = random_number(1,100)
for i in range(10):
    print(next(gen))


def formula(x):
    for i in range(x):
        yield i**2

gen = formula(10)
print(next(gen))
print(next(gen))
print(next(gen))


def spisok(list1, list2):
    for i in list1:
        if i in list2:
            yield i


list11 = [1, 2, 3, 4, 5]
list12 = [4, 5, 6]
gen2 = spisok(list11, list12)
for i in gen2:
    print(i)






