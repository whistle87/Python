"""
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""


class TrafficLight:
    _colour_ = {'red': 7, 'yellow': 2, 'green': 5}

    def running(self, colour=_colour_):
        import time
        import keyboard
        flag = True
        while flag:
            for key in colour:
                if keyboard.is_pressed('p'):
                    flag = False
                    break
                else:
                    print("\n" * 25)
                    print(key)
                    time.sleep(colour[key])


first_light = TrafficLight()
first_light.running()
