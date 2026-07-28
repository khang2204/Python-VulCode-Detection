def test_load_session_no_session(self):...
req = EngineAuthRequest.blank('/auth/google')
s_count = models.Session.query().count()
self.assertTrue(s_count == 0)
sess = req._load_session()
s_count = models.Session.query().count()
self.assertTrue(s_count == 1)
