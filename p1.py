from tweepy import OAuthHandler
from tweepy import API
from jinja2 import Template
from spoon import spoon_output
import flask
import random
import string
import os
import json

#Twitter api validation pre flasking
consumer_key=os.environ['TKEY']
consumer_secret=os.environ['TSKEY']
access_token=os.environ['TACC']
access_token_secret=os.environ['TSACC']
tauth = OAuthHandler(consumer_key , consumer_secret)
tauth.set_access_token(access_token , access_token_secret)
twitter_api = API(tauth)

#The creaton of the webpage
app = flask.Flask(__name__)
@app.route('/')  # we’ll use the default page
def index(): 
    
    output=spoon_output() #list gotten from spoon
    cfood=output[0]
    ingred=output[5]
    
    
    tweets=twitter_api.search(cfood.split()[ len( cfood.split() ) - 1 ], count=10)
    tweetlist=[]
    for tweet in tweets:
        tweetlist.append([tweet.user.screen_name, str(tweet.created_at), tweet.text, tweet.user.profile_image_url])
    random.seed() #initialize rng
    select_tweets=[]
    if len(tweetlist)>0:
        while len(select_tweets)<len(tweetlist):
            chosen=random.randint(0,len(tweetlist)-1)
            if tweetlist[chosen] not in select_tweets:
                select_tweets.append(tweetlist[chosen])
    tweets=json.dumps(select_tweets)
    
    return flask.render_template(
        "app.html.jninja", 
        food=cfood,
        fsource=output[1],
        fimg=output[2],
        fpreptime=output[3],
        fserv=output[4],
        fing=ingred,
        ilen=len(ingred),
        #export all of the different parts of the 5 tweets
        tweets=tweets
        )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
)
