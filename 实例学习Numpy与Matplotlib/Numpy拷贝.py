import  numpy as np
# reshape
b1 = np.arange(15)
b2 = b1.reshape((3,5))

b3 = b2[:2,:3]
b4 = b2[:2,:3].copy()
print(b3,b3)
b2[0,0] = 100
print(b3,b4)



