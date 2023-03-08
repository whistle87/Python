"""
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
"""


def sum_of_numbers(first_number, second_number):
    if second_number == 0:
        return first_number
    else:
        return sum_of_numbers(first_number + 1, second_number - 1)


try:
    first_input_number = int(input("Enter a first number: "))
    if first_input_number < 0:
        raise ValueError
except ValueError:
    print("It's not a positive number!")
else:
    try:s
        second_input_number = int(input("Enter a second number: "))
    except ValueError:
        print("It's not a positive number!")
    else:
        print("Answer: ", sum_of_numbers(first_input_number, second_input_number))
