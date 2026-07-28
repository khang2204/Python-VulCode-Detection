def get(self, request):...
"""docstring"""
nonce = request.session.get('oidc_nonce')
if nonce:
if 'code' in request.GET and 'state' in request.GET:
kwargs = {'request': request, 'nonce': nonce}
return self.login_failure()
if 'oidc_state' not in request.session:
return self.login_failure()
if request.GET['state'] != request.session['oidc_state']:
msg = 'Session `oidc_state` does not match the OIDC callback state'
self.user = auth.authenticate(**kwargs)
if self.user and self.user.is_active:
return self.login_success()
