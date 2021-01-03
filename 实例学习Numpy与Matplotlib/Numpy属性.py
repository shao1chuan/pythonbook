import  numpy as np
# reshape
b1 = np.arange(15)
b2 = b1.reshape((3,5))
print(f"b1 = {b1} \n  "
      f"b2 = {b2}  \n  "
f"b1.ndim = {b1.ndim}  b2.ndim= {b2.ndim}  \n "
f"b1.shape = {b1.shape}  b2.shape = {b2.shape} \n "
f"b1.size = {b1.size}  b2.size = {b2.size} \n "
            )

