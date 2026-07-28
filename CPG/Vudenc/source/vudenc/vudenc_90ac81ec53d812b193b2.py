def test_authorization_error(self):...
"""docstring"""
test = self
calls = []
@api.require(lambda : False)...
test.fail('Handler code should not be called')
def authorization_error(self, err):...
calls.append('authorization_error')
super(Handler, self).authorization_error(err)
app = self.make_test_app('/request', Handler)
response = app.get('/request', expect_errors=True)
self.assertEqual(['authorization_error'], calls)
self.assertEqual(403, response.status_int)
