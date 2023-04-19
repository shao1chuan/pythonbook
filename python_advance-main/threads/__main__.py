from threading import Thread


def task(count: int):
    for n in range(count):
        print(n)


thread1 = Thread(target=task, args=(10,))
thread2 = Thread(target=task, args=(20,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Main threads is end")
