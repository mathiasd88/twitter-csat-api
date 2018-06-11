import os

import tweepy
from textblob import TextBlob
from textblob.exceptions import TranslatorError


def analyze(country, text = None):
    consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
    consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')

    access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    places = api.geo_search(query=country, granularity='country')
    place_id = places[0].id

    tweets = api.search(q="place:%s" % place_id)
    polarity = 0
    tweets_array = []

    for tweet in tweets:
        analysis = TextBlob(tweet.text)

        try:
            translated_text = analysis.translate(from_lang='es', to='en')
            tweets_array.append(tweet.text)
            polarity += translated_text.sentiment.polarity
        except TranslatorError:
            pass

    return {
        'tweets': tweets_array,
        'polarity': polarity/len(tweets)
    }
