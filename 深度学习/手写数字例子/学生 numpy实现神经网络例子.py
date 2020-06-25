
"""
线性回归测试
"""

import numpy as np
import  torch
import  torch.nn as nn
import  torch.nn.functional as F
import  torch.optim as optim

import matplotlib.pyplot

def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))         #定义sigmoid函数

"""
定义学习次数 epochs为100
定义学习率为 0.01
对x在-2到2区间内采样1000个值
定义回归目标函数 y = x^完整例子
"""
epochs = 100
learning_rate=0.01
lr = learning_rate
x = torch.linspace(-2., 2., 1000)
y = x**2

"""
定义三个权重，分别为 wih, whh, who
wih: weight of input layer to hidden layer 1        矩阵长度【 1X4 】
whh: weight of hidden layer 1 to 完整例子                     矩阵长度【 4X4 】
who: weight of hidden layer 完整例子 to output layer    矩阵长度【 4X1 】
"""

wih = np.random.rand(1, 4)
whh =  np.random.rand(4, 4)
who =  np.random.rand(4, 1)

def forward(input):

    result1 = input@wih                     #初始值传入第一个隐藏层时进行加权计算
    input1 = sigmoid(result1)              #第一次加权运算后对结果进行sigmoid压缩
    result2 = input1@whh                  #压缩后的结果传入第二层隐藏层时进行加权运算
    input2 = sigmoid(result2)             #对第二次加权运算结果进行sigmoid压缩
    result3 = input2@who                 #压缩后的结果传入输出层时进行加权运算，得到的结果result3即为输出值

    final_result = result3
    return final_result, result2, result1, input

"""
定义损失函数，用来计算三个层面的权值改变，分别为eoh， ehh， ehi
eoh：输出层与第二隐藏层之间的损失值
ehh：第二隐藏层与第一隐藏层之间的损失值
ehi ：第一隐藏层与输入层之间的损失值
"""
def loss(result):
    eho = target - result
    ehh = np.dot(who, [eho])
    ehi = np.dot(whh.T, ehh)
    return eho, ehh, ehi

def backward(eho,ehh,ehi,final_result,result2,result1,input):
    global who,whh,wih
    who += lr * np.dot((eho * final_result * (1.0 - final_result)), np.transpose(result2))
    whh += lr * np.dot((ehh * result2 * (1.0 - result2)), np.transpose(result1))
    wih += lr * np.dot((ehh * result1 * (1.0 - result1)), np.transpose(input))


for z in range(4):
    target = z*z
    final_result,result2,result1,input=forward([z])

    eho,ehh,ehi = loss(final_result)

    backward(eho,ehh,ehi,final_result,result2,result1,input)

    print("输出结果误差",eho)




