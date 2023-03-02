"""
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
причем кусты высажены только по окружности. Таким образом, у каждого куста есть
 ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло
различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один
заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
"""

import random

file_name = input("Enter a file path: ")
with open(file_name, 'r') as f:
    berries_on_bush = f.readlines()
    bush = random.randint(0, len(berries_on_bush))
    if bush == 0:
        berries = int(berries_on_bush[0]) + int(berries_on_bush[1]) + int(berries_on_bush[len(berries_on_bush) - 1])
    elif bush == len(berries_on_bush) - 1:
        berries = int(berries_on_bush[0]) + int(berries_on_bush[len(berries_on_bush) - 2]) + int(
            berries_on_bush[len(berries_on_bush) - 1])
    else:
        berries = int(berries_on_bush[bush]) + int(berries_on_bush[bush - 1]) + int(berries_on_bush[bush + 1])
    print(f"If bush is {int(bush) + 1} we will get {berries} berries.")
