#!/usr/bin/python
# -*- coding: utf-8 -*-
from twython import Twython, TwythonError
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

userID = ""

myDict = {}
data = []
lastID = 0

user_timeline = twitter.get_user_timeline(id = userID, count = 1)

for tweets in user_timeline:
	lastID = tweets['id']

for i in range(0,2):
	try:
		user_timeline = twitter.get_user_timeline(id = userID, count = 160, max_id = lastID)
		#user_timeline = twitter.get_user_timeline(id = userID, count = 50, max_id = lastID, filter='media')
		
		for tweets in user_timeline:

			myDict['tweet'] = tweets['text']
			myDict['RT'] = tweets['retweet_count']
			myDict['FAV'] = tweets['favorite_count']
			myDict['time'] = tweets['created_at']
			
			data.append(myDict.copy())
			
			lastID = tweets['id']
	except TwythonError as e:
		print e

f = open('tweets.txt','w')

for tweets in data:
	f.write("%s \n" % tweets['tweet'])
	try:
		print "%s -- RT: %s -- FAV: %s -- time: %s" % (tweets['tweet'], tweets['RT'], tweets['FAV'], tweets['time'])
	except:
		pass

f.close()
print "done"







