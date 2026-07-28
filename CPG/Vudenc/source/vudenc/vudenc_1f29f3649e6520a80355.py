def log_in(self):...
"""docstring"""
self_page = request.script_root + request.path
return flask.redirect(self.login_redirect_url(return_to=self_page))
