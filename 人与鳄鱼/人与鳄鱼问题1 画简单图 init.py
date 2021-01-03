

import turtle
import time

human = (0.00, 100)
lion1 = (100, 0.00)
angle1 = 0

angle = 240

turtle.pensize(3)

turtle.color("black")
turtle.penup()
turtle.goto(human)
turtle.dot(2, "red")
turtle.pendown()
turtle.setheading(angle)
turtle.fd(10)

human = turtle.position()

turtle.color("green")
turtle.penup()
turtle.goto(lion1)
turtle.dot(2, "black")
turtle.pendown()
angle1 = turtle.towards(human)
turtle.setheading(angle1)
turtle.forward(15)
lion1 = turtle.position()

time.sleep(10)