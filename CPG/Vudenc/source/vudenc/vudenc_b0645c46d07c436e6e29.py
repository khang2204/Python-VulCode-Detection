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
