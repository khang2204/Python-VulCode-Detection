import tweepy
import secretConstants
import cgi
from getAlcohol import getAlcoholByName
from lastReplied import getLastReplied, setLastReplied
auth = tweepy.OAuthHandler(secretConstants.CONSUMER_KEY, secretConstants.
    CONSUMER_SECRET)
auth.set_access_token(secretConstants.ACCESS_TOKEN, secretConstants.
    ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
def formatReply(result):...
if result[2] == '':
reply = result[0] + ' is ' + result[1] + '.'
if result[0][2] != '' and result[2]:
return reply
reply = result[0] + ' brewed in ' + result[2] + ' is ' + result[1] + '.'
