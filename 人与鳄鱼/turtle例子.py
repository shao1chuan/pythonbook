# turtle.setheading()：设置当前画笔朝向，即人或鳄鱼的朝向
# turtle.distance()：获取两个坐标之间的距离
# turtle.position()：得到当前位置的坐标（用来获得人或鳄鱼在每次运动之后的坐标）
# turtle.towards()：得到两个坐标之间的相位角（鳄鱼需要不停的调整角度来使鳄鱼的脸一直朝着人的方向


#代码写的比较乱，直接在前一个案例基础上改进的

import turtle, time
def drawGap(): #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):   #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDigit(d): #根据数字绘制七段数码管
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write('年',font=("Arial", 18, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font=("Arial", 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=("Arial", 18, "normal"))
            turtle.fd(40)
        else:
            drawDigit(eval(i))
def all(day):
    turtle.goto(-350,-300)
    turtle.pencolor("orange")
    turtle.write('总共',font=("Arial", 40, "normal"))
    turtle.fd(110)
    for j in day:
        drawDigit(eval(j))
    turtle.write('天',font=("Arial", 18, "normal"))
def count(t1,t2,t3):
    t=t1*365
    if t2 in [1,2]:
        t+=t2*30
    if t2 in [3]:
        t=t+91
    if t2==4:
        t+=122
    if t2==5:
        t+=152
    if t2==6:
        t+=183
    if t2==7:
        t+=213
    if t2==8:
        t+=244
    if t2==9:
        t+=275
    if t2==10:
        t+=303
    if t2==11:
        t+=334
    t+=t3
    return(str(t))
def text():
    turtle.penup()
    turtle.goto(-350,400)
    turtle.pendown()
    turtle.write('今天是：',font=("Arial", 18, "normal"))
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(-350,300)
    turtle.pendown()
    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
    turtle.penup()
    turtle.goto(-350,200)
    turtle.pensize(1)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.write('孙小姐和刘先生在一起：',font=("Arial", 18, "normal"))
    turtle.penup()
    turtle.goto(-350,100)
    turtle.pendown()
    turtle.pensize(5)
    drawDate('2018-05=10+')
    turtle.penup()
    turtle.goto(-350,0)
    turtle.pensize(1)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.write('我们一起经历了：',font=("Arial", 18, "normal"))
    turtle.penup()
    turtle.goto(0,-100)
    turtle.pensize(1)
    turtle.pendown()
def main():
    turtle.setup(900, 900, 200, 0)
    text()
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(5)
#    drawDate('2018-10=10+')
    t1=time.gmtime()
    t2=t1.tm_year-2018
    t3=t1.tm_mon-5
    if t3<0:
        t2-=1
        t3+=12
    t4=t1.tm_mday-10
    if t4<0:
        t3-=1
        if t1.tm_mon-1 in [1,3,5,7,8,10,12]:
            t4+=31
        else:
            t4+=30
    tatol=count(t2,t3,t4)
    drawDate(str(t2)+'-'+str(t3)+'='+str(t4)+'+')
    all(tatol)
    turtle.hideturtle()
    turtle.done()
main()
