
import torch
from torch.autograd import Variable
a = Variable(torch.rand(1, 4), requires_grad=True)
b = a**2
c = b*2
d = c.mean()
e = c.sum()

d.backward(retain_graph=True) # fine
e.backward(retain_graph=True) # fine
d.backward() # also fine
e.backward() # error will occur!