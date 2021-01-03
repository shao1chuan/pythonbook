class Animal:
    '''
    人和狗都是动物，所以创造一个Animal基类
    '''
    def __init__(self, name, aggressivity, life_value):
        self.name = name  # 人和狗都有自己的昵称;
        self.aggressivity = aggressivity  # 人和狗都有自己的攻击力;
        self.life_value = life_value  # 人和狗都有自己的生命值;

    def eat(self):
        print('%s is eating'%self.name)

class Dog(Animal):
    '''
    狗类，继承Animal类
    '''
    def __init__(self,name,breed,aggressivity,life_value):
        super().__init__(name, aggressivity, life_value) #执行父类Animal的init方法
        self.breed = breed  #派生出了新的属性

    def bite(self, people):
        '''
        派生出了新的技能：狗有咬人的技能
        :param people:
        '''
        people.life_value -= self.aggressivity

    def eat(self):
        # Animal.eat(self)
        #super().eat()
        print('from Dog')

class Person(Animal):
    '''
    人类，继承Animal
    '''
    def __init__(self,name,aggressivity, life_value,money):
        #Animal.__init__(self, name, aggressivity, life_value)
        #super(Person, self).__init__(name, aggressivity, life_value)
        super().__init__(name,aggressivity, life_value)  #执行父类的init方法
        self.money = money   #派生出了新的属性

    def attack(self, dog):
        '''
        派生出了新的技能：人有攻击的技能
        :param dog:
        '''
        dog.life_value -= self.aggressivity

    def eat(self):
        #super().eat()
        Animal.eat(self)
        print('from Person')

egg = Person('egon',10,1000,600)
ha2 = Dog('二愣子','哈士奇',10,1000)
print(egg.name)
print(ha2.name)
egg.eat()