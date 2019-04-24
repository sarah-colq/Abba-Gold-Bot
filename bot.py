from keys import consumer_key, consumer_secret, access_token, access_token_secret
import tweepy


def get_lyrics():
    lyrics = 'Waterloo I was defeated, you won the war'
    return lyrics

def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    search = 'abba'

    search = "Keyword"
    numberOfTweets = 20
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            if tweet.user.name != 'abbashitpost':
                tweet.favorite()
        except tweepy.TweepError as e:
            continue
        except StopIteration:
            break

    lyrics = get_lyrics()
    api.update_status(lyrics)

if __name__== "__main__":
    main()


