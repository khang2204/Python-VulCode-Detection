def post(self, request):...
"""docstring"""
logout_url = self.redirect_url
if is_authenticated(request.user):
logout_from_op = import_from_settings('OIDC_OP_LOGOUT_URL_METHOD', '')
return HttpResponseRedirect(logout_url)
if logout_from_op:
logout_url = import_string(logout_from_op)()
auth.logout(request)
