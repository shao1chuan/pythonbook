# 已知有十六支男子足球队参加2008 北京奥运会。写一个程序，把这16 支球队随机分为4 个组。采用List集合和随机数
# 2008 北京奥运会男足参赛国家：
# 科特迪瓦，阿根廷，澳大利亚，塞尔维亚，荷兰，尼日利亚，日本，美国，中国，新西兰，巴西，比利时，韩国，喀麦隆，洪都拉斯，意大利
# 提示：分配一个，删除一个
# // key保存的是第几组，value是该组对应的国家集合
# // map，保存最终分组结果
import random
dic = {}
country = "科特迪瓦，阿根廷，澳大利亚，塞尔维亚，荷兰，尼日利亚，日本，美国，中国，新西兰，巴西，比利时，韩国，喀麦隆，洪都拉斯，意大利"
country = country.split('，')
print (country)

# 方法1
import random
value = [i for i in range(1,len(country))]
random.shuffle(value)
print(value)
dic = {k:v for k,v in zip(country,value)}
map = {}
for i in range(1,5):
    li = []
    for j in range(4):
        index = random.randint(0,len(country)-1)
        li.append(country[index])
        country.remove(country[index])
    map[i] = li
print(map)
