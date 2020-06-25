import torch
import torch.nn
import torch.nn.functional
import torch.optim
import torch.utils.data
import numpy
import matplotlib
import matplotlib.pyplot
import time
import torchvision
from torchvision import *
import matplotlib.colors
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 6666))


device = torch.device("cuda:0")

train_loader = torch.utils.data.DataLoader(
    datasets.MNIST('mnist_data',
                   train=True,
                   download=True,
                   transform=transforms.Compose([transforms.ToTensor()])))


train_images = torch.zeros(60000, 784)
train_number = torch.zeros(60000, dtype=torch.int64)

for index, data in enumerate(train_loader):
    image = data[0].squeeze()
    number = data[1]

    if index < 3:
        matplotlib.pyplot.figure()
        matplotlib.pyplot.imshow(image, cmap='gist_gray')
        matplotlib.pyplot.show()

    train_images[index] = image.view(-1)
    train_number[index] = number


print(train_images.shape)

test_loader = torch.utils.data.DataLoader(
    datasets.MNIST('mnist_data',
                   train=False,
                   download=True,
                   transform=transforms.Compose([transforms.ToTensor()])))


test_images = torch.zeros(10000, 784)
test_number = torch.zeros(10000, dtype=torch.int64)

for index, data in enumerate(test_loader):
    image = data[0].squeeze()
    number = data[1]

    if index < 3:
        matplotlib.pyplot.figure()
        matplotlib.pyplot.imshow(image, cmap='gist_gray')
        matplotlib.pyplot.show()

    test_images[index] = image.view(-1)
    test_number[index] = number


print(test_images.shape)

train_images = train_images.to(device)
train_number = train_number.to(device)

test_images = test_images.to(device)
test_number = test_number.to(device)


net_shape = [784, 256, 64, 64, 10]
net_f = [0, torch.sigmoid, torch.sigmoid, 0]

W = []
B = []
Params = []

for n in range(0, len(net_shape)-1):
    w = torch.randn(net_shape[n], net_shape[n+1])
    w = w.to(device)
    w.requires_grad = True
    W.append(w)
    b = torch.zeros(net_shape[n+1])
    b = b.to(device)
    b.requires_grad = True
    B.append(b)
    Params.append(w)
    Params.append(b)


loss_array = []


def compute(data):
    global W, B

    if data.dim() == 2:
        buffer = data
    if data.dim() == 1:
        buffer = data.unsqueeze(1)

    for i in range(0, len(net_shape)-1):
        buffer = torch.matmul(buffer, W[i]) + B[i]

        if net_f[i] != 0:
            buffer = net_f[i](buffer)

    if buffer.shape[1] == 0:
        result = buffer[:, 0]
    else:
        result = buffer

    return result


loop = 500
lr_base = 0.01


def train():
    global W, B, Params
    optimizer = torch.optim.Adam(Params, lr=0.01)

    for i in range(0, loop):

        r = compute(train_images)
        loss = torch.nn.functional.cross_entropy(r, train_number)
        loss_array.append(loss)
        loss.backward()

        optimizer.step()
        optimizer.zero_grad()

        if i % 10 == 0:
            print(f"loss={loss} time={i}")


t = time.time()
train()
print(time.time() - t)
print(f"w:{w[0]}")


for n in range(0, len(Params)):
    Params[n].requires_grad = False


matplotlib.pyplot.figure()
matplotlib.pyplot.plot(range(0, len(loss_array)), loss_array)
matplotlib.pyplot.show()

test_result = compute(test_images)


test_index = test_result.argmax(1)
test_eq = test_index.eq(test_number)
print(test_eq)
test_total = test_eq.sum()


print('accuracy:')
print(test_total * 100.0/10000)


while True:
    data, address = s.recvfrom(8192)
    temp = torch.zeros(1, 784)
    for i in range(0, 784):
        temp[0, i] = data[i] / 255.0

    temp_image = temp.view(28, 28)

    temp = temp.to(device)
    temp_result = compute(temp)
    temp_index = temp_result.argmax(1)

    s.sendto(bytes([temp_index]), address)  #upper() 小写变大写


    matplotlib.pyplot.figure()
    matplotlib.pyplot.imshow(temp_image, cmap='gist_gray')
    matplotlib.pyplot.show()
