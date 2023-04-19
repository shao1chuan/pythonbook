message = "module"


def outer():
    message = "outer"

    def inner():
        nonlocal message

        message = "inner"
        print(message)

    inner()
    print(message)


outer()

print(message)
