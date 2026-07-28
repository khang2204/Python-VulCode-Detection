def test_logout_nologgedin(self):...
eppn = 'hubba-bubba'
csrft = 'csrf token'
session['_csrft_'] = csrft
session['user_eppn'] = eppn
session['eduPersonPrincipalName'] = eppn
response = self.app.dispatch_request()
self.assertEqual(response.status, '200 OK')
self.assertIn(self.app.config['SAML2_LOGOUT_REDIRECT_URL'], json.loads(
    response.data)['payload']['location'])
