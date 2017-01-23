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

def getFollowers(user, followerslist):
	next_cursor = -1
	while (next_cursor):
		get_followers = twitter.get_followers_ids(screen_name = user, count = 5000, cursor = next_cursor) #count max: 5000
		for follower in get_followers['ids']:
			followerslist.append(follower)
			next_cursor = get_followers['next_cursor']

def getCommonFollowers(user1_followers, user2_followers):
	return list(set(user1_followers).intersection(user2_followers))

def getCommonFriendsInfo(common_followers_IDs):
	tempList = []
	infos = twitter.lookup_user(user_id = list(common_followers_IDs))
	for info in infos:
		 tempList.append(info['screen_name'])
	return tempList

user1 = ""
user2 = ""

user1_followers = []
user2_followers = []

getFollowers(user1, user1_followers)
getFollowers(user2, user2_followers)
common_followers_IDs = getCommonFollowers(user1_followers, user2_followers)
common_followers = getCommonFriendsInfo(common_followers_IDs)

print "%s common followers" % len(common_followers)
for f in common_followers:
	print f
print "\ndone"
