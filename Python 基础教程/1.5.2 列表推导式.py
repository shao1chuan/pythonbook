# 列表推导式

x = [[1,2,3], [4,5,6], [7,8,9]]
y = [num for i in x for num in i]
print(y)
y = []
for i in x:
    for num in i:
        y.append(num)
print(y)
# 过滤不符合条件的元素 从列表中选择符合条件的元素组成新的列表
print('过滤不符合条件的元素 从列表中选择符合条件的元素组成新的列表'.center(50,'*'))
x = [-1,-4,6,7.5,-2.3,9,-11]
y = [i for i in x if i>0]
print(y)

x = [(x, y) for x in range(3) for y in range(3)]
print(x)
x = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(x)

# 列表综合练习 写一个循环，不断的问用户想买什么，用户选择一个商品编号，
# 就把对应的商品添加到购物车里，最终用户输入q退出时，打印购物车里的商品列表
l1 = [['a',23],['b',34],['c',33],['d',345]]
l2 = []
print("商品列表****************")
for (index, i) in enumerate(l1):
    print("商品{}，价格为{}", index, i)
while True:

    choise = input("请输入你选择的商品编号：")
    if choise.isdigit():
        if int(choise) in range(len(l1)) :
            print("你选择的是{}".format(choise))
            l2.append(l1[int(choise)])
            print(l2)
        else:
            print("你选的商品不在列表中")
    elif choise == 'q':
        break

if len(l2)>0:
    print("你选的商品如下：")
    for index,i in enumerate(l2):
        print("商品编号{},商品名称{}，商品价格{}".format(index,i[0],i[1]))



