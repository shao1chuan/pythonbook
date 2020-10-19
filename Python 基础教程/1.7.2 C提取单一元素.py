import random

li = [random.randint(1,10) for i in range(10)]
print(li)

norepeat = []
for i in li:
    if i not in norepeat:
        norepeat.append(i)
print(norepeat)
print(set(norepeat))
print(set(li))