def test_save_session(self):...
s = models.Session.create()
s_count = models.Session.query().count()
self.assertTrue(s_count == 1)
req = EngineAuthRequest.blank('/auth/google')
req.cookies['_eauth'] = s.serialize()
resp = req.get_response(app)
resp.request = req
resp._save_session()
self.assertTrue(resp.request.session.session_id == s.session_id)
s_count2 = models.Session.query().count()
self.assertTrue(s_count2 == 1)
resp.request.session.user_id = '1'
resp._save_session()
s_count = models.Session.query().count()
self.assertTrue(s_count == 1)
s1 = models.Session.query().get()
self.assertEqual(s1.key.id(), '1')
