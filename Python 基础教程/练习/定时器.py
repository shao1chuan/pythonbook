#引入库 threading
import threading
#定义函数
def printaaa():
    print(111)

timer = threading.Timer(1,printaaa)  #首次启动
timer.start()