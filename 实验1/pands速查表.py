import pandas as pd
pop = pd.read_csv('.\state-population.csv')
areas = pd.read_csv('.\state-areas.csv')
abbrevs = pd.read_csv('.\state-abbrevs.csv')
# print(pop.head())
# print(areas.head())
# print(abbrevs.head())
df = pd.DataFrame(pop)
a1 = df[df.population > 1125763]
a2 = df.drop_duplicates()
a3 = df.nsmallest(2, 'population')
a4 = df.drop(columns=['population'])
a5 = df.query('population == 1117489')
a6 = df.iloc[10:20]
a7 = df.loc[df['population'] > 10,['population', 'ages']]
a8 = df.iat[1, 2]
a9 = df.at[4, 'population']
a10 =df['ages'].value_counts()
a11 = df.assign(Area=lambda df: df.population*2)
a12 = df.groupby(by="state/region")
print(a12.agg(min))

