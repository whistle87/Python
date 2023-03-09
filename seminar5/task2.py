"""
Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
"""


def count_even_odd(number, even_count=0, odd_count=0):
    if number < 1:
        return even_count, odd_count
    else:
        if (number % 10) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        return count_even_odd(number // 10, even_count, odd_count)


try:
    input_number = int(input("Enter a positive  number: "))
    if input_number < 0:
        raise ValueError
except ValueError:
    print("It's not a positive number!")
else:
    even, odd = count_even_odd(input_number)
    print(f"Amount of even is {even}, amount of odd is {odd}")
