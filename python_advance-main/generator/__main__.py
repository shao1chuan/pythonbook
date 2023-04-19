def hello():  # an iteratable object
    print("step 1")
    yield 1
    print("step 2")
    yield 2
    print("step 3")
    yield 3


def my_fun():
    result = []
    for n in range(3):
        result.append(n ** 2)

    return result


g = hello()
for res in g:
    print(res)


def squares(count: int):
    for n in range(count):
        yield n ** 2


for num in squares(3):
    print(num)
