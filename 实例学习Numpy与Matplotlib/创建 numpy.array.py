
import numpy as np
nparr = np.array([i for i in range(10)])

a = np.zeros(10)
f = np.zeros(10,dtype=float)
n = np.full((3,5),44)
r = np.random.randint(0,100,size=(3,5))
r2 = np.random.random((3,5))
x = np.linspace(0,100,50)
print(nparr,a,f,n,r,r2,x)