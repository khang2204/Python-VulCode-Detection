def test__load_user_by_profile(self):...
auth_id = 'test:12345'
user_info = {'auth_id': auth_id, 'info': {}}
p = models.UserProfile.get_or_create(auth_id, user_info)
req = EngineAuthRequest.blank('/auth/google')
req._load_session()
req._load_user()
user_count = models.User.query().count()
self.assertEqual(user_count, 0)
req.load_user_by_profile(p)
user_count = models.User.query().count()
self.assertEqual(user_count, 1)
user = models.User.query().get()
self.assertTrue(p.key.id() in user.auth_ids)
req = EngineAuthRequest.blank('/auth/google')
req._load_session()
req._load_user()
req.load_user_by_profile(p)
user_count = models.User.query().count()
self.assertEqual(user_count, 1)
auth_id = 'test:abc'
user_info = {'auth_id': auth_id, 'info': {}}
p1 = models.UserProfile.get_or_create(auth_id, user_info)
req.load_user_by_profile(p1)
user_count = models.User.query().count()
self.assertEqual(user_count, 1)
