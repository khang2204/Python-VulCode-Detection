def make_test_app(self, path, request_handler):...
"""docstring"""
return webtest.TestApp(webapp2.WSGIApplication([(path, request_handler)],
    debug=True), extra_environ={'REMOTE_ADDR': '127.0.0.1'})
