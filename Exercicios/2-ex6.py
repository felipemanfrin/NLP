import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')
matcher = Matcher(nlp.vocab)
pattern = [{'LOWER': 'swimming vigorously'}]
pattern2 = [{'LOWER': 'swimming'}, {'IS_SPACE': True}, {'LOWER': 'vigorously'}]
pattern3 = [{'LOWER': 'swimmingvigorously'}]
matcher.add('SwimmingVigorously', None, pattern, pattern2, pattern3)
with open('../UPDATED_NLP_COURSE/TextFiles/owlcreek.txt') as f:
    doc = nlp(f.read())
found_matches = matcher(doc)
print(found_matches)
