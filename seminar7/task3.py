"""
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


class Worker:
    name = []
    surname = []
    position = []
    _income = {'wage': 0, 'bonus': 0}

    def __init__(self, input_name, input_surname, input_position, input_wage, input_bonus):
        self.name = input_name
        self.surname = input_surname
        self.position = input_position
        self._income['wage'] = input_wage
        self._income['bonus'] = input_bonus

    def __str__(self):
        return f"Worker: {self.name} {self.surname} \nincome: {int(self._income['wage']) + int(self._income['bonus'])}"


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"{int(self._income['wage']) + int(self._income['bonus'])}"


first_worker = Position("Nick", "Baggins", 'Counter', 10000, 500)
second_worker = Position("Tom", "Baggins", 'Developer', 10000, 500)
print(f"{first_worker.get_full_name()} income: {first_worker.get_total_income()}")
print(second_worker)
