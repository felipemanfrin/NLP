import pandas as pd
import numpy as np

df = pd.read_csv('../UPDATED_NLP_COURSE/TextFiles/moviereviews2.tsv', sep='\t')
print(df['label'].value_counts())
