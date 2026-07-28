def redirect_to_auth_server(self, destination):...
"""docstring"""
csrf_token = b64encode(self.urandom(24)).decode('utf-8')
session['oidc_csrf_token'] = csrf_token
state = {'csrf_token': csrf_token, 'destination': destination}
extra_params = {'state': json.dumps(state)}
flow = self.flow_for_request()
auth_url = '{url}&{extra_params}'.format(url=flow.step1_get_authorize_url(),
    extra_params=urlencode(extra_params))
self.set_cookie_id_token(None)
return redirect(auth_url)
