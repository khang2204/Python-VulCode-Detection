def run(self, thing_name):...
if c.user_is_admin:
return True
if c.user_is_loggedin:
item = Thing._by_fullname(thing_name, data=True)
abort(403, 'forbidden')
subreddit = item.subreddit_slow
if subreddit.can_ban(c.user):
return True
