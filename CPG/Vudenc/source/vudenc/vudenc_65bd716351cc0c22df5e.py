def _get_creds_from(self, request):...
username = request.args['username'][0]
password = request.args['password'][0]
return credentials.UsernamePassword(username, password)
