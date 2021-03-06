# 设有三条鳄鱼ABC分别站在等边三角形的三个角上，一个人站在三角形的正中间。
# 每条鳄鱼和人的距离为100米，人的奔跑速度是10m/s鳄鱼A的奔跑速度是15m/s鳄鱼B和C的奔跑速度是20m/s。
# 问:这个人最多还能活几秒?


# 贪心算法
#
# 贪心算法（又称贪婪算法）是指，在对问题求解时，总是做出在当前看来是最好的选择。也就是说，不从整体最优上加以考虑，他所做出的是在某种意义上的局部最优解。
#
# 我的做法是：每过一段时间（比如0.1秒）做一次判断，选择此刻延直线距离运动到人 所需时间最短的那只鳄鱼，使人下一时间段所奔跑的方向为背离此鳄鱼的方向。
# 程序中以人为原点建立平面直角坐标系，输出每个时间点人和鳄鱼的坐标。当任意一只鳄鱼在下一时间段内，追上人所需时间小于单位时间，程序结束，并输出人奔跑的总时间。
# 将人和鳄鱼的所有时刻的坐标写入文件，用来画出运动轨迹。

import turtle

positionHuman = (0.00, 86.00)
positionLion1 = (-150.00, 0.00)
positionLion2 = (150.00, 0.00)
positionLion3 = (0.00, 260.00)
escapeDregree = 240

turtle.pensize(3)
for x in range(100):
    turtle.color("black")
    turtle.penup()
    turtle.goto(positionHuman)
    turtle.dot(2, "yellow")
    turtle.pendown()
    turtle.setheading(escapeDregree)

    lenthLion1 = turtle.distance(positionLion1)
    lenthLion2 = turtle.distance(positionLion2)
    if (x >= 2):
        if (lenthLion1 > lenthLion2):
            escapeDregree = escapeDregree - 20
            turtle.fd(10)
            print("1", escapeDregree)
        else:
            escapeDregree = escapeDregree + 20
            turtle.fd(10)
            print("2", escapeDregree)
    else:
        turtle.fd(10)
        print("3", escapeDregree)

    positionHuman = turtle.position()

    turtle.color("green")
    turtle.penup()
    turtle.goto(positionLion1)
    turtle.dot(2, "green")
    turtle.pendown()
    positionLion1ToHuman = turtle.towards(positionHuman)
    turtle.setheading(positionLion1ToHuman)
    turtle.fd(15)
    positionLion1 = turtle.position()

    turtle.color("red")
    turtle.penup()
    turtle.goto(positionLion2)
    turtle.dot(2, "red")
    turtle.pendown()
    positionLion2ToHuman = turtle.towards(positionHuman)
    turtle.setheading(positionLion2ToHuman)
    turtle.fd(20)
    positionLion2 = turtle.position()

    turtle.color("yellow")
    turtle.penup()
    turtle.goto(positionLion3)
    turtle.dot(2, "yellow")
    turtle.pendown()
    positionLion3ToHuman = turtle.towards(positionHuman)
    turtle.setheading(positionLion3ToHuman)
    turtle.fd(20)
    positionLion3 = turtle.position()