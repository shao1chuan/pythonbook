li =  ['a','b','c','d','e']
#index  0   1   2   3   4
#index -5  -4  -3  -2  -1
print(li[0:1])
print(li[2:])
print(li[::2])

print(li[:-2])
print(li[::-1])

# 在尾部最佳
li[len(li):]=[9]
# 删除前2个元素
li[:2] = []
print(li)

# 删除偶数位置上的元素
li =  ['a','b','c','d','e']
del li[::2]
print(li)

# 切片，浅复制
x = li[::]