# Get ready to tweet.
from botOnesec import *
import tweepy

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

# Tweet the tweet!
api.update_status(tweet)
