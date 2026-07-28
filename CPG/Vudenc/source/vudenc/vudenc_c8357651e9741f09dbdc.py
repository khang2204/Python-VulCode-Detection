def run(self, fullname):...
if fullname:
parent = Thing._by_fullname(fullname, False, data=True)
abort(403, 'forbidden')
if isinstance(parent, Message):
return parent
sr = parent.subreddit_slow
if c.user_is_loggedin and sr.can_comment(c.user):
return parent
