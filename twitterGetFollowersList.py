#!/usr/bin/python
# -*- coding: utf-8 -*-
from twython import Twython, TwythonRateLimitError
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

screen_name = ""
next_cursor = -1
followers = []

while (next_cursor):
	try:
		get_followers = twitter.get_followers_list(screen_name = screen_name, count = 200, cursor = next_cursor)
		for follower in get_followers['users']:
			followers.append(follower["screen_name"].encode("utf-8"))
			#followers.append(follower["name"].encode("utf-8"))
			next_cursor = get_followers['next_cursor']
	except TwythonRateLimitError as e:
		print e
		break

print "%s followers" % str(len(followers))
for f in followers:
	print f

print "done"