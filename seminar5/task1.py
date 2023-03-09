"""
Задание 1. Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Решите через рекурсию. В задании нельзя применять циклы.
"""


def calc():
    operation = input("Enter sign of operation or 0 for exit: ")
    if operation == '0':
        return
    elif operation == '-' or operation == '+' or operation == '*' or operation == '/':
        first_number = input("Enter first number: ")
        try:
            first_number = int(first_number)
        except ValueError:
            print("It is not a number. Try again")
            calc()
        else:
            second_number = input("Enter second number: ")
            try:
                second_number = int(second_number)
            except ValueError:
                print("It is not a number. Try again")
                calc()
            else:
                if operation == '+':
                    print(f"{first_number} {operation} {second_number} ="
                          f" {int(first_number) + int(second_number)}")
                elif operation == '-':
                    print(f"{first_number} {operation} {second_number} = "
                          f"{int(first_number) - int(second_number)}")
                elif operation == '*':
                    print(f"{first_number} {operation} {second_number} = "
                          f"{int(first_number) * int(second_number)}")
                else:
                    if int(second_number) == 0:
                        print("You can't divide by zero")
                    else:
                        print(f"{first_number} {operation} {second_number} = "
                              f"{int(first_number) / int(second_number)}")
                calc()
    else:
        print("Sign should be +, -, /, * or 0 for exit")
        calc()


calc()
