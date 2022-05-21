import pandas as pd


data = {
  "name": ["a1", "a2", "a3"],
  "age": [50, 60, 70]
}

df = pd.DataFrame(data, index = ["c1", "c2", "c3"])

print(df)