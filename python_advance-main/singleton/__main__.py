def singleton(cls):
    _instance = {}

    def inner(*args, **kwargs):
        if cls in _instance:
            return _instance[cls]

        obj = cls(*args, **kwargs)
        _instance[cls] = obj

        return obj

    return inner


class SingletonMeta(type):
    def __call__(cls, *args, **kwargs):
        if hasattr(cls, '_instance'):
            return getattr(cls, '_instance')

        obj = super().__call__(*args, **kwargs)
        setattr(cls, '_instance', obj)

        return obj


# @singleton
class Person(metaclass=SingletonMeta):
    pass


p_1 = Person()
p_2 = Person()

print(p_1 is p_2)
