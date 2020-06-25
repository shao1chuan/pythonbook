# 从最简单的例子开始，比如我们想测试一个列表推导式究竟要比正常写for快多少。
import timeit
foooo = """
sum = []
for i in range(1000):
    sum.append(i)
"""
print(timeit.timeit(stmt="[i for i in range(1000)]", number=100000))
print(timeit.repeat(stmt=foooo, number=100000))