from threading import Thread, Lock, Condition


task_lock = Lock()


def task(name: str):
    global task_lock
    for n in range(2):
        task_lock.acquire()
        print(f"{name} - round {n} - step 1\n", end='')
        print(f"{name} - round {n} - step 2\n", end='')
        print(f"{name} - round {n} - step 3\n", end='')
        task_lock.release()


t1 = Thread(target=task, args=("A",))
t2 = Thread(target=task, args=("B",))
t3 = Thread(target=task, args=("C",))

t1.start()
t2.start()
t3.start()


class SafeQueue:
    def __init__(self, size: int):
        self.__item_list = list()
        self.size = size
        self.__item_lock = Condition()

    def put(self, item):
        with self.__item_lock:
            while len(self.__item_list) >= self.size:
                self.__item_lock.wait()

            self.__item_list.insert(0, item)
            self.__item_lock.notify_all()

    def get(self):
        with self.__item_lock:
            while len(self.__item_list) == 0:
                self.__item_lock.wait()

            result = self.__item_list.pop()
            self.__item_lock.notify_all()

            return result


class MsgProducer(Thread):
    def __init__(self, name: str, count: int, queue: SafeQueue):
        super().__init__()

        self.setName(name)
        self.count = count
        self.queue = queue

    def run(self) -> None:
        for n in range(self.count):
            msg = f"{self.getName()} - {n}"
            self.queue.put(msg)


class MsgConsumer(Thread):
    def __init__(self, name: str, queue: SafeQueue):
        super().__init__()

        self.setName(name)
        self.queue = queue
        self.setDaemon(True)

    def run(self) -> None:
        while True:
            msg = self.queue.get()
            print(f"{self.getName()} - {msg}\n", end='')


queue = SafeQueue(3)
threads = list()
threads.append(MsgProducer("PA", 10, queue))
threads.append(MsgProducer("PB", 10, queue))
threads.append(MsgProducer("PC", 10, queue))

threads.append(MsgConsumer("CA", queue))
threads.append(MsgConsumer("CB", queue))

for t in threads:
    t.start()
