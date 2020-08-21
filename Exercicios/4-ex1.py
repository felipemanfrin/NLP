import pandas as pd
import numpy as np

df = pd.read_csv('../UPDATED_NLP_COURSE/TextFiles/moviereviews2.tsv', sep='\t')#aqui estou importando e carregando o dataset no dataframe do pandas
print(df.head())