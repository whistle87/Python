class IdenticalObjects(type):

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


class MyClass(metaclass=IdenticalObjects):
    pass


obg1 = MyClass()
obg2 = MyClass()
obg3 = MyClass()
print(obg1 is obg2)
print(obg1 is obg3)
print(obg3 is obg2)
