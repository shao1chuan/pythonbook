import torch
import torchvision
import torchvision.transforms as transforms
import cv2
import numpy as np
import matplotlib.pyplot as plt
BATCH_SIZE=200
path_train = './data/train/'
path_vaild = './data/vaild/'
transforms_train = transforms.Compose([
    transforms.Grayscale(),#使用ImageFolder默认扩展为三通道，重新变回去就行
    transforms.RandomHorizontalFlip(),#随机翻转
    transforms.ColorJitter(brightness=0.5, contrast=0.5),#随机调整亮度和对比度
    transforms.ToTensor()
])
transforms_vaild = transforms.Compose([
    transforms.Grayscale(),
    transforms.ToTensor()
])
data_train = torchvision.datasets.ImageFolder(root=path_train,transform=transforms_train)
print(data_train[0][0])
data_vaild = torchvision.datasets.ImageFolder(root=path_vaild,transform=transforms_vaild)
train_set = torch.utils.data.DataLoader(dataset=data_train,batch_size=BATCH_SIZE,shuffle=True)
vaild_set = torch.utils.data.DataLoader(dataset=data_vaild,batch_size=BATCH_SIZE,shuffle=False)
for i in range(1,16+1):
    plt.subplot(4,4,i)
    plt.imshow(data_train[0][0].reshape(-1,48*48),cmap='Greys_r')
    plt.axis('off')
plt.show()