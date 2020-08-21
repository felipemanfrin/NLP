import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics

df = pd.read_csv('../UPDATED_NLP_COURSE/TextFiles/moviereviews2.tsv', sep='\t')
X = df['review']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
clf_text = Pipeline([('tfidf', TfidfVectorizer()), ('clf', LinearSVC())])
clf_text.fit(X_train, y_train)
prediction = clf_text.predict(X_test)
print(metrics.confusion_matrix(y_test, prediction))

