class MyDecorator:
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print("start")
        result = self.f(*args, **kwargs)
        print("end")
        return result


class ParamDecorator:
    def __init__(self, name):
        self.name = name

    def __call__(self, f):
        def wrap(*args):
            print(f"start {self.name}")
            result = f(*args)
            print("end")
            return result

        return wrap


@ParamDecorator("Jack")
def test():
    print("test")
    return 200


print(test())


def cls_decorator(cls):
    print("start class decorator")

    def inner():
        print("start")
        obj = cls()
        print("end")
        return obj

    return inner


@cls_decorator
class Person:
    pass

p1 = Person()
p2 = Person()
