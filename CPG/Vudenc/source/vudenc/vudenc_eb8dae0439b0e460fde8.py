def run(self, meetup_id36):...
if meetup_id36:
meetup_id = int(meetup_id36, 36)
if self.redirect:
return Meetup._byID(meetup_id, True)
abort(404, 'page not found')
return None
