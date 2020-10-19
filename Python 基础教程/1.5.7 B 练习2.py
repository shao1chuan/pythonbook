# 2.给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
x = int(input())
y = list(str(x))
print(len(y))
y.reverse()
print(y)





