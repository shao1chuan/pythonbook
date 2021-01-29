# https://www.cnblogs.com/ssyfj/p/12913015.html

# https://www.jianshu.com/p/42b0b6ffcf97

import numpy as np
# 1-D array
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print('result1 = a*b', a*b)
print('result2 = a@b' ,a@b)
# result1 = a@b [ 4 10 18]
# result2 = b@a 32

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2], [3, 4], [5, 6]])
print("result3 = a@b",a@b)
# result3 = a@b [[22 28]
#   [49 64]]

a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([1, 2, 3,4])

outer_result_1 =  np.outer(a,b)
print('outer_result_1:\n %s' %(outer_result_1))
# outer_result_1:
#  [[ 1  2  3  4]
#  [ 2  4  6  8]
#  [ 3  6  9 12]
#  [ 4  8 12 16]
#  [ 5 10 15 20]
#  [ 6 12 18 24]]

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2], [3,4]])

outer_result_2 =  np.outer(a,b)
print('outer_result_2:\n %s' %(outer_result_2))
# outer_result_2:
#  [[ 1  2  3  4]
#  [ 2  4  6  8]
#  [ 3  6  9 12]
#  [ 4  8 12 16]
#  [ 5 10 15 20]
#  [ 6 12 18 24]]


