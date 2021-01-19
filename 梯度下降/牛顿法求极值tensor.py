import torch
from torch.autograd import Variable
def f(x):
    y = x ** 2 -3
    return y
x = Variable(torch.Tensor([15]), requires_grad=True)
for i in range(40):
    grad_x = torch.autograd.grad(f(x), x, create_graph=True)
    grad_grad_x = torch.autograd.grad(grad_x[0], x)
    x = Variable(x.data - grad_x[0].data / grad_grad_x[0].data, requires_grad=True)
print(x)
