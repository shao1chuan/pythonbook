def add(*aa,sum1 = 1):
    sum = 0
    for i in aa:
        sum+=i
    return sum+sum1

print(add(2,3,4,12))