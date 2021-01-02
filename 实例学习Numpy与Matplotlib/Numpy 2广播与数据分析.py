import  numpy as np

a = np.arange(0,12,2).reshape(2,3)
b = np.arange(3)

print(f"a = {a}")
print(f"b = {b}")
a1 = a+b
print(f"a1 = {a1}")
a2 = np.row_stack([a,b])
print(f"a2 = {a2}")

a = np.arange(12).reshape(4,3)
b = np.array([5,15,25])
a3 = a+b
print(f"a3 = {a3}")