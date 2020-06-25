# 原始
def fibonacci(n):
    a = 0
    b = 1
    nums = []
    for _ in range(n):
        nums.append(a)
        a,b = b,a+b
    return nums

print(fibonacci(12))

def fibonacci(n):
    a = 0
    b = 1
    # nums = []
    for _ in range(n):
        yield a
        # nums.append(a)
        a,b = b,a+b
    # return nums

for i in fibonacci(12):
    print(i)