import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
df = pd.read_csv('../UPDATED_NLP_COURSE/TextFiles/moviereviews2.tsv', sep='\t')
X = df['review']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
