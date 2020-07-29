from config import getApi
import os
import sys
import time
print()

# Search : 180/15m // Tweet : 300/3H

api = getApi(os.environ['consumer_key'], os.environ['consumer_secret'], os.environ['access_token_key'], os.environ['access_token_secret'])
tweets = 0
searchs = 0
limitTweets = 300
limitSearchs = 180

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
    stop = False
    while(not stop):
        try:
            search("quoi", "100")
        except:
            print("Erreur (probablement de quota, on arrete)")
            stop = True
        if(searchs >= limitSearchs):
            print("Limite atteinte des searchs")
            stop = True
        elif(tweets >= limitTweets):
            print("Limite atteinte des tweets")
            stop = True
        print(f"On a tweeté {str(tweets)} fois !")
        time.sleep(5)
    print("Fini, on attend 3H maintenant et on reprend.")

start()