import random

random.randint(0, 10)
random.random()

s = 'helloWorld'
random.choice(s)

# random.sample(population, k)：在一个序列或者集合中选择k个随机元素()
random.sample('12345', 2)

# random.uniform(a, b)：产生一个指定范围内的随机浮点数 若a < b，随机数n范围：a <= n <= b； 若a > b，随机数n范围：a<= n <= b；
random.uniform(1,10)
random.randrange(1, 10, 1)   #[1,10)之间随机整数

# random.shuffle(x, random=None)：将列表顺序打乱；
l = ['C', 'C++', 'Java', 'C#', 'Python']
random.shuffle(l)