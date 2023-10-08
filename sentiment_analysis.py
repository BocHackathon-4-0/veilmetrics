'''
 Three well known libraries for sentiment analysis that are easy to implement
'''

from flair.models import TextClassifier
from flair.data import Sentence
import nltk
#nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer  # VADER
from textblob import TextBlob
from scipy.interpolate import interp1d

class SentimentAnalyzers:

    def __init__(self):
        self.vader = SentimentIntensityAnalyzer()
        self.fl = TextClassifier.load('en-sentiment')
        self.m = interp1d([-1, 1], [0, 100])

        print(">>> Initialized Sentiment Analyzer")

    def vader_score(self, text):
        vader_sentiment = self.vader.polarity_scores(text)['compound']
        return float(self.m(vader_sentiment))

    def tb_score(self, text):
        textblob_sentiment = TextBlob(text).sentiment.polarity
        return float(self.m(textblob_sentiment))

    def flair_score(self, text):
        if len(text) > 0:
            sentence = Sentence(text)
            self.fl.predict(sentence)

            if "POSITIVE" in sentence.labels[0].value:
                fl_sentiment = sentence.labels[0].score
            else:
                fl_sentiment = -sentence.labels[0].score
            return float(self.m(fl_sentiment))
        else:
            print(">>> Empty string kati paei lathos?")
            return 0