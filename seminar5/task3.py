"""
 Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,то надо вывести число 6843.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
"""


def overturn(number, result=''):
    if number < 10:
        return result + str(number)
    else:
        result = result + str(number % 10)
        return overturn(number // 10, result)


try:
    input_number = int(input("Enter a number: "))
except ValueError:
    print("It's not a number!")
else:
    print(overturn(input_number))
