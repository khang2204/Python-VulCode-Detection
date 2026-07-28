def run(self):...
if c.user_is_loggedin and c.user.safe_karma >= g.discussion_karma_to_post:
return True
abort(403, 'forbidden')
