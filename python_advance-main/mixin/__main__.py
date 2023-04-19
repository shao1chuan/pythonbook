import json


class MapMixin:
    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value


class DictMixin:
    def to_dict(self):
        return self.__convert_dict(self.__dict__)

    def __convert_dict(self, attrs: dict):
        result = {}
        for key, value in attrs.items():
            result[key] = self.__convert_value(value)

        return result

    def __convert_value(self, value):
        if isinstance(value, DictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self.__convert_dict(value)
        elif isinstance(value, list):
            return [self.__convert_value(v) for v in value]
        elif hasattr(value, '__dict__'):
            return self.__convert_dict(value.__dict__)
        else:
            return value


class JSONMixin:
    def to_json(self):
        return json.dumps(self.to_dict())


class Student(MapMixin, DictMixin, JSONMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

# {"name": "Jack", "age": 20, "clasx": {"name": "class 9-1", "building": "A"}}

s = Student("Jack", 20)

print(s["name"])
print(s.to_dict())
print(s.to_json())

