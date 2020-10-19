class Cat:
    name = ''
    def __init__(self):
        # self.name = 'Tom'
        print('init')
    def __str__(self):
        return(self.name)
    def drink(self):
        print('drink')
cat = Cat()
cat.name = 'Tom'
print(f'我是小猫{cat},我的id是{id(cat)}',cat,cat.name)
cat.drink()
