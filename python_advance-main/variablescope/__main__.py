count = 10

print(count)


def greeting(flag: bool):
    global count
    if flag:
        count = 20

    print(count)


greeting(True)

print(count)

