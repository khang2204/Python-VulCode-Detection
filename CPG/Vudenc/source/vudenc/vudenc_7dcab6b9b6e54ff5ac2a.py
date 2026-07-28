def init_user_auth_class(*args, **kwargs):...
if not app.config['USE_AUTH']:
module = NullUserAuthenticator
module_name = app.config['USER_AUTH_MODULE'].lower()
logging.info('Initializing {} user authenticator'.format(module.auth_type))
if module_name == 'google':
return module(*args, **kwargs)
module = GoogleOauthAuthenticator
if module_name == 'saml':
module = SamlAuthenticator
if module_name == 'null':
module = NullUserAuthenticator
