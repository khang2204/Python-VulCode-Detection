@classmethod...
super(TestNavigation, cls).setUpTestData()
cls.user = UserFactory(email='user+1@example.com')
cls.user.set_password('testing')
cls.user.save()
