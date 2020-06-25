

CNN = nn.Sequential(
    nn.Conv2d(1,64,3),
    nn.ReLU(True),
    nn.MaxPool2d(2,2),
    nn.Conv2d(64,256,3),
    nn.ReLU(True),
    nn.MaxPool2d(3,3),
    Reshape(),# 两个卷积和池化后，tensor形状为（batchsize,256,7,7）
    nn.Linear(256*7*7,4096),
    nn.ReLU(True),
    nn.Linear(4096,1024),
    nn.ReLU(True),
    nn.Linear(1024,7)
    )

class Reshape(nn.Module):
    def __init__(self, *args):
        super(Reshape, self).__init__()
    def forward(self, x):
        return x.view(x.shape[0],-1)

class Reshape(nn.Module):
    def __init__(self, *args):
        super(Reshape, self).__init__()
    def forward(self, x):
        return x.view(x.shape[0],-1)