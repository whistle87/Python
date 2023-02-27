"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.
"""

number = int(input("Enter a number: "))
max_digit = number % 10
number = number // 10
while number > 0:
    digit = number % 10
    if digit > max_digit:
        max_digit = digit
    number = number // 10
print(f"Max digit is {max_digit}")
