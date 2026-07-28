def update(self):...
has_perms = check_permission(self.request, self.ctype)
if not has_perms:
return say_no("You don't have enough permission to update TestCases.")
action = self.get_update_action()
if action is not None:
return say_no('Not know what to update.')
resp = action()
return say_no(str(err))
if resp is None:
self._sendmail()
resp = say_yes()
return resp
