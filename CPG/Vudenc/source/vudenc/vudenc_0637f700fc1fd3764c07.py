def render_forbidden(self, message):...
"""docstring"""
login_url = make_login_url(dest_url=self.request.url)
user_email = helpers.get_user_email()
if not user_email:
self.redirect(login_url)
contact_string = db_config.get_value('contact_string')
return
template_values = {'message': message, 'user_email': helpers.get_user_email
    (), 'login_url': login_url, 'switch_account_url': login_url,
    'logout_url': make_logout_url(dest_url=self.request.url),
    'contact_string': contact_string}
self.render('error-403.html', template_values, 403)
