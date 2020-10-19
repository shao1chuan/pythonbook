# 加了星号（*）的变量名会存放所有未命名的变量参数。而加(**)的变量名会存放命名的变量参数
def print_info(**kwargs):
    print(kwargs)
    for i in kwargs:
        print('%s:%s'%(i,kwargs[i]))#根据参数可以打印任意相关信息了
        return
print_info(name='alex',age=18,sex='female',hobby='girl',nationality='Chinese',ability='Python')

def print_info(name,*args,**kwargs):#def print_info(name,**kwargs,*args):报错
    print('Name:%s'%name)
    print('args:',args)
    print('kwargs:',kwargs)
    return
print_info('alex',18,17,'dfgdfg',hobby='girl',nationality='Chinese',ability='Python')
# print_info(hobby='girl','alex',18,nationality='Chinese',ability='Python')  #报错
#print_info('alex',hobby='girl',18,nationality='Chinese',ability='Python')   #报错

def f(*args):
    print(args)

f(*[1,2,5])

def f(**kargs):
    print(kargs)
f(**{'name':'alex'})