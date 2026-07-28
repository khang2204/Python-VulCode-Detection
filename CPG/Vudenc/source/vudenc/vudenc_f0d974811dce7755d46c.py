def test_applicable(self):...
request = webapp2.Request({'HTTP_X_APPENGINE_INBOUND_APPID': 'some-app'})
self.assertEqual(model.Identity(model.IDENTITY_SERVICE, 'some-app'),
    handler.service_to_service_authentication(request))
