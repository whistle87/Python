"""
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""


def generator(array, min_value, max_value):
    for i in range(len(array)):
        if min_value <= array[i] <= max_value:
            yield i


array = [3, 6, 8, 1, 12, 23945, 983, 564, 20, 1237, 45, 12, 90, 23, 6, 0, -1, -4, -67, - 8]
min_value, max_value = input("Enter min and max value: ").split()
try:
    min_value = int(min_value)
    max_value = int(max_value)
except ValueError:
    print("It is not a number")
else:
    new_array = generator(array, min_value, max_value)
    for el in new_array:
        print(el)
