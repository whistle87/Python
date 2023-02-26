"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""

n = int(input("Enter max number: "))
degree = 2
while degree <= n:
    print(f"{degree} ")
    degree = degree * 2
