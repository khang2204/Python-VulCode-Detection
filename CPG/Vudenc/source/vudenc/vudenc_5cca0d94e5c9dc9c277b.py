def test_urls_for_emails_with_pluses(self):...
self.client.login(username=self.user.username, password='testing')
response = self.client.get(reverse('iframe-navigation'))
self.assertContains(response, urlencode({'people': self.user.email}))
self.assertContains(response, urlencode({'author__email__startswith': self.
    user.email}))
