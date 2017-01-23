#!/usr/bin/python
# -*- coding: utf-8 -*-
from twython import Twython
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
	get_followers = twitter.get_followers_ids(id = screen_name, count = 5000, cursor = next_cursor) #count max: 5000
	for follower in get_followers['ids']:
		followers.append(follower)
		next_cursor = get_followers['next_cursor']

print "%s followers" % str(len(followers))
for f in followers:
	print f
print "done"