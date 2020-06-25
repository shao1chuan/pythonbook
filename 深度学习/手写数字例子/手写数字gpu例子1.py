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


device = torch.device("cuda:0")


class DrNet(torch.nn.Module):
    def __init__(self):
        super(DrNet, self).__init__()

        self.model = torch.nn.Sequential(
            torch.nn.Linear(784, 256),
            torch.nn.ReLU(inplace=True),
            torch.nn.Linear(256, 64),
            torch.nn.ReLU(inplace=True),
            torch.nn.Linear(64, 10),
        )

    def forward(self, x):
        x = self.model(x)
        return x


net = DrNet()
net = net.to(device)


train_loader = torch.utils.data.DataLoader(
    datasets.MNIST('mnist_data',
                   train=True,
                   download=True,
                   transform=transforms.Compose([transforms.ToTensor()])))


train_images = torch.zeros(60000, 784)
train_number = torch.zeros(60000, dtype=torch.int64)

train_images = train_images.to(device)
train_number = train_number.to(device)

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

test_images = test_images.to(device)
test_number = test_number.to(device)


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


loss_array = []


def compute(source):
    result = net(source)
    return result


loop = 5


def train():
    global net
    optimizer = torch.optim.Adam(net.parameters(), lr=0.01)

    for i in range(0, loop):

        r = compute(train_images)
        loss = torch.nn.functional.cross_entropy(r, train_number)
        loss_array.append(loss)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()


        if i % 10 == 0:
            print(f"loss={loss} time={i}")


t = time.time()
train()
print(time.time() - t)

matplotlib.pyplot.figure()
matplotlib.pyplot.plot(range(0, len(loss_array)), loss_array)
matplotlib.pyplot.show()

test_result = compute(test_images)
test_index = test_result.argmax(1)
test_eq = test_index.eq(test_number)
test_total = test_eq.sum()

print('accuracy:')
print(test_total * 100.0/10000)


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 6666))

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