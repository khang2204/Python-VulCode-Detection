def __init__(self, *args, **kwargs):...
super(OIDCAuthenticationRequestView, self).__init__(*args, **kwargs)
self.OIDC_OP_AUTH_ENDPOINT = import_from_settings(
    'OIDC_OP_AUTHORIZATION_ENDPOINT')
self.OIDC_RP_CLIENT_ID = import_from_settings('OIDC_RP_CLIENT_ID')
