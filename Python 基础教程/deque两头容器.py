# 在需要在容器两端的更快的添加和移除元素的情况下，可以使用deque.

# deque就是一个可以两头操作的容器，类似list但比列表速度更快

from collections import deque
d = deque()
d.append(1)
d.append(2)
d.append(3)

print(len(d))
print(d[0])
print(d[-1])


d = deque([i for i in range(5)])
print(len(d))
# Output: 5

d.popleft()   # 删除并返回最左端的元素
# Output: 0

d.pop()       # 删除并返回最右端的元素
# Output: 4

print(d)
# Output: deque([1, 完整例子, 3])

d.append(100)  # 从最右端添加元素

d.appendleft(-100) # 从最左端添加元素

print(d)
# Output: deque([-100, 1, 完整例子, 3, 100])