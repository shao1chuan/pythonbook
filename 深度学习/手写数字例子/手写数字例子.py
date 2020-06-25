import torch
from torch import nn
from torch.nn import functional as F
from torch import optim

import  torchvision
from matplotlib import pyplot as plot
from    utils import plot_image, plot_curve, one_hot, save_data

# step1 装数据

batch_size = 512

# step1. load dataset
train_loader = torch.utils.data.DataLoader(
    torchvision.datasets.MNIST('mnist_data', train=True, download=True,
                               transform=torchvision.transforms.Compose([
                                   torchvision.transforms.ToTensor(),
                                   torchvision.transforms.Normalize(
                                       (0.1307,), (0.3081,))
                               ])),
    batch_size=batch_size, shuffle=True)

test_loader = torch.utils.data.DataLoader(
    torchvision.datasets.MNIST('mnist_data/', train=False, download=True,
                               transform=torchvision.transforms.Compose([
                                   torchvision.transforms.ToTensor(),
                                   torchvision.transforms.Normalize(
                                       (0.1307,), (0.3081,))
                               ])),
    batch_size=batch_size, shuffle=False)

x,y = next(iter(train_loader))
print(x.shape,y.shape,x.min(),y.min())
# plot_image(x,y,'sample')

# step2 构建神经网络
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()

        # xw+b
        self.fc1 = nn.Linear(28*28, 256)
        self.fc2 = nn.Linear(256, 64)
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):
        # x: [b, 1, 28, 28]
        # h1 = relu(xw1+b1)
        x = F.relu(self.fc1(x))
        # h2 = relu(h1w2+b2)
        x = F.relu(self.fc2(x))
        # h3 = h2w3+b3
        x = self.fc3(x)

        return x

    def backward(self, x):
        # x: [b, 1, 28, 28]
        # h1 = relu(xw1+b1)
        x = F.relu(self.fc1(x))
        # h2 = relu(h1w2+b2)
        x = F.relu(self.fc2(x))
        # h3 = h2w3+b3
        x = self.fc3(x)

        return x
# step3 训练网络
net = Net()
optimizer = optim.SGD(net.parameters(), lr=0.01, momentum=0.9)
train_loss = []
for epoch in range(10):
    for idx,(x,y) in enumerate(train_loader):
        x = x.view(x.size(0),28*28)
        # =>[b,10]
        out = net(x)
        y_onehot = one_hot(y)
        loss = F.mse_loss(out,y_onehot)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        train_loss.append(loss.item())
        if idx %10 ==0:
            print(epoch,idx,loss.item())
# step4 可视化显示
save_data(train_loss,'train_loss.csv')
plot_curve(train_loss)

total_correct = 0
for x,y in test_loader:
    x = x.view(x.size(0),28*28)
    out = net(x)
    pred = out.argmax(dim = 1)
    correct = pred.eq(y).sum().float().item()
    total_correct+=correct
total_num = len(test_loader.dataset)
acc = total_correct / total_num

print("acuccy",acc)

x,y = next(iter(test_loader))
out = net(x.view(x.size(0),28*28))
pred = out.argmax(dim = 1)
plot_image(x,pred,"test")


