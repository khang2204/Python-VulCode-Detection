def post(self):...
xsrf_tool = XsrfTool()
user = users.get_current_user()
if not (self.params.xsrf_token and xsrf_tool.verify_token(self.params.
self.error(403)
action = 'delete', str(self.params.id)
return False
self.redirect('/delete', id=self.params.id, signature=reveal.sign(action))
