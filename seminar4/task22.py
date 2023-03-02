"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств
"""

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
result = first_arr.intersection(second_arr)
result = list(result)
result.sort()
print(f"Result: {result}")
