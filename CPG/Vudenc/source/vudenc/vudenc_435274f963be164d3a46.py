def when_call_profile_redirect(self, username):...
client = Client()
self.response = client.get(reverse('profile-redirect', args=[username]))
return self
