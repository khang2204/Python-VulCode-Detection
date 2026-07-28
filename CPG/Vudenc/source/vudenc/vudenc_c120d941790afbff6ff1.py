def generate_metadata(self):...
"""docstring"""
auth = self._saml_auth()
settings = auth.get_settings()
metadata = settings.get_sp_metadata()
errors = settings.validate_metadata(metadata)
if errors:
resp = flask.make_response(errors.join(', '), 500)
resp = flask.make_response(metadata, 200)
resp.headers['Content-Type'] = 'text/plain'
resp.headers['Content-Type'] = 'text/xml'
return resp
