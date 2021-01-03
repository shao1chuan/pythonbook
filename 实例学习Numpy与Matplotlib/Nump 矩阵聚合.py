import  numpy as np
a1 = np.array([i for i in range(1,5)])

a2 = a1.reshape((2,2))
print(f"a1 = {a1}   "
f"a2 = {a2}   "
      )

print(f"np.sum(a2) = {np.sum(a2)}\n"
      f"np.sum(a2,axis = 0) = {np.sum(a2,axis = 0)}\n"
f"np.std(a2) = {np.std(a2)}\n"
f"np.mean(a2) = {np.mean(a2)}\n"
f"np.var(a2) = {np.var(a2)}\n"
f"np.median(a2) = {np.median(a2)}\n"
f"np.random.shuffle(a2) = {a2}\n"
      )
np.random.shuffle(a2)
print(
f"np.random.shuffle(a2) = {a2}\n"
      )
np.sort(a2)
print(
f"np.random.sort(a2) = {a2}\n"
      )

X = np.random.randint(100, size=(4,4))
print(X)
np.sort(X, axis=0)
print(X)
np.sort(X, axis=1)
print(X)