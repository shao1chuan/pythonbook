# // map，保存最终分组结果
# // key保存的是第几组，value是该组对应的国家集合
import random
groupNum2Countrys = {}

strCountrys = "科特迪瓦，阿根廷，澳大利亚，塞尔维亚，荷兰，尼日利亚，日本，美国，中国，新西兰，巴西，比利时，韩国，喀麦隆，洪都拉斯，意大利";
countryList = strCountrys.split("，")

for i in range(4):
    lstGroup = []
    # // 分第1组
    # // 随机从集合中选出一个国家，放到第1组里；然后将这个选出的国家，从原来集合中干掉（删除）
    # // 重复以上步骤4次
    for j in range(4):
        selectIndex = random.randint(0,len(countryList)-1)
        lstGroup.append(countryList[selectIndex])
        countryList.remove(countryList[selectIndex])

    groupNum2Countrys[i+1] = lstGroup

for key,value in groupNum2Countrys.items():
    print('第' + str(key) + '组')
    print(value)