import spacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher

nlp = spacy.load('en_core_web_sm')
matcher = PhraseMatcher(nlp.vocab)
pattern = ['swimming vigorously']
phrase_patterns = [nlp(text) for text in pattern]
matcher.add('SwimmingVigorously', None, *phrase_patterns)
with open('../UPDATED_NLP_COURSE/TextFiles/owlcreek.txt') as f:
    doc = nlp(f.read())
found_matches = matcher(doc)
for match_id, start, end in found_matches:
    string_id = nlp.vocab[match_id]
    span = doc[start+10:end+10]
    print(match_id, string_id, start, end, span.text)