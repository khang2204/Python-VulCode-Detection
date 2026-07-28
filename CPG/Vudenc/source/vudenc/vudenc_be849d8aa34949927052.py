def run(self, param):...
meetup = VMeetup.run(self, param)
if meetup and not (c.user_is_loggedin and meetup.can_edit(c.user, c.
abort(403, 'forbidden')
return meetup
