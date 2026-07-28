def test_applicable(self):...
os.environ.update({'USER_EMAIL': 'joe@example.com', 'USER_ID': '123',
    'USER_IS_ADMIN': '0'})
self.assertEqual(model.Identity(model.IDENTITY_USER, 'joe@example.com'),
    handler.gae_cookie_authentication(webapp2.Request({})))
