import  torch
import  torch.nn.functional as F

# a表示数据样本的概率
a = torch.tensor([0.3,0.3,0.3,0.3])
b = torch.tensor([0.001,0.001,0.009])
# a1的和表示数据样本的信息熵
a1 = -(a*torch.log2(a)).sum()
b1 = -(b*torch.log2(b)).sum()
print("a1的和表示数据样本的信息熵 : ",a1," b1的和表示数据样本的信息熵 : ",b1)

# a表示真是样本的分类信息 比如狗的照片，其余都不是狗
a = torch.tensor([1.,0,0])
out = torch.tensor([1.1,1,0.1])
# 首先out需要softmax
out = out.view(1,-1)
out = F.softmax(out,dim=1)
print("out需要softmax",out)
# tensor([[0.6590, 0.2424, 0.0986]])
# a与out的交叉熵表示为
out= out.view(1,-1)
print(-(a*torch.log2(out)).sum())


print(torch.nn.CrossEntropyLoss(out,a.view(-1,1)))

