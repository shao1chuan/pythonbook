Foo = type('Foo', (), {'bar':True})


# class Foo(object):
#     bar = True

def echo_bar(self):  # 定义了一个普通的函数
    print(self.bar)

FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar}) #让FooChild类中的echo_bar属性，指向了上面定义的函数