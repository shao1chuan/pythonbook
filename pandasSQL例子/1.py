from sklearn.datasets import load_iris
import pandas as pd
from pandasql import sqldf
from pandasql import load_meat, load_births
import re

births = load_births()
meat = load_meat()
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)

print(sqldf("SELECT * FROM iris_df  where species = 'virginica'", locals()))
