class NotNegative:

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value should be positive")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    mass = 25
    thick = 0.05
    _length = NotNegative()
    _width = NotNegative()

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_count(self):
        return Road.mass * Road.thick * self._width * self._length / 1000


first_road = Road(-20, 5000)
