java = 86
python = 68

if (80 <= java < 90) or (80 <= python < 90):
    print('良好')
# 练习1
    # 我想买车，买什么车决定于我在银行有多少存款
    # 如果我的存款超过500万，我就买路虎
    # 否则，如果我的存款超过100万，我就买宝马
    # 否则， 如果我的存款超过50万，我就买迈腾
    # 否则， 如果我的存款超过10万，我就买福特
    # 否则， 如果我的存款10万以下 ，我买比亚迪
# 练习2
#     输入小明的考试成绩，显示所获奖励
#     成绩==100分，爸爸给他买辆车
#     成绩>=90分，妈妈给他买MP4
#     90分>成绩>=60分，妈妈给他买本参考书
#     成绩<60分，什么都不买

for letter in 'www.baidu.com':
    print(letter)
for value in range(1,100):
    print(value)
# 练习3
# 打印质数

for num in range(2,100):
    for i in range(2,num):
        if num%i == 0:
            break;
    else:
        print("%d is zhishu " % num)

# 练习4
# 打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{} = {} \t".format(i,j,i*j),end=" ")
    print()

# 随机数的处理
综合练习---猜数字

# 计算机要求用户输入数值范围的最小值和最大值。计算机随后“思考”出在这个范围之内的一个随机数，并且重复地要求用户猜测这个数，直到用户猜对了。在用户每次进行猜测之后，计算机都会给出一个提示，并且会在这个过程的最后显示出总的猜测次数。这个程序包含了几种类型的我们学过的 Python 语句，例如，输入语句、输出语句、赋值语句、循环和条件语句
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