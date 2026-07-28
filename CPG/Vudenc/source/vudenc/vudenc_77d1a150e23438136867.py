def update_config(self, config):...
"""docstring"""
saml_config = os.path.join(HERE, 'saml2_settings.py')
config.update({'SAML2_LOGIN_REDIRECT_URL': '/', 'SAML2_LOGOUT_REDIRECT_URL':
    '/logged-out', 'SAML2_SETTINGS_MODULE': saml_config,
    'TOKEN_LOGIN_SHARED_KEY': 'shared_secret',
    'TOKEN_LOGIN_SUCCESS_REDIRECT_URL': 'http://test.localhost/success',
    'TOKEN_LOGIN_FAILURE_REDIRECT_URL': 'http://test.localhost/failure'})
return config
