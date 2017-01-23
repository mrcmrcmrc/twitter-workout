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

def getFriends(user, friendslist):
	next_cursor = -1
	while (next_cursor):
		get_friends = twitter.get_friends_ids(screen_name = user, count = 1000, cursor = next_cursor) #count max: 5000
		for friend in get_friends['ids']:
			friendslist.append(friend)
			next_cursor = get_friends['next_cursor']

def getCommonFriends(user1_friends, user2_friends):
	return list(set(user1_friends).intersection(user2_friends))

def getCommonFriendsInfo(common_friends_IDs):
	tempList = []
	infos = twitter.lookup_user(user_id = list(common_friends_IDs))
	for info in infos:
		 tempList.append(info['screen_name'])
	return tempList

user1 = ""
user2 = ""

user1_friends = []
user2_friends = []

getFriends(user1, user1_friends)
getFriends(user2, user2_friends)
common_friends_IDs = getCommonFriends(user1_friends, user2_friends)
common_friends = getCommonFriendsInfo(common_friends_IDs)

print "%s common friends" % len(common_friends)
for f in common_friends:
	print f
print "\ndone"
