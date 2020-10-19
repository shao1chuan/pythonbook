class Teacher:
    def __init__(self, name, age,speak):
        self.name = name
        self.__age = age
        self.__speak = speak

    @property      #注意1.@proterty下面默认跟的是get方法，如果设置成set会报错。
    def age(self):
        return self.__age

    @age.setter    #注意2.这里是使用的上面函数名.setter，不是property.setter.
    def age(self,age):
        if age > 150 and age <=0:  #还可以在setter方法里增加判断条件
            print("年龄输入有误")
        else:
            self.__age = age

    @property
    def for_speak(self):  #注意2.这个同名函数名可以自定义名称，一般都是默认使用属性名。
        return self.__speak

    @for_speak.setter
    def for_speak(self, speak):
        self.__speak = speak

t1 = Teacher("herry",45,"Chinese")
t1.age = 38    #注意4.有了property后，直接使用t1.age,而不是t1.age()方法了。
t1.for_speak = "English"

print(t1.name,t1.age,t1.for_speak)  #herry 38 English