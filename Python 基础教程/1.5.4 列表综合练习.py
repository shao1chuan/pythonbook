# 写一个循环，不断的问用户想买什么，用户选择一个商品编号，就把对应的商品添加到购物车里，
# 最终用户输入q退出时，打印购物车里的商品列表

products = [['iphone',6888],['三星',3000],['小米',2500]]
shopping_car = []
flag = True
while flag:
    print("******商品列表******")
    for index,i in enumerate(products):
        print("%s.  %s|  %s" %(index,i[0],i[1]))
    choice = input("请输入您想购买的商品的编号：")
    if choice.isdigit():#isdigit()判断变量是什么类型
        choice = int(choice)
        if choice>=0 and choice<len(products):
            shopping_car.append(products[choice])
            print("已经将%s加入购物车" %(products[choice]))
        else:
            print("该商品不存在")
    elif choice == "q":
        if len(shopping_car)>0:
            print("您打算购买以下商品：")
            for index,i in enumerate(shopping_car):
                print("%s. %s|  %s" %(index,i[0],i[1]))
        else:
            print("您的购物车中没有添加商品")
        flag = False