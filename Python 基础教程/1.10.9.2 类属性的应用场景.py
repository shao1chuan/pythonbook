# 我们有一个班级类，创建班级对象的时候，需要按序号指定班级名称，
# 我们就需要知道当前已经创建了多少个班级对象，这个数量可以设计成类属性

class EduClass:
    class_num = 0
    price = "11111111111"
    def __init__(self):
        self.class_name = f'Python{EduClass.class_num+1}班'
        EduClass.class_num += 1
        self.price = "222222222"


classList = [EduClass() for i in range(10)]
for c in classList:
    del c.price
    print(c.class_name,c.price)