#!/usr/bin/python
# -*- coding: utf-8 -*-
from twython import TwythonStreamer
import sys

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = '191905517-'
ACCESS_SECRET = ''

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
        	if not 'RT' in data['text']:
    			print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()

reload(sys)
sys.setdefaultencoding('utf-8')
stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET,
                    ACCESS_KEY, ACCESS_SECRET)
stream.statuses.filter(track = 'turkey')
