# 实例1—— 学生注册

# 定义变量---学生学号
studentNo = 232535

# 定义变量---学生密码
stuentPassword = "123"

# 在程序中，如果要输出变量的内容，需要使用 print 函数
print(studentNo)
print(stuentPassword)

# 定义柿子价格变量
price = 8.5

# 定义购买重量
weight = 7.5

# 计算金额
money = price * weight

print(money)

first_name = "三"
last_name = "张"
print(first_name + last_name)
print("-" * 50)

# 变量的格式化输出
print("我的名字叫 %s，请多多关照！" % stuentPassword)
print("我的学号是 %06d" % studentNo)
print("苹果单价 %.02f 元／斤，购买 %.02f 斤，需要支付 %.02f 元" % (price, weight, money))
print("数据比例是 %.02f%%" % (money * 100))

# 使用format
str = "{}曰：学而时习之，不亦说乎。".format("孔子")
print(str)