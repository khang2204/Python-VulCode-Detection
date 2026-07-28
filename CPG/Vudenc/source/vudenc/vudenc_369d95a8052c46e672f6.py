def run(self, link_name):...
link = VLink.run(self, link_name)
if link and not (c.user_is_loggedin and link.can_submit(c.user)):
abort(403, 'forbidden')
return link
