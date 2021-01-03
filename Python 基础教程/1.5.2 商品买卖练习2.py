# 列表综合练习 写一个循环，不断的问用户想买什么，用户选择一个商品编号，
# 就把对应的商品添加到购物车里，最终用户输入q退出时，打印购物车里的商品列表
l1 = [['a',23],['b',34],['c',33],['d',345]]
l2 = []
print("商品列表****************")
for  i in l1:
    print(f"商品{i[0]}，价格为{i[1]}")

while True:
    name = input("输入商品名称：")
    if  name!="q":
        for bb in l1:
            if name==bb[0]:
                print(f"你选择的是{name}")
                l2.append(bb)
                break
        else:
            print("你选择的没有再列表中")
    else:
        break

if len(l2)>0:
    print(f"您选择的商品是{l2}")


