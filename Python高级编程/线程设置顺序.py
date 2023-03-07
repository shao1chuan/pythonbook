import threading
import time


def thread_test1(a):
    time.sleep(10)
    print("thread_pool_list111: ",a)

def thread_test2(a):
    time.sleep(10)
    print("thread_pool_list2222: ",a)

def main_model():
    print('aaa')

    thread_pool_list111 = []
    thread_pool_list2222 = []
    '''开启多线程n个'''
    n = 5
    for i in range(n):
        t = threading.Thread(target=thread_test1, args=(i,))
        thread_pool_list111.append(t)

    for i in range(n):
        t = threading.Thread(target=thread_test2, args=(i,))
        thread_pool_list2222.append(t)
    '''一个一个启动线程'''
    for t in thread_pool_list111:
        t.start()
    for t in thread_pool_list2222:
        t.start()

    '''线程同步,也就是需要两个线程都跑完后，才继续跑主线程；反之则直接跑主线程，不需要等这两个跑完才跑主线程'''
    for t in thread_pool_list111:
        t.join()
    print('bbb')

if __name__ == '__main__':
    main_model()