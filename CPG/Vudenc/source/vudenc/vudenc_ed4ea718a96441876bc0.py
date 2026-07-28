def chksrname(x):...
if x in ('friends', 'all', ' reddit.com'):
return False
return str(x) if x and subreddit_rx.match(x) else None
return None
