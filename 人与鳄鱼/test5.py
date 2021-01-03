# 5.机器人从原点（0,0）开始在平面中移动。 机器人可以通过给定的步骤向上，向下，向左和向右移动。
# 机器人运动的痕迹如下所示： UP 5 DOWN 3 LETF 3 RIGHT 2 方向之后的数字是步骤。
# 请编写一个程序来计算一系列运动和原点之后距当前位置的距离。
# 如果距离是浮点数，则只打印最接近的整数。
# 例：如果给出以下元组作为程序的输入：
# UP 5 DOWN 3 LETF 3 RIGHT 2 然后，程序的输出应该是：2

import turtle
import math
import time
print("请输入：")
str=input()
lis=str.split(" ")
for i in range(0,len(lis)-1):
    if lis[i]=='UP':
        turtle.left(90)
        turtle.fd(int(lis[i+1]))
        turtle.setheading(0)
    if lis[i]=='DOWN':
        turtle.right(90)
        turtle.fd(int(lis[i+1]))
        turtle.setheading(0)
    if lis[i]=='LETF':
        turtle.left(180)
        turtle.fd(int(lis[i+1]))
        turtle.setheading(0)
    if lis[i]=='RIGHT':
        turtle.fd(int(lis[i+1]))
#pos=turtle.position()
# print(pos)
# dis=math.sqrt(math.pow((pos[0]-0.0),2)+math.pow((pos[1]-0.0),2))
# print(round(dis))

