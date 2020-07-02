# Spacy é uma biblioteca de NLP
# NLTK - Natural Language Toolkit (lançada em 2001, diferente da spacy que foi lançada em 2015)

import PyPDF2
import spacy
nlp = spacy.load('en_core_web_sm')

doc = nlp(u'Tesla is lookong at buying U.S startup for $6 million')
