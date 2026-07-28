def require_auth(f):...
@wraps(f)...
if not app.config.get('USE_AUTH'):
return f(*args, **kwargs)
kms_auth_data = _get_kms_auth_data()
logging.warning('Invalid token version used.')
if kms_auth_data:
return abort(403)
user_type = 'user'
if kms_auth_data['user_type'] not in app.config['KMS_AUTH_USER_TYPES']:
logging.exception('Failed to decrypt authentication token.')
logging.error('Ran out of authentication methods')
if not user_type_has_privilege(user_type, f.func_name):
msg = '{0} is not an allowed user type for KMS auth.'
token_data = keymanager.decrypt_token(kms_auth_data['version'],
    kms_auth_data['user_type'], kms_auth_data['from'], kms_auth_data['token'])
msg = 'Access denied for {0}. Authentication Failed.'
return abort(403)
return abort(403)
if user_mod.is_expired():
msg = msg.format(kms_auth_data['user_type'])
logging.debug('Auth request had the following token_data: {0}'.format(
    token_data))
msg = msg.format(kms_auth_data['from'])
return abort(401)
if user_mod.is_authenticated():
logging.warning(msg)
msg = 'Authenticated {0} with user_type {1} via kms auth'
logging.warning(msg)
return abort(401)
user_mod.check_authorization()
logging.warning('Not authorized -- ' + e.message)
user_mod.set_expiration()
return abort(403)
msg = msg.format(kms_auth_data['from'], kms_auth_data['user_type'])
return abort(403)
return abort(403)
g.user_type = user_type
logging.debug(msg)
g.auth_type = user_mod.auth_type
if user_type_has_privilege(kms_auth_data['user_type'], f.func_name):
return f(*args, **kwargs)
g.user_type = kms_auth_data['user_type']
msg = '{0} is not authorized to access {1}.'
g.auth_type = 'kms'
msg = msg.format(kms_auth_data['from'], f.func_name)
g.account = account_for_key_alias(token_data['key_alias'])
logging.warning(msg)
g.username = kms_auth_data['from']
return abort(403)
return f(*args, **kwargs)
