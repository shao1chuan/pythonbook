import operator
from dataclasses import dataclass, field


@dataclass(order=True)
class Student:
    sort_index: int = field(init=False, repr=False)

    name: str
    age: int = 19
    independent: bool = field(default=False, init=False, repr=True)

    def __post_init__(self):
        self.independent = self.age > 19
        self.sort_index = self.age


s_1 = Student("Jack", 20)
print(s_1)

s_2 = Student("Tom")
print(s_2)

print(s_1 == s_2)

students = [s_2, s_1]
sorted_students = sorted(students)
print(sorted_students)

students.sort(key=operator.attrgetter('name'))
print(students)
