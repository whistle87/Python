"""
Задание 4. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

input_list = input("Enter integers separated by space: ").split()
n = 0
while n <= len(input_list) // 2:
    temp_el = input_list[n]
    input_list[n] = input_list[len(input_list) - n - 1]
    input_list[len(input_list) - n - 1] = temp_el
    n += 1
print(input_list)
