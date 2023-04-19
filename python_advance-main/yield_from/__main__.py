def magic_number(exponent: int):
    for n in range(3):
        yield (n + 1) ** exponent


def magic_data():
    yield from magic_number(2)
    yield from magic_number(3)


# for n in magic_data():
#     print(n)


def magic_two():
    exponent = yield 'Please give an exponent based on two'

    while True:
        exponent = yield 2 ** exponent

        if exponent is None:
            break


# m = magic_two()
# print(next(m))
#
# print(m.send(2))
#
# print(m.send(3))
#
# try:
#     m.send(None)
# except StopIteration:
#     pass


def magic_three():
    exponent = yield 'Please give an exponent based on three'

    while True:
        exponent = yield 3 ** exponent

        if exponent is None:
            break


def magic_switch():
    option = yield 'Please choose, 1 - two, 2 - three'

    while True:
        if option == 1:
            yield from magic_two()
        elif option == 2:
            yield from magic_three()
        else:
            break


mm = magic_switch()
print(next(mm))
print(mm.send(2))
print(mm.send(2))
print(mm.send(3))
try:
    mm.send(None)
except StopIteration:
    pass

