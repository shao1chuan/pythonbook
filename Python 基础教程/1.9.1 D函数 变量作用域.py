# global关键字声明的变量必须在全局作用域上，不能嵌套作用域上，
# 当要修改嵌套作用域（enclosing作用域，外层非全局作用域）中的变量怎么办呢，这时就需要nonlocal关键字了
def outer():
    count = 10
    def inner():
        # nonlocal count
        # global count
        count = 100
        print(count)
    inner()
    print(count)
outer()

# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了，
# 当修改的变量是在全局作用域（global作用域）上的，就要使用global先声明一下