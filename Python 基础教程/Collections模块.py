from collections import defaultdict
person = defaultdict(lambda : 'Key Not found') # 初始默认所有key对应的value均为‘Key Not Found’

person['name'] = 'xiaobai'
person['age'] = 18

print ("The value of key  'name' is : ",person['name'])
print ("The value of key  'adress' is : ",person['city'])
