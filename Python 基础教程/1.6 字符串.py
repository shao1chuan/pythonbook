# strip 默认去除字符前后两端的空格， 换行符， tab
ss = '     qqwalex qqwusir barryy'
s = ss.strip()
print(s)
print(s.strip('qqw'))
print(s.strip(''))
print(s.lstrip('yy'))
print(s.rstrip('yy'))

# split 把字符串分割成列表
#### 分割出的元素比分隔符数+1  ***
#### 字符串变成->>>列表
s = 'qqwalex qqwusir barryy'
s1 = 'qqwale;x qqwu;sir bar;ryy'
print(s.split())    #### 默认以空格分割
print(s1.split(';'))    #### 以指定字符分割
print(s1.split(';', 1)) #### 指定分割多少个

# join把列表转化成字符串
#### 列表转化成字符串 list --> str
s = 'alex'####看成字符列表
li = ['aa', 'ddj', 'kk']    #### 必须全是字符串
s1 = '_'.join(s)
print(s1)
s2 = '   '.join(li)
print(s2)

#### count 计算字符串中某个字符出现的次数  ***
s = 'www.neuedu.com'
print(s.count('u'))
print(s.count('u', 7))

#### format 格式化输出  ***
#### 第一种方式：
s = '我叫{}, 今年{}， 性别{}'.format('小五', 25, '女')
print(s)
#### 第二种方式
s1 = '我叫{0}, 今年{1}， 性别{2}，我依然叫{0}'.format('小五', 25, '女')
print(s1)
#### 第三种方式
s2 = '我叫{name}, 今年{age}， 性别{sex}，我依然叫{name}'.format(age=25, sex='女',name='小五')
print(s2)
# 字符串是不可变变量，不支持直接通过下标修改
msg = 'abcdefg'
# msg[2] = 'z'
msg = msg[:2] + 'z' + msg[3:]
print(msg)