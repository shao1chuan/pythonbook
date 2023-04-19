class Student:
    def greeting(self):
        print("Hello student")


print(type(Student))
print(isinstance(Student, type))


class_body = """
def greeting(self):
    print('Hello customer')
    
def jump(self):
    print('jump')
"""
class_dict = {}
exec(class_body, globals(), class_dict)

Customer = type("Customer", (object,), class_dict)

c = Customer()
c.greeting()
c.jump()
