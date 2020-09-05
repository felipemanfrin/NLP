import pandas as pd
import numpy as np

df = pd.read_csv('../UPDATED_NLP_COURSE/TextFiles/moviereviews2.tsv', sep='\t')
print(df.isnull().sum())

blanks = []
for i, lb, rv in df.itertuples():
    if type(rv) == str:
      if rv.isspace():
          blanks.append(i)
print(len(blanks))


#no resultado review temos 20 valores missing