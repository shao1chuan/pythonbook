import matplotlib.pyplot as plt
import numpy as np
import json, time, requests, os

url = "https://zhujia.zhuwang.cc/api/chartData?areaId=-1&aa=%d"% int(time.time()*1000)

header = {'User-Agent': 'Mozilla/5.0'}
html = requests.get(url, headers=header).text

j0 = json.loads(html)

priceList = []

print("***********",j0.keys())

if not os.path.exists("猪肉价格"):
    os.mkdir("猪肉价格")

# j0['pig_in'][i], j0['pig_local'][i], j0['maizeprice'][i], j0['bean'][i]
for item in j0:
    if item != "time":
        f = open("猪肉价格/"+item+'.txt', 'w+')
        for i in range(366):
            f.write("%.2f\n" % float(j0[item][i]))
        f.close()
        plt.figure(item)
        plt.title(item)
        plt.plot(j0[item])
        plt.xlabel("时间")
        plt.ylabel("元/公斤")
        plt.xlim([0, 366])
        plt.savefig("猪肉价格/"+item + '.png', dpi=600)
    else:
        f = open("猪肉价格/"+item+'.txt', 'w+')
        for i in range(4):
            for j in range(3):
                f.write("%s" % j0[item][i][j])
            f.write("\n")