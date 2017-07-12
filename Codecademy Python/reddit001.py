# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 18:53:29 2014

author: Eric Cotner

This program posts a comment in a thread every minute counting the number
of minutes that have passed
"""

import praw         # initializes Reddit API wrapper
import time         # initializes time utilites

r = praw.Reddit(user_agent = 'practicebot01 practicing posting comments')   # set user agent
r.login('practicebot01','Fusion1!')                                         # login as practicebot
submissions = r.get_submission(submission_id="29d7np")                      # get the test submission
x=0                                                                         # initialize the counting variable

while 1:
    submissions.add_comment(x)          # comment in thread
    x=x+1                               # increment minutes that have passed
    time.sleep(60)                      # wait 1 minute