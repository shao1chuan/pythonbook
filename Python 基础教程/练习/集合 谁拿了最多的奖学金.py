# 4
# YaoLin 87 82 Y N 0
# ChenRuiyi 88 78 N Y 1
# LiXin 92 88 N N 0
# ZhangQin 83 87 Y N 1

num = int(input('请输入学生数量：'))
std_dict = {}
for i in range(num):
    line = input(f'请输入第{i+1}名学生信息')
    stu_lst = line.split(' ')
    std_dict[stu_lst[0]] = stu_lst[1:]

# print(std_dict)
reward_dict = {}
#开始计算每一位学生的奖学金
for stu_name,stu_info in std_dict.items():
    if int(stu_info[0]) > 80 and int(stu_info[4]) > 0:
        reward_dict[stu_name] = reward_dict.get(stu_name,0) + 8000
    if int(stu_info[0]) > 85 and int(stu_info[1]) > 80:
        reward_dict[stu_name] = reward_dict.get(stu_name, 0) + 4000
    if int(stu_info[0]) > 90:
        reward_dict[stu_name] = reward_dict.get(stu_name, 0) + 2000
    if int(stu_info[0]) > 85 and stu_info[3] == 'Y':
        reward_dict[stu_name] = reward_dict.get(stu_name, 0) + 1000
    if int(stu_info[1]) > 80 and stu_info[2] == 'Y':
        reward_dict[stu_name] = reward_dict.get(stu_name, 0) + 850

sum = 0
max = 0
max_stu = ''
for stu_name,money in reward_dict.items():
    if max < money:
        max = money
        max_stu = stu_name
    sum += money

print(max_stu)
print(max)
print(sum)