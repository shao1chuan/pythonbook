import time
from threading import Thread
from queue import Queue


class MyThread(Thread):
    def __init__(self, name: str, count: int):
        super().__init__()

        self.setName(name)
        self.setDaemon(True)
        self.count = count

    def run(self) -> None:
        for n in range(self.count):
            print(f"{self.getName()} - {n}\n", end='')
            time.sleep(0.01)


t_1 = MyThread("A", 10)
t_2 = MyThread("B", 10)

t_1.start()
t_2.start()

t_1.join()


class MsgProducer(Thread):
    def __init__(self, name: str, count: int, queue: Queue):
        super().__init__()

        self.setName(name)
        self.count = count
        self.queue = queue

    def run(self) -> None:
        for n in range(self.count):
            msg = f"{self.getName()} - {n}"
            self.queue.put(msg, block=True)


class MsgConsumer(Thread):
    def __init__(self, name: str, queue: Queue):
        super().__init__()

        self.setName(name)
        self.queue = queue
        self.setDaemon(True)

    def run(self) -> None:
        while True:
            msg = self.queue.get(block=True)
            print(f"{self.getName()} - {msg}\n", end='')


queue = Queue(3)
threads = list()
threads.append(MsgProducer("PA", 10, queue))
threads.append(MsgProducer("PB", 10, queue))
threads.append(MsgProducer("PC", 10, queue))

threads.append(MsgConsumer("CA", queue))
threads.append(MsgConsumer("CB", queue))

for t in threads:
    t.start()


