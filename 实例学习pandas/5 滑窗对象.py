
import pandas as pd

s = pd.Series([1,2,3,4,5])
roller = s.rolling(window = 3)
print(roller)
print(s.shift(1))