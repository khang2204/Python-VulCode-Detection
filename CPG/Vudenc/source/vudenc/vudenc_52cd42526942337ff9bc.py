def get(self, request):...
"""docstring"""
state = get_random_string(import_from_settings('OIDC_STATE_SIZE', 32))
redirect_field_name = import_from_settings('OIDC_REDIRECT_FIELD_NAME', 'next')
params = {'response_type': 'code', 'scope': 'openid', 'client_id': self.
    OIDC_RP_CLIENT_ID, 'redirect_uri': absolutify(request, reverse(
    'oidc_authentication_callback')), 'state': state}
if import_from_settings('OIDC_USE_NONCE', True):
nonce = get_random_string(import_from_settings('OIDC_NONCE_SIZE', 32))
request.session['oidc_state'] = state
params.update({'nonce': nonce})
request.session['oidc_login_next'] = request.GET.get(redirect_field_name)
request.session['oidc_nonce'] = nonce
query = urlencode(params)
redirect_url = '{url}?{query}'.format(url=self.OIDC_OP_AUTH_ENDPOINT, query
    =query)
return HttpResponseRedirect(redirect_url)
