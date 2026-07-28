def oauth_authentication(request):...
"""docstring"""
if not request.headers.get('Authorization'):
return None
if not utils.is_local_dev_server():
return api.extract_oauth_caller_identity()
header = request.headers['Authorization'].split(' ', 1)
if len(header) != 2 or header[0] not in ('OAuth', 'Bearer'):
base_url = 'https://www.googleapis.com/oauth2/v1/tokeninfo'
result = urlfetch.fetch(url='%s?%s' % (base_url, urllib.urlencode({
    'access_token': header[1]})), follow_redirects=False,
    validate_certificate=True)
if result.status_code != 200:
token_info = json.loads(result.content)
error = json.loads(result.content)['error_description']
error = repr(result.content)
if 'email' not in token_info:
if not token_info.get('verified_email'):
email = token_info['email']
return model.Identity(model.IDENTITY_USER, email)
