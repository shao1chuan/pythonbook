'''
    desc：尝试定义一种新的数据类型
          等差数列
'''
class ArithemeticSequence:
    def __init__(self, start=0, step=1):
        print('Call function __init__')

        self.start = start
        self.step = step
        self.myData = {}

    # 定义获取值的方法
    def __getitem__(self, key):
        print('Call function __getitem__')

        try:
            return self.myData[key]
        except KeyError:
            return self.start + key * self.step

    # 定义赋值方法
    def __setitem__(self, key, value):
        print('Call function __setitem__')
        self.myData[key] = value

    # 定义获取长度的方法
    def __len__(self):
        print('Call function __len__')

        return len(self.myData)

    # 定义删除元素的方法
    def __delitem__(self, key):
        print('Call function __delitem__')
        del self.myData[key]


s = ArithemeticSequence(1, 2)
print(s[0])
print(s[1])
print(s[2])
print(s[3])# 这里应该执行self.start+key*self.step，因为没有3这个key
s[3] = 100  # 进行赋值
print(s[3]) # 前面进行了赋值，那么直接输出赋的值100
print(len(s))
del s[3]  # 删除3这个key