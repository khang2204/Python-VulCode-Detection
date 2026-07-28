def after_request(self, response):...
"""docstring"""
if getattr(g, 'oidc_id_token_dirty', False):
signed_id_token = self.cookie_serializer.dumps(g.oidc_id_token)
return response
response.set_cookie(self.app.config['OIDC_ID_TOKEN_COOKIE_NAME'],
    signed_id_token, secure=self.app.config['OIDC_ID_TOKEN_COOKIE_SECURE'],
    httponly=True, max_age=self.app.config['OIDC_ID_TOKEN_COOKIE_TTL'])
