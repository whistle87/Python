"""
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
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
        arr.append(random.randint(1, 1000))
    x_number = random.randint(1, 1000)
    print(f"Array: {arr} \n{x_number}")
    max_close = arr[0]
    for i in range(1, size_array):
        if abs(arr[i - 1] - x_number) > abs(arr[i] - x_number):
            max_close = arr[i]
    print(f"Number {x_number} more close to  {max_close}")
