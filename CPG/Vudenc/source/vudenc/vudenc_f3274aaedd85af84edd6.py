def test_laod_session_cookie_and_no_session(self):...
s = models.Session.create()
old_sid = s.session_id
s_serialized = s.serialize()
s.key.delete()
s_count = models.Session.query().count()
self.assertTrue(s_count == 0)
req = EngineAuthRequest.blank('/auth/google')
req.cookies['_eauth'] = s_serialized
req._load_session()
self.assertTrue(req.session.session_id != old_sid)
s_count2 = models.Session.query().count()
self.assertTrue(s_count2 == 1)
