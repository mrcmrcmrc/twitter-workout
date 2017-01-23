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

screen_name = ''
next_cursor = -1
friends = []

while (next_cursor):
	try:
		get_friends = twitter.get_friends_list(screen_name = screen_name, count = 200, cursor = next_cursor)
		for friend in get_friends['users']:
			friends.append(friend["screen_name"].encode("utf-8"))
			#followers.append(friend["name"].encode("utf-8"))
			next_cursor = get_friends['next_cursor']
	except TwythonRateLimitError as e:
		print e
		break

print "%s friends" % str(len(friends))
for f in friends:
	print f

print "done"