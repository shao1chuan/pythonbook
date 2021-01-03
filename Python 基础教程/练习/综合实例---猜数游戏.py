import random
import pickle
from collections import deque

n = random.randint(0, 100)  # 随机找出0-100之中的数
history_list = deque([], maxlen=5)  # 限制最大长度
try_num = 0
print(n)


def pk(m):
    if m != n:
        if m > n:
            print("大了")
        else:
            print("小了")
        return False
    return True


def h_print():# pickle取
    ret = pickle.load(open('history', 'rb'))
    return ret


def history(history_list): # pickle存
    history_list = list(history_list)
    pickle.dump(history_list, open('history', 'wb'))


while True:
    try_num += 1
    if try_num > 10:
        print("尝试次数过多，您已经笨死了！！！")
        break
    m = input("输入您的答案:")
    try:                               # 异常处理 防止用户输入字母
        # m = input("输入您的答案:")
        if len(m) == 0:
            print("not null")
        m = int(m)
        history_list.append(m)
        history(history_list)
        if pk(m) == True:
            print("以您的智商，居然TM答对了")
            break
    except ValueError:
        if m == "h":
            print("您猜数的历史记录：")
            print(h_print())
        else:
            print("格式有误，请输入整数字")