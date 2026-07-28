def _render_saml_errors_json(self, auth):...
"""docstring"""
logging.warn('Handling SAML errors')
data = {'message': 'SAML request failed', 'errors': auth.get_errors(),
    'reason': auth.get_last_error_reason(), 'request_id': auth.
    get_last_request_id()}
logging.warn('Errors: {0}'.format(data))
resp = jsonify(**data)
resp.status_code = 500
return resp
