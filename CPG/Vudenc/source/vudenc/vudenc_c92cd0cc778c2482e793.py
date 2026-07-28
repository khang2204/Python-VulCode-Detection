def test_logout_service_startingSP_already_logout(self):...
came_from = '/afterlogin/'
session_id = self.add_outstanding_query(came_from)
response = self.app.dispatch_request()
self.assertEqual(response.status, '302 FOUND')
self.assertIn('testing-relay-state', response.location)
