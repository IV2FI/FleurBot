from config import getApi
import os
import time
print()

# Search : 180/15m // Tweet : 300/3H

api = getApi(os.environ['consumer_key'], os.environ['consumer_secret'], os.environ['access_token_key'], os.environ['access_token_secret'])
tweets = 0
searchs = 0
limitTweets = 100
limitSearchs = 80

def endsWith(sentence, keyword):
    return sentence.endswith(keyword)

def postStatus(update, inReplyTo, media):
    global tweets
    tweets += 1
    api.PostUpdate(update, media=media, in_reply_to_status_id=inReplyTo)

def search(research, howMany):
    global searchs
    searchs += 1
    searchResults = api.GetSearch(raw_query="q="+research+"&result_type=recent&count="+howMany)
    for search in searchResults:
        if(endsWith(search.text, "quoi") or endsWith(search.text, "quoi ?") or endsWith(search.text, "quoi !")):
            postStatus("@" + search.user.screen_name + " feur", search.id, "monkey.jpg")

def start():
    global searchs
    global tweets
    global limitTweets
    global limitSearchs
    while(True):
        search("quoi", "100")
        if(searchs >= limitSearchs):
            print("Limite atteinte des searchs")
            time.sleep(60*60*15)
            searchs = 0
        elif(tweets >= limitTweets):
            print("Limite atteinte des tweets")
            time.sleep(60*60*3)
            tweets = 0
        print(f"On a tweeté {str(tweets)} fois !")
        time.sleep(5)

start()