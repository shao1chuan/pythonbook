def f(x):
    return (x-6)**2 -3

def df(x):
    return 2*(x-6)


if __name__ == '__main__':
    x0 = 14
    y = []

    step = 400
    lr = 0.01
    x = x0
    for i in range(step):
        x = x-df(x)*lr
        y.append(f(x))
    print(y)