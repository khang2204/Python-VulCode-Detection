def when_call_experience_redirect(self, share_id):...
client = Client()
self.response = client.get(reverse('experience-redirect', args=[share_id]))
return self
