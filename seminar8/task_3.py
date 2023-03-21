"""
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);
Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import yaml

currency = {
    'currency_name': ['euro', 'pound', 'yuan', 'ruble'],
    'currency_quantity': 4,
    'currency_sign': {
        '€': 'U+20AC',
        '£': 'U+00A3',
        '元': 'U+5143',
        '₽': 'U+20BD'
    }
}

with open('new_file.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(currency, file, default_flow_style=False, allow_unicode=True)
with open('new_file.yaml', encoding='utf-8') as file:
    currency_from_file = yaml.full_load(file)
    print("Data from file")
    for item, doc in currency_from_file.items():
        print(item, ":", doc)
if currency == currency_from_file:
    print("\nIt is identical data from program")
