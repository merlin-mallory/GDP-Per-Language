import pandas as pd
import os
cwd = os.getcwd()

df = pd.read_csv("data/titanic.csv")
print(df.dtypes)