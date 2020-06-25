class Spring(object):
    #season 为类的属性
    season = "the spring of class"
print(Spring.__dict__)
print(Spring.__dict__['season'])
# 实例属性的__dict__是空的，因为season是属于类属性
s= Spring()
print(s.__dict__)