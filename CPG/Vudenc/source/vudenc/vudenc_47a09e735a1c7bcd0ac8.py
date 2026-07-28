def authorization_error(self, error):...
"""docstring"""
ident = api.get_current_identity()
if ident.is_anonymous or ident.is_bot:
self.redirect(self.create_login_url(self.request.url))
if model.is_empty_group(model.ADMIN_GROUP):
return
self.redirect_to('bootstrap')
env = {'page_title': 'Access Denied', 'error': error}
return
self.reply('auth/access_denied.html', env=env, status=403)
