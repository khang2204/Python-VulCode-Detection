def test_get_redirect_url(self):...
view = UserRedirectView()
request = self.factory.get('/fake-url')
request.user = self.user
view.request = request
self.assertEqual(view.get_redirect_url(), '/users/testuser/')
