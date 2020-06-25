a = {"aaa":111,"bbb":222,"ccc":333}
b = {"ddd":444,"eee":555,"fff":666}

# 合并字典
c = {}
for x in a:
    c[x] = a[x]
for x in b:
    c[x] = b[x]
print(c)

# 改变后
c = {**a,**b}
print(c)