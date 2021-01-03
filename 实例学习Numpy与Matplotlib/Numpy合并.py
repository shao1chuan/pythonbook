import  numpy as np
# reshape
b1 = np.arange(15)
# b1 = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
b2 = b1.reshape((3,5))
b2 = b2.reshape(1,-1)
b3 = b1[::-1].reshape(1,-1)
#   b2 = [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]
print(b1.shape,b2.shape,b3.shape)
b4 = np.concatenate([b2, b3])
print(f"b4 = {b4} \n  ")





