def login_success(self):...
auth.login(self.request, self.user)
expiration_interval = import_from_settings('OIDC_RENEW_ID_TOKEN_EXPIRY_SECONDS'
    , 60 * 15)
self.request.session['oidc_id_token_expiration'] = time.time(
    ) + expiration_interval
return HttpResponseRedirect(self.success_url)
