#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "842680395447619584-MV3rx4akb7c3kaPjg6wVVTHb3hMphZu"
access_token_secret = "Wvf2s2Wkffgilwf2RI2tgKp9ggHlwFtjh39MywTZ6BBEG"
consumer_key = "TJZ4xwLn9sNOWuv53hs8oyj0W"
consumer_secret = "m2sZmyR82gK2AjTvypS4lZNVCvf2bC8PENSsYT0bUlvNwsZMRN"
class listeners(StreamListener):

    def on_data(self, data):
        tweet=data.split(',"text":"')[1].split('","source')[0]
        save=tweet.decode('utf8')
        output=open('output.csv','a')
        output.write(save)
        output.close()
        return True

    def on_error(self,status):
        print status


l = listeners()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=['car'],languages=['en'])
