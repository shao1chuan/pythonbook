# 需求：
# 房子(House)有户型、总面积和家具名称列表
# 新房子没有任何的家具
# 家具(HouseItem)有名字和占地面积，其中
# 席梦思(bed)占地4平米
# 衣柜(chest)占地2平米
# 餐桌(table)占地1.5平米
# 将以上三件家具添加到房子中：
# 打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表
# 剩余面积
# 在创建房子对象时，定义一个剩余面积的属性，初始值和总面积相等
# 当调用add_item方法，向房间添加家具时，让剩余面积-=家具面积
# 思考：应该先开发哪一个类？

class House:
    def __init__(self,type,area):
        self.type = type
        self.area = area
        self.fl = []
        self.left = area
    def show(self):
        ss = f"the type is {self.type}, and the area is {self.area}, 剩余的面积是{self.left},家具是{self.fl}"
        for i in self.fl:
            print (i)
        return ss

    def add(self,h):
        self.left -=h.area
        self.fl.append(h)
class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return f"{self.name}的占地面积是：{self.area}"

bed = HouseItem("aa",4)
chest = HouseItem("bb",2)
table = HouseItem("cc",1.5)
print(table.name)

h = House("big",4000)
h.add(bed)
h.add(chest)
h.add(table)

print(h.show())



