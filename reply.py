import praw
reddit = praw.Reddit("Geophrei")
subreddit = r.subreddit("traandroid")
for submission in subreddit.hot(limit=5):
    print (submission)