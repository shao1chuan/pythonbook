# 随机数的处理
# 综合练习---猜数字

# 计算机要求用户输入数值范围的最小值和最大值。
# 计算机随后“思考”出在这个范围之内的一个随机数，
# 并且重复地要求用户猜测这个数，直到用户猜对了。
# 在用户每次进行猜测之后，计算机都会给出一个提示，
# 并且会在这个过程的最后显示出总的猜测次数。这
# 个程序包含了几种类型的我们学过的 Python 语句，例如，输入语句、输出语句、赋值语句、循环和条件语句
import random

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = random.randint(smaller, larger)
count = 0
while True:
    count += 1
    userNumber = int(input("Enter your guess: "))
    if userNumber < myNumber:
        print("Too small")
    elif userNumber > myNumber:
        print("Too large")
    else:
        print("You've got it in", count, "tries!")
        break
