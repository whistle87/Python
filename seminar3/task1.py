"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.
"""

try:
    month = int(input("Enter number of month: "))
except ValueError:
    print("Enter wrong symbol")
else:
    if month < 1 or month > 12:
        print(print('Number of month should be from 1 to 12!'))
    else:
        season_list = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer',
                       'summer', 'autumn', 'autumn', 'autumn', 'winter']
        season_dict = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer',
                       8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}
        print(f"Result via a list: {season_list[month - 1]}")
        print(f"Result via a dict: {season_dict[month]}")
