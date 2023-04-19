l = [i for i in range(2,30)]
print(l)
for i in range(2,30):
    for j in range(2,i):
        if i%j ==0:
            print(f"{i} is not zhishu")
            l.remove(i)
            break
print(l)


