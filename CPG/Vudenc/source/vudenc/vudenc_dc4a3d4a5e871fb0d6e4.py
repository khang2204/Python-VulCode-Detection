def test_logout_service_startingIDP(self):...
eppn = 'hubba-bubba'
came_from = '/afterlogin/'
session_id = self.add_outstanding_query(came_from)
cookie = self.dump_session_cookie(session_id)
saml_response = auth_response(session_id, eppn)
response = self.app.dispatch_request()
response = self.app.dispatch_request()
self.assertEqual(response.status, '302 FOUND')
self.assertIn(
    'https://idp.example.com/simplesaml/saml2/idp/SingleLogoutService.php?SAMLResponse='
    , response.location)
