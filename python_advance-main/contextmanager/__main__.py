# instance = open("mydata.txt", "w")
# instance.write("Hello this is a test file")
# instance.close()

# with open("mydata.txt", "w") as instance:
#     instance.write("Hello this is a test file")
#
#
# print("The end")
import time


class Timer:
    def __init__(self):
        self.elapsed = 0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time.perf_counter()
        self.elapsed = self.stop - self.start
        return False


with Timer() as timer:
    nums = []
    for n in range(10000):
        nums.append(n ** 2)

print(timer.elapsed)


