from keys import consumer_key, consumer_secret, access_token, access_token_secret
import tweepy
import time

def get_lyrics():
    lyrics = ''
    return lyrics

def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    time_interval = 60*60*2
    while True:
        lyrics = get_lyrics()
        api.update_status(lyrics)
        time.sleep(time_interval)

if __name__== "__main__":
    main()


