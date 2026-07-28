def when_call_aasa(self):...
client = Client()
self.response = client.get(reverse('aasa'))
return self
