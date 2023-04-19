import pandas as pd
pop = pd.read_csv('.\state-population.csv')
areas = pd.read_csv('.\state-areas.csv')
abbrevs = pd.read_csv('.\state-abbrevs.csv')
print(pop.head())
print(areas.head())
print(abbrevs.head())

merged = pd.merge(pop, abbrevs, how='outer', left_on='state/region', right_on='abbreviation')
print(merged.head(3))
merged = merged.drop('abbreviation', 1) # 丢弃重复信息
merged.head()

print("merged.isnull().any()",merged.isnull().any())
print(merged[merged['population'].isnull()].head())