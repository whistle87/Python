"""
Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел
(каждый элемент ряда меньше или равен предыдущему).
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""

my_list = [7, 5, 3, 3, 2]
print(my_list)
while True:
    number = input("Enter a number or print exit to close program: ")
    if number == "exit":
        break
    else:
        try:
            number = int(number)
        except ValueError:
            print("It's not a number")
        else:
            if number > 0:
                if number <= my_list[len(my_list) - 1]:
                    my_list.append(number)
                else:
                    for i in range(len(my_list)):
                        if number > my_list[i]:
                            my_list.insert(i, number)
                            break
                print(f"Result: {my_list}")
            else:
                print("Number should be positive")
