class User(ORM):
    # 定义数据表的字段
    name = CharField()
    age = IntField()

if __name__ == '__main__':
    user = User()
    user.name = "seanlee"
    user.age = 21
    user.save()   # 调用save函数框架自动将数据插入到数据库中