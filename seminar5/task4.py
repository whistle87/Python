"""
 Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def count_sum_of_row(number, sum_of_row=0.0, el_of_row=1.0):
    if number == 0:
        return sum_of_row
    else:
        sum_of_row = sum_of_row + el_of_row
        return count_sum_of_row(number - 1, sum_of_row, el_of_row / (-2))


try:
    input_number = int(input("Enter a number: "))
except ValueError:
    print("It's not a number!")
else:
    print(count_sum_of_row(input_number))
