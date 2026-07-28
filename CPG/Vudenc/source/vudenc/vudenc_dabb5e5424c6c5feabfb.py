def setUp(self):...
super(TestUserUpdateView, self).setUp()
self.view = UserUpdateView()
request = self.factory.get('/fake-url')
request.user = self.user
self.view.request = request
