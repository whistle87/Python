"""
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    mass = 25
    thick = 0.05

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_count(self):
        return Road.mass * Road.thick * self._width * self._length / 1000


first_road = Road(20, 5000)
print(first_road.mass_count())
Road.mass = 1
Road.thick = 0.5
print(first_road.mass_count())
second_road = Road(20, 5000)
print(second_road.mass_count())
