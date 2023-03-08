"""Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы."""


def sum_of_numbers(number, sum_of_num=0, count=1):
    if number < count:
        return sum_of_num
    else:
        sum_of_num = sum_of_num + count
        return sum_of_numbers(number, sum_of_num, count + 1)


try:
    input_number = int(input("Enter a positive number: "))
    if input_number < 0:
        raise ValueError
except ValueError:
    print("It's not a positive number!")
else:
    left_result = sum_of_numbers(input_number)
    right_result = input_number * (input_number + 1) / 2
    if left_result == right_result:
        print(f"{left_result} = {int(right_result)},therefore equality is fulfilled")
    else:
        print(f"{left_result} != {int(right_result)},therefore equality is not fulfilled")
