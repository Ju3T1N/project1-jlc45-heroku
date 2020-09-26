from tweepy import OAuthHandler
from tweepy import API
from jinja2 import Template
from spoon import spoon_output
import flask
import random
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
    
    foodlist=['pork chop','cookie','pizza','curry', 'steak','spaghetti', 'shrimp'] #list
    random.seed() #initialize rng
    cfood=foodlist[random.randint(0,len(foodlist)-1)] #use random to choose a food
    print(cfood+'\n'+'\n')
    tweets=twitter_api.search(cfood, count=50)
    tweetlist=[]
    for tweet in tweets:
        tweetlist.append([tweet.user.screen_name, str(tweet.created_at), tweet.text, tweet.user.profile_image_url])
    select_tweets=[]
    while len(select_tweets)<10:
        chosen=random.randint(0,len(tweetlist)-1)
        if tweetlist[chosen] not in select_tweets:
            select_tweets.append(tweetlist[chosen])
        tweets=json.dumps(select_tweets)
    
    return flask.render_template(
        "app.html.jninja", 
        food=cfood,
        #export all of the different parts of the 5 tweets
        tweets=tweets
        )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)
