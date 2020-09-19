from tweepy import OAuthHandler
from tweepy import API
import flask
import random
import os

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
    
    foodlist=['pork chop','cookie','pizza','curry', 'steak','jumbo shrimp','spaghetti'] #list
    random.seed() #initialize rng
    cfood=foodlist[random.randint(0,6)] #use random to choose a food

    tweets=twitter_api.search(cfood, count=50)
    tweetlist=[]
    for tweet in tweets:
        tweetlist.append([tweet.user.screen_name, str(tweet.created_at), tweet.text])
    select_tweets=[]
    while len(select_tweets)<5:
        chosen=random.randint(0,len(tweetlist))
        if chosen not in select_tweets:
            select_tweets.append(chosen)
    
    return flask.render_template(
        "app.html", 
        food=cfood,
        #export all of the different parts of the 5 tweets
	    tweet1=tweetlist[select_tweets[0]],
	    tweet2=tweetlist[select_tweets[1]],
	    tweet3=tweetlist[select_tweets[2]],
	    tweet4=tweetlist[select_tweets[3]],
	    tweet5=tweetlist[select_tweets[4]]
         
        )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)
