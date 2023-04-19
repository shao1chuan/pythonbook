class Prop:
    def __init__(self, attr):
        self._attr = f'_{attr}'

    def get(self, obj):
        if not hasattr(obj, self._attr):
            return None

        return getattr(obj, self._attr)

    def set(self, obj, value):
        setattr(obj, self._attr, value)


class Human(type):
    @staticmethod
    def __new__(mcs, *args, **kwargs):
        class_ = super().__new__(mcs, *args)
        for property_name in class_.props:
            prop = Prop(property_name)
            p_obj = property(fget=prop.get, fset=prop.set)
            setattr(class_, property_name, p_obj)

        return class_


class Student(object, metaclass=Human):
    props = ["name", "age"]


def human(cls):
    return Human(cls.__name__, cls.__bases__, dict(cls.__dict__))


@human
class Man:
    props = ["name", "age"]


man = Man()
print(man.name)
man.name = "Tom"
print(man.name)


student = Student()
print(student.name)
student.name = "Jack"
print(student.name)
