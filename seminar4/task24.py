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

file_name = input("Enter a file path: ")
with open(file_name, 'r') as f:
    berries_on_bush = f.readlines()
    bush = list()
    bush.append(int(berries_on_bush[0]) + int(berries_on_bush[1]) + int(berries_on_bush[len(berries_on_bush) - 1]))
    bush.append(int(berries_on_bush[0]) + int(berries_on_bush[len(berries_on_bush) - 2]) + int(
        berries_on_bush[len(berries_on_bush) - 1]))
    for i in range(1, len(berries_on_bush) - 1):
        bush.append(int(berries_on_bush[i]) + int(berries_on_bush[i - 1]) + int(berries_on_bush[i + 1]))
    print(f"We can get {max(bush)} max berries.")
