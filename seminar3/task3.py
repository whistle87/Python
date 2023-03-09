"""
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:

{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

goods = []
i = 0
while True:
    product = input("Enter a product name: ")
    while True:
        price = input("Enter price: ")
        try:
            price = int(price)
        except ValueError:
            print("Price should be a number")
        else:
            if price < 0:
                print("Price should be positive")
            else:
                break
    while True:
        amount = input("Enter amount of goods: ")
        try:
            amount = int(amount)
        except ValueError:
            print("Amount should be a number")
        else:
            if amount < 0:
                print("Amount should be positive")
            else:
                break
    measure_unit = input("Enter a unit of measure: ")
    line = (i + 1, {"name": product, "price": price, "amount": amount, "measure": measure_unit})
    goods.append(line)
    i += 1
    if input("Press any key to add more products or print exit: ") == 'exit':
        break
print("Goods structure: ")
print(*goods, sep='\n')
products_list = []
price_list = []
amount_list = []
measure_list = []
for el in range(len(goods)):
    if products_list.count(goods[el][1]['name']) == 0:
        products_list.append(goods[el][1]['name'])
    if price_list.count(goods[el][1]['price']) == 0:
        price_list.append(goods[el][1]['price'])
    if amount_list.count(goods[el][1]['amount']) == 0:
        amount_list.append(goods[el][1]['amount'])
    if measure_list.count(goods[el][1]['measure']) == 0:
        measure_list.append(goods[el][1]['measure'])
analiz_dict = {"name": products_list, "price": price_list, "amount": amount_list, "measure": measure_list}
print("Analiz dictionary: ")
for key, value in analiz_dict.items():
    print(f"{key} : {value}")
