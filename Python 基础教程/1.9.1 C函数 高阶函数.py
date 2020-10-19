# 接受一个或多个函数作为输入 输出一个函数
def add(x, y, f):
    return f(x) + f(y)

res = add(3, -6, abs)
print(res)


def method():
    x = 2

    def double(n):
        return n * x

    return double


fun = method()
num = fun(20)
print(num)

