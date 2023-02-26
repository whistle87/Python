"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток, которые нужно
перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.
"""

coins = int(input("Enter a number of coins: "))
tails = int(input("Enter an amount of tails: "))
if tails == 0 or tails == coins:
    print("All coins on one side")
elif tails > (coins - tails):
    print(f"Min {coins - tails} coins is needed to be flipped")
else:
    print(f"Min {tails} coins is needed to be flipped")
