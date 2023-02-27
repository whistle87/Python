"""
Задание 1.
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня,
на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b
и выводить одно натуральное число — номер дня.
"""

start_run = int(input("Enter amount of kilometers in first day: "))
max_run = int(input("Enter max result: "))
day = 1
while start_run <= max_run:
    start_run = start_run + start_run * 0.1
    day += 1
print(f"Max result will be reached on {day} day")
