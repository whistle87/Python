class IsStr:

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Value should be a string")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    name = IsStr()
    surname = IsStr()
    position = IsStr()
    _income = {'wage': 0, 'bonus': 0}

    def __init__(self, input_name, input_surname, input_position, input_wage, input_bonus):
        self.name = input_name
        self.surname = input_surname
        self.position = input_position
        self._income['wage'] = input_wage
        self._income['bonus'] = input_bonus

    def __str__(self):
        return f"Worker: {self.name} {self.surname} " \
               f"\nincome: {int(self._income['wage']) + int(self._income['bonus'])}"


second_worker = Worker('Tom', 984375, 'Developer', 10000, 500)
