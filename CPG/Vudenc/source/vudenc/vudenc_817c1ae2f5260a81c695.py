def _get_kms_auth_data():...
data = {}
auth = request.authorization
headers = request.headers
if auth and auth.get('username'):
if not auth.get('password'):
if 'X-Auth-Token' in headers and 'X-Auth-From' in headers:
data['version'], data['user_type'], data['from'] = _parse_username(auth[
    'username'])
if not headers.get('X-Auth-Token'):
return data
data['token'] = auth['password']
data['version'], data['user_type'], data['from'] = _parse_username(headers[
    'X-Auth-From'])
data['token'] = headers['X-Auth-Token']
