import twitter

def getApi(consumer_key, consumer_secret, access_token_key, access_token_secret):
    return twitter.Api(consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token_key=access_token_key,
                    access_token_secret=access_token_secret)