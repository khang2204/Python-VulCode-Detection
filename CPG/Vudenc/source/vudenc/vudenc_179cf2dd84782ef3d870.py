def log_in(self):...
response = flask.make_response()
result = self.authomatic.login(WerkzeugAdapter(request, response), 'google',
    session=session, session_saver=lambda : app.save_session(session,
    response), secure_cookie=True if request.is_secure else False)
if result:
if result.error:
return response
msg = 'Google auth failed with error: {0}'
if result.user:
logging.error(msg.format(result.error.message))
result.user.update()
return abort(403)
user = result.user
self.set_expiration()
self.set_current_user(email=user.email, first_name=user.first_name,
    last_name=user.last_name)
resp = self.redirect_to_index()
self.set_csrf_token(resp)
return resp
