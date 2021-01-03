import  numpy as np
# reshape
b1 = np.arange(15)
# b1 = [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
b2 = b1.reshape((3,5))
#   b2 = [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]
b3 = b2.reshape(-1,3)  #无论多少行  回城3列
b4 = b1.reshape(5,-1) #无论多少列  回城5行
print(f"b1 = {b1} \n  "
      f"b2 = {b2} \n  "
      f"b3 = {b3} \n  "
      f"b4 = {b4} \n  ")





