def update_config(self, config):...
"""docstring"""
saml_config = os.path.join(HERE, 'saml2_settings.py')
config.update({'TOKEN_SERVICE_URL': 'http://login', 'SAML2_SETTINGS_MODULE':
    saml_config})
return config
