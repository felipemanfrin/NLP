import pandas as pd

npr = pd.read_csv('..\Aulas/05-Topic-Modeling/quora_questions.csv')
print(npr.head())
print('-----------------------------------------------------')

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')
print(tfidf)
print('-----------------------------------------------------')

from sklearn.decomposition import NMF
dtm = tfidf.fit_transform(npr['Question'])
nmf_model = NMF(n_components=20, random_state=42)
nmf_model.fit(dtm)
print(nmf_model)
print('-----------------------------------------------------')

for index, question in enumerate(nmf_model.components_):
    print(f'The top 20 word for questions #{index}')
    print([tfidf.get_feature_names()[i] for i in question.argsort()[-15:]])

