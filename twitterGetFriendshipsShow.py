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

source = ""
target = ""

try:
	get_friendships = twitter.show_friendship(source_screen_name = source, target_screen_name = target)
except TwythonRateLimitError as e:
	print e

print "%s is following %s: %s" % (source, target, get_friendships['relationship']['source']['following'])
print "%s is following %s: %s" % (target, source, get_friendships['relationship']['source']['followed_by'])
print "%s can dm to %s: %s" % (source, target, get_friendships['relationship']['source']['can_dm'])

print "done"

