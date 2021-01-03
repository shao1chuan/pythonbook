import turtle
import math
import sys

tick = 0.1

position_human  = (150,50*(3**0.5))
position_lion_1 = (0,0)
position_lion_2 = (150,150*(3**0.5))

speed_human   = 10*tick
speed_lion_1  = 15*tick
speed_lion_2  = 20*tick

degree = 25
times = 0

#判断人在线上还是线下


while(True): #使其无限循环下去
  turtle.penup()
  turtle.goto(position_human)
  check_k = (position_lion_2[1]-position_lion_1[1])/(position_lion_2[0]-position_lion_1[0])
  check_b = position_lion_2[1] - (check_k*position_lion_2[0])
  check = check_k*position_human[0] + check_b
  #以下是人前进代码
  if(position_human[1]<check):
    #人在线条之下
    middle_dot = (((position_lion_2[0]+position_lion_1[0])/2),((position_lion_2[1]+position_lion_1[1])/2))
    turtle.setheading(turtle.towards(middle_dot)+degree)
    turtle.pendown()
    turtle.fd(speed_human)
    position_human = tuple(turtle.position())
    print("below")
  elif(position_human[1]>check):
    axis_k = (position_human[1]-position_lion_1[1])/(position_human[0]-position_lion_1[0])
    axis_b = position_human[1] - (axis_k*position_human[0])
    middle_dot = (((position_lion_2[0]+position_lion_1[0])/2),((position_lion_2[1]+position_lion_1[1])/2))
    vertical_k = -1/axis_k
    vertical_b = middle_dot[1] - (vertical_k*middle_dot[0])
    vertical_dot = ((vertical_b-axis_b)/(axis_k-vertical_k),(axis_k*((vertical_b-axis_b)/(axis_k-vertical_k)) + axis_b))
    point_dot = ((2*vertical_dot[0]-middle_dot[0]),(2*vertical_dot[1]-middle_dot[1]))
    turtle.pendown()
    turtle.setheading(turtle.towards(point_dot) + degree)
    turtle.fd(speed_human)
    position_human = tuple(turtle.position())
    print("above")
  elif(position_human == check):
    print("!!!!oneline")
    break
  distance_1 = turtle.distance(position_lion_1)
  distance_2 = turtle.distance(position_lion_2)
  if(distance_1<=speed_lion_1 or distance_2<=speed_lion_2):
    print(times)
    break
  #以下是狮子追人代码
  turtle.penup()
  turtle.goto(position_lion_1)
  turtle.setheading(turtle.towards(position_human))
  turtle.pendown()
  turtle.forward(speed_lion_1)
  position_lion_1 = tuple(turtle.position())
  turtle.penup()
  turtle.goto(position_lion_2)
  turtle.setheading(turtle.towards(position_human))
  turtle.pendown()
  turtle.forward(speed_lion_2)
  position_lion_2 = tuple(turtle.position())
  times = times + 1

# axis_k = (position_human[1]-position_lion_1[1])/(position_human[0]-position_lion_1[0])
# axis_b = position_human[1] - (axis_k*position_human[0])

# middle_dot = (((position_lion_2[0]-position_lion_1[0])/2),((position_lion_2[1]-position_lion_1[1])/2))

# vertical_k = -1/axis_k
# vertical_b = middle_dot[1] - (vertical_k*middle_dot[0])


# vertical_dot = ((vertical_b-axis_b)/(axis_k-vertical_k),(axis_k*((vertical_b-axis_b)/(axis_k-vertical_k)) + axis_b))

# point_dot = ((2*vertical_dot[0]-middle_dot[0]),(2*vertical_dot[1]-middle_dot[1]))


# turtle.pendown()
# turtle.goto(position_lion_2)
# turtle.penup()
# turtle.goto(position_human)
# turtle.pendown()
# turtle.setheading(turtle.towards(point_dot)+40)
# turtle.forward(100)
# turtle.penup()
# turtle.goto(position_human)
# turtle.setheading(turtle.towards(middle_dot))
# turtle.pendown()
# turtle.forward(100)

# turtle.penup()
# turtle.goto(position_lion_1)
# turtle.pendown()
# turtle.goto(position_lion_2)
# middle_dot = (((position_lion_2[0]-position_lion_1[0])/2),((position_lion_2[1]-position_lion_1[1])/2))
# print(middle_dot)
# turtle.penup()
# turtle.goto(position_human)
# turtle.pendown()
# turtle.setheading(turtle.towards(middle_dot) + 40 )

# turtle.fd(100)

input("ssssss")