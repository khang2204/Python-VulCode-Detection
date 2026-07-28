from engineauth.middleware import AuthMiddleware
from engineauth.middleware import EngineAuthRequest
from engineauth import models
import test_base
import webapp2
__author__ = 'kyle.finley@gmail.com (Kyle Finley)'
app = AuthMiddleware(webapp2.WSGIApplication())
def setUp(self):...
super(TestAuthMiddleware, self).setUp()
def test_load_strategy(self):...
from engineauth.strategies.google import GoogleStrategy
strategy_class = app._load_strategy('google')
self.assertEqual(strategy_class, GoogleStrategy)
self.assertRaises(Exception, app._load_strategy, 'enron')
from engineauth.strategies.appengine_openid import AppEngineOpenIDStrategy
strategy_class = app._load_strategy('appengine_openid')
self.assertEqual(strategy_class, AppEngineOpenIDStrategy)
def test_load_session_no_session(self):...
req = EngineAuthRequest.blank('/auth/google')
s_count = models.Session.query().count()
self.assertTrue(s_count == 0)
sess = req._load_session()
s_count = models.Session.query().count()
self.assertTrue(s_count == 1)
def test_laod_session_session_id_no_user_id(self):...
s = models.Session.create()
s_count = models.Session.query().count()
self.assertTrue(s_count == 1)
req = EngineAuthRequest.blank('/auth/google')
req.cookies['_eauth'] = s.serialize()
req._load_session()
self.assertTrue(req.session.session_id == s.session_id)
s_count2 = models.Session.query().count()
self.assertTrue(s_count2 == 1)
def test_laod_session_session_id_and_user_id(self):...
s = models.Session.create()
s_count = models.Session.query().count()
self.assertTrue(s_count == 1)
req = EngineAuthRequest.blank('/auth/google')
req.cookies['_eauth'] = s.serialize()
req._load_session()
self.assertTrue(req.session.session_id == s.session_id)
s_count2 = models.Session.query().count()
self.assertTrue(s_count2 == 1)
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
def test__load_user(self):...
user = models.User.create_user('test:12345')
req = EngineAuthRequest.blank('/auth/google')
req._load_session()
req.session.user_id = user.get_id()
req._load_user()
self.assertEqual(user, req.user)
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
def test_add_message(self):...
req = EngineAuthRequest.blank('/auth/google')
req._load_session()
msgs = req.get_messages()
self.assertEquals(msgs, None)
req.add_message('TEST MESSAGE')
msgs = req.get_messages()
self.assertEquals(msgs, [{'level': None, 'message': 'TEST MESSAGE'}])
msgs = req.get_messages()
self.assertEquals(msgs, None)
req.add_message('TEST1', 'error')
req.add_message('TEST2', 'success')
msgs = req.get_messages()
self.assertEquals(msgs, [{'level': 'error', 'message': 'TEST1'}, {'level':
    'success', 'message': 'TEST2'}])
msgs = req.get_messages()
self.assertEquals(msgs, None)
req.add_message('TEST1', 'error')
req.add_message('TEST2', 'success', '_mykey')
msgs = req.get_messages()
self.assertEquals(msgs, [{'level': 'error', 'message': 'TEST1'}])
msgs_key = req.get_messages('_mykey')
self.assertEquals(msgs_key, [{'level': 'success', 'message': 'TEST2'}])
msgs = req.get_messages()
self.assertEquals(msgs, None)
msgs_key = req.get_messages()
self.assertEquals(msgs_key, None)
def test_set_redirect_uri(self):...
req = EngineAuthRequest.blank('/auth/google')
req._load_session()
req.set_redirect_uri()
req._config = {'success_uri': '/callback'}
redirect_uri = req.get_redirect_uri()
self.assertEqual(redirect_uri, '/callback')
req = EngineAuthRequest.blank('/auth/google?next=/newcallback')
req._load_session()
req.set_redirect_uri()
req._config = {'success_uri': '/callback'}
redirect_uri = req.get_redirect_uri()
self.assertEqual(redirect_uri, '/newcallback')
req = EngineAuthRequest.blank('/auth/google?next=/newcallback&a=121&123=a')
req._load_session()
req.set_redirect_uri()
req._config = {'success_uri': '/callback'}
redirect_uri = req.get_redirect_uri()
self.assertEqual(redirect_uri, '/newcallback')
