# !/usr/bin/python
import time
import praw

reddit = praw.Reddit('Geophrei')

subreddit = reddit.subreddit("learnpython")

for submission in subreddit.hot(limit=5):
   print("Title: ", submission.title)
   print("Text: ", submission.selftext)
   print("Score: ", submission.score)
   print("---------------------------------\n")