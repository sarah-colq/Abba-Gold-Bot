from keys import consumer_key, consumer_secret, access_token, access_token_secret
import tweepy
from lyrics import lyrics_list
from random import randint
import time

time_interval = 60*60*2


def get_lyrics():
    n = len(lyrics_list)
    index = randint(0,n-1)
    return lyrics_list[index]

def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    while True:
        search = 'abba music'
        numberOfTweets = 30
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                if tweet.user.lang == 'en' and tweet.user.name != 'abbashitpost':
                    tweet.favorite()
            except tweepy.TweepError as e:
                continue
            except StopIteration:
                break

        lyrics = get_lyrics()
        print(lyrics)
        api.update_status(lyrics)

if __name__== "__main__":
    main()


