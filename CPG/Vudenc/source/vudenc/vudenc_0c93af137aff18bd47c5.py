def run(self):...
if not (c.default_sr or c.user_is_loggedin and c.site.can_submit(c.user)):
return False
return True
