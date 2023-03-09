"""
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
"""
import random

try:
    size_array = int(input("Enter number of elements in array: "))
except ValueError:
    print("Its not a number!")
else:
    arr = []
    for i in range(size_array):
        arr.append(random.randint(1, size_array))
    x_number = random.randint(1, size_array)
    print(f"Array: {arr} \n{x_number}")
    print(f"Number {x_number} occurs {arr.count(x_number)} times in array")
