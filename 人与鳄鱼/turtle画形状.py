# https://blog.csdn.net/zhubao124/article/details/82867759
import turtle as tl
import time

tl.setup(500,500,0,0)
tl.pensize(2)
tl.pencolor('red')

tl.home()
for i in range(0,10):
    # tl.pendown()
    # tl.dot()
    # tl.penup()
    tl.forward(10)
    tl.right(60)
    tl.forward(10)

time.sleep(10)
