"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств
"""
from timeit import Timer


def sort_common(arr_one, arr_two):
    result = arr_one.intersection(arr_two)
    result = list(result)
    result.sort()
    return result


n = int(input("Enter a number of element in the first array: "))
m = int(input("Enter a number of element in the second array: "))
print(f"Enter {n} numbers in the first array")
first_arr = set()
for i in range(n):
    first_arr.add(int(input()))
print(f"Enter {m} numbers in the second array")
second_arr = set()
for i in range(m):
    second_arr.add(int(input()))
result = sort_common(first_arr, second_arr)
print(f"Result: {result}")
t1 = Timer(stmt="sort_common(first_arr, second_arr)", setup="from __main__ import sort_common, first_arr, second_arr")
print("Time: ", t1.timeit(number=1000), "seconds")
