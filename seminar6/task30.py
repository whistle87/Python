"""
Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""
first_num, diff, el_amount = input("Enter first number, difference and amount of element: ").split()
try:
    first_num = int(first_num)
    diff = int(diff)
    el_amount = int(el_amount)
except ValueError:
    print("It is not a number")
else:
    progression = [first_num + el * diff for el in range(el_amount)]
    print(progression)
