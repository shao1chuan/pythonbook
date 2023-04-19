import multiprocessing
import time


def task(name: str, count: int):
    print(f"{name} - start\n", end='')
    result = 0
    for n in range(count):
        result += n + 1
    # time.sleep(1)
    print(f"{name} - end with {result}")


def start_process_1():
    process = multiprocessing.Process(target=task, args=["A", 100])

    process.start()

    process.join()

    print("Main process over")


def start_process_2():
    args_list = [("A", 1000000), ("B", 9900000), ("C", 98000)]
    processes = [multiprocessing.Process(target=task, args=[name, count]) for name, count in args_list]
    processes[0].start()
    processes[1].start()
    processes[1].join()

    # for p in processes:
    #     p.start()
    #
    # for p in processes:
    #     p.join()

    print("Main process over")



if __name__ == "__main__":
    start_process_2()
