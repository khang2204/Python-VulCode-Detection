def _saml_req_dict_from_request(self, flask_request=None):...
"""docstring"""
if flask_request is None:
flask_request = flask.request
url_data = urlparse.urlparse(flask_request.url)
if flask_request.scheme == 'https':
https = 'on'
if app.debug and app.config['SAML_FAKE_HTTPS']:
return {'https': https, 'http_host': flask_request.host, 'server_port':
    url_data.port, 'script_name': flask_request.path, 'get_data':
    flask_request.args.copy(), 'post_data': flask_request.form.copy()}
https = 'on'
https = 'off'
