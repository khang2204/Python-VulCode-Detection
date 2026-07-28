def test_logout_loggedin(self):...
eppn = 'hubba-bubba'
came_from = '/afterlogin/'
cookie = self.login(eppn, came_from)
csrft = 'csrf token'
session['_csrft_'] = csrft
response2 = self.app.dispatch_request()
self.assertEqual(response2.status, '200 OK')
self.assertIn(
    'https://idp.example.com/simplesaml/saml2/idp/SingleLogoutService.php',
    json.loads(response2.data)['payload']['location'])
