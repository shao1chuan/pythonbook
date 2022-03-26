
import pandas as pd

s = pd.Series([-1, 1.2345, 100, -50])

print(s.where(s<0, 100))