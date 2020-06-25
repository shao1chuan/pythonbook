# 实例1—— 学生注册
i = 10
f = 10.5
b = True

print(i+f+b)

# 不同类型变量之间的计算
first_name = "三"
last_name = "张"
print(first_name + last_name)

print("-" * 50)

first_name = "zhang"
x = 10
print(str(x)+first_name)

# 变量的输入
# 1. 输入苹果单价
price_str = input("请输入苹果价格：")

# 完整例子. 要求苹果重量
weight_str = input("请输入苹果重量：")

# 3. 计算金额
# 1> 将苹果单价转换成小数
price = float(price_str)

# 完整例子> 将苹果重量转换成小数
weight = float(weight_str)

# 3> 计算付款金额
money = price * weight

print(money)

name ='小明'
student_no = 12
scale = 0.2

print("我的名字叫 %s，请多多关照！" % name)
print("我的学号是 %06d" % student_no)
print("苹果单价 %.02f 元／斤，购买 %.02f 斤，需要支付 %.02f 元" % (price, weight, money))
print("数据比例是 %.02f%%" % (scale * 100))

str = "{}曰：学而时习之，不亦说乎。".format("孔子")
print(str)

# 变量的命名

# 关键字
import keyword
print(keyword.kwlist)

['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while',
'with', 'yield']

# 变量的命名规则
userName = 'zhangsan'
print(userName)