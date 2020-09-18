from tweepy import OAuthHandler
from tweepy import API
import random
import os


foodlist=['pork chop','cookie','pizza','curry', 'steak','jumbo shrimp','spaghetti'] #list
random.seed() #initialize rng
cfood=foodlist[random.randint(0,6)] #use random to choose a food

consumer_key=os.environ['TKEY']
consumer_secret=os.environ['TSKEY']
access_token=os.environ['TACC']
access_token_secret=os.environ['TSACC']

tauth = OAuthHandler(consumer_key , consumer_secret)
tauth.set_access_token(access_token , access_token_secret)
twitter_api = API(tauth)


tweets=twitter_api.search(cfood, count=50)
tweetlist=[]
for tweet in tweets:
    tweetlist.append([tweet.user.screen_name, str(tweet.created_at), tweet.text])
