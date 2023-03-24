"""
Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.
Подсказки:
--- b'class' - используйте маркировку b''
"""

words = ['class', 'function', 'method']
words_b = []
for el in words:
    words_b.append(bytes(el, 'utf-8'))
for el in words_b:
    print(f"word: {el}, type: {type(el)}, length: {len(el)}")
