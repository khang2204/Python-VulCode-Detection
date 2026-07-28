def test__load_user(self):...
user = models.User.create_user('test:12345')
req = EngineAuthRequest.blank('/auth/google')
req._load_session()
req.session.user_id = user.get_id()
req._load_user()
self.assertEqual(user, req.user)
