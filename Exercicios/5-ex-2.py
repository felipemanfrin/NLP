import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# sid = SentimentIntensityAnalyzer()
review = 'this film was so long, but i general it was a funny movie. Some parts of the movie was a kind of boring but even in this parts the actor was preary good acting'
# print(sid.polarity_scores(review))

def review_rating(string):
    sid = SentimentIntensityAnalyzer()
    review = string
    print(sid.polarity_scores(review))

review_rating(review)