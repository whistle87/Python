"""
Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).
Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение, придумайте как это сделать
"""

words = ['attribute', 'класс', 'функция', 'type']

for el in words:
    try:
        byte_el = bytes(el, 'ascii')
    except ValueError:
        print(f"Word '{el}' can't be converted")
    else:
        print(f"This word can be converted: '{el}' - {byte_el}")
