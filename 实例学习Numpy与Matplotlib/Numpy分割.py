import  numpy as np
# reshape
b1 = np.arange(15)

a1,a2,a3 = np.split(b1,[3,7])
print(f"np.split(b1,[3,7] = \n",a1,a2,a3,"\n")

b2 = b1.reshape((3,5))
a1,a2,a3 = np.split(b2,[1,2],axis=1)
print(f"a1 = {a1}\n"
      f"a2 = {a2}\n"
      f"a3 = {a3}\n")


c1,c2 = np.hsplit(b2,[-1])
print(f"c1 = {c1}\n"
      f"c2 = {c2}\n")