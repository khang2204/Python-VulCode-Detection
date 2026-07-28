def test_logout_service_startingIDP_no_subject_id(self):...
eppn = 'hubba-bubba'
came_from = '/afterlogin/'
session_id = self.add_outstanding_query(came_from)
cookie = self.dump_session_cookie(session_id)
saml_response = auth_response(session_id, eppn)
response = self.app.dispatch_request()
session.persist()
response = self.app.dispatch_request()
self.assertEqual(response.status, '302 FOUND')
self.assertIn('testing-relay-state', response.location)
