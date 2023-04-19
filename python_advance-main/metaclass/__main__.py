class Human(type):
    @staticmethod
    def __new__(mcs, *args, **kwargs):
        class_ = super().__new__(mcs, *args)
        # class_.freedom = True
        if kwargs:
            for name, value in kwargs.items():
                setattr(class_, name, value)
        return class_


class Student(object, metaclass=Human, country="China", freedom=True):
    pass


print(Student.country)
print(Student.freedom)
